from __future__ import annotations

import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, time, timedelta, timezone
from pathlib import Path
from typing import Any

JST = timezone(timedelta(hours=9), "JST")
UTC = timezone.utc
ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT_DIR / "config" / "cve-digest.json"
HISTORY_PATH = ROOT_DIR / "data" / "history.json"
OUTPUT_ROOT = ROOT_DIR / "docs"
USER_AGENT = "cve-digest/1.0"


@dataclass(frozen=True)
class Vulnerability:
    cve_id: str
    title: str
    description: str
    source: str
    published_at: str | None
    updated_at: str | None
    cvss: float | None
    severity: str
    kev: bool
    affected_products: list[str]
    matched_keywords: list[str]
    references: list[str]
    score: int
    priority_group: str
    category: str
    ai_summary: str | None = None


def load_json(path: Path, default: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2, sort_keys=True)
        file.write("\n")


def fetch_json(url: str, params: dict[str, str] | None = None, timeout: int = 45) -> dict[str, Any]:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def today_range_utc(now: datetime) -> tuple[datetime, datetime]:
    today = now.astimezone(JST).date()
    start_jst = datetime.combine(today, time.min, tzinfo=JST)
    end_jst = start_jst + timedelta(days=1)
    return start_jst.astimezone(UTC), end_jst.astimezone(UTC)


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed


def is_today_jst(value: str | None, now: datetime) -> bool:
    parsed = parse_datetime(value)
    if parsed is None:
        return False
    return parsed.astimezone(JST).date() == now.astimezone(JST).date()


def is_today_date(value: str | None, now: datetime) -> bool:
    if not value:
        return False
    try:
        return datetime.strptime(value, "%Y-%m-%d").date() == now.astimezone(JST).date()
    except ValueError:
        return False


def format_date(value: str | None) -> str | None:
    parsed = parse_datetime(value)
    if parsed is None:
        return value
    return parsed.astimezone(JST).strftime("%Y-%m-%d %H:%M:%S JST")


def compact_text(value: str | None, max_length: int = 700) -> str:
    if not value:
        return "-"
    text = " ".join(str(value).split())
    return text[:max_length].rstrip() + "..." if len(text) > max_length else text


def severity_from_cvss(score: float | None) -> str:
    if score is None:
        return "UNKNOWN"
    if score >= 9.0:
        return "CRITICAL"
    if score >= 7.0:
        return "HIGH"
    if score >= 4.0:
        return "MEDIUM"
    return "LOW"


def extract_cvss_and_severity(cve: dict[str, Any]) -> tuple[float | None, str]:
    metrics = cve.get("metrics", {})
    if not isinstance(metrics, dict):
        return None, "UNKNOWN"
    best_score: float | None = None
    best_severity = "UNKNOWN"
    for key in ["cvssMetricV40", "cvssMetricV31", "cvssMetricV30", "cvssMetricV2"]:
        values = metrics.get(key) or []
        if not isinstance(values, list):
            continue
        for item in values:
            if not isinstance(item, dict):
                continue
            cvss_data = item.get("cvssData", {})
            if not isinstance(cvss_data, dict):
                continue
            try:
                score = float(cvss_data.get("baseScore"))
            except (TypeError, ValueError):
                continue
            severity = item.get("baseSeverity") or cvss_data.get("baseSeverity") or severity_from_cvss(score)
            if best_score is None or score > best_score:
                best_score = score
                best_severity = str(severity).upper()
    return best_score, best_severity


def extract_affected_products(cve: dict[str, Any]) -> list[str]:
    products: set[str] = set()
    configurations = cve.get("configurations", [])
    if not isinstance(configurations, list):
        return []

    def walk_node(node: dict[str, Any]) -> None:
        for match in node.get("cpeMatch", []) or []:
            if not isinstance(match, dict):
                continue
            parts = str(match.get("criteria", "")).split(":")
            if len(parts) >= 5:
                vendor = parts[3].replace("_", " ")
                product = parts[4].replace("_", " ")
                if product and product != "*":
                    products.add(f"{vendor} {product}".strip())
        for child in node.get("nodes", []) or []:
            if isinstance(child, dict):
                walk_node(child)

    for config in configurations:
        if not isinstance(config, dict):
            continue
        for node in config.get("nodes", []) or []:
            if isinstance(node, dict):
                walk_node(node)
    return sorted(products)[:10]


def extract_references(cve: dict[str, Any]) -> list[str]:
    raw_references = cve.get("references", [])
    if isinstance(raw_references, dict):
        refs = raw_references.get("referenceData", [])
    elif isinstance(raw_references, list):
        refs = raw_references
    else:
        refs = []
    if not isinstance(refs, list):
        return []
    urls: list[str] = []
    for ref in refs:
        if isinstance(ref, dict) and ref.get("url"):
            urls.append(str(ref["url"]))
    return urls[:5]


def match_keywords(text: str, keywords: list[str], exclude_keywords: list[str]) -> tuple[bool, list[str], bool]:
    lower_text = text.lower()
    excluded = any(keyword.lower() in lower_text for keyword in exclude_keywords)
    if excluded:
        return False, [], True
    matched = [keyword for keyword in keywords if keyword.lower() in lower_text]
    return bool(matched), list(dict.fromkeys(matched)), False


def category_matches(search_text: str, config: dict[str, Any], category: str) -> list[str]:
    keywords = [str(item) for item in config.get(f"{category}_keywords", [])]
    _, matched, _ = match_keywords(search_text, keywords, [])
    return matched


def classify_category(search_text: str, config: dict[str, Any]) -> tuple[str, list[str]]:
    frontend_matches = category_matches(search_text, config, "frontend")
    backend_matches = category_matches(search_text, config, "backend")
    if frontend_matches:
        return "frontend", frontend_matches
    if backend_matches:
        return "backend", backend_matches
    return "security", []


def calculate_score(cvss: float | None, kev: bool, matched_keywords: list[str], description: str, category: str) -> int:
    score = 1000 if category == "frontend" else 900 if category == "backend" else 0
    score += 100 if kev else 0
    if cvss is not None:
        if cvss >= 9.0:
            score += 50
        elif cvss >= 7.0:
            score += 30
        elif cvss >= 4.0:
            score += 10
    score += len(matched_keywords) * 10
    lower_description = description.lower()
    risky_words = ["remote code execution", "rce", "authentication bypass", "privilege escalation", "xss", "prototype pollution", "csrf", "ssrf"]
    for word in risky_words:
        if word in lower_description:
            score += 15
    return score


def fetch_nvd_today(config: dict[str, Any], now: datetime) -> list[dict[str, Any]]:
    source = config.get("sources", {}).get("nvd", {})
    if not source.get("enabled", True):
        return []
    start, end = today_range_utc(now)
    data = fetch_json(
        str(source.get("url")),
        {
            "pubStartDate": start.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "pubEndDate": end.strftime("%Y-%m-%dT%H:%M:%S.000Z"),
            "resultsPerPage": "200",
        },
    )
    vulnerabilities = data.get("vulnerabilities", [])
    return vulnerabilities if isinstance(vulnerabilities, list) else []


def fetch_cisa_kev(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    source = config.get("sources", {}).get("cisa_kev", {})
    if not source.get("enabled", True):
        return {}
    data = fetch_json(str(source.get("url")))
    vulnerabilities = data.get("vulnerabilities", [])
    result: dict[str, dict[str, Any]] = {}
    if isinstance(vulnerabilities, list):
        for item in vulnerabilities:
            cve_id = item.get("cveID") if isinstance(item, dict) else None
            if cve_id:
                result[str(cve_id)] = item
    return result


def make_vulnerability(
    cve_id: str,
    title: str,
    description: str,
    source: str,
    published_at: str | None,
    updated_at: str | None,
    cvss: float | None,
    severity: str,
    kev: bool,
    affected_products: list[str],
    references: list[str],
    config: dict[str, Any],
) -> Vulnerability | None:
    search_text = " ".join([title, description, " ".join(affected_products), severity])
    matched, matched_keywords, excluded = match_keywords(
        search_text,
        [str(item) for item in config.get("watch_keywords", [])],
        [str(item) for item in config.get("exclude_keywords", [])],
    )
    if excluded:
        return None
    category, category_keywords = classify_category(search_text, config)
    min_cvss = float(config.get("min_cvss", 7.0))
    if not (kev or matched or category != "security" or (cvss is not None and cvss >= min_cvss)):
        return None
    merged_keywords = list(dict.fromkeys(category_keywords + matched_keywords))
    return Vulnerability(
        cve_id=cve_id,
        title=title,
        description=description,
        source=source,
        published_at=published_at,
        updated_at=updated_at,
        cvss=cvss,
        severity=severity,
        kev=kev,
        affected_products=[item for item in affected_products if item],
        matched_keywords=merged_keywords,
        references=references,
        score=calculate_score(cvss, kev, merged_keywords, description, category),
        priority_group=category if category in {"frontend", "backend"} else "security",
        category=category,
    )


def normalize_nvd_item(item: dict[str, Any], kev_map: dict[str, dict[str, Any]], config: dict[str, Any], now: datetime) -> Vulnerability | None:
    cve = item.get("cve", {})
    if not isinstance(cve, dict) or not is_today_jst(cve.get("published"), now):
        return None
    cve_id = str(cve.get("id") or "")
    if not cve_id:
        return None
    descriptions = cve.get("descriptions", [])
    description = ""
    if isinstance(descriptions, list):
        english = [desc for desc in descriptions if isinstance(desc, dict) and desc.get("lang") == "en"]
        selected = english[0] if english else descriptions[0] if descriptions else {}
        description = str(selected.get("value") or "") if isinstance(selected, dict) else ""
    cvss, severity = extract_cvss_and_severity(cve)
    severity = severity if severity != "UNKNOWN" else severity_from_cvss(cvss)
    affected_products = extract_affected_products(cve)
    references = extract_references(cve)
    kev_item = kev_map.get(cve_id)
    is_kev = kev_item is not None
    if is_kev and kev_item:
        affected_products = affected_products or [
            " ".join(part for part in [str(kev_item.get("vendorProject") or ""), str(kev_item.get("product") or "")] if part).strip()
        ]
        if kev_item.get("notes"):
            references.append(str(kev_item.get("notes")))
    title = f"{cve_id}: {kev_item.get('vulnerabilityName')}" if is_kev and kev_item and kev_item.get("vulnerabilityName") else cve_id
    if title == cve_id and affected_products:
        title = f"{cve_id}: {affected_products[0]}"
    return make_vulnerability(
        cve_id,
        title,
        description,
        "NVD" + (" / CISA KEV" if is_kev else ""),
        format_date(cve.get("published")),
        format_date(cve.get("lastModified")),
        cvss,
        severity,
        is_kev,
        affected_products,
        references,
        config,
    )


def normalize_kev_today_item(cve_id: str, item: dict[str, Any], config: dict[str, Any], now: datetime) -> Vulnerability | None:
    if not is_today_date(str(item.get("dateAdded") or ""), now):
        return None
    vendor = str(item.get("vendorProject") or "")
    product = str(item.get("product") or "")
    vulnerability_name = str(item.get("vulnerabilityName") or cve_id)
    description = str(item.get("shortDescription") or "")
    affected = " ".join(part for part in [vendor, product] if part).strip()
    return make_vulnerability(
        cve_id,
        f"{cve_id}: {vulnerability_name}",
        description,
        "CISA KEV",
        str(item.get("dateAdded") or "-"),
        None,
        None,
        "KEV",
        True,
        [affected] if affected else [],
        [str(item.get("notes"))] if item.get("notes") else [],
        config,
    )


def prune_history(history: dict[str, Any], now: datetime, retention_days: int) -> dict[str, Any]:
    seen = history.get("seen", {})
    if not isinstance(seen, dict):
        seen = {}
    threshold = (now - timedelta(days=retention_days)).date()
    pruned: dict[str, Any] = {}
    for cve_id, value in seen.items():
        first_seen = str(value.get("first_seen", "")) if isinstance(value, dict) else ""
        try:
            first_seen_date = datetime.strptime(first_seen, "%Y-%m-%d").date()
        except ValueError:
            continue
        if first_seen_date >= threshold:
            pruned[cve_id] = value
    return {"seen": pruned}


def filter_new(vulnerabilities: list[Vulnerability], history: dict[str, Any]) -> list[Vulnerability]:
    seen = history.get("seen", {})
    return [vuln for vuln in vulnerabilities if vuln.cve_id not in seen]


def update_history(history: dict[str, Any], vulnerabilities: list[Vulnerability], now: datetime) -> dict[str, Any]:
    seen = history.setdefault("seen", {})
    today = now.strftime("%Y-%m-%d")
    for vuln in vulnerabilities:
        seen[vuln.cve_id] = {
            "title": vuln.title,
            "severity": vuln.severity,
            "cvss": vuln.cvss,
            "kev": vuln.kev,
            "category": vuln.category,
            "first_seen": today,
        }
    return history


def render_card(vuln: Vulnerability) -> list[str]:
    cvss_text = "-" if vuln.cvss is None else f"{vuln.cvss:.1f}"
    keywords = ", ".join(vuln.matched_keywords) if vuln.matched_keywords else "-"
    products = ", ".join(vuln.affected_products) if vuln.affected_products else "-"
    refs = vuln.references or [f"https://nvd.nist.gov/vuln/detail/{vuln.cve_id}"]
    priority_label = {
        "frontend": "Frontend",
        "backend": "Backend",
    }.get(vuln.category, "Security")
    lines = [
        f"### [{vuln.cve_id}]({refs[0]})",
        "",
        f"> **{priority_label}** / **{vuln.severity}** / CVSS: **{cvss_text}** / KEV: **{'yes' if vuln.kev else 'no'}**",
        "",
        f"- タイトル: {vuln.title}",
        f"- 概要: {compact_text(vuln.description)}",
        f"- 関連キーワード: {keywords}",
        f"- 影響製品: {products}",
        f"- 公開日: {vuln.published_at or '-'}",
        f"- 更新日: {vuln.updated_at or '-'}",
        f"- 出典: {vuln.source}",
        "- 参照:",
    ]
    lines.extend(f"  - {ref}" for ref in refs[:5])
    lines.append("")
    return lines


def render_summary(vulnerabilities: list[Vulnerability], now: datetime, errors: list[str], used_model: bool) -> str:
    fetched_text = now.strftime("%Y-%m-%d %H:%M:%S JST")
    date_text = now.strftime("%Y-%m-%d")
    frontend_count = sum(1 for vuln in vulnerabilities if vuln.category == "frontend")
    backend_count = sum(1 for vuln in vulnerabilities if vuln.category == "backend")
    kev_count = sum(1 for vuln in vulnerabilities if vuln.kev)
    critical_count = sum(1 for vuln in vulnerabilities if vuln.severity == "CRITICAL")
    lines = [
        f"# CVE Digest Summary ({date_text})",
        "",
        "## Overview",
        "",
        f"- 取得日時: {fetched_text}",
        "- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ",
        f"- 新規掲載件数: {len(vulnerabilities)}",
        f"- Frontend関連: {frontend_count}",
        f"- Backend関連: {backend_count}",
        f"- KEV掲載: {kev_count}",
        f"- Critical: {critical_count}",
        f"- 日本語AI要約: {'GitHub Models' if used_model else '未使用'}",
        "",
    ]
    if errors:
        lines.extend(["## 取得エラー", ""])
        lines.extend(f"- {error}" for error in errors)
        lines.append("")
    if not vulnerabilities:
        lines.extend(["## 結果", "", "条件に一致する今日公開の新規脆弱性はありませんでした。", ""])
        return "\n".join(lines)
    groups = [
        ("Frontend", lambda vuln: vuln.category == "frontend"),
        ("Backend", lambda vuln: vuln.category == "backend"),
        ("Exploited / KEV", lambda vuln: vuln.category == "security" and vuln.kev),
        ("Critical", lambda vuln: vuln.category == "security" and not vuln.kev and vuln.severity == "CRITICAL"),
        ("High", lambda vuln: vuln.category == "security" and not vuln.kev and vuln.severity == "HIGH"),
        ("Other", lambda vuln: vuln.category == "security" and not vuln.kev and vuln.severity not in {"CRITICAL", "HIGH"}),
    ]
    for heading, predicate in groups:
        items = [vuln for vuln in vulnerabilities if predicate(vuln)]
        if not items:
            continue
        lines.extend([f"## {heading}", ""])
        for vuln in items:
            lines.extend(render_card(vuln))
    return "\n".join(lines)


def render_category_summary(vulnerabilities: list[Vulnerability], now: datetime, errors: list[str], category: str) -> str:
    date_text = now.strftime("%Y-%m-%d")
    fetched_text = now.strftime("%Y-%m-%d %H:%M:%S JST")
    label = "Frontend" if category == "frontend" else "Backend"
    items = [vuln for vuln in vulnerabilities if vuln.category == category]
    lines = [
        f"# {label} CVE Summary ({date_text})",
        "",
        "## Overview",
        "",
        f"- 取得日時: {fetched_text}",
        "- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ",
        f"- 掲載件数: {len(items)}",
        f"- Critical: {sum(1 for vuln in items if vuln.severity == 'CRITICAL')}",
        f"- High: {sum(1 for vuln in items if vuln.severity == 'HIGH')}",
        f"- KEV掲載: {sum(1 for vuln in items if vuln.kev)}",
        "- 日本語AI要約: 未使用",
        "",
    ]
    if errors:
        lines.extend(["## 取得エラー", ""])
        lines.extend(f"- {error}" for error in errors)
        lines.append("")
    if not items:
        lines.extend(["## 結果", "", f"条件に一致する{label}関連の新規脆弱性はありませんでした。", ""])
        return "\n".join(lines)
    lines.extend(["## CVEs", ""])
    for vuln in items:
        lines.extend(render_card(vuln))
    return "\n".join(lines)


def collect_vulnerabilities(config: dict[str, Any], now: datetime) -> tuple[list[Vulnerability], list[str]]:
    errors: list[str] = []
    kev_map: dict[str, dict[str, Any]] = {}
    nvd_items: list[dict[str, Any]] = []
    try:
        kev_map = fetch_cisa_kev(config)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as error:
        errors.append(f"CISA KEV: {error}")
    try:
        nvd_items = fetch_nvd_today(config, now)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as error:
        errors.append(f"NVD: {error}")
    vulnerabilities_by_id: dict[str, Vulnerability] = {}
    for item in nvd_items:
        if isinstance(item, dict):
            vuln = normalize_nvd_item(item, kev_map, config, now)
            if vuln:
                vulnerabilities_by_id[vuln.cve_id] = vuln
    for cve_id, kev_item in kev_map.items():
        if cve_id in vulnerabilities_by_id:
            continue
        vuln = normalize_kev_today_item(cve_id, kev_item, config, now)
        if vuln:
            vulnerabilities_by_id[cve_id] = vuln
    vulnerabilities = list(vulnerabilities_by_id.values())
    order = {"frontend": 0, "backend": 1, "security": 2}
    vulnerabilities.sort(key=lambda vuln: (order.get(vuln.category, 9), -vuln.score, -(vuln.cvss or 0), vuln.cve_id))
    return vulnerabilities[: int(config.get("max_items", 30))], errors


def main() -> int:
    now = datetime.now(JST)
    config = load_json(CONFIG_PATH, {})
    history = load_json(HISTORY_PATH, {"seen": {}})
    history = prune_history(history, now, int(config.get("history_retention_days", 120)))
    vulnerabilities, errors = collect_vulnerabilities(config, now)
    new_vulnerabilities = filter_new(vulnerabilities, history)
    used_model = False

    output_dir = OUTPUT_ROOT / now.strftime("%Y-%m-%d")
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "summary.md": render_summary(new_vulnerabilities, now, errors, used_model),
        "frontend-summary.md": render_category_summary(new_vulnerabilities, now, errors, "frontend"),
        "backend-summary.md": render_category_summary(new_vulnerabilities, now, errors, "backend"),
    }
    for filename, content in outputs.items():
        output_path = output_dir / filename
        output_path.write_text(content, encoding="utf-8")
        print(f"created: {output_path.relative_to(ROOT_DIR)}")

    write_json(HISTORY_PATH, update_history(history, new_vulnerabilities, now))
    if errors:
        print("warning: one or more sources failed, but markdown files were generated", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

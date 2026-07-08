from __future__ import annotations

import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
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


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def format_date(value: str | None) -> str | None:
    parsed = parse_datetime(value)
    if parsed is None:
        return value
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=UTC)
    return parsed.astimezone(JST).strftime("%Y-%m-%d %H:%M:%S JST")


def compact_text(value: str | None, max_length: int = 320) -> str:
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
            criteria = str(match.get("criteria", ""))
            parts = criteria.split(":")
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
    refs: list[Any]

    if isinstance(raw_references, dict):
        reference_data = raw_references.get("referenceData", [])
        refs = reference_data if isinstance(reference_data, list) else []
    elif isinstance(raw_references, list):
        refs = raw_references
    else:
        refs = []

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
    return bool(matched), matched, False


def calculate_score(cvss: float | None, kev: bool, matched_keywords: list[str], description: str) -> int:
    score = 100 if kev else 0
    if cvss is not None:
        if cvss >= 9.0:
            score += 50
        elif cvss >= 7.0:
            score += 30
        elif cvss >= 4.0:
            score += 10
    score += len(matched_keywords) * 10
    lower_description = description.lower()
    for word in [
        "remote code execution",
        "rce",
        "authentication bypass",
        "privilege escalation",
        "sql injection",
        "command injection",
    ]:
        if word in lower_description:
            score += 15
    return score


def fetch_nvd(config: dict[str, Any], now: datetime) -> list[dict[str, Any]]:
    source = config.get("sources", {}).get("nvd", {})
    if not source.get("enabled", True):
        return []
    lookback_days = int(config.get("lookback_days", 2))
    start = (now.astimezone(UTC) - timedelta(days=lookback_days)).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    end = now.astimezone(UTC).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    data = fetch_json(
        str(source.get("url")),
        {"pubStartDate": start, "pubEndDate": end, "resultsPerPage": "200"},
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


def normalize_nvd_item(item: dict[str, Any], kev_map: dict[str, dict[str, Any]], config: dict[str, Any]) -> Vulnerability | None:
    cve = item.get("cve", {})
    if not isinstance(cve, dict):
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
            " ".join(
                part for part in [str(kev_item.get("vendorProject") or ""), str(kev_item.get("product") or "")] if part
            ).strip()
        ]
        if kev_item.get("notes"):
            references.append(str(kev_item.get("notes")))

    title = cve_id
    if is_kev and kev_item and kev_item.get("vulnerabilityName"):
        title = f"{cve_id}: {kev_item.get('vulnerabilityName')}"
    elif affected_products:
        title = f"{cve_id}: {affected_products[0]}"

    keywords = [str(item) for item in config.get("watch_keywords", [])]
    excludes = [str(item) for item in config.get("exclude_keywords", [])]
    matched, matched_keywords, excluded = match_keywords(
        " ".join([title, description, " ".join(affected_products), severity]), keywords, excludes
    )
    if excluded:
        return None

    min_cvss = float(config.get("min_cvss", 7.0))
    if not (is_kev or matched or (cvss is not None and cvss >= min_cvss)):
        return None

    return Vulnerability(
        cve_id=cve_id,
        title=title,
        description=description,
        source="NVD" + (" / CISA KEV" if is_kev else ""),
        published_at=format_date(cve.get("published")),
        updated_at=format_date(cve.get("lastModified")),
        cvss=cvss,
        severity=severity,
        kev=is_kev,
        affected_products=[item for item in affected_products if item],
        matched_keywords=matched_keywords,
        references=references,
        score=calculate_score(cvss, is_kev, matched_keywords, description),
    )


def is_recent_kev(item: dict[str, Any], now: datetime, lookback_days: int) -> bool:
    date_added = str(item.get("dateAdded") or "")
    try:
        added_date = datetime.strptime(date_added, "%Y-%m-%d").date()
    except ValueError:
        return False
    threshold = (now - timedelta(days=lookback_days)).date()
    return added_date >= threshold


def normalize_kev_only_item(cve_id: str, item: dict[str, Any], config: dict[str, Any], now: datetime) -> Vulnerability | None:
    vendor = str(item.get("vendorProject") or "")
    product = str(item.get("product") or "")
    vulnerability_name = str(item.get("vulnerabilityName") or cve_id)
    description = str(item.get("shortDescription") or "")
    title = f"{cve_id}: {vulnerability_name}"
    affected = " ".join(part for part in [vendor, product] if part).strip()
    search_text = " ".join([title, description, affected])
    matched, matched_keywords, excluded = match_keywords(
        search_text,
        [str(item) for item in config.get("watch_keywords", [])],
        [str(item) for item in config.get("exclude_keywords", [])],
    )
    if excluded:
        return None
    if not (matched or is_recent_kev(item, now, int(config.get("lookback_days", 2)))):
        return None
    return Vulnerability(
        cve_id=cve_id,
        title=title,
        description=description,
        source="CISA KEV",
        published_at=str(item.get("dateAdded") or "-"),
        updated_at=None,
        cvss=None,
        severity="KEV",
        kev=True,
        affected_products=[affected] if affected else [],
        matched_keywords=matched_keywords,
        references=[str(item.get("notes"))] if item.get("notes") else [],
        score=calculate_score(None, True, matched_keywords, description),
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
            "first_seen": today,
        }
    return history


def render_summary(vulnerabilities: list[Vulnerability], now: datetime, errors: list[str]) -> str:
    fetched_text = now.strftime("%Y-%m-%d %H:%M:%S JST")
    date_text = now.strftime("%Y-%m-%d")
    lines = [
        f"# CVE Digest Summary ({date_text})",
        "",
        f"- 取得日時: {fetched_text}",
        f"- 新規掲載件数: {len(vulnerabilities)}",
        "- 出力対象: 新規CVEのみ",
        "",
    ]
    if errors:
        lines.extend(["## 取得エラー", ""])
        lines.extend(f"- {error}" for error in errors)
        lines.append("")
    if not vulnerabilities:
        lines.extend(["## 結果", "", "条件に一致する新規脆弱性はありませんでした。", ""])
        return "\n".join(lines)

    groups = [
        ("緊急対応候補", lambda vuln: vuln.kev),
        ("Critical", lambda vuln: not vuln.kev and vuln.severity == "CRITICAL"),
        ("High", lambda vuln: not vuln.kev and vuln.severity == "HIGH"),
        ("Other", lambda vuln: not vuln.kev and vuln.severity not in {"CRITICAL", "HIGH"}),
    ]
    for heading, predicate in groups:
        items = [vuln for vuln in vulnerabilities if predicate(vuln)]
        if not items:
            continue
        lines.extend([f"## {heading}", ""])
        for vuln in items:
            cvss_text = "-" if vuln.cvss is None else f"{vuln.cvss:.1f}"
            keywords = ", ".join(vuln.matched_keywords) if vuln.matched_keywords else "-"
            products = ", ".join(vuln.affected_products) if vuln.affected_products else "-"
            references = vuln.references or [f"https://nvd.nist.gov/vuln/detail/{vuln.cve_id}"]
            lines.extend(
                [
                    f"### {vuln.title}",
                    "",
                    f"- 重要度: {vuln.severity}",
                    f"- CVSS: {cvss_text}",
                    f"- KEV掲載: {'yes' if vuln.kev else 'no'}",
                    f"- 関連キーワード: {keywords}",
                    f"- 影響製品: {products}",
                    f"- 公開日: {vuln.published_at or '-'}",
                    f"- 更新日: {vuln.updated_at or '-'}",
                    f"- 出典: {vuln.source}",
                    f"- 概要: {compact_text(vuln.description)}",
                    "- 参照:",
                ]
            )
            lines.extend(f"  - {ref}" for ref in references[:5])
            lines.append("")
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
        nvd_items = fetch_nvd(config, now)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as error:
        errors.append(f"NVD: {error}")

    vulnerabilities_by_id: dict[str, Vulnerability] = {}
    for item in nvd_items:
        if isinstance(item, dict):
            vuln = normalize_nvd_item(item, kev_map, config)
            if vuln:
                vulnerabilities_by_id[vuln.cve_id] = vuln

    for cve_id, kev_item in kev_map.items():
        if cve_id in vulnerabilities_by_id:
            continue
        vuln = normalize_kev_only_item(cve_id, kev_item, config, now)
        if vuln:
            vulnerabilities_by_id[cve_id] = vuln

    vulnerabilities = list(vulnerabilities_by_id.values())
    vulnerabilities.sort(key=lambda vuln: (vuln.score, vuln.cvss or 0), reverse=True)
    return vulnerabilities[: int(config.get("max_items", 30))], errors


def main() -> int:
    now = datetime.now(JST)
    config = load_json(CONFIG_PATH, {})
    history = load_json(HISTORY_PATH, {"seen": {}})
    history = prune_history(history, now, int(config.get("history_retention_days", 120)))
    vulnerabilities, errors = collect_vulnerabilities(config, now)
    new_vulnerabilities = filter_new(vulnerabilities, history)

    output_dir = OUTPUT_ROOT / now.strftime("%Y-%m-%d")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "summary.md"
    output_path.write_text(render_summary(new_vulnerabilities, now, errors), encoding="utf-8")
    print(f"created: {output_path.relative_to(ROOT_DIR)}")

    write_json(HISTORY_PATH, update_history(history, new_vulnerabilities, now))
    if errors:
        print("warning: one or more sources failed, but summary.md was generated", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

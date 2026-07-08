from __future__ import annotations

import json
import os
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
    return bool(matched), matched, False


def is_frontend_vulnerability(vuln_text: str, config: dict[str, Any]) -> tuple[bool, list[str]]:
    keywords = [str(item) for item in config.get("frontend_keywords", [])]
    _, matched, _ = match_keywords(vuln_text, keywords, [])
    return bool(matched), matched


def calculate_score(cvss: float | None, kev: bool, matched_keywords: list[str], description: str, is_frontend: bool) -> int:
    score = 1000 if is_frontend else 0
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
    for word in ["remote code execution", "rce", "authentication bypass", "privilege escalation", "xss", "prototype pollution", "csrf", "ssrf"]:
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
    is_frontend, frontend_matches = is_frontend_vulnerability(search_text, config)
    min_cvss = float(config.get("min_cvss", 7.0))
    if not (kev or matched or is_frontend or (cvss is not None and cvss >= min_cvss)):
        return None
    priority_group = "frontend" if is_frontend else "security"
    merged_keywords = list(dict.fromkeys(frontend_matches + matched_keywords))
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
        score=calculate_score(cvss, kev, merged_keywords, description, is_frontend),
        priority_group=priority_group,
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


def compact_for_model(vuln: Vulnerability) -> dict[str, Any]:
    return {
        "cve_id": vuln.cve_id,
        "title": vuln.title,
        "severity": vuln.severity,
        "cvss": vuln.cvss,
        "kev": vuln.kev,
        "priority_group": vuln.priority_group,
        "matched_keywords": vuln.matched_keywords,
        "affected_products": vuln.affected_products,
        "description": compact_text(vuln.description, 700),
    }


def call_github_models(vulnerabilities: list[Vulnerability], config: dict[str, Any]) -> dict[str, str]:
    model_config = config.get("github_models", {})
    if not model_config.get("enabled", True) or not vulnerabilities:
        return {}
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if not token:
        return {}
    max_items = int(model_config.get("max_items", 30))
    payload = [compact_for_model(vuln) for vuln in vulnerabilities[:max_items]]
    request_body = {
        "model": str(model_config.get("model", "openai/gpt-4.1-mini")),
        "messages": [
            {
                "role": "system",
                "content": "あなたは脆弱性情報を日本語で簡潔に整理するセキュリティ担当です。誇張せず、開発者が読む要約だけをJSONで返してください。",
            },
            {
                "role": "user",
                "content": "次のCVEごとに日本語で2文以内の要約と対応目安を作ってください。返却は {\"items\":[{\"cve_id\":\"...\",\"summary\":\"...\"}]} のJSONのみ。\n" + json.dumps({"items": payload}, ensure_ascii=False),
            },
        ],
        "temperature": 0.2,
        "max_tokens": int(model_config.get("max_tokens", 2500)),
    }
    request = urllib.request.Request(
        str(model_config.get("endpoint", "https://models.github.ai/inference/chat/completions")),
        data=json.dumps(request_body).encode("utf-8"),
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            response_data = json.loads(response.read().decode("utf-8"))
        content = response_data["choices"][0]["message"]["content"]
        content = re.sub(r"^```(?:json)?\s*|\s*```$", "", content.strip())
        parsed = json.loads(content)
        items = parsed.get("items", [])
        if not isinstance(items, list):
            return {}
        return {str(item.get("cve_id")): str(item.get("summary")) for item in items if isinstance(item, dict) and item.get("cve_id") and item.get("summary")}
    except Exception as error:  # noqa: BLE001
        print(f"github models summary failed: {error}", file=sys.stderr)
        return {}


def apply_ai_summaries(vulnerabilities: list[Vulnerability], summaries: dict[str, str]) -> list[Vulnerability]:
    return [
        Vulnerability(
            **{**vuln.__dict__, "ai_summary": summaries.get(vuln.cve_id)}
        )
        for vuln in vulnerabilities
    ]


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
        seen[vuln.cve_id] = {"title": vuln.title, "severity": vuln.severity, "cvss": vuln.cvss, "kev": vuln.kev, "first_seen": today}
    return history


def render_card(vuln: Vulnerability) -> list[str]:
    cvss_text = "-" if vuln.cvss is None else f"{vuln.cvss:.1f}"
    keywords = ", ".join(vuln.matched_keywords) if vuln.matched_keywords else "-"
    products = ", ".join(vuln.affected_products) if vuln.affected_products else "-"
    refs = vuln.references or [f"https://nvd.nist.gov/vuln/detail/{vuln.cve_id}"]
    priority_label = "フロントエンド最優先" if vuln.priority_group == "frontend" else "通常優先"
    lines = [
        f"### [{vuln.cve_id}]({refs[0]})",
        "",
        f"> **{priority_label}** / **{vuln.severity}** / CVSS: **{cvss_text}** / KEV: **{'yes' if vuln.kev else 'no'}**",
        "",
        f"- タイトル: {vuln.title}",
        f"- AI要約: {vuln.ai_summary or 'GitHub Modelsの要約は取得できませんでした。'}",
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
    frontend_count = sum(1 for vuln in vulnerabilities if vuln.priority_group == "frontend")
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
        f"- フロントエンド関連: {frontend_count}",
        f"- KEV掲載: {kev_count}",
        f"- Critical: {critical_count}",
        f"- 日本語要約: {'GitHub Models' if used_model else '未使用または失敗'}",
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
        ("Frontend Priority", lambda vuln: vuln.priority_group == "frontend"),
        ("Exploited / KEV", lambda vuln: vuln.priority_group != "frontend" and vuln.kev),
        ("Critical", lambda vuln: vuln.priority_group != "frontend" and not vuln.kev and vuln.severity == "CRITICAL"),
        ("High", lambda vuln: vuln.priority_group != "frontend" and not vuln.kev and vuln.severity == "HIGH"),
        ("Other", lambda vuln: vuln.priority_group != "frontend" and not vuln.kev and vuln.severity not in {"CRITICAL", "HIGH"}),
    ]
    for heading, predicate in groups:
        items = [vuln for vuln in vulnerabilities if predicate(vuln)]
        if not items:
            continue
        lines.extend([f"## {heading}", ""])
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
    vulnerabilities.sort(key=lambda vuln: (0 if vuln.priority_group == "frontend" else 1, -vuln.score, -(vuln.cvss or 0), vuln.cve_id))
    return vulnerabilities[: int(config.get("max_items", 30))], errors


def main() -> int:
    now = datetime.now(JST)
    config = load_json(CONFIG_PATH, {})
    history = load_json(HISTORY_PATH, {"seen": {}})
    history = prune_history(history, now, int(config.get("history_retention_days", 120)))
    vulnerabilities, errors = collect_vulnerabilities(config, now)
    new_vulnerabilities = filter_new(vulnerabilities, history)
    summaries = call_github_models(new_vulnerabilities, config)
    used_model = bool(summaries)
    new_vulnerabilities = apply_ai_summaries(new_vulnerabilities, summaries)

    output_dir = OUTPUT_ROOT / now.strftime("%Y-%m-%d")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "summary.md"
    output_path.write_text(render_summary(new_vulnerabilities, now, errors, used_model), encoding="utf-8")
    print(f"created: {output_path.relative_to(ROOT_DIR)}")
    write_json(HISTORY_PATH, update_history(history, new_vulnerabilities, now))
    if errors:
        print("warning: one or more sources failed, but summary.md was generated", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

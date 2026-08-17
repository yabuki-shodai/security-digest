from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, replace
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
DEFAULT_MODEL_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models"
DEFAULT_MODEL = "gemini-2.5-flash"
FRONTEND_PRIORITY = ["next.js", "nextjs", "react", "typescript", "npm", "pnpm", "yarn", "vite", "tailwind css"]
BACKEND_PRIORITY = ["django", "fastapi", "nestjs", "nest.js", "go", "golang", "python", "docker", "aws", "postgresql", "mysql", "redis"]


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


def post_json(url: str, payload: dict[str, Any], headers: dict[str, str], timeout: int = 60) -> dict[str, Any]:
    request = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def model_config(config: dict[str, Any]) -> dict[str, Any]:
    raw = config.get("gemini", {})
    return raw if isinstance(raw, dict) else {}


def gemini_enabled(config: dict[str, Any]) -> bool:
    models = model_config(config)
    return bool(models.get("enabled", config.get("gemini_enabled", True)))


def model_text(messages: list[dict[str, str]], config: dict[str, Any], default_max_tokens: int = 700) -> str | None:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key or not gemini_enabled(config):
        return None
    models = model_config(config)
    model_name = str(models.get("model") or config.get("gemini_model") or DEFAULT_MODEL)
    endpoint = f"{str(models.get('endpoint') or DEFAULT_MODEL_ENDPOINT)}/{model_name}:generateContent"
    system_parts = [str(message.get("content", "")) for message in messages if message.get("role") == "system"]
    user_parts = [str(message.get("content", "")) for message in messages if message.get("role") != "system"]
    payload: dict[str, Any] = {
        "contents": [{"role": "user", "parts": [{"text": "\n\n".join(user_parts)}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": int(models.get("max_tokens", default_max_tokens))},
    }
    if system_parts:
        payload["systemInstruction"] = {"parts": [{"text": "\n\n".join(system_parts)}]}
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json", "Content-Type": "application/json", "x-goog-api-key": api_key}
    try:
        data = post_json(endpoint, payload, headers)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError):
        return None
    candidates = data.get("candidates", [])
    if not candidates or not isinstance(candidates[0], dict):
        return None
    content = candidates[0].get("content", {})
    parts = content.get("parts", []) if isinstance(content, dict) else []
    if not parts or not isinstance(parts[0], dict):
        return None
    text = parts[0].get("text")
    return str(text).strip() if text else None


def compact_text(value: str | None, max_length: int = 700) -> str:
    if not value:
        return "-"
    text = " ".join(str(value).split())
    return text[:max_length].rstrip() + "..." if len(text) > max_length else text


def parse_datetime(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=UTC)


def is_today_jst(value: str | None, now: datetime) -> bool:
    parsed = parse_datetime(value)
    return bool(parsed and parsed.astimezone(JST).date() == now.astimezone(JST).date())


def is_today_date(value: str | None, now: datetime) -> bool:
    try:
        return bool(value and datetime.strptime(value, "%Y-%m-%d").date() == now.astimezone(JST).date())
    except ValueError:
        return False


def format_date(value: str | None) -> str | None:
    parsed = parse_datetime(value)
    return value if parsed is None else parsed.astimezone(JST).strftime("%Y-%m-%d %H:%M:%S JST")


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
    best_score: float | None = None
    best_severity = "UNKNOWN"
    if not isinstance(metrics, dict):
        return None, best_severity
    for key in ["cvssMetricV40", "cvssMetricV31", "cvssMetricV30", "cvssMetricV2"]:
        for item in metrics.get(key) or []:
            if not isinstance(item, dict):
                continue
            cvss_data = item.get("cvssData", {})
            if not isinstance(cvss_data, dict):
                continue
            try:
                score = float(cvss_data.get("baseScore"))
            except (TypeError, ValueError):
                continue
            if best_score is None or score > best_score:
                best_score = score
                best_severity = str(item.get("baseSeverity") or cvss_data.get("baseSeverity") or severity_from_cvss(score)).upper()
    return best_score, best_severity


def extract_affected_products(cve: dict[str, Any]) -> list[str]:
    products: set[str] = set()

    def walk(node: dict[str, Any]) -> None:
        for match in node.get("cpeMatch", []) or []:
            parts = str(match.get("criteria", "")).split(":") if isinstance(match, dict) else []
            if len(parts) >= 5 and parts[4] != "*":
                products.add(f"{parts[3].replace('_', ' ')} {parts[4].replace('_', ' ')}".strip())
        for child in node.get("nodes", []) or []:
            if isinstance(child, dict):
                walk(child)

    for config in cve.get("configurations", []) if isinstance(cve.get("configurations", []), list) else []:
        if isinstance(config, dict):
            for node in config.get("nodes", []) or []:
                if isinstance(node, dict):
                    walk(node)
    return sorted(products)[:10]


def extract_references(cve: dict[str, Any]) -> list[str]:
    raw = cve.get("references", [])
    refs = raw.get("referenceData", []) if isinstance(raw, dict) else raw if isinstance(raw, list) else []
    return [str(ref["url"]) for ref in refs if isinstance(ref, dict) and ref.get("url")][:5]


def match_keywords(text: str, keywords: list[str], exclude_keywords: list[str]) -> tuple[bool, list[str], bool]:
    lower_text = text.lower()
    if any(keyword.lower() in lower_text for keyword in exclude_keywords):
        return False, [], True
    matched = [keyword for keyword in keywords if keyword.lower() in lower_text]
    return bool(matched), list(dict.fromkeys(matched)), False


def category_matches(text: str, config: dict[str, Any], category: str) -> list[str]:
    _, matched, _ = match_keywords(text, [str(item) for item in config.get(f"{category}_keywords", [])], [])
    return matched


def classify_category(text: str, config: dict[str, Any]) -> tuple[str, list[str]]:
    frontend_matches = category_matches(text, config, "frontend")
    backend_matches = category_matches(text, config, "backend")
    if frontend_matches:
        return "frontend", frontend_matches
    if backend_matches:
        return "backend", backend_matches
    return "security", []


def tech_priority(vuln: Vulnerability) -> int:
    priority = FRONTEND_PRIORITY if vuln.category == "frontend" else BACKEND_PRIORITY if vuln.category == "backend" else []
    haystack = " ".join([vuln.title, vuln.description, " ".join(vuln.matched_keywords), " ".join(vuln.affected_products)]).lower()
    for index, keyword in enumerate(priority):
        if keyword in haystack:
            return index
    return len(priority) + 1


def calculate_score(cvss: float | None, kev: bool, matched_keywords: list[str], description: str, category: str) -> int:
    score = 1000 if category == "frontend" else 900 if category == "backend" else 0
    score += 100 if kev else 0
    if cvss is not None:
        score += 50 if cvss >= 9.0 else 30 if cvss >= 7.0 else 10 if cvss >= 4.0 else 0
    score += len(matched_keywords) * 10
    for word in ["remote code execution", "rce", "authentication bypass", "privilege escalation", "xss", "prototype pollution", "csrf", "ssrf"]:
        if word in description.lower():
            score += 15
    return score


def make_vulnerability(cve_id: str, title: str, description: str, source: str, published_at: str | None, updated_at: str | None, cvss: float | None, severity: str, kev: bool, affected_products: list[str], references: list[str], config: dict[str, Any]) -> Vulnerability | None:
    search_text = " ".join([title, description, " ".join(affected_products), severity])
    matched, matched_keywords, excluded = match_keywords(search_text, [str(item) for item in config.get("watch_keywords", [])], [str(item) for item in config.get("exclude_keywords", [])])
    if excluded:
        return None
    category, category_keywords = classify_category(search_text, config)
    min_cvss = float(config.get("min_cvss", 7.0))
    if not (kev or matched or category != "security" or (cvss is not None and cvss >= min_cvss)):
        return None
    keywords = list(dict.fromkeys(category_keywords + matched_keywords))
    return Vulnerability(cve_id, title, description, source, published_at, updated_at, cvss, severity, kev, [item for item in affected_products if item], keywords, references, calculate_score(cvss, kev, keywords, description, category), category)


def fetch_nvd_today(config: dict[str, Any], now: datetime) -> list[dict[str, Any]]:
    source = config.get("sources", {}).get("nvd", {})
    if not source.get("enabled", True):
        return []
    start = datetime.combine(now.astimezone(JST).date(), time.min, tzinfo=JST).astimezone(UTC)
    end = (datetime.combine(now.astimezone(JST).date(), time.min, tzinfo=JST) + timedelta(days=1)).astimezone(UTC)
    data = fetch_json(str(source.get("url")), {"pubStartDate": start.strftime("%Y-%m-%dT%H:%M:%S.000Z"), "pubEndDate": end.strftime("%Y-%m-%dT%H:%M:%S.000Z"), "resultsPerPage": "200"})
    vulnerabilities = data.get("vulnerabilities", [])
    return vulnerabilities if isinstance(vulnerabilities, list) else []


def fetch_cisa_kev(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    source = config.get("sources", {}).get("cisa_kev", {})
    if not source.get("enabled", True):
        return {}
    data = fetch_json(str(source.get("url")))
    result: dict[str, dict[str, Any]] = {}
    for item in data.get("vulnerabilities", []) if isinstance(data.get("vulnerabilities", []), list) else []:
        cve_id = item.get("cveID") if isinstance(item, dict) else None
        if cve_id:
            result[str(cve_id)] = item
    return result


def normalize_nvd_item(item: dict[str, Any], kev_map: dict[str, dict[str, Any]], config: dict[str, Any], now: datetime) -> Vulnerability | None:
    cve = item.get("cve", {})
    if not isinstance(cve, dict) or not is_today_jst(cve.get("published"), now):
        return None
    cve_id = str(cve.get("id") or "")
    if not cve_id:
        return None
    descriptions = cve.get("descriptions", [])
    english = [desc for desc in descriptions if isinstance(desc, dict) and desc.get("lang") == "en"] if isinstance(descriptions, list) else []
    selected = english[0] if english else descriptions[0] if isinstance(descriptions, list) and descriptions else {}
    description = str(selected.get("value") or "") if isinstance(selected, dict) else ""
    cvss, severity = extract_cvss_and_severity(cve)
    affected_products = extract_affected_products(cve)
    references = extract_references(cve)
    kev_item = kev_map.get(cve_id)
    if kev_item:
        affected_products = affected_products or [" ".join(part for part in [str(kev_item.get("vendorProject") or ""), str(kev_item.get("product") or "")] if part).strip()]
        if kev_item.get("notes"):
            references.append(str(kev_item.get("notes")))
    title = f"{cve_id}: {kev_item.get('vulnerabilityName')}" if kev_item and kev_item.get("vulnerabilityName") else cve_id
    if title == cve_id and affected_products:
        title = f"{cve_id}: {affected_products[0]}"
    return make_vulnerability(cve_id, title, description, "NVD" + (" / CISA KEV" if kev_item else ""), format_date(cve.get("published")), format_date(cve.get("lastModified")), cvss, severity if severity != "UNKNOWN" else severity_from_cvss(cvss), bool(kev_item), affected_products, references, config)


def normalize_kev_today_item(cve_id: str, item: dict[str, Any], config: dict[str, Any], now: datetime) -> Vulnerability | None:
    if not is_today_date(str(item.get("dateAdded") or ""), now):
        return None
    affected = " ".join(part for part in [str(item.get("vendorProject") or ""), str(item.get("product") or "")] if part).strip()
    return make_vulnerability(cve_id, f"{cve_id}: {item.get('vulnerabilityName') or cve_id}", str(item.get("shortDescription") or ""), "CISA KEV", str(item.get("dateAdded") or "-"), None, None, "KEV", True, [affected] if affected else [], [str(item.get("notes"))] if item.get("notes") else [], config)


def prune_history(history: dict[str, Any], now: datetime, retention_days: int) -> dict[str, Any]:
    seen = history.get("seen", {}) if isinstance(history.get("seen", {}), dict) else {}
    threshold = (now - timedelta(days=retention_days)).date()
    pruned = {}
    for cve_id, value in seen.items():
        first_seen = str(value.get("first_seen", "")) if isinstance(value, dict) else ""
        try:
            if datetime.strptime(first_seen, "%Y-%m-%d").date() >= threshold:
                pruned[cve_id] = value
        except ValueError:
            continue
    return {"seen": pruned}


def update_history(history: dict[str, Any], vulnerabilities: list[Vulnerability], now: datetime) -> dict[str, Any]:
    seen = history.setdefault("seen", {})
    today = now.strftime("%Y-%m-%d")
    for vuln in vulnerabilities:
        seen[vuln.cve_id] = {"title": vuln.title, "severity": vuln.severity, "cvss": vuln.cvss, "kev": vuln.kev, "category": vuln.category, "first_seen": today}
    return history


def collect_vulnerabilities(config: dict[str, Any], now: datetime) -> tuple[list[Vulnerability], list[str]]:
    errors: list[str] = []
    try:
        kev_map = fetch_cisa_kev(config)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as error:
        errors.append(f"CISA KEV: {error}")
        kev_map = {}
    try:
        nvd_items = fetch_nvd_today(config, now)
    except (urllib.error.URLError, TimeoutError, OSError, ValueError, json.JSONDecodeError) as error:
        errors.append(f"NVD: {error}")
        nvd_items = []
    by_id: dict[str, Vulnerability] = {}
    for item in nvd_items:
        if isinstance(item, dict):
            vuln = normalize_nvd_item(item, kev_map, config, now)
            if vuln:
                by_id[vuln.cve_id] = vuln
    for cve_id, kev_item in kev_map.items():
        if cve_id not in by_id:
            vuln = normalize_kev_today_item(cve_id, kev_item, config, now)
            if vuln:
                by_id[cve_id] = vuln
    vulnerabilities = list(by_id.values())
    order = {"frontend": 0, "backend": 1, "security": 2}
    vulnerabilities.sort(key=lambda vuln: (order.get(vuln.category, 9), tech_priority(vuln), -vuln.score, -(vuln.cvss or 0), vuln.cve_id))
    return vulnerabilities[: int(config.get("max_items", 30))], errors


def fallback_ai_summary(vuln: Vulnerability) -> str:
    return "\n".join([
        f"- 日本語要約: {compact_text(vuln.description, 320)}",
        "- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。",
        "- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。",
    ])


def add_ai_summaries(vulnerabilities: list[Vulnerability], config: dict[str, Any]) -> tuple[list[Vulnerability], bool]:
    enriched: list[Vulnerability] = []
    used_model = False
    for vuln in vulnerabilities:
        prompt = "\n".join([
            "次のCVEについて、日本語で3行だけ出力してください。形式は必ず次の通り: - 日本語要約: ... / - 影響: ... / - 推奨対応: ...。不明点は断定しないでください。",
            f"CVE: {vuln.cve_id}", f"Title: {vuln.title}", f"Severity: {vuln.severity}", f"CVSS: {vuln.cvss}", f"KEV: {vuln.kev}",
            f"Products: {', '.join(vuln.affected_products)}", f"Description: {compact_text(vuln.description, 1200)}",
        ])
        content = model_text([{"role": "system", "content": "あなたは開発者向けCVE要約を作るセキュリティアナリストです。"}, {"role": "user", "content": prompt}], config, 500)
        enriched.append(replace(vuln, ai_summary=content or fallback_ai_summary(vuln)))
        used_model = used_model or bool(content)
    return enriched, used_model


def build_today_ai_overview(vulnerabilities: list[Vulnerability], config: dict[str, Any]) -> tuple[str, bool]:
    if not vulnerabilities:
        return "今日掲載された対象CVEはありません。", False
    rows = [{"cve_id": vuln.cve_id, "title": vuln.title, "severity": vuln.severity, "cvss": vuln.cvss, "kev": vuln.kev, "category": vuln.category, "keywords": vuln.matched_keywords, "description": compact_text(vuln.description, 500)} for vuln in vulnerabilities]
    prompt = "今日掲載されたCVE一覧だけを根拠に、次の3セクションで短く総括してください: ## 今日のまとめ / ## 優先して確認すべき3〜5件 / ## 開発者向けコメント\n" + json.dumps(rows, ensure_ascii=False)
    content = model_text([{"role": "system", "content": "あなたは開発者向け脆弱性ダイジェストを作るセキュリティアナリストです。"}, {"role": "user", "content": prompt}], config, 900)
    if content:
        return content, True
    top_items = sorted(vulnerabilities, key=lambda vuln: (-int(vuln.kev), vuln.severity != "CRITICAL", tech_priority(vuln), -vuln.score))[:5]
    lines = ["## 今日のまとめ", "", f"対象CVEは{len(vulnerabilities)}件です。Geminiの総括生成に失敗したため、スコア順の機械的な要約を表示します。", "", "## 優先して確認すべき3〜5件", ""]
    lines.extend(f"- {vuln.cve_id}: {vuln.title}" for vuln in top_items)
    lines.extend(["", "## 開発者向けコメント", "", "使用技術に該当するもの、KEV掲載、Criticalを先に確認してください。"])
    return "\n".join(lines), False


def render_card(vuln: Vulnerability) -> list[str]:
    cvss_text = "-" if vuln.cvss is None else f"{vuln.cvss:.1f}"
    refs = vuln.references or [f"https://nvd.nist.gov/vuln/detail/{vuln.cve_id}"]
    lines = [
        f"### [{vuln.cve_id}]({refs[0]})", "",
        f"> **{vuln.category.title()}** / **{vuln.severity}** / CVSS: **{cvss_text}** / KEV: **{'yes' if vuln.kev else 'no'}**", "",
        f"- タイトル: {vuln.title}",
        f"- 関連キーワード: {', '.join(vuln.matched_keywords) if vuln.matched_keywords else '-'}",
        f"- 影響製品: {', '.join(vuln.affected_products) if vuln.affected_products else '-'}",
        f"- 公開日: {vuln.published_at or '-'}",
        f"- 更新日: {vuln.updated_at or '-'}",
        f"- 出典: {vuln.source}", "", "#### Gemini要約", "", vuln.ai_summary or fallback_ai_summary(vuln), "", "#### References",
    ]
    lines.extend(f"- {ref}" for ref in refs[:5])
    lines.append("")
    return lines


def render_category_summary(vulnerabilities: list[Vulnerability], now: datetime, errors: list[str], category: str, used_model: bool) -> str:
    date_text = now.strftime("%Y-%m-%d")
    label = "Frontend" if category == "frontend" else "Backend"
    items = sorted([vuln for vuln in vulnerabilities if vuln.category == category], key=lambda vuln: (tech_priority(vuln), -int(vuln.kev), vuln.severity != "CRITICAL", -vuln.score, vuln.cve_id))
    lines = [f"# {label} CVE Summary ({date_text})", "", "## Overview", "", f"- 取得日時: {now.strftime('%Y-%m-%d %H:%M:%S JST')}", "- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ", f"- 掲載件数: {len(items)}", f"- Critical: {sum(1 for vuln in items if vuln.severity == 'CRITICAL')}", f"- High: {sum(1 for vuln in items if vuln.severity == 'HIGH')}", f"- KEV掲載: {sum(1 for vuln in items if vuln.kev)}", f"- 日本語AI要約: {'Gemini' if used_model else 'fallback'}", ""]
    if errors:
        lines.extend(["## 取得エラー", ""] + [f"- {error}" for error in errors] + [""])
    if not items:
        lines.extend(["## 結果", "", f"条件に一致する{label}関連の新規脆弱性はありませんでした。", ""])
        return "\n".join(lines)
    lines.extend(["## CVEs", ""])
    for vuln in items:
        lines.extend(render_card(vuln))
    return "\n".join(lines)


def render_today(vulnerabilities: list[Vulnerability], now: datetime, ai_overview: str, used_model: bool) -> str:
    date_text = now.strftime("%Y-%m-%d")
    docs_dir = f"docs/{date_text}"
    frontend_count = sum(1 for vuln in vulnerabilities if vuln.category == "frontend")
    backend_count = sum(1 for vuln in vulnerabilities if vuln.category == "backend")
    critical_count = sum(1 for vuln in vulnerabilities if vuln.severity == "CRITICAL")
    high_count = sum(1 for vuln in vulnerabilities if vuln.severity == "HIGH")
    kev_count = sum(1 for vuln in vulnerabilities if vuln.kev)
    top_items = sorted(vulnerabilities, key=lambda vuln: (-int(vuln.kev), vuln.severity != "CRITICAL", tech_priority(vuln), -vuln.score, vuln.cve_id))[:5]
    lines = [f"# CVE Digest Dashboard ({date_text})", "", "## Overview", "", f"- Total: {len(vulnerabilities)}", f"- Critical件数: {critical_count}", f"- High件数: {high_count}", f"- KEV件数: {kev_count}", f"- Frontend件数: {frontend_count}", f"- Backend件数: {backend_count}", f"- Gemini総括: {'Gemini' if used_model else 'fallback'}", "", "## Links", "", f"- [Frontend Summary]({docs_dir}/frontend-summary.md)", f"- [Backend Summary]({docs_dir}/backend-summary.md)", "", "## Today TOP5", ""]
    if top_items:
        lines.extend(f"- [{vuln.cve_id}]({vuln.references[0] if vuln.references else f'https://nvd.nist.gov/vuln/detail/{vuln.cve_id}'}) {vuln.title} / {vuln.severity} / {vuln.category}" for vuln in top_items)
    else:
        lines.append("- 条件に一致する今日公開の新規脆弱性はありません。")
    lines.extend(["", "## Geminiによる今日の総括", "", ai_overview, ""])
    return "\n".join(lines)


def main() -> int:
    now = datetime.now(JST)
    config = load_json(CONFIG_PATH, {})
    history = prune_history(load_json(HISTORY_PATH, {"seen": {}}), now, int(config.get("history_retention_days", 120)))
    vulnerabilities, errors = collect_vulnerabilities(config, now)
    new_vulnerabilities = [vuln for vuln in vulnerabilities if vuln.cve_id not in history.get("seen", {})]
    new_vulnerabilities, used_cve_model = add_ai_summaries(new_vulnerabilities, config)
    ai_overview, used_today_model = build_today_ai_overview(new_vulnerabilities, config)

    output_dir = OUTPUT_ROOT / now.strftime("%Y-%m-%d")
    output_dir.mkdir(parents=True, exist_ok=True)
    outputs = {
        "frontend-summary.md": render_category_summary(new_vulnerabilities, now, errors, "frontend", used_cve_model),
        "backend-summary.md": render_category_summary(new_vulnerabilities, now, errors, "backend", used_cve_model),
    }
    for filename, content in outputs.items():
        output_path = output_dir / filename
        output_path.write_text(content, encoding="utf-8")
        print(f"created: {output_path.relative_to(ROOT_DIR)}")

    today_path = ROOT_DIR / "today.md"
    today_path.write_text(render_today(new_vulnerabilities, now, ai_overview, used_today_model), encoding="utf-8")
    print(f"created: {today_path.relative_to(ROOT_DIR)}")

    write_json(HISTORY_PATH, update_history(history, new_vulnerabilities, now))
    if errors:
        print("warning: one or more sources failed, but markdown files were generated", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

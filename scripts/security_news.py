from __future__ import annotations

import html
import json
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, replace
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import cve_digest as digest

JST = timezone(timedelta(hours=9), "JST")
ROOT_DIR = SCRIPT_DIR.parent
OUTPUT_ROOT = ROOT_DIR / "docs"
LATEST_OUTPUT = ROOT_DIR / "security-news.md"
TODAY_OUTPUT = ROOT_DIR / "today.md"
USER_AGENT = "cve-digest-security-news/1.0"
MAX_ITEMS = 10
DASHBOARD_ITEMS = 5
NEWS_SECTION_START = "<!-- SECURITY_NEWS_START -->"
NEWS_SECTION_END = "<!-- SECURITY_NEWS_END -->"

FEEDS = [
    ("SecurityWeek", "https://www.securityweek.com/feed/"),
    ("Krebs on Security", "https://krebsonsecurity.com/feed/"),
]


@dataclass(frozen=True)
class NewsItem:
    source: str
    title: str
    url: str
    published_at: datetime | None
    description: str
    summary_ja: str | None = None


def clean_html(value: str | None) -> str:
    if not value:
        return ""
    text = re.sub(r"<[^>]+>", " ", html.unescape(value))
    return " ".join(text.split())


def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        parsed = parsedate_to_datetime(value)
    except (TypeError, ValueError, OverflowError):
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed


def child_text(element: ET.Element, names: tuple[str, ...]) -> str:
    for child in element.iter():
        local_name = child.tag.rsplit("}", 1)[-1].lower()
        if local_name in names and child.text:
            return child.text.strip()
    return ""


def item_link(element: ET.Element) -> str:
    for child in element.iter():
        if child.tag.rsplit("}", 1)[-1].lower() != "link":
            continue
        href = child.attrib.get("href")
        if href:
            return href.strip()
        if child.text:
            return child.text.strip()
    return ""


def fetch_feed(source: str, url: str) -> list[NewsItem]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml",
        },
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        root = ET.fromstring(response.read())

    entries = [
        element
        for element in root.iter()
        if element.tag.rsplit("}", 1)[-1].lower() in {"item", "entry"}
    ]
    results: list[NewsItem] = []
    for entry in entries:
        title = clean_html(child_text(entry, ("title",)))
        link = item_link(entry)
        description = clean_html(child_text(entry, ("description", "summary", "content", "encoded")))
        published = child_text(entry, ("pubdate", "published", "updated", "date"))
        if not title or not link:
            continue
        results.append(
            NewsItem(
                source=source,
                title=title,
                url=link,
                published_at=parse_date(published),
                description=description,
            )
        )
    return results


def parse_json_object(content: str) -> dict[str, Any] | None:
    text = content.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        lines = lines[1:] if lines else lines
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def add_ai_summaries(items: list[NewsItem], config: dict[str, Any]) -> list[NewsItem]:
    if not items:
        return items

    rows = [
        {
            "id": str(index),
            "source": item.source,
            "title": item.title,
            "description": digest.compact_text(item.description, 700),
        }
        for index, item in enumerate(items)
    ]
    prompt = "\n".join(
        [
            "次のセキュリティニュースを日本語で要約してください。",
            "JSONオブジェクトだけを返してください。キーは入力のid、値は2文以内の日本語要約にしてください。",
            "記事に書かれていない事実は追加せず、不明点は断定しないでください。",
            json.dumps(rows, ensure_ascii=False),
        ]
    )
    content = digest.model_text(
        [
            {
                "role": "system",
                "content": "あなたは開発者向けのセキュリティニュース編集者です。",
            },
            {"role": "user", "content": prompt},
        ],
        config,
        max(1200, len(items) * 180),
    )
    parsed = parse_json_object(content) if content else None
    if not parsed:
        return items

    enriched: list[NewsItem] = []
    for index, item in enumerate(items):
        summary = parsed.get(str(index))
        normalized = clean_html(str(summary)) if isinstance(summary, str) else ""
        enriched.append(replace(item, summary_ja=normalized or None))
    return enriched


def fallback_summary(item: NewsItem) -> str:
    if item.description:
        return digest.compact_text(item.description, 280)
    return "記事の詳細はリンク先を確認してください。"


def render_markdown(items: list[NewsItem], generated_at: datetime) -> str:
    lines = [
        "# セキュリティニュース",
        "",
        f"更新日時: {generated_at.astimezone(JST).strftime('%Y-%m-%d %H:%M:%S JST')}",
        "",
        "SecurityWeek と Krebs on Security のRSSから、JST基準で本日公開されたセキュリティ関連記事を収集しています。",
        "",
    ]
    if not items:
        lines.extend(["本日公開されたニュースはありません。", ""])
        return "\n".join(lines)

    for item in items:
        published = item.published_at.astimezone(JST).strftime("%Y-%m-%d %H:%M JST")
        lines.extend(
            [
                f"## [{item.title}]({item.url})",
                "",
                f"- メディア: {item.source}",
                f"- 公開日時: {published}",
                f"- 要約: {item.summary_ja or fallback_summary(item)}",
                "",
            ]
        )
    return "\n".join(lines)


def render_dashboard_section(items: list[NewsItem]) -> str:
    lines = [
        NEWS_SECTION_START,
        "## セキュリティニュース",
        "",
    ]
    if not items:
        lines.append("本日公開されたニュースはありません。")
    else:
        for item in items[:DASHBOARD_ITEMS]:
            lines.append(f"- [{item.title}]({item.url}) — {item.source}")
        lines.extend(["", "- [セキュリティニュースをすべて見る](security-news.md)"])
    lines.extend(["", NEWS_SECTION_END])
    return "\n".join(lines)


def update_today_dashboard(items: list[NewsItem]) -> None:
    section = render_dashboard_section(items)
    current = TODAY_OUTPUT.read_text(encoding="utf-8") if TODAY_OUTPUT.exists() else "# CVE Digest Dashboard\n"
    pattern = re.compile(
        rf"{re.escape(NEWS_SECTION_START)}.*?{re.escape(NEWS_SECTION_END)}",
        flags=re.DOTALL,
    )
    if pattern.search(current):
        updated = pattern.sub(section, current)
    else:
        updated = current.rstrip() + "\n\n" + section + "\n"
    TODAY_OUTPUT.write_text(updated, encoding="utf-8")


def main() -> int:
    now = datetime.now(timezone.utc)
    today_jst = now.astimezone(JST).date()
    config = digest.load_json(digest.CONFIG_PATH, {})
    collected: list[NewsItem] = []

    for source, url in FEEDS:
        try:
            items = fetch_feed(source, url)
            print(f"Fetched {len(items)} articles from {source}")
            collected.extend(items)
        except (urllib.error.URLError, TimeoutError, OSError, ET.ParseError, ValueError) as error:
            print(f"Failed to fetch {source}: {error}", file=sys.stderr)

    deduplicated: dict[str, NewsItem] = {}
    for item in collected:
        if item.published_at is None or item.published_at.astimezone(JST).date() != today_jst:
            continue
        key = item.url.split("#", 1)[0].rstrip("/") or item.title.lower()
        deduplicated.setdefault(key, item)

    items = sorted(
        deduplicated.values(),
        key=lambda item: item.published_at or datetime.min.replace(tzinfo=timezone.utc),
        reverse=True,
    )[:MAX_ITEMS]
    items = add_ai_summaries(items, config)

    markdown = render_markdown(items, now)
    archive_path = OUTPUT_ROOT / now.astimezone(JST).strftime("%Y-%m-%d") / "security-news.md"
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    archive_path.write_text(markdown, encoding="utf-8")
    LATEST_OUTPUT.write_text(markdown, encoding="utf-8")
    update_today_dashboard(items)

    print(f"Wrote {LATEST_OUTPUT.relative_to(ROOT_DIR)}")
    print(f"Wrote {archive_path.relative_to(ROOT_DIR)}")
    print(f"Updated {TODAY_OUTPUT.relative_to(ROOT_DIR)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

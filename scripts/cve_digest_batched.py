from __future__ import annotations

import json
import sys
from dataclasses import replace
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import cve_digest as digest


def parse_json_object(content: str) -> dict[str, Any] | None:
    text = content.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        text = "\n".join(lines).strip()

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def format_summary(item: dict[str, Any]) -> str | None:
    summary = str(item.get("summary") or "").strip()
    impact = str(item.get("impact") or "").strip()
    recommendation = str(item.get("recommendation") or "").strip()
    if not summary or not impact or not recommendation:
        return None
    return "\n".join(
        [
            f"- 日本語要約: {summary}",
            f"- 影響: {impact}",
            f"- 推奨対応: {recommendation}",
        ]
    )


def add_ai_summaries_batched(
    vulnerabilities: list[digest.Vulnerability],
    config: dict[str, Any],
) -> tuple[list[digest.Vulnerability], bool]:
    if not vulnerabilities:
        return [], False

    models = digest.model_config(config)
    batch_size = max(1, int(models.get("batch_size", 10)))
    summaries: dict[str, str] = {}

    for start in range(0, len(vulnerabilities), batch_size):
        batch = vulnerabilities[start : start + batch_size]
        rows = [
            {
                "cve_id": vuln.cve_id,
                "title": vuln.title,
                "severity": vuln.severity,
                "cvss": vuln.cvss,
                "kev": vuln.kev,
                "products": vuln.affected_products,
                "description": digest.compact_text(vuln.description, 900),
            }
            for vuln in batch
        ]
        prompt = "\n".join(
            [
                "次のCVEを日本語で要約してください。",
                "JSONオブジェクトだけを返し、キーはCVE ID、値は summary・impact・recommendation を持つオブジェクトにしてください。",
                "各項目は簡潔にし、不明点は断定しないでください。入力にないCVEは追加しないでください。",
                json.dumps(rows, ensure_ascii=False),
            ]
        )
        content = digest.model_text(
            [
                {
                    "role": "system",
                    "content": "あなたは開発者向けCVE要約を作るセキュリティアナリストです。",
                },
                {"role": "user", "content": prompt},
            ],
            config,
            max(1200, len(batch) * 220),
        )
        parsed = parse_json_object(content) if content else None
        if not parsed:
            continue

        expected_ids = {vuln.cve_id for vuln in batch}
        for cve_id, item in parsed.items():
            if cve_id not in expected_ids or not isinstance(item, dict):
                continue
            formatted = format_summary(item)
            if formatted:
                summaries[cve_id] = formatted

    enriched = [
        replace(
            vuln,
            ai_summary=summaries.get(vuln.cve_id) or digest.fallback_ai_summary(vuln),
        )
        for vuln in vulnerabilities
    ]
    return enriched, bool(summaries)


def main() -> int:
    digest.add_ai_summaries = add_ai_summaries_batched
    return digest.main()


if __name__ == "__main__":
    raise SystemExit(main())

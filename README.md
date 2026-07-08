# CVE Digest

CVE Digest は、NVD と CISA KEV から脆弱性情報を収集し、関心技術に関連するものだけを `summary.md` にまとめる GitHub Actions ベースの自動化ツールです。

## 概要

毎日 GitHub Actions で実行し、以下の条件に該当する脆弱性を抽出します。

- `config/cve-digest.json` の `watch_keywords` に一致する
- CVSS が設定値以上
- CISA KEV に掲載されている

出力は日付ごとの `summary.md` のみです。

## ディレクトリ構成

```txt
.
├── config/
│   └── cve-digest.json
├── scripts/
│   └── cve_digest.py
├── docs/
│   └── YYYY-MM-DD/
│       └── summary.md
├── data/
│   └── history.json
└── .github/
    └── workflows/
        └── cve-digest.yml
```

## ローカル実行

```bash
python scripts/cve_digest.py
```

## GitHub Actions

毎日 JST 07:10 に実行します。手動実行にも対応しています。

```yaml
workflow_dispatch:
schedule:
  - cron: "10 22 * * *"
```

## 設定

監視対象の技術や最小CVSSは `config/cve-digest.json` で変更します。

```json
{
  "watch_keywords": ["python", "django", "fastapi", "react", "docker"],
  "min_cvss": 7.0,
  "lookback_days": 2,
  "max_items": 30
}
```

## 出力例

```md
# CVE Digest Summary (2026-07-08)

## Critical

### CVE-XXXX-YYYY
- 重要度: CRITICAL
- CVSS: 9.8
- KEV掲載: yes
- 関連キーワード: django
- 公開日: 2026-07-08
- 概要: ...
- 参照: https://...
```

# CVE Digest

CVE Digest は、NVD と CISA KEV から脆弱性情報を収集し、開発で使う技術に関連するものを Frontend / Backend に分けて Markdown へ出力する GitHub Actions ベースの自動化ツールです。

## セキュリティーニュース

[![LED Board](https://led-borad-svg.vercel.app/api/led-board?text=%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E3%83%BC%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E9%80%9F%E5%A0%B1&duration=11)](https://github.com/yabuki-shodai/cve-digest/blob/main/security-news.md)

## 概要

毎日 GitHub Actions で実行し、以下の条件に該当する脆弱性を抽出します。

- `config/cve-digest.json` の `watch_keywords` に一致する
- CVSS が設定値以上
- CISA KEV に掲載されている
- `frontend_keywords` / `backend_keywords` に一致する

GitHub Models が利用できる場合、各CVEに以下を追加します。

- 日本語要約
- 影響
- 推奨対応

GitHub Models が失敗した場合は、元の description を使った fallback 要約を出力します。

## ディレクトリ構成

```txt
.
├── today.md
├── config/
│   └── cve-digest.json
├── scripts/
│   └── cve_digest.py
├── docs/
│   └── YYYY-MM-DD/
│       ├── frontend-summary.md
│       └── backend-summary.md
├── data/
│   └── history.json
└── .github/
    └── workflows/
        └── cve-digest.yml
```

## 出力

`today.md` はダッシュボードです。

- Overview
- Today TOP5
- Frontend Summary へのリンク
- Backend Summary へのリンク
- GitHub Models による今日の総括
- Critical件数
- KEV件数
- Frontend件数
- Backend件数

日付別の詳細は以下に出力します。

- `docs/YYYY-MM-DD/frontend-summary.md`
- `docs/YYYY-MM-DD/backend-summary.md`

`summary.md` は廃止済みです。

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
  "frontend_keywords": ["typescript", "next.js", "react", "npm"],
  "backend_keywords": ["django", "fastapi", "go", "aws"],
  "min_cvss": 7.0,
  "max_items": 30,
  "github_models": {
    "enabled": true,
    "endpoint": "https://models.github.ai/inference/chat/completions",
    "model": "openai/gpt-4.1-mini"
  }
}
```
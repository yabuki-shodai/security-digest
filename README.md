# Security Digest

> Daily security digest powered by GitHub Actions and AI.

[![LED Board](https://led-borad-svg.vercel.app/api/led-board?text=%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3%E3%83%BC%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%B9%E9%80%9F%E5%A0%B1&duration=11)](https://github.com/yabuki-shodai/security-digest/blob/main/security-news.md)

Security Digest は、CVE・CISA KEV・セキュリティーニュースを毎日収集し、日本語で要約・重要度判定を行う OSS プロジェクトです。

## ✨ Features

### 🛡️ Vulnerability Digest

毎日公開される脆弱性情報を収集し、日本語で要約します。

#### Sources

- NVD (National Vulnerability Database)
- CISA Known Exploited Vulnerabilities (KEV)

#### Output

- 日本語要約
- CVSS
- CWE
- 影響製品
- CISA KEV情報
- フロントエンド・バックエンド別の分類

---

### 📰 Security News

当日公開された主要なセキュリティーニュースを収集します。

#### Sources

- SecurityWeek
- Krebs on Security
- BleepingComputer
- The Record
- Dark Reading

#### Output

- 日本語要約
- HIGH / MEDIUM / LOW の重要度
- 今日の総括

---

## 📋 Dashboard

最新のダイジェスト

- 📊 `today.md`

---

## 📁 Outputs

```text
today.md

security-news.md

docs/
└── YYYY-MM-DD/
    ├── frontend-summary.md
    ├── backend-summary.md
    └── security-news.md
```

---

## ⚙️ GitHub Actions

毎日自動で実行されます。

| Workflow | Description |
|----------|-------------|
| CVE Digest | CVE・CISA KEVの収集・要約 |
| Security News | セキュリティーニュースの収集・要約 |

---

## ⚙️ Configuration

監視設定は以下で変更できます。

```text
config/cve-digest.json
```

設定例

- 監視キーワード
- CVSS閾値
- AI要約の有効・無効

---

## 🤖 AI

GitHub Models を利用して以下を生成します。

- 日本語要約
- 重要度判定
- 今日の総括

GitHub Models が利用できない場合でも、フォールバック処理によりダイジェストを生成します。

# CVE Digest Dashboard (2026-07-24)

## Overview

- Total: 5
- Critical件数: 2
- High件数: 2
- KEV件数: 0
- Frontend件数: 5
- Backend件数: 0
- GitHub Models総括: GitHub Models

## Links

- [Frontend Summary](docs/2026-07-24/frontend-summary.md)
- [Backend Summary](docs/2026-07-24/backend-summary.md)

## Today TOP5

- [CVE-2026-28698](https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-04) CVE-2026-28698 / CRITICAL / frontend
- [CVE-2026-42933](https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-04) CVE-2026-42933 / CRITICAL / frontend
- [CVE-2026-40430](https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-04) CVE-2026-40430 / HIGH / frontend
- [CVE-2026-50044](https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-04) CVE-2026-50044 / HIGH / frontend
- [CVE-2026-44955](https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-04) CVE-2026-44955 / MEDIUM / frontend

## GitHub Modelsによる今日の総括

## 今日のまとめ
本日報告された脆弱性はすべてPronetiqs IntraVUE 3.2.1a14以前のバージョンに集中しており、主にフロントエンド（Vue.js）関連の問題です。重大度はクリティカルからミディアムまで幅広く、特に認証情報の漏洩や不適切なアクセス制御に関わるものが多く見られます。

## 優先して確認すべき3〜5件
1. CVE-2026-42933（CRITICAL, CVSS 10.0）: アクティブプロキシを悪用しOTセグメンテーションを回避される恐れ。
2. CVE-2026-28698（CRITICAL, CVSS 9.2）: 未承認の制御領域にシステム情報が漏洩し、ホストや共有ファイルシステムが露出。
3. CVE-2026-40430（HIGH, CVSS 8.7）: API経由でパスワードが平文保存されている問題。
4. CVE-2026-50044（HIGH, CVSS 7.6）: 弱い暗号化により管理者資格情報が盗まれるリスク。

## 開発者向けコメント
Pronetiqs IntraVUEの旧バージョンを使用している場合は、速やかに最新バージョンへのアップデートを推奨します。特に認証情報の管理やアクセス制御の強化が必要です。パスワードの平文保存や弱いハッシュ利用は直ちに見直し、APIのセキュリティ設計も再検討してください。OTネットワークのセグメンテーション回避を許すプロキシ設定も要注意です。

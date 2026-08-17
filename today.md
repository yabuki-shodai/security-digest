# CVE Digest Dashboard (2026-08-17)

## Overview

- Total: 30
- Critical件数: 22
- High件数: 5
- KEV件数: 0
- Frontend件数: 0
- Backend件数: 30
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-17/frontend-summary.md)
- [Backend Summary](docs/2026-08-17/backend-summary.md)

## Today TOP5

- [CVE-2026-74798](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-43jx-gxq4-jpjc) CVE-2026-74798 / CRITICAL / backend
- [CVE-2026-15623](https://docs.cloud.google.com/chronicle/docs/soar/release-notes#May_23_2026) CVE-2026-15623 / CRITICAL / backend
- [CVE-2026-19959](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWanTcpipSetup-34b53a41781f8047b36bd11dbcaa84dc?source=copy_link) CVE-2026-19959 / CRITICAL / backend
- [CVE-2026-19961](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWlSiteSurvey-34b53a41781f804fb328d87416095401?source=copy_link) CVE-2026-19961 / CRITICAL / backend
- [CVE-2026-74799](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-9cqq-p2hw-mj3f) CVE-2026-74799 / CRITICAL / backend

## Geminiによる今日の総括

自前サンドボックスや暗号実装の自作は抜け道（`__subclasses__` や環境変数、フォールバック処理）が生じやすいため、厳格なテストと安全な標準ライブラリ/検証済みパッケージの利用が必須。
- **MCP/AIコンポーネントの急増に伴うセキュリティ**: LLM/MCP連携ツールの導入が進む中、入力パラメーターの検証不足によるコード注入やSSRFが散見

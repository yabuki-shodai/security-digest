# CVE Digest Dashboard (2026-07-28)

## Overview

- Total: 30
- Critical件数: 4
- High件数: 10
- KEV件数: 1
- Frontend件数: 16
- Backend件数: 14
- GitHub Models総括: GitHub Models

## Links

- [Frontend Summary](docs/2026-07-28/frontend-summary.md)
- [Backend Summary](docs/2026-07-28/backend-summary.md)

## Today TOP5

- [CVE-2026-16812](https://www.arista.com/en/support/advisories-notices/security-advisory/24364-security-advisory-0144) CVE-2026-16812: Arista VeloCloud Orchestrator On-Prem OS Command Injection Vulnerability / CRITICAL / backend
- [CVE-2026-55953](https://cna.erlef.org/cves/CVE-2026-55953.html) CVE-2026-55953 / CRITICAL / backend
- [CVE-2025-50455](https://github.com/threatlance-org/security-advisories/blob/main/CVE-2025-50455/advisory.md) CVE-2025-50455 / CRITICAL / backend
- [CVE-2026-55579](https://github.com/pheditor/pheditor/releases/tag/2.0.6) CVE-2026-55579 / CRITICAL / backend
- [CVE-2026-64642](https://github.com/vercel/next.js/commit/6bf4df14508ad6c0cd46af50c6051ee42f2d9151) CVE-2026-64642 / HIGH / frontend

## GitHub Modelsによる今日の総括

## 今日のまとめ
本日公開された脆弱性は、特にNext.jsを中心としたフロントエンドのReactフレームワーク関連と、Go言語を用いたバックエンドシステムに多く集中しています。Next.jsでは複数の高リスクなサーバーサイドリクエストフォージェリ（SSRF）や認証バイパス、リソース消費問題が報告されており、バージョン16.2.11で修正されています。バックエンドでは、Erlang/OTPのTLS処理の脆弱性やSQLインジェクション、認証バイパスなどが目立ちます。全体的に認証回避やリモートコード実行、クロスサイトスクリプティング（XSS）など、重大な影響を及ぼす問題が多く含まれています。

## 優先して確認すべき3〜5件
1. **CVE-2026-16812 (CRITICAL, CVSS 10.0)**  
   Arista VeloCloud OrchestratorのOSコマンドインジェクション。リモートからの完全な制御を許すため、最優先で対応が必要。

2. **CVE-2026-55579 (CRITICAL, CVSS 9.8)**  
   Pheditorのハードコードされた管理者パスワードによるリモートコード実行。初期設定のまま運用している場合は即時対策必須。

3. **CVE-2025-50455 (CRITICAL, CVSS 9.1)**  
   EasyAppointmentsのSQLインジェクション。MySQL環境によってはリモートコード実行に繋がるため注意。

4. **CVE-2026-64642 / CVE-2026-64645 / CVE-2026-64649 (HIGH, CVSS 8.3)**  
   Next.jsの複数の認証バイパスおよびSSRF脆弱性。対象バージョンを使用している場合は16.2.11へのアップデートが必須。

5. **CVE-2026-59239 (HIGH, CVSS 8.6)**  
   Roskus Prospero Flow CRMのストアドXSS。管理者権限の乗っ取りに繋がるため、早急な修正が望ましい。

## 開発者向けコメント
Next.js関連の脆弱性は、App RouterやServer Actionsを利用した最新機能に起因するものが多く、特に外部ホストへのリクエスト制御不備や認証バイパスが目立ちます。これらはサーバーサイドリクエストフォージェリ（SSRF）や認証回避を招き、重大なセキュリティリスクとなるため、必ず最新の16.2.11以上にアップデートしてください。また、バックエンドではTLSハンドシェイクの不備やSQLインジェクション、ハードコードされたパスワードなど基本的なセキュリティ対策の見直しが必要です。クロスサイトスクリプティング（XSS）も多く報告されているため、入力値の適切なサニタイズとエスケープを徹底してください。今回の脆弱性は認証やアクセス制御の甘さに起因するものが多いため、権限管理の強化も併せて推奨します。

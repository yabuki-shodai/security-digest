# CVE Digest Dashboard (2026-09-10)

## Overview

- Total: 30
- Critical件数: 6
- High件数: 14
- KEV件数: 0
- Frontend件数: 7
- Backend件数: 22
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-10/frontend-summary.md)
- [Backend Summary](docs/2026-09-10/backend-summary.md)

## Today TOP5

- [CVE-2026-67401](https://support.cpanel.net/hc/en-us/articles/43187903921559-Security-CVE-2026-67401-SQL-Injection-Vulnerability-in-cPanel-s-EmailTrack-Functionality-September-8-2026) CVE-2026-67401 / CRITICAL / security
- [CVE-2026-87911](https://aws.amazon.com/security/security-bulletins/2026-104-aws/) CVE-2026-87911 / CRITICAL / backend
- [CVE-2026-54694](https://github.com/NationalSecurityAgency/skills-service/security/advisories/GHSA-hqfg-c8wf-w2g8) CVE-2026-54694 / CRITICAL / frontend
- [CVE-2026-47156](https://github.com/mantisbt/mantisbt/commit/e3571c319b1721b41b0dc4b5b5203cbdcbe0c2ee) CVE-2026-47156 / CRITICAL / backend
- [CVE-2026-67403](https://helpcenter.sara.sage.com/hc/en-us/articles/52106283946651-June-R2-Release-2026) CVE-2026-67403 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ
本日掲載された脆弱性では、cPanelにおけるroot権限奪取が可能なRCEや、MCP（Model Context Protocol）サーバーの読み取り専用制限をバイパスするOSコマンド注入、ハードコードされた暗号鍵によるセッション捏造など、重大度の高い脆弱性が複数報告されています。また、フロントエンドにおけるVueの`v-html`悪用や不適切なクライアントサイドでのエスケープ解除処理に起因するXSS、さらにOAuth/SSRF関連の脆弱性も目立ちます。

## 優先して確認すべき3〜5件

1. **CVE-2026-67401 (CVSS 9.9 / CRITICAL)**
   - **概要:** cPanelのEmailTrackコンポーネントにおけるSQLインジェクション脆弱性。メール有効アカウントからroot権限でのリモートコード実行（RCE）が可能です。
2. **CVE-2026-87929 (CVSS 9.8 / CRITICAL)**
   - **概要:** MaxSite CMSにハードコードされたセッション暗号化キーが存在。未認証の第三者が管理者セッションクッキー（HMAC-SHA1）を捏造して管理者権限を奪取できます。
3. **CVE-2026-87911 (CVSS 9.6 / CRITICAL)**
   - **概要:** Amazon awslabsの`postgres-mcp-server`におけるSQL検証の不備。デフォルトの読み取り専用モードであっても、`COPY ... TO PROGRAM`文を含んだ入力を処理させることでホスト上でOSコマンドが実行可能です。
4. **CVE-2026-47156 (CVSS 9.3 / CRITICAL)**
   - **概要:** MantisBTのSOAP API（`mci_check_login`）における認証バイパス。有効な`cookie_string`を1つ把握できれば、パスワードなしで任意のユーザー（管理者含む）として認証可能です。
5. **CVE-2026-54694 (CVSS 9.6 / CRITICAL)**
   - **概要:** SkillTreeにおけるエスケープなしの文字列結合とVueの`v-html`（`innerHTML`設定）の組み合わせによる攻撃チェーン。任意のスクリプト実行につながる重大なXSSが発生します。

## 開発者向けコメント

- **AI/LLM連携ツール（MCPサーバー）の安全策:** MCPサーバー等で「アプリ側でのSQL構文解析による読み取り専用化」に依存すると、コメント挿入や特定文脈（`COPY TO PROGRAM`等）でバイパスされるリスクが生じます。アプリ側のフィルタだけでなく、DBユーザー権限自体を読み取り専用（`SELECT`のみ許可）に絞り込む多層防御を行ってください。
- **DOMレンダー時の危険な指令の回避:** Vueの`v-html`やjQueryでの`html().text()`によるデコード・注入は、依然として深刻なXSSの温床になっています。生のHTMLレンダリングを避け、テキストバインディング（`v-text`や標準のテキストノード展開）を徹底してください。
- **暗号鍵の管理と認証実装の再点検:** デフォルトで共通の暗号化キーを出荷する実装（MaxSite CMS）や、クッキー値の検証で十分な身元確認を行わないロジック（MantisBT）は一打でシステム全体の奪取につながります。秘密鍵のユニーク生成と安全なセッション検証ロジックを実装してください。

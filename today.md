# CVE Digest Dashboard (2026-08-26)

## Overview

- Total: 30
- Critical件数: 6
- High件数: 14
- KEV件数: 0
- Frontend件数: 8
- Backend件数: 22
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-26/frontend-summary.md)
- [Backend Summary](docs/2026-08-26/backend-summary.md)

## Today TOP5

- [CVE-2026-55546](https://github.com/QWED-AI/qwed-mcp/commit/362e61892052e250c56cb1ee852024d6f98c467b) CVE-2026-55546 / CRITICAL / backend
- [CVE-2026-45018](https://github.com/Chainlit/chainlit/blob/2.12.0/docs/security-advisory-2026-mcp.md#spl-2026-001--command-injection-via-mcp-stdio) CVE-2026-45018 / CRITICAL / backend
- [CVE-2026-78379](https://aws.amazon.com/security/security-bulletins/2026-089-aws/) CVE-2026-78379 / CRITICAL / backend
- [CVE-2026-79782](https://github.com/rclone/rclone/security/advisories/GHSA-gx4c-2hqx-cw2r) CVE-2026-79782 / CRITICAL / backend
- [CVE-2026-79787](https://github.com/Alluxio/alluxio) CVE-2026-79787 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ
本日掲載された脆弱性では、AI/LLMフレームワークやMCP（Model Context Protocol）関連コンポーネントにおける深刻な脆弱性が集中しています。特に、未認証でアクセス可能なMCPエンドポイントを経由した任意コマンド実行、式評価処理（SymPyなど）での安全でない `eval()` 実行によるRCE、プロンプトインジェクションによる同意ゲートの回避、AWS認証情報の漏洩やなりすましなど、CVSS 9.0以上のCRITICALな脆弱性が多数含まれています。

## 優先して確認すべき3〜5件
1. **CVE-2026-45018 (Chainlit / CVSS 9.8: CRITICAL)**
   - MCP機能有効時に未認証で利用可能な `POST /mcp` エンドポイントが存在し、検証不足のコマンド実行機能を通じて任意のOSコマンドが実行可能です（2.12.0未満が対象）。
2. **CVE-2026-55546 (QWED-MCP / CVSS 9.8: CRITICAL)**
   - 数式検証エンジンがSymPyの `parse_expr()` を安全な制限（組み込み関数の削除等）なしで呼び出すため、Pythonの `eval()` を通じて任意のコードが実行可能です（0.2.1未満が対象）。
3. **CVE-2026-79787 (Alluxio / CVSS 9.8: CRITICAL)**
   - S3 RESTプロキシのデフォルト設定においてAWS SigV4署名の検証が行われず、攻撃者が未検証の認証ヘッダーを用いて任意ユーザーになりすまし、データの閲覧・変更・削除が可能です。
4. **CVE-2026-78379 (Amazon Strands Agents Tools / CVSS 9.2: CRITICAL)**
   - LLMプロンプトインジェクションにより `python_repl` ツール利用時の人間による同意ゲート（確認処理）をバイパスされ、ホスト上で任意のPythonコードを実行される恐れがあります（0.8.5未満が対象）。
5. **CVE-2026-79782 (rclone / CVSS 9.3: CRITICAL)**
   - S3のリダイレクトにより通信がHTTPSからHTTPに切り替わる際、`X-Amz-Security-Token` ヘッダーが削られず平文通信上でAWS STSセッションキーが漏洩します（1.74.4未満が対象）。

## 開発者向けコメント
LLM連携基盤やMCPサーバーを組み込んでいるシステムにおいて、**「入力の安全でない評価（SymPy/eval）」「不十分なCLI引数検証」「未認証でのツール実行エンドポイントの露出」**が大きな攻撃面となっています。AIエージェントやMCPツールを導入している環境では、エンドポイントの認証設定、実行可能なコマンドの厳密なリスト化、プロンプト経由での制御権奪取への対策を直ちに見直してください。また、S3連携などのクラウドインフラ周りでも認証トークンや署名検証に関する致命的な不備があるため、影響を受けるライブラリの最新版へのアップデートを優先して実施してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

政府インフラに対する大規模なDDoS攻撃や、数万人規模の個人・医療情報が流出するデータ侵害インシデントが発生しています。また、音声AIエージェントを用いたパスコードの奪取や、隠しプロンプトによるAIメール要約の操作など、AI技術を悪用した新たな攻撃手法が顕著になっています。一方で、国際的なサイバー犯罪ネットワークの摘発やAIセキュリティの標準化に向けた取り組みも進められています。

- **HIGH** [AnonyMousKIT PhaaS uses voice AI agents to phish iPhone passcodes](https://www.bleepingcomputer.com/news/security/anonymouskit-phaas-uses-voice-ai-agents-to-phish-iphone-passcodes/) — BleepingComputer
- **HIGH** [Employee benefits platform Paylogix says hackers stole financial and health data](https://therecord.media/paylogix-cyberattack-akira-ransomware) — The Record
- **HIGH** [Massive DDoS attack disrupts Norway’s government digital services](https://www.bleepingcomputer.com/news/security/massive-ddos-attack-disrupts-norways-government-digital-services/) — BleepingComputer
- **MEDIUM** [LACMA data breach last year exposed social security and medical data](https://www.bleepingcomputer.com/news/security/lacma-data-breach-last-year-exposed-social-security-and-medical-data/) — BleepingComputer
- **MEDIUM** [Hackers abuse npm mirrors to host phishing redirect pages](https://www.bleepingcomputer.com/news/security/hackers-abuse-npm-mirrors-to-host-phishing-redirect-pages/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

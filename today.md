# CVE Digest Dashboard (2026-10-17)

## Overview

- Total: 30
- Critical件数: 6
- High件数: 12
- KEV件数: 0
- Frontend件数: 2
- Backend件数: 28
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-17/frontend-summary.md)
- [Backend Summary](docs/2026-10-17/backend-summary.md)

## Today TOP5

- [CVE-2026-111641](https://github.com/fastapiadmin/FastapiAdmin/blob/v3.0/backend/app/api/v1/module_system/auth/controller.py#L173-L251) CVE-2026-111641 / CRITICAL / backend
- [CVE-2026-57169](https://github.com/Finsys/dockhand/commit/efb634701c55f80a8c752df8ae08d88f2c16cce9) CVE-2026-57169 / CRITICAL / backend
- [CVE-2026-111663](https://github.com/chaskiq/chaskiq/blob/2.0.3/app/controllers/graphql_controller.rb#L3-L33) CVE-2026-111663 / CRITICAL / frontend
- [CVE-2026-85748](https://github.com/MariaDB/server/commit/91156c3de58762196605150ab3f756fe952592d1) CVE-2026-85748 / CRITICAL / backend
- [CVE-2026-92262](https://github.com/MariaDB/server/commit/574ba66b2d6c5d71db83d416677876e9b592858e) CVE-2026-92262 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載されたCVEでは、データベース（MariaDB）における複数の深刻なRCE脆弱性や、Webアプリケーション・管理ツール（FastapiAdmin、Dockhand、Chaskiq等）における**認証・認可の不備**（自動ログイン悪用、未認証WebSocket接続、OAuthトークンの検証漏れなど）が目立ちます。また、プロトコル実装ライブラリ（libIEC61850、libp2p-rust等）のメモリ安全性の不備やDoS脆弱性も複数報告されています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-111641 (FastapiAdmin | CVSS 9.8 : CRITICAL)**
   - **概要**: 未保護の自動ログインエンドポイントを悪用し、未認証で管理者トークンを取得して完全な管理権限を奪取できる脆弱性。
2. **CVE-2026-57169 (Dockhand | CVSS 9.6 : CRITICAL)**
   - **概要**: コンテナターミナルのWebSocketエンドポイント（`/api/containers/<id>/exec`）で認証が欠落しており、未認証でターゲットコンテナ内で任意コマンドを実行される恐れ。
3. **MariaDBのRCE脆弱性群 (CVE-2026-85748, CVE-2026-92262, CVE-2026-85746 | CVSS 各 9.9 : CRITICAL)**
   - **概要**: UAF、テーブル名の`#mysql50#`プレフィックスによるパスバイパス、GIS関数（`ST_AsText`）のバッファオーバーフローなど、低権限ユーザーから任意コード実行やデータ強奪につながる重大な脆弱性。
4. **CVE-2026-111663 (Chaskiq | CVSS 9.2 : CRITICAL)**
   - **概要**: GraphQLの `createUrlUpload` ミューテーションを利用したSSRF。未認証の攻撃者にクラウドメタデータなどの内部リソースへアクセスされる危険性。
5. **CVE-2026-111613 (AllData | CVSS 8.7 : HIGH)**
   - **概要**: 未認証のJDBCインジェクション。`allowLoadLocalInfile=true` を含む外部パラメータを指定されることで、ホスト上の任意ファイルが読み取られる危険性。

---

## 開発者向けコメント

- **認証・認可およびトークン検証の徹底**:
  WebSocketエンドポイントのハンドシェイク時の認証チェック漏れ（CVE-2026-57169）や、OAuth連携時の `aud` (Audience) クレームチェック不足（CVE-2026-111639）、ハードコードされたJWT署名鍵（CVE-2026-111642）など、基本構造の欠陥による致命的な脆弱性が多発しています。認証フローの再点検を行ってください。
- **外部パラメータと接続指定の安全化**:
  ユーザー入力からGraphQL経由のURL取得（SSRF）や、JDBC接続文字列のダイレクト指定（任意ファイル読み取り）を許容しないよう、入力のホワイトリスト検証や危険なパラメータ（`allowLoadLocalInfile` 等）のサニタイズを実施してください。
- **データベース・基盤ライブラリの更新**:
  MariaDBを使用している環境では、最新パッチ（10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3.3, 13.0.2等）への更新を速やかに検討してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

エッジデバイスにおけるゼロデイ脆弱性の悪用や、広告表示のみで感染するゼロクリック攻撃によるスパイウェア配信など、高度な攻撃手法が確認されています。また、Magento等の主要システムにおける重大な脆弱性や、人気AIブランドを偽装した攻撃手法の急増が報告されています。さらに、ランサムウェア交渉人の不正関与疑惑や業界内の大型買収といった動向も注目を集めています。

- **HIGH** [BeyondTrust Remote Support Zero-Day Continues Trend of Exploited Edge Bugs](https://www.darkreading.com/endpoint-security/beyondtrust-remote-support-exploited-edge-bugs) — Dark Reading
- **HIGH** [Critical BlockStrap flaw lets hackers run code on Magento servers](https://www.bleepingcomputer.com/news/security/critical-blockstrap-flaw-lets-hackers-run-code-on-magento-servers/) — BleepingComputer
- **HIGH** [Targeted ads installed Candiru spyware in zero-click attacks](https://www.bleepingcomputer.com/news/security/zero-click-attacks-used-targeted-ads-to-deliver-candiru-spyware/) — BleepingComputer
- **MEDIUM** [Fake Claude, ChatGPT Attacks Surge, Putting Developers at Risk](https://www.darkreading.com/application-security/fake-claude-chatgpt-attacks-developers-risk) — Dark Reading
- **MEDIUM** [AI Takes Control of Robotic Arm in 16 Minutes Flat](https://www.darkreading.com/ics-ot-security/ai-takes-control-robotic-arm-16-minutes) — Dark Reading

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

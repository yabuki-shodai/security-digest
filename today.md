# CVE Digest Dashboard (2026-09-09)

## Overview

- Total: 30
- Critical件数: 4
- High件数: 18
- KEV件数: 0
- Frontend件数: 1
- Backend件数: 29
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-09/frontend-summary.md)
- [Backend Summary](docs/2026-09-09/backend-summary.md)

## Today TOP5

- [CVE-2026-82067](https://jira.mongodb.org/browse/SERVER-131229) CVE-2026-82067 / CRITICAL / backend
- [CVE-2026-82533](https://github.com/deepseek-ai/deepseek-harness/commit/3e24087bfaeabe40b58ba2f7b936895b8f93fe27) CVE-2026-82533 / CRITICAL / backend
- [CVE-2026-86729](https://github.com/WWBN/AVideo/security/advisories/GHSA-vvqm-mgc5-hhx3) CVE-2026-86729 / CRITICAL / backend
- [CVE-2026-61516](https://hackwithmike.com/research/advisories/netis/cve-2026-61516) CVE-2026-61516 / CRITICAL / backend
- [CVE-2026-82058](https://jira.mongodb.org/browse/SERVER-130926) CVE-2026-82058 / HIGH / backend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載されたCVEでは、**MongoDB Serverに関する大量の脆弱性報告**（起動時の認証機能無効化、OutOfBoundsメモリ書き込み、リソース枯渇によるDoSなど）が大部分を占めています。また、AI関連ツール（DeepSeek Harness）でのHostヘッダー偽装による認証バイパスや、ネットワーク機器（Netis NX10）、Webアプリケーション（WWBN AVideo、Snipe-IT）における深刻な認証回避・リモートコード実行（RCE）・資格情報漏洩も確認されています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-82533（CVSS 9.6 / CRITICAL）：DeepSeek Harness の認証バイパス**
   - **概要:** HTTPコントロールプレーンAPIが送信元IPではなくクライアントが指定したHostヘッダーのみを検証しているため、ヘッダー偽装により未認証でフルエージェント制御や危険なコマンドの実行が可能になります。
2. **CVE-2026-82067（CVSS 9.2 / CRITICAL）：MongoDB Server の起動時認証無効化**
   - **概要:** 設定検証における大文字・小文字の取り扱い不備により、サーバー起動時に認証サブシステムが無効状態のまま維持されることがあります。ネットワークアクセス可能な未認証攻撃者が管理者操作を実行可能です。
3. **CVE-2026-61516（CVSS 9.8 / CRITICAL）：Netis NX10 の管理者パスワード漏洩**
   - **概要:** Web管理インターフェースの `sysinfo` リクエストにセッション検証がなく、未認証で管理者パスワードを取得・再利用して管理者セッションを確立できてしまいます。
4. **CVE-2026-86729（CVSS 9.1 / CRITICAL）：WWBN AVideo のレート制限なし認証エンドポイント**
   - **概要:** レート制限（`checkRateLimit`）が適用されていないエンドポイント（`get_api_preauthorize`）が露出しており、無制限のブルートフォース攻撃やアカウント存在チェックに悪用される恐れがあります。
5. **CVE-2026-86733（CVSS 8.6 / HIGH）：Snipe-IT のリストア処理におけるRCE**
   - **概要:** アップロードされたバックアップZIP内のSQLを `--binary-mode` オプションなしで `mysql` コマンドラインクライアントにストリーミングするため、`\!` などの特殊コマンドを用いた任意のローカルシェルコマンド実行が可能です。

---

## 開発者向けコメント

* **MongoDB依存関係の更新:** MongoDB Serverでは認証回避・権限昇格からメモリクラッシュ・DoSまで多数の脆弱性が報告されています。利用中の構成・バージョンを緊急で確認してください。
* **ヘッダーベースのアクセス制御回避:** クライアントが供給する `Host` などのHTTPヘッダーのみを信頼して認証・認可を行うと、簡単に偽装される危険があります。TCP接続の送信元や適切な認証トークンによる検証を行ってください（CVE-2026-82533参照）。
* **外部コマンド呼び出し時の引数・モード指定:** SQLファイルや外部テキストを CLI ツール（`mysql` 等）へ投入する際は、ツール固有のエスケープシーケンスやインサイドコマンド（例: `\!`）が解釈されないよう、`--binary-mode` の付与や厳格な事前サニタイズを徹底してください（CVE-2026-86733参照）。
* **認証エンドポイントの網羅的なレート制限:** レギュラーなログイン処理だけでなく、別名・互換用として用意した認証系APIエンドポイントに対しても、同等のレート制限や制御を適用しているか見直す必要があります（CVE-2026-86729参照）。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

Microsoftが過去最多となる約970件の脆弱性を修正する更新プログラムを公開し、すでに一部でアクティブな悪用が確認されています。また、F5ネットワーク機器へのルートキット注入や大規模な偽ECサイトによるクレカ情報窃取など、深刻な攻撃手法が報じられています。さらに、アクティブに悪用された脆弱性を24時間以内に報告させるEUサイバーレジリエンス法への対応など、規制面の課題も浮上しています。

- **HIGH** [Microsoft posts nearly 1,000 bugs for Patch Tuesday as CISA warns two being exploited](https://therecord.media/microsoft-patch-tuesday-september-2026) — The Record
- **HIGH** [Microsoft Plugs Nearly 1,000 Security Holes](https://krebsonsecurity.com/2026/09/microsoft-plugs-nearly-1000-security-holes/) — Krebs on Security
- **HIGH** [Patch Tuesday Sets Another Record With 974 CVEs](https://www.darkreading.com/vulnerabilities-threats/patch-tuesday-another-record-974-cves) — Dark Reading
- **HIGH** [DoppelCart fraud network uses 119,000 fake shops to steal credit cards](https://www.bleepingcomputer.com/news/security/doppelcart-fraud-network-uses-119-000-fake-shops-to-steal-credit-cards/) — BleepingComputer
- **HIGH** [Hackers breach F5 BIG-IP APM devices to deploy Linux rootkit](https://www.bleepingcomputer.com/news/security/hackers-breach-f5-big-ip-apm-devices-to-deploy-linux-rootkit/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

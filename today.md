# CVE Digest Dashboard (2026-09-18)

## Overview

- Total: 30
- Critical件数: 2
- High件数: 9
- KEV件数: 0
- Frontend件数: 8
- Backend件数: 22
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-18/frontend-summary.md)
- [Backend Summary](docs/2026-09-18/backend-summary.md)

## Today TOP5

- [CVE-2026-86863](https://github.com/pgadmin-org/pgadmin4/issues/10383) CVE-2026-86863 / CRITICAL / backend
- [CVE-2026-76834](https://b2evolution.net/news/2022/03/26/2022-update-eol) CVE-2026-76834 / CRITICAL / backend
- [CVE-2026-90144](https://git.kernel.org/stable/c/33f016b23a219fe034213849b51436b8e79df251) CVE-2026-90144 / UNKNOWN / frontend
- [CVE-2026-71538](https://github.com/CycloneDX/cyclonedx-node-npm/commit/15d3beb5bcd2b0b6eccfdf31192f5103b3f12c0f) CVE-2026-71538 / HIGH / frontend
- [CVE-2026-85719](https://github.com/AsyncHttpClient/async-http-client/commit/4d887704dec22027310f66c81503226722e9bd23) CVE-2026-85719 / HIGH / backend

## Geminiによる今日の総括

## 今日のまとめ

本日公開された脆弱性では、**pgAdmin 4の認証回避（CVSS 9.8）**や**b2evolution CMSのRCE（CVSS 9.2）**など、緊急度の高い脆弱性が含まれています。また、開発ツール（`cyclonedx-npm`）、Webフレームワーク（`Sanic`）、HTTPクライアント（`AsyncHttpClient`）など、開発・運用環境で広く使われるライブラリ群におけるコマンド注入やヘッダーインジェクション、情報漏洩のリスクも目立ちます。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-86863 (pgAdmin 4 | CVSS 9.8 CRITICAL)**
   - **概要:** Webserver認証設定時、リクエストヘッダーから`REMOTE_USER`を直接参照してしまう実装不備。
   - **影響:** 攻撃者がヘッダーを偽装することで、未認証で任意のユーザーとしてログインが可能。

2. **CVE-2026-76834 (b2evolution CMS | CVSS 9.2 CRITICAL)**
   - **概要:** シリアル化データの検証において負の整数キーのチェック漏れが存在。
   - **影響:** 未認証の攻撃者が任意のPHPオブジェクトを注入し、条件が揃うとリモートコード実行（RCE）が可能。

3. **CVE-2026-71538 (@cyclonedx/cyclonedx-npm | CVSS 8.5 HIGH)**
   - **概要:** Windows環境でのフォールバック処理時、`--workspace`オプションにシェルメタ文字が含まれるとそのまま実行される。
   - **影響:** SBOM作成（CI/CDパイプライン等）時に任意のOSコマンドを実行される恐れ。

4. **CVE-2026-85077 (Sanic | CVSS 8.2 HIGH)**
   - **概要:** HTTP/1.1レスポンスヘッダーの設定時にCR/LF（改行コード）のチェックが行われない。
   - **影響:** ユーザー入力をヘッダーやクッキーに反射している場合、レスポンス分割やヘッダーインジェクション攻撃を受ける。

5. **CVE-2026-85719 (AsyncHttpClient | CVSS 7.5 HIGH)**
   - **概要:** SOCKSプロキシ利用時、プロキシ認証用ヘッダー（`Proxy-Authorization`）が送信先（Origin）へそのまま送信される。
   - **影響:** プロキシの認証情報が通信先サーバーへ漏洩する。

---

## 開発者向けコメント

- **ヘッダー起因の認証・信頼境界に注意:** プロキシやWebサーバー経由の認証情報（`REMOTE_USER`等）を扱う際は、リクエストヘッダーからの安易なフォールバックを許可せず、環境変数からのみ取得する設計を徹底してください。
- **依存ライブラリの最新化:** `Sanic`（ヘッダー/リクエスト分離問題）、`AsyncHttpClient`（クレデンシャル漏洩）、`ExifReader` / `Soup Sieve`（DoS/ReDoS）など、バックエンド・フロントエンド問わずライブラリのアップデートを速やかに実施してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近24時間ではBleepingComputer、Dark Reading、SecurityWeek、The Recordから10件を収集しました。重要度HIGHは0件です。

- **MEDIUM** [New RatHat Android malware uses AI to automate device control](https://www.bleepingcomputer.com/news/security/new-rathat-android-malware-uses-ai-to-automate-device-control/) — BleepingComputer
- **MEDIUM** [CISA Ditches Weekly Vulnerability Roundups for Risk-Based Focus](https://www.darkreading.com/cyber-risk/cisa-ditches-weekly-vuln-roundups-risk-based-focus) — Dark Reading
- **MEDIUM** [European Commission set to push social media restrictions, safety requirements into law](https://therecord.media/european-commission-set-to-push-social-media-kids-restrictions-into-law) — The Record
- **MEDIUM** [China's FamousSparrow APT Spies on US Politics in Latin America](https://www.darkreading.com/cyberattacks-data-breaches/china-famoussparrow-spies-latin-america) — Dark Reading
- **MEDIUM** [OpenAI details more cases of AI agents taking unauthorized actions](https://www.bleepingcomputer.com/news/security/openai-details-more-cases-of-ai-agents-taking-unauthorized-actions/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

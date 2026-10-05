# CVE Digest Dashboard (2026-10-05)

## Overview

- Total: 23
- Critical件数: 10
- High件数: 11
- KEV件数: 0
- Frontend件数: 1
- Backend件数: 15
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-05/frontend-summary.md)
- [Backend Summary](docs/2026-10-05/backend-summary.md)

## Today TOP5

- [CVE-2026-105086](https://github.com/WWBN/AVideo/commit/c4b6ca95a0ae3efa09919a98879870086cff150e) CVE-2026-105086 / CRITICAL / security
- [CVE-2026-105209](https://github.com/zitadel/zitadel/security/advisories/GHSA-pq2q-2c6r-75c4) CVE-2026-105209 / CRITICAL / security
- [CVE-2026-105216](https://github.com/micro/go-micro) CVE-2026-105216 / CRITICAL / backend
- [CVE-2026-105222](https://github.com/alexpechkarev/google-maps) CVE-2026-105222 / CRITICAL / backend
- [CVE-2026-105218](https://github.com/go-pay/gopay) CVE-2026-105218 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ
本日掲載された脆弱性では、ID管理・認証基盤である**ZITADELにおける多数の深刻な認証バイパスおよびアカウント乗っ取りの脆弱性**（CVSS 9.8含む）と、各種通信ライブラリ・SDKにおける**デフォルトでのTLS証明書検証無効化**（CVSS 9.1）が目立ちます。その他にもReDoSやXSSからの任意コード実行、SQLインジェクションなどが報告されており、認証実装および依存ライブラリの設定見直しが強く求められます。

## 優先して確認すべき3〜5件
1. **CVE-2026-105207 (ZITADEL) - CVSS 9.8 (CRITICAL)**
   - 一次認証や権限確認なしに外部IdPアカウントを結合できる不備。ログイン名を知る攻撃者によるアカウント乗っ取りが可能です。
2. **CVE-2026-105209 (ZITADEL) - CVSS 9.6 (CRITICAL)**
   - パスキー/パスワードレス登録コード発行時の組織（テナント）チェック不備。別組織のユーザーアカウントの乗っ取りが可能です。
3. **CVE-2026-105216 (go-micro) - CVSS 9.1 (CRITICAL)**
   - 共通TLSヘルパーで `InsecureSkipVerify` がデフォルトで `true` に設定されており、中間者（MitM）攻撃によりgRPCやRabbitMQ等の通信盗聴・改ざんが可能です。
4. **CVE-2026-105218 (gopay) - CVSS 9.1 (CRITICAL)**
   - デフォルトクライアントでTLS検証が無効化されており、決済プロバイダAPIとの通信が盗聴・改ざんされ、加盟店認証情報や取引データが漏洩する恐れがあります。
5. **CVE-2026-105211 (ZITADEL) - CVSS 9.2 (CRITICAL)**
   - Login V2においてサーバーレスポンスからOTPコードが取得できる不備。MFAを突破したアカウント乗っ取りが可能です。

## 開発者向けコメント
- **認証基盤（ZITADEL等）の緊急アップデート**: ZITADELを利用中の場合は、一次認証前の要素登録や外部IdP連携における認証バイパスが多数判明しているため、速やかに修正済みバージョン（4.17.3 / 3.4.15 等以降）へ更新してください。
- **通信ライブラリのTLS検証設定の確認**: GoやRuby、PHP等のサードパーティ製ライブラリ（`go-micro`, `gopay`, `gist`, `alexpechkarev/google-maps` など）でTLS証明書検証がデフォルト無効になっている事例が頻発しています。依存ライブラリの更新と明示的なTLS検証設定の確認を行ってください。
- **入力値処理とリソース制限**: ファイル解析時のReDoS（Mammoth.js）や、内部リダイレクトによるSSRF（ZITADELのhttp.Get使用例）など、外部からの入力値を検証せずに処理する実装がないかコードレビューを行ってください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近24時間ではBleepingComputer、SecurityWeekから3件を収集しました。重要度HIGHは1件です。

- **HIGH** [Citrix patches NetScaler SAML zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-patches-netscaler-saml-zero-day-exploited-in-attacks/) — BleepingComputer
- **MEDIUM** [Trump Names National Intelligence Director Jay Clayton to Lead a New Federal AI Task Force](https://www.securityweek.com/trump-names-national-intelligence-director-jay-clayton-to-lead-a-new-federal-ai-task-force/) — SecurityWeek
- **MEDIUM** [Anthropic asks Claude users to share voice data for AI model training](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-asks-claude-users-to-share-voice-data-for-ai-model-training/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

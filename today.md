# CVE Digest Dashboard (2026-09-07)

## Overview

- Total: 17
- Critical件数: 0
- High件数: 10
- KEV件数: 0
- Frontend件数: 0
- Backend件数: 14
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-07/frontend-summary.md)
- [Backend Summary](docs/2026-09-07/backend-summary.md)

## Today TOP5

- [CVE-2026-86283](https://github.com/MISP/MISP/commit/44573e4a8.patch) CVE-2026-86283 / HIGH / security
- [CVE-2026-82750](https://cna.erlef.org/cves/CVE-2026-82750.html) CVE-2026-82750 / HIGH / security
- [CVE-2026-82751](https://cna.erlef.org/cves/CVE-2026-82751.html) CVE-2026-82751 / HIGH / security
- [CVE-2026-13608](https://curl.se/docs/CVE-2026-13608.html) CVE-2026-13608 / UNKNOWN / backend
- [CVE-2026-19931](https://curl.se/docs/CVE-2026-19931.html) CVE-2026-19931 / UNKNOWN / backend

## Geminiによる今日の総括

## 今日のまとめ
本日公開されたCVEでは、データベース拡張機能（PostgreSQL Anonymizer）、通信ライブラリ（libcurl）、Webフレームワークや情報共有ツール（MISP、ZenHive mppなど）における脆弱性が報告されています。

特に、PostgreSQL Anonymizerにおける高権限での任意コード実行（CVSS 8.8）や、ZenHive mppにおける未認証リクエストによるガスコスト増大の不備（CVSS 8.3）、さらにlibcurlにおけるメモリ管理（Use-After-Free）やセッション・Cookie処理の不備などが目立ちます。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-19633 (PostgreSQL Anonymizer) - CVSS 8.8 (HIGH)**
   - **内容:** 低権限のマスクドユーザーが、演算子やキャスト、サブクエリを悪用して拡張機能のコンテキスト上で高権限で任意コードを実行可能。
   - **対策:** PostgreSQL Anonymizer 3.1.4 以降へアップデート。

2. **CVE-2026-82750 / CVE-2026-82751 (ZenHive mpp) - CVSS 8.3 (HIGH)**
   - **内容:** 入力量の検証不備により、未認証のリモート攻撃者が手数料支払者のガスコストを大幅に膨らませたり、意図しない委任・プロビジョニング費用を支払わせることが可能。
   - **対策:** 該当機能を利用中の場合は、パラメータ制限および入力検証処理の見直しを実施。

3. **CVE-2026-80229 (libcurl / OpenSSL 3)**
   - **内容:** libcurlのmultiインターフェース利用時、OpenSSL 3構成下でイージーハンドル破棄後も接続がダングリングポインタを保持し、Heap Use-After-Freeが発生する。
   - **対策:** libcurlの最新版への更新および接続・ハンドルのライフサイクル管理の再確認。

4. **CVE-2026-86283 (MISP) - CVSS 7.1 (HIGH)**
   - **内容:** UiBetaテーマのコレクションビュー処理において、イベントの再照会時にACL（アクセス制御リスト）チェックが適用されず、アクセス制御が回避される。
   - **対策:** 該当ビュー処理の更新、またはACLが正しく適用されている修正版を適用。

---

## 開発者向けコメント

- **ミドルウェア・拡張機能のアップデート:** PostgreSQL Anonymizerのように、DB拡張機能が持つ権限を悪用した昇格攻撃が報告されています。利用中の拡張機能のバージョンを至急確認してください。
- **通信ライブラリのセキュアな実装:** libcurlにおいてUse-After-Free（CVE-2026-80229）、空資格情報時の接続誤再利用（CVE-2026-19931）、Cookieドメイン境界チェック不足（CVE-2026-82209）など複数問題が報告されています。HTTP接続やライフサイクル管理を行うコードの安全性を再確認してください。
- **UI/ビュー層でのアクセス制御と入力制限:** Viewテンプレート側で個別にDBクエリを発行した際、ACLチェックが抜け落ちるパターン（MISP）や、パラメータの数値検証不足で計算コストを奪われるパターン（ZenHive mpp）に留意し、ロジック層・表示層双方で適切なバリデーションとアクセス制御を徹底しましょう。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

フィッシング攻撃において、電子メールセキュリティフィルタを回避するために不可視のUnicode文字を利用する手法が悪用されています。攻撃者はASCIIスマグリング手法を用いてフィッシングのおとりを隠蔽しています。これにより、既存のセキュリティ対策を回避する新たな脅威への注意が必要です。

- **MEDIUM** [Attackers conceal phishing lures using invisible Unicode characters](https://www.bleepingcomputer.com/news/security/attackers-conceal-phishing-lures-using-invisible-unicode-characters/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

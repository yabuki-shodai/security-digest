# CVE Digest Dashboard (2026-09-27)

## Overview

- Total: 12
- Critical件数: 6
- High件数: 5
- KEV件数: 0
- Frontend件数: 0
- Backend件数: 8
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-27/frontend-summary.md)
- [Backend Summary](docs/2026-09-27/backend-summary.md)

## Today TOP5

- [CVE-2026-94132](https://www.acymailing.com/) CVE-2026-94132 / CRITICAL / security
- [CVE-2026-82901](https://plugins.trac.wordpress.org/browser/ultimate-addons-for-contact-form-7/tags/3.5.48/addons/pdf-generator/pdf-generator.php#L608) CVE-2026-82901 / CRITICAL / backend
- [CVE-2026-85984](https://plugins.trac.wordpress.org/browser/miniorange-otp-verification/tags/5.5.5/includes/js/loginform.js#L176) CVE-2026-85984 / CRITICAL / backend
- [CVE-2026-97160](https://up.lomart.fr/) CVE-2026-97160 / CRITICAL / backend
- [CVE-2026-97161](https://up.lomart.fr/) CVE-2026-97161 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ
本日公開された12件の脆弱性一覧では、主にJoomlaやWordPressなどのCMS向けプラグイン・拡張機能における深刻度CRITICALおよびHIGHの脆弱性が多数を占めています。未認証でのリモートコード実行（RCE）、認証バイパス、任意ファイルアップロード、SQLインジェクションのほか、Kibanaにおける認可バイパスや権限昇格の脆弱性が報告されています。

## 優先して確認すべき3〜5件
1. **CVE-2026-97163** (Joomla UP plugin / CVSS 10.0 - CRITICAL)
   - UPプラグイン拡張機能（5.0.0〜5.2.0、6.0.0〜6.0.29）に存在する、未認証でリモートコードインストールが可能な最高深刻度の脆弱性。
2. **CVE-2026-85984** (WordPress miniOrange OTP Login / CVSS 9.8 - CRITICAL)
   - プラグイン（<=5.5.5）の `mo_wp_login_intent` パラメータ不備により、未認証の攻撃者が管理者権限等の認証をバイパスできる脆弱性。
3. **CVE-2026-94132** (Joomla AcyMailing Enterprise / CVSS 9.5 - CRITICAL)
   - AcyMailing Enterprise（<11.1.0）のメールボックスアクション機能にて、受信メールの添付ファイルが拡張子チェックなしでWebルート配下に保存され、RCEに繋がる脆弱性。
4. **CVE-2026-82901** (WordPress Ultra Addons for Contact Form 7 / CVSS 9.8 - CRITICAL)
   - プラグイン（<=3.5.50）のPDF Generatorモジュール有効時において、ファイル種別の検証不足により未認証での任意ファイルアップロードおよびRCEが可能となる脆弱性。

## 開発者向けコメント
掲載された脆弱性の多くは、Webアプリケーションやプラグインにおける入力検証・権限管理の不備に起因しています。
* **ファイルアップロード・受信処理の検証徹底**: 拡張子チェックの欠落（CVE-2026-94132）や不十分なファイル検証（CVE-2026-82901）は、Webルートへの悪意あるコード配置（RCE）に直結します。適切なアクセス制御と厳しいバリデーションを設定してください。
* **認証・認可チェックの厳格化**: リクエストパラメータを過信した認証回避（CVE-2026-85984）や、オブジェクト所有者の適切なチェックを怠る認可不備（CVE-2026-72662, CVE-2026-77203）を防止するため、サーバーサイドでの確実な権限判定を実装してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近24時間ではBleepingComputer、SecurityWeekから8件を収集しました。重要度HIGHは0件です。

- **MEDIUM** [ShinyHunters uses WAF bypass trick in Oracle PeopleSoft attacks](https://www.bleepingcomputer.com/news/security/shinyhunters-uses-waf-bypass-trick-in-oracle-peoplesoft-attacks/) — BleepingComputer
- **MEDIUM** [China and US Agree to Establish AI Safety Channel and Continue Trade and Military Talks](https://www.securityweek.com/china-and-us-agree-to-establish-ai-safety-channel-and-continue-trade-and-military-talks/) — SecurityWeek
- **MEDIUM** [Claude Opus 5.5 uses 95% fewer em dashes, but its answers are getting longer](https://www.bleepingcomputer.com/news/artificial-intelligence/claude-opus-55-uses-95-percent-fewer-em-dashes-but-its-answers-are-getting-longer/) — BleepingComputer
- **MEDIUM** [Microsoft pauses KB5002907 update after Office license deactivations](https://www.bleepingcomputer.com/news/microsoft/microsoft-365-kb5002907-update-paused-after-office-license-deactivations/) — BleepingComputer
- **MEDIUM** [GitHub Actions re-enabled with Mini Shai-Hulud payload still active](https://www.bleepingcomputer.com/news/security/github-actions-re-enabled-with-mini-shai-hulud-payload-still-active/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

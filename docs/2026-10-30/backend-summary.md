# Backend CVE Summary (2026-10-30)

## Overview

- 取得日時: 2026-10-30 10:53:37 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 20
- Critical: 1
- High: 8
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-116864](https://patchstack.com/database/wordpress/plugin/wpcargo/vulnerability/wordpress-wpcargo-track-trace-plugin-8-0-5-php-object-injection-vulnerability?_s_id=cve)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-116864
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-30 01:18:01 JST
- 更新日: 2026-10-30 01:20:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WPCargo Track & Trace (バージョン 8.0.5 以下) における PHP オブジェクト注入の脆弱性。
- 影響: 攻撃者によって任意の PHP オブジェクトが注入され、意図しないコード実行やデータ改ざん等が行われる可能性があります。
- 推奨対応: WPCargo Track & Trace を最新の修正済みバージョンへアップデートしてください。

#### References
- https://patchstack.com/database/wordpress/plugin/wpcargo/vulnerability/wordpress-wpcargo-track-trace-plugin-8-0-5-php-object-injection-vulnerability?_s_id=cve

### [CVE-2026-107040](https://f-droid.org/packages/net.basov.omngo.fdroid/)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-107040
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-30 01:17:49 JST
- 更新日: 2026-10-30 01:30:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MBasov OMN-Go (versionCode 26080824) におけるコンポーネントの不適切な権限設定の脆弱性。
- 影響: 未認証の攻撃者によって外部公開コンポーネントが呼び出され、データへの任意アクセスやデータフローの操作が行われる可能性があります。
- 推奨対応: コンポーネントのアクセス権限の見直しまたは修正版への更新が推奨されます。

#### References
- https://f-droid.org/packages/net.basov.omngo.fdroid/
- https://github.com/FFG0d/fdroid-android-advisories/blob/main/advisories/CVE-2026-107040.md
- https://github.com/mvbasov/OMN-Go

### [CVE-2026-119120](https://github.com/unclecode/crawl4ai/security/advisories/GHSA-f856-7xp9-w3cc)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-119120
- 関連キーワード: python, gin, docker
- 影響製品: -
- 公開日: 2026-10-30 01:18:04 JST
- 更新日: 2026-10-30 01:18:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Crawl4AI の Docker API における CosineStrategy の model_name パラメータ検証不備の脆弱性。
- 影響: 悪意のあるモデルの読み込みを通じて Python コードが実行されたり、ディスクやメモリ等のリソースが枯渇させられたりする可能性があります。
- 推奨対応: Crawl4AI 0.9.5 以降のバージョンへアップデートしてください。

#### References
- https://github.com/unclecode/crawl4ai/security/advisories/GHSA-f856-7xp9-w3cc
- https://www.vulncheck.com/advisories/crawl4ai-0.9.0-before-0.9.5-untrusted-model-loading-via-cosinestrategy-model-name

### [CVE-2026-18894](https://www.ibm.com/support/pages/node/7293016)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-18894
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-30 01:18:08 JST
- 更新日: 2026-10-30 05:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Langflow OSS における信頼境界のバイパスおよびコード実行の脆弱性。
- 影響: 遠隔の攻撃者により、公開ワークフロー内の既存コードが所有者の実行権限で呼び出され、サーバープロセス上で実行される可能性があります。
- 推奨対応: 修正された最新バージョンへアップデートしてください。

#### References
- https://www.ibm.com/support/pages/node/7293016

### [CVE-2026-119119](https://github.com/unclecode/crawl4ai/security/advisories/GHSA-rhjm-7hj7-75fx)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-119119
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-30 01:18:04 JST
- 更新日: 2026-10-30 01:18:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Crawl4AI の Docker API サーバーにおける入力制限不備による Denial of Service (DoS) の脆弱性。
- 影響: 未認証の攻撃者が巨大な遅延値を送信することでリソースが枯渇し、他のクロール処理が妨害される可能性があります。
- 推奨対応: Crawl4AI 0.9.5 以降のバージョンへアップデートしてください。

#### References
- https://github.com/unclecode/crawl4ai/security/advisories/GHSA-rhjm-7hj7-75fx
- https://www.vulncheck.com/advisories/crawl4ai-before-0.9.5-denial-of-service-via-unbounded-crawlerrunconfig-delay-fields

### [CVE-2026-119122](https://github.com/unclecode/crawl4ai/security/advisories/GHSA-w4xc-px5p-c32w)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-119122
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-30 01:18:04 JST
- 更新日: 2026-10-30 06:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Crawl4AI の Docker サーバーにおける Blind Server-Side Request Forgery (SSRF) の脆弱性。
- 影響: API クライアントによりプロキシがバイパスされ、内部ネットワークやクラウドメタデータへのスキャン・サービス探索が行われる可能性があります。
- 推奨対応: Crawl4AI 0.9.5 以降のバージョンへアップデートしてください。

#### References
- https://github.com/unclecode/crawl4ai/security/advisories/GHSA-w4xc-px5p-c32w
- https://www.vulncheck.com/advisories/crawl4ai-before-0.9.5-blind-ssrf-via-cachevalidator-freshness-check
- https://github.com/unclecode/crawl4ai/security/advisories/GHSA-w4xc-px5p-c32w

### [CVE-2026-119128](https://github.com/zitadel/zitadel/security/advisories/GHSA-84fg-x5h4-w8xv)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-119128
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 01:18:05 JST
- 更新日: 2026-10-30 01:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADEL の Login V2 UI における認証バイパスの脆弱性。
- 影響: 未認証の攻撃者により、認証手段が未設定のユーザーに対して不正な資格情報が登録され、アカウントが乗っ取られる可能性があります。
- 推奨対応: ZITADEL 4.19.5 以降のバージョンへアップデートしてください。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-84fg-x5h4-w8xv
- https://www.vulncheck.com/advisories/zitadel-4.0.0-before-4.19.5-login-v2-account-takeover-via-forgeable-verificationcheck-cookie

### [CVE-2026-116866](https://patchstack.com/database/wordpress/plugin/woo-conditional-product-fees-for-checkout/vulnerability/wordpress-extra-fees-plugin-for-woocommerce-plugin-4-4-0-php-object-injection-vulnerability?_s_id=cve)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-116866
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 01:18:01 JST
- 更新日: 2026-10-30 01:20:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Extra Fees Plugin for WooCommerce (バージョン4.4.0以下) におけるPHPオブジェクト注入の脆弱性。
- 影響: 寄稿者 (Contributor) 権限を持つ攻撃者により、任意コードの実行や不審な操作が行われる可能性があります。
- 推奨対応: プラグインを最新バージョンへ更新することを推奨します。

#### References
- https://patchstack.com/database/wordpress/plugin/woo-conditional-product-fees-for-checkout/vulnerability/wordpress-extra-fees-plugin-for-woocommerce-plugin-4-4-0-php-object-injection-vulnerability?_s_id=cve

### [CVE-2026-54866](https://patchstack.com/database/wordpress/plugin/razorpay-payment-button-elementor/vulnerability/wordpress-razorpay-payment-button-elementor-plugin-plugin-1-2-8-cross-site-scripting-xss-vulnerability?_s_id=cve)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-54866
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 01:18:10 JST
- 更新日: 2026-10-30 03:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Razorpay Payment Button Elementor Plugin (バージョン1.2.8以下) における未認証のクロスサイトスクリプティング (XSS) の脆弱性。
- 影響: 未認証の第三者により悪意のあるスクリプトが実行され、セッションハイジャックや情報漏洩が発生する可能性があります。
- 推奨対応: プラグインを最新バージョンへ更新することを推奨します。

#### References
- https://patchstack.com/database/wordpress/plugin/razorpay-payment-button-elementor/vulnerability/wordpress-razorpay-payment-button-elementor-plugin-plugin-1-2-8-cross-site-scripting-xss-vulnerability?_s_id=cve

### [CVE-2026-115709](https://discuss.elastic.co/t/elastic-cloud-enterprise-ece-3-8-6-and-4-2-1-security-update-esa-2026-216/391263)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-115709
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 00:17:18 JST
- 更新日: 2026-10-30 00:26:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Elastic Cloud Enterprise (ECE) における不適切なリンク解決 (シンボリックリンク追跡、CWE-59) の脆弱性。
- 影響: シンボリックリンク攻撃により、同一ホスト上の他デプロイメントに属するデータの不正開示や消失が発生する可能性があります。
- 推奨対応: ベンダーが提供する修正済みバージョンへ ECE を更新することを推奨します。

#### References
- https://discuss.elastic.co/t/elastic-cloud-enterprise-ece-3-8-6-and-4-2-1-security-update-esa-2026-216/391263

### [CVE-2026-119129](https://github.com/zitadel/zitadel/security/advisories/GHSA-qj3q-235g-qr6w)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-119129
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 01:18:05 JST
- 更新日: 2026-10-30 03:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADEL (3.0.0〜3.4.15、および4.0.0〜4.19.5未満) の Login V2 における認可欠如の脆弱性。
- 影響: 攻撃者が被害者の既存セッションを利用してOAuth 2.0デバイス認可を承認し、トークンの不正取得やアクセス制限の回避を行う可能性があります。
- 推奨対応: ZITADEL を修正済みバージョン (4.19.5以降など) へ更新することを推奨します。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-qj3q-235g-qr6w
- https://www.vulncheck.com/advisories/zitadel-3.0.0-through-3.4.15-and-4.0.0-before-4.19.5-account-takeover-via-device-authorization-approval

### [CVE-2026-119144](https://github.com/frappe/frappe/security/advisories/GHSA-6pmg-vc6m-6wrr)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-119144
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-10-30 01:18:08 JST
- 更新日: 2026-10-30 01:18:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Frappe Framework (15.111.0未満、および16.21.0未満の16.x) におけるサーバーサイドテンプレート注入 (SSTI) の脆弱性。
- 影響: 認証された攻撃者によりテンプレート式が評価され、制限のないコンテキストで任意コードの実行や不正操作が行われる可能性があります。
- 推奨対応: Frappe Framework を15.111.0、16.21.0、またはそれ以降の修正済みバージョンへ更新することを推奨します。

#### References
- https://github.com/frappe/frappe/security/advisories/GHSA-6pmg-vc6m-6wrr
- https://www.vulncheck.com/advisories/frappe-framework-before-15.111.0-and-16-x-before-16.21.0-server-side-template-injection-via-message-fields

### [CVE-2026-116849](https://patchstack.com/database/wordpress/plugin/streamcast/vulnerability/wordpress-streamcast-plugin-2-4-6-cross-site-scripting-xss-vulnerability?_s_id=cve)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-116849
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 00:17:20 JST
- 更新日: 2026-10-30 02:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: bPlugins StreamCast (バージョン2.4.6以下) における格納型クロスサイトスクリプティング (XSS) の脆弱性。
- 影響: 悪意のあるスクリプトが保存・実行され、ユーザーのブラウザ上で不正な操作や情報漏洩が発生する可能性があります。
- 推奨対応: プラグインを最新バージョンへ更新することを推奨します。

#### References
- https://patchstack.com/database/wordpress/plugin/streamcast/vulnerability/wordpress-streamcast-plugin-2-4-6-cross-site-scripting-xss-vulnerability?_s_id=cve

### [CVE-2026-118097](https://patchstack.com/database/wordpress/plugin/html5-video-player/vulnerability/wordpress-flash-html5-video-plugin-2-14-0-cross-site-scripting-xss-vulnerability?_s_id=cve)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-118097
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 00:17:21 JST
- 更新日: 2026-10-30 05:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: bPlugins Flash & HTML5 Video (バージョン2.14.0以下) における格納型クロスサイトスクリプティング (XSS) の脆弱性。
- 影響: 悪意のあるスクリプトが保存・実行され、ユーザーのブラウザ上で不正な操作や情報漏洩が発生する可能性があります。
- 推奨対応: プラグインを最新バージョンへ更新することを推奨します。

#### References
- https://patchstack.com/database/wordpress/plugin/html5-video-player/vulnerability/wordpress-flash-html5-video-plugin-2-14-0-cross-site-scripting-xss-vulnerability?_s_id=cve

### [CVE-2026-116406](https://patchstack.com/database/wordpress/plugin/webba-booking-lite/vulnerability/wordpress-webba-booking-plugin-6-5-4-broken-access-control-vulnerability?_s_id=cve)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-116406
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 00:17:19 JST
- 更新日: 2026-10-30 02:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Webba Booking（6.5.4以下）における認可検証の欠如に関する脆弱性。
- 影響: アクセス制御の設定不備を悪用され、不正な操作が行われる可能性があります。
- 推奨対応: 最新バージョンへのアップデートおよびアクセス制御設定の確認を行ってください。

#### References
- https://patchstack.com/database/wordpress/plugin/webba-booking-lite/vulnerability/wordpress-webba-booking-plugin-6-5-4-broken-access-control-vulnerability?_s_id=cve

### [CVE-2026-119140](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-5hhx-4wrr-3j9g)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-119140
- 関連キーワード: fiber
- 影響製品: -
- 公開日: 2026-10-30 01:18:07 JST
- 更新日: 2026-10-30 01:18:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Wasmtime (46.0.0〜48.0.6未満、および49.0.0〜49.0.3未満) におけるサービス拒否 (DoS) の脆弱性。
- 影響: 悪意のあるコンポーネントによりホストがパニックを起こし、組み込み環境やサービスがクラッシュする可能性があります。
- 推奨対応: Wasmtime を48.0.6、49.0.3、またはそれ以降の修正済みバージョンへ更新することを推奨します。

#### References
- https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-5hhx-4wrr-3j9g
- https://www.vulncheck.com/advisories/wasmtime-46.0.0-before-48.0.6-and-49.0.0-before-49.0.3-host-panic-via-thread-yield

### [CVE-2026-48200](https://patchstack.com/database/wordpress/plugin/document-library-lite/vulnerability/wordpress-document-library-lite-plugin-1-3-0-sensitive-data-exposure-vulnerability?_s_id=cve)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-48200
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 01:18:09 JST
- 更新日: 2026-10-30 03:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Barn2 Plugins Document Library Lite (バージョン1.3.0以下) における機密情報の不適切な送信の脆弱性。
- 影響: 埋め込まれた機密情報が不正に取得・開示される可能性があります。
- 推奨対応: プラグインを最新バージョンへ更新することを推奨します。

#### References
- https://patchstack.com/database/wordpress/plugin/document-library-lite/vulnerability/wordpress-document-library-lite-plugin-1-3-0-sensitive-data-exposure-vulnerability?_s_id=cve

### [CVE-2026-80067](https://docs.stylemixthemes.com/masterstudy-lms/changelog-free-version)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-80067
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 00:17:24 JST
- 更新日: 2026-10-30 02:18:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用 MasterStudy LMS プラグイン (バージョン3.7.50未満) における権限検証不足を伴うパストラバーサルの脆弱性。
- 影響: 購読者 (Subscriber) 権限を持つ攻撃者が任意のWXRファイルを読み込み、意図しない投稿データやメタデータを自身のアカウントで公開する可能性があります。
- 推奨対応: プラグインをバージョン3.7.50以降へ更新することを推奨します。

#### References
- https://docs.stylemixthemes.com/masterstudy-lms/changelog-free-version
- https://wordpress.org/plugins/masterstudy-lms-learning-management-system
- https://www.vulncheck.com/advisories/masterstudy-lms-wordpress-plugin-path-traversal-via-stm-lms-step-parameter

### [CVE-2026-80069](https://docs.stylemixthemes.com/masterstudy-lms/changelog-free-version)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-80069
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 00:17:24 JST
- 更新日: 2026-10-30 02:18:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MasterStudy LMSプラグイン（3.7.50未満）において、AJAXアクションの権限およびnonce検証が不足している脆弱性。
- 影響: 認証済みユーザーが不適切な処理を呼び出し、 display_errors が有効な場合に絶対ファイルパスが漏洩する可能性があります。
- 推奨対応: プラグインをバージョン 3.7.50 以降に更新してください。

#### References
- https://docs.stylemixthemes.com/masterstudy-lms/changelog-free-version
- https://wordpress.org/plugins/masterstudy-lms-learning-management-system
- https://www.vulncheck.com/advisories/masterstudy-lms-wordpress-plugin-missing-authorization-via-stm-lms-send-test-email-ajax

### [CVE-2026-119126](https://github.com/parse-community/parse-server/security/advisories/GHSA-969q-274f-mc7w)

> **Backend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-119126
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-30 01:18:05 JST
- 更新日: 2026-10-30 06:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Parse Server（8.6.106未満、および9.0.0以上9.10.5-alpha.7未満）において、ドット表記キー（null/undefined値）の不適切な処理が存在する脆弱性。
- 影響: 書き込み権限を持つクライアントにより、監査ログ記録や通知イベント（afterSave, LiveQuery等）を回避される可能性があります。
- 推奨対応: Parse Serverを 8.6.106 または 9.10.5-alpha.7 以降に更新してください。

#### References
- https://github.com/parse-community/parse-server/security/advisories/GHSA-969q-274f-mc7w
- https://www.vulncheck.com/advisories/parse-server-before-8.6.106-and-9.0.0-before-9.10.5-alpha.7-aftersave-trigger-and-livequery-bypass-via-dot-notation-keys

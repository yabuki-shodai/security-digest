# Frontend CVE Summary (2026-08-22)

## Overview

- 取得日時: 2026-08-22 07:36:29 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 18
- Critical: 0
- High: 8
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-55850](https://github.com/element-hq/element-web/commit/7949980a7e3c7e397d7afe899ef1b0563c417b0e)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-55850
- 関連キーワード: javascript, react
- 影響製品: -
- 公開日: 2026-08-22 04:17:04 JST
- 更新日: 2026-08-22 05:16:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Element Webのホームページコンテンツ描画処理において、サニタイズを行わずにdangerouslySetInnerHTMLへデータを渡している脆弱性。
- 影響: 悪意あるホームサーバーからフィッシングHTMLなどを挿入・表示される可能性があります（CSPによりJS実行は防止されます）。
- 推奨対応: Element Webをバージョン 1.12.22 以降に更新してください。

#### References
- https://github.com/element-hq/element-web/commit/7949980a7e3c7e397d7afe899ef1b0563c417b0e
- https://github.com/element-hq/element-web/releases/tag/v1.12.22
- https://github.com/element-hq/element-web/security/advisories/GHSA-wrcp-5v3v-3j6v
- https://www.machinespirits.com/advisory/563a17

### [CVE-2026-50288](https://github.com/asymmetric-effort/specifyjs/commit/25d1fb491d99479efdf501f5f75e0bb80c908f0a)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-50288
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-08-22 05:16:36 JST
- 更新日: 2026-08-22 05:16:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SpecifyJSのassertSecureUrl関数において、URLパースエラー発生時に例外を投げず処理を継続してしまう問題。
- 影響: HTTPS検証を無効化され、安全でないリクエストがそのまま進行する可能性があります。
- 推奨対応: SpecifyJSをバージョン 0.2.136 以降に更新してください。

#### References
- https://github.com/asymmetric-effort/specifyjs/commit/25d1fb491d99479efdf501f5f75e0bb80c908f0a
- https://github.com/asymmetric-effort/specifyjs/releases/tag/v0.2.136
- https://github.com/asymmetric-effort/specifyjs/security/advisories/GHSA-8882-frvv-92w4

### [CVE-2026-50290](https://github.com/asymmetric-effort/specifyjs/commit/25d1fb491d99479efdf501f5f75e0bb80c908f0a)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-50290
- 関連キーワード: typescript, javascript, express
- 影響製品: -
- 公開日: 2026-08-22 05:16:36 JST
- 更新日: 2026-08-22 06:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SpecifyJSのCSSサニタイズ処理において、Unicodeエスケープやコメント等で正規表現チェックを回避できる不備。
- 影響: レガシーブラウザ（IE6〜IE10など）環境において、悪意のあるCSSが挿入・実行される可能性があります。
- 推奨対応: SpecifyJSをバージョン 0.2.136 以降に更新してください。

#### References
- https://github.com/asymmetric-effort/specifyjs/commit/25d1fb491d99479efdf501f5f75e0bb80c908f0a
- https://github.com/asymmetric-effort/specifyjs/security/advisories/GHSA-93q6-wwjh-jc6h

### [CVE-2026-55241](https://github.com/bluewave-labs/Checkmate/commit/091c36cbf338b673110b0806d76df26d52516468)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-55241
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-08-22 03:16:48 JST
- 更新日: 2026-08-22 03:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Checkmateのユーザー登録APIにおいて、登録検証や制限チェックの前にファイル制限のないMulter処理を行う不備。
- 影響: 未認証の攻撃者が巨大なファイルを過剰送信することでメモリを枯渇させ、サービスを停止（DoS）させる可能性があります。
- 推奨対応: Checkmateをバージョン 3.9.1 以降に更新してください。

#### References
- https://github.com/bluewave-labs/Checkmate/commit/091c36cbf338b673110b0806d76df26d52516468
- https://github.com/bluewave-labs/Checkmate/releases/tag/v3.9.1
- https://github.com/bluewave-labs/Checkmate/security/advisories/GHSA-9xvg-x28f-m78m

### [CVE-2026-63421](https://github.com/keystonejs/keystone/commit/9fb88b246950ce4de754a43fe6416f20403577b1)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-63421
- 関連キーワード: graphql, node.js
- 影響製品: -
- 公開日: 2026-08-22 06:17:01 JST
- 更新日: 2026-08-22 06:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KeystoneのfindManyリゾルバにおいて、負のtake引数をmaxTake制限と比較する際の入力検証不足。
- 影響: 未認証の攻撃者が想定以上のレコードを取得したり、リソースを枯渇させたりする可能性があります。
- 推奨対応: Keystoneをバージョン 6.5.3 以降に更新してください。

#### References
- https://github.com/keystonejs/keystone/commit/9fb88b246950ce4de754a43fe6416f20403577b1
- https://github.com/keystonejs/keystone/pull/9859
- https://github.com/keystonejs/keystone/releases/tag/@keystone-6/core@6.5.3
- https://github.com/keystonejs/keystone/security/advisories/GHSA-cqmq-8755-7xvh

### [CVE-2026-63135](https://github.com/YOURLS/YOURLS/commit/e1e93476655107e6caab34e52259eb1c91079ec7)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-63135
- 関連キーワード: javascript, go, gin
- 影響製品: -
- 公開日: 2026-08-22 06:17:01 JST
- 更新日: 2026-08-22 06:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: YOURLSの統計表示機能において、Refererヘッダーのドメイン名をエスケープせずにインラインJavaScriptへ埋め込んでいる脆弱性。
- 影響: 統計データのポイズニングにより、管理者が統計ページを閲覧した際に任意JSが実行され、APIトークン等の機密情報が盗取される可能性があります。
- 推奨対応: YOURLSをバージョン 1.10.4 以降に更新してください。

#### References
- https://github.com/YOURLS/YOURLS/commit/e1e93476655107e6caab34e52259eb1c91079ec7
- https://github.com/YOURLS/YOURLS/pull/4107
- https://github.com/YOURLS/YOURLS/releases/tag/1.10.4
- https://github.com/YOURLS/YOURLS/security/advisories/GHSA-5h77-88j3-r659

### [CVE-2026-54071](https://github.com/funstory-ai/BabelDOC/blob/main/docs/release-notes/v0.6.3.md)

> **Frontend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-54071
- 関連キーワード: babel, python
- 影響製品: -
- 公開日: 2026-08-22 04:17:02 JST
- 更新日: 2026-08-22 07:16:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: BabelDOCで使われるPDFパーサーにおいて、パス・トラバーサルにより攻撃者制御のpickleファイルを読み込んでデシリアライズする脆弱性。
- 影響: BabelDOCプロセスの権限で、攻撃者による任意のPythonコードが実行される可能性があります。
- 推奨対応: BabelDOCをバージョン 0.6.3 以降に更新してください。

#### References
- https://github.com/funstory-ai/BabelDOC/blob/main/docs/release-notes/v0.6.3.md
- https://github.com/funstory-ai/BabelDOC/commit/28f784ca6b437dbba040bfd9c67110373cd0924b
- https://github.com/funstory-ai/BabelDOC/releases/tag/v0.6.3
- https://github.com/funstory-ai/BabelDOC/security/advisories/GHSA-m8gf-v64p-gfmg

### [CVE-2026-77811](https://aws.amazon.com/security/security-bulletins/2026-088-aws/)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-77811
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-22 06:17:08 JST
- 更新日: 2026-08-22 06:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenSearch Dashboardsのdashboards-observabilityプラグインにおける不適切な入力検証の脆弱性。
- 影響: 保存オブジェクトの書き込み権限を持つ攻撃者が、他ユーザーのセッション上で任意のJavaScriptを実行（XSS）する可能性があります。
- 推奨対応: 修正されたバージョンへオープンサーチダッシュボードおよびプラグインを更新してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-088-aws/
- https://github.com/opensearch-project/dashboards-observability/security/advisories/GHSA-rmqx-r3wm-3px5
- https://opensearch.org/artifacts/by-version/#release-2-19-6
- https://opensearch.org/artifacts/by-version/#release-3-4-0

### [CVE-2026-61824](https://github.com/kepano/defuddle/commit/baf2eaef61d334ef595b28c89e5c5e89e52daf7f)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-61824
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-22 06:17:01 JST
- 更新日: 2026-08-22 06:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Defuddleの抽出処理において、ページ由来の属性値や説明文を適切にエスケープせずにHTML文字列を構築する問題。
- 影響: 抽出されたHTMLをレンダリングしたユーザーの環境で、悪意あるJavaScriptが実行される可能性があります。
- 推奨対応: Defuddleをバージョン 0.19.1 以降に更新してください。

#### References
- https://github.com/kepano/defuddle/commit/baf2eaef61d334ef595b28c89e5c5e89e52daf7f
- https://github.com/kepano/defuddle/pull/326
- https://github.com/kepano/defuddle/releases/tag/0.19.1
- https://github.com/kepano/defuddle/security/advisories/GHSA-jg4p-g6xj-4qmf

### [CVE-2026-75933](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-232-02.json)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-75933
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-22 01:18:17 JST
- 更新日: 2026-08-22 02:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Jet Adminのサインインページの設定オプションを介してJavaScriptが注入可能な脆弱性。
- 影響: 認証された攻撃者が挿入したスクリプトが、アクセスしたユーザーのコンテキストで実行（XSS）される可能性があります。
- 推奨対応: Jet Adminを修正済みの最新バージョンへ更新してください。

#### References
- https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-232-02.json
- https://www.cve.org/CVERecord?id=CVE-2026-75933
- https://www.jetadmin.io/

### [CVE-2026-53529](https://github.com/perber/leafwiki/security/advisories/GHSA-j344-qxqm-wg64)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-53529
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-22 07:16:39 JST
- 更新日: 2026-08-22 07:16:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LeafWiki is a self-hosted wiki. Prior to version 0.10.2, page titles returned by the search API could be rendered as raw HTML in the frontend. A user with editor or administrator permissions could create or modify a page title containing an HTML/JavaScript payload. When another user searched for a matching term, the pa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/perber/leafwiki/security/advisories/GHSA-j344-qxqm-wg64

### [CVE-2026-77795](https://github.com/SunRisexyz/Vul-of-Ruoyi/issues/1)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-77795
- 関連キーワード: vue, go
- 影響製品: -
- 公開日: 2026-08-22 04:17:51 JST
- 更新日: 2026-08-22 05:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was identified in Dromara RuoYi-Vue-Plus up to 5.6.2. This issue affects the function FlwInstanceController/FlwDefinitionController/FlwCategoryController/FlwSpelController/TestLeaveController of the component Workflow Endpoint. Such manipulation leads to improper authorization. The attack can be launche...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/SunRisexyz/Vul-of-Ruoyi/issues/1
- https://vuldb.com/cve/CVE-2026-77795
- https://vuldb.com/submit/881227
- https://vuldb.com/vuln/394113
- https://vuldb.com/vuln/394113/cti

### [CVE-2026-35163](https://github.com/OctoPrint/OctoPrint/commit/42e0f9863935e136f04ed3c560cb96483a580d1b)

> **Frontend** / **MEDIUM** / CVSS: **4.6** / KEV: **no**

- タイトル: CVE-2026-35163
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-22 04:17:01 JST
- 更新日: 2026-08-22 05:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OctoPrint provides a web interface for controlling consumer 3D printers. Prior to 1.11.8 and 2.0.0rc3, Suppressed Command notification popups use PNotify rendering for printer-controlled payload.command and payload.message values in src/octoprint/static/js/app/viewmodels/terminal.js without HTML escaping. An attacker w...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/OctoPrint/OctoPrint/commit/42e0f9863935e136f04ed3c560cb96483a580d1b
- https://github.com/OctoPrint/OctoPrint/commit/6e3db9096f8a94f7c2249be24b6d03a7d9c12bc7
- https://github.com/OctoPrint/OctoPrint/releases/tag/1.11.8
- https://github.com/OctoPrint/OctoPrint/releases/tag/2.0.0rc3
- https://github.com/OctoPrint/OctoPrint/security/advisories/GHSA-p6qx-ghxm-389h

### [CVE-2026-43980](https://github.com/pypa/advisory-database/tree/main/vulns/malla/PYSEC-2026-2618.yaml)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-43980
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-22 07:16:37 JST
- 更新日: 2026-08-22 07:16:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Malla is a web analyzer for Meshtastic networks based on MQTT data. Prior to commit 4086e2b5f61615a813b70b25bc76095083552135, code names (long_name, short_name) received via MQTT are stored in SQLite without sanitization and rendered into the DOM without escaping. Any participant on a public Meshtastic MQTT broker can...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pypa/advisory-database/tree/main/vulns/malla/PYSEC-2026-2618.yaml
- https://github.com/zenitraM/malla/commit/4086e2b5f61615a813b70b25bc76095083552135
- https://github.com/zenitraM/malla/security/advisories/GHSA-ch57-39q2-4crm

### [CVE-2026-69231](https://www.esri.com/arcgis-blog/products/arcgis-enterprise/administration/august-2026-arcgis-security-bulletin)

> **Frontend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-69231
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-22 06:17:03 JST
- 更新日: 2026-08-22 06:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: There is a stored cross site scripting issue in Esri Portal for ArcGIS versions 11.5 and prior that may allow a remote, privileged attacker to inject malicious code that could potentially execute arbitrary JavaScript in a victim’s browser. Users working with ArcGIS Enterprise 11.1, 11.3, 11.5 are encouraged to patch. A...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.esri.com/arcgis-blog/products/arcgis-enterprise/administration/august-2026-arcgis-security-bulletin

### [CVE-2026-69232](https://www.esri.com/arcgis-blog/products/arcgis-enterprise/administration/august-2026-arcgis-security-bulletin)

> **Frontend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-69232
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-22 06:17:03 JST
- 更新日: 2026-08-22 06:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: There is a stored cross site scripting issue in Esri Portal for ArcGIS versions 11.5 and prior that may allow a remote, privileged attacker to inject malicious code that could potentially execute arbitrary JavaScript in a victim’s browser. Users working with ArcGIS Enterprise 11.1, 11.3, 11.5 are encouraged to patch. A...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.esri.com/arcgis-blog/products/arcgis-enterprise/administration/august-2026-arcgis-security-bulletin

### [CVE-2026-69234](https://www.esri.com/arcgis-blog/products/arcgis-enterprise/administration/august-2026-arcgis-security-bulletin)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-69234
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-22 06:17:04 JST
- 更新日: 2026-08-22 06:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: There is a reflected cross site scripting vulnerability in Esri Portal for ArcGIS versions 11.5 and prior which may allow a remote, unauthenticated attacker to create a crafted link which when clicked could potentially execute arbitrary JavaScript code in the victim’s browser. Users working with ArcGIS Enterprise 11.1,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.esri.com/arcgis-blog/products/arcgis-enterprise/administration/august-2026-arcgis-security-bulletin

### [CVE-2026-69236](https://www.esri.com/arcgis-blog/products/arcgis-enterprise/administration/august-2026-arcgis-security-bulletin)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-69236
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-22 06:17:04 JST
- 更新日: 2026-08-22 06:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: There is a stored cross site scripting issue in Esri Portal for ArcGIS versions 12.1 and prior that may allow a remote, privileged attacker to inject malicious code that could potentially execute arbitrary JavaScript in a victim’s browser. Users working with ArcGIS Enterprise 11.1, 11.3, 11.5, 12.0 or 12.1 are encourag...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.esri.com/arcgis-blog/products/arcgis-enterprise/administration/august-2026-arcgis-security-bulletin

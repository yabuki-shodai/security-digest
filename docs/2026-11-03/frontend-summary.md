# Frontend CVE Summary (2026-11-03)

## Overview

- 取得日時: 2026-11-03 12:26:14 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 0
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-119733](https://medium.com/@TheWildEye/a-sub-user-could-delete-a-company-in-munshi-94bf92476e5c)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-119733
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-11-03 04:18:02 JST
- 更新日: 2026-11-03 05:17:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Petpooja製Munshiにおける会社削除API（DELETE /api/companies/{company_id}）の認可欠如の脆弱性。
- 影響: 権限のないサブユーザーにより会社情報が不当に削除され、請求書や設定などの関連データが永久に失われる可能性があります。
- 推奨対応: 2026年7月7日以降に提供された修正済みバージョンへアップデートしてください。

#### References
- https://medium.com/@TheWildEye/a-sub-user-could-delete-a-company-in-munshi-94bf92476e5c
- https://www.petpooja.com/
- https://www.vulncheck.com/advisories/munshi-missing-authorization-in-company-deletion-api

### [CVE-2026-111048](https://github.com/FOSSBilling/FOSSBilling/commit/87528920b6cb1ba6f113583253eb4d7abdd1d8c6)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-111048
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-03 03:18:35 JST
- 更新日: 2026-11-03 03:18:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FOSSBilling（0.1.0から0.8.9未満）の管理者チケットメモ表示における蓄積型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 悪意あるHTML/JavaScriptが埋め込まれたチケットを閲覧した管理者のセッションでスクリプトが実行され、CSRFトークンや各種データの窃取、最高管理者権限での操作を行われる可能性があります。
- 推奨対応: バージョン0.8.9以降へアップデートしてください。

#### References
- https://github.com/FOSSBilling/FOSSBilling/commit/87528920b6cb1ba6f113583253eb4d7abdd1d8c6
- https://github.com/FOSSBilling/FOSSBilling/pull/4548
- https://github.com/FOSSBilling/FOSSBilling/releases/tag/0.8.9
- https://github.com/FOSSBilling/FOSSBilling/security/advisories/GHSA-493h-fvcx-6q62

### [CVE-2026-119301](https://aws.amazon.com/security/security-bulletins/2026-161-aws/)

> **Frontend** / **HIGH** / CVSS: **7.9** / KEV: **no**

- タイトル: CVE-2026-119301
- 関連キーワード: swr, aws
- 影響製品: -
- 公開日: 2026-11-03 02:17:39 JST
- 更新日: 2026-11-03 04:34:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AWS SDK for pandas (awswrangler) のApache Iceberg書き込みコンポーネントにおけるSQLクォート構文のエスケープ不備の脆弱性。
- 影響: Glue Data Catalogのメタデータ変更権限を持つユーザーにより、より上位権限を持つ主体がアクセス可能な任意のテーブルの参照や書き込みが行われる可能性があります。
- 推奨対応: バージョン3.17.1以降へアップデートしてください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-161-aws/
- https://github.com/aws/aws-sdk-pandas/releases/tag/3.17.1
- https://github.com/aws/aws-sdk-pandas/security/advisories/GHSA-g8fh-6w6x-mhqf

### [CVE-2026-120438](https://github.com/quickjs-ng/quickjs/blob/v0.15.1/quickjs.c#L51509)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-120438
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-03 00:17:25 JST
- 更新日: 2026-11-03 04:34:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: QuickJS-NG（0.16.0未満）の js_proxy_get_own_property_names 関数における32ビット環境での整数オーバーフローの脆弱性。
- 影響: ヒープバッファオーバーフローが誘発され、プロセスのクラッシュや任意のコード実行に繋がる可能性があります。
- 推奨対応: バージョン0.16.0以降へアップデートしてください。

#### References
- https://github.com/quickjs-ng/quickjs/blob/v0.15.1/quickjs.c#L51509
- https://github.com/quickjs-ng/quickjs/commit/252209d99cf112568160548bdcaa98d95e0d0068
- https://github.com/quickjs-ng/quickjs/releases/tag/v0.16.0
- https://github.com/quickjs-ng/quickjs/security/advisories/GHSA-jp52-chwg-2p9p
- https://www.vulncheck.com/advisories/quickjs-ng-before-0.16.0-heap-buffer-overflow-via-proxy-ownkeys-enumeration

### [CVE-2026-120439](https://github.com/quickjs-ng/quickjs/blob/v0.15.1/quickjs.c#L60032)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-120439
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-03 00:17:25 JST
- 更新日: 2026-11-03 04:34:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: QuickJS-NG（0.16.0未満）の js_typed_array_sort 関数における32ビット環境での整数オーバーフローの脆弱性。
- 影響: 巨大なTypedArrayに対するソート操作時にバッファ外への書き込みが発生し、クラッシュや任意のコード実行に繋がる可能性があります。
- 推奨対応: バージョン0.16.0以降へアップデートしてください。

#### References
- https://github.com/quickjs-ng/quickjs/blob/v0.15.1/quickjs.c#L60032
- https://github.com/quickjs-ng/quickjs/commit/e93cca611908e12b824ec85fbee6b31a5ee61568
- https://github.com/quickjs-ng/quickjs/releases/tag/v0.16.0
- https://github.com/quickjs-ng/quickjs/security/advisories/GHSA-9wv5-5cgr-grj6
- https://www.vulncheck.com/advisories/quickjs-ng-before-0.16.0-heap-buffer-overflow-via-typedarray-prototype-sort

### [CVE-2026-120443](https://github.com/sea-team/gofound/blob/v1.4.1/searcher/engine.go)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-120443
- 関連キーワード: vue, go, gin
- 影響製品: -
- 公開日: 2026-11-03 00:17:26 JST
- 更新日: 2026-11-03 04:35:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GoFound（1.4.1以下）の /api/index 端点および検索結果表示処理における蓄積型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 未認証の攻撃者が登録した悪意あるコンテンツを管理者が検索した際、ブラウザ上で任意スクリプトが実行される可能性があります。
- 推奨対応: 修正版へのアップデートまたは入力データの適切なエスケープ処理の実施を検討してください。

#### References
- https://github.com/sea-team/gofound/blob/v1.4.1/searcher/engine.go
- https://github.com/sea-team/gofound/blob/v1.4.1/web/admin/assets/web/src/views/dashboard.vue
- https://github.com/sea-team/gofound/issues/101
- https://vul.yulun.ac.cn/20261102/gofound/
- https://www.vulncheck.com/advisories/gofound-through-1.4.1-stored-xss-via-admin-dashboard-search-results

### [CVE-2026-2102](https://github.com/WrenSecurity/wrensec-commons/commit/5b50c64c14943b6f4d7faf996345e603956bae1d)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-2102
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-03 01:17:40 JST
- 更新日: 2026-11-03 02:17:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: wrensec-commonsのCRESTフレームワークにおける _mimeType パラメータのサニタイズ不足による反射型XSSの脆弱性。
- 影響: 攻撃者が作成したURLをユーザーに開かせることで、レスポンスがHTMLとして解釈され、ユーザーのブラウザ上で任意のJavaScriptが実行される可能性があります。
- 推奨対応: バージョン22.6.2または23.0.0以降へアップデートしてください。

#### References
- https://github.com/WrenSecurity/wrensec-commons/commit/5b50c64c14943b6f4d7faf996345e603956bae1d
- https://github.com/WrenSecurity/wrensec-commons/commit/65bbfd8c63c42e84ff7699aa5b82a22c08a12624
- https://github.com/WrenSecurity/wrensec-commons/security/advisories/GHSA-4vhv-49g2-496q

### [CVE-2026-119735](https://medium.com/@TheWildEye/stored-xss-in-munshi-a-purchase-inquiry-message-could-rewrite-the-page-6b8ef14f9999)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-119735
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-03 04:18:02 JST
- 更新日: 2026-11-03 04:35:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Petpooja製Munshiの購入照会スレッド（/purchase-inquiry/thread/{thread-id}）における蓄積型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 認証済みユーザーが送信した悪意あるメッセージを他のユーザーが閲覧した際、ブラウザ上でスクリプトが実行されページ改ざんなどが生じる可能性があります。
- 推奨対応: 2026年7月13日以降に提供された修正済みバージョンへアップデートしてください。

#### References
- https://medium.com/@TheWildEye/stored-xss-in-munshi-a-purchase-inquiry-message-could-rewrite-the-page-6b8ef14f9999
- https://www.petpooja.com/
- https://www.vulncheck.com/advisories/munshi-xss-via-purchase-inquiry-thread-rendering

### [CVE-2026-120440](https://github.com/quickjs-ng/quickjs/blob/v0.15.1/quickjs.c#L61154)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-120440
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-03 00:17:26 JST
- 更新日: 2026-11-03 04:34:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: QuickJS-NG（0.16.0未満）の js_atomics_store 関数におけるメモリリークの脆弱性。
- 影響: エラー発生時にメモリが解放されず、繰り返しの呼び出しによりヒープメモリが枯渇してサービス拒否（DoS）状態に陥る可能性があります。
- 推奨対応: バージョン0.16.0以降へアップデートしてください。

#### References
- https://github.com/quickjs-ng/quickjs/blob/v0.15.1/quickjs.c#L61154
- https://github.com/quickjs-ng/quickjs/commit/62951e1bc68711d37aad986ff84ef0fe17038a7e
- https://github.com/quickjs-ng/quickjs/releases/tag/v0.16.0
- https://github.com/quickjs-ng/quickjs/security/advisories/GHSA-wm7w-r6qf-3c9w
- https://www.vulncheck.com/advisories/quickjs-ng-before-0.16.0-memory-leak-via-atomics-store

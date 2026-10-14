# Frontend CVE Summary (2026-10-14)

## Overview

- 取得日時: 2026-10-14 10:09:47 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 11
- Critical: 2
- High: 1
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-102989](https://github.com/TanStack/router/commit/d521abd71c69f1ff010bb3def4d417cb5fa058cb)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-102989
- 関連キーワード: react, vue, gin
- 影響製品: -
- 公開日: 2026-10-14 02:17:14 JST
- 更新日: 2026-10-14 02:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TanStack Startのサーバー関数処理におけるレスポンス検証不備の脆弱性。未認証の攻撃者がリクエストペイロードに非公開フィールドを挿入し、特定のサーバー関数URLを介して応答オブジェクトを偽装できます。
- 影響: アプリケーションと同一オリジン上で攻撃者が制御するHTMLやスクリプトが実行され、ユーザーのデータ閲覧や不正リクエストの送信（XSS）が行われる可能性があります。
- 推奨対応: @tanstack/start-server-core 1.169.39、@tanstack/react-start 1.168.60、@tanstack/solid-start 1.168.57、@tanstack/vue-start 1.168.56 以降の安全なバージョンへアップデートしてください。

#### References
- https://github.com/TanStack/router/commit/d521abd71c69f1ff010bb3def4d417cb5fa058cb
- https://github.com/TanStack/router/pull/8573
- https://github.com/TanStack/router/releases/tag/release-2026-09-30-1747
- https://github.com/TanStack/router/security/advisories/GHSA-qx66-fv34-fjm8

### [CVE-2026-102981](https://github.com/makeplane/plane/commit/6220ba990b2276a1a1979d1d5df68f650b8b47ad)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-102981
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-10-14 01:17:10 JST
- 更新日: 2026-10-14 01:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: セルフホスト型Planeの招待エンドポイントにおける不適切なアクセス制御の脆弱性。未認証のGETリクエストで招待トークンが直接公開されています。
- 影響: 外部の第三者が他者宛ての招待トークンを取得してワークスペースに参加し、本来付与されるべき権限を不正に獲得する可能性があります。
- 推奨対応: Planeをバージョン 1.4.0 以降へアップデートしてください。

#### References
- https://github.com/makeplane/plane/commit/6220ba990b2276a1a1979d1d5df68f650b8b47ad
- https://github.com/makeplane/plane/pull/9297
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-gf48-p6jp-cwc4

### [CVE-2026-106108](https://github.com/quasarframework/quasar/commit/cdd4daeec839215540221122763c7a17cd478abc)

> **Frontend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-106108
- 関連キーワード: vue, vite
- 影響製品: -
- 公開日: 2026-10-14 00:17:31 JST
- 更新日: 2026-10-14 06:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Quasar Framework (@quasar/app-vite SSG) におけるパス検証不備（ディレクトリトラバーサル）の脆弱性。getSsgPages()の出力パス結合時に検証が行われません。
- 影響: ビルド処理時に意図しないディレクトリトラバーサルが発生し、ビルド実行ユーザーの権限で出力ツリー外部にファイルやディレクトリが作成される可能性があります。
- 推奨対応: Quasar Framework (@quasar/app-vite) を 3.3.0 以降へアップデートしてください。

#### References
- https://github.com/quasarframework/quasar/commit/cdd4daeec839215540221122763c7a17cd478abc
- https://github.com/quasarframework/quasar/releases/tag/@quasar/app-vite-v3.3.0
- https://github.com/quasarframework/quasar/security/advisories/GHSA-vhhq-m2gm-rwc9

### [CVE-2026-100133](https://www.adobe.com/trust/security/products/commerce/apsb26-153.html)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-100133
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-14 04:17:39 JST
- 更新日: 2026-10-14 04:17:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Adobe Commerceにおける格納型クロスサイトスクリプティング（Stored XSS）の脆弱性。フォームフィールドにおける入力入力検証不備に起因します。
- 影響: 悪意あるスクリプトが保存され、該当ページを開いた被害者のブラウザ上で実行されることで、アカウントやセッションの制御を奪われる可能性があります。
- 推奨対応: Adobeが提供する最新のセキュリティ修正パッチの適用、または最新バージョンへの更新を実施してください。

#### References
- https://www.adobe.com/trust/security/products/commerce/apsb26-153.html

### [CVE-2026-110118](https://github.com/risesoft-y9/WorkFlow-Engine/blob/v9.6.11/y9-module-flowableui/risenet-y9boot-support-flowableui/src/main/java/net/risesoft/controller/buttonOperation/ButtonOperationRestController.java#L1035-L1054)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-110118
- 関連キーワード: vue, gin
- 影響製品: -
- 公開日: 2026-10-14 02:17:36 JST
- 更新日: 2026-10-14 02:17:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WorkFlow-Engineのエンドポイント (/vue/buttonOperation) における認可欠如の脆弱性。taskIdのチェックが不適切です。
- 影響: 低権限の認証済みユーザーが他ユーザーのタスクIDを指定することで、他人のワークフロータスクを不正に承認・再割り当てする可能性があります。
- 推奨対応: 9.6.11より後の修正済みバージョンへの更新、または該当エンドポイントでの適切なアクセス権限チェックを実装してください。

#### References
- https://github.com/risesoft-y9/WorkFlow-Engine/blob/v9.6.11/y9-module-flowableui/risenet-y9boot-support-flowableui/src/main/java/net/risesoft/controller/buttonOperation/ButtonOperationRestController.java#L1035-L1054
- https://github.com/risesoft-y9/WorkFlow-Engine/blob/v9.6.11/y9-module-flowableui/risenet-y9boot-support-flowableui/src/main/java/net/risesoft/controller/buttonOperation/ButtonOperationRestController.java#L216-L252
- https://github.com/risesoft-y9/WorkFlow-Engine/blob/v9.6.11/y9-module-processadmin/risenet-y9boot-support-processadmin/src/main/java/net/risesoft/service/impl/CustomTaskServiceImpl.java#L76-L79
- https://hackmd.io/@1ExmmukzRMWN7B4gQ4W-4Q/workflow-engine-task-op-missing-authz
- https://www.vulncheck.com/advisories/workflow-engine-through-9.6.11-missing-authorization-via-flowableui-buttonoperation-endpoints

### [CVE-2026-104250](https://github.com/Unstructured-IO/unstructured/commit/cda16b3f2170019be9c6ea5635946fb3eaa2d66f)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-104250
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-14 02:17:15 JST
- 更新日: 2026-10-14 02:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Python `unstructured` ライブラリでのHTML出力時におけるエスケープ処理不足の脆弱性。`metadata.text_as_html` 等で危険なタグや `javascript:` リンクが残存します。
- 影響: 生成されたHTMLをブラウザや管理画面で開いた際、任意のスクリプトが実行され、閲覧者のコンテキストでXSSが発生する可能性があります。
- 推奨対応: unstructured ライブラリを 0.24.1 以降へアップデートしてください。

#### References
- https://github.com/Unstructured-IO/unstructured/commit/cda16b3f2170019be9c6ea5635946fb3eaa2d66f
- https://github.com/Unstructured-IO/unstructured/pull/4394
- https://github.com/Unstructured-IO/unstructured/releases/tag/0.24.1
- https://github.com/Unstructured-IO/unstructured/security/advisories/GHSA-v5mq-3xhg-98m9

### [CVE-2026-49264](https://github.com/oauthlib/oauthlib/commit/c888359f3c42bec235b2c5caab2069c9ed62457c)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-49264
- 関連キーワード: javascript, python, gin
- 影響製品: -
- 公開日: 2026-10-14 01:17:20 JST
- 更新日: 2026-10-14 01:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Python `OAuthLib` の `RevocationEndpoint` におけるJSONPコールバック名の検証不備（`enable_jsonp=True` 設定時のみ発生）。
- 影響: JSONP機能を有効にしている場合、不正なコールバック名を反射させることで、読み込み元アプリケーションの同一オリジン上で任意のJavaScriptが実行される可能性があります。
- 推奨対応: OAuthLibを 4.0.0 以降へアップデートするか、不要であれば `enable_jsonp` 設定を無効（デフォルト）に維持してください。

#### References
- https://github.com/oauthlib/oauthlib/commit/c888359f3c42bec235b2c5caab2069c9ed62457c
- https://github.com/oauthlib/oauthlib/pull/951
- https://github.com/oauthlib/oauthlib/releases/tag/v4.0.0
- https://github.com/oauthlib/oauthlib/security/advisories/GHSA-hj66-6f7g-4r5v

### [CVE-2026-102342](https://github.com/rust-ammonia/ammonia/commit/9394bd81179e756cb911314deabd943f1a9c8989)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-102342
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-14 00:17:30 JST
- 更新日: 2026-10-14 06:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Rust向けHTMLサニタイズライブラリ `ammonia` におけるSVGアニメーション要素の不適切な無害化処理の脆弱性。
- 影響: SVGの `animate` や `set` 要素を許容している場合、`javascript:` 属性を含むリンクが除去されずに残り、ユーザーのクリック時にXSSが実行される可能性があります。
- 推奨対応: ammonia を 3.3.3、4.0.3、または 4.1.4 以降へアップデートしてください。

#### References
- https://github.com/rust-ammonia/ammonia/commit/9394bd81179e756cb911314deabd943f1a9c8989
- https://github.com/rust-ammonia/ammonia/commit/9e3335e2dd8ab07346ff7997f20662a3da4023f6
- https://github.com/rust-ammonia/ammonia/commit/d2ae1547f478bd84d158bc5e57f5d31437dc4d8d
- https://github.com/rust-ammonia/ammonia/pull/250
- https://github.com/rust-ammonia/ammonia/pull/251

### [CVE-2026-110106](https://github.com/dromara/RuoYi-Vue-Plus)

> **Frontend** / **MEDIUM** / CVSS: **4.2** / KEV: **no**

- タイトル: CVE-2026-110106
- 関連キーワード: vue, gin
- 影響製品: -
- 公開日: 2026-10-14 02:17:34 JST
- 更新日: 2026-10-14 02:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RuoYi-Vue-Plusにおける不適切な直接オブジェクト参照（IDOR）の脆弱性。`/auth/unlock/{socialId}` に対するパラメータ検証が不足しています。
- 影響: 認証済みユーザーが他人の `socialId` を送信することで、他ユーザーのソーシャルログイン連携（GitHub、WeChat、Gitee等）やOAuthトークンを不正に削除する可能性があります。
- 推奨対応: 修正されたバージョンへ更新するか、リクエスト送信者の所有権チェックを追加してください。

#### References
- https://github.com/dromara/RuoYi-Vue-Plus
- https://github.com/dromara/RuoYi-Vue-Plus/blob/7180b529776834fee912113b23f0bd7a387a8222/ruoyi-admin/src/main/java/org/dromara/web/controller/AuthController.java#L156-L162
- https://github.com/dromara/RuoYi-Vue-Plus/blob/7180b529776834fee912113b23f0bd7a387a8222/ruoyi-modules/ruoyi-system/src/main/java/org/dromara/system/service/impl/SysSocialServiceImpl.java#L116-L118
- https://hackmd.io/@1ExmmukzRMWN7B4gQ4W-4Q/ruoyi-vue-plus-social-unbind-idor
- https://www.vulncheck.com/advisories/ruoyi-vue-plus-through-6.0.0-idor-via-delete-auth-unlock-socialid

### [CVE-2026-102672](https://github.com/electron/electron/commit/01faabfc250801a980fc94d64608046c67fc1cd9)

> **Frontend** / **MEDIUM** / CVSS: **6.7** / KEV: **no**

- タイトル: CVE-2026-102672
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-14 01:17:09 JST
- 更新日: 2026-10-14 06:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: macOS版Electronにおける Squirrel.Mac 自動更新ヘルパー（ShipIt）のローカル競合状態（レースコンディション）の脆弱性。
- 影響: ローカルの攻撃者がルート権限でのファイル書き込み先を書き換え、他アプリケーションのファイルを上書き・破壊する可能性があります。
- 推奨対応: Electron を 39.8.10、41.10.5、または 42.0.0-beta.2 以降の安全なバージョンへアップデートしてください。

#### References
- https://github.com/electron/electron/commit/01faabfc250801a980fc94d64608046c67fc1cd9
- https://github.com/electron/electron/commit/15e2928a5c5f01759107b414010e220d90d59cef
- https://github.com/electron/electron/commit/a0f9ff4cc0340545008424232d49caadd9c0c767
- https://github.com/electron/electron/commit/b8f25c4cedb2e0f5f475912b709aba19c57c26be
- https://github.com/electron/electron/pull/50745

### [CVE-2026-110101](https://github.com/benjaminjonard/koillection/blob/1.8.4/src/Entity/Datum.php#L141-L145)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-110101
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-14 02:17:33 JST
- 更新日: 2026-10-14 02:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Koillection 1.8.4以前における、添付ファイルアップロード時のMIME制限不足に起因する格納型XSSの脆弱性。
- 影響: 認証された攻撃者が悪意のあるHTMLファイルをアップロードし、アクセスした被害者のセッション上で任意のJavaScriptを実行する可能性があります。
- 推奨対応: 修正されたバージョンへのアップデート、または適切なファイル形式の検証とレスポンスヘッダの設定を検討してください。

#### References
- https://github.com/benjaminjonard/koillection/blob/1.8.4/src/Entity/Datum.php#L141-L145
- https://github.com/benjaminjonard/koillection/blob/1.8.4/src/Service/ImageHandler.php#L43-L50
- https://github.com/benjaminjonard/koillection/issues/1609
- https://github.com/benjaminjonard/koillection/releases/tag/1.8.4
- https://www.vulncheck.com/advisories/koillection-through-1.8.4-stored-xss-via-datum-file-attachment-uploads

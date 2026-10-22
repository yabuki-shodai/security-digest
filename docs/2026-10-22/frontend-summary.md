# Frontend CVE Summary (2026-10-22)

## Overview

- 取得日時: 2026-10-22 09:38:23 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 19
- Critical: 1
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-114139](https://github.com/getsentry/sentry-javascript/commit/878b685c85dc12045e47e1932c96f5381d7ac532)

> **Frontend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-114139
- 関連キーワード: javascript, nextjs, webpack
- 影響製品: -
- 公開日: 2026-10-22 06:17:56 JST
- 更新日: 2026-10-22 06:17:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: @sentry/nextjs の webpack 統合において、`tunnelRoute` 使用時に特定パスへのリクエストでアプリケーションミドルウェアがスキップされる不具合。
- 影響: 認可制御をミドルウェアのみに依存している場合、未認証の攻撃者が保護されたルートへアクセスできる可能性があります。
- 推奨対応: Sentry SDK を 9.47.2、10.75.2、または 11.0.0-rc.1 以降の修正済みバージョンに更新してください。

#### References
- https://github.com/getsentry/sentry-javascript/commit/878b685c85dc12045e47e1932c96f5381d7ac532
- https://github.com/getsentry/sentry-javascript/commit/c122aac4f29541eb6da494296822c91eab3cf5ae
- https://github.com/getsentry/sentry-javascript/commit/d525a2f6015b47384bc139c30d58e0d5435d52e5
- https://github.com/getsentry/sentry-javascript/pull/24499
- https://github.com/getsentry/sentry-javascript/pull/24565

### [CVE-2026-113787](https://github.com/GitHubNewbie0/odf-kit/commit/fa3abc5a7a757f56c7212b2dbe99d1d2db995420)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-113787
- 関連キーワード: typescript, javascript, go, gin
- 影響製品: -
- 公開日: 2026-10-22 01:17:26 JST
- 更新日: 2026-10-22 07:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: odf-kit の HTML レンダラーにおいて、インライン CSS スタイル生成時の HTML エスケープが不十分な問題。
- 影響: 悪意のあるスタイルの埋め込みにより属性が不正に終了し、クロスサイトスクリプティング（XSS）等の不具合を引き起こす可能性があります。
- 推奨対応: odf-kit を 0.14.2 以降に更新してください。

#### References
- https://github.com/GitHubNewbie0/odf-kit/commit/fa3abc5a7a757f56c7212b2dbe99d1d2db995420
- https://github.com/GitHubNewbie0/odf-kit/security/advisories/GHSA-3cgg-c5pp-57h6

### [CVE-2026-107588](https://github.com/highcharts/highcharts/security/advisories/GHSA-35rr-xwfh-x789)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-107588
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-10-22 04:16:57 JST
- 更新日: 2026-10-22 04:16:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vaadin Charts にバンドルされた Highcharts ライブラリにおける複数の既知の脆弱性（プロトタイプ汚染および XSS）。
- 影響: 攻撃者制御のデータがチャート設定に渡された場合、スクリプト実行やプロトタイプ汚染が発生する可能性があります。
- 推奨対応: 修正済みの Vaadin バージョンへ更新するか、提供されている回避策を適用してください。

#### References
- https://github.com/highcharts/highcharts/security/advisories/GHSA-35rr-xwfh-x789
- https://github.com/highcharts/highcharts/security/advisories/GHSA-5793-x2q3-c3q7
- https://github.com/highcharts/highcharts/security/advisories/GHSA-65hg-cf3f-5m39
- https://github.com/highcharts/highcharts/security/advisories/GHSA-gfvx-2c2g-38wq
- https://github.com/highcharts/highcharts/security/advisories/GHSA-mw4f-gj5x-6xr4

### [CVE-2026-114126](https://github.com/storybookjs/storybook/commit/243c06bf8f1e2f09446c44868ea100261e1374da)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-114126
- 関連キーワード: vite, vitest
- 影響製品: -
- 公開日: 2026-10-22 03:17:25 JST
- 更新日: 2026-10-22 03:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Storybook の開発サーバーが WebSocket 認証トークンを同一 LAN 上のクライアントに漏洩する脆弱性。
- 影響: LAN 上の攻撃者がトークンを取得し、ファイルを書き換えたり Vitest アドオン経由で任意のコードを実行したりする可能性があります。
- 推奨対応: Storybook を 8.6.19、9.1.21、10.6.2、または 11.0.0-alpha.6 以降に更新してください。

#### References
- https://github.com/storybookjs/storybook/commit/243c06bf8f1e2f09446c44868ea100261e1374da
- https://github.com/storybookjs/storybook/commit/3be03ec6f11f4616471cebc3fc65c13e1bf8c178
- https://github.com/storybookjs/storybook/commit/5540f03b209cc56c66f56a9c7cb4b2ee5b883ce5
- https://github.com/storybookjs/storybook/commit/a9ef9345d73224c73e0b81dc2701ec5b465ea9bb
- https://github.com/storybookjs/storybook/commit/d9b09e332510a88689c71ecc081bbbc2d072476e

### [CVE-2026-113779](https://github.com/pfrest/pfSense-pkg-RESTAPI/releases/tag/v2.9.0)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-113779
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-10-22 00:17:16 JST
- 更新日: 2026-10-22 01:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pfSense-pkg-RESTAPI において、設定同期権限を持つユーザーに対するアクセス制御が不適切な脆弱性。
- 影響: 設定同期権限を持つ認証済み非管理者ユーザーが REST API シークレットを変更し、完全な管理者権限に昇格する可能性があります。
- 推奨対応: pfSense-pkg-RESTAPI を 2.9.0 以降に更新してください。

#### References
- https://github.com/pfrest/pfSense-pkg-RESTAPI/releases/tag/v2.9.0
- https://github.com/pfrest/pfSense-pkg-RESTAPI/security/advisories/GHSA-8q8g-9f77-8g8g

### [CVE-2026-114130](https://github.com/nuxt/nuxt/commit/355ed9565127ff9b1453deb7160059ed55b3cb85)

> **Frontend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-114130
- 関連キーワード: javascript, vue, nuxt, gin
- 影響製品: -
- 公開日: 2026-10-22 03:17:25 JST
- 更新日: 2026-10-22 03:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nuxt（ページ無効化構成時）の `NuxtLink` において、制御文字プレフィックス付きの不審な URL 処理に起因する脆弱性（CVE-2026-53722の不完全な修正）。
- 影響: ユーザーがリンクをクリックした場合、そのオリジン上で意図しない JavaScript が実行される（XSS）可能性があります。
- 推奨対応: Nuxt を 4.6.0 以降に更新してください。

#### References
- https://github.com/nuxt/nuxt/commit/355ed9565127ff9b1453deb7160059ed55b3cb85
- https://github.com/nuxt/nuxt/commit/df46569d5d3c7a7799de54c328634168fbae70bb
- https://github.com/nuxt/nuxt/pull/36459
- https://github.com/nuxt/nuxt/releases/tag/v4.6.0
- https://github.com/nuxt/nuxt/security/advisories/GHSA-jjm6-p2m9-9w4x

### [CVE-2026-114131](https://github.com/nuxt/nuxt/commit/81f86ac5ee82bb1a9b887e59f3bc84624d711497)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-114131
- 関連キーワード: vue, nuxt, swr
- 影響製品: -
- 公開日: 2026-10-22 03:17:25 JST
- 更新日: 2026-10-22 03:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nuxt において、パーセントエンコードされたパス判定とルート解決のミスマッチによりルート規則（routeRules）が適用されない不具合。
- 影響: サーバーレンダリング時にミドルウェア等がスキップされ、未認証ユーザーに保護されたページや SSR データが取得される可能性があります。
- 推奨対応: Nuxt を 3.21.4 または 4.4.4 以降に更新してください。

#### References
- https://github.com/nuxt/nuxt/commit/81f86ac5ee82bb1a9b887e59f3bc84624d711497
- https://github.com/nuxt/nuxt/commit/9123ed850c468a7424a868c20d0d49a5507d32e5
- https://github.com/nuxt/nuxt/releases/tag/v3.21.11
- https://github.com/nuxt/nuxt/releases/tag/v4.5.2
- https://github.com/nuxt/nuxt/security/advisories/GHSA-6gq8-jgmh-3ffp

### [CVE-2026-114133](https://github.com/nuxt/nuxt/commit/493565e99451a0f52330b1f6b979254a4a39e5d0)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-114133
- 関連キーワード: vue, nuxt, gin
- 影響製品: -
- 公開日: 2026-10-22 03:17:26 JST
- 更新日: 2026-10-22 03:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nuxt の `NuxtIsland` レンダラーにおける `useHeadSafe` 入力のサニタイズ処理不備。
- 影響: 許可リストで無効化されるべき属性やスクリプトがページヘッドに挿入され、格納型クロスサイトスクリプティング（XSS）が発生する可能性があります。
- 推奨対応: Nuxt を 4.6.2 以降に更新してください。

#### References
- https://github.com/nuxt/nuxt/commit/493565e99451a0f52330b1f6b979254a4a39e5d0
- https://github.com/nuxt/nuxt/releases/tag/v4.6.2
- https://github.com/nuxt/nuxt/security/advisories/GHSA-xfq5-w38q-pc2x

### [CVE-2026-114492](https://github.com/flipped-aurora/gin-vue-admin/blob/v2.9.2-stable/server/api/v1/system/auto_code_plugin.go#L209-L219)

> **Frontend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-114492
- 関連キーワード: vue, gin
- 影響製品: -
- 公開日: 2026-10-22 03:17:27 JST
- 更新日: 2026-10-22 03:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: gin-vue-admin の `/autoCode/removePlugin` エンドポイントにおけるパストラバーサルの脆弱性。
- 影響: 認証された管理者が `pluginName` パラメータにトラバーサルシーケンスを指定することで、サーバープロセスが書き込み可能な任意のディレクトリを再帰的に削除できる可能性があります。
- 推奨対応: 最新の修正版へ更新するか、該当エンドポイントでの入力検証を強化してください。

#### References
- https://github.com/flipped-aurora/gin-vue-admin/blob/v2.9.2-stable/server/api/v1/system/auto_code_plugin.go#L209-L219
- https://github.com/flipped-aurora/gin-vue-admin/blob/v2.9.2-stable/server/service/system/auto_code_plugin.go#L371-L390
- https://github.com/flipped-aurora/gin-vue-admin/security/advisories/GHSA-mqv7-9mvf-h9fh
- https://www.vulncheck.com/advisories/gin-vue-admin-through-2.9.2-path-traversal-via-removeplugin-endpoint

### [CVE-2026-114132](https://github.com/nuxt/nuxt/commit/f6cfee52cf9576ddc4f4ee83b486969328b358f8)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-114132
- 関連キーワード: vue, nuxt
- 影響製品: -
- 公開日: 2026-10-22 03:17:26 JST
- 更新日: 2026-10-22 03:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nuxt のページ解決（大文字小文字不問）と Nitro のルート規則判定（大文字小文字区別）における一致不全。
- 影響: パスの大文字小文字を変えたリクエストにより、意図したリダイレクトやセキュリティヘッダー等のサーバー規則が適用されない可能性があります。
- 推奨対応: Nuxt を 4.6.2 以降に更新するか、`nuxt.config` で `router.options.sensitive: true` を設定してください。

#### References
- https://github.com/nuxt/nuxt/commit/f6cfee52cf9576ddc4f4ee83b486969328b358f8
- https://github.com/nuxt/nuxt/releases/tag/v4.6.2
- https://github.com/nuxt/nuxt/security/advisories/GHSA-vjh5-4x84-xrqp

### [CVE-2026-114128](https://github.com/withastro/astro/commit/a548223607b9bb146d5d90ddda495343f9a2a739)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-114128
- 関連キーワード: javascript, gin, express
- 影響製品: -
- 公開日: 2026-10-22 03:17:25 JST
- 更新日: 2026-10-22 03:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AstroのJSX/MDXレンダリングにおいて、scriptおよびstyle要素内の文字列が適切にエスケープされない問題。
- 影響: 動的入力に閉じタグ等が含まれていた場合、要素が終了されて任意のHTMLやJavaScriptが注入され、XSSが実行される可能性があります。
- 推奨対応: Astroをバージョン7.3.2以降へ更新してください。

#### References
- https://github.com/withastro/astro/commit/a548223607b9bb146d5d90ddda495343f9a2a739
- https://github.com/withastro/astro/pull/17896
- https://github.com/withastro/astro/releases/tag/astro@7.3.2
- https://github.com/withastro/astro/security/advisories/GHSA-98hj-9722-w3j8

### [CVE-2026-113796](https://github.com/electron/electron/commit/079b9b1594ee62c336adc3aa430d4c1cf62bd51e)

> **Frontend** / **MEDIUM** / CVSS: **4.2** / KEV: **no**

- タイトル: CVE-2026-113796
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-22 02:18:24 JST
- 更新日: 2026-10-22 02:18:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Electronにおいて、新しいウィンドウを開く際のナビゲーション開始元の判定処理に不備が存在する問題。
- 影響: SameSite=Strictクッキーが意図せず送信され、信頼できないコンテンツからCSRF保護を迂回したリクエストが行われる可能性があります。
- 推奨対応: Electronを42.11.3、43.7.0、44.3.0、または45.0.0-alpha.6以降に更新してください。

#### References
- https://github.com/electron/electron/commit/079b9b1594ee62c336adc3aa430d4c1cf62bd51e
- https://github.com/electron/electron/commit/0e6aca0618eeae50a18cfd50548b8688820629ed
- https://github.com/electron/electron/commit/652ef79ac79c6767b31e59b2f28d0d46114645e5
- https://github.com/electron/electron/commit/98940cb274bb6adcb7cdb2da2d4495ac83119670
- https://github.com/electron/electron/commit/a86ae4205ba2ba7ae60a6caa9d5d3a44321f2f9b

### [CVE-2026-113798](https://github.com/electron/electron/commit/076c7496791a45968cf8d9e76e9657bc161ea979)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-113798
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-22 02:18:24 JST
- 更新日: 2026-10-22 02:18:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Electronにおいて、クロスオリジンiframeからのpointerLock権限要求時にリクエスト送信元が誤判定される問題。
- 影響: 信頼できないiframeに対して、トップレベルページの識別子でpointerLock権限が誤って許可される可能性があります。
- 推奨対応: Electronを42.11.9、43.7.6、44.5.0、または45.0.0-alpha.13以降に更新してください。

#### References
- https://github.com/electron/electron/commit/076c7496791a45968cf8d9e76e9657bc161ea979
- https://github.com/electron/electron/commit/0b680cfa1ffa70a50282da53efde37a210d5223b
- https://github.com/electron/electron/commit/1755ee598697356959219beefee1e139bc3f8207
- https://github.com/electron/electron/commit/4073e9f4712f61e6b8abd5548673cc7638f6c1a1
- https://github.com/electron/electron/commit/a48e6eaaafa85b6fc40f7431ceec4fd6ef4bb899

### [CVE-2026-113800](https://github.com/electron/electron/commit/22de0a3a06cfd3174fc6c59c3810ab5e1c91bf1a)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-113800
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-22 02:18:25 JST
- 更新日: 2026-10-22 02:18:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Electronにおいて、iframeからのHIDおよびUSB権限チェック時に送信元オリジンが誤ってトップレベルのものとして渡される問題。
- 影響: 信頼できないクロスオリジンiframeに対して、トップレベルページ向けに意図されたHIDやUSBデバイスへのアクセス権限が付与される可能性があります。
- 推奨対応: Electronを42.11.3、43.7.0、44.3.0、または45.0.0-alpha.5以降に更新してください。

#### References
- https://github.com/electron/electron/commit/22de0a3a06cfd3174fc6c59c3810ab5e1c91bf1a
- https://github.com/electron/electron/commit/36042b2e1b1c60c67b05ba0e95d1a34f608b9742
- https://github.com/electron/electron/commit/56cc43eb677d46b86b0d3f49b5fba71404ab1ff0
- https://github.com/electron/electron/commit/922073f8601479e93071f56f0745041291b206fd
- https://github.com/electron/electron/commit/c965cee73284c4b230a81d51a7db6115e55da8c0

### [CVE-2026-114121](https://github.com/electron/electron/commit/25057643bf6d9a20bad69e45707551ccf546f5ce)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-114121
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-22 02:18:25 JST
- 更新日: 2026-10-22 02:18:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Electronにおいて、外部プロトコルURLの起動リクエストにおける送信元ドキュメントの帰属判定に失敗する問題。
- 影響: 信頼できないコンテンツからの要求であっても、OSに登録された外部アプリケーションが起動される可能性があります。
- 推奨対応: Electronを42.11.3、43.7.0、44.3.0、または45.0.0-alpha.5以降に更新してください。

#### References
- https://github.com/electron/electron/commit/25057643bf6d9a20bad69e45707551ccf546f5ce
- https://github.com/electron/electron/commit/8aa5414f73792ed3b2e3f9ab6391b1832e6dc2c3
- https://github.com/electron/electron/commit/92a783952891805f2f82f344c40a6917b98a7d98
- https://github.com/electron/electron/commit/e0a20d5277b567aea8603f8e9852a4341407a586
- https://github.com/electron/electron/commit/e3a400911084537bce7380ffea8af939572ce8dd

### [CVE-2026-114127](https://github.com/withastro/astro/commit/0b4dc3a211910b589d3805ab4dfedf11b0e712bb)

> **Frontend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-114127
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-22 03:17:25 JST
- 更新日: 2026-10-22 03:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AstroのView Transition用CSS生成において、アニメーションプロパティ内の文字列エスケープが不十分な問題。
- 影響: 攻撃者制御の入力により任意のCSSルールが注入され、UIの改ざんやDOM属性情報の限定的な漏洩に繋がる可能性があります。
- 推奨対応: Astroをバージョン7.3.3以降へ更新してください。

#### References
- https://github.com/withastro/astro/commit/0b4dc3a211910b589d3805ab4dfedf11b0e712bb
- https://github.com/withastro/astro/pull/17970
- https://github.com/withastro/astro/releases/tag/astro@7.3.3
- https://github.com/withastro/astro/security/advisories/GHSA-mpr7-6m5w-76rw

### [CVE-2026-114122](https://github.com/electron/electron/commit/24d8dbc661c6a109476ae59e9a2740b35d005cf4)

> **Frontend** / **LOW** / CVSS: **3.9** / KEV: **no**

- タイトル: CVE-2026-114122
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-22 02:18:25 JST
- 更新日: 2026-10-22 02:18:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ElectronのwebContents.beginFrameSubscription処理において、GPUプロセスから受信したフレームデータの検証が不十分な問題。
- 影響: GPUプロセスでコード実行権限を持つ攻撃者により、メインプロセスで境界外メモリ読み取りが発生し、メモリ漏洩やアプリのクラッシュを引き起こす可能性があります。
- 推奨対応: Electronを42.11.6、43.7.3、44.4.3、または45.0.0-alpha.9以降に更新してください。

#### References
- https://github.com/electron/electron/commit/24d8dbc661c6a109476ae59e9a2740b35d005cf4
- https://github.com/electron/electron/commit/64ae597deda8956037387b439e6361f0fe936c86
- https://github.com/electron/electron/commit/8d48be150c3fd53b0d02854124bdb7858598799c
- https://github.com/electron/electron/commit/d496507ffa1693edaa704a4be130fbcb8ecb4ada
- https://github.com/electron/electron/commit/d7f87070a8d738e561245d1ade4d6fbb082db80a

### [CVE-2026-113797](https://github.com/electron/electron/commit/16e6103c1d84cd1c46336647b55e96414da501a4)

> **Frontend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-113797
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-22 02:18:24 JST
- 更新日: 2026-10-22 02:18:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Electronのchrome.tabs.query() APIにおいて、必要な権限を持たない拡張機能に対してもタブ情報を返してしまう問題。
- 影響: ロードされた拡張機能によって、セッション内にある全webContentsのURLおよびタイトルが取得される可能性があります。
- 推奨対応: Electronを42.11.1、43.5.1、44.1.1、または45.0.0-alpha.4以降に更新してください。

#### References
- https://github.com/electron/electron/commit/16e6103c1d84cd1c46336647b55e96414da501a4
- https://github.com/electron/electron/commit/5acc76667d32ff310d04f965b47983412ab6553c
- https://github.com/electron/electron/commit/b1eb86ca8f6fa39fe9d5fee21bb9a0bf591a6a3f
- https://github.com/electron/electron/commit/d6529d65e5f096cd45bbb2828febb2c6baa53921
- https://github.com/electron/electron/commit/f3ae30fab9aabfd445eedff4dd7a2f003eb1ff2f

### [CVE-2026-114124](https://github.com/electron/electron/commit/24d8dbc661c6a109476ae59e9a2740b35d005cf4)

> **Frontend** / **LOW** / CVSS: **3.9** / KEV: **no**

- タイトル: CVE-2026-114124
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-22 03:17:24 JST
- 更新日: 2026-10-22 03:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ElectronにおけるmacOS向けオフスクリーンレンダリング処理で、GPUプロセスからのフレームデータ検証が不十分な問題。
- 影響: GPUプロセスでコード実行権限を持つ攻撃者により、メインプロセスで境界外メモリの読み取りが発生し、情報漏洩やクラッシュが引き起こされる可能性があります。
- 推奨対応: Electronを42.11.6、43.7.3、44.4.3、または45.0.0-alpha.9以降に更新してください。

#### References
- https://github.com/electron/electron/commit/24d8dbc661c6a109476ae59e9a2740b35d005cf4
- https://github.com/electron/electron/commit/64ae597deda8956037387b439e6361f0fe936c86
- https://github.com/electron/electron/commit/8d48be150c3fd53b0d02854124bdb7858598799c
- https://github.com/electron/electron/commit/d496507ffa1693edaa704a4be130fbcb8ecb4ada
- https://github.com/electron/electron/commit/d7f87070a8d738e561245d1ade4d6fbb082db80a

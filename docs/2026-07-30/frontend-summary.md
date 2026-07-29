# Frontend CVE Summary (2026-07-30)

## Overview

- 取得日時: 2026-07-30 08:09:26 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 10
- Critical: 1
- High: 6
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-54660](https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-54660
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-07-30 00:16:25 JST
- 更新日: 2026-07-30 00:16:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: swagger-typescript-apiが外部$ref解決時に認証トークンを攻撃者制御のURLに送信する可能性。
- 影響: 開発者やCIのベアラートークンが漏洩する恐れ。
- 推奨対応: バージョン13.12.2以降にアップデートすること。

#### References
- https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de
- https://github.com/acacode/swagger-typescript-api/pull/1779
- https://github.com/acacode/swagger-typescript-api/releases/tag/v13.12.2
- https://github.com/acacode/swagger-typescript-api/security/advisories/GHSA-h754-fxp7-88wx

### [CVE-2026-54666](https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-54666
- 関連キーワード: typescript, javascript
- 影響製品: -
- 公開日: 2026-07-30 00:16:25 JST
- 更新日: 2026-07-30 00:16:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: swagger-typescript-apiのOpenAPIパスキーがテンプレートリテラルで適切にエスケープされず、攻撃者制御のパスでコード実行の可能性。
- 影響: 生成されたAPIクライアントのメソッド呼び出し時に任意コードが実行される恐れ。
- 推奨対応: バージョン13.12.2以降にアップデートすること。

#### References
- https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de
- https://github.com/acacode/swagger-typescript-api/pull/1779
- https://github.com/acacode/swagger-typescript-api/releases/tag/v13.12.2
- https://github.com/acacode/swagger-typescript-api/security/advisories/GHSA-w284-33mx-6g9v

### [CVE-2026-54661](https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-54661
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-07-30 00:16:25 JST
- 更新日: 2026-07-30 01:17:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: swagger-typescript-apiがHttpClientコンストラクタに攻撃者制御のURLをエスケープせずに埋め込み、コード注入を許す可能性。
- 影響: 生成されたHttpClientやApiのインスタンス生成時に任意コードが実行される恐れ。
- 推奨対応: バージョン13.12.2以降にアップデートすること。

#### References
- https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de
- https://github.com/acacode/swagger-typescript-api/pull/1779
- https://github.com/acacode/swagger-typescript-api/releases/tag/v13.12.2
- https://github.com/acacode/swagger-typescript-api/security/advisories/GHSA-38c3-wv3c-v3xj

### [CVE-2026-54662](https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-54662
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-07-30 00:16:25 JST
- 更新日: 2026-07-30 01:17:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: swagger-typescript-apiがfetchクライアントのbaseUrlに攻撃者制御のURLをエスケープせずに埋め込み、コード注入を許す可能性。
- 影響: 生成されたfetchクライアントモジュールのインポート時に任意コードが実行される恐れ。
- 推奨対応: バージョン13.12.2以降にアップデートすること。

#### References
- https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de
- https://github.com/acacode/swagger-typescript-api/pull/1779
- https://github.com/acacode/swagger-typescript-api/releases/tag/v13.12.2
- https://github.com/acacode/swagger-typescript-api/security/advisories/GHSA-hqj5-cw9f-rx67
- https://github.com/acacode/swagger-typescript-api/security/advisories/GHSA-hqj5-cw9f-rx67

### [CVE-2026-54664](https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-54664
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-07-30 00:16:25 JST
- 更新日: 2026-07-30 00:16:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: swagger-typescript-apiがTypeScriptのenum宣言に攻撃者制御のenum値をエスケープせずに埋め込み、コード注入を許す可能性。
- 影響: 生成されたモジュールのインポート時に任意コードが実行される恐れ。
- 推奨対応: バージョン13.12.2以降にアップデートすること。

#### References
- https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de
- https://github.com/acacode/swagger-typescript-api/pull/1779
- https://github.com/acacode/swagger-typescript-api/releases/tag/v13.12.2
- https://github.com/acacode/swagger-typescript-api/security/advisories/GHSA-5f94-x226-ccpm

### [CVE-2026-54663](https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-54663
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-07-30 00:16:25 JST
- 更新日: 2026-07-30 01:17:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: swagger-typescript-apiが外部$ref解決時に内部ネットワークやリンクローカルへのリクエスト制限を行わず、SSRFの可能性。
- 影響: 攻撃者制御のOpenAPI仕様により内部サービスへのアクセスが可能になる恐れ。
- 推奨対応: バージョン13.12.2以降にアップデートすること。

#### References
- https://github.com/acacode/swagger-typescript-api/commit/306d59acb8ffbb00f953f807b97234b21f51d9de
- https://github.com/acacode/swagger-typescript-api/pull/1779
- https://github.com/acacode/swagger-typescript-api/releases/tag/v13.12.2
- https://github.com/acacode/swagger-typescript-api/security/advisories/GHSA-x36r-4347-pm5x
- https://github.com/acacode/swagger-typescript-api/security/advisories/GHSA-x36r-4347-pm5x

### [CVE-2026-67595](https://github.com/webreinvent/vaahcms/commit/8d7898f7a385a5fade1180a9b664ff158d873129)

> **Frontend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-67595
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-30 07:16:52 JST
- 更新日: 2026-07-30 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: VaahCMSのOTPメールテンプレートに悪意あるJavaScriptが埋め込まれ、ブラウザで実行される可能性。
- 影響: リモート攻撃者がWebSocket経由でコマンド実行やキー入力の盗聴などを行える恐れ。
- 推奨対応: 影響バージョンの使用を避け、修正済みバージョンへの更新を検討すること。

#### References
- https://github.com/webreinvent/vaahcms/commit/8d7898f7a385a5fade1180a9b664ff158d873129
- https://github.com/webreinvent/vaahcms/pull/317
- https://www.vulncheck.com/advisories/vaahcms-malicious-javascript-supply-chain-via-security-otp-blade-php

### [CVE-2026-67428](https://github.com/flytohub/flyto-core/commit/0a0a528520ec18f5a21f1ddf858a71cc1edfb6e9)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-67428
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-07-30 04:16:52 JST
- 更新日: 2026-07-30 04:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Flyto2 CoreのHTTPモジュールがURL検証を適切に行わず、内部やメタデータエンドポイントへのSSRFを許す可能性。
- 影響: 攻撃者が内部ネットワークへの不正リクエストを送信できる恐れ。
- 推奨対応: バージョン2.26.7以降にアップデートすること。

#### References
- https://github.com/flytohub/flyto-core/commit/0a0a528520ec18f5a21f1ddf858a71cc1edfb6e9
- https://github.com/flytohub/flyto-core/releases/tag/v2.26.7
- https://github.com/flytohub/flyto-core/security/advisories/GHSA-pgwh-4jj4-qm8v

### [CVE-2026-3093](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-1-released/)

> **Frontend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-3093
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-30 05:17:03 JST
- 更新日: 2026-07-30 05:17:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: GitLab CE/EEの特定バージョンでユーザー入力の不適切なサニタイズにより、他ユーザーのブラウザで任意JavaScriptが実行される可能性。
- 影響: クロスサイトスクリプティング（XSS）攻撃のリスク。
- 推奨対応: 影響バージョンを修正済みバージョンにアップデートすること。

#### References
- https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-1-released/
- https://gitlab.com/gitlab-org/gitlab/-/work_items/591274
- https://hackerone.com/reports/3539833

### [CVE-2026-54705](https://github.com/arnog/mathlive/commit/5fe1c46153883f9ec0249a5c8c34e64aaae9cfb8)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-54705
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-30 03:16:54 JST
- 更新日: 2026-07-30 03:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: MathLiveが特定のLaTeXコマンドのテキスト内容を適切にエスケープせず、悪意あるJavaScriptが実行される可能性。
- 影響: 悪意ある入力により任意のJavaScriptが実行される恐れ。
- 推奨対応: バージョン0.110.0以降にアップデートすること。

#### References
- https://github.com/arnog/mathlive/commit/5fe1c46153883f9ec0249a5c8c34e64aaae9cfb8
- https://github.com/arnog/mathlive/issues/3028
- https://github.com/arnog/mathlive/security/advisories/GHSA-fm7p-gw32-828p
- https://github.com/arnog/mathlive/security/advisories/GHSA-fm7p-gw32-828p

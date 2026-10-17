# Frontend CVE Summary (2026-10-17)

## Overview

- 取得日時: 2026-10-17 09:23:10 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 2
- Critical: 1
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-111663](https://github.com/chaskiq/chaskiq/blob/2.0.3/app/controllers/graphql_controller.rb#L3-L33)

> **Frontend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-111663
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-10-17 03:17:48 JST
- 更新日: 2026-10-17 04:03:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Chaskiq 2.0.3以下における createUrlUpload GraphQL mutation の SSRF（サーバーサイドリクエストフォージェリ）の脆弱性。
- 影響: 未認証の遠隔攻撃者が内部ネットワークやクラウドインスタンスのメタデータなどの任意のURLにリクエストを送信し、応答を取得する可能性があります。
- 推奨対応: Chaskiq を最新バージョンへアップデートし、GraphQL の URL アップロード処理に対する入力検証やネットワーク制限を実施してください。

#### References
- https://github.com/chaskiq/chaskiq/blob/2.0.3/app/controllers/graphql_controller.rb#L3-L33
- https://github.com/chaskiq/chaskiq/blob/2.0.3/app/graphql/mutations/create_url_upload.rb#L29-L66
- https://hackmd.io/@hieuPenguinnn/chaskiq-unauthenticated-ssrf-oembed-url-upload
- https://www.vulncheck.com/advisories/chaskiq-through-2.0.3-ssrf-via-createurlupload-graphql-mutation

### [CVE-2026-111713](https://github.com/AmauriC/tarteaucitron.js/blob/v1.36.0/tarteaucitron.js#L2641-L2648)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-111713
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-17 03:17:55 JST
- 更新日: 2026-10-17 04:00:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: tarteaucitron.js 1.37.0 未満における属性検証不備に起因するクロスサイトスクリプティング（XSS）の脆弱性。
- 影響: CMS作成者などのマークアップ権限を持つ攻撃者が javascript: URL を含む data-url 属性を挿入し、サイトのオリジン上で任意のスクリプトを実行させる可能性があります。
- 推奨対応: tarteaucitron.js を 1.37.0 以降の安全なバージョンに更新してください。

#### References
- https://github.com/AmauriC/tarteaucitron.js/blob/v1.36.0/tarteaucitron.js#L2641-L2648
- https://github.com/AmauriC/tarteaucitron.js/commit/068653bd47f5d4a493251ca8e15bd2b0be9b544f
- https://github.com/AmauriC/tarteaucitron.js/compare/v1.36.0...v1.37.0
- https://github.com/AmauriC/tarteaucitron.js/releases/tag/v1.37.0
- https://www.vulncheck.com/advisories/tarteaucitron-js-before-1.37.0-xss-via-getelemattr-attribute-validation-mismatch

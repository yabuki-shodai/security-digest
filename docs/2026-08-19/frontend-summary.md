# Frontend CVE Summary (2026-08-19)

## Overview

- 取得日時: 2026-08-19 07:36:43 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 12
- Critical: 2
- High: 7
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-75926](https://github.com/gohugoio/hugo)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-75926
- 関連キーワード: babel, go, node.js
- 影響製品: -
- 公開日: 2026-08-19 01:18:24 JST
- 更新日: 2026-08-19 05:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HugoのTailwindCSS実行時におけるNode.jsパーミッションモデルの制御不備によるアクセス制限回避の脆弱性。
- 影響: 悪意のあるテーマやモジュールを含むサイトのビルド時に、ビルドを実行する権限で任意のシェルプロセスが生成され任意コードが実行される恐れがあります。
- 推奨対応: Hugoを修正済みバージョンへ更新するか、信頼できないサードパーティ製テーマやテンプレートのビルドを避けてください。

#### References
- https://github.com/gohugoio/hugo
- https://github.com/gohugoio/hugo/blob/v0.164.0/common/hexec/exec.go#L292-L295
- https://github.com/gohugoio/hugo/blob/v0.164.0/config/security/securityConfig.go#L72-L79
- https://github.com/gohugoio/hugo/commit/8a55df7af2e6da31297245cc54fa2e3b521d93e8
- https://github.com/gohugoio/hugo/issues/15178

### [CVE-2026-45118](https://github.com/mybb/mybb/releases/tag/mybb_1840)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-45118
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-19 01:17:06 JST
- 更新日: 2026-08-19 03:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MyBBのコンタクトモジュールにおけるリダイレクトURLおよびプロトコルの検証不備の脆弱性。
- 影響: オープンリダイレクトや反射型クロスサイトスクリプティング（XSS）が発生し、ユーザーのブラウザ上で任意のJavaScriptが実行される恐れがあります。
- 推奨対応: MyBBをバージョン 1.8.40 以降にアップデートしてください。

#### References
- https://github.com/mybb/mybb/releases/tag/mybb_1840
- https://github.com/mybb/mybb/security/advisories/GHSA-wf92-5q5h-qr53
- https://mybb.com/versions/1.8.40

### [CVE-2026-55839](https://github.com/kestra-io/kestra/commit/6c8e6d099ed172cbb6b003b7fb30b7bb1f8f710e)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-55839
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-19 01:17:53 JST
- 更新日: 2026-08-19 03:18:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KestraのカスタムMarkdownパーサーにおける特定のリンク構文の処理不備の脆弱性。
- 影響: Flow説明文を閲覧した他のユーザーのブラウザ上でJavaScriptイベントハンドラが実行される（蓄積型XSS）恐れがあります。
- 推奨対応: Kestraをバージョン 1.3.24 以降にアップデートしてください。

#### References
- https://github.com/kestra-io/kestra/commit/6c8e6d099ed172cbb6b003b7fb30b7bb1f8f710e
- https://github.com/kestra-io/kestra/pull/16835
- https://github.com/kestra-io/kestra/releases/tag/v1.3.24
- https://github.com/kestra-io/kestra/security/advisories/GHSA-34pm-923j-7wf8

### [CVE-2026-19869](https://github.com/neo4j/graphql/security/advisories/GHSA-82m8-p9px-c3x5)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-19869
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-08-19 02:16:57 JST
- 更新日: 2026-08-19 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: @neo4j/graphqlにおけるフィールドレベルの@authenticationルールの評価漏れの脆弱性。
- 影響: タイプレベルとフィールドレベルの認証規則が併用された際、フィールドレベルの規則が無視され、制限されたフィールドへ権限不足のユーザーがアクセスできる恐れがあります。
- 推奨対応: @neo4j/graphqlを修正済みの最新バージョンへ更新してください。

#### References
- https://github.com/neo4j/graphql/security/advisories/GHSA-82m8-p9px-c3x5
- https://neo4j.com/security/CVE-2026-19869

### [CVE-2026-45115](https://github.com/mybb/mybb/releases/tag/mybb_1840)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-45115
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-19 01:17:06 JST
- 更新日: 2026-08-19 03:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MyBBのBuddy/Ignore機能におけるユーザー名のサニタイズ不足（シングルクォートのエスケープ漏れ）の脆弱性。
- 影響: 特定の操作時に被害者のブラウザで JavaScript が実行される（XSS）恐れがあります。
- 推奨対応: MyBBをバージョン 1.8.40 以降にアップデートしてください。

#### References
- https://github.com/mybb/mybb/releases/tag/mybb_1840
- https://github.com/mybb/mybb/security/advisories/GHSA-p766-qqxv-rfc2
- https://mybb.com/versions/1.8.40

### [CVE-2026-45116](https://github.com/mybb/mybb/commit/c32f0c22baab704a68b8d58fcdd2f26fadbbe19b)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-45116
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-19 01:17:06 JST
- 更新日: 2026-08-19 03:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MyBBのユーザーデータハンドラにおけるプロフィールフィールドの入力検証不備の脆弱性。
- 影響: 不正な形式の入力値がサニタイズされずに保存・描画され、蓄積型クロスサイトスクリプティング（XSS）が発生する恐れがあります。
- 推奨対応: MyBBをバージョン 1.8.40 以降にアップデートしてください。

#### References
- https://github.com/mybb/mybb/commit/c32f0c22baab704a68b8d58fcdd2f26fadbbe19b
- https://github.com/mybb/mybb/releases/tag/mybb_1840
- https://github.com/mybb/mybb/security/advisories/GHSA-4p6g-p3qh-559v
- https://mybb.com/versions/1.8.40

### [CVE-2026-69189](https://github.com/hoppscotch/hoppscotch/commit/9cc980bc4feb1f8e139b23b9de0beed0db72d4b7)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-69189
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-08-19 00:17:00 JST
- 更新日: 2026-08-19 01:18:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HoppscotchのGraphQLエンドポイントおよびUserHistoryサービスにおける所有権検証不足の脆弱性。
- 影響: 認証済みのユーザーが同一ワークスペース内の他ユーザーのアクセス履歴、認証ヘッダー、環境変数などの不当な閲覧、変更、削除を行える恐れがあります。
- 推奨対応: Hoppscotchをバージョン 2026.6.0 以降にアップデートしてください。

#### References
- https://github.com/hoppscotch/hoppscotch/commit/9cc980bc4feb1f8e139b23b9de0beed0db72d4b7
- https://github.com/hoppscotch/hoppscotch/pull/6409
- https://github.com/hoppscotch/hoppscotch/releases/tag/2026.6.0
- https://github.com/hoppscotch/hoppscotch/security/advisories/GHSA-p25p-g9jp-7q46
- https://github.com/hoppscotch/hoppscotch/security/advisories/GHSA-p25p-g9jp-7q46

### [CVE-2026-71539](https://github.com/n8n-io/n8n/releases/tag/n8n@1.123.64)

> **Frontend** / **HIGH** / CVSS: **8.9** / KEV: **no**

- タイトル: CVE-2026-71539
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-19 00:17:01 JST
- 更新日: 2026-08-19 03:19:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: n8nのGitノード操作におけるシンボリックリンク置換に起因するファイル配置の脆弱性。
- 影響: コミュニティノードディレクトリ内に不正なリポジトリが配置され、再起動後にサーバー上で任意コードを実行される恐れがあります。
- 推奨対応: n8nをバージョン 1.123.64、2.29.8、または 2.30.1 以降にアップデートしてください。

#### References
- https://github.com/n8n-io/n8n/releases/tag/n8n@1.123.64
- https://github.com/n8n-io/n8n/releases/tag/n8n@2.29.8
- https://github.com/n8n-io/n8n/releases/tag/n8n@2.30.1
- https://github.com/n8n-io/n8n/security/advisories/GHSA-g3r5-9h93-4j2c

### [CVE-2026-75915](https://github.com/Hmbown/CodeWhale/commit/26de44a8bd5051f8f944ea60b2c37ae1d2b7d25e)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-75915
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-08-19 01:18:23 JST
- 更新日: 2026-08-19 01:18:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CodeWhaleのjs_executionツールにおける環境変数のクレンジング不備の脆弱性。
- 影響: 実行されたJavaScriptコードからprocess.envを通じて親プロセスのAPIキーや認証トークンなどの機密情報が漏洩する恐れがあります。
- 推奨対応: CodeWhaleをバージョン 0.8.64 以降にアップデートしてください。

#### References
- https://github.com/Hmbown/CodeWhale/commit/26de44a8bd5051f8f944ea60b2c37ae1d2b7d25e
- https://github.com/Hmbown/CodeWhale/security/advisories/GHSA-h539-c7r8-3xq4
- https://www.vulncheck.com/advisories/codewhale-before-environment-variable-leak-via-js-execution
- https://github.com/Hmbown/CodeWhale/security/advisories/GHSA-h539-c7r8-3xq4

### [CVE-2026-48744](https://github.com/saleor/saleor/commit/11efb4e9ea76942cf142bc01de8846cbaf764465)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-48744
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-08-19 02:16:57 JST
- 更新日: 2026-08-19 02:16:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Saleorの認可ユーティリティにおける検証ロジックの不備の脆弱性。
- 影響: 未認証のGraphQLリクエストによってチャンネル設定が誤って更新されたり、非公開に設定されたデータが漏洩する恐れがあります。
- 推奨対応: Saleorをバージョン 3.21.67、3.22.63、または 3.23.22 以降にアップデートしてください。

#### References
- https://github.com/saleor/saleor/commit/11efb4e9ea76942cf142bc01de8846cbaf764465
- https://github.com/saleor/saleor/commit/580b93b6e0faef7800e667f0c3bc507d3ef6f5f5
- https://github.com/saleor/saleor/commit/9b1f59b3ed86c3fad3ce071639cf434c1ab94a85
- https://github.com/saleor/saleor/commit/afd1ddd13b79e78db4e05f846b1f159078c50417
- https://github.com/saleor/saleor/releases/tag/3.21.67

### [CVE-2026-52606](https://github.com/kilotel/vulnerability-research/tree/main/CVE-2026-52606)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-52606
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-19 02:16:59 JST
- 更新日: 2026-08-19 04:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: reportico-web 8.1.0 以前における `run.php` の `loadTemplate` パラメータに起因する反射型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 攻撃者によって誘導されたユーザーのブラウザ上で任意コードを実行される可能性があります。
- 推奨対応: 製品を最新バージョンへアップデートするか、入力パラメータの検証および適切なエスケープ処理を実施してください。

#### References
- https://github.com/kilotel/vulnerability-research/tree/main/CVE-2026-52606
- https://github.com/reportico-web/reportico
- https://github.com/kilotel/vulnerability-research/tree/main/CVE-2026-52606

### [CVE-2026-73426](https://github.com/basecamp/trix/commit/3229c29c771ded4d247ed79b2ccd2cd05c4e74b4)

> **Frontend** / **MEDIUM** / CVSS: **4.6** / KEV: **no**

- タイトル: CVE-2026-73426
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-19 00:17:08 JST
- 更新日: 2026-08-19 03:19:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Trix 2.1.17 未満における DOMPurify サニタイザーのバイパスによるクロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 悪意のあるHTMLを描画することでユーザーセッション内で任意JavaScriptを実行され、不正操作や機密情報の漏洩に繋がる可能性があります。
- 推奨対応: Trix 2.1.17 以降へ更新してください。

#### References
- https://github.com/basecamp/trix/commit/3229c29c771ded4d247ed79b2ccd2cd05c4e74b4
- https://github.com/basecamp/trix/commit/53197ab5a142e6b0b76127cb790726b274eaf1bc
- https://github.com/basecamp/trix/pull/1282
- https://github.com/basecamp/trix/releases/tag/v2.1.17
- https://github.com/basecamp/trix/security/advisories/GHSA-qmpg-8xg6-ph5q

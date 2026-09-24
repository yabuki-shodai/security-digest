# Frontend CVE Summary (2026-09-24)

## Overview

- 取得日時: 2026-09-24 09:26:23 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 5
- High: 3
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-18872](https://www.ibm.com/support/pages/node/7288641)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-18872
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-09-24 01:16:41 JST
- 更新日: 2026-09-24 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Financial Transaction Manager (FTM) for RedHat OpenShift is vulnerable to stored cross-site scripting (CWE-79) in the FTM UI NetworkAcknowledgement React component (NetworkAcknowledgement.jsx:42). A malicious actor can inject script into stored network acknowledgement data that executes in authenticated operator br...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7288641

### [CVE-2026-96754](https://github.com/orval-labs/orval)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-96754
- 関連キーワード: typescript, javascript
- 影響製品: -
- 公開日: 2026-09-24 02:17:24 JST
- 更新日: 2026-09-24 02:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: orval versions before 8.29.0 contain a code injection vulnerability in the @orval/hono generator that fails to escape OpenAPI path values in single-quoted route literals. Attackers can craft an OpenAPI document with an apostrophe in a static path segment to inject arbitrary JavaScript code that executes when the genera...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/orval-labs/orval
- https://github.com/orval-labs/orval/blob/v8.28.1/packages/hono/src/index.ts#L169-L175
- https://github.com/orval-labs/orval/commit/155a5b7a38ff6886020cbc4c292db57c2793e6b6
- https://github.com/orval-labs/orval/commit/d346d94a660e50a2f8d0f7c17fee2c4c69d8dc23
- https://github.com/orval-labs/orval/pull/4006

### [CVE-2026-96755](https://github.com/orval-labs/orval)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-96755
- 関連キーワード: javascript, express
- 影響製品: -
- 公開日: 2026-09-24 02:17:24 JST
- 更新日: 2026-09-24 03:16:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: orval versions 8.14.0 through 8.28.1 contain a code injection vulnerability in the @orval/effect generator that converts OpenAPI schema defaults into template literals. Attackers can inject arbitrary JavaScript expressions via schema defaults containing ${...} syntax, which are executed at module scope when the generat...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/orval-labs/orval
- https://github.com/orval-labs/orval/blob/v8.28.1/packages/effect/src/index.ts#L298-L302
- https://github.com/orval-labs/orval/commit/d346d94a660e50a2f8d0f7c17fee2c4c69d8dc23
- https://github.com/orval-labs/orval/pull/3995
- https://github.com/orval-labs/orval/security/advisories/GHSA-q7f2-jg6j-r867

### [CVE-2026-96759](https://github.com/orval-labs/orval)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-96759
- 関連キーワード: javascript, tanstack query
- 影響製品: -
- 公開日: 2026-09-24 02:17:25 JST
- 更新日: 2026-09-24 03:16:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: orval before 8.29.0 fails to escape the operationId parameter when emitting it into generated TanStack Query mutator options metadata objects. Attackers can inject arbitrary JavaScript code through a crafted operationId in an OpenAPI specification that executes when generated hooks are called.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/orval-labs/orval
- https://github.com/orval-labs/orval/blob/v8.28.1/packages/query/src/query-generator.ts#L784
- https://github.com/orval-labs/orval/commit/b28c53f3e0c06190e0f6ea136737e6316432448f
- https://github.com/orval-labs/orval/pull/4008
- https://github.com/orval-labs/orval/security/advisories/GHSA-vv88-cm6j-665j

### [CVE-2026-96757](https://github.com/orval-labs/orval)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-96757
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-24 02:17:24 JST
- 更新日: 2026-09-24 03:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: orval before 8.29.0 fails to escape OpenAPI media-type keys when emitting them into single-quoted Content-Type string literals in generated code. Attackers can inject JavaScript through crafted media-type keys in OpenAPI specifications that executes when generated fetch operations or mock resolvers are invoked.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/orval-labs/orval
- https://github.com/orval-labs/orval/blob/v8.28.1/packages/fetch/src/index.ts#L584
- https://github.com/orval-labs/orval/commit/43af282d62dca0ef3140023741fb768f6a718adb
- https://github.com/orval-labs/orval/commit/a2d4af59f3b167dc8a7a65d15f51cdb89ebe2fe5
- https://github.com/orval-labs/orval/pull/4007

### [CVE-2026-93769](https://fluidattacks.com/advisories/cali)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-93769
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-09-24 01:16:48 JST
- 更新日: 2026-09-24 02:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HumHub 1.18.5 is affected by a stored cross-site scripting (XSS) vulnerability that allows any user holding the delegated, non-system-administrator Manage Users permission (admin_manage_users) to inject persistent HTML/JavaScript into a Profile Field Category title.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://fluidattacks.com/advisories/cali
- https://github.com/humhub/humhub
- https://github.com/humhub/humhub/pull/8499

### [CVE-2026-77394](https://github.com/OpenC3/cosmos/commit/10371f8f410b9ad588f98dfa3befaaacb6587cd3)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-77394
- 関連キーワード: vue, gin
- 影響製品: -
- 公開日: 2026-09-24 04:19:15 JST
- 更新日: 2026-09-24 05:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenC3 COSMOS provides the functionality needed to send commands to and receive data from one or more embedded systems. From 5.0.6 until 7.3.0, an authenticated actor with system_set permission can store a shared screen through POST /openc3-api/screen whose BUTTON widget action is evaluated by openc3-cosmos-init/plugin...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/OpenC3/cosmos/commit/10371f8f410b9ad588f98dfa3befaaacb6587cd3
- https://github.com/OpenC3/cosmos/pull/3560
- https://github.com/OpenC3/cosmos/releases/tag/v7.3.0
- https://github.com/OpenC3/cosmos/security/advisories/GHSA-gvf2-2rh5-mpgf
- https://github.com/OpenC3/cosmos/security/advisories/GHSA-gvf2-2rh5-mpgf

### [CVE-2026-61695](https://github.com/square/wire/commit/24043b6b3a5e5974a978f2745b76d50b31407c1c)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-61695
- 関連キーワード: swr
- 影響製品: -
- 公開日: 2026-09-24 04:17:32 JST
- 更新日: 2026-09-24 04:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Wire provides gRPC and protocol buffers for Android, Kotlin, Swift, and Java. Prior to 6.4.1 and 7.0.0-alpha04, Wire's Swift runtime ProtoReader.skipGroup(expectedEndTag:unknownFieldsWriter:) accepts a negative length for a LENGTH_DELIMITED field inside an unknown START_GROUP field. ProtoReader.readData() forwards the...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/square/wire/commit/24043b6b3a5e5974a978f2745b76d50b31407c1c
- https://github.com/square/wire/commit/81ff7f24a6795d9a8be2e03f272b2d979a5d2c7e
- https://github.com/square/wire/pull/3616
- https://github.com/square/wire/releases/tag/6.4.1
- https://github.com/square/wire/releases/tag/7.0.0-alpha04

### [CVE-2026-88974](https://github.com/wp-graphql/wp-graphql/commit/55441663eaa33c3f2e05de038c8286c845916461)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-88974
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-09-24 00:17:23 JST
- 更新日: 2026-09-24 03:12:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WPGraphQL provides a GraphQL API for WordPress sites. Prior to 2.22.2, the updatePost mutation in src/Mutation/PostObjectUpdate.php checks only the collection-level edit_posts capability and the post author, but does not enforce the object-level edit_post capability or require publish_posts for public status transition...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/wp-graphql/wp-graphql/commit/55441663eaa33c3f2e05de038c8286c845916461
- https://github.com/wp-graphql/wp-graphql/pull/4270
- https://github.com/wp-graphql/wp-graphql/releases/tag/wp-graphql%2Fv2.22.2
- https://github.com/wp-graphql/wp-graphql/security/advisories/GHSA-5mmc-8pc9-wggg
- https://github.com/wp-graphql/wp-graphql/security/advisories/GHSA-5mmc-8pc9-wggg

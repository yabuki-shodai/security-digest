# Frontend CVE Summary (2026-09-17)

## Overview

- 取得日時: 2026-09-17 09:24:01 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 15
- Critical: 0
- High: 8
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-61593](https://github.com/djust-org/djust/releases/tag/v1.0.7)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-61593
- 関連キーワード: react, django, go, gin
- 影響製品: -
- 公開日: 2026-09-17 01:17:13 JST
- 更新日: 2026-09-17 04:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: djust provides Phoenix LiveView-style reactive server-side rendering for Django with Rust-powered performance. Prior to version 1.0.7, the SSE client→server POST endpoints are `@csrf_exempt` and the SSE GET stream endpoint had no Origin check, so a cross-origin page could drive a victim-cookie-authenticated SSE session...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/djust-org/djust/releases/tag/v1.0.7
- https://github.com/djust-org/djust/security/advisories/GHSA-pg97-jvmf-qfvc

### [CVE-2026-61595](https://github.com/djust-org/djust/releases/tag/v1.0.7)

> **Frontend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-61595
- 関連キーワード: react, django, go
- 影響製品: -
- 公開日: 2026-09-17 01:17:14 JST
- 更新日: 2026-09-17 04:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: djust provides Phoenix LiveView-style reactive server-side rendering for Django with Rust-powered performance. Prior to version 1.0.7, `djust.tenants` isolation was enforced only on the HTTP path. The current tenant was stored in `threading.local()` and set exclusively by the HTTP-only `TenantMiddleware`, so on the liv...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/djust-org/djust/releases/tag/v1.0.7
- https://github.com/djust-org/djust/security/advisories/GHSA-3492-cvg7-9mr2

### [CVE-2026-84997](https://github.com/reactphp/http/commit/b6d4688790adf3797071fcf88a3fc4225f30486a)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-84997
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-09-17 00:18:00 JST
- 更新日: 2026-09-17 00:18:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: react/http is an event-driven, streaming HTTP client and server implementation for ReactPHP. From 0.6.0 until 1.11.1, React\Http\Io\ChunkedDecoder could enter an infinite loop while processing a malformed Transfer-Encoding: chunked body because handleData required its buffer to shrink on every iteration. An incomplete...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/reactphp/http/commit/b6d4688790adf3797071fcf88a3fc4225f30486a
- https://github.com/reactphp/http/releases/tag/v1.11.1
- https://github.com/reactphp/http/security/advisories/GHSA-x424-64qh-5j54
- https://github.com/reactphp/http/security/advisories/GHSA-x424-64qh-5j54

### [CVE-2026-68904](https://github.com/node-opcua/node-opcua/commit/1959cbb8946b386d2e24a1cce05b7148099d36e7)

> **Frontend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-68904
- 関連キーワード: typescript, go, gin, node.js
- 影響製品: -
- 公開日: 2026-09-17 02:18:00 JST
- 更新日: 2026-09-17 04:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: node-opcua is an OPC UA implementation for TypeScript and Node.js. From 2.0.0 until 2.170.0, node-opcua clients using the default keepSessionAlive setting can enter a repeated reconnection cycle when an OPC UA server's clock skew causes BadInvalidTimestamp responses. ClientSessionKeepAliveManager._ping_server treated t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/node-opcua/node-opcua/commit/1959cbb8946b386d2e24a1cce05b7148099d36e7
- https://github.com/node-opcua/node-opcua/commit/481664fa6ba8204737c5a92797ff68c3ae780c1c
- https://github.com/node-opcua/node-opcua/commit/4d59197e2dbd82791d7f36dad7da178715e0c27a
- https://github.com/node-opcua/node-opcua/commit/dc406fd2d364aa69dd173be21ed32a7ff425017a
- https://github.com/node-opcua/node-opcua/pull/1497

### [CVE-2026-84993](https://github.com/mikro-orm/mikro-orm/commit/3aba926fd07156f5e1ebf06294fd77ee1215bad5)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-84993
- 関連キーワード: typescript, go, node.js, express, postgresql, mysql, mongodb
- 影響製品: -
- 公開日: 2026-09-17 02:18:15 JST
- 更新日: 2026-09-17 03:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MikroORM is a TypeScript ORM for Node.js based on Data Mapper, Unit of Work and Identity Map patterns. Prior to 6.6.16 and 7.1.7, the shared SQL layer validates the field key of an orderBy clause but does not validate its direction value before AbstractSqlPlatform.getOrderByExpression concatenates it into an ORDER BY c...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mikro-orm/mikro-orm/commit/3aba926fd07156f5e1ebf06294fd77ee1215bad5
- https://github.com/mikro-orm/mikro-orm/commit/89e5546bf8e10f8465682016a3bdf622ff55d8c5
- https://github.com/mikro-orm/mikro-orm/pull/7996
- https://github.com/mikro-orm/mikro-orm/pull/7997
- https://github.com/mikro-orm/mikro-orm/releases/tag/v6.6.16

### [CVE-2026-69200](https://github.com/node-opcua/node-opcua/security/advisories/GHSA-cv5q-7543-48q4)

> **Frontend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-69200
- 関連キーワード: typescript, node.js
- 影響製品: -
- 公開日: 2026-09-17 02:18:01 JST
- 更新日: 2026-09-17 02:18:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: node-opcua is an OPC UA implementation for TypeScript and Node.js. Prior to node-opcua-client 2.145.0, the internal fieldsToJson method in packages/node-opcua-client/source/alarms_and_conditions/client_alarm.ts directly assigns unsanitized field names and allows a __proto__.pollutedKey path to modify Object.prototype....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/node-opcua/node-opcua/security/advisories/GHSA-cv5q-7543-48q4

### [CVE-2026-92565](https://github.com/lukevella/rallly)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-92565
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-09-17 00:19:01 JST
- 更新日: 2026-09-17 00:19:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Rallly before 4.15.0 contains an information disclosure vulnerability in the polls.get tRPC procedure that returns scheduled-event invitee names and email addresses to unauthenticated callers. Attackers can access a poll's urlId from public invite links to retrieve sensitive invitee information regardless of privacy se...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/lukevella/rallly
- https://github.com/lukevella/rallly/blob/885bfaf4313f427a60c5349646c5b69d863750db/apps/web/src/trpc/routers/polls.ts#L568-L675
- https://github.com/lukevella/rallly/commit/0db11a2cd9e48656d08773e4be6de0e7df584a00
- https://github.com/lukevella/rallly/pull/3247
- https://github.com/lukevella/rallly/releases/tag/v4.15.0

### [CVE-2026-84858](https://www.tenable.com/security/research/tra-2026-60)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-84858
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-17 00:18:00 JST
- 更新日: 2026-09-17 00:18:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ScadaLTS 2.8.1-release-candidate build 0 is affected by an Authenticated Remote Code Execution via Scripting Sandbox Bypass The DWR "DataSourceEditDwr" class exposes the "validateScript" method that compiles and executes attacker-supplied JavaScript via the Rhino scripting engine. There are no authorization checks on t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.tenable.com/security/research/tra-2026-60

### [CVE-2026-63671](https://github.com/nuxt-content/mdc/commit/61d636c2983f021288e4fc5c4006733b38cf0d53)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-63671
- 関連キーワード: javascript, vue, nuxt, gin
- 影響製品: -
- 公開日: 2026-09-17 00:17:40 JST
- 更新日: 2026-09-17 00:17:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MDC is a tool to take regular Markdown and write documents interacting deeply with a Vue component. Prior to 0.22.1, @nuxtjs/mdc uses parseMarkdown with allowDangerousHtml enabled by default and relies on validateProps, validateProp, and unsafeLinkPrefix to remove executable URLs from untrusted Markdown. validateProp c...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nuxt-content/mdc/commit/61d636c2983f021288e4fc5c4006733b38cf0d53
- https://github.com/nuxt-content/mdc/pull/491
- https://github.com/nuxt-content/mdc/releases/tag/v0.22.1
- https://github.com/nuxt-content/mdc/security/advisories/GHSA-mxm6-v9r6-r94c
- https://github.com/nuxt-content/mdc/security/advisories/GHSA-mxm6-v9r6-r94c

### [CVE-2026-63325](https://github.com/Redocly/redocly-cli/commit/d26d452368066be1400f43cea915dd9ea508e18b)

> **Frontend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-63325
- 関連キーワード: javascript, express
- 影響製品: -
- 公開日: 2026-09-17 04:17:24 JST
- 更新日: 2026-09-17 04:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Redocly CLI makes OpenAPI validation, linting, and documentation workflows easier. Prior to version 2.33.0 of @redocly/respect-core and @redocly/cli, the respect command dynamically evaluates $faker runtime expressions in Arazzo descriptions. A crafted expression can traverse constructor, prototype, or __proto__ proper...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Redocly/redocly-cli/commit/d26d452368066be1400f43cea915dd9ea508e18b
- https://github.com/Redocly/redocly-cli/pull/2881
- https://github.com/Redocly/redocly-cli/pull/2922
- https://github.com/Redocly/redocly-cli/releases/tag/@redocly/respect-core@1.34.17
- https://github.com/Redocly/redocly-cli/releases/tag/@redocly/respect-core@2.33.0

### [CVE-2026-85386](https://documentation.concretecms.org/developers/introduction/version-history/954-release-notes)

> **Frontend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-85386
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-17 02:18:15 JST
- 更新日: 2026-09-17 04:16:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Concrete CMSのフォームブロックにおけるファイルアップロード機能でXML/XSLTのサニタイズが不十分なため、蓄積型XSSが発生する脆弱性。
- 影響: 未認証の訪問者が悪意のあるXMLをアップロードし、閲覧者のブラウザ上でJSを実行できる。管理者が閲覧した場合は管理者権限でのアカウント作成などの不正操作が行われる可能性がある。
- 推奨対応: Concrete CMS 9.5.4 以降にアップデートする。

#### References
- https://documentation.concretecms.org/developers/introduction/version-history/954-release-notes

### [CVE-2026-84397](https://helpx.adobe.com/security/products/experience-manager/apsb26-98.html)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-84397
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-17 03:17:16 JST
- 更新日: 2026-09-17 04:08:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Adobe Experience Managerのフォームフィールドにおける入力検証不備による蓄積型XSSの脆弱性。
- 影響: 低権限の攻撃者が悪意のあるスクリプトを注入し、被害者が該当ページを閲覧した際にブラウザ上で任意スクリプトを実行される可能性がある。
- 推奨対応: アドビが提供する最新の修正パッチまたは更新版を適用する。

#### References
- https://helpx.adobe.com/security/products/experience-manager/apsb26-98.html

### [CVE-2026-81176](https://github.com/sveltejs/devalue/commit/8b2a4562c446d7c36d9d629778079a5fae4243e1)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-81176
- 関連キーワード: javascript, svelte
- 影響製品: -
- 公開日: 2026-09-17 04:17:43 JST
- 更新日: 2026-09-17 04:17:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JavaScriptライブラリ devalue の `parse` 処理における配列境界チェック不足の脆弱性。
- 影響: 悪意のあるペイロードの処理時に計算量が著しく増大（二次関数的処理）し、アプリケーションがサービス拒否（DoS）状態に陥る可能性がある。
- 推奨対応: devalue 5.9.2 以降にアップデートする。

#### References
- https://github.com/sveltejs/devalue/commit/8b2a4562c446d7c36d9d629778079a5fae4243e1
- https://github.com/sveltejs/devalue/releases/tag/v5.9.2
- https://github.com/sveltejs/devalue/security/advisories/GHSA-9rgm-9g3h-6x36

### [CVE-2026-88976](https://github.com/udecode/plate/commit/d02afe45d5ec3a9fb95e0745bc5820ff18a3c12b)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-88976
- 関連キーワード: shadcn/ui, gin
- 影響製品: -
- 公開日: 2026-09-17 00:18:05 JST
- 更新日: 2026-09-17 01:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: リッチテキストエディタ Plate の HTML デシリアライズAPIにおいて、信頼できないHTML属性の処理に起因するXSSの脆弱性。
- 影響: 攻撃者制御のスクリプトが、他のユーザーがコンテンツを読み込んだ際に対象アプリケーションのコンテキストで実行される可能性がある。
- 推奨対応: Plate 53.3.11 以降（または54系の修正済みバージョン）へアップデートする。

#### References
- https://github.com/udecode/plate/commit/d02afe45d5ec3a9fb95e0745bc5820ff18a3c12b
- https://github.com/udecode/plate/pull/5117
- https://github.com/udecode/plate/releases/tag/v53.3.11
- https://github.com/udecode/plate/security/advisories/GHSA-qrfj-mgw8-j9c6

### [CVE-2026-88593](https://github.com/sg-summer/cve/issues/3)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-88593
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-17 03:17:18 JST
- 更新日: 2026-09-17 03:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kkFileView の `/onlinePreview` エンドポイントにおいて、ユーザー入力がサニタイズされずにテンプレートへ渡される反射型XSSの脆弱性。
- 影響: 攻撃者によってJavaScriptコンテキスト内に悪意のあるスクリプトが注入・実行される可能性がある。
- 推奨対応: 修正されたバージョンへ更新するか、入力パラメータの適切なサニタイズ処理を実施する。

#### References
- https://github.com/sg-summer/cve/issues/3

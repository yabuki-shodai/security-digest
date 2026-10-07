# Frontend CVE Summary (2026-10-07)

## Overview

- 取得日時: 2026-10-07 10:28:19 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 15
- Critical: 1
- High: 9
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-104850](https://github.com/modelcontextprotocol/typescript-sdk/commit/edd12e282620ebf770d67316f19cf91d4112a1bd)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-104850
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-10-07 02:17:15 JST
- 更新日: 2026-10-07 05:03:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MCP TypeScript SDK is the official TypeScript SDK for Model Context Protocol servers and clients. Starting in version 1.12.0 and prior to versions 1.31.0 and 2.2.0, the SDK's OAuth client support let the MCP server a client connected to decide which authorization server received the client's OAuth credentials. Stored a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/modelcontextprotocol/typescript-sdk/commit/edd12e282620ebf770d67316f19cf91d4112a1bd
- https://github.com/modelcontextprotocol/typescript-sdk/pull/2887
- https://github.com/modelcontextprotocol/typescript-sdk/releases/tag/v2.2.0
- https://github.com/modelcontextprotocol/typescript-sdk/security/advisories/GHSA-6qxp-vccf-f47h

### [CVE-2026-106105](https://github.com/quasarframework/quasar/commit/b719460aa78e88714b8a1b7ca68267234d217575)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-106105
- 関連キーワード: vue, vite
- 影響製品: -
- 公開日: 2026-10-07 03:16:51 JST
- 更新日: 2026-10-07 05:03:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Quasar Framework is a framework for building high-performance Vue.js user interfaces. Prior to @quasar/ssl-certificate 2.1.0, @quasar/cli 5.0.4, and @quasar/app-vite 3.3.0, the @quasar/ssl-certificate utility cached a combined private key and certificate PEM without explicitly applying owner-only filesystem permissions...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/quasarframework/quasar/commit/b719460aa78e88714b8a1b7ca68267234d217575
- https://github.com/quasarframework/quasar/releases/tag/@quasar/app-vite-v3.3.0
- https://github.com/quasarframework/quasar/releases/tag/@quasar/cli-v5.0.4
- https://github.com/quasarframework/quasar/security/advisories/GHSA-fh39-c73x-5pjv

### [CVE-2026-106106](https://github.com/quasarframework/quasar/commit/61c2bd8a607785fdade72cce20e8faf1de7eee15)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-106106
- 関連キーワード: vue, vite
- 影響製品: -
- 公開日: 2026-10-07 03:16:52 JST
- 更新日: 2026-10-07 05:03:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Quasar Framework is a framework for building high-performance Vue.js user interfaces. Prior to @quasar/render-ssr-error 2.2.4 and @quasar/app-vite 3.3.0, renderSSRError() in utils/render-ssr-error/src/index.js used diagnostic data from utils/render-ssr-error/src/env.js to serialize process.env, request headers, and coo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/quasarframework/quasar/commit/61c2bd8a607785fdade72cce20e8faf1de7eee15
- https://github.com/quasarframework/quasar/releases/tag/@quasar/app-vite-v3.3.0
- https://github.com/quasarframework/quasar/security/advisories/GHSA-r5mf-4r5x-q78f
- https://github.com/quasarframework/quasar/security/advisories/GHSA-r5mf-4r5x-q78f

### [CVE-2026-106107](https://github.com/quasarframework/quasar/commit/91271c38859bec51e154b60c24497a637ce903d7)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-106107
- 関連キーワード: vue, vite
- 影響製品: -
- 公開日: 2026-10-07 03:16:52 JST
- 更新日: 2026-10-07 05:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Quasar Framework is a framework for building high-performance Vue.js user interfaces. Prior to 3.3.0, several @quasar/app-vite SSR and SSG rendering paths interpolated ssrContext.nonce directly into quoted HTML attributes. An application that derives or overrides this value with attacker-controlled data can allow a quo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/quasarframework/quasar/commit/91271c38859bec51e154b60c24497a637ce903d7
- https://github.com/quasarframework/quasar/releases/tag/@quasar/app-vite-v3.3.0
- https://github.com/quasarframework/quasar/security/advisories/GHSA-5m6h-8g35-p3m7

### [CVE-2026-106109](https://github.com/quasarframework/quasar/commit/6c009734b406e246a0855ed060e3a822de8aecc1)

> **Frontend** / **MEDIUM** / CVSS: **4.1** / KEV: **no**

- タイトル: CVE-2026-106109
- 関連キーワード: vue, vite, gin
- 影響製品: -
- 公開日: 2026-10-07 03:16:52 JST
- 更新日: 2026-10-07 05:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Quasar Framework is a framework for building high-performance Vue.js user interfaces. From 1.0.0 until 3.3.0, @quasar/app-vite recursively removed the resolved build.distDir before building without rejecting the project root, user home directory, filesystem roots, or symlink-resolved external directories. An unsafe tru...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/quasarframework/quasar/commit/6c009734b406e246a0855ed060e3a822de8aecc1
- https://github.com/quasarframework/quasar/releases/tag/@quasar/app-vite-v3.3.0
- https://github.com/quasarframework/quasar/security/advisories/GHSA-q9mq-245r-4g93

### [CVE-2026-106102](https://github.com/quasarframework/quasar/commit/11505afe5b5218f2c468f130181815b898fd1e40)

> **Frontend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-106102
- 関連キーワード: vue, gin
- 影響製品: -
- 公開日: 2026-10-07 02:17:24 JST
- 更新日: 2026-10-07 05:03:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Quasar Framework is a framework for building high-performance Vue.js user interfaces. Prior to 2.22.0, the SSR-only getHead() serializer in ui/src/plugins/meta/Meta.js used getAttr() to interpolate values supplied through useMeta() into title, meta, link, and script markup without HTML text or quoted-attribute encoding...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/quasarframework/quasar/commit/11505afe5b5218f2c468f130181815b898fd1e40
- https://github.com/quasarframework/quasar/releases/tag/quasar-v2.22.0
- https://github.com/quasarframework/quasar/security/advisories/GHSA-pq96-jpmf-w254

### [CVE-2026-106104](https://github.com/quasarframework/quasar/commit/7a954ddafa756afe95c8f633f48ed68a07209d3d)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-106104
- 関連キーワード: vue, gin, node.js, express
- 影響製品: -
- 公開日: 2026-10-07 03:16:51 JST
- 更新日: 2026-10-07 05:03:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Quasar Framework is a framework for building high-performance Vue.js user interfaces. Prior to 2.23.3, Platform.parseSSR() passed an unbounded User-Agent request header to getMatch() in ui/src/plugins/platform/Platform.js, whose browser-detection expressions combined greedy captures with repeated unbounded scans. Platf...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/quasarframework/quasar/commit/7a954ddafa756afe95c8f633f48ed68a07209d3d
- https://github.com/quasarframework/quasar/releases/tag/quasar-v2.23.3
- https://github.com/quasarframework/quasar/security/advisories/GHSA-68jq-fhch-4xq4

### [CVE-2026-105868](https://github.com/payloadcms/payload/commit/a8c3a8e8e2680c96ec4f66f5b3854c5df6c35adf)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-105868
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-07 02:17:23 JST
- 更新日: 2026-10-07 05:03:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Payload is a free and open source headless content management system. In versions before 3.90.0 and canary versions before 4.0.0-canary.34, local upload configurations that accept XML files can store an XML file and stylesheet that execute JavaScript in the Payload origin when a logged-in user opens the file. This issu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/payloadcms/payload/commit/a8c3a8e8e2680c96ec4f66f5b3854c5df6c35adf
- https://github.com/payloadcms/payload/releases/tag/v3.90.0
- https://github.com/payloadcms/payload/security/advisories/GHSA-9qpg-3cf8-w33x

### [CVE-2026-105862](https://github.com/payloadcms/payload/commit/a8c3a8e8e2680c96ec4f66f5b3854c5df6c35adf)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-105862
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-07 02:17:22 JST
- 更新日: 2026-10-07 05:03:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Payload is a free and open source headless content management system. In versions before 3.90.0 and canary versions before 4.0.0-canary.34, a collection that allows downloadable SVG uploads can store a malicious SVG that bypasses sanitization and executes attacker-controlled JavaScript when a user downloads and opens t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/payloadcms/payload/commit/a8c3a8e8e2680c96ec4f66f5b3854c5df6c35adf
- https://github.com/payloadcms/payload/releases/tag/v3.90.0
- https://github.com/payloadcms/payload/security/advisories/GHSA-2pwp-2369-8fg3

### [CVE-2026-105798](https://github.com/microsoft/simplechat/commit/537a259eb048b8f6d1c94193fa0c9683ab0bace9)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-105798
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-07 00:17:16 JST
- 更新日: 2026-10-07 00:25:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SimpleChat is a secure AI conversation application with personal and group workspaces for document-grounded interactions. Prior to 0.261.029, POST /api/group_documents/upload stores an attacker-controlled group document filename that group_workspaces.html later interpolates into inline Share event handlers. The escapeG...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/microsoft/simplechat/commit/537a259eb048b8f6d1c94193fa0c9683ab0bace9
- https://github.com/microsoft/simplechat/security/advisories/GHSA-qwcw-r653-j8c6
- https://github.com/microsoft/simplechat/security/advisories/GHSA-qwcw-r653-j8c6

### [CVE-2026-106103](https://github.com/quasarframework/quasar/commit/87c89a80ec84f1eb7dbe258e5367161b0598ceb3)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-106103
- 関連キーワード: vue
- 影響製品: -
- 公開日: 2026-10-07 03:16:51 JST
- 更新日: 2026-10-07 05:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Quasar Framework is a framework for building high-performance Vue.js user interfaces. Prior to @quasar/icongenie 6.1.1, the icongenie generate --profile command accepted folder and name values from a user-supplied profile without constraining the resolved destination to the Quasar project directory. icongenie/lib/utils...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/quasarframework/quasar/commit/87c89a80ec84f1eb7dbe258e5367161b0598ceb3
- https://github.com/quasarframework/quasar/releases/tag/@quasar/icongenie-v6.1.1
- https://github.com/quasarframework/quasar/security/advisories/GHSA-wmpw-j6qv-mw88

### [CVE-2026-106033](https://access.redhat.com/security/cve/CVE-2026-106033)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-106033
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-07 04:17:41 JST
- 更新日: 2026-10-07 05:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A DOM-based Cross-Site Scripting (XSS) vulnerability exists in the Ansible Platform UI due to unvalidated input handling within the application's redirect route. Specifically, the application extracts a target destination from the next query parameter and directly assigns it to the browser's location.href without verif...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-106033
- https://bugzilla.redhat.com/show_bug.cgi?id=2546603

### [CVE-2026-106120](https://github.com/harttle/liquidjs/commit/552819a84b80c62306fe61072628a756272dc749)

> **Frontend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-106120
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-07 04:17:42 JST
- 更新日: 2026-10-07 04:17:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LiquidJS is a Shopify / GitHub Pages compatible template engine in pure JavaScript. Prior to 10.27.2, enabling ownPropertyOnly does not consistently restrict inherited array indices because negative indexing, .first, .last, the first filter, the last filter, join, reverse, slice, compact, and for-loop iteration can rea...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/harttle/liquidjs/commit/552819a84b80c62306fe61072628a756272dc749
- https://github.com/harttle/liquidjs/pull/924
- https://github.com/harttle/liquidjs/releases/tag/v10.27.2
- https://github.com/harttle/liquidjs/security/advisories/GHSA-fwxr-j5w2-587m

### [CVE-2026-103620](https://docs.github.com/en/enterprise-server@3.18/admin/release-notes#3.18.16)

> **Frontend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-103620
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-10-07 04:17:39 JST
- 更新日: 2026-10-07 05:03:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A missing authorization vulnerability was identified in GitHub Enterprise Server that allowed a repository collaborator with write access to delete the current default branch through the GraphQL API and cause an attacker-controlled branch to become the new default. In repositories that required pull-request review but...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.github.com/en/enterprise-server@3.18/admin/release-notes#3.18.16
- https://docs.github.com/en/enterprise-server@3.19/admin/release-notes#3.19.13
- https://docs.github.com/en/enterprise-server@3.20/admin/release-notes#3.20.9
- https://docs.github.com/en/enterprise-server@3.21/admin/release-notes#3.21.7
- https://docs.github.com/en/enterprise-server@3.22/admin/release-notes#3.22.2

### [CVE-2026-106101](https://github.com/quasarframework/quasar/commit/52d874bf55309dd3656fb02aed033ab025d477ec)

> **Frontend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-106101
- 関連キーワード: vue, gin
- 影響製品: -
- 公開日: 2026-10-07 02:17:24 JST
- 更新日: 2026-10-07 05:03:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Quasar Framework is a framework for building high-performance Vue.js user interfaces. Prior to 2.32.2, the openURL() utility in ui/src/utils/open-url/open-url.js trusted window.SafariViewController whenever that global existed in an iOS environment. Attacker-controlled HTML rendered by components such as QEditor can cr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/quasarframework/quasar/commit/52d874bf55309dd3656fb02aed033ab025d477ec
- https://github.com/quasarframework/quasar/releases/tag/quasar-v2.32.2
- https://github.com/quasarframework/quasar/security/advisories/GHSA-89vp-x45c-52cq
- https://github.com/quasarframework/quasar/security/advisories/GHSA-89vp-x45c-52cq

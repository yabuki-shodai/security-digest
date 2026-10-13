# Frontend CVE Summary (2026-10-13)

## Overview

- 取得日時: 2026-10-13 11:59:56 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 16
- Critical: 1
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-109332](https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-4pvg-m42h-c3x2)

> **Frontend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-109332
- 関連キーワード: npm, gin
- 影響製品: -
- 公開日: 2026-10-13 02:17:29 JST
- 更新日: 2026-10-13 02:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Network-AI (npm network-ai) before 5.15.2 contains an origin validation error in McpSseServer._handleRequest in lib/mcp-transport-sse.ts that reflects localhost Origins into Access-Control-Allow-Origin regardless of bind interface. When the server binds a non-loopback address, an attacker page with a localhost Origin v...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-4pvg-m42h-c3x2
- https://www.vulncheck.com/advisories/network-ai-before-5.15.2-cors-origin-validation-error-in-mcp-sse-transport

### [CVE-2026-92681](https://github.com/neo4j/graphql/commit/ef69cc69ff5e97c60d64aa524005f939c5ba3633)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-92681
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-10-13 01:17:07 JST
- 更新日: 2026-10-13 01:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In @neo4j/graphql versions up to and including 7.6.3, @authentication directives applied at the schema level or on the Query or Mutation types are silently ignored for top-level fields annotated with @cypher. Only @authentication directives placed directly on the individual fields are enforced. An application that expo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/neo4j/graphql/commit/ef69cc69ff5e97c60d64aa524005f939c5ba3633
- https://github.com/neo4j/graphql/releases/tag/%40neo4j%2Fgraphql%407.6.4
- https://github.com/neo4j/graphql/security/advisories/GHSA-8xj4-8gg9-fx9h
- https://www.npmjs.com/package/@neo4j/graphql

### [CVE-2026-109288](https://github.com/open-webui/open-webui/security/advisories/GHSA-wf9m-46cp-c6h6)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-109288
- 関連キーワード: javascript, svelte
- 影響製品: -
- 公開日: 2026-10-13 02:17:21 JST
- 更新日: 2026-10-13 02:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open WebUI before 0.11.4 contains a stored cross-site scripting vulnerability in MarkdownInlineTokens.svelte, which renders markdown link URLs into anchor hrefs without validating their scheme. Authenticated users can embed javascript: links in shared chats that, when clicked by a victim, steal the victim's JWT from lo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-webui/open-webui/security/advisories/GHSA-wf9m-46cp-c6h6
- https://www.vulncheck.com/advisories/open-webui-before-0.11.4-stored-xss-via-javascript-urls-in-markdown-links

### [CVE-2026-109290](https://github.com/open-webui/open-webui/security/advisories/GHSA-f9xp-mfmq-x6cg)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-109290
- 関連キーワード: svelte
- 影響製品: -
- 公開日: 2026-10-13 02:17:22 JST
- 更新日: 2026-10-13 02:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open WebUI from 0.11.1 before 0.11.4 contains a stored cross-site scripting vulnerability in DocxPreview.svelte that allows authenticated users to execute script by uploading crafted DOCX attachments. Attackers can embed an OOXML altChunk HTML part or script-scheme hyperlink to steal a previewing administrator's sessio...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-webui/open-webui/security/advisories/GHSA-f9xp-mfmq-x6cg
- https://www.vulncheck.com/advisories/open-webui-0.11.1-before-0.11.4-stored-xss-via-docx-preview

### [CVE-2026-109291](https://github.com/open-webui/open-webui/security/advisories/GHSA-qpqv-xwg8-cqpj)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-109291
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-13 02:17:22 JST
- 更新日: 2026-10-13 02:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open WebUI from 0.6.33 before 0.11.4 contains a cross-site scripting vulnerability that allows authenticated users to execute script in victims' sessions by storing javascript: URLs in citation embed_url fields. Attackers can share a crafted chat whose citation, when clicked, is passed to window.open, letting them stea...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-webui/open-webui/security/advisories/GHSA-qpqv-xwg8-cqpj
- https://www.vulncheck.com/advisories/open-webui-0.6.33-before-0.11.4-stored-xss-via-citation-embed-url

### [CVE-2026-109338](https://github.com/surrealdb/surrealdb/security/advisories/GHSA-84w9-87hm-mxqx)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-109338
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-13 02:17:30 JST
- 更新日: 2026-10-13 02:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SurrealDB before 3.3.0 contains a denial of service vulnerability that allows query-capable users to crash the server by reading non-ASCII header values in embedded JavaScript. Attackers with scripting enabled can read such values via Headers get(), entries(), values(), or getSetCookie(), or return them from fetch() en...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/surrealdb/surrealdb/security/advisories/GHSA-84w9-87hm-mxqx
- https://www.vulncheck.com/advisories/surrealdb-before-3.3.0-denial-of-service-via-headers-non-ascii-values

### [CVE-2026-92682](https://github.com/neo4j/graphql/commit/17650cc370445a6bb9d394d34063d3623e987aa2)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-92682
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-10-13 01:17:07 JST
- 更新日: 2026-10-13 01:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In @neo4j/graphql versions from 7.0.0 up to but not including 7.6.4, the none quantifier in @authorization filters on relationships and connections is not negated when translated to Cypher, so it behaves like some. A rule such as "none of the related denied users matches the JWT subject" therefore returns exactly the r...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/neo4j/graphql/commit/17650cc370445a6bb9d394d34063d3623e987aa2
- https://github.com/neo4j/graphql/releases/tag/%40neo4j%2Fgraphql%407.6.4
- https://github.com/neo4j/graphql/security/advisories/GHSA-h873-p2wr-fjx6
- https://www.npmjs.com/package/@neo4j/graphql

### [CVE-2026-103524](https://kb.cert.org/vuls/id/162329)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-103524
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-10-13 00:17:05 JST
- 更新日: 2026-10-13 00:17:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Thelia v2.6.0 is vulnerable to multiple stored XSS vulnerabilities within the administrative interface. User-supplied input is stored without sufficient output encoding or sanitization and is later rendered in the administrator interface and/or the web store's product pages, allowing arbitrary JavaScript execution when...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://kb.cert.org/vuls/id/162329

### [CVE-2026-109300](https://github.com/open-webui/open-webui/security/advisories/GHSA-9wj4-mcm3-ppj6)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-109300
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-13 02:17:23 JST
- 更新日: 2026-10-13 02:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open WebUI from 0.6.31 before 0.11.4 contains a stored cross-site scripting vulnerability in its Markdown renderer, which treats user-authored tool-call details blocks as tool output and mounts their embeds attribute in script-enabled iframes. Authenticated users can post crafted channel messages, chat messages, or cit...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-webui/open-webui/security/advisories/GHSA-9wj4-mcm3-ppj6
- https://www.vulncheck.com/advisories/open-webui-0.6.31-before-0.11.4-stored-xss-via-tool-call-embeds

### [CVE-2026-109302](https://github.com/parse-community/parse-server/security/advisories/GHSA-gxxq-pghq-9vrc)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-109302
- 関連キーワード: apollo, graphql
- 影響製品: -
- 公開日: 2026-10-13 02:17:24 JST
- 更新日: 2026-10-13 02:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Parse Server 8.2.2 before 8.6.94 and 9.0.0 before 9.10.1-alpha.14 applies its GraphQL introspection control only to operation text sent directly with a request, not to operations resolved from Apollo Server's automatic persisted query cache. Unauthenticated attackers holding the public Application Id and client key can...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/parse-community/parse-server/security/advisories/GHSA-gxxq-pghq-9vrc
- https://www.vulncheck.com/advisories/parse-server-8.2.2-before-8.6.94-and-9.0.0-before-9.10.1-alpha.14-graphql-schema-disclosure-via-persisted-queries

### [CVE-2026-109307](https://github.com/craftcms/cms/security/advisories/GHSA-w5rh-mhxj-wr8r)

> **Frontend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-109307
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-13 02:17:25 JST
- 更新日: 2026-10-13 02:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Craft CMS 5.0.0 before 5.10.14 contains a DOM-based cross-site scripting vulnerability in the control panel login and 2FA verification flow, where a user-controlled returnUrl accepting javascript: URLs is used in client-side navigation. Attackers can lure a 2FA-enabled victim into opening a crafted /admin/login?verify=...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/craftcms/cms/security/advisories/GHSA-w5rh-mhxj-wr8r
- https://www.vulncheck.com/advisories/craft-cms-5.0.0-before-5.10.14-dom-xss-via-returnurl-in-2fa-verification

### [CVE-2026-109327](https://github.com/Admidio/admidio/security/advisories/GHSA-vxfg-x6vc-7w3w)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-109327
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-13 02:17:28 JST
- 更新日: 2026-10-13 02:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Admidio 4.0.12 through 4.3.17 and 5.0.0 before 5.0.15 contains a reflected cross-site scripting vulnerability in system/redirect.php that allows unauthenticated attackers to inject JavaScript via the url GET parameter, due to an incomplete fix for CVE-2021-43810. Attackers can craft a javascript: URL containing a decoy...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Admidio/admidio/security/advisories/GHSA-vxfg-x6vc-7w3w
- https://www.vulncheck.com/advisories/admidio-4.0.12-through-4.3.17-and-5.0.0-before-5.0.15-reflected-xss-via-system-redirect-php

### [CVE-2026-109352](https://github.com/librenms/librenms/security/advisories/GHSA-ffjc-4fr5-47c6)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-109352
- 関連キーワード: javascript, echo
- 影響製品: -
- 公開日: 2026-10-13 02:17:32 JST
- 更新日: 2026-10-13 02:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LibreNMS before 26.9.0 contains a stored cross-site scripting vulnerability in includes/html/pages/device/wireless.inc.php, which echoes wireless sensor sensor_descr values, populated from SNMP DisplayString fields during discovery, into HTML without escaping. Attackers controlling a monitored device's SNMP agent can s...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/librenms/librenms/security/advisories/GHSA-ffjc-4fr5-47c6
- https://www.vulncheck.com/advisories/librenms-before-26.9.0-stored-xss-via-wireless-sensor-description

### [CVE-2026-109392](https://github.com/pimcore/admin-ui-classic-bundle/blob/2.3/templates/admin/data_object/data_object/preview_version.html.twig#L198)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-109392
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-13 01:17:04 JST
- 更新日: 2026-10-13 01:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Pimcore through 2026.3.1 contains a stored cross-site scripting vulnerability that allows authenticated backend users to inject scripts by storing unescaped URLs in ExternalImage fields. Attackers with data object edit permission can store attribute-breaking payloads that execute JavaScript in the admin origin when oth...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pimcore/admin-ui-classic-bundle/blob/2.3/templates/admin/data_object/data_object/preview_version.html.twig#L198
- https://github.com/pimcore/pimcore
- https://github.com/pimcore/pimcore/blob/v2026.3.1/models/DataObject/ClassDefinition/Data/ExternalImage.php#L169-L203
- https://hackmd.io/@1ExmmukzRMWN7B4gQ4W-4Q/rJCbgCKjMe
- https://www.vulncheck.com/advisories/pimcore-through-2026.3.1-stored-xss-via-externalimage-field-version-preview

### [CVE-2026-103527](https://kb.cert.org/vuls/id/162329)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-103527
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-13 00:17:06 JST
- 更新日: 2026-10-13 00:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Thelia v2.6.0's Smarty templates (address.html and address-update.html) fail to properly escape double quotes in the “next” parameter, enabling reflected Cross‑Site Scripting (XSS) when an authenticated user visits the malicious link containing attacker‑controlled JavaScript.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://kb.cert.org/vuls/id/162329

### [CVE-2026-109328](https://github.com/Admidio/admidio/security/advisories/GHSA-c86v-h8qw-rxjp)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-109328
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-13 02:17:28 JST
- 更新日: 2026-10-13 02:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Admidio 5.0.0 before 5.0.15 contains an unauthenticated stored cross-site scripting vulnerability in RegistrationPresenter.php, which inserts the raw FIRST_NAME registration value into an unencoded data-message attribute. Attackers can register with a double-quoted event handler that executes JavaScript in an administr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Admidio/admidio/security/advisories/GHSA-c86v-h8qw-rxjp
- https://www.vulncheck.com/advisories/admidio-5.0.0-before-5.0.15-unauthenticated-stored-xss-via-registration-name

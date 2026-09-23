# Frontend CVE Summary (2026-09-23)

## Overview

- 取得日時: 2026-09-23 09:24:03 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 15
- Critical: 3
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-56681](https://github.com/decolua/9router/commit/efd20be8d81ef2e256a7037f3aa78e6b567b5fd3)

> **Frontend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-56681
- 関連キーワード: next.js
- 影響製品: -
- 公開日: 2026-09-23 01:17:48 JST
- 更新日: 2026-09-23 01:17:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: 9Router is an AI router & token saver. Prior to 0.5.6, 9Router deployments that allow requests to reach Next.js without the sanitizing custom-server.js wrapper trust the client-supplied X-9r-Real-Ip header in src/dashboardGuard.js when isLocalRequest decides whether canAccessPublicLlmApi may skip API-key validation for...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/decolua/9router/commit/efd20be8d81ef2e256a7037f3aa78e6b567b5fd3
- https://github.com/decolua/9router/releases/tag/v0.5.6
- https://github.com/decolua/9router/security/advisories/GHSA-5mj8-gf6m-fhw8

### [CVE-2026-56682](https://github.com/decolua/9router/commit/efd20be8d81ef2e256a7037f3aa78e6b567b5fd3)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-56682
- 関連キーワード: next.js, gin
- 影響製品: -
- 公開日: 2026-09-23 02:17:24 JST
- 更新日: 2026-09-23 03:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: 9Router is an AI router & token saver. Prior to 0.5.6, 9Router deployments that allow requests to reach Next.js without the sanitizing custom-server.js wrapper use the client-supplied X-9r-Real-Ip value as the bucket key in getClientIp, checkLock, and recordFail in src/lib/auth/loginLimiter.js for POST /api/auth/login....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/decolua/9router/commit/efd20be8d81ef2e256a7037f3aa78e6b567b5fd3
- https://github.com/decolua/9router/releases/tag/v0.5.6
- https://github.com/decolua/9router/security/advisories/GHSA-32gc-64m7-hj7v
- https://github.com/decolua/9router/security/advisories/GHSA-32gc-64m7-hj7v

### [CVE-2026-75510](https://github.com/novuhq/novu/commit/f105f3d41a4405a75f803634d49f15a967524d8a)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-75510
- 関連キーワード: javascript, react, gin
- 影響製品: -
- 公開日: 2026-09-23 01:17:53 JST
- 更新日: 2026-09-23 01:17:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Novu provides an API for sending notifications through multiple channels. Prior to 3.18.0, Novu's @novu/js In-App Inbox and the @novu/react Inbox component accept a notification call-to-action redirect.url from the v1 cta.data object and pass it through apps/api/src/app/inbox/utils/notification-mapper.ts and packages/j...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/novuhq/novu/commit/f105f3d41a4405a75f803634d49f15a967524d8a
- https://github.com/novuhq/novu/pull/11453
- https://github.com/novuhq/novu/releases/tag/v3.18.0
- https://github.com/novuhq/novu/security/advisories/GHSA-8gr3-5j6f-25gp
- https://github.com/novuhq/novu/security/advisories/GHSA-8gr3-5j6f-25gp

### [CVE-2026-86062](https://github.com/HKUDS/LightRAG/commit/8bf032a5200f293b482dd945d436e25cd08bd953)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-86062
- 関連キーワード: javascript, react, gin
- 影響製品: -
- 公開日: 2026-09-23 02:17:27 JST
- 更新日: 2026-09-23 04:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LightRAG provides simple and fast retrieval-augmented generation. Prior to 1.5.5, lightrag_webui/src/components/retrieval/ChatMessage.tsx renders answer and thinking content with react-markdown, rehypeRaw, and skipHtml=false without an HTML sanitizer. An attacker who can add a document can store raw HTML that is return...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/HKUDS/LightRAG/commit/8bf032a5200f293b482dd945d436e25cd08bd953
- https://github.com/HKUDS/LightRAG/pull/3437
- https://github.com/HKUDS/LightRAG/releases/tag/v1.5.5
- https://github.com/HKUDS/LightRAG/security/advisories/GHSA-xpjq-3w4w-w5wr
- https://github.com/HKUDS/LightRAG/security/advisories/GHSA-xpjq-3w4w-w5wr

### [CVE-2026-92706](https://github.com/darkreader/darkreader/releases/tag/v4.9.126)

> **Frontend** / **LOW** / CVSS: **3.4** / KEV: **no**

- タイトル: CVE-2026-92706
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-09-23 01:18:12 JST
- 更新日: 2026-09-23 01:18:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dark Reader is an accessibility browser extension that makes web pages colors dark. Prior to 4.9.126, a website can cause the browser extension's image inversion pipeline to request an unauthenticated icon-like bitmap from a locally running web server when the resource uses a known public-like HTTPS URL and is detected...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/darkreader/darkreader/releases/tag/v4.9.126
- https://github.com/darkreader/darkreader/releases/tag/v4.9.128
- https://github.com/darkreader/darkreader/security/advisories/GHSA-jh5x-rphw-x532

### [CVE-2026-75684](https://helpx.adobe.com/security/products/connect/apsb26-150.html)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-75684
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-23 04:16:46 JST
- 更新日: 2026-09-23 04:23:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to inject malicious scripts into vulnerable form fields. Malicious JavaScript may be executed in a victim's browser when they browse to the page containing the vulnerable field, potentially gaining elevate...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://helpx.adobe.com/security/products/connect/apsb26-150.html

### [CVE-2026-75689](https://helpx.adobe.com/security/products/connect/apsb26-150.html)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-75689
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-23 04:16:46 JST
- 更新日: 2026-09-23 04:23:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to inject malicious scripts into vulnerable form fields. Malicious JavaScript may be executed in a victim's browser when they browse to the page containing the vulnerable field, potentially gaining elevate...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://helpx.adobe.com/security/products/connect/apsb26-150.html

### [CVE-2026-75697](https://helpx.adobe.com/security/products/connect/apsb26-150.html)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-75697
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-23 04:16:46 JST
- 更新日: 2026-09-23 05:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to inject malicious scripts into vulnerable form fields. Malicious JavaScript may be executed in a victim's browser when they browse to the page containing the vulnerable field, potentially gaining elevate...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://helpx.adobe.com/security/products/connect/apsb26-150.html

### [CVE-2026-75744](https://helpx.adobe.com/security/products/aem-forms/apsb26-151.html)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-75744
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-23 04:16:47 JST
- 更新日: 2026-09-23 05:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Adobe Experience Manager Forms JEE is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a high-privileged attacker to inject malicious scripts into vulnerable form fields. Malicious JavaScript may be executed in a victim's browser when they browse to the page containing the vulnerabl...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://helpx.adobe.com/security/products/aem-forms/apsb26-151.html

### [CVE-2026-85055](https://github.com/twentyhq/twenty/commit/a5108d512f754a937860bda5e0c2c40c7266e19e)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-85055
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-09-23 01:18:03 JST
- 更新日: 2026-09-23 01:18:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Twenty is an open-source CRM (customer relationship management) platform. Prior to 2.22.0, field-level read permission is enforced on selected output fields but not on GraphQL or REST filter predicates. A workspace member or API key with permission to read an object but not a particular field can reference that denied...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/twentyhq/twenty/commit/a5108d512f754a937860bda5e0c2c40c7266e19e
- https://github.com/twentyhq/twenty/pull/22873
- https://github.com/twentyhq/twenty/releases/tag/twenty/v2.22.0
- https://github.com/twentyhq/twenty/security/advisories/GHSA-v93q-4jcx-7p9m

### [CVE-2026-76803](https://github.com/projectdiscovery/nuclei/commit/9611926a9a1ca99e8ed554d1b26fbeff60e06368)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-76803
- 関連キーワード: javascript, mysql
- 影響製品: -
- 公開日: 2026-09-23 02:17:24 JST
- 更新日: 2026-09-23 02:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nuclei is a vulnerability scanner built on a simple YAML-based DSL. From 3.0.0 until 3.10.0, the nuclei/mysql JavaScript library does not enforce the local-file sandbox when a JavaScript template supplies the allowAllFiles MySQL DSN option. An untrusted javascript: template scanning an attacker-controlled MySQL-compati...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/projectdiscovery/nuclei/commit/9611926a9a1ca99e8ed554d1b26fbeff60e06368
- https://github.com/projectdiscovery/nuclei/pull/7473
- https://github.com/projectdiscovery/nuclei/releases/tag/v3.10.0
- https://github.com/projectdiscovery/nuclei/security/advisories/GHSA-xhmx-w2j4-rw3q

### [CVE-2026-95624](https://github.com/tauri-apps/plugins-workspace/commit/1308bfa399b962b3977c767100a6339d1cbfdd20)

> **Frontend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-95624
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-23 03:17:36 JST
- 更新日: 2026-09-23 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The Tauri updater plugin's 'check' IPC command accepts an allowDowngrades boolean parameter directly from frontend JavaScript code. When set to true, it replaces the version comparator from "update must be newer" to "update must be different." Because the default permission set grants allow-check to the webview, any XS...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/tauri-apps/plugins-workspace/commit/1308bfa399b962b3977c767100a6339d1cbfdd20
- https://github.com/tauri-apps/plugins-workspace/releases/tag/updater-v2.12.0
- https://github.com/tauri-apps/tauri
- https://github.com/tauri-apps/tauri/security/advisories/GHSA-rjc6-5hfg-grp9

### [CVE-2026-79315](https://github.com/lichoin/TraceLoom/blob/main/CVEs/CVE-2026-79315.md)

> **Frontend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-79315
- 関連キーワード: javascript, gin, express
- 影響製品: -
- 公開日: 2026-09-23 00:17:15 JST
- 更新日: 2026-09-23 05:00:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A reflected cross-site scripting vulnerability exists in x-ui 0.3.2. The management interface reflects the raw request URI into a client-side template binding expression used for sidebar menu highlighting. Server-side HTML entity escaping is ineffective in this context: the browser decodes the entities before the clien...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/lichoin/TraceLoom/blob/main/CVEs/CVE-2026-79315.md
- https://github.com/vaxilu/x-ui

### [CVE-2026-48361](https://helpx.adobe.com/security/products/connect/apsb26-150.html)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-48361
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-23 04:16:43 JST
- 更新日: 2026-09-23 05:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Adobe Connect is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by an attacker to inject malicious scripts into vulnerable form fields. Malicious JavaScript may be executed in a victim's browser when they browse to the page containing the vulnerable field. Scope is changed.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://helpx.adobe.com/security/products/connect/apsb26-150.html

### [CVE-2026-63386](https://github.com/sunnyadn/js-toml/commit/4e10acf1f99ff3cb443c58b8f0a57664e41e87c6)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-63386
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-23 04:16:44 JST
- 更新日: 2026-09-23 04:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: js-toml is a TOML parser for JavaScript. Prior to 1.1.3, load() does not bound nesting or dotted-key depth in the recursive parser at src/load/parser.ts or the interpreter at src/load/interpreter.ts, so deeply nested arrays, deeply nested inline tables, or long dotted keys can exhaust the V8 call stack and throw a raw...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/sunnyadn/js-toml/commit/4e10acf1f99ff3cb443c58b8f0a57664e41e87c6
- https://github.com/sunnyadn/js-toml/releases/tag/v1.1.3
- https://github.com/sunnyadn/js-toml/security/advisories/GHSA-3g82-77xr-68x5

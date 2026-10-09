# Frontend CVE Summary (2026-10-09)

## Overview

- 取得日時: 2026-10-09 11:04:25 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 18
- Critical: 2
- High: 7
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-107303](https://github.com/jhipster/generator-jhipster/commit/efe95edd4dedc3379735094936439410a51ce3d9)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-107303
- 関連キーワード: react, gin
- 影響製品: -
- 公開日: 2026-10-09 03:17:19 JST
- 更新日: 2026-10-09 06:03:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JHipster is a development platform to quickly generate, develop, and deploy modern web applications and microservice architectures. Prior to generator-jhipster 9.4.0 and react-jhipster 1.1.0, generated applications can persist attacker-controlled Blob data and companion ContentType values, return them through generated...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jhipster/generator-jhipster/commit/efe95edd4dedc3379735094936439410a51ce3d9
- https://github.com/jhipster/generator-jhipster/pull/34807
- https://github.com/jhipster/generator-jhipster/releases/tag/v9.4.0
- https://github.com/jhipster/generator-jhipster/security/advisories/GHSA-9ffp-22j7-56r2

### [CVE-2026-107375](https://github.com/jhipster/generator-jhipster/commit/f6f1579581da8db0d1b8bd28dd473b56951c83af)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-107375
- 関連キーワード: react, gin
- 影響製品: -
- 公開日: 2026-10-09 03:17:21 JST
- 更新日: 2026-10-09 06:03:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JHipster is a development platform to quickly generate, develop, and deploy modern web applications and microservice architectures. From 7.0.0 until 9.4.0, reactive applications generated with Spring WebFlux, Spring Data R2DBC, and a SQL database pass the attacker-controlled sort request parameter from paginated entity...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jhipster/generator-jhipster/commit/f6f1579581da8db0d1b8bd28dd473b56951c83af
- https://github.com/jhipster/generator-jhipster/releases/tag/v9.4.0
- https://github.com/jhipster/generator-jhipster/security/advisories/GHSA-r223-96jv-q533

### [CVE-2026-107376](https://github.com/webonyx/graphql-php/commit/6c1d6009a0f7557f66753bcfd07badd15acf77f4)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-107376
- 関連キーワード: react, graphql
- 影響製品: -
- 公開日: 2026-10-09 03:17:22 JST
- 更新日: 2026-10-09 06:34:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: webonyx graphql-php is a PHP implementation of the GraphQL specification. Prior to 15.32.3, GraphQL\Language\Parser performs recursive descent without a recursion limit in parseSelectionSet, parseValueLiteral, and parseTypeReference. A remote attacker can submit deeply nested selection sets, object or list values, or l...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/webonyx/graphql-php/commit/6c1d6009a0f7557f66753bcfd07badd15acf77f4
- https://github.com/webonyx/graphql-php/commit/7b7f2080ca5f7d5340a696fc5701b19a9222d2c2
- https://github.com/webonyx/graphql-php/releases/tag/v15.32.3
- https://github.com/webonyx/graphql-php/security/advisories/GHSA-r7cg-qjjm-xhqq
- https://github.com/webonyx/graphql-php/security/advisories/GHSA-r7cg-qjjm-xhqq

### [CVE-2026-107391](https://github.com/Borewit/music-metadata/commit/90a7d52c69e921a0b019592d887acd97b1c8b8a5)

> **Frontend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-107391
- 関連キーワード: npm, node.js
- 影響製品: -
- 公開日: 2026-10-09 05:17:33 JST
- 更新日: 2026-10-09 05:46:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: music-metadata is a metadata parser for audio and video media files. In the public development revision introduced after 11.14.0, a development-branch regression in the MP4 stsd sample-description parser allows an attacker-controlled sample-entry size of zero to prevent the StsdAtom.get cursor from advancing while an a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Borewit/music-metadata/commit/90a7d52c69e921a0b019592d887acd97b1c8b8a5
- https://github.com/Borewit/music-metadata/pull/2734
- https://github.com/Borewit/music-metadata/releases/tag/v11.16.0
- https://github.com/Borewit/music-metadata/security/advisories/GHSA-f94x-6692-553q

### [CVE-2026-104075](https://code-white.com/public-vulnerability-list/#authentication-bypass-in-tvu-receiver-transceiver-web-management-interface)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-104075
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-09 05:17:29 JST
- 更新日: 2026-10-09 06:35:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TVU Networks Receiver/Transceiver devices running firmware before version 7.9 contain an authentication bypass vulnerability in the web management login endpoint POST /tvu/Login that allows remote unauthenticated attackers to obtain an administrative session by submitting an empty or absent UserName parameter. Attacker...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://code-white.com/public-vulnerability-list/#authentication-bypass-in-tvu-receiver-transceiver-web-management-interface
- https://www.vulncheck.com/advisories/tvu-networks-receiver-transceiver-authentication-bypass-via-tvu-login

### [CVE-2026-107700](https://gist.github.com/R3tro16/e094e4318a040f189fd5d2d33e8c3ec2)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-107700
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-10-09 04:17:02 JST
- 更新日: 2026-10-09 06:35:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: dot-access 0.0.3 through 1.0.0 contains a code injection vulnerability that allows remote attackers to execute JavaScript by supplying crafted paths to get(). The path is concatenated into a new Function body in index.js, so attackers can reach constructor.constructor to load child_process and run operating system comm...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gist.github.com/R3tro16/e094e4318a040f189fd5d2d33e8c3ec2
- https://github.com/ntharim/dot-access
- https://github.com/ntharim/dot-access/blob/v1.0.0/index.js#L1-L7
- https://www.vulncheck.com/advisories/dot-access-0.0.3-through-1.0.0-code-injection-via-get-path-argument

### [CVE-2026-104077](https://obsidian.md/changelog/2026-10-05-desktop-v1.14.4/)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-104077
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-09 02:17:11 JST
- 更新日: 2026-10-09 06:33:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Obsidian Desktop before 1.14.0 contains a remote code execution vulnerability that allows attackers to craft malicious Markdown notes exploiting insufficient sanitization of the data-background-iframe attribute, which bypasses DOMPurify and is processed by the bundled Reveal.js 4.3.1 within the Slides core plugin, allo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://obsidian.md/changelog/2026-10-05-desktop-v1.14.4/

### [CVE-2026-107300](https://github.com/mcollina/msgpack5/commit/77fbef144d05def5d16fc22c37caa64c0a7efeba)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-107300
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-10-09 02:17:16 JST
- 更新日: 2026-10-09 05:48:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: msgpack5 is a msgpack v5 implementation for node.js and the browser. Prior to 6.1.0, the streaming decoder recursively invokes itself for each complete MessagePack value remaining in a chunk. A remote peer can send one chunk containing many small valid values, causing recursion proportional to the value count, exhausti...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mcollina/msgpack5/commit/77fbef144d05def5d16fc22c37caa64c0a7efeba
- https://github.com/mcollina/msgpack5/releases/tag/v6.1.0
- https://github.com/mcollina/msgpack5/security/advisories/GHSA-5x5g-h9x8-2fh9

### [CVE-2026-104078](https://obsidian.md/changelog/2026-10-05-desktop-v1.14.4/)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-104078
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-09 02:17:11 JST
- 更新日: 2026-10-09 06:33:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Obsidian Desktop before 1.14.0 contains a filter bypass vulnerability in the bundled MathJax 3.2.2 Safe component that allows attackers to execute arbitrary code by embedding a crafted \href value with a TAB byte in the URL scheme, causing filterURL to produce an empty protocol that bypasses the configured safeProtocol...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://obsidian.md/changelog/2026-10-05-desktop-v1.14.4/

### [CVE-2026-17189](https://www.ibm.com/support/pages/node/7291628)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-17189
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-09 06:17:56 JST
- 更新日: 2026-10-09 06:26:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 is vulnerable to cross-site scripting. This vulnerability allows an unauthenticated user to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials disclo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7291628

### [CVE-2026-107298](https://github.com/mcollina/msgpack5/commit/1e2b5874e555dd7c99417f64788a03b0590bb102)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-107298
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-10-09 02:17:15 JST
- 更新日: 2026-10-09 05:48:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: msgpack5 is a msgpack v5 implementation for node.js and the browser. Prior to 6.1.0, the array and map decoding paths have no nesting-depth limit, allowing an attacker who can provide MessagePack input to submit deeply nested containers that exhaust the JavaScript call stack and interrupt a process, worker, or request...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mcollina/msgpack5/commit/1e2b5874e555dd7c99417f64788a03b0590bb102
- https://github.com/mcollina/msgpack5/releases/tag/v6.1.0
- https://github.com/mcollina/msgpack5/security/advisories/GHSA-24ch-f2g6-9hhh

### [CVE-2026-107380](https://github.com/darylldoyle/svg-sanitizer/commit/23877db7e76f1e1df5c3e65ab30239219c3d2867)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-107380
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-09 03:17:23 JST
- 更新日: 2026-10-09 06:35:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: savg-sanitizer is a PHP SVG/XML sanitizer. Prior to 1.0.0, svg-sanitizer's isHrefSafeValue() validates an SVG href after XML DTD entity expansion, but saveXML() serializes the original entity reference after removing the DTD declaration. A crafted entity such as Tab can appear to the sanitizer as a safe fragment prefix...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/darylldoyle/svg-sanitizer/commit/23877db7e76f1e1df5c3e65ab30239219c3d2867
- https://github.com/darylldoyle/svg-sanitizer/releases/tag/1.0.0
- https://github.com/darylldoyle/svg-sanitizer/security/advisories/GHSA-9rjx-3jch-6vjf

### [CVE-2026-107396](https://github.com/indico/indico/commit/d4c8c7127176efa4cb53c64119ca8ee2b551be18)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-107396
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-09 05:17:34 JST
- 更新日: 2026-10-09 05:48:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Indico is an event management system that uses Flask-Multipass, a multi-backend authentication system for Flask. Prior to 3.3.13, users who can manage events or create content, including speakers who can upload material, can store crafted javascript URLs in fields that accept custom URLs. A user who follows one of thes...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/indico/indico/commit/d4c8c7127176efa4cb53c64119ca8ee2b551be18
- https://github.com/indico/indico/pull/7619
- https://github.com/indico/indico/releases/tag/v3.3.13
- https://github.com/indico/indico/security/advisories/GHSA-c4wc-ggrj-jg9v

### [CVE-2026-105828](https://github.com/parse-community/parse-server/security/advisories/GHSA-6m77-f8xr-f723)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-105828
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-10-09 00:17:34 JST
- 更新日: 2026-10-09 06:35:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Parse Server 8.2.2 before 8.6.92 and 9.0.0 before 9.10.1-alpha.12 contains an information disclosure vulnerability in which GraphQL validation error messages reveal hidden class names when public introspection is disabled. Unauthenticated attackers holding only the public Application Id can send crafted operations trig...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/parse-community/parse-server/security/advisories/GHSA-6m77-f8xr-f723
- https://www.vulncheck.com/advisories/parse-server-9.0.0-before-9.10.1-alpha.12-class-name-disclosure-via-graphql-errors

### [CVE-2026-105831](https://github.com/espocrm/espocrm/security/advisories/GHSA-xfqv-j65r-qqgh)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-105831
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-09 00:17:35 JST
- 更新日: 2026-10-09 03:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: EspoCRM before 10.0.6 contains a stored HTML injection vulnerability that allows unauthenticated attackers to inject HTML by submitting crafted Lead Capture public form data. The request body is stored in LeadCaptureLogRecord.data and rendered unescaped when administrators view the log record, though Content Security P...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/espocrm/espocrm/security/advisories/GHSA-xfqv-j65r-qqgh
- https://www.vulncheck.com/advisories/espocrm-before-10.0.6-unauthenticated-stored-html-injection-via-lead-capture-form

### [CVE-2026-107390](https://github.com/Borewit/music-metadata/commit/0f19ad66d71889b1c5f3ba84d4824f079ac4c005)

> **Frontend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-107390
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-09 05:17:33 JST
- 更新日: 2026-10-09 05:46:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: music-metadata is a metadata parser for audio and video media files. Prior to 11.16.0, the MP4 parser accepts an attacker-controlled 64-bit extended atom size, converts it to a JavaScript Number, and uses the resulting payload length for atom-specific readToken calls before proving that the atom fits within its parent...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Borewit/music-metadata/commit/0f19ad66d71889b1c5f3ba84d4824f079ac4c005
- https://github.com/Borewit/music-metadata/pull/2746
- https://github.com/Borewit/music-metadata/releases/tag/v11.16.0
- https://github.com/Borewit/music-metadata/security/advisories/GHSA-qc8q-pw95-mq6c

### [CVE-2026-11936](https://www.ibm.com/support/pages/node/7291628)

> **Frontend** / **MEDIUM** / CVSS: **4.9** / KEV: **no**

- タイトル: CVE-2026-11936
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-09 06:17:54 JST
- 更新日: 2026-10-09 06:26:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Security Verify Access 10.0 through 10.0.9.2 and IBM Verify Identity Access 11.0 through 11.0.3 local management interface in certain configurations is vulnerable to cross-site scripting. This vulnerability allows an authenticated user to embed arbitrary JavaScript code in the Web UI thus altering the intended func...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7291628

### [CVE-2026-13258](https://www.ibm.com/support/pages/node/7289775)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-13258
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-09 00:17:48 JST
- 更新日: 2026-10-09 05:49:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM DataPower Gateway 10.5.0.0 through 10.5.0.22, 10.6.1 through 10.6.6, 10.6.0.0 through 10.6.0.10, and 11.0.0.0 through 11.0.0.2 is vulnerable to cross-site scripting. This vulnerability allows an authenticated user to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7289775

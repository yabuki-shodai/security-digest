# Frontend CVE Summary (2026-10-24)

## Overview

- 取得日時: 2026-10-24 09:34:25 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 1
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-115774](https://github.com/twisted/twisted/commit/3d125548bcbe955007cb97f480bb699a5e074741)

> **Frontend** / **MEDIUM** / CVSS: **4.9** / KEV: **no**

- タイトル: CVE-2026-115774
- 関連キーワード: react, python
- 影響製品: -
- 公開日: 2026-10-24 06:17:22 JST
- 更新日: 2026-10-24 06:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Twisted is an event-based framework for internet applications, supporting Python 3.6+. Prior to 26.10.0rc1, twisted.mail.imap4.IMAP4Server reaches twisted.mail.imap4.parseNestedParens with a negative literal size in an authenticated SEARCH command after the client enters the selected mailbox state. The negative size mo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/twisted/twisted/commit/3d125548bcbe955007cb97f480bb699a5e074741
- https://github.com/twisted/twisted/pull/12764
- https://github.com/twisted/twisted/releases/tag/twisted-26.10.0rc1
- https://github.com/twisted/twisted/security/advisories/GHSA-2qrf-pqgx-qh9v

### [CVE-2026-115569](https://github.com/fallow-rs/fallow/commit/75c0c60948a53ddfe042e65b446343989f4c5649)

> **Frontend** / **LOW** / CVSS: **3.3** / KEV: **no**

- タイトル: CVE-2026-115569
- 関連キーワード: typescript, javascript, vite, vitest, jest
- 影響製品: -
- 公開日: 2026-10-24 04:17:44 JST
- 更新日: 2026-10-24 04:57:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Fallow is a codebase intelligence tool for TypeScript and JavaScript. From 2.68.0 until 3.34.0, Fallow follows attacker-controlled Jest projects paths outside the project root through absolute paths, parent segments, dot-prefixed wildcard globs, or symlinks. In version 3.33.1, the same behavior also affects Vitest test...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/fallow-rs/fallow/commit/75c0c60948a53ddfe042e65b446343989f4c5649
- https://github.com/fallow-rs/fallow/pull/3556
- https://github.com/fallow-rs/fallow/releases/tag/v3.34.0
- https://github.com/fallow-rs/fallow/security/advisories/GHSA-jfwm-3p3c-6hx5

### [CVE-2026-58202](https://github.com/open-reception/appointment-booking-software/commit/df5432776a1a5b47c3a64d64e9d05dbe2b7a7819)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-58202
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-10-24 06:17:24 JST
- 更新日: 2026-10-24 06:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to version 2.0.0, the account-confirmation link in emails is built from the request Host header, with no allowlist. The unauthenticated POST /api/auth/resend-confirmation rotates a pending invitee's confirm...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-reception/appointment-booking-software/commit/df5432776a1a5b47c3a64d64e9d05dbe2b7a7819
- https://github.com/open-reception/appointment-booking-software/releases/tag/v2.0.0
- https://github.com/open-reception/appointment-booking-software/security/advisories/GHSA-w5g9-g2p4-2g4m

### [CVE-2026-65824](https://github.com/open-reception/appointment-booking-software/commit/da921eb9d36953276577c0a6deb9267bfec03622)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-65824
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-10-24 06:17:24 JST
- 更新日: 2026-10-24 06:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenReception's appointment booking software provides an end-to-end encrypted appointment booking platform. Prior to version 2.2.1, an attacker who captures a pending invite token can replay it to obtain a passkey-registration credential and register their own passkey on the invited account, taking control of that acco...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-reception/appointment-booking-software/commit/da921eb9d36953276577c0a6deb9267bfec03622
- https://github.com/open-reception/appointment-booking-software/releases/tag/v2.2.1
- https://github.com/open-reception/appointment-booking-software/security/advisories/GHSA-hvcx-8476-rwv6

### [CVE-2026-55486](https://github.com/intranda/goobi-viewer-core/commit/0e488c6b02a28c1d1a747dfe3958ad2bbcff2d0b)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-55486
- 関連キーワード: javascript, go, gin
- 影響製品: -
- 公開日: 2026-10-24 00:17:33 JST
- 更新日: 2026-10-24 01:28:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The Goobi viewer is a web application that allows digitised material to be displayed in a web browser. From version 25.08 to before version 26.05, the IIIF Auth 2.0 endpoints auth/login and auth/token in AuthorizationFlowResource accept an origin query parameter without validation and then (1) embed it into the Content...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/intranda/goobi-viewer-core/commit/0e488c6b02a28c1d1a747dfe3958ad2bbcff2d0b
- https://github.com/intranda/goobi-viewer-core/releases/tag/v26.05
- https://github.com/intranda/goobi-viewer-core/security/advisories/GHSA-975w-g9gj-xq48

### [CVE-2026-115570](https://github.com/electron/electron/commit/093583c71be71c85453e6e225137bf2af755fbcc)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-115570
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-10-24 04:17:44 JST
- 更新日: 2026-10-24 06:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 42.11.16, 43.8.1, 44.9.1, and 45.0.0-beta.6, Electron does not block compromised eMudhra intermediate certificates in Chromium networking, Node.js tls, Node.js https, or Node.js fetch. An attacker who holds...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/093583c71be71c85453e6e225137bf2af755fbcc
- https://github.com/electron/electron/commit/1d2f13b1985444a38abf389db38228ac42f5bcad
- https://github.com/electron/electron/commit/817c43f925677eb88034bfba4f0b8dfd28e7ad20
- https://github.com/electron/electron/commit/e02265be96c5e13ae43644ef482b718e1e800499
- https://github.com/electron/electron/pull/55127

### [CVE-2026-115895](https://github.com/capricorn86/happy-dom/commit/fd163520b74d9fa146be91f7b4e4f46d6cccbe13)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-115895
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-10-24 07:16:58 JST
- 更新日: 2026-10-24 07:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Happy DOM is a JavaScript implementation of a web browser without its graphical user interface. From 17.0.0 until 21.0.4, packages/happy-dom/src/module/ECMAScriptModuleCompiler.ts accepts a named ESM import alias without validating that it is a JavaScript binding identifier before inserting it into a generated destruct...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/capricorn86/happy-dom/commit/fd163520b74d9fa146be91f7b4e4f46d6cccbe13
- https://github.com/capricorn86/happy-dom/pull/2537
- https://github.com/capricorn86/happy-dom/releases/tag/v21.0.4
- https://github.com/capricorn86/happy-dom/security/advisories/GHSA-834v-8h66-3h79

### [CVE-2026-115887](https://github.com/graphql-hive/graphql-scalars/commit/210fd2485641afa2452800c00144245c74361701)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-115887
- 関連キーワード: graphql, node.js
- 影響製品: -
- 公開日: 2026-10-24 07:16:58 JST
- 更新日: 2026-10-24 07:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GraphQL Scalars is a library of custom GraphQL scalars for creating precise type-safe GraphQL schemas. From 1.24.1 until 2.0.1, GraphQLPhoneNumber in src/scalars/PhoneNumber.ts uses ambiguous nested digit quantifiers that backtrack exponentially when a PhoneNumber value contains a run of digits followed by a character...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/graphql-hive/graphql-scalars/commit/210fd2485641afa2452800c00144245c74361701
- https://github.com/graphql-hive/graphql-scalars/pull/2719
- https://github.com/graphql-hive/graphql-scalars/releases/tag/v2.0.1
- https://github.com/graphql-hive/graphql-scalars/security/advisories/GHSA-x8rm-f576-gq67

### [CVE-2026-115897](https://github.com/yahoo/serialize-javascript/commit/2864b3c6260a3bfd52d2db3e70d1a079de108a61)

> **Frontend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-115897
- 関連キーワード: javascript, express
- 影響製品: -
- 公開日: 2026-10-24 07:16:59 JST
- 更新日: 2026-10-24 07:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Serialize JavaScript serializes JavaScript values to a superset of JSON that includes regular expressions and functions. Prior to 7.1.3, the function-source escaping logic does not neutralize a bare closing-script prefix when attacker-influenced function source text ends exactly at that prefix. Because each function bo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/yahoo/serialize-javascript/commit/2864b3c6260a3bfd52d2db3e70d1a079de108a61
- https://github.com/yahoo/serialize-javascript/pull/235
- https://github.com/yahoo/serialize-javascript/releases/tag/v7.1.3
- https://github.com/yahoo/serialize-javascript/security/advisories/GHSA-m5mm-p8h7-m29v

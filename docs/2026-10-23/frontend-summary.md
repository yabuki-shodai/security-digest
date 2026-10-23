# Frontend CVE Summary (2026-10-23)

## Overview

- 取得日時: 2026-10-23 09:35:54 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 1
- High: 6
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-94482](https://github.com/vercel/next.js/releases/tag/v15.5.28)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-94482
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-10-23 01:19:16 JST
- 更新日: 2026-10-23 02:29:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Next.js is a React framework for building full-stack web applications. From 13.0.0 until 15.5.28 and 16.4.1, crafted requests targeting App Router applications with at least one Server Action can cause excessive CPU consumption and block processing of further requests in the same process. Applications using the Pages R...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vercel/next.js/releases/tag/v15.5.28
- https://github.com/vercel/next.js/releases/tag/v16.4.1
- https://github.com/vercel/next.js/security/advisories/GHSA-p3m5-59mp-jv5r

### [CVE-2026-114607](https://github.com/better-auth/better-auth/commit/ac54bfd67821a7607533af2059858b12bc54e26a)

> **Frontend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-114607
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-10-23 02:16:58 JST
- 更新日: 2026-10-23 02:40:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Better Auth is an authentication and authorization library for TypeScript. From 1.4.0-beta.18 until 1.7.7, deployments that enable Magic Link with storeToken set to plain, or with storeToken set to hashed and the global verification.storeIdentifier setting also set to hashed, enable a built-in social or Generic OAuth p...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/better-auth/better-auth/commit/ac54bfd67821a7607533af2059858b12bc54e26a
- https://github.com/better-auth/better-auth/pull/11494
- https://github.com/better-auth/better-auth/releases/tag/v1.7.7
- https://github.com/better-auth/better-auth/security/advisories/GHSA-965c-763c-88jm

### [CVE-2026-115513](https://github.com/opencats/OpenCATS/commit/f82e0ee3045845b90b7e111c46f30998496e38a8)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-115513
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-23 02:16:59 JST
- 更新日: 2026-10-23 02:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenCATS before 0.12.0 contains a stored cross-site scripting vulnerability that allows a low-privileged authenticated user to inject HTML/JavaScript payloads by setting a Candidate, Company, Contact, Job Order, or List name/title field, which is stored unsanitized and later rendered unescaped in the 'Recent' (MRU) nav...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/opencats/OpenCATS/commit/f82e0ee3045845b90b7e111c46f30998496e38a8
- https://github.com/opencats/OpenCATS/commits/master/lib/MRU.php
- https://github.com/opencats/OpenCATS/releases/tag/v0.12.0
- https://www.vulncheck.com/advisories/opencats-before-stored-xss-via-mru-navigation-panel

### [CVE-2026-75507](https://github.com/graphql-python/graphql-core/commit/150e59814d97d12140be005a558c93188ef89198)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-75507
- 関連キーワード: graphql, python
- 影響製品: -
- 公開日: 2026-10-23 02:16:59 JST
- 更新日: 2026-10-23 02:40:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GraphQL-core is a Python port of the GraphQL.js reference implementation. From 3.0.0 until 3.2.12 and 3.3.0rc1, the OverlappingFieldsCanBeMerged rule in specified_rules repeatedly compares fields that share response names and recursively re-compares flattened inline fragments during the validation phase. The prior name...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/graphql-python/graphql-core/commit/150e59814d97d12140be005a558c93188ef89198
- https://github.com/graphql-python/graphql-core/commit/29c2753a7ee30a96a4109e7c6add1a2dae0497d7
- https://github.com/graphql-python/graphql-core/releases/tag/v3.2.12
- https://github.com/graphql-python/graphql-core/releases/tag/v3.3.0rc1
- https://github.com/graphql-python/graphql-core/security/advisories/GHSA-vj8h-fx38-h3vc

### [CVE-2026-75508](https://github.com/graphql-python/graphql-core/commit/437dea102e92fdf05a2971ca76787c5a5bad875a)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-75508
- 関連キーワード: graphql, python
- 影響製品: -
- 公開日: 2026-10-23 02:16:59 JST
- 更新日: 2026-10-23 02:40:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GraphQL-core is a Python port of the GraphQL.js reference implementation. From 3.2.3 until 3.2.12 and 3.3.0rc1, the parser's max_tokens limit in Parser.advance_lexer counts only non-comment tokens returned after Lexer.lookahead skips comments. Each skipped comment is still allocated as a Token and retained through toke...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/graphql-python/graphql-core/commit/437dea102e92fdf05a2971ca76787c5a5bad875a
- https://github.com/graphql-python/graphql-core/commit/80ef435a1808fbbcc4aaac63ae76771a1c91002d
- https://github.com/graphql-python/graphql-core/releases/tag/v3.2.12
- https://github.com/graphql-python/graphql-core/releases/tag/v3.3.0rc1
- https://github.com/graphql-python/graphql-core/security/advisories/GHSA-r77w-qph3-7vf8

### [CVE-2026-61791](https://github.com/schorschii/OCO-Server/commit/ef02f9768e5e1792c3ee53c72e8d7e4ea58ddaa8)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-61791
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-23 00:17:05 JST
- 更新日: 2026-10-23 02:40:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OCO-Server is a self-hosted endpoint management application for computer inventory, software deployment, and mobile device management. Prior to 1.2.1, `Html::commandButton()` in `lib/Html.class.php` embeds an action URL containing a stored computer hostname into a JavaScript string in an inline `onclick` handler, using...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/schorschii/OCO-Server/commit/ef02f9768e5e1792c3ee53c72e8d7e4ea58ddaa8
- https://github.com/schorschii/OCO-Server/releases/tag/v1.2.1
- https://github.com/schorschii/OCO-Server/security/advisories/GHSA-9c2r-9j95-22pr

### [CVE-2026-97635](https://github.com/agent0ai/agent-zero/issues/943)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-97635
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-23 03:17:32 JST
- 更新日: 2026-10-23 03:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The Agent Zero Web UI before 1.15 does not correctly sanitize user-provided input in chat messages or file uploads. When Agent Zero reproduces content in the chat interface, any injected JavaScript is executed in the context of the victim’s authenticated Agent Zero Web UI session.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/agent0ai/agent-zero/issues/943
- https://github.com/agent0ai/agent-zero/releases/tag/v1.15
- https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-296-01.json
- https://www.cve.org/CVERecord?id=CVE-2026-97635

### [CVE-2025-69723](https://cyberroute.github.io/post/2025-12-11-localstack-hack/)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2025-69723
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-23 04:17:33 JST
- 更新日: 2026-10-23 04:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A reflected cross-site scripting (XSS) vulnerability in localstack v4.9.2 allows attackers to execute arbitrary Javascript in the context of the user's browser via a crafted URL.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cyberroute.github.io/post/2025-12-11-localstack-hack/

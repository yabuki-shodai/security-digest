# Frontend CVE Summary (2026-10-20)

## Overview

- 取得日時: 2026-10-20 10:03:21 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 7
- Critical: 2
- High: 1
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-109437](https://github.com/CognicellAI/Cognition/releases/tag/v0.13.0)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-109437
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-10-20 04:17:19 JST
- 更新日: 2026-10-20 06:14:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cognition before 0.13.0 contains an unauthenticated remote code execution vulnerability due to defaulting its agent sandbox backend to local execution and shipping no authentication on its REST/SSE API. Attackers can create a session via POST /sessions and post a message via POST /sessions/{id}/messages without credent...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/CognicellAI/Cognition/releases/tag/v0.13.0
- https://www.lasso.security/vulnerability-database/cve-2026-109437
- https://www.vulncheck.com/advisories/cognition-unauthenticated-rce-via-local-shell-backend

### [CVE-2026-112776](https://github.com/craftcms/cms/security/advisories/GHSA-7rr3-4jcm-x526)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-112776
- 関連キーワード: graphql, go
- 影響製品: -
- 公開日: 2026-10-20 05:17:54 JST
- 更新日: 2026-10-20 05:59:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Craft CMS from 5.0.0 before 5.11.0 contains an authorization bypass vulnerability that allows site-scoped GraphQL tokens to mutate other sites' content because requireAllowedSite() is not enforced. Attackers holding a site-A token can create entries in site B via supplied siteId and delete entries, categories, tags, an...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/craftcms/cms/security/advisories/GHSA-7rr3-4jcm-x526
- https://www.vulncheck.com/advisories/craft-cms-5.0.0-before-5.11.0-graphql-site-scope-bypass-via-mutations

### [CVE-2026-3295](https://www.ibm.com/support/pages/node/7290183)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-3295
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-20 03:17:07 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Cloud Pak System 2.3.6.0, and 2.3.6.1 is vulnerable to cross site scripting. The web app user‑supplied input is not properly sanitized or HTML‑encoded before being stored and rendered. An authenticated attacker could exploit this vulnerability by entering specially crafted payloads containing malicious JavaScript w...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7290183

### [CVE-2026-111757](https://github.com/honojs/hono/commit/8b05c774ef1555c70f5ba5e2991b7e77cc3635cc)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-111757
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-20 03:17:00 JST
- 更新日: 2026-10-20 03:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Hono is a Web application framework that provides support for any JavaScript runtime. From 4.12.4 until 4.13.11, serveStatic can interpret a malformed percent-encoded path differently from upstream routing middleware and bypass protection for a static prefix. The root cause is serveStatic decodes a routed request path...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/honojs/hono/commit/8b05c774ef1555c70f5ba5e2991b7e77cc3635cc
- https://github.com/honojs/hono/security/advisories/GHSA-5r4p-p66f-jhc7
- https://github.com/honojs/hono/security/advisories/GHSA-5r4p-p66f-jhc7

### [CVE-2023-38375](https://www.ibm.com/support/pages/node/7290183)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2023-38375
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-20 03:16:57 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Cloud Pak System 2.3.6.0, and 2.3.6.1 is vulnerable to cross-site scripting. This vulnerability allows users to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials disclosure within a trusted session.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7290183

### [CVE-2025-6623](https://github.com/wso2/carbon-analytics-common/pull/870)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2025-6623
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-20 02:16:59 JST
- 更新日: 2026-10-20 06:06:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The carbon console accepts user-supplied XML input without sufficiently encoding potentially executable content, allowing for the injection of malicious scripts. Successful exploitation allows a remote attacker to execute arbitrary JavaScript in the context of a victim's browser, leading to actions such as redirecting...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/wso2/carbon-analytics-common/pull/870
- https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2025-4316/

### [CVE-2026-4413](https://www.ibm.com/support/pages/node/7292374)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-4413
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-20 03:17:07 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Concert 1.0 through 3.0.0 is vulnerable to cross-site scripting. This vulnerability allows an unauthenticated attacker to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials disclosure within a trusted session.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7292374

# Frontend CVE Summary (2026-09-10)

## Overview

- 取得日時: 2026-09-10 09:08:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 7
- Critical: 1
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-54694](https://github.com/NationalSecurityAgency/skills-service/security/advisories/GHSA-hqfg-c8wf-w2g8)

> **Frontend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-54694
- 関連キーワード: javascript, vue, gin, aws
- 影響製品: -
- 公開日: 2026-09-10 04:17:28 JST
- 更新日: 2026-09-10 04:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SkillTree is a micro-learning gamification platform. Prior to version 4.4.2, two independent code flaws combine into a single exploitable attack chain, with three distinct exploitation paths of escalating impact. `StringHighlighter.js` builds an HTML string by interpolating raw `value` substrings directly into a templa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/NationalSecurityAgency/skills-service/security/advisories/GHSA-hqfg-c8wf-w2g8

### [CVE-2026-87996](https://github.com/open-webui/open-webui/commit/27402ff210bfa253445720920dfb86b15a00327b)

> **Frontend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-87996
- 関連キーワード: playwright, python
- 影響製品: -
- 公開日: 2026-09-10 07:18:47 JST
- 更新日: 2026-09-10 07:18:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. From 0.9.6 until 0.11.1, SafePlaywrightURLLoader in backend/open_webui/retrieval/web/utils.py validated a user-controlled hostname in Python and then let the Playwright browser resolve it again in the sync and async request intercepto...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-webui/open-webui/commit/27402ff210bfa253445720920dfb86b15a00327b
- https://github.com/open-webui/open-webui/pull/28634
- https://github.com/open-webui/open-webui/releases/tag/v0.11.1
- https://github.com/open-webui/open-webui/security/advisories/GHSA-4v28-j6q3-5m4r

### [CVE-2026-18147](https://access.redhat.com/security/cve/CVE-2026-18147)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-18147
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-10 02:17:17 JST
- 更新日: 2026-09-10 05:14:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw was found in FreeIPA. An unauthenticated remote attacker could exploit a DOM Cross-Site Scripting (XSS) vulnerability in the FreeIPA/IdM Web UI password reset page. By enticing a victim to click a specially crafted link and complete a password reset, the attacker could inject and execute arbitrary JavaScript cod...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-18147
- https://bugzilla.redhat.com/show_bug.cgi?id=2508181

### [CVE-2026-87995](https://github.com/open-webui/open-webui/commit/54d7a223707f03172efbb9e754db6e69709956d0)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-87995
- 関連キーワード: svelte, gin
- 影響製品: -
- 公開日: 2026-09-10 07:18:47 JST
- 更新日: 2026-09-10 07:18:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. From 0.8.11 until 0.11.1, src/lib/components/chat/FileNav/PortPreview.svelte rendered terminal port content in an iframe sandbox containing both allow-scripts and allow-same-origin. Because the terminal proxy serves that content from...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-webui/open-webui/commit/54d7a223707f03172efbb9e754db6e69709956d0
- https://github.com/open-webui/open-webui/releases/tag/v0.11.1
- https://github.com/open-webui/open-webui/security/advisories/GHSA-jmc6-2wr8-h3wj

### [CVE-2026-71802](https://github.com/W000i/vuln/issues/6)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-71802
- 関連キーワード: javascript, go, gin
- 影響製品: -
- 公開日: 2026-09-10 06:17:03 JST
- 更新日: 2026-09-10 06:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A stored Cross-Site Scripting (XSS) vulnerability exists in the announcement preview component of REBUILD 4.4.3. Although the announcement content undergoes HTML escaping on the server side, the client-side preview code reverses the escaped entities using jQuery's `html().text()` method and subsequently injects the res...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/W000i/vuln/issues/6

### [CVE-2026-79323](https://gist.github.com/mrtantoine/4331a5f04f8309eb1799b257a7371f34)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-79323
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-09-10 04:17:48 JST
- 更新日: 2026-09-10 05:20:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Information disclosure in the blogComments GraphQL query in Magefan Blog GraphQL for Magento 2 (magefan/module-blog-graph-ql) through 2.2.1 allows remote unauthenticated attackers to obtain blog commenter email addresses and internal customer and admin identifiers via a POST request to /graphql.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gist.github.com/mrtantoine/4331a5f04f8309eb1799b257a7371f34
- https://magefan.com/magento2-blog-extension

### [CVE-2026-71803](https://github.com/W000i/vuln/issues/7)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-71803
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-09-10 06:17:03 JST
- 更新日: 2026-09-10 06:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: money-pos 1.0 contains a stored Cross-Site Scripting (XSS) vulnerability. When processing returns, the backend fails to filter or escape the goodsName parameter, directly concatenating it into the order log description; the frontend subsequently renders this content using v-html. An attacker with product creation privi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/W000i/vuln/issues/7

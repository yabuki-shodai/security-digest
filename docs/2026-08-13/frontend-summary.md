# Frontend CVE Summary (2026-08-13)

## Overview

- 取得日時: 2026-08-13 07:55:58 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 11
- Critical: 1
- High: 1
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-73299](https://github.com/microsoft/prompty/commit/e4a0ebf49e3a78d5d7796c8480bf9a4f0c54d19e)

> **Frontend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-73299
- 関連キーワード: typescript, javascript, node.js
- 影響製品: -
- 公開日: 2026-08-13 03:18:15 JST
- 更新日: 2026-08-13 05:17:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Prompty is a markdown file format (.prompty) for LLM prompts. Prior to 0.1.5 and 2.0.0-beta.5, the TypeScript Nunjucks renderer evaluated untrusted .prompty template bodies with unrestricted JavaScript member access. An attacker-controlled template could traverse constructor and prototype properties to execute JavaScri...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/microsoft/prompty/commit/e4a0ebf49e3a78d5d7796c8480bf9a4f0c54d19e
- https://github.com/microsoft/prompty/commit/f5c57c94a0990cca79d095c3daab661b4b1fb89f
- https://github.com/microsoft/prompty/pull/404
- https://github.com/microsoft/prompty/pull/405
- https://github.com/microsoft/prompty/security/advisories/GHSA-w28w-gp39-m4p6

### [CVE-2026-49467](https://github.com/smp46/pingvin-share-x/security/advisories/GHSA-59q6-jvp6-w282)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-49467
- 関連キーワード: javascript, gin, express
- 影響製品: -
- 公開日: 2026-08-13 03:17:30 JST
- 更新日: 2026-08-13 03:17:30 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Pingvin Share X is a secure and easy self-hosted file sharing platform. A vulnerability in versions 1.5.0 through 1.18.0 allow an attacker to bypass password verification when managing Time-based One-Time Password (TOTP) settings. The root cause is a missing `await` keyword on calls to the asynchronous `verifyPassword`...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/smp46/pingvin-share-x/security/advisories/GHSA-59q6-jvp6-w282

### [CVE-2026-49466](https://github.com/dartiss/draft-list/compare/2.6.3...2.6.4)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-49466
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-13 05:17:44 JST
- 更新日: 2026-08-13 05:17:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Draft List is a WordPress plugin to manage and promote unpublished content. Versions 2.6.3 and below are vulnerable to stored Cross-Site Scripting (XSS) in the `[drafts]` shortcode and Draft List widget when the documented custom `template` option places the `{{draft}}` placeholder inside an HTML attribute. The vulnera...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dartiss/draft-list/compare/2.6.3...2.6.4
- https://github.com/dartiss/draft-list/releases/tag/2.6.4
- https://github.com/dartiss/draft-list/security/advisories/GHSA-xxx9-hfqp-f83f

### [CVE-2026-73262](https://github.com/prowler-cloud/prowler/commit/6db407ed3c17d4c73a8f619fdb30580c8465027f)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-73262
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-13 00:18:30 JST
- 更新日: 2026-08-13 00:18:30 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Prowler is a cloud security platform. Prior to 5.37.0, Prowler's HTML output formatter in prowler/lib/outputs/html/html.py inserted finding.resource_tags, assembled by unroll_dict and parse_html_string, into generated reports without HTML escaping, allowing a cloud principal who can modify a scanned resource tag to sto...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/prowler-cloud/prowler/commit/6db407ed3c17d4c73a8f619fdb30580c8465027f
- https://github.com/prowler-cloud/prowler/pull/12221
- https://github.com/prowler-cloud/prowler/releases/tag/5.37.0
- https://github.com/prowler-cloud/prowler/security/advisories/GHSA-c2jg-2778-ggm4

### [CVE-2026-73374](https://github.com/vulnerability-lookup/vulnerability-lookup/commit/d29901655c50cf3c25737d9ea86180268df51b57)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-73374
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-13 00:18:33 JST
- 更新日: 2026-08-13 03:18:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A stored cross-site scripting (XSS) vulnerability existed in Vulnerability-Lookup in the render_tag_badges Jinja filter used to display reference tags associated with vulnerability records. Values from containers.cna.references[].tags[] were directly interpolated into HTML badge elements and the resulting string was wr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vulnerability-lookup/vulnerability-lookup/commit/d29901655c50cf3c25737d9ea86180268df51b57

### [CVE-2026-18433](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-2-released/)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-18433
- 関連キーワード: graphql, gin
- 影響製品: -
- 公開日: 2026-08-13 05:17:41 JST
- 更新日: 2026-08-13 05:17:41 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: GitLab has remediated an issue in GitLab EE affecting all versions from 19.1 before 19.1.4 and 19.2 before 19.2.2 that under certain conditions could have allowed an authenticated user to read policy configuration belonging to a namespace they were not authorized to access, due to incorrect authorization checks in a Gr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-2-released/
- https://gitlab.com/gitlab-org/gitlab/-/work_items/607556
- https://hackerone.com/reports/3776182

### [CVE-2026-73295](https://github.com/squidfunk/mkdocs-material/commit/52fb6be8aafe326419f34dc94d3211e7bbfbfb25)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-73295
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-13 02:17:32 JST
- 更新日: 2026-08-13 02:17:32 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Material for MkDocs is a powerful documentation framework built on top of MkDocs. From 7.2.0 until 9.7.7, the mountSearchSuggest function in src/templates/assets/javascripts/components/search/suggest/index.ts contains a DOM-based cross-site scripting vulnerability in the optional search.suggest feature that allows a cr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/squidfunk/mkdocs-material/commit/52fb6be8aafe326419f34dc94d3211e7bbfbfb25
- https://github.com/squidfunk/mkdocs-material/releases/tag/9.7.7
- https://github.com/squidfunk/mkdocs-material/security/advisories/GHSA-xvg9-69gf-fjrf

### [CVE-2026-16694](https://www.ibm.com/support/pages/node/7283292)

> **Frontend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-16694
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-13 02:17:23 JST
- 更新日: 2026-08-13 05:53:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: IBM i 7.6, 7.5, 7.4, and 7.3 is vulnerable to stored cross-site scripting. This vulnerability allows an authenticated user to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials disclosure within a trusted session.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7283292

### [CVE-2026-19657](https://www.tenable.com/security/research/tra-2026-55)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-19657
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-13 05:17:43 JST
- 更新日: 2026-08-13 05:17:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ScadaLTS 2.7.8.1 reflects user-supplied input into an HTML response without sanitization. An unauthenticated attacker who lures a victim into visiting a crafted URL can execute arbitrary JavaScript in the context of the victim's browser session.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.tenable.com/security/research/tra-2026-55

### [CVE-2026-48550](https://github.com/NagiosEnterprises/nagioscore/blob/master/Changelog)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-48550
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-13 02:17:27 JST
- 更新日: 2026-08-13 04:17:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nagios Core before 4.5.14 and Nagios XI before 2026R1.7 are vulnerable to reflected cross-site scripting in cmd.cgi via the NagFormId parameter. An unauthenticated remote attacker can craft a malicious link that, when followed by an authenticated user, executes arbitrary JavaScript in the victim's browser.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/NagiosEnterprises/nagioscore/blob/master/Changelog
- https://www.nagios.com/security-disclosures/nagios-core/
- https://www.vulncheck.com/advisories/nagios-core-xi-cmd-cgi-reflected-xss-via-nagformid-parameter

### [CVE-2026-48552](https://github.com/NagiosEnterprises/nagioscore/blob/master/Changelog)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-48552
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-13 02:17:27 JST
- 更新日: 2026-08-13 02:17:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nagios Core before 4.5.14 and Nagios XI before 2026R1.7 are vulnerable to DOM-based cross-site scripting in jsonquery.js. Unencoded JSON string values reflected from stored fields are inserted into the DOM without sanitization, allowing attackers to run arbitrary JavaScript in the victim's browser.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/NagiosEnterprises/nagioscore/blob/master/Changelog
- https://www.nagios.com/security-disclosures/nagios-core/
- https://www.vulncheck.com/advisories/nagios-core-xi-dom-based-xss-via-jsonquery-js

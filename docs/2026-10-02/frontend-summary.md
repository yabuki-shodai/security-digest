# Frontend CVE Summary (2026-10-02)

## Overview

- 取得日時: 2026-10-02 10:37:46 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 12
- Critical: 1
- High: 7
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-103004](https://github.com/vercel/next.js/releases/tag/v16.3.8)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-103004
- 関連キーワード: next.js, redis
- 影響製品: -
- 公開日: 2026-10-02 00:17:25 JST
- 更新日: 2026-10-02 02:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Next.js versions from 16.3.0 to 16.3.7 warm `use cache` handlers using `next/root-params` and can leak their return value to pages with different root params. With Cache Components enabled (cacheComponents: true), a 'use cache' function that calls another 'use cache' function that reads a root param can be keyed incorr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vercel/next.js/releases/tag/v16.3.8
- https://github.com/vercel/next.js/security/advisories/GHSA-h694-7cp9-m8p3

### [CVE-2026-102667](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-275-03.json)

> **Frontend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-102667
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-02 05:17:21 JST
- 更新日: 2026-10-02 05:31:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joyland AI app allows an attacker with shared network access to inject JavaScript into content loaded in WebView. Without user-granted permissions, an attacker could access the clipboard, make arbitrary HTTP requests via the Weex 'stream' module, or access app-internal storage. If the installed app has been granted per...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-275-03.json
- https://www.cve.org/CVERecord?id=CVE-2026-1026667

### [CVE-2026-103921](https://github.com/ardatan/graphql-tools/commit/3831a0661514c91d99971052f983552556880402)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-103921
- 関連キーワード: graphql, node.js
- 影響製品: -
- 公開日: 2026-10-02 02:17:19 JST
- 更新日: 2026-10-02 04:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GraphQL Tools provides utilities for building, stitching, and mocking GraphQL schemas. Prior to 1.1.35, the executor-legacy-ws buildWSLegacyExecutor() function hardcodes TLS certificate rejection off for Node.js connections to wss:// endpoints. Applications using the executor directly, or url-loader with SubscriptionPr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/ardatan/graphql-tools/commit/3831a0661514c91d99971052f983552556880402
- https://github.com/ardatan/graphql-tools/pull/8426
- https://github.com/ardatan/graphql-tools/releases/tag/@graphql-tools/executor-legacy-ws@1.1.35
- https://github.com/ardatan/graphql-tools/security/advisories/GHSA-6fw5-9hq8-w87g

### [CVE-2023-54404](https://github.com/colinhacks/zod/issues/1872)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2023-54404
- 関連キーワード: zod
- 影響製品: -
- 公開日: 2026-10-02 03:17:11 JST
- 更新日: 2026-10-02 03:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zod schema-validation library through 4.6.5 contains an uncontrolled resource consumption vulnerability that allows attackers to exhaust memory by submitting a large array to an application using an array schema without a length constraint. Attackers can exploit the handleArrayResult parse logic in $ZodArray, which acc...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/colinhacks/zod/issues/1872
- https://github.com/colinhacks/zod/pull/6475
- https://www.vulncheck.com/advisories/zod-uncontrolled-resource-consumption-via-array-validation

### [CVE-2026-54049](https://github.com/sakaiproject/sakai/commit/2696b4b48cbef2e81512f52f84f7477adff78b27)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-54049
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-02 05:17:25 JST
- 更新日: 2026-10-02 05:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Sakai is a Collaboration and Learning Environment (CLE). From versions 23.0 to before 23.5, and versions 25.0 to before 25.3, the Sakai Conversations tool stores topic and post messages without HTML sanitization, and the frontend renders them using LitElement's unsafeHTML() directive, resulting in stored cross-site scr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/sakaiproject/sakai/commit/2696b4b48cbef2e81512f52f84f7477adff78b27
- https://github.com/sakaiproject/sakai/security/advisories/GHSA-w2x5-gv52-9ccv

### [CVE-2026-55230](https://github.com/givanz/Vvveb/releases/tag/1.0.8.6)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-55230
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-02 04:17:21 JST
- 更新日: 2026-10-02 05:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vvveb is a powerful and easy to use CMS with page builder to build websites, blogs or ecommerce stores. Prior to version 1.0.8.6, Vvveb's HTML sanitizer fails to strip event-handler attributes when a tag carries a greater-than character inside a quoted attribute value. A low-privilege content author (default role autho...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/givanz/Vvveb/releases/tag/1.0.8.6
- https://github.com/givanz/Vvveb/security/advisories/GHSA-97xr-82vc-wj2v
- https://github.com/givanz/Vvveb/security/advisories/GHSA-97xr-82vc-wj2v

### [CVE-2026-70650](https://github.com/GetSimpleCMS-CE/GetSimpleCMS-CE/security/advisories/GHSA-p6vf-2xr7-mcf4)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-70650
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-02 05:17:29 JST
- 更新日: 2026-10-02 05:23:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. In versions 3.3.22 and prior, an authenticated stored Cross-Site Scripting (XSS) vulnerability exists in the page backup viewer (admin/backup-edit.php). Page fields are correctly HTML-encoded when a page is sa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/GetSimpleCMS-CE/GetSimpleCMS-CE/security/advisories/GHSA-p6vf-2xr7-mcf4

### [CVE-2026-71542](https://github.com/GetSimpleCMS-CE/GetSimpleCMS-CE/security/advisories/GHSA-vqfh-838q-xfqh)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-71542
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-02 05:17:29 JST
- 更新日: 2026-10-02 05:23:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. In versions 3.3.22 and prior, GetSimpleCMS-CE is vulnerable to stored Cross-Site Scripting (XSS) in the "Theme to Components" functionality (admin/components.php) via the title parameter. The stored title is r...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/GetSimpleCMS-CE/GetSimpleCMS-CE/security/advisories/GHSA-vqfh-838q-xfqh
- https://github.com/GetSimpleCMS-CE/GetSimpleCMS-CE/security/advisories/GHSA-vqfh-838q-xfqh

### [CVE-2026-103923](https://github.com/KaTeX/KaTeX/commit/0adf7e77db6915d991803b29699f82b1ccf8d4f4)

> **Frontend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-103923
- 関連キーワード: javascript, express
- 影響製品: -
- 公開日: 2026-10-02 03:17:13 JST
- 更新日: 2026-10-02 03:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KaTeX is a fast, easy-to-use JavaScript library for TeX math rendering on the web. From 0.11.0 until 0.18.2, KaTeX uses ordinary JavaScript property access for the renderer options object, the trust setting, default and processor setting metadata, and namespace lookup and group restoration, allowing inherited propertie...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/KaTeX/KaTeX/commit/0adf7e77db6915d991803b29699f82b1ccf8d4f4
- https://github.com/KaTeX/KaTeX/pull/4260
- https://github.com/KaTeX/KaTeX/releases/tag/v0.18.2
- https://github.com/KaTeX/KaTeX/security/advisories/GHSA-238p-pmpm-9mq7

### [CVE-2026-96780](https://github.com/patorjk/figlet.js/commit/cb2839d0e53aeafbd361e9587abc72e49e41cbb3)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-96780
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-02 06:17:26 JST
- 更新日: 2026-10-02 06:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: figlet.js is a FIG driver written in JavaScript that aims to implement the FIGfont specification. Prior to 1.11.3, text() and textSync() can enter an unbounded loop when whitespaceBreak is enabled and width is smaller than the rendered width of a single FIGlet character. Under these conditions, breakWord() cannot find...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/patorjk/figlet.js/commit/cb2839d0e53aeafbd361e9587abc72e49e41cbb3
- https://github.com/patorjk/figlet.js/pull/169
- https://github.com/patorjk/figlet.js/security/advisories/GHSA-62ch-8vmq-8xm7

### [CVE-2026-101890](https://wordpress.org/plugins/prime-mover/#developers)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-101890
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-02 02:17:17 JST
- 更新日: 2026-10-02 04:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The Prime Mover plugin for WordPress before 2.2.1 contains a stored cross-site scripting vulnerability that allows attackers to execute arbitrary JavaScript by injecting an unescaped site_title value in a package's footprint.json file. Attackers can place a crafted package under the prime-mover-export-files directory s...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://wordpress.org/plugins/prime-mover/#developers
- https://www.vulncheck.com/advisories/prime-mover-stored-xss-via-package-metadata

### [CVE-2026-67104](https://support.hcl-software.com/csm?id=kb_article&sysparm_article=KB0134015)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-67104
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-02 00:17:31 JST
- 更新日: 2026-10-02 05:36:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HCL BigFix Service Management is affected by an Information Disclosure vulnerability, which could allow an unauthenticated attacker to analyze publicly accessible JavaScript files, enabling the discovery of hidden administrative API endpoints for further targeted exploitation.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://support.hcl-software.com/csm?id=kb_article&sysparm_article=KB0134015

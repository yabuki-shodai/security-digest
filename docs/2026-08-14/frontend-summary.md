# Frontend CVE Summary (2026-08-14)

## Overview

- 取得日時: 2026-08-14 07:57:12 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 15
- Critical: 3
- High: 2
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-55987](https://blog.gitea.com/gitea-1.27.0-is-released/)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-55987
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-08-14 02:17:25 JST
- 更新日: 2026-08-14 02:17:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OAuth2 sign-in reactivates an administrator-deactivated account on auth sources without refresh tokens (incomplete fix of #38009)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://blog.gitea.com/gitea-1.27.0-is-released/
- https://github.com/go-gitea/gitea/releases/tag/v1.27.0
- https://github.com/go-gitea/gitea/security/advisories/GHSA-vrhc-jjfc-m3m3

### [CVE-2026-73651](https://github.com/typeorm/typeorm/commit/41d1c62fe49f99c3ca916d4d986f61ee9f45d519)

> **Frontend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-73651
- 関連キーワード: typescript, javascript, gin, node.js, typeorm, postgresql, mysql
- 影響製品: -
- 公開日: 2026-08-14 04:17:38 JST
- 更新日: 2026-08-14 04:17:38 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: TypeORM is a TypeScript and JavaScript ORM for Node.js that supports PostgreSQL, MySQL, MariaDB, SQLite, SQL Server, Oracle, and other databases. Prior to versions 0.3.31 and 1.1.0, typeorm migration:generate embeds database schema metadata into JavaScript or TypeScript template literals in src/commands/MigrationGenera...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/typeorm/typeorm/commit/41d1c62fe49f99c3ca916d4d986f61ee9f45d519
- https://github.com/typeorm/typeorm/commit/b175f9b8be422edd2a2ac035ba90c3f2ce782dfe
- https://github.com/typeorm/typeorm/releases/tag/0.3.31
- https://github.com/typeorm/typeorm/releases/tag/1.1.0
- https://github.com/typeorm/typeorm/security/advisories/GHSA-2rp8-mm9q-fp49

### [CVE-2026-42931](https://blog.gitea.com/gitea-1.27.0-is-released/)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-42931
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-08-14 02:17:22 JST
- 更新日: 2026-08-14 05:17:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Denial of Service via Unbounded io.ReadAll in NPM Package Tag Endpoint
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://blog.gitea.com/gitea-1.27.0-is-released/
- https://github.com/go-gitea/gitea/releases/tag/v1.27.0
- https://github.com/go-gitea/gitea/security/advisories/GHSA-wwqq-x6w4-frm2

### [CVE-2026-73653](https://github.com/vitest-dev/vitest/commit/33f96a145ef09ca6a43b4e555eb273e64a87be23)

> **Frontend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-73653
- 関連キーワード: vite, vitest
- 影響製品: -
- 公開日: 2026-08-14 04:17:38 JST
- 更新日: 2026-08-14 04:17:38 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Vitest is a testing framework powered by Vite. Prior to versions 3.2.7, 4.1.10, and 5.0.0-beta.6, Browser Mode provider commands including upload, takeScreenshot, screenshotMatcher, stopChunkTrace, deleteTracing, and annotateTraces accept browser-supplied file paths without enforcing the allowWrite permission gate or c...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vitest-dev/vitest/commit/33f96a145ef09ca6a43b4e555eb273e64a87be23
- https://github.com/vitest-dev/vitest/commit/5c18dd267ff7f47f24cab2f615a16b37d90feb7f
- https://github.com/vitest-dev/vitest/commit/b795e36b34969bec50b47a9f29d26f799a6a04fb
- https://github.com/vitest-dev/vitest/pull/10674
- https://github.com/vitest-dev/vitest/pull/10679

### [CVE-2026-73567](https://github.com/JuneAndGreen/sm-crypto/commit/1f9bd7bd160c24efd9c26c8f7fda997c68c823d0)

> **Frontend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-73567
- 関連キーワード: javascript, go, node.js
- 影響製品: -
- 公開日: 2026-08-14 03:18:19 JST
- 更新日: 2026-08-14 03:18:19 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: sm-crypto provides JavaScript implementations of the Chinese cryptographic algorithms SM2, SM3, and SM4. Prior to 0.5.0, the default no-argument sm2.generateKeyPairHex() path in Node.js uses the module-wide SecureRandom instance in src/sm2/utils.js, supplied by jsbn@1.1.0, which seeds an ARC4 stream from Math.random()...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/JuneAndGreen/sm-crypto/commit/1f9bd7bd160c24efd9c26c8f7fda997c68c823d0
- https://github.com/JuneAndGreen/sm-crypto/security/advisories/GHSA-vh45-f885-3848

### [CVE-2026-73649](https://github.com/shepherdwind/velocity.js/commit/f8e47a6c4607249b9c967d3a1ced959b4dd64dba)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-73649
- 関連キーワード: javascript, gin, express
- 影響製品: -
- 公開日: 2026-08-14 03:18:20 JST
- 更新日: 2026-08-14 03:18:20 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Velocity.js is a JavaScript implementation of the Apache Velocity template engine. Prior to 2.1.7, the earlier fix for CVE-2026-44966 filtered constructor, __proto__, and prototype only in the #set assignment handler in src/compile/set.ts, while property-read expressions in src/compile/references.ts remained unfiltered...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/shepherdwind/velocity.js/commit/f8e47a6c4607249b9c967d3a1ced959b4dd64dba
- https://github.com/shepherdwind/velocity.js/pull/192
- https://github.com/shepherdwind/velocity.js/releases/tag/v2.1.7
- https://github.com/shepherdwind/velocity.js/security/advisories/GHSA-7gfh-x38p-prh3

### [CVE-2026-73650](https://github.com/svg/svgo/commit/628e3bc7336625a30365d0a9b60185307d852466)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-73650
- 関連キーワード: javascript, go, gin, node.js
- 影響製品: -
- 公開日: 2026-08-14 04:17:38 JST
- 更新日: 2026-08-14 04:17:38 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SVGO, short for SVG Optimizer, is a Node.js library and command-line application for optimizing SVG files. From version 1.0.0 until versions 2.8.3, 3.3.4, and 4.0.2, the removeScripts plugin, named removeScriptElement in versions 1 through 3, can leave executable content in optimized SVGs because it does not remove nam...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/svg/svgo/commit/628e3bc7336625a30365d0a9b60185307d852466
- https://github.com/svg/svgo/commit/72a23886b4698b27624b936f3a15a80afd36d75f
- https://github.com/svg/svgo/commit/f529cfccc6c154d6f6eabe276ec637a8c5db6763
- https://github.com/svg/svgo/releases/tag/v2.8.3
- https://github.com/svg/svgo/releases/tag/v3.3.4

### [CVE-2026-49856](https://github.com/vmoranv/jshookmcp/commit/02111311f7bd0f86a7d7ef8538986594b3a18afa)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-49856
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-14 00:19:41 JST
- 更新日: 2026-08-14 03:17:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: @jshookmcp/jshook is an MCP server that gives AI agents tools for JavaScript analysis and security research. In version 0.3.1, he network domain has a central SSRF authorization policy that blocks private, loopback, link-local, and reserved targets unless an explicit authorization object allows private network access....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vmoranv/jshookmcp/commit/02111311f7bd0f86a7d7ef8538986594b3a18afa
- https://github.com/vmoranv/jshookmcp/security/advisories/GHSA-c5r6-m4mr-8q5j
- https://github.com/vmoranv/jshookmcp/security/advisories/GHSA-c5r6-m4mr-8q5j

### [CVE-2026-73643](https://github.com/nodeca/js-yaml/commit/3e5240f9cbe645ce5afb58524954a13c8539c853)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-73643
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-08-14 03:18:19 JST
- 更新日: 2026-08-14 03:18:19 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: js-yaml is a JavaScript YAML parser and dumper. From 5.0.0 until 5.2.2, parsing a small YAML document can take exponential time when an application calls load() or loadAll() on untrusted input. In src/parser/parser.ts, readFlowCollection uses restoreState and calls parseNode a second time when a flow-sequence entry is...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nodeca/js-yaml/commit/3e5240f9cbe645ce5afb58524954a13c8539c853
- https://github.com/nodeca/js-yaml/security/advisories/GHSA-pm4m-ph32-ghv5

### [CVE-2026-73647](https://github.com/quasarframework/quasar/commit/d0a95d95ab3c29d13e1b8ba8c5e5025fd6ce35e7)

> **Frontend** / **MEDIUM** / CVSS: **5.6** / KEV: **no**

- タイトル: CVE-2026-73647
- 関連キーワード: javascript, vue
- 影響製品: -
- 公開日: 2026-08-14 03:18:20 JST
- 更新日: 2026-08-14 04:17:36 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Quasar Framework is a framework for building high-performance Vue.js user interfaces. Prior to 2.22.0, the public extend() utility in ui/src/utils/extend/extend.js recursively copied attacker-controlled object keys during extend(true, target, source) deep merges without rejecting an own __proto__ property. The merge co...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/quasarframework/quasar/commit/d0a95d95ab3c29d13e1b8ba8c5e5025fd6ce35e7
- https://github.com/quasarframework/quasar/releases/tag/quasar-v2.22.0
- https://github.com/quasarframework/quasar/security/advisories/GHSA-3r53-75j5-3g7j
- https://github.com/quasarframework/quasar/security/advisories/GHSA-3r53-75j5-3g7j

### [CVE-2026-73671](https://github.com/DevVaibhav07/VULN-POC/blob/main/Saurus_OpenRedirect.md)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-73671
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-08-14 01:19:07 JST
- 更新日: 2026-08-14 01:19:07 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Saurus CMS Community Edition contains an unauthenticated open redirect vulnerability in the logout handling code in classes/port.inc.php, where the url parameter supplied via GET or POST is passed directly to the Location header without domain allowlist, scheme validation, or relative path enforcement. Attackers can cr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/DevVaibhav07/VULN-POC/blob/main/Saurus_OpenRedirect.md
- https://github.com/sauruscms/Saurus-CMS-Community-Edition
- https://www.vulncheck.com/advisories/saurus-cms-unauthenticated-open-redirect-via-logout-url-parameter

### [CVE-2026-73572](https://wiki.zimbra.com/wiki/Zimbra_Responsible_Disclosure_Policy)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-73572
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-14 01:19:06 JST
- 更新日: 2026-08-14 01:19:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: In Zimbra Collaboration (ZCS) before 10.1.17, a stored cross-site scripting (XSS) vulnerability exists in the Zimbra Classic Web Client due to insufficient sanitization of specific attachment content during inline preview. An attacker can send a crafted email containing a malicious attachment that, when previewed by a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://wiki.zimbra.com/wiki/Zimbra_Responsible_Disclosure_Policy
- https://wiki.zimbra.com/wiki/Zimbra_Security_Advisories

### [CVE-2026-19744](https://github.com/ccyl13/Pentestify/commit/272f7d6033fd93fbc858835f55d616157041f123)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-19744
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-14 01:17:59 JST
- 更新日: 2026-08-14 03:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Cross-site Scripting in the Markdown renderer in maalfer Pentestify before 2.3.2 allows authenticated users to execute arbitrary JavaScript in the application origin via a Markdown link whose URL contains a double quote, which closes the anchor's href attribute because the renderer's sanitization step does not escape q...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/ccyl13/Pentestify/commit/272f7d6033fd93fbc858835f55d616157041f123
- https://github.com/ccyl13/Pentestify/releases/tag/v2.3.2
- https://secur0.com/en/cna/cve-list/cve-2026-19744-stored-xss-in-pentestify-markdown-renderer-via-unescaped-quotes

### [CVE-2026-73037](https://github.com/DayuanJiang/next-ai-draw-io/issues/917)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-73037
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-14 04:17:33 JST
- 更新日: 2026-08-14 04:17:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Next AI Draw.io 0.2.1 through 0.4.16 contains a reflected cross-site scripting vulnerability in the mcp query parameter that is interpolated without escaping into HTML and JavaScript. Attackers can craft malicious URLs to execute arbitrary JavaScript in the localhost origin, enabling exfiltration of diagram sessions an...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/DayuanJiang/next-ai-draw-io/issues/917
- https://www.vulncheck.com/advisories/next-ai-draw-io-reflected-xss-via-unsanitized-mcp-query-parameter

### [CVE-2026-73038](https://github.com/NodeBB/NodeBB/commit/c0d94a217edcafcdb9b3920a6e80935194bcb19e)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-73038
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-14 04:17:34 JST
- 更新日: 2026-08-14 04:17:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: NodeBB before 4.15.0 contains a stored cross-site scripting vulnerability in the renderEmoji function that fails to escape tag.icon.url and tag.name attributes. Attackers can deliver malicious ActivityPub Create/Note objects with crafted emoji tags to inject arbitrary HTML and JavaScript into stored post content, execu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/NodeBB/NodeBB/commit/c0d94a217edcafcdb9b3920a6e80935194bcb19e
- https://github.com/NodeBB/NodeBB/issues/14601
- https://github.com/NodeBB/NodeBB/releases/tag/v4.15.0
- https://www.vulncheck.com/advisories/nodebb-stored-xss-via-activitypub-emoji-tag-icon-url-and-tag-name

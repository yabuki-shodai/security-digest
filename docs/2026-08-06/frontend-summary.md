# Frontend CVE Summary (2026-08-06)

## Overview

- 取得日時: 2026-08-06 08:14:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 28
- Critical: 2
- High: 9
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-71319](https://github.com/nuxt/devtools/commit/a7b2718b930766e1ffb0640259d53f5b041a50b4)

> **Frontend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-71319
- 関連キーワード: vue, nuxt, vite, gin
- 影響製品: -
- 公開日: 2026-08-06 07:17:08 JST
- 更新日: 2026-08-06 07:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nuxt is an open-source web development framework for Vue.js. Prior to 3.3.1, Nuxt DevTools (development mode only) exposes a bidirectional RPC channel over the Vite HMR WebSocket via the nuxt:devtools:rpc plugin. On affected versions the channel has no authentication: any client that can reach the Vite HMR endpoint (ws...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nuxt/devtools/commit/a7b2718b930766e1ffb0640259d53f5b041a50b4
- https://github.com/nuxt/devtools/releases/tag/v3.3.1
- https://github.com/nuxt/nuxt/security/advisories/GHSA-279x-mwfv-vcqv

### [CVE-2026-9195](https://community.progress.com/s/article/Marklogic-Critical-Security-Alert-Bulletin-August-2026)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-9195
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-06 01:17:10 JST
- 更新日: 2026-08-06 04:17:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A cross-site scripting vulnerability in the Query Console of Progress MarkLogic Server before 11.3.6 and 12.0.3 allows a remote attacker who lures an authenticated administrator to a crafted URL to execute arbitrary JavaScript in the administrator's browser session, capture credentials, and perform privileged actions o...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://community.progress.com/s/article/Marklogic-Critical-Security-Alert-Bulletin-August-2026

### [CVE-2026-66298](https://cna.erlef.org/cves/CVE-2026-66298.html)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-66298
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-06 05:17:12 JST
- 更新日: 2026-08-06 05:17:12 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Origin Validation Error vulnerability in livebook-dev livebook allows untrusted notebook output JavaScript to trigger session-wide keyboard shortcuts, including forced evaluation of all cells and runtime restart. Livebook's JS-view feature renders notebook-defined JavaScript inside a sandboxed, cross-origin iframe spec...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-66298.html
- https://github.com/livebook-dev/livebook/commit/296318ffdfa6e5ed7b18ad8d5a5b2af90f3cd728
- https://github.com/livebook-dev/livebook/commit/5980e5c6b71036806b3bf54101eb1d6c0f50f19c
- https://github.com/livebook-dev/livebook/commit/a552ce8f99ad348ea37061394dc950a0cebdb33e
- https://github.com/livebook-dev/livebook/security/advisories/GHSA-68c2-prqg-x62g

### [CVE-2026-70604](https://github.com/electron/electron/security/advisories/GHSA-v3j7-r9gq-3gjw)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-70604
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-06 01:17:04 JST
- 更新日: 2026-08-06 04:17:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.10, 40.9.3, 41.4.0, and 42.0.0, a custom scheme registered with supportFetchAPI: true but without corsEnabled: true was not subject to CORS enforcement. A page loaded from a remote origin could therefor...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/security/advisories/GHSA-v3j7-r9gq-3gjw

### [CVE-2026-71314](https://github.com/nuxt/nuxt/commit/4e35ae9babd94be53246e31200232d48438bb34e)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-71314
- 関連キーワード: vue, nuxt
- 影響製品: -
- 公開日: 2026-08-06 06:16:59 JST
- 更新日: 2026-08-06 06:16:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nuxt is an open-source web development framework for Vue.js. From 3.1.0 until 3.21.10 and 4.5.1, an unauthenticated attacker can use a server island v-for prop, including vforToArray and , to trigger unbounded SSR memory allocation until MAX_VFOR_LENGTH = 100000 and crash the Nuxt process. This issue is fixed in 3.21.1...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nuxt/nuxt/commit/4e35ae9babd94be53246e31200232d48438bb34e
- https://github.com/nuxt/nuxt/commit/668cdfdfda41849ed11c1ee5e2067a11fc103b22
- https://github.com/nuxt/nuxt/releases/tag/v3.21.10
- https://github.com/nuxt/nuxt/releases/tag/v4.5.1
- https://github.com/nuxt/nuxt/security/advisories/GHSA-hxcr-hm88-mpq6

### [CVE-2026-71315](https://github.com/nuxt/nuxt/commit/619963309e082190bac4a26b05f2dd155b039b81)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-71315
- 関連キーワード: vue, nuxt
- 影響製品: -
- 公開日: 2026-08-06 06:16:59 JST
- 更新日: 2026-08-06 06:16:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nuxt is an open-source web development framework for Vue.js. From 3.21.7 until 3.21.10 and 4.5.1, mixed-case routeRules keys can fail to match case-folded lookups when router.options.sensitive is false and drop appMiddleware authorization gates. This is caused by an incomplete fix for CVE-2026-53721. This issue is fixe...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nuxt/nuxt/commit/619963309e082190bac4a26b05f2dd155b039b81
- https://github.com/nuxt/nuxt/commit/ad624a75ad2d215f43633f6b40be346a7194d34d
- https://github.com/nuxt/nuxt/releases/tag/v3.21.10
- https://github.com/nuxt/nuxt/releases/tag/v4.5.1
- https://github.com/nuxt/nuxt/security/advisories/GHSA-hxvh-4h3w-prp9

### [CVE-2026-71316](https://github.com/nuxt/nuxt/commit/ac9b41a36b62296a117862254ee7d2b21a2a5203)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-71316
- 関連キーワード: vue, nuxt
- 影響製品: -
- 公開日: 2026-08-06 07:17:07 JST
- 更新日: 2026-08-06 07:17:07 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nuxt is an open-source web development framework for Vue.js. From 4.4.0 until 4.5.1, runtime cache:nuxt:payload entries for /<page>/_payload.json can be returned before route middleware and page guards because import.meta.prerender is not enforced, disclosing another user's SSR data. This issue is fixed in 4.5.1.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nuxt/nuxt/commit/ac9b41a36b62296a117862254ee7d2b21a2a5203
- https://github.com/nuxt/nuxt/releases/tag/v4.5.1
- https://github.com/nuxt/nuxt/security/advisories/GHSA-wm8w-6qjm-cv43

### [CVE-2026-71320](https://github.com/nuxt/nuxt/commit/5b60017f7f1d5e9384cadf1d6c580b99d583c418)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-71320
- 関連キーワード: vue, nuxt
- 影響製品: -
- 公開日: 2026-08-06 07:17:08 JST
- 更新日: 2026-08-06 07:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nuxt is an open-source web development framework for Vue.js. From 3.4.0 until 3.21.10 and 4.5.1, an attacker can inject a template key through /__nuxt_island/ props into a dynamic component when `vue.runtimeCompiler: true` is enabled, causing template execution in the Nitro process. This issue is fixed in 3.21.10 and 4...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nuxt/nuxt/commit/5b60017f7f1d5e9384cadf1d6c580b99d583c418
- https://github.com/nuxt/nuxt/commit/ee6c846338f4eb75801815dda86df1f494725859
- https://github.com/nuxt/nuxt/releases/tag/v3.21.10
- https://github.com/nuxt/nuxt/releases/tag/v4.5.1
- https://github.com/nuxt/nuxt/security/advisories/GHSA-9473-5f9j-94wq

### [CVE-2026-71321](https://github.com/nuxt/nuxt/commit/4e35ae9babd94be53246e31200232d48438bb34e)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-71321
- 関連キーワード: vue, nuxt
- 影響製品: -
- 公開日: 2026-08-06 07:17:08 JST
- 更新日: 2026-08-06 07:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nuxt is an open-source web development framework for Vue.js. From 3.1.0 until 3.21.10 and 4.5.1, the internal island renderer endpoint `/__nuxt_island/...` decodes and hashes attacker-controlled JSON body input with destr and ohash before validating the URL-resident hash. An unauthenticated `POST /__nuxt_island/_.json`...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nuxt/nuxt/commit/4e35ae9babd94be53246e31200232d48438bb34e
- https://github.com/nuxt/nuxt/commit/668cdfdfda41849ed11c1ee5e2067a11fc103b22
- https://github.com/nuxt/nuxt/releases/tag/v3.21.10
- https://github.com/nuxt/nuxt/releases/tag/v4.5.1
- https://github.com/nuxt/nuxt/security/advisories/GHSA-9pgf-384g-p7mv

### [CVE-2026-70601](https://github.com/electron/electron/security/advisories/GHSA-h7rp-cf8h-j98x)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-70601
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-08-06 01:17:04 JST
- 更新日: 2026-08-06 03:17:14 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.9, 40.9.2, 41.2.2, and 42.0.0-beta.5, apps that expose Promise-returning functions to web content via contextBridge may be vulnerable to a context isolation bypass. Untrusted web content could obtain ac...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/security/advisories/GHSA-h7rp-cf8h-j98x

### [CVE-2026-70440](https://www.jenkins.io/security/advisory/2026-08-05/#SECURITY-3749)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-70440
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-06 03:17:13 JST
- 更新日: 2026-08-06 05:17:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Jenkins Qualys Container Scanning Connector Plugin 1.8.0.5 and earlier does not escape user-controlled field values in a JavaScript context, resulting in a stored cross-site scripting (XSS) vulnerability exploitable by attackers with Item/Configure permission.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.jenkins.io/security/advisory/2026-08-05/#SECURITY-3749

### [CVE-2026-70441](https://www.jenkins.io/security/advisory/2026-08-05/#SECURITY-3750)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-70441
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-06 03:17:13 JST
- 更新日: 2026-08-06 05:17:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Jenkins Summary Display Plugin 1.15 and earlier does not escape the job name in a JavaScript context in build report pages, resulting in a stored cross-site scripting (XSS) vulnerability exploitable by attackers with Item/Create or Item/Configure permission.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.jenkins.io/security/advisory/2026-08-05/#SECURITY-3750

### [CVE-2026-71318](https://github.com/nuxt/nuxt/releases/tag/v3.21.10)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-71318
- 関連キーワード: vue, nuxt
- 影響製品: -
- 公開日: 2026-08-06 07:17:08 JST
- 更新日: 2026-08-06 07:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nuxt is an open-source web development framework for Vue.js. From 3.1.0 until 3.21.10 and 4.5.1, an attacker can supply a top-level `as` prop to the /__nuxt_island/ endpoint and drive dynamic component resolution through <component :is>, resolveDynamicComponent, or h(). This issue is fixed in 3.21.10 and 4.5.1.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nuxt/nuxt/releases/tag/v3.21.10
- https://github.com/nuxt/nuxt/releases/tag/v4.5.1
- https://github.com/nuxt/nuxt/security/advisories/GHSA-48hr-524c-v5w3

### [CVE-2026-53992](https://github.com/projectsend/projectsend)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-53992
- 関連キーワード: javascript, gin, echo
- 影響製品: -
- 公開日: 2026-08-06 01:16:57 JST
- 更新日: 2026-08-06 01:16:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ProjectSend r2029 contains a reflected cross-site scripting vulnerability in thumbnails-regenerate.php that allows remote attackers to inject arbitrary HTML and JavaScript by supplying unsanitized values in the start_date and end_date GET parameters, which are echoed unescaped into HTML attribute values. Attackers can...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/projectsend/projectsend
- https://github.com/projectsend/projectsend/commit/b4ad95b1bd3d18b23261b7c3496bfbac8ebfe324
- https://www.vulncheck.com/advisories/reflected-xss-in-projectsend-thumbnails-regenerate-php-via-start-date-end-date-parameters

### [CVE-2026-70608](https://github.com/electron/electron/commit/3ff23c52ab364a0afc6ab5bd7851291d3159de57)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-70608
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-06 03:17:15 JST
- 更新日: 2026-08-06 04:17:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.10, 41.10.3, and 42.0.1, a sandboxed iframe without the allow-popups keyword could still open a new window or trigger setWindowOpenHandler with no user interaction because new-window navigations taking...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/3ff23c52ab364a0afc6ab5bd7851291d3159de57
- https://github.com/electron/electron/commit/57cbe329c4ae8aab5ac5ebdcb588adc9a11de0d3
- https://github.com/electron/electron/commit/68cf8b7d9122260f6b534a69a82c701a56cf159f
- https://github.com/electron/electron/pull/51437
- https://github.com/electron/electron/pull/51438

### [CVE-2026-70605](https://github.com/electron/electron/security/advisories/GHSA-v64r-4m7r-3mvq)

> **Frontend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-70605
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-06 01:17:04 JST
- 更新日: 2026-08-06 01:17:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.8, 40.9.0, 41.2.1, and 42.0.0-beta.3, when following HTTP redirects, net.fetch() and net.request() did not restrict which schemes a redirect could target. A remote server could redirect a request to a l...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/security/advisories/GHSA-v64r-4m7r-3mvq

### [CVE-2026-70599](https://github.com/electron/electron/commit/0cbdf2f0375466d701aa393c92e0ec29eb89ea6c)

> **Frontend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-70599
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-06 01:17:03 JST
- 更新日: 2026-08-06 04:17:38 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.7, 40.9.0, 41.2.0, and 42.0.0-beta.1, serial-port and media permission checks made from an iframe passed the top-level frame origin to session.setPermissionCheckHandler instead of the requesting iframe...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/0cbdf2f0375466d701aa393c92e0ec29eb89ea6c
- https://github.com/electron/electron/security/advisories/GHSA-9pf5-hg6p-4pwp

### [CVE-2026-70602](https://github.com/electron/electron/security/advisories/GHSA-m55f-7gqj-fr98)

> **Frontend** / **MEDIUM** / CVSS: **6.6** / KEV: **no**

- タイトル: CVE-2026-70602
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-06 01:17:04 JST
- 更新日: 2026-08-06 02:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.8, 40.9.0, 41.2.1, and 42.0.0-beta.3, extension tab and scripting APIs were not scoped to the extension's own session. A malicious or compromised extension loaded into one session could navigate, script...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/security/advisories/GHSA-m55f-7gqj-fr98

### [CVE-2026-70609](https://github.com/electron/electron/commit/04614eed17986bddc43eb509ec870424ee6a47d1)

> **Frontend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-70609
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-08-06 03:17:15 JST
- 更新日: 2026-08-06 05:17:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.7, 40.9.0, 41.2.0, and 42.0.0-beta.1, the mode option of webContents.openDevTools() was not sanitized before use by the DevTools frontend. If an attacker can influence this value, script under their con...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/04614eed17986bddc43eb509ec870424ee6a47d1
- https://github.com/electron/electron/commit/2046ae87731d80a7b535512ae19acb529e10e33b
- https://github.com/electron/electron/commit/969741f9f847c5c583f6bbc63ca22549dbd954ce
- https://github.com/electron/electron/commit/efc4d3c6b6f1c04f658ca0d9d2512dcfe78eb7ba
- https://github.com/electron/electron/pull/50665

### [CVE-2026-70597](https://github.com/electron/electron/commit/0a6291a97d210db3733689e70a51f5711e38ed35)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-70597
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-06 01:17:03 JST
- 更新日: 2026-08-06 01:17:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.8, 40.9.0, 41.2.1, and 42.0.0-beta.3, the check Electron uses on macOS to confirm it was launched by a same-signed parent process could be bypassed by a local process. Apps that enable fuse-based harden...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/0a6291a97d210db3733689e70a51f5711e38ed35
- https://github.com/electron/electron/security/advisories/GHSA-jm7p-cc5g-qwxx

### [CVE-2026-70600](https://github.com/electron/electron/security/advisories/GHSA-x8rc-wpg4-grpf)

> **Frontend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-70600
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-06 01:17:04 JST
- 更新日: 2026-08-06 01:17:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.8, 40.9.0, 41.2.1, and 42.0.0-beta.3, the native autofill popup could be positioned by a cross-origin iframe outside that iframe's bounds, over the embedding page's UI, enabling clickjacking or spoofing...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/security/advisories/GHSA-x8rc-wpg4-grpf

### [CVE-2026-70603](https://github.com/electron/electron/security/advisories/GHSA-5c9j-mhmv-5xgx)

> **Frontend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-70603
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-06 01:17:04 JST
- 更新日: 2026-08-06 04:17:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.6, 40.9.0, 41.1.1, and 42.0.0-beta.1, shell.openPath() did not reject paths containing embedded null bytes. Apps that perform string-only validation of file paths, for example checking the file extensio...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/security/advisories/GHSA-5c9j-mhmv-5xgx

### [CVE-2026-70606](https://github.com/electron/electron/security/advisories/GHSA-r4w5-6pfg-jxp5)

> **Frontend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-70606
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-06 01:17:04 JST
- 更新日: 2026-08-06 03:17:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 40.10.6, 41.9.1, 42.5.1, and 43.0.0, when a custom protocol handler returned a ProtocolResponse with a url and no session, Electron made the upstream request through defaultSession instead of the session tha...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/security/advisories/GHSA-r4w5-6pfg-jxp5

### [CVE-2026-70607](https://github.com/electron/electron/commit/30cf3882de75ee651bd4e5f27002f13fd3d3163a)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-70607
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-06 02:16:54 JST
- 更新日: 2026-08-06 04:17:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.8, 40.9.0, 41.2.1, and 42.0.0-beta.3, some window options supplied by web content in the window.open() features string were applied to the new BrowserWindow without an allowlist. Untrusted content could...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/30cf3882de75ee651bd4e5f27002f13fd3d3163a
- https://github.com/electron/electron/commit/4eff3dc09e4d1e62d649c5ce9902f532bb7469c7
- https://github.com/electron/electron/commit/615d62500fc7732d068274b796c49487e652e90b
- https://github.com/electron/electron/commit/fe2e7d0073949b4593b624b93abf1788f5377e55
- https://github.com/electron/electron/pull/50946

### [CVE-2026-70610](https://github.com/electron/electron/commit/17d5d26499cd279fab48f5f26527f8edc02a7713)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-70610
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-06 03:17:15 JST
- 更新日: 2026-08-06 03:17:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.9, 40.9.2, 41.2.2, and 42.0.0-beta.4, objects copied across the contextBridge boundary from untrusted content could carry an attacker-influenced prototype, enabling prototype-pollution-style attacks aga...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/17d5d26499cd279fab48f5f26527f8edc02a7713
- https://github.com/electron/electron/commit/23a6efb714dec80e2cf45d3054d18d701162e4dd
- https://github.com/electron/electron/commit/4ac50292d552fb510eb778392620c85308770a55
- https://github.com/electron/electron/commit/5b699544cbbed51bedb7c60d75c8c42be5825737
- https://github.com/electron/electron/pull/51083

### [CVE-2026-70611](https://github.com/electron/electron/commit/10fb5b39c5287f70c4bbcab4c24197f3871ec322)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-70611
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-06 03:17:15 JST
- 更新日: 2026-08-06 04:17:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.9, 40.9.2, 41.2.1, and 42.0.0-beta.3, the DevTools reveal in file manager action could launch the target file rather than reveal it. An attacker with a separate means of running script inside the DevToo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/10fb5b39c5287f70c4bbcab4c24197f3871ec322
- https://github.com/electron/electron/commit/1b8a298d629d5a642c816ea5f7505359de17b771
- https://github.com/electron/electron/commit/27bf1cae9274d5025684c7268496f435b7e06b44
- https://github.com/electron/electron/commit/7a1eb7e5585991b3726cedb890a6244f327f43de
- https://github.com/electron/electron/pull/50937

### [CVE-2026-70612](https://github.com/electron/electron/commit/08b9d0a220e267d1a2402a44bdd01a2e9aa320b5)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-70612
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-06 04:17:41 JST
- 更新日: 2026-08-06 05:17:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.8, 40.9.0, 41.2.1, and 42.0.0-beta.3, requests to open external protocol URLs from web content did not take iframe sandbox restrictions into account, so a sandboxed iframe could cause an OS-registered e...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/08b9d0a220e267d1a2402a44bdd01a2e9aa320b5
- https://github.com/electron/electron/commit/2764e4c35168855f614876051823db4f58a3714a
- https://github.com/electron/electron/commit/477dcf7afc6550715f9ec5e6f39ee38e5dd7bf39
- https://github.com/electron/electron/commit/c39e3d5687d57434c8d5fe814c5152efd2f631c3
- https://github.com/electron/electron/pull/50961

### [CVE-2026-70598](https://github.com/electron/electron/commit/2c24640e7b0b9c74fe9f44bce0fde138340ff4fb)

> **Frontend** / **LOW** / CVSS: **3.9** / KEV: **no**

- タイトル: CVE-2026-70598
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-06 01:17:03 JST
- 更新日: 2026-08-06 04:17:38 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 39.8.10, 40.9.0, 41.2.1, and 42.0.0-beta.3, offscreen rendering frame data received from the GPU process was not fully validated by the main process. A compromised GPU process could cause the main process to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/2c24640e7b0b9c74fe9f44bce0fde138340ff4fb
- https://github.com/electron/electron/security/advisories/GHSA-pfmc-3mgc-p6fp

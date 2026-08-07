# Frontend CVE Summary (2026-08-08)

## Overview

- 取得日時: 2026-08-08 07:51:11 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 13
- Critical: 1
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-19244](https://gist.github.com/YLChen-007/3de5f50d167a878f7530f57ed018d508)

> **Frontend** / **MEDIUM** / CVSS: **5.8** / KEV: **no**

- タイトル: CVE-2026-19244
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-08-08 06:17:27 JST
- 更新日: 2026-08-08 06:17:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability was detected in HKUDS nanobot up to 0.2.1. The affected element is the function connect_mcp_servers of the file nanobot/agent/tools/mcp.py of the component MCP enabledTools Scope Handler. Performing a manipulation results in improper access controls. The attack is possible to be carried out remotely. Th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gist.github.com/YLChen-007/3de5f50d167a878f7530f57ed018d508
- https://github.com/HKUDS/nanobot/
- https://github.com/HKUDS/nanobot/issues/4435
- https://github.com/HKUDS/nanobot/pull/4436
- https://github.com/HKUDS/nanobot/releases/tag/v0.3.0

### [CVE-2026-19243](https://gist.github.com/YLChen-007/8fcbf8e49e7be568e1a92e9e0414fdba)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-19243
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-08-08 05:16:50 JST
- 更新日: 2026-08-08 05:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A security vulnerability has been detected in HKUDS nanobot up to 0.2.1. Impacted is the function ExecTool._guard_command/ExecTool._spawn of the file nanobot/agent/tools/shell.py of the component Shell Allowlist Handler. Such manipulation leads to os command injection. The attack can be executed remotely. The exploit h...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gist.github.com/YLChen-007/8fcbf8e49e7be568e1a92e9e0414fdba
- https://github.com/HKUDS/nanobot/
- https://github.com/HKUDS/nanobot/issues/4521
- https://github.com/HKUDS/nanobot/pull/4562
- https://github.com/HKUDS/nanobot/releases/tag/v0.3.0

### [CVE-2026-19245](https://gist.github.com/YLChen-007/b25f3f185478e0b2cd0e727bf5c5ed9b)

> **Frontend** / **LOW** / CVSS: **3.3** / KEV: **no**

- タイトル: CVE-2026-19245
- 関連キーワード: react, gin
- 影響製品: -
- 公開日: 2026-08-08 06:17:27 JST
- 更新日: 2026-08-08 06:17:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A flaw has been found in HKUDS nanobot up to 0.2.1. The impacted element is the function ExecTool._prepare_command of the file nanobot/agent/tools/shell.py of the component Login-shell Environment Handler. Executing a manipulation can lead to information disclosure. The attack requires local access. The exploit has bee...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gist.github.com/YLChen-007/b25f3f185478e0b2cd0e727bf5c5ed9b
- https://github.com/HKUDS/nanobot/
- https://github.com/HKUDS/nanobot/issues/4518
- https://github.com/HKUDS/nanobot/pull/4525
- https://github.com/HKUDS/nanobot/releases/tag/v0.3.0

### [CVE-2026-59717](https://github.com/home-assistant/android/commit/26154d923c3813cd4650e124900780f4f796d094)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-59717
- 関連キーワード: vite, gin
- 影響製品: -
- 公開日: 2026-08-08 06:17:29 JST
- 更新日: 2026-08-08 06:17:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Home Assistant is open source home automation software focused on local control and privacy. Prior to 2026.6.1, the Android Companion app is vulnerable to an open redirect. The app passes the URL fragment from a homeassistant://invite deep link into the onboarding flow without ever displaying the destination hostname....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/home-assistant/android/commit/26154d923c3813cd4650e124900780f4f796d094
- https://github.com/home-assistant/android/pull/6955
- https://github.com/home-assistant/core/security/advisories/GHSA-68f4-97mf-f68w
- https://github.com/home-assistant/core/security/advisories/GHSA-68f4-97mf-f68w

### [CVE-2026-71851](https://github.com/brix/crypto-js/commit/b405ff597fb3ac76a7bdfbc72dca10ba1079b1d5)

> **Frontend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-71851
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-08 04:18:54 JST
- 更新日: 2026-08-08 04:18:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: crypto-js is a JavaScript library of crypto standards. Versions of crypto-js prior to 4.0.0 generate randomness in CryptoJS.lib.WordArray.random() using a custom variation of the Multiply-With-Carry pseudorandom number generator, seeded from Math.random(), instead of a cryptographically secure source. This generator wa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/brix/crypto-js/commit/b405ff597fb3ac76a7bdfbc72dca10ba1079b1d5
- https://github.com/brix/crypto-js/security/advisories/GHSA-rg76-677x-56q9
- https://www.coinspect.com/blog/ill-bloom-investigation

### [CVE-2026-48093](https://github.com/dartiss/code-embed/commit/399752029c62fea82a9bc13fd156713fb4d50ea8)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-48093
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-08 01:17:24 JST
- 更新日: 2026-08-08 01:17:24 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The Code Embed WordPress plugin prior to version 2.6.1 is vulnerable to stored Cross-Site Scripting (XSS) through the external URL embed feature in post content. The vulnerable code scans rendered content for URL embed tokens, fetches the remote URL, and inserts the remote response body into the page without output san...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dartiss/code-embed/commit/399752029c62fea82a9bc13fd156713fb4d50ea8
- https://github.com/dartiss/code-embed/releases/tag/2.6.1
- https://github.com/dartiss/code-embed/security/advisories/GHSA-7c9x-px5v-5hcp

### [CVE-2026-66062](https://github.com/sveltejs/kit/commit/82712fc02c24b1dcf5b25d7a52129cd8455f04f5)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-66062
- 関連キーワード: svelte, go, express
- 影響製品: -
- 公開日: 2026-08-08 02:17:06 JST
- 更新日: 2026-08-08 07:16:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SvelteKit is a framework for rapidly developing robust, performant web applications using Svelte. Prior to 2.70.2, the content negotiation header parser used by SvelteKit's request handling (for headers such as Accept) uses a regular expression vulnerable to quadratic backtracking, so a maliciously crafted header value...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/sveltejs/kit/commit/82712fc02c24b1dcf5b25d7a52129cd8455f04f5
- https://github.com/sveltejs/kit/releases/tag/@sveltejs/kit@2.70.2
- https://github.com/sveltejs/kit/security/advisories/GHSA-29g2-3rmr-qm68

### [CVE-2026-62293](https://github.com/hapifhir/org.hl7.fhir.core/commit/3a9befd8845f003095ed75f4b24b9a80630275be)

> **Frontend** / **MEDIUM** / CVSS: **5.0** / KEV: **no**

- タイトル: CVE-2026-62293
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-08 05:16:52 JST
- 更新日: 2026-08-08 06:17:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: HAPI FHIR is a complete implementation of the HL7 FHIR standard for healthcare interoperability in Java. Prior to 6.9.11, the hidden scan command concatenates attacker-controlled Implementation Guide titles, profile titles, and source references into scan.html without escaping in Scanner.java. As a result, a user who s...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/hapifhir/org.hl7.fhir.core/commit/3a9befd8845f003095ed75f4b24b9a80630275be
- https://github.com/hapifhir/org.hl7.fhir.core/security/advisories/GHSA-6vcw-fq7v-4vhw
- https://github.com/hapifhir/org.hl7.fhir.core/security/advisories/GHSA-6vcw-fq7v-4vhw

### [CVE-2026-71850](https://github.com/honojs/hono/security/advisories/GHSA-f23p-vx2j-j53r)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-71850
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-08 04:18:54 JST
- 更新日: 2026-08-08 04:18:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Hono is a Web application framework that provides support for any JavaScript runtime. From 3.8.0 to 4.12.33, memo() from hono/jsx retains the result of a server side render and reuses it for later renders with comparator equal props, and request scoped values read inside the component take no part in that comparison, s...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/honojs/hono/security/advisories/GHSA-f23p-vx2j-j53r

### [CVE-2026-69207](https://github.com/honojs/hono/commit/93fc250d8b4df58ea542cb945171de8013d5e6d5)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-69207
- 関連キーワード: javascript, express
- 影響製品: -
- 公開日: 2026-08-08 06:17:29 JST
- 更新日: 2026-08-08 06:17:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Hono is a Web application framework that provides support for any JavaScript runtime. Prior to 4.12.34, the built-in CORS middleware, hono/cors, is vulnerable to a regular expression denial of service (ReDoS). During a preflight OPTIONS request, the middleware parses the attacker-controlled Access-Control-Request-Heade...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/honojs/hono/commit/93fc250d8b4df58ea542cb945171de8013d5e6d5
- https://github.com/honojs/hono/releases/tag/v4.12.34
- https://github.com/honojs/hono/security/advisories/GHSA-8j4g-w8fx-2239

### [CVE-2026-71848](https://github.com/honojs/hono/commit/f70e2c31684387b3231cc38512a31df6ca76a1c7)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-71848
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-08-08 04:18:53 JST
- 更新日: 2026-08-08 04:18:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Hono is a Web application framework that provides support for any JavaScript runtime. From 4.12.0 to 4.12.33, the languageDetector middleware is vulnerable to algorithmic complexity denial of service when processing a crafted language tag containing a large number of hyphen separated subtags. To implement progressive l...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/honojs/hono/commit/f70e2c31684387b3231cc38512a31df6ca76a1c7
- https://github.com/honojs/hono/releases/tag/v4.12.34
- https://github.com/honojs/hono/security/advisories/GHSA-54fx-42gc-7vw4

### [CVE-2026-11425](https://github.com/domoticz/domoticz)

> **Frontend** / **MEDIUM** / CVSS: **4.4** / KEV: **no**

- タイトル: CVE-2026-11425
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-08 06:17:27 JST
- 更新日: 2026-08-08 06:17:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Domoticz versions prior to 2026.3 contains a stored cross-site scripting vulnerability in the mobile dashboard that allows authenticated attackers to inject arbitrary HTML and JavaScript by updating Text or Alert subtype device values through the API. The mobile dashboard renders device data via ng-bind-html with only...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/domoticz/domoticz
- https://github.com/domoticz/domoticz/commit/f734fde31a4c2ecab3edd825ceb9854719444f64
- https://www.vulncheck.com/advisories/domoticz-mobile-dashboard-versions-prior-to-stored-xss-via-text-alert-device-rendering

### [CVE-2026-71849](https://github.com/honojs/hono/commit/720b566290793d4358bf39843adcb7cf4da4548f)

> **Frontend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-71849
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-08 04:18:54 JST
- 更新日: 2026-08-08 04:18:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Hono is a Web application framework that provides support for any JavaScript runtime. From 4.7.0 to 4.12.33, the Proxy Helper proxy() function in hono/proxy does not remove response headers named by the origin's Connection header. Per RFC 9110 Section 7.6.1, an intermediary must remove the header fields listed in a mes...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/honojs/hono/commit/720b566290793d4358bf39843adcb7cf4da4548f
- https://github.com/honojs/hono/releases/tag/v4.12.34
- https://github.com/honojs/hono/security/advisories/GHSA-79qm-7rj5-m7r9

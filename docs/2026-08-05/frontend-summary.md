# Frontend CVE Summary (2026-08-05)

## Overview

- 取得日時: 2026-08-05 08:15:42 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 16
- Critical: 6
- High: 5
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-18401](https://github.com/FasterXML/jackson-core/commit/b0c428e6f993e1b5ece5c1c3cb2523e887cd52cf)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-18401
- 関連キーワード: react, gin
- 影響製品: -
- 公開日: 2026-08-05 00:16:29 JST
- 更新日: 2026-08-05 04:16:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The non-blocking (asynchronous) JSON parser in jackson-core does not enforce the maxNumberLength constraint defined in StreamReadConstraints (default: 1000 characters). An attacker able to submit JSON to an application that uses the async parser API can supply a number token of arbitrary length, leading to excessive me...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FasterXML/jackson-core/commit/b0c428e6f993e1b5ece5c1c3cb2523e887cd52cf
- https://github.com/FasterXML/jackson-core/pull/1555
- https://github.com/FasterXML/jackson-core/security/advisories/GHSA-72hv-8253-57qq
- https://github.com/FasterXML/jackson-core/security/advisories/GHSA-72hv-8253-57qq

### [CVE-2026-68494](https://github.com/FasterXML/jackson-core/commit/050b429804dce2a7e08f0be1b0b4c3d040fdb9cd)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-68494
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-08-05 00:16:41 JST
- 更新日: 2026-08-05 04:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The fix released in jackson-core 2.18.6 and 2.21.1 for CVE-2026-18401 (GHSA-72hv-8253-57qq, number length constraint bypass in the non-blocking parser) is incomplete. This record covers the remaining bypass. The earlier fix wired validateIntegerLength() into a new _setIntLength() helper and invoked it wherever the inte...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FasterXML/jackson-core/commit/050b429804dce2a7e08f0be1b0b4c3d040fdb9cd
- https://github.com/FasterXML/jackson-core/commit/4cdd529749da396cc7edf6d4a2aad41d47902641
- https://github.com/FasterXML/jackson-core/commit/c5941e5aae7fd5aeac55d66933cfb82b9aabeef8
- https://github.com/FasterXML/jackson-core/pull/1611
- https://github.com/FasterXML/jackson-core/security/advisories/GHSA-r7wm-3cxj-wff9

### [CVE-2026-69263](https://github.com/FlowiseAI/Flowise/commit/a4c4e4988cded15edf725e762560575b889ae351)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-69263
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-08-05 02:17:01 JST
- 更新日: 2026-08-05 03:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Flowise is a drag & drop user interface to build a customized large language model flow. Prior to 3.1.3, the mitigation for CVE-2025-8943 blocked -y and --yes flags on npx, but packages/components/nodes/tools/MCP/core.ts denied only PATH, LD_LIBRARY_PATH, DYLD_LIBRARY_PATH, and NODE_OPTIONS by exact environment-variabl...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FlowiseAI/Flowise/commit/a4c4e4988cded15edf725e762560575b889ae351
- https://github.com/FlowiseAI/Flowise/pull/6471
- https://github.com/FlowiseAI/Flowise/releases/tag/flowise@3.1.3
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-xc48-889x-5qmw
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-xc48-889x-5qmw

### [CVE-2026-69264](https://github.com/FlowiseAI/Flowise/commit/f4e2794f6a576b94578f2fdafbf49c2fb304626c)

> **Frontend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-69264
- 関連キーワード: javascript, python, node.js
- 影響製品: -
- 公開日: 2026-08-05 03:16:57 JST
- 更新日: 2026-08-05 04:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Prior to 3.1.3, Flowise CSVAgent interpolates an attacker-controlled segment of the csvFile data URI directly into a Python source-code template that is then executed by Pyodide. Because Pyodide is loaded with the default js bridge to globalThis, which on Node.js exposes eval and dynamic import, the attacker can break...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FlowiseAI/Flowise/commit/f4e2794f6a576b94578f2fdafbf49c2fb304626c
- https://github.com/FlowiseAI/Flowise/pull/6499
- https://github.com/FlowiseAI/Flowise/releases/tag/flowise@3.1.3
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-4j8x-x6v7-w9rq
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-4j8x-x6v7-w9rq

### [CVE-2026-69251](https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-g32j-mmxr-gfq5)

> **Frontend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-69251
- 関連キーワード: javascript, typeorm, mysql
- 影響製品: -
- 公開日: 2026-08-05 00:16:44 JST
- 更新日: 2026-08-05 01:16:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Flowise is a drag & drop user interface to build a customized large language model flow. Prior to 3.1.3, Flowise record manager and agent memory nodes allowed users to set arbitrary TypeORM DataSource options through the additionalConfig input in packages/components/nodes/recordmanager/MySQLRecordManager/MySQLrecordMan...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-g32j-mmxr-gfq5
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-g32j-mmxr-gfq5

### [CVE-2026-69253](https://github.com/FlowiseAI/Flowise/commit/3f257bdc8196082a178da7134a075824401b13b9)

> **Frontend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-69253
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-08-05 01:16:29 JST
- 更新日: 2026-08-05 01:16:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Flowise is a drag-and-drop user interface for building customized large language model (LLM) flows. Prior to version 3.1.3, several custom-tool components — AgentAsTool, ChatflowTool, and ExecuteFlow — ran code in the in-process vm2 sandbox. To build that code, they inserted a user-controlled baseURL value straight int...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FlowiseAI/Flowise/commit/3f257bdc8196082a178da7134a075824401b13b9
- https://github.com/FlowiseAI/Flowise/pull/6417
- https://github.com/FlowiseAI/Flowise/releases/tag/flowise@3.1.3
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-wg86-r78f-74mp

### [CVE-2025-29296](https://app.notion.com/p/Multiple-Command-Injection-Vulnerabilities-in-Several-H3C-Network-Devices-3b2797159f158056bfd1c3ba38e7a7b7)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2025-29296
- 関連キーワード: swc, express
- 影響製品: -
- 公開日: 2026-08-05 02:16:42 JST
- 更新日: 2026-08-05 05:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: H3C Magic BE18000 V200R007, H3C NX400 V100R015, H3C Magic NX30 Pro V100R0011, H3C Magic R3010 V100R009, H3C Magic NX15 V100R017, H3C Magic R1510 V100R016, and H3C NE36 Pro V100R002 contain multiple command injection vulnerabilities in the /api/esps request handler. The affected object interfaces and methods are esps.dh...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://app.notion.com/p/Multiple-Command-Injection-Vulnerabilities-in-Several-H3C-Network-Devices-3b2797159f158056bfd1c3ba38e7a7b7
- https://www.h3c.com
- https://app.notion.com/p/Multiple-Command-Injection-Vulnerabilities-in-Several-H3C-Network-Devices-3b2797159f158056bfd1c3ba38e7a7b7

### [CVE-2026-70470](https://github.com/FlowiseAI/Flowise/commit/f4e2794f6a576b94578f2fdafbf49c2fb304626c)

> **Frontend** / **CRITICAL** / CVSS: **9.5** / KEV: **no**

- タイトル: CVE-2026-70470
- 関連キーワード: javascript, python
- 影響製品: -
- 公開日: 2026-08-05 03:16:57 JST
- 更新日: 2026-08-05 05:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Flowise is a drag & drop user interface to build a customized large language model flow. Prior to 3.1.3, Flowise validatePythonCodeForDataFrame in packages/components/src/pythonCodeValidator.ts can be bypassed with Unicode homoglyph identifiers, allowing arbitrary Python execution inside Pyodide and full OS command exe...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FlowiseAI/Flowise/commit/f4e2794f6a576b94578f2fdafbf49c2fb304626c
- https://github.com/FlowiseAI/Flowise/pull/6499
- https://github.com/FlowiseAI/Flowise/releases/tag/flowise@3.1.3
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-52fh-8v99-63c2
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-52fh-8v99-63c2

### [CVE-2026-69254](https://github.com/FlowiseAI/Flowise/commit/3086cb7e323bb96c5a581d3232ef975b0d92183d)

> **Frontend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-69254
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-05 01:16:29 JST
- 更新日: 2026-08-05 04:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Flowise is a drag & drop user interface to build a customized large language model flow. Prior to 3.1.3, executeJavaScriptCode() accepted caller-provided nodeVMOptions and merged them over the default NodeVM security settings in packages/components/src/utils.ts. An authenticated attacker reaching packages/server/src/ro...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FlowiseAI/Flowise/commit/3086cb7e323bb96c5a581d3232ef975b0d92183d
- https://github.com/FlowiseAI/Flowise/pull/6306
- https://github.com/FlowiseAI/Flowise/releases/tag/flowise@3.1.3
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-3769-jgqc-cxm7
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-3769-jgqc-cxm7

### [CVE-2026-70479](https://github.com/open-webui/open-webui/commit/bef63a2ae915571d50d2722a635e8bfa753d7877)

> **Frontend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-70479
- 関連キーワード: javascript, playwright, gin
- 影響製品: -
- 公開日: 2026-08-05 05:16:54 JST
- 更新日: 2026-08-05 05:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. From 0.9.6 until 0.11.0, with WEB_LOADER_ENGINE=playwright, the Playwright web loader validates only the top-level page request and lets sub-resource requests pass unvalidated. A page supplied by an authenticated user can use JavaScri...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-webui/open-webui/commit/bef63a2ae915571d50d2722a635e8bfa753d7877
- https://github.com/open-webui/open-webui/pull/27526
- https://github.com/open-webui/open-webui/releases/tag/v0.11.0
- https://github.com/open-webui/open-webui/security/advisories/GHSA-w2rx-84hp-gg95

### [CVE-2026-65986](https://github.com/cvat-ai/cvat/commit/44d717ad3a9d914f1cb2593ce09efd87d0b9159e)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-65986
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-05 06:16:36 JST
- 更新日: 2026-08-05 06:16:36 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CVAT is an open source interactive video and image annotation tool for computer vision. Versions 2.5.0 through 2.66.0 contain a XSS vulnerability that can be accessed through annotation guide assets. When CVAT serves the files attached to an annotation guide, it labels them with a media type ( Content-Type ) that the a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/cvat-ai/cvat/commit/44d717ad3a9d914f1cb2593ce09efd87d0b9159e
- https://github.com/cvat-ai/cvat/security/advisories/GHSA-w6mx-95ff-72cv

### [CVE-2026-70492](https://github.com/open-webui/open-webui/commit/bc600d3f085802c45aa8f38c30e6e8c986bde6cc)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-70492
- 関連キーワード: svelte, gin
- 影響製品: -
- 公開日: 2026-08-05 06:16:38 JST
- 更新日: 2026-08-05 06:16:38 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. From 0.10.0 until 0.11.0, src/lib/components/chat/Messages/Markdown/KatexRenderer.svelte could store and render a chat message whose math block makes KaTeX fail with a stack overflow instead of a parse error. The catch branch fell bac...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-webui/open-webui/commit/bc600d3f085802c45aa8f38c30e6e8c986bde6cc
- https://github.com/open-webui/open-webui/pull/26718
- https://github.com/open-webui/open-webui/releases/tag/v0.11.0
- https://github.com/open-webui/open-webui/security/advisories/GHSA-pwxh-7358-jq2x

### [CVE-2026-10032](https://github.com/a2ui-project/a2ui/security/advisories/GHSA-72qq-p3r5-f7wq)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-10032
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-05 01:16:20 JST
- 更新日: 2026-08-05 04:16:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The openUrl function in @a2ui/web_core passes an agent-controlled URL directly to window.open() without validating the URI scheme. A malicious agent can supply a javascript: URI as the url argument of a Button component's functionCall action. When the user clicks the rendered button, arbitrary JavaScript executes in th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/a2ui-project/a2ui/security/advisories/GHSA-72qq-p3r5-f7wq

### [CVE-2026-66300](https://github.com/IHTSDO/snowstorm/commit/575b555695811110dafe2fcea7dd2fd7e4bcee39)

> **Frontend** / **MEDIUM** / CVSS: **5.0** / KEV: **no**

- タイトル: CVE-2026-66300
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-05 04:16:51 JST
- 更新日: 2026-08-05 05:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SNOMED International Snowstorm contains a reflected XSS vulnerability within the "Web Route" redirection functionality. An attacker can inject arbitrary JavaScript which will execute upon a target user navigating to a crafted, malicious link. Fixed in 10.12.2 and 10.9.3.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/IHTSDO/snowstorm/commit/575b555695811110dafe2fcea7dd2fd7e4bcee39
- https://github.com/IHTSDO/snowstorm/commit/b8061add427c930b3030549e77aa23ec5957ceb6
- https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-212-01.json
- https://www.cve.org/CVERecord?id=CVE-2026-66300

### [CVE-2026-67196](https://christbowel.com/blog/perspective-5-0-0-five-cves/)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-67196
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-05 00:16:40 JST
- 更新日: 2026-08-05 00:16:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Perspective 5.0.0 contains a cross-site scripting vulnerability in the built-in Debug plugin that allows attackers to inject arbitrary HTML and JavaScript by writing table cell values containing unescaped HTML markup, which are interpolated directly into innerHTML during CSV serialization rendering. Attackers can craft...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://christbowel.com/blog/perspective-5-0-0-five-cves/
- https://www.vulncheck.com/advisories/perspective-xss-via-debug-plugin-innerhtml-interpolation

### [CVE-2026-52370](https://github.com/RichardKabuto/CVE-2026-52370/issues/1)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-52370
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-05 07:17:15 JST
- 更新日: 2026-08-05 07:17:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A reflected cross-site scripting (XSS) vulnerability in the Forum posting function of O2OA v10 allows attackers to execute arbitrary Javascript in the context of the victim's browser via a crafted URL.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/RichardKabuto/CVE-2026-52370/issues/1
- https://www.o2oa.net/download.html

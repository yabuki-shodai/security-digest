# Frontend CVE Summary (2026-10-15)

## Overview

- 取得日時: 2026-10-15 09:28:40 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 11
- Critical: 1
- High: 3
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-101897](https://github.com/angular/angular/commit/7c053599c79a6ddd785a9bae33ff9fc7b355ea0d)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-101897
- 関連キーワード: typescript, javascript, angular, gin
- 影響製品: -
- 公開日: 2026-10-15 01:17:29 JST
- 更新日: 2026-10-15 01:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. From 1.20.0 until 1.21.1, the Angular DevTools background service worker accepts chrome.runtime.sendMessage runtime messages from untrusted web pages or third-party content scripts without...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/angular/angular/commit/7c053599c79a6ddd785a9bae33ff9fc7b355ea0d
- https://github.com/angular/angular/commit/cf492e8a372e2bbddb84987df12c33a52c23c72f
- https://github.com/angular/angular/commit/e02c4d89bcf5da9af499e0dfbba8c29206976ab3
- https://github.com/angular/angular/pull/70623
- https://github.com/angular/angular/security/advisories/GHSA-r653-wxfp-pp9c

### [CVE-2026-101895](https://github.com/angular/angular/commit/3db26e2544964d07a520836ad01f02f36ec88e25)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-101895
- 関連キーワード: typescript, javascript, angular, node.js
- 影響製品: -
- 公開日: 2026-10-15 00:17:03 JST
- 更新日: 2026-10-15 03:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 20.3.31, 21.2.23, and 22.1.6, the @angular/platform-server DOM emulation parser can enter an infinite synchronous loop when Angular server-side rendering processes attacker-contro...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/angular/angular/commit/3db26e2544964d07a520836ad01f02f36ec88e25
- https://github.com/angular/angular/commit/fc2e8fbc0bda2f5c11585e8a0cbd88c074f5e567
- https://github.com/angular/angular/releases/tag/v20.3.31
- https://github.com/angular/angular/releases/tag/v21.2.23
- https://github.com/angular/angular/releases/tag/v22.1.6

### [CVE-2026-101896](https://github.com/angular/angular/commit/03872a80bcf1c89b2b04cdd3f444b2ee954da583)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-101896
- 関連キーワード: typescript, javascript, angular, node.js
- 影響製品: -
- 公開日: 2026-10-15 01:17:29 JST
- 更新日: 2026-10-15 01:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 20.3.32, 21.2.24, and 22.2.0, the @angular/router URL parser stores numeric matrix parameter names and numeric outlet names as properties on initially empty JavaScript objects dur...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/angular/angular/commit/03872a80bcf1c89b2b04cdd3f444b2ee954da583
- https://github.com/angular/angular/commit/5af61216eab8bf4a6697a1d79bda3d857c06f89d
- https://github.com/angular/angular/commit/ddfe21072ba32ca4cd9d7d3c6b7df66af81d58c4
- https://github.com/angular/angular/issues/70716
- https://github.com/angular/angular/pull/70717

### [CVE-2020-37281](https://github.com/gravitee-io/gravitee-api-management/blob/4.12.22/gravitee-apim-rest-api/gravitee-apim-rest-api-management/gravitee-apim-rest-api-management-security/src/main/java/io/gravitee/rest/api/management/security/config/BasicSecurityConfigurerAdapter.java#L157-L175)

> **Frontend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2020-37281
- 関連キーワード: vite, gin
- 影響製品: -
- 公開日: 2026-10-15 00:16:59 JST
- 更新日: 2026-10-15 02:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Gravitee API Management through 4.12.22 contains an authentication bypass vulnerability that allows unauthenticated remote attackers to impersonate any user by forging JWTs signed with the shipped default jwt.secret. Attackers knowing an existing user ID can sign an HS256 token with that subject and present it as a bea...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gravitee-io/gravitee-api-management/blob/4.12.22/gravitee-apim-rest-api/gravitee-apim-rest-api-management/gravitee-apim-rest-api-management-security/src/main/java/io/gravitee/rest/api/management/security/config/BasicSecurityConfigurerAdapter.java#L157-L175
- https://github.com/gravitee-io/gravitee-api-management/blob/4.12.22/gravitee-apim-rest-api/gravitee-apim-rest-api-standalone/gravitee-apim-rest-api-standalone-distribution/src/main/resources/config/gravitee.yml#L636-L637
- https://github.com/gravitee-io/gravitee-api-management/blob/4.12.22/helm/values.yaml#L103
- https://github.com/gravitee-io/gravitee-docs/blob/master/pages/apim/3.x/how-tos/how-to-general-configuration.adoc
- https://github.com/gravitee-io/issues/issues/4204

### [CVE-2026-110658](https://github.com/freeswitch/sofia-sip)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-110658
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-10-15 01:17:42 JST
- 更新日: 2026-10-15 05:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Sofia-SIP through 1.13.18 contains a heap out-of-bounds read vulnerability in msg_multipart_parse() that allows unauthenticated remote attackers to crash the process by sending oversized MIME boundaries. Attackers can send an INVITE with a multipart Content-Type whose boundary exceeds the body length, causing memcmp to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/freeswitch/sofia-sip
- https://github.com/freeswitch/sofia-sip/blob/ad36ac8f755308e8b87f98a505e83d4e408e5cc3/libsofia-sip-ua/msg/msg_mime.c#L404
- https://hackmd.io/@haind-pwn/sofia-sip-multipart-oob-read
- https://www.vulncheck.com/advisories/sofia-sip-through-1.13.18-heap-out-of-bounds-read-via-msg-multipart-parse

### [CVE-2026-101019](https://my.f5.com/manage/s/article/K000162615)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-101019
- 関連キーワード: javascript, gin, nginx
- 影響製品: -
- 公開日: 2026-10-15 00:17:01 JST
- 更新日: 2026-10-15 01:04:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Description NGINX JavaScript (njs) has a vulnerability where the njs XML module exposes entity-backed XML attributes inconsistently with libxml2 canonicalization. In both the built-in njs and QuickJS backends during the canonicalization process, the $attr$Name getter may return undefined for an explicitly present attri...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://my.f5.com/manage/s/article/K000162615

### [CVE-2026-110610](https://github.com/YunaiV/ruoyi-vue-pro/blob/1697112f1164b206aeb031493980f5cb3a6e2cd5/yudao-module-ai/src/main/java/cn/iocoder/yudao/module/ai/controller/admin/image/AiImageController.java#L97-L102)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-110610
- 関連キーワード: vue, gin
- 影響製品: -
- 公開日: 2026-10-15 00:17:12 JST
- 更新日: 2026-10-15 00:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ruoyi-vue-pro through 2026.09 contains a server-side request forgery vulnerability in the yudao-module-ai image service that allows authenticated users to make the server fetch arbitrary URLs by supplying referImageUrl to the midjourney imagine endpoint. Attackers can force Hutool HttpUtil.downloadBytes() requests to l...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/YunaiV/ruoyi-vue-pro/blob/1697112f1164b206aeb031493980f5cb3a6e2cd5/yudao-module-ai/src/main/java/cn/iocoder/yudao/module/ai/controller/admin/image/AiImageController.java#L97-L102
- https://github.com/YunaiV/ruoyi-vue-pro/blob/1697112f1164b206aeb031493980f5cb3a6e2cd5/yudao-module-ai/src/main/java/cn/iocoder/yudao/module/ai/service/image/AiImageServiceImpl.java#L231
- https://hackmd.io/@1ExmmukzRMWN7B4gQ4W-4Q/yudao-ai-image-midjourney-ssrf
- https://www.vulncheck.com/advisories/ruoyi-vue-pro-through-2026.09-ssrf-via-midjourney-referimageurl-and-notify-imageurl

### [CVE-2026-101025](https://my.f5.com/manage/s/article/K000162614)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-101025
- 関連キーワード: javascript, gin, nginx
- 影響製品: -
- 公開日: 2026-10-15 00:17:01 JST
- 更新日: 2026-10-15 01:04:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Description NGINX JavaScript (njs) has a vulnerability where the built-in njs engine leaks a libxml2 parser context when xml.parse() fails. The failure path did not register cleanup and the context was not released for the lifetime of the process. An unauthenticated attacker may send requests with malformed XML and can...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://my.f5.com/manage/s/article/K000162614

### [CVE-2026-110261](https://asm.ow2.io/versions.html)

> **Frontend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-110261
- 関連キーワード: swr, go
- 影響製品: -
- 公開日: 2026-10-15 00:17:07 JST
- 更新日: 2026-10-15 03:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OW2 ASM 3.0 before 9.11 contains a denial of service vulnerability that allows attackers to exhaust CPU by supplying crafted class files processed with ClassWriter.COMPUTE_FRAMES. Attackers can craft methods that make the unbounded MethodWriter.computeAllFrames() fix point algorithm converge slowly, tying up transformi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://asm.ow2.io/versions.html
- https://gitlab.ow2.org/asm/asm/-/blob/ASM_9_10_1/asm/src/main/java/org/objectweb/asm/MethodWriter.java#L1595
- https://gitlab.ow2.org/asm/asm/-/commit/ab68bbd2521359b7c8cd3517c6331ced3d817ed0
- https://gitlab.ow2.org/asm/asm/-/merge_requests/463
- https://www.vulncheck.com/advisories/ow2-asm-3.0-before-9.11-excessive-cpu-consumption-via-classwriter-compute-frames

### [CVE-2026-110259](https://asm.ow2.io/versions.html)

> **Frontend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-110259
- 関連キーワード: swr
- 影響製品: -
- 公開日: 2026-10-15 00:17:07 JST
- 更新日: 2026-10-15 01:14:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OW2 ASM 3.0 before 9.11 contains an uncontrolled recursion vulnerability in ClassWriter.replaceAsmInstructions() that allows attackers to cause denial of service through crafted class files. Attackers can supply a class with a large method containing many long forward jumps, triggering unbounded toByteArray() recursion...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://asm.ow2.io/versions.html
- https://gitlab.ow2.org/asm/asm/-/blob/ASM_9_10_1/asm/src/main/java/org/objectweb/asm/ClassWriter.java#L751
- https://gitlab.ow2.org/asm/asm/-/commit/e9aca627c17e1619bcb8059afb43382dac6b275f
- https://gitlab.ow2.org/asm/asm/-/merge_requests/459
- https://www.vulncheck.com/advisories/ow2-asm-3.0-before-9.11-uncontrolled-recursion-via-classwriter-replaceasminstructions

### [CVE-2026-110715](https://codeberg.org/ccxvii/mujs)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-110715
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-15 01:17:43 JST
- 更新日: 2026-10-15 01:17:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MuJS 1.3.6 before 1.3.9 contains a heap out-of-bounds read and write vulnerability in Array.prototype.sort that allows attackers to corrupt memory by inflating a simple array's length. Attackers can supply JavaScript that enlarges a dense array's length and calls sort, causing Ap_sort_cmp and Ap_sort_swap to access slo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://codeberg.org/ccxvii/mujs
- https://codeberg.org/ccxvii/mujs/commit/32064e10caa45e68fc87331ca53d042049cc9396
- https://codeberg.org/ccxvii/mujs/src/commit/307f18c4216420f2f56e22d8e7040baa39a6304a/jsarray.c#L245
- https://hackmd.io/@haind-pwn/mujs-array-length-flat-oob
- https://mujs.com/downloads/

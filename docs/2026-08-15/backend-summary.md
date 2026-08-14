# Backend CVE Summary (2026-08-15)

## Overview

- 取得日時: 2026-08-15 07:35:40 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 21
- Critical: 3
- High: 7
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-49989](https://github.com/crate/crate/security/advisories/GHSA-2xv8-gjwh-fv8p)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-49989
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-15 02:18:27 JST
- 更新日: 2026-08-15 03:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CrateDB is a distributed SQL database. Prior to versions 6.2.8 and 6.3.2, any authenticated user can read or delete any blob whose SHA-1 digest they know, and can plant new blobs unconditionally, in any blob table, regardless of `GRANT`s. CrateDB has two ways to access blob storage: SQL (`SELECT ... FROM blob.<table>`...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/crate/crate/security/advisories/GHSA-2xv8-gjwh-fv8p
- https://github.com/crate/crate/security/advisories/GHSA-2xv8-gjwh-fv8p

### [CVE-2026-46603](https://go.dev/cl/793460)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-46603
- 関連キーワード: go, golang
- 影響製品: -
- 公開日: 2026-08-15 02:18:15 JST
- 更新日: 2026-08-15 05:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: VP8L decoding in golang.org/x/image/vp8l can allocate an excessive amount of memory when processing a crafted VP8L image containing many unused Huffman tree groups. This allows a remote attacker to cause a denial of service via memory exhaustion.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://go.dev/cl/793460
- https://go.dev/issue/80069
- https://pkg.go.dev/vuln/GO-2026-6222

### [CVE-2026-73845](https://github.com/ondata/ckan-mcp-server/commit/8e1522f9bbfa1f3b21550f17887f60f133e24151)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-73845
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-08-15 02:20:36 JST
- 更新日: 2026-08-15 03:19:09 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CKAN MCP Server is a tool for querying CKAN open data portals. Prior to 0.4.112, the ckan_get_mqa_quality and ckan_get_mqa_quality_details tools in src/tools/quality.ts use isValidMqaServer to validate the server_url parameter with a prefix-only regular expression for dati.gov.it, allowing suffix-host and URL-userinfo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/ondata/ckan-mcp-server/commit/8e1522f9bbfa1f3b21550f17887f60f133e24151
- https://github.com/ondata/ckan-mcp-server/releases/tag/v0.4.112
- https://github.com/ondata/ckan-mcp-server/security/advisories/GHSA-83x6-42hr-jc76

### [CVE-2026-27871](https://www.johnsoncontrols.com/trust-center/cybersecurity/security-advisories)

> **Backend** / **LOW** / CVSS: **2.9** / KEV: **no**

- タイトル: CVE-2026-27871
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-15 05:16:52 JST
- 更新日: 2026-08-15 05:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Cwe-327 Use of a Broken or Risky Cryptographic Algorithm vulnerability in Johnson Controls TL280 allows Cryptanalytic Attack. This issue affects TL280: before 5.63.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.johnsoncontrols.com/trust-center/cybersecurity/security-advisories

### [CVE-2026-49826](https://github.com/concourse/concourse/commit/ac60be5f0435b6592f5a4fcc089050d72ad2452c)

> **Backend** / **NONE** / CVSS: **0.0** / KEV: **no**

- タイトル: CVE-2026-49826
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-15 02:18:27 JST
- 更新日: 2026-08-15 03:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Concourse is a container-based automation system written in Go. Prior to version 8.2.3, an attacker is able to craft and send a user a URL that will redirect the user from the Concourse web server to any other site. This could be used in a phishing attack to steal user's credentials. This has been fixed in 8.2.3. No kn...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/concourse/concourse/commit/ac60be5f0435b6592f5a4fcc089050d72ad2452c
- https://github.com/concourse/concourse/releases/tag/v8.2.3
- https://github.com/concourse/concourse/security/advisories/GHSA-8w27-c4vc-88q9

### [CVE-2026-73678](https://github.com/mindsdb/minds-platform)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-73678
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-15 04:18:01 JST
- 更新日: 2026-08-15 04:18:01 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: MindsDB Minds Platform version 26.1.0 and earlier contains an unauthenticated remote code execution vulnerability that allows unauthenticated attackers to execute arbitrary OS commands by submitting crafted prompts to the unprotected POST /api/v1/responses/ endpoint, which reaches the Anton agent's scratchpad tool that...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mindsdb/minds-platform
- https://github.com/mindsdb/minds-platform/security/advisories/GHSA-jcxw-h8ph-pxpv
- https://www.vulncheck.com/advisories/mindsdb-minds-platform-unauthenticated-rce-via-scratchpad-exec

### [CVE-2026-48528](https://github.com/NCEAS/metacat/security/advisories/GHSA-6g6j-wh5h-77h5)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-48528
- 関連キーワード: gin, postgresql
- 影響製品: -
- 公開日: 2026-08-15 03:17:27 JST
- 更新日: 2026-08-15 03:17:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Metacat is data repository software that helps researchers preserve, share, and discover data. Metacat versions 2.0.0 through 3.4.0 contain an unauthenticated SQL injection vulnerability in the `/cn/v1/object` and `/cn/v2/object` REST API endpoints due to unsanitized user input that can be passed through to the backend...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/NCEAS/metacat/security/advisories/GHSA-6g6j-wh5h-77h5

### [CVE-2026-50027](https://github.com/advisories/GHSA-84hp-mqvj-3p8h)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-50027
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 04:17:18 JST
- 更新日: 2026-08-15 04:17:18 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: mcp-memory-service is a semantic memory layer for AI applications. Prior to 10.67.1, all HTTP routes under /api/documents/* in mcp-memory-service are served without any authentication dependency, even when the server is configured with an API key (MCP_API_KEY) or OAuth. An unauthenticated remote attacker can upload arb...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/advisories/GHSA-84hp-mqvj-3p8h
- https://pypi.org/project/mcp-memory-service
- https://web.archive.org/web/20260508112116/https://github.com/doobidoo/mcp-memory-service

### [CVE-2026-12364](https://github.com/zephyrproject-rtos/zephyr/commit/77aa26d8b940f39778154f02563caf15d02efdac)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-12364
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 03:17:21 JST
- 更新日: 2026-08-15 05:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The user-space system-call verifier z_vrfy_z_log_msg_static_create() in subsys/logging/log_msg.c was a pure pass-through: it forwarded the caller-supplied source, desc, package, and data arguments directly to the kernel-mode implementation z_impl_z_log_msg_static_create() without performing any of the mandatory K_SYSCA...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/77aa26d8b940f39778154f02563caf15d02efdac
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-h7rf-g9mg-g23f

### [CVE-2026-19629](https://www.tenable.com/security/tns-2026-22)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-19629
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 03:17:22 JST
- 更新日: 2026-08-15 04:17:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A privilege escalation vulnerability exists in Tenable Security Center that allows a user with "Security Manager" role and "manage user" permission on a single group to modify users belonging to other groups. This bypasses the intended access control restrictions and enables unauthorized cross-group user management.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.tenable.com/security/tns-2026-22

### [CVE-2026-19884](https://github.com/eclipse-theia/theia/pull/16809)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-19884
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 01:16:55 JST
- 更新日: 2026-08-15 05:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: In Eclipse Theia versions up to and including 1.69.0, opening a folder starts source control integration without requiring the user to trust the folder first. This affects applications built on Theia that include the git integration, such as the Theia IDE. Both Theia's own `@theia/git` extension and the builtin VS Code...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/eclipse-theia/theia/pull/16809
- https://github.com/eclipse-theia/theia/pull/17098
- https://github.com/eclipse-theia/theia/pull/17148
- https://gitlab.eclipse.org/security/cve-assignment/-/work_items/231
- https://gitlab.eclipse.org/security/vulnerability-reports/-/work_items/175

### [CVE-2026-73847](https://github.com/emlog/emlog/security/advisories/GHSA-v6wr-4x55-7qp5)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-73847
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 03:19:09 JST
- 更新日: 2026-08-15 05:16:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Emlog is an open source website building system. In 2.6.26 and earlier, missing CSRF protection on the AI Assistant execute_tool action in admin/ai.php lets a remote unauthenticated attacker submit a forged cross-site request from an attacker-controlled page to a recently logged-in administrator. The authentication coo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/emlog/emlog/security/advisories/GHSA-v6wr-4x55-7qp5
- https://github.com/emlog/emlog/security/advisories/GHSA-v6wr-4x55-7qp5

### [CVE-2026-46439](https://github.com/oscal-compass/compliance-trestle/commit/247fcce289f60103f3d8e28d8ec51a6986b94fb6)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-46439
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 02:18:14 JST
- 更新日: 2026-08-15 02:18:14 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: compliance-trestle is a tooling platform for managing compliance as code. Versions prior to 3.12.2 and 4.0.3 have a Server-Side Template Injection (SSTI) vulnerability exists in the `trestle author jinja` command. The command recursively evaluates rendered templates, allowing an attacker to achieve arbitrary command ex...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/oscal-compass/compliance-trestle/commit/247fcce289f60103f3d8e28d8ec51a6986b94fb6
- https://github.com/oscal-compass/compliance-trestle/commit/7d107b3ac53caca7bde97a6278b23cd739d94525
- https://github.com/oscal-compass/compliance-trestle/security/advisories/GHSA-gg2g-p7xc-qqmm
- https://github.com/pypa/advisory-database/tree/main/vulns/compliance-trestle/PYSEC-2026-2425.yaml
- https://github.com/oscal-compass/compliance-trestle/security/advisories/GHSA-gg2g-p7xc-qqmm

### [CVE-2026-69414](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-69414
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 07:17:06 JST
- 更新日: 2026-08-15 07:17:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Microsoft is aware of an elevation of privilege in the Microsoft Malware Protection Engine in Microsoft Defender publicly referred to as &quot;ShieldBreak &quot;. We are working to provide a high quality security update that addresses this vulnerability. We will provide information in this CVE when the update is availa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414

### [CVE-2026-57469](https://www.nozominetworks.com/labs/vulnerability-advisories-cve-2026-57469)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-57469
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 01:16:58 JST
- 更新日: 2026-08-15 05:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nozomi Networks Labs identified a CWE-352: Cross-Site Request Forgery (CSRF) vulnerability in the web-based configuration backend of KUNBUS PiCtory in version 2.16.0 that allows a remote unauthenticated attacker to perform state-changing operations in the context of an authenticated operator, including deletion of proj...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.nozominetworks.com/labs/vulnerability-advisories-cve-2026-57469

### [CVE-2026-67366](https://www.icagenda.com/)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-67366
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 06:17:51 JST
- 更新日: 2026-08-15 06:17:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Joomla Extension - icagenda.com - CSRF on frontend registration actions in iCagenda < 2.0.0-4.0.11 - Multiple state changing operations in the frontend are callable without a CSRF token check.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.icagenda.com/

### [CVE-2026-47192](https://github.com/pypa/advisory-database/tree/main/vulns/kas/PYSEC-2026-2543.yaml)

> **Backend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-47192
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 02:18:15 JST
- 更新日: 2026-08-15 05:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: kas is a setup tool for bitbake based projects. Starting in version 4.8 and prior to version 5.3, kas checks out and processes repositories regarding configuration includes prior to validating signatures of those repositories. This may allow to replace on original repository with one under the control of an attacker un...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pypa/advisory-database/tree/main/vulns/kas/PYSEC-2026-2543.yaml
- https://github.com/siemens/kas/commit/4cb4a3d01122ffaec9feaae768a5814092f6f9b5
- https://github.com/siemens/kas/commit/5b2114becfc154b16ef496d24f8c2191a2297f57
- https://github.com/siemens/kas/security/advisories/GHSA-4vqc-wpwg-vh7j
- https://github.com/siemens/kas/security/advisories/GHSA-qjwp-hrq6-r26r

### [CVE-2026-12363](https://github.com/zephyrproject-rtos/zephyr/commit/452c704a28369236e555543c61a1894cd1a4afbb)

> **Backend** / **MEDIUM** / CVSS: **4.2** / KEV: **no**

- タイトル: CVE-2026-12363
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 03:17:21 JST
- 更新日: 2026-08-15 05:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The LoRaWAN Fragmented Data Block Transport service (subsys/lorawan/services/frag_transport.c) does not validate the fragment counter in a received DATA_FRAGMENT command before forwarding it to the configured decoder. In frag_transport_package_callback() the value frag_counter = hdr->frag_index_n & 0x3FFF is taken dire...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/452c704a28369236e555543c61a1894cd1a4afbb
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-fvm7-7whg-8gj6

### [CVE-2026-19834](https://github.com/Mitchell45/PHP_Web_POCs/blob/main/Bagisto/01_english_vulnerability_report.md)

> **Backend** / **MEDIUM** / CVSS: **5.8** / KEV: **no**

- タイトル: CVE-2026-19834
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 01:16:54 JST
- 更新日: 2026-08-15 04:09:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability was determined in Webkul Bagisto up to 2.4.4. Affected is an unknown function of the file /admin/customers/login-as-customer/ of the component Admin Customer Impersonation Feature. This manipulation of the argument ID causes authorization bypass. The attack can be initiated remotely. The exploit has bee...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Mitchell45/PHP_Web_POCs/blob/main/Bagisto/01_english_vulnerability_report.md
- https://vuldb.com/cve/CVE-2026-19834
- https://vuldb.com/submit/870342
- https://vuldb.com/vuln/389972
- https://vuldb.com/vuln/389972/cti

### [CVE-2026-46380](https://github.com/oscal-compass/compliance-trestle/commit/53de5e75332888ea54f5da41d4c7859bb1d608e1)

> **Backend** / **MEDIUM** / CVSS: **6.7** / KEV: **no**

- タイトル: CVE-2026-46380
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 02:18:14 JST
- 更新日: 2026-08-15 02:18:14 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: compliance-trestle is a tooling platform for managing compliance as code. Prior to versions 3.12.2 and 4.0.3, the HTTPSFetcher._do_fetch() method passes a user-supplied URL directly to requests.get() without validation. This allows an attacker to perform Server-Side Request Forgery, targeting internal services or cloud...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/oscal-compass/compliance-trestle/commit/53de5e75332888ea54f5da41d4c7859bb1d608e1
- https://github.com/oscal-compass/compliance-trestle/commit/5c65c5926fe7ca908b9c1d281f904e7d97ba8310
- https://github.com/oscal-compass/compliance-trestle/security/advisories/GHSA-w76h-q7c6-jpjp
- https://github.com/pypa/advisory-database/tree/main/vulns/compliance-trestle/PYSEC-2026-2427.yaml

### [CVE-2026-47191](https://github.com/pypa/advisory-database/tree/main/vulns/kas/PYSEC-2026-2544.yaml)

> **Backend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-47191
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-15 02:18:15 JST
- 更新日: 2026-08-15 02:18:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: kas is a setup tool for bitbake based projects. Prior to version 5.3, when relying solely on a git commit ID (SHA-1 or SHA-256) to qualify if a checkout of a repository is equivalent to the state validated while adding its commit ID to a kas configuration, users may be tricked to check out a branch of the same name fro...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pypa/advisory-database/tree/main/vulns/kas/PYSEC-2026-2544.yaml
- https://github.com/siemens/kas/commit/4cb4a3d01122ffaec9feaae768a5814092f6f9b5
- https://github.com/siemens/kas/security/advisories/GHSA-qjwp-hrq6-r26r

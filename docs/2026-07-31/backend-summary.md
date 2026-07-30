# Backend CVE Summary (2026-07-31)

## Overview

- 取得日時: 2026-07-31 08:16:03 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 23
- Critical: 5
- High: 8
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-55768](https://github.com/allinurl/goaccess/commit/ea74b87254d0adc675c087ff49bddd2d60dc01d5)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-55768
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-31 06:17:57 JST
- 更新日: 2026-07-31 06:17:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: GoAccess is a real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems or through the browser. Prior to version 1.11, the built-in WebSocket server narrows a 64-bit extended frame length into the signed 32-bit WSFrame.payloadlen field before enforcing the maximum frame size, allowing an...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/allinurl/goaccess/commit/ea74b87254d0adc675c087ff49bddd2d60dc01d5
- https://github.com/allinurl/goaccess/security/advisories/GHSA-5gm5-pvh2-wg46

### [CVE-2026-54715](https://github.com/allinurl/goaccess/commit/81f90d9dafd6956c188dea9f944d24946d3d3351)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-54715
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-31 06:17:49 JST
- 更新日: 2026-07-31 06:17:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: GoAccess is a real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems or through the browser. In version 1.10.2, parse_browser assumes the matched browser token begins with Opera and moves a trailing version substring to match plus five, allowing a crafted User-Agent in a processed acc...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/allinurl/goaccess/commit/81f90d9dafd6956c188dea9f944d24946d3d3351
- https://github.com/allinurl/goaccess/security/advisories/GHSA-qcx5-vh2x-35fr

### [CVE-2026-67550](https://github.com/uhop/node-re2/commit/56293de4fc0914d7bc35f92e98de25b0d9bb417d)

> **Backend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-67550
- 関連キーワード: go, gin, node.js, express
- 影響製品: -
- 公開日: 2026-07-31 05:18:15 JST
- 更新日: 2026-07-31 05:18:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: re2 provides Node.js bindings for Google's RE2 regular expression engine. Prior to 1.25.2, re2 validates lastIndex against the UTF-8 byte length of a subject but uses it as a UTF-16 code-unit offset in exec, test, match, replace, and split, allowing an attacker-influenced lastIndex on a non-ASCII subject to trigger an...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/uhop/node-re2/commit/56293de4fc0914d7bc35f92e98de25b0d9bb417d
- https://github.com/uhop/node-re2/releases/tag/1.25.2
- https://github.com/uhop/node-re2/security/advisories/GHSA-ff84-5f28-78qj

### [CVE-2026-68499](https://github.com/uhop/node-re2/commit/56293de4fc0914d7bc35f92e98de25b0d9bb417d)

> **Backend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-68499
- 関連キーワード: go, gin, node.js, express
- 影響製品: -
- 公開日: 2026-07-31 06:18:12 JST
- 更新日: 2026-07-31 06:18:12 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: re2 provides Node.js bindings for Google's RE2 regular expression engine. Prior to 1.25.2, re2's String.prototype.match implementation with a global RE2 pattern that can match the empty string fails to advance its native matching cursor in lib/match.cc, causing an infinite loop and unbounded native memory growth that b...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/uhop/node-re2/commit/56293de4fc0914d7bc35f92e98de25b0d9bb417d
- https://github.com/uhop/node-re2/releases/tag/1.25.2
- https://github.com/uhop/node-re2/security/advisories/GHSA-6hxr-mr5r-9836

### [CVE-2026-65835](https://github.com/projectcapsule/capsule/releases/tag/v0.13.8)

> **Backend** / **MEDIUM** / CVSS: **6.6** / KEV: **no**

- タイトル: CVE-2026-65835
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-07-31 05:18:13 JST
- 更新日: 2026-07-31 05:30:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Capsule is a multi-tenancy and policy-based framework for Kubernetes. From 0.13.0 until 0.13.8, after the incomplete CVE-2026-22872 fix, TenantResource RawItems and Generators in internal/controllers/resources/collect.go, including handleRawItem and handleGeneratorItem, did not apply the ResourceReference.LoadResources...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/projectcapsule/capsule/releases/tag/v0.13.8
- https://github.com/projectcapsule/capsule/security/advisories/GHSA-jr6p-8pjj-mfx6

### [CVE-2026-55777](https://github.com/allinurl/goaccess/commit/ba813ed97d998dbdcb8d87e178799a4bb2da9e81)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-55777
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-31 06:17:57 JST
- 更新日: 2026-07-31 06:17:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: GoAccess is a real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems or through the browser. Prior to 1.11, the parse_ios() function uses an attacker-controlled keyword-to-OS offset as both the source offset and copy length for memmove, allowing a crafted User-Agent in a processed acc...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/allinurl/goaccess/commit/ba813ed97d998dbdcb8d87e178799a4bb2da9e81
- https://github.com/allinurl/goaccess/security/advisories/GHSA-5phr-qpgf-hgrg

### [CVE-2026-59881](http://github.com/aio-libs/aiohttp/releases/tag/v3.14.2)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-59881
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-07-31 04:18:33 JST
- 更新日: 2026-07-31 05:03:32 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.2, the WebSocket client accepts and decompresses frames with the RSV1 bit set even when the permessage-deflate extension was not negotiated, allowing a malicious server to cause unexpected CPU and memory consumption. This issu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- http://github.com/aio-libs/aiohttp/releases/tag/v3.14.2
- https://github.com/aio-libs/aiohttp/commit/47fb6ae354d4fa22048f4dbe7dbf82b625f0a2f6
- https://github.com/aio-libs/aiohttp/pull/12978
- https://github.com/aio-libs/aiohttp/security/advisories/GHSA-mq44-7p77-q5h7

### [CVE-2026-65834](https://github.com/projectcapsule/capsule/releases/tag/v0.13.8)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-65834
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-07-31 05:18:13 JST
- 更新日: 2026-07-31 05:30:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Capsule is a multi-tenancy and policy-based framework for Kubernetes. Prior to 0.13.8, CapsuleConfiguration.Spec.NodeMetadata.ForbiddenLabels.Regex and CapsuleConfiguration.Spec.NodeMetadata.ForbiddenAnnotations.Regex were not validated by the configuration admission webhook, allowing a Cluster Admin to store a malform...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/projectcapsule/capsule/releases/tag/v0.13.8
- https://github.com/projectcapsule/capsule/security/advisories/GHSA-68cj-mvg9-rgm2

### [CVE-2026-41186](https://github.com/projectcalico/calico/pull/12491)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-41186
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-31 00:16:31 JST
- 更新日: 2026-07-31 02:16:31 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: When Calico's shared debug server is enabled (disabled by default), the Calico kube-controllers and Goldmane components bind their Go pprof debug listener to 0.0.0.0 without authentication. Any pod with network reachability to the listener can retrieve the process heap, goroutine stacks (including function arguments),...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/projectcalico/calico/pull/12491
- https://github.com/projectcalico/calico/pull/12633
- https://github.com/projectcalico/calico/pull/12634
- https://www.tigera.io/security-bulletins/tta-2026-004/

### [CVE-2026-13435](https://www.ibm.com/support/pages/node/7279987)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-13435
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-31 04:17:06 JST
- 更新日: 2026-07-31 04:31:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: IBM Langflow OSS 1.0.0 through 1.10.1 contains an improper input validation vulnerability in the PythonREPL sandbox implementation.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7279987

### [CVE-2026-62663](https://github.com/masci/banks/security/advisories/GHSA-98rr-gvc9-3cjh)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-62663
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-31 02:16:33 JST
- 更新日: 2026-07-31 04:26:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Banks generates meaningful LLM prompts using a simple template language. In versions prior to 2.4.4, all four media filters (image, audio, video, document) in banks accept untrusted user input as file paths via Path(value) and pass them directly to open(file_path, "rb") without any path sanitization, canonicalization,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/masci/banks/security/advisories/GHSA-98rr-gvc9-3cjh
- https://github.com/masci/banks/security/advisories/GHSA-98rr-gvc9-3cjh

### [CVE-2026-61536](https://github.com/masci/banks/security/advisories/GHSA-64vx-6h2c-rjh7)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-61536
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-31 04:18:34 JST
- 更新日: 2026-07-31 04:26:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Banks generates meaningful LLM prompts using a simple template language. In versions prior to 2.4.3, banks parses Tool JSON objects from the rendered body of {% completion %} blocks and later resolves their import_path field through importlib.import_module(...) + getattr(...) to obtain the callable that handles a tool...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/masci/banks/security/advisories/GHSA-64vx-6h2c-rjh7

### [CVE-2026-67208](https://github.com/somta/Juggle/issues/86)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-67208
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-07-31 05:18:14 JST
- 更新日: 2026-07-31 05:27:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Juggle through 1.6.0 contains a remote code execution vulnerability that allows unauthenticated remote attackers to execute arbitrary OS commands by connecting to the exposed H2 database web console using default shipped credentials. Attackers can access the unprotected /h2-console endpoint, authenticate with default c...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/somta/Juggle/issues/86
- https://www.vulncheck.com/advisories/juggle-unauthenticated-rce-via-exposed-h2-console
- https://github.com/somta/Juggle/issues/86

### [CVE-2026-58222](https://access.redhat.com/security/cve/CVE-2026-58222)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-58222
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-07-31 01:17:14 JST
- 更新日: 2026-07-31 02:16:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A security flaw combining LDAP filter injection and improper authorization checks was found in Samba Active Directory Domain Controller (AD DC). When processing LDAP Compare requests, Samba fails to properly validate user-supplied attribute names and executes the resulting internal database search in a trusted context,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-58222
- https://bugzilla.redhat.com/show_bug.cgi?id=2502722
- https://bugzilla.samba.org/show_bug.cgi?id=16148
- https://www.samba.org/samba/security/CVE-2026-58222.html

### [CVE-2026-18140](https://aws.amazon.com/security/security-bulletins/2026-067-aws/)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-18140
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-07-31 04:17:26 JST
- 更新日: 2026-07-31 05:17:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Uncontrolled recursion in the unknown-key skip path of the aws-smithy-json runtime crate before 0.62.7, which the smithy-rs code generator invokes from every generated struct deserializer, might allow remote unauthenticated users to cause a denial of service (process abort via stack exhaustion) via a single small HTTP...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-067-aws/
- https://crates.io/crates/aws-smithy-json/0.62.7
- https://github.com/smithy-lang/smithy-rs/security/advisories/GHSA-8ffr-xgwf-xj56

### [CVE-2026-62845](https://github.com/clastix/kamaji/commit/6a9f3e10ae408e7948e2aca2db694791a299e79c)

> **Backend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-62845
- 関連キーワード: postgresql, mysql, kubernetes
- 影響製品: -
- 公開日: 2026-07-31 07:16:55 JST
- 更新日: 2026-07-31 07:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Kamaji is the Hosted Control Plane Manager for Kubernetes. Prior to 26.7.4-edge, the PostgreSQL and MySQL datastore drivers build DDL statements by interpolating the user-supplied DataStoreUsername/DataStoreSchema directly into SQL via fmt.Sprintf, without escaping identifiers. These fields have no format validation, s...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/clastix/kamaji/commit/6a9f3e10ae408e7948e2aca2db694791a299e79c
- https://github.com/clastix/kamaji/releases/tag/26.7.4-edge
- https://github.com/clastix/kamaji/security/advisories/GHSA-r47v-ppwp-fh4r

### [CVE-2026-68563](https://access.redhat.com/security/cve/CVE-2026-68563)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-68563
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-07-31 07:16:56 JST
- 更新日: 2026-07-31 07:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A flaw was found in ansible-collection-redhat-leapp. When a remediation task is executed with elevated privileges and the `leapp_old_postgresql_data` option is selected, a PostgreSQL data backup archive is created with insecure permissions. This allows a local non-root user on the managed node to read sensitive archive...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-68563
- https://bugzilla.redhat.com/show_bug.cgi?id=2465419

### [CVE-2025-65336](https://github.com/um-dsp/TaintRadar/blob/main/sql_injection_cves/ecommercefruitsbazarmaster/20250811-ecommerce-project-with-php-and-mysqli-fruits-bazar-show_price_by_pdtid.php-pid-sqli/20250811-ecommerce-project-with-php-and-mysqli-fruits-bazar-show_price_by_pdtid.php-pid-sqli.md)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2025-65336
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-07-31 06:16:50 JST
- 更新日: 2026-07-31 06:27:30 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Ecommerce-project-with-php-and-mysqli-Fruits-Bazar 1.0 is vulnerable to SQL Injection in /show_price_by_pdtId.php.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/um-dsp/TaintRadar/blob/main/sql_injection_cves/ecommercefruitsbazarmaster/20250811-ecommerce-project-with-php-and-mysqli-fruits-bazar-show_price_by_pdtid.php-pid-sqli/20250811-ecommerce-project-with-php-and-mysqli-fruits-bazar-show_price_by_pdtid.php-pid-sqli.md

### [CVE-2026-48499](https://github.com/activepieces/activepieces/commit/9d8d328424bd32d295c5727af7550e1b57f9074d)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-48499
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-31 04:17:32 JST
- 更新日: 2026-07-31 05:07:01 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Activepieces is an open source AI workflow automation platform. Prior to 0.84.0, an unsanitized path segment in the Code piece sandbox can let an authenticated flow author reach read-write cached flow and code files belonging to other tenants on the same worker, exposing embedded data and allowing modified code to exec...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/activepieces/activepieces/commit/9d8d328424bd32d295c5727af7550e1b57f9074d
- https://github.com/activepieces/activepieces/releases/tag/0.84.0
- https://github.com/activepieces/activepieces/security/advisories/GHSA-5h2x-g6m3-grmq

### [CVE-2026-11707](https://www.ibm.com/support/pages/node/7281073)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-11707
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-31 00:16:24 JST
- 更新日: 2026-07-31 01:33:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: IBM Tivoli System Automation Application Manager 4.1 and IBM WebSphere Application Server is affected by a cross-site scripting vulnerability in the administrative console login page.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7281073

### [CVE-2026-66418](https://github.com/theopaid/Unauthenticated-Stored-Cross-Site-Scripting-Leading-To-Administrator-Account-Takeover)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-66418
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-31 06:18:12 JST
- 更新日: 2026-07-31 06:18:12 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenClaw Dashboard v3.0.0 contains a stored cross-site scripting vulnerability that allows unauthenticated remote attackers to inject arbitrary HTML and script payloads by submitting a crafted username in a failed login POST request, which is recorded verbatim in the audit log. When an administrator opens the notificat...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/theopaid/Unauthenticated-Stored-Cross-Site-Scripting-Leading-To-Administrator-Account-Takeover
- https://github.com/tugcantopaloglu/openclaw-dashboard
- https://www.vulncheck.com/advisories/openclaw-dashboard-stored-xss-via-failed-login-username-field

### [CVE-2026-54722](https://github.com/HackingRepo/dssrf-js/commit/9211f91bf532433a1a1b27d946571546a63664b3)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-54722
- 関連キーワード: gin, node.js
- 影響製品: -
- 公開日: 2026-07-31 02:16:33 JST
- 更新日: 2026-07-31 04:18:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: DSSRF is a Node.js library that provides a wide range of utilities and advanced SSRF defense checks. Prior to 1.0.4, is_url_safe in src/helpers.ts strips the @ userinfo delimiter with remove_at_symbol_in_string before new URL parses the URL, allowing an attacker-controlled URL to bypass internal-IP validation and cause...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/HackingRepo/dssrf-js/commit/9211f91bf532433a1a1b27d946571546a63664b3
- https://github.com/HackingRepo/dssrf-js/issues/97
- https://github.com/HackingRepo/dssrf-js/pull/98
- https://github.com/HackingRepo/dssrf-js/security/advisories/GHSA-cg4g-m8jx-vjv2
- https://github.com/HackingRepo/dssrf-js/security/advisories/GHSA-cg4g-m8jx-vjv2

### [CVE-2026-66416](https://github.com/Leantime/leantime)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-66416
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-31 04:18:36 JST
- 更新日: 2026-07-31 04:56:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Leantime 3.6.2 contains a cross-site request forgery vulnerability that allows unauthenticated attackers to perform state-changing actions on behalf of authenticated users by excluding the Laravel VerifyCsrfToken middleware from the global middleware stack in app/Http/Kernel.php. Attackers can craft malicious pages del...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Leantime/leantime
- https://github.com/Leantime/leantime/pull/3659
- https://github.com/javokhir-sec/CVE-PoC-Hub/security/advisories/GHSA-x8vx-9g5w-w5rr
- https://www.vulncheck.com/advisories/leantime-csrf-protection-globally-disabled-by-omission-of-laravel-verifycsrftoken-middleware

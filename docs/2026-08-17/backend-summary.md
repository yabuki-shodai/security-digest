# Backend CVE Summary (2026-08-17)

## Overview

- 取得日時: 2026-08-17 20:23:42 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 30
- Critical: 22
- High: 5
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-74798](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-43jx-gxq4-jpjc)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-74798
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-17 20:16:39 JST
- 更新日: 2026-08-17 20:16:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SiYuan kernel before v3.7.4 contains a path traversal vulnerability in the database_clean MCP tool. The tool performs only an empty-string check on the id parameter before passing it to RemoveUnusedAttributeView (kernel/model/attribute_view.go), which builds a filesystem path via filepath.Join without validating that i...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-43jx-gxq4-jpjc
- https://www.vulncheck.com/advisories/siyuan-kernel-path-traversal-via-database-clean-mcp-tool

### [CVE-2026-15623](https://docs.cloud.google.com/chronicle/docs/soar/release-notes#May_23_2026)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-15623
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 16:17:12 JST
- 更新日: 2026-08-17 16:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A SQL Injection vulnerability in a legacy dashboard widget API in Google Cloud Google SecOps (Chronicle SOAR) versions prior to 6.3.85 on Google Cloud Platform allows an authenticated attacker to execute blind SQL queries using a crafted request parameter. This vulnerability was patched in version 6.3.85, and no custom...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.cloud.google.com/chronicle/docs/soar/release-notes#May_23_2026

### [CVE-2026-19959](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWanTcpipSetup-34b53a41781f8047b36bd11dbcaa84dc?source=copy_link)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-19959
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 08:16:24 JST
- 更新日: 2026-08-17 08:16:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A weakness has been identified in Edimax EW-7478APC 1.04. This affects the function formWanTcpipSetup of the file /goform/formWanTcpipSetup. This manipulation of the argument pppUserName causes stack-based buffer overflow. Remote exploitation of the attack is possible. The exploit has been made available to the public...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWanTcpipSetup-34b53a41781f8047b36bd11dbcaa84dc?source=copy_link
- https://vuldb.com/cve/CVE-2026-19959
- https://vuldb.com/submit/872873
- https://vuldb.com/vuln/391136
- https://vuldb.com/vuln/391136/cti

### [CVE-2026-19961](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWlSiteSurvey-34b53a41781f804fb328d87416095401?source=copy_link)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-19961
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 08:16:25 JST
- 更新日: 2026-08-17 08:16:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was detected in Edimax EW-7478APC 1.04. Affected is the function formWlSiteSurvey of the file /goform/formWlSiteSurvey. Performing a manipulation of the argument selSSID results in buffer overflow. The attack is possible to be carried out remotely. The exploit is now public and may be used. The vendor w...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWlSiteSurvey-34b53a41781f804fb328d87416095401?source=copy_link
- https://vuldb.com/cve/CVE-2026-19961
- https://vuldb.com/submit/872875
- https://vuldb.com/vuln/391138
- https://vuldb.com/vuln/391138/cti

### [CVE-2026-74799](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-9cqq-p2hw-mj3f)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-74799
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 20:16:40 JST
- 更新日: 2026-08-17 20:16:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SiYuan before 3.7.4 registers Go net/http/pprof debug endpoints including heap and goroutine dumps without authentication when --mode flag is not set to exactly prod. Attackers can access /debug/pprof/heap and related endpoints to extract in-memory secrets including AccessAuthCode and AI provider API keys.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-9cqq-p2hw-mj3f
- https://www.vulncheck.com/advisories/siyuan-before-unauthenticated-debug-endpoint-information-disclosure

### [CVE-2026-74868](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-phg7-xcr4-q5wg)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-74868
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 20:16:41 JST
- 更新日: 2026-08-17 20:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SiYuan versions before 3.7.4 contain an unthrottled brute-force vulnerability in the Publish Service Basic Auth implementation (PublishServiceTransport.RoundTrip() in kernel/server/proxy/publish.go). The Publish Service runs on a separate, unauthenticated-by-default listener (default TCP port 6808) and gates named publ...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-phg7-xcr4-q5wg
- https://www.vulncheck.com/advisories/siyuan-before-brute-force-authentication-via-publish-service

### [CVE-2026-19960](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWlbasic-34b53a41781f8097b9efd3042e977e09?source=copy_link)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-19960
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 08:16:24 JST
- 更新日: 2026-08-17 08:16:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security vulnerability has been detected in Edimax EW-7478APC 1.04. This impacts the function formWlbasic of the file /goform/formWlbasic. Such manipulation of the argument rootAPmac leads to command injection. The attack can be executed remotely. The exploit has been disclosed publicly and may be used. The vendor wa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWlbasic-34b53a41781f8097b9efd3042e977e09?source=copy_link
- https://vuldb.com/cve/CVE-2026-19960
- https://vuldb.com/submit/872874
- https://vuldb.com/vuln/391137
- https://vuldb.com/vuln/391137/cti

### [CVE-2026-19962](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-setWAN-34b53a41781f808aaf2bc972cc6d38d3?source=copy_link)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-19962
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 09:16:26 JST
- 更新日: 2026-08-17 09:16:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw has been found in Edimax EW-7478APC 1.04. Affected by this vulnerability is the function setWAN of the file /goform/setWAN. Executing a manipulation of the argument pppUserName/pptpUserName/L2TPUserName can lead to command injection. The attack may be performed from remote. The exploit has been published and may...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-setWAN-34b53a41781f808aaf2bc972cc6d38d3?source=copy_link
- https://vuldb.com/cve/CVE-2026-19962
- https://vuldb.com/submit/872876
- https://vuldb.com/vuln/391139
- https://vuldb.com/vuln/391139/cti

### [CVE-2026-19963](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-stainfo-34b53a41781f80ed8e15c109f7a50844?source=copy_link)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-19963
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 09:16:27 JST
- 更新日: 2026-08-17 09:16:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability has been found in Edimax EW-7478APC 1.04. Affected by this issue is the function stainfo of the file /goform/stainfo. The manipulation of the argument interface leads to command injection. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The v...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-stainfo-34b53a41781f80ed8e15c109f7a50844?source=copy_link
- https://vuldb.com/cve/CVE-2026-19963
- https://vuldb.com/submit/872877
- https://vuldb.com/vuln/391140
- https://vuldb.com/vuln/391140/cti

### [CVE-2026-19956](https://github.com/gomarble-ai/facebook-ads-mcp-server/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-19956
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-17 06:16:37 JST
- 更新日: 2026-08-17 06:16:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability has been found in gomarble-ai facebook-ads-mcp-server 0.1.0. The impacted element is the function fetch_pagination_url of the file server.py. Such manipulation leads to server-side request forgery. The attack can be launched remotely. The name of the patch is 4e53875aa22e8991c2fa4a7660d86e1caba66659. Ap...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gomarble-ai/facebook-ads-mcp-server/
- https://github.com/gomarble-ai/facebook-ads-mcp-server/commit/4e53875aa22e8991c2fa4a7660d86e1caba66659
- https://github.com/gomarble-ai/facebook-ads-mcp-server/issues/29
- https://github.com/gomarble-ai/facebook-ads-mcp-server/pull/32
- https://vuldb.com/cve/CVE-2026-19956

### [CVE-2026-19978](https://github.com/jiantao88/android-mcp-server/)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-19978
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 13:16:54 JST
- 更新日: 2026-08-17 13:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw has been found in jiantao88 android-mcp-server up to cfb872b2446794193b58edd63f4dbf6af48a6292. The impacted element is the function child_process.exec of the file build/index.js of the component Command Execution. Executing a manipulation of the argument deviceId/packageName/permission/extras[].key/extras[].valu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jiantao88/android-mcp-server/
- https://github.com/jiantao88/android-mcp-server/commit/14e2bf27c88ba137e35cbb0c2a75f72b595bb98a
- https://github.com/jiantao88/android-mcp-server/issues/1
- https://vuldb.com/cve/CVE-2026-19978
- https://vuldb.com/submit/873898

### [CVE-2026-74895](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-623h-chj7-hfx8)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74895
- 関連キーワード: python, gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:44 JST
- 更新日: 2026-08-17 20:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 fail to apply sandbox restrictions in the default process isolation mode for plugin execution. Attackers can execute malicious plugins with unrestricted access to the filesystem, network, subprocess execution, and all Python modules.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-623h-chj7-hfx8
- https://www.vulncheck.com/advisories/openssl-encrypt-before-plugin-sandbox-bypass-via-process-isolation

### [CVE-2026-74899](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-m25m-ggxg-239c)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74899
- 関連キーワード: python, gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:44 JST
- 更新日: 2026-08-17 20:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a sandbox escape vulnerability in IsolatedPluginExecutor that exposes Python type objects in restricted exec() builtins. Attackers can traverse the Python class hierarchy via __class__.__mro__.__subclasses__() to access system functions and execute arbitrary OS commands.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-m25m-ggxg-239c
- https://www.vulncheck.com/advisories/openssl-encrypt-before-sandbox-escape-via-type-hierarchy

### [CVE-2026-74887](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-cx72-m6xj-3vf6)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-74887
- 関連キーワード: python, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:43 JST
- 更新日: 2026-08-17 20:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt before 1.4.0 imports Python's non-cryptographic 'random' module (Mersenne Twister PRNG) at line 15 of openssl_encrypt/modules/pqc.py. No direct calls to random.* were present in the code, so no cryptographic operation is currently affected; however, the import creates a hazard that future code could ina...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-cx72-m6xj-3vf6
- https://www.vulncheck.com/advisories/openssl-encrypt-before-insecure-random-import-in-pqc-module

### [CVE-2026-74874](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-vfgx-5q85-58q3)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-74874
- 関連キーワード: python, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:41 JST
- 更新日: 2026-08-17 20:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 use Python's non-cryptographic random module for steganographic pixel selection in the generate_pseudorandom_sequence function. Attackers who know the password can recover the Mersenne Twister state from approximately 624 outputs and predict pixel locations containing hidden data f...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-vfgx-5q85-58q3
- https://www.vulncheck.com/advisories/openssl-encrypt-before-weak-prng-steganography-pixel-selection

### [CVE-2026-19964](http://github.com/Jij-Inc/Jij-MCP-Server/issues/4)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-19964
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-17 09:16:27 JST
- 更新日: 2026-08-17 09:16:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was found in Jij-Inc Jij-MCP-Server 0.1.0. This affects the function PythonREPL.run of the file jij_mcp/python_repr.py of the component jm_check. The manipulation of the argument code results in code injection. It is possible to launch the attack remotely. The exploit has been made public and could be u...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- http://github.com/Jij-Inc/Jij-MCP-Server/issues/4
- https://vuldb.com/cve/CVE-2026-19964
- https://vuldb.com/submit/872906
- https://vuldb.com/vuln/391141
- https://vuldb.com/vuln/391141/cti

### [CVE-2026-74891](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-v4vm-4xf2-fhqj)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74891
- 関連キーワード: postgresql, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:44 JST
- 更新日: 2026-08-17 20:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain hardcoded database credentials in standalone server configuration files. Attackers on the same network can access PostgreSQL databases using well-known default credentials to retrieve sensitive data.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-v4vm-4xf2-fhqj
- https://www.vulncheck.com/advisories/openssl-encrypt-before-hardcoded-database-credentials

### [CVE-2026-74894](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-4g2c-wpgj-49w8)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74894
- 関連キーワード: gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:44 JST
- 更新日: 2026-08-17 20:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt before 1.4.0 contains an authentication bypass vulnerability in the verify_api_token function that accepts any non-empty Bearer token string without validation. Attackers can upload arbitrary public keys, enumerate all keys, and revoke keys belonging to any user by providing any Bearer token in the Auth...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-4g2c-wpgj-49w8
- https://www.vulncheck.com/advisories/openssl-encrypt-before-authentication-bypass-via-bearer-token

### [CVE-2026-74878](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-h45m-mgcp-q388)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74878
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:42 JST
- 更新日: 2026-08-17 20:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 use an in-memory rate limiter for TOTP brute-force protection that is not shared across workers and is lost on server restart. Attackers can distribute authentication attempts across multiple server instances or retry immediately after a restart to bypass rate limiting protections.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-h45m-mgcp-q388
- https://www.vulncheck.com/advisories/openssl-encrypt-before-totp-rate-limiter-bypass

### [CVE-2026-74890](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-rvc2-5jxq-gpcj)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-74890
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:43 JST
- 更新日: 2026-08-17 20:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain an authentication bypass vulnerability in CamelliaCipher that disables HMAC tag generation and verification when the PYTEST_CURRENT_TEST environment variable is set. Attackers with code execution can set this environment variable to produce unauthenticated ciphertext and by...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-rvc2-5jxq-gpcj
- https://www.vulncheck.com/advisories/openssl-encrypt-before-hmac-authentication-bypass-via-environment-variable

### [CVE-2026-74901](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-w4j7-wfgw-r52w)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74901
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:45 JST
- 更新日: 2026-08-17 20:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain an authentication bypass vulnerability in pqc.py where AES-GCM decryption failures trigger fallback to unauthenticated AES-CTR mode. Attackers can modify ciphertext in transit to bypass integrity verification and perform bit-flipping attacks without detection.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-w4j7-wfgw-r52w
- https://www.vulncheck.com/advisories/openssl-encrypt-before-authentication-bypass-via-aes-ctr-fallback

### [CVE-2026-74885](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-43r4-3hf9-m84q)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-74885
- 関連キーワード: gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:43 JST
- 更新日: 2026-08-17 20:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a logging bug in restore_hidden_modules() that logs module counts after clearing, always showing zero restored modules and corrupting audit trails. Additionally, a race condition exists between module hiding and import hook installation where another thread could re-import...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-43r4-3hf9-m84q
- https://www.vulncheck.com/advisories/openssl-encrypt-before-logging-bug-and-race-condition

### [CVE-2026-74886](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-9pgj-v69p-q586)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74886
- 関連キーワード: gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:43 JST
- 更新日: 2026-08-17 20:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a plugin sandbox bypass vulnerability where the PluginImportGuard blocks a different set of modules than the AST analyzer's DANGEROUS_MODULES set. Attackers can bypass AST analysis through string obfuscation or encoding to import unblocked dangerous modules like sys, shutil...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-9pgj-v69p-q586
- https://www.vulncheck.com/advisories/openssl-encrypt-before-plugin-import-guard-bypass

### [CVE-2026-74896](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-w7gr-9g4g-33mx)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74896
- 関連キーワード: gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:44 JST
- 更新日: 2026-08-17 20:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a sandbox escape vulnerability in the DangerousPatternVisitor AST analyzer that fails to detect dunder attribute traversal techniques. Attackers can use __class__, __bases__, __subclasses__(), and __globals__ chains to access restricted functions and execute arbitrary syste...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-w7gr-9g4g-33mx
- https://www.vulncheck.com/advisories/openssl-encrypt-before-sandbox-escape-via-dunder-attribute-traversal

### [CVE-2026-74872](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-j48q-4c78-rhf9)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74872
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:41 JST
- 更新日: 2026-08-17 20:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain an arbitrary code execution vulnerability in the Whirlpool hash implementation that uses broad glob patterns to load .so modules without integrity verification. Attackers can place malicious .so files matching the whirlpool*py313*.so pattern in site-packages directories to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-j48q-4c78-rhf9
- https://www.vulncheck.com/advisories/openssl-encrypt-before-arbitrary-code-execution-via-whirlpool

### [CVE-2026-74875](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-425g-fjhq-5h92)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74875
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:41 JST
- 更新日: 2026-08-17 20:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 silently skip JSON schema validation when the jsonschema library is not installed, allowing malformed metadata to be accepted. Attackers can remove the jsonschema package or supply unknown metadata format versions to bypass all schema checks and process malicious data.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-425g-fjhq-5h92
- https://www.vulncheck.com/advisories/openssl-encrypt-before-schema-validation-bypass

### [CVE-2026-74876](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-8h88-gxp3-j7pg)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74876
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:42 JST
- 更新日: 2026-08-17 20:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a vulnerability in PublicKeyBundle.from_dict() that creates key bundles from untrusted data without verifying signatures. Attackers can call from_dict() followed by to_identity() without signature verification to encrypt data using attacker-controlled public keys, leaking s...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-8h88-gxp3-j7pg
- https://www.vulncheck.com/advisories/openssl-encrypt-before-unverified-key-bundle-encryption

### [CVE-2026-74880](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-4rh7-jwg9-m28m)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74880
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:42 JST
- 更新日: 2026-08-17 20:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 accept refresh tokens as URL query parameters in keyserver and telemetry server routes. Attackers can extract tokens from server logs, proxy logs, browser history, and HTTP Referer headers to gain unauthorized access.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-4rh7-jwg9-m28m
- https://www.vulncheck.com/advisories/openssl-encrypt-before-token-leakage-via-query-parameters

### [CVE-2026-74889](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-j9mh-57cc-665x)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74889
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:43 JST
- 更新日: 2026-08-17 20:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 use HKDF with no salt and static info parameter in key normalization functions, reducing entropy extraction and determinism. Attackers can exploit predictable key derivation with identical inputs to weaken cryptographic security against multi-target attacks.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-j9mh-57cc-665x
- https://www.vulncheck.com/advisories/openssl-encrypt-before-weak-key-derivation-via-hkdf

### [CVE-2026-74900](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-p3gq-pcg9-qvfv)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74900
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:45 JST
- 更新日: 2026-08-17 20:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a critical vulnerability in pqc.py where KEM decapsulation failures silently fall back to simulation mode, generating a deterministic shared secret from only 16 bytes of the private key and publicly available encapsulated key data. Attackers who obtain 16 bytes of the priva...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-p3gq-pcg9-qvfv
- https://www.vulncheck.com/advisories/openssl-encrypt-before-weak-shared-secret-via-pqc-simulation-mode

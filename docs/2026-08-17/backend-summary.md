# Backend CVE Summary (2026-08-17)

## Overview

- 取得日時: 2026-08-17 19:48:32 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 11
- Critical: 3
- High: 3
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-15623](https://docs.cloud.google.com/chronicle/docs/soar/release-notes#May_23_2026)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-15623
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 16:17:12 JST
- 更新日: 2026-08-17 16:17:12 JST
- 出典: NVD

#### GitHub Models要約

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

#### GitHub Models要約

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

#### GitHub Models要約

- 日本語要約: A vulnerability was detected in Edimax EW-7478APC 1.04. Affected is the function formWlSiteSurvey of the file /goform/formWlSiteSurvey. Performing a manipulation of the argument selSSID results in buffer overflow. The attack is possible to be carried out remotely. The exploit is now public and may be used. The vendor w...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWlSiteSurvey-34b53a41781f804fb328d87416095401?source=copy_link
- https://vuldb.com/cve/CVE-2026-19961
- https://vuldb.com/submit/872875
- https://vuldb.com/vuln/391138
- https://vuldb.com/vuln/391138/cti

### [CVE-2026-19960](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWlbasic-34b53a41781f8097b9efd3042e977e09?source=copy_link)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-19960
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 08:16:24 JST
- 更新日: 2026-08-17 08:16:24 JST
- 出典: NVD

#### GitHub Models要約

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

#### GitHub Models要約

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

#### GitHub Models要約

- 日本語要約: A vulnerability has been found in Edimax EW-7478APC 1.04. Affected by this issue is the function stainfo of the file /goform/stainfo. The manipulation of the argument interface leads to command injection. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The v...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-stainfo-34b53a41781f80ed8e15c109f7a50844?source=copy_link
- https://vuldb.com/cve/CVE-2026-19963
- https://vuldb.com/submit/872877
- https://vuldb.com/vuln/391140
- https://vuldb.com/vuln/391140/cti

### [CVE-2026-19978](https://github.com/jiantao88/android-mcp-server/)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-19978
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 13:16:54 JST
- 更新日: 2026-08-17 13:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A flaw has been found in jiantao88 android-mcp-server up to cfb872b2446794193b58edd63f4dbf6af48a6292. The impacted element is the function child_process.exec of the file build/index.js of the component Command Execution. Executing a manipulation of the argument deviceId/packageName/permission/extras[].key/extras[].valu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jiantao88/android-mcp-server/
- https://github.com/jiantao88/android-mcp-server/commit/14e2bf27c88ba137e35cbb0c2a75f72b595bb98a
- https://github.com/jiantao88/android-mcp-server/issues/1
- https://vuldb.com/cve/CVE-2026-19978
- https://vuldb.com/submit/873898

### [CVE-2026-19964](http://github.com/Jij-Inc/Jij-MCP-Server/issues/4)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-19964
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-17 09:16:27 JST
- 更新日: 2026-08-17 09:16:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability was found in Jij-Inc Jij-MCP-Server 0.1.0. This affects the function PythonREPL.run of the file jij_mcp/python_repr.py of the component jm_check. The manipulation of the argument code results in code injection. It is possible to launch the attack remotely. The exploit has been made public and could be u...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- http://github.com/Jij-Inc/Jij-MCP-Server/issues/4
- https://vuldb.com/cve/CVE-2026-19964
- https://vuldb.com/submit/872906
- https://vuldb.com/vuln/391141
- https://vuldb.com/vuln/391141/cti

### [CVE-2026-14832](https://wpscan.com/vulnerability/3b651e19-37f5-468e-8d0b-a82bbe04eaf2/)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-14832
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-17 15:17:31 JST
- 更新日: 2026-08-17 15:17:31 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The ShopSmart Loyalty for WooCommerce WordPress plugin through 1.0.0 does not perform any authorization or ownership check on a phone-number lookup exposed to unauthenticated users, allowing anyone who knows a customer's phone number to retrieve that customer's loyalty profile, including name, email, and account balanc...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://wpscan.com/vulnerability/3b651e19-37f5-468e-8d0b-a82bbe04eaf2/

### [CVE-2026-13700](https://wpscan.com/vulnerability/dd9e51a2-43fb-46de-8e59-2d9611fcc4ff/)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-13700
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-17 15:17:31 JST
- 更新日: 2026-08-17 15:17:31 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The WooMS WordPress plugin through 9.14 does not validate a user-supplied URL before using it in a server-side request and attaches stored third-party integration credentials to every such request, allowing unauthenticated attackers to perform Server-Side Request Forgery and to disclose the configured integration crede...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://wpscan.com/vulnerability/dd9e51a2-43fb-46de-8e59-2d9611fcc4ff/

### [CVE-2026-74579](https://git.kernel.org/stable/c/16b553c46e347bc9de9946c4960654d5884a86de)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74579
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-08-17 15:19:56 JST
- 更新日: 2026-08-17 15:19:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_payload: fix mask build for partial field offload nft_payload_offload_mask() builds the offload match mask for a payload expression that covers only part of a header field. For a partial IPv6 address match (field_len = 16, priv_len = 1)...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/16b553c46e347bc9de9946c4960654d5884a86de
- https://git.kernel.org/stable/c/39e88f28fb32bf02bd4b525c24c842c9cff5663d
- https://git.kernel.org/stable/c/630295d5bba1d0e0f494cc459452eb0a0058c545
- https://git.kernel.org/stable/c/a375d8ace807767f29f276b681b6324c74929b1d
- https://git.kernel.org/stable/c/b19b5d2e042c294e2cc1c908dc598f9d64015396

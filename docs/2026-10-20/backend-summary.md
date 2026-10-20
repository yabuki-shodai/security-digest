# Backend CVE Summary (2026-10-20)

## Overview

- 取得日時: 2026-10-20 10:03:21 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 23
- Critical: 3
- High: 7
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-112368](https://jira.mongodb.org/browse/PHPC-276)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-112368
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-20 01:17:07 JST
- 更新日: 2026-10-20 06:13:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An uncontrolled recursion weakness in the BSON decoding logic of the MongoDB PHP driver may allow an unauthenticated party who can supply crafted binary document data to the decoder to exhaust the process stack. This may cause the PHP process using the driver to terminate unexpectedly, resulting in a loss of availabili...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/PHPC-276

### [CVE-2026-112150](https://github.com/vraj404/Criminal-Management-System/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-112150
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-20 00:17:05 JST
- 更新日: 2026-10-20 05:43:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security flaw has been discovered in vraj404 Criminal-Management-System up to 2808d057e7ddc5295519a487365b0cacfd0ba8c4. Affected is an unknown function of the file search.php. The manipulation of the argument Search results in sql injection. The attack can be executed remotely. The exploit has been released to the pu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vraj404/Criminal-Management-System/
- https://github.com/vraj404/Criminal-Management-System/issues/2
- https://vuldb.com/cve/CVE-2026-112150
- https://vuldb.com/submit/1014016
- https://vuldb.com/vuln/422257

### [CVE-2026-6719](https://www.ibm.com/support/pages/node/7292374)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-6719
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-20 03:17:08 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Concert 1.0 through 3.0.0 uses weaker than expected cryptographic algorithms that could allow an attacker to decrypt highly sensitive information.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7292374

### [CVE-2025-13173](https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2025-4727/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2025-13173
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-20 02:16:59 JST
- 更新日: 2026-10-20 06:06:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tokens associated with user sessions are not revoked when the corresponding user session is terminated, unless another SSO request is initiated. This occurs when the session-bound token feature is enabled with token binding validation and the "Revoke token upon user logout" option is not active. The software fails to a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2025-4727/

### [CVE-2026-112300](https://github.com/DiffSK/configobj/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-112300
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-10-20 06:17:06 JST
- 更新日: 2026-10-20 06:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was identified in DiffSK configobj up to 5.0.9. Affected by this vulnerability is the function _sectionmarker of the file configobj/__init__.py. The manipulation leads to inefficient regular expression complexity. Remote exploitation of the attack is possible. The project was informed of the problem ear...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/DiffSK/configobj/
- https://github.com/DiffSK/configobj/issues/281
- https://vuldb.com/cve/CVE-2026-112300
- https://vuldb.com/submit/989395
- https://vuldb.com/vuln/422346

### [CVE-2026-112159](https://gist.github.com/Seikruun/b628bb6d4403d9c41a54a4b92d775583)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-112159
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-20 02:17:13 JST
- 更新日: 2026-10-20 05:43:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security vulnerability has been detected in JumpServer up to 4.10.19. The affected element is an unknown function of the component Template Rendering. The manipulation of the argument IP/HOST leads to os command injection. Remote exploitation of the attack is possible. The exploit has been disclosed publicly and may...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gist.github.com/Seikruun/b628bb6d4403d9c41a54a4b92d775583
- https://github.com/jumpserver/jumpserver/
- https://github.com/jumpserver/jumpserver/commit/fcf2904cdb884230e9676f50f37a44d09fa97040
- https://github.com/jumpserver/jumpserver/pull/17500/
- https://github.com/jumpserver/jumpserver/releases/tag/v5.0.0

### [CVE-2026-112251](https://drive.google.com/drive/folders/1fvX6wjfHd58SzCAZd5-4Zn-mh9jqx8mz?usp=drive_link)

> **Backend** / **MEDIUM** / CVSS: **5.0** / KEV: **no**

- タイトル: CVE-2026-112251
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-20 04:17:26 JST
- 更新日: 2026-10-20 05:43:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was detected in antoinersx clawhost up to 0.0.45. This affects the function handleRequest of the file apps/clawhostgo/src/main/services/reverseProxy.ts of the component Reverse Proxy. Performing a manipulation of the argument token results in open redirect. The attack can be initiated remotely. The expl...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://drive.google.com/drive/folders/1fvX6wjfHd58SzCAZd5-4Zn-mh9jqx8mz?usp=drive_link
- https://vuldb.com/cve/CVE-2026-112251
- https://vuldb.com/submit/986376
- https://vuldb.com/vuln/422332
- https://vuldb.com/vuln/422332/cti

### [CVE-2026-3161](https://www.ibm.com/support/pages/node/7290183)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-3161
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-20 03:17:07 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Cloud Pak System 2.3.6.0, and 2.3.6.1 uses weaker than expected cryptographic algorithms that could allow an attacker to decrypt highly sensitive information.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7290183

### [CVE-2026-6930](https://www.ibm.com/support/pages/node/7292374)

> **Backend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-6930
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-20 02:17:21 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Concert 1.0 through 3.0.0 uses weaker than expected cryptographic algorithms that could allow an attacker to decrypt highly sensitive information.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7292374

### [CVE-2026-111057](https://github.com/mljar/mercury/commit/8c467129037ee9df269d543ac217ffd33b97bf3f)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-111057
- 関連キーワード: python, express
- 影響製品: -
- 公開日: 2026-10-20 01:17:03 JST
- 更新日: 2026-10-20 06:14:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mercury is a Python framework for sharing Jupyter notebooks as web applications and dashboards. From 3.0.0 until 3.2.4, a missing comma in BLOCKED_PATTERNS concatenates the /lab and /api/terminals regular-expression literals. Requests to /api/terminals therefore bypass the anonymous endpoint blocklist and reach Jupyter...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mljar/mercury/commit/8c467129037ee9df269d543ac217ffd33b97bf3f
- https://github.com/mljar/mercury/releases/tag/v3.2.4
- https://github.com/mljar/mercury/security/advisories/GHSA-f8c7-rwf9-fmgm

### [CVE-2026-112393](https://github.com/python-pillow/Pillow/commit/11582e5ffbdceb973d5ee593f3105af5a9852b40)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-112393
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-20 06:17:07 JST
- 更新日: 2026-10-20 07:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Pillow is a Python imaging library. From 2.0.0 until 13.0.0, Pillow has a heap buffer overflow and stale-heap disclosure in _tiffWriteProc when saving compressed TIFF data through libtiff to a target without a usable fileno(), such as BytesIO. The callback sizes its allocation from the prior buffer size instead of the...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/python-pillow/Pillow/commit/11582e5ffbdceb973d5ee593f3105af5a9852b40
- https://github.com/python-pillow/Pillow/releases/tag/13.0.0
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-332p-7hrc-92wf
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-332p-7hrc-92wf

### [CVE-2026-111058](https://github.com/mljar/mercury/commit/73a40ceb0becf057f495a5738ad7f5a5222a53e1)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-111058
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-20 01:17:03 JST
- 更新日: 2026-10-20 06:13:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mercury is a Python framework for sharing Jupyter notebooks as web applications and dashboards. Prior to 3.2.6, default tokenless deployments allow anonymous clients to create Jupyter kernels and send execute_request messages containing arbitrary Python. The endpoint blocklist does not cover /api/kernels, and the webso...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mljar/mercury/commit/73a40ceb0becf057f495a5738ad7f5a5222a53e1
- https://github.com/mljar/mercury/releases/tag/3.2.6
- https://github.com/mljar/mercury/security/advisories/GHSA-rv4m-xm3f-3ccq

### [CVE-2026-112390](https://github.com/python-pillow/Pillow/commit/26cb3ed061173b817b9ee4b6f507cb0e1e293218)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-112390
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-20 06:17:07 JST
- 更新日: 2026-10-20 06:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Pillow is a Python imaging library. From 7.2.0 until 13.0.0, Pillow can enter an infinite loop while determining the frame count of a MIC image. MicImageFile inherits TIFF frame traversal, but MicImageFile.tell reports the OLE stream index and its seek() resets TIFF frame state, so an embedded TIFF with at least three...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/python-pillow/Pillow/commit/26cb3ed061173b817b9ee4b6f507cb0e1e293218
- https://github.com/python-pillow/Pillow/releases/tag/13.0.0
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-22hg-r758-rrw9

### [CVE-2026-111064](https://github.com/aio-libs/aiohttp/commit/be846822b4b3a5a54b6163e794b42dc06fba54a3)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-111064
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-20 02:17:03 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, keepalive timeout handling is absent during the initial portion of a request. An attacker can keep an idle connection open indefinitely before sending any request data, consuming server connection capacity. This issue is fi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/aio-libs/aiohttp/commit/be846822b4b3a5a54b6163e794b42dc06fba54a3
- https://github.com/aio-libs/aiohttp/releases/tag/v3.14.4
- https://github.com/aio-libs/aiohttp/security/advisories/GHSA-5wr8-gcqf-gqf3

### [CVE-2026-111066](https://github.com/aio-libs/aiohttp/commit/2d94633b7f1b4c1ba07d647b629a8440652b2d09)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-111066
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-20 02:17:03 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. From 2.0.0 until 3.14.4, multipart request processing can retain an unbounded number of open file descriptors. An unauthenticated attacker can consequently exhaust file descriptors with specially crafted multipart requests when a handler us...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/aio-libs/aiohttp/commit/2d94633b7f1b4c1ba07d647b629a8440652b2d09
- https://github.com/aio-libs/aiohttp/releases/tag/v3.14.4
- https://github.com/aio-libs/aiohttp/security/advisories/GHSA-9xw5-w5jj-pvcg

### [CVE-2026-112304](https://github.com/mindee/doctr/blob/v1.1.0/doctr/models/utils/pytorch.py)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-112304
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-20 01:17:06 JST
- 更新日: 2026-10-20 06:14:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: docTR through 1.1.0 contains an unsafe deserialization vulnerability in load_pretrained_params() that loads checkpoints with torch.load without weights_only=True. Attackers who control a local or URL-supplied checkpoint can embed a malicious pickle payload to execute Python code with the loading process's privileges on...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mindee/doctr/blob/v1.1.0/doctr/models/utils/pytorch.py
- https://github.com/mindee/doctr/commit/687503dd15592483c4699ee51280b41938579a9e
- https://github.com/mindee/doctr/issues/2175
- https://www.vulncheck.com/advisories/doctr-through-1.1.0-unsafe-deserialization-rce-via-load-pretrained-params

### [CVE-2026-111063](https://github.com/aio-libs/aiohttp/commit/999c356d61e966faffa97b06ab0d0455226d36c5)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-111063
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-20 02:17:03 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, the Secure attribute for a shared cookie is not enforced. An attacker can consequently cause a shared cookie marked Secure to be sent with an unencrypted request. This issue is fixed in version 3.14.4.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/aio-libs/aiohttp/commit/999c356d61e966faffa97b06ab0d0455226d36c5
- https://github.com/aio-libs/aiohttp/releases/tag/v3.14.4
- https://github.com/aio-libs/aiohttp/security/advisories/GHSA-494j-54xm-rwp3

### [CVE-2026-112391](https://github.com/python-pillow/Pillow/commit/94cb11c44ff7345414da17ebfea1598a529ad9cd)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-112391
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-20 06:17:07 JST
- 更新日: 2026-10-20 06:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Pillow is a Python imaging library. From 5.1.0 until 13.0.0, Pillow's PdfParser.get_value() can recurse without a limit while reading nested PDF objects. The parser follows attacker-controlled arrays and dictionaries when an existing PDF is opened for append. An attacker can provide a deeply nested PDF to an applicatio...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/python-pillow/Pillow/commit/94cb11c44ff7345414da17ebfea1598a529ad9cd
- https://github.com/python-pillow/Pillow/releases/tag/13.0.0
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-254f-3936-288h

### [CVE-2026-112394](https://github.com/python-pillow/Pillow/commit/392ee6f0d19a4adb766a63e9a99f3c28193b8d31)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-112394
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-20 06:17:07 JST
- 更新日: 2026-10-20 06:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Pillow is a Python imaging library. Prior to 13.0.0, Pillow's P;2L and P;4L raw decoders can read past the end of an input buffer. ImagingRawDecode calculates a packed-pixel row size, while the unpackers read separately padded bit planes. A caller can supply a buffer and image dimensions whose accepted size is smaller...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/python-pillow/Pillow/commit/392ee6f0d19a4adb766a63e9a99f3c28193b8d31
- https://github.com/python-pillow/Pillow/releases/tag/13.0.0
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-4558-3h8r-v8xp

### [CVE-2026-112395](https://github.com/python-pillow/Pillow/commit/76869efdbbf2ad7dccd7536520fb61b7a00ab61e)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-112395
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-20 06:17:07 JST
- 更新日: 2026-10-20 06:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Pillow is a Python imaging library. From 8.2.0 until 13.0.0, Pillow's tiled-TIFF decoder can read past the tile buffer while copying four-byte pixels. In _decodeTile, libtiff can return a tile allocation smaller than the required row stride multiplied by the tile length, and Pillow's stride-and-copy loop walks beyond t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/python-pillow/Pillow/commit/76869efdbbf2ad7dccd7536520fb61b7a00ab61e
- https://github.com/python-pillow/Pillow/releases/tag/13.0.0
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-462x-pgg6-55fp

### [CVE-2026-111065](https://github.com/aio-libs/aiohttp/commit/9dd8eaf4e31f1237ef2c1574a8c82a739fca5805)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-111065
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-20 02:17:03 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, Max-Age processing can overflow and skip closing a connection. An attacker can consequently exhaust the connection pool temporarily until garbage collection resolves the connections. This issue is fixed in version 3.14.4.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/aio-libs/aiohttp/commit/9dd8eaf4e31f1237ef2c1574a8c82a739fca5805
- https://github.com/aio-libs/aiohttp/releases/tag/v3.14.4
- https://github.com/aio-libs/aiohttp/security/advisories/GHSA-6cjc-53gc-5rqm

### [CVE-2026-111748](https://github.com/aio-libs/aiohttp/commit/6d4e7b01f9b951aa084a75d7356e907d4ee80411)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-111748
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-20 02:17:03 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, an attacker can send an absolute-form request that causes Request.scheme to use attacker-controlled request-target scheme data instead of the connection protocol. Applications that use Request.scheme for security decisions...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/aio-libs/aiohttp/commit/6d4e7b01f9b951aa084a75d7356e907d4ee80411
- https://github.com/aio-libs/aiohttp/releases/tag/v3.14.4
- https://github.com/aio-libs/aiohttp/security/advisories/GHSA-f9xw-jh8m-3mwq

### [CVE-2026-111750](https://github.com/aio-libs/aiohttp/commit/9b27347e61454d9f8ca2055f4c67a37dee336e83)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-111750
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-20 02:17:04 JST
- 更新日: 2026-10-20 05:55:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.4, the pure Python parser accepts ambiguous HTTP request framing. An unauthenticated attacker can consequently smuggle requests when an application uses AIOHTTP_NO_EXTENSIONS or otherwise runs without a standard wheel and an i...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/aio-libs/aiohttp/commit/9b27347e61454d9f8ca2055f4c67a37dee336e83
- https://github.com/aio-libs/aiohttp/releases/tag/v3.14.4
- https://github.com/aio-libs/aiohttp/security/advisories/GHSA-pqxq-w44r-73xw

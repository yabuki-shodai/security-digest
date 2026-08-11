# Backend CVE Summary (2026-08-12)

## Overview

- 取得日時: 2026-08-12 07:57:23 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 22
- Critical: 4
- High: 14
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-73080](https://github.com/seaweedfs/seaweedfs/commit/69da20bdaec923e5a43d8aa71bf3c0a2051fc019)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-73080
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-12 01:17:39 JST
- 更新日: 2026-08-12 01:17:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SeaweedFS is a distributed storage system. Prior to 4.24, VolumeServer.FetchAndWriteNeedle in weed/server/volume_grpc_remote.go fetches a caller-supplied remote endpoint through weed/remote_storage/s3/s3_storage_client.go and writes the response into a needle. The RPC performs no authentication and no target validation...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/seaweedfs/seaweedfs/commit/69da20bdaec923e5a43d8aa71bf3c0a2051fc019
- https://github.com/seaweedfs/seaweedfs/pull/9441
- https://github.com/seaweedfs/seaweedfs/releases/tag/4.24
- https://github.com/seaweedfs/seaweedfs/security/advisories/GHSA-87fv-vqqr-m4jr

### [CVE-2026-42142](https://github.com/baptisteArno/typebot.io/commit/91d2a986d942232b98c066fc460d7c48c04a464b)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-42142
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-12 01:17:31 JST
- 更新日: 2026-08-12 02:17:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: TypeBot is a chatbot builder tool. Prior to version 3.17.0, the `handleGetSheets` API handler (`POST /api/sheets/getSheets`) does not validate workspace membership, allowing any authenticated user to access and decrypt another workspace's Google Sheets OAuth credentials and retrieve spreadsheet data (sheet names, IDs,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/baptisteArno/typebot.io/commit/91d2a986d942232b98c066fc460d7c48c04a464b
- https://github.com/baptisteArno/typebot.io/pull/2467
- https://github.com/baptisteArno/typebot.io/releases/tag/v3.17.0
- https://github.com/baptisteArno/typebot.io/security/advisories/GHSA-7jr4-r73c-h4h9
- https://github.com/baptisteArno/typebot.io/security/advisories/GHSA-7jr4-r73c-h4h9

### [CVE-2026-48386](https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-48386
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-12 02:18:00 JST
- 更新日: 2026-08-12 03:17:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ColdFusion is affected by a Use of a Broken or Risky Cryptographic Algorithm vulnerability that could lead to disclosure of sensitive memory. An attacker could leverage this vulnerability to disclose sensitive information. Exploitation of this issue does not require user interaction.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html

### [CVE-2026-48495](https://github.com/baptisteArno/typebot.io/commit/c0ffd825e2f4ee2256a157fd085fb624dcede625)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-48495
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-12 01:17:32 JST
- 更新日: 2026-08-12 01:17:32 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: TypeBot is a chatbot builder tool. Prior to version 3.17.0, the Google Sheets OAuth callback decodes a base64-encoded JSON `state` parameter and trusts the embedded `workspaceId`, `typebotId`, `blockId`, and `redirectUrl` without cryptographic integrity protection or authorization checks. The callback route is authenti...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/baptisteArno/typebot.io/commit/c0ffd825e2f4ee2256a157fd085fb624dcede625
- https://github.com/baptisteArno/typebot.io/pull/2501
- https://github.com/baptisteArno/typebot.io/releases/tag/v3.17.0
- https://github.com/baptisteArno/typebot.io/security/advisories/GHSA-w789-9gxq-2xcj

### [CVE-2026-67180](https://github.com/google/turbinia/issues/1629)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-67180
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-12 01:17:34 JST
- 更新日: 2026-08-12 01:17:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Google Turbinia allows arbitrary command execution via worker tasks. An attacker with privileges to submit a processing request or influence an evidence path/name obtains code execution on the worker fleet. Fixed on 2026-07-10.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/google/turbinia/issues/1629
- https://github.com/google/turbinia/pull/1631
- https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-223-02.json
- https://www.cve.org/CVERecord?id=CVE-2026-67180

### [CVE-2026-72921](https://github.com/seaweedfs/seaweedfs/commit/05ed5c9ae8a2a45101b52b61d02f170d20d587ff)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-72921
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-12 00:17:38 JST
- 更新日: 2026-08-12 00:17:38 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SeaweedFS is a distributed storage system. Prior to 4.24, the weed/server/filer_server_handlers.go allowed_prefixes authorization check used strings.HasPrefix on raw path strings, so a filer JWT scoped to /tenant1 also authorized sibling paths such as /tenant1234, /tenant1-old, and /tenant1backup, enabling cross-tenant...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/seaweedfs/seaweedfs/commit/05ed5c9ae8a2a45101b52b61d02f170d20d587ff
- https://github.com/seaweedfs/seaweedfs/pull/9439
- https://github.com/seaweedfs/seaweedfs/releases/tag/4.24
- https://github.com/seaweedfs/seaweedfs/security/advisories/GHSA-gv5w-hfx8-8cwq

### [CVE-2026-54981](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-54981)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-54981
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-12 02:18:03 JST
- 更新日: 2026-08-12 05:17:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Inclusion of functionality from untrusted control sphere in Visual Studio Code - Python extension allows an unauthorized attacker to bypass a security feature locally.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-54981

### [CVE-2026-12571](https://www.manageengine.com/dns-dhcp-ipam/security-updates/security-updates.html)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-12571
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 02:17:46 JST
- 更新日: 2026-08-12 05:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An authentication bypass in ManageEngine DDI Central's password-reset workflow allows account takeover.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.manageengine.com/dns-dhcp-ipam/security-updates/security-updates.html

### [CVE-2026-17061](https://www.3ds.com/trust-center/security/security-advisories/cve-2026-17061)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-17061
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 00:17:27 JST
- 更新日: 2026-08-12 05:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A Deserialization of Untrusted Data vulnerability affecting SIMULIA Execution Engine from Release 2023 through Release 2026 could lead to an unauthenticated remote code execution.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.3ds.com/trust-center/security/security-advisories/cve-2026-17061

### [CVE-2026-50516](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50516)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-50516
- 関連キーワード: kubernetes
- 影響製品: -
- 公開日: 2026-08-12 02:18:02 JST
- 更新日: 2026-08-12 06:17:37 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Missing authentication for critical function in Microsoft Azure Kubernetes Service allows an unauthorized attacker to elevate privileges over a network.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-50516

### [CVE-2026-73077](https://github.com/vim/vim/commit/c5a82fe013e73c98004ad7cd4f906b1ad1ed610e)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-73077
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 01:17:39 JST
- 更新日: 2026-08-12 04:18:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Vim is an open source, command line text editor. Prior to 9.2.0839, the runtime/ftplugin/sh.vim, runtime/ftplugin/zsh.vim, and runtime/ftplugin/ps1.vim filetype plugins pass attacker-controlled Visual-mode selections from K through keywordprg commands without safely separating shell arguments. fnameescape() and PATH_ES...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vim/vim/commit/c5a82fe013e73c98004ad7cd4f906b1ad1ed610e
- https://github.com/vim/vim/security/advisories/GHSA-r5v6-q6j8-8qw2

### [CVE-2026-73078](https://github.com/vim/vim/commit/29c6fd090d4520592f8be7d9ec81190edf25ef69)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-73078
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 01:17:39 JST
- 更新日: 2026-08-12 02:19:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Vim is an open source, command line text editor. Prior to 9.2.0840, runtime/plugin/netrwPlugin.vim loads netrw and runtime/pack/dist/opt/netrw/autoload/netrw.vim constructs Bookmarks, History, and Targets menu entries by interpolating attacker-controlled directory paths into executed :menu commands. s:NetrwBookmarkMenu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vim/vim/commit/29c6fd090d4520592f8be7d9ec81190edf25ef69
- https://github.com/vim/vim/security/advisories/GHSA-rcr7-f3wr-22r2

### [CVE-2026-18635](http://docs.velociraptor.app/announcements/advisories/cve-2026-18635/)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-18635
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 00:17:28 JST
- 更新日: 2026-08-12 00:17:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Velociraptor's VQL has a query() plugin which allows running a VQL query in a different org or user context. To be able to run as a different user, the calling user needs to have the IMPERSONATE permission (usually only given to administrators). Velociraptor versions prior to 0.77.2 evaluate this permission against the...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- http://docs.velociraptor.app/announcements/advisories/cve-2026-18635/

### [CVE-2026-19546](https://access.redhat.com/security/cve/CVE-2026-19546)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-19546
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 01:17:31 JST
- 更新日: 2026-08-12 01:17:31 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A flaw was found in DBI. This is a fix for a partial fix for CVE-2026-14380 for RHEL 9.8.z and 10.2.z. For a detailed Statement, Description and Mitigation please reffer to the original https://access.redhat.com/security/cve/cve-2026-19546.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-19546
- https://bugzilla.redhat.com/show_bug.cgi?id=2513963

### [CVE-2026-53416](https://www.zoom.com/en/trust/security-bulletin/zsb-26017)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-53416
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 01:17:32 JST
- 更新日: 2026-08-12 02:18:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Path traversal in Zoom VDI Client and Plugins may allow an authenticated user to conduct information disclosure via local access.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.zoom.com/en/trust/security-bulletin/zsb-26017

### [CVE-2026-54984](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-54984)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-54984
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 02:18:03 JST
- 更新日: 2026-08-12 07:17:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Heap-based buffer overflow in Windows Imaging Component allows an unauthorized attacker to execute code locally.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-54984

### [CVE-2026-56179](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-56179)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-56179
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 02:18:04 JST
- 更新日: 2026-08-12 03:53:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Origin validation error in Windows Network Address Translation (NAT) allows an unauthorized attacker to perform spoofing over an adjacent network.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-56179

### [CVE-2026-72922](https://github.com/Significant-Gravitas/AutoGPT/commit/646dd5b8cfad1206e92ec7bcc3b8312657e2a92e)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-72922
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 00:17:38 JST
- 更新日: 2026-08-12 00:17:38 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: AutoGPT is a workflow automation platform for creating, deploying, and managing continuous artificial intelligence agents. Prior to 0.6.70, AutoGPT's autogpt_platform/backend/backend/api/features/integrations/router.py webhook_ingress_generic route selected get_webhook_manager(provider) from the untrusted provider URL...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Significant-Gravitas/AutoGPT/commit/646dd5b8cfad1206e92ec7bcc3b8312657e2a92e
- https://github.com/Significant-Gravitas/AutoGPT/pull/13559
- https://github.com/Significant-Gravitas/AutoGPT/releases/tag/autogpt-platform-beta-v0.6.70
- https://github.com/Significant-Gravitas/AutoGPT/security/advisories/GHSA-349p-3c3r-8mjr

### [CVE-2026-73066](https://github.com/tesseract-ocr/tesseract/commit/2f4d2f4bf45c363785d7bf1da29b6628f8939a72)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-73066
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 00:17:38 JST
- 更新日: 2026-08-12 01:17:37 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Tesseract is an open source OCR engine. Prior to 5.5.3, a crafted .traineddata LSTM model component loaded through Tesseract's deserializer can cause an unchecked signed integer multiplication in Convolve::DeSerialize in src/lstm/convolve.cpp to wrap the convolution output-channel count, undersizing the forward-pass ou...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/tesseract-ocr/tesseract/commit/2f4d2f4bf45c363785d7bf1da29b6628f8939a72
- https://github.com/tesseract-ocr/tesseract/pull/4588
- https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.3
- https://github.com/tesseract-ocr/tesseract/security/advisories/GHSA-7j76-5rq5-5jg8

### [CVE-2026-73067](https://github.com/tesseract-ocr/tesseract/commit/55287a94b8044c05ce3fd10f5aca6ebbd238e518)

> **Backend** / **MEDIUM** / CVSS: **6.7** / KEV: **no**

- タイトル: CVE-2026-73067
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 00:17:38 JST
- 更新日: 2026-08-12 01:17:37 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Tesseract is an open source OCR engine. Prior to 5.5.3, a crafted .traineddata model loaded through TessBaseAPI::Init can cause SquishedDawg::read_squished_dawg in src/dict/dawg.cpp to accept an unterminated forward-edge run, after which SquishedDawg::Load calls num_forward_edges(0) and last_edge in src/dict/dawg.h rea...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/tesseract-ocr/tesseract/commit/55287a94b8044c05ce3fd10f5aca6ebbd238e518
- https://github.com/tesseract-ocr/tesseract/commit/82727cc11c34eaf1249af002d69f6bbae70993b9
- https://github.com/tesseract-ocr/tesseract/issues/4580
- https://github.com/tesseract-ocr/tesseract/pull/4581
- https://github.com/tesseract-ocr/tesseract/releases/tag/5.5.3

### [CVE-2026-20770](https://intel.com/content/www/us/en/security-center/advisory/intel-sa-01460.html)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-20770
- 関連キーワード: kubernetes
- 影響製品: -
- 公開日: 2026-08-12 02:17:52 JST
- 更新日: 2026-08-12 02:17:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Protection mechanism failure for some Cluster Management Toolkit for Kubernetes software before version v0.8.5 within Ring 3: User Applications may allow an escalation of privilege. System software adversary with a privileged user combined with a low complexity attack may enable escalation of privilege. This result may...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://intel.com/content/www/us/en/security-center/advisory/intel-sa-01460.html

### [CVE-2026-27765](https://intel.com/content/www/us/en/security-center/advisory/intel-sa-01487.html)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-27765
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-12 02:17:56 JST
- 更新日: 2026-08-12 02:17:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Improper input validation for some vLLM Hardware Plugin for Intel(R) Gaudi(R) software before version 0.16.0 within Ring 3: User Applications may allow a denial of service. Authorized adversary with an authenticated user combined with a low complexity attack may enable denial of service. This result may potentially occ...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://intel.com/content/www/us/en/security-center/advisory/intel-sa-01487.html

# Backend CVE Summary (2026-08-14)

## Overview

- 取得日時: 2026-08-14 07:57:12 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 15
- Critical: 1
- High: 6
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-67614](https://cyberpanel.net/KnowledgeBase/home/change-logs/)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-67614
- 関連キーワード: fastapi
- 影響製品: -
- 公開日: 2026-08-14 03:18:08 JST
- 更新日: 2026-08-14 03:18:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CyberPanel before 3.0.0 contains a hard-coded JWT secret vulnerability in the WebTerminal FastAPI SSH service that allows unauthenticated remote attackers to forge valid authentication tokens and obtain an interactive root shell via WebSocket on port 8888. Attackers can craft a forged JWT signed with the hardcoded secr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cyberpanel.net/KnowledgeBase/home/change-logs/
- https://github.com/usmannasir/cyberpanel/issues/1858
- https://www.vulncheck.com/advisories/cyberpanel-hard-coded-jwt-secret-authentication-bypass-via-webterminal

### [CVE-2026-73555](https://github.com/vllm-project/vllm/commit/e87521626febe2763f997691d1599de4175f4324)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-73555
- 関連キーワード: python, fastapi, gin
- 影響製品: -
- 公開日: 2026-08-14 00:20:17 JST
- 更新日: 2026-08-14 00:20:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: vLLM is an inference and serving engine for large language models. Prior to 0.26.0, the validation_exception_handler in vllm/entrypoints/openai/server_utils.py converts FastAPI RequestValidationError objects with str(exc), and sanitize_message in vllm/entrypoints/utils.py does not remove traceback-style file paths, all...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vllm-project/vllm/commit/e87521626febe2763f997691d1599de4175f4324
- https://github.com/vllm-project/vllm/pull/46415
- https://github.com/vllm-project/vllm/releases/tag/v0.26.0
- https://github.com/vllm-project/vllm/security/advisories/GHSA-hwrm-c4cx-rf4j

### [CVE-2026-73652](https://github.com/vantage6/vantage6/security/advisories/GHSA-47w6-gwp4-w6vc)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-73652
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-14 04:17:38 JST
- 更新日: 2026-08-14 05:17:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: vantage6 is an open-source infrastructure for privacy preserving analysis. In version 5.0.2 and earlier, the algorithm-store edit permission lacks an ownership check, allowing one algorithm developer to alter another developer's algorithm while it is pending or under review. The attacker can change metadata including t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vantage6/vantage6/security/advisories/GHSA-47w6-gwp4-w6vc

### [CVE-2026-16867](https://www.ibm.com/support/pages/node/7283573)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-16867
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-14 05:17:15 JST
- 更新日: 2026-08-14 05:36:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: IBM i 7.6, 7.5, 7.4, and 7.3 could allow a remote attacker to access server resources with the privileges of an authenticated user due to improper authentication during NTLM session negotiation.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7283573

### [CVE-2026-70453](https://github.com/RsyncProject/rsync/releases/tag/v3.5.0)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-70453
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-14 00:19:58 JST
- 更新日: 2026-08-14 03:18:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: rsync before 3.5.0 contains an algorithmic complexity vulnerability in the hash_search() function that allows a remote attacker to cause a denial of service by delivering a carefully constructed file list. A sender can exploit the quadratic-time worst-case behavior in hash lookups to exhaust receiver CPU resources with...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/RsyncProject/rsync/releases/tag/v3.5.0
- https://github.com/RsyncProject/rsync/security/advisories/GHSA-8x5r-mjx8-83hv
- https://www.vulncheck.com/advisories/rsync-algorithmic-complexity-dos-via-hash-search

### [CVE-2026-73509](https://github.com/OpenListTeam/OpenList/commit/651da18da4c647d96648d4bb64462baac1c37e04)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-73509
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-14 00:20:17 JST
- 更新日: 2026-08-14 01:19:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenList a file list program that supports multiple storage. Prior to 4.2.4, the authenticated /api/fs/batch_rename handler in server/handles/fsbatch.go authorizes only the source directory produced by user.JoinPath(req.SrcDir) and validates renameObject.NewName with checkRelativePath, but does not validate attacker-co...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/OpenListTeam/OpenList/commit/651da18da4c647d96648d4bb64462baac1c37e04
- https://github.com/OpenListTeam/OpenList/releases/tag/v4.2.4
- https://github.com/OpenListTeam/OpenList/security/advisories/GHSA-95cv-r8x4-vh75
- https://github.com/OpenListTeam/OpenList/security/advisories/GHSA-95cv-r8x4-vh75

### [CVE-2026-73505](https://github.com/JanDeDobbeleer/oh-my-posh/commit/88ddbe0b0a4dd13cc345996108c9869493f2c690)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-73505
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-08-14 00:20:16 JST
- 更新日: 2026-08-14 01:19:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Oh My Posh is the most customisable and low-latency cross platform/shell prompt renderer. Prior to 29.35.1, the setStyle() function in src/segments/path.go passed pt.Path, which includes raw folder names, to template.Render, whose function map exposes cmd, so an attacker-controlled directory name containing a Go templa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/JanDeDobbeleer/oh-my-posh/commit/88ddbe0b0a4dd13cc345996108c9869493f2c690
- https://github.com/JanDeDobbeleer/oh-my-posh/pull/7711
- https://github.com/JanDeDobbeleer/oh-my-posh/releases/tag/v29.35.1
- https://github.com/JanDeDobbeleer/oh-my-posh/security/advisories/GHSA-6xj8-qv9j-xcjq
- https://github.com/JanDeDobbeleer/oh-my-posh/security/advisories/GHSA-6xj8-qv9j-xcjq

### [CVE-2026-49820](https://github.com/getprobo/probo/blob/main/SECURITY_NOTES.md)

> **Backend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-49820
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-14 00:19:41 JST
- 更新日: 2026-08-14 00:19:41 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Probo is a self-hostable governance, risk, and compliance (GRC) platform built for engineering and security teams. Probo's `saferedirect` package validates redirect URLs used across authentication flows (OIDC, SAML, session transfer, OAuth connectors, and trust-center magic links). Prior to version 0.19.3.1, the valida...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/getprobo/probo/blob/main/SECURITY_NOTES.md
- https://github.com/getprobo/probo/security/advisories/GHSA-x7qq-m748-8p2c

### [CVE-2026-73562](https://github.com/Automattic/mongoose/commit/35a3f33bc9a0a28671f99e3c5010000425650d0f)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-73562
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-08-14 03:18:18 JST
- 更新日: 2026-08-14 03:18:18 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Mongoose is a MongoDB object modeling tool designed to work in an asynchronous environment. Prior to 6.13.10, 7.8.10, 8.24.1, and 9.7.2, passing a user-controlled update such as MyModel.updateOne(filter, req.body) can exploit Mongoose update casting with a __proto__.x dotted path under $set. Schema.prototype.path and S...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Automattic/mongoose/commit/35a3f33bc9a0a28671f99e3c5010000425650d0f
- https://github.com/Automattic/mongoose/commit/7285466b860d3b511f8d07b2ab72656703ee707a
- https://github.com/Automattic/mongoose/commit/953d085bee5a16b5d6c5af33a156e6314d6d9a45
- https://github.com/Automattic/mongoose/commit/fab793b747131c68927888cba41cf3e6d6593740
- https://github.com/Automattic/mongoose/security/advisories/GHSA-664h-wqgq-64gw

### [CVE-2026-73564](https://github.com/fatedier/frp/commit/7dc7be930e2452ae93fd32f2a77f8c6fcd0b652b)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-73564
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-14 03:18:18 JST
- 更新日: 2026-08-14 03:18:18 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: frp is a fast reverse proxy. From 0.53.0 until 0.70.1, frp's optional SSH Tunnel Gateway in pkg/ssh/server.go parses an SSH exec channel request by adding 4 to an attacker-controlled four-byte big-endian length. A length of 0xFFFFFFFF makes the uint32 addition wrap to 3, defeats the payload bounds check, and causes pay...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/fatedier/frp/commit/7dc7be930e2452ae93fd32f2a77f8c6fcd0b652b
- https://github.com/fatedier/frp/pull/5428
- https://github.com/fatedier/frp/releases/tag/v0.70.1
- https://github.com/fatedier/frp/security/advisories/GHSA-26gq-p25f-99cp
- https://github.com/fatedier/frp/security/advisories/GHSA-26gq-p25f-99cp

### [CVE-2026-19730](https://access.redhat.com/security/cve/CVE-2026-19730)

> **Backend** / **MEDIUM** / CVSS: **4.2** / KEV: **no**

- タイトル: CVE-2026-19730
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-14 03:17:25 JST
- 更新日: 2026-08-14 04:17:19 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The 'podman quadlet install --replace' command opens the existing destination file with O_CREATE|O_WRONLY but omits O_TRUNC. When the initial reflink copy attempt fails (common on non-reflink-capable filesystems including many RHEL default XFS configurations), the fallback in ReflinkOrCopy uses io.Copy which performs a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-19730
- https://bugzilla.redhat.com/show_bug.cgi?id=2508234
- https://github.com/podman-container-tools/podman/issues/29013
- https://github.com/podman-container-tools/podman/security/advisories/GHSA-fx76-2j3w-2mx6
- https://github.com/podman-container-tools/podman/issues/29013

### [CVE-2026-73506](https://github.com/JanDeDobbeleer/oh-my-posh/commit/edcf3c88f3fb582e84358b385c49d33d04c04224)

> **Backend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-73506
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-14 00:20:17 JST
- 更新日: 2026-08-14 00:20:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Oh My Posh is the most customisable and low-latency cross platform/shell prompt renderer. Prior to 29.35.1, write(s rune) in src/terminal/writer.go emitted attacker-controlled current directory names and Git metadata, including Commit.Subject, Commit.Author.Name, Commit.Author.Email, and RawUpstreamURL, without removin...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/JanDeDobbeleer/oh-my-posh/commit/edcf3c88f3fb582e84358b385c49d33d04c04224
- https://github.com/JanDeDobbeleer/oh-my-posh/pull/7711
- https://github.com/JanDeDobbeleer/oh-my-posh/releases/tag/v29.35.1
- https://github.com/JanDeDobbeleer/oh-my-posh/security/advisories/GHSA-fwjx-9p69-h25h

### [CVE-2026-56443](https://blog.gitea.com/gitea-1.27.0-is-released/)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-56443
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-14 02:17:25 JST
- 更新日: 2026-08-14 02:17:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Token public-only scope bypassed on Limited-visibility owners (Repository + Package categories) — residual after CVE-2026-25714 / PR #37118
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://blog.gitea.com/gitea-1.27.0-is-released/
- https://github.com/go-gitea/gitea/releases/tag/v1.27.0
- https://github.com/go-gitea/gitea/security/advisories/GHSA-7p4h-3gxq-x3h3

### [CVE-2026-58440](https://blog.gitea.com/gitea-1.27.0-is-released/)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-58440
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-14 02:17:28 JST
- 更新日: 2026-08-14 02:17:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Webhooks created by a collaborator keep firing after their repo access is revoked → ongoing real-time exfiltration of private repo content (incomplete revocation cleanup in `DeleteCollaboration`)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://blog.gitea.com/gitea-1.27.0-is-released/
- https://github.com/go-gitea/gitea/releases/tag/v1.27.0
- https://github.com/go-gitea/gitea/security/advisories/GHSA-66m4-5jjr-2rg5

### [CVE-2026-58507](https://blog.gitea.com/gitea-1.27.0-is-released/)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-58507
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-14 02:17:28 JST
- 更新日: 2026-08-14 02:17:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Private Repository Existence Disclosure via go-get Meta Endpoint
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://blog.gitea.com/gitea-1.27.0-is-released/
- https://github.com/go-gitea/gitea/releases/tag/v1.27.0
- https://github.com/go-gitea/gitea/security/advisories/GHSA-p4mj-98mv-xq26

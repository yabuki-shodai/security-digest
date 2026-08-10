# Backend CVE Summary (2026-08-11)

## Overview

- 取得日時: 2026-08-11 07:52:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 23
- Critical: 14
- High: 5
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-72869](https://github.com/Dokploy/dokploy/commit/ccd2e83c57d99f725220d37e0152270e0827d71b)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-72869
- 関連キーワード: go, node.js, postgresql, mysql, mongodb, docker
- 影響製品: -
- 公開日: 2026-08-11 04:17:35 JST
- 更新日: 2026-08-11 04:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the backup.restoreBackupWithLogs tRPC subscription passes the databaseName parameter to restore builders in packages/server/src/utils/restore/utils.ts, where PostgreSQL, MariaDB, MySQL, and MongoDB commands embed the value in nested shell...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/ccd2e83c57d99f725220d37e0152270e0827d71b
- https://github.com/Dokploy/dokploy/pull/4862
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-f7mp-9jfp-mjrr

### [CVE-2026-72862](https://github.com/Dokploy/dokploy/commit/b24202e69b244f0ece8d2f56e99cad9bb5e1a248)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-72862
- 関連キーワード: go, mysql, redis, docker
- 影響製品: -
- 公開日: 2026-08-11 03:18:53 JST
- 更新日: 2026-08-11 03:18:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the mariadb.ts, mongo.ts, mysql.ts, postgres.ts, redis.ts, and libsql.ts Dokploy database service deployment functions pass user-controlled dockerImage fields unquoted into docker pull ${dockerImage} shell commands on the remote-server cod...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/b24202e69b244f0ece8d2f56e99cad9bb5e1a248
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-6jrh-8qmg-jj3p

### [CVE-2026-47754](https://github.com/NCEAS/metacat/commit/07e034b2bbf7029e28af32f472f4d70ea6b5ab1b)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-47754
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-11 01:19:47 JST
- 更新日: 2026-08-11 04:17:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Metacat is data repository software that helps researchers preserve, share, and discover data. Versions 2.x through 2.19.1 and all 1.x versions contain an unauthenticated path traversal in the `archiveEntryName` parameter of the `action=read` endpoint that is part of the original 1.x Metacat API. `ArchiveHandler.readAr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/NCEAS/metacat/commit/07e034b2bbf7029e28af32f472f4d70ea6b5ab1b
- https://github.com/NCEAS/metacat/issues/1365
- https://github.com/NCEAS/metacat/pull/1713
- https://github.com/NCEAS/metacat/security/advisories/GHSA-m852-f287-7cgw

### [CVE-2026-72733](https://github.com/Dokploy/dokploy/commit/8539a5c82f47eb3fd1464b574eb034c6dc2a6bbd)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-72733
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-11 03:18:51 JST
- 更新日: 2026-08-11 06:17:24 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the backup.restoreBackupWithLogs tRPC subscription builds database restore shell pipelines from the user-controlled databaseName and backupFile fields without safely separating them from shell syntax. packages/server/src/utils/restore/util...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/8539a5c82f47eb3fd1464b574eb034c6dc2a6bbd
- https://github.com/Dokploy/dokploy/commit/ccd2e83c57d99f725220d37e0152270e0827d71b
- https://github.com/Dokploy/dokploy/commit/eeb6e7b8ea88e4b4b1fac8460755464100516ac9
- https://github.com/Dokploy/dokploy/pull/4862
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13

### [CVE-2026-72881](https://github.com/Dokploy/dokploy/commit/ccd2e83c57d99f725220d37e0152270e0827d71b)

> **Backend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-72881
- 関連キーワード: go, postgresql, mysql, mongodb
- 影響製品: -
- 公開日: 2026-08-11 05:17:34 JST
- 更新日: 2026-08-11 05:17:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, database backup and restore command builders in packages/server/src/utils/backups/utils.ts and packages/server/src/utils/restore/utils.ts interpolate database names, usernames, and passwords into nested shell command strings passed to chil...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/ccd2e83c57d99f725220d37e0152270e0827d71b
- https://github.com/Dokploy/dokploy/pull/4862
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-qc73-mp78-4833
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-qc73-mp78-4833

### [CVE-2026-72723](https://github.com/discourse/discourse/commit/0248e9ca82d0493037a9ca04d73904ccfad795f9)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-72723
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-11 01:19:49 JST
- 更新日: 2026-08-11 06:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Discourse is an open-source discussion platform. Prior to 2026.1.6, 2026.5.2, 2026.6.1, and 2026.7.0, SiteSerializer.anonymous_default_navigation_menu_tags serializes tags from SiteSetting.default_navigation_menu_tags without applying DiscourseTagging.filter_visible for the anonymous viewer. An unauthenticated user can...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/discourse/discourse/commit/0248e9ca82d0493037a9ca04d73904ccfad795f9
- https://github.com/discourse/discourse/commit/03444ddb74d535dda557350f4c5800a6ec2669d7
- https://github.com/discourse/discourse/commit/900f51c147913f667e64484c2f2dd48c723314ac
- https://github.com/discourse/discourse/commit/da84c677213cac3b024e753f180f45472b89efde
- https://github.com/discourse/discourse/pull/42091

### [CVE-2026-18621](https://access.redhat.com/security/cve/CVE-2026-18621)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-18621
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-11 06:17:20 JST
- 更新日: 2026-08-11 06:17:20 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A flaw was found in Data Science Pipelines (DSP). An attacker with namespace editor privileges can bypass security hardening by submitting a malicious Argo Workflow through the V1 API path. This allows the API server to create pods with elevated privileges, acting as a 'confused deputy' on behalf of the attacker. Succe...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-18621
- https://bugzilla.redhat.com/show_bug.cgi?id=2510327

### [CVE-2026-72718](https://github.com/aaif-goose/goose/commit/f8b5b7ba1fe6d006ccf6942f6b85a1bae985a2de)

> **Backend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-72718
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-11 01:19:48 JST
- 更新日: 2026-08-11 02:17:36 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: goose is general-purpose AI agent that runs on your machine. Prior to 1.44.0, the `goose review` command runs the system `git` executable to gather the diff for review without stripping attacker-controlled Git configuration. A malicious repository whose `.git/config` sets [`core] fsmonitor = <command>` causes Git to ex...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/aaif-goose/goose/commit/f8b5b7ba1fe6d006ccf6942f6b85a1bae985a2de
- https://github.com/aaif-goose/goose/releases/tag/v1.44.0
- https://github.com/aaif-goose/goose/security/advisories/GHSA-r5pp-p5r8-466r
- https://github.com/aaif-goose/goose/security/advisories/GHSA-r5pp-p5r8-466r

### [CVE-2026-72863](https://github.com/Dokploy/dokploy/commit/68f5afae42fca353dcb3d3bc6219ffe9e168cb91)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-72863
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 04:17:34 JST
- 更新日: 2026-08-11 06:17:24 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, Dokploy's WebSocket handlers (in-app terminals and log streamers) authenticate the session but never authorize it. They establish who the user is via validateRequest() and then proceed without consulting the role/permission model that ever...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/68f5afae42fca353dcb3d3bc6219ffe9e168cb91
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-7r6p-v9gw-pwc8
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-7r6p-v9gw-pwc8

### [CVE-2026-72902](https://github.com/Dokploy/dokploy/commit/d3f522b7a6f5100fc0fc0bff5851e48d11d459e2)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-72902
- 関連キーワード: gin, docker
- 影響製品: -
- 公開日: 2026-08-11 05:17:35 JST
- 更新日: 2026-08-11 05:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, Dokploy allows an authenticated user to execute arbitrary commands on a local or SSH-connected target server because registry.testRegistry and registry.testRegistryById in apps/dokploy/server/api/routers/registry.ts interpolate the passwor...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/d3f522b7a6f5100fc0fc0bff5851e48d11d459e2
- https://github.com/Dokploy/dokploy/pull/4875
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-w6r4-f26v-8g36

### [CVE-2026-72736](https://github.com/Dokploy/dokploy/commit/df2779eaeb4a58f0c85d4caa713c776c790fa708)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-72736
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 03:18:52 JST
- 更新日: 2026-08-11 03:18:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, Dokploy passes user-controlled values directly into shell commands via unquoted template literal interpolation in the registry credential testing and Docker Swarm cluster management endbpoints. Both endpoints have a safe local code path (u...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/df2779eaeb4a58f0c85d4caa713c776c790fa708
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-4mfc-grxw-6858

### [CVE-2026-72864](https://github.com/Dokploy/dokploy/commit/68f5afae42fca353dcb3d3bc6219ffe9e168cb91)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-72864
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 04:17:35 JST
- 更新日: 2026-08-11 04:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the local branch of /docker-container-terminal in apps/dokploy/server/wss/docker-container-terminal.ts authenticates with validateRequest but does not authorize the attacker-controlled containerId against the caller's role, organization, o...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/68f5afae42fca353dcb3d3bc6219ffe9e168cb91
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-899j-cjwp-v4gw

### [CVE-2026-72865](https://github.com/Dokploy/dokploy/commit/d48037a80203bb0ecaec4f5653aef75fcfdb656d)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-72865
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 04:17:35 JST
- 更新日: 2026-08-11 04:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the compose.update operation stores an unvalidated composePath that packages/server/src/utils/builders/compose.ts and packages/server/src/services/compose.ts interpolate into docker compose -f, docker stack deploy -c, and touch shell comma...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/d48037a80203bb0ecaec4f5653aef75fcfdb656d
- https://github.com/Dokploy/dokploy/pull/4863
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-8r5w-vqjr-8c44

### [CVE-2026-72868](https://github.com/Dokploy/dokploy/commit/eeb6e7b8ea88e4b4b1fac8460755464100516ac9)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-72868
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 04:17:35 JST
- 更新日: 2026-08-11 04:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, apps/dokploy/server/api/routers/destination.ts interpolates the accessKey, secretAccessKey, region, endpoint, provider, and bucket fields from destination.testConnection into an rclone ls command executed through child_process.exec. The `w...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/eeb6e7b8ea88e4b4b1fac8460755464100516ac9
- https://github.com/Dokploy/dokploy/pull/4873
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-f6x8-vfwh-8hjr

### [CVE-2026-72876](https://github.com/Dokploy/dokploy/commit/5563699f71b2058b49eebdfd66c6c3dbd92ede9c)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-72876
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 05:17:33 JST
- 更新日: 2026-08-11 05:17:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, swarm.getNodes, swarm.getNodeInfo, swarm.getNodeApps, and swarm.getAppInfos in apps/dokploy/server/api/routers/swarm.ts accept another organization’s serverId without an activeOrganizationId ownership check, and getNodeInfo in packages/ser...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/5563699f71b2058b49eebdfd66c6c3dbd92ede9c
- https://github.com/Dokploy/dokploy/pull/4858
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-jj6h-388v-9rwm
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-jj6h-388v-9rwm

### [CVE-2026-72877](https://github.com/Dokploy/dokploy/commit/cba0b253c7de4157dd932de7f16a2ad247c7cee9)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-72877
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 05:17:34 JST
- 更新日: 2026-08-11 05:17:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the dockerImage field is interpolated without quoting into shell commands in buildRemoteDocker() in packages/server/src/utils/providers/docker.ts and is validated only as an optional string. An authenticated user with application create or...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/cba0b253c7de4157dd932de7f16a2ad247c7cee9
- https://github.com/Dokploy/dokploy/pull/4860
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-jxxj-gmpx-h5rj

### [CVE-2026-72879](https://github.com/Dokploy/dokploy/commit/1f4f94042f1d874349c42d8ae7fee51346cd086e)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-72879
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 05:17:34 JST
- 更新日: 2026-08-11 05:17:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.8, the getRegistryCommands() function in packages/server/src/utils/cluster/upload.ts interpolates registry.password and registry.registryUrl directly into a shell command without escaping. An authenticated user with project access can configur...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/1f4f94042f1d874349c42d8ae7fee51346cd086e
- https://github.com/Dokploy/dokploy/pull/4579
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.8
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-prwq-2mcm-mvhr

### [CVE-2026-72901](https://github.com/Dokploy/dokploy/commit/d629faebc6dcb9d4785f84bf30b2b285f9f59379)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-72901
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 05:17:35 JST
- 更新日: 2026-08-11 05:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, Dokploy allows an authenticated low-privilege member to execute arbitrary commands on the control-plane host because the volumeName field accepted by volumeBackup.create and volumeBackup.runManually is interpolated without quoting in packa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/d629faebc6dcb9d4785f84bf30b2b285f9f59379
- https://github.com/Dokploy/dokploy/pull/4873
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-w223-vw9m-4f9c

### [CVE-2026-72883](https://github.com/Dokploy/dokploy/commit/1bc76e9e5b8a9acd14a58cd8a1828c25918f162e)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-72883
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 05:17:35 JST
- 更新日: 2026-08-11 05:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the WebSocket handlers in apps/dokploy/server/wss/terminal.ts, apps/dokploy/server/wss/docker-container-terminal.ts, apps/dokploy/server/wss/docker-container-logs.ts, and apps/dokploy/server/wss/docker-stats.ts validate organization member...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/1bc76e9e5b8a9acd14a58cd8a1828c25918f162e
- https://github.com/Dokploy/dokploy/commit/68f5afae42fca353dcb3d3bc6219ffe9e168cb91
- https://github.com/Dokploy/dokploy/pull/4865
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-qf9j-c9p4-r4xp

### [CVE-2026-72870](https://github.com/Dokploy/dokploy/commit/cba0b253c7de4157dd932de7f16a2ad247c7cee9)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-72870
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 04:17:35 JST
- 更新日: 2026-08-11 04:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the buildRemoteDocker() function in packages/server/src/utils/providers/docker.ts interpolates the application-controlled dockerImage value directly into a docker pull shell command. An authenticated user with project access can set a craf...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/cba0b253c7de4157dd932de7f16a2ad247c7cee9
- https://github.com/Dokploy/dokploy/pull/4860
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-g9cg-4mmj-mh7p

### [CVE-2026-72884](https://github.com/Dokploy/dokploy/commit/d48037a80203bb0ecaec4f5653aef75fcfdb656d)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-72884
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 05:17:35 JST
- 更新日: 2026-08-11 05:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, sanitizeCommand in packages/server/src/utils/builders/compose.ts only trims whitespace and strips surrounding quotes from compose.command before exportEnvCommand and docker command interpolation, allowing an authenticated user who can upda...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/d48037a80203bb0ecaec4f5653aef75fcfdb656d
- https://github.com/Dokploy/dokploy/pull/4863
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-qh6h-669j-77rw

### [CVE-2026-72739](https://github.com/Dokploy/dokploy/commit/d48037a80203bb0ecaec4f5653aef75fcfdb656d)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-72739
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 03:18:52 JST
- 更新日: 2026-08-11 04:17:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, the createCommand() function constructs shell commands by interpolating compose service names and configuration into bash command strings. When a compose with a maliciously crafted name or service definition is deployed, the shell metachar...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/d48037a80203bb0ecaec4f5653aef75fcfdb656d
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-5xv2-7f8w-9j5c
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-5xv2-7f8w-9j5c

### [CVE-2026-72885](https://github.com/Dokploy/dokploy/commit/cba0b253c7de4157dd932de7f16a2ad247c7cee9)

> **Backend** / **NONE** / CVSS: **0.0** / KEV: **no**

- タイトル: CVE-2026-72885
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-11 05:17:35 JST
- 更新日: 2026-08-11 05:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dokploy is a free, self-hostable Platform as a Service (PaaS). Prior to 0.29.13, dockerContextPath accepted by apps/dokploy/components/dashboard/application/build/show.tsx flows through getDockerContextPath in packages/server/src/utils/filesystem/directory.ts into the unquoted cd command in packages/server/src/utils/bu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Dokploy/dokploy/commit/cba0b253c7de4157dd932de7f16a2ad247c7cee9
- https://github.com/Dokploy/dokploy/pull/4860
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-qjrc-g63x-qhp9

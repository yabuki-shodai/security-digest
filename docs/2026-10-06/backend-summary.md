# Backend CVE Summary (2026-10-06)

## Overview

- 取得日時: 2026-10-06 11:14:16 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 15
- Critical: 6
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-105638](https://github.com/makeplane/plane/commit/b1c78fe4c832e188454840eb38fd20cd05ef8b0a)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-105638
- 関連キーワード: django, go, gin, redis
- 影響製品: -
- 公開日: 2026-10-06 04:17:18 JST
- 更新日: 2026-10-06 04:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Plane is an open-source project management tool. Prior to 1.4.0, Plane's magic-code email login uses a six-digit numeric OTP with approximately 20 bits of entropy. The verifier has no per-code failed-attempt counter, and an incorrect code does not increment a counter, invalidate the Redis entry, or lock the email addre...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/makeplane/plane/commit/b1c78fe4c832e188454840eb38fd20cd05ef8b0a
- https://github.com/makeplane/plane/pull/9130
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-mqjv-rwgv-4gxq
- https://github.com/makeplane/plane/security/advisories/GHSA-mqjv-rwgv-4gxq

### [CVE-2026-105641](https://github.com/makeplane/plane/commit/1acc69e816a9a8789032bf711aa9a3c12fcd285c)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-105641
- 関連キーワード: django, go, docker
- 影響製品: -
- 公開日: 2026-10-06 04:17:18 JST
- 更新日: 2026-10-06 04:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Plane is an open-source project management tool. Prior to 1.4.0, the deployments/aio/community/ and deployments/cli/community/ manifests provide fixed, publicly known SECRET_KEY and LIVE_SERVER_SECRET_KEY defaults that remain active when operators do not override them. The top-level setup.sh randomizes secrets only for...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/makeplane/plane/commit/1acc69e816a9a8789032bf711aa9a3c12fcd285c
- https://github.com/makeplane/plane/pull/9291
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-cmwv-pjmw-8483

### [CVE-2026-105640](https://github.com/makeplane/plane/commit/b91b61c379908d9e451613dbca23fc3803e926d2)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-105640
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-06 04:17:18 JST
- 更新日: 2026-10-06 04:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Plane is an open-source project management tool. Prior to 1.4.0, Plane trusts email addresses returned by Gitea OAuth and by self-managed GitLab OAuth deployments where email confirmation is disabled, without verifying that the provider authenticated ownership of the address. An attacker can set an OAuth identity's unv...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/makeplane/plane/commit/b91b61c379908d9e451613dbca23fc3803e926d2
- https://github.com/makeplane/plane/pull/9289
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-7j95-vh8g-f365
- https://github.com/makeplane/plane/security/advisories/GHSA-7j95-vh8g-f365

### [CVE-2026-88395](https://github.com/fangtang7/CVE/blob/main/GouGuOA/sql.md)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-88395
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-06 01:17:16 JST
- 更新日: 2026-10-06 04:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GouGuOA v6.0.5 and before is vulnerable to SQL Injection in /home/message/rubbish via the keywords parameter.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/fangtang7/CVE/blob/main/GouGuOA/sql.md
- https://github.com/fangtang7/CVE/blob/main/GouGuOA/sql.md

### [CVE-2026-100511](https://patchstack.com/database/wordpress/plugin/vk-google-job-posting-manager/vulnerability/wordpress-vk-google-job-posting-manager-plugin-1-3-1-php-object-injection-vulnerability?_s_id=cve)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-100511
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-06 05:17:07 JST
- 更新日: 2026-10-06 05:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Deserialization of Untrusted Data vulnerability in Vektor Inc. VK Google Job Posting Manager vk-google-job-posting-manager allows Object Injection.This issue affects VK Google Job Posting Manager: from n/a through 1.3.1.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://patchstack.com/database/wordpress/plugin/vk-google-job-posting-manager/vulnerability/wordpress-vk-google-job-posting-manager-plugin-1-3-1-php-object-injection-vulnerability?_s_id=cve

### [CVE-2026-102775](https://www.phoca.cz/)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-102775
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-06 01:17:04 JST
- 更新日: 2026-10-06 02:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla Extension - phoca.cz - Authorisation bypass through user-controlled key (IDOR) in Order View in Phoca Cart 5.0.0 - 6.1.8 - Phoca Cart's order-file download endpoint does not verify the download tokens it asks for. The d (download token) and o (order token) parameters are checked for non-emptiness only — they are...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.phoca.cz/

### [CVE-2026-105383](https://github.com/onetwothreeneth/HospitalManagementSystem/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-105383
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-06 02:17:14 JST
- 更新日: 2026-10-06 02:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability has been found in onetwothreeneth HospitalManagementSystem up to 9ef91ed6007314b6473110ed699dff76d158f61d. This impacts an unknown function of the file php/controller.php. Such manipulation of the argument transaction_idS leads to sql injection. The attack can be executed remotely. The exploit has been...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/onetwothreeneth/HospitalManagementSystem/
- https://github.com/onetwothreeneth/HospitalManagementSystem/issues/8
- https://vuldb.com/cve/CVE-2026-105383
- https://vuldb.com/submit/977737
- https://vuldb.com/vuln/413577

### [CVE-2026-104955](https://github.com/makeplane/plane/commit/4c1bdd1d625fa3f1141e8af9c15423946472069e)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-104955
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-06 02:17:10 JST
- 更新日: 2026-10-06 02:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Plane is an open-source project management tool. Prior to 1.4.0, a Project Member with role 15 can send a PATCH request to the project-member update endpoint at /api/workspaces/{workspace_slug}/projects/{project_id}/members/{member_pk}/ to change another user's project role. The role-update logic blocks only a new role...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/makeplane/plane/commit/4c1bdd1d625fa3f1141e8af9c15423946472069e
- https://github.com/makeplane/plane/pull/9014
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-x63v-p7wc-47x4

### [CVE-2026-105690](https://github.com/penpot/penpot/commit/7c85837290c4e7d6f7d99472b092ad4f7c9d6a97)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-105690
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-06 05:17:18 JST
- 更新日: 2026-10-06 06:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Penpot is an open-source design and prototyping platform. Prior to 2.18.0, logout clears the browser's auth-token cookie without revoking the corresponding server-side session. A previously captured session token remains usable after the victim logs out and can continue to make authenticated requests with the victim's...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/penpot/penpot/commit/7c85837290c4e7d6f7d99472b092ad4f7c9d6a97
- https://github.com/penpot/penpot/releases/tag/2.18.0
- https://github.com/penpot/penpot/security/advisories/GHSA-mj9f-5cwq-7p3q

### [CVE-2026-102777](https://www.svenbluege.de/)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-102777
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-06 02:17:09 JST
- 更新日: 2026-10-06 05:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla Extension - svenbluege.de - Server-side request forgery in the Google Photos picker in Event Gallery extension < 6.6.0 - The Google Photos picker of the back-end upload page fetches the thumbnails of the picked images through the server, with the OAuth access token of the Google Photos account. The task took the...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.svenbluege.de/

### [CVE-2026-93323](https://github.com/moby/buildkit/releases/tag/v0.33.1)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-93323
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-06 03:17:39 JST
- 更新日: 2026-10-06 04:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The Dockerfile frontend loaded the Dockerfile and .dockerignore files of a build context into memory without a size limit. A build context containing an oversized file could make buildkitd allocate memory proportional to that file, potentially exhausting memory and terminating the daemon, which interrupts other builds...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/moby/buildkit/releases/tag/v0.33.1
- https://github.com/moby/buildkit/security/advisories/GHSA-mgqf-486f-49vp

### [CVE-2026-105387](https://github.com/girishsaraf/Online-Appointment-Booking-System/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-105387
- 関連キーワード: gin, mysql
- 影響製品: -
- 公開日: 2026-10-06 04:17:16 JST
- 更新日: 2026-10-06 04:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security flaw has been discovered in girishsaraf Online-Appointment-Booking-System up to f427b4757128ca253d33d0cc4e87bbb9c999a4d5. This affects the function mysqli_query of the file cover.php of the component Patient Login Handler. The manipulation of the argument uname/psw results in sql injection. It is possible to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/girishsaraf/Online-Appointment-Booking-System/
- https://github.com/girishsaraf/Online-Appointment-Booking-System/issues/5
- https://vuldb.com/cve/CVE-2026-105387
- https://vuldb.com/submit/980739
- https://vuldb.com/vuln/413581

### [CVE-2026-105636](https://github.com/makeplane/plane/commit/04622ce1188c4680951f0001e35efb342fe51615)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-105636
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-06 04:17:17 JST
- 更新日: 2026-10-06 04:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Plane is an open-source project management tool. Prior to 1.4.0, the webhook delivery task in apps/api/plane/bgtasks/webhook_task.py calls requests.post() without allow_redirects=False and does not validate redirect targets. validate_url() blocks private, loopback, link-local, and reserved addresses in the original web...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/makeplane/plane/commit/04622ce1188c4680951f0001e35efb342fe51615
- https://github.com/makeplane/plane/pull/9163
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-mq87-52pf-hm3h

### [CVE-2026-105697](https://github.com/langflow-ai/langflow/commit/eba285edf1dd4a33bf23a9cb8113c991fcdf3d1d)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-105697
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-06 06:16:35 JST
- 更新日: 2026-10-06 06:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Langflow is a tool for building and deploying AI-powered agents and workflows. Before Langflow 1.10.3, the MCP stdio transport launched whatever command / args a user put in an MCP server configuration, with no allowlist and (before 1.10.3) wrapped in bash -c "exec {command} ...". Any user able to reach the MCP server...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/langflow-ai/langflow/commit/eba285edf1dd4a33bf23a9cb8113c991fcdf3d1d
- https://github.com/langflow-ai/langflow/commit/efbc4a16e639409d938a4883463d27ef0bc637a0
- https://github.com/langflow-ai/langflow/pull/12290
- https://github.com/langflow-ai/langflow/pull/14036
- https://github.com/langflow-ai/langflow/releases/tag/v1.10.3

### [CVE-2026-12171](https://github.com/cookpete/auto-changelog/commit/1d02a48a0a57c69a3cd268aca375d64d50877c1a)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-12171
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-06 02:17:14 JST
- 更新日: 2026-10-06 05:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: auto-changelog before 2.6.1 merges configuration from inside the target repository (the .auto-changelog file and the auto-changelog key in package.json) into its options, and honors security-sensitive options from that untrusted source. The handlebarsSetup option is passed to require(), so running auto-changelog over a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/cookpete/auto-changelog/commit/1d02a48a0a57c69a3cd268aca375d64d50877c1a
- https://github.com/cookpete/auto-changelog/security/advisories/GHSA-xpvr-2hvx-m8q4
- https://github.com/cookpete/auto-changelog/security/advisories/GHSA-xpvr-2hvx-m8q4

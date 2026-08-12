# Backend CVE Summary (2026-08-13)

## Overview

- 取得日時: 2026-08-13 07:55:58 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 19
- Critical: 4
- High: 5
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-68968](https://github.com/apache/airflow/pull/70889)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-68968
- 関連キーワード: fastapi, gin
- 影響製品: -
- 公開日: 2026-08-13 01:17:19 JST
- 更新日: 2026-08-13 05:50:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Apache Airflow's Backfill API authorized a request against a Dag id supplied by the caller whenever the `backfill_id` path segment failed to parse. The authorization dependency parsed it with `int()` while the route handler parsed it as pydantic's `NonNegativeInt`, which accepts values `int()` rejects (`1.0` coerces to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/apache/airflow/pull/70889
- https://lists.apache.org/thread/f9zmw6xs5b4syhwzbl6fsxm4kf2632ol
- http://www.openwall.com/lists/oss-security/2026/08/12/12

### [CVE-2026-73285](https://github.com/rustfs/rustfs/blob/380ed40b471887014fe21d069b61df9eacca074b/.agents/skills/security-advisory-lessons/references/advisory-patterns.md?plain=1#L47)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-73285
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-13 00:18:31 JST
- 更新日: 2026-08-13 00:18:31 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: RustFS is a distributed object storage system built in Rust. From 1.0.0-alpha.64 until 1.0.0-rc.1, RustFS external OPA authorization enabled by RUSTFS_POLICY_PLUGIN_URL in crates/iam/src/sys.rs sets PreparedIamAuth.needs_existing_object_tag incorrectly for PreparedIamMode::Opa, causing maybe_merge_object_tag_conditions...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/rustfs/rustfs/blob/380ed40b471887014fe21d069b61df9eacca074b/.agents/skills/security-advisory-lessons/references/advisory-patterns.md?plain=1#L47
- https://github.com/rustfs/rustfs/commit/98d3619613722308498494d412797a52ea8ae64d
- https://github.com/rustfs/rustfs/releases/tag/1.0.0-rc.1
- https://github.com/rustfs/rustfs/security/advisories/GHSA-5w8r-p896-6vq2
- https://github.com/rustfs/rustfs/security/advisories/GHSA-5w8r-p896-6vq2

### [CVE-2026-65937](https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2026)

> **Backend** / **HIGH** / CVSS: **8.0** / KEV: **no**

- タイトル: CVE-2026-65937
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-13 01:17:13 JST
- 更新日: 2026-08-13 03:18:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: In WhatsUp Gold versions released before 2026.0.2, an authenticated attacker can bypass frontend controls and inject persistent script content.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2026
- https://docs.progress.com/bundle/whatsupgold-release-notes-26-0/page/WhatsUp-Gold-2026.0-Release-Notes.html
- https://www.progress.com/network-monitoring

### [CVE-2026-65941](https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2026)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-65941
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-13 01:17:14 JST
- 更新日: 2026-08-13 02:17:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: In WhatsUp Gold versions released before 2026.0.2, an unauthenticated remote attacker with network access to the affected service can execute arbitrary code in the context of the IIS application service account.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2026
- https://docs.progress.com/bundle/whatsupgold-release-notes-26-0/page/WhatsUp-Gold-2026.0-Release-Notes.html
- https://www.progress.com/network-monitoring

### [CVE-2026-49349](https://github.com/regclient/regclient/security/advisories/GHSA-qvqc-4c52-x6qp)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-49349
- 関連キーワード: go, docker
- 影響製品: -
- 公開日: 2026-08-13 00:17:37 JST
- 更新日: 2026-08-13 00:17:37 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: regclient is a Docker and OCI Registry Client in Go. Prior to version 0.11.5, credentials for a registry may be inadvertently leaked to external servers. A prerequisite for this attack is a malicious registry server, a malicious blob store, or a registry that does not restrict the external URLs for foreign blobs. Versi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/regclient/regclient/security/advisories/GHSA-qvqc-4c52-x6qp

### [CVE-2026-18675](https://developer.konghq.com/mesh/changelog/)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-18675
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-13 04:17:30 JST
- 更新日: 2026-08-13 04:17:30 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The dataplane token validator in kuma-cp performs an unchecked Go type assertion on the JWT kid header. A token whose kid is a JSON number decodes as a float64 and triggers a runtime panic before any signature, claims, or authorization check runs. The panic terminates the entire kuma-cp process, HTTP API, the health an...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://developer.konghq.com/mesh/changelog/
- https://github.com/kumahq/kuma/pull/17465
- https://github.com/kumahq/kuma/pull/17467
- https://github.com/kumahq/kuma/pull/17468
- https://github.com/kumahq/kuma/pull/17469

### [CVE-2026-65938](https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2026)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-65938
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-13 01:17:13 JST
- 更新日: 2026-08-13 03:18:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: In WhatsUp Gold versions released before 2026.0.2, an improper authorization vulnerability in the Scheduled Reports API allows any authenticated user to invoke restricted actions.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2026
- https://docs.progress.com/bundle/whatsupgold-release-notes-26-0/page/WhatsUp-Gold-2026.0-Release-Notes.html
- https://www.progress.com/network-monitoring

### [CVE-2026-65939](https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2026)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-65939
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-13 01:17:13 JST
- 更新日: 2026-08-13 03:18:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: In WhatsUp Gold versions released before 2026.0.2, a privileged attacker can create a LogToFile action specifying an arbitrary file extension within the IIS web root.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2026
- https://docs.progress.com/bundle/whatsupgold-release-notes-26-0/page/WhatsUp-Gold-2026.0-Release-Notes.html
- https://www.progress.com/network-monitoring

### [CVE-2026-65940](https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2026)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-65940
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-13 01:17:13 JST
- 更新日: 2026-08-13 02:17:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: In WhatsUp Gold versions released before 2026.0.2, a privileged attacker can write arbitrary files to a web-accessible location on the host server.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://community.progress.com/s/article/WhatsUp-Gold-Security-Bulletin-August-2026
- https://docs.progress.com/bundle/whatsupgold-release-notes-26-0/page/WhatsUp-Gold-2026.0-Release-Notes.html
- https://www.progress.com/network-monitoring

### [CVE-2026-73263](https://github.com/prowler-cloud/prowler/commit/0b782fcb8c24ece7bd38deede2b8f13d8583e39c)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-73263
- 関連キーワード: python, kubernetes
- 影響製品: -
- 公開日: 2026-08-13 00:18:30 JST
- 更新日: 2026-08-13 01:17:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Prowler is a cloud security platform. Prior to 5.36.0, the Kubernetes provider connection test accepted kubeconfig_content containing a legacy gcp auth-provider with config.cmd-path and config.cmd-args because kubeconfig_contains_exec_auth in api/src/backend/api/v1/serializers.py checked only exec blocks, and POST /api...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/prowler-cloud/prowler/commit/0b782fcb8c24ece7bd38deede2b8f13d8583e39c
- https://github.com/prowler-cloud/prowler/pull/12091
- https://github.com/prowler-cloud/prowler/releases/tag/5.36.0
- https://github.com/prowler-cloud/prowler/security/advisories/GHSA-ccqh-6cjc-wp4j
- https://github.com/prowler-cloud/prowler/security/advisories/GHSA-ccqh-6cjc-wp4j

### [CVE-2026-73325](https://pypi.org/project/onecomp/)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-73325
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-13 01:17:23 JST
- 更新日: 2026-08-13 05:17:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Fujitsu Research's OneCompression library 1.2.0 contains an unsafe deserialization vulnerability that allows attackers to execute arbitrary code by supplying a crafted model.pt checkpoint file, as QuantizedModelLoader.load_quantized_model_pt() unconditionally calls torch.load with weights_only=False, invoking Python's...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://pypi.org/project/onecomp/
- https://pypi.org/project/onecomp/1.2.1/
- https://www.vulncheck.com/advisories/fujitsu-onecompression-arbitrary-code-execution-via-torch-load-deserialization

### [CVE-2026-18171](https://docs.docker.com/ai/sandboxes/)

> **Backend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-18171
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-13 00:17:32 JST
- 更新日: 2026-08-13 03:17:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Docker Sandboxes (sbx) applies the read-only intent of a runtime host mount to the in-guest container bind only: the underlying virtio-fs host-edge grant is added to the sandbox's policy-share allowlist with no access mode. The directory stays writable at its shared-export path, so unprivileged code inside the sandbox...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.docker.com/ai/sandboxes/
- https://docs.docker.com/ai/sandboxes/architecture/

### [CVE-2026-66384](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-66384
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-13 01:17:14 JST
- 更新日: 2026-08-13 04:17:37 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An authenticated user may write data outside the intended Docker cache path under specific remote-repository conditions.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases
- https://docs.jfrog.com/releases/docs/jfrog-security-advisories

### [CVE-2026-19642](https://aws.amazon.com/security/security-bulletins/2026-080-aws/)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-19642
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-13 05:17:42 JST
- 更新日: 2026-08-13 05:50:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An out-of-bounds write issue in the Base64 decoder in Amazon aws-sdk-cpp before 1.11.862 might allow a remote authenticated user to cause a crash or heap memory corruption in an application that processes crafted Base64-encoded input. To remediate this issue, users should upgrade to version 1.11.862.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-080-aws/
- https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.862
- https://github.com/aws/aws-sdk-cpp/security/advisories/GHSA-wxx3-prfc-69xx

### [CVE-2026-19643](https://aws.amazon.com/security/security-bulletins/2026-080-aws/)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-19643
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-13 05:17:42 JST
- 更新日: 2026-08-13 05:50:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An out-of-bounds read issue in the Base64 decoder in Amazon aws-sdk-cpp before 1.11.862, on some platforms, might allow a remote authenticated user to crash an application that processes crafted Base64-encoded input. To remediate this issue, users should upgrade to version 1.11.862.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-080-aws/
- https://github.com/aws/aws-sdk-cpp/releases/tag/1.11.862
- https://github.com/aws/aws-sdk-cpp/security/advisories/GHSA-mxm9-xpf9-x66x

### [CVE-2026-73300](https://github.com/Budibase/budibase/releases/tag/3.40.0)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-73300
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-08-13 03:18:15 JST
- 更新日: 2026-08-13 05:17:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Budibase is an open-source low-code platform. Prior to 3.40.0, the MySQL integration component in Budibase is configured with multipleStatements: true, enabling execution of multiple SQL statements in a single query. Attackers can inject malicious SQL commands through user input fields, leading to complete database com...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Budibase/budibase/releases/tag/3.40.0
- https://github.com/Budibase/budibase/security/advisories/GHSA-q6x4-v3qx-85qw
- https://github.com/Budibase/budibase/security/advisories/GHSA-q6x4-v3qx-85qw

### [CVE-2026-63297](https://github.com/canonical/lxd/security/advisories/GHSA-v989-qw7w-xvg4)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-63297
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-13 05:17:47 JST
- 更新日: 2026-08-13 05:17:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An authorization bypass vulnerability in LXD due to a timing flaw during configuration merging allows an authenticated attacker to bypass target project restrictions during cross-project instance copies. When copying an instance to a target project, LXD performs restriction checks before configuration merging is comple...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/canonical/lxd/security/advisories/GHSA-v989-qw7w-xvg4

### [CVE-2026-73294](https://github.com/semaphoreui/semaphore/commit/7e8a9434bd81b82cf42220151c74801ea97542d6)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-73294
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-13 01:17:22 JST
- 更新日: 2026-08-13 02:17:32 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Semaphore UI is a web interface for managing DevOps tools. Prior to 2.18.17 and 2.19.5-beta2, repository git_url handling passes an attacker-controlled --upload-pack option to CmdGitClient.GetLastRemoteCommitHash through POST /api/project/{id}/repositories and scheduled commit-hash polling, allowing a project Manager o...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/semaphoreui/semaphore/commit/7e8a9434bd81b82cf42220151c74801ea97542d6
- https://github.com/semaphoreui/semaphore/commit/a7a7a33a64aea382a0726b3722856f298663eacf
- https://github.com/semaphoreui/semaphore/security/advisories/GHSA-xp7j-h7jc-4w8p
- https://github.com/semaphoreui/semaphore/tree/v2.18.17
- https://github.com/semaphoreui/semaphore/tree/v2.19.5-beta2

### [CVE-2026-18669](https://www.ibm.com/support/pages/node/7283278)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-18669
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-13 03:17:28 JST
- 更新日: 2026-08-13 05:53:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: IBM i 7.6, 7.5, 7.4, and 7.3 is vulnerable to a privilege escalation as the result of a remote code execution vulnerability in the activation engine component. An authenticated attacker can execute a maliciously planted script with root authority.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7283278

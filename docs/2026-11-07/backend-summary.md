# Backend CVE Summary (2026-11-07)

## Overview

- 取得日時: 2026-11-07 10:50:38 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 12
- Critical: 2
- High: 4
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-59105](https://offseq.com/en/research/jumis-cve-2026-59105/)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-59105
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-11-07 00:17:22 JST
- 更新日: 2026-11-07 01:18:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Jumis (formerly Tildes Jumis) creates and uses a Microsoft SQL Server login named ##Tilde_JumisAdmin## whose password is derived deterministically from a single non-secret input - the SQL Server name (@@servername). The derivation algorithm is hard-coded in the client application and is identical across every installat...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://offseq.com/en/research/jumis-cve-2026-59105/
- https://www.mansjumis.lv/

### [CVE-2026-119170](https://github.com/python/cpython/issues/160923)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-119170
- 関連キーワード: python, go, openssl
- 影響製品: -
- 公開日: 2026-11-07 00:17:12 JST
- 更新日: 2026-11-07 10:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: There was a regression in how FIPS algorithms were enforced for the hashlib module. Only users that are using OpenSSL in FIPS mode are affected. Only Python 3.14.10 is affected, all other Python versions are unaffected.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/python/cpython/issues/160923
- https://github.com/python/cpython/pull/160984
- https://mail.python.org/archives/list/security-announce@python.org/thread/PXVTTOBPUMFJSSUXN6XCS7FC5DZOSZXK/
- http://www.openwall.com/lists/oss-security/2026/11/06/30

### [CVE-2026-65960](https://github.com/cilium/tetragon/commit/8e89933d3526f37c04f7523013ff32f8b1c6f62a)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-65960
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-07 05:17:24 JST
- 更新日: 2026-11-07 05:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tetragon is an eBPF-based security observability and runtime enforcement project. Versions before 1.7.0 can use a Helm default that exposes the privileged Tetragon gRPC API through an unauthenticated TCP listener on localhost:54321. An attacker who can run or compromise same-node hostNetwork pods can reach the listener...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/cilium/tetragon/commit/8e89933d3526f37c04f7523013ff32f8b1c6f62a
- https://github.com/cilium/tetragon/commit/fe46101770b960ebbf39fe9749bb20d49cf178b2
- https://github.com/cilium/tetragon/pull/4882
- https://github.com/cilium/tetragon/releases/tag/v1.7.0
- https://github.com/cilium/tetragon/security/advisories/GHSA-6qqg-3qf7-p3v5

### [CVE-2026-108262](https://github.com/ddev/ddev/security/advisories/GHSA-9hq4-hm3j-jmph)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-108262
- 関連キーワード: go, node.js
- 影響製品: -
- 公開日: 2026-11-07 04:17:06 JST
- 更新日: 2026-11-07 04:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DDEV is an open-source tool for running local web development environments for PHP and Node.js. From 1.25.2 until 1.25.4, Untar in pkg/archive/archive.go validates an absolute tar symlink target after rebasing it beneath dest, but creates the symlink with the raw absolute Linkname. A crafted archive can therefore plant...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/ddev/ddev/security/advisories/GHSA-9hq4-hm3j-jmph

### [CVE-2026-123748](https://github.com/chenyme/grok2api/)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-123748
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-07 03:18:04 JST
- 更新日: 2026-11-07 03:18:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security flaw has been discovered in chenyme grok2api up to 3.1.6. Affected by this vulnerability is the function proxyVoiceWebSocket of the file backend/internal/transport/http/inference/voice_ws_handler.go of the component WebSocket Proxy. The manipulation results in resource consumption. The attack may be launched...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/chenyme/grok2api/
- https://github.com/chenyme/grok2api/commit/7ad0f791f0a9eb5a0ddfe38ac4dfcef01e19a6d4
- https://github.com/chenyme/grok2api/issues/1071
- https://github.com/chenyme/grok2api/pull/1073
- https://github.com/chenyme/grok2api/releases/tag/v3.1.7

### [CVE-2026-123617](https://github.com/openwhyd/openwhyd/blob/v1.65.0/app/models/user.js#L288-L294)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-123617
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-11-07 00:17:19 JST
- 更新日: 2026-11-07 03:18:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Openwhyd before 1.65.1 contains a NoSQL injection vulnerability that allows unauthenticated attackers to manipulate user lookups by passing JSON objects in the id parameter. Attackers can send MongoDB query operators such as $ne or $gt to POST /api/user to select and enumerate other users' public profile records.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/openwhyd/openwhyd/blob/v1.65.0/app/models/user.js#L288-L294
- https://github.com/openwhyd/openwhyd/commit/167c45d6754df0adb3415f71cbd7cde91cbe7874
- https://github.com/openwhyd/openwhyd/releases/tag/v1.65.1
- https://github.com/openwhyd/openwhyd/security/advisories/GHSA-hfg3-vq24-hprp
- https://www.vulncheck.com/advisories/openwhyd-before-1.65.1-nosql-injection-via-post-api-user

### [CVE-2026-123664](https://github.com/nasa-gcn/gcn.nasa.gov/)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-123664
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-07 00:17:20 JST
- 更新日: 2026-11-07 00:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security flaw has been discovered in nasa-gcn gcn.nasa.gov up to b299b562af665878964b981a459f0a9c04b11adf. This issue affects some unknown processing of the file /user/email of the component Email Notification Handler. Performing a manipulation of the argument Recipient results in improper authorization. The attack i...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nasa-gcn/gcn.nasa.gov/
- https://github.com/nasa-gcn/gcn.nasa.gov/issues/3805
- https://https:/github.com/nasa-gcn/gcn.nasa.gov/pull/3863
- https://vuldb.com/cve/CVE-2026-123664
- https://vuldb.com/submit/1033135

### [CVE-2026-124039](https://github.com/gitleaks/gitleaks)

> **Backend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-124039
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-07 05:17:22 JST
- 更新日: 2026-11-07 05:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Gitleaks through 8.30.1 contains an incorrect permission assignment vulnerability that allows local users to read scan reports because cmd/root.go creates the --report-path file with os.Create and default permissions. Unless --redact is passed, other local users on shared hosts or CI runners can read plaintext secrets...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gitleaks/gitleaks
- https://github.com/gitleaks/gitleaks/blob/v8.30.1/cmd/root.go#L474
- https://github.com/gitleaks/gitleaks/issues/2299
- https://www.vulncheck.com/advisories/gitleaks-through-8.30.1-world-readable-report-files-via-report-path

### [CVE-2026-123665](https://github.com/kubescape/kubescape/)

> **Backend** / **LOW** / CVSS: **2.8** / KEV: **no**

- タイトル: CVE-2026-123665
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-07 00:17:20 JST
- 更新日: 2026-11-07 00:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A weakness has been identified in kubescape up to 4.0.15. Impacted is the function GetWriter of the file core/pkg/resultshandling/printer/printresults.go of the component Output. Executing a manipulation of the argument outputFile can lead to permission issues. The attack requires local access. Upgrading to version 4.0...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/kubescape/kubescape/
- https://github.com/kubescape/kubescape/commit/d90f77314c7d4f2b53cf2425844bde2315bd26d2
- https://github.com/kubescape/kubescape/issues/4091
- https://github.com/kubescape/kubescape/pull/4092
- https://github.com/kubescape/kubescape/releases/tag/v4.0.16

### [CVE-2026-123859](https://docs.snowflake.com/en/release-notes/clients-drivers/python-connector-2026#version-481-oct-26-2026)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-123859
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-11-07 02:17:25 JST
- 更新日: 2026-11-07 06:15:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: When identifier escaping is disabled through a non-default configuration, the write_pandas() data-loading functionality in the Snowflake Connector for Python and the Snowflake Connector for Python (Universal Core) did not escape DataFrame column names before including them in generated SQL, which could allow SQL inject...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.snowflake.com/en/release-notes/clients-drivers/python-connector-2026#version-481-oct-26-2026
- https://docs.snowflake.com/en/release-notes/clients-drivers/python-connector-2026#version-520-nov-4-2026

### [CVE-2026-58490](https://github.com/TracecatHQ/tracecat/commit/018258ba6a17c36cbfa7ca977526c34fb6afc35f)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-58490
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-11-07 05:17:23 JST
- 更新日: 2026-11-07 05:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tracecat is an open-source security automation platform for teams and AI agents. From version 0.37.0 until 1.0.0-beta.49, Docker Compose deployments with SAML enabled can render SAML_SIGNED_ASSERTIONS and SAML_SIGNED_RESPONSES as empty values, overriding secure application defaults and disabling both signature requirem...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/TracecatHQ/tracecat/commit/018258ba6a17c36cbfa7ca977526c34fb6afc35f
- https://github.com/TracecatHQ/tracecat/commit/a97aafbfd667a6b9a3b7b524e1c1bfa9d8c59779
- https://github.com/TracecatHQ/tracecat/commit/dab64eb7ac0eb2088783ca14f4cb2d058547bfff
- https://github.com/TracecatHQ/tracecat/pull/2824
- https://github.com/TracecatHQ/tracecat/pull/2825

### [CVE-2026-58141](https://github.com/langgenius/dify/commit/7bfcf9185c75bb18f0b44335080524e659f087d9)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-58141
- 関連キーワード: postgresql, aws
- 影響製品: -
- 公開日: 2026-11-07 01:18:54 JST
- 更新日: 2026-11-07 02:18:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dify before 1.15.0 contains a server-side request forgery vulnerability that allows any authenticated console user to bypass SSRF protections and issue arbitrary HTTP requests to internal services and cloud metadata endpoints due to the Squid proxy configuration only defining source ACLs without destination deny rules...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/langgenius/dify/commit/7bfcf9185c75bb18f0b44335080524e659f087d9
- https://github.com/langgenius/dify/pull/36332
- https://github.com/langgenius/dify/releases/tag/1.15.0
- https://www.vulncheck.com/advisories/dify-ssrf-protection-bypass-via-remote-files-endpoints

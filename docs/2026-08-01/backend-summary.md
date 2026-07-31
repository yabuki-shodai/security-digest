# Backend CVE Summary (2026-08-01)

## Overview

- 取得日時: 2026-08-01 08:13:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 27
- Critical: 7
- High: 10
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-54725](https://github.com/bank-vaults/vault-secrets-webhook/commit/76db45976fee0f54cafd94dffa425e6b542f65a0)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-54725
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-08-01 03:17:17 JST
- 更新日: 2026-08-01 04:17:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: vault-secrets-webhook is a Kubernetes mutating webhook that makes direct secret injection into Pods possible. Prior to 1.23.1, parseVaultConfig() in pkg/webhook/config.go accepts the vault.security.banzaicloud.io/vault-addr annotation, MutateConfigMap and MutateSecret call newVaultClient in pkg/webhook/webhook.go, and...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/bank-vaults/vault-secrets-webhook/commit/76db45976fee0f54cafd94dffa425e6b542f65a0
- https://github.com/bank-vaults/vault-secrets-webhook/releases/tag/v1.23.1
- https://github.com/bank-vaults/vault-secrets-webhook/security/advisories/GHSA-r2v3-8gwf-7ghm
- https://github.com/bank-vaults/vault-secrets-webhook/security/advisories/GHSA-r2v3-8gwf-7ghm

### [CVE-2026-67822](https://github.com/Tristerjh/Tenda/blob/main/Tenda_W6-S_GO_overflow.md)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-67822
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-01 02:16:35 JST
- 更新日: 2026-08-01 04:17:12 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Tenda W6-S 1.0.0.4(510) contains a stack-based buffer overflow vulnerability in the /goform/wifiSSIDset endpoint. The function formwrlSSIDset uses sprintf to copy user-controlled 'GO' and 'index' parameters into a 64-byte stack buffer without length restriction, leading to stack overflow.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Tristerjh/Tenda/blob/main/Tenda_W6-S_GO_overflow.md
- https://github.com/Tristerjh/Tenda/blob/main/Tenda_W6-S_GO_overflow.md

### [CVE-2026-52856](https://github.com/pterodactyl/wings/commit/8e49c7c0eda815d3ada171831876a1c14c493026)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-52856
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-01 02:16:33 JST
- 更新日: 2026-08-01 04:17:09 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Wings is the server control plane for Pterodactyl, a free, open-source game server management panel. Prior to 1.13.0, a malformed packet received during the SFTP connection handshake causes a Go panic. This issue is fixed in version 1.13.0.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pterodactyl/wings/commit/8e49c7c0eda815d3ada171831876a1c14c493026
- https://github.com/pterodactyl/wings/releases/tag/v1.13.0
- https://github.com/pterodactyl/wings/security/advisories/GHSA-ghrq-5wpp-hxx5

### [CVE-2026-52857](https://github.com/pterodactyl/wings/commit/5f71f65711b6b9e6f913bec94a7b36d9a5eaae49)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-52857
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-01 01:17:06 JST
- 更新日: 2026-08-01 02:16:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Wings is the server control plane for Pterodactyl, a free, open-source game server management panel. Prior to 1.13.0, unbounded json, yaml, and xml configuration-file parsers in parser.go can process an oversized non-file parser configuration file and exhaust Wings process memory. This issue is fixed in version 1.13.0.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pterodactyl/wings/commit/5f71f65711b6b9e6f913bec94a7b36d9a5eaae49
- https://github.com/pterodactyl/wings/releases/tag/v1.13.0
- https://github.com/pterodactyl/wings/security/advisories/GHSA-q6hh-gp44-4hcm

### [CVE-2026-53551](https://github.com/free5gc/ausf/commit/bfc4a10094dbacbd862baa4686829f3fcc06ce1e)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-53551
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-01 05:16:51 JST
- 更新日: 2026-08-01 05:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: free5GC is an open-source implementation of the 5G core network. Prior to 1.4.5, the free5GC AUSF (Authentication Server Function) does not validate the supiOrSuci field in UE authentication requests. Null bytes (\x00) and other control characters pass through JSON parsing unchanged and are forwarded to the UDM in an u...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/free5gc/ausf/commit/bfc4a10094dbacbd862baa4686829f3fcc06ce1e
- https://github.com/free5gc/ausf/pull/61
- https://github.com/free5gc/ausf/releases/tag/v1.4.5
- https://github.com/free5gc/free5gc/issues/1048
- https://github.com/free5gc/free5gc/releases/tag/v4.2.2

### [CVE-2026-59231](https://github.com/ccyl13/Pentestify/commit/a058a22b42c6311895622645265df79a60265b1d)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-59231
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-01 01:17:08 JST
- 更新日: 2026-08-01 03:17:18 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Server-Side Request Forgery in the PDF export component in maalfer Pentestify before 1.1.0 allows authenticated users to cause outbound HTTP GET requests from the server to arbitrary attacker-chosen destinations via unvalidated URLs stored in the finding images field or the report client_logo field, which the server-si...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/ccyl13/Pentestify/commit/a058a22b42c6311895622645265df79a60265b1d
- https://github.com/ccyl13/Pentestify/releases/tag/v1.1.1
- https://secur0.com/en/cna/cve-list/cve-2026-59231-ssrf-in-pentestify-via-unvalidated-image-urls-cve-id-cve-2026-59231

### [CVE-2026-51785](https://fenrisk.com/hiawatha-http-smuggling)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-51785
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-01 06:17:31 JST
- 更新日: 2026-08-01 06:17:31 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An issue in Hugo Leisink Hiawatha v.12.1 and before allows a remote attacker to execute arbitrary code via a crafted request
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://fenrisk.com/hiawatha-http-smuggling
- https://www.rfc-editor.org/rfc/rfc2616
- https://www.rfc-editor.org/rfc/rfc2616.html#section-4.4
- https://www.rfc-editor.org/rfc/rfc9112.html#section-6.3

### [CVE-2026-51953](https://github.com/altamish1994/CVE_Published/blob/main/FeehiCMS/CVE-2026-51953.MD)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-51953
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-01 07:17:02 JST
- 更新日: 2026-08-01 07:17:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An issue in FeehiCMS v.2.1.1 allows an attacker to escalate privileges via the Session management module, authentication logic, logout handler components
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/altamish1994/CVE_Published/blob/main/FeehiCMS/CVE-2026-51953.MD
- https://github.com/liufee/cms

### [CVE-2026-52134](https://github.com/if-forget/CVE-2026-52134-libiec61850)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-52134
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-01 07:17:02 JST
- 更新日: 2026-08-01 07:17:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An issue in the parseGoosePayload() function (/goose/goose_receiver.c) of libiec61850 v1.6 allows attackers to bypass authentication via a captured GOOSE frame.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/if-forget/CVE-2026-52134-libiec61850
- https://github.com/mz-automation/libiec61850
- https://github.com/mz-automation/libiec61850/tree/v1.6/src/goose/goose_receiver.c

### [CVE-2026-68770](https://github.com/huggingface/sentence-transformers)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-68770
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-01 06:17:32 JST
- 更新日: 2026-08-01 06:17:32 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: sentence-transformers contains a security control bypass vulnerability that allows attackers to achieve arbitrary code execution by exploiting a logic flaw in the import_module_class helper within sentence_transformers/util/misc.py, where the guard condition includes an 'or os.path.exists(model_name_or_path)' clause th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/huggingface/sentence-transformers
- https://github.com/huggingface/sentence-transformers/commit/ae1acc3fb2aa2004577b297eb4a915ce7a03316a
- https://github.com/huggingface/sentence-transformers/issues/3801
- https://github.com/huggingface/sentence-transformers/pull/3807
- https://www.vulncheck.com/advisories/sentence-transformers-arbitrary-code-execution-on-local-model-load-despite-trust-remote-code-false

### [CVE-2026-68771](https://github.com/Comfy-Org/ComfyUI)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-68771
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-01 07:17:03 JST
- 更新日: 2026-08-01 07:17:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ComfyUI v0.23.0 contains an unsafe deserialization vulnerability in the LoadTrainingDataset node that allows unauthenticated remote attackers to execute arbitrary Python code by uploading a crafted pickle file and triggering its deserialization. Attackers can upload a malicious shard_*.pkl file via the unauthenticated...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Comfy-Org/ComfyUI
- https://github.com/Comfy-Org/ComfyUI/commit/94ee49b1612824366a8631ea069b2a1fa5c73720
- https://github.com/Comfy-Org/ComfyUI/pull/14543
- https://www.vulncheck.com/advisories/comfyui-unauthenticated-rce-via-loadtrainingdataset-pickle-deserialization

### [CVE-2026-53501](https://github.com/thumbor/thumbor/commit/e3ae3e2500537b4d735df4144129a649374bb70b)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-53501
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-01 04:17:09 JST
- 更新日: 2026-08-01 05:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Thumbor is an open-source photo thumbnail service by globo.com. Prior to 7.8.0, Thumbor’s HMAC validation can be bypassed due to the use of Python’s .replace() when removing the signature from the URL before validation. Since .replace() removes all occurrences of the substring, an attacker can insert the same signature...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/thumbor/thumbor/commit/e3ae3e2500537b4d735df4144129a649374bb70b
- https://github.com/thumbor/thumbor/releases/tag/7.8.0
- https://github.com/thumbor/thumbor/security/advisories/GHSA-mw3h-qjxj-6xg9

### [CVE-2026-52855](https://github.com/pterodactyl/wings/commit/eb65e27ae077a63e38518c490768486af1cd86a9)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-52855
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-01 02:16:33 JST
- 更新日: 2026-08-01 05:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Wings is the server control plane for Pterodactyl, a free, open-source game server management panel. Prior to 1.12.3, {{config.}} placeholders in egg configuration-file templates allow a low-privileged user to read {{config.token}}, {{config.token_id}}, and {{config.docker.registries}} from the full daemon configuratio...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pterodactyl/wings/commit/eb65e27ae077a63e38518c490768486af1cd86a9
- https://github.com/pterodactyl/wings/releases/tag/v1.12.3
- https://github.com/pterodactyl/wings/security/advisories/GHSA-pfvc-3p5h-x7h6

### [CVE-2026-16503](https://kb.cert.org/vuls/id/243636)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-16503
- 関連キーワード: postgresql, docker
- 影響製品: -
- 公開日: 2026-08-01 01:16:58 JST
- 更新日: 2026-08-01 01:16:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Deployment of the VPS.org one-click Supabase template deploys a PostgreSQL instance that is published on all interfaces (0.0.0.0:5432) with a default database password set to "postgres". Because Docker installs its own iptables rules, this exposure bypasses a standard host UFW configuration.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://kb.cert.org/vuls/id/243636

### [CVE-2026-18481](https://aws.amazon.com/security/security-bulletins/2026-068-aws/)

> **Backend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-18481
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-01 04:17:08 JST
- 更新日: 2026-08-01 05:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Stored cross-site scripting in the participant URL handling in AWS Ops Wheel before PR #168 might allow an authenticated remote user to steal session tokens and escalate to full administrative control of the deployed instance via a crafted participant_url value containing a dangerous URI scheme. To remediate this issue...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-068-aws/
- https://github.com/aws/aws-ops-wheel/pull/168
- https://github.com/aws/aws-ops-wheel/security/advisories/GHSA-6rr8-cf9x-pj23

### [CVE-2026-17351](https://github.com/pgadmin-org/pgadmin4/commit/bf4792444446f0e7ab721d23cbd6bfe6afaa7a8b)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-17351
- 関連キーワード: gin, postgresql
- 影響製品: -
- 公開日: 2026-08-01 01:16:59 JST
- 更新日: 2026-08-01 03:17:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The fix for CVE-2026-12045 in pgAdmin 4 9.16 required the LLM-supplied query passed to the AI Assistant's execute_sql_query tool to parse, via sqlparse, as exactly one non-transaction-control statement before running it inside a BEGIN TRANSACTION READ ONLY wrapper. sqlparse's string-literal lexing can disagree with Pos...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pgadmin-org/pgadmin4/commit/bf4792444446f0e7ab721d23cbd6bfe6afaa7a8b
- https://github.com/pgadmin-org/pgadmin4/commit/ef76102bcd1cdb544eb9b4ef18d3382f22b76752
- https://github.com/pgadmin-org/pgadmin4/issues/10192

### [CVE-2026-17566](https://github.com/pgadmin-org/pgadmin4/commit/1496fabe28c9f825f6bac0f0d000d9d3276322c3)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-17566
- 関連キーワード: echo, postgresql
- 影響製品: -
- 公開日: 2026-08-01 01:17:00 JST
- 更新日: 2026-08-01 03:17:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: pgAdmin 4's Import/Export Data tool builds a psql \copy (...) command line by interpolating a user-supplied SQL query into a Jinja template and passing the rendered line to psql via --command. To stop an attacker from breaking out of the (...) wrapper, create_import_export_job() (route POST /import_export/job/<sid>, ga...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pgadmin-org/pgadmin4/commit/1496fabe28c9f825f6bac0f0d000d9d3276322c3
- https://github.com/pgadmin-org/pgadmin4/issues/10213

### [CVE-2026-17346](https://github.com/pgadmin-org/pgadmin4/commit/73b3218992cc37af6e10b7e54eaeed6ec293c6b2)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-17346
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-08-01 01:16:58 JST
- 更新日: 2026-08-01 03:17:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The fix for CVE-2026-12044 in pgAdmin 4 9.16 hardened qtLiteral and switched sixteen COMMENT ON / pgstattuple / pgstatindex templates to it, but missed several sinks that had been placed in test_sql_string_literal_lint.py's ALLOWLIST on the incorrect assumption that schema, table, publication, and subscription names so...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pgadmin-org/pgadmin4/commit/73b3218992cc37af6e10b7e54eaeed6ec293c6b2
- https://github.com/pgadmin-org/pgadmin4/commit/f75452bfd0f786d0c071638919d48fc1d76f987d
- https://github.com/pgadmin-org/pgadmin4/issues/10193

### [CVE-2026-17347](https://github.com/pgadmin-org/pgadmin4/commit/e7a85767314e7b0fe0b35fe80b9c1af38f48dff6)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-17347
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-01 01:16:59 JST
- 更新日: 2026-08-01 03:17:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The MASTER_PASSWORD_HOOK setting, introduced in pgAdmin 4 7.2, lets an administrator configure an external command that returns a per-user encryption key, with %u in the configured string replaced by the current user's name. The previous implementation substituted the username directly into the command string and execu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pgadmin-org/pgadmin4/commit/e7a85767314e7b0fe0b35fe80b9c1af38f48dff6
- https://github.com/pgadmin-org/pgadmin4/commit/ea7e798aac27174d2bacee1d6e136bed76a95e23
- https://github.com/pgadmin-org/pgadmin4/issues/10191

### [CVE-2026-53504](https://github.com/thumbor/thumbor/commit/3f38fe1610d20168e91f76d432212de30727eb2e)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-53504
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-08-01 04:17:09 JST
- 更新日: 2026-08-01 04:17:09 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Thumbor is an open-source photo thumbnail service by globo.com. Prior to 7.8.0, the convolution filter regular expression performs exponential backtracking on crafted repeated numeric input, allowing a URL request to exhaust processing time. This issue is fixed in 7.8.0.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/thumbor/thumbor/commit/3f38fe1610d20168e91f76d432212de30727eb2e
- https://github.com/thumbor/thumbor/releases/tag/7.8.0
- https://github.com/thumbor/thumbor/security/advisories/GHSA-5vjc-7cxw-4w6j

### [CVE-2026-54729](https://github.com/HackingRepo/dssrf-js/commit/668c21792cd1252baf779a176aa652e2b4c0067d)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-54729
- 関連キーワード: node.js
- 影響製品: -
- 公開日: 2026-08-01 03:17:17 JST
- 更新日: 2026-08-01 03:17:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: DSSRF is a Node.js library that provides a wide range of utilities and advanced SSRF defense checks. Prior to 1.0.5, is_url_safe can treat localhost as safe when DNS resolver 1.1.1.1 returns NXDOMAIN because dns.resolve4 yields no address and no dns.lookup fallback occurs, allowing server-side request forgery. This iss...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/HackingRepo/dssrf-js/commit/668c21792cd1252baf779a176aa652e2b4c0067d
- https://github.com/HackingRepo/dssrf-js/pull/102
- https://github.com/HackingRepo/dssrf-js/security/advisories/GHSA-5846-7qm3-r52j
- https://github.com/HackingRepo/dssrf-js/security/advisories/GHSA-5846-7qm3-r52j

### [CVE-2026-65981](https://github.com/coturn/coturn/commit/37df0513168f830a7c9ce0a411db0300fa182f05)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-65981
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-01 06:17:31 JST
- 更新日: 2026-08-01 06:17:31 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Coturn is a free open source implementation of TURN and STUN Server. Prior to 4.15.0, a server using --mobility authenticates a resumed REFRESH request with the resuming user's credentials but does not verify that identity against the original allocation owner, allowing an authenticated attacker who obtains a victim MO...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/coturn/coturn/commit/37df0513168f830a7c9ce0a411db0300fa182f05
- https://github.com/coturn/coturn/security/advisories/GHSA-69wx-x7x6-pjj8

### [CVE-2026-18141](https://access.redhat.com/security/cve/CVE-2026-18141)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-18141
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-01 01:17:05 JST
- 更新日: 2026-08-01 04:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A flaw was found in aap-gateway, a component of Ansible Automation Platform's Event-Driven Ansible (EDA). An unauthenticated remote attacker can bypass mutual Transport Layer Security (mTLS) authentication for event streams. This is achieved by manipulating the event stream URL and forging the HTTP Subject header. The...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-18141
- https://bugzilla.redhat.com/show_bug.cgi?id=2508155

### [CVE-2026-55100](https://github.com/kyndryl-open-source/hashi-vault-js/commit/ea2f76052d366a08f35f62ef4c12b6a334c91ec2)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-55100
- 関連キーワード: node.js
- 影響製品: -
- 公開日: 2026-08-01 03:17:17 JST
- 更新日: 2026-08-01 05:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: hashi-vault-js is a Node.js module for interacting with the HashiCorp Vault API. Prior to 0.5.2, src/Vault.js concatenates unencoded identifier values including name, username, group, role, and version into Vault request paths and query strings instead of using encodeURIComponent() and URLSearchParams, allowing path tr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/kyndryl-open-source/hashi-vault-js/commit/ea2f76052d366a08f35f62ef4c12b6a334c91ec2
- https://github.com/kyndryl-open-source/hashi-vault-js/pull/66
- https://github.com/kyndryl-open-source/hashi-vault-js/releases/tag/v0.5.2
- https://github.com/kyndryl-open-source/hashi-vault-js/security/advisories/GHSA-g956-2f74-rmv7

### [CVE-2026-17348](https://github.com/pgadmin-org/pgadmin4/commit/24fdcf0f58591c87ada31366c01e1af180eceb05)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-17348
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-01 01:16:59 JST
- 更新日: 2026-08-01 03:17:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: In SERVER mode, pgAdmin 4 enforces authentication per route via the @pga_login_required decorator; the application's before_request hook only handles desktop-mode auto-login and the Kerberos/Webserver-auth redirect, so any route shipped without the decorator is reachable without authentication (CWE-306). This is the sa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pgadmin-org/pgadmin4/commit/24fdcf0f58591c87ada31366c01e1af180eceb05
- https://github.com/pgadmin-org/pgadmin4/issues/10194

### [CVE-2026-17350](https://github.com/pgadmin-org/pgadmin4/commit/461c3afba92baad37c70a6fbd52d205d13a9de53)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-17350
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-01 01:16:59 JST
- 更新日: 2026-08-01 03:17:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The per-tool permission system (custom roles / role-based tool permissions, introduced in pgAdmin 4 9.3) did not enforce its permission check consistently. In SERVER mode, pgAdmin 4 gates each tool behind a per-tool Flask-Security permission, but the permission decorator (permissions_required) was applied only to a sin...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pgadmin-org/pgadmin4/commit/461c3afba92baad37c70a6fbd52d205d13a9de53
- https://github.com/pgadmin-org/pgadmin4/commit/64a9cdbd6a240a962144f84418beaf9e66419779
- https://github.com/pgadmin-org/pgadmin4/commit/ba1984718ad703011740ad48cb9b82402b89cc2c
- https://github.com/pgadmin-org/pgadmin4/commit/d36bd8dc96812c716664feac533d240544e70adc
- https://github.com/pgadmin-org/pgadmin4/issues/10190

### [CVE-2026-25552](https://github.com/TryGhost/Ghost-CLI/security/advisories/GHSA-wjx2-9fpq-8997)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-25552
- 関連キーワード: gin, nginx
- 影響製品: -
- 公開日: 2026-08-01 04:17:08 JST
- 更新日: 2026-08-01 04:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Ghost CLI before 1.30.1 contains an IP spoofing vulnerability that allows unauthenticated remote attackers to bypass rate-limiting controls by manipulating the X-Forwarded-For header through a misconfigured Nginx configuration. Attackers can append attacker-controlled values to the header chain using the $proxy_add_x_f...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/TryGhost/Ghost-CLI/security/advisories/GHSA-wjx2-9fpq-8997
- https://www.vulncheck.com/advisories/ghost-cli-ip-spoofing-via-x-forwarded-for-header

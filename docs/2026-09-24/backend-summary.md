# Backend CVE Summary (2026-09-24)

## Overview

- 取得日時: 2026-09-24 09:26:23 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 21
- Critical: 5
- High: 4
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-71461](https://access.redhat.com/security/cve/CVE-2026-71461)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-71461
- 関連キーワード: django, go, postgresql
- 影響製品: -
- 公開日: 2026-09-24 04:19:02 JST
- 更新日: 2026-09-24 04:40:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HostList.list() catches bare Exception and returns str(e) verbatim. Via host_filter, any authenticated user triggers Django FieldError (leaking complete Host model relation graph including internal reverse accessors) or PostgreSQL DataError (leaking raw database error strings). Two primitives: credential__search=x dump...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-71461
- https://bugzilla.redhat.com/show_bug.cgi?id=2512370

### [CVE-2026-63132](https://github.com/hashicorp/vault/blob/main/CHANGELOG.md#203)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-63132
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-24 04:17:34 JST
- 更新日: 2026-09-24 05:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenBao is an open source identity-based secrets management system. Prior to 2.6.0, OpenBao's handleLogicalRecovery path in http/logical.go compared the highly privileged recovery token with ordinary string equality. A remote unauthenticated attacker able to make repeated recovery mode requests and measure response tim...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/hashicorp/vault/blob/main/CHANGELOG.md#203
- https://github.com/openbao/openbao/commit/0f2d90c331f25d1c6cd108638da03f4c7bd949a8
- https://github.com/openbao/openbao/commit/763625a2072103ea9e9122f2a8408e0b988d287a
- https://github.com/openbao/openbao/pull/3388
- https://github.com/openbao/openbao/pull/3472

### [CVE-2026-96770](https://docs.temporal.io/production-deployment/data-encryption#codec-server-setup)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-96770
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-24 04:19:55 JST
- 更新日: 2026-09-24 05:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: All published s2s-proxy versions through 0.2.2 are affected. In versions 0.1.16 through 0.2.2, TLS server listeners use Go's RequireAnyClientCert mode when skipCAVerification is false. This mode checks that the client holds the certificate's private key but does not verify the certificate against the configured CA. An...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.temporal.io/production-deployment/data-encryption#codec-server-setup
- https://github.com/temporalio/s2s-proxy/blob/v0.2.2/encryption/tls.go#L47-L62
- https://github.com/temporalio/s2s-proxy/commit/d100c2258dbc37d7df51298ea045315f36c7eb3b
- https://github.com/temporalio/s2s-proxy/commit/f1dc6b9a3919d37e82545ab461cbe6bb62618d3c
- https://github.com/temporalio/s2s-proxy/pull/296

### [CVE-2026-90903](https://www.joomshaper.com/easystore)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-90903
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-24 04:19:43 JST
- 更新日: 2026-09-24 05:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla Extension - joomshaper.com - Missing CSRF Token Verification across Administrator AJAX API Endpoints in Easy Store extension 1.0.0-3.0.0 - The administrator ApiController only validated CSRF tokens inside the products() action. All other administrative AJAX endpoints (orders, coupons, media, customers, settings,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.joomshaper.com/easystore

### [CVE-2026-88830](https://access.redhat.com/security/cve/CVE-2026-88830)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-88830
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-24 02:17:18 JST
- 更新日: 2026-09-24 05:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A unit confusion in BusyBox TLS Montgomery reduction buffer allocation causes a pre-authentication heap buffer overflow when processing a crafted ClientKeyExchange message.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-88830
- https://bugzilla.redhat.com/show_bug.cgi?id=2531344

### [CVE-2026-63131](https://github.com/hashicorp/vault/blob/main/CHANGELOG.md#203)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-63131
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-24 04:17:34 JST
- 更新日: 2026-09-24 04:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenBao is an open source identity-based secrets management system. Prior to 2.6.0, OpenBao's vault/policy/acl.go could evaluate a broader wildcard ACL grant before more-specific trailing-wildcard ACL paths with capabilities = ["deny"] for a LIST operation. When a parent path permitted LIST and a child path was denied,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/hashicorp/vault/blob/main/CHANGELOG.md#203
- https://github.com/openbao/openbao/commit/2e9625d6cebe4639d051ef53dd6ce7c49914ae6a
- https://github.com/openbao/openbao/commit/f58d848c139e5ba71aa63103fcfe101972b999fc
- https://github.com/openbao/openbao/pull/3389
- https://github.com/openbao/openbao/pull/3474

### [CVE-2026-92692](https://github.com/sulu/sulu/commit/d19c01487af8c3de2fb3aa145856707a6367392c)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-92692
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-24 04:19:44 JST
- 更新日: 2026-09-24 05:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Sulu is an open-source PHP content management system based on the Symfony framework. Prior to 2.6.25 and 3.0.8, the affected Sulu 2.6 and 3.0 release lines have a Smart Content QueryBuilder in src/Sulu/Component/Content/SmartContent/QueryBuilder.php that concatenates category identifiers from the public categories quer...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/sulu/sulu/commit/d19c01487af8c3de2fb3aa145856707a6367392c
- https://github.com/sulu/sulu/releases/tag/2.6.25
- https://github.com/sulu/sulu/releases/tag/3.0.8
- https://github.com/sulu/sulu/security/advisories/GHSA-jg26-q8hg-3pq4

### [CVE-2026-52744](https://github.com/gocd/gocd/commit/ce9602d7bb27dcb89bf8fc15eb859306cdc8995c)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-52744
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-24 04:17:30 JST
- 更新日: 2026-09-24 04:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GoCD is a continuous deliver server. From 20.2.0 until 26.1.0, the internal GoCD UI fetch-artifact auto-suggestion API at /go/api/internal/pipelines/**/upstream does not adequately authorize access to upstream dependency data. An authenticated user can retrieve inter-pipeline dependency hierarchy details and user-defin...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gocd/gocd/commit/ce9602d7bb27dcb89bf8fc15eb859306cdc8995c
- https://github.com/gocd/gocd/releases/tag/26.1.0
- https://github.com/gocd/gocd/security/advisories/GHSA-mvpm-hmc9-2q8p
- https://www.gocd.org/releases/#26-1-0

### [CVE-2026-77285](https://github.com/openbao/openbao/commit/90272575e5f58b3883fbb0ccb2238e9285722d1a)

> **Backend** / **LOW** / CVSS: **2.4** / KEV: **no**

- タイトル: CVE-2026-77285
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-24 04:19:15 JST
- 更新日: 2026-09-24 05:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenBao is an open source identity-based secrets management system. Prior to 2.6.0, OpenBao Agent's exec rendering mode could write secrets from env_template to standard output when command/agent/exec/exec.go re-created the template runner after repeated rendering failures, primarily after num_retries was reached. A pr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/openbao/openbao/commit/90272575e5f58b3883fbb0ccb2238e9285722d1a
- https://github.com/openbao/openbao/commit/ee3aa4aff72c5176cf02af21eac7158899080878
- https://github.com/openbao/openbao/pull/3494
- https://github.com/openbao/openbao/pull/3495
- https://github.com/openbao/openbao/releases/tag/v2.6.0

### [CVE-2026-55632](https://github.com/gocd/gocd/commit/c93d9e7b32b64257725a7d1c6f148fb571c86c7e)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-55632
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-24 04:17:31 JST
- 更新日: 2026-09-24 05:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GoCD is a continuous deliver server. From 20.2.0 until 26.1.0, the internal pipeline structure API used for autocompletion while editing pipeline, template, environment, and user-preference configuration returns its users-and-roles mode to regular authenticated users without requiring an administrator role. A lower-pri...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gocd/gocd/commit/c93d9e7b32b64257725a7d1c6f148fb571c86c7e
- https://github.com/gocd/gocd/releases/tag/26.1.0
- https://github.com/gocd/gocd/security/advisories/GHSA-57pf-j652-c3c9
- https://www.gocd.org/releases/#26-1-0

### [CVE-2026-92284](https://github.com/caddyserver/caddy/security/advisories/GHSA-j8px-rmrx-76h9)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-92284
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-24 04:19:43 JST
- 更新日: 2026-09-24 05:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Caddy is an extensible server platform that uses TLS by default. In version 2.11.3 and earlier, in modules/caddyhttp/replacer.go, resolving http.request.body reads the complete request body with an unbounded io.Copy before request-body middleware limits apply, allowing memory exhaustion and process termination.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/caddyserver/caddy/security/advisories/GHSA-j8px-rmrx-76h9
- https://github.com/caddyserver/caddy/security/advisories/GHSA-j8px-rmrx-76h9

### [CVE-2026-92700](https://github.com/caddyserver/caddy/security/advisories/GHSA-j8px-rmrx-76h9)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-92700
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-24 04:19:44 JST
- 更新日: 2026-09-24 05:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Caddy is an extensible server platform that uses TLS by default. In version 2.11.3 and earlier, in modules/caddyhttp/fileserver/staticfiles.go, fileHidden() uses case-sensitive filepath.Match checks, so case variants can bypass hide rules on case-insensitive filesystems or when mixed-case paths coexist and expose files...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/caddyserver/caddy/security/advisories/GHSA-j8px-rmrx-76h9
- https://github.com/caddyserver/caddy/security/advisories/GHSA-j8px-rmrx-76h9

### [CVE-2026-77602](https://github.com/OpenC3/cosmos/commit/71943352a28128ef3e7e894319d97a656b5cd4f2)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-77602
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-24 04:19:18 JST
- 更新日: 2026-09-24 04:19:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenC3 COSMOS provides the functionality needed to send commands to and receive data from one or more embedded systems. From 5.1.0 until 7.3.0, authenticated non-administrator users can write content under targets_modified/ that is later executed by multiple configuration paths below the intended code-execution privile...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/OpenC3/cosmos/commit/71943352a28128ef3e7e894319d97a656b5cd4f2
- https://github.com/OpenC3/cosmos/commit/7a1538a4626f82c0d1540fcaa27ffdcbbd71ff81
- https://github.com/OpenC3/cosmos/pull/3488
- https://github.com/OpenC3/cosmos/security/advisories/GHSA-jjq7-m736-w977

### [CVE-2026-77601](https://github.com/OpenC3/cosmos/commit/be70d1d836c83c3b084e768e31a399312d4cbe0b)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-77601
- 関連キーワード: python, gin, redis
- 影響製品: -
- 公開日: 2026-09-24 04:19:18 JST
- 更新日: 2026-09-24 05:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenC3 COSMOS provides the functionality needed to send commands to and receive data from one or more embedded systems. From 5.12.0 until 7.3.0, an authenticated actor can write the pypi_url setting through set_setting at POST /openc3-api/api, then cause OpenC3::PluginModel.install_phase2 in openc3/lib/openc3/models/pl...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/OpenC3/cosmos/commit/be70d1d836c83c3b084e768e31a399312d4cbe0b
- https://github.com/OpenC3/cosmos/pull/3489
- https://github.com/OpenC3/cosmos/security/advisories/GHSA-vp3w-52v9-q57f
- https://github.com/OpenC3/cosmos/security/advisories/GHSA-vp3w-52v9-q57f

### [CVE-2026-79310](https://github.com/lichoin/TraceLoom/blob/main/CVEs/CVE-2026-79310.md)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-79310
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-09-24 01:16:45 JST
- 更新日: 2026-09-24 04:19:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: webpy web.py 0.76 is vulnerable to server-side template injection (SSTI). The template engine can be tricked into executing attacker-controlled template code that built-in security checks are designed to reject. When an application precompiles templates from a directory the attacker can write to and later renders them...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/lichoin/TraceLoom/blob/main/CVEs/CVE-2026-79310.md
- https://github.com/webpy/webpy

### [CVE-2026-71463](https://access.redhat.com/errata/RHSA-2026:71113)

> **Backend** / **LOW** / CVSS: **2.7** / KEV: **no**

- タイトル: CVE-2026-71463
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-24 04:19:03 JST
- 更新日: 2026-09-24 08:18:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Notification template Jinja AST whitelist only inspects static Getattr nodes. Dynamic subscripts (job['job'+'_env']) and {% if job.id > 100 %} conditional gating bypass both the AST check and the test-render (stub has small job.id). At runtime, the gated branch executes and exceptions write full tracebacks into notific...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/errata/RHSA-2026:71113
- https://access.redhat.com/security/cve/CVE-2026-71463
- https://bugzilla.redhat.com/show_bug.cgi?id=2512372

### [CVE-2026-93421](https://github.com/mesop-dev/mesop/commit/f38c42a1d3eba246941ef8d7f645072d53c58785)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-93421
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-24 04:19:45 JST
- 更新日: 2026-09-24 05:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mesop is a Python-based UI framework that allows users to build web applications. Prior to 1.3.4, the unauthenticated /__csp__ endpoint passes attacker-controlled document-uri, blocked-uri, and violated-directive values to the csp_report handler in mesop/server/static_file_serving.py, which prints them to standard outp...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mesop-dev/mesop/commit/f38c42a1d3eba246941ef8d7f645072d53c58785
- https://github.com/mesop-dev/mesop/pull/1397
- https://github.com/mesop-dev/mesop/releases/tag/v1.3.4
- https://github.com/mesop-dev/mesop/security/advisories/GHSA-g7f6-rxc4-qhph

### [CVE-2026-96672](https://github.com/frappe/erpnext)

> **Backend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-96672
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-24 01:16:49 JST
- 更新日: 2026-09-24 01:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Frappe ERPNext versions before 16.34.1 fail to validate that Financial Report Template calculation_formula values reference whitelisted methods before passing them to frappe.call(). Accounts Managers can supply arbitrary dotted Python paths to invoke non-whitelisted internal server-side methods and read their return va...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/frappe/erpnext
- https://github.com/frappe/erpnext/blob/v16.34.0/erpnext/accounts/doctype/financial_report_template/financial_report_engine.py#L1166-L1171
- https://github.com/frappe/erpnext/blob/v16.34.0/erpnext/accounts/doctype/financial_report_template/financial_report_template.json
- https://github.com/frappe/erpnext/commit/7aad59b129711e9bba17b25665428d1fc57bf37c
- https://github.com/frappe/erpnext/security/advisories/GHSA-794x-fhm7-58j7

### [CVE-2026-6669](https://www.pgbouncer.org/changelog.html)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-6669
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-09-24 02:17:16 JST
- 更新日: 2026-09-24 04:40:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Missing upper bound on the key derivation iteration count accepted during SCRAM authentication to a backend server in PgBouncer through 1.25.2 allows a malicious or compromised PostgreSQL backend to cause uncontrolled CPU consumption in PgBouncer. The resulting key derivation cannot be interrupted in frontend builds su...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.pgbouncer.org/changelog.html

### [CVE-2025-63564](http://moodle.com)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2025-63564
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-24 02:17:14 JST
- 更新日: 2026-09-24 05:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SQL injection vulnerability in Moodle Socialwall plugin v.3.0 through v.3.3 allows an attacker to execute arbitrary code via crafted HTTP requests
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- http://moodle.com
- https://medium.com/@lcrawfqrd/sqli-in-moodle-plugin-9f0ce4eb05f2

### [CVE-2026-84502](https://access.redhat.com/errata/RHSA-2026:71113)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-84502
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-24 04:19:40 JST
- 更新日: 2026-09-24 07:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw was found in Red Hat Ansible Automation Platform's automation- controller. The Project scm_url field is not validated against values that begin with a dash and is stored and passed verbatim to the git SCM module. Because the module runs git ls-remote with the URL as a positional argument and without a "--" separ...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/errata/RHSA-2026:71113
- https://access.redhat.com/errata/RHSA-2026:71115
- https://access.redhat.com/security/cve/CVE-2026-84502
- https://bugzilla.redhat.com/show_bug.cgi?id=2527096

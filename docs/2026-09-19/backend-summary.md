# Backend CVE Summary (2026-09-19)

## Overview

- 取得日時: 2026-09-19 09:14:05 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 21
- Critical: 3
- High: 8
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-93559](https://github.com/Forget-C/Jellyfish/issues/37)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-93559
- 関連キーワード: fastapi
- 影響製品: -
- 公開日: 2026-09-19 02:17:06 JST
- 更新日: 2026-09-19 04:14:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was identified in Forget-C Jellyfish AI Short Drama Studio 0.1.0-alpha/0.2.0/0.3.0/0.3.1/0.3.2. This affects an unknown function of the file backend/app/dependencies.py of the component FastAPI. The manipulation leads to missing authentication. It is possible to initiate the attack remotely. The reporte...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Forget-C/Jellyfish/issues/37
- https://vuldb.com/cve/CVE-2026-93559
- https://vuldb.com/submit/943920
- https://vuldb.com/vuln/407460
- https://vuldb.com/vuln/407460/cti

### [CVE-2023-54399](https://cn-sec.com/archives/1861976.html)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2023-54399
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 04:16:40 JST
- 更新日: 2026-09-19 04:16:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Hongjing e-HR before 8.2 contains a SQL injection vulnerability in the /servlet/codesettree endpoint where the categories query parameter is passed to a database query without sanitization after HRMS-encoding is stripped. An unauthenticated remote attacker can supply a crafted UNION SELECT payload to read arbitrary dat...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cn-sec.com/archives/1861976.html
- https://www.cloudsek.com/blog/mozi-resurfaces-as-androxgh0st-botnet-unraveling-the-latest-exploitation-wave
- https://www.cnblogs.com/pursue-security/p/17704093.html
- https://www.cnvd.org.cn/flaw/show/CNVD-2023-08743
- https://www.vulncheck.com/advisories/hongjing-e-hr-sql-injection-via-servlet-codesettree

### [CVE-2026-93762](https://jira.mongodb.org/browse/MONGOID-5973)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-93762
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 03:18:35 JST
- 更新日: 2026-09-19 04:05:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mongoid contains an unsafe reflection weakness in the query path used for embedded documents. An application that passes an externally supplied field name to certain in-memory query methods may allow an unauthenticated party to obtain unintended disclosure of stored document data and to permanently remove stored record...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/MONGOID-5973

### [CVE-2026-93765](https://jira.mongodb.org/browse/MONGOID-5973)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-93765
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 02:17:07 JST
- 更新日: 2026-09-19 04:05:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mongoid contains an unsafe reflection weakness in the document persistence layer of its object-document mapping code. Input whose keys are passed through from an unauthenticated party by an embedding application can cause unintended internal method invocation instead of the intended array field update. This may result...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/MONGOID-5973

### [CVE-2026-81505](https://github.com/frain-dev/convoy/commit/1cc67cd16fb1f8890cc83a3998d3f92dceb7fd06)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-81505
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 02:17:02 JST
- 更新日: 2026-09-19 03:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Convoy is a cloud native webhooks gateway. Prior to 26.6.8, Convoy's GET /api/v1/projects/{projectID}/sources/{sourceID} endpoint authorizes access to the project in the URL, but Handler.GetSource calls sources.Service.FindSourceByID() and fetches the Source only by sourceID without confirming that its ProjectID matche...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/frain-dev/convoy/commit/1cc67cd16fb1f8890cc83a3998d3f92dceb7fd06
- https://github.com/frain-dev/convoy/pull/2755
- https://github.com/frain-dev/convoy/releases/tag/v26.6.8
- https://github.com/frain-dev/convoy/security/advisories/GHSA-p5vg-v7mj-f6q4
- https://github.com/frain-dev/convoy/security/advisories/GHSA-p5vg-v7mj-f6q4

### [CVE-2026-61672](https://github.com/projectcapsule/capsule/commit/755cef54bf4a1bc56d6692130132bc70755bef46)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-61672
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-09-19 02:16:58 JST
- 更新日: 2026-09-19 02:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Capsule is a multi-tenancy and policy-based framework for Kubernetes. Prior to 0.13.7, ForbiddenListSpec.ExactMatch in pkg/api/forbidden_list.go sorts denied metadata keys case-insensitively and then uses sort.SearchStrings, which assumes byte-order sorting. When an administrator's forbidden list mixes capitalized and...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/projectcapsule/capsule/commit/755cef54bf4a1bc56d6692130132bc70755bef46
- https://github.com/projectcapsule/capsule/pull/1982
- https://github.com/projectcapsule/capsule/releases/tag/v0.13.7
- https://github.com/projectcapsule/capsule/security/advisories/GHSA-gjw4-3v3v-rqxg

### [CVE-2026-93758](https://jira.mongodb.org/browse/MONGOID-5992)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-93758
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-19 02:17:07 JST
- 更新日: 2026-09-19 04:05:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An insecure direct object reference in the nested attributes handling of the Mongoid object-document mapper may allow a user with basic application privileges to reference a record identifier that is not their own. Processing such a request can cause that record to be looked up without the usual ownership or scoping re...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/MONGOID-5992

### [CVE-2026-93761](https://jira.mongodb.org/browse/MONGOID-5981)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-93761
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-09-19 03:18:34 JST
- 更新日: 2026-09-19 04:05:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An inefficient regular expression complexity issue in the in-memory query evaluation component of the Mongoid library may allow an unauthenticated party to cause excessive processing within an embedding application process. Applications that place user-supplied text into a pattern-matching query condition on an embedde...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/MONGOID-5981

### [CVE-2026-61794](https://github.com/projectcapsule/capsule/commit/8d89d6865df6f41c7faa22fc9e807a57b01bfd0e)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-61794
- 関連キーワード: go, express, kubernetes
- 影響製品: -
- 公開日: 2026-09-19 02:16:58 JST
- 更新日: 2026-09-19 02:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Capsule is a multi-tenancy and policy-based framework for Kubernetes. From 0.13.0 until 0.13.7, the Tenant update validation in internal/webhook/tenant/validation/forbidden_annotations_regex.go compiles ForbiddenLabels.Regex for both the labels and annotations checks instead of validating ForbiddenAnnotations.Regex. An...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/projectcapsule/capsule/commit/8d89d6865df6f41c7faa22fc9e807a57b01bfd0e
- https://github.com/projectcapsule/capsule/pull/1983
- https://github.com/projectcapsule/capsule/releases/tag/v0.13.7
- https://github.com/projectcapsule/capsule/security/advisories/GHSA-gxjc-74v5-3vx3

### [CVE-2026-61795](https://github.com/projectcapsule/capsule/commit/8d89d6865df6f41c7faa22fc9e807a57b01bfd0e)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-61795
- 関連キーワード: go, express, kubernetes
- 影響製品: -
- 公開日: 2026-09-19 02:16:58 JST
- 更新日: 2026-09-19 02:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Capsule is a multi-tenancy and policy-based framework for Kubernetes. From 0.13.0 until 0.13.7, hostnameRegexHandler.OnUpdate in internal/webhook/tenant/validation/hostname_regex.go reverses the new and old Tenant parameters and validates the previous AllowedHostnames.Regex instead of the submitted value. A cluster adm...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/projectcapsule/capsule/commit/8d89d6865df6f41c7faa22fc9e807a57b01bfd0e
- https://github.com/projectcapsule/capsule/pull/1983
- https://github.com/projectcapsule/capsule/releases/tag/v0.13.7
- https://github.com/projectcapsule/capsule/security/advisories/GHSA-f94q-w3w8-cj67

### [CVE-2026-61833](https://github.com/project-zot/zot/commit/7bb211bcd4352b90f3e99752607fbd1f050bf7ca)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-61833
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 02:16:59 JST
- 更新日: 2026-09-19 02:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: zot is a container image and artifact registry based on the Open Container Initiative Distribution Specification. Prior to 2.1.18, the bearer authentication handler in pkg/api/authn.go maps every HTTP method other than GET and HEAD to the push action, so DELETE requests are not checked for the distinct delete permissio...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/project-zot/zot/commit/7bb211bcd4352b90f3e99752607fbd1f050bf7ca
- https://github.com/project-zot/zot/pull/4161
- https://github.com/project-zot/zot/releases/tag/v2.1.18
- https://github.com/project-zot/zot/security/advisories/GHSA-qg67-7m6v-qg25

### [CVE-2026-93760](https://jira.mongodb.org/browse/MONGOID-5994)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-93760
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 03:18:34 JST
- 更新日: 2026-09-19 04:05:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mongoid does not restrict which query operators may come from caller-supplied filter data when an application hands that data to its query-building methods. In an application that forwards externally supplied filter parameters in this way, a party with no credentials may influence how the database evaluates the query....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/MONGOID-5994

### [CVE-2026-93764](https://jira.mongodb.org/browse/MONGOID-5989)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-93764
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 03:18:35 JST
- 更新日: 2026-09-19 04:05:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mongoid may omit encryption rules for fields declared on embedded models when generating the client-side field-level encryption schema. Applications that enable this feature can therefore store values intended to be encrypted in readable form, with no error or warning. A party with routine read access to the database,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/MONGOID-5989

### [CVE-2026-63406](https://github.com/anycable/anycable/commit/201c67e99e463ed63bd6b345562f4c458385fcee)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-63406
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 02:16:59 JST
- 更新日: 2026-09-19 03:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AnyCable is a realtime server for reliable two-way communication that supports any backend. Prior to 1.6.15, the telemetry subsystem in telemetry/config.go enables tracking with a hardcoded public authToken, while clusterFingerprint in telemetry/telemetry.go reads the full configuration file and raw os.Args returned by...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/anycable/anycable/commit/201c67e99e463ed63bd6b345562f4c458385fcee
- https://github.com/anycable/anycable/releases/tag/v1.6.15
- https://github.com/anycable/anycable/security/advisories/GHSA-w72w-9qmj-c9qm
- https://github.com/anycable/anycable/security/advisories/GHSA-w72w-9qmj-c9qm

### [CVE-2026-93685](https://access.redhat.com/security/cve/CVE-2026-93685)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-93685
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 00:17:22 JST
- 更新日: 2026-09-19 04:06:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw was found in the multicluster-observability-addon. A remote attacker can access a debug endpoint without authentication, due to a misconfiguration in the underlying addon-framework library. This allows for the disclosure of sensitive operational information, such as goroutine, heap, and command-line details, aft...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-93685
- https://bugzilla.redhat.com/show_bug.cgi?id=2518377

### [CVE-2026-77339](https://github.com/F1bonacc1/process-compose/commit/6ffa74f462cd2fa4f8dc1ee63c70b793b298c858)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-77339
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-19 02:17:00 JST
- 更新日: 2026-09-19 02:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Process Compose is a scheduler and orchestrator for non-containerized applications. Prior to 1.120.0, the MCP SSE listener in src/mcp/server.go accepts browser-origin requests to /sse and the returned message endpoint without validating the Host header, validating the Origin header, or authenticating the caller. When M...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/F1bonacc1/process-compose/commit/6ffa74f462cd2fa4f8dc1ee63c70b793b298c858
- https://github.com/F1bonacc1/process-compose/releases/tag/v1.120.0
- https://github.com/F1bonacc1/process-compose/security/advisories/GHSA-5gm3-9crp-6g3v
- https://github.com/F1bonacc1/process-compose/security/advisories/GHSA-5gm3-9crp-6g3v

### [CVE-2026-77386](https://github.com/zoriya/Kyoo/commit/02ab3af8127a081295fd7bed103847173c0d7632)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-77386
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-19 03:17:14 JST
- 更新日: 2026-09-19 03:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Kyoo is a self-hosted media server focused on movies, series, and anime. Prior to 5.1.0, an unauthenticated attacker could initiate the OIDC login flow with an attacker-controlled redirectUrl. The login handling in auth/oidc.go stored that URL with the opaque login state, and /auth/oidc/logged/{provider} appended the p...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zoriya/Kyoo/commit/02ab3af8127a081295fd7bed103847173c0d7632
- https://github.com/zoriya/Kyoo/pull/1576
- https://github.com/zoriya/Kyoo/releases/tag/v5.1.0
- https://github.com/zoriya/Kyoo/security/advisories/GHSA-xhg6-v78p-xf44

### [CVE-2026-54147](https://github.com/http4k/http4k/commit/65d23d99fc5afbe34f29d8f61d0a003fbebb381c)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-54147
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 01:17:06 JST
- 更新日: 2026-09-19 03:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: http4k is a functional toolkit for Kotlin HTTP applications. Prior to 4.51.0.0, 5.42.0.0, and 6.50.0.0, DigestAuthProvider.verify in http4k-security-digest ignores its configured algorithm parameter and verifies every Digest response with hardcoded MD5. Deployments configured for SHA-256 therefore receive weaker MD5-ba...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/http4k/http4k/commit/65d23d99fc5afbe34f29d8f61d0a003fbebb381c
- https://github.com/http4k/http4k/releases/tag/6.50.0.0
- https://github.com/http4k/http4k/security/advisories/GHSA-vxxm-wwqh-mh47

### [CVE-2026-63405](https://github.com/anycable/anycable/commit/d2cbadec792f038f4695c84a65c0d957b0fde72c)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-63405
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 02:16:59 JST
- 更新日: 2026-09-19 03:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AnyCable is a realtime server for reliable two-way communication that supports any backend. Prior to 1.6.15, the Pusher-compatible REST API in pusher/http.go includes the caller-supplied body_md5 value in the HMAC input but does not calculate the digest of the received request body or compare it with the signed value....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/anycable/anycable/commit/d2cbadec792f038f4695c84a65c0d957b0fde72c
- https://github.com/anycable/anycable/releases/tag/v1.6.15
- https://github.com/anycable/anycable/security/advisories/GHSA-5p54-whvp-x327
- https://github.com/anycable/anycable/security/advisories/GHSA-5p54-whvp-x327

### [CVE-2026-75883](https://github.com/ppp-project/ppp/security/advisories/GHSA-rwr9-4vx8-vc35)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-75883
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 01:17:09 JST
- 更新日: 2026-09-19 04:06:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The code in pppd that formats a response to a PEAP Request packet in peap_response() copies an entire TLS record of up to 16384 bytes into the fixed global buffer outpacket_buf without checking the available space and without implementing outgoing PEAP fragmentation. Thus a pppd process connecting to a server which req...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/ppp-project/ppp/security/advisories/GHSA-rwr9-4vx8-vc35

### [CVE-2026-81946](https://www.planet.com.tw/en/support/security-advisory/11)

> **Backend** / **MEDIUM** / CVSS: **6.7** / KEV: **no**

- タイトル: CVE-2026-81946
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-19 01:17:11 JST
- 更新日: 2026-09-19 01:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PLANET IGS-5225-8P2T4S industrial managed switch V1 and V2 firmware versions before 1.2412b260707 and 2.2412b260519 use MD5-based password hashing, a cryptographic algorithm with known weaknesses. An attacker who obtains the device configuration file can recover the privileged-mode access password.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.planet.com.tw/en/support/security-advisory/11
- https://www.vulncheck.com/advisories/planet-igs-5225-8p2t4s-v1-v2-weak-password-hashing-via-md5-algorithm

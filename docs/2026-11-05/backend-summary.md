# Backend CVE Summary (2026-11-05)

## Overview

- 取得日時: 2026-11-05 11:18:45 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 14
- Critical: 2
- High: 6
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-122224](https://github.com/catborise/webvirtcloud/commit/1227674d8f5a5230e5c654267773aca4ebc5c717)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-122224
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-11-05 06:18:10 JST
- 更新日: 2026-11-05 06:18:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WebVirtCloud through commit bb920b0 contains a missing authorization vulnerability that allows low-privileged authenticated users to reach MigrateViewSet and CreateInstanceViewSet because no permission_classes are declared, so Django REST Framework defaults to AllowAny. Attackers can send requests to /api/v1/migrate/ o...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/catborise/webvirtcloud/commit/1227674d8f5a5230e5c654267773aca4ebc5c717
- https://github.com/retspen/webvirtcloud
- https://github.com/retspen/webvirtcloud/blob/bb920b0a7ffdf00c09e994dc2e45f05bc9ec1bb3/instances/api/viewsets.py#L125-L162
- https://github.com/retspen/webvirtcloud/blob/bb920b0a7ffdf00c09e994dc2e45f05bc9ec1bb3/instances/api/viewsets.py#L174-L183
- https://github.com/retspen/webvirtcloud/issues/689

### [CVE-2026-115770](https://github.com/pocket-id/pocket-id/commit/43aaccd5bfacb76283b11ce039fb3f0716196fcb)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-115770
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-05 08:17:18 JST
- 更新日: 2026-11-05 08:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Pocket ID is an OIDC provider that allows users to authenticate with their passkeys to services. From 2.2.0 until 2.12.0, SendEmailVerification uses the token model in backend/internal/model/email_verification_token.go to bind an email-verification token only to the user's identifier, while UpdateUser can change the ac...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pocket-id/pocket-id/commit/43aaccd5bfacb76283b11ce039fb3f0716196fcb
- https://github.com/pocket-id/pocket-id/pull/1625
- https://github.com/pocket-id/pocket-id/releases/tag/v2.12.0
- https://github.com/pocket-id/pocket-id/security/advisories/GHSA-rm8c-2cv8-jwf6

### [CVE-2026-121966](https://github.com/traefik/traefik/security/advisories/GHSA-hrpp-p4fc-wwf8)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-121966
- 関連キーワード: go, gin, nginx, traefik
- 影響製品: -
- 公開日: 2026-11-05 01:17:50 JST
- 更新日: 2026-11-05 04:17:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Traefik 2.x before 2.11.60 and 3.x before 3.7.16 sends ForwardAuth subrequests (and, in 3.7, Ingress NGINX auth-url requests) through an auth-server connection pool shared by all clients, exposing connection-bound NTLM or Negotiate authentication. An unauthenticated attacker can reuse another user's authenticated conne...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/traefik/traefik/security/advisories/GHSA-hrpp-p4fc-wwf8
- https://www.vulncheck.com/advisories/traefik-before-2.11.60-and-3.7.16-forwardauth-ntlm-negotiate-identity-leak

### [CVE-2026-102339](https://github.com/telepresenceio/telepresence/commit/1312482488b771742dbedd3015f9a81a27532de6)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-102339
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-11-05 06:17:40 JST
- 更新日: 2026-11-05 06:17:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Telepresence enables local development against a remote Kubernetes or OpenShift cluster. Prior to 2.31.0, the Traffic Manager Tunnel gRPC streaming endpoint parses a session ID from the first bytes of a caller-controlled message in pkg/tunnel/message.go and passes it to state.Tunnel without verifying that the caller ow...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/telepresenceio/telepresence/commit/1312482488b771742dbedd3015f9a81a27532de6
- https://github.com/telepresenceio/telepresence/commit/36458b65a010d2b316af48cd90e193ba190785d9
- https://github.com/telepresenceio/telepresence/pull/4217
- https://github.com/telepresenceio/telepresence/releases/tag/v2.31.0
- https://github.com/telepresenceio/telepresence/security/advisories/GHSA-6j3h-rp73-6rvf

### [CVE-2026-102664](https://github.com/sysown/proxysql/commit/396c742f7d50b1f479e1157e296ee9d0aff1b724)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-102664
- 関連キーワード: go, postgresql, mysql
- 影響製品: -
- 公開日: 2026-11-05 06:17:41 JST
- 更新日: 2026-11-05 06:17:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ProxySQL is a proxy for MySQL and its forks, as well as PostgreSQL. Prior to 3.0.10, 3.1.10, and 4.0.10, decompress_mysql_payload() in lib/mysql_data_stream.cpp accepts a zlib stream when uncompress() returns Z_OK without checking that the actual output length equals the attacker-controlled payload_length. An authentic...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/sysown/proxysql/commit/396c742f7d50b1f479e1157e296ee9d0aff1b724
- https://github.com/sysown/proxysql/commit/a8c1cef4d44c4beea7f6aa21b8a09a7cb8c75520
- https://github.com/sysown/proxysql/releases/tag/v3.0.10
- https://github.com/sysown/proxysql/releases/tag/v3.1.10
- https://github.com/sysown/proxysql/releases/tag/v4.0.10

### [CVE-2026-121960](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-3pg4-5r42-wxvj)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-121960
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-05 01:17:48 JST
- 更新日: 2026-11-05 04:17:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreeRDP before 3.32.2 contains a denial of service vulnerability in the NLA-enabled shadow server when a CredSSP TSRequest omits negoTokens. Unauthenticated attackers can send a crafted seven-byte TSRequest containing only the version field to trigger a fatal WINPR_ASSERT and abort the server process.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-3pg4-5r42-wxvj
- https://www.vulncheck.com/advisories/freerdp-before-3.32.2-unauthenticated-denial-of-service-via-credssp-tsrequest
- https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-3pg4-5r42-wxvj

### [CVE-2026-54383](https://github.com/je-lv/vitafit-security-research)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-54383
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-05 08:17:48 JST
- 更新日: 2026-11-05 08:17:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: VitaFit cloud API before 2026-10-30 contained an excessive data exposure vulnerability that allows any authenticated user to query the GET /front/relation/search/ endpoint and retrieve PII and health-related profile information for user records. Attackers can enumerate the user directory using overlapping alphanumeric...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/je-lv/vitafit-security-research
- https://play.google.com/store/apps/details?id=com.vt.vitafit
- https://www.vulncheck.com/advisories/vitafit-cloud-api-excessive-data-exposure-via-relation-search-endpoint

### [CVE-2026-106554](https://github.com/FasterXML/jackson-dataformats-binary/security/advisories/GHSA-cjg7-h3pr-p927)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-106554
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-05 01:17:32 JST
- 更新日: 2026-11-05 01:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: One CBOR-parsing issue in jackson-dataformats-binary's CBOR module: an unbounded run of CBOR tags drives quadratic-time TagList growth (CPU/GC-exhaustion DoS, PoC-proven). PoC executed against com.fasterxml.jackson.dataformat:jackson-dataformat-cbor:2.18.2; present in current 2.x and 3.x (tools.jackson.dataformat.cbor)...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FasterXML/jackson-dataformats-binary/security/advisories/GHSA-cjg7-h3pr-p927

### [CVE-2026-115473](https://github.com/cesanta/mongoose/commit/b55de8b151d1466a3e41d1f854f22eeb6faa23dc)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-115473
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-05 07:17:50 JST
- 更新日: 2026-11-05 07:17:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mongoose is an embedded web server and network library. Prior to 7.22, mg_path_is_sane in src/util.c read path.buf[1] without first requiring path.len to be at least two and read s[2] when only two bytes remained. Unauthenticated remote requests reaching mg_http_upload or mg_http_serve_dir with the affected short path...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/cesanta/mongoose/commit/b55de8b151d1466a3e41d1f854f22eeb6faa23dc
- https://github.com/cesanta/mongoose/releases/tag/7.22
- https://github.com/cesanta/mongoose/security/advisories/GHSA-cjmx-764f-286c

### [CVE-2026-121007](https://github.com/dbsrgits/sql-abstract/commit/79fc34e874b4edb441154eccddb04c57d5c1c90e.patch)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-121007
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-11-05 00:17:41 JST
- 更新日: 2026-11-05 00:17:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SQL::Abstract versions from 1.90_01 before 2.000001_04 for Perl allow SQL injection via the where values of a nested statement in an identifier position. A nested statement such as { -select => ... } in a position where plain scalars are identifiers treats its own plain scalars as identifiers too. These positions are t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dbsrgits/sql-abstract/commit/79fc34e874b4edb441154eccddb04c57d5c1c90e.patch
- https://metacpan.org/release/GETTY/SQL-Abstract-2.000001_04/changes

### [CVE-2026-122132](https://github.com/go-chi/chi)

> **Backend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-122132
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-05 06:18:08 JST
- 更新日: 2026-11-05 06:18:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: go-chi chi 5.2.2 through 5.5.0 contains an open redirect vulnerability in the RedirectSlashes middleware that allows attackers to redirect victims to external hosts by embedding tab characters in request paths. Attackers can craft links with a URL-encoded tab, which browsers strip from the 301 Location header and resol...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/go-chi/chi
- https://github.com/go-chi/chi/blob/v5.5.0/middleware/strip.go#L41-L69
- https://github.com/go-chi/chi/pull/1238
- https://github.com/go-chi/chi/security/advisories/GHSA-mqqf-5wvp-8fh8
- https://www.vulncheck.com/advisories/go-chi-chi-5.2.2-through-5.5.0-open-redirect-via-redirectslashes-middleware

### [CVE-2026-122139](https://github.com/blueprintue/blueprintue-self-hosted-edition/blob/v4.3.2/app/middlewares/ForgotPasswordMiddleware.php#L130-L157)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-122139
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-05 06:18:10 JST
- 更新日: 2026-11-05 06:18:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: blueprintUE Self-Hosted Edition before 4.3.3 contains an account enumeration vulnerability in ForgotPasswordMiddleware.php that allows unauthenticated attackers to identify registered email addresses. Attackers can compare password reset redirect targets for submitted emails, and failed lookups are never rate-limited,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/blueprintue/blueprintue-self-hosted-edition/blob/v4.3.2/app/middlewares/ForgotPasswordMiddleware.php#L130-L157
- https://github.com/blueprintue/blueprintue-self-hosted-edition/commit/45832742182a6c4438a0d58de95ba9c7686851f2
- https://github.com/blueprintue/blueprintue-self-hosted-edition/pull/265
- https://github.com/blueprintue/blueprintue-self-hosted-edition/releases/tag/v4.3.3
- https://github.com/blueprintue/blueprintue-self-hosted-edition/security/advisories/GHSA-fwgq-c3c6-p67j

### [CVE-2026-121009](https://github.com/dbsrgits/sql-abstract/commit/b6e7d991ac588b937e8943a5b28b6837ff276a51.patch)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-121009
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-05 00:17:42 JST
- 更新日: 2026-11-05 00:17:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SQL::Abstract versions from 1.90_01 before 2.000001_04 for Perl skip the injection_guard check for function names given with -func. injection_guard is documented to apply to every function name, but only the { -name => ... } shorthand goes through it. The explicit { -func => [ $name, ... ] } form puts $name into the SQ...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dbsrgits/sql-abstract/commit/b6e7d991ac588b937e8943a5b28b6837ff276a51.patch
- https://metacpan.org/release/GETTY/SQL-Abstract-2.000001_04/changes

### [CVE-2026-97693](https://github.com/xerrors/Yuxi/commit/b5b5713e6e639dd4ed2ebce41579a3c458347663)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-97693
- 関連キーワード: postgresql, docker
- 影響製品: -
- 公開日: 2026-11-05 07:18:07 JST
- 更新日: 2026-11-05 07:18:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Yuxi is a large-model-based intelligent knowledge base and knowledge graph agent development platform. From 0.6.0.beta1 until 0.7.1, there is insufficient isolation between execution-capable Docker sandboxes and trusted application services. A low-privileged authenticated user who can execute commands in their own sand...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/xerrors/Yuxi/commit/b5b5713e6e639dd4ed2ebce41579a3c458347663
- https://github.com/xerrors/Yuxi/security/advisories/GHSA-qpm5-6332-9445

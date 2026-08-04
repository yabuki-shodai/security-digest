# Backend CVE Summary (2026-08-05)

## Overview

- 取得日時: 2026-08-05 08:15:42 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 14
- Critical: 4
- High: 2
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-15307](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-15307
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-08-05 02:16:46 JST
- 更新日: 2026-08-05 03:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An issue was discovered in Django 5.2 before 5.2.17 and 6.0 before 6.0.8. GeoDjango spatial lookups optimistically parse the right-hand-side value as a raster by passing it to the `django.contrib.gis.gdal.GDALRaster` constructor. Any value used in a spatial lookup against a `GeometryField` or `RasterField` reaches this...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://github.com/django/django/commit/115ffd0463a765ab1cc93de18e94b5459b8a300e
- https://github.com/django/django/commit/208f80cb682868b584ed0a78f23e4ba6304212aa
- https://github.com/django/django/commit/39b3e2d0c743a338def6c473086ebc06865e86b6
- https://github.com/django/django/commit/f1949c1f9758947ade984c895ff16bef46f56520

### [CVE-2026-15337](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-15337
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-08-05 02:16:46 JST
- 更新日: 2026-08-05 03:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An issue was discovered in Django 5.2 before 5.2.17 and 6.0 before 6.0.8. `django.utils.translation.check_for_language()` is subject to a potential denial-of-service attack when given many distinct, very long language codes, which are retained as keys in an in-memory cache and consume process memory. Such codes reach t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://github.com/django/django/commit/224dbc832586ad5cfb0237c2ff30d14baeaddc6f
- https://github.com/django/django/commit/27137e655e442e81095f1f8f77ff3870d9fdf169
- https://github.com/django/django/commit/5b3523d29be25948e1dd90b3863a002f00fc865f
- https://github.com/django/django/commit/c72a5dbb64d0777f3f471f1be94e8b2ca91e0959

### [CVE-2026-15830](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-15830
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-08-05 02:16:46 JST
- 更新日: 2026-08-05 03:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An issue was discovered in Django 5.2 before 5.2.17 and 6.0 before 6.0.8. GeoDjango's `django.contrib.gis.geos.GEOSGeometry` is subject to a potential denial-of-service when parsing deeply nested `GEOMETRYCOLLECTION` objects supplied as well-known text (WKT), well-known binary (WKB), or hex-encoded WKB, which triggers...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://github.com/django/django/commit/6af5da31775417c610dbf9c3f1b5b8333d42daf6
- https://github.com/django/django/commit/9e4a3f186b6b07b483bfd9195ea06734663fcd06
- https://github.com/django/django/commit/ba80833fa656dd09660b97c4429331067db1b080
- https://github.com/django/django/commit/d2e59b77fe18de318a8272c2a7bbc798d84d1d0d

### [CVE-2026-15920](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-15920
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-08-05 02:16:46 JST
- 更新日: 2026-08-05 03:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An issue was discovered in Django 5.2 before 5.2.17 and 6.0 before 6.0.8. `django.contrib.admin.utils.display_for_field()` renders `URLField` values as clickable links in the admin without validating the URL. A value stored with an unsafe scheme is displayed as a link on changelist and read-only admin pages, which allo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://github.com/django/django/commit/13debb622a32720bda1bccda7622fd14fbf3931b
- https://github.com/django/django/commit/47511a21026cdd721d8fbf8571cc079bc38bb46d
- https://github.com/django/django/commit/5a260d309a4c8010c2ebda24eb758a5d95e2508a
- https://github.com/django/django/commit/b9adb81339cc418f8f56b1050cca6dfec3ab6349

### [CVE-2026-45538](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-37wc-5j8j-95x3)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-45538
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-05 06:16:36 JST
- 更新日: 2026-08-05 06:16:36 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenSIPS is a Session Initiation Protocol (SIP) server implementation. In versions 4.0.0 and prior, processing a SIP message with a header name longer than 255 bytes causes a stack buffer overflow when sip_to_json() is called in the routing script. Function sip_to_json() (modules/sipmsgops/sipmsgops.c) copies SIP heade...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/OpenSIPS/opensips/security/advisories/GHSA-37wc-5j8j-95x3

### [CVE-2026-48121](https://github.com/langchain-ai/langgraphjs/commit/284226c7ca164b3c81fe2d9e32b10f1fc6b99a3c)

> **Backend** / **MEDIUM** / CVSS: **6.7** / KEV: **no**

- タイトル: CVE-2026-48121
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-08-05 02:16:55 JST
- 更新日: 2026-08-05 05:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: @langchain/langgraph-checkpoint-mongodb provides a LangGraph.js CheckpointSaver implementation that uses MongoDB for storage. Versions 1.3.0 and below are vulnerable to NoSQL injection: checkpoint identifiers (thread_id, checkpoint_ns, checkpoint_id) from config.configurable are passed into MongoDB find() queries in Mo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/langchain-ai/langgraphjs/commit/284226c7ca164b3c81fe2d9e32b10f1fc6b99a3c
- https://github.com/langchain-ai/langgraphjs/issues/2351
- https://github.com/langchain-ai/langgraphjs/security/advisories/GHSA-98xf-r82g-9mhx

### [CVE-2026-48154](https://github.com/pilinux/gorest/commit/117ff55fc21b47442da07c44c30b403af2da407b)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-48154
- 関連キーワード: go, golang, gin
- 影響製品: -
- 公開日: 2026-08-05 05:16:52 JST
- 更新日: 2026-08-05 05:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: GoRest is a Golang starter kit built with the Gin framework for prototyping and developing RESTful APIs. In versions prior to 1.12.2 nMemorySecret2FA contains a race condition due to an unsynchronized package-level map used to store 2FA secrets. Multiple HTTP handlers in handler/login.go and handler/twoFA.go read from...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pilinux/gorest/commit/117ff55fc21b47442da07c44c30b403af2da407b
- https://github.com/pilinux/gorest/pull/391
- https://github.com/pilinux/gorest/security/advisories/GHSA-cpwg-x64r-rgwg

### [CVE-2026-66901](https://github.com/GoogleCloudPlatform/google-auth-library-perl/commit/9b5157062acc605ca9e6c507b910587f4829ce9e.patch)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-66901
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-05 06:16:37 JST
- 更新日: 2026-08-05 06:16:37 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Google::Auth versions before 0.09 for Perl allow server side request forgery and credential exfiltration via unvalidated URLs taken from the credentials JSON. The URLs the library requests are read from the credentials JSON, and their hosts were not checked against the universe domain before the request. For an externa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/GoogleCloudPlatform/google-auth-library-perl/commit/9b5157062acc605ca9e6c507b910587f4829ce9e.patch
- https://github.com/GoogleCloudPlatform/google-auth-library-perl/commit/c95c77e70bec94f17e239d88050f843ea1cade95.patch
- https://github.com/GoogleCloudPlatform/google-auth-library-perl/commit/cbbb07804e3f8cc7cf9638ecc9c2097d80a9ef50.patch
- https://github.com/GoogleCloudPlatform/google-auth-library-perl/commit/cd42bdef53afcc4531161e85e91d0d5997e01324.patch
- https://metacpan.org/release/CJCOLLIER/Google-Auth-0.09/changes

### [CVE-2026-66902](https://github.com/GoogleCloudPlatform/google-auth-library-perl/commit/c95c77e70bec94f17e239d88050f843ea1cade95.patch)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-66902
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-05 06:16:37 JST
- 更新日: 2026-08-05 06:16:37 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Google::Auth versions before 0.06 for Perl run a command named in an external_account credentials JSON via an ungated system call. The Pluggable subclass reads credential_source.executable.command from the credentials JSON and runs it as `system($command)`, a single argument call that passes the whole string to /bin/sh...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/GoogleCloudPlatform/google-auth-library-perl/commit/c95c77e70bec94f17e239d88050f843ea1cade95.patch
- https://metacpan.org/release/CJCOLLIER/Google-Auth-0.06/diff/CJCOLLIER/Google-Auth-0.05

### [CVE-2026-24078](https://docs.qualcomm.com/product/publicresources/securitybulletin/august-2026-bulletin.html)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-24078
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-05 01:16:23 JST
- 更新日: 2026-08-05 02:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Information Disclosure when IPSec negotiation fails or is not established properly during NG-eCall SIP signaling.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.qualcomm.com/product/publicresources/securitybulletin/august-2026-bulletin.html

### [CVE-2026-69098](https://github.com/Cinnamon/kotaemon/issues/844)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-69098
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-05 01:16:28 JST
- 更新日: 2026-08-05 01:16:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: kotaemon through 0.12.0 contains an insecure deserialization vulnerability in the check_connection endpoint that allows unauthenticated attackers to instantiate arbitrary Python classes by supplying crafted YAML/JSON input with a __type__ field. Attackers can exploit this to override the __type__ field with subprocess....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Cinnamon/kotaemon/issues/844
- https://www.vulncheck.com/advisories/kotaemon-unauthenticated-remote-code-execution-via-insecure-deserialization

### [CVE-2026-69255](https://github.com/FlowiseAI/Flowise/commit/f4e2794f6a576b94578f2fdafbf49c2fb304626c)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-69255
- 関連キーワード: python, node.js
- 影響製品: -
- 公開日: 2026-08-05 02:17:00 JST
- 更新日: 2026-08-05 05:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Flowise is a drag & drop user interface to build a customized large language model flow. Prior to 3.1.3, the CSVAgent in packages/components/nodes/agents/CSVAgent/CSVAgent.ts extracted attacker-controlled CSV data with file.split(',').pop() and interpolated it directly into executable Python as base64_string = "${base6...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FlowiseAI/Flowise/commit/f4e2794f6a576b94578f2fdafbf49c2fb304626c
- https://github.com/FlowiseAI/Flowise/pull/6499
- https://github.com/FlowiseAI/Flowise/releases/tag/flowise%403.1.3
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-vmv7-4m6c-3cg5
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-vmv7-4m6c-3cg5

### [CVE-2026-70477](https://github.com/FlowiseAI/Flowise/commit/f4e2794f6a576b94578f2fdafbf49c2fb304626c)

> **Backend** / **CRITICAL** / CVSS: **9.5** / KEV: **no**

- タイトル: CVE-2026-70477
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-05 05:16:54 JST
- 更新日: 2026-08-05 05:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Flowise is a drag & drop user interface to build a customized large language model flow. Prior to 3.1.3, a prompt injection sent to a chatflow using a CSV Agent node can cause the LLM to respond with a malicious Python script that bypasses the blocklist validator and executes in an unsandboxed Pyodide environment. The...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FlowiseAI/Flowise/commit/f4e2794f6a576b94578f2fdafbf49c2fb304626c
- https://github.com/FlowiseAI/Flowise/pull/6499
- https://github.com/FlowiseAI/Flowise/releases/tag/flowise@3.1.3
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-5xvg-pmgg-3mxr

### [CVE-2026-67195](https://christbowel.com/blog/perspective-5-0-0-five-cves/)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-67195
- 関連キーワード: python, express
- 影響製品: -
- 公開日: 2026-08-05 00:16:40 JST
- 更新日: 2026-08-05 01:16:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Perspective 5.0.0 contains a remote code execution vulnerability that allows unauthenticated attackers to execute arbitrary operating system commands by submitting crafted expression strings to the PolarsVirtualServer backend, which passes client-supplied input directly to Python's eval() with only __builtins__={} clea...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://christbowel.com/blog/perspective-5-0-0-five-cves/
- https://www.vulncheck.com/advisories/perspective-rce-via-eval-expression-injection

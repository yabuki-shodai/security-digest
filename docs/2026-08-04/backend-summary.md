# Backend CVE Summary (2026-08-04)

## Overview

- 取得日時: 2026-08-04 08:16:00 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 17
- Critical: 3
- High: 6
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-48031](https://github.com/dhax/go-base/commit/cc82b9740fa6b08e0fad409cd4b418e240dd0e00)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-48031
- 関連キーワード: go, gin, postgresql
- 影響製品: -
- 公開日: 2026-08-04 05:17:24 JST
- 更新日: 2026-08-04 05:17:24 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: go-base is a Go RESTful API Boilerplate template with JWT Authentication, backed by PostgreSQL. In versions prior to 2026-05-18, the JWT signing secret is hardcoded to the known string "random", letting any attacker who reads the public repository forge tokens for arbitrary users, including admin roles, and completely...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dhax/go-base/commit/cc82b9740fa6b08e0fad409cd4b418e240dd0e00
- https://github.com/dhax/go-base/pull/31
- https://github.com/dhax/go-base/security/advisories/GHSA-mqq6-462x-jxmm
- https://github.com/dhax/go-base/security/advisories/GHSA-mqq6-462x-jxmm

### [CVE-2026-39932](https://jivasecurity.com/writeups/openemr-eval-rce-category-tree-cve-2026-39932)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-39932
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-04 02:16:36 JST
- 更新日: 2026-08-04 02:16:36 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenEMR through 8.2.0 contains a remote code execution vulnerability in the document category tree component (library/classes/Tree.class.php) that allows authenticated administrators to execute arbitrary operating system commands by injecting PHP payloads into the categories database table. Attackers can chain arbitrar...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jivasecurity.com/writeups/openemr-eval-rce-category-tree-cve-2026-39932
- https://www.vulncheck.com/advisories/openemr-remote-code-execution-via-categorytree-eval-injection

### [CVE-2026-69245](https://github.com/guzzle/guzzle/commit/3aeea0406aab88cbbd86531313d7cebf8ae149a4)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-69245
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-04 06:16:42 JST
- 更新日: 2026-08-04 06:16:42 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Guzzle is an extensible PHP HTTP client. Prior to 7.15.2 and 8.0.1, SetCookie::matchesDomain() gives every subdomain of a cookie Domain that cookie unless SetCookie::matchesDomain() recognizes the Domain as an IP literal or a numeric host, and the decision comes from the domain's own text, so two spellings a transport...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/guzzle/guzzle/commit/3aeea0406aab88cbbd86531313d7cebf8ae149a4
- https://github.com/guzzle/guzzle/commit/744101956d78b7c1384d0cbf379db13e859167bf
- https://github.com/guzzle/guzzle/pull/3907
- https://github.com/guzzle/guzzle/pull/3908
- https://github.com/guzzle/guzzle/releases/tag/7.15.2

### [CVE-2025-15544](https://www.omadanetworks.com/en/support/download/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2025-15544
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-04 04:16:39 JST
- 更新日: 2026-08-04 04:16:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A cryptographic weakness exists in the Omada device adoption process. During adoption, authentication credentials associated with site management are transmitted using a weak hashing algorithm that does not provide sufficient protection. An attacker who successfully intercepts adoption-related authentication traffic ma...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.omadanetworks.com/en/support/download/
- https://www.omadanetworks.com/us/support/download/
- https://www.tp-link.com/us/support/faq/5216/

### [CVE-2025-15631](https://www.omadanetworks.com/en/support/download/)

> **Backend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2025-15631
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-04 04:16:41 JST
- 更新日: 2026-08-04 04:16:41 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A cryptographic weakness exists in affected Omada devices where site credentials are protected using a legacy hashing algorithm that does not provide sufficient protection. An attacker who obtains access to stored credential data may be able to recover valid credentials to gain unauthorized access to affected devices o...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.omadanetworks.com/en/support/download/
- https://www.omadanetworks.com/us/support/download/
- https://www.tp-link.com/us/support/faq/5216/

### [CVE-2026-18604](https://github.com/actuator/com.gogii.textplus)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-18604
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-04 02:16:35 JST
- 更新日: 2026-08-04 05:17:16 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability was identified in textPlus Text Message and Call App up to 8.3.5 on Android. This impacts the function DialerActivity of the component com.gogii.textplus. Such manipulation leads to improper export of android application components. The attack needs to be performed locally. The exploit is publicly avail...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/actuator/com.gogii.textplus
- https://vuldb.com/cve/CVE-2026-18604
- https://vuldb.com/submit/851700
- https://vuldb.com/vuln/385527
- https://vuldb.com/vuln/385527/cti

### [CVE-2026-69249](https://github.com/pyca/cryptography/commit/4a12cf49675a184e47f912b00b04f3a629283582)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-69249
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-04 07:16:52 JST
- 更新日: 2026-08-04 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: python-cryptography is a package designed to expose cryptographic primitives and recipes to Python developers. Prior to 49.0.0, when resolving invalid certificate chains that include duplicate copies of self-signed certificates, the processing recursively invokes the same candidate, leading to an exponential blowup. Al...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pyca/cryptography/commit/4a12cf49675a184e47f912b00b04f3a629283582
- https://github.com/pyca/cryptography/pull/14960
- https://github.com/pyca/cryptography/security/advisories/GHSA-jwv3-5hgf-82ww

### [CVE-2026-69247](https://github.com/pyca/cryptography/commit/53fccd93413a8d7f07d6d8999681f27b75cffa3f)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-69247
- 関連キーワード: python, openssl
- 影響製品: -
- 公開日: 2026-08-04 07:16:52 JST
- 更新日: 2026-08-04 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: cryptography is a package designed to expose cryptographic primitives and recipes to Python developers. From 44.0.0 until 50.0.0, pkcs7_decrypt_der, pkcs7_decrypt_pem, and pkcs7_decrypt_smime reported the outcome of decrypting a RecipientInfo's encryptedKey in several distinguishable ways, one of which disclosed the ex...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pyca/cryptography/commit/53fccd93413a8d7f07d6d8999681f27b75cffa3f
- https://github.com/pyca/cryptography/pull/15369
- https://github.com/pyca/cryptography/security/advisories/GHSA-g6cj-pr64-35w5

### [CVE-2026-69244](https://github.com/aio-libs/aiohttp/commit/49f65d54150397892f7bcc4aae887767d51c322d)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-69244
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-04 06:16:42 JST
- 更新日: 2026-08-04 06:16:42 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.3, an out-of-bounds heap read could occur in the C response parser while building an error message for a malformed response. An attacker controlled server, or possibly an accidental response, could trigger a DoS in the client....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/aio-libs/aiohttp/commit/49f65d54150397892f7bcc4aae887767d51c322d
- https://github.com/aio-libs/aiohttp/pull/13223
- https://github.com/aio-libs/aiohttp/releases/tag/v3.14.3
- https://github.com/aio-libs/aiohttp/security/advisories/GHSA-cq5v-8q36-5273

### [CVE-2026-69243](https://github.com/aio-libs/aiohttp/commit/6ae358f0983c3f4d6f67692b2f8e65dc8e091c98)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-69243
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-04 06:16:42 JST
- 更新日: 2026-08-04 06:16:42 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: AIOHTTP is an asynchronous HTTP client/server framework for asyncio and Python. Prior to 3.14.2, the HTTP parsers were vulnerable to a request smuggling attack relating to WebSocket upgrades. If using the server-side component, an attacker may be able to execute a request smuggling vulnerability using an edge case in t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/aio-libs/aiohttp/commit/6ae358f0983c3f4d6f67692b2f8e65dc8e091c98
- https://github.com/aio-libs/aiohttp/pull/13017
- https://github.com/aio-libs/aiohttp/releases/tag/v3.14.2
- https://github.com/aio-libs/aiohttp/security/advisories/GHSA-mfx4-hv73-q22v

### [CVE-2026-69248](https://github.com/pyca/cryptography/commit/4d035a4225965edeffd312079a510ef25fcfdcb2)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-69248
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-04 07:16:52 JST
- 更新日: 2026-08-04 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: cryptography is a package designed to expose cryptographic primitives and recipes to Python developers. Prior to 49.0.0, if an intermediate constrained CA permits the DNS name foo.example.com, and the leaf certificate has a wildcard in its DNS SAN of *.example.com, python-cryptography's verifier accepts which allows es...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pyca/cryptography/commit/4d035a4225965edeffd312079a510ef25fcfdcb2
- https://github.com/pyca/cryptography/pull/14888
- https://github.com/pyca/cryptography/security/advisories/GHSA-m2h6-j472-rp4c

### [CVE-2026-18248](https://cna.openjsf.org/security-advisories.html)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-18248
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-04 01:16:28 JST
- 更新日: 2026-08-04 05:17:14 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: @fastify/aws-lambda version 6.4.0 decorates each Fastify request with request.awsLambda.event and request.awsLambda.context, values that applications are documented to use for authorization decisions such as reading API Gateway authorizer claims. In the default configuration, the getter that populates this decoration r...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.openjsf.org/security-advisories.html
- https://github.com/fastify/aws-lambda-fastify/security/advisories/GHSA-m93c-jj3f-68ph

### [CVE-2026-18655](https://aws.amazon.com/security/security-bulletins/2026-070-aws/)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-18655
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-04 05:17:17 JST
- 更新日: 2026-08-04 05:17:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Improper restriction of intended endpoints in the RabbitMQ broker connection tools of the Amazon MQ MCP Server (awslabs.amazon-mq-mcp-server) before 2.0.24 may allow a remote unauthenticated actor (via prompt injection) to obtain Amazon MQ for RabbitMQ broker credentials or OAuth access tokens sent to a crafted endpoin...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-070-aws/
- https://github.com/awslabs/mcp/security/advisories/GHSA-xwj6-8x5h-hjp6
- https://pypi.org/project/awslabs.amazon-mq-mcp-server/2.0.24/

### [CVE-2026-18654](https://aws.amazon.com/security/security-bulletins/2026-071-aws/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-18654
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-04 05:17:17 JST
- 更新日: 2026-08-04 05:17:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Key exchange without entity authentication in the EMR SSH helper commands in Amazon AWS CLI before 1.45.28 and AWS CLI v2 before 2.35.3 might allow man-in-the-middle attackers to intercept SSHsessions and file transfers via network positioning between the client and the EMR cluster endpoint. To remediate this issue, us...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-071-aws/
- https://github.com/aws/aws-cli/blob/develop/CHANGELOG.rst
- https://github.com/aws/aws-cli/blob/v2/CHANGELOG.rst
- https://github.com/aws/aws-cli/security/advisories/GHSA-hqvf-45jj-mccq

### [CVE-2026-58139](https://github.com/duckdb/duckdb-aws/commit/7d04119ee8d3f8836e278f0e8cbf21827ff5338b)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-58139
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-04 05:17:25 JST
- 更新日: 2026-08-04 07:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The DuckDB AWS extension for DuckDB contains a security policy bypass vulnerability that allows any database user with SQL execution permissions to extract plaintext AWS credentials by calling the load_aws_credentials function with the redact_secret parameter set to false, circumventing the database-wide allow_unredact...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/duckdb/duckdb-aws/commit/7d04119ee8d3f8836e278f0e8cbf21827ff5338b
- https://github.com/duckdb/duckdb-aws/pull/156
- https://www.vulncheck.com/advisories/duckdb-aws-extension-security-policy-bypass-via-load-aws-credentials-procedure

### [CVE-2026-39931](https://jivasecurity.com/writeups/openemr-backup-import-arbitrary-sql-cve-2026-39931)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-39931
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-08-04 02:16:36 JST
- 更新日: 2026-08-04 05:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenEMR through 8.2.0 contains an authenticated SQL injection vulnerability in the backup configuration import feature that allows administrators with admin or super ACL privileges to execute arbitrary DDL and DML statements against the application database by uploading a crafted SQL file at the form_step=202 parameter...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jivasecurity.com/writeups/openemr-backup-import-arbitrary-sql-cve-2026-39931
- https://www.vulncheck.com/advisories/openemr-authenticated-sql-injection-via-backup-php-import-feature

### [CVE-2026-18614](https://github.com/StrTzz123/iot_vul/blob/main/GL-iNet/MT3000/4.4.5/s2s_enable_echo_server_glc_rce/CVE.md)

> **Backend** / **HIGH** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-18614
- 関連キーワード: gin, echo
- 影響製品: -
- 公開日: 2026-08-04 04:16:45 JST
- 更新日: 2026-08-04 04:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability was found in GL-iNet GL-MT3000 up to 4.4.5. Impacted is the function s2s.enable_echo_server of the file /cgi-bin/glc of the component s2s.so Native Plugin. Performing a manipulation of the argument port results in command injection. The attack may be initiated remotely. The exploit has been made public...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/StrTzz123/iot_vul/blob/main/GL-iNet/MT3000/4.4.5/s2s_enable_echo_server_glc_rce/CVE.md
- https://vuldb.com/cve/CVE-2026-18614
- https://vuldb.com/submit/851558
- https://vuldb.com/vuln/385534
- https://vuldb.com/vuln/385534/cti

# Backend CVE Summary (2026-09-29)

## Overview

- 取得日時: 2026-09-29 10:51:14 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 14
- Critical: 3
- High: 7
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-102281](https://github.com/nestjs/nest/commit/aa97b5144d8dff1ce700aac521eb86449a679d6f)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-102281
- 関連キーワード: nestjs, node.js
- 影響製品: -
- 公開日: 2026-09-29 07:17:32 JST
- 更新日: 2026-09-29 07:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nest is a framework for building scalable Node.js server-side applications. Prior to 11.2.4 and 12.0.2, a single message with a deeply nested object in its pattern can terminate a NestJS microservice using the TCP or RabbitMQ transport. ServerTCP#handleMessage and ServerRMQ#handleMessage pass a client-controlled non-st...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nestjs/nest/commit/aa97b5144d8dff1ce700aac521eb86449a679d6f
- https://github.com/nestjs/nest/commit/e9dcd4c7ac64361fbfe79461da85f5b3fc3e02da
- https://github.com/nestjs/nest/pull/17737
- https://github.com/nestjs/nest/releases/tag/v11.2.4
- https://github.com/nestjs/nest/releases/tag/v12.0.2

### [CVE-2026-102268](https://github.com/jpadilla/pyjwt/commit/8b4e233a22206b34ec1186e912e75c0b2396ac07)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-102268
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-09-29 06:17:14 JST
- 更新日: 2026-09-29 06:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PyJWT is a Python implementation of JSON Web Token standards. Prior to 2.14.0, is_pem_format in jwt/utils.py is affected because is_pem_format does not recognize every PEM representation accepted by the cryptography loader. This occurs when an application mixes HMAC and asymmetric algorithms and supplies a mutated publ...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jpadilla/pyjwt/commit/8b4e233a22206b34ec1186e912e75c0b2396ac07
- https://github.com/jpadilla/pyjwt/releases/tag/2.14.0
- https://github.com/jpadilla/pyjwt/security/advisories/GHSA-ffc3-869f-jxw9

### [CVE-2026-100752](https://www.ordasoft.com/)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-100752
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-29 04:16:46 JST
- 更新日: 2026-09-29 04:16:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla Extension - ordasoft.com - Unauthenticated SQL Injection in Real Estate Manager (Free) < 6.7.9 - site/realestatemanager.php builds the ORDER BY clause of three separate frontend property-listing queries (category browsing, search results, and the full property listing) from a request-controlled order_field param...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ordasoft.com/

### [CVE-2026-101108](https://www.ordasoft.com/)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-101108
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-29 04:16:46 JST
- 更新日: 2026-09-29 04:16:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla Extension - ordasoft.com - Unauthenticated SQL Injection in Vehicle Manager (Free) < 6.5.8 - site/vehiclemanager.php reads the order_field and order_direction sort parameters at three separate anonymous-reachable frontend entry points (category listing, search, and the all-vehicles listing) through a sanitizing...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ordasoft.com/

### [CVE-2026-55096](https://github.com/leshchenko1979/fast-mcp-telegram/commit/e6b3032cfc906e14f5b84f2c2b8ec378eb457e57)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-55096
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-29 02:17:50 JST
- 更新日: 2026-09-29 02:17:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: fast-mcp-telegram is a Telegram MCP Server. Prior to version 30.1, the send_message/send_message_to_phone MCP tools accept files as a list of http(s) URLs, which the server downloads and attaches to the outgoing Telegram message. Downloads are guarded by _validate_url_security, an SSRF denylist that checks the URL's li...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/leshchenko1979/fast-mcp-telegram/commit/e6b3032cfc906e14f5b84f2c2b8ec378eb457e57
- https://github.com/leshchenko1979/fast-mcp-telegram/releases/tag/0.30.1
- https://github.com/leshchenko1979/fast-mcp-telegram/security/advisories/GHSA-xr72-j7vj-vp7g

### [CVE-2026-102266](https://github.com/jpadilla/pyjwt/commit/f91ed44dd65baaf457f4b3353ed35e98a753934c)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-102266
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-09-29 06:17:14 JST
- 更新日: 2026-09-29 06:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PyJWT is a Python implementation of JSON Web Token standards. From 2.13.0 until 2.14.0, HMACAlgorithm.from_jwk is affected because PyJWK verification path used the decoded key without applying prepare_key validation. This occurs when a trusted JWK Set contains an oct entry with an empty k value. As a result, an attacke...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jpadilla/pyjwt/commit/f91ed44dd65baaf457f4b3353ed35e98a753934c
- https://github.com/jpadilla/pyjwt/releases/tag/2.14.0
- https://github.com/jpadilla/pyjwt/security/advisories/GHSA-9j54-fg26-wv3r

### [CVE-2026-102271](https://github.com/jpadilla/pyjwt/commit/2798504fa2663364573cf2d1043d8d7fef389499)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-102271
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-09-29 06:17:15 JST
- 更新日: 2026-09-29 06:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PyJWT is a Python implementation of JSON Web Token standards. From 2.4.0 until 2.14.0, PyJWT HMACAlgorithm.prepare_key is affected because asymmetric-key guard relies on textual markers that are absent from DER encoding. This occurs when an application mixes HMAC and asymmetric algorithms and supplies a DER public key...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jpadilla/pyjwt/commit/2798504fa2663364573cf2d1043d8d7fef389499
- https://github.com/jpadilla/pyjwt/releases/tag/2.14.0
- https://github.com/jpadilla/pyjwt/security/advisories/GHSA-p4g4-x82p-q773

### [CVE-2026-102272](https://github.com/jpadilla/pyjwt/commit/180783930de91876bc0d601f826a1f2956057291)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-102272
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-09-29 06:17:15 JST
- 更新日: 2026-09-29 06:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PyJWT is a Python implementation of JSON Web Token standards. From 2.13.0 until 2.14.0, HMACAlgorithm.prepare_key in jwt/algorithms.py is affected because raw-JWK detector does not normalize accepted Unicode byte-order marks before checking for JSON. This occurs when a public JWK is prefixed with a UTF-8 BOM and used i...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jpadilla/pyjwt/commit/180783930de91876bc0d601f826a1f2956057291
- https://github.com/jpadilla/pyjwt/releases/tag/2.14.0
- https://github.com/jpadilla/pyjwt/security/advisories/GHSA-r6x4-923q-g947

### [CVE-2026-102273](https://github.com/jpadilla/pyjwt/commit/801cd128528c62d9b23fcd161d1a2e1c17982f95)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-102273
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-09-29 06:17:15 JST
- 更新日: 2026-09-29 06:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PyJWT is a Python implementation of JSON Web Token standards. From 2.13.0 until 2.14.0, PyJWT HMACAlgorithm.prepare_key is affected because HMAC key guard only recognizes top-level public JWK forms and misses container representations. This occurs when an application allows HMAC and asymmetric algorithms and passes a p...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jpadilla/pyjwt/commit/801cd128528c62d9b23fcd161d1a2e1c17982f95
- https://github.com/jpadilla/pyjwt/releases/tag/2.14.0
- https://github.com/jpadilla/pyjwt/security/advisories/GHSA-w2cx-738m-mc7w

### [CVE-2026-88805](https://github.com/rancher/rancher/security/advisories/GHSA-6vpq-mf48-9794)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-88805
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-29 01:17:16 JST
- 更新日: 2026-09-29 03:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Incorrect credential cleaning on logout could be used by remote attackers to keep access credentials even after the account was logged out. Affected is SUSE Rancher 2.15 before 2.15.2.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/rancher/rancher/security/advisories/GHSA-6vpq-mf48-9794

### [CVE-2026-18417](https://github.com/zephyrproject-rtos/zephyr/commit/ef370a57d07637aaee8cec7b0bcebf4002ac8f54)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-18417
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-29 09:17:04 JST
- 更新日: 2026-09-29 09:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The native BSD-socket layer recorded a pending asynchronous socket error by type-punning it into struct net_context's void user_data field (ctx->user_data = INT_TO_POINTER(-status) in zsock_accepted_cb(), zsock_received_cb(), zsock_connected_cb() and zsock_close_ctx() in subsys/net/lib/sockets/sockets_inet.c), reading...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/ef370a57d07637aaee8cec7b0bcebf4002ac8f54
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-p8r8-8mw8-3wf9

### [CVE-2026-91154](https://github.com/MarcosCamara01/ecommerce-template/commit/ec97209e6c7663cba7b5164468d6946cbfe2f19a)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-91154
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-29 01:17:17 JST
- 更新日: 2026-09-29 03:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Missing Authentication for Critical Function (CWE-306) in the product cache revalidation Server Action (src/app/actions.ts, revalidateProducts) in MarcosCamara01 Ecommerce Template before commit ec97209 allows a remote, unauthenticated attacker to force expiration of the entire storefront product cache at will. The fil...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/MarcosCamara01/ecommerce-template/commit/ec97209e6c7663cba7b5164468d6946cbfe2f19a
- https://secur0.com/en/cna/cve-list/cve-2026-91154-missing-authentication-ecommerce-template-cache-revalidation-dos

### [CVE-2026-102274](https://github.com/jpadilla/pyjwt/commit/8915570a0bfda9f0ff0e34e7fb09bdb9d71580cf)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-102274
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-09-29 06:17:15 JST
- 更新日: 2026-09-29 06:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PyJWT is a Python implementation of JSON Web Token standards. From 2.9.0 until 2.14.0, PyJWKSet does not catch the plain ValueError raised for malformed RSA JWK components by RSAAlgorithm.from_jwk in jwt/api_jwk.py. This occurs when a JWK Set contains a malformed RSA key alongside otherwise usable keys. As a result, on...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jpadilla/pyjwt/commit/8915570a0bfda9f0ff0e34e7fb09bdb9d71580cf
- https://github.com/jpadilla/pyjwt/releases/tag/2.14.0
- https://github.com/jpadilla/pyjwt/security/advisories/GHSA-w6j9-cwv2-h6wq

### [CVE-2026-102275](https://github.com/jpadilla/pyjwt/commit/3cd9ceec33ced359decbad75b413ad668ae6332c)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-102275
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-09-29 06:17:15 JST
- 更新日: 2026-09-29 06:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PyJWT is a Python implementation of JSON Web Token standards. From 2.1.0 until 2.15.0, PyJWT OKPAlgorithm.from_jwk in jwt/algorithms.py is affected because private-JWK import path does not compare the public key derived from d with x. This occurs when an OKP private JWK supplies non-corresponding x and d components. As...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jpadilla/pyjwt/commit/3cd9ceec33ced359decbad75b413ad668ae6332c
- https://github.com/jpadilla/pyjwt/releases/tag/2.15.0
- https://github.com/jpadilla/pyjwt/security/advisories/GHSA-x33g-cr3x-6449

# Backend CVE Summary (2026-10-01)

## Overview

- 取得日時: 2026-10-01 10:14:49 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 24
- Critical: 4
- High: 13
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-103396](https://github.com/mlogclub/bbs-go)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-103396
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-01 00:22:28 JST
- 更新日: 2026-10-01 02:32:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: bbs-go through 4.4.6 contains a permission bypass vulnerability in the AdminMiddleware authorization logic where the read-only dashboard.user.view permission rule matches the /api/admin/user/synccount endpoint before the intended dashboard.user.update rule. Authenticated users with only view permissions can call the sy...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mlogclub/bbs-go
- https://github.com/mlogclub/bbs-go/blob/v4.4.6/internal/handlers/admin/user_handlers.go#L47-L59
- https://github.com/mlogclub/bbs-go/blob/v4.4.6/internal/permissions/admin_permission_registry.go#L59-L60
- https://github.com/mlogclub/bbs-go/commit/97d0bb3dcbacd686fd5300295afbf4f4a5da7609
- https://github.com/mlogclub/bbs-go/issues/303

### [CVE-2026-80490](https://github.com/richardjharris/Algorithm-AhoCorasick-XS/pull/1)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80490
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-01 01:19:10 JST
- 更新日: 2026-10-01 04:57:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Algorithm::AhoCorasick::XS versions through 0.04 for Perl read the haystack string length before the scalar is stringified. The matches, first_match and match_details methods use the T_STD_STRING typemap to translate Perl scalars (SVs) into strings via the std::string constructor, using the SvPV macro to stringify the...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/richardjharris/Algorithm-AhoCorasick-XS/pull/1
- https://metacpan.org/release/RJH/Algorithm-AhoCorasick-XS-0.04/source/typemap#L14
- https://rt.cpan.org/Ticket/Display.html?id=181560
- https://security.metacpan.org/patches/A/Algorithm-AhoCorasick-XS/0.04/CVE-2026-80490-r1.patch
- http://www.openwall.com/lists/oss-security/2026/09/30/15

### [CVE-2026-19553](https://github.com/python/cpython/commit/1697ea386c707142555d98a1263176bbbc014a96)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-19553
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-01 02:16:45 JST
- 更新日: 2026-10-01 08:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ssl.SSLContext.wrap_bio() didn't require the server_hostname argument to not be None if ssl.SSLContext.check_hostname was set. Due to a missing parameter check in SSLObject, if the server_hostname argument isn't supplied then hostname verification would be silently skipped. This defect could lead to programs where cert...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/python/cpython/commit/1697ea386c707142555d98a1263176bbbc014a96
- https://github.com/python/cpython/commit/641390146a16a38e6701923f4ee4f1940ae77082
- https://github.com/python/cpython/commit/869069d52ce0efab2f8c38197e92cdaaa312f1ed
- https://github.com/python/cpython/commit/966bf426d0b6c31c1b0a255ff14a17143a466ced
- https://github.com/python/cpython/commit/f4e43ba525187282f2011da0e6ffc0d2b08d8062

### [CVE-2026-62308](https://github.com/Quenary/tugtainer/commit/c0294d0ab64985b135d0c5b566ac30bf8371f9c3)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-62308
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-01 02:16:49 JST
- 更新日: 2026-10-01 05:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.6, Tugtainer allows an authenticated user to make the backend server send outbound HTTP requests to arbitrary user-supplied URLs through the notification test endpoint. The /settings/test_notification endpoint accepts a ur...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Quenary/tugtainer/commit/c0294d0ab64985b135d0c5b566ac30bf8371f9c3
- https://github.com/Quenary/tugtainer/releases/tag/v1.30.6
- https://github.com/Quenary/tugtainer/security/advisories/GHSA-c2h5-ppv9-7vrq
- https://github.com/Quenary/tugtainer/security/advisories/GHSA-c2h5-ppv9-7vrq

### [CVE-2026-55181](https://github.com/Quenary/tugtainer/commit/76371db679334b002d4af544b0f3b8587ad86f52)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-55181
- 関連キーワード: gin, docker
- 影響製品: -
- 公開日: 2026-10-01 02:16:46 JST
- 更新日: 2026-10-01 05:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.3, Tugtainer's OIDC authentication can still be initiated even when OIDC_ENABLED=false. The /auth/oidc/enabled endpoint correctly reports that OIDC is disabled. However, a direct request to /auth/oidc/login still starts th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Quenary/tugtainer/commit/76371db679334b002d4af544b0f3b8587ad86f52
- https://github.com/Quenary/tugtainer/releases/tag/v1.30.3
- https://github.com/Quenary/tugtainer/security/advisories/GHSA-rg7c-vpfp-2w43
- https://github.com/Quenary/tugtainer/security/advisories/GHSA-rg7c-vpfp-2w43

### [CVE-2026-55494](https://github.com/Quenary/tugtainer/commit/0052a5544e187a4d12f771838a8a23ca4afb61cd)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-55494
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-01 02:16:47 JST
- 更新日: 2026-10-01 04:57:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tugtainer is a self-hosted app for automating updates of Docker containers. Prior to version 1.30.4, Tugtainer Agent allows unauthenticated access to Docker management APIs when AGENT_SECRET is not configured. The Agent uses request signatures to protect its API routes. However, in agent/auth.py, the signature verifica...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Quenary/tugtainer/commit/0052a5544e187a4d12f771838a8a23ca4afb61cd
- https://github.com/Quenary/tugtainer/releases/tag/v1.30.4
- https://github.com/Quenary/tugtainer/security/advisories/GHSA-wgw2-c96g-p7h7
- https://github.com/Quenary/tugtainer/security/advisories/GHSA-wgw2-c96g-p7h7

### [CVE-2026-103229](https://github.com/AdithyaYelloju/Restaurant-Management-System/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-103229
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-10-01 01:17:08 JST
- 更新日: 2026-10-01 01:38:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was found in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff6b9c. This issue affects the function mysqli_query of the file admin/delete1.php of the component Unauthenticated Action Script. Performing a manipulation of the argument ID results in sql injection. The a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/AdithyaYelloju/Restaurant-Management-System/
- https://github.com/AdithyaYelloju/Restaurant-Management-System/issues/5
- https://vuldb.com/cve/CVE-2026-103229
- https://vuldb.com/submit/955078
- https://vuldb.com/vuln/411922

### [CVE-2026-103230](https://github.com/AdithyaYelloju/Restaurant-Management-System/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-103230
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-10-01 01:17:08 JST
- 更新日: 2026-10-01 05:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was determined in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff6b9c. Impacted is the function mysqli_query of the file User/ord.php of the component Order Placement. Executing a manipulation of the argument id/name can lead to sql injection. The attack can be lau...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/AdithyaYelloju/Restaurant-Management-System/
- https://github.com/AdithyaYelloju/Restaurant-Management-System/issues/6
- https://vuldb.com/cve/CVE-2026-103230
- https://vuldb.com/submit/955079
- https://vuldb.com/vuln/411923

### [CVE-2026-103231](https://github.com/AdithyaYelloju/Restaurant-Management-System/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-103231
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-10-01 01:17:08 JST
- 更新日: 2026-10-01 01:38:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was identified in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff6b9c. The affected element is the function mysqli_query of the file User/cancel.php of the component Order Cancellation. The manipulation of the argument ID leads to sql injection. The attack may be i...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/AdithyaYelloju/Restaurant-Management-System/
- https://github.com/AdithyaYelloju/Restaurant-Management-System/issues/7
- https://vuldb.com/cve/CVE-2026-103231
- https://vuldb.com/submit/955080
- https://vuldb.com/vuln/411924

### [CVE-2026-103232](https://github.com/AdithyaYelloju/Restaurant-Management-System/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-103232
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-10-01 02:16:42 JST
- 更新日: 2026-10-01 03:18:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A weakness has been identified in AdithyaYelloju Restaurant-Management-System up to 7f0e7e84255e8fcfd488e83f8f91451bbbff6b9c. This affects the function mysqli_query of the file admin/table_booking.php. This manipulation of the argument Name causes sql injection. Remote exploitation of the attack is possible. The exploi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/AdithyaYelloju/Restaurant-Management-System/
- https://github.com/AdithyaYelloju/Restaurant-Management-System/issues/8
- https://vuldb.com/cve/CVE-2026-103232
- https://vuldb.com/submit/955081
- https://vuldb.com/vuln/411926

### [CVE-2026-19445](https://github.com/python/cpython/commit/34a53dce8174da2fceb12fe084a4def02a10053d)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-19445
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 02:16:45 JST
- 更新日: 2026-10-01 08:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A remote, unauthenticated TLS client can make a server crash or call through a freed pointer if its sni_callback assigns a different context to SSLSocket.context (the documented way to select a certificate per server name) and nothing else keeps the original ssl.SSLContext alive. Typical cases are servers that create a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/python/cpython/commit/34a53dce8174da2fceb12fe084a4def02a10053d
- https://github.com/python/cpython/commit/46133cd57d309652139ada74014aca7665ac552b
- https://github.com/python/cpython/commit/63fab143d94cafae71850831acfb52041ba44af7
- https://github.com/python/cpython/commit/cd7e51e7d4563866fbaa1e2521ae69b45daf3698
- https://github.com/python/cpython/commit/d8717ed01717a9641686e6e6f83f0ab8af235e2c

### [CVE-2026-102983](https://github.com/withastro/astro/commit/e362d4cf540b27730482455c8fc02efe57d16702)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-102983
- 関連キーワード: gin, express
- 影響製品: -
- 公開日: 2026-10-01 00:22:22 JST
- 更新日: 2026-10-01 04:38:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Astro is a web framework for content-driven websites. From 5.2.0 until 8.2.4, the @astrojs/netlify adapter generates regular expressions for Netlify Image CDN remote-image allowlists without anchoring them to the beginning of the URL. Because Netlify evaluates these expressions with RegExp.test(), an allowed origin app...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/withastro/astro/commit/e362d4cf540b27730482455c8fc02efe57d16702
- https://github.com/withastro/astro/pull/17752
- https://github.com/withastro/astro/releases/tag/@astrojs/netlify@8.2.4
- https://github.com/withastro/astro/security/advisories/GHSA-4233-jc72-56c5

### [CVE-2026-102984](https://github.com/withastro/astro/commit/2066f39c60707a100531b4ef4bb5dab8feafa7f2)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-102984
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 00:22:23 JST
- 更新日: 2026-10-01 05:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Astro is a web framework for content-driven websites. Prior to 11.1.3, the @astrojs/node adapter builds a request URL from the Host header, and a malformed port can make that URL invalid. The recovery path reuses the same malformed host and throws an uncaught TypeError: Invalid URL before routing begins. In the default...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/withastro/astro/commit/2066f39c60707a100531b4ef4bb5dab8feafa7f2
- https://github.com/withastro/astro/pull/17572
- https://github.com/withastro/astro/releases/tag/@astrojs/node@11.1.3
- https://github.com/withastro/astro/security/advisories/GHSA-qh8j-hqjv-7m4x

### [CVE-2026-46711](https://github.com/Soft-Machine-io/security/security/advisories/GHSA-h6g6-qr45-qmrr)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-46711
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 02:16:46 JST
- 更新日: 2026-10-01 04:57:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Soft Machine is a Virtual Machine–based agentic development environment / Cloud OS. In versions 0.2.247 and prior, the workspace HTTP service that listens on 0.0.0.0:8080 inside each sm-ws-* Fly Machine exposes endpoints (/health, /file/<path>, /archive/<dir>) without any authentication or origin check. Any host that c...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Soft-Machine-io/security/security/advisories/GHSA-h6g6-qr45-qmrr
- https://github.com/Soft-Machine-io/security/security/advisories/GHSA-h6g6-qr45-qmrr

### [CVE-2026-47097](https://d26ddnfpy9hzf8.cloudfront.net/aja-web/public/pdf/2026/AJA_HELO_PLUS_ReleaseNotes_v2.1.7.pdf)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-47097
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 00:22:30 JST
- 更新日: 2026-10-01 07:16:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AJA HELO Plus firmware before 2.1.7 contains an information disclosure vulnerability that allows unauthenticated attackers to decrypt sensitive diagnostics bundles by exploiting a static AES passphrase embedded in obfuscated form within the firmware. Attackers can reverse engineer the publicly available firmware image...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://d26ddnfpy9hzf8.cloudfront.net/aja-web/public/pdf/2026/AJA_HELO_PLUS_ReleaseNotes_v2.1.7.pdf
- https://www.aja.com/security-advisories/aja-sa-2026-003
- https://www.aja.com/support/item/10457
- https://www.vulncheck.com/advisories/aja-helo-plus-hardcoded-aes-passphrase-for-diagnostics-export-bundle

### [CVE-2026-47496](https://github.com/NVIDIA/product-security/tree/main/2026/5861)

> **Backend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-47496
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 01:17:14 JST
- 更新日: 2026-10-01 03:18:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NVIDIA GPU Display Driver for Linux contains a vulnerability in the Virtual GPU Manager (vGPU plugin) where a guest VM user may cause an out-of-bounds write by sending a specially crafted RPC call to the host. A successful exploit of this vulnerability might lead to escalation of privileges, data tampering, and denial...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/NVIDIA/product-security/tree/main/2026/5861
- https://nvd.nist.gov/vuln/detail/CVE-2026-47496
- https://www.cve.org/CVERecord?id=CVE-2026-47496

### [CVE-2026-47498](https://github.com/NVIDIA/product-security/tree/main/2026/5861)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-47498
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 01:17:14 JST
- 更新日: 2026-10-01 03:18:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NVIDIA vGPU Manager contains a vulnerability in the GPU System Processor (GSP) plugin where a guest VM user may cause an out-of-bounds write by sending a specially crafted RPC message. A successful exploit of this vulnerability might lead to code execution, escalation of privileges, data tampering, denial of service, a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/NVIDIA/product-security/tree/main/2026/5861
- https://nvd.nist.gov/vuln/detail/CVE-2026-47498
- https://www.cve.org/CVERecord?id=CVE-2026-47498

### [CVE-2026-47503](https://github.com/NVIDIA/product-security/tree/main/2026/5861)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-47503
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 01:17:15 JST
- 更新日: 2026-10-01 03:18:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NVIDIA GPU Display Driver for Linux contains a vulnerability in the Virtual GPU Manager (vGPU plugin), where a guest VM user may cause an out-of-bounds write by sending a crafted RPC message with invalid performance state list size parameters. A successful exploit of this vulnerability might lead to code execution, esc...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/NVIDIA/product-security/tree/main/2026/5861
- https://nvd.nist.gov/vuln/detail/CVE-2026-47503
- https://www.cve.org/CVERecord?id=CVE-2026-47503

### [CVE-2026-47559](https://github.com/NVIDIA/product-security/tree/main/2026/5861)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-47559
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 01:17:24 JST
- 更新日: 2026-10-01 03:18:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NVIDIA GPU Display Driver for Windows and Linux contains a vulnerability in the kernel mode layer, where a user could access memory belonging to another user's process. A successful exploit of this vulnerability might lead to code execution, escalation of privileges, data tampering, denial of service, and information d...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/NVIDIA/product-security/tree/main/2026/5861
- https://nvd.nist.gov/vuln/detail/CVE-2026-47559
- https://www.cve.org/CVERecord?id=CVE-2026-47559

### [CVE-2026-62097](https://patchstack.com/database/wordpress/plugin/business-directory-plugin/vulnerability/wordpress-business-directory-plugin-6-4-27-sql-injection-vulnerability?_s_id=cve)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-62097
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 00:22:32 JST
- 更新日: 2026-10-01 01:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection') vulnerability in WPTasty Business Directory business-directory-plugin allows Blind SQL Injection.This issue affects Business Directory: from n/a through 6.4.27.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://patchstack.com/database/wordpress/plugin/business-directory-plugin/vulnerability/wordpress-business-directory-plugin-6-4-27-sql-injection-vulnerability?_s_id=cve

### [CVE-2026-100261](https://www.jetbrains.com/privacy-security/issues-fixed/)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-100261
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 01:16:56 JST
- 更新日: 2026-10-01 01:44:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In JetBrains YouTrack before 2026.2.18991 changing article visibility settings was possible without update permission
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.jetbrains.com/privacy-security/issues-fixed/

### [CVE-2026-100279](https://www.jetbrains.com/privacy-security/issues-fixed/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-100279
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 01:16:59 JST
- 更新日: 2026-10-01 01:44:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In JetBrains YouTrack before 2026.2.19197 changing an integration URL exposed its stored credentials
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.jetbrains.com/privacy-security/issues-fixed/

### [CVE-2026-55174](https://github.com/shrec/UltrafastSecp256k1/commit/5478ef566c6af91b48a45c0c61f161f5b1071981)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-55174
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 01:17:31 JST
- 更新日: 2026-10-01 05:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: UltrafastSecp256k1 is a high-performance, multi-backend secp256k1 engine with reproducible audit evidence, compatibility shims, and profile-based review scopes. Prior to version 4.2.0, UltrafastSecp256k1's ECDSA adaptor pre-signature verification accepts forged adaptor pre-signatures whose "r" value is not cryptographi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/shrec/UltrafastSecp256k1/commit/5478ef566c6af91b48a45c0c61f161f5b1071981
- https://github.com/shrec/UltrafastSecp256k1/releases/tag/v4.2.0
- https://github.com/shrec/UltrafastSecp256k1/releases/tag/v4.2.1
- https://github.com/shrec/UltrafastSecp256k1/security/advisories/GHSA-c7q2-gv3g-rgxm
- https://github.com/shrec/UltrafastSecp256k1/security/advisories/GHSA-c7q2-gv3g-rgxm

### [CVE-2026-100264](https://www.jetbrains.com/privacy-security/issues-fixed/)

> **Backend** / **LOW** / CVSS: **2.7** / KEV: **no**

- タイトル: CVE-2026-100264
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-01 01:16:57 JST
- 更新日: 2026-10-01 01:44:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In JetBrains YouTrack before 2026.2.18991 stored SMTP server credentials could be disclosed by changing the server host
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.jetbrains.com/privacy-security/issues-fixed/

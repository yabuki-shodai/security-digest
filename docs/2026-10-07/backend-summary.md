# Backend CVE Summary (2026-10-07)

## Overview

- 取得日時: 2026-10-07 10:28:19 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 15
- Critical: 7
- High: 8
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-104073](https://github.com/netbox-community/netbox/issues/22607)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-104073
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-10-07 04:17:40 JST
- 更新日: 2026-10-07 05:05:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NetBox versions 2.9.5 before 4.7.0 contain a server-side template injection vulnerability that allows a low-privileged user with the "Can add custom links" permission to steal session cookies and API tokens of other users by exposing the raw Django HttpRequest object to the Jinja2 template context. Attackers can craft...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/netbox-community/netbox/issues/22607
- https://github.com/netbox-community/netbox/pull/22616
- https://github.com/netbox-community/netbox/releases#release-v4.7.0
- https://www.vulncheck.com/advisories/netbox-session-hijacking-via-custom-links

### [CVE-2026-106211](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-106211
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-07 04:17:47 JST
- 更新日: 2026-10-07 05:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Use after free in TabStrip in Google Chrome prior to 155.0.8059.39 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/562002095

### [CVE-2026-106234](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-106234
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-07 04:17:50 JST
- 更新日: 2026-10-07 05:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Use after free in Network in Google Chrome prior to 155.0.8059.39 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted Chrome extension. (Chromium security severity: Low)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/564085088

### [CVE-2026-106241](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-106241
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-07 04:17:51 JST
- 更新日: 2026-10-07 06:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Incorrect authorization in Search in Google Chrome on on Android prior to 155.0.8059.39 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/501729675

### [CVE-2026-102322](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-102322
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-07 04:17:39 JST
- 更新日: 2026-10-07 07:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Incorrect Authorization in SiteIsolation in Google Chrome prior to 155.0.8059.39 allowed a remote attacker to execute arbitrary code via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/527023137

### [CVE-2026-106197](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-106197
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-07 04:17:45 JST
- 更新日: 2026-10-07 05:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Use after free in Browser in Google Chrome prior to 155.0.8059.39 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/560238696

### [CVE-2026-106227](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-106227
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-07 04:17:49 JST
- 更新日: 2026-10-07 05:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Use after free in Core in Google Chrome prior to 155.0.8059.39 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/561891645

### [CVE-2026-106239](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-106239
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-07 04:17:50 JST
- 更新日: 2026-10-07 07:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Integer overflow in WebGL in Google Chrome on on Android prior to 155.0.8059.39 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/546630009

### [CVE-2026-106100](https://github.com/payloadcms/payload/commit/2a69863deb0e3c87e36c1b3b17ab2d5b02fcb941)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-106100
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-07 02:17:23 JST
- 更新日: 2026-10-07 05:03:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Payload is a free and open source headless content management system. In @payloadcms/db-mongodb versions before 3.87.0 and canary versions before 4.0.0-canary.20, an authenticated user who can update a document can modify fields that field-level write access control does not permit that user to change. The Postgres and...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/payloadcms/payload/commit/2a69863deb0e3c87e36c1b3b17ab2d5b02fcb941
- https://github.com/payloadcms/payload/commit/8f77dffa9552885ec2710768cfee15b57e389935
- https://github.com/payloadcms/payload/releases/tag/v3.87.0
- https://github.com/payloadcms/payload/security/advisories/GHSA-4ww4-68q3-h7g5

### [CVE-2026-105797](https://github.com/microsoft/simplechat/commit/73ff7d6998dc4827a0f6ba002386275a7c1ec804)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-105797
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-07 00:17:16 JST
- 更新日: 2026-10-07 03:16:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SimpleChat is a secure AI conversation application with personal and group workspaces for document-grounded interactions. In versions 0.261.003 and 0.261.027, an authorization ordering flaw in POST /api/user/plugins allows an authenticated low-privileged user to omit the top-level MCP type so that _reject_non_admin_mcp...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/microsoft/simplechat/commit/73ff7d6998dc4827a0f6ba002386275a7c1ec804
- https://github.com/microsoft/simplechat/security/advisories/GHSA-h4mw-qw8m-5x4j
- https://github.com/microsoft/simplechat/security/advisories/GHSA-h4mw-qw8m-5x4j

### [CVE-2026-106203](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-106203
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-07 04:17:46 JST
- 更新日: 2026-10-07 06:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Incomplete cleanup in Autofill in Google Chrome on on iOS prior to 155.0.8059.39 allowed a remote attacker leveraging social engineering to obtain sensitive information via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/553394296

### [CVE-2026-106212](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-106212
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-07 04:17:47 JST
- 更新日: 2026-10-07 06:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Incorrect authorization in Autofill in Google Chrome prior to 155.0.8059.39 allowed a remote attacker leveraging social engineering to obtain sensitive information via a crafted HTML page. (Chromium security severity: Medium)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/540072162

### [CVE-2026-106225](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-106225
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-07 04:17:49 JST
- 更新日: 2026-10-07 06:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Missing authorization in Autofill in Google Chrome prior to 155.0.8059.39 allowed a remote attacker leveraging social engineering to obtain sensitive information via a crafted HTML page. (Chromium security severity: Medium)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/501805355

### [CVE-2026-106256](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-106256
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-07 04:17:52 JST
- 更新日: 2026-10-07 06:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Information leak in Passwords in Google Chrome on on Android prior to 155.0.8059.39 allowed a remote attacker leveraging social engineering to obtain sensitive information via a crafted HTML page. (Chromium security severity: Low)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/553335319

### [CVE-2026-106274](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-106274
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-07 04:17:55 JST
- 更新日: 2026-10-07 06:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Incorrect reference resolution in Browser in Google Chrome on on Mac prior to 155.0.8059.39 allowed a remote attacker leveraging social engineering to obtain sensitive information via a crafted HTML page. (Chromium security severity: Medium)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop_086471744.html
- https://issues.chromium.org/issues/497842821

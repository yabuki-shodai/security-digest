# Backend CVE Summary (2026-09-08)

## Overview

- 取得日時: 2026-09-08 09:16:40 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 7
- Critical: 1
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-86469](https://access.redhat.com/security/cve/CVE-2026-86469)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-86469
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-08 01:17:30 JST
- 更新日: 2026-09-08 01:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw was found in GLib2. When g_file_replace() is used with G_FILE_CREATE_REPLACE_DESTINATION and creating the .goutputstream-XXXXXX temporary file fails, the library unlinks the destination and recreates it without exclusive creation or symlink protection. A local attacker who can write to the destination directory...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-86469
- https://bugzilla.redhat.com/show_bug.cgi?id=2473839
- https://gitlab.gnome.org/GNOME/glib/-/blob/main/gio/glocalfileoutputstream.c
- https://gitlab.gnome.org/GNOME/glib/-/work_items/4044

### [CVE-2026-86506](https://www.jetbrains.com/privacy-security/issues-fixed/)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-86506
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-08 02:17:29 JST
- 更新日: 2026-09-08 02:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In JetBrains GoLand before 2026.2.2.1 missing authentication on the GoLand profiler's injected pprof server exposed profiling data
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.jetbrains.com/privacy-security/issues-fixed/

### [CVE-2026-75650](https://helpx.adobe.com/security/products/magento/apsb26-146.html)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-75650
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-08 06:17:30 JST
- 更新日: 2026-09-08 06:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Adobe Commerce is affected by an Improper Neutralization of Special Elements Used in a Template Engine vulnerability that could result in arbitrary code execution in the context of the current user. An attacker could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://helpx.adobe.com/security/products/magento/apsb26-146.html

### [CVE-2026-86503](https://www.jetbrains.com/privacy-security/issues-fixed/)

> **Backend** / **LOW** / CVSS: **3.3** / KEV: **no**

- タイトル: CVE-2026-86503
- 関連キーワード: kubernetes
- 影響製品: -
- 公開日: 2026-09-08 02:17:28 JST
- 更新日: 2026-09-08 02:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In JetBrains IntelliJ IDEA before 2026.2.2 opening an untrusted project could trigger SSRF via Kubernetes spec-source URL fetching
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.jetbrains.com/privacy-security/issues-fixed/

### [CVE-2026-82754](https://cna.erlef.org/cves/CVE-2026-82754.html)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-82754
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-08 08:16:52 JST
- 更新日: 2026-09-08 08:16:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper Protection of Alternate Path vulnerability in ash-project ash_authentication_oauth2_server exposes the state-changing OAuth endpoints under an unintended URL prefix, bypassing controls scoped to the canonical prefix. oauth2_server_protocol_routes/1 in AshAuthentication.Phoenix.Oauth2Server.Router forwards the...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-82754.html
- https://github.com/ash-project/ash_authentication_oauth2_server/commit/a72972d7ed3eb74c05dfa0653a258ef14454459a
- https://github.com/ash-project/ash_authentication_oauth2_server/security/advisories/GHSA-wwxg-h779-3wf4
- https://osv.dev/vulnerability/EEF-CVE-2026-82754

### [CVE-2026-86497](https://www.jetbrains.com/privacy-security/issues-fixed/)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-86497
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-08 02:17:28 JST
- 更新日: 2026-09-08 02:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In JetBrains YouTrack before 2026.2.18769 changing a mailbox host without re-authentication allowed a project administrator to exfiltrate stored mailbox credentials
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.jetbrains.com/privacy-security/issues-fixed/

### [CVE-2026-82584](https://cna.erlef.org/cves/CVE-2026-82584.html)

> **Backend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-82584
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-08 08:16:51 JST
- 更新日: 2026-09-08 08:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper Neutralization of Escape, Meta, or Control Sequences vulnerability in ash-project igniter allows a malicious package publisher to forge the mix igniter.install confirmation prompt. mix igniter.install prints a confirmation panel (an anti-typosquatting safeguard) listing a package's hex metadata before adding i...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-82584.html
- https://github.com/ash-project/igniter/commit/d492b1aa33f8fb0dacc0afa41b703fb922d42816
- https://github.com/ash-project/igniter/security/advisories/GHSA-cj7w-j579-gc42
- https://osv.dev/vulnerability/EEF-CVE-2026-82584

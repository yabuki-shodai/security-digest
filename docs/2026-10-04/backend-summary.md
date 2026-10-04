# Backend CVE Summary (2026-10-04)

## Overview

- 取得日時: 2026-10-04 09:32:26 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 3
- Critical: 0
- High: 1
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-105127](https://github.com/laradashboard/laradashboard)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-105127
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-04 09:16:36 JST
- 更新日: 2026-10-04 09:16:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LaraDashboard 1.4.2 before 1.4.8 applies advanced email validation to unauthenticated forgot-password and reset-password requests, triggering DNS lookups and paid AbstractAPI verification calls. Unauthenticated attackers can submit arbitrary addresses to exhaust the verification quota, making validation fail open for a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/laradashboard/laradashboard
- https://github.com/laradashboard/laradashboard/blob/v1.4.2/app/Http/Requests/Auth/ForgotPasswordRequest.php#L22-L27
- https://github.com/laradashboard/laradashboard/blob/v1.4.2/app/Http/Requests/Auth/ResetPasswordRequest.php#L23-L30
- https://github.com/laradashboard/laradashboard/blob/v1.4.2/app/Services/EmailDomainCheckService.php#L128
- https://github.com/laradashboard/laradashboard/blob/v1.4.2/app/Services/EmailVerificationService.php#L95-L114

### [CVE-2026-105126](https://github.com/laradashboard/laradashboard)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-105126
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-04 09:16:36 JST
- 更新日: 2026-10-04 09:16:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LaraDashboard before 1.4.8 contains an improper privilege management vulnerability that allows authenticated Admin users to escalate to Superadmin by editing or renaming roles. Attackers with role.edit can rename their role to Superadmin or grant user.login_as permissions to take over accounts and reach core upgrade an...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/laradashboard/laradashboard
- https://github.com/laradashboard/laradashboard/blob/v1.4.2/app/Http/Controllers/Backend/RoleController.php#L144
- https://github.com/laradashboard/laradashboard/blob/v1.4.2/app/Http/Controllers/Backend/RoleController.php#L180
- https://github.com/laradashboard/laradashboard/blob/v1.4.2/app/Http/Requests/CoreUpgrade/UploadRequest.php#L23
- https://github.com/laradashboard/laradashboard/blob/v1.4.2/app/Policies/RolePolicy.php#L39-L50

### [CVE-2026-105124](https://github.com/vincent-peugnet/wcms)

> **Backend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-105124
- 関連キーワード: gin, echo
- 影響製品: -
- 公開日: 2026-10-04 09:16:35 JST
- 更新日: 2026-10-04 09:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: W (vincent-peugnet/wcms) through 3.18.0 contains a stored cross-site scripting vulnerability that allows unauthenticated attackers to inject scripts via the login user field and visitor comment website field. Attackers can submit failed logins rendered unescaped in the adminlog.php log viewer, or comment URLs echoed in...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vincent-peugnet/wcms
- https://github.com/vincent-peugnet/wcms/blob/cda5bcdb95dbdb1e804fdfe0e5fd2e2b2f8a90e2/app/class/Controllerconnect.php#L56
- https://github.com/vincent-peugnet/wcms/blob/cda5bcdb95dbdb1e804fdfe0e5fd2e2b2f8a90e2/app/view/templates/adminlog.php#L71
- https://github.com/vincent-peugnet/wcms/blob/cda5bcdb95dbdb1e804fdfe0e5fd2e2b2f8a90e2/app/view/templates/editrightbar.php#L110
- https://github.com/vincent-peugnet/wcms/issues/662

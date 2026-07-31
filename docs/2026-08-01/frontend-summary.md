# Frontend CVE Summary (2026-08-01)

## Overview

- 取得日時: 2026-08-01 08:13:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 3
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-52232](https://github.com/whitewhale-dmb/Vulnerability-Research/tree/main/CVE-2026-52232)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-52232
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-08-01 07:17:02 JST
- 更新日: 2026-08-01 07:17:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A reflected cross-site scripting (XSS) vulnerability in the /logo.asp component of FS Inc S3150-8T2F Switch 2.2.0D Build 118101 allows attackers to execute arbitrary Javascript in the context of the victim's browser via a crafted URL.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/whitewhale-dmb/Vulnerability-Research/tree/main/CVE-2026-52232

### [CVE-2026-59232](https://github.com/Roskus/prospero-flow-crm/commit/8b2633ddb2178c2f79718efdfb906e051ba2f03c)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-59232
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-01 01:17:08 JST
- 更新日: 2026-08-01 03:17:18 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Cross-site Scripting in the lead index view in Roskus Prospero Flow CRM before 5.3.7 allows authenticated users holding the create or update lead permission to execute arbitrary JavaScript in the application origin via HTML markup stored in the lead name field, which the view renders through Blade's unescaped output di...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Roskus/prospero-flow-crm/commit/8b2633ddb2178c2f79718efdfb906e051ba2f03c
- https://github.com/Roskus/prospero-flow-crm/releases/tag/v5.5.3
- https://secur0.com/en/cna/cve-list/cve-2026-59232-stored-xss-in-prospero-flow-crm-lead-name-field

### [CVE-2026-62324](https://github.com/xdan/jodit/commit/5fba6ef2381d151d7cb8e3c5ad0b9996af0f97b0)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-62324
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-01 05:16:53 JST
- 更新日: 2026-08-01 05:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Jodit Editor is a WYSIWYG editor with a built-in file browser & image editor. Prior to 4.12.31, Jodit's sanitizeHTMLElement method fails to use isDangerousUrl to normalize javascript: href values before checking the scheme, allowing case variants, control-byte prefixes, and embedded tabs or newlines to bypass filtering...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/xdan/jodit/commit/5fba6ef2381d151d7cb8e3c5ad0b9996af0f97b0
- https://github.com/xdan/jodit/releases/tag/4.12.31
- https://github.com/xdan/jodit/security/advisories/GHSA-j839-gqq4-gf9j

# Frontend CVE Summary (2026-10-12)

## Overview

- 取得日時: 2026-10-12 10:15:24 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-108903](https://github.com/pH7Software/pH7-Social-Dating-CMS)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-108903
- 関連キーワード: vite, gin
- 影響製品: -
- 公開日: 2026-10-12 00:16:56 JST
- 更新日: 2026-10-12 00:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pH7Builder (pH7 Social Dating CMS) before 19.3.0 contains a CAPTCHA bypass vulnerability that allows unauthenticated attackers to skip form validation by supplying a client-chosen form ID to PFBC Form::isValid(). Attackers can load a CAPTCHA-free form like login or search, then submit its ID with contact, comment, foru...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pH7Software/pH7-Social-Dating-CMS
- https://github.com/pH7Software/pH7-Social-Dating-CMS/blob/v19.2.0/_protected/app/system/modules/contact/forms/ContactForm.php#L33-L38
- https://github.com/pH7Software/pH7-Social-Dating-CMS/commit/4758d7d2ebfd5772faa25ef728c14f8f452e82f4
- https://www.vulncheck.com/advisories/ph7builder-before-19.3.0-captcha-bypass-via-client-chosen-form-id

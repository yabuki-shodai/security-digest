# Frontend CVE Summary (2026-10-01)

## Overview

- 取得日時: 2026-10-01 10:14:49 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 2
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-103388](https://github.com/MISP/MISP/commit/118528767)

> **Frontend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-103388
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-01 00:22:27 JST
- 更新日: 2026-10-01 01:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MISP renders the source field of a Galaxy Cluster as a clickable hyperlink whenever the stored value passes PHP's FILTER_VALIDATE_URL validation. Because FILTER_VALIDATE_URL accepts the javascript: URI scheme, a user with galaxy editor privileges on the local instance or on a synced instance could store a javascript: U...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/MISP/MISP/commit/118528767

### [CVE-2026-103389](https://github.com/MISP/MISP/commit/8ea5783dd)

> **Frontend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-103389
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-01 00:22:27 JST
- 更新日: 2026-10-01 01:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MISP contains a stored cross-site scripting (XSS) vulnerability in the galaxy icon handling path. The icon field of a galaxy object was persisted without any server-side validation through the galaxy add, edit, and sync/import capture endpoints. The stored value was subsequently concatenated directly into HTML markup b...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/MISP/MISP/commit/8ea5783dd

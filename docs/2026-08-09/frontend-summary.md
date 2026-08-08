# Frontend CVE Summary (2026-08-09)

## Overview

- 取得日時: 2026-08-09 07:42:20 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-71502](https://github.com/MISP/cti-transmute/commit/4f43c9181a00262bec2a6dfbc9ff9c50d534e918)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-71502
- 関連キーワード: javascript, vue, gin, express
- 影響製品: -
- 公開日: 2026-08-09 07:16:34 JST
- 更新日: 2026-08-09 07:16:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CTI-Transmute contains a stored cross-site scripting vulnerability caused by insufficient neutralization of Vue template expression delimiters in server-rendered user-controlled data. An unauthenticated attacker can create a public conversion whose name or description contains a malicious Vue expression using the appli...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/MISP/cti-transmute/commit/4f43c9181a00262bec2a6dfbc9ff9c50d534e918
- https://github.com/MISP/cti-transmute/commit/522fa8ff8223b12a6128ea3fc2344a77b7b9108d
- https://github.com/MISP/cti-transmute/commit/ad8bf2b8031491cefb552314ef7ff6f4148ca95a
- https://github.com/MISP/cti-transmute/commit/ecfdaef63860a071c6f07afd30156ca77a77ad2b

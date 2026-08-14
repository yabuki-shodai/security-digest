# Frontend CVE Summary (2026-08-15)

## Overview

- 取得日時: 2026-08-15 07:35:40 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-50029](https://github.com/sunnyadn/js-toml/commit/e0504fa5d3dcde2d1d588c9001c24b7b700beeeb)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-50029
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-15 04:17:18 JST
- 更新日: 2026-08-15 04:17:18 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: js-toml is a TOML parser for JavaScript, Prior to version 1.1.2, the interpreter checks whether a key already exists in a parser-built container with `if (object[key])` instead of `if (key in object)`. When the prior value is a falsy primitive — `false`, `0`, `0n`, `0.0`, `-0`, or `""` — the duplicate-key branch is ski...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/sunnyadn/js-toml/commit/e0504fa5d3dcde2d1d588c9001c24b7b700beeeb
- https://github.com/sunnyadn/js-toml/releases/tag/v1.1.2
- https://github.com/sunnyadn/js-toml/security/advisories/GHSA-m34p-749j-x6m6

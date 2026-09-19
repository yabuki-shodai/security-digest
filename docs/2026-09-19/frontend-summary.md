# Frontend CVE Summary (2026-09-19)

## Overview

- 取得日時: 2026-09-19 09:14:05 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 0
- High: 3
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-84992](https://github.com/imzbf/md-editor-v3/commit/2c07360420e74087f5bc63032ab155d93e0a0b10)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-84992
- 関連キーワード: typescript, javascript, vue, gin
- 影響製品: -
- 公開日: 2026-09-19 03:17:17 JST
- 更新日: 2026-09-19 03:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: md-editor-v3 is a Markdown editor for Vue 3 developed in JSX and TypeScript. Prior to 6.5.4, MdPreview's useMarkdownIt() highlight callback in packages/MdEditor/layouts/Content/composition/useMarkdownIt.ts inserts a fenced-code language value into class and language HTML attributes without escaping or consistently quot...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/imzbf/md-editor-v3/commit/2c07360420e74087f5bc63032ab155d93e0a0b10
- https://github.com/imzbf/md-editor-v3/releases/tag/v6.5.4
- https://github.com/imzbf/md-editor-v3/security/advisories/GHSA-3rm2-h79c-8qw6
- https://github.com/imzbf/md-editor-v3/security/advisories/GHSA-3rm2-h79c-8qw6

### [CVE-2026-93759](https://jira.mongodb.org/browse/MONGOID-5993)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-93759
- 関連キーワード: javascript, go, gin, express
- 影響製品: -
- 公開日: 2026-09-19 03:18:34 JST
- 更新日: 2026-09-19 04:05:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mongoid does not neutralize a string-typed query criterion supplied to its query builder, and instead passes it to the database as a server-side JavaScript expression. An unauthenticated party able to influence the value an application supplies as a query argument may cause code of their choosing to be evaluated by the...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/MONGOID-5993

### [CVE-2026-77301](https://github.com/cthackers/adm-zip/commit/491600683dacb6cb9fe0718a0eeb9cb5eb49afa6)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-77301
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-09-19 02:17:00 JST
- 更新日: 2026-09-19 03:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: adm-zip is a JavaScript library for creating and extracting ZIP archives in Node.js. Prior to 0.6.1, getData() in zipEntry.js trusts an entry's central-directory uncompressed size and allocates output memory before validating that value against the actual compressed data and decompression result. A small crafted ZIP ca...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/cthackers/adm-zip/commit/491600683dacb6cb9fe0718a0eeb9cb5eb49afa6
- https://github.com/cthackers/adm-zip/releases/tag/v0.6.1
- https://github.com/cthackers/adm-zip/security/advisories/GHSA-7q85-xj36-vmfc
- https://github.com/cthackers/adm-zip/security/advisories/GHSA-7q85-xj36-vmfc

### [CVE-2026-91127](https://github.com/flyfish-dev/file-viewer/commit/ef045680f8d9830a3eee9612f7df46a734361b07)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-91127
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-19 03:18:02 JST
- 更新日: 2026-09-19 03:18:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: File Viewer is a browser-native viewer for Office, PDF, CAD, archive, and other files in private and internal web applications. Prior to @file-viewer/doc 2.3.1 and msdoc-viewer 0.2.2, the legacy DOC renderer emitted document-controlled hyperlink targets into generated HTML after character escaping but without restricti...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/flyfish-dev/file-viewer/commit/ef045680f8d9830a3eee9612f7df46a734361b07
- https://github.com/flyfish-dev/file-viewer/releases/tag/v2.3.1
- https://github.com/flyfish-dev/file-viewer/security/advisories/GHSA-3753-m2x2-q623

### [CVE-2025-36147](https://www.ibm.com/support/pages/node/7285838)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2025-36147
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-19 01:17:03 JST
- 更新日: 2026-09-19 03:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Financial Transaction Manager for SWIFT Services for Multiplatforms 3.2.4.0 through 3.2.4.16 is vulnerable to cross-site scripting. This vulnerability allows an unauthenticated attacker to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials discl...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7285838

### [CVE-2026-1025](https://www.ibm.com/support/pages/node/7286490)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-1025
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-19 01:17:06 JST
- 更新日: 2026-09-19 03:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Common Licensing Agent 9.0, Agent 9.0.0.1, Agent 9.0.0.2, ART 9.0, ART 9.0.0.1, and ART 9.0.0.2 is vulnerable to cross-site scripting. This vulnerability allows users to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials disclosure within a trus...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7286490

### [CVE-2026-1029](https://www.ibm.com/support/pages/node/7286490)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-1029
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-19 01:17:06 JST
- 更新日: 2026-09-19 03:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Common Licensing Agent 9.0, Agent 9.0.0.1, Agent 9.0.0.2, ART 9.0, ART 9.0.0.1, and ART 9.0.0.2 is vulnerable to cross-site scripting. This vulnerability allows users to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials disclosure within a trus...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7286490

### [CVE-2026-1031](https://www.ibm.com/support/pages/node/7286490)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-1031
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-19 01:17:06 JST
- 更新日: 2026-09-19 03:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Common Licensing Agent 9.0, Agent 9.0.0.1, Agent 9.0.0.2, ART 9.0, ART 9.0.0.1, and ART 9.0.0.2 is vulnerable to cross-site scripting. This vulnerability allows an unauthenticated attacker to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials di...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7286490

### [CVE-2026-1037](https://www.ibm.com/support/pages/node/7286490)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-1037
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-19 01:17:06 JST
- 更新日: 2026-09-19 03:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Common Licensing Agent 9.0, Agent 9.0.0.1, Agent 9.0.0.2, ART 9.0, ART 9.0.0.1, and ART 9.0.0.2 is vulnerable to cross-site scripting. This vulnerability allows an unauthenticated attacker to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials di...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7286490

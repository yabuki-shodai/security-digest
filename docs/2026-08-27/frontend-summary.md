# Frontend CVE Summary (2026-08-27)

## Overview

- 取得日時: 2026-08-27 12:06:15 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 1
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-80426](https://github.com/voxel51/fiftyone)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-80426
- 関連キーワード: react, gin
- 影響製品: -
- 公開日: 2026-08-27 01:16:44 JST
- 更新日: 2026-08-27 04:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FiftyOne renders a dataset field's description as markup. The sidebar field-information component at app/packages/core/src/components/FieldLabelAndInfo/index.tsx passes the description string to React's dangerouslySetInnerHTML, and no layer between storage and render escapes or sanitises it; the neighbouring info value...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/voxel51/fiftyone
- https://github.com/voxel51/fiftyone/blob/v1.20.1/app/packages/core/src/components/FieldLabelAndInfo/index.tsx
- https://github.com/voxel51/fiftyone/pull/8117
- https://github.com/voxel51/fiftyone/releases/tag/v1.21.0
- https://www.vulncheck.com/advisories/fiftyone-before-1.21.0-stored-cross-site-scripting-via-unescaped-field-description

### [CVE-2026-47848](https://spring.io/security/cve-2026-47848)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-47848
- 関連キーワード: react, gin
- 影響製品: -
- 公開日: 2026-08-27 05:17:27 JST
- 更新日: 2026-08-27 05:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In specific scenarios involving WebSocket handshake redirects to a different origin, the Reactor Netty WebSocket client may leak credentials. In order for this to happen, the HTTP client must have been explicitly configured to follow redirects. Reactor Netty 1.3.0 - 1.3.6 Reactor Netty 1.1.0 - 1.2.18 Reactor Netty 1.0....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://spring.io/security/cve-2026-47848

### [CVE-2026-47844](https://spring.io/security/cve-2026-47844)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-47844
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-08-27 05:17:26 JST
- 更新日: 2026-08-27 05:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In specific scenarios, the Reactor Netty HTTP Server may leak exception details across unrelated requests. In order for this to happen, the server must be configured with Brave Tracing. Reactor Netty 1.3.0 - 1.3.6 Reactor Netty 1.1.0 - 1.2.18 Reactor Netty 1.0.52 and earlier
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://spring.io/security/cve-2026-47844

### [CVE-2026-47843](https://spring.io/security/cve-2026-47843)

> **Frontend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-47843
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-08-27 05:17:26 JST
- 更新日: 2026-08-27 05:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In specific scenarios involving multiple clients with different DNS resolver configurations, Reactor Netty may incorrectly reuse a previously configured DNS resolver. Reactor Netty 1.3.0 - 1.3.6 Reactor Netty 1.1.0 - 1.2.18 Reactor Netty 1.0.52 and earlier
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://spring.io/security/cve-2026-47843

### [CVE-2026-81035](https://github.com/midday-ai/midday)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-81035
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-08-27 01:16:46 JST
- 更新日: 2026-08-27 02:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Midday allows any member of a team to delete it. The delete procedure in apps/api/src/trpc/routers/team.ts authorises the caller with the team-access helper, which returns true for every row in the team-membership table irrespective of the role it records, and the data-layer function it calls re-checks the same helper...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/midday-ai/midday
- https://github.com/midday-ai/midday/blob/e5f45ed0d49cdb34576373623c4579b72daa74c1/apps/api/src/trpc/routers/team.ts
- https://github.com/midday-ai/midday/issues/890
- https://www.vulncheck.com/advisories/midday-missing-owner-check-on-team-deletion
- https://github.com/midday-ai/midday/issues/890

### [CVE-2026-54569](https://github.com/senaite/senaite.core/commit/a24d65e99a17ac43c5374ed9f0a60d0fe60d2f74)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-54569
- 関連キーワード: zod, python, gin
- 影響製品: -
- 公開日: 2026-08-27 01:16:27 JST
- 更新日: 2026-08-27 03:16:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SENAITE.CORE is the core framework for the SENAITE laboratory information management system. From 2.0.0 to 2.6.0, the SENAITE.CORE JSON API permits unauthenticated remote code execution through a two-request chain involving missing authorization and unsafe evaluation. The state-changing routes in src/bika/lims/jsonapi/...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/senaite/senaite.core/commit/a24d65e99a17ac43c5374ed9f0a60d0fe60d2f74
- https://github.com/senaite/senaite.core/commit/ef4b6d73575b0fbc0edc6114e5e025089aaf9eb7
- https://github.com/senaite/senaite.core/pull/2903
- https://github.com/senaite/senaite.core/pull/2919
- https://github.com/senaite/senaite.core/security/advisories/GHSA-jrw6-7x4q-w25j

### [CVE-2026-66003](https://github.com/frappe/frappe/releases/tag/v15.115.0)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-66003
- 関連キーワード: javascript, python
- 影響製品: -
- 公開日: 2026-08-27 05:17:56 JST
- 更新日: 2026-08-27 05:17:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Frappe is a full-stack web application framework written in Python and JavaScript. Prior to version 15.115.0, an access control bypass in the REST API allows a user to read data from Linked DocTypes that they are not authorized to access. When a document references another document through a Link field, the framework d...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/frappe/frappe/releases/tag/v15.115.0
- https://github.com/frappe/frappe/security/advisories/GHSA-p25m-7rvg-6fvr

### [CVE-2026-54606](https://github.com/JiHong88/suneditor/commit/9d43a5e082101d2d6475cba86e0d58d7c2cf6677)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-54606
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-27 01:16:27 JST
- 更新日: 2026-08-27 04:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SunEditor is a lightweight and powerful WYSIWYG editor in vanilla JavaScript with no dependencies. Prior to 3.1.4, the SunEditor Embed plugin in src/plugins/modal/embed.js parses attacker-controlled raw embed HTML with DOMParser and processes the resulting DOM nodes. When an external script element follows a valid ifra...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/JiHong88/suneditor/commit/9d43a5e082101d2d6475cba86e0d58d7c2cf6677
- https://github.com/JiHong88/suneditor/issues/1649
- https://github.com/JiHong88/suneditor/releases/tag/3.1.4
- https://github.com/JiHong88/suneditor/security/advisories/GHSA-w93q-cq9w-58p7
- https://github.com/JiHong88/suneditor/security/advisories/GHSA-w93q-cq9w-58p7

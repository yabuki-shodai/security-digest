# Frontend CVE Summary (2026-08-12)

## Overview

- 取得日時: 2026-08-12 07:57:23 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 3
- Critical: 1
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-72925](https://github.com/swc-project/swc/commit/e1877b44bdac8abc9fd51e984d584f40f6999832)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-72925
- 関連キーワード: typescript, javascript, swc, gin
- 影響製品: -
- 公開日: 2026-08-12 00:17:38 JST
- 更新日: 2026-08-12 04:18:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SWC is a TypeScript / JavaScript compiler written in Rust. Prior to @swc/html 1.15.47-nightly-20260729.1 and swc_html_minifier 59.0.0, the minifyJson processing in crates/swc_html_minifier/src/lib.rs parsed and serialized attacker-controlled JSON in application/json and application/ld+json script elements without the e...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/swc-project/swc/commit/e1877b44bdac8abc9fd51e984d584f40f6999832
- https://github.com/swc-project/swc/pull/12080
- https://github.com/swc-project/swc/releases/tag/v1.15.47
- https://github.com/swc-project/swc/releases/tag/v1.15.47-nightly-20260729.1
- https://github.com/swc-project/swc/security/advisories/GHSA-5qr2-v392-m9g8

### [CVE-2026-73069](https://github.com/twentyhq/twenty/commit/0b8368cd6c1a47711bf52972800f162bde0bbab9)

> **Frontend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-73069
- 関連キーワード: graphql, gin, express, postgresql
- 影響製品: -
- 公開日: 2026-08-12 01:17:38 JST
- 更新日: 2026-08-12 04:18:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Twenty is an open-source CRM (customer relationship management) platform. Prior to 2.15.0, Twenty allowed a workspace administrator with the DATA_MODEL permission to supply settings.asExpression for the system TS_VECTOR field searchVector through PATCH /rest/metadata/fields/:id or the updateOneField GraphQL mutation, c...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/twentyhq/twenty/commit/0b8368cd6c1a47711bf52972800f162bde0bbab9
- https://github.com/twentyhq/twenty/pull/21947
- https://github.com/twentyhq/twenty/security/advisories/GHSA-mm7j-q9q3-qqwj
- https://github.com/twentyhq/twenty/security/advisories/GHSA-mm7j-q9q3-qqwj

### [CVE-2026-21269](https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html)

> **Frontend** / **MEDIUM** / CVSS: **4.6** / KEV: **no**

- タイトル: CVE-2026-21269
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-12 02:17:55 JST
- 更新日: 2026-08-12 03:17:24 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: is affected by a stored Cross-Site Scripting (XSS) vulnerability that could be abused by a low-privileged attacker to inject malicious scripts into vulnerable form fields. Malicious JavaScript may be executed in a victim's browser when they browse to the page containing the vulnerable field. Scope is changed.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://helpx.adobe.com/security/products/coldfusion/apsb26-90.html

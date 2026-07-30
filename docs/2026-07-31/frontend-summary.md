# Frontend CVE Summary (2026-07-31)

## Overview

- 取得日時: 2026-07-31 08:16:03 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 7
- Critical: 1
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-18245](https://aws.amazon.com/security/security-bulletins/2026-066-aws/)

> **Frontend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-18245
- 関連キーワード: react, aws
- 影響製品: -
- 公開日: 2026-07-31 04:17:26 JST
- 更新日: 2026-07-31 05:17:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Improper control of code generation in Amazon @aws-amplify/codegen-ui-react before 2.20.6 might allow a remote authenticated user to execute arbitrary code in end-user browsers, developer machines, CI/CD environments, and server-side rendering contexts via crafted Studio component or theme schema values due to insuffic...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-066-aws/
- https://github.com/aws-amplify/amplify-codegen-ui/releases/tag/v2.20.6
- https://github.com/aws-amplify/amplify-codegen-ui/security/advisories/GHSA-74xx-rjgf-m69j

### [CVE-2026-48910](https://lists.apache.org/thread/yvbdjnocw5qq3xkbjs9h77ghlg0bsw2c)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-48910
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-31 01:17:12 JST
- 更新日: 2026-07-31 04:33:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A carefully crafted editing request could trigger an XSS vulnerability on Apache JSPWiki when parsing errors on the markdown renderer, which could allow the attacker to execute javascript in the victim's browser and get some sensitive information about the victim. This issue affects Apache JSPWiki: through 2.12.3. User...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://lists.apache.org/thread/yvbdjnocw5qq3xkbjs9h77ghlg0bsw2c
- http://www.openwall.com/lists/oss-security/2026/07/30/18

### [CVE-2025-0152](https://www.ibm.com/support/pages/node/7279145)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2025-0152
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-31 04:16:57 JST
- 更新日: 2026-07-31 04:31:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: IBM Engineering Requirements Management DOORS and DOORS Web Access 9.7.2.1 through 9.7.2.11, and 9.6.1.1 through 9.6.1.13 is vulnerable to cross-site scripting. This vulnerability allows an unauthenticated attacker to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially lea...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7279145

### [CVE-2025-51684](https://github.com/CleverTap/clevertap-web-sdk/issues/416)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2025-51684
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-31 05:16:51 JST
- 更新日: 2026-07-31 05:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CleverTap Web SDK v1.15.1 is vulnerable to Cross Site Scripting (XSS). The application does not sanitize untrusted data received via window.postMessage before injecting it into the page DOM. An attacker can craft a malicious message that, when processed by renderCustomHtml, results in execution of arbitrary JavaScript...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/CleverTap/clevertap-web-sdk/issues/416

### [CVE-2025-36298](https://www.ibm.com/support/pages/node/7280668)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2025-36298
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-31 00:16:22 JST
- 更新日: 2026-07-31 01:33:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: IBM Sterling B2B Integrator 6.1.2.0 through 6.1.2.7_2, 6.2.0.0 through 6.2.0.5_2, 6.2.1.0 through 6.2.1.1_2, and 6.2.2.0 through 6.2.2.0_1 and IBM Sterling File Gateway 6.1.2.0 through 6.1.2.7_2, 6.2.0.0 through 6.2.0.5_2, 6.2.1.0 through 6.2.1.1_2, and 6.2.2.0 through 6.2.2.0_1 Ebics server component is vulnerable to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7280668

### [CVE-2025-36431](https://www.ibm.com/support/pages/node/7280647)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2025-36431
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-31 00:16:23 JST
- 更新日: 2026-07-31 02:16:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: IBM Sterling B2B Integrator 6.2.2.0 through 6.2.2.0_1 and IBM Sterling File Gateway 6.2.2.0 through 6.2.2.0_1 is vulnerable to cross-site scripting. This vulnerability allows an authenticated user to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credential...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7280647

### [CVE-2026-61526](https://github.com/adonisjs/http-server/commit/5d7465d599753b1fce8a36da18955f2c273e4f87)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-61526
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-31 06:18:12 JST
- 更新日: 2026-07-31 06:18:12 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: AdonisJS HTTP Server is a package for handling HTTP requests in the AdonisJS framework. In versions 8.0.0-next.0 through 8.2.0 and 9.0.0 through 9.0.2, the error.message is interpolated into the default HTML exception response without escaping, allowing a crafted missing-route URL to execute attacker-controlled JavaScr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/adonisjs/http-server/commit/5d7465d599753b1fce8a36da18955f2c273e4f87
- https://github.com/adonisjs/http-server/commit/71a0a8e375c375e3588ba44ef68b0ef5a993c3d3
- https://github.com/adonisjs/http-server/releases/tag/v8.2.1
- https://github.com/adonisjs/http-server/releases/tag/v9.1.0
- https://github.com/adonisjs/http-server/security/advisories/GHSA-cwm9-gfhc-46f6

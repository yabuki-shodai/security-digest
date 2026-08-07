# Frontend CVE Summary (2026-08-07)

## Overview

- 取得日時: 2026-08-07 10:32:55 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 4
- Critical: 0
- High: 1
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-5423](https://github.com/neo4j/graphql/security/advisories/GHSA-fcpg-3fw5-vc65)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-5423
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-08-07 01:16:44 JST
- 更新日: 2026-08-07 07:18:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: @neo4j/graphql library versions prior to 7.5.6 fail to verify the authenticity of a client-supplied, pre-decoded JWT object passed through GraphQL subscription connectionParams. As a result, any unauthenticated remote client that can open a GraphQL-over-WebSocket connection can forge arbitrary JWT claims (e.g. sub, rol...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/neo4j/graphql/security/advisories/GHSA-fcpg-3fw5-vc65
- https://neo4j.com/security/CVE-2026-5423

### [CVE-2026-66829](https://cna.erlef.org/cves/CVE-2026-66829.html)

> **Frontend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-66829
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-07 01:16:49 JST
- 更新日: 2026-08-07 07:18:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: URL Redirection to Untrusted Site ('Open Redirect') vulnerability in the HTML5 scrubber in rrrene html_sanitize_ex allows a remote attacker to force visitors of a page to navigate to a site of the attacker's choosing via a <meta http-equiv="refresh"> element in sanitized HTML. HtmlSanitizeEx.html5/1 keeps attacker-supp...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-66829.html
- https://github.com/rrrene/html_sanitize_ex/commit/9f7e38be51edc38f132dfe994f37af5cf5e0e76f
- https://github.com/rrrene/html_sanitize_ex/security/advisories/GHSA-2c6f-3j54-xpcr
- https://osv.dev/vulnerability/EEF-CVE-2026-66829

### [CVE-2026-66683](https://patchstack.com/database/wordpress/plugin/custom-css-and-javascript/vulnerability/wordpress-custom-css-and-javascript-plugin-2-0-16-sensitive-data-exposure-vulnerability?_s_id=cve)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-66683
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-07 00:17:21 JST
- 更新日: 2026-08-07 07:18:19 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Unauthenticated Sensitive Data Exposure in Custom CSS and JavaScript <= 2.0.16 versions.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://patchstack.com/database/wordpress/plugin/custom-css-and-javascript/vulnerability/wordpress-custom-css-and-javascript-plugin-2-0-16-sensitive-data-exposure-vulnerability?_s_id=cve

### [CVE-2026-66843](https://cna.erlef.org/cves/CVE-2026-66843.html)

> **Frontend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-66843
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-07 01:16:49 JST
- 更新日: 2026-08-07 07:18:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Inclusion of Functionality from Untrusted Control Sphere vulnerability in the HTML5 scrubber in rrrene html_sanitize_ex allows a remote attacker to load a document of their choosing into a trusted page via the data attribute of an <object> element in sanitized HTML. object is the one URI-bearing element in lib/html_san...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-66843.html
- https://github.com/rrrene/html_sanitize_ex/commit/bec27fec4de99e40c68c4285a610e09e791a3eaf
- https://github.com/rrrene/html_sanitize_ex/security/advisories/GHSA-xmm9-jc22-rcgj
- https://osv.dev/vulnerability/EEF-CVE-2026-66843

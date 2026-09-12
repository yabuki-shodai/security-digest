# Frontend CVE Summary (2026-09-12)

## Overview

- 取得日時: 2026-09-12 09:12:37 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 6
- Critical: 1
- High: 1
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-54072](https://github.com/authorizerdev/authorizer/security/advisories/GHSA-h29v-hj44-q8cv)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-54072
- 関連キーワード: vite, graphql, go, gin
- 影響製品: -
- 公開日: 2026-09-12 04:17:42 JST
- 更新日: 2026-09-12 04:17:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Authorizer is an open-source, self-hostable authentication and authorization server. Prior to version 2.2.1, the `/authorize` endpoint accepts any `redirect_uri` without validating it against `AllowedOrigins`. When `response_type=token` or `response_type=id_token`, the server appends `access_token`, `id_token`, and `re...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/authorizerdev/authorizer/security/advisories/GHSA-h29v-hj44-q8cv

### [CVE-2026-62102](https://patchstack.com/database/wordpress/plugin/gatographql/vulnerability/wordpress-gato-graphql-plugin-19-2-3-privilege-escalation-vulnerability?_s_id=cve)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-62102
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-09-12 04:17:43 JST
- 更新日: 2026-09-12 06:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Subscriber Privilege Escalation in Gato GraphQL <= 19.2.3 versions.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://patchstack.com/database/wordpress/plugin/gatographql/vulnerability/wordpress-gato-graphql-plugin-19-2-3-privilege-escalation-vulnerability?_s_id=cve

### [CVE-2026-81911](https://documentation.concretecms.org/developers/introduction/version-history/953-release-notes)

> **Frontend** / **MEDIUM** / CVSS: **5.8** / KEV: **no**

- タイトル: CVE-2026-81911
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-12 05:19:13 JST
- 更新日: 2026-09-12 05:19:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Concrete CMS versions 9.0.0 to 9.5.2 is vulnerable to Stored XSS in Board Custom Slot dialog. The custom_slot save_template endpoint authorizes the request only against the target board instance (canEditBoardContents()) and then persists the client-supplied selectedTemplateOption[collection] verbatim, rather than rebui...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://documentation.concretecms.org/developers/introduction/version-history/953-release-notes

### [CVE-2026-49462](https://github.com/nl-portal/nl-portal-backend-libraries/commit/0d2af7665a737e91565352bd4e6124cacaa853b7)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-49462
- 関連キーワード: graphql, go
- 影響製品: -
- 公開日: 2026-09-12 05:17:13 JST
- 更新日: 2026-09-12 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NL Portal Backend Libraries provide backend components for Dutch government portals that interact with residents, customers, suppliers, and partner organizations. In versions up to and including 3.0.0, deployments using the shipped default configuration exposed two GraphQL developer features without requiring authentic...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nl-portal/nl-portal-backend-libraries/commit/0d2af7665a737e91565352bd4e6124cacaa853b7
- https://github.com/nl-portal/nl-portal-backend-libraries/security/advisories/GHSA-9m9w-2vqr-m384

### [CVE-2026-49463](https://github.com/nl-portal/nl-portal-backend-libraries/security/advisories/GHSA-qpm9-h556-mwxm)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-49463
- 関連キーワード: graphql, go
- 影響製品: -
- 公開日: 2026-09-12 05:17:13 JST
- 更新日: 2026-09-12 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NL Portal Backend Libraries provide backend components for Dutch government portals that interact with residents, customers, suppliers, and partner organizations. The `nl.nl-portal:documenten-api` package through version 3.0.0 and the `nl.nl-portal:besluiten` package from version 1.5.0 through 3.0.0 lack per-user autho...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nl-portal/nl-portal-backend-libraries/security/advisories/GHSA-qpm9-h556-mwxm

### [CVE-2026-79035](https://github.com/nikolas-ch/CVEs/blob/main/ZetaMarketingPlatform/ReflectedXSS/ReflectedXSS.txt)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-79035
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-12 05:18:53 JST
- 更新日: 2026-09-12 05:18:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A reflected cross-site scripting (XSS) vulnerability in the p.rfihub.com component of Zeta Marketing Platform (ZMP) v1.0 allows attackers to execute arbitrary Javascript in the context of the victim's browser via injecting a crafted URL into the ca parameter.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nikolas-ch/CVEs/blob/main/ZetaMarketingPlatform/ReflectedXSS/ReflectedXSS.txt
- https://github.com/nikolas-ch/CVEs/tree/main/ZetaMarketingPlatform/ReflectedXSS

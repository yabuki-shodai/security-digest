# Frontend CVE Summary (2026-09-26)

## Overview

- 取得日時: 2026-09-26 09:34:33 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 0
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-56731](https://github.com/zammad/zammad/commit/16a4a2e1be6642ec0c3ba3a76e358ad065f48f78)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-56731
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-26 03:17:27 JST
- 更新日: 2026-09-26 05:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad is a web based open source helpdesk/customer support system. Prior to 7.0.1, a low-privilege authenticated user may inject arbitrary HTML markup, including JavaScript event handlers, into a ticket title via the standard ticket creation workflow. The title is persisted without sanitization. This issue is fixed in...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zammad/zammad/commit/16a4a2e1be6642ec0c3ba3a76e358ad065f48f78
- https://github.com/zammad/zammad/security/advisories/GHSA-p9xp-gx8r-4397

### [CVE-2026-67237](https://github.com/rabbitmq/rabbitmq-server/commit/5cd6d841d84450324a4613501ed917d98828af23)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-67237
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-26 02:17:11 JST
- 更新日: 2026-09-26 03:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RabbitMQ is a messaging and streaming broker. From 4.2.0 until 4.2.8 and 4.3.2, set_token_auth/2 inserted a bearer token from the Authorization header or access_token cookie into OAuth bootstrap JavaScript without escaping, allowing attacker-controlled token content to execute JavaScript in the management UI origin. Th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/rabbitmq/rabbitmq-server/commit/5cd6d841d84450324a4613501ed917d98828af23
- https://github.com/rabbitmq/rabbitmq-server/commit/a8041d528c1a71af4cb75ade247ed082fe6b83fb
- https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.2.8
- https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.3.2
- https://github.com/rabbitmq/rabbitmq-server/security/advisories/GHSA-2rf7-f6r6-8rwh

### [CVE-2026-67410](https://github.com/rabbitmq/rabbitmq-server/commit/60a85d3605ebf94fd234497242812547d441d457)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-67410
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-26 02:17:13 JST
- 更新日: 2026-09-26 03:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RabbitMQ is a messaging and streaming broker. From 4.2.0 until 4.3.3 and 4.2.9, OAuth2 Client Secret Exposed via Unauthenticated JavaScript Endpoint (CWE-200). when OAuth2 authentication is enabled for the RabbitMQ Management UI and the configured flow, IDP use a client secret, the oauthclientsecret configuration value...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/rabbitmq/rabbitmq-server/commit/60a85d3605ebf94fd234497242812547d441d457
- https://github.com/rabbitmq/rabbitmq-server/commit/869f800998334bb363f2ad046f58de9caedc409e
- https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.2.9
- https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.3.3
- https://github.com/rabbitmq/rabbitmq-server/security/advisories/GHSA-f9f2-q3jf-wfj3

### [CVE-2026-56728](https://github.com/zammad/zammad/commit/4ccd5d573023b66b0d0184914c92417e1780793f)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-56728
- 関連キーワード: graphql, gin
- 影響製品: -
- 公開日: 2026-09-26 03:17:26 JST
- 更新日: 2026-09-26 04:17:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad is a web based open source helpdesk/customer support system. Prior to 7.0.2, a broken access control vulnerability exists in Zammad's GraphQL API. An authenticated user can access taskbar item data belonging to another user by crafting a request with the target user's taskbar identifier. The taskbar feature stor...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zammad/zammad/commit/4ccd5d573023b66b0d0184914c92417e1780793f
- https://github.com/zammad/zammad/releases/tag/7.0.2
- https://github.com/zammad/zammad/security/advisories/GHSA-jvcg-5539-vvc3

### [CVE-2026-85293](https://github.com/InvoicePlane/InvoicePlane/commit/1e74c032ff1c65e6a4f9d173505f415c3a539f57)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-85293
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-26 01:17:28 JST
- 更新日: 2026-09-26 01:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: InvoicePlane is a self-hosted open source application for managing invoices, clients, and payments. In version 1.7.2-beta-1, InvoicePlane stores client_email values without enforcing email syntax and renders them unescaped inside double-quoted value attributes in the invoice mailer form and quote mailer form. An admini...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/InvoicePlane/InvoicePlane/commit/1e74c032ff1c65e6a4f9d173505f415c3a539f57
- https://github.com/InvoicePlane/InvoicePlane/pull/1635
- https://github.com/InvoicePlane/InvoicePlane/releases/tag/v1.7.2
- https://github.com/InvoicePlane/InvoicePlane/security/advisories/GHSA-477r-xmgc-vcvj
- https://github.com/InvoicePlane/InvoicePlane/security/advisories/GHSA-477r-xmgc-vcvj

### [CVE-2026-18312](https://kb.cert.org/vuls/id/699627)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-18312
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-26 02:17:07 JST
- 更新日: 2026-09-26 02:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Readwise Reader for Android constructs URLs in its WebView using attacker-controlled metadata without proper encoding or escaping. The application interpolates untrusted values directly into URL strings and inserts them into the DOM via innerHTML. Because the interpolation occurs without HTML or JavaScript context enco...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://kb.cert.org/vuls/id/699627

### [CVE-2026-63216](https://github.com/zammad/zammad/commit/74b4fd4db62dc3652bb9db24096a2fbd1b56dc7f)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-63216
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-26 04:17:55 JST
- 更新日: 2026-09-26 04:17:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, unsanitized option labels are rendered in the configuration dialogs of AI Agents within Zammad's admin UI. When rendering the list of selected options, the option label is output as raw HTML without escaping. An attacker who can control...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zammad/zammad/commit/74b4fd4db62dc3652bb9db24096a2fbd1b56dc7f
- https://github.com/zammad/zammad/security/advisories/GHSA-r95m-ghj7-646x

### [CVE-2026-56730](https://github.com/zammad/zammad/commit/b059bd1cac36b1eab04cfc0783799e38b8072da7)

> **Frontend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-56730
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-09-26 03:17:27 JST
- 更新日: 2026-09-26 03:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad is a web based open source helpdesk/customer support system. Prior to 7.0.2, an authorization bypass vulnerability was found that allows an authenticated agent to read knowledge base answer content they should not be able to access. The vulnerable GraphQL mutation is meant to transform a knowledge base answer su...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zammad/zammad/commit/b059bd1cac36b1eab04cfc0783799e38b8072da7
- https://github.com/zammad/zammad/releases/tag/7.0.2
- https://github.com/zammad/zammad/security/advisories/GHSA-pf47-8964-pp23

# Frontend CVE Summary (2026-09-25)

## Overview

- 取得日時: 2026-09-25 09:30:23 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 0
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-56744](https://github.com/bsv-blockchain/ts-stack/commit/3a11f6111919245a3090e9f3895cfc4f21a80d28)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-56744
- 関連キーワード: npm, gin
- 影響製品: -
- 公開日: 2026-09-25 02:17:05 JST
- 更新日: 2026-09-25 02:17:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: `@bsv/wallet-toolbox` provides BRC-100 wallet signing and storage components, while `@bsv/wallet-toolbox-client` and `@bsv/wallet-toolbox-mobile` provide client-focused distributions for standard and mobile applications using wallet storage services. A vulnerability in these packages causes transactions created through...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/bsv-blockchain/ts-stack/commit/3a11f6111919245a3090e9f3895cfc4f21a80d28
- https://github.com/bsv-blockchain/ts-stack/commit/5492cabbef4ddc7f60cc49cdf5d8c74ed2e5d949
- https://github.com/bsv-blockchain/ts-stack/commit/5ee60395e78e8b822d9a78efeacc6039c249819b
- https://github.com/bsv-blockchain/ts-stack/security/advisories/GHSA-36f9-7rg5-cpf8
- https://github.com/bsv-blockchain/wallet-toolbox/commit/ca651b067c0238cd8b1ddd3af225daa503857a07

### [CVE-2026-91161](https://github.com/rmyndharis/OpenWA/commit/a888a0121543426d4e1bf55f9edaed8306ae2699)

> **Frontend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-91161
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-09-25 02:17:09 JST
- 更新日: 2026-09-25 02:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenWA is a free, open source, self-hosted WhatsApp API gateway. Prior to 0.23.5, the GET /api/sessions/{sessionId}/groups/{groupId}/invite-code endpoint and the GroupGetInviteCode MCP tool have no OPERATOR role requirement, allowing a valid VIEWER key scoped to a session to retrieve an active group invite code. The in...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/rmyndharis/OpenWA/commit/a888a0121543426d4e1bf55f9edaed8306ae2699
- https://github.com/rmyndharis/OpenWA/commit/d66439db9653c7aa7cbfb763003c8d3cbc8f623c
- https://github.com/rmyndharis/OpenWA/pull/1572
- https://github.com/rmyndharis/OpenWA/releases/tag/v0.23.5
- https://github.com/rmyndharis/OpenWA/security/advisories/GHSA-45fh-xj7x-vj2x

### [CVE-2026-63630](https://github.com/alam00000/bentopdf/commit/b21f602cca972320bfffbf72e37df535313a6e48)

> **Frontend** / **LOW** / CVSS: **3.4** / KEV: **no**

- タイトル: CVE-2026-63630
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-09-25 01:17:08 JST
- 更新日: 2026-09-25 01:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: BentoPDF is a client-side PDF toolkit that is self hostable. In 2.8.6 and earlier, deserializeWorkflow() accepts the Timestamp node's tsaUrl control from imported JSON without schema or destination validation. When a user imports the crafted workflow and runs it against a PDF, timestampPdf() sends an RFC 3161 TimeStamp...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/alam00000/bentopdf/commit/b21f602cca972320bfffbf72e37df535313a6e48
- https://github.com/alam00000/bentopdf/releases/tag/v2.8.7
- https://github.com/alam00000/bentopdf/security/advisories/GHSA-cx8x-7rrr-r9x8

### [CVE-2026-56736](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-pgwp-vc7q-cvj3)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-56736
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-25 00:17:24 JST
- 更新日: 2026-09-25 00:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: phpMyFAQ is an open source FAQ web application. A stored cross-site scripting (XSS) vulnerability in versions prior to 4.2.0-alpha allows any unauthenticated user (or low-privileged registered user) to inject arbitrary JavaScript that executes in an administrator's browser when they review or edit a user-submitted FAQ...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-pgwp-vc7q-cvj3
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-pgwp-vc7q-cvj3

### [CVE-2026-91122](https://github.com/discourse/discourse/commit/05d92b8749f68d2626cbe65ec7adde7562a0283d)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-91122
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-25 02:17:08 JST
- 更新日: 2026-09-25 03:19:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Discourse is an open-source discussion platform. Prior to 2026.1.8, 2026.6.3, 2026.7.2, and 2026.8.0, the video placeholder component allowed crafted HTML to cause an attribute breakout and inject an attacker-controlled event handler. An authenticated user with default trust-level posting privileges could store the cra...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/discourse/discourse/commit/05d92b8749f68d2626cbe65ec7adde7562a0283d
- https://github.com/discourse/discourse/commit/5674b3e6594825c28d2678e55057fd6802f11031
- https://github.com/discourse/discourse/commit/c3993e318e172389be5c98455177876f1dd87dda
- https://github.com/discourse/discourse/commit/d7126af3264b672d2201d84c18a37cb8627424a8
- https://github.com/discourse/discourse/pull/42882

### [CVE-2026-63498](https://github.com/grokability/snipe-it/commit/e929b31f0b183c5810bd2b833c1f6f643cbe5284)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-63498
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-25 02:17:05 JST
- 更新日: 2026-09-25 02:17:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Snipe-IT is an IT asset/license management system. Prior to 8.7.0, the uploaded-files API endpoint GET /api/v1/{object_type}/{id}/files/{file_id} allows an authenticated user with file-management access to upload XML and XSLT attachments and request them with the inline=true parameter. The app/Http/Controllers/Api/Uplo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/grokability/snipe-it/commit/e929b31f0b183c5810bd2b833c1f6f643cbe5284
- https://github.com/grokability/snipe-it/releases/tag/v8.7.0
- https://github.com/grokability/snipe-it/security/advisories/GHSA-396x-xmvh-p563

### [CVE-2026-88390](https://github.com/espruino/Espruino/commit/ecd7d43e084ba9aafa8245609347fe0f4383b38c)

> **Frontend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-88390
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-25 02:17:08 JST
- 更新日: 2026-09-25 06:08:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An out-of-bounds write vulnerability in jslGetTokenValueAsString() in Espruino 2v29 (commit bffc6d0) allows crafted JavaScript input containing an overlong token to trigger a one-byte write beyond the JsLex.token buffer in RELEASE/NO_ASSERT builds. The out-of-bounds write corrupts the adjacent tokenValue pointer, resul...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/espruino/Espruino/commit/ecd7d43e084ba9aafa8245609347fe0f4383b38c
- https://github.com/espruino/Espruino/issues/2744
- https://github.com/espruino/Espruino/issues/2744

### [CVE-2026-88362](https://bugs.ghostscript.com/show_bug.cgi?id=709636)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-88362
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-25 01:17:13 JST
- 更新日: 2026-09-25 06:08:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MuJS e892c9fdb contains an incorrect numeric conversion vulnerability in jsR_isindex() in jsrun.c. A specially crafted JavaScript input containing an excessively large numeric array index can cause an out-of-range floating-point value to be converted to an integer without proper range validation. This results in undefi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://bugs.ghostscript.com/show_bug.cgi?id=709636
- https://cgit.ghostscript.com/cgi-bin/cgit.cgi/mujs.git/commit/?id=8a32c397b28fe45747ac4e9e4f3dca049825eda7

# Frontend CVE Summary (2026-09-30)

## Overview

- 取得日時: 2026-09-30 10:15:11 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 0
- High: 7
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-101127](https://www.balbooa.com/)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-101127
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-30 02:17:05 JST
- 更新日: 2026-09-30 06:39:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla Extension - balbooa.com - Unauthenticated upload filename stored XSS in Balbooa Forms < 2.4.3.4 - The public form upload endpoint validates the uploaded file's extension and detected MIME type, but stores the attacker-supplied original multipart filename verbatim in `#__baforms_submissions_attachments.name`. A l...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.balbooa.com/

### [CVE-2026-92231](https://developer.joomla.org/security-centre/1095-20260915-core-xss-filter-bypass-in-inputfilter-via-html5-entity-decode-mismatch.html)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-92231
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-30 02:17:14 JST
- 更新日: 2026-09-30 06:39:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla! Core - [20260915] - Core - XSS filter bypass in InputFilter via HTML5 entity decode mismatch in Joomla 1.5.0-5.4.8, 6.0.0-6.1.3 - The checkAttribute method normalized an attribute value before testing it against the "javascript:" scheme regex, however without decoding HTML5 entities beforehand, causing an XSS v...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://developer.joomla.org/security-centre/1095-20260915-core-xss-filter-bypass-in-inputfilter-via-html5-entity-decode-mismatch.html
- https://www.joomla.org/

### [CVE-2026-102673](https://github.com/electron/electron/commit/7ea14d5f55ecb11a30447701ddca16b3feee0bba)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-102673
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-30 02:17:07 JST
- 更新日: 2026-09-30 02:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 41.10.4, 42.5.2, and 43.0.0, popups opened from a sandboxed iframe through Electron's OpenURLFromTab navigation path, including links using target="_blank" or a middle-click, did not receive the inherited HT...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/7ea14d5f55ecb11a30447701ddca16b3feee0bba
- https://github.com/electron/electron/commit/e26b2640e7795c42bfb111b76009cbb4327c9a69
- https://github.com/electron/electron/commit/ebe1165ee2b05c203c26dd2244ef1c5b9b1c04da
- https://github.com/electron/electron/pull/52133
- https://github.com/electron/electron/releases/tag/v41.10.4

### [CVE-2026-102674](https://github.com/electron/electron/commit/29fc130569f970e91e355383821a4af0f25724a2)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-102674
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-30 02:17:07 JST
- 更新日: 2026-09-30 03:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 41.10.6, 42.9.2, 43.4.1, and 44.0.0-beta.5, windows opened from a sandboxed top-level document did not inherit that document's active HTML sandbox restrictions. Untrusted content in a sandboxed top-level doc...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/29fc130569f970e91e355383821a4af0f25724a2
- https://github.com/electron/electron/commit/3ecf3e74f4be6e2360644679b0b4698742be0e1d
- https://github.com/electron/electron/commit/6594d5a5b074cf501da084dc7908d3df0d68a886
- https://github.com/electron/electron/commit/e9c4d3cbe912e18d7c63af78e63e98ae7a48cd3a
- https://github.com/electron/electron/releases/tag/v41.10.6

### [CVE-2026-102675](https://github.com/electron/electron/commit/4d2784cc8592471ee2276235b8c2a03efddf937d)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-102675
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-30 02:17:07 JST
- 更新日: 2026-09-30 03:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 41.10.6, 42.9.2, 43.4.1, and 44.0.0-beta.5, responses served through protocol.registerFileProtocol or protocol.registerHttpProtocol for a custom scheme registered with supportFetchAPI enabled but corsEnabled...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/4d2784cc8592471ee2276235b8c2a03efddf937d
- https://github.com/electron/electron/commit/80178e4631cb2f6a5e42f8e793b2ae9624e78a0d
- https://github.com/electron/electron/commit/c595b05976e7a885465b043d17e00a92fc3c3397
- https://github.com/electron/electron/commit/ef75c4b98caaa3ebc615f1eba302027028ee04d2
- https://github.com/electron/electron/releases/tag/v41.10.6

### [CVE-2026-102676](https://github.com/electron/electron/commit/6462a2e1dc4e6adffd3b7d9b9be1474c45dcbbe2)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-102676
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-09-30 02:17:07 JST
- 更新日: 2026-09-30 05:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. Prior to 41.10.6, 42.9.2, 43.4.1, and 44.0.0-beta.5, an Electron <webview> guest could enable nodeIntegrationInWorker for its Web Workers even when the unsandboxed embedder had Node.js integration disabled, allowing...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/6462a2e1dc4e6adffd3b7d9b9be1474c45dcbbe2
- https://github.com/electron/electron/commit/9a675aef8822bae4088567822969f900b3a37671
- https://github.com/electron/electron/commit/b3ae0aab5cf81c2ed03d04df1ae8e69ecfab7886
- https://github.com/electron/electron/commit/cd34f335c8664613db5b6e61ae51e2e1846233ae
- https://github.com/electron/electron/releases/tag/v41.10.6

### [CVE-2026-97711](https://github.com/yahoo/serialize-javascript/commit/2bdbaaff9cb8a4639135eb24cfcd383d3fefb534)

> **Frontend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-97711
- 関連キーワード: javascript, gin, express
- 影響製品: -
- 公開日: 2026-09-30 01:17:19 JST
- 更新日: 2026-09-30 02:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Serialize JavaScript serializes JavaScript values to a superset of JSON that includes regular expressions and functions. From 7.1.1 until 7.1.2, function values serialized by serialize-javascript are not fully protected against script-closing tags in attacker-influenced function source because SCRIPT_CLOSE_REGEXP can c...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/yahoo/serialize-javascript/commit/2bdbaaff9cb8a4639135eb24cfcd383d3fefb534
- https://github.com/yahoo/serialize-javascript/releases/tag/v7.1.2
- https://github.com/yahoo/serialize-javascript/security/advisories/GHSA-gfhx-hw2g-v5hg

### [CVE-2026-102677](https://github.com/electron/electron/commit/000453e399bd1dee5e86376cdd9ece5fc071e601)

> **Frontend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-102677
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-30 03:17:09 JST
- 更新日: 2026-09-30 03:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Electron is a framework for writing cross-platform desktop applications using JavaScript, HTML and CSS. From 42.3.3 until 42.10.0, 43.5.0, and 44.0.0-beta.6, Electron's sandboxed preload code cache did not verify that a cached entry matched the preload it was served for. A compromised renderer could write attacker-cont...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/electron/electron/commit/000453e399bd1dee5e86376cdd9ece5fc071e601
- https://github.com/electron/electron/commit/25ba8be57c65a83d8c14ebb8aa37693df17a04f3
- https://github.com/electron/electron/commit/c38d6fd68756f04647ea857bdb6a2abec332e217
- https://github.com/electron/electron/pull/52480
- https://github.com/electron/electron/releases/tag/v42.10.0

### [CVE-2026-102630](https://github.com/unopim/unopim)

> **Frontend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-102630
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-30 01:17:06 JST
- 更新日: 2026-09-30 01:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: UnoPim versions before 2.0.1 and 2.1.1 trust all connecting clients as proxies and honor the X-Forwarded-Host header without validation, allowing unauthenticated attackers to inject arbitrary origins into admin layout pages. Attackers can set X-Forwarded-Host to redirect JavaScript asset loading to their server, and wh...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/unopim/unopim
- https://github.com/unopim/unopim/blob/v2.1.0/bootstrap/app.php#L24
- https://github.com/unopim/unopim/blob/v2.1.0/packages/Webkul/Admin/src/Resources/views/components/layouts/index.blade.php#L9
- https://github.com/unopim/unopim/commit/77e33618df5ba82fc9c9a32d137368e5bbe5ac9c
- https://github.com/unopim/unopim/releases/tag/v2.0.1

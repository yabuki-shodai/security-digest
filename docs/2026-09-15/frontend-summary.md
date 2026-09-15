# Frontend CVE Summary (2026-09-15)

## Overview

- 取得日時: 2026-09-15 09:32:10 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 13
- Critical: 1
- High: 6
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-55451](https://github.com/locize/gettext-converter/commit/df90c3b93e51faef68891d97b626544f619c5b31)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-55451
- 関連キーワード: javascript, next.js
- 影響製品: -
- 公開日: 2026-09-15 02:17:48 JST
- 更新日: 2026-09-15 04:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: gettext-converter provides gettext resource conversion utilities for JavaScript. Prior to 1.3.3, js2i18next() in lib/js2i18next.js splits nested translation keys using options.keyseparator, whose default value consists of two number signs, and uses each segment as a dynamic object key without rejecting __proto__, const...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/locize/gettext-converter/commit/df90c3b93e51faef68891d97b626544f619c5b31
- https://github.com/locize/gettext-converter/issues/15
- https://github.com/locize/gettext-converter/releases/tag/v1.3.3
- https://github.com/locize/gettext-converter/security/advisories/GHSA-f4jp-rw7w-ccwg
- https://github.com/locize/gettext-converter/issues/15

### [CVE-2026-54150](https://github.com/muxinc/next-video/commit/73abf1d534c2ac48db546ecfed0e89cbaf124f6f)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-54150
- 関連キーワード: next.js
- 影響製品: -
- 公開日: 2026-09-15 03:17:52 JST
- 更新日: 2026-09-15 04:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: next-video is a library for adding video to Next.js applications. Prior to 2.8.1, the GET endpoint exported by next-video/request-handler and commonly mounted at /api/video accepts an unauthenticated url query parameter, while src/utils/utils.ts isRemote() treats any value without an HTTP or HTTPS prefix as a local pat...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/muxinc/next-video/commit/73abf1d534c2ac48db546ecfed0e89cbaf124f6f
- https://github.com/muxinc/next-video/releases/tag/v2.8.1
- https://github.com/muxinc/next-video/security/advisories/GHSA-2p39-2jf3-fv2q

### [CVE-2026-54155](https://github.com/node-opcua/node-opcua/commit/c6b05738682f5c8d70b1ea275c881f01a1cd9787)

> **Frontend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-54155
- 関連キーワード: typescript, node.js
- 影響製品: -
- 公開日: 2026-09-15 02:17:46 JST
- 更新日: 2026-09-15 02:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: node-opcua is an OPC UA implementation for TypeScript and Node.js. Prior to 2.166.0, the UserNameIdentityToken authentication handler in packages/node-opcua-server/source/opcua_server.ts decrypts an RSA-OAEP password blob but does not verify that the trailing bytes match the current session serverNonce. An unauthentica...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/node-opcua/node-opcua/commit/c6b05738682f5c8d70b1ea275c881f01a1cd9787
- https://github.com/node-opcua/node-opcua/releases/tag/v2.166.0
- https://github.com/node-opcua/node-opcua/security/advisories/GHSA-mq36-523m-x7vv

### [CVE-2026-54156](https://github.com/node-opcua/node-opcua/commit/b82c2939fe9c658de58da993f2798ec5481d7313)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-54156
- 関連キーワード: typescript, node.js
- 影響製品: -
- 公開日: 2026-09-15 02:17:46 JST
- 更新日: 2026-09-15 02:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: node-opcua is an OPC UA implementation for TypeScript and Node.js. Prior to 2.166.0, the process-global g_alreadyUsedNonce cache used by nonceAlreadyBeenUsed in packages/node-opcua-secure-channel/source/server/server_secure_channel_layer.ts records nonces from OpenSecureChannelRequest and CreateSession without expirati...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/node-opcua/node-opcua/commit/b82c2939fe9c658de58da993f2798ec5481d7313
- https://github.com/node-opcua/node-opcua/releases/tag/v2.166.0
- https://github.com/node-opcua/node-opcua/security/advisories/GHSA-6wvw-vrw4-363w

### [CVE-2026-61534](https://github.com/confetti/yayson/commit/e460162d5a3ebac86424bead7424957c36f8dff9)

> **Frontend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-61534
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-15 01:17:16 JST
- 更新日: 2026-09-15 05:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Yayson is a library for serializing and reading JSON API data in JavaScript. Prior to 4.3.0, Store and LegacyStore use attacker-controlled JSON:API type, id, and relationship names as keys in plain-object lookup tables in src/yayson/store.ts and src/yayson/legacy-store.ts. A document whose type is __proto__ causes mode...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/confetti/yayson/commit/e460162d5a3ebac86424bead7424957c36f8dff9
- https://github.com/confetti/yayson/pull/111
- https://github.com/confetti/yayson/releases/tag/v4.3.0
- https://github.com/confetti/yayson/security/advisories/GHSA-325j-mg25-8q58
- https://github.com/confetti/yayson/security/advisories/GHSA-325j-mg25-8q58

### [CVE-2026-54087](https://github.com/EasyCorp/EasyAdminBundle/commit/8132b2b0ca3876c9261264fa267106a1b2c10a68)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-54087
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-15 03:17:51 JST
- 更新日: 2026-09-15 04:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: EasyAdmin is a fast and modern admin generator for Symfony applications. From 5.0.0 until 5.0.13, FileField and ImageField can accept browser-executable uploads while templates/crud/field/file.html.twig links to stored files for inline same-origin rendering without a download attribute or Content-Disposition attachment...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/EasyCorp/EasyAdminBundle/commit/8132b2b0ca3876c9261264fa267106a1b2c10a68
- https://github.com/EasyCorp/EasyAdminBundle/releases/tag/v5.0.13
- https://github.com/EasyCorp/EasyAdminBundle/security/advisories/GHSA-8559-gwj3-q37r

### [CVE-2026-59960](https://github.com/argos-ci/argos-javascript/commit/8355f3af3be3f4fe361d58a688d21535cf672717)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59960
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-09-15 02:17:49 JST
- 更新日: 2026-09-15 05:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Argos JavaScript provides official Argos SDKs for JavaScript. Prior to Argos core package version 6.2.1, attacker-controlled CI branch or ref values from GITHUB_HEAD_REF or ARGOS_BRANCH can flow through config.branch and getMergeBaseCommitSha() when hasRemoteContentAccess is false. The gitFetch() and gitMergeBase() fun...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/argos-ci/argos-javascript/commit/8355f3af3be3f4fe361d58a688d21535cf672717
- https://github.com/argos-ci/argos-javascript/pull/319
- https://github.com/argos-ci/argos-javascript/releases/tag/@argos-ci/core@6.2.1
- https://github.com/argos-ci/argos-javascript/security/advisories/GHSA-4x45-gxvp-6283

### [CVE-2026-90946](https://github.com/AsyncFuncAI/deepwiki-open)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-90946
- 関連キーワード: javascript, python
- 影響製品: -
- 公開日: 2026-09-15 03:20:29 JST
- 更新日: 2026-09-15 04:18:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DeepWiki-Open through commit d92819a contains an arbitrary file read vulnerability in the unauthenticated /ws/chat WebSocket endpoint that accepts repo_url as a filesystem path with no containment. Attackers can supply arbitrary directory paths to read all files with supported extensions including Python, JavaScript, Y...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/AsyncFuncAI/deepwiki-open
- https://github.com/AsyncFuncAI/deepwiki-open/blob/16f35a0fc0284e99b7963bbf4e8585e9957e2fe1/api/data_pipeline.py
- https://github.com/AsyncFuncAI/deepwiki-open/blob/d92819a9c9f3b99416e3580ff235fc9d3adf8b89/api/repository.py
- https://github.com/AsyncFuncAI/deepwiki-open/issues/536
- https://www.vulncheck.com/advisories/deepwiki-open-through-commit-d92819a-arbitrary-file-read-via-ws-chat-websocket

### [CVE-2026-91021](https://vokecyber.com/research/trilium-share-renderer-stored-xss)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-91021
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-15 03:20:29 JST
- 更新日: 2026-09-15 05:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Trilium Notes, version v0.103.0 and earlier, contains a stored cross-site scripting (XSS) vulnerability in the share renderer for webView notes due to improper HTML escaping of user-controlled #webViewSrc values. This vulnerability allows attackers with note-authoring privileges to inject arbitrary JavaScript that exec...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://vokecyber.com/research/trilium-share-renderer-stored-xss

### [CVE-2026-55847](https://github.com/allure-framework/allure2/commit/1c5693933f519e64379f1a14eb3c7beeba7bc7cd)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-55847
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-15 03:17:55 JST
- 更新日: 2026-09-15 05:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Allure 2 is the version 2.x branch of Allure Report, a multi-language test reporting tool. Prior to 2.39.0, the ansi.js helper at allure-generator/src/main/javascript/helpers/ansi.js passes attacker-influenced statusMessage and statusTrace values through AnsiToHtml without HTML escaping and wraps the result in Handleba...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/allure-framework/allure2/commit/1c5693933f519e64379f1a14eb3c7beeba7bc7cd
- https://github.com/allure-framework/allure2/pull/3296
- https://github.com/allure-framework/allure2/releases/tag/2.39.0
- https://github.com/allure-framework/allure2/security/advisories/GHSA-gx93-m64w-5m6h

### [CVE-2026-82019](https://hussein-mahmoud7.medium.com/cve-2026-82019-how-a-random-ad-led-to-dom-xss-while-testing-chess-com-f043584e1e68)

> **Frontend** / **MEDIUM** / CVSS: **4.2** / KEV: **no**

- タイトル: CVE-2026-82019
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-15 00:17:09 JST
- 更新日: 2026-09-15 01:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TripleLiftの広告レンダリングスクリプト（video-bundle.js）におけるオリジン検証不足によるDOMベースのXSS脆弱性。
- 影響: 未認証の攻撃者により、パブリッシャードメイン上で任意のJavaScriptを実行され、セッションハイジャックやDOM操作が行われる可能性があります。
- 推奨対応: オリジン検証が適切に行われるようスクリプトを修正するか、修正されたバージョンに更新してください。

#### References
- https://hussein-mahmoud7.medium.com/cve-2026-82019-how-a-random-ad-led-to-dom-xss-while-testing-chess-com-f043584e1e68
- https://triplelift.com/creative-technology/
- https://www.vulncheck.com/advisories/triplelift-video-bundle-js-dom-based-xss-via-postmessage

### [CVE-2026-4103](https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-4844/)

> **Frontend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-4103
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-15 01:17:11 JST
- 更新日: 2026-09-15 05:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Publisher PortalおよびDeveloper PortalにおけるHTMLサニタイズ不足によるクロスサイトスクリプティング（XSS）脆弱性。
- 影響: 影響を受けるAPIドキュメント閲覧時にブラウザ上で悪意あるJavaScriptが実行され、ユーザーのセッション権限に応じた不正操作が行われる可能性があります。
- 推奨対応: 入力データのサニタイズ処理を適切に実装し、修正済みバージョンへ更新してください。

#### References
- https://security.docs.wso2.com/en/latest/security-announcements/security-advisories/2026/WSO2-2026-4844/

### [CVE-2026-53496](https://github.com/mattiasw/ExifReader/commit/00878ca9df0e26480dda7a931c888048c9f7be45)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-53496
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-15 02:17:46 JST
- 更新日: 2026-09-15 04:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ExifReaderのISO-BMFFパーサーにおける境界チェック不足に伴う例外（RangeError）未捕捉の脆弱性。
- 影響: 悪意あるHEIC/AVIFデータを解析させることでキャッチされないRangeErrorが発生し、リクエスト処理やワーカーが停止してサービス拒否（DoS）状態に陥る可能性があります。
- 推奨対応: ExifReader を 4.40.1 以降の修正済みバージョンにアップデートしてください。

#### References
- https://github.com/mattiasw/ExifReader/commit/00878ca9df0e26480dda7a931c888048c9f7be45
- https://github.com/mattiasw/ExifReader/releases/tag/v4.40.1
- https://github.com/mattiasw/ExifReader/security/advisories/GHSA-g77h-45rf-hcx4
- https://github.com/mattiasw/ExifReader/security/advisories/GHSA-g77h-45rf-hcx4

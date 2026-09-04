# Backend CVE Summary (2026-09-04)

## Overview

- 取得日時: 2026-09-04 09:00:25 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 20
- Critical: 4
- High: 12
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-85394](https://github.com/advisories/GHSA-6c5p-j8vq-pqhj)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-85394
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-09-04 04:17:31 JST
- 更新日: 2026-09-04 04:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: python-jose through 3.5.0 fails to properly validate asymmetric keys in HMAC initialization, accepting DER-encoded public keys that lack PEM armor or SSH prefixes. Attackers holding the service's public key can forge HS256 tokens that pass verification when algorithms are not explicitly restricted. This is an incomplet...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/advisories/GHSA-6c5p-j8vq-pqhj
- https://github.com/mpdavis/python-jose
- https://github.com/mpdavis/python-jose/blob/018b310ddb8b50dcfd09a0c152117835a21dd656/jose/backends/native.py
- https://github.com/mpdavis/python-jose/blob/018b310ddb8b50dcfd09a0c152117835a21dd656/jose/utils.py
- https://github.com/mpdavis/python-jose/issues/414

### [CVE-2026-85042](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-85042
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 05:17:22 JST
- 更新日: 2026-09-04 05:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Use after free in DevTools in Google Chrome prior to 152.0.7977.82 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- https://issues.chromium.org/issues/553119925

### [CVE-2026-85047](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-85047
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 05:17:24 JST
- 更新日: 2026-09-04 05:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper input validation in Transactions Platform in Google Chrome on on iOS prior to 152.0.7977.82 allowed a remote attacker to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Medium)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- https://issues.chromium.org/issues/513790581

### [CVE-2026-85050](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-85050
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 05:17:26 JST
- 更新日: 2026-09-04 06:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Out of bounds write in WebGL in Google Chrome on on Android prior to 152.0.7977.82 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- https://issues.chromium.org/issues/549350408

### [CVE-2026-55658](https://github.com/1Hive/gardens-v2/security/advisories/GHSA-jwvq-5xmf-f377)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-55658
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-04 01:17:26 JST
- 更新日: 2026-09-04 01:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Gardens v2 is a modular governance framework that enables communities to create and manage multiple governance pools with customizable parameters and voting mechanisms. In 3e595f3 and prior, when a streaming proposal is funded, the cluster of streaming contracts moves real pool funds into the proposal's StreamingEscrow...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/1Hive/gardens-v2/security/advisories/GHSA-jwvq-5xmf-f377

### [CVE-2026-84964](https://jira.mongodb.org/browse/CDRIVER-6409)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-84964
- 関連キーワード: go, mongodb, openssl
- 影響製品: -
- 公開日: 2026-09-04 01:18:25 JST
- 更新日: 2026-09-04 01:25:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A double free in the OpenSSL-based TLS certificate revocation checking path of the MongoDB C Driver can be reached by a TLS endpoint that the client already trusts. During the handshake, specially formed certificate data can cause the same heap object to be released twice. An unauthenticated party acting as the trusted...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/CDRIVER-6409

### [CVE-2026-85053](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-85053
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 05:17:27 JST
- 更新日: 2026-09-04 05:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper resource exposure in CacheStorage in Google Chrome prior to 152.0.7977.82 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- https://issues.chromium.org/issues/552689418

### [CVE-2026-50554](https://github.com/enchant97/note-mark/commit/9c9b72740f22a06131a8f64b53bb08e3b05b81a6)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-50554
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-04 01:17:25 JST
- 更新日: 2026-09-04 01:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Note Mark is an open-source note-taking application. Prior to version 0.19.5, GET /api/books/{bookID}/notes is an unauthenticated endpoint that accepts a "deleted" query parameter. When the request is ?deleted=true, the service runs the query with Unscoped() (bypassing GORM's soft-delete scope) but keeps the read-autho...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/enchant97/note-mark/commit/9c9b72740f22a06131a8f64b53bb08e3b05b81a6
- https://github.com/enchant97/note-mark/releases/tag/v0.19.5
- https://github.com/enchant97/note-mark/security/advisories/GHSA-588f-fvcv-xhvf
- https://github.com/enchant97/note-mark/security/advisories/GHSA-588f-fvcv-xhvf

### [CVE-2026-48486](https://github.com/signum-network/signum-node/releases/tag/v3.9.9)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-48486
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 01:17:24 JST
- 更新日: 2026-09-04 03:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Signum Node 3.9.9 より前のバージョンにおける BlockServiceImpl.applyBlock() の整数オーバーフロー。
- 影響: マイナーが負の合計手数料キャッシュバック値を設定したブロックを作成し、不正に増額された報酬を取得する可能性があります。
- 推奨対応: Signum Node を 3.9.9 以降に更新してください。

#### References
- https://github.com/signum-network/signum-node/releases/tag/v3.9.9
- https://github.com/signum-network/signum-node/security/advisories/GHSA-4vjp-2m22-r2q9

### [CVE-2026-53924](https://github.com/1Hive/gardens-v2/security/advisories/GHSA-jxgc-cgfq-436j)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-53924
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 01:17:25 JST
- 更新日: 2026-09-04 01:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Gardens v2 の StreamingEscrow における異議申し立て状態のチェック不備。
- 影響: 異議申し立て中であっても syncOutflow() 経由でトークンが受取人に移動し、拒否時に回収できなくなる可能性があります。
- 推奨対応: コミット 0xc9d4e0dacd937364793278180551e59d93cd43f9 以降の修正適用版へ更新してください。

#### References
- https://github.com/1Hive/gardens-v2/security/advisories/GHSA-jxgc-cgfq-436j
- https://github.com/1Hive/gardens-v2/security/advisories/GHSA-jxgc-cgfq-436j

### [CVE-2026-57445](https://github.com/1Hive/gardens-v2/security/advisories/GHSA-3xpr-2mm7-77j7)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-57445
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 01:17:26 JST
- 更新日: 2026-09-04 03:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Gardens v2 の StreamingEscrow における承認時の異議解決処理の欠陥。
- 影響: 異議解決処理時に利用可能な全エスクロー残高が提案受取人に不適切に引き出される可能性があります。
- 推奨対応: 現時点で公開された修正パッチはありません。開発元からの更新情報を定期的に確認してください。

#### References
- https://github.com/1Hive/gardens-v2/security/advisories/GHSA-3xpr-2mm7-77j7

### [CVE-2026-85045](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-85045
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 05:17:23 JST
- 更新日: 2026-09-04 06:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Google Chrome 152.0.7977.82 より前のバージョンにおける V8 エンジンの競合状態（Race condition）。
- 影響: リモートの攻撃者が細工されたHTMLページを介して、サンドボックス内で任意のコードを実行する可能性があります。
- 推奨対応: Google Chrome を 152.0.7977.82 以降に更新してください。

#### References
- https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- https://issues.chromium.org/issues/547819997

### [CVE-2026-85046](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-85046
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 05:17:24 JST
- 更新日: 2026-09-04 05:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Type confusion in V8 in Google Chrome prior to 152.0.7977.82 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- https://issues.chromium.org/issues/542403045

### [CVE-2026-85048](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-85048
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 05:17:25 JST
- 更新日: 2026-09-04 05:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Google Chrome 152.0.7977.82 より前のバージョンにおける Compositing の解放後使用（Use After Free）。
- 影響: レンダラープロセスを侵害したリモート攻撃者が、細工されたHTMLページを介してサンドボックス外で任意のコードを実行する可能性があります。
- 推奨対応: Google Chrome を 152.0.7977.82 以降に更新してください。

#### References
- https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- https://issues.chromium.org/issues/540357382

### [CVE-2026-85049](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-85049
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 05:17:25 JST
- 更新日: 2026-09-04 05:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Use after free in Skia in Google Chrome prior to 152.0.7977.82 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- https://issues.chromium.org/issues/553345874

### [CVE-2026-85051](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-85051
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 05:17:26 JST
- 更新日: 2026-09-04 05:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Google Chrome 152.0.7977.82 より前のバージョンにおける Compositing の型の混乱（Type confusion）。
- 影響: リモートの攻撃者が細工されたHTMLページを介して、サンドボックス内で任意のコードを実行する可能性があります。
- 推奨対応: Google Chrome を 152.0.7977.82 以降に更新してください。

#### References
- https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- https://issues.chromium.org/issues/553449113

### [CVE-2026-85393](https://github.com/advisories/GHSA-ppp5-5v6c-4jwp)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-85393
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-04 04:17:31 JST
- 更新日: 2026-09-04 05:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: node-forge 1.4.0 以下における RSA PKCS#1 v1.5 署名検証時の DigestAlgorithm シーケンス検証不備（CVE-2026-33894の不完全な修正）。
- 影響: 低指数RSA鍵を使用している場合、攻撃者によって任意メッセージの有効な署名が偽造される可能性があります。
- 推奨対応: node-forge を修正適用済みバージョンへ更新するか、アップデート情報を確認してください。

#### References
- https://github.com/advisories/GHSA-ppp5-5v6c-4jwp
- https://github.com/digitalbazaar/forge
- https://github.com/digitalbazaar/forge/blob/v1.4.0/lib/asn1.js
- https://github.com/digitalbazaar/forge/blob/v1.4.0/lib/rsa.js
- https://github.com/digitalbazaar/forge/issues/1149

### [CVE-2026-85044](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-85044
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-04 05:17:23 JST
- 更新日: 2026-09-04 05:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Android 版 Google Chrome 152.0.7977.82 より前のバージョンにおける Mobile コンポーネントのリソース解放後使用。
- 影響: ソーシャルエンジニアリングと細工されたHTMLページを組み合わせることで、ウェブオリジンポリシーをバイパスされる可能性があります。
- 推奨対応: Android 版 Google Chrome を 152.0.7977.82 以降に更新してください。

#### References
- https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- https://issues.chromium.org/issues/517482830

### [CVE-2026-84963](https://jira.mongodb.org/browse/CDRIVER-6407)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-84963
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-04 01:18:25 JST
- 更新日: 2026-09-04 01:25:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB C ドライバーの BSON ライブラリにおける JSON パース時の不適切な数値変換。
- 影響: テキストの短縮やフィールド欠損がエラーなしで発生し、アプリケーション保持データが意図せず変更される可能性があります。
- 推奨対応: MongoDB C ドライバーを最新の修正済みバージョンへ更新してください。

#### References
- https://jira.mongodb.org/browse/CDRIVER-6407

### [CVE-2026-84968](https://jira.mongodb.org/browse/PHPC-2744)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-84968
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-04 03:17:33 JST
- 更新日: 2026-09-04 03:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB PHP ドライバーの BSON デコード処理における境界外読み取り（Out-of-bounds read）。
- 影響: 未認証の第三者が送った入力により、隣接するプロセスメモリの一部がエラーメッセージ経由で漏洩する可能性があります。
- 推奨対応: MongoDB PHP ドライバーを最新の修正済みバージョンへ更新してください。

#### References
- https://jira.mongodb.org/browse/PHPC-2744

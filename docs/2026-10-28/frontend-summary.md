# Frontend CVE Summary (2026-10-28)

## Overview

- 取得日時: 2026-10-28 10:14:49 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 6
- Critical: 0
- High: 2
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-118132](https://github.com/ChatGPTNextWeb/NextChat)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-118132
- 関連キーワード: javascript, react, gin
- 影響製品: -
- 公開日: 2026-10-28 03:17:36 JST
- 更新日: 2026-10-28 03:17:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NextChat v2.16.1のPlugin Editorにおけるクライアントサイドのクロスサイトスクリプティング（XSS）脆弱性。
- 影響: 悪意のあるOpenAPIスキーマを読み込ませることで、ユーザーのブラウザ上で任意のJavaScriptを実行され、クッキーやクライアントデータが盗取される可能性があります。
- 推奨対応: 適切な入力検証を行う修正版への更新、または信頼できない外部プラグインスキーマの読み込みを避けることが推奨されます。

#### References
- https://github.com/ChatGPTNextWeb/NextChat

### [CVE-2026-116688](https://github.com/ckeditor/ckeditor5/commit/4d9c5bb34f63cd956d15ccafbe584e14280c86a0)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-116688
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-28 05:17:14 JST
- 更新日: 2026-10-28 05:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CKEditor 5が依存するes-toolkitの不備に起因するプロトタイプ汚染およびXSSの脆弱性。
- 影響: スタイル属性の処理時にプロトタイプ汚染が発生し、エディタコンテンツを介してブラウザ上で不正なJavaScriptが実行される可能性があります。
- 推奨対応: CKEditor 5を修正済みバージョン（47.7.4または48.5.1以降）へアップデートしてください。

#### References
- https://github.com/ckeditor/ckeditor5/commit/4d9c5bb34f63cd956d15ccafbe584e14280c86a0
- https://github.com/ckeditor/ckeditor5/commit/a750e38635db6a18c5b11599c09f4fd702850423
- https://github.com/ckeditor/ckeditor5/releases/tag/v47.7.4
- https://github.com/ckeditor/ckeditor5/releases/tag/v48.5.1
- https://github.com/ckeditor/ckeditor5/security/advisories/GHSA-rh54-vffm-5fvp

### [CVE-2026-112353](https://gfi.ai/resource/kerioconnect-product-releases/)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-112353
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-28 02:16:58 JST
- 更新日: 2026-10-28 02:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GFI KerioConnectのWebmailコンポーネントにおける格納型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 悪意のあるSVG添付ファイルにより任意スクリプトが実行され、認証情報やメール内容が窃取される可能性があります。野外での悪用も報告されています。
- 推奨対応: KerioConnectを10.0.8 Patch 2以降へアップデートしてください。

#### References
- https://gfi.ai/resource/kerioconnect-product-releases/
- https://www.vulncheck.com/advisories/gfi-kerioconnect-8p2-stored-xss-via-svg-attachment

### [CVE-2026-116689](https://github.com/follow-redirects/follow-redirects/commit/b0a7751e9cd64cd8eeb6ec67d2f206a9cc88d3f8)

> **Frontend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-116689
- 関連キーワード: javascript, gin, node.js
- 影響製品: -
- 公開日: 2026-10-28 05:17:14 JST
- 更新日: 2026-10-28 05:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: follow-redirectsにおける機密ヘッダー（sensitiveHeaders）判定処理の不備に関する脆弱性。
- 影響: クロスオリジンのリダイレクト発生時に、本来除外されるべき機密なカスタム認証ヘッダーがリダイレクト先へ送信される可能性があります。
- 推奨対応: follow-redirectsをバージョン1.16.2以降へ更新してください。

#### References
- https://github.com/follow-redirects/follow-redirects/commit/b0a7751e9cd64cd8eeb6ec67d2f206a9cc88d3f8
- https://github.com/follow-redirects/follow-redirects/releases/tag/v1.16.2
- https://github.com/follow-redirects/follow-redirects/security/advisories/GHSA-mrwp-f3q8-3g9p

### [CVE-2026-105987](https://cert.pl/en/posts/2026/10/CVE-2026-105987)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-105987
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-28 00:16:31 JST
- 更新日: 2026-10-28 01:04:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KGS Software tia Viewerの注釈APIにおける格納型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 付箋注釈に注入されたスクリプトにより、ドキュメント閲覧者のブラウザで任意コードが実行され、セッションが侵害される可能性があります。
- 推奨対応: tia Viewerをバージョン1.2.8以降へアップデートしてください。

#### References
- https://cert.pl/en/posts/2026/10/CVE-2026-105987
- https://www.kgs-software.com/en/products/tia-viewer

### [CVE-2026-116687](https://github.com/ckeditor/ckeditor5/commit/4d9c5bb34f63cd956d15ccafbe584e14280c86a0)

> **Frontend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-116687
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-28 05:17:13 JST
- 更新日: 2026-10-28 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CKEditor 5でGeneral HTML Supportが特定の構成で有効な場合に発生するXSSの脆弱性。
- 影響: 操作されたマークアップの処理により、分離されたブラウザコンテキスト内で攻撃者制御のJavaScriptが実行される可能性があります。
- 推奨対応: CKEditor 5を修正済みバージョン（47.7.4または48.5.1以降）へ更新してください。

#### References
- https://github.com/ckeditor/ckeditor5/commit/4d9c5bb34f63cd956d15ccafbe584e14280c86a0
- https://github.com/ckeditor/ckeditor5/commit/a750e38635db6a18c5b11599c09f4fd702850423
- https://github.com/ckeditor/ckeditor5/releases/tag/v47.7.4
- https://github.com/ckeditor/ckeditor5/releases/tag/v48.5.1
- https://github.com/ckeditor/ckeditor5/security/advisories/GHSA-v6mg-96c6-gmpq

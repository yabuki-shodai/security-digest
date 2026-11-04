# Frontend CVE Summary (2026-11-04)

## Overview

- 取得日時: 2026-11-04 11:12:56 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 6
- Critical: 2
- High: 2
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-44266](https://github.com/enspirit/elo/commit/51b869963fbe445c18328714a7ccfbd76b21ba38)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-44266
- 関連キーワード: javascript, python, express
- 影響製品: -
- 公開日: 2026-11-04 03:18:02 JST
- 更新日: 2026-11-04 05:18:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Elo 1.0.1 未満のRubyバックエンドにおいて、文字列リテラル生成時に `#` が適切にエスケープされない脆弱性。
- 影響: Rubyの文字列補間が有効化され、任意のRubyコード実行やシェルコマンド実行につながる可能性がある。
- 推奨対応: Elo 1.0.1 以降へアップデートする。

#### References
- https://github.com/enspirit/elo/commit/51b869963fbe445c18328714a7ccfbd76b21ba38
- https://github.com/enspirit/elo/commit/d2a89a8db76a244eb740687524a7e8529b7554b5
- https://github.com/enspirit/elo/security/advisories/GHSA-7w38-ggh5-v542
- https://github.com/enspirit/elo/security/advisories/GHSA-7w38-ggh5-v542

### [CVE-2026-44267](https://github.com/enspirit/elo/commit/2136da1f64eec8ebf99890d3100be9394534b842)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-44267
- 関連キーワード: javascript, node.js, express
- 影響製品: -
- 公開日: 2026-11-04 03:18:03 JST
- 更新日: 2026-11-04 03:18:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Elo 1.0.1 未満において、プロパティアクセスの制限不備により `.constructor.constructor` を介して JavaScript の Function オブジェクトへアクセス可能なサンドボックス回避の脆弱性。
- 影響: ホスト環境上でのセッション侵害や任意のJavaScript / Node.jsコードの実行につながる可能性がある。
- 推奨対応: Elo 1.0.1 以降へアップデートする。

#### References
- https://github.com/enspirit/elo/commit/2136da1f64eec8ebf99890d3100be9394534b842
- https://github.com/enspirit/elo/commit/d2a89a8db76a244eb740687524a7e8529b7554b5
- https://github.com/enspirit/elo/security/advisories/GHSA-33r5-xmm8-v6x5

### [CVE-2026-44265](https://github.com/enspirit/elo/commit/d2a89a8db76a244eb740687524a7e8529b7554b5)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-44265
- 関連キーワード: javascript, python, gin, express
- 影響製品: -
- 公開日: 2026-11-04 03:18:02 JST
- 更新日: 2026-11-04 03:18:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Elo 1.0.1 未満において、プログラムAST APIが型未指定の入力を実行時検証なしで各言語（JavaScript/Ruby/Python/SQL）に埋め込む脆弱性。
- 影響: JavaScript、Ruby、Pythonでの任意のコード実行、またはSQLインジェクションが実行される可能性がある。
- 推奨対応: Elo 1.0.1 以降へアップデートする。

#### References
- https://github.com/enspirit/elo/commit/d2a89a8db76a244eb740687524a7e8529b7554b5
- https://github.com/enspirit/elo/commit/fb57dd37a2669d9c412454225c5b89a2adba5d93
- https://github.com/enspirit/elo/security/advisories/GHSA-x9rp-7wh3-2rj5

### [CVE-2026-121554](https://github.com/silkimen/cordova-plugin-advanced-http)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-121554
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-11-04 01:17:27 JST
- 更新日: 2026-11-04 01:30:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: cordova-plugin-advanced-http 1.5.0 から 3.3.1 において、Cookieを通常のヘッダーとして渡すため、リダイレクト時にCookieが第三者ホストへ送信される脆弱性。
- 影響: 外部ホストへのCookie漏洩により、ユーザーセッションが乗っ取られる可能性がある。
- 推奨対応: 修正された最新バージョンのプラグインへアップデートする。

#### References
- https://github.com/silkimen/cordova-plugin-advanced-http
- https://github.com/silkimen/cordova-plugin-advanced-http/blob/f6c3ea7f66fbe57770f53546e4af16a74bc2e0cf/src/ios/CordovaHttpPlugin.m#L88-L98
- https://github.com/silkimen/cordova-plugin-advanced-http/blob/f6c3ea7f66fbe57770f53546e4af16a74bc2e0cf/www/helpers.js#L376
- https://github.com/silkimen/cordova-plugin-advanced-http/commit/777a6f10939fd76ddf7f9fe029ae3fcaed850ca1
- https://github.com/silkimen/cordova-plugin-advanced-http/pull/549

### [CVE-2026-121578](https://github.com/Kuri119/Stored-XSS-In-Tactical-RMM-1.5.2/tree/main)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-121578
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-04 01:17:29 JST
- 更新日: 2026-11-04 03:17:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tactical RMM において、入力検証および出力エンコードの不備により悪意のあるスクリプトがデータベースに保存される蓄積型XSSの脆弱性。
- 影響: 対象のオブジェクトを閲覧したユーザーのブラウザ上でスクリプトが実行され、アカウント乗っ取りや任意コード実行につながる可能性がある。
- 推奨対応: Tactical RMM を修正済みバージョンへアップデートする。

#### References
- https://github.com/Kuri119/Stored-XSS-In-Tactical-RMM-1.5.2/tree/main
- https://github.com/amidaware/tacticalrmm-web/commit/ba5363ea99cf776511e5c828b6d744e4d0bddd08
- https://github.com/Kuri119/Stored-XSS-In-Tactical-RMM-1.5.2/tree/main

### [CVE-2026-121447](https://github.com/darylldoyle/svg-sanitizer/security/advisories/GHSA-q546-85r6-f39q)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-121447
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-04 00:17:37 JST
- 更新日: 2026-11-04 00:17:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: svg-sanitizer 1.1.0 未満において、`animateTransform` 属性の `javascript:` URL に対する検証が不十分なサニタイズ迂回の脆弱性。
- 影響: 操作されたSVGファイルを閲覧・クリックしたSafariユーザーのブラウザ上で任意のJavaScriptが実行される可能性がある。
- 推奨対応: svg-sanitizer 1.1.0 以降へアップデートする。

#### References
- https://github.com/darylldoyle/svg-sanitizer/security/advisories/GHSA-q546-85r6-f39q
- https://www.vulncheck.com/advisories/svg-sanitizer-before-1.1.0-xss-via-animatetransform-on-safari

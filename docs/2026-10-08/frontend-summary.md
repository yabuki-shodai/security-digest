# Frontend CVE Summary (2026-10-08)

## Overview

- 取得日時: 2026-10-08 10:51:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 4
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-107353](https://github.com/ljharb/js-traverse/commit/37a9ebd103d2a259c824c29cdcc3f0dfe1acffce)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-107353
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-10-08 05:17:11 JST
- 更新日: 2026-10-08 06:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: npmパッケージ traverse の set() 関数におけるプロトタイプ汚染の脆弱性。
- 影響: 信頼できないパス処理により、String、Number、Boolean 等の組み込みプロトタイプに属性が挿入・上書きされる可能性があります。
- 推奨対応: traverse を修正済みバージョン（0.3.10、0.4.7、0.5.3、0.6.12 以降）へアップデートしてください。

#### References
- https://github.com/ljharb/js-traverse/commit/37a9ebd103d2a259c824c29cdcc3f0dfe1acffce
- https://github.com/ljharb/js-traverse/commit/81ccab43e379cf42eb2a5f689630f7f79b3d71b8
- https://github.com/ljharb/js-traverse/security/advisories/GHSA-rj28-8w7x-jmqc

### [CVE-2026-76276](https://advisory.splunk.com/advisories/SVD-2026-1001)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-76276
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-08 06:17:18 JST
- 更新日: 2026-10-08 06:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Splunk Enterprise の Discover Splunk Observability Cloud アプリにおけるソースマップ埋め込みによる情報漏洩の脆弱性。
- 影響: 低権限ユーザーが Splunk Web 経由でアプリの元ソースコードを取得できる可能性があります。
- 推奨対応: Splunk Enterprise を 10.4.3、10.2.7、10.0.10 以降の修正版に更新してください。

#### References
- https://advisory.splunk.com/advisories/SVD-2026-1001

### [CVE-2025-70519](http://download.fanvil.com/Firmware/Release/PA2S/)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2025-70519
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-08 00:16:53 JST
- 更新日: 2026-10-08 04:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Fanvil x7a ファームウェアのデバイスログコンポーネントにおける反射型データのサニタイズ不足によるHTMLインジェクション/XSSの脆弱性。
- 影響: デバイスログを閲覧したユーザーのブラウザ上で悪意のあるJavaScriptが実行される可能性があります。
- 推奨対応: ベンダーが提供する修正済みファームウェアの適用や入力検証の導入を検討してください。

#### References
- http://download.fanvil.com/Firmware/Release/PA2S/
- https://www.darkpoint.ca/blog/2026/02/27/Fanvil-x7a-PA2S-Vulnerability-Disclosure
- https://www.fanvil.com/products/p5/wulianwangwangguan_1/20210921/5035.html
- https://www.darkpoint.ca/blog/2026/02/27/Fanvil-x7a-PA2S-Vulnerability-Disclosure

### [CVE-2025-70515](http://download.fanvil.com/Firmware/Release/X7A/)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2025-70515
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-08 00:16:51 JST
- 更新日: 2026-10-08 00:57:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Fanvil x7a ファームウェアのデバイスログコンポーネントにおけるHTMLインジェクション/XSSの脆弱性。
- 影響: ログを表示する閲覧者のブラウザ上で任意スクリプトが実行される可能性があります。
- 推奨対応: 修正済みファームウェアへの更新やベンダーのセキュリティ情報を確認してください。

#### References
- http://download.fanvil.com/Firmware/Release/X7A/
- https://www.darkpoint.ca/blog/2026/02/27/Fanvil-x7a-PA2S-Vulnerability-Disclosure
- https://www.fanvil.com/products/p1/x/20210921/5043.html

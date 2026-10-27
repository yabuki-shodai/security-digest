# Frontend CVE Summary (2026-10-27)

## Overview

- 取得日時: 2026-10-27 10:26:12 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 5
- Critical: 0
- High: 2
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-116467](https://github.com/ggml-org/llama.cpp/)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-116467
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-10-27 04:16:30 JST
- 更新日: 2026-10-27 05:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: llama.cpp (0.7.0以下) の Mirostat Sampler 機能 (src/llama-sampler.cpp) におけるアサーション到達に関する脆弱性。
- 影響: リモートの攻撃者によってサービス拒否 (DoS) が引き起こされる可能性がある。
- 推奨対応: 公式での修正対応を監視し、最新の修正版が提供され次第適用するか、該当機能の利用に注意する。

#### References
- https://github.com/ggml-org/llama.cpp/
- https://github.com/ggml-org/llama.cpp/pull/29992
- https://vuldb.com/cve/CVE-2026-116467
- https://vuldb.com/submit/1013917
- https://vuldb.com/vuln/426361

### [CVE-2026-115930](https://www.mongodb.com/docs/mongodb-shell/changelog/)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-115930
- 関連キーワード: npm, go, node.js, mongodb
- 影響製品: -
- 公開日: 2026-10-27 00:16:39 JST
- 更新日: 2026-10-27 01:54:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Shell (mongosh) が依存する Node.js の TLS ルート証明書ストアに、失効・回収可能な eMudhra 中間 CA 証明書が含まれている問題。
- 影響: TLS 通信における信頼性が影響を受ける可能性がある。
- 推奨対応: mongosh 2.14.0 以降にアップデートする。npm 経由で導入している場合はホスト上の Node.js 実行環境を更新する。

#### References
- https://www.mongodb.com/docs/mongodb-shell/changelog/

### [CVE-2026-57187](https://github.com/asterisk/asterisk/commit/0f076168e0be31ebee37762192d0ee049e9c0d42)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-57187
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-10-27 05:17:56 JST
- 更新日: 2026-10-27 05:17:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Asterisk の PJSIP TCP/SDP 処理において、接続型トランスポート経由で SIP INVITE 受信後に切断された際に発生する Heap Use-After-Free の脆弱性。
- 影響: 認証された攻撃者により、アプリケーションがクラッシュ（DoS）させられる可能性がある。
- 推奨対応: Asterisk 20.20.1, 21.12.3, 22.10.1, 23.4.1、または Certified Asterisk 20.7-cert11, 22.8-cert3 以降へアップデートする。

#### References
- https://github.com/asterisk/asterisk/commit/0f076168e0be31ebee37762192d0ee049e9c0d42
- https://github.com/asterisk/asterisk/commit/27b9544b32f059a4f614169243eaa7559f622aa0
- https://github.com/asterisk/asterisk/commit/6e1f4df744369d66ea6f412e355d819b2a7bf26c
- https://github.com/asterisk/asterisk/commit/9e0386c6d259f0c7499d52499d9891bee8a494fa
- https://github.com/asterisk/asterisk/commit/b7ba85458796ef54b471017287c7806095dbda76

### [CVE-2026-33520](https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/october-2026-arcgis-security-bulletin)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-33520
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-27 03:17:46 JST
- 更新日: 2026-10-27 05:17:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Esri Portal for ArcGIS (12.1以前) における反射型クロスサイトスクリプティング (XSS) の脆弱性。
- 影響: 未認証の遠隔攻撃者が作成したリンクを閲覧者が開くことで、ブラウザ上で任意の JavaScript が実行される可能性がある。
- 推奨対応: 提供されているパッチを適用するか、サポート対象のバージョンへアップグレードする。

#### References
- https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/october-2026-arcgis-security-bulletin

### [CVE-2026-50096](https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/october-2026-arcgis-security-bulletin)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-50096
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-27 03:17:48 JST
- 更新日: 2026-10-27 05:17:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Esri Portal for ArcGIS (12.1以前) における反射型クロスサイトスクリプティング (XSS) の脆弱性。
- 影響: 攻撃者が作成したリンクを介して、被害者のブラウザ上で任意の JavaScript が実行される可能性がある。
- 推奨対応: 対象バージョン向けの修正パッチを適用するか、対応するバージョンへアップグレードする。

#### References
- https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/october-2026-arcgis-security-bulletin

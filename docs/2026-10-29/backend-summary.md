# Backend CVE Summary (2026-10-29)

## Overview

- 取得日時: 2026-10-29 10:45:21 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 1
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-118264](https://github.com/labstack/echo/commit/1855061e572ae9dab727c811d8382f266bfbaaec)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-118264
- 関連キーワード: go, echo
- 影響製品: -
- 公開日: 2026-10-29 04:17:31 JST
- 更新日: 2026-10-29 04:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: EchoフレームワークのProxyミドルウェアにおけるWebSocketアップグレード拒否時の接続処理不備の脆弱性。
- 影響: 後続のHTTPリクエストがEchoのルーターを経由せず送信され、認証・認可がバイパスされる可能性があります。
- 推奨対応: Echoをバージョン4.16.1または5.4.1以降にアップデートしてください。

#### References
- https://github.com/labstack/echo/commit/1855061e572ae9dab727c811d8382f266bfbaaec
- https://github.com/labstack/echo/commit/3fb0ba7e17645bb65611e2a08875d0a2f65c421f
- https://github.com/labstack/echo/releases/tag/v4.16.1
- https://github.com/labstack/echo/releases/tag/v5.4.1
- https://github.com/labstack/echo/security/advisories/GHSA-cxf3-9h37-7rr8

### [CVE-2026-118262](https://github.com/labstack/echo/commit/1855061e572ae9dab727c811d8382f266bfbaaec)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-118262
- 関連キーワード: go, echo
- 影響製品: -
- 公開日: 2026-10-29 04:17:30 JST
- 更新日: 2026-10-29 04:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: EchoフレームワークのProxyミドルウェアにおけるWebSocket切断後のリソース解放不備の脆弱性。
- 影響: ゴルーチンやネットワーク接続が残存・蓄積し、サービス拒否（DoS）が発生する可能性があります。
- 推奨対応: Echoをバージョン4.16.1または5.4.1以降にアップデートしてください。

#### References
- https://github.com/labstack/echo/commit/1855061e572ae9dab727c811d8382f266bfbaaec
- https://github.com/labstack/echo/commit/3fb0ba7e17645bb65611e2a08875d0a2f65c421f
- https://github.com/labstack/echo/releases/tag/v4.16.1
- https://github.com/labstack/echo/releases/tag/v5.4.1
- https://github.com/labstack/echo/security/advisories/GHSA-9969-6676-49h5

### [CVE-2026-118650](https://github.com/labstack/echo/commit/b838391e2eade87ae7e5a09d7bb5087bec271ec1)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-118650
- 関連キーワード: go, echo
- 影響製品: -
- 公開日: 2026-10-29 05:17:21 JST
- 更新日: 2026-10-29 05:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: EchoフレームワークのグローバルマウントされたStaticミドルウェアとルーター間でのURLパス解釈差分の脆弱性。
- 影響: エンコードされたパスの解釈差分により、意図しないファイルアクセスやアクセス制限の迂回が発生する可能性があります。
- 推奨対応: Echoをバージョン4.16.0または5.4.0以降にアップデートしてください。

#### References
- https://github.com/labstack/echo/commit/b838391e2eade87ae7e5a09d7bb5087bec271ec1
- https://github.com/labstack/echo/commit/fc410094b2f3415cf2bf5204082137b205bfd5af
- https://github.com/labstack/echo/releases/tag/v4.16.0
- https://github.com/labstack/echo/releases/tag/v5.4.0
- https://github.com/labstack/echo/security/advisories/GHSA-375p-5qhx-8wq4

### [CVE-2026-118263](https://github.com/labstack/echo/commit/1855061e572ae9dab727c811d8382f266bfbaaec)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-118263
- 関連キーワード: go, gin, echo
- 影響製品: -
- 公開日: 2026-10-29 04:17:31 JST
- 更新日: 2026-10-29 04:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Echo v5のBodyDumpミドルウェアがBodyLimit超過エラーを適切にハンドリングしない脆弱性。
- 影響: 制限サイズを超えるHTTP/1.1 チャンク要求ボディが切り詰められて正常処理される可能性があります。
- 推奨対応: Echoをバージョン5.4.1以降にアップデートしてください。

#### References
- https://github.com/labstack/echo/commit/1855061e572ae9dab727c811d8382f266bfbaaec
- https://github.com/labstack/echo/pull/3105
- https://github.com/labstack/echo/releases/tag/v5.4.1
- https://github.com/labstack/echo/security/advisories/GHSA-x9ff-22gv-65f4

### [CVE-2026-118266](https://github.com/labstack/echo/commit/b838391e2eade87ae7e5a09d7bb5087bec271ec1)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-118266
- 関連キーワード: go, gin, echo
- 影響製品: -
- 公開日: 2026-10-29 05:17:21 JST
- 更新日: 2026-10-29 05:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: EchoフレームワークのMethodOverrideミドルウェアにおけるCSRF検証およびSec-Fetch-Siteチェックの迂回脆弱性。
- 影響: 安全なHTTPメソッドへの書き換えによりCSRF保護が回避され、意図しない操作を実行される可能性があります。
- 推奨対応: Echoをバージョン4.16.0または5.4.0以降にアップデートし、ミドルウェアの適用順序を確認してください。

#### References
- https://github.com/labstack/echo/commit/b838391e2eade87ae7e5a09d7bb5087bec271ec1
- https://github.com/labstack/echo/commit/fc410094b2f3415cf2bf5204082137b205bfd5af
- https://github.com/labstack/echo/releases/tag/v4.16.0
- https://github.com/labstack/echo/releases/tag/v5.4.0
- https://github.com/labstack/echo/security/advisories/GHSA-r7w9-592q-9vg4

### [CVE-2026-118619](https://www.zerodayinitiative.com/advisories/ZDI-26-818/)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-118619
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-29 02:18:29 JST
- 更新日: 2026-10-29 02:18:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: UltralyticsにおけるGoogle Driveからのファイルダウンロード処理時のパストラバーサルの脆弱性。
- 影響: 不審なファイルやページを開くことで、現在実行中のプロセス権限で任意コードを実行される可能性があります。
- 推奨対応: Ultralyticsを最新の修正済みバージョンへアップデートし、不審なファイルやURLの処理を避けてください。

#### References
- https://www.zerodayinitiative.com/advisories/ZDI-26-818/

### [CVE-2026-118260](https://github.com/labstack/echo/commit/3fb0ba7e17645bb65611e2a08875d0a2f65c421f)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-118260
- 関連キーワード: go, echo
- 影響製品: -
- 公開日: 2026-10-29 04:17:30 JST
- 更新日: 2026-10-29 04:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Echo v4のBodyDumpミドルウェアがリクエスト/レスポンスボディをキャプチャ制限なしにメモリ保持する脆弱性。
- 影響: 大容量データ通信によりプロセスメモリが枯渇し、サービス拒否（DoS）が引き起こされる可能性があります。
- 推奨対応: Echoをバージョン4.16.1以降にアップデートしてください。

#### References
- https://github.com/labstack/echo/commit/3fb0ba7e17645bb65611e2a08875d0a2f65c421f
- https://github.com/labstack/echo/releases/tag/v4.16.1
- https://github.com/labstack/echo/security/advisories/GHSA-f48p-c9v4-h7xv

### [CVE-2026-118510](https://github.com/mongodb/laravel-mongodb/releases/tag/5.12.0)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-118510
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-29 02:18:26 JST
- 更新日: 2026-10-29 02:18:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB統合ライブラリのリレーションクエリ構築におけるデータ型処理の不備。
- 影響: 関連レコードの非存在確認時に誤った型が用いられ、権限外のドキュメントの閲覧・変更・削除が行われる可能性があります。
- 推奨対応: 該当のMongoDB統合ライブラリを修正適用済みの最新バージョンに更新してください。

#### References
- https://github.com/mongodb/laravel-mongodb/releases/tag/5.12.0
- https://jira.mongodb.org/browse/PHPLARA-148

# Frontend CVE Summary (2026-08-20)

## Overview

- 取得日時: 2026-08-20 07:36:13 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 19
- Critical: 11
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-62681](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-62681
- 関連キーワード: typescript, javascript, react, swr
- 影響製品: -
- 公開日: 2026-08-20 03:16:54 JST
- 更新日: 2026-08-20 03:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Orval 8.21.0 未満において、OpenAPI パスに含まれるエスケープされていないバックティックがコード生成時に安全に処理されず、URL テンプレートリテラルへそのまま出力される脆弱性。
- 影響: 生成されたリクエスト関数や URL ビルダー等の実行時に、攻撃者が注入した JavaScript コードが評価され、開発、CI、テスト、またはアプリケーション環境でコード実行が発生する可能性があります。
- 推奨対応: Orval をバージョン 8.21.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6
- https://github.com/orval-labs/orval/pull/3692
- https://github.com/orval-labs/orval/releases/tag/v8.21.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-fg9p-mrxr-hvq7

### [CVE-2026-71868](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-71868
- 関連キーワード: typescript, javascript, zod, express
- 影響製品: -
- 公開日: 2026-08-20 03:17:24 JST
- 更新日: 2026-08-20 03:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Orval 8.21.0 未満において、enum のデフォルト値に含まれる `${...}` やバックティックが、Zod スキーマ生成時に安全にサニタイズされず出力される脆弱性。
- 影響: 生成された Zod スキーマモジュールのインポート時に任意 JavaScript が実行され、開発、CI、テスト、またはアプリケーション環境でコード実行につながる可能性があります。
- 推奨対応: Orval をバージョン 8.21.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6
- https://github.com/orval-labs/orval/pull/3692
- https://github.com/orval-labs/orval/releases/tag/v8.21.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-3575-w9fc-c2j6

### [CVE-2026-71869](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-71869
- 関連キーワード: typescript, javascript, zod, express
- 影響製品: -
- 公開日: 2026-08-20 03:17:24 JST
- 更新日: 2026-08-20 03:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Orval 8.21.0 未満において、配列アイテムのデフォルト値に含まれる `${...}` やバックティックが、Zod スキーマ生成時に安全にサニタイズされず出力される脆弱性。
- 影響: 生成された Zod スキーマモジュールのインポート時に任意 JavaScript が実行され、開発、CI、テスト、またはアプリケーション環境でコード実行につながる可能性があります。
- 推奨対応: Orval をバージョン 8.21.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6
- https://github.com/orval-labs/orval/pull/3692
- https://github.com/orval-labs/orval/releases/tag/v8.21.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-2h9g-j24r-h63g

### [CVE-2026-71871](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-71871
- 関連キーワード: typescript, javascript, zod, express
- 影響製品: -
- 公開日: 2026-08-20 03:17:24 JST
- 更新日: 2026-08-20 03:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Orval 8.21.0 未満において、ヘッダーパラメータのデフォルト値に含まれる `${...}` やバックティックが、Zod スキーマ生成時に安全にサニタイズされず出力される脆弱性。
- 影響: 生成された Zod スキーマモジュールのインポート時に任意 JavaScript が実行され、開発、CI、テスト、またはアプリケーション環境でコード実行につながる可能性があります。
- 推奨対応: Orval をバージョン 8.21.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6
- https://github.com/orval-labs/orval/pull/3692
- https://github.com/orval-labs/orval/releases/tag/v8.21.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-8j6p-r8jg-mxqh

### [CVE-2026-72716](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-72716
- 関連キーワード: typescript, javascript, zod, express
- 影響製品: -
- 公開日: 2026-08-20 03:17:25 JST
- 更新日: 2026-08-20 03:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Orval 8.21.0 未満において、クエリパラメータのデフォルト値に含まれる `${...}` やバックティックが、Zod スキーマ生成時に安全にサニタイズされず出力される脆弱性。
- 影響: 生成された Zod スキーマモジュールのインポート時に任意 JavaScript が実行され、開発、CI、テスト、またはアプリケーション環境でコード実行につながる可能性があります。
- 推奨対応: Orval をバージョン 8.21.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6
- https://github.com/orval-labs/orval/pull/3692
- https://github.com/orval-labs/orval/releases/tag/v8.21.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-p4cg-3328-rvfg
- https://github.com/orval-labs/orval/security/advisories/GHSA-p4cg-3328-rvfg

### [CVE-2026-72717](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-72717
- 関連キーワード: typescript, javascript, zod, express
- 影響製品: -
- 公開日: 2026-08-20 03:17:25 JST
- 更新日: 2026-08-20 03:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Orval 8.21.0 未満において、スキーマのデフォルト値に含まれる `${...}` やバックティックが、Zod スキーマ生成時に安全にサニタイズされず出力される脆弱性。
- 影響: 生成された Zod スキーマモジュールのインポート時に任意 JavaScript が実行され、開発、CI、テスト、またはアプリケーション環境でコード実行につながる可能性があります。
- 推奨対応: Orval をバージョン 8.21.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6
- https://github.com/orval-labs/orval/pull/3692
- https://github.com/orval-labs/orval/releases/tag/v8.21.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-w727-8j6c-2rj4

### [CVE-2026-71864](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-71864
- 関連キーワード: typescript, javascript, zod
- 影響製品: -
- 公開日: 2026-08-20 03:17:23 JST
- 更新日: 2026-08-20 03:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Orval 8.21.0 未満において、ヘッダーパラメータ名に含まれるダブルクォートが、リクエスト検証用 Zod スキーマの生成時に安全にエンコードされず出力される脆弱性。
- 影響: 生成された Zod スキーマモジュールのインポート時に任意 JavaScript が実行され、開発、CI、テスト、またはアプリケーション環境でコード実行につながる可能性があります。
- 推奨対応: Orval をバージョン 8.21.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6
- https://github.com/orval-labs/orval/pull/3692
- https://github.com/orval-labs/orval/releases/tag/v8.21.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-6437-gxhq-pqv8

### [CVE-2026-71865](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-71865
- 関連キーワード: typescript, javascript, zod
- 影響製品: -
- 公開日: 2026-08-20 03:17:23 JST
- 更新日: 2026-08-20 03:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Orval 8.21.0 未満において、クエリパラメータ名に含まれるダブルクォートが、リクエスト検証用 Zod スキーマの生成時に安全にエンコードされず出力される脆弱性。
- 影響: 生成された Zod スキーマモジュールのインポート時に任意 JavaScript が実行され、開発、CI、テスト、またはアプリケーション環境でコード実行につながる可能性があります。
- 推奨対応: Orval をバージョン 8.21.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6
- https://github.com/orval-labs/orval/pull/3692
- https://github.com/orval-labs/orval/releases/tag/v8.21.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-653q-5476-x79g

### [CVE-2026-71866](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-71866
- 関連キーワード: typescript, javascript, zod
- 影響製品: -
- 公開日: 2026-08-20 03:17:23 JST
- 更新日: 2026-08-20 03:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Orval 8.19.0 から 8.21.0 未満において、スキーマのプロパティ名に含まれるダブルクォートが、Zod スキーマのオブジェクトキー生成時に安全にエンコードされず出力される脆弱性。
- 影響: 生成された Zod スキーマモジュールのインポート時に任意 JavaScript が実行され、開発、CI、テスト、またはアプリケーション環境でコード実行につながる可能性があります。
- 推奨対応: Orval をバージョン 8.21.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6
- https://github.com/orval-labs/orval/pull/3692
- https://github.com/orval-labs/orval/releases/tag/v8.21.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-6mr6-jvcr-2f25
- https://github.com/orval-labs/orval/security/advisories/GHSA-6mr6-jvcr-2f25

### [CVE-2026-62682](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-62682
- 関連キーワード: typescript, javascript
- 影響製品: -
- 公開日: 2026-08-20 03:16:54 JST
- 更新日: 2026-08-20 04:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Orval 8.21.0 未満において、`getBaseUrlFromSpecification` オプションの利用時に `servers[0].url` 内のバックティックが安全にエンコードされず、URL テンプレートリテラルに出力される脆弱性。
- 影響: 生成されたリクエスト関数や URL ビルダーの呼び出し時に任意 JavaScript が実行され、開発、CI、テスト、またはアプリケーション環境でコード実行が発生する可能性があります。
- 推奨対応: Orval をバージョン 8.21.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6
- https://github.com/orval-labs/orval/pull/3692
- https://github.com/orval-labs/orval/releases/tag/v8.21.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-88f2-fpv8-89q2
- https://github.com/orval-labs/orval/security/advisories/GHSA-88f2-fpv8-89q2

### [CVE-2026-71867](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-71867
- 関連キーワード: typescript, javascript
- 影響製品: -
- 公開日: 2026-08-20 03:17:24 JST
- 更新日: 2026-08-20 04:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OrvalにおけるMSWモックファクトリ生成時のプロパティ名エスケープ不備（コードインジェクションの脆弱性）。
- 影響: テストやモック呼び出し時に悪意のあるJavaScriptが実行され、開発・CI・テスト環境等でコード実行が行われる可能性があります。
- 推奨対応: Orval 8.21.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6
- https://github.com/orval-labs/orval/pull/3692
- https://github.com/orval-labs/orval/releases/tag/v8.21.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-2w86-xfrc-g85r
- https://github.com/orval-labs/orval/security/advisories/GHSA-2w86-xfrc-g85r

### [CVE-2026-62680](https://github.com/orval-labs/orval/commit/23786c056f4eba38c02bf2968677988dbbe4de10)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-62680
- 関連キーワード: typescript, javascript
- 影響製品: -
- 公開日: 2026-08-20 03:16:54 JST
- 更新日: 2026-08-20 03:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Orvalにおける外部 $ref（リモートおよびローカルファイル）参照解決時のアクセス制御不足。
- 影響: 開発者やCIホストからの不審なHTTPリクエスト送信（SSRF）、範囲外のローカルファイル読み取り、信頼できないスキーマの取り込みが発生する可能性があります。
- 推奨対応: Orval 8.22.0 以降にアップデートしてください。

#### References
- https://github.com/orval-labs/orval/commit/23786c056f4eba38c02bf2968677988dbbe4de10
- https://github.com/orval-labs/orval/pull/3723
- https://github.com/orval-labs/orval/releases/tag/v8.22.0
- https://github.com/orval-labs/orval/security/advisories/GHSA-cxq5-97v7-87j8
- https://github.com/orval-labs/orval/security/advisories/GHSA-cxq5-97v7-87j8

### [CVE-2026-18430](https://fluidattacks.com/es/advisories/personajes)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-18430
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-20 01:17:06 JST
- 更新日: 2026-08-20 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HumHubにおけるコメント削除通知処理の格納型クロスサイトスクリプティング（XSS）脆弱性。
- 影響: スペース管理者が削除理由に挿入した悪意のあるコードにより、通知を受け取ったユーザーのブラウザ上でJavaScriptが実行される可能性があります。
- 推奨対応: 修正プログラムまたは最新バージョンへのアップデートを検討してください。

#### References
- https://fluidattacks.com/es/advisories/personajes
- https://github.com/humhub/humhub
- https://github.com/humhub/humhub/pull/8365
- https://fluidattacks.com/es/advisories/personajes

### [CVE-2026-63407](https://github.com/getgrav/grav-plugin-api/commit/56ae2ca3bf36c8299a4b3d376c6a20e8c0ed5ba9)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-63407
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-20 01:18:37 JST
- 更新日: 2026-08-20 01:18:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Grav API PluginのCorsMiddlewareにおける過剰に許可されたCORSおよびOPTIONSレスポンスの設定不備。
- 影響: 悪意のあるオリジンからJWTを用いて認証済みAPIへアクセスされ、データの窃取やアカウントの不正操作が行われる可能性があります。
- 推奨対応: Grav API Plugin 1.0.0-rc.16 以降にアップデートしてください。

#### References
- https://github.com/getgrav/grav-plugin-api/commit/56ae2ca3bf36c8299a4b3d376c6a20e8c0ed5ba9
- https://github.com/getgrav/grav-plugin-api/releases/tag/1.0.0-rc.16
- https://github.com/getgrav/grav/security/advisories/GHSA-93px-98wh-6fj2

### [CVE-2026-18756](https://fluidattacks.com/es/advisories/turizo)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-18756
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-20 00:16:58 JST
- 更新日: 2026-08-20 00:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HumHub Community Editionのメンバーシップリクエスト機能における反射型クロスサイトスクリプティング（XSS）脆弱性。
- 影響: 誘導されたユーザーがリクエストフォームを送信した際、ブラウザ上で悪意のあるJavaScriptが実行される可能性があります。
- 推奨対応: 修正プログラムまたは最新バージョンへのアップデートを検討してください。

#### References
- https://fluidattacks.com/es/advisories/turizo
- https://github.com/humhub/humhub
- https://github.com/humhub/humhub/pull/8381

### [CVE-2026-61807](https://github.com/grokability/snipe-it/commit/d12ad3d53869443b96b663ba3ce2673ef343da71)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-61807
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-20 04:17:21 JST
- 更新日: 2026-08-20 04:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Snipe-ITのメーカー/サプライヤー詳細ページにおけるDOMベースの格納型クロスサイトスクリプティング（XSS）脆弱性。
- 影響: 認証済みユーザーが対象ページを閲覧した際、悪意のあるJavaScriptが実行され、セッション情報やデータが露出する可能性があります。
- 推奨対応: Snipe-IT 8.6.2 以降にアップデートしてください。

#### References
- https://github.com/grokability/snipe-it/commit/d12ad3d53869443b96b663ba3ce2673ef343da71
- https://github.com/grokability/snipe-it/releases/tag/v8.6.2
- https://github.com/grokability/snipe-it/security/advisories/GHSA-c8qc-wf67-342w

### [CVE-2026-61607](https://github.com/getgrav/grav-plugin-api/commit/d25eedb84a387f2c71b12a374f2a4b3d74339a7e)

> **Frontend** / **MEDIUM** / CVSS: **4.6** / KEV: **no**

- タイトル: CVE-2026-61607
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-20 01:18:16 JST
- 更新日: 2026-08-20 01:18:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Grav API Pluginのメディアアップロード機能におけるSVGファイルのサニタイズ不足による格納型XSS脆弱性。
- 影響: アップロード権限を持つ攻撃者が悪意のあるSVGを保存し、閲覧した被害者のブラウザでJavaScriptが実行されセッション盗難等が発生する可能性があります。
- 推奨対応: Grav API Plugin 1.0.2 以降にアップデートしてください。

#### References
- https://github.com/getgrav/grav-plugin-api/commit/d25eedb84a387f2c71b12a374f2a4b3d74339a7e
- https://github.com/getgrav/grav-plugin-api/releases/tag/1.0.2
- https://github.com/getgrav/grav/security/advisories/GHSA-7vhm-8x52-2r5p

### [CVE-2026-40507](https://github.com/openemr/openemr/commit/ba316dd1d8de1291102da3f20f64240729ff899e)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-40507
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-20 00:17:01 JST
- 更新日: 2026-08-20 00:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenEMRの患者ポータルテンプレートインポート処理における反射型クロスサイトスクリプティング（XSS）脆弱性。
- 影響: 管理権限を持つユーザーが作成されたURLを開くことで、ブラウザ上で任意のJavaScriptが実行され、セッションハイジャック等の被害に遭う可能性があります。
- 推奨対応: OpenEMR 8.3.0 以降にアップデートしてください。

#### References
- https://github.com/openemr/openemr/commit/ba316dd1d8de1291102da3f20f64240729ff899e
- https://github.com/openemr/openemr/releases/tag/v8_3_0
- https://github.com/openemr/openemr/security/advisories/GHSA-rmmr-8498-463g
- https://www.vulncheck.com/advisories/openemr-reflected-xss-via-templatehtml-parameter-in-patient-portal

### [CVE-2026-40508](https://github.com/openemr/openemr/commit/ba316dd1d8de1291102da3f20f64240729ff899e)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-40508
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-20 00:17:01 JST
- 更新日: 2026-08-20 01:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenEMRの患者ポータルテンプレートインポート処理における格納型クロスサイトスクリプティング（XSS）脆弱性。
- 影響: 権限を持つ攻撃者が悪質なテンプレートをアップロードすることで、エディタで閲覧した他の管理ユーザーのブラウザ上で任意のスクリプトが実行される可能性があります。
- 推奨対応: OpenEMR 8.3.0 以降にアップデートしてください。

#### References
- https://github.com/openemr/openemr/commit/ba316dd1d8de1291102da3f20f64240729ff899e
- https://github.com/openemr/openemr/releases/tag/v8_3_0
- https://github.com/openemr/openemr/security/advisories/GHSA-5293-8q47-cf44
- https://www.vulncheck.com/advisories/openemr-stored-xss-via-patient-portal-template-import-handler
- https://github.com/openemr/openemr/security/advisories/GHSA-5293-8q47-cf44

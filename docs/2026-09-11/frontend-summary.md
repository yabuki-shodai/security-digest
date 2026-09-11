# Frontend CVE Summary (2026-09-11)

## Overview

- 取得日時: 2026-09-11 09:04:03 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 10
- Critical: 0
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-88032](https://jira.mongodb.org/browse/JAVA-6276)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-88032
- 関連キーワード: react, go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 04:17:40 JST
- 更新日: 2026-09-11 04:44:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Java Driverのリアクティブクライアント側暗号化コンポーネントにおけるUse-After-Freeの脆弱性。暗号化操作のキャンセル時に使用中のネイティブリソースが解放される場合がある。
- 影響: 対象の操作をキャンセルさせることで、ホストアプリケーションプロセスが強制終了（クラッシュ）させられる可能性がある。
- 推奨対応: オンデマンドでKMS認証情報を取得する対象構成を確認し、修正パッチや修正版ドライバが提供され次第適用することを推奨。

#### References
- https://jira.mongodb.org/browse/JAVA-6276

### [CVE-2026-88056](https://github.com/angular/angular/commit/3e924cc8dbbb57f23b262cb8f0d7e2bd0673034c)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-88056
- 関連キーワード: typescript, javascript, angular, gin
- 影響製品: -
- 公開日: 2026-09-11 04:17:41 JST
- 更新日: 2026-09-11 04:44:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Angular (@angular/platform-server) のSSRにおけるURL処理の脆弱性。WHATWG URL検証後にresolveUrl/parseUrlがString.prototype.trim()を実行するため、Unicode空白文字により相対パスがプロトコル相対URLへ変換される。
- 影響: SSRF（サーバーサイドリクエストフォージェリ）が発生し、Authorizationヘッダーなどの機密情報が攻撃者制御のオリジンへ漏洩する可能性がある。
- 推奨対応: Angularを 20.3.30、21.2.22、22.1.4 またはそれ以降の修正済みバージョンへアップデートする。

#### References
- https://github.com/angular/angular/commit/3e924cc8dbbb57f23b262cb8f0d7e2bd0673034c
- https://github.com/angular/angular/commit/5aa6d97deb9ef1de14e23748b7fa74f97d183132
- https://github.com/angular/angular/commit/71e52d1396b9cef98652929b73e08c4cde645970
- https://github.com/angular/angular/releases/tag/v20.3.30
- https://github.com/angular/angular/releases/tag/v21.2.22

### [CVE-2026-88058](https://github.com/angular/angular/commit/73d8bbd27cb46495426d4132975a1355b47ad915)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-88058
- 関連キーワード: typescript, javascript, angular, gin
- 影響製品: -
- 公開日: 2026-09-11 04:17:41 JST
- 更新日: 2026-09-11 04:44:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Angular (@angular/platform-server) のSSRにおいて、fallback raw-content要素（noscript, iframe等）内のProcessingInstruction DOMノードをシリアライズする際のエスケープ不備。
- 影響: コンテナ要素が不適切に早期終了し、ブラウザのHTML5 RAWTEXT解析に影響を与えることでXSS等につながる可能性がある。
- 推奨対応: Angularを 20.3.30、21.2.22、22.1.4 またはそれ以降の修正済みバージョンへアップデートする。

#### References
- https://github.com/angular/angular/commit/73d8bbd27cb46495426d4132975a1355b47ad915
- https://github.com/angular/angular/commit/89b20568dfaee1ec8e0b3bcf1872acdddd2f4fef
- https://github.com/angular/angular/commit/ba3bc47b20b3d12f5eb141ec9c651373ae4d15e8
- https://github.com/angular/angular/issues/70146
- https://github.com/angular/angular/releases/tag/v20.3.30

### [CVE-2026-88060](https://github.com/angular/angular/commit/73d8bbd27cb46495426d4132975a1355b47ad915)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-88060
- 関連キーワード: typescript, javascript, angular
- 影響製品: -
- 公開日: 2026-09-11 04:17:42 JST
- 更新日: 2026-09-11 05:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Angular (@angular/platform-server) のSSRにおけるDominoシリアライザの検証不備。fallback raw-content要素内のテンプレートコンテンツで未検証入力が十分にエスケープされない。
- 影響: HTML5 RAWTEXT要素が早期終了し、ブラウザ上で任意のJavaScriptが実行（XSS）される可能性がある。
- 推奨対応: Angularを 20.3.30、21.2.22、22.1.4 またはそれ以降の修正済みバージョンへアップデートする。

#### References
- https://github.com/angular/angular/commit/73d8bbd27cb46495426d4132975a1355b47ad915
- https://github.com/angular/angular/commit/89b20568dfaee1ec8e0b3bcf1872acdddd2f4fef
- https://github.com/angular/angular/commit/ba3bc47b20b3d12f5eb141ec9c651373ae4d15e8
- https://github.com/angular/angular/releases/tag/v20.3.30
- https://github.com/angular/angular/releases/tag/v21.2.22

### [CVE-2026-88059](https://github.com/angular/angular/commit/c45028e44f5f3c1e0006eaccf86642deca51b2af)

> **Frontend** / **MEDIUM** / CVSS: **4.0** / KEV: **no**

- タイトル: CVE-2026-88059
- 関連キーワード: typescript, javascript, angular
- 影響製品: -
- 公開日: 2026-09-11 04:17:41 JST
- 更新日: 2026-09-11 04:44:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Angular (@angular/common) のHttpTransferCacheにおけるキャッシュ不備。SSRおよびハイドレーション環境で階層型HttpClient使用時に、認証付きレスポンスが子TransferCacheに誤って保存される。
- 影響: JSONシリアライズされたng-stateスクリプトを介して、認証トークンやプライベートなレスポンスデータが外部へ漏洩する可能性がある。
- 推奨対応: Angularを 20.3.28、21.2.20、22.1.1 またはそれ以降の修正済みバージョンへアップデートする。

#### References
- https://github.com/angular/angular/commit/c45028e44f5f3c1e0006eaccf86642deca51b2af
- https://github.com/angular/angular/commit/caf616670fd20d528aa69e0131cc17d60f0cc27d
- https://github.com/angular/angular/commit/e4c416c20a1cb222ce73d29c035452b257380c56
- https://github.com/angular/angular/issues/69777
- https://github.com/angular/angular/pull/69778

### [CVE-2026-88057](https://github.com/angular/angular/commit/2f96c8020f85ccb715a76de4b79a0c680c2c7264)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-88057
- 関連キーワード: typescript, javascript, angular
- 影響製品: -
- 公開日: 2026-09-11 04:17:41 JST
- 更新日: 2026-09-11 04:44:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Angular (@angular/core, @angular/compiler) におけるサニタイザー選択の不備。ホストバインディング処理時にターゲット要素ではなく宣言元のコンポーネントからSecurityContextを導出してしまう。
- 影響: built-inサニタイザーによる検証がバイパスされ、攻撃者制御のURL属性等を通じてブラウザ上で任意JavaScriptが実行（XSS）される可能性がある。
- 推奨対応: Angularを 20.3.28、21.2.20、22.1.0 またはそれ以降の修正済みバージョンへアップデートする。

#### References
- https://github.com/angular/angular/commit/2f96c8020f85ccb715a76de4b79a0c680c2c7264
- https://github.com/angular/angular/commit/6afe6fa781c2f0931f0aedd729b9884a8fe212ee
- https://github.com/angular/angular/commit/6caa298dee58319b2d674dc91364e26ffe3ecb2b
- https://github.com/angular/angular/issues/69550
- https://github.com/angular/angular/pull/69558

### [CVE-2026-88061](https://github.com/career-ops-hq/career-ops/commit/b3974e6104d83c2714fd0d071898a7c7b9f68726)

> **Frontend** / **MEDIUM** / CVSS: **5.8** / KEV: **no**

- タイトル: CVE-2026-88061
- 関連キーワード: npm, gin
- 影響製品: -
- 公開日: 2026-09-11 05:17:31 JST
- 更新日: 2026-09-11 05:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: career-ops のローカルWebダッシュボード（web/）における /api ルートのアクセス制限不備。オリジン検証やループバックアドレス制限が行われていない。
- 影響: 同一ブラウザの別タブやローカルネットワークから未認証で任意のコマンドが実行される可能性がある（※npm配布版パッケージは影響外）。
- 推奨対応: career-ops を 0.8.0 以降へアップデートする。

#### References
- https://github.com/career-ops-hq/career-ops/commit/b3974e6104d83c2714fd0d071898a7c7b9f68726
- https://github.com/career-ops-hq/career-ops/releases/tag/web-v0.8.0
- https://github.com/career-ops-hq/career-ops/security/advisories/GHSA-wpqw-whgf-gr4g

### [CVE-2022-26962](https://www.gruppotim.it/it/footer/red-team/2022/CVE-2022-26962-Italtel-NFV.html)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2022-26962
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-11 06:17:06 JST
- 更新日: 2026-09-11 06:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Italtel NFV (11.1.2-20210318) のWeb GUIにおける蓄積型（Stored）XSSの脆弱性。特定の入力パラメータ（name, username, mrfAnnouncementName）に対する検証不足。
- 影響: 認証済みユーザーが該当ページを閲覧した際に、注入された任意のJavaScriptが実行される可能性がある。
- 推奨対応: ベンダー提供のアップデート情報を確認し、修正パッチを適用することを推奨。

#### References
- https://www.gruppotim.it/it/footer/red-team/2022/CVE-2022-26962-Italtel-NFV.html

### [CVE-2026-36392](https://github.com/moksh-nfsu/CVE-2026-36392)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-36392
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-11 07:16:55 JST
- 更新日: 2026-09-11 07:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FairSketch Rise CRM (バージョン 3.9.6) のストア機能におけるクロスサイトスクリプティング（XSS）の脆弱性。アイテムタイトルへの入力検証不足。
- 影響: ストアページを閲覧したユーザーのブラウザ上でJavaScriptが実行され、セッションハイジャックやアカウント乗っ取りが行われる可能性がある。
- 推奨対応: 修正版へのアップデートまたは該当入力値のエスケープ処理を実施することを推奨。

#### References
- https://github.com/moksh-nfsu/CVE-2026-36392

### [CVE-2026-88055](https://github.com/Mintplex-Labs/anything-llm/commit/6dff9d71ab585e87a3145a48abc63c2b60151149)

> **Frontend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-88055
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-11 03:18:14 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AnythingLLM (1.16.1以下) におけるメタデータ生成時のXSS脆弱性。管理設定（meta_page_title, meta_page_favicon）の値がHTMLへ適切にエスケープされず挿入される。
- 影響: 管理者がトップページを閲覧した際にJavaScriptが実行され、管理者用JWTの盗難、APIキー生成、データの改ざん・削除等が行われる可能性がある。
- 推奨対応: AnythingLLMを1.16.1より後の修正済みバージョンへアップデートする。

#### References
- https://github.com/Mintplex-Labs/anything-llm/commit/6dff9d71ab585e87a3145a48abc63c2b60151149
- https://github.com/Mintplex-Labs/anything-llm/security/advisories/GHSA-rh3m-xv7m-9jhf
- https://github.com/Mintplex-Labs/anything-llm/security/advisories/GHSA-rh3m-xv7m-9jhf

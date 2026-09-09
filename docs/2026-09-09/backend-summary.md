# Backend CVE Summary (2026-09-09)

## Overview

- 取得日時: 2026-09-09 09:07:41 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 29
- Critical: 4
- High: 18
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-82067](https://jira.mongodb.org/browse/SERVER-131229)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-82067
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:35 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper handling of case sensitivity in the configuration validation component of MongoDB Server may cause the authorization subsystem to remain in a default disabled state during server startup. An unauthenticated user with network access to a deployment where this condition occurs can perform arbitrary administrativ...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-131229

### [CVE-2026-82058](https://jira.mongodb.org/browse/SERVER-130926)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82058
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:34 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw in MongoDB's JSON Schema validation error generation code allows an authenticated user with readWrite privileges to crash the mongod server. When a BSON document containing an array with a malformed numeric field name fails a $jsonSchema items type constraint, the error generation path performs unsafe numeric co...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-130926

### [CVE-2026-82075](https://jira.mongodb.org/browse/SERVER-132650)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-82075
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:36 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An uncontrolled resource consumption weakness exists in the request-handling path of the MongoDB sharded-cluster router process. A client that has network access to a router port and has not authenticated can supply connection-monitoring parameters that cause the server to expend CPU resources without any rate limiting...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-132650

### [CVE-2026-82076](https://jira.mongodb.org/browse/SERVER-128253)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82076
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:36 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An integer overflow in the query planning component of MongoDB Server can allow an authenticated user with ordinary database-level read/write privileges to bypass an internal resource limit. Submitting a specially crafted query causes the server to consume memory without bound during query planning, and the resulting e...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128253

### [CVE-2026-82052](https://jira.mongodb.org/browse/SERVER-124077)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82052
- 関連キーワード: go, express, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:32 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The $regexFindAll expression can be used by an authenticated user who can run aggregation pipeline stages to crash a MongoDB server (mongod). Under certain specific conditions the regex match can start in the middle of a multi-code-unit character, triggering an assertion during query execution.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-124077

### [CVE-2026-82057](https://jira.mongodb.org/browse/SERVER-130495)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82057
- 関連キーワード: go, gin, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:34 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security issue was discovered in MongoDB where an authenticated user with readWrite privileges could crash the mongod server process. By specifying a custom WiredTiger storage configuration option with an incompatible value during collection creation, a user could cause a type confusion in the storage engine layer. W...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-130495

### [CVE-2026-82062](https://jira.mongodb.org/browse/SERVER-131138)

> **Backend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-82062
- 関連キーワード: go, gin, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:34 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security issue in MongoDB Server allows an authenticated user with elevated internal privileges to bypass a disabled feature gate in the applyOps command by specifying an internal replication mode value that was not intended to be client-selectable. This bypass enables execution of container operations that are disab...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-131138

### [CVE-2026-82065](https://jira.mongodb.org/browse/SERVER-131420)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82065
- 関連キーワード: go, gin, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:35 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security issue in the MongoDB Server's storage engine integration layer allows an authenticated user with collection creation privileges to cause a persistent denial of service. Insufficient validation of user-supplied storage configuration options permits values that, once persisted to durable metadata, trigger a fa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-131420

### [CVE-2026-82071](https://jira.mongodb.org/browse/SERVER-131860)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-82071
- 関連キーワード: go, gin, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:36 JST
- 更新日: 2026-09-09 04:20:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Insufficient validation of storage engine configuration options in MongoDB Server allows an authenticated user with write privileges to supply crafted parameters during collection creation that override internal storage metadata. This results in an out-of-bounds memory write in the server process, causing a denial of s...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-131860

### [CVE-2026-62759](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62759)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-62759
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-09 03:17:58 JST
- 更新日: 2026-09-09 03:38:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Windows Netlogonにおけるスプーフィングによる認証バイパスの脆弱性。
- 影響: 隣接ネットワーク上の未認証の攻撃者がスプーフィング攻撃を実行できる可能性があります。
- 推奨対応: ベンダーが提供する最新のセキュリティパッチの適用およびネットワークの適切な隔離を検討してください。

#### References
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62759

### [CVE-2026-82053](https://jira.mongodb.org/browse/SERVER-130785)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-82053
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:33 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDBのLDAP認可連携における接続プール内の古い認証アイデンティティ保持の問題。
- 影響: 認証済みユーザーが意図しないLDAPアイデンティティで評価され、不当に上位の権限を取得（権限昇格）する可能性があります。
- 推奨対応: 修正済みバージョンへの更新およびLDAP認可設定と接続プール設定の見直しを行ってください。

#### References
- https://jira.mongodb.org/browse/SERVER-130785

### [CVE-2026-82054](https://jira.mongodb.org/browse/SERVER-130901)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82054
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:33 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverの$jsonSchemaフィルター処理におけるJSON Pointerパーサーのメモリ制限欠如。
- 影響: 悪意のあるクエリにより大量のメモリが消費され、mongodプロセスが終了して全体的なサービス拒否（DoS）が発生する可能性があります。
- 推奨対応: 修正済みバージョンへのアップデート、およびリソース制限やクエリの検証を実施してください。

#### References
- https://jira.mongodb.org/browse/SERVER-130901

### [CVE-2026-82055](https://jira.mongodb.org/browse/SERVER-130202)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82055
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:33 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDBの2dsphereインデックスキー生成時におけるヌルポインタ参照の脆弱性。
- 影響: 書き込み権限を持つ認証済みユーザーが特殊なGeoJSONデータを挿入することでmongodプロセスをクラッシュさせ、サービス拒否（DoS）を引き起こす可能性があります。
- 推奨対応: 修正済みバージョンへのアップデートを適用してください。

#### References
- https://jira.mongodb.org/browse/SERVER-130202

### [CVE-2026-82064](https://jira.mongodb.org/browse/SERVER-130759)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-82064
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:35 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverのリードコンサーン処理におけるアサーション判定の不備。
- 影響: 未認証のネットワーク攻撃者が特定のレプリカセットメンバープロセスを強制終了させ、サービス拒否（DoS）を引き起こす可能性があります。
- 推奨対応: 修正済みのMongoDB Serverバージョンへアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-130759

### [CVE-2026-82068](https://jira.mongodb.org/browse/SERVER-131326)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82068
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:35 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverにおける再試行可能な書き込みコマンド処理の不備による永続的クラッシュの問題。
- 影響: 書き込み権限を持つ認証済みユーザーが特殊なコマンドを送信することで永続的なクラッシュ状態を引き起こし、再起動後もサービス拒否（DoS）が継続する可能性があります。
- 推奨対応: 修正済みバージョンへアップデートし、被災した場合は手動での復旧作業を実施してください。

#### References
- https://jira.mongodb.org/browse/SERVER-131326

### [CVE-2026-82070](https://jira.mongodb.org/browse/SERVER-131423)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82070
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:36 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverの診断報告インターフェースにおける資格情報のマスキング不備。
- 影響: 監視権限を持つ認証済みユーザーが他の管理操作の平文資格情報を取得し、管理者等の他ユーザーになりすます可能性があります。
- 推奨対応: 修正済みバージョンへの更新、および診断・監視権限の厳格なアクセス制御を行ってください。

#### References
- https://jira.mongodb.org/browse/SERVER-131423

### [CVE-2026-82073](https://jira.mongodb.org/browse/SERVER-132125)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82073
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:36 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverのアグリゲーションフレームワークにおける内部コマンドパラメータ検証不足（Atlas Search利用時）。
- 影響: 制限された読み取り権限を持つ認証済みユーザーがビューレベルの認可チェックを迂回し、非許可コレクションのデータを閲覧する可能性があります。
- 推奨対応: 修正済みバージョンへアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-132125

### [CVE-2026-82074](https://jira.mongodb.org/browse/SERVER-132275)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82074
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:36 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverのアグリゲーションフレームワークにおける認可評価の不備。
- 影響: 最小限の権限を持つ認証済みユーザーが特殊なリクエストにより認可システムを誤認させ、データベース内のデータを不正に読み取る可能性があります。
- 推奨対応: 修正済みバージョンへアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-132275

### [CVE-2026-82063](https://jira.mongodb.org/browse/SERVER-131870)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-82063
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:35 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverのカーソル管理コンポーネントにおけるUse-After-Freeの脆弱性。
- 影響: 特定のタイミングでカーソル操作を行うことで認証済みユーザーがサーバープロセスをクラッシュさせ、サービス拒否（DoS）を引き起こす可能性があります。
- 推奨対応: 修正済みバージョンへアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-131870

### [CVE-2026-82059](https://jira.mongodb.org/browse/SERVER-130571)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-82059
- 関連キーワード: go, express, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:34 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverにおける内部集計式の不適切なアクセス制限の脆弱性。
- 影響: 読み取り専用権限を持つ認証ユーザーが不正なインデックス仕様を送信することでアサーション失敗を引き起こし、`mongod` プロセスが停止して全クライアントにサービス拒否（DoS）が発生する可能性があります。
- 推奨対応: 影響を受けない修正済みバージョンへMongoDB Serverをアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-130571

### [CVE-2026-82056](https://jira.mongodb.org/browse/SERVER-130306)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-82056
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:33 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverのテキストインデックスクエリ解析における競合状態（Race Condition）の脆弱性。
- 影響: readWrite権限を持つ認証ユーザーが並行して特定の検索・管理操作を行うことでヒープUse-After-Free読み取りが発生し、サーバーがクラッシュしてサービス拒否（DoS）が発生する可能性があります。
- 推奨対応: 影響を受けない修正済みバージョンへMongoDB Serverをアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-130306

### [CVE-2026-82060](https://jira.mongodb.org/browse/SERVER-131202)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-82060
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:34 JST
- 更新日: 2026-09-09 04:19:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDBにおけるシャードキー値の入力検証不足の脆弱性。
- 影響: 認証ユーザーが不正なオブジェクトをシャードキーとして挿入した場合、Change Streams処理時にクエリオペレータとして解釈され、不正確なドキュメントの取得や回復不能なエラーが発生する可能性があります。
- 推奨対応: 影響を受けない修正済みバージョンへMongoDB Serverをアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-131202

### [CVE-2026-82066](https://jira.mongodb.org/browse/SERVER-131562)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-82066
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:35 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverのクエリ計画コンポーネントにおけるヒープ境界外読み取り（Out-of-Bounds Read）の脆弱性。
- 影響: データベースの読み書き権限を持つ認証ユーザーが特殊なクエリを実行することで、メモリ内容が読み取られ、診断統計出力を通じて一部漏洩する可能性があります。
- 推奨対応: 影響を受けない修正済みバージョンへMongoDB Serverをアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-131562

### [CVE-2026-82069](https://jira.mongodb.org/browse/SERVER-132835)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-82069
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-09 02:18:35 JST
- 更新日: 2026-09-09 04:07:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverのルーターにおけるクエリ統計シリアライズ時のデータマスク迂回の脆弱性。
- 影響: モニタリング権限を持つユーザーが、他ユーザーの操作に含まれる未マスクの機密な検索クエリテキストにアクセスできる可能性があります。
- 推奨対応: 影響を受けない修正済みバージョンへMongoDB Serverをアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-132835

### [CVE-2026-79571](https://github.com/fangtang7/CVE/blob/main/springboot-project%20Seller-Side/Authentication%20Bypass.md)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-79571
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-09 00:18:48 JST
- 更新日: 2026-09-09 00:18:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: springboot-project v1.0.0のSellerAuthorizeAspectコンポーネントにおける不適切なアクセス制御の脆弱性。
- 影響: 未認証の攻撃者がすべての出品者管理インターフェースにアクセスし、商品・注文の閲覧や操作、カテゴリ変更などを不正に行う可能性があります。
- 推奨対応: 適切なアクセス制御処理の実装またはパッチ適用を検討してください。

#### References
- https://github.com/fangtang7/CVE/blob/main/springboot-project%20Seller-Side/Authentication%20Bypass.md

### [CVE-2026-86733](https://github.com/grokability/snipe-it/security/advisories/GHSA-x53f-48vj-c5fc)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-86733
- 関連キーワード: gin, mysql
- 影響製品: -
- 公開日: 2026-09-09 01:18:35 JST
- 更新日: 2026-09-09 04:52:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Snipe-IT 8.7.0未満におけるバックアップ復元時のコマンドインジェクションの脆弱性。
- 影響: 認証されたスーパー管理者が不正なZIPバックアップをアップロード・復元することで、Webサーバー実行ユーザーの権限で任意のOSコマンドを実行でき、環境変数やデータの漏洩・改ざんにつながる可能性があります。
- 推奨対応: Snipe-ITをバージョン8.7.0以降にアップデートしてください。

#### References
- https://github.com/grokability/snipe-it/security/advisories/GHSA-x53f-48vj-c5fc
- https://www.vulncheck.com/advisories/snipe-it-before-8.7.0-remote-code-execution-via-backup-restore

### [CVE-2026-82533](https://github.com/deepseek-ai/deepseek-harness/commit/3e24087bfaeabe40b58ba2f7b936895b8f93fe27)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-82533
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-09 02:18:36 JST
- 更新日: 2026-09-09 04:53:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DeepSeek Harness 0.1.2-alpha.1未満のローカルHTTP制御APIにおけるHostヘッダー検証不備による認証バイパスの脆弱性。
- 影響: 攻撃者が偽装したHostヘッダーを送信することで、認証なしでエージェントを完全に制御し、高権限コマンドの実行や対話履歴の参照を行う可能性があります。
- 推奨対応: DeepSeek Harnessをバージョン0.1.2-alpha.1以降にアップデートしてください。

#### References
- https://github.com/deepseek-ai/deepseek-harness/commit/3e24087bfaeabe40b58ba2f7b936895b8f93fe27
- https://github.com/deepseek-ai/deepseek-harness/releases/tag/dsh-v0.1.2-alpha.1
- https://www.vulncheck.com/advisories/deepseek-harness-alpha-1-authentication-bypass-via-host-header-spoofing

### [CVE-2026-86729](https://github.com/WWBN/AVideo/security/advisories/GHSA-vvqm-mgc5-hhx3)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-86729
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-09 01:18:34 JST
- 更新日: 2026-09-09 04:53:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WWBN AVideoにおける `get_api_preauthorize` エンドポイントのレート制限欠落および認証情報の判定漏洩（認証オラクル）の脆弱性。
- 影響: 未認証の第三者が制限なくアカウントに対するブルートフォース攻撃を実施でき、管理者アカウントを含むアカウント乗っ取りが発生する可能性があります。
- 推奨対応: 修正版がリリースされるまで当該エンドポイントへのアクセスを制限するか、Webアプリケーションファイアウォール（WAF）等でレート制限を設定してください。

#### References
- https://github.com/WWBN/AVideo/security/advisories/GHSA-vvqm-mgc5-hhx3
- https://www.vulncheck.com/advisories/wwbn-avideo-unrestricted-authentication-attempts-via-get-api-preauthorize

### [CVE-2026-61516](https://hackwithmike.com/research/advisories/netis/cve-2026-61516)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-61516
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-09 00:18:44 JST
- 更新日: 2026-09-09 04:56:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Netis NX10ファームウェア（V4.0.1.5808およびV3.0.0.4142）のWeb管理インターフェースにおける情報漏洩の脆弱性。
- 影響: 未認証の第三者がセッションなしで `sysinfo` リクエストを送信することで管理者パスワードを取得し、デバイスのフル管理者権限を獲得する可能性があります。
- 推奨対応: 修正済みのファームウェアバージョンに更新するか、管理インターフェースへのアクセスを制限してください。

#### References
- https://hackwithmike.com/research/advisories/netis/cve-2026-61516
- https://hackwithmike.com/research/netis/2026-09
- https://www.netis-systems.com/products/NX10.html
- https://www.vulncheck.com/advisories/netis-nx10-credential-disclosure-via-sysinfo-diagnostic-endpoint

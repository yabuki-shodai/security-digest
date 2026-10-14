# Backend CVE Summary (2026-10-14)

## Overview

- 取得日時: 2026-10-14 10:09:47 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 19
- Critical: 2
- High: 7
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-102988](https://github.com/makeplane/plane/commit/cc3eb974f1142146ddfedf7126cd4dfd376d32d1)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-102988
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-10-14 01:17:10 JST
- 更新日: 2026-10-14 01:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Plane 1.4.0未満における、order_byパラメータに対するアロオリスト検証の欠如に起因するリレーションシップトラバーサルの脆弱性。
- 影響: 未認証の攻撃者がエラーメッセージを介してデータベース構造を把握したり、並び替え結果の差異からデータを推測・漏洩させたりする可能性があります。
- 推奨対応: Plane 1.4.0以降へアップデートしてください。

#### References
- https://github.com/makeplane/plane/commit/cc3eb974f1142146ddfedf7126cd4dfd376d32d1
- https://github.com/makeplane/plane/pull/9292
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-2r95-c453-vxmr

### [CVE-2026-77459](https://github.com/argoproj/argo-cd/commit/1149cdc6e932208c4402183cc3d7b7485239940c)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-77459
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-10-14 02:17:46 JST
- 更新日: 2026-10-14 02:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Argo CDにおける、PostDeleteリソースフック処理時のAppProject認可チェックの不足に関する脆弱性。
- 影響: Gitリポジトリの編集権限を持つユーザーが、本来許可されていない名前空間やクラスターリソースを削除フック経由で不正に作成・操作する可能性があります。
- 推奨対応: Argo CDを修正済みバージョン（3.3.15、3.4.10、3.5.4、3.6.0-rc2以降など）へアップデートしてください。

#### References
- https://github.com/argoproj/argo-cd/commit/1149cdc6e932208c4402183cc3d7b7485239940c
- https://github.com/argoproj/argo-cd/commit/4bc8085b0a6d2296b849539d3d09fc7be7a4a511
- https://github.com/argoproj/argo-cd/commit/7f0a05834b05103d69d7c150e1ee36541b314696
- https://github.com/argoproj/argo-cd/commit/d5dd7019ee65be8895133fe4df554e28074242c4
- https://github.com/argoproj/argo-cd/releases/tag/v3.3.15

### [CVE-2026-104192](https://github.com/dragonflydb/dragonfly/commit/6c6b27a5cfd03d67eb9583ab84a0f0709e3bc77e)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-104192
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-14 00:17:31 JST
- 更新日: 2026-10-14 01:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dragonfly 1.40未満における、RESTOREコマンド処理時の二重解放（Double-Free）の脆弱性。
- 影響: 未認証の攻撃者が細工したストリームデータを送信することでメモリを破壊し、サービス拒否（DoS）や任意のコード実行を引き起こす可能性があります。
- 推奨対応: 認証の有効化、および修正が適用されたコードや最新リリースへのアップデートを実施してください。

#### References
- https://github.com/dragonflydb/dragonfly/commit/6c6b27a5cfd03d67eb9583ab84a0f0709e3bc77e
- https://github.com/dragonflydb/dragonfly/pull/7929
- https://github.com/dragonflydb/dragonfly/security/advisories/GHSA-cg35-6jf4-crfh

### [CVE-2026-104005](https://jira.mongodb.org/browse/SERVER-131411)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-104005
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-14 01:17:11 JST
- 更新日: 2026-10-14 02:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB mongosにおける、集計パイプライン内部ステージの認可チェック不足に関する脆弱性。
- 影響: readWrite権限を持つ認証済みユーザーが特定の集計パイプラインを実行することで、mongosプロセスを不意に停止させ、サービス拒否（DoS）を引き起こす可能性があります。
- 推奨対応: 修正プログラムが提供されているMongoDB Serverのバージョンへアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-131411

### [CVE-2026-96299](https://jira.mongodb.org/browse/SERVER-130431)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-96299
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-14 01:17:24 JST
- 更新日: 2026-10-14 02:17:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB mongosにおける、集計パイプライン内部ステージの認可チェック不足に関する脆弱性。
- 影響: readWrite権限を持つ認証済みユーザーが特定の集計パイプラインを実行することで、mongosプロセスを不意に停止させ、サービス拒否（DoS）を引き起こす可能性があります。
- 推奨対応: 修正プログラムが提供されているMongoDB Serverのバージョンへアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-130431

### [CVE-2026-104004](https://jira.mongodb.org/browse/SERVER-131412)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-104004
- 関連キーワード: go, express, mongodb
- 影響製品: -
- 公開日: 2026-10-14 01:17:10 JST
- 更新日: 2026-10-14 01:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Serverのコレクション検証（validation）機能における特定の検証式の不適切な処理に関する脆弱性。
- 影響: 書き込み権限を持つ認証済みユーザーがドキュメントを挿入した際に、サーバープロセスが異常終了（DoS）する可能性があります。
- 推奨対応: 修正プログラムが提供されているMongoDB Serverのバージョンへアップデートしてください。

#### References
- https://jira.mongodb.org/browse/SERVER-131412

### [CVE-2026-82416](https://github.com/php/frankenphp/commit/be24d82531675f90862b8cde1e9fc7e9ee855aa5)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-82416
- 関連キーワード: go, docker
- 影響製品: -
- 公開日: 2026-10-14 02:17:47 JST
- 更新日: 2026-10-14 06:18:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FrankenPHP 1.12.5未満のワーカーモードにおける、特定の動的モジュール構成時にセッション状態がリクエスト間で残留する脆弱性。
- 影響: 並行リクエスト発生時に他ユーザーのセッションIDが再利用され、セッションハイジャックや情報漏洩が発生する可能性があります。
- 推奨対応: FrankenPHP 1.12.5以降へアップデートするか、セッション拡張機能を静的リンクしたビルドを使用してください。

#### References
- https://github.com/php/frankenphp/commit/be24d82531675f90862b8cde1e9fc7e9ee855aa5
- https://github.com/php/frankenphp/pull/2523
- https://github.com/php/frankenphp/releases/tag/caddy/v1.12.5
- https://github.com/php/frankenphp/security/advisories/GHSA-v3ph-cgqh-r8p5

### [CVE-2026-109523](https://github.com/girishsaraf/Online-Appointment-Booking-System/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-109523
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-14 00:17:34 JST
- 更新日: 2026-10-14 04:26:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Online-Appointment-Booking-Systemの Admin/getclinic.php におけるSQLインジェクションの脆弱性。
- 影響: リモートの攻撃者がcity/cidパラメータを操作することで、データベースの不正操作や情報漏洩を引き起こす可能性があります。
- 推奨対応: 公式な修正が提供されるまで対象エンドポイントへのアクセスを制限するか、入力値のパラメータ化（プレースホルダ利用）への修正を行ってください。

#### References
- https://github.com/girishsaraf/Online-Appointment-Booking-System/
- https://github.com/girishsaraf/Online-Appointment-Booking-System/issues/13
- https://vuldb.com/cve/CVE-2026-109523
- https://vuldb.com/submit/984341
- https://vuldb.com/vuln/417187

### [CVE-2026-110121](https://github.com/lilishop/lilishop/blob/v4.4/framework/src/main/java/cn/lili/modules/goods/serviceimpl/GoodsServiceImpl.java#L198-L222)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-110121
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-14 02:17:36 JST
- 更新日: 2026-10-14 03:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PickMall lilishop 4.4以前の店舗向け商品更新エンドポイントにおける不適切な直接オブジェクト参照（IDOR）の脆弱性。
- 影響: 認証された販売者が他店舗のgoodsIdを指定することで、他店舗の商品情報やSKUを不正に上書き・所有権変更する可能性があります。
- 推奨対応: 商品更新リクエスト処理時に適切な所有権の検証ロジックを追加するか、修正版へアップデートしてください。

#### References
- https://github.com/lilishop/lilishop/blob/v4.4/framework/src/main/java/cn/lili/modules/goods/serviceimpl/GoodsServiceImpl.java#L198-L222
- https://github.com/lilishop/lilishop/blob/v4.4/seller-api/src/main/java/cn/lili/controller/goods/GoodsStoreController.java#L143-L147
- https://hackmd.io/@1ExmmukzRMWN7B4gQ4W-4Q/lilishop-seller-goods-cross-store-authz-bypass
- https://www.vulncheck.com/advisories/pickmall-lilishop-through-4.4-idor-via-goods-edit-endpoint

### [CVE-2026-103028](https://github.com/drakkan/sftpgo/commit/dc8886bc079094b4ac2338df683f358b7676b5eb)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-103028
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-14 00:17:30 JST
- 更新日: 2026-10-14 00:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SFTPGo is an open source, event-driven file transfer solution. From 2.5.0 until 2.7.6, an authenticated user with copy permission can copy a source file denied by denied_patterns or outside allowed_patterns to an allowed destination name because file-pattern filters are evaluated only on the destination. The user can t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/drakkan/sftpgo/commit/dc8886bc079094b4ac2338df683f358b7676b5eb
- https://github.com/drakkan/sftpgo/releases/tag/v2.7.6
- https://github.com/drakkan/sftpgo/security/advisories/GHSA-wwv9-g5x4-966q

### [CVE-2026-110114](https://github.com/FJ-OMS/oms-erp/blob/14486c98280afd2e0372866f8f2345e2e2b32843/skyer-goods/src/main/java/org/skyer/goods/api/controller/v1/GoodsSkuController.java#L123-L131)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-110114
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-14 02:17:35 JST
- 更新日: 2026-10-14 02:17:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FJ-OMS oms-erp through PRE contains a missing authentication vulnerability that allows unauthenticated attackers to delete and rebuild product search indexes by calling public es-test maintenance endpoints in skyer-goods. Attackers can repeatedly request /v1/goods/sku/es-test to empty the shared goods_sku_index_01 inde...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FJ-OMS/oms-erp/blob/14486c98280afd2e0372866f8f2345e2e2b32843/skyer-goods/src/main/java/org/skyer/goods/api/controller/v1/GoodsSkuController.java#L123-L131
- https://github.com/FJ-OMS/oms-erp/blob/14486c98280afd2e0372866f8f2345e2e2b32843/skyer-goods/src/main/java/org/skyer/goods/api/controller/v1/SpuController.java#L104-L111
- https://github.com/FJ-OMS/oms-erp/blob/14486c98280afd2e0372866f8f2345e2e2b32843/skyer-goods/src/main/java/org/skyer/goods/app/service/impl/SkuEsServiceImpl.java#L276-L301
- https://hackmd.io/@1ExmmukzRMWN7B4gQ4W-4Q/oms-erp-es-test-unauth-index-wipe
- https://www.vulncheck.com/advisories/oms-erp-through-pre-missing-authentication-via-skyer-goods-es-test-endpoints

### [CVE-2026-77375](https://github.com/drakkan/sftpgo/commit/4f751232d7025cf2f7360e01ee8dca81e74b48b0)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-77375
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-14 00:17:49 JST
- 更新日: 2026-10-14 01:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SFTPGo is an open source, event-driven file transfer solution. Prior to 2.7.5, an authenticated SSH user can send a malformed protocol message while opening a channel, causing an unhandled error that terminates the server process and affects all connected users until restart. No confidentiality or integrity impact has...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/drakkan/sftpgo/commit/4f751232d7025cf2f7360e01ee8dca81e74b48b0
- https://github.com/drakkan/sftpgo/releases/tag/v2.7.5
- https://github.com/drakkan/sftpgo/security/advisories/GHSA-q7pc-356p-hggc

### [CVE-2026-103965](https://jira.mongodb.org/browse/SERVER-134618)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-103965
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-14 01:17:10 JST
- 更新日: 2026-10-14 02:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An issue in MongoDB Server's aggregation framework can cause certain constant values to be handled incorrectly during internal query rewriting. Under certain conditions, an authenticated user with read access may receive field values in aggregation output that the query did not intend to return.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-134618

### [CVE-2026-110103](https://github.com/mlogclub/bbs-go/blob/v4.4.6/internal/handlers/api/upload_handlers.go#L36-L54)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-110103
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-14 02:17:34 JST
- 更新日: 2026-10-14 02:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: bbs-go through 4.4.6 contains a stored cross-site scripting vulnerability that allows authenticated users to upload HTML or SVG files by spoofing the multipart Content-Type in POST /api/upload. Attackers can upload script-bearing documents served inline from /res and send their URLs to administrators, executing script...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mlogclub/bbs-go/blob/v4.4.6/internal/handlers/api/upload_handlers.go#L36-L54
- https://github.com/mlogclub/bbs-go/blob/v4.4.6/internal/pkg/uploader/uploader.go#L90-L121
- https://github.com/mlogclub/bbs-go/commit/5bebf98bb9e0ac5162d4f8faf7a65fc0d496a362
- https://github.com/mlogclub/bbs-go/issues/305
- https://github.com/mlogclub/bbs-go/pull/306

### [CVE-2026-96297](https://jira.mongodb.org/browse/SERVER-132946)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-96297
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-14 01:17:24 JST
- 更新日: 2026-10-14 02:17:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Use of freed memory in the aggregation feature of MongoDB Server can cause the server to read data from a memory area after it has been released. When an internal aggregation stage is combined with a batch size of 0, the server may read from memory that is no longer in use. Because that memory can be reused for other d...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-132946

### [CVE-2026-102603](https://github.com/gotify/server/commit/a8744482c668e07a61798573ec8e17bd3f6009f9)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-102603
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-14 00:17:30 JST
- 更新日: 2026-10-14 00:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Gotify server is a simple server for sending and receiving messages in real-time per WebSocket. Prior to 3.0.0, the password change endpoint (POST /current/user/password) accepts a valid client token without requiring the account's current password or another elevated authentication step. An attacker who obtains a clie...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gotify/server/commit/a8744482c668e07a61798573ec8e17bd3f6009f9
- https://github.com/gotify/server/pull/952
- https://github.com/gotify/server/releases/tag/v3.0.0
- https://github.com/gotify/server/security/advisories/GHSA-3hcj-9m7p-wwm9

### [CVE-2026-110122](https://github.com/lilishop/lilishop/blob/v4.4/framework/src/main/java/cn/lili/modules/goods/serviceimpl/GoodsServiceImpl.java#L424-L442)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-110122
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-14 02:17:36 JST
- 更新日: 2026-10-14 02:17:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PickMall lilishop through 4.4 contains an insecure direct object reference vulnerability that allows authenticated sellers to change other stores' product freight templates via PUT /store/goods/goods/freight. GoodsServiceImpl.freight and GoodsSkuServiceImpl.freight update goods and SKUs by id without store-scoped check...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/lilishop/lilishop/blob/v4.4/framework/src/main/java/cn/lili/modules/goods/serviceimpl/GoodsServiceImpl.java#L424-L442
- https://github.com/lilishop/lilishop/blob/v4.4/seller-api/src/main/java/cn/lili/controller/goods/GoodsStoreController.java#L177-L185
- https://hackmd.io/@1ExmmukzRMWN7B4gQ4W-4Q/lilishop-seller-goods-cross-store-authz-bypass
- https://www.vulncheck.com/advisories/pickmall-lilishop-through-4.4-idor-via-goods-freight-endpoint

### [CVE-2026-19940](https://github.com/zephyrproject-rtos/zephyr/commit/204c36b896fe8d68ca3cb3d00216f245f91d14be)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-19940
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-14 02:17:40 JST
- 更新日: 2026-10-14 05:20:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The Bluetooth Classic Hands-Free Profile Audio Gateway implementation in subsys/bluetooth/host/classic/hfp_ag.c keeps its struct bt_hfp_ag objects in a static pool indexed by ACL connection index. On link teardown, hfp_ag_disconnected() cancels ag->tx_work and the per-call work items and then clears ag->acl_conn, which...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/204c36b896fe8d68ca3cb3d00216f245f91d14be
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-v47w-8959-rx62

### [CVE-2026-108375](https://github.com/marcosschroh/dataclasses-avroschema/commit/01e6d5e15ab0ff69faac39a340d21b85da1e852f)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-108375
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-14 03:17:16 JST
- 更新日: 2026-10-14 03:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: dataclasses-avroschema generates Avro schemas from Python dataclasses, Pydantic models, and Faust Records and generates Python code from Avro schemas. From version 0.38.0 through 0.70.5, FieldRepresentation.get_field_default inserts schema-controlled string, UUID, bytes, and fixed field defaults into quoted literals in...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/marcosschroh/dataclasses-avroschema/commit/01e6d5e15ab0ff69faac39a340d21b85da1e852f
- https://github.com/marcosschroh/dataclasses-avroschema/releases/tag/0.70.6
- https://github.com/marcosschroh/dataclasses-avroschema/security/advisories/GHSA-9h8h-264x-jcg2
- https://github.com/marcosschroh/dataclasses-avroschema/security/advisories/GHSA-9h8h-264x-jcg2

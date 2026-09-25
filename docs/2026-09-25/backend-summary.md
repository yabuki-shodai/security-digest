# Backend CVE Summary (2026-09-25)

## Overview

- 取得日時: 2026-09-25 09:30:23 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 22
- Critical: 2
- High: 7
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-96744](https://github.com/mongodb/laravel-mongodb/pull/3579)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-96744
- 関連キーワード: go, express, mongodb
- 影響製品: -
- 公開日: 2026-09-25 01:17:27 JST
- 更新日: 2026-09-25 06:00:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper neutralization of special elements in data query logic in the cache lock implementation of the MongoDB integration for Laravel can cause a caller-supplied lock owner value to be evaluated as an aggregation expression rather than as a literal value. An authenticated user who can influence the owner value an app...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mongodb/laravel-mongodb/pull/3579
- https://github.com/mongodb/laravel-mongodb/releases/tag/5.11.0

### [CVE-2026-96746](https://github.com/mongodb/mongo-c-driver/releases/tag/1.30.12)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-96746
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-25 01:17:27 JST
- 更新日: 2026-09-25 06:04:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An out-of-bounds write in the connection-monitoring logic of the MongoDB C Driver may allow an unauthenticated party who controls name resolution and the responses of the hosts named in a client's connection string to write beyond the end of a heap buffer. This may cause the application using the driver to terminate un...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mongodb/mongo-c-driver/releases/tag/1.30.12
- https://github.com/mongodb/mongo-c-driver/releases/tag/2.5.5
- https://github.com/mongodb/mongo-c-driver/security/advisories/GHSA-frjf-h5jg-4v46

### [CVE-2026-96750](https://github.com/mongodb-js/compass/releases/tag/v1.49.12)

> **Backend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-96750
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-25 01:17:27 JST
- 更新日: 2026-09-25 06:00:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Compassにおいて、データベース名が適切にエスケープされずに埋め込みMongoDBシェルへ挿入される脆弱性。
- 影響: 特定条件化でCompassの権限で任意のシェル命令が実行される可能性があります。
- 推奨対応: MongoDB Compassを修正済みバージョンに更新し、信頼できないデータベースのシェルを開かないようにしてください。

#### References
- https://github.com/mongodb-js/compass/releases/tag/v1.49.12

### [CVE-2026-96745](https://github.com/mongodb/mongo-php-driver/pull/2115)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-96745
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-25 01:17:27 JST
- 更新日: 2026-09-25 06:04:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB PHP Driverのコマンドモニタリング機能における不適切なデータのデシリアライゼーションの脆弱性。
- 影響: 信頼できないデータにより特定クラスのインスタンス化やデシリアライズ処理が呼び出され、任意コード実行などの影響を受ける可能性があります。
- 推奨対応: MongoDB PHP Driverを最新バージョンへ更新し、データベース操作に含まれる外部入力を検証してください。

#### References
- https://github.com/mongodb/mongo-php-driver/pull/2115
- https://github.com/mongodb/mongo-php-driver/releases/tag/1.21.10
- https://github.com/mongodb/mongo-php-driver/releases/tag/2.1.10
- https://github.com/mongodb/mongo-php-driver/releases/tag/2.5.3
- https://github.com/mongodb/mongo-php-driver/security/advisories/GHSA-cmvj-vxvq-rh2c

### [CVE-2026-93221](https://git.kernel.org/stable/c/11a5fe42e1811f793e04ef885b639ea7668f439d)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-93221
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-25 01:17:17 JST
- 更新日: 2026-09-25 01:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのnfsdモジュールにおいて、フラグへのアクセスが非同期に行われることによる競合状態の脆弱性。
- 影響: 並行アクセスにより意図しない処理が同時に実行され、不整合や動作不良を引き起こす可能性があります。
- 推奨対応: 修正パッチが適用されたLinuxカーネルに更新してください。

#### References
- https://git.kernel.org/stable/c/11a5fe42e1811f793e04ef885b639ea7668f439d
- https://git.kernel.org/stable/c/df5922fe09a8131c793ffa86adf204999b0470f8

### [CVE-2026-93208](https://git.kernel.org/stable/c/30e8cb8598aa41b1b9f8803081d2ae5e5369c0f3)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-93208
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-25 01:17:15 JST
- 更新日: 2026-09-25 01:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのKASANにおいて、キャッシュ縮小処理とCPUホットプラグ処理が競合する脆弱性。
- 影響: オブジェクトがスラブアロケータに返却されず、メモリリークやカーネルの不安定化を招く可能性があります。
- 推奨対応: 修正パッチが適用されたLinuxカーネルに更新してください。

#### References
- https://git.kernel.org/stable/c/30e8cb8598aa41b1b9f8803081d2ae5e5369c0f3
- https://git.kernel.org/stable/c/3119d58e4ef8719d669911d38a53fc00086ac48b
- https://git.kernel.org/stable/c/709c3646545e0a1f99a5816384c633f6552c5a98
- https://git.kernel.org/stable/c/7cd164f0e1bab0f8dd125c92ed4f19bbd6b92a4a
- https://git.kernel.org/stable/c/8790303cbaac52a11dfed4aab261f8ea60682525

### [CVE-2026-93255](https://git.kernel.org/stable/c/2073f3d97b0c5d34fe64812d1237e37bd79c17ec)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-93255
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-25 01:17:22 JST
- 更新日: 2026-09-25 01:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのbtrfsファイルシステムにおけるフラグクリア処理の不備に関する脆弱性。
- 影響: 警告（WARNING）の発生や不適切な状態遷移により、システムの不整合が発生する可能性があります。
- 推奨対応: 修正パッチが適用されたLinuxカーネルに更新してください。

#### References
- https://git.kernel.org/stable/c/2073f3d97b0c5d34fe64812d1237e37bd79c17ec
- https://git.kernel.org/stable/c/690c2accacb1aca91ab8186d15dee56da8723f31

### [CVE-2026-93224](https://git.kernel.org/stable/c/0335800071a6dfdf7d21d729b5e7d8fa98936211)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-93224
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-25 01:17:17 JST
- 更新日: 2026-09-25 01:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのsvcrdmaにおいて、接続受付失敗時のリソース解放処理に不備がある脆弱性。
- 影響: 接続失敗が繰り返された際にメモリやトラッカーがリークし、リソース枯渇を引き起こす可能性があります。
- 推奨対応: 修正パッチが適用されたLinuxカーネルに更新してください。

#### References
- https://git.kernel.org/stable/c/0335800071a6dfdf7d21d729b5e7d8fa98936211
- https://git.kernel.org/stable/c/26190394c64c9429481fc88a4738f70bb92fb352
- https://git.kernel.org/stable/c/45a444a17240f4fa2235f0dfd4a96fc80f1eb2c2
- https://git.kernel.org/stable/c/5aabe070c00e5bdf4ab150fb5f72ad5f266d6241

### [CVE-2026-90959](https://access.redhat.com/security/cve/CVE-2026-90959)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-90959
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-09-25 00:17:53 JST
- 更新日: 2026-09-25 06:00:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pulpcoreのコンテンツアップロードAPIにおけるURL検証不備に起因するパストラバーサルの脆弱性。
- 影響: 認証されたユーザーによりサーバー上の任意ファイルが読み取られ、コンテナレジストリの秘密鍵漏洩やトークン偽造につながる可能性があります。
- 推奨対応: pulpcoreを修正済みバージョンに更新してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-90959
- https://bugzilla.redhat.com/show_bug.cgi?id=2533037

### [CVE-2026-93425](https://github.com/Dokploy/dokploy/commit/16b5b7293f9883327a89c69fcb6e5718767b064a)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-93425
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-09-25 01:17:25 JST
- 更新日: 2026-09-25 03:19:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DokployのtRPCプロシージャにおける引数のエスケープ不足によるOSコマンドインジェクションの脆弱性。
- 影響: 認証されたメンバーによりコンテナ内でroot権限の任意コマンドを実行され、Dockerソケット経由でホスト全体が侵害される可能性があります。
- 推奨対応: Dokployをバージョン0.29.13以降に更新してください。

#### References
- https://github.com/Dokploy/dokploy/commit/16b5b7293f9883327a89c69fcb6e5718767b064a
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.13
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-56g6-wjr4-5q7p
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-56g6-wjr4-5q7p

### [CVE-2026-88382](https://github.com/redis/hiredis/issues/1357)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-88382
- 関連キーワード: redis
- 影響製品: -
- 公開日: 2026-09-25 02:17:07 JST
- 更新日: 2026-09-25 06:00:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: hiredisのRESPパーサーにおける制御不能なメモリ割り当ての脆弱性。
- 影響: 過剰なメモリ消費により、サービス拒否（DoS）状態が引き起こされる可能性があります。
- 推奨対応: 修正されたバージョンのhiredisへ更新してください。

#### References
- https://github.com/redis/hiredis/issues/1357
- https://github.com/redis/hiredis/issues/1357

### [CVE-2026-97404](https://launchpad.net/bugs/2164987)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-97404
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-25 00:18:01 JST
- 更新日: 2026-09-25 06:08:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenStack ZaqarのWSGIトランスポートにおけるURL-Signatureヘッダー処理の不備。
- 影響: 空の署名ヘッダーを送信することで Keystone 認証および検証を回避され、キューやメッセージの不正操作、管理権限の悪用が行われる可能性があります。
- 推奨対応: OpenStack Zaqarをバージョン22.0.2以降に更新してください。

#### References
- https://launchpad.net/bugs/2164987
- http://www.openwall.com/lists/oss-security/2026/09/24/6

### [CVE-2026-62368](https://github.com/grokability/snipe-it/commit/58754e4e3b86b58a0c4523012ef04a2ae990d2c8)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-62368
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-25 02:17:05 JST
- 更新日: 2026-09-25 03:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Snipe-IT 8.7.0 未満において、CustomField.name に入力されたマークアップがエスケープされずにテーブルヘッダーとして表示される脆弱性（格納型XSS）が存在します。
- 影響: 影響を受ける資産一覧ページを開いたユーザーのセッション内で不正なスクリプトが実行され、データの漏洩や権限昇格などの不正操作が行われる可能性があります。
- 推奨対応: Snipe-IT をバージョン 8.7.0 以降へアップデートしてください。

#### References
- https://github.com/grokability/snipe-it/commit/58754e4e3b86b58a0c4523012ef04a2ae990d2c8
- https://github.com/grokability/snipe-it/releases/tag/v8.7.0
- https://github.com/grokability/snipe-it/security/advisories/GHSA-p9h3-gvpq-5539
- https://github.com/grokability/snipe-it/security/advisories/GHSA-p9h3-gvpq-5539

### [CVE-2026-77581](https://github.com/alam00000/bentopdf/commit/45496fcd2ed6e02dcdde0d3839cc5024c091760c)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-77581
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-25 01:17:10 JST
- 更新日: 2026-09-25 01:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: BentoPDF 2.8.6 以前の CORS プロキシ機能において、ホスト名検証時と DNS 解決時の解釈の差（TOCTOU/SSRF）が存在します。
- 影響: 内部ネットワークや制限された宛先へプロキシ経由でアクセスされ、情報を取得される可能性があります。
- 推奨対応: 最新の修正版へアップデートするか、プロキシ設定を見直してください。

#### References
- https://github.com/alam00000/bentopdf/commit/45496fcd2ed6e02dcdde0d3839cc5024c091760c
- https://github.com/alam00000/bentopdf/commit/58cd1a8893bfe06e4a59a72adc2e7db00a8b9266
- https://github.com/alam00000/bentopdf/releases/tag/v2.8.7
- https://github.com/alam00000/bentopdf/security/advisories/GHSA-5xjf-rr5x-pcfj
- https://github.com/alam00000/bentopdf/security/advisories/GHSA-5xjf-rr5x-pcfj

### [CVE-2026-67233](https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.2.6)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-67233
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-25 01:17:09 JST
- 更新日: 2026-09-25 01:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RabbitMQ の shovel 管理機能において、DELETE リクエストに対する十分な役割検証が行われない脆弱性が存在します。
- 影響: 閲覧権限（monitoring タグ）のみを持つユーザーが、 Shovel リソースを削除または再起動し、サービスに影響を与える可能性があります。
- 推奨対応: RabbitMQ 3.13.15、4.0.20、4.1.11、4.2.6、または 4.3.1 以降へアップデートしてください。

#### References
- https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.2.6
- https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.3.1
- https://github.com/rabbitmq/rabbitmq-server/security/advisories/GHSA-7jc3-73v6-rjvc

### [CVE-2026-91132](https://github.com/discourse/discourse/commit/80968704c1acb1d2ea2c6011dbf6c02ff13238e5)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-91132
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-25 02:17:08 JST
- 更新日: 2026-09-25 02:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Discourse is an open-source discussion platform. Prior to 2026.1.8, 2026.6.3, 2026.7.2, and 2026.8.0, sites using wildcard patterns in the allowed_iframes setting could accept a crafted iframe URL whose allowlisted suffix appeared after a URL authority separator. The wildcard origin check matched the allowed domain tex...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/discourse/discourse/commit/80968704c1acb1d2ea2c6011dbf6c02ff13238e5
- https://github.com/discourse/discourse/commit/d5ae0940707f95da5bc4562f7b544243e3103f8a
- https://github.com/discourse/discourse/commit/d88e02ceb2eede4d8b851d9fe8aef753f3aa40b9
- https://github.com/discourse/discourse/commit/db8064f2a2a2a3feb3308a1c932ac61d950c9e56
- https://github.com/discourse/discourse/pull/42882

### [CVE-2026-91133](https://github.com/discourse/discourse/commit/113c34d433d564bc69642649d501251a7e820b52)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-91133
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-25 02:17:08 JST
- 更新日: 2026-09-25 03:19:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Discourse において、アップロード検索パターン内の SQL LIKE メタ文字が適切にエスケープされない脆弱性が存在します。
- 影響: 認証されたユーザーがワイルドカードを入力することで、アクセス権限のないファイルのメタデータ（元ファイル名やパス等）を取得する可能性があります。
- 推奨対応: Discourse 2026.1.8、2026.6.3、2026.7.2、または 2026.8.0 以降へアップデートしてください。

#### References
- https://github.com/discourse/discourse/commit/113c34d433d564bc69642649d501251a7e820b52
- https://github.com/discourse/discourse/commit/20c48bef712ee3edd4f7af58ca1123cb0c16ef6f
- https://github.com/discourse/discourse/commit/a04cab107a9f57939456181c4b082d0a34ec39bd
- https://github.com/discourse/discourse/commit/cb3ca8420fcc7aba334effd011cf41943a336fa6
- https://github.com/discourse/discourse/pull/42882

### [CVE-2026-91134](https://github.com/discourse/discourse/commit/0a8015e6c7a5079981843721494d30c9a91f5415)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-91134
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-25 02:17:09 JST
- 更新日: 2026-09-25 02:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Discourse の投稿サニタイザーにおいて、エンコードされた userinfo を含む iframe URL の処理に不備があり、許可リストが回避される脆弱性が存在します。
- 影響: 認証済みユーザーが任意のクロスオリジンコンテンツ（iframe）を投稿内に埋め込み、閲覧者に表示させる可能性があります。
- 推奨対応: Discourse 2026.1.8、2026.6.3、2026.7.2、または 2026.8.0 以降へアップデートしてください。

#### References
- https://github.com/discourse/discourse/commit/0a8015e6c7a5079981843721494d30c9a91f5415
- https://github.com/discourse/discourse/commit/1304b0c04f87534053b0d574ae5a9b9ba13dd590
- https://github.com/discourse/discourse/commit/bac7dd1201911851462483271b4567246fa1309d
- https://github.com/discourse/discourse/commit/fed3a58c48412ce7207b72a4629ddbc44482cd64
- https://github.com/discourse/discourse/pull/42882

### [CVE-2026-93231](https://git.kernel.org/stable/c/0d72e78c9d38d5377a059a4837f82b65b91cdcf6)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-93231
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-25 01:17:18 JST
- 更新日: 2026-09-25 01:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linux カーネルの lockd 内 nlmsvc_match_ip() において、関数の引数が不適切に扱われている不具合が存在します。
- 影響: /proc/fs/nfsd/unlock_ip 経由で IP アドレス指定によるロック解除処理を行う際、予期せぬ挙動やカーネルの不具合を引き起こす可能性があります。
- 推奨対応: 修正済みの Linux カーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/0d72e78c9d38d5377a059a4837f82b65b91cdcf6
- https://git.kernel.org/stable/c/21bcb609e0ab1dd60f39ca3498f85808933bcc9f
- https://git.kernel.org/stable/c/b9060689f49dc663e9a3d069c4a65ff63a836e66

### [CVE-2026-93267](https://git.kernel.org/stable/c/2696626a0be5877f445fb647c25ef43930c777e6)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-93267
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-25 01:17:23 JST
- 更新日: 2026-09-25 01:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linux カーネルの RDMA/core における uverbs_free_dmah() で、リソース削除処理のタイミングに起因する Use-After-Free の脆弱性が存在します。
- 影響: リソース解放中のアクセスにより、メモリ破壊やシステムの不安定化、特権昇格などが引き起こされる可能性があります。
- 推奨対応: 修正済みの Linux カーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/2696626a0be5877f445fb647c25ef43930c777e6
- https://git.kernel.org/stable/c/8b22722f45a29a7c0900b1d4d0bc5da5492ece10
- https://git.kernel.org/stable/c/bfc119a40c04bbe3daad826f2160ccbfae6c64ce

### [CVE-2026-77703](https://siberguvenlik.gov.tr/guvenlik-bildirimleri/detay/tr-26-1172)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-77703
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-25 00:17:37 JST
- 更新日: 2026-09-25 04:36:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HAVELSAN Liman Render Engine において、実体認証を伴わない鍵交換が行われる脆弱性が存在します。
- 影響: 中間者攻撃（AiTM）によって暗号化通信が傍受・改ざんされる可能性があります。
- 推奨対応: Liman Render Engine 1.2-75 以降へアップデートしてください。

#### References
- https://siberguvenlik.gov.tr/guvenlik-bildirimleri/detay/tr-26-1172

### [CVE-2026-77707](https://siberguvenlik.gov.tr/guvenlik-bildirimleri/detay/tr-26-1172)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-77707
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-25 00:17:37 JST
- 更新日: 2026-09-25 04:36:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HAVELSAN Liman Render Engine において、SSL/TLS 証明書の検証が不十分な脆弱性が存在します。
- 影響: 中間者攻撃（AiTM）によって通信内容が盗聴または改ざんされる可能性があります。
- 推奨対応: Liman Render Engine 1.2-75 以降へアップデートしてください。

#### References
- https://siberguvenlik.gov.tr/guvenlik-bildirimleri/detay/tr-26-1172

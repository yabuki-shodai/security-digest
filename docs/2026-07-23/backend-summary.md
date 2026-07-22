# Backend CVE Summary (2026-07-23)

## Overview

- 取得日時: 2026-07-23 08:13:34 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 23
- Critical: 2
- High: 11
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-13072](https://jira.mongodb.org/browse/SERVER-128494)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-13072
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-23 05:16:45 JST
- 更新日: 2026-07-23 05:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 単独のmongodインスタンスでcompute modeが有効な場合、集約パイプライン処理中に外部からのBSONデータの検証が不十分でメモリ破損が発生する可能性があります。  
- 影響: メモリ破損によりプロセスの異常終了や予期しない動作が起こる恐れがあります。  
- 推奨対応: compute modeを使用している場合は、MongoDBのアップデートや設定の見直しを検討してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128494

### [CVE-2026-64829](https://github.com/q2a/question2answer/pull/1017)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-64829
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-23 05:17:08 JST
- 更新日: 2026-07-23 05:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Question2Answer 1.8.8以前において、パスワードリセット処理がセッション無効化を適切に行わず、以前取得した「remember-me」クッキーで認証を維持できる脆弱性が存在します。  
- 影響: 攻撃者はパスワードリセット後も不正に認証済み状態を保持でき、アカウント乗っ取りのリスクがあります。  
- 推奨対応: 最新バージョンへのアップデートや、パスワードリセット処理でセッションコードを確実にクリアする修正を適用してください。

#### References
- https://github.com/q2a/question2answer/pull/1017
- https://www.vulncheck.com/advisories/question2answer-session-fixation-via-forgot-password-flow

### [CVE-2026-13064](https://jira.mongodb.org/browse/SERVER-125872)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-13064
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-07-23 05:16:44 JST
- 更新日: 2026-07-23 05:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 深くネストされた$jsonSchemaを含む特定のクエリ操作が、MongoDBで過剰なCPU消費を引き起こす可能性があります。  
- 影響: CPUリソースの枯渇により、システムの応答性が低下し、管理操作で中断できない状態になる恐れがあります。  
- 推奨対応: クエリの設計を見直し、深いネストを避けるか、MongoDBのアップデート情報を確認して適切な対策を検討してください。

#### References
- https://jira.mongodb.org/browse/SERVER-125872

### [CVE-2026-13069](https://jira.mongodb.org/browse/SERVER-127566)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-13069
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-07-23 05:16:45 JST
- 更新日: 2026-07-23 05:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 認証済みユーザーが、検証されていないフィールドを含む特別に細工されたQueryable Encryptionのfindペイロードを送信することで、MongoDBサーバーのCPU過剰消費やメモリ不足を引き起こす可能性があります。  
- 影響: リソース枯渇により、他の操作の可用性が低下し、サービスの妨害が発生する恐れがあります。  
- 推奨対応: MongoDBの最新パッチ適用や、Queryable Encryption機能の利用制限、異常なクエリの監視を検討してください。

#### References
- https://jira.mongodb.org/browse/SERVER-127566

### [CVE-2026-13055](https://jira.mongodb.org/browse/SERVER-123081)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-13055
- 関連キーワード: go, express, mongodb
- 影響製品: -
- 公開日: 2026-07-23 05:16:43 JST
- 更新日: 2026-07-23 05:16:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 認証済みユーザーが`$_internalIndexKey`集約式を利用して、複合ワイルドカードインデックスの処理に失敗しMongoDBサーバーをクラッシュさせる可能性があります。  
- 影響: MongoDBサーバー(mongod)のサービス停止や可用性低下が発生する恐れがあります。  
- 推奨対応: 認証済みユーザーの集約パイプライン実行権限を見直し、MongoDBのアップデートやパッチ適用を検討してください。

#### References
- https://jira.mongodb.org/browse/SERVER-123081

### [CVE-2026-13065](https://jira.mongodb.org/browse/SERVER-127280)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-13065
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-07-23 05:16:44 JST
- 更新日: 2026-07-23 05:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 読み取り専用ユーザーが特定のsortBy式を用いた$linearFillウィンドウ関数を含む集約パイプラインを作成すると、mongodプロセスが異常終了しサービス拒否が発生する可能性があります。  
- 影響: mongodプロセスの異常終了によるサービス停止や可用性の低下が懸念されます。  
- 推奨対応: MongoDBのアップデートやパッチ適用を検討し、読み取り専用ユーザーの操作範囲を見直すことが推奨されます。

#### References
- https://jira.mongodb.org/browse/SERVER-127280

### [CVE-2026-13067](https://jira.mongodb.org/browse/SERVER-128387)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-13067
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-07-23 05:16:44 JST
- 更新日: 2026-07-23 05:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PROXYプロトコルv2をUnixドメインソケットで使用する際、X.509クライアント証明書から派生したロールが設定されたallow-listで検証されない可能性があります。  
- 影響: MONGODB-X509認証後に意図しないロール割り当てが発生する恐れがあり、ローカルのUnixドメインソケットへのアクセス権と有効な証明書が必要です。  
- 推奨対応: ロール検証の設定を見直し、信頼できる証明書のみを使用することを検討してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128387

### [CVE-2026-13075](https://jira.mongodb.org/browse/SERVER-128316)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-13075
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-23 05:16:46 JST
- 更新日: 2026-07-23 05:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 認証済みユーザーが$rankFusionおよび$scoreFusion集約ステージを利用して、メモリ不足時にmongodプロセスをOSにより終了させる可能性があります。  
- 影響: mongodプロセスの予期せぬ停止により、サービスの中断やデータベースの可用性低下が発生する恐れがあります。  
- 推奨対応: 集約クエリの実行権限を必要とするため、権限管理を見直しつつ、MongoDBのアップデートやパッチ適用を検討してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128316

### [CVE-2026-13076](https://jira.mongodb.org/browse/SERVER-128584)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-13076
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-07-23 05:16:46 JST
- 更新日: 2026-07-23 05:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 認証済みユーザーがMongoDBの集約フレームワークで特定のデータ型変換を実行すると、メモリ圧迫時にmongodプロセスがOSによって終了される可能性があります。  
- 影響: 書き込み権限と集約クエリ実行権限を持つユーザーによるサービス停止のリスクがあります。  
- 推奨対応: 不要な権限の制限とMongoDBのアップデートを検討し、メモリ使用状況の監視を強化してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128584

### [CVE-2026-13058](https://jira.mongodb.org/browse/SERVER-127661)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-13058
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-23 05:16:43 JST
- 更新日: 2026-07-23 05:16:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 認証済みの基本的な書き込み権限を持つユーザーが、不完全なトランザクションコマンドを送信することでmongodプロセスを異常終了させる可能性があります。  
- 影響: トランザクションコマンドの検証不整合により、サービス拒否（DoS）が発生する恐れがあります。  
- 推奨対応: トランザクションコマンドの送信を制限し、MongoDBのアップデートやパッチ適用を検討してください。

#### References
- https://jira.mongodb.org/browse/SERVER-127661

### [CVE-2026-13062](https://jira.mongodb.org/browse/SERVER-127831)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-13062
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-23 05:16:44 JST
- 更新日: 2026-07-23 05:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 認証済みの書き込み権限ユーザーが、シャードクラスタのmongosルーター経由で細工した書き込みコマンドを送信することで、Queryable Encryption対応コレクションの内部暗号化メタデータを不正に変更できる可能性があります。  
- 影響: 暗号化されたクエリの正確性が損なわれ、データの整合性に問題が生じる恐れがあります。  
- 推奨対応: 書き込み権限の管理を厳格に行い、該当製品のアップデート情報を確認して適切な修正パッチを適用してください。

#### References
- https://jira.mongodb.org/browse/SERVER-127831

### [CVE-2026-13063](https://jira.mongodb.org/browse/SERVER-127737)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-13063
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-07-23 05:16:44 JST
- 更新日: 2026-07-23 05:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An authenticated user with standard read/write privileges can cause the mongod process to terminate due to an out-of-memory condition by sending a crafted aggregation command. MongoDB's libmongocrypt library insufficiently validates payload-supplied values, which can result in an excessively large memory allocation.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-127737

### [CVE-2026-13070](https://jira.mongodb.org/browse/SERVER-128362)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-13070
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-07-23 05:16:45 JST
- 更新日: 2026-07-23 05:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A MongoDB server initiating an outbound TLS connection may terminate abnormally when processing a malformed OCSP response from a remote peer during the TLS handshake. OCSP stapling validation is enabled by default for outgoing TLS connections. Affected scenarios require the remote peer to hold a certificate issued by t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128362

### [CVE-2026-13073](https://jira.mongodb.org/browse/SERVER-128512)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-13073
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-23 05:16:45 JST
- 更新日: 2026-07-23 05:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An authenticated user with read-only privileges can cause the mongod process to terminate abnormally by issuing a crafted aggregation command, resulting in denial of service for all connected clients until the process is restarted. The issue stems from an internal engine selection inconsistency triggered by a specific...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128512

### [CVE-2026-13074](https://jira.mongodb.org/browse/SERVER-128517)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-13074
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-07-23 05:16:46 JST
- 更新日: 2026-07-23 05:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An unauthenticated remote client can cause excessive CPU consumption on a MongoDB server by sending a specific combination of parameters to the awaitable hello command in exhaust mode. The server's handling of this combination results in a response loop that bypasses normal throttling, allowing a small number of connec...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128517

### [CVE-2026-10822](https://downloads.isc.org/isc/bind9/9.20.26)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-10822
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-23 00:16:51 JST
- 更新日: 2026-07-23 05:33:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: If BIND encounters a particular invalid data structure in a DNS record, it will accept the invalid data, and may subsequently abort and exit. BIND will first need to store a DNS record for a key (KEY, DNSKEY, etc.). That key must specify a PRIVATEDNS algorithm (253), and in the algorithm identifier, improperly give a l...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://downloads.isc.org/isc/bind9/9.20.26
- https://downloads.isc.org/isc/bind9/9.21.24
- https://kb.isc.org/docs/cve-2026-10822

### [CVE-2026-13068](https://jira.mongodb.org/browse/SERVER-128198)

> **Backend** / **MEDIUM** / CVSS: **4.2** / KEV: **no**

- タイトル: CVE-2026-13068
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-23 05:16:45 JST
- 更新日: 2026-07-23 05:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An authenticated user holding cursor termination privileges on one database may incorrectly be permitted to terminate active cursors on a separate database, disrupting ongoing query operations for other users. The behavior stems from an authorization check that does not correctly scope privileges to the appropriate nam...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128198

### [CVE-2026-13089](https://datatracker.ietf.org/doc/html/rfc8725#section-3.1)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-13089
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-23 06:17:12 JST
- 更新日: 2026-07-23 06:17:12 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OIDC::Lite versions through 0.12.1 for Perl allow ID Token signature verification bypass via a token-controlled algorithm allowlist in verify. When the caller does not pin an algorithm, OIDC::Lite::Model::IDToken::verify sets $self->alg($self->header->{alg}) from the token's own header and then calls decode_jwt(token,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://datatracker.ietf.org/doc/html/rfc8725#section-3.1
- https://github.com/ritou/p5-oidc-lite/pull/31
- https://security.metacpan.org/patches/O/OIDC-Lite/0.10/CVE-2026-13089-r1.patch

### [CVE-2026-13056](https://jira.mongodb.org/browse/SERVER-124355)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-13056
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-07-23 05:16:43 JST
- 更新日: 2026-07-23 05:16:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Using expressions that generate large arrays it is possible to craft a query that creates very large intermediate objects in memory, causing the server to crash with OOM error.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-124355

### [CVE-2026-9737](https://jira.mongodb.org/browse/SERVER-128341)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-9737
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-07-23 05:17:09 JST
- 更新日: 2026-07-23 05:17:09 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: クエリプランニング時に生のBSONObj形式でソートパターンを読み取る際、メタ式の処理が不十分で不正な変換が発生し、インバリアント違反を引き起こす可能性があります。  
- 影響: クエリ処理の異常や予期しない動作、場合によってはサービスの停止やデータの整合性問題が生じる恐れがあります。  
- 推奨対応: 最新のパッチ適用やベンダーからの修正情報を確認し、該当するアップデートを速やかに適用してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128341

### [CVE-2026-13061](https://jira.mongodb.org/browse/SERVER-127689)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-13061
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-23 05:16:44 JST
- 更新日: 2026-07-23 05:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 認証済みユーザーが$listSessions集約ステージを通じて他ユーザーのセッションメタデータを閲覧できる可能性があります。  
- 影響: セッションIDやユーザー名、活動タイムスタンプなどの情報漏洩により、プライバシーやセキュリティリスクが生じる恐れがあります。  
- 推奨対応: アクセス権限の見直しや、該当機能の利用制限を検討し、最新のセキュリティパッチ適用を推奨します。

#### References
- https://jira.mongodb.org/browse/SERVER-127689

### [CVE-2026-16615](https://access.redhat.com/security/cve/CVE-2026-16615)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-16615
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-23 02:16:55 JST
- 更新日: 2026-07-23 05:33:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A flaw was found in librest. The PKCE implementation for OAuth authorization uses the GRand function from the GLib API, a cryptographically insecure pseudo-random number generator. Because the generated "code verifier" lacks sufficient cryptographic entropy, a malicious actor can reverse-engineer the pseudo-random numb...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-16615
- https://bugzilla.redhat.com/show_bug.cgi?id=2504432
- https://gitlab.gnome.org/GNOME/librest/-/issues/25

### [CVE-2026-16628](https://github.com/oclif/oclif/)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-16628
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-23 07:16:28 JST
- 更新日: 2026-07-23 07:16:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability was detected in oclif up to 4.23.16. Affected by this vulnerability is the function child_process.exec of the component JIT Plugin Entry Handler. Performing a manipulation of the argument jitPlugins results in os command injection. The attack is only possible with local access. The exploit is now public...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/oclif/oclif/
- https://github.com/oclif/oclif/commit/939b045725e065baebc4587b8bccfd56731eed3d
- https://github.com/oclif/oclif/issues/2051
- https://github.com/oclif/oclif/pull/2052
- https://vuldb.com/cve/CVE-2026-16628

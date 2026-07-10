# Backend CVE Summary (2026-07-11)

## Overview

- 取得日時: 2026-07-11 08:10:55 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 20
- Critical: 2
- High: 10
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-12761](https://plugins.trac.wordpress.org/browser/miniorange-login-openid/tags/7.7.0/class-mo-openid-login-widget.php#L1502)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-12761
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-11 06:16:53 JST
- 更新日: 2026-07-11 06:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WordPressのminiOrange Social Login and Registerプラグイン（バージョン7.7.0以下）において、OAuthプロバイダーからのメール検証が不十分なため認証バイパスが可能で、管理者アカウントの乗っ取りが発生する恐れがあります。  
- 影響: 未認証の攻撃者がOTPをオフラインで解析し、任意の管理者アカウントに不正ログインできるため、サイトの完全な管理権限を奪われるリスクがあります。  
- 推奨対応: プラグインの最新版への更新を行い、OAuthメール検証の強化やOTP処理の改善がなされているか確認してください。

#### References
- https://plugins.trac.wordpress.org/browser/miniorange-login-openid/tags/7.7.0/class-mo-openid-login-widget.php#L1502
- https://plugins.trac.wordpress.org/browser/miniorange-login-openid/tags/7.7.0/mo-openid-social-login-functions.php#L34
- https://plugins.trac.wordpress.org/browser/miniorange-login-openid/tags/7.7.0/view/profile_completion/mo_openid_prof_comp_funct.php#L191
- https://plugins.trac.wordpress.org/browser/miniorange-login-openid/tags/7.7.0/view/profile_completion/mo_openid_prof_comp_funct.php#L41
- https://plugins.trac.wordpress.org/changeset/3592642/

### [CVE-2026-55229](https://github.com/gotenberg/gotenberg/commit/98fc40347885ad510a311b990a73397c6d4143db)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-55229
- 関連キーワード: go, docker
- 影響製品: -
- 公開日: 2026-07-11 06:16:55 JST
- 更新日: 2026-07-11 06:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Gotenbergの8.34.0未満のバージョンにおいて、特別に細工されたドキュメントがLibreOfficeの変換処理中に外部およびローカルのリソースを自動取得し、盲目的なSSRFおよび限定的なローカルファイル情報漏洩を引き起こす可能性があります。  
- 影響: 攻撃者がリモートからSSRF攻撃を行い、内部ネットワークへのアクセスやローカルファイルの情報取得が可能になるリスクがあります。  
- 推奨対応: Gotenbergをバージョン8.34.0以降にアップデートし、外部リソースの自動取得を制限する設定を検討してください。

#### References
- https://github.com/gotenberg/gotenberg/commit/98fc40347885ad510a311b990a73397c6d4143db
- https://github.com/gotenberg/gotenberg/releases/tag/v8.34.0
- https://github.com/gotenberg/gotenberg/security/advisories/GHSA-2mrg-35hw-x3x9

### [CVE-2026-57220](https://github.com/rabbitmq/rabbitmq-server/commit/595ec28fa1621b1f2c28124e4e0466a8ad963547)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-57220
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-11 06:16:59 JST
- 更新日: 2026-07-11 06:16:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: RabbitMQの4.2.6未満のバージョンにおいて、認証前にストリームフレームサイズ制限が適切に適用されず、未認証のリモートクライアントが過大なフレーム長を宣言してメモリを消費できる脆弱性が存在します。  
- 影響: メモリ消費の増加により、サービスの可用性が低下する可能性があります。  
- 推奨対応: RabbitMQをバージョン4.2.6以降にアップデートし、脆弱性を修正してください。

#### References
- https://github.com/rabbitmq/rabbitmq-server/commit/595ec28fa1621b1f2c28124e4e0466a8ad963547
- https://github.com/rabbitmq/rabbitmq-server/commit/773a49c4921e8be990262a2d609c35916825679e
- https://github.com/rabbitmq/rabbitmq-server/pull/16171
- https://github.com/rabbitmq/rabbitmq-server/pull/16173
- https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.2.6

### [CVE-2026-53450](https://github.com/coturn/coturn/commit/b057acbebe721c8f2f202ddad5e16289e295c754)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-53450
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 04:17:24 JST
- 更新日: 2026-07-11 05:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Coturn 4.13.0以前のバージョンで、IPv4マップドIPv6アドレスを使うことでループバックピアの拒否機能が回避される脆弱性が存在します。  
- 影響: 認証済みTURNクライアントがlocalhostに限定されたサービスをTURNリレー経由で外部に公開できる可能性があります。  
- 推奨対応: Coturnをバージョン4.13.0以降にアップデートし、ループバックガードの適切な動作を確保してください。

#### References
- https://github.com/coturn/coturn/commit/b057acbebe721c8f2f202ddad5e16289e295c754
- https://github.com/coturn/coturn/security/advisories/GHSA-w4hf-cr3w-6h79
- https://github.com/coturn/coturn/security/advisories/GHSA-w4hf-cr3w-6h79

### [CVE-2026-54063](https://github.com/qax-os/excelize/releases/tag/v2.11.0)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-54063
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 02:16:58 JST
- 更新日: 2026-07-11 04:17:24 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ExcelizeライブラリのcheckSheet()関数が、攻撃者制御のXML属性値を検証せずにメモリ割り当てに使用するため、特別に細工されたXLSXファイルでサービス拒否(DoS)が発生する可能性があります。  
- 影響: 大量メモリ割り当てによるプロセス強制終了や、範囲外スライスアクセスによるランタイムパニックが発生し、認証不要で攻撃可能です。  
- 推奨対応: Excelizeをバージョン2.11.0以降にアップデートし、外部から提供されたXLSXファイルの取り扱いに注意してください。

#### References
- https://github.com/qax-os/excelize/releases/tag/v2.11.0
- https://github.com/qax-os/excelize/security/advisories/GHSA-h69g-9hx6-f3v4
- https://github.com/qax-os/excelize/security/advisories/GHSA-h69g-9hx6-f3v4

### [CVE-2026-56305](https://github.com/Cap-go/capgo/security/advisories/GHSA-rjr5-qxqj-cx8g)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-56305
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 00:16:42 JST
- 更新日: 2026-07-11 00:44:09 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Capgo 12.128.2以前のバージョンにおいて、パスワード変更エンドポイントで認証バイパスの脆弱性が存在し、現在のパスワード確認なしでパスワードを変更可能です。  
- 影響: 一時的なセッションアクセスを持つ攻撃者が正当なユーザーのアカウントを乗っ取り、永久にロックアウトさせる恐れがあります。  
- 推奨対応: 速やかにCapgoを最新版にアップデートし、パスワード変更機能のアクセス制御を確認してください。

#### References
- https://github.com/Cap-go/capgo/security/advisories/GHSA-rjr5-qxqj-cx8g
- https://www.vulncheck.com/advisories/capgo-authentication-bypass-in-password-change-via-missing-current-password-validation

### [CVE-2026-59161](https://github.com/qax-os/excelize/commit/93f0b3caed37f21ef5079e3259c6c21dcfe68453)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-59161
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 02:17:02 JST
- 更新日: 2026-07-11 02:49:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Excelizeの2.11.0以前のバージョンで、ストリーミングワークシートリーダーがTotalRows制限を適切に適用せず、大きな行番号を持つ不正なXLSXファイルで空行を大量に追加しメモリとCPUを過剰消費する問題。  
- 影響: 悪意のあるXLSXファイルにより、サービスのメモリ消費増大やCPU負荷上昇が発生し、DoS攻撃のリスクがある可能性。  
- 推奨対応: Excelizeをバージョン2.11.0以降にアップデートし、ストリーミングワークシートリーダーの制限が適切に適用されるようにすること。

#### References
- https://github.com/qax-os/excelize/commit/93f0b3caed37f21ef5079e3259c6c21dcfe68453
- https://github.com/qax-os/excelize/pull/2331
- https://github.com/qax-os/excelize/releases/tag/v2.11.0
- https://github.com/qax-os/excelize/security/advisories/GHSA-q5j5-6p94-4gwc

### [CVE-2026-56254](https://github.com/Cap-go/capgo/security/advisories/GHSA-j2f4-4pfc-p8rx)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-56254
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-11 00:16:41 JST
- 更新日: 2026-07-11 01:16:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: @capgo/capacitor-updater（Cap-go/capgo）12.128.2未満のバージョンでは、エンドツーエンド暗号化の設計によりプライベートキーが各デバイスに配布されているため、攻撃者が中間者攻撃やサーバー侵害を通じて正当な署名付き更新を偽造可能です。  
- 影響: 攻撃者が不正な更新を配布し、ユーザーのデバイスに悪意あるソフトウェアをインストールさせるリスクがあります。  
- 推奨対応: 可能な限り速やかに12.128.2以降のバージョンにアップデートし、プライベートキーの安全な管理を確認してください。

#### References
- https://github.com/Cap-go/capgo/security/advisories/GHSA-j2f4-4pfc-p8rx
- https://www.vulncheck.com/advisories/capacitor-updater-end-to-end-encryption-bypass-via-private-key-distribution

### [CVE-2026-56279](https://github.com/Cap-go/capgo/security/advisories/GHSA-fch8-pp28-mw2x)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-56279
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 00:16:42 JST
- 更新日: 2026-07-11 01:16:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Capgo 12.128.2以前のバージョンにおいて、get_orgs_v7(userid) RPC関数が本来のアクセス制御を回避し、認証なしで他ユーザーの組織情報を取得できる情報漏洩の脆弱性が存在します。  
- 影響: 攻撃者は任意のユーザーUUIDを指定して、他ユーザーの組織メンバーシップ、役割、管理者メール、請求関連のメタデータを取得可能です。  
- 推奨対応: 影響を受けるバージョンから最新バージョンへのアップデートを検討し、アクセス制御の設定を見直すことを推奨します。

#### References
- https://github.com/Cap-go/capgo/security/advisories/GHSA-fch8-pp28-mw2x
- https://www.vulncheck.com/advisories/capgo-information-disclosure-via-get-orgs-v7-rpc-endpoint
- https://github.com/Cap-go/capgo/security/advisories/GHSA-fch8-pp28-mw2x

### [CVE-2026-56335](https://github.com/Cap-go/capgo/security/advisories/GHSA-ph9c-vwjq-pqhj)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-56335
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 00:16:42 JST
- 更新日: 2026-07-11 01:16:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Capgo 12.128.2以前のバージョンにおいて、認証チェックの不備により書き込み権限のあるAPIキーで保護されたチャネル設定を不正に変更できる脆弱性が存在します。  
- 影響: 攻撃者は本来許可されていないチャネルの公開設定やセキュリティ関連フラグを変更可能で、サービスの安全性が損なわれる恐れがあります。  
- 推奨対応: 最新バージョンへのアップデートを検討し、APIキーの権限管理と認証処理の見直しを行うことが望ましいです。

#### References
- https://github.com/Cap-go/capgo/security/advisories/GHSA-ph9c-vwjq-pqhj
- https://www.vulncheck.com/advisories/capgo-channel-configuration-mutation-via-write-scoped-api-keys
- https://github.com/Cap-go/capgo/security/advisories/GHSA-ph9c-vwjq-pqhj

### [CVE-2026-56309](https://github.com/Cap-go/capgo/security/advisories/GHSA-q52j-ggvx-cr4v)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-56309
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 00:16:42 JST
- 更新日: 2026-07-11 01:16:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Capgo 12.128.2未満のバージョンで、/files/upload/attachmentsエンドポイントのプランやクォータ制限が適切に適用されず、プラン制限されたアプリが公開可能なR2オブジェクトを作成できる問題。  
- 影響: 攻撃者はアップロードスコープのAPIキーを使い、プランチェックを回避して任意の添付ファイルをアップロードし、ストレージや帯域幅の悪用が可能になる可能性がある。  
- 推奨対応: Capgoを12.128.2以降にアップデートし、APIキーの権限管理とプラン制限の適用状況を確認すること。

#### References
- https://github.com/Cap-go/capgo/security/advisories/GHSA-q52j-ggvx-cr4v
- https://www.vulncheck.com/advisories/capgo-plan-bypass-via-unrestricted-attachment-upload-endpoint
- https://github.com/Cap-go/capgo/security/advisories/GHSA-q52j-ggvx-cr4v

### [CVE-2026-56664](https://github.com/zitadel/zitadel/commit/4925fab849d39a88674485d937b79e54318b48a8)

> **Backend** / **MEDIUM** / CVSS: **4.2** / KEV: **no**

- タイトル: CVE-2026-56664
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 03:16:23 JST
- 更新日: 2026-07-11 04:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ZITADELのJWT外部IDプロバイダ検証で、iatクレームがないトークンの最大有効期限チェックがスキップされ、古いトークンが認証を通過する可能性があります。  
- 影響: 古いトークンを使った不正アクセスのリスクがあり、認証の信頼性が低下する恐れがあります。  
- 推奨対応: ZITADELをバージョン3.4.12または4.15.2以降にアップデートし、トークンの有効期限チェックを適切に行うことを推奨します。

#### References
- https://github.com/zitadel/zitadel/commit/4925fab849d39a88674485d937b79e54318b48a8
- https://github.com/zitadel/zitadel/commit/d1c3aa84af8fcb0f33910ada30b866f4afb551ac
- https://github.com/zitadel/zitadel/releases/tag/v3.4.12
- https://github.com/zitadel/zitadel/releases/tag/v4.15.2
- https://github.com/zitadel/zitadel/security/advisories/GHSA-wxg7-w2v3-w38g

### [CVE-2026-56665](https://github.com/zitadel/zitadel/commit/4925fab849d39a88674485d937b79e54318b48a8)

> **Backend** / **MEDIUM** / CVSS: **4.2** / KEV: **no**

- タイトル: CVE-2026-56665
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 03:16:24 JST
- 更新日: 2026-07-11 04:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ZITADELのJWT外部IDプロバイダー検証で、expクレームがないトークンの有効期限処理がスキップされる問題がありました。  
- 影響: 有効期限なしのトークンが信頼された発行者からのものであれば無期限に有効とみなされる可能性があります。  
- 推奨対応: バージョン3.4.12または4.15.2以降にアップデートして問題を修正してください。

#### References
- https://github.com/zitadel/zitadel/commit/4925fab849d39a88674485d937b79e54318b48a8
- https://github.com/zitadel/zitadel/commit/d1c3aa84af8fcb0f33910ada30b866f4afb551ac
- https://github.com/zitadel/zitadel/releases/tag/v3.4.12
- https://github.com/zitadel/zitadel/releases/tag/v4.15.2
- https://github.com/zitadel/zitadel/security/advisories/GHSA-v77h-2w3m-94hx

### [CVE-2026-10768](https://www.drupal.org/sa-contrib-2026-039)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-10768
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 07:16:38 JST
- 更新日: 2026-07-11 07:16:38 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: DrupalのLocalGov Workflowsモジュールに認可チェックの欠如による強制ブラウジングの脆弱性が存在します。  
- 影響: バージョン0.0.0から1.6.0までのLocalGov Workflowsが影響を受け、不正アクセスの可能性があります。  
- 推奨対応: 影響を受けるバージョンの使用を控え、アップデートやパッチの適用を検討してください。

#### References
- https://www.drupal.org/sa-contrib-2026-039

### [CVE-2026-55671](https://github.com/zitadel/zitadel/commit/b6f78086913b8d916bce9ab2e049ab0d84f947fd)

> **Backend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-55671
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 03:16:23 JST
- 更新日: 2026-07-11 03:56:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ZITADELのバージョン4.0.0-rc.1から4.15.1にかけて、HTTP通知チャネルやOIDC BackChannel Logout、SAMLメタデータのURL取得でユーザー定義URLの検証が不十分なため、DNSリバインディングやリダイレクトを利用した内部ネットワークへのリクエストが可能になる問題です。  
- 影響: 攻撃者が内部IPやループバックアドレスへの不正アクセスを試みる可能性があり、情報漏洩やサービスの誤動作を引き起こす恐れがあります。  
- 推奨対応: ZITADELをバージョン4.15.2以降にアップデートし、ユーザー定義URLの検証強化が適用された状態にすることを推奨します。

#### References
- https://github.com/zitadel/zitadel/commit/b6f78086913b8d916bce9ab2e049ab0d84f947fd
- https://github.com/zitadel/zitadel/releases/tag/v4.15.2
- https://github.com/zitadel/zitadel/security/advisories/GHSA-29jh-8cfq-rr8x

### [CVE-2026-56329](https://github.com/Cap-go/capgo/security/advisories/GHSA-76qq-gg2p-pwwj)

> **Backend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-56329
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 00:16:42 JST
- 更新日: 2026-07-11 02:17:00 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Capgo 12.128.2以前のバージョンにおいて、プレビュー用ホスト名の解析でダブルアンダースコアをドットに誤変換する問題により、テナント間で名前空間の衝突が発生する脆弱性が存在します。  
- 影響: 攻撃者がアンダースコアを含むアプリIDを登録することで、他のテナントのアプリIDと衝突し、プレビューの誤ルーティングや被害者アプリのプレビューアクセス拒否が発生する可能性があります。  
- 推奨対応: 影響を受けるバージョンからのアップデートや、アプリIDの命名規則の見直しなど、ベンダーの修正情報に基づく対策を検討してください。

#### References
- https://github.com/Cap-go/capgo/security/advisories/GHSA-76qq-gg2p-pwwj
- https://www.vulncheck.com/advisories/capgo-cross-tenant-preview-namespace-collision-via-non-bijective-underscore-decoding
- https://github.com/Cap-go/capgo/security/advisories/GHSA-76qq-gg2p-pwwj

### [CVE-2026-57994](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-mf8r-wm2w-f8c5)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-57994
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 00:16:47 JST
- 更新日: 2026-07-11 02:41:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: phpMyFAQ 4.1.5未満のバージョンで、公開APIのフィルタリングが不一致なため、認証なしで非公開のFAQコンテンツが取得可能になる問題です。  
- 影響: 非公開（ドラフトやレビュー中）のFAQタイトルや回答内容が第三者に漏洩する恐れがあります。  
- 推奨対応: phpMyFAQを4.1.5以降にアップデートし、APIのアクセス制御を適切に設定してください。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-mf8r-wm2w-f8c5
- https://www.vulncheck.com/advisories/phpmyfaq-information-disclosure-of-inactive-faq-content-via-public-api-endpoints
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-mf8r-wm2w-f8c5

### [CVE-2026-59162](https://github.com/qax-os/excelize/commit/93f0b3caed37f21ef5079e3259c6c21dcfe68453)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-59162
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-11 02:17:02 JST
- 更新日: 2026-07-11 04:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Excelizeライブラリの2.11.0以前のバージョンで、共有文字列セルの値を不適切に処理し、負のインデックス参照によるパニックが発生する可能性があります。  
- 影響: 悪意のあるXLSXファイルを読み込む際にプログラムがクラッシュするリスクがあります。  
- 推奨対応: バージョン2.11.0以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/qax-os/excelize/commit/93f0b3caed37f21ef5079e3259c6c21dcfe68453
- https://github.com/qax-os/excelize/pull/2331
- https://github.com/qax-os/excelize/releases/tag/v2.11.0
- https://github.com/qax-os/excelize/security/advisories/GHSA-fx5j-qcqg-grpf
- https://github.com/qax-os/excelize/security/advisories/GHSA-fx5j-qcqg-grpf

### [CVE-2026-61444](https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-g6j7-pffp-8whg)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-61444
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-11 00:16:50 JST
- 更新日: 2026-07-11 06:17:00 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PraisonAI 4.6.78未満のバージョンにおいて、deploy/api.pyのagents_fileパラメータが適切にサニタイズされず、コードインジェクションの脆弱性が存在します。  
- 影響: 攻撃者は任意のPythonコードを注入・実行でき、サーバー上での不正操作や情報漏洩のリスクがあります。  
- 推奨対応: 速やかにPraisonAIをバージョン4.6.78以降にアップデートし、入力値の検証・サニタイズを強化してください。

#### References
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-g6j7-pffp-8whg
- https://www.vulncheck.com/advisories/praisonai-before-code-injection-via-f-string
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-g6j7-pffp-8whg

### [CVE-2026-55659](https://github.com/gristlabs/grist-core/commit/4ced8064b7ea0e1763d5a6a2588b22774ce7efbc)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-55659
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-07-11 06:16:56 JST
- 更新日: 2026-07-11 06:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Gristの1.7.15以前のバージョンで、ユーザー制御の値が適切にエスケープされずにページやインラインスクリプトに埋め込まれ、クロスサイトスクリプティングが発生する脆弱性。  
- 影響: 悪意あるスクリプトが認証済みセッション内で実行され、データの読み取り・変更や共有設定の改変、編集者が所有者権限に昇格する可能性がある。  
- 推奨対応: バージョン1.7.15以降にアップデートし、ユーザー入力の適切なエスケープ処理を行うこと。

#### References
- https://github.com/gristlabs/grist-core/commit/4ced8064b7ea0e1763d5a6a2588b22774ce7efbc
- https://github.com/gristlabs/grist-core/releases/tag/v1.7.15
- https://github.com/gristlabs/grist-core/security/advisories/GHSA-6qrq-h2h6-cw54

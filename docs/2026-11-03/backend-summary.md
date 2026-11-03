# Backend CVE Summary (2026-11-03)

## Overview

- 取得日時: 2026-11-03 12:26:14 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 21
- Critical: 5
- High: 11
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-105769](https://github.com/chainguard-forks/kaniko/pull/495)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-105769
- 関連キーワード: go, express, docker
- 影響製品: -
- 公開日: 2026-11-03 02:17:32 JST
- 更新日: 2026-11-03 04:34:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kaniko（1.25.20未満）が依存するACR認証ヘルパーの不正規表現に起因するアクセス権限情報漏洩の脆弱性。
- 影響: 攻撃者が用意した不審なレジストリホスト名に対してビルド時のAzureアクセストークンが送信され、認証情報が窃取される可能性があります。
- 推奨対応: kanikoをバージョン1.25.20以降へアップデートしてください。

#### References
- https://github.com/chainguard-forks/kaniko/pull/495
- https://github.com/chainguard-forks/kaniko/releases/tag/v1.25.20
- https://github.com/chainguard-forks/kaniko/security/advisories/GHSA-5q7h-w9jf-cx97
- https://github.com/chrismellard/docker-credential-acr-env/issues/21
- https://pkg.go.dev/vuln/GO-2026-6225

### [CVE-2026-120447](https://github.com/bufanyun/hotgo/blob/269b2f9e435cf8ff6b18d53bc053a905f4e02d11/server/internal/logic/sys/sms_log.go)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-120447
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-11-03 00:17:27 JST
- 更新日: 2026-11-03 09:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HotGo 2.8.4〜2.15.1 における認証バイパスの脆弱性。/admin/sms/send リクエストの Code フィールドを介して任意のSMS検証コードを設定できる問題が存在します。
- 影響: 攻撃者が対象ユーザーの携帯電話番号を知っている場合、任意の検証コードを設定してログインし、管理者を含むアカウントを乗っ取る可能性があります。
- 推奨対応: 対策済みバージョンへのアップデート、およびSMS送信エンドポイントでの検証コード指定の制限を行ってください。

#### References
- https://github.com/bufanyun/hotgo/blob/269b2f9e435cf8ff6b18d53bc053a905f4e02d11/server/internal/logic/sys/sms_log.go
- https://github.com/bufanyun/hotgo/blob/269b2f9e435cf8ff6b18d53bc053a905f4e02d11/server/internal/model/input/sysin/sms_log.go
- https://github.com/bufanyun/hotgo/commit/cb57056c746650e6ff86dec1e97d404b63dcfd30
- https://github.com/bufanyun/hotgo/issues/240
- https://vul.yulun.ac.cn/20261102/hotgo/

### [CVE-2026-120433](https://sourceforge.net/p/netpbm/code/5328/)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-120433
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-03 00:17:24 JST
- 更新日: 2026-11-03 04:14:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Netpbm（10.86.51未満、11.02.30未満の11.x、11.15.08未満の11.03）の picttoppm paintPoly() 関数におけるスタックベースのバッファオーバーフローの脆弱性。
- 影響: 100を超えるポリゴン点を持つ細工されたPICTファイルを処理させることで、固定配列がオーバーフローし、クラッシュや任意コード実行が発生する可能性があります。
- 推奨対応: Netpbm 10.86.51、11.02.30、11.15.08 またはそれ以降の修正済みバージョンへアップデートしてください。

#### References
- https://sourceforge.net/p/netpbm/code/5328/
- https://svn.code.sf.net/p/netpbm/code/!svn/bc/5327/trunk/converter/ppm/picttoppm.c
- https://svn.code.sf.net/p/netpbm/code/!svn/bc/5357/advanced/doc/HISTORY
- https://svn.code.sf.net/p/netpbm/code/!svn/bc/5358/stable/doc/HISTORY
- https://svn.code.sf.net/p/netpbm/code/!svn/bc/5371/super_stable/doc/HISTORY

### [CVE-2026-120434](https://sourceforge.net/p/netpbm/code/5331/)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-120434
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-03 00:17:25 JST
- 更新日: 2026-11-03 04:14:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Netpbm（10.86.51未満、11.02.30未満の11.x、11.15.08未満の11.03）の picttoppm scanPoly() 関数におけるスタックベースのバッファオーバーフローの脆弱性。
- 影響: ポリゴンエッジが5000点を超える細工されたPICTファイルを処理させることで、coord配列が溢れ、クラッシュや任意コード実行につながる可能性があります。
- 推奨対応: Netpbm 10.86.51、11.02.30、11.15.08 またはそれ以降の修正済みバージョンへアップデートしてください。

#### References
- https://sourceforge.net/p/netpbm/code/5331/
- https://svn.code.sf.net/p/netpbm/code/!svn/bc/5330/trunk/converter/ppm/picttoppm.c
- https://svn.code.sf.net/p/netpbm/code/!svn/bc/5357/advanced/doc/HISTORY
- https://svn.code.sf.net/p/netpbm/code/!svn/bc/5358/stable/doc/HISTORY
- https://svn.code.sf.net/p/netpbm/code/!svn/bc/5371/super_stable/doc/HISTORY

### [CVE-2026-120444](https://github.com/sea-team/gofound/blob/v1.4.1/searcher/container.go)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-120444
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-03 00:17:26 JST
- 更新日: 2026-11-03 04:35:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GoFound 1.4.1 以下におけるパストラバーサルの脆弱性。database パラメータで ../ シーケンスを扱う処理の欠陥に起因します。
- 影響: 未認証の攻撃者が /api/db/create や /api/db/drop へリクエストを送信することで、データディレクトリ外の任意ディレクトリを削除される可能性があります。
- 推奨対応: GoFound を最新バージョンに更新するか、データベース操作APIに対する入力検証ルールを強化してください。

#### References
- https://github.com/sea-team/gofound/blob/v1.4.1/searcher/container.go
- https://github.com/sea-team/gofound/blob/v1.4.1/searcher/engine.go
- https://github.com/sea-team/gofound/issues/101
- https://vul.yulun.ac.cn/20261102/gofound/
- https://www.vulncheck.com/advisories/gofound-through-1.4.1-path-traversal-via-database-parameter-in-api-db-drop

### [CVE-2026-81938](https://grafana.com/security/security-advisories/cve-2026-81938)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-81938
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-03 04:18:11 JST
- 更新日: 2026-11-03 04:34:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Grafana Mimir の Alertmanager におけるローカルファイル参照チェックの不備。http_headers や basic_auth のファイル設定フィールドの検証漏れに起因します。
- 影響: 設定権限を持つテナントが、Alertmanagerプロセスが読み取り可能なホスト上の任意ファイル（認証情報等）を外部へ送信・漏洩させる可能性があります。
- 推奨対応: Grafana Mimir 3.1.7 / 3.2.2、GEM 2.17.20 以降へアップデートしてください。

#### References
- https://grafana.com/security/security-advisories/cve-2026-81938

### [CVE-2026-99218](https://git.kernel.org/stable/c/0fce73efee40c65ce26641c5d93942462f9e8307)

> **Backend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-99218
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-03 01:17:45 JST
- 更新日: 2026-11-03 01:17:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの coredump_finish() において、パーク状態のスレッド解放時に RCU ロックを保持せずに wake_up_process() を呼び出す脆弱性。
- 影響: スレッドが先行して解放されることで解放済みメモリ領域のロック取得（Use-After-Free）が発生し、カーネルクラッシュを引き起こす可能性があります。
- 推奨対応: 修正パッチが適用された最新のLinuxカーネルにアップデートしてください。

#### References
- https://git.kernel.org/stable/c/0fce73efee40c65ce26641c5d93942462f9e8307
- https://git.kernel.org/stable/c/16e94ed90b1b02398e044d41fd1db34828daa08e
- https://git.kernel.org/stable/c/71146c437bae59e5280f657965dc6d006ee3989b
- https://git.kernel.org/stable/c/a0f09ff4c6b93312e565cfe75d76c3a551a3ec4c
- https://git.kernel.org/stable/c/b0eca0edddf4c1dbaf6d1f6a8636b4235f5bc573

### [CVE-2026-99231](https://git.kernel.org/stable/c/8381a912c65b8de16e8a848225c7c5a56b6ea834)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-99231
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-03 01:17:48 JST
- 更新日: 2026-11-03 01:17:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの io_uring/waitid におけるリクエスト所有権の管理不備と競合状態の脆弱性。
- 影響: リクエスト処理中にメモリが解放・再利用され、Use-After-Freeやシステムクラッシュを引き起こす可能性があります。
- 推奨対応: 修正パッチが適用された最新のLinuxカーネルにアップデートしてください。

#### References
- https://git.kernel.org/stable/c/8381a912c65b8de16e8a848225c7c5a56b6ea834
- https://git.kernel.org/stable/c/bf01da1a9cca4a54e5c30b8344e52c26afb87be7
- https://git.kernel.org/stable/c/c10ad2813e15186fb51b37a4d17fafddc99e89a5

### [CVE-2026-99235](https://git.kernel.org/stable/c/173914501b97236d7ea7dc2af7f30feddd4e1436)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-99235
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-03 01:17:48 JST
- 更新日: 2026-11-03 01:17:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのトレーシング機能（create_field_var_hist）において、互換ヒストグラムのポインタ保持処理に不備がある脆弱性。
- 影響: 参照先のヒストグラムが削除された際に無効なポインタを参照（Use-After-Free）し、システム不具合を起こす可能性があります。
- 推奨対応: 修正パッチが適用された最新のLinuxカーネルにアップデートしてください。

#### References
- https://git.kernel.org/stable/c/173914501b97236d7ea7dc2af7f30feddd4e1436
- https://git.kernel.org/stable/c/3609ada3c12cecfb0ae5ee82ef4f86c5f18a2dea
- https://git.kernel.org/stable/c/7a111ba0d1b74c99bc8f096565dc71945f694254
- https://git.kernel.org/stable/c/7cafc82e6153f05a221be678cd649d02e06ba909
- https://git.kernel.org/stable/c/8b307d64a60548e4a74cb746f74d7ed4bd49965e

### [CVE-2026-120430](https://github.com/owen2345/camaleon-cms/blob/2.9.1/app/controllers/camaleon_cms/admin/categories_controller.rb)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-120430
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-03 00:17:24 JST
- 更新日: 2026-11-03 00:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Camaleon CMS 2.9.2 未満の Admin::CategoriesController における不適切な直接オブジェクト参照（IDOR）の脆弱性。
- 影響: 認証済みユーザーが任意のカテゴリーIDを指定することで、本来権限のないカテゴリーの名称変更や削除を行う可能性があります。
- 推奨対応: Camaleon CMS 2.9.2 以降にアップデートしてください。

#### References
- https://github.com/owen2345/camaleon-cms/blob/2.9.1/app/controllers/camaleon_cms/admin/categories_controller.rb
- https://github.com/owen2345/camaleon-cms/commit/fa465e994bcbf4e7be4605853c204b73dea7bbc5
- https://github.com/owen2345/camaleon-cms/pull/1148
- https://github.com/owen2345/camaleon-cms/releases/tag/2.9.2
- https://www.vulncheck.com/advisories/camaleon-cms-before-2.9.2-idor-via-admin-categoriescontroller

### [CVE-2026-99228](https://git.kernel.org/stable/c/08c42055b8f9a5d29236d34ad4bce08828239fe1)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-99228
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-03 01:17:47 JST
- 更新日: 2026-11-03 01:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの io_uring/io-wq において、ワーカー終了処理時に特定の bounded ワーク（FIFOのopenなど）でシグナルが失われる脆弱性。
- 影響: ワーカープロセスが終了待ちで永久にハングアップし、リソースリークやシステム不具合を引き起こす可能性があります。
- 推奨対応: 修正パッチが適用された最新のLinuxカーネルにアップデートしてください。

#### References
- https://git.kernel.org/stable/c/08c42055b8f9a5d29236d34ad4bce08828239fe1
- https://git.kernel.org/stable/c/62996803c1b5f18176de255db4c843021f2d19c8
- https://git.kernel.org/stable/c/7309fea05a3d66af9746843c43fef14c10b8141e
- https://git.kernel.org/stable/c/ddccc60f036b309430cf130d48aafed94ef7355a
- https://git.kernel.org/stable/c/fdb771015c1e13677b57a4015f0c938748f13781

### [CVE-2026-99240](https://git.kernel.org/stable/c/156aeda4d74e9007b56492ed1f3b5838822632be)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-99240
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-03 01:17:49 JST
- 更新日: 2026-11-03 01:17:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのDAMONコア層において、damos_quota_goalのtarget_valueが0の際のパラメータ検証が不十分な問題。
- 影響: ゼロ除算が発生し、カーネルエラーやシステム停止が引き起こされる可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/156aeda4d74e9007b56492ed1f3b5838822632be
- https://git.kernel.org/stable/c/cc190c4073f570fd78a9d00dd3d13a71eced5403
- https://git.kernel.org/stable/c/d5482be6243b816730689099c017109eb8730dd5

### [CVE-2026-120459](https://github.com/mpdavis/python-jose/blob/3.5.0/jose/backends/cryptography_backend.py)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-120459
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-11-03 00:17:29 JST
- 更新日: 2026-11-03 04:14:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: python-jose (3.5.0以下) のHMAC処理において、長さ0のHMACシークレットを受け入れてしまう不備。
- 影響: 空の鍵等を利用してトークンを偽造され、未認証の第三者に認証をバイパスされる可能性があります。
- 推奨対応: ライブラリを対策済みバージョンへ更新し、空のHMAC鍵が使用されないよう設定を確認してください。

#### References
- https://github.com/mpdavis/python-jose/blob/3.5.0/jose/backends/cryptography_backend.py
- https://github.com/mpdavis/python-jose/blob/3.5.0/jose/backends/native.py
- https://github.com/mpdavis/python-jose/issues/398
- https://www.vulncheck.com/advisories/python-jose-through-3.5.0-authentication-bypass-via-empty-hmac-key

### [CVE-2026-120460](https://github.com/dromara/Jpom/blob/v2.11.12/modules/server/src/main/java/org/dromara/jpom/controller/docker/DockerContainerController.java#L48-L51)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-120460
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-11-03 00:17:30 JST
- 更新日: 2026-11-03 03:18:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Jpom (2.11.12以下) において、他ワークスペースのDockerアセットIDに対する認可チェックが不十分な問題。
- 影響: 認証済みユーザーがアクセス権のない他ワークスペースのDockerホストやコンテナ、イメージ等を不正に操作・制御できる可能性があります。
- 推奨対応: Jpomを最新の安全なバージョンへアップデートしてください。

#### References
- https://github.com/dromara/Jpom/blob/v2.11.12/modules/server/src/main/java/org/dromara/jpom/controller/docker/DockerContainerController.java#L48-L51
- https://github.com/dromara/Jpom/blob/v2.11.12/modules/server/src/main/java/org/dromara/jpom/controller/docker/DockerImagesController.java#L48-L51
- https://github.com/dromara/Jpom/commit/ff09fe8095a792cea9c4b8babd93a333655d0a28
- https://github.com/dromara/Jpom/issues/119
- https://www.vulncheck.com/advisories/jpom-through-2.11.12-cross-workspace-authorization-bypass-via-docker-controllers

### [CVE-2026-119085](https://aws.amazon.com/security/security-bulletins/2026-162-aws/)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-119085
- 関連キーワード: gin, aws
- 影響製品: -
- 公開日: 2026-11-03 03:18:44 JST
- 更新日: 2026-11-03 04:34:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Amazon Virtual Engineering Workbench (VEW) のパブリッシング機能における、テンプレートエンジン命令の不適切な処理。
- 影響: 遠隔の認証済みユーザーが任意コードを実行し、パブリッシングLambdaのIAMロール権限で全テナントのリソースにアクセスできる可能性があります。
- 推奨対応: awslabs/virtual-engineering-workbench の最新バージョンから再デプロイを実施してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-162-aws/
- https://github.com/awslabs/virtual-engineering-workbench/commit/c146486cec41f5b04fae57e9ce1a7fb40e695615

### [CVE-2026-120497](https://aws.amazon.com/security/security-bulletins/2026-163-aws/)

> **Backend** / **MEDIUM** / CVSS: **5.0** / KEV: **no**

- タイトル: CVE-2026-120497
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-11-03 04:18:04 JST
- 更新日: 2026-11-03 05:17:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AWS AI-DLC Workflows (2026-07-03より前) のaidlc-traceability CLIが生成するHTMLレポートにおける格納型XSSの脆弱性。
- 影響: 悪意ある成果物データを含めることで、生成されたレポートを開いたユーザーのブラウザ上で任意スクリプトを実行される可能性があります。
- 推奨対応: 2026-07-03以前のaidlc-traceability CLIを削除するか、コミット96cf0ea以降に更新してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-163-aws/
- https://github.com/awslabs/aidlc-workflows/commit/96cf0eaa31a3ad8636e486c7fd2b91c55166393f
- https://github.com/awslabs/aidlc-workflows/security/advisories/GHSA-gjmq-52p3-7fh2
- https://github.com/awslabs/aidlc-workflows/security/advisories/GHSA-gjmq-52p3-7fh2

### [CVE-2026-77879](https://control-webpanel.com/changelog)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-77879
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-11-03 01:17:43 JST
- 更新日: 2026-11-03 04:35:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Control Web Panel (CWP) 1.16未満のaccess_token()関数におけるSQLインジェクションの脆弱性。
- 影響: 攻撃者により任意SQLが実行され、データベースの不法閲覧や認証偽造によるAPI制限のバイパスが行われる可能性があります。
- 推奨対応: CWPをバージョン1.16以上にアップデートしてください。

#### References
- https://control-webpanel.com/changelog
- https://www.vulncheck.com/advisories/control-web-panel-cwp-sql-injection-via-access-token-api

### [CVE-2026-77881](https://control-webpanel.com/changelog)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-77881
- 関連キーワード: gin, mysql
- 影響製品: -
- 公開日: 2026-11-03 01:17:44 JST
- 更新日: 2026-11-03 04:35:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Control Web Panel (CWP) 1.30未満の未認証APIルートにおけるブラインドSQLインジェクションの脆弱性。
- 影響: 未認証の遠隔攻撃者により、タイムベースのブラインドSQLインジェクション経由でデータベース内の任意データが抽出される可能性があります。
- 推奨対応: CWPをバージョン1.30以上にアップデートしてください。

#### References
- https://control-webpanel.com/changelog
- https://www.vulncheck.com/advisories/control-web-panel-cwp-blind-sql-injection-via-user-parameter

### [CVE-2026-102435](https://plugins.svn.wordpress.org/ultimate-addons-for-contact-form-7/tags/3.5.52/addons/pdf-generator/pdf-generator.php)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-102435
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-11-03 05:17:26 JST
- 更新日: 2026-11-03 05:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用Ultra Addons for Contact Form 7プラグイン (3.5.54以下) におけるファイルパス検証不足による任意ファイル削除の脆弱性。
- 影響: PDF生成機能が有効な環境において、未認証の攻撃者が任意ファイルを削除し、最終的にリモートコード実行を引き起こす可能性があります。
- 推奨対応: プラグインを修正済みバージョンへアップデートしてください。

#### References
- https://plugins.svn.wordpress.org/ultimate-addons-for-contact-form-7/tags/3.5.52/addons/pdf-generator/pdf-generator.php
- https://plugins.trac.wordpress.org/changeset/3738548/ultimate-addons-for-contact-form-7
- https://www.wordfence.com/threat-intel/vulnerabilities/id/187777a4-3438-489c-ad3b-7e16753189d6?source=cve

### [CVE-2026-119737](https://mstreet97.github.io/security-research/vulnerability-disclosure/embedded/cve/2026/10/29/From-UART-to-root-android-version.html)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-119737
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-11-03 05:17:38 JST
- 更新日: 2026-11-03 06:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nexbox A95X等で使われるAmlogic Android SDKのpppoe_wrapperデーモンにおけるコマンドインジェクションの脆弱性。
- 影響: ローカルの攻撃者が特定のUnixドメインソケットに特製メッセージを送ることで、root権限で任意のシェルフラグメントを実行できる可能性があります。
- 推奨対応: ベンダーが提供する修正済みファームウェアやセキュリティ更新を適用してください。

#### References
- https://mstreet97.github.io/security-research/vulnerability-disclosure/embedded/cve/2026/10/29/From-UART-to-root-android-version.html
- https://www.vulncheck.com/advisories/amlogic-pppoe-wrapper-command-injection-via-af-unix-socket

### [CVE-2026-119736](https://medium.com/@TheWildEye/from-an-android-apk-to-production-mqtt-exposed-credentials-in-attendo-formerly-petpooja-payroll-eb701d23233e)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-119736
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-11-03 04:18:02 JST
- 更新日: 2026-11-03 04:35:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Attendo (旧Petpooja Payroll) Admin Androidアプリ (3.0.13以下) におけるハードコードされた本番環境MQTT認証情報の問題。
- 影響: APK解凍等により抽出された認証情報を用いてMQTTブローカーへ不正接続され、従業員データ等の漏洩や不正なメッセージ注入が行われる可能性があります。
- 推奨対応: アプリを最新版へ更新し、流出したMQTT認証情報を失効・変更してください。

#### References
- https://medium.com/@TheWildEye/from-an-android-apk-to-production-mqtt-exposed-credentials-in-attendo-formerly-petpooja-payroll-eb701d23233e
- https://play.google.com/store/apps/details?id=com.petpooja.attendance
- https://www.vulncheck.com/advisories/attendo-admin-android-hard-coded-mqtt-broker-credentials

# Backend CVE Summary (2026-07-22)

## Overview

- 取得日時: 2026-07-22 08:08:14 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 23
- Critical: 9
- High: 6
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-64821](https://github.com/americooo/pentest-writeups/tree/main/djangoSIGE-CVE-2026-64821-64822)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-64821
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-07-22 06:16:53 JST
- 更新日: 2026-07-22 06:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: djangoSIGE 1.10以前のバージョンにおいて、HTTP GETメソッドで注文キャンセル処理を行うビューにCSRF脆弱性が存在し、認証済みユーザーの権限を悪用して注文を不正にキャンセルされる可能性があります。  
- 影響: 認証済みユーザーの注文や販売のキャンセルが攻撃者により不正に実行されるリスクがあります。  
- 推奨対応: 安全でないHTTPメソッドでの状態変更処理を避け、CSRFトークン検証を適切に実装するか、該当ビューの修正やアップデートを適用してください。

#### References
- https://github.com/americooo/pentest-writeups/tree/main/djangoSIGE-CVE-2026-64821-64822
- https://github.com/thiagopena/djangoSIGE/pull/163
- https://www.vulncheck.com/advisories/djangosige-csrf-via-get-based-order-cancellation-views

### [CVE-2026-64822](https://github.com/americooo/pentest-writeups/tree/main/djangoSIGE-CVE-2026-64821-64822)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-64822
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-07-22 06:16:53 JST
- 更新日: 2026-07-22 06:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: djangoSIGE 1.10以前のForgotPasswordViewにおいて、パスワードリセット機能を悪用したユーザー列挙の脆弱性が存在します。  
- 影響: 認証されていない攻撃者が有効なアカウントを特定できる可能性があります。  
- 推奨対応: エラーメッセージの統一やレスポンスの調整により、ユーザー情報の漏洩を防ぐ対策を検討してください。

#### References
- https://github.com/americooo/pentest-writeups/tree/main/djangoSIGE-CVE-2026-64821-64822
- https://github.com/thiagopena/djangoSIGE/pull/163
- https://www.vulncheck.com/advisories/djangosige-user-enumeration-via-forgotpasswordview

### [CVE-2026-47407](https://github.com/MervinPraison/PraisonAI/commit/24385d64876577620f749957bd4814f162f4ca47)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-47407
- 関連キーワード: python, fastapi
- 影響製品: -
- 公開日: 2026-07-22 02:17:09 JST
- 更新日: 2026-07-22 03:59:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PraisonAI Platform 0.1.4未満のバージョンでは、ワークスペースの認証が不十分で、異なるワークスペースのリソースに不正アクセス可能な脆弱性が存在します。また、メンバー管理機能で一般メンバーが自身の権限を昇格できる問題もあります。  
- 影響: 不正なワークスペースリソースの読み取り・更新・削除や、権限昇格による管理者権限の不正取得が可能となり、機密情報漏洩やサービスの不正操作が懸念されます。  
- 推奨対応: 最新バージョンへのアップデートを行い、ワークスペースIDの厳密な検証と権限管理の強化を実施してください。

#### References
- https://github.com/MervinPraison/PraisonAI/commit/24385d64876577620f749957bd4814f162f4ca47
- https://github.com/MervinPraison/PraisonAI/pull/1686
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-h8q5-cp56-rr65

### [CVE-2026-8982](https://cyberdanube.com/security-research/multiple-vulnerabilities-in-autel-maxi-charger/)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-8982
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-22 06:16:54 JST
- 更新日: 2026-07-22 06:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Autel Maxi Charger SingleのファームウェアV1.03.51以前に、ベンダー独自のパスワード生成機構を用いた2つの未公開特権アカウントが存在します。  
- 影響: 攻撃者がアルゴリズムと必要な入力値を知っている場合、管理者権限でウェブ管理インターフェースに認証可能です。  
- 推奨対応: ベンダーからの修正パッチ適用や、該当ファームウェアの使用停止を検討し、不明なアカウントの存在を確認してください。

#### References
- https://cyberdanube.com/security-research/multiple-vulnerabilities-in-autel-maxi-charger/

### [CVE-2026-46403](https://github.com/klever-io/klever-go/commit/333f6ec910906e227705fc5767dc897d8fbfc862)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-46403
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-22 05:17:01 JST
- 更新日: 2026-07-22 05:17:01 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Klever-GoのKVMにおいて、読み取り専用モード中でもコントラクトの削除やアップグレードが可能となる脆弱性が存在します。  
- 影響: 読み取り専用呼び出しを利用しているワークフローの分離境界が破られ、所有するコントラクトの不正削除が発生する可能性があります。  
- 推奨対応: バージョン1.7.17以降にアップデートし、読み取り専用モードの状態変更パスの修正を適用してください。

#### References
- https://github.com/klever-io/klever-go/commit/333f6ec910906e227705fc5767dc897d8fbfc862
- https://github.com/klever-io/klever-go/commit/68b94a40824fac2d848a4ded6eb7c91ada6ce9ef
- https://github.com/klever-io/klever-go/security/advisories/GHSA-jc6w-wmfc-fh33

### [CVE-2026-15829](https://github.com/googleapis/mcp-toolbox/pull/3324)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-15829
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-22 02:17:05 JST
- 更新日: 2026-07-22 03:33:31 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Googleのbigquery-forecastツールにSQLインジェクションとセキュリティ境界回避の脆弱性が存在し、ユーザー入力を適切に検証せずにクエリに組み込むことで不正なクエリ実行が可能です。  
- 影響: 攻撃者は許可されていないBigQueryテーブルへのアクセスや複数ステートメントの実行ができ、機密情報の漏洩リスクがあります。  
- 推奨対応: 入力パラメータの適切なエスケープと検証を実施し、ツールのアップデートやパッチ適用を検討してください。

#### References
- https://github.com/googleapis/mcp-toolbox/pull/3324

### [CVE-2026-10677](https://github.com/zephyrproject-rtos/zephyr/commit/8dc7a37bc75402a0a3329397887f32f5fb4da3ad)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-10677
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-22 07:16:59 JST
- 更新日: 2026-07-22 07:16:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ZephyrカーネルのCONFIG_USERSPACEのk_pollシステムコール検証で、誤ったオブジェクトハンドルによりカーネルメモリリークが発生し、最終的にサービス拒否状態を引き起こす可能性があります。  
- 影響: 攻撃者がリソースプールを枯渇させることで、正当なカーネルリソース割り当てが失敗し、システムの安定性に影響を与える恐れがあります。  
- 推奨対応: Zephyr v1.12.0からv4.4.1までの影響バージョンを使用している場合は、修正パッチを適用し、k_pollの検証処理が適切にバッファ解放を行うように更新してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/8dc7a37bc75402a0a3329397887f32f5fb4da3ad
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-r3cc-8wcr-xfj9

### [CVE-2026-16318](https://github.com/aws/s2n-tls/releases/tag/v1.7.6)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-16318
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-22 06:16:49 JST
- 更新日: 2026-07-22 06:16:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: s2n-tlsのQUICトランスポートパラメータ処理でメモリリークが発生し、HelloRetryRequestが複数回呼ばれる際に未使用メモリが蓄積される問題です。  
- 影響: サーバー側のQUIC対応環境で長時間稼働するとメモリ消費が増加し、サービスの安定性に影響を与える可能性があります。  
- 推奨対応: s2n-tlsをv1.7.6以降にアップデートし、メモリリークの修正を適用してください。

#### References
- https://github.com/aws/s2n-tls/releases/tag/v1.7.6
- https://github.com/aws/s2n-tls/security/advisories/GHSA-cr7x-863j-xrc7
- https://staging.prod.website.marketing.aws.dev/security/security-bulletins/2026-062-aws/

### [CVE-2026-21953](https://www.oracle.com/security-alerts/cpujul2026.html)

> **Backend** / **LOW** / CVSS: **3.3** / KEV: **no**

- タイトル: CVE-2026-21953
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-22 07:17:00 JST
- 更新日: 2026-07-22 07:17:00 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Oracle Retail Xstore Point of Service（バージョン21.0.3）において、低権限のログインユーザーが一部データの不正読み取りを行える脆弱性が存在します。  
- 影響: 低い権限の攻撃者による限定的な機密情報の漏洩リスクがあります。  
- 推奨対応: 最新のパッチ適用やアクセス権限の見直しを検討し、不審なアクセスの監視を強化してください。

#### References
- https://www.oracle.com/security-alerts/cpujul2026.html

### [CVE-2026-64824](https://github.com/home-assistant/core/commit/1e457600f1093c15e1325742d03e2b76498c79c1)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-64824
- 関連キーワード: python, docker
- 影響製品: -
- 公開日: 2026-07-22 01:17:21 JST
- 更新日: 2026-07-22 05:28:41 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Home Assistant Core 2026.7.0未満において、バックアップ復元機能のパストラバーサル脆弱性により、悪意あるtarアーカイブを用いて任意のファイルを書き込める可能性があります。  
- 影響: 攻撃者はroot権限でのリモートコード実行を達成し、Pythonの自動インポートパスやカスタムコンポーネントを上書きできる恐れがあります。  
- 推奨対応: 影響を受けるバージョンから2026.7.0以降へのアップデートを検討し、信頼できないバックアップファイルの復元を避けてください。

#### References
- https://github.com/home-assistant/core/commit/1e457600f1093c15e1325742d03e2b76498c79c1
- https://github.com/home-assistant/core/pull/172252
- https://github.com/home-assistant/core/releases/tag/2026.7.0
- https://www.vulncheck.com/advisories/home-assistant-core-symlink-path-traversal-rce-via-backup-restore
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-78r8-wwqv-r299

### [CVE-2026-47391](https://github.com/MervinPraison/PraisonAI/commit/e0fb8e7dd1ee6759c18ed07f436c21dbd9c20747)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-47391
- 関連キーワード: python, express
- 影響製品: -
- 公開日: 2026-07-22 01:17:11 JST
- 更新日: 2026-07-22 03:59:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PraisonAIの4.6.40未満のバージョンにおいて、認証なしでアクセス可能なA2A JSON-RPCエンドポイントがPythonのeval()を用いた危険なcalculateツールを登録しており、リモートから任意のPythonコード実行が可能です。  
- 影響: 認証なしのリモート攻撃者によるサーバープロセス上での任意コード実行や機密情報漏洩、タスク履歴の不正取得、タスクキャンセルによる整合性の損失が発生する可能性があります。  
- 推奨対応: 公式のA2A例や類似の公開A2A設定を使用している場合は、バージョン4.6.40以降にアップデートし、認証設定やツールの安全性を見直すことを推奨します。

#### References
- https://github.com/MervinPraison/PraisonAI/commit/e0fb8e7dd1ee6759c18ed07f436c21dbd9c20747
- https://github.com/MervinPraison/PraisonAI/pull/1793
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-vg22-4gmj-prxw

### [CVE-2026-47392](https://github.com/MervinPraison/PraisonAI/commit/b0d8f777528f3253a0cfb0a3ef65455da6ae32f6)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-47392
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-22 01:17:12 JST
- 更新日: 2026-07-22 03:59:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PraisonAIのexecute_code()関数において、print.__self__を利用したサンドボックス回避により任意のOSコマンド実行が可能な脆弱性が報告されています。  
- 影響: 悪用されるとホスト上で任意のコマンドが実行され、システムの完全な制御を奪われる恐れがあります。  
- 推奨対応: PraisonAIをバージョン4.6.40以上、praisonaiagentsを1.6.40以上にアップデートし、修正済みのパッチを適用してください。

#### References
- https://github.com/MervinPraison/PraisonAI/commit/b0d8f777528f3253a0cfb0a3ef65455da6ae32f6
- https://github.com/MervinPraison/PraisonAI/pull/1684
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-4mr5-g6f9-cfrh
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-4mr5-g6f9-cfrh

### [CVE-2026-47708](https://github.com/SepineTam/mcp-for-stata/commit/e6f945941ae0c7cf5e74a428e0b3dc82b396382f)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-47708
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-22 06:16:51 JST
- 更新日: 2026-07-22 06:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: MCP-for-Stataの`stata_do` APIおよびCLIの`log_file_name`パラメータに適切なサニタイズがなく、任意のStataコマンド注入が可能な脆弱性が存在します。  
- 影響: 悪意ある入力により任意のコマンド実行が可能となり、システムの制御奪取やデータ破壊のリスクがあります。  
- 推奨対応: バージョン1.17.3以降にアップデートし、`log_file_name`パラメータの適切な検証が行われていることを確認してください。

#### References
- https://github.com/SepineTam/mcp-for-stata/commit/e6f945941ae0c7cf5e74a428e0b3dc82b396382f
- https://github.com/SepineTam/mcp-for-stata/issues/74
- https://github.com/SepineTam/mcp-for-stata/security/advisories/GHSA-4p62-hqp5-g644

### [CVE-2026-46556](https://github.com/flaskbb/flaskbb/commit/e87e585f54bbe36694e91d52ee9b2d2e65dd4ab5)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-46556
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-22 06:16:50 JST
- 更新日: 2026-07-22 06:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: FlaskBBのget_image_info()関数に認証済みユーザーが任意の内部エンドポイントへHTTPリクエストを送信可能なSSRF脆弱性が存在します。  
- 影響: 内部ネットワークのポートスキャンや内部APIの不正呼び出しが行われる恐れがあります。  
- 推奨対応: バージョン2.2.1以降にアップデートして脆弱性を修正してください。

#### References
- https://github.com/flaskbb/flaskbb/commit/e87e585f54bbe36694e91d52ee9b2d2e65dd4ab5
- https://github.com/flaskbb/flaskbb/security/advisories/GHSA-xq32-9g7q-7297

### [CVE-2026-47425](https://github.com/conda/rattler/commit/4f06eca89aa13209774d26dbac077c41b72bac7c)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-47425
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-22 03:17:01 JST
- 更新日: 2026-07-22 03:17:01 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Rattlerライブラリの0.43.2以前のバージョンで、悪意あるnoarch:pythonパッケージが不正なエントリーポイント名を使い、インストール先外にファイルを書き込む可能性があります。  
- 影響: pixiやmamba、rattler-buildなどrattlerを利用する環境で、任意のファイル上書きや実行ファイルの改ざんが発生する恐れがあります。  
- 推奨対応: Rattlerをバージョン0.43.2以降にアップデートし、不正なエントリーポイントの処理が修正された状態で利用してください。

#### References
- https://github.com/conda/rattler/commit/4f06eca89aa13209774d26dbac077c41b72bac7c
- https://github.com/conda/rattler/security/advisories/GHSA-q53q-5r4j-5729

### [CVE-2026-47394](https://github.com/MervinPraison/PraisonAI/commit/b0d8f777528f3253a0cfb0a3ef65455da6ae32f6)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-47394
- 関連キーワード: gin, aws
- 影響製品: -
- 公開日: 2026-07-22 01:17:12 JST
- 更新日: 2026-07-22 03:59:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PraisonAIのバージョン4.6.40以前では、特定のワークフローハンドラに未修正の脆弱性が存在し、認証なしで任意のファイル内容を取得される可能性があります。  
- 影響: 攻撃者がホスト上の任意の読み取り可能なファイル（例：/etc/passwdや秘密鍵）を不正に取得できるリスクがあります。  
- 推奨対応: バージョン4.6.40以降にアップデートし、修正済みのパッチを適用することを推奨します。

#### References
- https://github.com/MervinPraison/PraisonAI/commit/b0d8f777528f3253a0cfb0a3ef65455da6ae32f6
- https://github.com/MervinPraison/PraisonAI/pull/1684
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-9cr9-25q5-8prj
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-9cr9-25q5-8prj

### [CVE-2026-47695](https://github.com/cc-tweaked/CC-Tweaked/security/advisories/GHSA-5jh9-2h63-pw4q)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-47695
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-07-22 06:16:51 JST
- 更新日: 2026-07-22 06:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CC: TweakedのHTTP APIにおいて、IPv6対応サーバーでNAT64プレフィックスを利用した場合にプライベートネットワークへのアクセス制限が回避される脆弱性が存在します。  
- 影響: 攻撃者がLuaコードを実行できる環境で、内部IPv4サービスへの不正アクセスが可能になる恐れがあります。  
- 推奨対応: バージョン1.119.0以降にアップデートし、脆弱性修正を適用してください。

#### References
- https://github.com/cc-tweaked/CC-Tweaked/security/advisories/GHSA-5jh9-2h63-pw4q

### [CVE-2026-15957](https://aws.amazon.com/security/security-bulletins/2026-061-aws/)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-15957
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-07-22 05:16:58 JST
- 更新日: 2026-07-22 05:16:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Smithy-RSのJSON、CBOR、XMLデシリアライザにおける制御されていない再帰処理により、深くネストされたデータを含むリクエストでスタック消耗によるサービス拒否が発生する可能性があります。  
- 影響: AWS SDK for Rustやsmithy-rsで生成されたサーバーやクライアントがリモートからの攻撃によりプロセス異常終了する恐れがあります。  
- 推奨対応: aws-sdk-rustは2026-06-02以降のリリースにアップグレードし、smithy-rsコード生成を利用する場合は2026-06-01以降のリリースで再生成してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-061-aws/
- https://github.com/awslabs/aws-sdk-rust/releases/tag/release-2026-06-02
- https://github.com/smithy-lang/smithy-rs/security/advisories/GHSA-4f2p-7j38-4xrg

### [CVE-2026-55084](https://github.com/dhis2/dhis2-core/pull/24162)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-55084
- 関連キーワード: express, postgresql
- 影響製品: -
- 公開日: 2026-07-22 04:17:11 JST
- 更新日: 2026-07-22 05:17:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: DHIS2のSqlView APIの`filter`パラメータにSQLインジェクションの脆弱性が存在し、認証ユーザーが任意のSQLを実行可能です。  
- 影響: 攻撃者はエラーベースのSQLインジェクションを利用してデータベースの任意の内容を抽出できる可能性があります。  
- 推奨対応: 影響を受けるバージョンから、修正済みの2.40.11.1以降や2.41.8.2以降などのパッチ適用済みバージョンへアップデートしてください。

#### References
- https://github.com/dhis2/dhis2-core/pull/24162
- https://github.com/dhis2/dhis2-core/security/advisories/GHSA-pwmg-mvjw-4m23

### [CVE-2016-20096](https://packetstorm.news/files/id/137159)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2016-20096
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-22 04:17:07 JST
- 更新日: 2026-07-22 04:17:07 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinknatのVOS3000およびVOS2009（バージョン2.1.2.0まで）に認証なしでSQLインジェクションが可能な脆弱性が存在します。  
- 影響: 攻撃者はログインフォームのnameパラメータを悪用し、任意のSQLコマンドを実行して平文の認証情報やデータベース内容を取得できる可能性があります。  
- 推奨対応: 影響を受ける製品のバージョンアップやパッチ適用、入力値の適切な検証・サニタイズを実施してください。

#### References
- https://packetstorm.news/files/id/137159
- https://web.archive.org/web/20160601102456/http://www.wooyun.org/bugs/wooyun-2010-0145458
- https://www.linknat.com/
- https://www.vulncheck.com/advisories/linknat-vos3000-vos2009-sql-injection-via-login-jsp

### [CVE-2026-65048](https://wordpress.org/plugins/ninja-forms/)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-65048
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-22 00:16:38 JST
- 更新日: 2026-07-22 03:55:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Ninja Formsプラグイン（バージョン3.10.4～3.14.9）に、認証なしで悪意あるスクリプトを管理者画面で実行可能な保存型クロスサイトスクリプティング脆弱性があります。  
- 影響: 攻撃者は管理者のセッション情報を盗んだり、管理者アカウントの作成や悪意あるプラグインのインストール、サイト内容の改ざんが可能になる恐れがあります。  
- 推奨対応: 公式の修正パッチ適用やプラグインのアップデートを速やかに実施し、不審なフォーム送信の監視を強化してください。

#### References
- https://wordpress.org/plugins/ninja-forms/
- https://wordpress.org/plugins/ninja-forms/changelog/
- https://www.vulncheck.com/advisories/ninja-forms-unauthenticated-stored-cross-site-scripting-via-repeatable-fieldset-submission-index

### [CVE-2026-65049](https://wordpress.org/plugins/ninja-forms/)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-65049
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-22 00:16:38 JST
- 更新日: 2026-07-22 03:55:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WordPressのNinja Formsプラグイン3.14.8以前に、サブサイト管理者がネットワーク全体のNinja Formsデータを削除できる認可不備の脆弱性があります。  
- 影響: サブサイト管理者権限のみで、全サブサイトのフォームデータが削除される可能性があり、重大なデータ損失を引き起こします。  
- 推奨対応: プラグインの最新版への更新を検討し、マルチサイト環境の権限設定と移行設定を見直すことを推奨します。

#### References
- https://wordpress.org/plugins/ninja-forms/
- https://wordpress.org/plugins/ninja-forms/changelog/
- https://www.vulncheck.com/advisories/ninja-forms-cross-site-network-wide-data-deletion-on-wordpress-multisite-via-nf-delete-all-data-ajax-action

### [CVE-2026-47688](https://github.com/FOGProject/fogproject/security/advisories/GHSA-95pr-mcrf-x2qg)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-47688
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-22 06:16:50 JST
- 更新日: 2026-07-22 06:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: FOGの特定バージョンにおいて、認証なしでHTTP GETリクエストを送ることでAES暗号化資格情報の消去や電源管理タスクの削除が可能な脆弱性が存在します。  
- 影響: 攻撃者がリモートからホストの暗号化情報を消去し、電源管理スケジュールを削除できるため、システムの機密性や可用性が損なわれる恐れがあります。  
- 推奨対応: FOGをバージョン1.5.10.1832または1.6.0-beta.2313以降にアップデートし、該当の脆弱性を修正してください。

#### References
- https://github.com/FOGProject/fogproject/security/advisories/GHSA-95pr-mcrf-x2qg

# Backend CVE Summary (2026-07-18)

## Overview

- 取得日時: 2026-07-18 08:02:25 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 18
- Critical: 2
- High: 9
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-42168](https://github.com/abhishek-ram/django-pyas2)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-42168
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-07-18 05:17:16 JST
- 更新日: 2026-07-18 05:17:16 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: django-pyas2 1.2.3以前のバージョンにおいて、Partnerモデルのcmd_receiveおよびcmd_sendフィールドを通じてOSコマンドインジェクションの脆弱性が存在します。  
- 影響: 認証済みの管理者ユーザーがAS2メッセージの送受信時に任意のOSコマンドを実行できる可能性があります。  
- 推奨対応: 最新バージョンへのアップデートまたは該当フィールドの入力値検証・サニタイズを実施してください。

#### References
- https://github.com/abhishek-ram/django-pyas2
- https://github.com/abhishek-ram/django-pyas2/releases/tag/v1.2.3
- https://github.com/m4ty-m/vulnerability-research/tree/main/CVE-2026-42168

### [CVE-2026-9586](https://labs.sra.io/posts/switchvox/)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-9586
- 関連キーワード: go, gin, postgresql
- 影響製品: -
- 公開日: 2026-07-18 02:17:18 JST
- 更新日: 2026-07-18 03:04:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Sangoma Switchvox SMB Edition 8.3の/paエンドポイントにおいて、認証なしでSQLインジェクションが可能な脆弱性が存在します。  
- 影響: 攻撃者は任意のSQL文を実行でき、データベース操作やリモートコード実行のリスクがあります。  
- 推奨対応: 公式のセキュリティアップデート適用や、入力値の適切なサニタイズ・パラメータ化を行うことが推奨されます。

#### References
- https://labs.sra.io/posts/switchvox/
- https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026

### [CVE-2026-50163](https://github.com/oras-project/oras-go/commit/c463c654ab3ef34422c1764cd619806cebf20451)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-50163
- 関連キーワード: go, gin, aws
- 影響製品: -
- 公開日: 2026-07-18 05:17:23 JST
- 更新日: 2026-07-18 05:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: oras-goライブラリの2.6.2未満のバージョンで、ハードリンクの検証処理に不備があり、悪意あるリンクによりファイルの露出や改ざんが発生する可能性があります。  
- 影響: .envや.git/config、AWS認証情報、SSH設定ファイルなどの機密ファイルが不正にアクセスまたは改ざんされるリスクがあります。  
- 推奨対応: oras-goをバージョン2.6.2以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/oras-project/oras-go/commit/c463c654ab3ef34422c1764cd619806cebf20451
- https://github.com/oras-project/oras-go/pull/1232
- https://github.com/oras-project/oras-go/releases/tag/v2.6.2
- https://github.com/oras-project/oras-go/security/advisories/GHSA-fxhp-mv3v-67qp

### [CVE-2026-12715](https://docs.cloud.google.com/support/bulletins#gcp-2026-043)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-12715
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-18 01:17:13 JST
- 更新日: 2026-07-18 03:08:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Google Cloud Firebase Studioの2026年4月15日以前のバージョンにおいて、認可チェックの欠如により攻撃者が他ユーザーのソースコードを不正にダウンロード可能な脆弱性。  
- 影響: 攻撃者が不正なGCS URL署名リクエストを通じて機密データにアクセスできる可能性がある。  
- 推奨対応: 既に2026年4月15日に修正済みのため、最新バージョンへの更新を確認し、必要に応じて適用すること。

#### References
- https://docs.cloud.google.com/support/bulletins#gcp-2026-043

### [CVE-2026-49852](https://github.com/authlib/joserfc/commit/86d00910b2b2d2d07503fee9b572906daefab7f1)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-49852
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-07-18 05:17:23 JST
- 更新日: 2026-07-18 05:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: joserfcライブラリの1.6.8未満のバージョンで、空文字列やNoneの検証キーを使うと、攻撃者が偽造したHMAC署名付きトークンを受け入れてしまう脆弱性が存在します。  
- 影響: 不正なトークンが認証を通過する可能性があり、認証回避や権限昇格のリスクがあります。  
- 推奨対応: joserfcをバージョン1.6.8以降にアップデートし、検証キーの適切な管理を行ってください。

#### References
- https://github.com/authlib/joserfc/commit/86d00910b2b2d2d07503fee9b572906daefab7f1
- https://github.com/authlib/joserfc/releases/tag/1.6.8
- https://github.com/authlib/joserfc/security/advisories/GHSA-gg9x-qcx2-xmrh

### [CVE-2026-50151](https://github.com/oras-project/oras-go/commit/4683c46ef078091544f5f55fd25102f002806991)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-50151
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-18 05:17:23 JST
- 更新日: 2026-07-18 05:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: oras-go is a Go library for managing OCI artifacts. Prior to 2.6.1, registry/remote/repository.go in blobStore.completePushAfterInitialPost follows a registry-controlled Location header during monolithic blob upload and reuses the Authorization header from the initial POST request for the subsequent PUT request, allowi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/oras-project/oras-go/commit/4683c46ef078091544f5f55fd25102f002806991
- https://github.com/oras-project/oras-go/pull/1152
- https://github.com/oras-project/oras-go/releases/tag/v2.6.1
- https://github.com/oras-project/oras-go/security/advisories/GHSA-jxpm-75mh-9fp7

### [CVE-2026-63094](https://github.com/SigNoz/signoz/issues/11746)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-63094
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-18 00:16:47 JST
- 更新日: 2026-07-18 03:28:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SigNoz through 0.133.0 contains an open redirect vulnerability in the SSO authentication flow that allows unauthenticated attackers to steal session tokens from any user on instances configured with Google OAuth, SAML, or OIDC. Attackers can call the unauthenticated sessions context endpoint with a ref parameter pointi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/SigNoz/signoz/issues/11746
- https://github.com/SigNoz/signoz/pull/11844
- https://www.vulncheck.com/advisories/signoz-sso-oauth-state-manipulation-session-token-theft

### [CVE-2026-50197](https://github.com/zalando/skipper/commit/3152f3b0bb52ca89c3564be42434db0a2a1cea23)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-50197
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-18 05:17:24 JST
- 更新日: 2026-07-18 05:17:24 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SkipperのOpenPolicyAgent統合において、特定のHTTPリクエストでリクエストボディの検査がバイパスされる脆弱性が存在します。  
- 影響: 攻撃者が制御するリクエストボディが検査されず、ポリシー違反のリクエストが通過する可能性があります。  
- 推奨対応: バージョン0.26.10以降にアップデートし、脆弱性を修正してください。

#### References
- https://github.com/zalando/skipper/commit/3152f3b0bb52ca89c3564be42434db0a2a1cea23
- https://github.com/zalando/skipper/pull/4041
- https://github.com/zalando/skipper/releases/tag/v0.26.10
- https://github.com/zalando/skipper/security/advisories/GHSA-659f-rgp5-w4wf

### [CVE-2026-50274](https://github.com/DataDog/dd-trace-go/commit/192712ba0291b2e89166259111ebb5e90c8f52df)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-50274
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-18 06:17:07 JST
- 更新日: 2026-07-18 06:17:07 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: DatadogのGo用トレーシングライブラリdd-trace-go（2.8.1未満）で、W3Cバゲージヘッダーのサイズ制限が適用されず、リモートから大量のデータを送信されるとCPUやメモリが過剰消費される脆弱性。  
- 影響: リモートの認証されていない攻撃者によるサービス拒否（DoS）攻撃が可能になる可能性がある。  
- 推奨対応: dd-trace-goをバージョン2.8.1以降にアップデートし、バゲージヘッダーのサイズ制限が適用されるようにすること。

#### References
- https://github.com/DataDog/dd-trace-go/commit/192712ba0291b2e89166259111ebb5e90c8f52df
- https://github.com/DataDog/dd-trace-go/pull/4720
- https://github.com/DataDog/dd-trace-go/releases/tag/v2.8.1
- https://github.com/DataDog/dd-trace-go/security/advisories/GHSA-74j5-xf3v-crq8

### [CVE-2026-53712](https://github.com/ongres/scram/releases/tag/3.3)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-53712
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-18 04:17:16 JST
- 更新日: 2026-07-18 05:17:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SCRAM認証機構のcom.ongres.scramライブラリにおいて、TLSの中間者攻撃によりSCRAM-SHA-256-PLUSからSCRAM-SHA-256へのダウングレードが可能な脆弱性が存在します。  
- 影響: TLS接続のチャンネルバインディングが無効化され、認証の安全性が低下する恐れがあります。  
- 推奨対応: バージョン3.3以降にアップデートし、修正済みのライブラリを使用することを推奨します。

#### References
- https://github.com/ongres/scram/releases/tag/3.3
- https://github.com/ongres/scram/security/advisories/GHSA-p9jg-fcr6-3mhf

### [CVE-2026-9587](https://github.com/sangoma/security-switchvox/security/advisories/GHSA-mhp4-x83p-phh2)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-9587
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-18 02:17:18 JST
- 更新日: 2026-07-18 03:04:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Sangoma Switchvox SMB Edition 8.3のplay_file機能において、認証済みユーザーがsound_pathパラメータを通じて任意のファイルパスを指定できるローカルファイルインクルージョンの脆弱性が存在します。  
- 影響: 認証済み攻撃者が本来アクセスできないファイルを読み取る可能性があり、情報漏洩のリスクがあります。  
- 推奨対応: 最新のパッチ適用やベンダーからの修正情報を確認し、適切なアクセス制御と入力検証の強化を行うことを推奨します。

#### References
- https://github.com/sangoma/security-switchvox/security/advisories/GHSA-mhp4-x83p-phh2
- https://labs.sra.io/posts/switchvox/

### [CVE-2026-48978](https://github.com/oras-project/oras-go/commit/7a9f4b0b9558821b0422152ebe21ae56930fe764)

> **Backend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-48978
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-18 05:17:21 JST
- 更新日: 2026-07-18 05:17:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: oras-goライブラリのauth.Clientが、レルムURLの検証を行わずに内部ネットワークへのSSRFを引き起こす可能性があります。  
- 影響: 悪意あるレジストリにより内部ネットワークへの不正アクセスやHTTPSからHTTPへのダウングレード攻撃が発生する恐れがあります。  
- 推奨対応: バージョン2.6.1以降にアップデートし、auth.Clientの脆弱性を修正してください。

#### References
- https://github.com/oras-project/oras-go/commit/7a9f4b0b9558821b0422152ebe21ae56930fe764
- https://github.com/oras-project/oras-go/releases/tag/v2.6.1
- https://github.com/oras-project/oras-go/security/advisories/GHSA-xf85-363p-868w

### [CVE-2026-50162](https://github.com/oras-project/oras-go/commit/cc323e564d90c6b5b4bdd71d3c8d2ee2713b37e5)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-50162
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-18 05:17:23 JST
- 更新日: 2026-07-18 05:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: oras-goライブラリのresolveWritePath()関数で、シンボリックリンクのトラバーサルを考慮せずにファイルパスを検証する問題があり、悪意ある入力により作業ディレクトリ外にファイルが作成される可能性があります。  
- 影響: 攻撃者が任意のファイルを作業ディレクトリ外に書き込めるため、ファイルシステムの整合性やセキュリティに影響を与える恐れがあります。  
- 推奨対応: oras-goをバージョン2.6.1以降にアップデートし、シンボリックリンクのトラバーサル問題が修正されたバージョンを使用してください。

#### References
- https://github.com/oras-project/oras-go/commit/cc323e564d90c6b5b4bdd71d3c8d2ee2713b37e5
- https://github.com/oras-project/oras-go/releases/tag/v2.6.1
- https://github.com/oras-project/oras-go/security/advisories/GHSA-8xwf-rjm4-xvhv

### [CVE-2026-63308](https://github.com/helm/helm/commit/ba6c9a29efa7bf9198dad6a5ec12b4fb30c96017)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-63308
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-18 02:17:17 JST
- 更新日: 2026-07-18 03:28:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Helm 4.2.3以前のFiles.Linesテンプレートヘルパーに、ゼロ長のバイトスライスを含むチャートファイルでインデックス範囲外のパニックを引き起こすDoS脆弱性があります。  
- 影響: 攻撃者は空ファイルをHelmチャートに含めることで、テンプレートのレンダリングやインストール、アップグレード、lint、SDKのレンダリング処理を失敗させる可能性があります。  
- 推奨対応: 修正コミットba6c9a2以降のバージョンにアップデートし、チャートファイルに空ファイルを含めないよう注意してください。

#### References
- https://github.com/helm/helm/commit/ba6c9a29efa7bf9198dad6a5ec12b4fb30c96017
- https://github.com/helm/helm/issues/32279
- https://github.com/helm/helm/pull/32290
- https://www.vulncheck.com/advisories/chat2db-insecure-direct-object-reference-via-get-api-connection-datasource

### [CVE-2026-16017](https://github.com/mosaxiv/clawlet/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-16017
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-18 00:16:46 JST
- 更新日: 2026-07-18 03:17:14 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: mosaxiv clawlet 0.2.10以前のcron Chat Toolのtools/tool_cron.go内のlist/remove関数に認可欠如の脆弱性が存在します。  
- 影響: リモートからの攻撃が可能で、認可されていない操作が実行される恐れがあります。  
- 推奨対応: 現時点で修正予定がないため、アクセス制御の強化や監視の強化を検討してください。

#### References
- https://github.com/mosaxiv/clawlet/
- https://github.com/mosaxiv/clawlet/issues/17
- https://vuldb.com/cve/CVE-2026-16017
- https://vuldb.com/submit/856824
- https://vuldb.com/vuln/379759

### [CVE-2026-49834](https://github.com/sigstore/sigstore-go/commit/dbb07e62623edd5b175fb9dd5a41dcb85a159207)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-49834
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-18 05:17:21 JST
- 更新日: 2026-07-18 05:17:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: sigstore-goライブラリの1.2.0以前のバージョンで、複数の透明性ログを用いた検証時に単一のログの証明で閾値を満たしてしまう問題が存在します。  
- 影響: 単一の透明性ログの侵害により、マルチログポリシーが回避される可能性があります。  
- 推奨対応: sigstore-goをバージョン1.2.0以降にアップデートしてください。

#### References
- https://github.com/sigstore/sigstore-go/commit/dbb07e62623edd5b175fb9dd5a41dcb85a159207
- https://github.com/sigstore/sigstore-go/pull/633
- https://github.com/sigstore/sigstore-go/releases/tag/v1.2.0
- https://github.com/sigstore/sigstore-go/security/advisories/GHSA-9vcr-p3rj-q5q6

### [CVE-2026-63097](https://github.com/geo-chen/oss/blob/main/dendrite.md#finding-3-context-returns-current-room-state-to-non-members-and-left-users-history-visibility-bypass)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-63097
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-18 01:17:16 JST
- 更新日: 2026-07-18 03:04:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dendrite 0.13.8以前のsyncapiの/contextエンドポイントにおいて、不適切なアクセス制御により、退室済みユーザーが部屋の状態イベントにアクセス可能な脆弱性が存在します。  
- 影響: 認証済みのローカルユーザーが退室後も部屋の現在の状態情報を不正に取得できる可能性があります。  
- 推奨対応: 最新バージョンへのアップデートやアクセス制御の見直しを行い、退室ユーザーの状態情報アクセスを防止してください。

#### References
- https://github.com/geo-chen/oss/blob/main/dendrite.md#finding-3-context-returns-current-room-state-to-non-members-and-left-users-history-visibility-bypass
- https://www.vulncheck.com/advisories/dendrite-syncapi-context-endpoint-post-leave-state-exposure

### [CVE-2026-9135](https://www.ibm.com/support/pages/node/7278920)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-9135
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-07-18 04:17:19 JST
- 更新日: 2026-07-18 04:17:19 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: IBM Langflow OSS 1.0.0～1.10.0のPoliciesコンポーネントにおいて、ToolGuard統合部分の検証不足によりコードインジェクションの脆弱性が存在します。  
- 影響: 認証済みユーザーが任意のPythonコードをサーバー側で実行可能となり、クロステナント攻撃による権限昇格も懸念されます。  
- 推奨対応: 公式の修正パッチ適用やバージョンアップを行い、Flowのアクセス制御設定を見直すことが推奨されます。

#### References
- https://www.ibm.com/support/pages/node/7278920

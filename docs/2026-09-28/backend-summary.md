# Backend CVE Summary (2026-09-28)

## Overview

- 取得日時: 2026-09-28 09:37:04 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 17
- Critical: 2
- High: 6
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-101090](https://github.com/nezhahq/nezha/security/advisories/GHSA-rf68-8gjr-36q7)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-101090
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-28 06:17:03 JST
- 更新日: 2026-09-28 06:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NezhaのOAuth2リダイレクト処理において、dashboard_host未設定時にリクエストのHostヘッダーを検証なくredirect_uriに反映してしまう再発脆弱性。
- 影響: 偽造されたHostヘッダーでOAuth2ログインを誘発されると、認可コードが攻撃者のサーバーへ送信され、アカウントを乗っ取られる可能性があります。
- 推奨対応: dashboard_hostを適切に設定するか、修正版が提供され次第速やかにアップデートしてください。

#### References
- https://github.com/nezhahq/nezha/security/advisories/GHSA-rf68-8gjr-36q7
- https://www.vulncheck.com/advisories/nezha-through-2.2.3-host-header-injection-via-oauth2-redirect-uri

### [CVE-2026-101042](https://github.com/parse-community/parse-server/security/advisories/GHSA-mr43-w6c2-mvjq)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-101042
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-28 02:16:55 JST
- 更新日: 2026-09-28 02:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Parse Serverのコードベース認証アダプターにおいて、ログイン時の認可コード検証が不十分な脆弱性。
- 影響: 攻撃者が未検証の外部プロバイダーIDを任意のアカウントに紐付けたり、未連携ユーザーのアカウントを事前に乗っ取ったりする可能性があります。
- 推奨対応: Parse Serverを修正済みバージョン（8.6.91以降、または9.10.1-alpha.10以降）へ更新してください。

#### References
- https://github.com/parse-community/parse-server/security/advisories/GHSA-mr43-w6c2-mvjq
- https://www.vulncheck.com/advisories/parse-server-9.0.0-authentication-bypass-via-unverified-provider-identity

### [CVE-2026-101085](https://github.com/nezhahq/nezha/security/advisories/GHSA-2qc6-x993-hjq9)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-101085
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-28 06:17:02 JST
- 更新日: 2026-09-28 06:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nezhaにおけるアラートルールの種類および期間の境界値検証不足の脆弱性。
- 影響: 認証済みの非管理者ユーザーが不正なアラートルールを送信することでダッシュボードプロセスをクラッシュさせ、再起動後も永続的なDoS（全監視機能の停止）を引き起こす可能性があります。
- 推奨対応: Nezhaをバージョン2.3.8以降に更新してください。

#### References
- https://github.com/nezhahq/nezha/security/advisories/GHSA-2qc6-x993-hjq9
- https://www.vulncheck.com/advisories/nezha-before-2.3.8-denial-of-service-via-alert-rule

### [CVE-2026-101088](https://github.com/nezhahq/nezha/security/advisories/GHSA-jx78-55p5-rwv5)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-101088
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-28 06:17:02 JST
- 更新日: 2026-09-28 06:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nezhaのサービス監視ワーカーにおけるNullポインター参照解除（DoS）の脆弱性（以前の修正不備に起因）。
- 影響: エージェントを所有する認証済みメンバーユーザーがサーバーの並行削除を行うことで競合状態が発生し、インスタンス全体がクラッシュ（DoS）する可能性があります。
- 推奨対応: Nezhaをバージョン2.3.1以降に更新してください。

#### References
- https://github.com/nezhahq/nezha/security/advisories/GHSA-jx78-55p5-rwv5
- https://www.vulncheck.com/advisories/nezha-before-2.3.1-denial-of-service-via-concurrent-server-delete

### [CVE-2026-100877](https://github.com/rmsbpro/Advisory/blob/main/registrationform-stored-xss.md)

> **Backend** / **MEDIUM** / CVSS: **5.0** / KEV: **no**

- タイトル: CVE-2026-100877
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-28 06:17:00 JST
- 更新日: 2026-09-28 06:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: mathurvishal CloudClassroom-PHP-Projectのregistrationform.phpにおけるクロスサイトスクリプティング（XSS）の脆弱性。
- 影響: FName、LName、Addrsパラメータの入力を操作されることで、リモートから悪意のあるスクリプトを実行される可能性があります。
- 推奨対応: 入力値の検証および出力時の適切なエスケープ処理を実装するか、利用の継続を再検討してください。

#### References
- https://github.com/rmsbpro/Advisory/blob/main/registrationform-stored-xss.md
- https://vuldb.com/cve/CVE-2026-100877
- https://vuldb.com/submit/915444
- https://vuldb.com/vuln/410807
- https://vuldb.com/vuln/410807/cti

### [CVE-2026-101087](https://github.com/nezhahq/nezha/commit/d1fcde8e)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-101087
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-28 06:17:02 JST
- 更新日: 2026-09-28 06:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NezhaのWebhook URL検証処理において、特定のIPv6遷移プレフィックス（6to4等）のチェックが漏れている脆弱性。
- 影響: 認証済みユーザーがWebhookを設定することで、本来アクセス制限されている特定のIPv6エンドポイントへリクエストが発生する可能性があります。
- 推奨対応: Nezhaを修正済みのバージョン2.3.3以降に更新してください。

#### References
- https://github.com/nezhahq/nezha/commit/d1fcde8e
- https://github.com/nezhahq/nezha/security/advisories/GHSA-jr2j-7hvh-h4q9
- https://www.vulncheck.com/advisories/nezha-2.0.10-through-2.3.2-ssrf-denylist-bypass-ipv6

### [CVE-2026-96283](https://access.redhat.com/security/cve/CVE-2026-96283)

> **Backend** / **LOW** / CVSS: **3.3** / KEV: **no**

- タイトル: CVE-2026-96283
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-28 07:17:06 JST
- 更新日: 2026-09-28 08:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FlatpakのCancelPullにおいて、他ユーザーのプル処理取り消しリクエストに対する処理の不備。
- 影響: 他ユーザーのプル処理を呼び出すと内部追跡から削除されてしまい、本来の所有者が該当するプル処理を停止できなくなる可能性があります。
- 推奨対応: Flatpakパッケージの修正版が提供され次第、アップデートを適用してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-96283
- https://bugzilla.redhat.com/show_bug.cgi?id=2539424
- https://github.com/flatpak/flatpak/security/advisories/GHSA-89xm-3m96-w3jg

### [CVE-2026-101058](https://github.com/universal-tool-calling-protocol/python-utcp/security/advisories/GHSA-8vxx-v7r9-948g)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-101058
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-09-28 03:16:31 JST
- 更新日: 2026-09-28 03:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: python-utcp (utcp-http) 1.1.12 未満において、外部から取得したUTCPマニュアル内のツールURLがループバックアドレス（127.0.0.1）を指しているか正しく検証しない問題が存在します。
- 影響: 攻撃者が作成したマニュアルを介して、被害者環境のローカル限定サービスへリクエストを送信させられ、その応答を取得される（SSRF）可能性があります。
- 推奨対応: utcp-http を 1.1.12 以降の修正済みバージョンへ更新してください。

#### References
- https://github.com/universal-tool-calling-protocol/python-utcp/security/advisories/GHSA-8vxx-v7r9-948g
- https://www.vulncheck.com/advisories/python-utcp-before-1.1.12-ssrf-via-remote-http-manual

### [CVE-2026-101060](https://github.com/universal-tool-calling-protocol/python-utcp/security/advisories/GHSA-9qhg-99ww-9mqc)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-101060
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-28 03:16:32 JST
- 更新日: 2026-09-28 03:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: python-utcp 1.1.4 未満の HttpCommunicationProtocol.call_tool において、初回URL検証後にHTTPリダイレクト先の再検証を行わずに接続する脆弱性が存在します。
- 影響: 攻撃者が制御するエンドポイントからの302リダイレクトにより、内部サービスやクラウドメタデータエンドポイントへアクセスされ、応答を取得される可能性があります。
- 推奨対応: python-utcp を 1.1.4 以降の修正済みバージョンへ更新してください。

#### References
- https://github.com/universal-tool-calling-protocol/python-utcp/security/advisories/GHSA-9qhg-99ww-9mqc
- https://www.vulncheck.com/advisories/python-utcp-before-1.1.4-ssrf-via-unvalidated-http-redirects

### [CVE-2026-101057](https://github.com/universal-tool-calling-protocol/python-utcp/security/advisories/GHSA-qwr9-cj2c-v3fv)

> **Backend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-101057
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-09-28 03:16:31 JST
- 更新日: 2026-09-28 03:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: utcp-mcp 1.1.2 以前において、設定されたMCPサーバーのURLに対して安全な接続検証（ensure_secure_url）が適用されない問題が存在します。
- 影響: 暗号化されていないHTTP接続が許可され、通信の盗聴や内部ホストへの平文アクセスにつながる可能性があります。
- 推奨対応: utcp-mcp を修正が適用されたバージョン（1.1.3以降など）へ更新してください。

#### References
- https://github.com/universal-tool-calling-protocol/python-utcp/security/advisories/GHSA-qwr9-cj2c-v3fv
- https://www.vulncheck.com/advisories/utcp-mcp-before-1.1.3-ssrf-via-unvalidated-mcp-server-url

### [CVE-2026-101065](https://github.com/obot-platform/obot/security/advisories/GHSA-jj4w-pfgv-4mrm)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-101065
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-09-28 06:17:02 JST
- 更新日: 2026-09-28 06:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Obot（コミットd7e6970以前）のドキュメントに記載されたDocker起動コマンドにより、認証が無効化された状態で外部公開（0.0.0.0:8080）される問題が存在します。
- 影響: 未認証の第三者に管理者権限でのアクセスを許し、マウントされたDockerソケットを介してホスト環境全体の制御を奪取される可能性があります。
- 推奨対応: 環境変数 OBOT_SERVER_ENABLE_AUTHENTICATION を有効にして起動し、最新のドキュメントに従って設定を見直してください。

#### References
- https://github.com/obot-platform/obot/security/advisories/GHSA-jj4w-pfgv-4mrm
- https://www.vulncheck.com/advisories/obot-quickstart-docker-deployment-unauthenticated-admin-access

### [CVE-2026-88774](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096&articleTitle=Citrix_NetScaler_ADC_and_Citrix_NetScaler_Gateway_Security_Bulletin_for_CVE_2026_88771_CVE_2026_88772_CVE_2026_88773_CVE_2026_88774_CVE_2026_88775_CVE_2026_88776_CVE_2026_88777_and_CVE_2026_88778)

> **Backend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-88774
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-09-28 02:16:56 JST
- 更新日: 2026-09-28 02:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Citrix NetScaler ADC および NetScaler Gateway において、HTTP URLベースの式の使用における不適切な処理により、機能ポリシーが不全となる問題が存在します。
- 影響: 攻撃者によって機能ポリシー（Feature Policy）をバイパスされる可能性があります。
- 推奨対応: Citrixが提供する修正済みファームウェア（14.1-73.37、13.1-64.23など以降）へ更新してください。

#### References
- https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096&articleTitle=Citrix_NetScaler_ADC_and_Citrix_NetScaler_Gateway_Security_Bulletin_for_CVE_2026_88771_CVE_2026_88772_CVE_2026_88773_CVE_2026_88774_CVE_2026_88775_CVE_2026_88776_CVE_2026_88777_and_CVE_2026_88778

### [CVE-2026-96280](https://access.redhat.com/security/cve/CVE-2026-96280)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-96280
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-28 06:17:04 JST
- 更新日: 2026-09-28 06:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OCIデルタストリームのパーサーにおいて、64ビットのサイズ情報を32ビット型の関数へ渡す型キャスト不備があり、メモリ割り当て不足が発生する問題が存在します。
- 影響: 32ビットシステム上で悪意のあるOCIレジストリからFlatpakの更新を行う際、ヒープバッファオーバーフローが発生し、任意コードを実行される可能性があります。
- 推奨対応: 関連ライブラリやFlatpakを修正済みバージョンへアップデートしてください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-96280
- https://bugzilla.redhat.com/show_bug.cgi?id=2539419
- https://github.com/flatpak/flatpak/security/advisories/GHSA-jr92-2v97-wgvc

### [CVE-2026-101046](https://github.com/fleetdm/fleet/security/advisories/GHSA-rxhg-vcww-2mpw)

> **Backend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-101046
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-28 03:16:31 JST
- 更新日: 2026-09-28 03:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Fleet 4.89.0 未満のアクティビティ一覧APIにおいて、ORDER BY句に渡されるソートキーの検証不足によるSQLインジェクション脆弱性が存在します。
- 影響: 認証済みの読み取り権限を持つユーザーにより、通常レスポンスに含まれないテーブル列のデータがソート順序を通じて推測・閲覧される可能性があります。
- 推奨対応: Fleet を 4.89.0 以降のバージョンへアップデートしてください。

#### References
- https://github.com/fleetdm/fleet/security/advisories/GHSA-rxhg-vcww-2mpw
- https://www.vulncheck.com/advisories/fleet-before-4.89.0-sql-injection-via-order-by-activity-endpoints

### [CVE-2026-100876](https://github.com/rmsbpro/Advisory/blob/main/broken-role-segregation.md)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-100876
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-28 05:16:48 JST
- 更新日: 2026-09-28 05:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CloudClassroom-PHP-Project（コミット5dadec0以前）の loginlinkstudent.php において、umail パラメーターの処理における認証欠如の脆弱性が存在します。
- 影響: 遠隔の攻撃者により認証を回避され、不正アクセスが行われる可能性があります。
- 推奨対応: ベンダーによる修正プログラムが提供されていないため、該当機能の使用停止やアクセス制御の実施を検討してください。

#### References
- https://github.com/rmsbpro/Advisory/blob/main/broken-role-segregation.md
- https://vuldb.com/cve/CVE-2026-100876
- https://vuldb.com/submit/915442
- https://vuldb.com/vuln/410806
- https://vuldb.com/vuln/410806/cti

### [CVE-2026-101041](https://github.com/vulnerability-lookup/vulnerability-lookup/commit/5462bab62d76df852619e01eb67da36c023c8c40)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-101041
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-28 00:16:27 JST
- 更新日: 2026-09-28 00:16:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: vulnerability-lookup Webアプリケーションのアカウント復旧機能において、リカバリトークンの確認と消費が別々に行われることによるTOCTOU競合状態が存在します。
- 影響: 有効な復旧トークンを持つ攻撃者が並行リクエストを送信することで、正当なユーザーのアカウントパスワードを意図した値へ上書きできる可能性があります。
- 推奨対応: vulnerability-lookup を最新バージョンへアップデートしてください。

#### References
- https://github.com/vulnerability-lookup/vulnerability-lookup/commit/5462bab62d76df852619e01eb67da36c023c8c40
- https://github.com/vulnerability-lookup/vulnerability-lookup/commit/ad6f22882975516adf193a1a920aaa54025c71d4

### [CVE-2026-96281](https://access.redhat.com/security/cve/CVE-2026-96281)

> **Backend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-96281
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-28 06:17:04 JST
- 更新日: 2026-09-28 07:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: マルチユーザー環境のFlatpakにおいて、非特権ユーザーが RemoveLocalRef メソッドを実行してアプリのリモート参照を削除できる不備が存在します。
- 影響: ダウングレード防止チェックが回避され、システム全体のアプリが過去の脆弱なバージョンへダウングレードさせられる可能性があります。
- 推奨対応: Flatpak を修正済みバージョンへアップデートしてください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-96281
- https://bugzilla.redhat.com/show_bug.cgi?id=2539421
- https://github.com/flatpak/flatpak/security/advisories/GHSA-q4gr-vc25-57m5

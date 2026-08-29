# Backend CVE Summary (2026-08-29)

## Overview

- 取得日時: 2026-08-29 12:41:04 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 21
- Critical: 4
- High: 8
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-55068](https://github.com/free5gc/free5gc/issues/1056)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-55068
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-08-29 05:18:24 JST
- 更新日: 2026-08-29 05:18:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: free5GCのNRFにおけるRegisterNFInstanceハンドラーが、NF Profileの妥当性検証（UUID形式や必須項目等）を適切に実施していない。
- 影響: 不正なネットワーク機能プロファイルが保存され、制御プレーン信号のリダイレクト、認証情報の漏洩、サービス拒否（DoS）が発生する恐れがある。
- 推奨対応: free5GCをバージョン4.2.3以降に更新する。

#### References
- https://github.com/free5gc/free5gc/issues/1056
- https://github.com/free5gc/free5gc/releases/tag/v4.2.3
- https://github.com/free5gc/free5gc/security/advisories/GHSA-x8mj-6p3q-g5pp
- https://github.com/free5gc/nrf/commit/bda0cf75be5556bb4c758c8b34710f3fe6bbe3ea
- https://github.com/free5gc/nrf/commit/fcd3cfaa27cc4dc17172ee0c4c3e0a3a696297c6

### [CVE-2026-54754](https://github.com/klever-io/klever-go/commit/8bcc600b0ac88070740c63c7ce1c8a968dd85251)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-54754
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:18:17 JST
- 更新日: 2026-08-29 05:18:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Klever-Go（1.7.19未満）のマーケットプレイス決済処理における紹介・ロイヤリティ比率の計算不備。
- 影響: 購入額を超える手数料計算により裏付けのない通貨が生成され、トークン供給の整合性が損なわれる可能性がある。
- 推奨対応: Klever-Go 1.7.19 以降へアップデートしてください。

#### References
- https://github.com/klever-io/klever-go/commit/8bcc600b0ac88070740c63c7ce1c8a968dd85251
- https://github.com/klever-io/klever-go/releases/tag/v1.7.19
- https://github.com/klever-io/klever-go/security/advisories/GHSA-p7gw-2pcp-5pf8

### [CVE-2026-54755](https://github.com/klever-io/klever-go/commit/8bcc600b0ac88070740c63c7ce1c8a968dd85251)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-54755
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:18:17 JST
- 更新日: 2026-08-29 05:18:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Klever-Go（1.7.19未満）における分割ロイヤリティ値の整数オーバーフローおよび検証不備。
- 影響: 不正なパラメータにより過大なロイヤリティが与えられ、取引時に裏付けのないKLV等の資産が生成される可能性がある。
- 推奨対応: Klever-Go 1.7.19 以降へアップデートしてください。

#### References
- https://github.com/klever-io/klever-go/commit/8bcc600b0ac88070740c63c7ce1c8a968dd85251
- https://github.com/klever-io/klever-go/releases/tag/v1.7.19
- https://github.com/klever-io/klever-go/security/advisories/GHSA-cgc5-v3f2-8m2v

### [CVE-2026-82277](https://github.com/argoproj/argo-rollouts)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-82277
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:20:18 JST
- 更新日: 2026-08-29 05:20:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Argo Rolloutsダッシュボード（1.10.0以下）において、認証・認可およびCSRF保護なしに全ネットワークインターフェースへバインドし変更操作を公開する脆弱性。
- 影響: 同一ネットワーク上の攻撃者が、全ネームスペースに対してRolloutの昇格や中断などの操作を実行できる可能性がある。
- 推奨対応: 最新版への更新や、ダッシュボードへのアクセス制限・認証の有効化を検討してください。

#### References
- https://github.com/argoproj/argo-rollouts
- https://github.com/argoproj/argo-rollouts/blob/4e6a2798688e22868340d9871a3c8d78371f1568/server/server.go
- https://github.com/argoproj/argo-rollouts/issues/4747
- https://www.vulncheck.com/advisories/argo-rollouts-dashboard-unauthenticated-mutating-operations

### [CVE-2026-55108](https://github.com/kubevela/kubevela/commit/65dedda40a69cc1eccf4072a4c835e5b9f13334e)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-55108
- 関連キーワード: go, terraform
- 影響製品: -
- 公開日: 2026-08-29 05:18:24 JST
- 更新日: 2026-08-29 07:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KubeVelaのTerraformリモート構成ローダーにおけるシンボリックリンク追跡に関する制御不備。
- 影響: /dev/zero などの特殊ファイルを参照させることで無制限のデータ読み込みが発生し、コントローラーのメモリ枯渇やDoSを引き起こす可能性がある。
- 推奨対応: 修正済みバージョン（1.9.14、1.10.10以上、1.11.0-alpha.5以上など）へ更新してください。

#### References
- https://github.com/kubevela/kubevela/commit/65dedda40a69cc1eccf4072a4c835e5b9f13334e
- https://github.com/kubevela/kubevela/commit/7a4e59b2958ce1cf031fafbc188d6fafe8fe4d2e
- https://github.com/kubevela/kubevela/commit/f6a64398b5e0065c57c3a0fb6765dd3dc48c749d
- https://github.com/kubevela/kubevela/pull/7191
- https://github.com/kubevela/kubevela/pull/7192

### [CVE-2026-55520](https://github.com/scrapy/protego/commit/785940181659bf440ba82f1da148fade5087e858)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-55520
- 関連キーワード: python, go, express
- 影響製品: -
- 公開日: 2026-08-29 05:18:28 JST
- 更新日: 2026-08-29 05:18:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PythonライブラリProtego（0.6.2未満）のrobots.txtパーサーにおける正規表現バックトラッキングの不備。
- 影響: 操作されたrobots.txtの読み込みによりCPUリソースが消費され、クローラーがサービス拒否（DoS）状態に陥る可能性がある。
- 推奨対応: Protego 0.6.2 以降へ更新してください。

#### References
- https://github.com/scrapy/protego/commit/785940181659bf440ba82f1da148fade5087e858
- https://github.com/scrapy/protego/releases/tag/0.6.2
- https://github.com/scrapy/protego/security/advisories/GHSA-wjmf-p669-5m5p

### [CVE-2026-55065](https://github.com/go-vikunja/vikunja/commit/6895a7765ef1667be4b79df29549d33b9e1ca9ca)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-55065
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:18:23 JST
- 更新日: 2026-08-29 05:18:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: タスク管理プラットフォームVikunja（0.24.6～2.4.0未満）のビュー削除APIにおける認可チェックの不備。
- 影響: 認証されたユーザーが他プロジェクトの看板ビューやタスク配置などの構成データを削除できる可能性がある。
- 推奨対応: Vikunja 2.4.0 以降へアップデートしてください。

#### References
- https://github.com/go-vikunja/vikunja/commit/6895a7765ef1667be4b79df29549d33b9e1ca9ca
- https://github.com/go-vikunja/vikunja/pull/3239
- https://github.com/go-vikunja/vikunja/releases/tag/v2.4.0
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-gg93-x632-9ccv

### [CVE-2026-55066](https://github.com/go-vikunja/vikunja/commit/36cdc2ce2be0b8ccc74227d178b92047d59cd65f)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-55066
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:18:23 JST
- 更新日: 2026-08-29 05:18:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vikunja（2.4.0未満）のタスク操作APIにおける認可検証の欠如。
- 影響: 認証されたユーザーがタスクIDを列挙・指定することで、他テナントのタスク内容を閲覧したり完了状態を変更したりできる可能性がある。
- 推奨対応: Vikunja 2.4.0 以降へアップデートしてください。

#### References
- https://github.com/go-vikunja/vikunja/commit/36cdc2ce2be0b8ccc74227d178b92047d59cd65f
- https://github.com/go-vikunja/vikunja/pull/3239
- https://github.com/go-vikunja/vikunja/releases/tag/v2.4.0
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-5pg6-m483-7vrg

### [CVE-2026-82269](https://github.com/gophish/gophish)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-82269
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:20:17 JST
- 更新日: 2026-08-29 07:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Gophish（0.12.1以下）のAPI認証ミドルウェアにおけるアカウントロックアウト等のアクセス制御の迂回。
- 影響: 有効なAPIキーを持つ攻撃者が、アカウントロック時やパスワード変更要求時であってもAPIアクセスを維持できる可能性がある。
- 推奨対応: 最新版へのアップデートや、該当するAPIキーの無効化・再発行を検討してください。

#### References
- https://github.com/gophish/gophish
- https://github.com/gophish/gophish/blob/95618469799295e2c0fec980805a2dfbb818816b/middleware/middleware.go
- https://github.com/gophish/gophish/issues/9440
- https://www.vulncheck.com/advisories/gophish-account-lockout-and-forced-password-change-bypassable-via-api-key
- https://github.com/gophish/gophish/issues/9440

### [CVE-2026-55484](https://github.com/guno1928/alos-http/commit/314b6783e19698c85ea9d9b197ff52f7f6a3a374)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-55484
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-29 05:18:27 JST
- 更新日: 2026-08-29 07:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ALOS HTTP（修正版未満）のリクエストパス解析時における境界外アクセス問題。
- 影響: 未認証の攻撃者が不正なパス文字列を送信することでサーバーがパニック（クラッシュ）し、DoSが発生する可能性がある。
- 推奨対応: 修正済みの疑似バージョン（0.0.0-20260617230736-314b6783e196 以降）へ更新してください。

#### References
- https://github.com/guno1928/alos-http/commit/314b6783e19698c85ea9d9b197ff52f7f6a3a374
- https://github.com/guno1928/alos-http/security/advisories/GHSA-hr6j-w4mw-g9mj
- https://github.com/guno1928/alos-http/security/advisories/GHSA-hr6j-w4mw-g9mj

### [CVE-2026-77586](https://www.mongodb.com/docs/bi-connector/current/release-notes/)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-77586
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-08-29 05:19:56 JST
- 更新日: 2026-08-29 06:16:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Connector for BIが出力するSHOW CREATE文での識別子エスケープ処理の不備。
- 影響: コレクション名等に挿入された任意のSQL構文が生成文に含まれ、他サーバーでの再実行時に特権で意図しないSQLが実行される可能性がある。
- 推奨対応: 修正版へのアップデートおよび自動生成されたDDL文の実行前の確認を検討してください。

#### References
- https://www.mongodb.com/docs/bi-connector/current/release-notes/

### [CVE-2026-55245](https://github.com/maximhq/bifrost/commit/54ec431fc5255ff42c36420d88549477e0b33d89)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-55245
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:18:26 JST
- 更新日: 2026-08-29 07:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: BifrostにおけるIP判定ロジックの不備によるSSRF（サーバーサイドリクエストフォージェリ）の脆弱性。CGNATやNAT64などの特定の非パブリックIPアドレスを誤ってパブリックIPとして処理してしまう。
- 影響: 遠隔の攻撃者がマルチモーダルリクエストのURLを操作し、クラウドのインスタンスメタデータなどの内部サービスへアクセスする可能性がある。
- 推奨対応: Bifrostをバージョン1.5.17以降へアップデートする。

#### References
- https://github.com/maximhq/bifrost/commit/54ec431fc5255ff42c36420d88549477e0b33d89
- https://github.com/maximhq/bifrost/pull/4092
- https://github.com/maximhq/bifrost/releases/tag/core/v1.5.17
- https://github.com/maximhq/bifrost/security/advisories/GHSA-w98g-5w9p-p3rc
- https://github.com/maximhq/bifrost/security/advisories/GHSA-w98g-5w9p-p3rc

### [CVE-2026-54766](https://github.com/go-vikunja/vikunja/commit/d911caaa11c748c3abc6b98b3189afea2677bcb0)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-54766
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:18:17 JST
- 更新日: 2026-08-29 07:16:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vikunjaのプロジェクト複製処理における権限チェック回避の脆弱性。複製先の親プロジェクトに対する書き込み権限の確認が不十分になっている。
- 影響: 認証済みユーザーが、自身に書き込み権限のない他のユーザーやチームのプロジェクト階層下に任意の複製コンテンツを注入する可能性がある。
- 推奨対応: Vikunjaをバージョン2.4.0以降へアップデートする。

#### References
- https://github.com/go-vikunja/vikunja/commit/d911caaa11c748c3abc6b98b3189afea2677bcb0
- https://github.com/go-vikunja/vikunja/pull/3239
- https://github.com/go-vikunja/vikunja/releases/tag/v2.4.0
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-f27p-pw2p-9pr4
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-f27p-pw2p-9pr4

### [CVE-2026-55064](https://github.com/go-vikunja/vikunja/commit/781ffac198548ae4f3d1febc613caed8e0e11d01)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-55064
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:18:23 JST
- 更新日: 2026-08-29 07:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vikunjaのプロジェクト更新処理における親プロジェクト分離時の認可バイパスの脆弱性。親プロジェクトIDに0を指定することで管理者権限チェックを回避できる。
- 影響: 書き込み権限のみを持つユーザーが共有子プロジェクトを親階層から切断し、プロジェクト階層構造や権限継承関係を破損させる可能性がある。
- 推奨対応: Vikunjaをバージョン2.4.0以降へアップデートする。

#### References
- https://github.com/go-vikunja/vikunja/commit/781ffac198548ae4f3d1febc613caed8e0e11d01
- https://github.com/go-vikunja/vikunja/pull/3239
- https://github.com/go-vikunja/vikunja/releases/tag/v2.4.0
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-44v6-7fxq-vgf4
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-44v6-7fxq-vgf4

### [CVE-2026-55067](https://github.com/go-vikunja/vikunja/commit/b31d606b8879ebe98fbb2ac5d8b3066b86f59868)

> **Backend** / **MEDIUM** / CVSS: **5.0** / KEV: **no**

- タイトル: CVE-2026-55067
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:18:24 JST
- 更新日: 2026-08-29 07:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vikunjaのバケット更新エンドポイントにおけるMass Assignment（一括割り当て）および認可不足の脆弱性。移動先ビューに対する権限検証が欠落している。
- 影響: 認証済みユーザーが他テナントのKanbanビューへ任意のバケットを移動させ、改ざんや不当なコンテンツ表示を引き起こす可能性がある。
- 推奨対応: Vikunjaをバージョン2.4.0以降へアップデートする。

#### References
- https://github.com/go-vikunja/vikunja/commit/b31d606b8879ebe98fbb2ac5d8b3066b86f59868
- https://github.com/go-vikunja/vikunja/pull/3239
- https://github.com/go-vikunja/vikunja/releases/tag/v2.4.0
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-569v-q83c-3j3g
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-569v-q83c-3j3g

### [CVE-2026-55545](https://github.com/yamcs/yamcs/commit/0691731846c5a0aca81b88fabbd2cd51d56fe076)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-55545
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:18:28 JST
- 更新日: 2026-08-29 05:18:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: YamcsのWebSocketサブスクリプション処理における認可検証欠落の脆弱性。REST APIと同等のアクセス権限チェックがWebSocketトピックで実施されていない。
- 影響: 低権限の認証済みユーザーが、本来許可されていないスコープ外のテレメトリ、アルゴリズム状態、ミッションデータベース変更情報を受信する可能性がある。
- 推奨対応: Yamcsをバージョン5.12.8または5.13.2以降へアップデートする。

#### References
- https://github.com/yamcs/yamcs/commit/0691731846c5a0aca81b88fabbd2cd51d56fe076
- https://github.com/yamcs/yamcs/commit/12864af555e6ca4941b01c1f1217859cc0492ce0
- https://github.com/yamcs/yamcs/releases/tag/yamcs-5.12.8
- https://github.com/yamcs/yamcs/releases/tag/yamcs-5.13.2
- https://github.com/yamcs/yamcs/security/advisories/GHSA-fwww-cp23-7f5g

### [CVE-2026-76794](https://www.mongodb.com/docs/sql-interface/changelog/)

> **Backend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-76794
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-08-29 05:19:54 JST
- 更新日: 2026-08-29 06:16:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoSQL Transition Readiness Toolにおける生成HTMLレポート出力時のメタデータエンコード不足（XSS）の脆弱性。
- 影響: 書き込み権限を持つユーザーが細工したメタデータをデータベースに挿入することで、レポートを閲覧したオペレーターのブラウザ上で任意のスクリプトが実行される可能性がある。
- 推奨対応: ツールの最新修正版を適用するか、信頼できないデータベース環境に対するレポート生成および開披に注意する。

#### References
- https://www.mongodb.com/docs/sql-interface/changelog/

### [CVE-2026-77184](https://www.mongodb.com/docs/bi-connector/current/release-notes/)

> **Backend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-77184
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-08-29 05:19:55 JST
- 更新日: 2026-08-29 06:16:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Connector for BIにおけるDDL生成時のエスケープ処理不足によるSQL注入の脆弱性。JSON schema validatorの記述に含まれるバックスラッシュが不完全にエスケープされる。
- 影響: スキーマ変更権限を持つユーザーが不当なSQLテキストを混入させ、生成されたDDLがSQLサーバーで再実行された際に意図しない処理が実行される可能性がある。
- 推奨対応: 製品の修正バージョンが提供されているか確認して適用するか、生成されたDDLを外部実行する前に記述内容を検証する。

#### References
- https://www.mongodb.com/docs/bi-connector/current/release-notes/

### [CVE-2026-55569](https://github.com/aquaproj/aqua/commit/d5b02b220188de376a661b3aabfa912202a1a59a)

> **Backend** / **MEDIUM** / CVSS: **6.6** / KEV: **no**

- タイトル: CVE-2026-55569
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:18:29 JST
- 更新日: 2026-08-29 05:18:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: aquaにおけるアーカイブ展開時のシンボリックリンク検証不備（パストラバーサル）の脆弱性。
- 影響: 悪意のあるパッケージアーカイブを展開した際、解凍先ディレクトリ外にあるファイル（シェル設定や実行ファイル等）が任意の内容で上書きされる可能性がある。
- 推奨対応: aquaをバージョン2.60.1以降へアップデートする。

#### References
- https://github.com/aquaproj/aqua/commit/d5b02b220188de376a661b3aabfa912202a1a59a
- https://github.com/aquaproj/aqua/releases/tag/v2.60.1
- https://github.com/aquaproj/aqua/security/advisories/GHSA-mf5c-hw34-4hpp

### [CVE-2026-76797](https://www.mongodb.com/docs/sql-interface/changelog/)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-76797
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:19:55 JST
- 更新日: 2026-08-29 06:16:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoSQL Transition Readiness Toolが生成するCSVレポートにおけるCSVインジェクション（数式注入）の脆弱性。
- 影響: データベース名やコレクション名に埋め込まれた先頭文字が数式として評価され、操作者が表計算ソフトでレポートを開いた際に外部通信や意図しない処理が実行される可能性がある。
- 推奨対応: ツールの最新修正版を適用するか、生成されたCSVを表計算ソフトで開く前に数式の無効化処理等を行う。

#### References
- https://www.mongodb.com/docs/sql-interface/changelog/

### [CVE-2026-76798](https://www.mongodb.com/docs/sql-interface/changelog/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-76798
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-29 05:19:55 JST
- 更新日: 2026-08-29 06:16:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoSQL Transition Readiness Toolにおけるログ由来のデータ出力処理でのエンコード不足（XSS）の脆弱性。クエリテキストやユーザー名が不適切にHTMLへ出力される。
- 影響: BI Connector経由でクエリを実行可能なユーザーがログを汚染し、レポート閲覧者のブラウザ上でスクリプトを実行させてログ情報等を漏洩させる可能性がある。
- 推奨対応: ツールの最新修正版を適用するか、不審なログが含まれる環境でのレポート開披に注意する。

#### References
- https://www.mongodb.com/docs/sql-interface/changelog/

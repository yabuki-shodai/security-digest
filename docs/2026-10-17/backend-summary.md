# Backend CVE Summary (2026-10-17)

## Overview

- 取得日時: 2026-10-17 09:23:10 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 28
- Critical: 5
- High: 12
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-59962](https://github.com/TandoorRecipes/recipes/commit/322696f618997e98f2d4c15ec64b9480735589f0)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-59962
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-10-17 02:17:35 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tandoor Recipes 2.6.10 未満における Django ORM の order_by() 処理における入力検証不備とソート順序による情報漏洩の脆弱性。
- 影響: 認証済みユーザーが関連テーブルの構造を利用したソートパラメーターを送信することで、パスワードハッシュやメールアドレスなどの機密データを推測・参照する可能性があります。
- 推奨対応: Tandoor Recipes を 2.6.10 以降へアップデートしてください。

#### References
- https://github.com/TandoorRecipes/recipes/commit/322696f618997e98f2d4c15ec64b9480735589f0
- https://github.com/TandoorRecipes/recipes/commit/382a976cc79635edc30aef84cb2b2b72eb8afd3c
- https://github.com/TandoorRecipes/recipes/commit/82fd4e00f1387a1c466489989f2e94487149f7f4
- https://github.com/TandoorRecipes/recipes/releases/tag/2.6.10
- https://github.com/TandoorRecipes/recipes/security/advisories/GHSA-4x57-2q4q-xwpp

### [CVE-2026-111641](https://github.com/fastapiadmin/FastapiAdmin/blob/v3.0/backend/app/api/v1/module_system/auth/controller.py#L173-L251)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-111641
- 関連キーワード: fastapi, gin
- 影響製品: -
- 公開日: 2026-10-17 03:17:44 JST
- 更新日: 2026-10-17 07:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FastapiAdmin 3.0 以下における自動ログインエンドポイントの不備による認証バイパスの脆弱性。
- 影響: 未認証の遠隔攻撃者が管理者ユーザーのトークンを生成し、管理者権限（JWTセッション）を取得して全権限を奪取する可能性があります。
- 推奨対応: FastapiAdmin を最新バージョンへアップデートし、自動ログイン機能の無効化またはアクセス制限を行ってください。

#### References
- https://github.com/fastapiadmin/FastapiAdmin/blob/v3.0/backend/app/api/v1/module_system/auth/controller.py#L173-L251
- https://hackmd.io/@hieuPenguinnn/fastapiadmin-unauthenticated-autologin-and-hardcoded-jwt-secret
- https://www.vulncheck.com/advisories/fastapiadmin-through-3.0-authentication-bypass-via-auto-login-endpoints

### [CVE-2026-111642](https://github.com/fastapiadmin/FastapiAdmin/blob/v3.0/backend/app/config/setting.py#L67)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-111642
- 関連キーワード: fastapi
- 影響製品: -
- 公開日: 2026-10-17 03:17:44 JST
- 更新日: 2026-10-17 05:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FastapiAdmin 3.0 以下におけるハードコードされた JWT 署名シークレットの脆弱性。
- 影響: 低権限の認証済みユーザーが JWT トークンを偽造し、スーパーユーザー権限へ昇格する可能性があります。
- 推奨対応: FastapiAdmin を最新版へアップデートし、設定ファイルの署名シークレットを変更してください。

#### References
- https://github.com/fastapiadmin/FastapiAdmin/blob/v3.0/backend/app/config/setting.py#L67
- https://github.com/fastapiadmin/FastapiAdmin/blob/v3.0/backend/app/core/dependencies.py#L72-L112
- https://hackmd.io/@hieuPenguinnn/fastapiadmin-unauthenticated-autologin-and-hardcoded-jwt-secret
- https://www.vulncheck.com/advisories/fastapiadmin-through-3.0-hard-coded-jwt-secret-privilege-escalation
- https://hackmd.io/@hieuPenguinnn/fastapiadmin-unauthenticated-autologin-and-hardcoded-jwt-secret

### [CVE-2026-111639](https://github.com/mlogclub/bbs-go/blob/v4.4.6/internal/pkg/google/jwt.go#L55-L58)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-111639
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-17 03:17:44 JST
- 更新日: 2026-10-17 04:03:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: bbs-go 4.4.6 以下における Google ID トークンの aud（オーディエンス）クレーム検証不備による認証バイパスの脆弱性。
- 影響: 攻撃者が別の OAuth クライアント経由で取得した他人の Google ID トークンを再利用し、対象被害者のアカウントとして不正ログインする可能性があります。
- 推奨対応: bbs-go を最新版へ更新し、Google ID トークン受取時に aud クレームを適切に検証するよう設定してください。

#### References
- https://github.com/mlogclub/bbs-go/blob/v4.4.6/internal/pkg/google/jwt.go#L55-L58
- https://github.com/mlogclub/bbs-go/blob/v4.4.6/internal/services/third_user_service.go#L274-L293
- https://hackmd.io/@hieuPenguinnn/bbs-go-google-one-tap-id-token-audience-confusion-account-takeover
- https://www.vulncheck.com/advisories/bbs-go-through-4.4.6-account-takeover-via-google-one-tap-login

### [CVE-2026-68906](https://github.com/mz-automation/libiec61850/commit/2edf2a12bf0ced6a2ac595862e3e873814983f7f)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-68906
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-17 01:20:00 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libIEC61850 1.6.2 未満の parseUserInformation における AARE PDU 解析時の長さ検証不備の脆弱性。
- 影響: 未認証の遠隔攻撃者が不正な PDU を送信することで、CPU の無限ループによるサービス拒否（DoS）や、境界外読み取りによるプロセス強制終了を引き起こす可能性があります。
- 推奨対応: libIEC61850 を 1.6.2 以降へアップデートしてください。

#### References
- https://github.com/mz-automation/libiec61850/commit/2edf2a12bf0ced6a2ac595862e3e873814983f7f
- https://github.com/mz-automation/libiec61850/releases/tag/v1.6.2
- https://github.com/mz-automation/libiec61850/security/advisories/GHSA-f7xm-q62q-22cx

### [CVE-2026-48503](https://github.com/mz-automation/libiec61850/commit/bba5bf2fab6d7ac88f5accb4c9e90b123436ebf2)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-48503
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-17 01:18:11 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libIEC61850 1.6.2 未満の MMS ファイルサービスにおける範囲外ファイル位置指定処理に伴う情報漏洩の脆弱性。
- 影響: 未認証の遠隔クライアントが大きすぎる読み取り位置を指定することで、以前の応答データやプロトコル断片などの残留データを取得する可能性があります。
- 推奨対応: libIEC61850 を 1.6.2 以降へアップデートしてください。

#### References
- https://github.com/mz-automation/libiec61850/commit/bba5bf2fab6d7ac88f5accb4c9e90b123436ebf2
- https://github.com/mz-automation/libiec61850/releases/tag/v1.6.2
- https://github.com/mz-automation/libiec61850/security/advisories/GHSA-4c8m-jr3r-h8j2
- https://github.com/mz-automation/libiec61850/security/advisories/GHSA-4c8m-jr3r-h8j2

### [CVE-2026-48741](https://github.com/mz-automation/libiec61850/commit/7c15310405def00cac628ebde4ce1404bfb8a411)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-48741
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-17 01:18:11 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libIEC61850 1.6.2 未満の alternateArrayAccess におけるサブ配列の範囲チェック欠如による NULL ポインタ参照の脆弱性。
- 影響: 遠隔の攻撃者が配列モデルを含むデータに対して不正な MMS Read リクエストを送信し、サーバーをクラッシュ（DoS）させる可能性があります。
- 推奨対応: libIEC61850 を 1.6.2 以降へアップデートしてください。

#### References
- https://github.com/mz-automation/libiec61850/commit/7c15310405def00cac628ebde4ce1404bfb8a411
- https://github.com/mz-automation/libiec61850/releases/tag/v1.6.2
- https://github.com/mz-automation/libiec61850/security/advisories/GHSA-8mfr-hq64-9w33

### [CVE-2026-68907](https://github.com/mz-automation/libiec61850/commit/062062daf4cb50c7aa76e01d6fb4d58fc9278a7d)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-68907
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-17 01:20:00 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libIEC61850 1.6.2 未満の checkDataSetAccess における引数順序の誤りによるメモリ読み取り・スタック破損の脆弱性。
- 影響: 遠隔の攻撃者が特定の定義リクエストを送信することで、バッファオーバーリードを発生させ、サーバーをクラッシュ（DoS）させる可能性があります。
- 推奨対応: libIEC61850 を 1.6.2 以降へアップデートしてください。

#### References
- https://github.com/mz-automation/libiec61850/commit/062062daf4cb50c7aa76e01d6fb4d58fc9278a7d
- https://github.com/mz-automation/libiec61850/releases/tag/v1.6.2
- https://github.com/mz-automation/libiec61850/security/advisories/GHSA-7v2x-39mw-2979

### [CVE-2026-46472](https://gstreamer.freedesktop.org/security/sa-2026-0018.html)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-46472
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-17 01:18:11 JST
- 更新日: 2026-10-17 04:55:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GStreamerのisomp4プラグインにおける境界外読み取りの脆弱性
- 影響: 悪意のあるMP4ファイルを解析する際にグローバル配列外の読み取りが発生し、情報漏洩に繋がる可能性があります。
- 推奨対応: GStreamer (gst-plugins-good) を 1.28.2 以降の修正済みバージョンに更新してください。

#### References
- https://gstreamer.freedesktop.org/security/sa-2026-0018.html

### [CVE-2026-57447](https://github.com/discourse/discourse-doc-categories/commit/b15d4de02ad29d7c9525346afee51fef4a2c605a)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-57447
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-17 01:18:44 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Discourse Doc Categoriesプラグインにおけるアクセス制御の不備による認可不全の脆弱性
- 影響: インデックスのトピックを編集可能なユーザーが、本来閲覧権限のない非公開メッセージや制限付きトピックのタイトルを取得できる可能性があります。
- 推奨対応: 修正コミット (b15d4de02ad29d7c9525346afee51fef4a2c605a) が適用された修正版へ更新してください。

#### References
- https://github.com/discourse/discourse-doc-categories/commit/b15d4de02ad29d7c9525346afee51fef4a2c605a
- https://github.com/discourse/discourse-doc-categories/security/advisories/GHSA-x63p-48vw-8r64

### [CVE-2026-102941](https://github.com/gomarkdown/markdown/commit/61af6e1e69710c5ca13cfbaaaa1bc11bc763a8a9)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-102941
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-17 01:16:52 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: gomarkdown/markdownライブラリのparser.IsSafeURLにおける境界チェック不備の脆弱性
- 影響: 短く不審なURLを含むMarkdownを処理した際にスライス境界エラー（パニック）が発生し、アプリケーションが停止（DoS）する可能性があります。
- 推奨対応: github.com/gomarkdown/markdown を修正済みバージョン (0.0.0-20260724235538-61af6e1e6971 以降) に更新してください。

#### References
- https://github.com/gomarkdown/markdown/commit/61af6e1e69710c5ca13cfbaaaa1bc11bc763a8a9
- https://github.com/gomarkdown/markdown/security/advisories/GHSA-cv23-7vc5-jfh7

### [CVE-2026-95859](https://github.com/libp2p/rust-libp2p/commit/51ed5f00e1b0620ded3444ecadf18477052148ea)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-95859
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-17 01:22:44 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libp2p-rustのGossipsub制御メッセージ処理におけるメモリ制御不足の脆弱性
- 影響: 未認証のリモート攻撃者が多数の未購読トピックを送信することでピアごとのメモリを無制限に消費させ、プロセスをクラッシュ（DoS）させる可能性があります。
- 推奨対応: libp2p-rust を 0.49.5 以降のバージョンに更新してください。

#### References
- https://github.com/libp2p/rust-libp2p/commit/51ed5f00e1b0620ded3444ecadf18477052148ea
- https://github.com/libp2p/rust-libp2p/pull/6608
- https://github.com/libp2p/rust-libp2p/security/advisories/GHSA-g3g5-x568-qvqx

### [CVE-2026-111653](https://github.com/53AI/53AIHub/blob/v0.5.3/api/controller/enterprise.go#L122-L160)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-111653
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-17 03:17:46 JST
- 更新日: 2026-10-17 04:03:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: 53AIHubにおけるAPIエンドポイントの認証欠落の脆弱性
- 影響: 未認証の攻撃者が企業IDを列挙し、PUTリクエストを送信して任意企業のロゴや表示名などの情報を上書き改ざん・改ざん表示に悪用する可能性があります。
- 推奨対応: 53AIHubを適切な認証チェックが有効化された修正済みバージョンへ更新してください。

#### References
- https://github.com/53AI/53AIHub/blob/v0.5.3/api/controller/enterprise.go#L122-L160
- https://github.com/53AI/53AIHub/blob/v0.5.3/api/router/api.go#L54-L66
- https://hackmd.io/@hieuPenguinnn/53aihub-unauth-cross-tenant-enterprise-update
- https://www.vulncheck.com/advisories/53aihub-through-0.5.3-missing-authentication-via-put-api-enterprises-id

### [CVE-2026-57446](https://github.com/mz-automation/libiec61850/commit/d86b4a9c7a903641819235e1678b18901518f3cd)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-57446
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-17 01:18:44 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libIEC61850のMMS ObtainFile処理における不適切なリソース解放（二重クローズ）の脆弱性
- 影響: 特定の成功と失敗のリクエストシーケンスを送信されることで、サーバープロセスがクラッシュ（DoS）する可能性があります。
- 推奨対応: libIEC61850 を 1.6.2 以降のバージョンに更新してください。

#### References
- https://github.com/mz-automation/libiec61850/commit/d86b4a9c7a903641819235e1678b18901518f3cd
- https://github.com/mz-automation/libiec61850/releases/tag/v1.6.2
- https://github.com/mz-automation/libiec61850/security/advisories/GHSA-cxgr-7v9h-fj9p

### [CVE-2026-68908](https://github.com/mz-automation/libiec61850/commit/5b2a69f44256b8548927d8afdd7ac5f5381abe1e)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-68908
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-17 01:20:01 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libIEC61850のレポート制御ブロック処理における不正なメモリ解放の脆弱性
- 影響: リモートのクライアントが制限を超える長さのRptIDを書き込んでレポート生成を誘発することで、サーバーをクラッシュさせる可能性があります。
- 推奨対応: libIEC61850 を 1.6.2 以降のバージョンに更新してください。

#### References
- https://github.com/mz-automation/libiec61850/commit/5b2a69f44256b8548927d8afdd7ac5f5381abe1e
- https://github.com/mz-automation/libiec61850/releases/tag/v1.6.2
- https://github.com/mz-automation/libiec61850/security/advisories/GHSA-7qg8-hm25-rv5v
- https://github.com/mz-automation/libiec61850/security/advisories/GHSA-7qg8-hm25-rv5v

### [CVE-2026-85745](https://github.com/MariaDB/server/commit/2bf355e361db85153fdfba7b8a0f0d114d6a26ce)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-85745
- 関連キーワード: go, mysql
- 影響製品: -
- 公開日: 2026-10-17 02:17:51 JST
- 更新日: 2026-10-17 03:09:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MariaDB ServerのST_Area関数における境界外読み取り（バッファオーバーリード）の脆弱性
- 影響: 低権限の攻撃者が不正な空間データを送信することでメモリ内容を読み取り、ASLR等の保護機能を回避する情報として悪用する可能性があります。
- 推奨対応: MariaDB Server を該当系列の修正済みバージョン（10.6.28, 10.11.19, 11.4.13, 11.8.9, 12.3.3, 13.0.2 など）へ更新してください。

#### References
- https://github.com/MariaDB/server/commit/2bf355e361db85153fdfba7b8a0f0d114d6a26ce
- https://github.com/MariaDB/server/releases/tag/mariadb-10.11.19
- https://github.com/MariaDB/server/releases/tag/mariadb-10.6.28
- https://github.com/MariaDB/server/releases/tag/mariadb-11.4.13
- https://github.com/MariaDB/server/releases/tag/mariadb-11.8.9

### [CVE-2026-111624](https://github.com/umbraco/Umbraco-CMS/blob/release-18.2.0/src/Umbraco.Cms.Api.Management/Preview/PreviewHub.cs#L9-L11)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-111624
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-17 03:17:42 JST
- 更新日: 2026-10-17 04:00:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Umbraco CMSのSignalRハブにおける認可チェック欠落の脆弱性
- 影響: 未認証のクライアントがバックオフィス用ハブに接続し、未公開コンテンツ情報や編集アクティビティなどのメタデータを取得する可能性があります。
- 推奨対応: Umbraco CMS を 17.7.1 または 18.2.1 以降の修正版に更新してください。

#### References
- https://github.com/umbraco/Umbraco-CMS/blob/release-18.2.0/src/Umbraco.Cms.Api.Management/Preview/PreviewHub.cs#L9-L11
- https://github.com/umbraco/Umbraco-CMS/blob/release-18.2.0/src/Umbraco.Cms.Api.Management/Preview/PreviewHubUpdater.cs#L58
- https://github.com/umbraco/Umbraco-CMS/commit/243e082479c777d0f585bbd2f8db571607767b22
- https://github.com/umbraco/Umbraco-CMS/commit/b4f6cfc9d0955f9d8443e68353db4a692e91bd94
- https://github.com/umbraco/Umbraco-CMS/releases/tag/release-17.7.1

### [CVE-2026-111672](https://github.com/data-infra/cube-studio/blob/v2026.09.01/myapp/views/view_pipeline.py#L1144-L1268)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-111672
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-17 03:17:49 JST
- 更新日: 2026-10-17 04:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cube-studioのパイプライン表示エンドポイントにおける認可不足の脆弱性
- 影響: 認証済みユーザーがIDを推測・指定することで他グループのパイプライン情報（DAG、ポッド名、構成情報等）を閲覧したり複製したりできる可能性があります。
- 推奨対応: Cube-studioをアクセス制御が強化された修正済みバージョンに更新してください。

#### References
- https://github.com/data-infra/cube-studio/blob/v2026.09.01/myapp/views/view_pipeline.py#L1144-L1268
- https://hackmd.io/@hieuPenguinnn/cube-studio-idor-expose-api-lifecycle
- https://www.vulncheck.com/advisories/cube-studio-through-2026.09.01-idor-via-pipeline-view-and-copy-endpoints
- https://hackmd.io/@hieuPenguinnn/cube-studio-idor-expose-api-lifecycle

### [CVE-2026-46471](https://github.com/atredispartners/advisories/blob/master/2026/ATREDIS-2026-0004.md)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-46471
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-17 01:18:11 JST
- 更新日: 2026-10-17 04:55:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GStreamerのisomp4プラグインにおける、MP4ファイル解析時のヒープバッファオーバーリードの脆弱性。
- 影響: 攻撃者によってヒープメモリの内容が読み取られ、情報が漏洩する可能性があります。
- 推奨対応: GStreamer (gst-plugins-good) をバージョン1.28.2以降にアップデートしてください。

#### References
- https://github.com/atredispartners/advisories/blob/master/2026/ATREDIS-2026-0004.md
- https://gstreamer.freedesktop.org/security/sa-2026-0002.html

### [CVE-2026-109839](https://www.ibm.com/support/pages/node/7292486)

> **Backend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-109839
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-17 03:17:31 JST
- 更新日: 2026-10-17 05:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Db2 Genius Hub 1.0における暗号化アルゴリズムの初期化ベクトル（IV）欠損の脆弱性。
- 影響: 認証された遠隔の攻撃者により、セキュリティ制限を回避される可能性があります。
- 推奨対応: IBMが提供する最新の修正パッチまたはアップデートを適用してください。

#### References
- https://www.ibm.com/support/pages/node/7292486

### [CVE-2026-57169](https://github.com/Finsys/dockhand/commit/efb634701c55f80a8c752df8ae08d88f2c16cce9)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-57169
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-17 02:17:35 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DockhandのコンテナターミナルエンドポイントにおけるWebSocket認証不備の脆弱性。
- 影響: 未認証の攻撃者がコンテナ内で任意のコマンドを実行できる可能性があり、環境によってはホストシステムが侵害される恐れがあります。
- 推奨対応: Dockhandをバージョン1.0.34以降にアップデートしてください。

#### References
- https://github.com/Finsys/dockhand/commit/efb634701c55f80a8c752df8ae08d88f2c16cce9
- https://github.com/Finsys/dockhand/releases/tag/v1.0.34
- https://github.com/Finsys/dockhand/security/advisories/GHSA-f6q3-chhc-4hxm

### [CVE-2026-86008](https://github.com/Mailu/Mailu/commit/8577c929b4ade04d3cd4210cf036601abd793556)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-86008
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-17 02:17:51 JST
- 更新日: 2026-10-17 02:17:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mailuにおけるアクセス制御不備による不適切な認可の脆弱性。
- 影響: ドメイン管理者がより上位の権限を持つアカウントのパスワードリセットやトークン取得を行い、アカウントを乗っ取る可能性があります。
- 推奨対応: 修正コミット（8577c929b4ade04d3cd4210cf036601abd793556）が含まれるバージョンへ更新してください。

#### References
- https://github.com/Mailu/Mailu/commit/8577c929b4ade04d3cd4210cf036601abd793556
- https://github.com/Mailu/Mailu/issues/2685
- https://github.com/Mailu/Mailu/pull/4050
- https://github.com/Mailu/Mailu/security/advisories/GHSA-9pv5-rm76-3qwj

### [CVE-2026-86009](https://github.com/Mailu/Mailu/commit/f05aeb8322e2f61096af6b089d61ba6f40587d96)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-86009
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-17 02:17:51 JST
- 更新日: 2026-10-17 02:17:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mailuにおけるドメイン管理者による他ドメインのスプーフィング設定不備の脆弱性。
- 影響: 悪意のあるドメイン管理者が、自身が管理していない別ドメインになりすましてDKIM/SPF認証済みのメールを送信できる可能性があります。
- 推奨対応: 修正コミット（f05aeb8322e2f61096af6b089d61ba6f40587d96）が含まれるバージョンへ更新してください。

#### References
- https://github.com/Mailu/Mailu/commit/f05aeb8322e2f61096af6b089d61ba6f40587d96
- https://github.com/Mailu/Mailu/issues/2686
- https://github.com/Mailu/Mailu/pull/4072
- https://github.com/Mailu/Mailu/security/advisories/GHSA-crww-m82r-2wfm

### [CVE-2026-62362](https://github.com/PBH-BTN/PeerBanHelper/commit/bec34c8b93c6ea3a3bc2ad992aedd41b95cd400a)

> **Backend** / **MEDIUM** / CVSS: **4.9** / KEV: **no**

- タイトル: CVE-2026-62362
- 関連キーワード: postgresql, mysql
- 影響製品: -
- 公開日: 2026-10-17 02:17:35 JST
- 更新日: 2026-10-17 05:04:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PeerBanHelperの統計解析APIにおける入力サニタイズ不足によるSQLインジェクションの脆弱性。
- 影響: 認証されたユーザーにより、PeerBanHelperのデータベース内の全データを閲覧される可能性があります。
- 推奨対応: PeerBanHelperをバージョン9.3.15以降にアップデートしてください。

#### References
- https://github.com/PBH-BTN/PeerBanHelper/commit/bec34c8b93c6ea3a3bc2ad992aedd41b95cd400a
- https://github.com/PBH-BTN/PeerBanHelper/releases/tag/v9.3.15
- https://github.com/PBH-BTN/PeerBanHelper/security/advisories/GHSA-pc89-mfwm-hj9x

### [CVE-2026-85748](https://github.com/MariaDB/server/commit/91156c3de58762196605150ab3f756fe952592d1)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-85748
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-10-17 02:17:51 JST
- 更新日: 2026-10-17 03:09:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MariaDB ServerのSYS_REFCURSOR処理におけるUse-After-Freeの脆弱性。
- 影響: 低権限の攻撃者がメモリ破壊を引き起こし、他の脆弱性と組み合わせることでリモートコード実行に繋がる可能性があります。
- 推奨対応: MariaDB Serverを修正済みバージョン（12.3.3、13.0.2など）にアップデートしてください。

#### References
- https://github.com/MariaDB/server/commit/91156c3de58762196605150ab3f756fe952592d1
- https://github.com/MariaDB/server/commit/9b075b2cb53338f67e7230cc585e02d2d34514ed
- https://github.com/MariaDB/server/releases/tag/mariadb-12.3.3
- https://github.com/MariaDB/server/releases/tag/mariadb-13.0.2
- https://github.com/MariaDB/server/security/advisories/GHSA-mv8g-9f7q-hprm

### [CVE-2026-92262](https://github.com/MariaDB/server/commit/574ba66b2d6c5d71db83d416677876e9b592858e)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-92262
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-10-17 02:17:52 JST
- 更新日: 2026-10-17 03:09:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MariaDB Serverの`#mysql50#`プレフィックス処理におけるファイルシステム名検証回避の脆弱性。
- 影響: 攻撃者がレガシーファイルにアクセスし、サービスのクラッシュ、データの破壊・漏洩、あるいはリモートコード実行を引き起こす可能性があります。
- 推奨対応: MariaDB Serverを修正済みバージョン（10.6.28、10.11.19、11.4.13、11.8.9、12.3.3、13.0.2など）にアップデートしてください。

#### References
- https://github.com/MariaDB/server/commit/574ba66b2d6c5d71db83d416677876e9b592858e
- https://github.com/MariaDB/server/commit/f277eefa424850a8cba5c2371406047f6395e8bb
- https://github.com/MariaDB/server/releases/tag/mariadb-10.11.19
- https://github.com/MariaDB/server/releases/tag/mariadb-10.6.28
- https://github.com/MariaDB/server/releases/tag/mariadb-11.4.13

### [CVE-2026-85746](https://github.com/MariaDB/server/commit/5c04ca5524385356ff7cf84974a7d491974c1f85)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-85746
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-10-17 02:17:51 JST
- 更新日: 2026-10-17 03:19:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MariaDB ServerのST_AsText関数における境界外書き込み（バッファオーバーフロー）の脆弱性。
- 影響: 低権限の遠隔攻撃者がメモリを破壊し、他の脆弱性と組み合わせることでコード実行を達成する可能性があります。
- 推奨対応: MariaDB Serverを修正済みバージョン（10.6.28、10.11.19、11.4.13、11.8.9、12.3.3、13.0.2など）にアップデートしてください。

#### References
- https://github.com/MariaDB/server/commit/5c04ca5524385356ff7cf84974a7d491974c1f85
- https://github.com/MariaDB/server/releases/tag/mariadb-10.11.19
- https://github.com/MariaDB/server/releases/tag/mariadb-10.6.28
- https://github.com/MariaDB/server/releases/tag/mariadb-11.4.13
- https://github.com/MariaDB/server/releases/tag/mariadb-11.8.9

### [CVE-2026-111613](https://github.com/alldatacenter/alldata)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-111613
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-10-17 03:17:40 JST
- 更新日: 2026-10-17 04:03:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AllDataのテスト用エンドポイントにおける未認証のJDBCインジェクションの脆弱性。
- 影響: 未認証の遠隔攻撃者が任意のデータベース接続を確立し、ホスト上の任意のファイルを読み取る可能性があります。
- 推奨対応: AllDataの修正済みバージョンへのアップデートや、該当エンドポイントへのアクセス制限を実施してください。

#### References
- https://github.com/alldatacenter/alldata
- https://github.com/alldatacenter/alldata/blob/alldata-release-0.7.1/moat/studio/data-dts/service-data-dts/src/main/java/com/platform/admin/config/WebSecurityConfiguration.java
- https://github.com/alldatacenter/alldata/blob/alldata-release-0.7.1/moat/studio/data-dts/service-data-dts/src/main/java/com/platform/admin/controller/JobDatasourceController.java#L131-L135
- https://github.com/alldatacenter/alldata/blob/alldata-release-0.7.1/moat/studio/data-dts/service-data-dts/src/main/java/com/platform/admin/tool/query/BaseQueryTool.java#L107-L124
- https://hackmd.io/@hieuPenguinnn/alldata-dts-unauthenticated-jdbc-url-injection

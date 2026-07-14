# Backend CVE Summary (2026-07-15)

## Overview

- 取得日時: 2026-07-15 08:07:55 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 21
- Critical: 2
- High: 16
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-15694](https://github.com/cve-a/dexingzhiqing/issues/4)

> **Backend** / **HIGH** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-15694
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-15 00:17:00 JST
- 更新日: 2026-07-15 00:26:24 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Tenda BE12 Pro 16.03.66.23の/goform/SetIpBind内のfromSetIpBind関数にスタックベースのバッファオーバーフロー脆弱性が存在します。  
- 影響: リモートからの悪意ある引数操作により、任意のコード実行やサービス停止が発生する可能性があります。  
- 推奨対応: 最新のファームウェアへの更新や、該当機能へのアクセス制限を検討してください。

#### References
- https://github.com/cve-a/dexingzhiqing/issues/4
- https://vuldb.com/cve/CVE-2026-15694
- https://vuldb.com/submit/856015
- https://vuldb.com/vuln/378241
- https://vuldb.com/vuln/378241/cti

### [CVE-2026-15695](https://github.com/cve-a/dexingzhiqing/issues/5)

> **Backend** / **HIGH** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-15695
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-15 00:17:00 JST
- 更新日: 2026-07-15 00:26:24 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Tenda BE12 Pro 16.03.66.23の/fromDhcpListClient関数にスタックベースのバッファオーバーフロー脆弱性が存在します。  
- 影響: リモートからの攻撃により、任意のコード実行やサービス停止の可能性があります。  
- 推奨対応: 公式の修正パッチ適用やファームウェアのアップデートを速やかに行うことを推奨します。

#### References
- https://github.com/cve-a/dexingzhiqing/issues/5
- https://vuldb.com/cve/CVE-2026-15695
- https://vuldb.com/submit/856017
- https://vuldb.com/vuln/378242
- https://vuldb.com/vuln/378242/cti

### [CVE-2026-15696](https://github.com/cve-a/dexingzhiqing/issues/6)

> **Backend** / **HIGH** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-15696
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-15 00:17:00 JST
- 更新日: 2026-07-15 01:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Tenda BE12 Pro 16.03.66.23の/goform/VirtualSer内のfromVirtualSer関数にスタックベースのバッファオーバーフロー脆弱性が存在します。  
- 影響: リモートからの攻撃により、サービスの停止や任意コード実行の可能性があります。  
- 推奨対応: 最新のファームウェアへの更新や、該当機能へのアクセス制限を検討してください。

#### References
- https://github.com/cve-a/dexingzhiqing/issues/6
- https://vuldb.com/cve/CVE-2026-15696
- https://vuldb.com/submit/856019
- https://vuldb.com/vuln/378243
- https://vuldb.com/vuln/378243/cti

### [CVE-2026-15701](https://github.com/fu9-dotom/cve/issues/1)

> **Backend** / **HIGH** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-15701
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-15 02:16:45 JST
- 更新日: 2026-07-15 05:21:36 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Totolink NR1800X 9.1.0u.6279_B20210910のlighttpdコンポーネントの/formLogout.htm内のForm_Logout関数において、Host引数の操作によりスタックベースのバッファオーバーフローが発生する脆弱性が確認されました。  
- 影響: リモートからの攻撃が可能で、悪用されるとシステムの制御権を奪われる恐れがあります。  
- 推奨対応: 公式の修正パッチ適用またはファームウェアのアップデートを速やかに実施し、不審なアクセスを監視してください。

#### References
- https://github.com/fu9-dotom/cve/issues/1
- https://vuldb.com/cve/CVE-2026-15701
- https://vuldb.com/submit/856136
- https://vuldb.com/vuln/378248
- https://vuldb.com/vuln/378248/cti

### [CVE-2026-10714](https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1786.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-10714
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-15 00:16:55 JST
- 更新日: 2026-07-15 01:46:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: FactoryTalk® Services PlatformのOkta Web認証でJWT署名検証が回避される脆弱性が存在し、攻撃者が「none」アルゴリズムを設定して偽造トークンを作成可能です。  
- 影響: 低権限の認証済みユーザーが任意のユーザーを偽装し、システム設定への不正アクセスや他システムへの権限付与が可能になる恐れがあります。  
- 推奨対応: JWTアルゴリズムの検証強化や、ベンダーからの修正パッチ適用を検討し、不審なトークンの使用を監視してください。

#### References
- https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1786.html

### [CVE-2026-15698](https://github.com/kofrasa/mingo/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-15698
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-15 01:16:46 JST
- 更新日: 2026-07-15 02:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: kofrasa mingo 7.2.1以前のUpdate APIのupdate系関数において、引数Setの操作によりオブジェクトプロトタイプ属性が不適切に変更される脆弱性が存在します。  
- 影響: リモートからの攻撃により、予期しないオブジェクトの変更が発生し、セキュリティ上の問題が生じる可能性があります。  
- 推奨対応: 影響を受けるバージョンから7.2.2以降にアップグレードすることを推奨します。

#### References
- https://github.com/kofrasa/mingo/
- https://github.com/kofrasa/mingo/commit/fadc398251792c2ba441cbc539f359fc7943c0c2
- https://github.com/kofrasa/mingo/issues/606
- https://github.com/kofrasa/mingo/releases/tag/7.2.2
- https://vuldb.com/cve/CVE-2026-15698

### [CVE-2026-52841](https://github.com/alextselegidis/easyappointments/commit/4b2d245d2cd2058dc76e05f6eb65b26699268471)

> **Backend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-52841
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-15 01:17:00 JST
- 更新日: 2026-07-15 01:42:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Easy!Appointmentsの1.6.0未満のバージョンで、Google OAuthトークンの紐付け処理に不適切な検証があり、他のプロバイダーの同期を乗っ取る可能性があります。  
- 影響: ログイン済みの管理者やプロバイダーが他のユーザーのGoogleカレンダー同期を不正に操作でき、顧客情報が漏洩する恐れがあります。  
- 推奨対応: バージョン1.6.0以降にアップデートし、OAuthトークンの所有者検証が適切に行われるようにしてください。

#### References
- https://github.com/alextselegidis/easyappointments/commit/4b2d245d2cd2058dc76e05f6eb65b26699268471
- https://github.com/alextselegidis/easyappointments/security/advisories/GHSA-8hm4-r66f-29wr
- https://github.com/alextselegidis/easyappointments/security/advisories/GHSA-8hm4-r66f-29wr

### [CVE-2026-59204](https://github.com/python-pillow/Pillow/commit/13ada41172142f2fd9f0906f615a00ea623a11ca)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-59204: python pillow
- 関連キーワード: python, gin
- 影響製品: python pillow
- 公開日: 2026-07-15 01:17:02 JST
- 更新日: 2026-07-15 05:10:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PillowのJPEG2000画像デコード処理において、タイルごとにメモリ使用量を誤って累積する問題があり、細工された画像でメモリ不足を引き起こす可能性があります。  
- 影響: Pillowバージョン8.2.0から12.2.0までの間で、悪意あるJPEG2000画像によりメモリ不足やサービス停止が発生する恐れがあります。  
- 推奨対応: Pillowをバージョン12.3.0以降にアップデートし、脆弱性修正を適用してください。

#### References
- https://github.com/python-pillow/Pillow/commit/13ada41172142f2fd9f0906f615a00ea623a11ca
- https://github.com/python-pillow/Pillow/pull/9704
- https://github.com/python-pillow/Pillow/releases/tag/12.3.0
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-vjc4-5qp5-m44j

### [CVE-2026-54058](https://github.com/python-pillow/Pillow/commit/6a8de891fb00968e5ea79bfa84368ed90b3cfc1d)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-54058
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-07-15 02:17:03 JST
- 更新日: 2026-07-15 03:18:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Pillowの12.3.0未満のバージョンで、McIdas AREA画像の読み込み時に不正なヘッダーによりメモリ外参照が発生し、隣接メモリの情報漏洩やクラッシュが起こる可能性があります。  
- 影響: 攻撃者が細工した画像を読み込むことで、プロセスの隣接メモリ情報が漏洩するリスクがあります。  
- 推奨対応: Pillowをバージョン12.3.0以降にアップデートし、該当の脆弱性を修正してください。

#### References
- https://github.com/python-pillow/Pillow/commit/6a8de891fb00968e5ea79bfa84368ed90b3cfc1d
- https://github.com/python-pillow/Pillow/pull/9719
- https://github.com/python-pillow/Pillow/releases/tag/12.3.0
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-62p4-gmf7-7g93
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-62p4-gmf7-7g93

### [CVE-2026-59198](https://github.com/python-pillow/Pillow/commit/eada3cbd7fb9963ee90673fb7b5270124a0d5f4b)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59198: python pillow
- 関連キーワード: python, gin
- 影響製品: python pillow
- 公開日: 2026-07-15 01:17:01 JST
- 更新日: 2026-07-15 05:18:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PillowのTGA RLEエンコーダがモード1画像の保存時にバッファ外読み取りを行い、隣接するヒープメモリがTGAファイルにコピーされる可能性があります。  
- 影響: 不正な画像ファイル生成により、情報漏洩やメモリ破損のリスクが考えられます。  
- 推奨対応: Pillowをバージョン12.3.0以降にアップデートして問題を修正してください。

#### References
- https://github.com/python-pillow/Pillow/commit/eada3cbd7fb9963ee90673fb7b5270124a0d5f4b
- https://github.com/python-pillow/Pillow/pull/9709
- https://github.com/python-pillow/Pillow/releases/tag/12.3.0
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-fj7v-r99m-22gq
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-fj7v-r99m-22gq

### [CVE-2026-59199](https://github.com/python-pillow/Pillow/commit/ceefc348eb3c3844c7f9796ef2cc3a7dd5fbba7b)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59199: python pillow
- 関連キーワード: python, gin
- 影響製品: python pillow
- 公開日: 2026-07-15 01:17:01 JST
- 更新日: 2026-07-15 05:18:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Pythonの画像処理ライブラリPillowの12.3.0以前のバージョンにおいて、Image.paste()、Image.crop()、Image.alpha_composite()で符号付き32ビット整数の境界付近の座標を指定すると、ヒープの境界外書き込みが発生する可能性があります。  
- 影響: ヒープの境界外書き込みにより、プログラムの異常終了や潜在的なコード実行のリスクが考えられます。  
- 推奨対応: Pillowをバージョン12.3.0以降にアップデートして、この脆弱性を修正してください。

#### References
- https://github.com/python-pillow/Pillow/commit/ceefc348eb3c3844c7f9796ef2cc3a7dd5fbba7b
- https://github.com/python-pillow/Pillow/pull/9703
- https://github.com/python-pillow/Pillow/releases/tag/12.3.0
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-6r8x-57c9-28j4

### [CVE-2026-59203](https://github.com/python-pillow/Pillow/commit/03992618118b4a76b6163cd72ab5ecd684133b83)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59203: python pillow
- 関連キーワード: python, gin
- 影響製品: python pillow
- 公開日: 2026-07-15 01:17:02 JST
- 更新日: 2026-07-15 05:16:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PillowのEPSパーサーが負のバイト数を受け入れて無限ループを引き起こす脆弱性が12.0.0から12.2.0まで存在します。  
- 影響: 悪意のあるEPSファイルを処理するとImage.open()が無限ループに陥り、サービス拒否状態になる可能性があります。  
- 推奨対応: Pillowをバージョン12.3.0以降にアップデートして脆弱性を修正してください。

#### References
- https://github.com/python-pillow/Pillow/commit/03992618118b4a76b6163cd72ab5ecd684133b83
- https://github.com/python-pillow/Pillow/pull/9708
- https://github.com/python-pillow/Pillow/releases/tag/12.3.0
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-pg7v-jwj7-p798

### [CVE-2026-59205](https://github.com/python-pillow/Pillow/commit/a9ffc42bedf4fc0a7ef8d6486e7f9e81e3397721)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59205: python pillow
- 関連キーワード: python, gin
- 影響製品: python pillow
- 公開日: 2026-07-15 01:17:02 JST
- 更新日: 2026-07-15 05:09:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PillowのImageCms.ImageCmsTransform.apply関数で、出力画像のモードが変換の宣言された出力モードと一致しない場合にネイティブヒープ破損が発生する可能性があります。  
- 影響: 不適切な画像モード指定により、メモリ破損が起こりアプリケーションの異常終了やセキュリティリスクが生じる恐れがあります。  
- 推奨対応: Pillowをバージョン12.3.0以降にアップデートし、出力画像のモードを正しく指定することを推奨します。

#### References
- https://github.com/python-pillow/Pillow/commit/a9ffc42bedf4fc0a7ef8d6486e7f9e81e3397721
- https://github.com/python-pillow/Pillow/pull/9715
- https://github.com/python-pillow/Pillow/releases/tag/12.3.0
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-9hw9-ch79-4vh6
- https://github.com/python-pillow/Pillow/security/advisories/GHSA-9hw9-ch79-4vh6

### [CVE-2026-15265](https://www.tenable.com/security/tns-2026-18)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-15265
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-15 00:16:57 JST
- 更新日: 2026-07-15 01:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Tenable Agent 11.2.0および11.1.3以下において、パス・トラバーサルの脆弱性が存在し、特権攻撃者が意図しないディレクトリに任意のファイルを書き込める可能性があります。  
- 影響: 任意のファイル書き込みにより、リモートコード実行のリスクが生じる可能性があります。  
- 推奨対応: 最新バージョンへのアップデートや、アクセス権限の厳格な管理を検討してください。

#### References
- https://www.tenable.com/security/tns-2026-18

### [CVE-2026-58479](https://www.vulncheck.com/advisories/sustainable-irrigation-platform-rce-via-cli-control-plugin-command-injection)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-58479: dan-in-ca sustainable irrigation platform
- 関連キーワード: gin
- 影響製品: dan-in-ca sustainable irrigation platform
- 公開日: 2026-07-15 00:17:06 JST
- 更新日: 2026-07-15 03:45:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: dan-in-caのSustainable Irrigation Platform（バージョン5.2.16以前）に、認証なしまたはCSRF攻撃により任意のOSコマンドを実行可能なコマンドインジェクション脆弱性が存在します。  
- 影響: 攻撃者はプラットフォームのHTTPエンドポイントを介して悪意あるペイロードを保存し、灌漑ステーションの起動時に任意のコマンドを実行できる可能性があります。  
- 推奨対応: 公式の修正パッチ適用や、プラグインの使用制限、パスフレーズの強化を検討してください。

#### References
- https://www.vulncheck.com/advisories/sustainable-irrigation-platform-rce-via-cli-control-plugin-command-injection
- https://www.zeroscience.mk/#/advisories/ZSL-2026-5999

### [CVE-2026-58476](https://www.vulncheck.com/advisories/sustainable-irrigation-platform-csrf-via-administrative-get-requests)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-58476: dan-in-ca sustainable irrigation platform
- 関連キーワード: gin
- 影響製品: dan-in-ca sustainable irrigation platform
- 公開日: 2026-07-15 00:17:06 JST
- 更新日: 2026-07-15 04:10:30 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: dan-in-caのSustainable Irrigation Platform（SIP）バージョン5.2.16以前に、CSRF脆弱性が存在し、管理者が悪意あるページを訪問すると状態変更操作が実行される可能性があります。  
- 影響: パスフレーズ無効化、デバイス再起動、プログラム削除、プラグインインストールなどの管理操作が不正に行われる恐れがあり、デフォルト設定では認証なしでアクセス可能です。  
- 推奨対応: 最新バージョンへの更新、CSRF対策の実装、デフォルト認証情報の変更および適切な認証設定を行うことが推奨されます。

#### References
- https://www.vulncheck.com/advisories/sustainable-irrigation-platform-csrf-via-administrative-get-requests
- https://www.zeroscience.mk/#/advisories/ZSL-2026-5995

### [CVE-2026-14504](https://help.sonatype.com/en/sonatype-nexus-repository-3-94-0-release-notes.html)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-14504
- 関連キーワード: terraform
- 影響製品: -
- 公開日: 2026-07-15 01:16:45 JST
- 更新日: 2026-07-15 01:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nexus Repository 3のコンポーネントアップロードAPIにおいて、読み取り/閲覧権限のみのユーザーが任意のアーティファクトをアップロードできる認可バイパスの脆弱性が存在します。  
- 影響: 読み取り権限しかないユーザーが書き込み権限を回避して不正なファイルをアップロードできる可能性があります。  
- 推奨対応: ベンダーの提供する修正パッチの適用や、アクセス権限の見直しを行うことが推奨されます。

#### References
- https://help.sonatype.com/en/sonatype-nexus-repository-3-94-0-release-notes.html
- https://support.sonatype.com/hc/en-us/articles/53137654741907

### [CVE-2026-15736](https://github.com/snowflakedb/snowflake-sqlalchemy/releases)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-15736
- 関連キーワード: sqlalchemy
- 影響製品: -
- 公開日: 2026-07-15 00:17:01 JST
- 更新日: 2026-07-15 01:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Snowflake SQLAlchemy 1.11.0未満のバージョンにおいて、SQLインジェクションやローカルファイル読み取りの脆弱性が複数存在します。  
- 影響: 攻撃者が悪意ある入力を通じてデータベースの読み取り・改ざんやローカルファイルの情報漏洩を引き起こす可能性があります。  
- 推奨対応: 影響を受けるバージョンから1.11.0以降へアップデートし、ユーザー入力の検証を強化してください。

#### References
- https://github.com/snowflakedb/snowflake-sqlalchemy/releases

### [CVE-2026-55651](https://github.com/alextselegidis/easyappointments/security/advisories/GHSA-4vmm-5qvc-w5p7)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-55651
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-15 01:17:00 JST
- 更新日: 2026-07-15 01:42:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Easy!Appointments 1.5.2の顧客検索エンドポイントに過剰なデータ露出の脆弱性があり、認証ユーザーが他ユーザーの予約ハッシュを取得可能です。  
- 影響: 取得したハッシュを悪用し、他のプロバイダーの予約を改ざんまたは削除される恐れがあります。  
- 推奨対応: バージョン1.6.0へのアップデートを推奨します。

#### References
- https://github.com/alextselegidis/easyappointments/security/advisories/GHSA-4vmm-5qvc-w5p7
- https://github.com/alextselegidis/easyappointments/security/advisories/GHSA-4vmm-5qvc-w5p7

### [CVE-2026-8590](https://community.spotfire.com/articles/spotfire/spotfire-security-advisory-july-14-2026-spotfire-cve-2026-8590-r3641/)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-8590
- 関連キーワード: kubernetes
- 影響製品: -
- 公開日: 2026-07-15 00:17:10 JST
- 更新日: 2026-07-15 00:17:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Spotfireの複数の製品において、サーバーモジュールに影響する脆弱性が報告されています。  
- 影響: 攻撃者が不正にシステムにアクセスする可能性があり、機密情報の漏洩やサービスの妨害が懸念されます。  
- 推奨対応: ベンダーから提供される修正バージョンへのアップデートを検討し、適用することを推奨します。

#### References
- https://community.spotfire.com/articles/spotfire/spotfire-security-advisory-july-14-2026-spotfire-cve-2026-8590-r3641/

### [CVE-2026-58478](https://www.vulncheck.com/advisories/sustainable-irrigation-platform-ssrf-via-node-red-callback-url)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-58478: dan-in-ca sustainable irrigation platform
- 関連キーワード: gin
- 影響製品: dan-in-ca sustainable irrigation platform
- 公開日: 2026-07-15 00:17:06 JST
- 更新日: 2026-07-15 04:04:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: dan-in-caのSustainable Irrigation Platform（SIP）バージョン5.2.16以前に、Node-REDプラグイン使用時に認証なしで任意のHTTPリクエストを送信可能なSSRF脆弱性が存在します。  
- 影響: 攻撃者は内部ネットワークや外部の任意ホストに盲目的なHTTPリクエストを送信でき、情報漏洩や不正アクセスのリスクがあります。  
- 推奨対応: Node-REDプラグインの使用を見直し、可能であればアップデートや設定変更で送信先の検証を強化し、デフォルトのパスフレーズを変更してください。

#### References
- https://www.vulncheck.com/advisories/sustainable-irrigation-platform-ssrf-via-node-red-callback-url
- https://www.zeroscience.mk/#/advisories/ZSL-2026-5998

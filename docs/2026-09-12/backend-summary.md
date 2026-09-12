# Backend CVE Summary (2026-09-12)

## Overview

- 取得日時: 2026-09-12 09:12:37 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 24
- Critical: 1
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-3869](https://download.se.com/files?p_Doc_Ref=SEVD-2026-251-04&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2026-251-04.pdf)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-3869
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 01:17:06 JST
- 更新日: 2026-09-12 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CWE-303 : Incorrect Implementation of Authentication Algorithm vulnerability exists that could cause loss of confidentiality, integrity and availability of the PLC provided an application project with a lower application level is running on the PLC.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://download.se.com/files?p_Doc_Ref=SEVD-2026-251-04&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2026-251-04.pdf

### [CVE-2026-68497](https://github.com/FasterXML/jackson-databind/commit/a99b7e74c8928f43f6975773a8c862c8316178bd)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-68497
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-12 01:17:39 JST
- 更新日: 2026-09-12 02:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: jackson-databind binds a JSON string to a javax.xml.datatype.Duration or javax.xml.datatype.XMLGregorianCalendar field by passing the raw string verbatim to DatatypeFactory.newDuration(value) or newXMLGregorianCalendar(value) in CoreXMLDeserializers.Std._deserialize. These deserializers are registered by default with n...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FasterXML/jackson-databind/commit/a99b7e74c8928f43f6975773a8c862c8316178bd
- https://github.com/FasterXML/jackson-databind/pull/6127
- https://github.com/FasterXML/jackson-databind/security/advisories/GHSA-q4xh-88c3-wmh7
- https://github.com/FasterXML/jackson-databind/security/advisories/GHSA-q4xh-88c3-wmh7

### [CVE-2026-89090](https://aws.amazon.com/security/security-bulletins/2026-110-aws/)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-89090
- 関連キーワード: go, aws
- 影響製品: -
- 公開日: 2026-09-12 03:17:00 JST
- 更新日: 2026-09-12 05:19:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An unrecovered panic in the event stream header decoder in Amazon AWS SDK for Go v2 before release-2026-03-23 might allow an unauthenticated remote actor to terminate the consuming application process via a crafted event stream response frame containing a header value type outside the valid range. To remediate this iss...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-110-aws/
- https://github.com/aws/aws-sdk-go-v2/releases/tag/release-2026-03-23
- https://github.com/aws/aws-sdk-go-v2/security/advisories/GHSA-xmrv-pmrh-hhx2

### [CVE-2026-89099](https://jira.mongodb.org/browse/SERVER-134063)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-89099
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-12 03:17:00 JST
- 更新日: 2026-09-12 04:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A race condition in the document value layer of MongoDB Server can allow concurrent server threads to operate on the same internal memory without synchronization, leading to memory corruption. An authenticated user holding ordinary read-write privileges on a database may be able to trigger this condition over the norma...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/SERVER-134063

### [CVE-2026-82578](https://github.com/cisagov/CSAF/blob/develop/csaf_files/OT/white/2026/icsma-26-253-01.json)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-82578
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 00:17:06 JST
- 更新日: 2026-09-12 00:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: XMLバッチ処理でXPath選択時、外部エンティティの制限がないデフォルト設定が使用される脆弱性。
- 影響: XXE（XML外部実体）注入により、機密データの漏洩やサービス拒否（DoS）攻撃を受ける可能性がある。
- 推奨対応: XMLパーサーで外部エンティティの参照（DOCTYPE宣言）を無効化し、安全な設定へ更新する。

#### References
- https://github.com/cisagov/CSAF/blob/develop/csaf_files/OT/white/2026/icsma-26-253-01.json
- https://www.cisa.gov/news-events/ics-medical-advisories/icsma-26-253-01

### [CVE-2026-62139](https://patchstack.com/database/wordpress/plugin/google-site-kit/vulnerability/wordpress-site-kit-by-google-plugin-1-186-0-cross-site-request-forgery-csrf-vulnerability?_s_id=cve)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-62139
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 04:17:45 JST
- 更新日: 2026-09-12 06:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPressプラグイン Site Kit by Google 1.186.0 以下のバージョンにおける未認証のCSRF（クロスサイトリクエストフォージェリ）の脆弱性。
- 影響: 未認証の攻撃者が誘導等により、ユーザーの意図しないリクエストを実行させる可能性がある。
- 推奨対応: Site Kit by Google を 1.186.0 より後の修正バージョンにアップデートする。

#### References
- https://patchstack.com/database/wordpress/plugin/google-site-kit/vulnerability/wordpress-site-kit-by-google-plugin-1-186-0-cross-site-request-forgery-csrf-vulnerability?_s_id=cve

### [CVE-2026-89265](https://gitee.com/moxi159753/mogu_blog_v2/releases)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-89265
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 01:17:51 JST
- 更新日: 2026-09-12 06:17:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MoguBlog 6.2以下において、POST /pictureSort/getPictureSortByUid エンドポイントで権限検証アノテーションが欠落している脆弱性。
- 影響: 権限のないログイン済みバックオフィスユーザーが、制限された画像カテゴリのメタデータ（名称、UID、タイムスタンプ等）を取得できる可能性がある。
- 推奨対応: 該当エンドポイントに適切な権限チェックを追加した修正バージョンへ更新する。

#### References
- https://gitee.com/moxi159753/mogu_blog_v2/releases
- https://github.com/LinYuanyi1/cve-request-poc/blob/master/mogublog-poc/C13_pictureSort_getByUid_bfla.py
- https://github.com/moxi624/mogu_blog_v2
- https://github.com/moxi624/mogu_blog_v2/blob/025d78c7ac7e19b1abf796fa3cc158d855723d15/mogu_admin/src/main/java/com/moxi/mogublog/admin/restapi/PictureSortRestApi.java
- https://www.vulncheck.com/advisories/mogublog-through-6.2-missing-authorization-on-the-admin-getpicturesortbyuid-endpoint

### [CVE-2026-80939](https://git.kernel.org/stable/c/667c12782aaf8dd3cb2213e528fe63a73cb63345)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80939
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-12 05:18:58 JST
- 更新日: 2026-09-12 05:18:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのrtw89 PCI Wi-Fiドライバにおいて、ウォームリブート時にrfkillポーリングを停止する .shutdown コールバックが実装されていない脆弱性。
- 影響: リブート処理中に非同期SError割り込みが発生し、カーネルパニックを引き起こす可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルバージョンに更新する。

#### References
- https://git.kernel.org/stable/c/667c12782aaf8dd3cb2213e528fe63a73cb63345
- https://git.kernel.org/stable/c/c1f214dd1351244156deb57761b14190a233aef6

### [CVE-2026-80977](https://git.kernel.org/stable/c/0370da114a9bc044e248b85c6809d1b5e0c1f7f9)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80977
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-12 05:19:04 JST
- 更新日: 2026-09-12 05:19:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの net: skbuff において、skb_tx_error() が共有されたゼロコピー状態（skb_shinfo）を誤って操作する脆弱性。
- 影響: パケット転送中にマーカーが削除され、ネットワーク処理の誤作動やメモリ整合性の問題を引き起こす可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルバージョンに更新する。

#### References
- https://git.kernel.org/stable/c/0370da114a9bc044e248b85c6809d1b5e0c1f7f9
- https://git.kernel.org/stable/c/15aa81b390d401abf4b8211042470e9e92e3b7fb
- https://git.kernel.org/stable/c/288f9970670841044ab030104fa6b6ed159949d0
- https://git.kernel.org/stable/c/f66bdb1cc0fcd227a062378f8be0b5873aa5600a

### [CVE-2026-80989](https://git.kernel.org/stable/c/3c8b26ebf525ba5960510f48c6e9936a79ebe76f)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80989
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-12 05:19:05 JST
- 更新日: 2026-09-12 05:19:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの net: thunderbolt ドライバにおいて、接続確立の失敗時に login_sent フラグがクリアされない脆弱性。
- 影響: teardown 処理の重複実行による警告や、他で利用中のリソースが誤って解放される可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルバージョンに更新する。

#### References
- https://git.kernel.org/stable/c/3c8b26ebf525ba5960510f48c6e9936a79ebe76f
- https://git.kernel.org/stable/c/d6c0af293129345a17dc31c9b4179dc7f3d6af7a
- https://git.kernel.org/stable/c/ed1d6e3d735e7b03f43a02f4306c89eb7663da14
- https://git.kernel.org/stable/c/f01e6a35c440b62f060e21f36b385e574a7f308c

### [CVE-2026-80997](https://git.kernel.org/stable/c/30cef9c1229a36a9c80edb29296459849a2fbaa3)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80997
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-12 05:19:06 JST
- 更新日: 2026-09-12 05:19:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの Qualcomm IPA ドライバにおいて、ランタイムレジューム中にTXキューの再開処理が早期に消費される脆弱性。
- 影響: モデムの送信（TX）キューが永久に停止し、ネットワーク送信が不全に陥る可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルバージョンに更新する。

#### References
- https://git.kernel.org/stable/c/30cef9c1229a36a9c80edb29296459849a2fbaa3
- https://git.kernel.org/stable/c/30d5226bac52073c91ce85c2dcff93b866baefdb
- https://git.kernel.org/stable/c/3cbfd627ee720f3d2460d2cbe2fe9e4130240db6
- https://git.kernel.org/stable/c/62da38b4b3a0dd74a3e0eecf4992d40385924205

### [CVE-2026-81915](https://documentation.concretecms.org/developers/introduction/version-history/953-release-notes)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-81915
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 05:19:14 JST
- 更新日: 2026-09-12 05:19:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Concrete CMS 9.5.3 未満において、Page Typeの更新時にオブジェクトレベルのアクセス制御（canEditPageType）が不足している脆弱性。
- 影響: 特定のPage Typeの編集権限を持つダッシュボードユーザーが、割り当てられた権限外のPage Type設定を変更できる可能性がある。
- 推奨対応: Concrete CMS を 9.5.3 以降の修正バージョンにアップデートする。

#### References
- https://documentation.concretecms.org/developers/introduction/version-history/953-release-notes

### [CVE-2026-80931](https://git.kernel.org/stable/c/169ae5e65e5aaf213b6a578f6478a9fd2e523606)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80931
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 05:18:56 JST
- 更新日: 2026-09-12 05:18:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの DS28E17 1-Wire to I2C ブリッジドライバにおいて、I2Cブロック読み込み時に受領サイズの上限チェックが不十分な脆弱性。
- 影響: 最大34バイトのバッファに対して過大な長さを読み込み、境界外メモリ読み取りが発生する可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルバージョンに更新する。

#### References
- https://git.kernel.org/stable/c/169ae5e65e5aaf213b6a578f6478a9fd2e523606
- https://git.kernel.org/stable/c/6df05f630c84a109736642362e452089886f9974
- https://git.kernel.org/stable/c/ae0c79a8527044e54d81fd5a3b49ce6177633758
- https://git.kernel.org/stable/c/cb55c5da9828f77db2a2701316949d4de1e9b773

### [CVE-2026-80936](https://git.kernel.org/stable/c/304470333b7f525b23699ea7a7aed3b40ca37ca9)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80936
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 05:18:57 JST
- 更新日: 2026-09-12 05:18:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの mt7925 Wi-Fiドライバにおいて、デバイス停止時に mlo_pm_work の遅延タイマーがキャンセルされない脆弱性。
- 影響: デバイス解放後にタイマーが発火し、消失したワークキューへの登録試行による警告や不具合が発生する可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルバージョンに更新する。

#### References
- https://git.kernel.org/stable/c/304470333b7f525b23699ea7a7aed3b40ca37ca9
- https://git.kernel.org/stable/c/81faf578320df2dfc682a96baa6e85851dd68b6f
- https://git.kernel.org/stable/c/9e20da749ad229a1aa649ece528721b9652f15e1

### [CVE-2026-80961](https://git.kernel.org/stable/c/5ac38f4b4862fad6e7270fde5c3356a822ce74ca)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80961
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 05:19:01 JST
- 更新日: 2026-09-12 05:19:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのdm-pcacheにおける、ksetのkey_numおよびセグメント内境界の検証不備。
- 影響: キャッシュデバイスを提示可能な攻撃者によって境界外読み取りが引き起こされ、永続メモリ内のデータがユーザー空間に漏洩する可能性があります。
- 推奨対応: 対策が組み込まれたLinuxカーネルバージョンに更新してください。

#### References
- https://git.kernel.org/stable/c/5ac38f4b4862fad6e7270fde5c3356a822ce74ca
- https://git.kernel.org/stable/c/d8caf96040a06096276ab72f5e1e8547c014c564
- https://git.kernel.org/stable/c/f11deb032fd84081e7831cffcba895d893054a22

### [CVE-2026-80983](https://git.kernel.org/stable/c/719296c4aa8213d4ac8002e77d5956d436bc98d0)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80983
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 05:19:04 JST
- 更新日: 2026-09-12 05:19:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのnet/smcモジュールにおける、smc_switch_conns()でのエラー復帰時のソケット参照カウント（sk_refcnt）解放漏れ。
- 影響: ソケットや関連バッファが破棄されずメモリーリークが発生し、ネットワークネームスペースの解体が不能になる可能性があります。
- 推奨対応: 対策が組み込まれたLinuxカーネルバージョンに更新してください。

#### References
- https://git.kernel.org/stable/c/719296c4aa8213d4ac8002e77d5956d436bc98d0
- https://git.kernel.org/stable/c/84dea0585f6b538ae895a8b1d025f4897737f3b1
- https://git.kernel.org/stable/c/d89dc1bd8845c669a700eee58c64ebd3cc1b6d2d
- https://git.kernel.org/stable/c/d9a879ac25958bdaecb669ce70e58f8e2ff170de

### [CVE-2026-80990](https://git.kernel.org/stable/c/1c361f6cf39be7cc0ce37c0b67bd1cdf74b0a0c1)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80990
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 05:19:05 JST
- 更新日: 2026-09-12 05:19:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのnet/thunderboltにおいて、要求と異なるHopIDが割り当てられた際に不要なRx HopIDの解放が漏れる問題。
- 影響: 不要な割当リソースが解放されずに残り続け、リソースリークが発生する可能性があります。
- 推奨対応: 対策が組み込まれたLinuxカーネルバージョンに更新してください。

#### References
- https://git.kernel.org/stable/c/1c361f6cf39be7cc0ce37c0b67bd1cdf74b0a0c1
- https://git.kernel.org/stable/c/2f1463554d0561a2fead81e3888604e5c1125e29
- https://git.kernel.org/stable/c/61ff3c353e5d2ff4eb9d0b6d8d9e47805b136eea
- https://git.kernel.org/stable/c/9eac1817bfc5fa76e3a2d1b8fd824cc6ef5a9ab0

### [CVE-2026-81000](https://git.kernel.org/stable/c/0ada54ea63e48b9c1608e917ccb7dfadbe86db28)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-81000
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 05:19:07 JST
- 更新日: 2026-09-12 05:19:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのnet/tunにおける受信用ヘッドルーム境界チェックの不備。
- 影響: 過大なヘッドルーム要求によりSKBバッファの位置が正しく計算されず、領域外アクセスやシステムの不安定化を引き起こす可能性があります。
- 推奨対応: 対策が組み込まれたLinuxカーネルバージョンに更新してください。

#### References
- https://git.kernel.org/stable/c/0ada54ea63e48b9c1608e917ccb7dfadbe86db28
- https://git.kernel.org/stable/c/379d85c7f25f3e05a428225e6b8a65613c6e9b9d
- https://git.kernel.org/stable/c/447c9303942c439a117d9b76ce6d6e2116b38ee7
- https://git.kernel.org/stable/c/e098d9cc8859614a7f7baebc96e32a5a16b18ed2

### [CVE-2026-81005](https://git.kernel.org/stable/c/53af3a8bae0a93c1342e1b5519812203332aca8e)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-81005
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-12 05:19:09 JST
- 更新日: 2026-09-12 05:19:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのIPMI siドライバーにおける、BMCデバイスID取得失敗後のエラー処理時の不備。
- 影響: 初期化失敗時にNULLポインタ参照等が発生し、カーネルパニックやシステムの不具合を引き起こす可能性があります。
- 推奨対応: 対策が組み込まれたLinuxカーネルバージョンに更新してください。

#### References
- https://git.kernel.org/stable/c/53af3a8bae0a93c1342e1b5519812203332aca8e
- https://git.kernel.org/stable/c/6d920a75df9a83ab096b3cde7a643b656e4fdfeb
- https://git.kernel.org/stable/c/8ada17dd4c4ffd6b94621e735d77eda196ce118f
- https://git.kernel.org/stable/c/d4be659a3e56f4eb16039ab8a1162efea086a714

### [CVE-2026-81014](https://git.kernel.org/stable/c/4c6374dcb270d12907b880cf82a5a5ef21785fc3)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-81014
- 関連キーワード: python, gin, echo
- 影響製品: -
- 公開日: 2026-09-12 05:19:10 JST
- 更新日: 2026-09-12 05:19:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのhp-bioscfgドライバー（sk_storeおよびkek_store）におけるヒープ領域外読み取りの脆弱性。
- 影響: sysfs経由で末尾に改行を含むデータを書き込んだ場合、1バイトのヒープバッファオーバーリードが発生し情報漏洩や不具合を引き起こす可能性があります。
- 推奨対応: 対策が組み込まれたLinuxカーネルバージョンに更新してください。

#### References
- https://git.kernel.org/stable/c/4c6374dcb270d12907b880cf82a5a5ef21785fc3
- https://git.kernel.org/stable/c/67b60703d7d8af1ca0e49f72e1bdb1ccecd41b5b
- https://git.kernel.org/stable/c/7cd8fe01aba303a2382db0966eb6c8ab41d5f3c2
- https://git.kernel.org/stable/c/a7508c7959ff8d037327d377ed21a9c0eabe4674

### [CVE-2026-18061](https://aws.amazon.com/security/security-bulletins/2026-109-aws/)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-18061
- 関連キーワード: gin, aws
- 影響製品: -
- 公開日: 2026-09-12 02:17:08 JST
- 更新日: 2026-09-12 05:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AWS Advanced JDBC WrapperのRemoteQueryCachePluginにおけるXXE（XML外部実体参照）の脆弱性。
- 影響: 共有キャッシュへの書き込み権限を持つ攻撃者が、キャッシュ結果を読み取るアプリケーションホストから機密ファイル（認証情報等）を閲覧・漏洩させる可能性があります。
- 推奨対応: AWS Advanced JDBC Wrapperをバージョン 4.3.0 以降へアップデートしてください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-109-aws/
- https://github.com/aws/aws-advanced-jdbc-wrapper/releases/tag/4.3.0
- https://github.com/aws/aws-advanced-jdbc-wrapper/security/advisories/GHSA-fpvp-qwgm-v6h9

### [CVE-2026-72708](https://blog.lexfo.fr/casse-spip-sqli-to-rce.html)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-72708
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-09-12 02:18:57 JST
- 更新日: 2026-09-12 02:35:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SPIPの公開sitemapエンドポイントにおけるエスケープ処理の不備に起因するブラインドSQLインジェクションの脆弱性。
- 影響: 未認証の遠隔の攻撃者が任意SQLを実行し、データベース内の任意情報（nonce署名用シークレット等）を奪取する可能性があります。
- 推奨対応: SPIPをバージョン 4.4.18 以降へアップデートしてください。

#### References
- https://blog.lexfo.fr/casse-spip-sqli-to-rce.html
- https://blog.spip.net/Mise-a-jour-critique-de-securite-sortie-de-SPIP-4-4-18.html
- https://www.vulncheck.com/advisories/spip-unauthenticated-sql-injection-via-sitemap-annee-parameter

### [CVE-2026-15439](https://plugins.trac.wordpress.org/browser/gamipress/tags/7.9.3/integrations/wpforo/includes/functions.php#L24)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-15439
- 関連キーワード: gin, mysql
- 影響製品: -
- 公開日: 2026-09-12 01:17:05 JST
- 更新日: 2026-09-12 03:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用GamiPressプラグインにおけるwpForo統合AJAXセレクターの'q'パラメータのSQLインジェクションの脆弱性。
- 影響: 購読者（Subscriber）以上の権限を持つ攻撃者が、エスケープ不備を利用して任意SQLを実行しデータベース情報を漏洩させる可能性があります。
- 推奨対応: GamiPressプラグインを最新バージョン（7.9.7より後）へアップデートしてください。

#### References
- https://plugins.trac.wordpress.org/browser/gamipress/tags/7.9.3/integrations/wpforo/includes/functions.php#L24
- https://plugins.trac.wordpress.org/browser/gamipress/tags/7.9.3/integrations/wpforo/includes/functions.php#L40
- https://www.wordfence.com/threat-intel/vulnerabilities/id/72ad7420-5793-496e-8607-2b346c7a3ce5?source=cve

### [CVE-2026-89263](https://gitee.com/moxi159753/mogu_blog_v2/releases)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-89263
- 関連キーワード: redis
- 影響製品: -
- 公開日: 2026-09-12 01:17:51 JST
- 更新日: 2026-09-12 02:35:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MoguBlogにおける/web/comment/closeEmailNotificationエンドポイントの認証不備。
- 影響: 未認証の攻撃者が任意のユーザーのメール通知フラグを改ざんし、返信通知を停止させる可能性があります。
- 推奨対応: MoguBlogを修正版へアップデートするか、該当エンドポイントへの適切な認証・認可制御を導入してください。

#### References
- https://gitee.com/moxi159753/mogu_blog_v2/releases
- https://github.com/LinYuanyi1/cve-request-poc/blob/master/mogublog-poc/C08_comment_closeEmailNotification.py
- https://github.com/moxi624/mogu_blog_v2
- https://github.com/moxi624/mogu_blog_v2/blob/025d78c7ac7e19b1abf796fa3cc158d855723d15/mogu_web/src/main/java/com/moxi/mogublog/web/config/WebSecurityConfig.java
- https://github.com/moxi624/mogu_blog_v2/blob/025d78c7ac7e19b1abf796fa3cc158d855723d15/mogu_web/src/main/java/com/moxi/mogublog/web/restapi/CommentRestApi.java

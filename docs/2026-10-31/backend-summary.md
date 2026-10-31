# Backend CVE Summary (2026-10-31)

## Overview

- 取得日時: 2026-10-31 10:32:06 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 11
- Critical: 3
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-61730](https://github.com/socfortress/CoPilot/commit/bfa630b65d554670c7462a32ce6fd4e3cbd0254c)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-61730
- 関連キーワード: go, aws
- 影響製品: -
- 公開日: 2026-10-31 00:16:53 JST
- 更新日: 2026-10-31 02:13:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SOCFortress CoPilot の `/scoutsuite-report` ディレクトリに対する不適切なアクセス制御の脆弱性。
- 影響: 未認証の攻撃者がクラウド環境（AWS/Azure/GCP）の構成レポートや、アップロードされたGoogleサービスアカウントのJSONキーを閲覧・取得できる可能性があります。
- 推奨対応: 対象パスへの認証の強制、公開ディレクトリの構成見直し、または修正プログラムを適用してください。

#### References
- https://github.com/socfortress/CoPilot/commit/bfa630b65d554670c7462a32ce6fd4e3cbd0254c
- https://github.com/socfortress/CoPilot/pull/940
- https://github.com/socfortress/CoPilot/security/advisories/GHSA-pm2w-mmc3-h8hc
- https://github.com/socfortress/CoPilot/tree/v0.1.77

### [CVE-2026-61826](https://github.com/morpheus65535/bazarr/commit/4bd29252feebd0803e84cc3ce1bdd24c3a076ed4)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-61826
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-31 02:17:27 JST
- 更新日: 2026-10-31 04:39:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: BazarrのPlex OAuth関連APIエンドポイントにおいて適切な認証チェックが欠落している脆弱性。
- 影響: 未認証の第三者がPlex連携の解除、任意のAPIキー設定、または攻撃者のPlexアカウントの接続などを行う可能性がある。
- 推奨対応: Bazarrをバージョン 1.5.7-beta.14 以降へアップデートする。

#### References
- https://github.com/morpheus65535/bazarr/commit/4bd29252feebd0803e84cc3ce1bdd24c3a076ed4
- https://github.com/morpheus65535/bazarr/commit/f9a8a9514944be0e7b826e67cde042cebfe9c97e
- https://github.com/morpheus65535/bazarr/security/advisories/GHSA-fvcv-hh55-x3r4
- https://github.com/morpheus65535/bazarr/tree/v1.5.7-beta.14

### [CVE-2026-93327](https://docs.cloud.google.com/support/bulletins)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-93327
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-31 00:16:56 JST
- 更新日: 2026-10-31 04:37:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Google Cloud Application IntegrationのSubWorkflowタスクにおける不適切なデシリアライゼーションの脆弱性。
- 影響: 認証された攻撃者が悪意のあるシリアル化オブジェクトを送信することで、任意のコードを実行できる可能性がある。
- 推奨対応: クラウド側で2026年9月11日にパッチが適用されているため、ユーザー側での追加対応は不要とされている。

#### References
- https://docs.cloud.google.com/support/bulletins

### [CVE-2026-119300](https://github.com/wekan/wekan/commit/4ce5cf6e102854d326e1dcacde6cd20614525dec)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-119300
- 関連キーワード: go, express, mongodb
- 影響製品: -
- 公開日: 2026-10-31 02:17:18 JST
- 更新日: 2026-10-31 02:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Wekanのユーザー検索処理において、入力文字列がエスケープされずに正規表現（`new RegExp()`）へ渡される脆弱性。
- 影響: 認証されたユーザーが破滅的バックトラッキングを引き起こす正規表現を送信し、データベースのCPUリソースを枯渇させてサービス拒否（DoS）を引き起こす可能性がある。
- 推奨対応: Wekanをバージョン 11.11 以降にアップデートする。

#### References
- https://github.com/wekan/wekan/commit/4ce5cf6e102854d326e1dcacde6cd20614525dec
- https://github.com/wekan/wekan/releases/tag/v11.11
- https://github.com/wekan/wekan/security/advisories/GHSA-9846-cj96-6hv5

### [CVE-2026-50000](https://github.com/freedomofpress/securedrop/commit/cbe60cd68b67f44ffdd44c364c71cc71b40acfb5)

> **Backend** / **MEDIUM** / CVSS: **5.0** / KEV: **no**

- タイトル: CVE-2026-50000
- 関連キーワード: go, redis
- 影響製品: -
- 公開日: 2026-10-31 02:17:25 JST
- 更新日: 2026-10-31 04:37:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SecureDropのJournalist Interfaceにおいて、Redis内のセッションキー接頭辞の競合によりAPIセッションとWeb UIセッションの分離が不十分となる脆弱性。
- 影響: 攻撃者が有効なAPIセッショントークンを保有している場合、トークンの有効期限内であればWeb UIに対してそのトークンを再利用してアクセスできる可能性がある。
- 推奨対応: 修正済みの最新バージョンへアップデートする。

#### References
- https://github.com/freedomofpress/securedrop/commit/cbe60cd68b67f44ffdd44c364c71cc71b40acfb5
- https://github.com/freedomofpress/securedrop/releases/tag/2.16.0
- https://github.com/freedomofpress/securedrop/security/advisories/GHSA-78xq-8jf3-gpfx

### [CVE-2026-118696](https://blog.jetbrains.com/security/2026/10/compromised-emudhra-certificates-ides/)

> **Backend** / **HIGH** / CVSS: **8.0** / KEV: **no**

- タイトル: CVE-2026-118696
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-31 03:17:24 JST
- 更新日: 2026-10-31 04:37:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JetBrainsの各種IDE製品に組み込まれたブラウザにおいて、失効した中間証明書を誤って信頼してしまう脆弱性。
- 影響: 中間者攻撃（MitM）などの通信上の問題により、暗号化通信の安全性や整合性が損なわれる可能性がある。
- 推奨対応: 該当するJetBrains製品（IntelliJ IDEA、PyCharm等）を修正済みバージョンへ更新する。

#### References
- https://blog.jetbrains.com/security/2026/10/compromised-emudhra-certificates-ides/
- https://bugzilla.mozilla.org/show_bug.cgi?id=2083449
- https://emudhra.com/en/post/certificate-security-incident
- https://www.jetbrains.com/privacy-security/issues-fixed/

### [CVE-2026-119655](https://github.com/CoreUnion/CoreShop)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-119655
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-31 00:16:49 JST
- 更新日: 2026-10-31 00:16:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CoreShop（1.5.5以下）の `api/Good/GetGoodsPageList` エンドポイントにおける `order` パラメータに対するSQLインジェクションの脆弱性。
- 影響: 未認証の攻撃者がブラインドSQLインジェクションを実行し、会員アカウントや注文情報などのデータベース内の情報を不正に取得する可能性がある。
- 推奨対応: CoreShopを修正済みバージョンへアップデートする。

#### References
- https://github.com/CoreUnion/CoreShop
- https://github.com/CoreUnion/CoreShop/blob/v1.5.5/CoreCms.Net.Repository/BaseRepository.cs#L155-L165
- https://github.com/CoreUnion/CoreShop/blob/v1.5.5/CoreCms.Net.Web.WebApi/Controllers/GoodController.cs#L233-L241
- https://github.com/CoreUnion/CoreShop/commit/0453011fe2a5abc4c202894ed1d9e87b2accc9e4
- https://github.com/CoreUnion/CoreShop/issues/20

### [CVE-2026-119656](https://github.com/CoreUnion/CoreShop)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-119656
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-31 00:16:49 JST
- 更新日: 2026-10-31 00:16:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CoreShop（1.5.5以下）の `api/Agent/GetGoodsPageList` エンドポイントにおける `order` パラメータに対するSQLインジェクションの脆弱性。
- 影響: 未認証の攻撃者がブラインドSQLインジェクションを実行し、会員アカウントや注文情報などを不正に抽出する可能性がある。
- 推奨対応: CoreShopを修正済みバージョンへアップデートする。

#### References
- https://github.com/CoreUnion/CoreShop
- https://github.com/CoreUnion/CoreShop/blob/v1.5.5/CoreCms.Net.Repository/Good/CoreCmsGoodsRepository.cs#L1622-L1730
- https://github.com/CoreUnion/CoreShop/blob/v1.5.5/CoreCms.Net.Web.WebApi/Controllers/AgentController.cs#L164-L170
- https://github.com/CoreUnion/CoreShop/commit/e40085b81d78ea55790305bc4a1592309b294048
- https://github.com/CoreUnion/CoreShop/issues/20

### [CVE-2026-55551](https://github.com/infonl/dimpact-zaakafhandelcomponent/commit/7b90586be658cec9fa5c98c0838636237f40931f)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-55551
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-31 02:17:25 JST
- 更新日: 2026-10-31 04:39:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: 自治体向け案件管理システムZACにおいて、特定のID指定読み取りエンドポイントで認可チェックが欠落している脆弱性。
- 影響: 認証された低権限ユーザーが案件や決定のUUIDを知っている場合、本来アクセス権のない決定情報や監査履歴などを閲覧できる可能性がある。
- 推奨対応: ZACをバージョン 5.2.0 以降へアップデートする。

#### References
- https://github.com/infonl/dimpact-zaakafhandelcomponent/commit/7b90586be658cec9fa5c98c0838636237f40931f
- https://github.com/infonl/dimpact-zaakafhandelcomponent/commit/d050f247301a1bcfb867015725a693c540a06f5a
- https://github.com/infonl/dimpact-zaakafhandelcomponent/pull/6225
- https://github.com/infonl/dimpact-zaakafhandelcomponent/pull/6229
- https://github.com/infonl/dimpact-zaakafhandelcomponent/releases/tag/v5.2.0

### [CVE-2026-102905](https://plugins.trac.wordpress.org/browser/ad-inserter/tags/2.8.19/ad-inserter.php#L12974)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-102905
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-31 03:17:14 JST
- 更新日: 2026-10-31 03:33:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用プラグイン「Ad Inserter – Ad Manager & AdSense Ads」（2.8.19以下）において、入力検証不備により任意のショートコードが実行される脆弱性。
- 影響: 特定の動的タグ構成が有効な場合、未認証の第三者によって任意のショートコードを実行される可能性がある。
- 推奨対応: プラグインを最新バージョンにアップデートする。

#### References
- https://plugins.trac.wordpress.org/browser/ad-inserter/tags/2.8.19/ad-inserter.php#L12974
- https://plugins.trac.wordpress.org/browser/ad-inserter/tags/2.8.19/ad-inserter.php#L13142
- https://plugins.trac.wordpress.org/browser/ad-inserter/tags/2.8.19/class.php#L3297
- https://plugins.trac.wordpress.org/changeset/3770281/ad-inserter/trunk/ad-inserter.php
- https://www.wordfence.com/threat-intel/vulnerabilities/id/a36f813c-97c5-466d-92e0-7341c12b5a46?source=cve

### [CVE-2026-119298](https://github.com/schollz/croc/commit/25fe49b6f14db99f517e902cfef76299ad0a95a3)

> **Backend** / **MEDIUM** / CVSS: **4.2** / KEV: **no**

- タイトル: CVE-2026-119298
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-31 02:17:18 JST
- 更新日: 2026-10-31 04:39:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ファイル転送ツール croc において、受信用ファイル名の処理で `croc-stdin-` プレフィックスを持つファイルの上書き確認がスキップされる脆弱性。
- 影響: 受信者がファイル転送を承諾した際、攻撃者が予測可能な同名ファイルを作成・送信することで、確認なしに対象ファイルを上書きまたは置換される可能性がある。
- 推奨対応: crocをバージョン 11.5.2 以降にアップデートする。

#### References
- https://github.com/schollz/croc/commit/25fe49b6f14db99f517e902cfef76299ad0a95a3
- https://github.com/schollz/croc/pull/1327
- https://github.com/schollz/croc/releases/tag/v11.5.2
- https://github.com/schollz/croc/security/advisories/GHSA-x89h-7h96-v88f

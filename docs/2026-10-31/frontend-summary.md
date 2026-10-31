# Frontend CVE Summary (2026-10-31)

## Overview

- 取得日時: 2026-10-31 10:32:06 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 19
- Critical: 3
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-119715](https://github.com/nocodb/nocodb)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-119715
- 関連キーワード: vite, gin
- 影響製品: -
- 公開日: 2026-10-31 01:17:54 JST
- 更新日: 2026-10-31 04:23:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NocoDB（2026.08.0未満）におけるクリックジャッキングの脆弱性。レスポンスヘッダー（X-Frame-OptionsおよびCSP frame-ancestors）が設定されていないことが原因です。
- 影響: 攻撃者のWebページに認証済み画面をフレーム表示され、ユーザーの誤操作によってレコードの変更・削除や設定変更などが行われる可能性があります。
- 推奨対応: NocoDB 2026.08.0 以降へアップデートしてください。

#### References
- https://github.com/nocodb/nocodb
- https://github.com/nocodb/nocodb/commit/42128735eba328d157c2e90b98795cb248dc0847
- https://github.com/nocodb/nocodb/releases/tag/2026.08.0
- https://github.com/nocodb/nocodb/security/advisories/GHSA-3rj6-rvwh-j2xg
- https://www.vulncheck.com/advisories/nocodb-before-2026.08.0-clickjacking-via-missing-frame-control-headers

### [CVE-2026-61728](https://github.com/socfortress/CoPilot/commit/461e8f84794aee8ada588de3bad79430dc9f4f3d)

> **Frontend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-61728
- 関連キーワード: javascript, vue, gin
- 影響製品: -
- 公開日: 2026-10-31 00:16:52 JST
- 更新日: 2026-10-31 02:13:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SOCFortress CoPilot（0.1.70および0.1.76未満の該当コード）における蓄積型クロスサイトスクリプティング（Stored XSS）の脆弱性。コメントやケース、資産情報などの描画時にHTMLのサニタイズ処理が行われず `v-html` で出力されることが原因です。
- 影響: 悪意あるスクリプトが保存され、他のユーザーが該当項目を閲覧した際にセッション情報の窃取や不正操作が実行される可能性があります。
- 推奨対応: 修正が含まれるバージョン（0.1.70 または 0.1.76 以降）へアップデートしてください。

#### References
- https://github.com/socfortress/CoPilot/commit/461e8f84794aee8ada588de3bad79430dc9f4f3d
- https://github.com/socfortress/CoPilot/commit/ab9078bdee5d1c737f37f481103984665a670bdd
- https://github.com/socfortress/CoPilot/pull/904
- https://github.com/socfortress/CoPilot/pull/938
- https://github.com/socfortress/CoPilot/security/advisories/GHSA-8hqj-cqcc-5f6w

### [CVE-2026-61737](https://github.com/huajian123/ng-antd-admin/commit/23e92ff9176074ee534af3ea3700b3652a9726a9)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-61737
- 関連キーワード: angular, nestjs
- 影響製品: -
- 公開日: 2026-10-31 00:16:53 JST
- 更新日: 2026-10-31 04:39:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ng-antd-admin（バージョン22.0未満）におけるハードコードされたデフォルトJWTシークレットの脆弱性。デフォルトの鍵が変更されずに使用されている場合に発生します。
- 影響: 攻撃者が認証トークンを偽造して認証・認可を回避し、管理者を含む任意のユーザーになりすましてデータの閲覧や不正な操作を行う可能性があります。
- 推奨対応: ng-antd-admin 22.0 以降にアップデートし、本番環境で独自の安全なJWTシークレットを設定してください。

#### References
- https://github.com/huajian123/ng-antd-admin/commit/23e92ff9176074ee534af3ea3700b3652a9726a9
- https://github.com/huajian123/ng-antd-admin/releases/tag/v22.0
- https://github.com/huajian123/ng-antd-admin/security/advisories/GHSA-qphq-m2hv-wj5h

### [CVE-2026-119978](https://github.com/FlowiseAI/Flowise)

> **Frontend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-119978
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-31 03:17:27 JST
- 更新日: 2026-10-31 03:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Flowise（バージョン3.1.4まで）におけるサンドボックス回避の脆弱性。`ALLOW_BUILTIN_DEP=true` 設定時にホワイトリスト化された依存関係（langchain/mammoth）を悪用してvm2サンドボックスを脱出できます。
- 影響: 認証された攻撃者が `/api/v1/node-custom-function` 経由で任意のOSコマンドを実行する可能性があります。
- 推奨対応: 修正バージョンの適用や、不必要な組み込み依存関係の無効化（`ALLOW_BUILTIN_DEP` の見直し）を検討してください。

#### References
- https://github.com/FlowiseAI/Flowise
- https://github.com/FlowiseAI/Flowise/blob/a65f81bb43ef66d3ce734bf0dff4223ae8041c95/packages/components/src/utils.ts#L1733
- https://github.com/FlowiseAI/Flowise/blob/a65f81bb43ef66d3ce734bf0dff4223ae8041c95/packages/components/src/utils.ts#L55-L114
- https://github.com/advisories/GHSA-9gvv-qjj3-2p6g
- https://www.vulncheck.com/advisories/flowise-through-3.1.4-custom-function-sandbox-escape-rce-via-localfilestore

### [CVE-2026-61804](https://github.com/myTinyWMS/myTinyWMS/commit/a01af6bb0e8f4013125c47c795a4736e7cbac7ec)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-61804
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-10-31 02:17:27 JST
- 更新日: 2026-10-31 04:39:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: myTinyWMS（バージョン1.6.4未満）における蓄積型クロスサイトスクリプティング（Stored XSS）の脆弱性。商品およびカテゴリー管理機能でのサニタイズ不足およびエスケープ処理の欠落が原因です。
- 影響: 認証された攻撃者が悪意のあるスクリプトを登録し、他のユーザーが一覧画面やダッシュボードを閲覧した際にセッションの窃取やアカウントの乗っ取りが発生する可能性があります。
- 推奨対応: myTinyWMS 1.6.4 以降へアップデートしてください。

#### References
- https://github.com/myTinyWMS/myTinyWMS/commit/a01af6bb0e8f4013125c47c795a4736e7cbac7ec
- https://github.com/myTinyWMS/myTinyWMS/security/advisories/GHSA-gw9m-vphv-gxm5
- https://github.com/myTinyWMS/myTinyWMS/tree/v1.6.4

### [CVE-2026-119764](https://github.com/h00die/mythic_xss)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-119764
- 関連キーワード: javascript, graphql, gin
- 影響製品: -
- 公開日: 2026-10-31 03:17:27 JST
- 更新日: 2026-10-31 04:14:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mythic（3.2.16から3.4.0.61まで）における蓄積型クロスサイトスクリプティング（Stored XSS）の脆弱性。.pdf 拡張子を持つファイル内のHTMLが同一オリジンでプレビュー出力されることが原因です。
- 影響: オペレーターが該当ファイルをプレビューした際、悪意のあるJavaScriptが実行され、localStorageに保存されたJWTが漏洩してフルアクセス権限を奪われる可能性があります。
- 推奨対応: Mythicを修正済みの最新バージョンへアップデートしてください。

#### References
- https://github.com/h00die/mythic_xss
- https://github.com/its-a-feature/Mythic
- https://github.com/its-a-feature/Mythic/blob/33a46d7db7e237458d7e20e7d3cfefef8112e590/MythicReactUI/src/components/pages/Callbacks/ResponseDisplayMedia.js#L335-L336
- https://github.com/its-a-feature/Mythic/commit/f06b3ed2d1de6577744cc0b3146966c625685859
- https://www.vulncheck.com/advisories/mythic-3.2.16-through-3.4.0.61-stored-xss-via-agent-downloaded-file-preview

### [CVE-2026-119680](https://pitstop.manageengine.com/portal/en/community/topic/sharepoint-manager-plus-build-4508-is-here)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-119680
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-31 00:16:51 JST
- 更新日: 2026-10-31 04:37:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SharePoint Manager Plus (SPMP) のグラフ機能における蓄積型クロスサイトスクリプティング（Stored XSS）の脆弱性。ユーザー名やサイト名などのデータに対するサニタイズおよびHTMLエンコードの不備が原因です。
- 影響: 注入されたコンテンツがグラフ描画時に他ユーザーのブラウザ上で実行され、セッション情報や機密データが窃取される可能性があります。
- 推奨対応: クライアントアプリケーションをビルド4508以降にアップデートしてください。

#### References
- https://pitstop.manageengine.com/portal/en/community/topic/sharepoint-manager-plus-build-4508-is-here

### [CVE-2026-112365](https://plugins.trac.wordpress.org/browser/easyjobs/tags/2.8.3/admin/includes/class-easyjobs-admin-candidates.php#L226)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-112365
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-31 03:17:20 JST
- 更新日: 2026-10-31 04:18:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用プラグイン easy.jobs（2.8.4以下）における蓄積型クロスサイトスクリプティング（Stored XSS）の脆弱性。`cover_letter` パラメータに対するサニタイズおよびエスケープが不十分です。
- 影響: 未認証の攻撃者が悪意のあるスクリプトを保存し、管理者が応募者の詳細タブで該当リンクをクリックした際にスクリプトが実行される可能性があります。
- 推奨対応: easy.jobs プラグインを修正済みの最新バージョンへアップデートしてください。

#### References
- https://plugins.trac.wordpress.org/browser/easyjobs/tags/2.8.3/admin/includes/class-easyjobs-admin-candidates.php#L226
- https://plugins.trac.wordpress.org/browser/easyjobs/tags/2.8.3/admin/react/src/components/Candidate/Details/Tabs/Application.js#L100
- https://plugins.trac.wordpress.org/browser/easyjobs/tags/2.8.3/admin/react/src/components/Messages/sanitize.js#L139
- https://plugins.trac.wordpress.org/browser/easyjobs/tags/2.8.3/admin/react/src/components/Messages/sanitize.js#L66
- https://plugins.trac.wordpress.org/browser/easyjobs/tags/2.8.4/admin/includes/class-easyjobs-admin-candidates.php#L226

### [CVE-2026-119662](https://github.com/songloft-org/songloft)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-119662
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-31 00:16:50 JST
- 更新日: 2026-10-31 04:23:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Songloft（2.9.0以上2.13.6未満）におけるハードコードされた初期認証情報の脆弱性。既定の管理者情報（admin/admin）が固定で設定されています。
- 影響: 同一ネットワーク上の攻撃者が管理者としてログインし、ライブラリや設定の変更、QuickJS上で動作するJavaScriptプラグインの設置を行う可能性があります。
- 推奨対応: Songloft 2.13.6 以降へアップデートし、初期管理者パスワードを直ちに変更してください。

#### References
- https://github.com/songloft-org/songloft
- https://github.com/songloft-org/songloft/blob/v2.13.3/internal/config/types.go#L15-L22
- https://github.com/songloft-org/songloft/blob/v2.13.3/mobile/mobile.go#L60-L84
- https://github.com/songloft-org/songloft/commit/034fc1c442af5d6bc188642f1fb766af648e014d
- https://github.com/songloft-org/songloft/issues/534

### [CVE-2026-119699](https://github.com/wp-graphql/wp-graphql)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-119699
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-10-31 01:17:50 JST
- 更新日: 2026-10-31 04:23:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WPGraphQL Smart Cache（2.3.3未満）における制御不能なリソース消費の脆弱性。Automatic Persisted Query ハンドラーが入力制限なくクエリを保存することが原因です。
- 影響: 未認証の攻撃者が大量のクエリを送信して `wp_posts` テーブルを膨大に増加させ、データベースのパフォーマンス低下やサービス停止を引き起こす可能性があります。
- 推奨対応: WPGraphQL Smart Cache 2.3.3 以降へアップデートしてください。

#### References
- https://github.com/wp-graphql/wp-graphql
- https://github.com/wp-graphql/wp-graphql/blob/wp-graphql-smart-cache/v2.3.2/plugins/wp-graphql-smart-cache/src/Document.php
- https://github.com/wp-graphql/wp-graphql/commit/80c021c42f4d4969e1b41760a08b4faf3c544a9e
- https://github.com/wp-graphql/wp-graphql/releases/tag/wp-graphql-smart-cache%2Fv2.3.3
- https://github.com/wp-graphql/wp-graphql/security/advisories/GHSA-5p5r-f66g-r4vp

### [CVE-2026-115820](https://downloads.wordpress.org/plugin/majestic-support.1.2.3.zip)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-115820
- 関連キーワード: jest, gin
- 影響製品: -
- 公開日: 2026-10-31 03:17:23 JST
- 更新日: 2026-10-31 04:18:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Majestic Supportプラグイン（1.2.2以下）の `columns` パラメータにおけるSQLインジェクションの脆弱性。
- 影響: 購読者（Subscriber）権限以上の認証済み攻撃者が、既存のクエリに任意のSQLを挿入してデータベースから機密情報を抽出する可能性があります。
- 推奨対応: プラグインを修正済みバージョンへ更新してください。

#### References
- https://downloads.wordpress.org/plugin/majestic-support.1.2.3.zip
- https://plugins.trac.wordpress.org/browser/majestic-support/tags/1.2.2/includes/formhandler.php#L68
- https://plugins.trac.wordpress.org/browser/majestic-support/tags/1.2.2/includes/tables/table.php#L50
- https://plugins.trac.wordpress.org/browser/majestic-support/tags/1.2.2/includes/tables/table.php#L72
- https://plugins.trac.wordpress.org/browser/majestic-support/tags/1.2.2/modules/gdpr/controller.php#L80

### [CVE-2026-119647](https://github.com/dromara/RuoYi-Vue-Plus)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-119647
- 関連キーワード: vue, gin
- 影響製品: -
- 公開日: 2026-10-31 00:16:48 JST
- 更新日: 2026-10-31 00:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RuoYi-Vue-Plus（6.0.0以下）の `SysUserServiceImpl.selectUserListByDept` における認可バイパスの脆弱性。
- 影響: 部署制限のある権限を持つ認証済みユーザーが、他部署のユーザー名、ログイン履歴、アカウント状態などの情報を閲覧する可能性があります。
- 推奨対応: 最新バージョンへのアップデート、または適切なアクセス制御チェックを実装してください。

#### References
- https://github.com/dromara/RuoYi-Vue-Plus
- https://github.com/dromara/RuoYi-Vue-Plus/blob/v6.0.0/ruoyi-modules/ruoyi-system/src/main/java/org/dromara/system/controller/system/SysUserController.java#L352-L356
- https://github.com/dromara/RuoYi-Vue-Plus/blob/v6.0.0/ruoyi-modules/ruoyi-system/src/main/java/org/dromara/system/service/impl/SysUserServiceImpl.java#L555-L560
- https://github.com/dromara/RuoYi-Vue-Plus/commit/a8b1bea7b7a4ca260172cf74fbf4ea7763092996
- https://github.com/dromara/RuoYi-Vue-Plus/issues/60

### [CVE-2015-20130](http://packetstormsecurity.com/files/133034/Netsweeper-Bypass-XSS-Redirection-SQL-Injection-Execution.html)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2015-20130
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-31 00:16:44 JST
- 更新日: 2026-10-31 04:14:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Netsweeper（4.0.11未満、および4.1.0〜4.1.4）の `view_server_log.php` における反射型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 管理者が悪意のあるURLにアクセスした際、ブラウザ上で任意のJavaScriptを実行される可能性があります。
- 推奨対応: Netsweeper 4.0.11 または 4.1.5 以降へ更新してください。

#### References
- http://packetstormsecurity.com/files/133034/Netsweeper-Bypass-XSS-Redirection-SQL-Injection-Execution.html
- https://github.com/projectdiscovery/nuclei-templates/blob/main/http/vulnerabilities/netsweeper/netsweeper-rxss.yaml
- https://www.exploit-db.com/exploits/37930
- https://www.netsweeper.com/
- https://www.vulncheck.com/advisories/netsweeper-reflected-xss-via-view-server-log-php

### [CVE-2026-105456](https://cert.pl/en/posts/2026/10/CVE-2026-105454)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-105456
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-31 01:17:37 JST
- 更新日: 2026-10-31 04:37:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RTIRが導入された Request Tracker (RT) 環境における HTML スクラバーのサニタイズ不備（Stored XSS）。
- 影響: 未認証の送信者などが `javascript:` スキームを含むリンクをチケット内に保持させ、それを閲覧したユーザーの権限で任意のスクリプトを実行される可能性があります。
- 推奨対応: RTIR / RT を 5.0.11 または 6.0.4 以降へ更新してください。

#### References
- https://cert.pl/en/posts/2026/10/CVE-2026-105454
- https://requesttracker.com/rtir/

### [CVE-2026-117184](https://github.com/Primandito/CVE-2026-117184)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-117184
- 関連キーワード: graphql, go
- 影響製品: -
- 公開日: 2026-10-31 01:17:41 JST
- 更新日: 2026-10-31 04:37:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: traggo server v0.8.3 の GraphQL エンドポイントにおけるリクエスト処理の不備。
- 影響: 攻撃者が作成したPOSTリクエストを送信することで、サービス拒否（DoS）状態を引き起こされる可能性があります。
- 推奨対応: 修正版ソフトウェアの適用、またはGraphQLエンドポイントへのリクエスト制限を検討してください。

#### References
- https://github.com/Primandito/CVE-2026-117184
- https://github.com/traggo/server/issues/253

### [CVE-2026-119700](https://github.com/wp-graphql/wp-graphql)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-119700
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-10-31 01:17:50 JST
- 更新日: 2026-10-31 04:23:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WPGraphQL（2.24.2未満）のエラー応答処理の差異に起因する情報漏洩の脆弱性。
- 影響: 未認証の攻撃者がIDを列挙して各種ミューテーションを実行することで、非公開・下書き・ゴミ箱内の投稿や未承認コメントの存在を判別される可能性があります。
- 推奨対応: WPGraphQL 2.24.2 以降へ更新してください。

#### References
- https://github.com/wp-graphql/wp-graphql
- https://github.com/wp-graphql/wp-graphql/blob/wp-graphql/v2.24.0/plugins/wp-graphql/src/Mutation/MediaItemDelete.php
- https://github.com/wp-graphql/wp-graphql/commit/3fb1904acff4df00287ef6278fe40438d276a9f9
- https://github.com/wp-graphql/wp-graphql/commit/bb4f778cae04f60c40bbcb1c80bed4faf91ad836
- https://github.com/wp-graphql/wp-graphql/releases/tag/wp-graphql%2Fv2.24.2

### [CVE-2026-119701](https://github.com/wp-graphql/wp-graphql)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-119701
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-10-31 01:17:50 JST
- 更新日: 2026-10-31 04:23:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WPGraphQL（2.24.1未満）の `sendPasswordResetEmail` ミューテーションにおけるレート制限の欠如。
- 影響: 未認証の攻撃者が1つのリクエストで大量のエイリアスを送信してバッチ制限を回避し、メール配信枠の枯渇やリセットキーの連続無効化を引き起こす可能性があります。
- 推奨対応: WPGraphQL 2.24.1 以降へ更新してください。

#### References
- https://github.com/wp-graphql/wp-graphql
- https://github.com/wp-graphql/wp-graphql/blob/wp-graphql/v2.24.0/plugins/wp-graphql/src/Mutation/SendPasswordResetEmail.php
- https://github.com/wp-graphql/wp-graphql/commit/760db555e3e60fbd86c1d96f1689bacfc9265592
- https://github.com/wp-graphql/wp-graphql/releases/tag/wp-graphql%2Fv2.24.1
- https://github.com/wp-graphql/wp-graphql/security/advisories/GHSA-f5f8-v768-93c8

### [CVE-2026-119702](https://github.com/wp-graphql/wp-graphql)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-119702
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-10-31 01:17:50 JST
- 更新日: 2026-10-31 04:23:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WPGraphQL（2.24.1未満）の `createComment` ミューテーションにおける認可チェックの不備。
- 影響: 未認証の攻撃者が非公開やパスワード保護された投稿に対してコメントを追加し、通知経由でのタイトル漏洩や投稿IDの特定などを行う可能性があります。
- 推奨対応: WPGraphQL 2.24.1 以降へ更新してください。

#### References
- https://github.com/wp-graphql/wp-graphql
- https://github.com/wp-graphql/wp-graphql/blob/wp-graphql/v2.24.0/plugins/wp-graphql/src/Mutation/CommentCreate.php
- https://github.com/wp-graphql/wp-graphql/commit/b9da32bd8e6025e19a9b04acaa129978eba71177
- https://github.com/wp-graphql/wp-graphql/releases/tag/wp-graphql%2Fv2.24.1
- https://github.com/wp-graphql/wp-graphql/security/advisories/GHSA-4vgv-vvxr-9fh9

### [CVE-2026-39375](https://github.com/frappe/lms/commit/cd6aca25f7d28425660720db4fdb920727edb670)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-39375
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-31 02:17:23 JST
- 更新日: 2026-10-31 04:39:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Frappe Learning Management System (LMS)（2.52.0未満）の Course Management モジュールにおける Stored XSS の脆弱性。
- 影響: コース編集権限を持つユーザーが meta tag フィールドを通じて悪意のあるJavaScriptを注入し、他ユーザーの閲覧時に実行させる可能性があります。
- 推奨対応: Frappe LMS 2.52.0 以降へ更新してください。

#### References
- https://github.com/frappe/lms/commit/cd6aca25f7d28425660720db4fdb920727edb670
- https://github.com/frappe/lms/commit/f244a6c9ff6e0b104fec48b2d97af4cc09896b60
- https://github.com/frappe/lms/security/advisories/GHSA-9fqj-95wr-6hm6
- https://github.com/frappe/lms/tree/v2.52.0

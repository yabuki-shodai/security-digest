# Frontend CVE Summary (2026-07-10)

## Overview

- 取得日時: 2026-07-10 08:23:44 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 0
- High: 5
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-57026](https://supportportal.juniper.net/JSA110086)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-57026
- 関連キーワード: vite, gin
- 影響製品: -
- 公開日: 2026-07-10 07:17:07 JST
- 更新日: 2026-07-10 07:17:07 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Juniper Networks Junos OSのMXシリーズおよびSRXシリーズのSIPプラグインにおいて、SIP ALGが有効な場合に不正なSIP招待パケットが原因でflowdがクラッシュし、サービス拒否（DoS）が発生する脆弱性。  
- 影響: 認証されていないネットワーク攻撃者によるサービス停止とシステムの一時的な完全停止が引き起こされる可能性がある。  
- 推奨対応: 影響を受けるJuniper Junos OSのバージョンを確認し、23.2R2-S7以降や23.4R2-S8以降などの修正済みバージョンへアップデートすることが推奨される。

#### References
- https://supportportal.juniper.net/JSA110086

### [CVE-2026-45780](https://github.com/discourse/discourse/commit/37969503f20369eb1712b7b88daedcfb4f63f5f1)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-45780
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-07-10 07:17:04 JST
- 更新日: 2026-07-10 07:17:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: DiscourseのEventSerializerにおいて、非公開イベントの招待者リストを閲覧権限のないユーザーに対して招待グループ名や参加者統計が漏洩する問題がありました。  
- 影響: 権限のないユーザーがプライベートイベントの招待情報を閲覧できる可能性があります。  
- 推奨対応: Discourseをバージョン2026.6.0、2026.5.1、2026.4.2、または2026.1.5以降にアップデートしてください。

#### References
- https://github.com/discourse/discourse/commit/37969503f20369eb1712b7b88daedcfb4f63f5f1
- https://github.com/discourse/discourse/commit/4d46638041b5f3d1e1f7f6f6f19c1df3bd65a586
- https://github.com/discourse/discourse/commit/6457ab71f36a2d1440fe96af0a2593897844b023
- https://github.com/discourse/discourse/commit/7deb4b6963442569357b41e61febe37594e5e730
- https://github.com/discourse/discourse/releases/tag/v2026.1.5

### [CVE-2026-59833](https://github.com/siyuan-note/siyuan/commit/ebe252e61fb93f258d083b9da0fa403679fdf94a)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-59833
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-10 08:17:05 JST
- 更新日: 2026-07-10 08:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SiYuanの3.7.1以前のバージョンで、Luteエンジンのサニタイズ機能に不備があり、SVGやフォームの属性を通じて保存型クロスサイトスクリプティングが発生し、Electronデスクトップレンダラー上でOSコマンドが実行される可能性があります。  
- 影響: 悪意あるスクリプトがノートやパッケージのエクスポートプレビューおよびREADMEレンダリング時に実行され、OSコマンドの実行を許す恐れがあります。  
- 推奨対応: SiYuanをバージョン3.7.1以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/siyuan-note/siyuan/commit/ebe252e61fb93f258d083b9da0fa403679fdf94a
- https://github.com/siyuan-note/siyuan/releases/tag/v3.7.1
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-97xv-3v84-h358

### [CVE-2026-55424](https://github.com/discourse/discourse/commit/1bce8881e4253d9bbab56f011a12ef899b926b59)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-55424
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-10 07:17:06 JST
- 更新日: 2026-07-10 07:17:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Discourseの特定バージョンにおいて、トピックの「featured link」が適切に正規化およびエスケープされず、JavaScriptのインジェクションが可能となる脆弱性が存在します。  
- 影響: ユーザーが設定可能なfeatured linkを通じて、CSPが変更または無効化されている場合にクロスサイトスクリプティング攻撃が発生する可能性があります。  
- 推奨対応: 影響を受けるバージョンから2026.6.0、2026.5.1、2026.4.2、または2026.1.5以降のバージョンへアップデートしてください。

#### References
- https://github.com/discourse/discourse/commit/1bce8881e4253d9bbab56f011a12ef899b926b59
- https://github.com/discourse/discourse/commit/6679d9a5083488bae10c2adbb345c481c583242c
- https://github.com/discourse/discourse/commit/6828aee9b15c2655d63b515ac919830bd540ff83
- https://github.com/discourse/discourse/commit/c9b9405f5bd0bf0269e505e28e3aad388d7657c5
- https://github.com/discourse/discourse/releases/tag/v2026.1.5

### [CVE-2026-59721](https://github.com/hoppscotch/hoppscotch/commit/73a88c82b1b2cada26cc4b2bc095b54554242239)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-59721
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-07-10 03:16:57 JST
- 更新日: 2026-07-10 05:16:30 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: HoppscotchのupdateInfraConfigs GraphQLミューテーションで、攻撃者が制御可能なMAILER_SMTP_URLを通じて任意のコマンド実行が可能になる脆弱性が存在します。  
- 影響: 管理者権限でバックエンドコンテナ内のroot権限による任意コマンド実行が発生する恐れがあります。  
- 推奨対応: Hoppscotchをバージョン2026.6.0以降にアップデートしてください。

#### References
- https://github.com/hoppscotch/hoppscotch/commit/73a88c82b1b2cada26cc4b2bc095b54554242239
- https://github.com/hoppscotch/hoppscotch/pull/6413
- https://github.com/hoppscotch/hoppscotch/releases/tag/2026.6.0
- https://github.com/hoppscotch/hoppscotch/security/advisories/GHSA-v7q6-r45w-2c6r
- https://github.com/hoppscotch/hoppscotch/security/advisories/GHSA-v7q6-r45w-2c6r

### [CVE-2026-59855](https://github.com/siyuan-note/siyuan/commit/efbe3a557720034782643e55c9e0282530cb6bbb)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-59855
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-10 08:17:06 JST
- 更新日: 2026-07-10 08:17:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SiYuanの3.7.1以前のバージョンで、Asset.render関数が未サニタイズのパスをinnerHTMLに挿入し、悪意あるリンクからJavaScriptが実行される脆弱性が存在します。  
- 影響: 攻撃者がElectronレンダラー内で任意のOSコマンドを実行できる可能性があります。  
- 推奨対応: バージョン3.7.1-alpha.2または3.7.1にアップデートし、脆弱性を修正してください。

#### References
- https://github.com/siyuan-note/siyuan/commit/efbe3a557720034782643e55c9e0282530cb6bbb
- https://github.com/siyuan-note/siyuan/releases/tag/v3.7.1
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-w3gq-5j72-36vc

### [CVE-2026-60120](https://github.com/bagisto/bagisto/commit/49d0c3fc90dedf8782c45c5979df4f4595d6bb97)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-60120
- 関連キーワード: javascript, vue, express
- 影響製品: -
- 公開日: 2026-07-10 06:16:56 JST
- 更新日: 2026-07-10 06:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Bagisto 2.4.4未満のバージョンにおいて、顧客登録時の名前フィールドに悪意あるペイロードを含めることで、管理者のブラウザ上で任意のJavaScriptが実行される保存型クロスサイトスクリプティングの脆弱性が存在します。  
- 影響: 認証されていない攻撃者が管理者権限のブラウザで任意のスクリプトを実行できる可能性があります。  
- 推奨対応: Bagistoをバージョン2.4.4以降にアップデートし、顧客名フィールドのテンプレート処理を適切に修正してください。

#### References
- https://github.com/bagisto/bagisto/commit/49d0c3fc90dedf8782c45c5979df4f4595d6bb97
- https://github.com/bagisto/bagisto/releases/tag/v2.4.4
- https://www.vulncheck.com/advisories/bagisto-stored-xss-via-csti-in-create-blade-php

### [CVE-2026-0279](https://security.paloaltonetworks.com/CVE-2026-0279)

> **Frontend** / **LOW** / CVSS: **1.3** / KEV: **no**

- タイトル: CVE-2026-0279
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-10 04:16:58 JST
- 更新日: 2026-07-10 05:16:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Palo Alto NetworksのPAN-OSにおけるUser-ID認証ポータルやGlobalProtectの複数のクロスサイトスクリプティング脆弱性により、認証されていない攻撃者が悪意あるJavaScriptを実行可能です。  
- 影響: 悪意あるスクリプトの実行により、情報漏洩やセッション乗っ取りのリスクが考えられますが、管理インターフェースのアクセス制限によりリスクは低減されます。  
- 推奨対応: 管理アクセスを信頼できる内部IPアドレスのみに制限し、Palo Alto Networksのベストプラクティスに従って設定を見直すことが推奨されます。

#### References
- https://security.paloaltonetworks.com/CVE-2026-0279

### [CVE-2026-13461](https://cwe.mitre.org/data/definitions/94.html)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-13461
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-10 02:16:56 JST
- 更新日: 2026-07-10 04:49:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PayRangeアプリバージョン7.0.7において、SSLバイパス脆弱性と組み合わさることで、WebView内にJavaScriptが注入される可能性があります。  
- 影響: 攻撃者がWebViewのサンドボックスを回避し、ユーザー端末上で危険な操作を実行できる恐れがあります。  
- 推奨対応: アプリのアップデートを確認し、提供されている修正があれば適用することを推奨します。

#### References
- https://cwe.mitre.org/data/definitions/94.html
- https://kb.cert.org/vuls/id/152953

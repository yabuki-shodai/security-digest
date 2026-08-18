# Backend CVE Summary (2026-08-19)

## Overview

- 取得日時: 2026-08-19 07:36:43 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 18
- Critical: 3
- High: 9
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-12564](https://access.redhat.com/security/cve/CVE-2026-12564)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-12564
- 関連キーワード: django, go, gin, kubernetes
- 影響製品: -
- 公開日: 2026-08-19 01:17:01 JST
- 更新日: 2026-08-19 05:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AAP Controller の HashiCorp Vault 認証情報プラグインにおける Kubernetes サービスアカウントトークンの不適切な送信の脆弱性。
- 影響: 認証済み攻撃者にトークンが窃取され、Kubernetes API経由でのリソース操作やデータベース認証情報等の漏洩に繋がる可能性があります。
- 推奨対応: 関連コンポーネントを最新の安全なバージョンへ更新し、認証情報テスト設定およびアクセス権限を見直してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-12564
- https://bugzilla.redhat.com/show_bug.cgi?id=2490556

### [CVE-2026-52723](https://github.com/fbeta-GmbH/ePA3-Service-OpenSource/commit/197c8c7fc41675f19c7f448696a2bc63fab9db5b)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-52723
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-19 02:16:59 JST
- 更新日: 2026-08-19 03:18:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ePA 3.x Integration 1.3.0 未満における VAU サーバー証明書および TLS 証明書検証の欠落による脆弱性。
- 影響: 中間者攻撃により通信内容を可視化・改ざんされ、サーバーへのなりすましが行われる可能性があります。
- 推奨対応: ePA 3.x Integration 1.3.0 以降へアップデートしてください。

#### References
- https://github.com/fbeta-GmbH/ePA3-Service-OpenSource/commit/197c8c7fc41675f19c7f448696a2bc63fab9db5b
- https://github.com/fbeta-GmbH/ePA3-Service-OpenSource/pull/12
- https://github.com/fbeta-GmbH/ePA3-Service-OpenSource/releases/tag/1.3.0
- https://github.com/fbeta-GmbH/ePA3-Service-OpenSource/security/advisories/GHSA-q2jw-6c4w-86jc
- https://www.machinespirits.de/advisory/a1da93

### [CVE-2026-73366](https://patchstack.com/database/wordpress/plugin/google-maps-easy/vulnerability/wordpress-easy-google-maps-plugin-1-13-0-php-object-injection-vulnerability?_s_id=cve)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-73366
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-19 00:17:04 JST
- 更新日: 2026-08-19 00:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Easy Google Maps 1.13.0 以前における未認証で悪用可能な PHP オブジェクト注入の脆弱性。
- 影響: 認証されていないリモートの攻撃者によって任意の処理を実行されるなどの重大な影響を受ける可能性があります。
- 推奨対応: 該当プラグインの最新版への更新または利用の停止を検討してください。

#### References
- https://patchstack.com/database/wordpress/plugin/google-maps-easy/vulnerability/wordpress-easy-google-maps-plugin-1-13-0-php-object-injection-vulnerability?_s_id=cve

### [CVE-2026-66793](https://access.redhat.com/security/cve/CVE-2026-66793)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-66793
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-08-19 00:17:00 JST
- 更新日: 2026-08-19 03:19:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Red Hat Advanced Cluster Management for Kubernetes の governance-policy-addon-controller におけるコンテナイメージの上書きに起因する権限昇格の脆弱性。
- 影響: ManagedClusterAddOn のアノテーション権限を持つ攻撃者により、cluster-admin 権限で任意コンテナが実行され権限昇格が発生する可能性があります。
- 推奨対応: アノテーション権限を厳格に制御し、最新の修正パッチを適用してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-66793
- https://bugzilla.redhat.com/show_bug.cgi?id=2507538

### [CVE-2026-50138](https://github.com/goshs-labs/goshs/security/advisories/GHSA-3whc-qvhv-xqjp)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-50138
- 関連キーワード: go, golang
- 影響製品: -
- 公開日: 2026-08-19 00:16:54 JST
- 更新日: 2026-08-19 00:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: goshs 2.1.0 未満において、WebDAV有効時に各種モード制限フラグ（--read-only等）が WebDAV ポートに適用されない脆弱性。
- 影響: 認証された WebDAV クライアントにより、設定されたアクセス制限を制限外の操作（ファイルの削除やアップロード等）で迂回される可能性があります。
- 推奨対応: goshs 2.1.0 以降へアップデートしてください。

#### References
- https://github.com/goshs-labs/goshs/security/advisories/GHSA-3whc-qvhv-xqjp

### [CVE-2026-61574](https://github.com/goauthentik/authentik/releases/tag/version/2026.2.6)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-61574
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-19 02:16:59 JST
- 更新日: 2026-08-19 02:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: authentik 2026.2.6 および 2026.5.5 未満における Remote Access Control エンドポイントの一覧表示および認証情報のアクセス制御不備の脆弱性。
- 影響: 認証されたすべてのユーザーに全エンドポイントの設定情報や認証情報（RDP/SSH/VNC等）が漏洩し、未認可システムへアクセスされる可能性があります。
- 推奨対応: authentik 2026.2.6 または 2026.5.5 以降へアップデートしてください。

#### References
- https://github.com/goauthentik/authentik/releases/tag/version/2026.2.6
- https://github.com/goauthentik/authentik/releases/tag/version/2026.5.5
- https://github.com/goauthentik/authentik/security/advisories/GHSA-rv9x-92g6-9cpf

### [CVE-2026-54730](https://github.com/goauthentik/authentik/commit/27866a94f29d0d7f784b3c462a697a968d3f6b9c)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-54730
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-19 02:16:59 JST
- 更新日: 2026-08-19 03:18:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: authentik 2026.2.6 および 2026.5.5 未満における Google Chrome デバイス信頼性の検証フェーズの迂回が可能な脆弱性。
- 影響: 攻撃者が検証用 iframe をスキップすることで、信頼されていない未検証デバイスからの認証を突破される可能性があります。
- 推奨対応: authentik 2026.2.6 または 2026.5.5 以降へアップデートしてください。

#### References
- https://github.com/goauthentik/authentik/commit/27866a94f29d0d7f784b3c462a697a968d3f6b9c
- https://github.com/goauthentik/authentik/commit/85adb0bbbd7ad4f2807ec21cf25bb42aee81afbc
- https://github.com/goauthentik/authentik/pull/24053
- https://github.com/goauthentik/authentik/pull/24058
- https://github.com/goauthentik/authentik/releases/tag/version/2026.2.6

### [CVE-2026-62357](https://github.com/dragonflydb/dragonfly/commit/c004623249fe2151dc5d64e21364fb9fb07c90d3)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-62357
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-19 01:18:11 JST
- 更新日: 2026-08-19 01:18:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dragonfly 1.40.0 未満の CMS.INITBYDIM および CMS.INITBYPROB コマンドにおける整数オーバーフローによるメモリ破損の脆弱性。
- 影響: 未認証のリモート攻撃者によってヒープメモリの破壊、情報漏洩、あるいはサーバーをクラッシュさせられる可能性があります。
- 推奨対応: Dragonfly 1.40.0 以降へアップデートしてください。

#### References
- https://github.com/dragonflydb/dragonfly/commit/c004623249fe2151dc5d64e21364fb9fb07c90d3
- https://github.com/dragonflydb/dragonfly/pull/7647
- https://github.com/dragonflydb/dragonfly/releases/tag/v1.40.0
- https://github.com/dragonflydb/dragonfly/security/advisories/GHSA-cmmv-h748-v93x

### [CVE-2026-66046](https://github.com/libexpat/libexpat/pull/1321)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-66046
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-19 00:16:57 JST
- 更新日: 2026-08-19 00:16:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Expat（2.8.3 以前）の `storeAtts()` 関数における計算量の増大による脆弱性。特定の非正規化属性を持つXMLを処理する際、アルゴリズムの複雑性が二次式 $O(N^2)$ となる問題が存在します。
- 影響: 未認証の遠隔の攻撃者が特製XML文書を送信することで、多大なCPUリソースを消費させ、サービス運用妨害（DoS）を引き起こす可能性があります。
- 推奨対応: Expat を修正済みバージョンへ更新するか、信頼できないXML入力に対する適切な制限の実施を検討してください。

#### References
- https://github.com/libexpat/libexpat/pull/1321
- https://www.vulncheck.com/advisories/expat-denial-of-service-via-storeatts-quadratic-complexity

### [CVE-2026-73367](https://patchstack.com/database/wordpress/plugin/google-maps-easy/vulnerability/wordpress-easy-google-maps-plugin-1-14-2-remote-file-inclusion-vulnerability?_s_id=cve)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-73367
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-19 00:17:05 JST
- 更新日: 2026-08-19 05:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Easy Google Maps（1.14.2 未満）における未認証のリモートファイルインクルージョン（RFI）の脆弱性。
- 影響: 未認証の遠隔の攻撃者により、外部スクリプトの実行や任意のコード実行が行われる可能性があります。
- 推奨対応: Easy Google Maps を 1.14.2 以降の最新バージョンにアップデートしてください。

#### References
- https://patchstack.com/database/wordpress/plugin/google-maps-easy/vulnerability/wordpress-easy-google-maps-plugin-1-14-2-remote-file-inclusion-vulnerability?_s_id=cve

### [CVE-2026-50126](https://github.com/KNMI/adaguc-server/commit/30dffde1a1776b994d60026f41ca620f7cad72e9)

> **Backend** / **MEDIUM** / CVSS: **4.0** / KEV: **no**

- タイトル: CVE-2026-50126
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-19 02:16:58 JST
- 更新日: 2026-08-19 03:17:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Adaguc-server（7.2.2 未満）における GeoJSON パーサーの入力検証不足。不正な形状の座標データが含まれる GeoJSON の解析時に、ヒープ領域外読み取りやヌルポインタ参照が発生します。
- 影響: 不正な GeoJSON データを処理させることで、サーバーをクラッシュ（DoS）させる可能性があります。
- 推奨対応: Adaguc-server を 7.2.2 以降にアップデートしてください。

#### References
- https://github.com/KNMI/adaguc-server/commit/30dffde1a1776b994d60026f41ca620f7cad72e9
- https://github.com/KNMI/adaguc-server/pull/710
- https://github.com/KNMI/adaguc-server/releases/tag/7.2.2
- https://github.com/KNMI/adaguc-server/security/advisories/GHSA-mwgv-59vv-rp2m
- https://github.com/KNMI/adaguc-server/security/advisories/GHSA-mwgv-59vv-rp2m

### [CVE-2026-63328](https://github.com/aquasecurity/trivy/commit/d4213d7735c74e57f06c02ccb39ebca67abc7959)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-63328
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-19 01:18:12 JST
- 更新日: 2026-08-19 01:18:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Trivy（0.72.0 未満）のプラグイン管理機能におけるパストラバーサルの脆弱性。公式インデックス外の非公式プラグインインストール時に制限外のパス構築が行われます。
- 影響: 悪意のあるプラグインのインストールや実行へ誘導された場合、任意の書き込み可能パスへファイルを出力・上書きされる可能性があります。
- 推奨対応: Trivy を 0.72.0 以降にアップデートし、信頼できないプラグインのインストールを避けてください。

#### References
- https://github.com/aquasecurity/trivy/commit/d4213d7735c74e57f06c02ccb39ebca67abc7959
- https://github.com/aquasecurity/trivy/releases/tag/v0.72.0
- https://github.com/aquasecurity/trivy/security/advisories/GHSA-8rc5-4fr6-64pw

### [CVE-2026-46482](https://github.com/mybb/mybb/commit/bd2a3447939d3084a5926dd66ece04649e0e0d60)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-46482
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-19 01:17:09 JST
- 更新日: 2026-08-19 03:17:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MyBB のユーザー登録機能における秘密の質問（CAPTCHA）の検証バイパスの脆弱性。`question_id` が無効・偽造・空である場合に正しくエラー処理されません。
- 影響: 攻撃者によって秘密の質問による保護を回避され、自動化されたユーザー登録やスパム送信が行われる可能性があります。
- 推奨対応: MyBB を修正コミットが適用された最新バージョンにアップデートしてください。

#### References
- https://github.com/mybb/mybb/commit/bd2a3447939d3084a5926dd66ece04649e0e0d60
- https://github.com/mybb/mybb/releases/tag/mybb_1840
- https://github.com/mybb/mybb/security/advisories/GHSA-v2h7-4jp7-j6hh
- https://mybb.com/versions/1.8.40

### [CVE-2026-50139](https://github.com/goshs-labs/goshs/security/advisories/GHSA-j48m-h7xq-2xpj)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-50139
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-19 00:16:54 JST
- 更新日: 2026-08-19 00:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: goshs（2.1.0 未満）の `ShareHandler` におけるダウンロード制限処理の競合状態（TOCTOU）の脆弱性。
- 影響: 並行リクエストの発生により、管理者が設定したファイルダウンロード上限数を越えてアクセスされる可能性があります。
- 推奨対応: goshs を 2.1.0 以降にアップデートしてください。

#### References
- https://github.com/goshs-labs/goshs/security/advisories/GHSA-j48m-h7xq-2xpj

### [CVE-2026-72532](https://developer.joomla.org/security-centre/1072-20260805-core-improper-acl-checks-for-category-webservice-endpoints.html)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-72532
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-19 01:18:16 JST
- 更新日: 2026-08-19 05:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla! Core（4.0.0〜5.4.7、6.0.0〜6.1.2）のカテゴリWebサービスエンドポイントにおけるアクセス制御チェック（ACL）の不備。
- 影響: 権限のないユーザーがWebサービスエンドポイント経由で不正にカテゴリを作成できる可能性があります。
- 推奨対応: Joomla! Core を修正されたバージョン（5.4.8以上または6.1.3以上など）へアップデートしてください。

#### References
- https://developer.joomla.org/security-centre/1072-20260805-core-improper-acl-checks-for-category-webservice-endpoints.html
- https://www.joomla.org/

### [CVE-2026-61634](https://github.com/rabbitmq/rabbitmq-java-client/commit/08790f09686173eb17b48d08a25edcb32e71a591)

> **Backend** / **NONE** / CVSS: **0.0** / KEV: **no**

- タイトル: CVE-2026-61634
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-19 02:16:59 JST
- 更新日: 2026-08-19 03:18:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RabbitMQ Java クライアント（5.33.0 未満）におけるフレームサイズ上限設定の整合性チェック不全。
- 影響: 悪意のあるまたは侵害されたブローカーから過大なフレームが送信された場合、クライアント接続の強制断絶やサービス運用妨害（DoS）が発生する可能性があります。
- 推奨対応: RabbitMQ Java クライアントを 5.33.0 以降にアップデートしてください。

#### References
- https://github.com/rabbitmq/rabbitmq-java-client/commit/08790f09686173eb17b48d08a25edcb32e71a591
- https://github.com/rabbitmq/rabbitmq-java-client/commit/b491075f42e89967610c40beded68d3680cfd472
- https://github.com/rabbitmq/rabbitmq-java-client/pull/1994
- https://github.com/rabbitmq/rabbitmq-java-client/pull/1995
- https://github.com/rabbitmq/rabbitmq-java-client/releases/tag/v5.33.0

### [CVE-2026-75858](https://github.com/Hmbown/CodeWhale/commit/57f3c89471e27ac4032d9791f6885e5d4408c381)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-75858
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-08-19 01:18:21 JST
- 更新日: 2026-08-19 03:19:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CodeWhale（0.8.41 以上 0.8.64 未満）の `rlm_eval` ツールにおける承認要件自動化の不備。プロンプトインジェクション等により提示された任意コードがユーザーの確認なしで実行される問題。
- 影響: 信頼できない外部データ（Webページやリポジトリファイル等）を読み込ませることで、攻撃者がユーザー権限で任意の Python コードを実行できる可能性があります。
- 推奨対応: CodeWhale を 0.8.64 以降にアップデートしてください。

#### References
- https://github.com/Hmbown/CodeWhale/commit/57f3c89471e27ac4032d9791f6885e5d4408c381
- https://github.com/Hmbown/CodeWhale/security/advisories/GHSA-wrj3-vj8c-784f
- https://www.vulncheck.com/advisories/codewhale-rlm-eval-before-remote-code-execution
- https://github.com/Hmbown/CodeWhale/security/advisories/GHSA-wrj3-vj8c-784f

### [CVE-2026-75857](https://github.com/Hmbown/CodeWhale/commit/57f3c89471e27ac4032d9791f6885e5d4408c381)

> **Backend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-75857
- 関連キーワード: python, mysql
- 影響製品: -
- 公開日: 2026-08-19 01:18:21 JST
- 更新日: 2026-08-19 01:18:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CodeWhale（0.8.41 以上 0.8.64 未満）の `exec_shell_interact` ツールにおける承認要件自動化の不備。対話型シェルへの入力に対して確認プロンプトがスキップされます。
- 影響: プロンプトインジェクション等を通じ、既に起動・承認されている対話型プロセス（ssh, mysql, sudo 等）の権限で任意のコマンドを実行される可能性があります。
- 推奨対応: CodeWhale を 0.8.64 以降にアップデートしてください。

#### References
- https://github.com/Hmbown/CodeWhale/commit/57f3c89471e27ac4032d9791f6885e5d4408c381
- https://github.com/Hmbown/CodeWhale/security/advisories/GHSA-g29h-pfmp-qp9r
- https://www.vulncheck.com/advisories/codewhale-before-privilege-escalation-via-exec-shell-interact

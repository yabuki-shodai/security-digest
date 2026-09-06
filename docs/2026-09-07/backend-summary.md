# Backend CVE Summary (2026-09-07)

## Overview

- 取得日時: 2026-09-07 08:48:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 14
- Critical: 0
- High: 7
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-13608](https://curl.se/docs/CVE-2026-13608.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-13608
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-07 03:17:19 JST
- 更新日: 2026-09-07 03:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libcurlにおけるLDAP認証用SASLネゴシエーションの不備に関する脆弱性。不完全なハンドシェイクシーケンスが、暗号検証成功と誤認される可能性があります。
- 影響: 中間者（MITM）攻撃者によりピア検証を回避され、通信の信頼性が損なわれる可能性があります。
- 推奨対応: 公式から提供される最新のセキュリティ修正情報を確認し、対策版libcurlへアップデートを行ってください。

#### References
- https://curl.se/docs/CVE-2026-13608.html
- https://curl.se/docs/CVE-2026-13608.json
- https://hackerone.com/reports/3822248

### [CVE-2026-19931](https://curl.se/docs/CVE-2026-19931.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19931
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-07 03:17:20 JST
- 更新日: 2026-09-07 03:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libcurlにおける接続再利用の不備。空の資格情報で初回リクエストを行った際、Negotiate認証用に設定されたHTTP接続が誤って再利用される場合があります。
- 影響: あるユーザーのリクエストが、過去に別ユーザーが認証した接続経由で送信され、不正アクセスやセッション混同に繋がる可能性があります。
- 推奨対応: libcurlの最新バージョンへのアップデート、および適切な認証情報管理を行ってください。

#### References
- https://curl.se/docs/CVE-2026-19931.html
- https://curl.se/docs/CVE-2026-19931.json
- https://hackerone.com/reports/3923520

### [CVE-2026-19633](https://gitlab.com/dalibo/postgresql_anonymizer/-/issues/665)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-19633
- 関連キーワード: express, postgresql
- 影響製品: -
- 公開日: 2026-09-07 01:16:49 JST
- 更新日: 2026-09-07 01:16:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PostgreSQL Anonymizerにおける特権昇格の脆弱性。非特権ユーザーが演算子、ドメインキャスト、またはビューサブクエリを悪用して信頼できない式を挿入できます。
- 影響: マスク処理のコンテキスト内で評価された際、高権限で任意のコードが実行される可能性があります。
- 推奨対応: PostgreSQL Anonymizer 3.1.4 以降のバージョンへアップデートしてください。

#### References
- https://gitlab.com/dalibo/postgresql_anonymizer/-/issues/665

### [CVE-2026-19634](https://gitlab.com/dalibo/postgresql_anonymizer/-/issues/665)

> **Backend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-19634
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-09-07 01:16:50 JST
- 更新日: 2026-09-07 01:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PostgreSQL Anonymizerのルールインポート関数（anon.import_database_rules() / anon.import_roles_rules()）におけるSQLインジェクションの脆弱性。
- 影響: スーパーユーザーがインポート関数を実行した際、悪意あるJSONドキュメントによりスーパーユーザー権限でコードが実行される可能性があります。
- 推奨対応: PostgreSQL Anonymizer 3.1.4 以降のバージョンへアップデートしてください。

#### References
- https://gitlab.com/dalibo/postgresql_anonymizer/-/issues/665

### [CVE-2026-83534](https://gitlab.com/dalibo/postgresql_anonymizer/-/issues/666)

> **Backend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-83534
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-09-07 01:16:50 JST
- 更新日: 2026-09-07 01:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PostgreSQL Anonymizerの `anon.anonymize_database_parallel()` 関数における権限管理の不備。
- 影響: テーブルの所有者がスーパーユーザー権限で任意コードを実行できる可能性があります。
- 推奨対応: PostgreSQL Anonymizer 3.2.0 以降のバージョンへアップデートしてください。

#### References
- https://gitlab.com/dalibo/postgresql_anonymizer/-/issues/666

### [CVE-2026-86220](https://github.com/justconter/_CVE/issues/1)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-86220
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-09-07 03:17:23 JST
- 更新日: 2026-09-07 03:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SourceCodester Class and Exam Timetabling System 1.0 の `/admin/modal_add_course.php` における SQL インジェクションの脆弱性。`course` 引数の不十分な検証に起因します。
- 影響: リモートの第三者によって任意のSQLコマンドが実行され、データベースの不当な操作や情報漏洩が発生する可能性があります（概念実証コードが公開済み）。
- 推奨対応: 該当箇所のコード修正（プリペアドステートメントの適用等）や入力値検証を行うか、適切なアクセス制限を設けてください。

#### References
- https://github.com/justconter/_CVE/issues/1
- https://vuldb.com/cve/CVE-2026-86220
- https://vuldb.com/submit/897734
- https://vuldb.com/vuln/399373
- https://vuldb.com/vuln/399373/cti

### [CVE-2026-86221](https://github.com/justconter/_CVE/issues/2)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-86221
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-09-07 04:17:27 JST
- 更新日: 2026-09-07 04:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SourceCodester Class and Exam Timetabling System 1.0 の `/admin/modal_add_course1.php` における SQL インジェクションの脆弱性。`course` 引数の不十分な検証に起因します。
- 影響: リモートの第三者によって任意のSQLコマンドが実行され、データの不正改ざんや漏洩が発生する可能性があります（概念実証コードが公開済み）。
- 推奨対応: 該当箇所のコード修正（プリペアドステートメントの適用等）を行うか、ベンダーによる修正情報を確認してください。

#### References
- https://github.com/justconter/_CVE/issues/2
- https://vuldb.com/cve/CVE-2026-86221
- https://vuldb.com/submit/897747
- https://vuldb.com/vuln/399374
- https://vuldb.com/vuln/399374/cti

### [CVE-2026-86222](https://github.com/justconter/_CVE/issues/3)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-86222
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-09-07 05:17:28 JST
- 更新日: 2026-09-07 05:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SourceCodester Class and Exam Timetabling System 1.0 の `/admin/modal_add_course2.php` における SQL インジェクションの脆弱性。`course` 引数の不十分な検証に起因します。
- 影響: リモートからデータベースを不正操作され、データの閲覧や改ざんが行われる可能性があります（概念実証コードが公開済み）。
- 推奨対応: 該当機能に対するプリペアドステートメントの実装、またはアクセス制御等の緩和策を実施してください。

#### References
- https://github.com/justconter/_CVE/issues/3
- https://vuldb.com/cve/CVE-2026-86222
- https://vuldb.com/submit/897748
- https://vuldb.com/vuln/399375
- https://vuldb.com/vuln/399375/cti

### [CVE-2026-86223](https://github.com/justconter/_CVE/issues/4)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-86223
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-09-07 05:17:28 JST
- 更新日: 2026-09-07 05:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SourceCodester Class and Exam Timetabling System 1.0 の `/admin/modal_add_coursea.php` における SQL インジェクションの脆弱性。`course` 引数の不十分な検証に起因します。
- 影響: リモート攻撃者によりデータベースへ不当なクエリが実行され、情報漏洩等を引き起こす可能性があります（概念実証コードが公開済み）。
- 推奨対応: パラメータのバインド処理（プリペアドステートメント）を追加するなどのコード修正を行ってください。

#### References
- https://github.com/justconter/_CVE/issues/4
- https://vuldb.com/cve/CVE-2026-86223
- https://vuldb.com/submit/897749
- https://vuldb.com/vuln/399376
- https://vuldb.com/vuln/399376/cti

### [CVE-2026-86224](https://github.com/justconter/_CVE/issues/5)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-86224
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-09-07 06:17:22 JST
- 更新日: 2026-09-07 06:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SourceCodester Class and Exam Timetabling System 1.0 の `/admin/modal_add_product.php` における SQL インジェクションの脆弱性。`fname` 引数の不十分な検証に起因します。
- 影響: リモート攻撃者によりデータベースが不当に操作される可能性があります（概念実証コードが公開済み）。
- 推奨対応: パラメータの無害化およびプリペアドステートメントの使用など、該当処理の修正を実施してください。

#### References
- https://github.com/justconter/_CVE/issues/5
- https://vuldb.com/cve/CVE-2026-86224
- https://vuldb.com/submit/897750
- https://vuldb.com/vuln/399377
- https://vuldb.com/vuln/399377/cti

### [CVE-2026-86225](https://github.com/justconter/_CVE/issues/6)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-86225
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-09-07 07:17:20 JST
- 更新日: 2026-09-07 07:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SourceCodester Class and Exam Timetabling System 1.0 の modal_add_room.php における SQL インジェクションの脆弱性。
- 影響: リモートの攻撃者が room_name パラメータを操作することで、データベースの不正閲覧や改ざんを行う可能性があります。
- 推奨対応: 入力値の適切なプレースホルダー化（パラメータ化クエリ）を実施するか、修正プログラムを適用してください。

#### References
- https://github.com/justconter/_CVE/issues/6
- https://vuldb.com/cve/CVE-2026-86225
- https://vuldb.com/submit/897751
- https://vuldb.com/vuln/399378
- https://vuldb.com/vuln/399378/cti

### [CVE-2026-82209](https://curl.se/docs/CVE-2026-82209.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-82209
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-07 03:17:22 JST
- 更新日: 2026-09-07 03:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libpsl サポート有効時の libcurl における Public Suffix List (PSL) 境界チェック不備の脆弱性。
- 影響: Set-Cookie の Domain 属性がパブリックサフィックスに設定された際、同一サフィックス配下の別サブドメイン（攻撃者所有ドメイン等）へクッキーが漏洩する可能性があります。
- 推奨対応: libcurl を修正済みの最新バージョンへアップデートしてください。

#### References
- https://curl.se/docs/CVE-2026-82209.html
- https://curl.se/docs/CVE-2026-82209.json
- https://hackerone.com/reports/3972385

### [CVE-2026-86304](https://metacpan.org/release/POLETTIX/MojoX-Authentication-0.004/source/lib/MojoX/Authentication/Model/SAML2.pm#L188)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-86304
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-07 08:17:39 JST
- 更新日: 2026-09-07 08:17:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MojoX::Authentication（バージョン 0.006 未満）における SAML 認証バイパスの脆弱性。
- 影響: 攻撃者が独自に署名した SAML レスポンスを送信することで、任意のユーザーとして認証を突破する可能性があります。
- 推奨対応: MojoX::Authentication を 0.006 以降の安全なバージョンへアップデートしてください。

#### References
- https://metacpan.org/release/POLETTIX/MojoX-Authentication-0.004/source/lib/MojoX/Authentication/Model/SAML2.pm#L188
- https://metacpan.org/release/POLETTIX/MojoX-Authentication-0.006/source/Changes
- https://www.cve.org/CVERecord?id=CVE-2026-18089

### [CVE-2026-80229](https://curl.se/docs/CVE-2026-80229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80229
- 関連キーワード: gin, openssl
- 影響製品: -
- 公開日: 2026-09-07 03:17:22 JST
- 更新日: 2026-09-07 03:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libcurl の multi インターフェースと OpenSSL 3 プロバイダー構成における Heap Use-After-Free の脆弱性。
- 影響: easy handle 破棄後のアクティブ接続の I/O 等により、メモリ破損、アプリケーションのクラッシュ、または任意のコード実行が発生する可能性があります。
- 推奨対応: libcurl を修正済みの最新バージョンへアップデートしてください。

#### References
- https://curl.se/docs/CVE-2026-80229.html
- https://curl.se/docs/CVE-2026-80229.json
- https://hackerone.com/reports/3969255

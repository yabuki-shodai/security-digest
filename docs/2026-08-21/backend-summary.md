# Backend CVE Summary (2026-08-21)

## Overview

- 取得日時: 2026-08-21 07:39:17 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 23
- Critical: 5
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-54623](https://github.com/django-cms/django-cms/commit/7642a98ab3170793c0b27b4125dd1f3d318b8a1c)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-54623
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-08-21 03:16:28 JST
- 更新日: 2026-08-21 04:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: django CMSにおけるプラグイン移動処理の不備による無限再帰（DoS）の脆弱性。`move_plugin`エンドポイントで親プラグインIDの循環チェックが行われていません。
- 影響: 権限を持つスタッフユーザーがプラグインツリー内に循環参照を作成でき、レンダリングや複製処理時に無限再帰が発生してサーバーリソースを枯渇させる可能性があります。
- 推奨対応: django CMS 5.0.8 以降へアップデートしてください。

#### References
- https://github.com/django-cms/django-cms/commit/7642a98ab3170793c0b27b4125dd1f3d318b8a1c
- https://github.com/django-cms/django-cms/pull/8645
- https://github.com/django-cms/django-cms/releases/tag/5.0.8
- https://github.com/django-cms/django-cms/security/advisories/GHSA-8jj7-4v57-frf5

### [CVE-2026-54622](https://github.com/django-cms/django-cms/commit/7642a98ab3170793c0b27b4125dd1f3d318b8a1c)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-54622
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-08-21 04:16:55 JST
- 更新日: 2026-08-21 04:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: django CMSのプラグイン複製機能における不適切な認可チェックの脆弱性。コピー元（ソース）のプレースホルダーに対する権限検証が行われていません。
- 影響: 権限を持つスタッフユーザーが、本来アクセス権のないページやプレースホルダーからプラグインを自分のクリップボードにコピーし、非公開情報を読み取る可能性があります。
- 推奨対応: django CMS 5.0.8 以降へアップデートしてください。

#### References
- https://github.com/django-cms/django-cms/commit/7642a98ab3170793c0b27b4125dd1f3d318b8a1c
- https://github.com/django-cms/django-cms/pull/8645
- https://github.com/django-cms/django-cms/releases/tag/5.0.8
- https://github.com/django-cms/django-cms/security/advisories/GHSA-4xfr-4p46-gc6p

### [CVE-2026-61663](https://github.com/django-cms/django-cms/commit/9c82abfeb25471583e23906ea1ebef9202527b04)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-61663
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-08-21 04:16:56 JST
- 更新日: 2026-08-21 04:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: django CMSの `render_object_structure` において、PlaceholderRelationFieldを使用する非PageContentオブジェクトに対する認可チェックが不足している不具合。
- 影響: 適切な権限を持たないスタッフユーザーにプレースホルダーのスロット名やプラグインツリーなどの構造情報が漏洩する可能性がある。
- 推奨対応: django CMSをバージョン 5.0.9 以降にアップデートする。

#### References
- https://github.com/django-cms/django-cms/commit/9c82abfeb25471583e23906ea1ebef9202527b04
- https://github.com/django-cms/django-cms/pull/8703
- https://github.com/django-cms/django-cms/releases/tag/5.0.9
- https://github.com/django-cms/django-cms/security/advisories/GHSA-8qj2-c6q4-f399

### [CVE-2026-63003](https://github.com/django-cms/django-cms/commit/3e1ccf7573eb1a74ebbbfaaa812c1f5cadf14e6c)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-63003
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-08-21 04:16:57 JST
- 更新日: 2026-08-21 04:16:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: django CMSのページ複製機能における不適切なアクセス制御の脆弱性。コピー元ページのオブジェクトレベル認可チェックが欠落しています。
- 影響: スタッフユーザーがアクセス権のないページを指定して複製することで、制限されたコンテンツやプラグイン情報を権限範囲外に漏洩させる可能性があります。
- 推奨対応: django CMS 5.0.9 以降へアップデートしてください。

#### References
- https://github.com/django-cms/django-cms/commit/3e1ccf7573eb1a74ebbbfaaa812c1f5cadf14e6c
- https://github.com/django-cms/django-cms/pull/8713
- https://github.com/django-cms/django-cms/releases/tag/5.0.9
- https://github.com/django-cms/django-cms/security/advisories/GHSA-6x92-6vx4-5fwr

### [CVE-2026-75526](https://github.com/django-cms/django-cms/commit/b56a568844ff3702495945f73a31d0868285bf88)

> **Backend** / **MEDIUM** / CVSS: **4.4** / KEV: **no**

- タイトル: CVE-2026-75526
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-08-21 04:17:03 JST
- 更新日: 2026-08-21 05:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: django CMSの編集モードにおけるプラグイン描画失敗時、例外メッセージ等の攻撃者制御可能な値がエスケープされずに処理される不具合。
- 影響: 編集者のブラウザ上で蓄積型HTML/XSSが実行される可能性がある。
- 推奨対応: django CMSをバージョン 5.0.9 以降にアップデートする。

#### References
- https://github.com/django-cms/django-cms/commit/b56a568844ff3702495945f73a31d0868285bf88
- https://github.com/django-cms/django-cms/pull/8711
- https://github.com/django-cms/django-cms/releases/tag/5.0.9
- https://github.com/django-cms/django-cms/security/advisories/GHSA-hvq6-2r72-p2x7

### [CVE-2026-54624](https://github.com/django-cms/django-cms/commit/7642a98ab3170793c0b27b4125dd1f3d318b8a1c)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-54624
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-08-21 04:16:55 JST
- 更新日: 2026-08-21 05:17:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: django CMSの `render_object_structure` が `user_can_view_page()` によるアクセス制限チェックを呼出さずに構造を描画する不具合。
- 影響: スタッフアカウントが閲覧制限のあるページのプラグイン情報（リンク名、URL、テキスト等）を取得できる可能性がある。
- 推奨対応: django CMSをバージョン 5.0.8 以降にアップデートする。

#### References
- https://github.com/django-cms/django-cms/commit/7642a98ab3170793c0b27b4125dd1f3d318b8a1c
- https://github.com/django-cms/django-cms/pull/8645
- https://github.com/django-cms/django-cms/releases/tag/5.0.8
- https://github.com/django-cms/django-cms/security/advisories/GHSA-vgxm-h9gx-h9w7

### [CVE-2026-54625](https://github.com/django-cms/django-cms/commit/8758714b865ffa79c6bcd0e5c503958ea48885aa)

> **Backend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-54625
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-08-21 03:16:28 JST
- 更新日: 2026-08-21 05:17:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: django CMSのページキャッシュ処理において、プラグインが指定する `get_vary_cache_on()` リクエストヘッダーがキャッシュキー生成時に無視される不具合。
- 影響: 異なるユーザー向けコンテンツが混同されて返却されるか、未認証の攻撃者によってキャッシュポイズニングが行われる可能性がある。
- 推奨対応: django CMSをバージョン 5.0.8 または 5.1.0 以降にアップデートする。

#### References
- https://github.com/django-cms/django-cms/commit/8758714b865ffa79c6bcd0e5c503958ea48885aa
- https://github.com/django-cms/django-cms/commit/d5dc1efa18d157445491c4b12c2dd1efd56f439f
- https://github.com/django-cms/django-cms/pull/8646
- https://github.com/django-cms/django-cms/pull/8647
- https://github.com/django-cms/django-cms/releases/tag/5.0.8

### [CVE-2026-71485](https://github.com/centrifugal/centrifugo/commit/84d38cea1dd2efa24375a148817a974c8727f4b0)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-71485
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-21 06:17:08 JST
- 更新日: 2026-08-21 06:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Centrifugoにおいて、クライアントが送信したリクエストヘッダーをバックエンドへ転送する際に適切な検証が行われない不具合。
- 影響: リモートクライアントが `x-trusted-user` などの信頼されたヘッダーを偽装し、バックエンドの認証・認可を回避できる可能性がある。
- 推奨対応: Centrifugoをバージョン 6.9.0 以降にアップデートする。

#### References
- https://github.com/centrifugal/centrifugo/commit/84d38cea1dd2efa24375a148817a974c8727f4b0
- https://github.com/centrifugal/centrifugo/pull/1182
- https://github.com/centrifugal/centrifugo/releases/tag/v6.9.0
- https://github.com/centrifugal/centrifugo/security/advisories/GHSA-9468-v6mj-fppw

### [CVE-2026-73251](https://github.com/cesanta/mongoose/commit/2988bc9df3a5efc9539471cb7455975fa25df483)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-73251
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-21 03:16:45 JST
- 更新日: 2026-08-21 05:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mongooseの組み込みTLSスタックにおいて、複数証明書のCAバンドル使用時に署名検証をスキップしてCN一致のみで検証をパスしてしまう不具合。
- 影響: ネットワーク上の攻撃者が偽造された証明書を用いてTLSサーバーになりすまし、通信の盗聴や改ざんを行う可能性がある。
- 推奨対応: Mongooseをバージョン 7.23 以降にアップデートする。

#### References
- https://github.com/cesanta/mongoose/commit/2988bc9df3a5efc9539471cb7455975fa25df483
- https://github.com/cesanta/mongoose/releases/tag/7.23
- https://github.com/cesanta/mongoose/security/advisories/GHSA-qj6j-2692-v2r8
- https://github.com/cesanta/mongoose/security/advisories/GHSA-qj6j-2692-v2r8
- https://github.com/cesanta/mongoose/security/advisories/GHSA-qj6j-2692-v2r8

### [CVE-2026-73253](https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-73253
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-21 03:16:45 JST
- 更新日: 2026-08-21 04:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mongooseの組み込みTLSスタックにおけるホスト名検証で、ワイルドカードがDNSラベル境界を超えてマッチしてしまう不具合。
- 影響: 親ドメインのワイルドカード証明書を持つ攻撃者が、より深いサブドメインになりすましてTLS通信を盗聴・改ざんする可能性がある。
- 推奨対応: Mongooseをバージョン 7.22 以降にアップデートする。

#### References
- https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71
- https://github.com/cesanta/mongoose/pull/3611
- https://github.com/cesanta/mongoose/releases/tag/7.22
- https://github.com/cesanta/mongoose/security/advisories/GHSA-jp6g-796f-39vp
- https://github.com/cesanta/mongoose/security/advisories/GHSA-jp6g-796f-39vp

### [CVE-2026-73257](https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-73257
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-21 03:16:46 JST
- 更新日: 2026-08-21 05:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongooseのHTTP解析処理において、`Content-Length` と `Transfer-Encoding: chunked` が両方指定された場合の判定に不備が存在する（CL.TEの不整合）。
- 影響: リバースプロキシ環境においてHTTPリクエストスマグリングが発生し、他ユーザーの文脈で不正アクセスやデータ改ざんが行われる可能性がある。
- 推奨対応: Mongooseをバージョン 7.22 以降にアップデートする。

#### References
- https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71
- https://github.com/cesanta/mongoose/pull/3611
- https://github.com/cesanta/mongoose/releases/tag/7.22
- https://github.com/cesanta/mongoose/security/advisories/GHSA-5wfq-r6mr-wqp6
- https://github.com/cesanta/mongoose/security/advisories/GHSA-5wfq-r6mr-wqp6

### [CVE-2026-73256](https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-73256
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-21 03:16:46 JST
- 更新日: 2026-08-21 03:16:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongooseのHTTP/1.0処理においてプロトコル長チェックの条件不備により、`Transfer-Encoding: chunked` が誤って処理される不具合。
- 影響: HTTP/1.0リバースプロキシ環境においてHTTPリクエストスマグリングが発生し、不正アクセスやデータ操作が行われる可能性がある。
- 推奨対応: Mongooseをバージョン 7.22 以降にアップデートする。

#### References
- https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71
- https://github.com/cesanta/mongoose/pull/3611
- https://github.com/cesanta/mongoose/releases/tag/7.22
- https://github.com/cesanta/mongoose/security/advisories/GHSA-mgp5-rjrv-h5j3

### [CVE-2026-69183](https://github.com/monkeytypegame/monkeytype/security/advisories/GHSA-c878-p3jh-mmjf)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-69183
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-21 02:19:34 JST
- 更新日: 2026-08-21 02:19:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Monkeytypeのバックエンドにおいて、レートリミットの識別キー作成時にクライアント制御可能なヘッダー（`cf-connecting-ip` や `x-forwarded-for`）を優先して使用する不具合。
- 影響: 未認証の攻撃者がヘッダーを回転させてレート制限を回避し、ブルートフォース保護の無効化、メール爆撃、リソース枯渇を引き起こす可能性がある。
- 推奨対応: 信頼できるプロキシ側で該当ヘッダーを上書き・削除するか、コード上で信頼されたIPのみを使用するよう修正を検討する（修正バージョンについての詳細は提示された入力からは断定不可）。

#### References
- https://github.com/monkeytypegame/monkeytype/security/advisories/GHSA-c878-p3jh-mmjf
- https://github.com/monkeytypegame/monkeytype/security/advisories/GHSA-c878-p3jh-mmjf

### [CVE-2026-76998](https://github.com/normabowie11-max/cve/issues/1)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-76998
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-21 01:18:31 JST
- 更新日: 2026-08-21 01:18:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security vulnerability has been detected in SourceCodester Simple Online Food Ordering System 1.0. The impacted element is an unknown function of the file /admin/ajax.php?action=delete_category. Such manipulation of the argument ID leads to sql injection. It is possible to launch the attack remotely. The exploit has...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/normabowie11-max/cve/issues/1
- https://vuldb.com/cve/CVE-2026-76998
- https://vuldb.com/submit/880465
- https://vuldb.com/vuln/393621
- https://vuldb.com/vuln/393621/cti

### [CVE-2026-61625](https://github.com/VictoriaMetrics/VictoriaMetrics/commit/710c920d6083327042a309e449fae4383617d817)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-61625
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-21 02:18:51 JST
- 更新日: 2026-08-21 04:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: VictoriaMetrics is a scalable solution for monitoring and managing time series data. Prior to 1.122.25, 1.136.12, and 1.146.0, vmrestore does not validate backup part path components before using lib/backup/actions/restore.go and lib/backup/fslocal/fslocal.go to write restored data below storageDataPath. An attacker wh...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/VictoriaMetrics/VictoriaMetrics/commit/710c920d6083327042a309e449fae4383617d817
- https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.122.25
- https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.136.12
- https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.146.0
- https://github.com/VictoriaMetrics/VictoriaMetrics/security/advisories/GHSA-8q3c-rjr9-xxrp

### [CVE-2026-67445](https://github.com/axllent/mailpit/commit/993bed95b3c74d95231af93bd0e0d4c3d5b4db4d)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-67445
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-21 06:17:07 JST
- 更新日: 2026-08-21 06:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mailpit is an email testing tool and API for developers. Prior to 1.30.4, Mailpit reads SMTP commands through internal/smtpd/smtpd.go session.readLine() using bufio.Reader.ReadString before session.parseLine() parses the verb or the RFC 5321 512-octet command-line limit is enforced. An unauthenticated remote SMTP clien...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/axllent/mailpit/commit/993bed95b3c74d95231af93bd0e0d4c3d5b4db4d
- https://github.com/axllent/mailpit/releases/tag/v1.30.4
- https://github.com/axllent/mailpit/security/advisories/GHSA-w878-pj84-3j5v

### [CVE-2026-73259](https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-73259
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-21 03:16:47 JST
- 更新日: 2026-08-21 05:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mongoose is an embedded web server and network library. Prior to 7.22, a remote attacker can send a crafted percent-encoded request path to a deployment using MG_ENABLE_DIRLIST and persuade a user to visit it. The mg_http_serve_dir() and listdir() path in src/http.c places the decoded request URI into the title and h1...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71
- https://github.com/cesanta/mongoose/pull/3611
- https://github.com/cesanta/mongoose/releases/tag/7.22
- https://github.com/cesanta/mongoose/security/advisories/GHSA-9cwm-487w-h25w
- https://github.com/cesanta/mongoose/security/advisories/GHSA-9cwm-487w-h25w

### [CVE-2026-77019](https://codeastro.com/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-77019
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-21 02:19:49 JST
- 更新日: 2026-08-21 02:19:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was determined in CodeAstro Apartment Visitor Management System 1.0. Affected is an unknown function of the file /apartment-visitor/forgotpw.php. Executing a manipulation of the argument secode can lead to sql injection. The attack may be launched remotely. The exploit has been publicly disclosed and ma...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://codeastro.com/
- https://github.com/Witiers/CVEs/issues/1
- https://vuldb.com/cve/CVE-2026-77019
- https://vuldb.com/submit/880593
- https://vuldb.com/vuln/393635

### [CVE-2026-77031](https://candle-throne-f75.notion.site/Tenda-CH22-formcreateFileName-392df0aa118580c38c4ad15fb15cd30d)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-77031
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-21 03:16:53 JST
- 更新日: 2026-08-21 04:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability has been found in Tenda CH22 1.0.0.1. The affected element is the function formcreateFileName of the file /goform/formcreateFileName. The manipulation of the argument fileNameMit leads to command injection. The attack can be initiated remotely. The exploit has been disclosed to the public and may be use...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://candle-throne-f75.notion.site/Tenda-CH22-formcreateFileName-392df0aa118580c38c4ad15fb15cd30d
- https://vuldb.com/cve/CVE-2026-77031
- https://vuldb.com/submit/880667
- https://vuldb.com/vuln/393642
- https://vuldb.com/vuln/393642/cti

### [CVE-2026-76997](https://github.com/hubdk01/cve/issues/3)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-76997
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-21 01:18:31 JST
- 更新日: 2026-08-21 01:18:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A weakness has been identified in SourceCodester Simple Online Food Ordering System 1.0. The affected element is an unknown function of the file /admin/ajax.php?action=save_category. This manipulation of the argument ID causes sql injection. It is possible to initiate the attack remotely. The exploit has been made avai...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/hubdk01/cve/issues/3
- https://vuldb.com/cve/CVE-2026-76997
- https://vuldb.com/submit/880392
- https://vuldb.com/vuln/393620
- https://vuldb.com/vuln/393620/cti

### [CVE-2026-73254](https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-73254
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-21 03:16:46 JST
- 更新日: 2026-08-21 03:16:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mongoose is an embedded web server and network library. Prior to 7.22, an attacker who can create a file with an HTML payload in its name can trigger stored cross-site scripting when a user browses a directory served with MG_ENABLE_DIRLIST. The printdirentry() path called by listdir() in src/http.c URL-encodes the href...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71
- https://github.com/cesanta/mongoose/pull/3611
- https://github.com/cesanta/mongoose/releases/tag/7.22
- https://github.com/cesanta/mongoose/security/advisories/GHSA-5g6j-m3pv-4f7g

### [CVE-2026-76023](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_0404570826.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-76023
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-21 06:17:10 JST
- 更新日: 2026-08-21 06:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper resource control in Linux Toolkit Theming in Google Chrome prior to 151.0.7922.173 allowed a remote attacker who had compromised the renderer process to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_0404570826.html
- https://issues.chromium.org/issues/545124048

### [CVE-2026-73255](https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-73255
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-21 03:16:46 JST
- 更新日: 2026-08-21 03:16:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mongoose is an embedded web server and network library. Prior to 7.22, an attacker who can control an SSI-enabled file can place directory traversal sequences in an #include file or #include virtual directive. The mg_ssi() function in src/ssi.c concatenates the directive argument into a filesystem path without calling...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71
- https://github.com/cesanta/mongoose/pull/3611
- https://github.com/cesanta/mongoose/releases/tag/7.22
- https://github.com/cesanta/mongoose/security/advisories/GHSA-h7m9-764r-7x4x

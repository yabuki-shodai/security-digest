# Backend CVE Summary (2026-09-26)

## Overview

- 取得日時: 2026-09-26 09:34:33 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 22
- Critical: 3
- High: 7
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-42322](https://github.com/Piwigo/Piwigo/commit/1e7f7262cb30e6916779f93e66d5d6579ec75a11)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-42322
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 01:17:25 JST
- 更新日: 2026-09-26 01:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Piwigo is a full featured open source photo gallery application for the web. Prior to 16.4.0, admin/themes_standard_pages.php validates uploaded logo content by MIME type but reuses the attacker-controlled extension from std_pgs_logo when constructing the stored filename. An authenticated administrator can upload image...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Piwigo/Piwigo/commit/1e7f7262cb30e6916779f93e66d5d6579ec75a11
- https://github.com/Piwigo/Piwigo/commit/4a13ec9a8f4881ae1f23bdfd24d7b90cd0802cdc
- https://github.com/Piwigo/Piwigo/releases/tag/16.4.0
- https://github.com/Piwigo/Piwigo/security/advisories/GHSA-7w97-5g4p-xqvv

### [CVE-2026-62262](https://github.com/Piwigo/Piwigo/commit/9755d88edf38b94bafdedb0b3aba7304a94e2e5c)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-62262
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 01:17:26 JST
- 更新日: 2026-09-26 01:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Piwigo is a full featured open source photo gallery application for the web. In 17.0.0beta1 and earlier, when rating is enabled, an unauthenticated guest can call pwg.images.filteredSearch.create with a crafted ratings[] value and then open the returned search URL. include/ws_functions/pwg.images.php stores the unvalid...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Piwigo/Piwigo/commit/9755d88edf38b94bafdedb0b3aba7304a94e2e5c
- https://github.com/Piwigo/Piwigo/commit/aede490a0b3a6c246f1f4689ca86c8fee377a7ae
- https://github.com/Piwigo/Piwigo/security/advisories/GHSA-hq29-8hhx-5jwc

### [CVE-2026-84458](https://github.com/zammad/zammad/commit/0dba387df8e2b46956907975034cd44e4d021b1c)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-84458
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 04:17:57 JST
- 更新日: 2026-09-26 04:17:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, when the "Automatic account link on initial logon" setting is enabled, Zammad binds an incoming third-party (SSO) identity to an existing local account by matching the email address the identity provider reports, without verifying that...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zammad/zammad/commit/0dba387df8e2b46956907975034cd44e4d021b1c
- https://github.com/zammad/zammad/security/advisories/GHSA-86cc-3ggh-mf2m

### [CVE-2026-94445](https://go.dev/cl/838485)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-94445
- 関連キーワード: go, golang
- 影響製品: -
- 公開日: 2026-09-26 02:17:19 JST
- 更新日: 2026-09-26 03:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A malicious txtar could escape the intended execution context and force arbitrary writes to the playground host's trusted filesystem. Disjointly, one of the three possible paths to invoke go vet on the playground host did not correctly restrict the execution environment. This permitted a Go process to make a read for a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://go.dev/cl/838485
- https://go.dev/issue/81737

### [CVE-2026-42323](https://github.com/Piwigo/Piwigo/commit/c7e30da5c1775b531ce9a30aac04134cd714b472)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-42323
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-09-26 01:17:25 JST
- 更新日: 2026-09-26 01:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Piwigo is a full featured open source photo gallery application for the web. Prior to 16.4.0, admin/batch_manager.php accepts administrator-controlled dimension width, height, and ratio values and filesize values from the Batch Manager filter URL without numeric validation. The URL filter parser stores those values in...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Piwigo/Piwigo/commit/c7e30da5c1775b531ce9a30aac04134cd714b472
- https://github.com/Piwigo/Piwigo/commit/e4f0989d350d66207066ea61f8ee8c137164fb2f
- https://github.com/Piwigo/Piwigo/releases/tag/16.4.0
- https://github.com/Piwigo/Piwigo/security/advisories/GHSA-7r67-9xhq-7p2c

### [CVE-2026-42324](https://github.com/Piwigo/Piwigo/commit/ba1f803f8cefd3602ccb9c6f0155cd529510288a)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-42324
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-09-26 01:17:25 JST
- 更新日: 2026-09-26 02:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Piwigo is a full featured open source photo gallery application for the web. Prior to 16.4.0, admin/element_set_ranks.php stores administrator-controlled image_order[] values without enforcing the existing sort-field whitelist. The stored album image_order expression is later concatenated into ORDER BY clauses by admin...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Piwigo/Piwigo/commit/ba1f803f8cefd3602ccb9c6f0155cd529510288a
- https://github.com/Piwigo/Piwigo/commit/ef9e65386d76f9c85f1e23a45dd7af14a5b73a47
- https://github.com/Piwigo/Piwigo/releases/tag/16.4.0
- https://github.com/Piwigo/Piwigo/security/advisories/GHSA-jhp4-7f82-8f6q
- https://github.com/Piwigo/Piwigo/security/advisories/GHSA-jhp4-7f82-8f6q

### [CVE-2026-44642](https://github.com/Piwigo/Piwigo/commit/1ff9d04534feb5f8f3cc2d3613c0fe8b51a1c0ba)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-44642
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 01:17:25 JST
- 更新日: 2026-09-26 02:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Piwigo is a full featured open source photo gallery application for the web. Prior to 16.4.0, check_upgrade_access_rights() in admin/include/functions_upgrade.php conditionally escapes the submitted username only when the removed get_magic_quotes_gpc function exists, so PHP 8 and later concatenate an unauthenticated us...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Piwigo/Piwigo/commit/1ff9d04534feb5f8f3cc2d3613c0fe8b51a1c0ba
- https://github.com/Piwigo/Piwigo/commit/2cfa7a3d194c8b95edde43038d8f5be5a359e785
- https://github.com/Piwigo/Piwigo/releases/tag/16.4.0
- https://github.com/Piwigo/Piwigo/security/advisories/GHSA-6wj3-7fhw-gfpm
- https://github.com/Piwigo/Piwigo/security/advisories/GHSA-6wj3-7fhw-gfpm

### [CVE-2026-56727](https://github.com/zammad/zammad/commit/4a9dd5f8a85948c5a2f96f6479d785153aac05d7)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-56727
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 03:17:26 JST
- 更新日: 2026-09-26 03:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad is a web based open source helpdesk/customer support system. Prior to 7.0.2, summary In Zammad's inbound PGP email processing, the return value of the gpg verification call was silently discarded. Regardless of whether gpg reported a valid, invalid, or missing signature, the handler unconditionally wrote sign: {...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zammad/zammad/commit/4a9dd5f8a85948c5a2f96f6479d785153aac05d7
- https://github.com/zammad/zammad/releases/tag/7.0.2
- https://github.com/zammad/zammad/security/advisories/GHSA-56jc-34c8-2xq4

### [CVE-2026-96812](https://github.com/google/gvisor/commit/573a9e73cf844f)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-96812
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 00:17:57 JST
- 更新日: 2026-09-26 02:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper Exposure of Resource to Wrong Sphere in the host file helper (gofer) in Google gVisor prior to commit 573a9e73cf844f on Linux platforms with CUSE enabled allows a local attacker with container image deployment privileges to achieve root code execution on the host system. By including a /dev/cuse character devi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/google/gvisor/commit/573a9e73cf844f

### [CVE-2026-57443](https://github.com/issdandavis/SCBE-AETHERMOORE/commit/ca833795e01eab060e92572e5f667c0c136b8c1e)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-57443
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-26 06:17:23 JST
- 更新日: 2026-09-26 06:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SCBE-AETHERMOORE is a geometric AI governance and evaluation framework. Starting in version 4.0.2 and prior to version 4.2.1, the AetherBrowser API server (`scripts/aetherbrowser/api_server.py`) exposes the `POST /api/ops/check-email` endpoint without any authentication. Any remote attacker can call this endpoint and t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/issdandavis/SCBE-AETHERMOORE/commit/ca833795e01eab060e92572e5f667c0c136b8c1e
- https://github.com/issdandavis/SCBE-AETHERMOORE/commit/de7779b722c501dbcf4eae95dd51bb3984506fb1
- https://github.com/issdandavis/SCBE-AETHERMOORE/security/advisories/GHSA-q986-4x7x-gx39

### [CVE-2026-63205](https://github.com/zammad/zammad/commit/f3e4da83621efad8443a4e9fe6bd87befad47c44)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-63205
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-26 04:17:54 JST
- 更新日: 2026-09-26 04:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, when creating or updating an email signature, Zammad processes inline images referenced in the signature body. If a signature body contains an HTML img tag pointing to any existing attachment, the system copies that attachment into a ne...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zammad/zammad/commit/f3e4da83621efad8443a4e9fe6bd87befad47c44
- https://github.com/zammad/zammad/security/advisories/GHSA-pp8r-x7pp-5qj5

### [CVE-2026-67241](https://github.com/rabbitmq/rabbitmq-server/commit/18eac8d547b4382bf830c621b20a35932dd1cfa5)

> **Backend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-67241
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-26 02:17:12 JST
- 更新日: 2026-09-26 02:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RabbitMQ is a messaging and streaming broker. From 4.2.0 until 4.2.9 and 4.3.3, AMQP 1.0 management exchange.declare skips alternate-exchange permission check. pUT /exchanges/:name (lines 192-240) checks only configure on the declared exchange and passes XArgs straight to rabbitexchange:declare/7. It omits the checkrea...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/rabbitmq/rabbitmq-server/commit/18eac8d547b4382bf830c621b20a35932dd1cfa5
- https://github.com/rabbitmq/rabbitmq-server/commit/56005e7cebffc478ef397573de24aff1167e7cda
- https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.2.9
- https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.3.3
- https://github.com/rabbitmq/rabbitmq-server/security/advisories/GHSA-rg2g-289m-xhhw

### [CVE-2026-56732](https://github.com/zammad/zammad/commit/3f6e8a5fa34eb0ce40f63292cf744f5f2992c9d0)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-56732
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 03:17:27 JST
- 更新日: 2026-09-26 03:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad（バージョン7.0.2未満）のHTMLサニタイズ処理におけるHTMLインジェクションの脆弱性。
- 影響: 悪意のあるチケットを閲覧したユーザーのセッションが切断され、強制的にログアウトさせられる可能性があります。
- 推奨対応: Zammadをバージョン7.0.2以上に更新してください。

#### References
- https://github.com/zammad/zammad/commit/3f6e8a5fa34eb0ce40f63292cf744f5f2992c9d0
- https://github.com/zammad/zammad/releases/tag/7.0.2
- https://github.com/zammad/zammad/security/advisories/GHSA-6rmm-28j9-q99q

### [CVE-2026-56735](https://github.com/zammad/zammad/commit/02c1ff8dc65961352dc047013bece9dff1f2ffb7)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-56735
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 03:17:28 JST
- 更新日: 2026-09-26 04:17:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad（7.0.2未満および7.1.0未満）のHTMLサニタイザーにおけるimgタグのsrcset属性チェック不備の脆弱性。
- 影響: チケット閲覧時に外部コンテンツが読み込まれ、ユーザーのIPアドレス、User-Agent、Refererなどの情報が外部へ漏洩する可能性があります。
- 推奨対応: Zammadをバージョン7.0.2または7.1.0以上に更新してください。

#### References
- https://github.com/zammad/zammad/commit/02c1ff8dc65961352dc047013bece9dff1f2ffb7
- https://github.com/zammad/zammad/releases/tag/7.0.2
- https://github.com/zammad/zammad/releases/tag/7.1.0
- https://github.com/zammad/zammad/security/advisories/GHSA-7fwx-3xr4-qm6w

### [CVE-2026-61855](https://github.com/zammad/zammad/commit/dd22716ced9f18861ed6f3b326c9d332c8c2072d)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-61855
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 04:17:53 JST
- 更新日: 2026-09-26 04:17:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad（バージョン7.0.3および7.1.1）における受信PGP署名検証結果の不整合の脆弱性。
- 影響: 署名で保護されていない表示コンテンツであっても有効なPGP署名として表示され、ユーザーが送信者の信頼性を誤認する可能性があります。
- 推奨対応: Zammadをバージョン7.1.2以上に更新してください。

#### References
- https://github.com/zammad/zammad/commit/dd22716ced9f18861ed6f3b326c9d332c8c2072d
- https://github.com/zammad/zammad/security/advisories/GHSA-r957-vp26-563q

### [CVE-2026-63006](https://github.com/zammad/zammad/commit/856af85c12413087d6a74ffee25b16048a5ed8c3)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-63006
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 04:17:54 JST
- 更新日: 2026-09-26 04:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad（バージョン7.1.2未満）におけるパストラバーサルを用いた画像URLサニタイザー回避の脆弱性。
- 影響: コンテンツ閲覧時に認証情報付きで保護されたAPIエンドポイントへ意図しないリクエストが送信され、強制ログアウトなどの副作用が発生する可能性があります。
- 推奨対応: Zammadをバージョン7.1.2以上に更新してください。

#### References
- https://github.com/zammad/zammad/commit/856af85c12413087d6a74ffee25b16048a5ed8c3
- https://github.com/zammad/zammad/security/advisories/GHSA-33p2-cm7w-62g3

### [CVE-2026-84460](https://github.com/zammad/zammad/commit/13217eb6b3fdf350228b13f8cf69f640b8fd0da2)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-84460
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 04:17:57 JST
- 更新日: 2026-09-26 04:17:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad（バージョン7.1.2未満）のタグ一覧取得RESTエンドポイントにおける不適切なアクセス制御の脆弱性。
- 影響: 認証済みユーザーであれば、アクセス権限のないチケットの内部タグ情報を閲覧・一括列挙できる可能性があります。
- 推奨対応: Zammadをバージョン7.1.2以上に更新してください。

#### References
- https://github.com/zammad/zammad/commit/13217eb6b3fdf350228b13f8cf69f640b8fd0da2
- https://github.com/zammad/zammad/commit/d1a5eabdd1285b202f75761c4406edc5509e217e
- https://github.com/zammad/zammad/security/advisories/GHSA-6vgm-xxp4-p6jv

### [CVE-2026-84463](https://github.com/zammad/zammad/commit/f7a97ea209696bce85ed62901ee753b88368851c)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-84463
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 04:17:57 JST
- 更新日: 2026-09-26 04:17:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad（バージョン7.1.2未満）のナレッジベースにおける不十分なHTMLエスケープに起因するHTMLインジェクションの脆弱性。
- 影響: 権限を持つユーザーが記事を閲覧した際、自動的にリクエストが送信され、攻撃者が指定したアカウントへセッションが強制的に切り替えられる可能性があります。
- 推奨対応: Zammadをバージョン7.1.2以上に更新してください。

#### References
- https://github.com/zammad/zammad/commit/f7a97ea209696bce85ed62901ee753b88368851c
- https://github.com/zammad/zammad/security/advisories/GHSA-cxjg-4gmf-5xqc

### [CVE-2026-96875](https://phabricator.wikimedia.org/T435206#12360644)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-96875
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 05:17:47 JST
- 更新日: 2026-09-26 06:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MediaWikiのCargo拡張機能（バージョン3.9.4以下）における入力検証不足による蓄積型XSSの脆弱性。
- 影響: 攻撃者によって送信された悪意のあるスクリプトが保存され、閲覧したユーザーのブラウザ上で実行される可能性があります。
- 推奨対応: MediaWiki Cargo拡張機能を最新の修正済みバージョンへアップデートすることを検討してください。

#### References
- https://phabricator.wikimedia.org/T435206#12360644

### [CVE-2026-96876](https://phabricator.wikimedia.org/T435121)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-96876
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 05:17:47 JST
- 更新日: 2026-09-26 06:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MediaWikiのCargo拡張機能（バージョン3.9.4以下）における入力検証不足による反射型XSSの脆弱性。
- 影響: 攻撃者が用意したリンクをユーザーがクリックすることで、ユーザーのブラウザ上で任意のスクリプトが実行される可能性があります。
- 推奨対応: MediaWiki Cargo拡張機能を最新の修正済みバージョンへアップデートすることを検討してください。

#### References
- https://phabricator.wikimedia.org/T435121

### [CVE-2026-96877](https://phabricator.wikimedia.org/T434977)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-96877
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 05:17:48 JST
- 更新日: 2026-09-26 06:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MediaWikiのCargo拡張機能（バージョン3.9.4以下）における入力検証不足による反射型XSSの脆弱性。
- 影響: 攻撃者が用意したリンクをユーザーがクリックすることで、ユーザーのブラウザ上で任意のスクリプトが実行される可能性があります。
- 推奨対応: MediaWiki Cargo拡張機能を最新の修正済みバージョンへアップデートすることを検討してください。

#### References
- https://phabricator.wikimedia.org/T434977

### [CVE-2026-96878](https://phabricator.wikimedia.org/T434784)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-96878
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-26 05:17:48 JST
- 更新日: 2026-09-26 06:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MediaWikiのCargo拡張機能（バージョン3.9.4以下）における入力検証不足による反射型XSSの脆弱性。
- 影響: 攻撃者が用意したリンクをユーザーがクリックすることで、ユーザーのブラウザ上で任意のスクリプトが実行される可能性があります。
- 推奨対応: MediaWiki Cargo拡張機能を最新の修正済みバージョンへアップデートすることを検討してください。

#### References
- https://phabricator.wikimedia.org/T434784

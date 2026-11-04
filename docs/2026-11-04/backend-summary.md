# Backend CVE Summary (2026-11-04)

## Overview

- 取得日時: 2026-11-04 11:12:56 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 24
- Critical: 1
- High: 8
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-111211](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-111211
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-11-04 01:17:18 JST
- 更新日: 2026-11-04 03:17:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Django (6.1.3未満、6.0.10未満、5.2.19未満) の `BaseGeometryWidget.deserialize()` において、無効なジオメトリ値をログ出力する際のエスケープが不足している脆弱性。
- 影響: リモートの攻撃者によってログエントリーの注入や偽造が行われる可能性がある。
- 推奨対応: Django 6.1.3、6.0.10、5.2.19 以降（またはサポートされる各系列の最新版）へアップデートする。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://github.com/django/django/commit/1b747694d6a68a6b5d48cbe81c71053092a5d374
- https://github.com/django/django/commit/af4319f7217e33ad5db747226765f09b49ec07ba
- https://github.com/django/django/commit/b336d9a4e8a919d2e5f979b663de2b27e245b793
- https://github.com/django/django/commit/b83bf870ee0006ab0dd84a01d1f3b0391320a51a

### [CVE-2026-108147](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-108147
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-11-04 01:17:18 JST
- 更新日: 2026-11-04 04:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Django (6.1.3未満、6.0.10未満、5.2.19未満) の `MultiPartParser` において、base64 エンコードされたマルチパートファイルの処理時に過剰なメモリ消費が発生する脆弱性。
- 影響: 大量のメモリを消費させられることで、サービス拒否（DoS）状態に陥る可能性がある。
- 推奨対応: Django 6.1.3、6.0.10、5.2.19 以降（またはサポートされる各系列の最新版）へアップデートする。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://github.com/django/django/commit/4bd1f59a80adafddbd47527c66d92d6a224244d8
- https://github.com/django/django/commit/5d95d9236fa4ededfb1931c60a65432385ece85f
- https://github.com/django/django/commit/8b435411f11d69a0dd41a8837654323502e6058e
- https://github.com/django/django/commit/a29ee4a55acedbe7ba0cb4d2db28c4e4d2848e02

### [CVE-2026-111362](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-111362
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-11-04 01:17:18 JST
- 更新日: 2026-11-04 04:17:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Django (6.1.3未満、6.0.10未満、5.2.19未満) の `OGRGeometry` において、GeoJSON 入力内の外部座標参照系（CRS）の定義制限が行われない脆弱性。
- 影響: 攻撃者が指定した任意の宛先に対してサーバーサイドリクエストフォージェリ（SSRF）が引き起こされる可能性がある。
- 推奨対応: Django 6.1.3、6.0.10、5.2.19 以降（またはサポートされる各系列の最新版）へアップデートする。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://github.com/django/django/commit/31bef742da017bc71fdce9298c30984aad844102
- https://github.com/django/django/commit/649fb7985f67d5936dfb8caae6a54c0870dc8eec
- https://github.com/django/django/commit/e938f676fcca72f41247b0e96d4f0805e1722913
- https://github.com/django/django/commit/ecb2b77b49890d6b2120f73fb3d7eb7ac7650143

### [CVE-2026-114582](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-114582
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-11-04 01:17:19 JST
- 更新日: 2026-11-04 04:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Django (6.1.3未満、6.0.10未満、5.2.19未満) の `SpatialReference` 等において、空間参照文字列の解析時に GDAL のファイル/ネットワークアクセスが制限されない脆弱性。
- 影響: サーバーサイドリクエストフォージェリ（SSRF）やローカルファイルの読み取りが発生する可能性がある。
- 推奨対応: Django 6.1.3、6.0.10、5.2.19 以降（またはサポートされる各系列の最新版）へアップデートする。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://github.com/django/django/commit/1c980729e53ef119d43a01d32ead30116c46cd36
- https://github.com/django/django/commit/3a2ec4378b53c7b8ff5283ad7eba624ffa6f2b2f
- https://github.com/django/django/commit/8bda4d0db15f28828d8db000287562efae5ce063
- https://github.com/django/django/commit/a658355eb51feccbe90b5ca2e3b7f3543cd99e01

### [CVE-2026-113593](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-113593
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-11-04 01:17:19 JST
- 更新日: 2026-11-04 04:17:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Djangoのキャッシュミドルウェアおよび`cache_page`デコレータにおけるキャッシュキー生成の不備。
- 影響: Varyヘッダーに指定された項目が省略されたリクエストと空値で送信されたリクエストに同一のキャッシュキーが生成され、他者の非公開データが閲覧される可能性がある。
- 推奨対応: Django 6.1.3、6.0.10、5.2.19以降などの修正済みバージョンへの更新を検討してください。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://github.com/django/django/commit/2006a2b068766bf332f1afcc32b7614d8e5759a2
- https://github.com/django/django/commit/55e2e009b4f3996e5c55af7b22a8c41eb826e892
- https://github.com/django/django/commit/9007fecd3633cfd90b093ebe106af564347c8aee
- https://github.com/django/django/commit/c0b7e5e4e4546e8ddc58262f1945938bb9d9ac2d

### [CVE-2026-113733](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **LOW** / CVSS: **2.2** / KEV: **no**

- タイトル: CVE-2026-113733
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-11-04 01:17:19 JST
- 更新日: 2026-11-04 04:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Django Adminの`display_for_field()`における一部ユーザーモデルのパスワードフィールドの不適切な処理。
- 影響: 閲覧権限のみを持つスタッフユーザーが、閲覧用フォームからパスワードハッシュを取得できる可能性がある。
- 推奨対応: Django 6.1.3、6.0.10以降などの修正済みバージョンへの更新を検討してください。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://github.com/django/django/commit/67cce9dcd23ddeec41ccf0abfe3431e3cd724365
- https://github.com/django/django/commit/7d875c0a49d2a59335c65f6bf57970a5bac03be2
- https://github.com/django/django/commit/f5b039a619b3b5394ea5b966e17c7546fda6f937
- https://groups.google.com/g/django-announce

### [CVE-2026-38600](https://github.com/Den-Sec/security-research/blob/master/advisories/gohttpserver/VDR-001-zipslip.md)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-38600
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-04 02:18:13 JST
- 更新日: 2026-11-04 07:19:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: codeskyblue gohttpserver の `/upload` エンドポイントにおける Zip Slip 脆弱性。
- 影響: 悪意を持って作成されたZipファイルをアップロードされることで、サーバー上の任意の位置にファイルが書き込まれる可能性がある。
- 推奨対応: 修正されたバージョンへの更新や、アップロード機能のアクセス制限およびアーカイブ展開処理の検証強化を検討してください。

#### References
- https://github.com/Den-Sec/security-research/blob/master/advisories/gohttpserver/VDR-001-zipslip.md
- https://github.com/codeskyblue/gohttpserver
- https://github.com/codeskyblue/gohttpserver/issues/232
- https://security.snyk.io/research/zip-slip-vulnerability
- https://github.com/Den-Sec/security-research/blob/master/advisories/gohttpserver/VDR-001-zipslip.md

### [CVE-2026-121452](https://github.com/mlogclub/bbs-go)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-121452
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-04 01:17:24 JST
- 更新日: 2026-11-04 04:18:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: bbs-go の `sendEmail()` における不適切なTLS証明書検証（`InsecureSkipVerify` が true）。
- 影響: 中間者攻撃によりSMTPトラフィックが盗聴・改ざんされ、認証情報やパスワード再設定メールの内容が漏洩・制御される可能性がある。
- 推奨対応: 証明書検証を適切に行う修正バージョンへのアップデートを検討してください。

#### References
- https://github.com/mlogclub/bbs-go
- https://github.com/mlogclub/bbs-go/blob/v4.4.6/internal/services/email_service.go#L86-L113
- https://github.com/mlogclub/bbs-go/commit/1a06e35fa6314ee2d3ada70685a7afa740baf6f5
- https://github.com/mlogclub/bbs-go/issues/310
- https://www.vulncheck.com/advisories/bbs-go-through-4.4.6-improper-tls-certificate-validation-in-smtp-email-service

### [CVE-2026-119675](https://github.com/mongodb/mongo-tools/blob/master/CHANGELOG.md)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-119675
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-11-04 02:18:07 JST
- 更新日: 2026-11-04 05:00:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Database Tools の `mongorestore` における `system.buckets.` プレフィックスの検証不備。
- 影響: リストア処理時に特殊コレクション保護をバイパスされ、root権限を含む意図しない管理者アカウントが作成される可能性がある。
- 推奨対応: MongoDB Database Tools 100.20.1 以降への更新を検討してください。

#### References
- https://github.com/mongodb/mongo-tools/blob/master/CHANGELOG.md

### [CVE-2026-121444](https://github.com/darylldoyle/svg-sanitizer/security/advisories/GHSA-hrwm-vcc9-hcm4)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-121444
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-04 00:17:36 JST
- 更新日: 2026-11-04 04:18:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: svg-sanitizer における要素参照解析処理の計算複雑性によるDoSの脆弱性。
- 影響: ネストされた `<use>` タグを持つSVGファイルを解析させられることで、PHPワーカープロセスが長時間占有される可能性がある。
- 推奨対応: svg-sanitizer 1.1.0 以降へのアップデートを検討してください。

#### References
- https://github.com/darylldoyle/svg-sanitizer/security/advisories/GHSA-hrwm-vcc9-hcm4
- https://www.vulncheck.com/advisories/svg-sanitizer-0.11.0-before-1.1.0-algorithmic-complexity-dos-via-use-reference-graph

### [CVE-2026-121557](https://github.com/wppconnect-team/wppconnect-server)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-121557
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-04 01:17:28 JST
- 更新日: 2026-11-04 01:30:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WPPConnect Server の Chatwoot Webhook ルートにおける認証ミドルウェアの欠落。
- 影響: 未認証の第三者がセッション名を指定してAPIを呼び出すことで、任意のアカウントからWhatsAppメッセージやファイルを不正送信できる可能性がある。
- 推奨対応: 修正済みバージョンへの更新、または `verifyToken` ミドルウェアの適切な設定を検討してください。

#### References
- https://github.com/wppconnect-team/wppconnect-server
- https://github.com/wppconnect-team/wppconnect-server/blob/v2.10.74/src/controller/deviceController.ts#L2230-L2324
- https://github.com/wppconnect-team/wppconnect-server/blob/v2.10.74/src/routes/index.ts#L963
- https://github.com/wppconnect-team/wppconnect-server/issues/2701
- https://github.com/wppconnect-team/wppconnect-server/pull/2702

### [CVE-2026-119672](https://github.com/mongodb/mongo-tools/blob/master/CHANGELOG.md)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-119672
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-11-04 02:18:06 JST
- 更新日: 2026-11-04 05:00:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Database Tools の `mongofiles` における、GridFSに保存されたファイル名の出力先利用問題。
- 影響: ファイル名が特定値（`-`など）に変更されている場合、リストア実行時の出力が標準出力に書き出され、本来アクセス権のないデータが漏洩する可能性がある。
- 推奨対応: MongoDB Database Tools 100.20.1 以降への更新、およびリストア時に明示的な `--local`Destination を指定することを検討してください。

#### References
- https://github.com/mongodb/mongo-tools/blob/master/CHANGELOG.md

### [CVE-2026-119674](https://github.com/mongodb/mongo-tools/blob/master/CHANGELOG.md)

> **Backend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-119674
- 関連キーワード: go, gin, mongodb
- 影響製品: -
- 公開日: 2026-11-04 02:18:06 JST
- 更新日: 2026-11-04 05:00:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Database Tools の `mongorestore` におけるメタデータからのコレクション名デコード処理の不備。
- 影響: リストア時にドキュメントが異なるコレクションへ上書き・挿入されたり、既存データが置換・消失する可能性がある。
- 推奨対応: MongoDB Database Tools 100.20.1 以降への更新を検討してください。

#### References
- https://github.com/mongodb/mongo-tools/blob/master/CHANGELOG.md

### [CVE-2026-121415](https://github.com/parse-community/parse-server/pull/10804)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-121415
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-11-04 00:17:31 JST
- 更新日: 2026-11-04 00:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDBを使用する Parse Server における、null値を持つドット表記キーの型検証スキップ問題。
- 影響: 書き込み権限を持つクライアントによりフィールドデータが破壊されたり、アトミック操作や読み取り処理が不全に陥る可能性がある。
- 推奨対応: Parse Server 8.6.111、9.10.6-alpha.3 以降へのアップデートを検討してください。

#### References
- https://github.com/parse-community/parse-server/pull/10804
- https://github.com/parse-community/parse-server/pull/10805
- https://github.com/parse-community/parse-server/security/advisories/GHSA-655c-2xf3-77x9
- https://www.vulncheck.com/advisories/parse-server-before-8.6.111-and-9.0.0-before-9.10.6-alpha.3-field-corruption-via-null-dot-notation-key

### [CVE-2026-115297](https://discuss.elastic.co/t/packetbeat-8-19-24-9-4-9-9-5-6-security-update-esa-2026-208/391361)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-115297
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-04 02:17:55 JST
- 更新日: 2026-11-04 05:32:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NULL Pointer Dereference (CWE-476) in the AMQP protocol parser in Packetbeat can lead to denial of service via specially crafted network traffic. An unauthenticated attacker who can send traffic on a network segment that Packetbeat monitors for AMQP can cause a Go runtime panic that terminates the Packetbeat process. A...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://discuss.elastic.co/t/packetbeat-8-19-24-9-4-9-9-5-6-security-update-esa-2026-208/391361

### [CVE-2026-119673](https://github.com/mongodb/mongo-tools/blob/master/CHANGELOG.md)

> **Backend** / **LOW** / CVSS: **2.8** / KEV: **no**

- タイトル: CVE-2026-119673
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-11-04 02:18:06 JST
- 更新日: 2026-11-04 05:00:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Database Tools mongofiles does not resolve existing parent-directory symlinks when validating output paths for get_regex. An unauthorized user who can both upload a GridFS file and place a symlink in the operator's download working directory can cause a later retrieval to create a file containing unauthorized u...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mongodb/mongo-tools/blob/master/CHANGELOG.md

### [CVE-2026-121387](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-wg7g-gx9g-r96c)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-121387: freerdp freerdp
- 関連キーワード: go
- 影響製品: freerdp freerdp
- 公開日: 2026-11-04 00:17:25 JST
- 更新日: 2026-11-04 06:14:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreeRDP 2.0.0 before 3.32.2 contains an out-of-bounds read vulnerability in freerdp_dsp_decode_gsm610 that allows malicious RDP servers to read past audio buffers by sending truncated GSM610 frames. Attackers can negotiate GSM610 on rdpsnd and send a WAVE2 message shorter than a 33- or 32-byte WAV49 frame to crash the...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-wg7g-gx9g-r96c
- https://www.vulncheck.com/advisories/freerdp-2.0.0-before-3.32.2-out-of-bounds-read-via-gsm610-wav49-decoder

### [CVE-2026-121401](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-8rjm-m7xg-mg6m)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-121401: freerdp freerdp
- 関連キーワード: go
- 影響製品: freerdp freerdp
- 公開日: 2026-11-04 00:17:28 JST
- 更新日: 2026-11-04 02:18:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreeRDP before 3.32.2 contains a denial of service vulnerability where rdg_process_packet dispatches a PKT_TYPE_EXTENDED_AUTH_MSG without verifying negotiated mode or auth context. A malicious or compromised RD Gateway can send the extended-auth packet before tunnel authentication, triggering a null-pointer dereference...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-8rjm-m7xg-mg6m
- https://www.vulncheck.com/advisories/freerdp-before-3.32.2-denial-of-service-via-rd-gateway-extended-auth-packet
- https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-8rjm-m7xg-mg6m

### [CVE-2026-38601](https://github.com/Den-Sec/security-research/blob/master/advisories/gohttpserver/VDR-002-hardcoded-secret.md)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-38601
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-04 02:18:13 JST
- 更新日: 2026-11-04 02:18:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A hardcoded session secret key in codeskyblue gohttpserver through v1.3.0 allows attackers to impersonate any user, bypass OpenID Connect authentication and access all controls via forged session cookies.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Den-Sec/security-research/blob/master/advisories/gohttpserver/VDR-002-hardcoded-secret.md
- https://github.com/codeskyblue/gohttpserver
- https://github.com/codeskyblue/gohttpserver/issues/232

### [CVE-2026-115714](https://discuss.elastic.co/t/multiple-elastic-docker-images-8-19-24-9-4-9-9-5-6-security-update-esa-2026-237/391374)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-115714
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-11-04 02:17:56 JST
- 更新日: 2026-11-04 05:32:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper Certificate Validation (CWE-295) in the operating system certificate bundle shipped in the Docker images of APM Server; Auditbeat, Filebeat, Heartbeat, Metricbeat and Packetbeat; Elastic Agent, including Fleet Server and Cloudbeat; Logstash, for TLS connections that use the operating system certificate bundle;...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://discuss.elastic.co/t/multiple-elastic-docker-images-8-19-24-9-4-9-9-5-6-security-update-esa-2026-237/391374

### [CVE-2026-103916](https://docs.docker.com/ai/sandboxes/)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-103916
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-11-04 02:17:52 JST
- 更新日: 2026-11-04 05:32:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Docker Sandboxes sbx cp does not safely confine host-side paths to a shared workspace. A malicious sandbox can create or replace a workspace symlink so that a later user-initiated copy reads a host file outside the workspace into the sandbox or writes sandbox-controlled data to a host path outside the workspace with th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.docker.com/ai/sandboxes/
- https://docs.docker.com/ai/sandboxes/security/isolation/
- https://github.com/docker/sbx-releases/releases/tag/v0.51.0

### [CVE-2026-121435](https://github.com/froxlor/froxlor/security/advisories/GHSA-6vjr-55fw-r5x2)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-121435
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-11-04 00:17:34 JST
- 更新日: 2026-11-04 00:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Froxlor before 2.3.15 contains an authorization bypass vulnerability that allows authenticated customers to create MySQL databases by calling the Mysqls.add API endpoint, which lacks the customer_hide_options check. Customers can invoke Mysqls.add even when the admin has disabled the MySQL feature, creating unauthorize...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/froxlor/froxlor/security/advisories/GHSA-6vjr-55fw-r5x2
- https://www.vulncheck.com/advisories/froxlor-before-2.3.15-authorization-bypass-via-mysqls-add-api

### [CVE-2026-121416](https://github.com/surrealdb/surrealdb/security/advisories/GHSA-p296-7pr4-87rr)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-121416
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-11-04 00:17:31 JST
- 更新日: 2026-11-04 04:18:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SurrealDB 2.0.0 before 3.3.1 does not enforce --deny-funcs restrictions on method-style function calls in the streaming engine, because MethodPart::evaluate invokes resolved functions without a capability check. Authenticated users who can submit queries can run denied functions via method syntax, e.g. [1,2].map() or $...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/surrealdb/surrealdb/security/advisories/GHSA-p296-7pr4-87rr
- https://www.vulncheck.com/advisories/surrealdb-2.0.0-before-3.3.1-deny-funcs-capability-bypass-via-method-style-invocations

### [CVE-2026-121559](https://github.com/glpi-project/glpi/commit/10a827c8c1868a0a65ab977d30878ff16547d9a7)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-121559
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-11-04 01:17:28 JST
- 更新日: 2026-11-04 04:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GLPI 10.0.0 before 10.0.28 and 11.0.0 before 11.0.10 contains a privilege escalation vulnerability that allows authenticated users to obtain elevated profiles by cloning accounts. A user with the Technician profile can clone a Super-Admin account with a new login and password, since User::getCloneRelations() copies eve...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/glpi-project/glpi/commit/10a827c8c1868a0a65ab977d30878ff16547d9a7
- https://github.com/glpi-project/glpi/commit/d30faa501e8b549ae507615b05e7d99dacfe5d98
- https://github.com/glpi-project/glpi/security/advisories/GHSA-c46f-4v9j-5gpc
- https://www.vulncheck.com/advisories/glpi-10.0.0-before-10.0.28-and-11.0.0-before-11.0.10-privilege-escalation-via-user-cloning

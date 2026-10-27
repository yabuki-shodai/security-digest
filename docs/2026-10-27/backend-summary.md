# Backend CVE Summary (2026-10-27)

## Overview

- 取得日時: 2026-10-27 10:26:12 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 25
- Critical: 3
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-102649](https://github.com/padok-team/burrito/commit/1d48432a4a0126429c99f5fa42567bf3711d1ca1)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-102649
- 関連キーワード: go, kubernetes, terraform
- 影響製品: -
- 公開日: 2026-10-27 03:17:21 JST
- 更新日: 2026-10-27 03:39:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Burrito (0.13.0未満) の `/api/webhook` において、`webhookSecret` が空の際に Webhook の署名検証が行われない問題。
- 影響: 攻撃者によりイベントが偽造され、TerraformPullRequest カスタムリソースの不正な作成や削除が行われる可能性がある。
- 推奨対応: Burrito 0.13.0 以降へアップデートする。

#### References
- https://github.com/padok-team/burrito/commit/1d48432a4a0126429c99f5fa42567bf3711d1ca1
- https://github.com/padok-team/burrito/releases/tag/v0.13.0
- https://github.com/padok-team/burrito/security/advisories/GHSA-7m68-72r6-3jx8

### [CVE-2026-93328](https://github.com/googleapis/mcp-toolbox/pull/3454)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-93328
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 00:16:45 JST
- 更新日: 2026-10-27 02:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Google Cloud MCP Toolbox for Databases (1.2.0〜1.4.0) の cloud-storage ソースにおけるパストラバーサルおよび認可欠如の脆弱性。
- 影響: 未認証のリモート攻撃者により、ホストファイルの外部 GCS バケットへの流出や、ローカルファイルの任意上書きが行われる可能性がある。
- 推奨対応: 修正済みの最新バージョンへ更新し、ツールの呼び出しパラメータの安全性を確認する。

#### References
- https://github.com/googleapis/mcp-toolbox/pull/3454

### [CVE-2026-77055](https://boneio.eu/en/docs/black)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-77055
- 関連キーワード: go, docker
- 影響製品: -
- 公開日: 2026-10-27 00:16:43 JST
- 更新日: 2026-10-27 02:11:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: boneIO (black_debian_images) の `boneio` サービスアカウントにパスワードなしの sudo 権限や docker グループ権限が過剰に付与されている問題。
- 影響: ローカルの攻撃者が `boneio` アカウントを奪取した場合、root 権限へ昇格される可能性がある。
- 推奨対応: boneIO 1.6.0 以降へアップデートし、権限設定を適切に適用する。

#### References
- https://boneio.eu/en/docs/black
- https://cert.pl/en/posts/2026/10/CVE-2026-77052

### [CVE-2026-85297](https://github.com/GoogleCloudPlatform/cloud-run-mcp/releases/tag/v1.11.0)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-85297
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 01:17:23 JST
- 更新日: 2026-10-27 01:50:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Google Cloud Run MCP (1.11.0未満) における Bucket Squatting (バケット居座り) の脆弱性。
- 影響: 攻撃者にソースコードを傍受されたり、任意のコード実行やデータの外部流出が引き起こされる可能性がある。
- 推奨対応: Google Cloud Run MCP 1.11.0 以降にアップデートする。

#### References
- https://github.com/GoogleCloudPlatform/cloud-run-mcp/releases/tag/v1.11.0

### [CVE-2026-116539](https://github.com/netty/netty-tcnative)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-116539
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 01:17:19 JST
- 更新日: 2026-10-27 01:54:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Netty netty-tcnative (2.0.84.Final未満) の `tcn_write_to_bytebuffer` におけるヒープバッファオーバーフローの脆弱性。
- 影響: リモート TLS 対向から送信されるメッセージにより領域外メモリ書き込みが発生し、JVM プロセスがクラッシュさせられる可能性がある。
- 推奨対応: netty-tcnative 2.0.84.Final 以降へアップデートする。

#### References
- https://github.com/netty/netty-tcnative
- https://github.com/netty/netty-tcnative/blob/netty-tcnative-parent-2.0.83.Final/openssl-dynamic/src/main/c/ssl.c#L199
- https://github.com/netty/netty-tcnative/commit/92dd66fd1243d85c05a61288f96367a70260b6b8
- https://github.com/netty/netty-tcnative/releases/tag/netty-tcnative-parent-2.0.84.Final
- https://github.com/netty/netty-tcnative/security/advisories/GHSA-gf9q-9mg7-g5qh

### [CVE-2026-65631](https://cna.erlef.org/cves/CVE-2026-65631.html)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-65631
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 05:17:58 JST
- 更新日: 2026-10-27 05:17:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: erlang-joseにおいて、パラメータが一部省略された攻撃者指定のRSA JWKを処理する際、素因数分解のループが非効率に実行されるアルゴリズム実効複雑性の脆弱性。
- 影響: 認証されていないリモートの攻撃者により、高負荷な処理を発生させてCPUリソースを枯渇させ、サービス拒否（DoS）状態を引き起こされる可能性があります。
- 推奨対応: 修正版のerlang-joseへのアップデート、またはパブリックAPIでの信頼できないJWKパース処理の見直しを検討してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-65631.html
- https://github.com/potatosalad/erlang-jose/commit/bfd336c0062bff93e65d08c22361897e96afd956
- https://github.com/potatosalad/erlang-jose/commit/d19e1ba68d88c68d29aa942be2573a22dbafca1f
- https://github.com/potatosalad/erlang-jose/security/advisories/GHSA-3m45-vrpj-xmrq
- https://osv.dev/vulnerability/EEF-CVE-2026-65631

### [CVE-2026-112415](https://support.apple.com/en-us/149227)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-112415
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 06:17:31 JST
- 更新日: 2026-10-27 10:19:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apple各種OSにおける入力検証不足に起因する境界外書き込み（Out-of-bounds write）の脆弱性。
- 影響: アプリケーションにより、予期しないシステム強制終了やプロセスメモリの破壊が引き起こされる可能性があります。
- 推奨対応: iOS/iPadOS 26.7.2/27.2、macOS 15.8.2/26.7.2/27.2、visionOS 27.2以降の修正済みバージョンへアップデートしてください。

#### References
- https://support.apple.com/en-us/149227
- https://support.apple.com/en-us/149230
- https://support.apple.com/en-us/149521
- https://support.apple.com/en-us/149522
- https://support.apple.com/en-us/149523

### [CVE-2026-116478](https://github.com/a2aproject/a2a-go/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-116478
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 05:17:55 JST
- 更新日: 2026-10-27 05:17:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: a2aproject a2a-go 2.4.0以前のPush Notification HandlerのCreateExecutor関数における、エラーメッセージを通じた情報漏洩の脆弱性。
- 影響: リモートの攻撃者により、エラーメッセージを介してシステムの内部情報を取得される可能性があります。
- 推奨対応: a2a-goをバージョン2.5.0以降へアップグレードしてください。

#### References
- https://github.com/a2aproject/a2a-go/
- https://github.com/a2aproject/a2a-go/commit/f4d588216b0c9520e94d571bab725c38ce23064c
- https://github.com/a2aproject/a2a-go/pull/393
- https://github.com/a2aproject/a2a-go/releases/tag/v2.5.0
- https://vuldb.com/cve/CVE-2026-116478

### [CVE-2026-65627](https://cna.erlef.org/cves/CVE-2026-65627.html)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-65627
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 05:17:58 JST
- 更新日: 2026-10-27 05:17:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: potatosalad jose (erlang-jose) において、zip: DEFヘッダーを持つJWEトークンの解凍処理時に出力サイズ制限を行わないデータ増幅の脆弱性。
- 影響: リモートの攻撃者により、高倍率で圧縮された小さなJWEトークンを用いてメモリを大量消費させられ、サービス拒否（DoS）状態を引き起こされる可能性があります。
- 推奨対応: 修正版のerlang-joseへアップデートするか、トークン解凍時のサイズ制限対策を行ってください。

#### References
- https://cna.erlef.org/cves/CVE-2026-65627.html
- https://github.com/potatosalad/erlang-jose/commit/857eb8e7f2d33e2c9ca2189e77226561cacaf2ad
- https://github.com/potatosalad/erlang-jose/commit/a7746ecd4950f85a393136e449a91dac62b5c429
- https://github.com/potatosalad/erlang-jose/security/advisories/GHSA-wfpv-qxp8-x5gm
- https://osv.dev/vulnerability/EEF-CVE-2026-65627

### [CVE-2026-65630](https://cna.erlef.org/cves/CVE-2026-65630.html)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-65630
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 05:17:58 JST
- 更新日: 2026-10-27 05:17:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: potatosalad joseの純粋Erlang実装によるX25519処理において、処理時間のおけるサイドチャネルが存在する脆弱性。
- 影響: タイミング攻撃により、長期的に使用しているX25519秘密鍵を推測・復元される可能性があります。
- 推奨対応: 修正版erlang-joseへの更新、またはC言語バインディング等の安全な暗号化実装の利用を検討してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-65630.html
- https://github.com/potatosalad/erlang-jose/commit/3670f873c274bba86fb7f5ee5727a7efa1322b79
- https://github.com/potatosalad/erlang-jose/commit/8e532095de114ef4bf88a9ec5d651fa251a972b3
- https://github.com/potatosalad/erlang-jose/security/advisories/GHSA-xvr2-gggj-h2pp
- https://osv.dev/vulnerability/EEF-CVE-2026-65630

### [CVE-2026-92171](https://access.redhat.com/security/cve/CVE-2026-92171)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-92171
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 00:16:45 JST
- 更新日: 2026-10-27 01:54:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Infinispan Operator for Red Hat Data Gridにおいて、xsite TLS有効化時にGossip Routerのパスワードがコマンドライン引数として平文で渡される脆弱性。
- 影響: Podの参照権限を持つユーザー、ノード上のプロセス、あるいは監査ログなどを通じてパスワードが情報漏洩する可能性があります。
- 推奨対応: 修正版オペレーターへの更新、およびコマンドライン引数での秘密情報受渡しを避ける設定へ見直してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-92171
- https://bugzilla.redhat.com/show_bug.cgi?id=2529806

### [CVE-2026-107090](http://maltego.com)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-107090
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 01:17:10 JST
- 更新日: 2026-10-27 03:39:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Maltego Windows Installer 4.13.0における実行ファイル解決ロジックの脆弱性。
- 影響: ローカルの攻撃者により、インストーラーを介して任意のコードを実行される可能性があります。
- 推奨対応: 修正された公式インストーラーを使用し、安全なディレクトリで実行してください。

#### References
- http://maltego.com
- https://gist.github.com/Vishnu-0609/87105bccf3bb524171a56a7a18480bfb

### [CVE-2026-107091](http://huion.com)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-107091
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 02:17:12 JST
- 更新日: 2026-10-27 03:41:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HUION Inspiroy Frego S (L310) Windows Driver 20.0.1.118のインストーラーにおけるDLL読み込みロジックの脆弱性。
- 影響: ローカルの攻撃者により、悪意のあるDLLを読み込ませることで任意のコードを実行される可能性があります。
- 推奨対応: 修正済みのドライバーインストーラーを取得して更新してください。

#### References
- http://huion.com
- https://gist.github.com/Vishnu-0609/44627ad4d1b6f1301440aece5d16c450

### [CVE-2026-112410](https://support.apple.com/en-us/149521)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-112410
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 06:17:30 JST
- 更新日: 2026-10-27 06:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: macOSにおけるメモリ管理の不備に起因する二重解放（Double Free）の脆弱性。
- 影響: リモートの攻撃者により、予期しないプロセスの強制終了を引き起こされる可能性があります。
- 推奨対応: macOS Sequoia 15.8.2、macOS Tahoe 26.7.2、macOS Golden Gate 27.2 以降へアップデートしてください。

#### References
- https://support.apple.com/en-us/149521
- https://support.apple.com/en-us/149522
- https://support.apple.com/en-us/149523

### [CVE-2026-112413](https://support.apple.com/en-us/149227)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-112413
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 06:17:30 JST
- 更新日: 2026-10-27 06:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apple製品における境界外読み取り（Out-of-bounds read）の脆弱性。境界チェックの改善により対処されました。
- 影響: 悪意を持って作成されたファイルを処理することにより、アプリが予期せず終了する可能性があります。
- 推奨対応: iOS/iPadOS 26.7.2および27.2、macOS Sequoia 15.8.2/Tahoe 26.7.2/Golden Gate 27.2、visionOS 27.2 以降などの修正済みバージョンへアップデートしてください。

#### References
- https://support.apple.com/en-us/149227
- https://support.apple.com/en-us/149230
- https://support.apple.com/en-us/149521
- https://support.apple.com/en-us/149522
- https://support.apple.com/en-us/149523

### [CVE-2026-112414](https://support.apple.com/en-us/149227)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-112414
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 06:17:31 JST
- 更新日: 2026-10-27 06:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apple製品におけるスタックオーバーフローの脆弱性。入力検証の改善により対処されました。
- 影響: 悪意を持って作成されたメッセージを処理することにより、サービス拒否（DoS）が発生する可能性があります。
- 推奨対応: iOS/iPadOS 26.7.2および27.2、macOS Sequoia 15.8.2/Tahoe 26.7.2/Golden Gate 27.2、visionOS 27.2 以降などの修正済みバージョンへアップデートしてください。

#### References
- https://support.apple.com/en-us/149227
- https://support.apple.com/en-us/149230
- https://support.apple.com/en-us/149521
- https://support.apple.com/en-us/149522
- https://support.apple.com/en-us/149523

### [CVE-2026-112416](https://support.apple.com/en-us/149227)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-112416
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 06:17:31 JST
- 更新日: 2026-10-27 06:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apple製品における境界外書き込み（Out-of-bounds write）の脆弱性。境界チェックの改善により対処されました。
- 影響: 悪意を持って作成された動画ファイルを処理することにより、アプリが予期せず終了する可能性があります。
- 推奨対応: iOS/iPadOS 26.7.2および27.2、macOS Sequoia 15.8.2/Tahoe 26.7.2/Golden Gate 27.2、tvOS 27.2、visionOS 27.2 以降などの修正済みバージョンへアップデートしてください。

#### References
- https://support.apple.com/en-us/149227
- https://support.apple.com/en-us/149230
- https://support.apple.com/en-us/149521
- https://support.apple.com/en-us/149522
- https://support.apple.com/en-us/149523

### [CVE-2026-112421](https://support.apple.com/en-us/149521)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-112421
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 06:17:31 JST
- 更新日: 2026-10-27 06:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: macOSにおけるシンボリックリンク処理に起因するレースコンディションの脆弱性。
- 影響: 悪意のあるアプリによって、ファイルシステムの保護された部分が変更される可能性があります。
- 推奨対応: macOS Golden Gate 27.2、macOS Sequoia 15.8.2、macOS Tahoe 26.7.2 以降などの修正済みバージョンへアップデートしてください。

#### References
- https://support.apple.com/en-us/149521
- https://support.apple.com/en-us/149522
- https://support.apple.com/en-us/149523

### [CVE-2026-112423](https://support.apple.com/en-us/149227)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-112423
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 06:17:31 JST
- 更新日: 2026-10-27 06:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apple製品における境界外読み取りの脆弱性。境界チェックの改善により対処されました。
- 影響: 悪意を持って作成されたファイルを処理することにより、サービス拒否（DoS）が発生するか、メモリ内容が漏洩する可能性があります。
- 推奨対応: iOS/iPadOS 26.7.2および27.2、macOS Sequoia 15.8.2/Tahoe 26.7.2/Golden Gate 27.2、visionOS 27.2 以降などの修正済みバージョンへアップデートしてください。

#### References
- https://support.apple.com/en-us/149227
- https://support.apple.com/en-us/149230
- https://support.apple.com/en-us/149521
- https://support.apple.com/en-us/149522
- https://support.apple.com/en-us/149523

### [CVE-2026-112424](https://support.apple.com/en-us/149521)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-112424
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 06:17:32 JST
- 更新日: 2026-10-27 06:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: macOSにおける境界外読み取りの脆弱性。境界チェックの改善により対処されました。
- 影響: アプリによって、システムの予期せぬ終了が引き起こされたり、カーネルメモリが読み取られたりする可能性があります。
- 推奨対応: macOS Golden Gate 27.2、macOS Sequoia 15.8.2、macOS Tahoe 26.7.2 以降などの修正済みバージョンへアップデートしてください。

#### References
- https://support.apple.com/en-us/149521
- https://support.apple.com/en-us/149522
- https://support.apple.com/en-us/149523

### [CVE-2026-72755](https://www.nlnetlabs.nl/downloads/routinator/CVE-2026-72755.txt)

> **Backend** / **LOW** / CVSS: **3.8** / KEV: **no**

- タイトル: CVE-2026-72755
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-27 03:18:41 JST
- 更新日: 2026-10-27 03:35:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Routinatorにおいて、HTTPSで新たに取得したTA証明書を検証なしでキャッシュに保存する処理の脆弱性。
- 影響: 検証に失敗した場合であっても、既存の正当なTA証明書が未検証のデータで上書きされる可能性があります。
- 推奨対応: Routinatorを修正済みバージョンにアップデートしてください。

#### References
- https://www.nlnetlabs.nl/downloads/routinator/CVE-2026-72755.txt

### [CVE-2026-115912](https://github.com/vllm-project/vllm/commit/3d5625cc3c2474994107047d7a6ecb8e4008f9b0)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-115912
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-27 02:17:18 JST
- 更新日: 2026-10-27 05:17:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: vLLMにおける共有メモリマルチモーダルキャッシュ使用時の不正なデシリアライズの脆弱性。
- 影響: 認証された攻撃者が偽造した引数を渡すことで、pickle.loads()を介して任意のPythonコードを実行できる可能性があります。
- 推奨対応: vLLM 0.32.0 以降に更新してください。

#### References
- https://github.com/vllm-project/vllm/commit/3d5625cc3c2474994107047d7a6ecb8e4008f9b0
- https://github.com/vllm-project/vllm/pull/59357
- https://github.com/vllm-project/vllm/releases/tag/v0.32.0
- https://github.com/vllm-project/vllm/security/advisories/GHSA-6757-hggm-hp2w

### [CVE-2026-115910](https://github.com/python-social-auth/social-core/commit/c2f2ae4663bef19ee8b07f2cf5a2344f9155d826)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-115910
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-27 02:17:18 JST
- 更新日: 2026-10-27 03:34:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Python Social Auth (social-core) の OpenIdConnectAuth における OpenID Connect ナンス（nonce）の検証不備の脆弱性。
- 影響: 被害者の認可コードを入手した攻撃者が、被害者になりすましてログインできる可能性があります（特にデフォルト設定でPKCEが無効な場合）。
- 推奨対応: social-core 6.2.0 以降に更新してください。

#### References
- https://github.com/python-social-auth/social-core/commit/c2f2ae4663bef19ee8b07f2cf5a2344f9155d826
- https://github.com/python-social-auth/social-core/pull/2141
- https://github.com/python-social-auth/social-core/releases/tag/6.2.0
- https://github.com/python-social-auth/social-core/security/advisories/GHSA-h2r5-x5m7-3935

### [CVE-2026-115927](https://github.com/tornadoweb/tornado/commit/ceab33581489751a66fba8566ad6d5960d4b01c8)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-115927
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-27 05:17:52 JST
- 更新日: 2026-10-27 05:17:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TornadoにおけるHTTP/1.1 チャンク転送符号化（chunked）デコード処理時のイベントループ占有の脆弱性。
- 影響: 未認証のリモート攻撃者が多数の小規模チャンクを送信することでイベントループを占有し、他の接続を応答停止（DoS）させたり、メモリを過剰消費させたりする可能性があります。
- 推奨対応: Tornado 6.6.0 以降に更新してください。

#### References
- https://github.com/tornadoweb/tornado/commit/ceab33581489751a66fba8566ad6d5960d4b01c8
- https://github.com/tornadoweb/tornado/pull/3773
- https://github.com/tornadoweb/tornado/releases/tag/v6.6.0
- https://github.com/tornadoweb/tornado/security/advisories/GHSA-r4j5-9xpp-3985

### [CVE-2026-115533](https://gist.github.com/mtholmquist/eba1cba80ea66997b8f7e6a839e49120)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-115533
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-27 05:17:51 JST
- 更新日: 2026-10-27 05:17:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LeRobot ライブラリの `from_pretrained()` 等における、安全でない動的クラスインスタンス化の脆弱性。
- 影響: 悪意のあるリポジトリや構成ファイルを読み込むことで、任意のコードが実行される可能性があります。
- 推奨対応: 信頼できないリポジトリからのモデルや構成のロードを避け、安全なバージョンが提供されている場合は速やかに更新してください。

#### References
- https://gist.github.com/mtholmquist/eba1cba80ea66997b8f7e6a839e49120

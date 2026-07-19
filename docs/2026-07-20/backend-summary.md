# Backend CVE Summary (2026-07-20)

## Overview

- 取得日時: 2026-07-20 08:05:33 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 27
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-63872](https://git.kernel.org/stable/c/2982e599fff6faa21c8df147d96fc7af6c1a2f24)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63872
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-20 00:16:54 JST
- 更新日: 2026-07-20 00:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのESP処理において、skb_to_sgvec関数の失敗時に古いページフラグメントの参照が解放されずリークする問題が修正されました。  
- 影響: 古いページフラグメントの参照リークによりメモリ消費が増加する可能性がありますが、具体的な影響範囲は不明です。  
- 推奨対応: Linuxカーネルの該当修正を適用し、関連するアップデートを導入することを推奨します。

#### References
- https://git.kernel.org/stable/c/2982e599fff6faa21c8df147d96fc7af6c1a2f24
- https://git.kernel.org/stable/c/e705b8ff4dd38fb8fe4e6fdc5378a86acea4feb5

### [CVE-2026-63876](https://git.kernel.org/stable/c/237dc8c08de3cb293b6607aaee8b13b3a671e267)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63876
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-20 01:17:04 JST
- 更新日: 2026-07-20 01:17:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのシリアルドライバ(zs)において、プラットフォームデバイスへの変換により、最初のシリアルポート初期化時のクラッシュを防止する修正が行われました。  
- 影響: 初期化時にカーネルページング要求の処理エラーが発生しクラッシュする可能性がありましたが、詳細な影響範囲は不明です。  
- 推奨対応: Linuxカーネルの該当修正を適用し、シリアルドライバの安定性向上を図ることが推奨されます。

#### References
- https://git.kernel.org/stable/c/237dc8c08de3cb293b6607aaee8b13b3a671e267
- https://git.kernel.org/stable/c/4dc9f1517503c883d5ce25b7ab29d177d05edc6a
- https://git.kernel.org/stable/c/6a83d5e24a84e746425cd93539130e5f7381ef47
- https://git.kernel.org/stable/c/7cac59d08a73cb866ec51a483a6f3fe0f531947c
- https://git.kernel.org/stable/c/bb2040484f90f91b717060e1a66026cc4287bcf0

### [CVE-2026-63877](https://git.kernel.org/stable/c/2ff0401ffddaccc85f758c8259912d686d052b31)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63877
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-20 01:17:04 JST
- 更新日: 2026-07-20 01:17:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのserial: dzドライバで、最初のシリアルポート初期化時にクラッシュが発生する問題が修正されました。  
- 影響: シリアルポート初期化時のカーネルクラッシュにより、システムの安定性が損なわれる可能性があります。  
- 推奨対応: Linuxカーネルを修正済みバージョンにアップデートし、該当ドライバの問題を回避してください。

#### References
- https://git.kernel.org/stable/c/2ff0401ffddaccc85f758c8259912d686d052b31
- https://git.kernel.org/stable/c/5c9fb95c8d6430d11dbb7b44fbe23222585cda86
- https://git.kernel.org/stable/c/5d7a49d60b8fda66da60e240fd7315232fa1754f
- https://git.kernel.org/stable/c/6f59646229490a93cda950017ad4bdfbfe770a1d
- https://git.kernel.org/stable/c/c9e78361fe92fb64662fc3c8f34e2cdbb8c25bc6

### [CVE-2026-63880](https://git.kernel.org/stable/c/1eb86334e391695d4a40743b114afc15df4dc506)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63880
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:05 JST
- 更新日: 2026-07-20 01:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのAMDGPUドライバで、メモリ確保失敗時にロックが解放されずリークする問題が修正されました。  
- 影響: /dev/dri/renderD*へのアクセス権を持つ任意のプロセスが、GPUコンテキストに対するサービス拒否（DoS）を引き起こす可能性があります。  
- 推奨対応: 最新のLinuxカーネルパッチを適用し、AMDGPUドライバの修正を取り込むことを推奨します。

#### References
- https://git.kernel.org/stable/c/1eb86334e391695d4a40743b114afc15df4dc506
- https://git.kernel.org/stable/c/2e7f55eb408c3f72ee1957a0d0ad11d8648a6379
- https://git.kernel.org/stable/c/8f643d534ffc6f1b6182e4f3acff8f04890504b9

### [CVE-2026-63913](https://git.kernel.org/stable/c/2006979a15af5404bf932a325357683c0bac1656)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63913
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:09 JST
- 更新日: 2026-07-20 01:17:09 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのnetfilterのconntrackで、無効なシーケンス番号のRSTパケットにより接続が誤ってCLOSE状態に遷移する問題が修正されました。  
- 影響: 不正なRSTパケットでアクティブなNAT接続が予期せず終了される可能性があります。  
- 推奨対応: Linuxカーネルの該当部分をアップデートし、RSTパケットの方向と有効性を正しく検証する修正を適用してください。

#### References
- https://git.kernel.org/stable/c/2006979a15af5404bf932a325357683c0bac1656
- https://git.kernel.org/stable/c/2bb6d82b586ea5a4cb73bbdd6b7432e96096bc77
- https://git.kernel.org/stable/c/6476c17d536dbd321c073242e762ddb2713a1238
- https://git.kernel.org/stable/c/b98ab51c45c5608a1c19ce7fd17a3032469bb83f
- https://git.kernel.org/stable/c/bed6e04be8e6b9133d8b16d5a42d0e0ce674fa9a

### [CVE-2026-63888](https://git.kernel.org/stable/c/5118ea225fe63b44207ba88047e4866e1ea43812)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63888
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-20 01:17:05 JST
- 更新日: 2026-07-20 01:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのiSCSIターゲット機能において、テキストフェーズ処理でのCRCバッファのオーバーリードと二重解放の脆弱性が修正されました。  
- 影響: 攻撃者が細工したパケットを送信することで、メモリの不正読み取りや二重解放による不安定化が発生する可能性があります。  
- 推奨対応: Linuxカーネルの該当部分を最新の修正パッチに更新し、iSCSIターゲット機能を利用している場合は適用を検討してください。

#### References
- https://git.kernel.org/stable/c/5118ea225fe63b44207ba88047e4866e1ea43812
- https://git.kernel.org/stable/c/6e22a1cdcc8277af4acc43710577157b77a02c5d
- https://git.kernel.org/stable/c/778c2ab142c625a8a8afa570e0f9b7873f445d99
- https://git.kernel.org/stable/c/89c81d1228c00fa6dd91de6c1c5aa1ef8a7875e3
- https://git.kernel.org/stable/c/badf178b76b0690851df00f4ca9cf2eb8eb0f963

### [CVE-2026-63942](https://git.kernel.org/stable/c/15b1723c1472e802f9f7e69ae4e64f7dbf588848)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63942
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-20 01:17:12 JST
- 更新日: 2026-07-20 01:17:12 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのparportサブシステムで、ポートとクライアントの登録処理に競合状態が存在し、初期化中のポートにクライアントドライバが接続されることでクラッシュが発生する可能性があります。  
- 影響: モジュールとしてビルドされたポートとクライアントドライバが同時にロードされる際に、システムのクラッシュを引き起こす恐れがあります。  
- 推奨対応: Linuxカーネルの該当パッチを適用し、ポート登録処理の競合を解消するアップデートを適用してください。

#### References
- https://git.kernel.org/stable/c/15b1723c1472e802f9f7e69ae4e64f7dbf588848
- https://git.kernel.org/stable/c/290f515c5e3b3900bc2fe24f179999fd08d23bfa
- https://git.kernel.org/stable/c/51026cff1f4f3b762a0b5a07c727bd59cef45320
- https://git.kernel.org/stable/c/74d6aae1df45d3414178986be743f946988fddf6
- https://git.kernel.org/stable/c/a1e81b58da0179531bedf0b9f2811f5f992d5c4b

### [CVE-2026-63858](https://git.kernel.org/stable/c/10f79dbd7719d1da9f5884d13060322d8729f091)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63858
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 00:16:52 JST
- 更新日: 2026-07-20 00:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのnetfilter nf_tablesで、デバイス削除時のフック管理に関する問題が修正されました。  
- 影響: フック削除処理の不整合により、netlinkのデータ取得に影響が出る可能性があります。  
- 推奨対応: 最新のLinuxカーネルパッチを適用し、該当の修正を取り込むことを検討してください。

#### References
- https://git.kernel.org/stable/c/10f79dbd7719d1da9f5884d13060322d8729f091
- https://git.kernel.org/stable/c/4e69bfb32b2db323d9205fdb30e284481b37817c

### [CVE-2026-63934](https://git.kernel.org/stable/c/15a0b3f33ffb6c78b3de6f69b026ceb09b973dd1)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63934
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:11 JST
- 更新日: 2026-07-20 01:17:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのiioサブシステムにおいて、itg3200ジャイロセンサーのi2c読み取り処理で誤ったスタック位置にデータを書き込むバグが修正されました。  
- 影響: ジャイロセンサーのデータが正しく取得できず、未初期化のスタック内容がユーザ空間に漏洩する可能性があります。  
- 推奨対応: Linuxカーネルの該当修正を適用し、影響を受けるシステムでのアップデートを推奨します。

#### References
- https://git.kernel.org/stable/c/15a0b3f33ffb6c78b3de6f69b026ceb09b973dd1
- https://git.kernel.org/stable/c/31bbd4b87dd6701fa10e03ba7f6268e49e178d16
- https://git.kernel.org/stable/c/63203bd072b613c18c237b906b1c9d2dc4527337
- https://git.kernel.org/stable/c/6bdc3023d62ed5c7d591f0eb27a5adb37fb892ae
- https://git.kernel.org/stable/c/8654b5e2617819ff4f7c78071dfd0275e971a9b6

### [CVE-2026-63950](https://git.kernel.org/stable/c/0fcc34d0d8fefca4fea349e45c10e3a3d90350eb)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63950
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:13 JST
- 更新日: 2026-07-20 01:17:13 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのメモリ管理において、nr_pages変数の初期化漏れにより、参照カウントやマップカウントの破損が発生する可能性がある問題が修正された。  
- 影響: メモリ管理の不整合により、カーネルの不安定化やクラッシュが起こる恐れがあるが、詳細な影響範囲は不明。  
- 推奨対応: Linuxカーネルの最新版にアップデートし、該当の修正が適用されていることを確認すること。

#### References
- https://git.kernel.org/stable/c/0fcc34d0d8fefca4fea349e45c10e3a3d90350eb
- https://git.kernel.org/stable/c/3f8968e9cbf95d5d87d32218906cab0b9b9eddbe
- https://git.kernel.org/stable/c/f611db9b771b2b6775357555d2517af044fca4f0

### [CVE-2026-63962](https://git.kernel.org/stable/c/3389c149c68c3fea61910ad5d34f7bf3bff44e32)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63962
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:15 JST
- 更新日: 2026-07-20 01:17:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのUSB Type-Cサブシステムにおいて、altmode_desc配列の境界チェックがループ内で不十分なため、バッファオーバーフローが発生する可能性があります。  
- 影響: 悪意のあるパートナー機器からの不正なメッセージにより、メモリ破損や予期しない動作が引き起こされる恐れがあります。  
- 推奨対応: Linuxカーネルの該当する修正パッチを適用し、信頼できないUSB Type-C機器の接続を避けることが望ましいです。

#### References
- https://git.kernel.org/stable/c/3389c149c68c3fea61910ad5d34f7bf3bff44e32
- https://git.kernel.org/stable/c/4505f33dab56c274e82f47f94bf60a8cbf8f4b42
- https://git.kernel.org/stable/c/845598b154b9a92e9d279fafafa9405c121ae805
- https://git.kernel.org/stable/c/cbad85b446c06adbc5e5bed565871bb918ce9d32

### [CVE-2026-63979](https://git.kernel.org/stable/c/c06876d4fac38f35820946ee3b1be7d7da799cd4)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63979
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:17 JST
- 更新日: 2026-07-20 01:17:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのnet/handshakeで、ソケットのファイル参照が不適切に解放されることで、解放済みメモリの読み取りが発生する脆弱性が修正されました。  
- 影響: 攻撃者が特定のタイミングで接続処理をキャンセルすると、NULL参照や解放済みメモリへのアクセスが起こる可能性があります。  
- 推奨対応: 最新のLinuxカーネルパッチを適用し、handshake関連の修正を取り込むことを推奨します。

#### References
- https://git.kernel.org/stable/c/c06876d4fac38f35820946ee3b1be7d7da799cd4
- https://git.kernel.org/stable/c/f4251190e58b209999c1ba9e6d2976136a1be055

### [CVE-2026-63986](https://git.kernel.org/stable/c/2008f9bb1ede9b688624a241228b8e54fc74f0f6)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63986
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:17 JST
- 更新日: 2026-07-20 01:17:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのethtoolで、エラーポインタをgenlmsg_cancelに渡す不具合が修正されました。  
- 影響: エラーハンドリング時にクラッシュが発生する可能性があります。  
- 推奨対応: 最新のLinuxカーネルにアップデートし、該当修正を適用してください。

#### References
- https://git.kernel.org/stable/c/2008f9bb1ede9b688624a241228b8e54fc74f0f6
- https://git.kernel.org/stable/c/c3fc9976f686f9a95baf87db9d387f218fd65394
- https://git.kernel.org/stable/c/d0d2c5ccd1de28368cebeef74d9c530a60eff9a5

### [CVE-2026-63996](https://git.kernel.org/stable/c/2f818cc98fd2c63a08239cb48995f6c3bfe9d9b3)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63996
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:39 JST
- 更新日: 2026-07-20 01:17:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのethtoolのcmisモジュールで、SFPモジュールからの応答長が想定より長い場合に発生する範囲外書き込みの脆弱性が修正されました。  
- 影響: 悪意のあるまたは不具合のあるSFPモジュールが異常な応答を返すことで、カーネルのメモリ破損が起こる可能性があります。  
- 推奨対応: Linuxカーネルの最新版にアップデートし、ethtoolのcmis関連の修正を適用してください。

#### References
- https://git.kernel.org/stable/c/2f818cc98fd2c63a08239cb48995f6c3bfe9d9b3
- https://git.kernel.org/stable/c/4d42fb88ec61f2e98c33a9e3a2de371d5edbc6b1
- https://git.kernel.org/stable/c/6c3f999a9d1338c6c89a9ff4549eafe72bc2e7b1
- https://git.kernel.org/stable/c/eb5dcd740cd7fa27bc2caeff2d28ef28e93ff4d3

### [CVE-2026-64007](https://git.kernel.org/stable/c/92170e6afe927ab2792a3f71902845789c8e31b1)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64007
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:40 JST
- 更新日: 2026-07-20 01:17:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのnetfilter synproxy機能において、TCPヘッダのチェックサム更新処理が解放済みメモリやスタック上のコピーに対して行われる可能性がある問題が修正されました。  
- 影響: TCPタイムスタンプオプションのチェックサムが不正確になることで、通信の整合性に影響を及ぼす恐れがありますが、詳細な影響範囲は明確ではありません。  
- 推奨対応: Linuxカーネルの該当部分を修正したアップデートを適用し、ネットワーク関連の脆弱性対策を行うことが望ましいです。

#### References
- https://git.kernel.org/stable/c/92170e6afe927ab2792a3f71902845789c8e31b1
- https://git.kernel.org/stable/c/9902a1058992de5d95656b64a3bd95c077f7ba2c
- https://git.kernel.org/stable/c/a91887a5b6ee4b98dfbf1db657ed2b879430149e
- https://git.kernel.org/stable/c/af2c22ccb1f621aff487ff47a040e38e058541e7
- https://git.kernel.org/stable/c/c7f945f7da097245a2f8ed7775ce48421047ee96

### [CVE-2026-64013](https://git.kernel.org/stable/c/614cb8c26c5aa53196ee9b211b76ee618b147d32)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64013
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:41 JST
- 更新日: 2026-07-20 01:17:41 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのACPIボタン処理において、ドライバー削除時に通知ハンドラーが解放されずリークする問題が修正されました。  
- 影響: ドライバー削除後にACPI通知が発生するとカーネルクラッシュや再プローブ失敗の可能性があります。  
- 推奨対応: 最新のLinuxカーネルにアップデートし、該当の修正を適用してください。

#### References
- https://git.kernel.org/stable/c/614cb8c26c5aa53196ee9b211b76ee618b147d32
- https://git.kernel.org/stable/c/fe80251152fed5b185f795ef2cd9f7fe9c3162e0

### [CVE-2026-64026](https://git.kernel.org/stable/c/46cb765e2e5ad52303ea157e10d370bb6b7acbbf)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64026
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:42 JST
- 更新日: 2026-07-20 01:17:42 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのrxrpcサブシステムで、splice()を用いたDATAパケットの復号処理に関する問題が修正されました。  
- 影響: パケットのページキャッシュ破損やデータ復号の不整合が解消され、暗号処理のパフォーマンスも改善される可能性があります。  
- 推奨対応: Linuxカーネルの該当修正を適用し、rxrpc関連の通信処理を安全に保つことを推奨します。

#### References
- https://git.kernel.org/stable/c/46cb765e2e5ad52303ea157e10d370bb6b7acbbf
- https://git.kernel.org/stable/c/a05bf6d9e621fa71e89ccebe3047ba45218d7b38
- https://git.kernel.org/stable/c/b94a6ccbaf1104dd980150a65fdeb2f69d17d2f5
- https://git.kernel.org/stable/c/c580087743712112778a06d65a4074053072d7bf
- https://git.kernel.org/stable/c/d2bc90cf6c75cb96d2ce549be6c35efa3099d25b

### [CVE-2026-64032](https://git.kernel.org/stable/c/1900ca8acb92fbea8bf9abef9927c7fed03db7fc)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64032
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:43 JST
- 更新日: 2026-07-20 01:17:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのブリッジ機能において、マルチキャストスヌーピングの設定変更時にポートのマルチキャストコンテキストが不適切に管理され、use-after-freeの脆弱性が修正されました。  
- 影響: ブリッジポートの削除時にメモリ破損が発生する可能性があり、システムの安定性やセキュリティに影響を与える恐れがあります。  
- 推奨対応: Linuxカーネルの該当する修正パッチを適用し、マルチキャストスヌーピング設定の変更操作を慎重に行うことを推奨します。

#### References
- https://git.kernel.org/stable/c/1900ca8acb92fbea8bf9abef9927c7fed03db7fc
- https://git.kernel.org/stable/c/4df78ff02629c7729168f0696a7a2123c389818d
- https://git.kernel.org/stable/c/7213256c91ed778a0997c2029c152b18dc50e4fd
- https://git.kernel.org/stable/c/a9224862d597d0eed0a34bbb27343f703fc4113f
- https://git.kernel.org/stable/c/ddefd1b8e5eb58933a697ab38334f0fd82e7fb8b

### [CVE-2026-64034](https://git.kernel.org/stable/c/09ec063d87c2dd3fa6f3561361a017bd882e9f37)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64034
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-20 01:17:43 JST
- 更新日: 2026-07-20 01:17:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのmanaモジュールで、DMAバッファからのhwc_msg_idの二重読み取りによるTOCTOU脆弱性が修正されました。  
- 影響: 悪意のあるハードウェアが検証済みの値を改変し、境界チェックを回避する可能性があります。  
- 推奨対応: 最新のLinuxカーネルにアップデートし、該当の修正を適用してください。

#### References
- https://git.kernel.org/stable/c/09ec063d87c2dd3fa6f3561361a017bd882e9f37
- https://git.kernel.org/stable/c/35f0f0a2536a4d604b4dbad92c85c4a8fdebb870
- https://git.kernel.org/stable/c/3c4db56ccd13dd020fbf43afabaee74a40ec75e4
- https://git.kernel.org/stable/c/566f42fb67a7ebfed6650e407e5b72e6b3e83bf7
- https://git.kernel.org/stable/c/6180a06bbc99fd9114b8db4be6c4d46e40f046ef

### [CVE-2026-63892](https://git.kernel.org/stable/c/37abc4504fa19d8f9f1e87792e8a2b8fdb308e40)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63892
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-20 01:17:06 JST
- 更新日: 2026-07-20 01:17:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのthunderboltプロパティ処理において、dir_lenが4未満の場合にサイズのアンダーフローやバッファオーバーリードが発生する脆弱性が修正されました。  
- 影響: 攻撃者が細工したプロパティを用いることで、カーネルメモリの不正読み取りやクラッシュを引き起こす可能性があります。  
- 推奨対応: Linuxカーネルの該当修正を適用し、dir_lenが4未満の入力を拒否する更新を導入してください。

#### References
- https://git.kernel.org/stable/c/37abc4504fa19d8f9f1e87792e8a2b8fdb308e40
- https://git.kernel.org/stable/c/3bec49ca55e08fb085cc4318f24b1b37eaab28cb
- https://git.kernel.org/stable/c/542a13890b742099c461d70920e97b14e568f6ec
- https://git.kernel.org/stable/c/5506c825f14d810f0690b1f4367cb7249ebb387a
- https://git.kernel.org/stable/c/d548179adcc87e1bc66b17e00352a1f536e76065

### [CVE-2026-63861](https://git.kernel.org/stable/c/3e79a563377a319d016ed0d3cd8c43171670c0f3)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63861
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-20 00:16:52 JST
- 更新日: 2026-07-20 00:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのmtk-snfiドライバで、NAND ECCエンジンの登録解除処理が不十分だった問題が修正されました。  
- 影響: probe失敗時やデバイス削除時にECCエンジンの登録解除が行われず、リソースリークや不整合が発生する可能性があります。  
- 推奨対応: 最新のLinuxカーネルバージョンにアップデートし、修正パッチを適用してください。

#### References
- https://git.kernel.org/stable/c/3e79a563377a319d016ed0d3cd8c43171670c0f3
- https://git.kernel.org/stable/c/6aea4a99410615912d80a4ba0827c4e8d4a8312d
- https://git.kernel.org/stable/c/86357e1d0157d8408b78f8768a69ab263d010316
- https://git.kernel.org/stable/c/98cf4b58299e0c6a537c68cd32155d9e7569e7cb
- https://git.kernel.org/stable/c/ab00febad191d7a4400aa1c3468279fb508258d4

### [CVE-2026-63871](https://git.kernel.org/stable/c/859bb1f4cb615d98c9c1ab2bd76ebb0b8fe46020)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63871
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-20 00:16:54 JST
- 更新日: 2026-07-20 00:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのBluetooth ISOモジュールで、iso_piフィールドへのデータ競合が発生する問題が修正されました。  
- 影響: 同一ソケット上でconnect()やsetsockopt()が同時に呼ばれた場合にデータ競合が起こり、予期しない動作やクラッシュの可能性があります。  
- 推奨対応: 最新のLinuxカーネルにアップデートし、該当の修正が適用されたバージョンを使用してください。

#### References
- https://git.kernel.org/stable/c/859bb1f4cb615d98c9c1ab2bd76ebb0b8fe46020
- https://git.kernel.org/stable/c/9798f7d41d85ff763afd1f1cc0533b5c416c8348
- https://git.kernel.org/stable/c/9ca7053d6215d89c33f28893bfd1625a32919d3f
- https://git.kernel.org/stable/c/ab84fd7779a2a7ff5d2c8eac212c43733f56216e

### [CVE-2026-63886](https://git.kernel.org/stable/c/4a3a19c98a8207ad08bec554703d90f2c34a8cc6)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63886
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-20 01:17:05 JST
- 更新日: 2026-07-20 01:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのiSCSIターゲットで、CHAP認証のBASE64デコード処理においてバッファオーバーフローの脆弱性が存在します。  
- 影響: 不適切な長さ検証により、メモリ破損が発生し、サービスの異常終了や潜在的なコード実行のリスクがあります。  
- 推奨対応: 最新のLinuxカーネルパッチを適用し、CHAP_Rの長さ検証が適切に行われるように修正されたバージョンを使用してください。

#### References
- https://git.kernel.org/stable/c/4a3a19c98a8207ad08bec554703d90f2c34a8cc6
- https://git.kernel.org/stable/c/82454e6f21e56ea9a0a9de7d0ff7e1dfb83e34d6
- https://git.kernel.org/stable/c/85db7391310b1304d2dc8ae3b0b12105a9567147
- https://git.kernel.org/stable/c/bf154c657828ed05399bca5d98cf1611bb048b12
- https://git.kernel.org/stable/c/c04e85799356120209b351a148ac2db888d5ffd9

### [CVE-2026-63887](https://git.kernel.org/stable/c/26e4a304b7e6f1338c675d527608d32549c091db)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63887
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-20 01:17:05 JST
- 更新日: 2026-07-20 01:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのiSCSIターゲット機能で、8192バイトのバッファに対して最大32KiBのデータを書き込む可能性があり、ヒープオーバーランが発生する脆弱性が修正されました。  
- 影響: 攻撃者が細工したiSCSIログイン要求を送信することで、ヒープオーバーランによりメモリ破壊やサービス拒否が発生する恐れがあります。  
- 推奨対応: Linuxカーネルの該当バージョンに対して、修正パッチを適用し、iSCSIターゲット機能を利用している場合はアップデートを行うことを推奨します。

#### References
- https://git.kernel.org/stable/c/26e4a304b7e6f1338c675d527608d32549c091db
- https://git.kernel.org/stable/c/30bf335e8fe170322080ee001f05ca29c50680b3
- https://git.kernel.org/stable/c/4e9f0c4a645c995bc75c06c7b3644254ffb4c76b
- https://git.kernel.org/stable/c/594a40360012ce5f94c715d5e3b20fa3af7d525a
- https://git.kernel.org/stable/c/b19382dfc6e7dee6d3859ba44b6ca29e97a51627

### [CVE-2026-63905](https://git.kernel.org/stable/c/1036ac6148995feaf486014d32bf26bf993c06a9)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63905
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-20 01:17:08 JST
- 更新日: 2026-07-20 01:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: usbip: vudc: Fix use after free bug in vudc_remove due to race condition This patch follows up Zheng Wang's 2023 report of a use-after-free in vudc_remove(). The original thread stalled on Shuah Khan's request for runtime testing of the unplug/unbind p...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/1036ac6148995feaf486014d32bf26bf993c06a9
- https://git.kernel.org/stable/c/207bf80362df3fce8ebc9723351dcb1bc6d9ed0f
- https://git.kernel.org/stable/c/61704e5cf9cd7464b510eb606e7e2978b1160a64
- https://git.kernel.org/stable/c/88d459e5b5a46da1ef9fd6f52d9439343edeec88
- https://git.kernel.org/stable/c/a0638db2340ee053ab0450656a763fd111475e54

### [CVE-2026-63911](https://git.kernel.org/stable/c/7f83d174073234839aea176f265e517e0d50a1d2)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63911
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-20 01:17:08 JST
- 更新日: 2026-07-20 01:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのxfrmモジュールで、IPTFSの状態クローン時にランタイム状態が適切にリセットされず、use-after-freeやdouble-freeが発生する脆弱性が修正されました。  
- 影響: クローンされたIPTFS状態が不正に破棄されることで、メモリ破壊やシステムの不安定化が起こる可能性があります。  
- 推奨対応: 最新のLinuxカーネルアップデートを適用し、xfrmのIPTFS関連の修正を取り込むことを推奨します。

#### References
- https://git.kernel.org/stable/c/7f83d174073234839aea176f265e517e0d50a1d2
- https://git.kernel.org/stable/c/9327252e04626d4bb02ca8c0c108fbe8eabf0c5a
- https://git.kernel.org/stable/c/dfb9f6cbfa9826655a49698cf90eb800fce2178e

### [CVE-2026-63914](https://git.kernel.org/stable/c/00f2c451e57df50b1151d9b2254878f106b7c892)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63914
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-20 01:17:09 JST
- 更新日: 2026-07-20 01:17:09 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのxfrmサブシステムで、ネットワーク名前空間(netns)を考慮せずにマルチキャスト通知がinit_netに固定されていた問題が修正されました。  
- 影響: IKEデーモンが異なるnetns間で誤った通知を受け取ったり、自身のnetns内の通知を受け取れなかったりするため、IKEv2 MOBIKEのアドレス更新処理が正常に動作しない可能性があります。  
- 推奨対応: Linuxカーネルの該当修正を適用し、IKEデーモンの動作を確認してください。

#### References
- https://git.kernel.org/stable/c/00f2c451e57df50b1151d9b2254878f106b7c892
- https://git.kernel.org/stable/c/26ce8dbf2e23fe4fcc3351d19ef6d3fb703ed126
- https://git.kernel.org/stable/c/448bb92ca101dde8a6e88b4dc824044b4e341604
- https://git.kernel.org/stable/c/6df8157547347b5257bf640a0ae3dfc4411e06cd
- https://git.kernel.org/stable/c/7e2a4f7ca0952820731ef7bdadfc9a9e9d3571b4

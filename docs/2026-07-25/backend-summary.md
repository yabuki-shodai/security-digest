# Backend CVE Summary (2026-07-25)

## Overview

- 取得日時: 2026-07-25 08:12:50 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 26
- Critical: 2
- High: 11
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-66033](https://github.com/libssh2/libssh2/commit/a2ed82d40964bbc0d64cd717aa0a5a892117d2e6)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-66033
- 関連キーワード: go, express, openssl
- 影響製品: -
- 公開日: 2026-07-25 02:17:35 JST
- 更新日: 2026-07-25 02:17:35 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: libssh2のssh2_cipher_crypt()関数に整数アンダーフロー。悪意あるSSHサーバーがAES-GCM暗号交渉時にクライアントをクラッシュ可能。
- 影響: 認証前に接続クライアントが異常終了し、サービス拒否が発生する可能性。
- 推奨対応: libssh2を修正済みバージョンに更新すること。

#### References
- https://github.com/libssh2/libssh2/commit/a2ed82d40964bbc0d64cd717aa0a5a892117d2e6
- https://github.com/libssh2/libssh2/pull/2401
- https://www.vulncheck.com/advisories/libssh2-integer-underflow-dos-via-aes-gcm-cipher-negotiation

### [CVE-2026-65623](https://cna.erlef.org/cves/CVE-2026-65623.html)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-65623
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-25 02:17:34 JST
- 更新日: 2026-07-25 03:18:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: mtrudel banditのWebSocket断片再構築処理に非効率なアルゴリズム。多数の小さな断片を送信されるとCPU負荷が急増しDoSを引き起こす可能性。
- 影響: CPUリソース枯渇によるサービス停止のリスク。
- 推奨対応: 断片数の制限や再構築処理の最適化を検討すること。

#### References
- https://cna.erlef.org/cves/CVE-2026-65623.html
- https://github.com/mtrudel/bandit/commit/418ef7e906192a230ddba112f7a669c87b6b0e3a
- https://github.com/mtrudel/bandit/security/advisories/GHSA-vg8x-66vg-5pxh
- https://osv.dev/vulnerability/EEF-CVE-2026-65623
- https://github.com/mtrudel/bandit/security/advisories/GHSA-vg8x-66vg-5pxh

### [CVE-2026-66035](https://github.com/libssh2/libssh2/commit/42e33d81577ed4b95d4b4f6f845e5ee8efe5eeb4)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-66035
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-25 02:17:35 JST
- 更新日: 2026-07-25 04:17:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: libssh2のEncrypt-then-MAC暗号交渉でヒープバッファオーバーフロー。悪意あるSSHサーバーが接続クライアントのヒープメタデータを破壊可能。
- 影響: ヒープ破壊により任意コード実行やクラッシュの恐れ。
- 推奨対応: libssh2を修正済みバージョンに更新すること。

#### References
- https://github.com/libssh2/libssh2/commit/42e33d81577ed4b95d4b4f6f845e5ee8efe5eeb4
- https://github.com/libssh2/libssh2/pull/2198
- https://www.vulncheck.com/advisories/libssh2-heap-buffer-overflow-via-etm-cipher-negotiation

### [CVE-2026-64239](https://git.kernel.org/stable/c/0ba6c05156d9ff9fc6ca22b7690e2eec9eca66f7)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64239
- 関連キーワード: go, echo
- 影響製品: -
- 公開日: 2026-07-25 01:16:53 JST
- 更新日: 2026-07-25 01:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのDAMON sysfsで、領域ディレクトリ削除処理の遅延によりリスト破損やUse-After-Freeが発生する可能性。
- 影響: メモリ破損や予期せぬ動作のリスクがあるが詳細は不明。
- 推奨対応: Linuxカーネルの該当修正を適用し、システムを最新状態に保つこと。

#### References
- https://git.kernel.org/stable/c/0ba6c05156d9ff9fc6ca22b7690e2eec9eca66f7
- https://git.kernel.org/stable/c/2c33177023c92e76806c535ddbffaa3d3fc37777
- https://git.kernel.org/stable/c/441f92f7d386b85bad16de49db95a307cba048a2
- https://git.kernel.org/stable/c/a5fa42214de55e43d165144727ce9facb9fc6b08
- https://git.kernel.org/stable/c/c0e37017a452addec873865c94cf7a665663a9b2

### [CVE-2026-64248](https://git.kernel.org/stable/c/6eda71977ee11c222f8ad4cae4d18d50448e56f4)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64248
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-25 01:16:54 JST
- 更新日: 2026-07-25 01:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのMIPSアーキテクチャで、CPU停止処理がRCUに正しく通知されず、RCU待機が永久に続く可能性。
- 影響: RCU同期処理のブロックによるシステム停止や不安定化の恐れ。
- 推奨対応: Linuxカーネルの該当修正を適用し、システムを最新状態に保つこと。

#### References
- https://git.kernel.org/stable/c/6eda71977ee11c222f8ad4cae4d18d50448e56f4
- https://git.kernel.org/stable/c/9f3f3bdc6d9dac1a5a8262ee7ad0f2ff1527a7e7
- https://git.kernel.org/stable/c/9fef09df42df55ab819b285ea892e0fc1b95a9c4
- https://git.kernel.org/stable/c/e1919d026706544cb6e7251ec06e908edd6f34ee
- https://git.kernel.org/stable/c/f8a1ef884013dc99f712d3eb75624c7cd3fd94f6

### [CVE-2026-64250](https://git.kernel.org/stable/c/0833b2b84c2fc1387f8165f0cbf6a02d67f647a5)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64250
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-25 01:16:54 JST
- 更新日: 2026-07-25 01:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのLoongArchアーキテクチャで、CPU停止処理がRCUに正しく通知されず、RCU待機が永久に続く可能性。
- 影響: RCU同期処理のブロックによるシステム停止や不安定化の恐れ。
- 推奨対応: Linuxカーネルの該当修正を適用し、システムを最新状態に保つこと。

#### References
- https://git.kernel.org/stable/c/0833b2b84c2fc1387f8165f0cbf6a02d67f647a5
- https://git.kernel.org/stable/c/1fa22de588a65880d6fe54c38c87fffe7d519f60
- https://git.kernel.org/stable/c/262dadc619e69ebeb97affd334cd1078a9704e98
- https://git.kernel.org/stable/c/90e254f18b8c224460082329dd5c42fd30995c2f
- https://git.kernel.org/stable/c/a0269e928728f970c782319fee53d92d4ea4e512

### [CVE-2026-64252](https://git.kernel.org/stable/c/07c245bc39f94481fd75ff1ed54f7ab97111f3dd)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64252
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-25 01:16:54 JST
- 更新日: 2026-07-25 01:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのMIPS 64ビット構成で初期コンソール出力処理が誤ったメモリアドレスを参照し、カーネルクラッシュなどの予測不能な動作を引き起こす可能性がある問題が修正された。
- 影響: カーネルクラッシュや予期しない動作を引き起こす可能性がある。
- 推奨対応: Linuxカーネルの該当修正を適用すること。

#### References
- https://git.kernel.org/stable/c/07c245bc39f94481fd75ff1ed54f7ab97111f3dd
- https://git.kernel.org/stable/c/1c80327dedf05b8c8ca025b76c21235b19dd3a86
- https://git.kernel.org/stable/c/35212f2adc2cf15122b96b987519de235b855e46
- https://git.kernel.org/stable/c/6e61fc2e06e44b6d30248cc5bc47a58e75c2b43e
- https://git.kernel.org/stable/c/7fb13fd35110ebe95eb053faf79d018f51144d85

### [CVE-2026-64223](https://git.kernel.org/stable/c/2becaaeebe230ade1fcd5d0f1cde4d6ee93ec78f)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64223
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-25 01:16:50 JST
- 更新日: 2026-07-25 01:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのwifi mac80211で、交渉されたTTLMマップの解析において境界外読み取りが発生する可能性がある問題が修正された。
- 影響: 境界外読み取りによりメモリの不正アクセスが発生する可能性があるが、攻撃者によるポリシー変更は制限されている。
- 推奨対応: Linuxカーネルの該当修正を適用し、メモリ安全性を確保すること。

#### References
- https://git.kernel.org/stable/c/2becaaeebe230ade1fcd5d0f1cde4d6ee93ec78f
- https://git.kernel.org/stable/c/2dd9304727c7041df0a599595910bdbe02ad03c5
- https://git.kernel.org/stable/c/a6e6ccd5bd07155c2add6c74ce1a5e68ad3b95ea
- https://git.kernel.org/stable/c/f7d395dc5008168ac5b9c1ac2791e59a6078cca1

### [CVE-2026-64234](https://git.kernel.org/stable/c/5f2e2a240dc1846e049bc67e9c3cdf5b031d08bf)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64234
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-25 01:16:52 JST
- 更新日: 2026-07-25 01:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのtty serial pch_uartでdma_alloc_coherent()の失敗チェックが不足しており、NULLポインタ参照の可能性がある問題が修正された。
- 影響: NULLポインタ参照によるカーネルの不安定化やクラッシュの可能性がある。
- 推奨対応: Linuxカーネルの該当修正を適用し、DMA割り当て失敗時の適切な処理を行うこと。

#### References
- https://git.kernel.org/stable/c/5f2e2a240dc1846e049bc67e9c3cdf5b031d08bf
- https://git.kernel.org/stable/c/66f8bfea055b23719b4fd6ce207c44de37d82a59
- https://git.kernel.org/stable/c/6dd5c0ea139b586ad5a091677056dafd405cfe82
- https://git.kernel.org/stable/c/6fe472c1bbbe238e91141f7cabc1226e96a60d43
- https://git.kernel.org/stable/c/760df81763b391bb5f0dcb0b7597b736da753ae4

### [CVE-2026-64240](https://git.kernel.org/stable/c/060fca8e098387f949e4eedaf215d952e477ac12)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64240
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-25 01:16:53 JST
- 更新日: 2026-07-25 01:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのmedia rc igorplugusbドライバで、USB制御要求のセットアップパケットの誤ったポインタ渡しにより不正な制御方向警告が発生する問題が修正された。
- 影響: USB制御要求の誤動作や警告が発生する可能性がある。
- 推奨対応: Linuxカーネルの該当修正を適用し、正しいセットアップパケットを渡すこと。

#### References
- https://git.kernel.org/stable/c/060fca8e098387f949e4eedaf215d952e477ac12
- https://git.kernel.org/stable/c/0d880d2db9856e94127ab09331363bef59f98005
- https://git.kernel.org/stable/c/171022c7d594c133a45f92357a2a91475edabe20
- https://git.kernel.org/stable/c/2243ad78ce64d344754260533ae7730c2174a34a
- https://git.kernel.org/stable/c/5cc3f6db72f77d1a8f7f1cf4ac01803927ffdf15

### [CVE-2026-64251](https://git.kernel.org/stable/c/257595adf9dac15ae1edd9d07753fbc576a7583d)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64251
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-25 01:16:54 JST
- 更新日: 2026-07-25 01:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのpwrseqコアで、pwrseq_debugfs_seq_next()関数の参照カウント管理不整合によるUse-After-Freeが修正された。
- 影響: Use-After-Freeによりカーネルの不安定化や予期しない動作が発生する可能性がある。
- 推奨対応: Linuxカーネルの該当修正を適用し、参照カウント管理を一貫させること。

#### References
- https://git.kernel.org/stable/c/257595adf9dac15ae1edd9d07753fbc576a7583d
- https://git.kernel.org/stable/c/73569a44fca2992f0ca4a4c0104069741b9873a0
- https://git.kernel.org/stable/c/ba0b9f04c7a5f9887b8ce672eaf049502c0548ec
- https://git.kernel.org/stable/c/e91df6d273445c03f5aa302bfe147eda33d45794

### [CVE-2025-71408](https://aydinnyunus.github.io/2026/06/07/command-injection-nltk-collocations-eval/)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2025-71408
- 関連キーワード: python, express
- 影響製品: -
- 公開日: 2026-07-25 07:16:50 JST
- 更新日: 2026-07-25 07:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: NLTKのnltk.collocationsモジュールで、コマンドライン引数をevalに直接渡すことで任意のPythonコード実行が可能なevalインジェクション脆弱性が存在した。
- 影響: 攻撃者が任意のPythonコードやOSコマンドを実行できる可能性がある。
- 推奨対応: NLTKをバージョン3.9.3以降にアップデートし、evalの安全な使用を確保すること。

#### References
- https://aydinnyunus.github.io/2026/06/07/command-injection-nltk-collocations-eval/
- https://github.com/nltk/nltk/commit/66f14096d952ec8f04934f515e027534bd4eb0ac
- https://github.com/nltk/nltk/pull/3465
- https://github.com/nltk/nltk/releases/tag/3.9.3
- https://www.vulncheck.com/advisories/nltk-eval-injection-via-collocations-py-command-line-arguments

### [CVE-2026-48035](https://github.com/kerberosmansour/hulumi/pull/178)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-48035
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-07-25 04:16:58 JST
- 更新日: 2026-07-25 04:16:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: HulumiのAccountFoundationで、CloudTrail/Config監査ログがS3削除権限を持つ任意のプリンシパルにより削除可能であった問題が修正された。
- 影響: 監査ログの改ざんや削除により監査の信頼性が損なわれる可能性がある。
- 推奨対応: Hulumiをバージョン1.4.0以降にアップデートし、監査ログの不正削除を防止すること。

#### References
- https://github.com/kerberosmansour/hulumi/pull/178
- https://github.com/kerberosmansour/hulumi/releases/tag/v1.4.0
- https://github.com/kerberosmansour/hulumi/security/advisories/GHSA-2mxr-p26x-mj73

### [CVE-2026-56163](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-56163)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-56163
- 関連キーワード: kubernetes
- 影響製品: -
- 公開日: 2026-07-25 00:18:33 JST
- 更新日: 2026-07-25 05:48:18 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Microsoft Azure Kubernetes Serviceで重要な機能に認証が欠如しており、未認証の攻撃者がネットワーク経由で権限昇格可能な脆弱性が存在する。
- 影響: 攻撃者による権限昇格によりシステム制御が奪われる可能性がある。
- 推奨対応: Microsoftの提供する修正やアップデートを適用し、認証強化を行うこと。

#### References
- https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-56163

### [CVE-2026-61884](https://github.com/cisagov/CSAF/blob/develop/csaf_files/OT/white/2026/icsa-26-202-01.json)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-61884
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-25 07:16:50 JST
- 更新日: 2026-07-25 07:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Tycon Systems TPDIN-Monitor-WEB2のWeb管理インターフェースで、ログイン時のサーバー側認証検証が不十分であり、空の認証情報で管理者セッションを取得可能な問題がある。
- 影響: 攻撃者が管理者権限を取得し、機器の制御や設定変更が可能になる。
- 推奨対応: 製品のアップデートを適用し、認証処理の強化を行うこと。

#### References
- https://github.com/cisagov/CSAF/blob/develop/csaf_files/OT/white/2026/icsa-26-202-01.json
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-202-01
- https://www.tyconsystems.com/contact

### [CVE-2026-66027](https://github.com/geo-chen/oss/blob/main/suna.md)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-66027
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-25 01:16:55 JST
- 更新日: 2026-07-25 02:17:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SunaのメッセージキューAPIで、認証済み攻撃者が他ユーザーのキュー資源にアクセス・操作可能なアクセス制御不備が存在する。
- 影響: 他ユーザーのメッセージ読み取り・削除や悪意あるメッセージ注入により、権限を持つAIエージェントの誤動作を引き起こす可能性がある。
- 推奨対応: Sunaをバージョン0.9.102以降にアップデートし、アクセス制御を強化すること。

#### References
- https://github.com/geo-chen/oss/blob/main/suna.md
- https://github.com/kortix-ai/suna/commit/7536a7d47fc93abcb66e677fcc993b390c81296a
- https://github.com/kortix-ai/suna/pull/4373
- https://github.com/kortix-ai/suna/releases/tag/v0.9.102
- https://www.vulncheck.com/advisories/suna-broken-access-control-via-message-queue-api

### [CVE-2026-17107](https://access.redhat.com/security/cve/CVE-2026-17107)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-17107
- 関連キーワード: gin, kubernetes
- 影響製品: -
- 公開日: 2026-07-25 04:16:55 JST
- 更新日: 2026-07-25 05:49:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Red Hat Advanced Cluster Managementのcluster-proxy service-proxyで、認証済みユーザーが偽装グループヘッダーを注入し、管理クラスタでクラスタ管理者権限を取得可能な脆弱性。
- 影響: 認証済みユーザーによるクラスタ管理者権限の昇格が可能。
- 推奨対応: サービスプロキシのヘッダー処理を修正し、権限管理を強化することを推奨。

#### References
- https://access.redhat.com/security/cve/CVE-2026-17107
- https://bugzilla.redhat.com/show_bug.cgi?id=2506771

### [CVE-2026-65693](https://gist.github.com/W40X/584f4b088d310bc5280cc74bbf97831a)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-65693
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-07-25 01:16:55 JST
- 更新日: 2026-07-25 01:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Microweber CMS 2.0.20までで、認証済み管理者がメールテンプレートにTwig式を注入し、任意OSコマンドを実行可能なサーバーサイドテンプレートインジェクション。
- 影響: 認証済み管理者による任意コマンド実行が可能。
- 推奨対応: Twig環境にSandboxExtensionやSecurityPolicyを適用し、テンプレートの入力検証を強化すること。

#### References
- https://gist.github.com/W40X/584f4b088d310bc5280cc74bbf97831a
- https://www.vulncheck.com/advisories/microweber-cms-server-side-template-injection-via-mail-templates

### [CVE-2026-65708](https://github.com/Caycon/cve-advisories/blob/main/2026/sysPass/CVE-2026-65708.md)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-65708
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-25 02:17:34 JST
- 更新日: 2026-07-25 03:18:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: sysPass 3.2.11までで、認証済み攻撃者がACLチェックの欠如により他アカウントのファイル添付を不正に閲覧・操作可能な不適切な直接オブジェクト参照。
- 影響: 認証済みユーザーによる他アカウントの添付ファイルの不正アクセス・操作。
- 推奨対応: AccountFileControllerで適切な認可チェックを実装し、アクセス制御を強化すること。

#### References
- https://github.com/Caycon/cve-advisories/blob/main/2026/sysPass/CVE-2026-65708.md
- https://www.vulncheck.com/advisories/syspass-insecure-direct-object-reference-via-accountfilecontroller

### [CVE-2026-66038](https://code.ffmpeg.org/FFmpeg/FFmpeg/commit/e7cbfd1c507b57a806a5825b87d609963e862c8c)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-66038
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-25 05:18:20 JST
- 更新日: 2026-07-25 06:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: FFmpeg 8.1.2までのLCL/ZLIBデコーダで、未初期化ヒープメモリが情報漏洩する脆弱性。短いzlibストリーム処理時に未初期化データが出力に含まれる可能性。
- 影響: 攻撃者による未初期化メモリ内容の情報漏洩やASLR回避の可能性。
- 推奨対応: 修正済みバージョンにアップデートし、脆弱なデコーダ処理を回避すること。

#### References
- https://code.ffmpeg.org/FFmpeg/FFmpeg/commit/e7cbfd1c507b57a806a5825b87d609963e862c8c
- https://code.ffmpeg.org/FFmpeg/FFmpeg/pulls/23626
- https://www.vulncheck.com/advisories/ffmpeg-lcl-zlib-video-decoder-information-disclosure-via-lcldec-c

### [CVE-2026-8789](https://plugins.trac.wordpress.org/changeset?reponame=&old=3595856%40easy-appointments&new=3595856%40easy-appointments)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-8789
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-25 00:19:08 JST
- 更新日: 2026-07-25 05:45:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WordPressのEasy Appointmentsプラグイン3.12.27までで、権限チェックとnonce検証の欠如により、Contributor以上の認証ユーザーが任意の接続レコードを削除可能。
- 影響: 認証ユーザーによるデータの不正削除で予約機能が妨害される可能性。
- 推奨対応: 権限チェックとnonce検証を追加し、不正な操作を防止すること。

#### References
- https://plugins.trac.wordpress.org/changeset?reponame=&old=3595856%40easy-appointments&new=3595856%40easy-appointments
- https://www.wordfence.com/threat-intel/vulnerabilities/id/47ed52b3-4bfe-46ce-aabc-7a4647ab7db5?source=cve

### [CVE-2026-64232](https://git.kernel.org/stable/c/0943f81e1b3176f27dbaf6db268fc69d8a94f0ba)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64232
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-25 01:16:52 JST
- 更新日: 2026-07-25 01:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのblk_insert_cloned_requestで、積層ドライバの整合性セグメント数の再計算不備によりBUG_ONが発生する問題が修正された。
- 影響: 特定条件下でカーネルのBUG_ONが発生し、システムの安定性に影響する可能性。
- 推奨対応: Linuxカーネルの該当修正を適用し、積層ドライバの整合性処理を改善すること。

#### References
- https://git.kernel.org/stable/c/0943f81e1b3176f27dbaf6db268fc69d8a94f0ba
- https://git.kernel.org/stable/c/2c6e6a18a37b905cb584eb0dda3ae482162a81ca
- https://git.kernel.org/stable/c/42929c98d044f126508baf54a65b0f87f932fa75
- https://git.kernel.org/stable/c/53a01bcc0242590eda4c452a5bd996f62457113b

### [CVE-2026-66005](https://github.com/janhq/jan/commit/3e1c1e724f696620d89bb4a9cc18a380e0753757)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-66005
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-25 00:19:07 JST
- 更新日: 2026-07-25 01:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Jan 0.8.4までのローカルAPIサーバでCORS設定ミスにより、ネットワーク内攻撃者が信頼ホスト制限を回避し、認証不要のAPI操作が可能。
- 影響: ネットワーク内攻撃者によるAPIの不正利用や情報取得の可能性。
- 推奨対応: CORS設定を見直し、信頼ホストの適切な制限を実施すること。

#### References
- https://github.com/janhq/jan/commit/3e1c1e724f696620d89bb4a9cc18a380e0753757
- https://github.com/janhq/jan/issues/8453
- https://github.com/janhq/jan/pull/8506
- https://www.vulncheck.com/advisories/jan-local-api-server-cors-origin-reflection-via-binding

### [CVE-2026-17039](https://access.redhat.com/security/cve/CVE-2021-20179)

> **Backend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-17039
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-25 01:16:34 JST
- 更新日: 2026-07-25 05:49:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: pki-coreで、証明書更新要求においてレルムベースの認可チェックが欠如し、認証済みユーザーが他レルムの証明書を更新可能な問題。
- 影響: 認証ユーザーによる他レルム証明書の不正更新。
- 推奨対応: 証明書更新処理にレルム認可チェックを追加し、権限管理を強化すること。

#### References
- https://access.redhat.com/security/cve/CVE-2021-20179
- https://access.redhat.com/security/cve/CVE-2026-17039
- https://bugzilla.redhat.com/show_bug.cgi?id=2506720
- https://github.com/dogtagpki/pki/blob/master/base/ca/database/ds/acl.ldif
- https://github.com/dogtagpki/pki/blob/master/base/ca/src/main/java/com/netscape/cms/servlet/cert/EnrollmentProcessor.java

### [CVE-2026-64211](https://git.kernel.org/stable/c/593889c401426004bd0ea0f6d4fcece728b03420)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64211
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-25 01:16:48 JST
- 更新日: 2026-07-25 01:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのsrcuで、CPUがオンラインになる前にワークキュー処理がキューイングされる問題が修正された。これによりs390でハングが発生する可能性があった。
- 影響: 特定環境でシステムハングの発生リスク。
- 推奨対応: 修正パッチを適用し、CPUオンライン状態の管理を改善すること。

#### References
- https://git.kernel.org/stable/c/593889c401426004bd0ea0f6d4fcece728b03420
- https://git.kernel.org/stable/c/a4153538fcd2361c4e0039eb103265492d26044e

### [CVE-2026-64212](https://git.kernel.org/stable/c/3a74aaad047353da3344aed32e9042d4f334f926)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64212
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-25 01:16:48 JST
- 更新日: 2026-07-25 01:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのiwlwifiドライバで、NULLチェック前にポインタを参照する不具合が修正された。これによりuse-after-freeの可能性があった。
- 影響: カーネルクラッシュや予期しない動作のリスク。
- 推奨対応: 修正済みカーネルにアップデートし、ポインタの安全な扱いを確保すること。

#### References
- https://git.kernel.org/stable/c/3a74aaad047353da3344aed32e9042d4f334f926
- https://git.kernel.org/stable/c/b6b4db85c7baf0788c5e7ec61350c1ff2bb775e0
- https://git.kernel.org/stable/c/d733ed481fd20a8e7bfe5119c4e77761ba3f87ee

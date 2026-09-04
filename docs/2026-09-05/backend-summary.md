# Backend CVE Summary (2026-09-05)

## Overview

- 取得日時: 2026-09-05 08:58:46 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 26
- Critical: 3
- High: 8
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-85684](https://github.com/datalab-to/marker)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-85684
- 関連キーワード: fastapi
- 影響製品: -
- 公開日: 2026-09-05 00:17:46 JST
- 更新日: 2026-09-05 00:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: marker 2.0.0 までの FastAPI /marker/upload ハンドラにおける file.filename パラメータのサニタイズ不備によるパストラバーサル脆弱性です。
- 影響: 未認証の攻撃者により、システム上の任意の場所にファイルを書き込まれたり、既存ファイルを削除されたりする可能性があります。
- 推奨対応: 修正パッチの適用、またはファイル名取得時のディレクトリトラバーサル対策の実装が推奨されます。

#### References
- https://github.com/datalab-to/marker
- https://github.com/datalab-to/marker/blob/v2.0.0/marker/scripts/server.py
- https://github.com/datalab-to/marker/issues/1047
- https://www.vulncheck.com/advisories/marker-through-2.0.0-path-traversal-via-upload-filename

### [CVE-2026-85692](https://github.com/ccfos/nightingale)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-85692
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 00:17:47 JST
- 更新日: 2026-09-05 03:18:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nightingale (n9e) の http_fetch ツールにおける SSRF 防御機能（isPublicIP）が、特定形式のIPv6アドレス（6to4, NAT64等）を十分に検証しない脆弱性です。
- 影響: 攻撃者が特別なIPv6形式のURLを与えることでフィルタをバイパスし、内部ネットワークやクラウドのメタデータサービスにアクセスされる可能性があります。
- 推奨対応: 対策された最新コードへの更新、およびSSRFフィルタにおけるIPv6アドレス検証範囲の修正が推奨されます。

#### References
- https://github.com/ccfos/nightingale
- https://github.com/ccfos/nightingale/blob/v9.1.1/aiagent/tools/http.go
- https://github.com/ccfos/nightingale/issues/3363
- https://www.vulncheck.com/advisories/nightingale-9.1.1-ssrf-guard-bypass-via-ipv6-encoding
- https://github.com/ccfos/nightingale/issues/3363

### [CVE-2026-85623](https://github.com/aaif-goose/goose)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-85623
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 00:17:42 JST
- 更新日: 2026-09-05 00:17:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: goose 1.37.0 において、レシピの stdio 拡張や retry.checks に含まれるコマンドを検証なしで実行してしまう脆弱性です。
- 影響: 悪意のあるレシピを読み込むことで、gooseを実行しているユーザーの権限で任意のシェルコマンドを実行される可能性があります。
- 推奨対応: 信頼できないレシピの利用を避け、セキュリティ検証が強化された最新版へ更新することが推奨されます。

#### References
- https://github.com/aaif-goose/goose
- https://github.com/aaif-goose/goose/blob/v1.49.0/crates/goose/src/agents/extension_manager.rs
- https://github.com/aaif-goose/goose/blob/v1.49.0/crates/goose/src/recipe/mod.rs
- https://github.com/aaif-goose/goose/issues/10325
- https://www.vulncheck.com/advisories/goose-1.37.0-arbitrary-command-execution-via-recipe-extensions

### [CVE-2026-81859](https://www.ibm.com/support/pages/node/7285931)

> **Backend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-81859
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 00:17:35 JST
- 更新日: 2026-09-05 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CP4BA - IBM Enterprise Records において、脆弱または推奨されない暗号化アルゴリズムが使用されている脆弱性です。
- 影響: ローカルの攻撃者により、暗号化された解読・解析を通じて機密情報を取得される可能性があります。
- 推奨対応: IBMが提供する修正パッチの適用や、より安全な暗号化アルゴリズムへの変更が推奨されます。

#### References
- https://www.ibm.com/support/pages/node/7285931

### [CVE-2026-82729](https://cna.erlef.org/cves/CVE-2026-82729.html)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-82729
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 00:17:36 JST
- 更新日: 2026-09-05 05:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: elixir-mint (mint) の Chunked 応答解析処理において、ヘキサデシマル桁数制限がないことによるアルゴリズム複雑性の脆弱性です。
- 影響: 悪意のあるHTTPサーバーから巨大な桁数の応答を受信した場合、クライアントのCPUリソースが枯渇し、サービス拒否（DoS）を引き起こす可能性があります。
- 推奨対応: ライブラリを最新バージョンへ更新し、解析時の入力制限を設けることが推奨されます。

#### References
- https://cna.erlef.org/cves/CVE-2026-82729.html
- https://github.com/elixir-mint/mint/commit/bd2a4e7513594997c140cfef9fe0e968712fb588
- https://github.com/elixir-mint/mint/security/advisories/GHSA-7p8w-j234-7qc8
- https://osv.dev/vulnerability/EEF-CVE-2026-82729
- https://github.com/elixir-mint/mint/security/advisories/GHSA-7p8w-j234-7qc8

### [CVE-2026-80776](https://git.kernel.org/stable/c/19b4be0717fa83265d66aea836b7022d898422cf)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80776
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:03 JST
- 更新日: 2026-09-05 01:18:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの futex_pivot_pending() において、プライベートハッシュのリサイズ時に発生する競合状態の脆弱性です。
- 影響: タスクが無期限に停止（Dステート）し、カーネルパニックやシステムの応答停止を引き起こす可能性があります。
- 推奨対応: 本問題を修正したカーネルバージョンへの更新が推奨されます。

#### References
- https://git.kernel.org/stable/c/19b4be0717fa83265d66aea836b7022d898422cf
- https://git.kernel.org/stable/c/4a7e941ca29a608c6244cbd028d3599ecaef7207
- https://git.kernel.org/stable/c/8e7ff730dd96519a333d1570edf1c3fabb6d3629

### [CVE-2026-80787](https://git.kernel.org/stable/c/1ed1eeaef55cebf2d74b3ef104c20bdab719b165)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80787
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:04 JST
- 更新日: 2026-09-05 01:18:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのNVMe Target (PCI EPF)実装において、コマンド処理関数 nvmet_pci_epf_exec_iod_work() で非同期完了後に解放済みのiod構造体を参照するUse-After-Freeの脆弱性が存在します。
- 影響: カーネルのクラッシュ（DoS）や不安定化、あるいは不正なメモリ参照によるセキュリティ上の影響が生じる可能性があります。
- 推奨対応: 修正パッチが適用された Linux カーネルの更新版へアップデートすることが推奨されます。

#### References
- https://git.kernel.org/stable/c/1ed1eeaef55cebf2d74b3ef104c20bdab719b165
- https://git.kernel.org/stable/c/20be486d1c225402b067391e72ff5b0dd8ebff76
- https://git.kernel.org/stable/c/c9e9bb757971485b4e8414b1744507af186d72c9
- https://git.kernel.org/stable/c/cede8d2852570c79b9bbb9527255ae9ed3317b82

### [CVE-2026-80788](https://git.kernel.org/stable/c/737a3b535247226f6e1a7988fd9d6e63e7d6fc71)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80788
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:04 JST
- 更新日: 2026-09-05 01:18:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの NVMe over Fabrics TCP (nvmet-tcp) において、リモートのイニシエータから過大なSGL要求を送信することで、メモリ割当時の警告(WARN_ON_ONCE_GFP)を誘発させられる脆弱性が存在します。
- 影響: 警告発生時にパニックを起こす設定（panic-on-warn）が有効なシステムにおいて、リモートからサービス拒否（DoS）を引き起こされる可能性があります。
- 推奨対応: 修正パッチが適用された Linux カーネルの更新版へアップデートすることが推奨されます。

#### References
- https://git.kernel.org/stable/c/737a3b535247226f6e1a7988fd9d6e63e7d6fc71
- https://git.kernel.org/stable/c/7b6a54d4e7b0da423c2b53ed293fd36b16c0b19e
- https://git.kernel.org/stable/c/7fd6da0f28932442b51658bac4ff55565ca9b377
- https://git.kernel.org/stable/c/86cc450022473c4a29b43a09f3ec22a9ef566dac
- https://git.kernel.org/stable/c/8d01f0d0e96485e39ad89b859ef85e1dc3020465

### [CVE-2026-80795](https://git.kernel.org/stable/c/0dc59de0075f88404a0f4a2b5233104ef459fbb2)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80795
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:06 JST
- 更新日: 2026-09-05 01:18:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのNFC (NCI) サブシステムにおいて、nci_target_auto_activated() が配列の上限数を検証せずにターゲットを追加するため、スラブ領域での境界外書き込み（Out-of-bounds write）が発生します。
- 影響: カーネルメモリの破損によるシステムクラッシュや、任意のコード実行などの権限昇格につながる可能性があります。
- 推奨対応: 修正パッチが適用された Linux カーネルの更新版へアップデートすることが推奨されます。

#### References
- https://git.kernel.org/stable/c/0dc59de0075f88404a0f4a2b5233104ef459fbb2
- https://git.kernel.org/stable/c/129032c0616d83a5e3e304f6ebf88f14ba01e5f7
- https://git.kernel.org/stable/c/24761d3a5f692df5f7d848caeabcb2afd10917aa
- https://git.kernel.org/stable/c/2f08dbce3b37624ec6b424d759336a99586170ec
- https://git.kernel.org/stable/c/50e87e1c0e18d791dcd7dccf30f9a2f3e2cf3951

### [CVE-2026-80824](https://git.kernel.org/stable/c/0a960b88c5979f853019d4dc4957dfbeeb193440)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80824
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:10 JST
- 更新日: 2026-09-05 01:18:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの usbfs ドライバにおいて、usbdev_release() で非同期URBのドレイン処理を完了する前にデバイスの参照を破棄するため、解放済みメモリへのアクセス（Use-After-Free）が発生します。
- 影響: /dev/bus/usb ノードへのアクセス権を持つローカルの非特権ユーザーによって、カーネルのクラッシュや権限昇格を引き起こされる可能性があります。
- 推奨対応: 修正パッチが適用された Linux カーネルの更新版へアップデートすることが推奨されます。

#### References
- https://git.kernel.org/stable/c/0a960b88c5979f853019d4dc4957dfbeeb193440
- https://git.kernel.org/stable/c/0dd68b5d01d022fc9c5e71c82a82b0a94d3d0671
- https://git.kernel.org/stable/c/47a7f98fbb5006d46d15a3a210ffdc61448a4f19
- https://git.kernel.org/stable/c/5f08c45bdcfd28d1171de38c5ef29fc89a76eedc
- https://git.kernel.org/stable/c/65879e0a452ca2a234b9475e0c11aff7a4343738

### [CVE-2026-80833](https://git.kernel.org/stable/c/8ab58786b4c63b8f1b6c522f33bb67a3c8c2791f)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80833
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:11 JST
- 更新日: 2026-09-05 01:18:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Allwinner sun8i-ss 暗号ドライバの crypto_rng インターフェースにおいて、DMA中断処理の不備による Use-After-Free やバッファオーバーリードの脆弱性が存在します（非推奨機能としてインターフェース自体が削除されました）。
- 影響: 暗号処理実行時にカーネルクラッシュや情報の不正読み取りが発生する可能性があります。
- 推奨対応: 該当コードの削除を含む修正パッチが適用された Linux カーネルへ更新することが推奨されます。

#### References
- https://git.kernel.org/stable/c/8ab58786b4c63b8f1b6c522f33bb67a3c8c2791f
- https://git.kernel.org/stable/c/a78446ee6fae86ac8733f120e3ffce2e5d9384f5

### [CVE-2026-80834](https://git.kernel.org/stable/c/011556f71d094da61379ae3672692cae2795304e)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80834
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:11 JST
- 更新日: 2026-09-05 01:18:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Allwinner sun8i-ce 暗号ドライバの crypto_rng インターフェースにおいて、シグナル受信時の処理不備により Use-After-Free の脆弱性が存在します（非推奨機能としてインターフェース自体が削除されました）。
- 影響: 暗号処理実行時にカーネルクラッシュや不整合が発生する可能性があります。
- 推奨対応: 該当コードの削除を含む修正パッチが適用された Linux カーネルへ更新することが推奨されます。

#### References
- https://git.kernel.org/stable/c/011556f71d094da61379ae3672692cae2795304e
- https://git.kernel.org/stable/c/1017f987c5f0841f00408a78f947990c9d84b346

### [CVE-2026-80835](https://git.kernel.org/stable/c/14d9ee8286460a7b82f3b8610b5c7ebf4550b06b)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80835
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:11 JST
- 更新日: 2026-09-05 01:18:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Qualcomm RNG ドライバにおいて、crypto_rng と hwrng インターフェースの同時アクセス制御が適切に行われておらず、同一レジスタへの競合が発生する脆弱性が存在します（crypto_rng インターフェースが削除されました）。
- 影響: 乱数生成時に同じ出力が繰り返される、またはランダムでない値が出力されるなど、暗号的安全性が低下する可能性があります。
- 推奨対応: 該当コードの修正・削除が適用された Linux カーネルへ更新することが推奨されます。

#### References
- https://git.kernel.org/stable/c/14d9ee8286460a7b82f3b8610b5c7ebf4550b06b
- https://git.kernel.org/stable/c/2ecdf5c9910e20f73639bc322f0518a3439d17c0
- https://git.kernel.org/stable/c/669d940351eda316b82e24986e2e0e057653ce7d
- https://git.kernel.org/stable/c/843e2bdaf8deb8bc341203094dfe582e38ea4af2
- https://git.kernel.org/stable/c/bb474dcd9d0224264a27a60891f00872b879835f

### [CVE-2026-80843](https://git.kernel.org/stable/c/37426395cb90ef217beec8407a14bd82153793d3)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80843
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:12 JST
- 更新日: 2026-09-05 01:18:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの XFRM サブシステムにおいて、特定認証アルゴリズム処理時の判定不備により、割り当て済みのメモリ構造体が上書きされ漏洩するメモリリークの問題が存在します。
- 影響: カーネルメモリが徐々に枯渇し、長期的にはシステムの不安定化やDoSにつながる可能性があります。
- 推奨対応: 修正パッチが適用された Linux カーネルの更新版へアップデートすることが推奨されます。

#### References
- https://git.kernel.org/stable/c/37426395cb90ef217beec8407a14bd82153793d3
- https://git.kernel.org/stable/c/71d42da01740ec6557837bebec0bc48cfc3b4c39
- https://git.kernel.org/stable/c/958ae9f261319e1cdc44879886bcda2263258cca
- https://git.kernel.org/stable/c/ba0c110c205855b3f1e3130d8c0fdb484d704c8c
- https://git.kernel.org/stable/c/be19d20e53a239572bb2a28efcc1cd2b069b1ef9

### [CVE-2026-80849](https://git.kernel.org/stable/c/2857dcbd03cf3354af0fba1b65c6a260fb43811a)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80849
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:13 JST
- 更新日: 2026-09-05 01:18:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの TCP-AO (TCP Authentication Option) 実装において、ソケット再接続時に解放された鍵オブジェクトへアクセスしてしまう Use-After-Free の脆弱性が存在します。
- 影響: 通信処理中にカーネルクラッシュやシステムの不安定化が引き起こされる可能性があります。
- 推奨対応: 修正パッチが適用された Linux カーネルの更新版へアップデートすることが推奨されます。

#### References
- https://git.kernel.org/stable/c/2857dcbd03cf3354af0fba1b65c6a260fb43811a
- https://git.kernel.org/stable/c/73fde8fe4469f4ed8f0afcc0b9d6413002a9e6b3
- https://git.kernel.org/stable/c/84a93b4e012587d0a4a84ffb23ec6da18e9d85f9
- https://git.kernel.org/stable/c/da4471557f279d0f56605158a625bb6e49ef7d41
- https://git.kernel.org/stable/c/e54ad693eddb40c595add013f545354c538e325b

### [CVE-2026-80853](https://git.kernel.org/stable/c/97f6402f5950ca3450541287c4b3664f3acda976)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80853
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:14 JST
- 更新日: 2026-09-05 01:18:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SNPが有効なホスト上の KVM (SEV/SEV-ES) において、メモリの暗号化/復号化用バッファに不完全なページ割当が行われ、ファームウェアへの権限譲渡時に他カーネル処理と競合する問題が存在します。
- 影響: 仮想マシンメモリ処理の失敗や、カーネルクラッシュなどの予期せぬ動作が発生する可能性があります。
- 推奨対応: 修正パッチが適用された Linux カーネルの更新版へアップデートすることが推奨されます。

#### References
- https://git.kernel.org/stable/c/97f6402f5950ca3450541287c4b3664f3acda976
- https://git.kernel.org/stable/c/a33c40b93ccf5177e042253807d40e0b92e7f206

### [CVE-2026-80855](https://git.kernel.org/stable/c/1b04d80a27d317064cce2307472f5bef9975bc50)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80855
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-05 01:18:14 JST
- 更新日: 2026-09-05 01:18:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのFUSE機能におけるDAX処理のロック解除不備。
- 影響: 処理失敗時に適切なロック解除が行われず、対象ファイルへの後続処理がストール（応答停止）する可能性があります。
- 推奨対応: 修正パッチの適用やカーネルの更新を検討してください。

#### References
- https://git.kernel.org/stable/c/1b04d80a27d317064cce2307472f5bef9975bc50
- https://git.kernel.org/stable/c/1d3e701cda2f41d48aa721b3ebefbe0fbf8d74da
- https://git.kernel.org/stable/c/7288c279ddbd654a06c82118c1a3f5570c1807f0
- https://git.kernel.org/stable/c/776e85fda752f9a15e0f82dec42ecacd12a9bd94
- https://git.kernel.org/stable/c/a61524da59a2f5ac9c8de23ff98b30da769ab144

### [CVE-2026-85694](https://github.com/lavague-ai/LaVague)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-85694
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-05 00:17:47 JST
- 更新日: 2026-09-05 00:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LaVague 0.2.35におけるプロンプトインジェクション起因のリモートコード実行の脆弱性。
- 影響: 悪意あるWebコンテンツを解釈させることで、ホスト上で任意のPythonコードが実行される可能性があります。
- 推奨対応: ソフトウェアを修正済みバージョンへ更新し、不信頼な外部出力の自動実行を制限してください。

#### References
- https://github.com/lavague-ai/LaVague
- https://github.com/lavague-ai/LaVague/blob/9024bb83/lavague-core/lavague/core/extractors.py
- https://github.com/lavague-ai/LaVague/issues/650
- https://www.vulncheck.com/advisories/lavague-0.2.35-remote-code-execution-via-eval-extraction

### [CVE-2026-85689](https://github.com/llmware-ai/llmware)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-85689
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-09-05 00:17:46 JST
- 更新日: 2026-09-05 00:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: llmware 0.4.6のデータベースレイヤーにおけるSQLインジェクションの脆弱性。
- 影響: フィルター値の検証不備により、本来アクセスできないデータの閲覧やSQL処理の操作が行われる可能性があります。
- 推奨対応: 修正済みバージョンへのアップデートおよび入力値のサニタイズ処理を確認してください。

#### References
- https://github.com/llmware-ai/llmware
- https://github.com/llmware-ai/llmware/blob/v0.4.6/llmware/resources.py
- https://github.com/llmware-ai/llmware/issues/1304
- https://www.vulncheck.com/advisories/llmware-0.4.6-sql-injection-via-unescaped-filter-values

### [CVE-2026-19274](https://www.ibm.com/support/pages/node/7286070)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-19274
- 関連キーワード: kubernetes
- 影響製品: -
- 公開日: 2026-09-05 01:17:21 JST
- 更新日: 2026-09-05 03:17:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Instana Agent OperatorにおけるマルチテナントのRBAC識別不備。
- 影響: Kubernetes上の別テナントによりクラスタースコープのRBAC権限が上書き・削除され、監視機能が停止させられる可能性があります。
- 推奨対応: IBMが提供する修正ビルドへ更新してください。

#### References
- https://www.ibm.com/support/pages/node/7286070

### [CVE-2026-6958](https://olografix.org/acme/_poc/CVE-2026-6958.pdf)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-6958
- 関連キーワード: gin, openssl
- 影響製品: -
- 公開日: 2026-09-05 00:17:35 JST
- 更新日: 2026-09-05 01:17:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Windows版Acunetixにおける未存在ディレクトリパスの検索に起因するローカル権限昇格の脆弱性。
- 影響: 低権限の攻撃者が悪意あるファイルを配置することで、SYSTEM権限で任意のコードを実行する可能性があります。
- 推奨対応: Acunetixを最新バージョンへアップデートしてください。

#### References
- https://olografix.org/acme/_poc/CVE-2026-6958.pdf
- https://seclists.org/fulldisclosure/2026/Sep/0
- https://www.acunetix.com/
- https://www.vulncheck.com/advisories/acunetix-local-privilege-escalation-via-wvsc-exe
- http://seclists.org/fulldisclosure/2026/Sep/0

### [CVE-2026-85618](https://github.com/C4illin/ConvertX)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-85618
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-05 00:17:41 JST
- 更新日: 2026-09-05 00:17:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ConvertX 0.17.0のxelatexコンバーターにおける任意ファイル読み取りの脆弱性。
- 影響: 認証されたユーザーが意図的に作成したLaTeXファイルをアップロードすることで、サーバー上のファイルを外部へ閲覧・取得する可能性があります。
- 推奨対応: ソフトウェアの更新や、LaTeXコンパイル環境の実行制限・サンドボックス化を検討してください。

#### References
- https://github.com/C4illin/ConvertX
- https://github.com/C4illin/ConvertX/blob/v0.18.0/src/converters/xelatex.ts
- https://github.com/C4illin/ConvertX/issues/573
- https://www.vulncheck.com/advisories/convertx-0.17.0-arbitrary-file-read-via-latex-input-directives

### [CVE-2026-85670](https://github.com/huggingface/tokenizers)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-85670
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-05 00:17:44 JST
- 更新日: 2026-09-05 03:18:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Hugging Face tokenizersにおける境界外アクセスおよびプロセス停止（DoS）の脆弱性。
- 影響: 不正なtokenizer.jsonを読み込ませることで、バッファオーバーランやクラッシュを引き起こし、サービス拒否（DoS）が発生する可能性があります。
- 推奨対応: tokenizersライブラリを修正済みバージョンへ更新してください。

#### References
- https://github.com/huggingface/tokenizers
- https://github.com/huggingface/tokenizers/blob/v0.23.2/tokenizers/src/models/bpe/model.rs
- https://github.com/huggingface/tokenizers/issues/2094
- https://www.vulncheck.com/advisories/tokenizers-bpebuilder-buffer-overflow-via-merge-token
- https://github.com/huggingface/tokenizers/issues/2094

### [CVE-2026-85693](https://github.com/mckaywrigley/chatbot-ui)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-85693
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-05 00:17:47 JST
- 更新日: 2026-09-05 00:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Chatbot UIの検索エンドポイントにおけるアクセスコントロールバイパスの脆弱性。
- 影響: 所有権検証の欠如により、認証された攻撃者が他ユーザーの非公開ファイル内容を取得する可能性があります。
- 推奨対応: 適切なアクセス制御と所有権チェックを行う修正パッチを適用してください。

#### References
- https://github.com/mckaywrigley/chatbot-ui
- https://github.com/mckaywrigley/chatbot-ui/blob/81328b61d2a4ab597a7a057be70e785cf756d9f8/app/api/retrieval/retrieve/route.ts
- https://github.com/mckaywrigley/chatbot-ui/issues/2028
- https://www.vulncheck.com/advisories/chatbot-ui-cross-user-private-file-content-disclosure-via-retrieval-api

### [CVE-2026-85697](https://github.com/documenso/documenso)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-85697
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-05 00:17:48 JST
- 更新日: 2026-09-05 03:18:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Documenso 2.17.0のPDF配信機能におけるアクセス制御不備の脆弱性。
- 影響: 制限されたドキュメントの識別子を利用され、低権限ユーザーに他者の文書を閲覧される可能性があります。
- 推奨対応: Documensoを修正済みバージョンへアップデートしてください。

#### References
- https://github.com/documenso/documenso
- https://github.com/documenso/documenso/blob/v2.17.0/apps/remix/server/api/files/files.helpers.ts
- https://github.com/documenso/documenso/issues/3112
- https://www.vulncheck.com/advisories/documenso-2.17.0-pdf-route-ignores-document-visibility
- https://github.com/documenso/documenso/issues/3112

### [CVE-2026-80780](https://git.kernel.org/stable/c/2e0471bf3ab2a6b7eedcc3b8a2a17286b6a9ae1a)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80780
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-05 01:18:03 JST
- 更新日: 2026-09-05 01:18:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのHID pidffドライバーにおける境界外書き込みの脆弱性。
- 影響: 入力デバイス初期化時の条件によって型混同が発生し、ヒープメモリが破損する可能性があります。
- 推奨対応: カーネルを修正パッチが適用された最新バージョンに更新してください。

#### References
- https://git.kernel.org/stable/c/2e0471bf3ab2a6b7eedcc3b8a2a17286b6a9ae1a
- https://git.kernel.org/stable/c/4529c03c3da8f91392cd630453452f569973f4cd
- https://git.kernel.org/stable/c/67bb1074e3d2d12fa059a9cc707e89398a4e4704
- https://git.kernel.org/stable/c/86b63adfa5e132beac4be72668fdf9128fe51d2e
- https://git.kernel.org/stable/c/ad9330f7e74a97842815a291a0d7389ed2f34504

# Backend CVE Summary (2026-08-23)

## Overview

- 取得日時: 2026-08-23 07:34:00 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 30
- Critical: 1
- High: 1
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-74674](https://git.kernel.org/stable/c/0b8ff21cbda8808c86b18f1b0ca2d0025af9a80a)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74674
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-23 01:16:41 JST
- 更新日: 2026-08-23 01:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのダイレクトページテーブル回収処理（mm）において、`zap_pte_range`実行時にTLBフラッシュへ不適切なアドレスが渡される不具合。
- 影響: ページ構造キャッシュ等の不適切なTLBフラッシュが発生し、カーネルの安定性に影響を及ぼす可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/0b8ff21cbda8808c86b18f1b0ca2d0025af9a80a
- https://git.kernel.org/stable/c/478a1c3abebfc717db0d1281a9cdd7befafee542

### [CVE-2026-74702](https://git.kernel.org/stable/c/42bc45df5905e2b7dccb72adaf7730f66cfbe03f)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74702
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-23 01:16:44 JST
- 更新日: 2026-08-23 01:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのvhost-scsiにおいて、エンドポイント有効化後に機能ビット（T10-PI等）の変更を受け入れてしまう不具合。
- 影響: メモリ構造体が未割り当て（NULL）のままI/O処理が実行され、システムクラッシュを引き起こす可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/42bc45df5905e2b7dccb72adaf7730f66cfbe03f
- https://git.kernel.org/stable/c/9a3eb77a612f9d158e4d27df43677a014e9cfa55
- https://git.kernel.org/stable/c/a06e4611d45518896fbff4f45d9581578b107e91

### [CVE-2026-74700](https://git.kernel.org/stable/c/34e77d8e3570f9df3952496ddb402833695662fd)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74700
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:44 JST
- 更新日: 2026-08-23 01:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのネットワーク分類器API（net/sched: cls_api）における、ロック未保持のフィルタ処理に関する競合状態の不具合。
- 影響: 並行処理時に競合が発生し、メモリ不整合やシステムクラッシュを引き起こす可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/34e77d8e3570f9df3952496ddb402833695662fd
- https://git.kernel.org/stable/c/a347304b2ca1a5377d5bd2d8a72e4b4f12afe648
- https://git.kernel.org/stable/c/a81f9c44d87fb59d99fce72e29e02cab3a49a1c3
- https://git.kernel.org/stable/c/b648c8a56531aeabd1c14f6b5cf1891e269b3756
- https://git.kernel.org/stable/c/d6222af7274f08e7a1848131dc30319993d8f377

### [CVE-2026-62383](https://github.com/nltk/nltk/security/advisories/GHSA-3hhw-38pf-pxj6)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-62383
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 00:16:17 JST
- 更新日: 2026-08-23 00:16:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NLTK（バージョン3.10.2未満）の`IPIPANCorpusReader`メソッドにおける、パス検証（pathsec）を回避されるシンボリックリンク脆弱性。
- 影響: 攻撃者がコーパス内にシンボリックリンクを設置することで、実行プロセス権限でアクセス可能な任意のファイルを読み取られる可能性があります。
- 推奨対応: NLTKをバージョン3.10.2以降にアップデートしてください。

#### References
- https://github.com/nltk/nltk/security/advisories/GHSA-3hhw-38pf-pxj6
- https://www.vulncheck.com/advisories/nltk-ipipancorpusreader-symlink-arbitrary-file-read

### [CVE-2026-74591](https://git.kernel.org/stable/c/267ecd2eb7759c26f1a026eb0a5b231071534c9c)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74591
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-23 01:16:31 JST
- 更新日: 2026-08-23 01:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのファイルマップ処理（`__filemap_add_folio`）において、競合解決のリトライ時にインデックス位置が正しく復元されない不具合。
- 影響: データ構造（xarray）の不整合が発生し、システムの安定性に悪影響を与える可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/267ecd2eb7759c26f1a026eb0a5b231071534c9c
- https://git.kernel.org/stable/c/4917e3ebcab50f0265e8ca01c8567de4c4a47511
- https://git.kernel.org/stable/c/86da3f7e1e609e1e8bfbab198af68467c5a015a5

### [CVE-2026-74621](https://git.kernel.org/stable/c/439d3e404f9d5e515911cc8132cde198b337c19e)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74621
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-23 01:16:34 JST
- 更新日: 2026-08-23 01:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのパケット動作処理（act_ct）において、ヘッダー検証でパケットが拒否された際にソケットバッファ（`sk_buff`）が解放されない不具合。
- 影響: メモリリークが発生し、長期的なリソース枯渇やパフォーマンス低下を引き起こす可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/439d3e404f9d5e515911cc8132cde198b337c19e
- https://git.kernel.org/stable/c/47d99828591d0fe8be4b9c8992ff3b8e47968db9
- https://git.kernel.org/stable/c/737873a59905a54ca0d2d127ef882f3f88bf4379
- https://git.kernel.org/stable/c/8a7ed561671aa6a911a2de99e59ef670a4d0b1df
- https://git.kernel.org/stable/c/b47bb899e04b5407c5a63fe88d4b6676586a6e84

### [CVE-2026-74641](https://git.kernel.org/stable/c/10a87401fb3148c388e55df0148295b3b137da07)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74641
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-23 01:16:37 JST
- 更新日: 2026-08-23 01:16:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのALSA usx2yドライバにおける、`mmap`フォルト処理時のオフセット境界チェック不足の不具合。
- 影響: 呼び出し元のプロセスが対象領域外のカーネルメモリに対して読み書きアクセスを獲得してしまう可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/10a87401fb3148c388e55df0148295b3b137da07
- https://git.kernel.org/stable/c/2ca1eea3cd17930daffe9e429a7c89232036ec24
- https://git.kernel.org/stable/c/34ab56ed854baa73a731cfd99af689f0b1bac444
- https://git.kernel.org/stable/c/4208db2453e1ea71b8048a5b7802360cb29a53f1
- https://git.kernel.org/stable/c/5bf5ccddf00b59f1e3ea7e65d76a5f5b5c21cc2e

### [CVE-2026-74643](https://git.kernel.org/stable/c/684f271210becd7b8c4088f06c442499e48a43a0)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74643
- 関連キーワード: go, echo
- 影響製品: -
- 公開日: 2026-08-23 01:16:37 JST
- 更新日: 2026-08-23 01:16:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのDAMONサンプルモジュール（DAMON_SAMPLE_MTIER）において、パラメータに0が設定された際にゼロ除算が発生する不具合。
- 影響: ゼロ除算が発生し、カーネルの例外エラーやシステム停止を引き起こす可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/684f271210becd7b8c4088f06c442499e48a43a0
- https://git.kernel.org/stable/c/a16fd3ad9d89b05475864da97327870464611736
- https://git.kernel.org/stable/c/e16b8d640ec99b28bc827560edcf9706e610c3aa

### [CVE-2026-74645](https://git.kernel.org/stable/c/06befa61c427e74319781e6f35a364cfc32dbae8)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74645
- 関連キーワード: go, echo
- 影響製品: -
- 公開日: 2026-08-23 01:16:37 JST
- 更新日: 2026-08-23 01:16:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのDAMON LRU SORTモジュールにおいて、`active_mem_bp`パラメータに10000を超える値を渡すとゼロ除算が発生する不具合。
- 影響: ゼロ除算例外が発生し、カーネルエラーやシステムクラッシュを引き起こす可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/06befa61c427e74319781e6f35a364cfc32dbae8
- https://git.kernel.org/stable/c/e7e5e5e0dfe2ea171044c24c263efae4ee882b3f

### [CVE-2026-74655](https://git.kernel.org/stable/c/1c31e2377f4c1bb110ca7f6e597b2253a7440c37)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74655
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-23 01:16:39 JST
- 更新日: 2026-08-23 01:16:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのQualcomm GENIシリアルドライバ（qcom-geni）において、送信DMA処理中のバッファフラッシュが正しく処理されない不具合。
- 影響: 送信データフレームの破損や無限ループが発生し、シリアル通信機能が正常に動作しなくなる可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/1c31e2377f4c1bb110ca7f6e597b2253a7440c37
- https://git.kernel.org/stable/c/313ae287442e5e8d3f7b53b73f37d384bda072d0
- https://git.kernel.org/stable/c/b1801c0d40f62778b613334de5840aba10a564d5
- https://git.kernel.org/stable/c/e3c04834ae1ab5e9cfbe8ac54ec734aa4774249d

### [CVE-2026-74672](https://git.kernel.org/stable/c/26444eb71465c9934d9d418ef69c43f61185329b)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74672
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-23 01:16:41 JST
- 更新日: 2026-08-23 01:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのmm/vmallocにおいて、ptdump処理とvmapページテーブル解放処理の間に競合状態が存在し、Use-After-Free（UAF）が発生する脆弱性。
- 影響: システムの不安定化やカーネルクラッシュ（DoS）、または権限昇格につながる可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/26444eb71465c9934d9d418ef69c43f61185329b
- https://git.kernel.org/stable/c/3cc26c8907db0f5d1ff8043b5851ee572e9b3c98
- https://git.kernel.org/stable/c/c5bf8cd148cfea948cfa3db71da427294b20db0f

### [CVE-2026-74691](https://git.kernel.org/stable/c/0da9a6d27155ad072dd76db8cd637feead99a0e0)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74691
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-23 01:16:43 JST
- 更新日: 2026-08-23 01:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Thunderboltネットワークドライバ（tbnet）において、リング停止時の解体シーケンス順序の不備により処理中フレームが適切に処理されない脆弱性。
- 影響: 通信障害やメモリ異常、システムクラッシュを引き起こす可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/0da9a6d27155ad072dd76db8cd637feead99a0e0
- https://git.kernel.org/stable/c/103a9b663ac1cacb8465aeff18f84a247154a562
- https://git.kernel.org/stable/c/4dd71cb0d23d40cb58fe4261c7bd183dca66caa0
- https://git.kernel.org/stable/c/68bf02b6b4ad3f748c6db71fd77b6c0402d252f4
- https://git.kernel.org/stable/c/7cce39109206bc5497e0953806563644b88bfc44

### [CVE-2026-74584](https://git.kernel.org/stable/c/53c97e9882f4e747b4ac31b211317c2eba541af9)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74584
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 00:16:21 JST
- 更新日: 2026-08-23 00:16:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: bnxt_re RDMAドライバにおいて、ユーザー空間へマッピングされる共有ページが事前にゼロ初期化されず、直前まで使用されていたカーネルデータが露出する脆弱性。
- 影響: ローカル権限を持つ攻撃者によって、カーネルメモリの機密情報が閲覧される可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/53c97e9882f4e747b4ac31b211317c2eba541af9
- https://git.kernel.org/stable/c/9128c2411b83a64c0a69d2ff059c741bde25a9cc
- https://git.kernel.org/stable/c/9896bdfd21d918e9f26a52bc6109cc77970ee0b1
- https://git.kernel.org/stable/c/a3ed2daab02b2a706e882ad31b5c3c4f33cb5bb1
- https://git.kernel.org/stable/c/c19b360fa10c521c0b681875cdaa51545d45a491

### [CVE-2026-74590](https://git.kernel.org/stable/c/1344b632cb5043e32939a84568125719111c5af3)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74590
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:31 JST
- 更新日: 2026-08-23 01:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: fsverityのbpf_get_fsverity_digest()において、ダイジェストサイズが並行して改変された場合の考慮が不十分な脆弱性。
- 影響: 並行処理中にカーネルがクラッシュし、サービス拒否（DoS）が発生する可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/1344b632cb5043e32939a84568125719111c5af3
- https://git.kernel.org/stable/c/2a5cfcad1d56e26d645b7887b0ed24c371851525
- https://git.kernel.org/stable/c/3e8ec7c0387273329374f5c7bd61f5f38af71fe1
- https://git.kernel.org/stable/c/5bd63cad9df4328a184c409fbdad4f17944bcdb8

### [CVE-2026-74609](https://git.kernel.org/stable/c/2be741ad565c610871a6a95062c12c39da7168fd)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74609
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:33 JST
- 更新日: 2026-08-23 01:16:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TIPCサブシステムのtipc_node_link_down()において、ロック保護外でリンクポインタを参照しているため競合時にUse-After-Free（UAF）が発生する脆弱性。
- 影響: カーネルクラッシュ（DoS）や意図しないメモリ破壊を引き起こす可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/2be741ad565c610871a6a95062c12c39da7168fd
- https://git.kernel.org/stable/c/47ba70891b10b2feb52462086b7fcd2ad75d3ce3
- https://git.kernel.org/stable/c/5558a8312452ddb21eff22b1cbd84302ad951944
- https://git.kernel.org/stable/c/69d209461c110388710e483a130caf051e4fd09a
- https://git.kernel.org/stable/c/a714d62513befef37f71f4ae89bb1fe173b65f2e

### [CVE-2026-74620](https://git.kernel.org/stable/c/2e8df8c9190335475a3b64a159d3efd8cdd1cb73)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74620
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:34 JST
- 更新日: 2026-08-23 01:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ネットワークスケジューラのアクション（act_gact, act_police）において、フォールバック制御アクションの範囲チェック不備により非想定の内部判定値（TC_ACT_CONSUMED等）が設定可能な脆弱性。
- 影響: ソケットバッファ（skb）の解放漏れによるメモリリークや、ネットワーク処理の異常を引き起こす可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/2e8df8c9190335475a3b64a159d3efd8cdd1cb73
- https://git.kernel.org/stable/c/5344e01179baa37547ab29fd7b8614f83faa190c
- https://git.kernel.org/stable/c/6bcb8839aa2d686964a4154650afc4db91e1c514
- https://git.kernel.org/stable/c/725efc2ab4a40affc4e285a2dc4896d103948a6c
- https://git.kernel.org/stable/c/883b56ae58fe657d8497806c7059646e9ba6dbd0

### [CVE-2026-74622](https://git.kernel.org/stable/c/17c99dd86f169c7a3e73d6778e79ef5b1ed3ceac)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74622
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:35 JST
- 更新日: 2026-08-23 01:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: atlanticネットワークドライバにおいて、インタフェース停止時に消費済みかつ未再充填の受信用バッファ（RXページおよびDMAマッピング）が解放されない脆弱性。
- 影響: インタフェースの停止・再起動を繰り返すことでメモリリーク（DoS）が発生する可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/17c99dd86f169c7a3e73d6778e79ef5b1ed3ceac
- https://git.kernel.org/stable/c/1e58b0bab40dcbdfc04acaba6a221d40801c3770
- https://git.kernel.org/stable/c/24d87dc28ddd3771dd0e88719209811809729439
- https://git.kernel.org/stable/c/30c473ea097ef0c93b064281b3e295c97d17e28b
- https://git.kernel.org/stable/c/64e1346bc66b947eb80b848e4c8d9828ba50e0fe

### [CVE-2026-74623](https://git.kernel.org/stable/c/307d80193b4a4a75b8dc4e0d3162be3755abbed7)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74623
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:35 JST
- 更新日: 2026-08-23 01:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: atlanticネットワークドライバにおいて、送信リング解放時に未クリーンアップの送信バッファ（TX/XDP_TX）が残留し参照が喪失する脆弱性。
- 影響: 高負荷時のインタフェースダウンに伴いメモリリークが発生し、リソースが枯渇する可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/307d80193b4a4a75b8dc4e0d3162be3755abbed7
- https://git.kernel.org/stable/c/3447641d361dcc5511841d986ad4d849b2900d9b
- https://git.kernel.org/stable/c/452636ea5410a96e02ebaaf80b21e3620b98e0dd
- https://git.kernel.org/stable/c/7a3e1481f4ee6c581bccc6bfc6c970aac5be7b0c
- https://git.kernel.org/stable/c/b13202d401e1a20fec89b0cda733dcbaf279f79d

### [CVE-2026-74629](https://git.kernel.org/stable/c/7a1df20a8d2cc89e3a442b6e0b43b1cacde8d403)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74629
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:35 JST
- 更新日: 2026-08-23 01:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DIBSドライバにおいて、dmb_clientid_arrの解放タイミング不備によりUse-After-Free（UAF）や二重解放（Double Free）が発生する脆弱性。
- 影響: カーネルクラッシュ（DoS）やメモリ破壊を引き起こす可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/7a1df20a8d2cc89e3a442b6e0b43b1cacde8d403
- https://git.kernel.org/stable/c/9e6869be49064915edb6c8776b27c376cfdb0df5
- https://git.kernel.org/stable/c/ece6426b61241e9bfb41aa131f235168f55229b1

### [CVE-2026-74644](https://git.kernel.org/stable/c/460181e4bb47a57776c64f0832c2096de8878cb3)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74644
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:37 JST
- 更新日: 2026-08-23 01:16:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DAMON（Data Access Monitor）サブシステムにおいて、無効な移動先ノードIDが渡された際にページ（folio）がLRUリストに戻されず孤立する脆弱性。
- 影響: メモリページが不必要に固定され、リソース漏洩やメモリ管理の不整合が発生する可能性があります。
- 推奨対応: 修正パッチが適用されたカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/460181e4bb47a57776c64f0832c2096de8878cb3
- https://git.kernel.org/stable/c/5deb65c34e682e7c5f5df417a70e223e8fcc5f5a
- https://git.kernel.org/stable/c/cfef454862b7d2776e0955b873dd59af6b47cfcb

### [CVE-2026-74647](https://git.kernel.org/stable/c/0beaa9bd7eb10d9b5e6352ed5161f3f3bbd4c3c5)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74647
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:38 JST
- 更新日: 2026-08-23 01:16:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのfastrpcドライバーにおいて、マルチスレッド環境でのアンマップ処理時に競合状態（レースコンディション）が発生する問題。
- 影響: 同時実行によってメモリ管理上の競合が生じ、システムの不安定化や予期せぬ不具合を引き起こす可能性がある。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/0beaa9bd7eb10d9b5e6352ed5161f3f3bbd4c3c5
- https://git.kernel.org/stable/c/6102ceb4eab845743ee57acd3863fbd06e93c927
- https://git.kernel.org/stable/c/97273624f7b356eaf8261609a75cfcb8738a165a
- https://git.kernel.org/stable/c/9bf22a7d950cec2d1efeca7f16bb20fcca84c36a
- https://git.kernel.org/stable/c/fe70329055977fc1e8dc6291318d0dd75470795a

### [CVE-2026-74659](https://git.kernel.org/stable/c/014c062d23c63ec77ef2cf17a0d9363c7441cc94)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74659
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:39 JST
- 更新日: 2026-08-23 01:16:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのブリッジMRP（Media Redundancy Protocol）において、送信フレームの構築時に未初期化パディングや未設定フィールドが残る問題。
- 影響: 送信されるフレーム内に未初期化メモリのデータ（3バイト）が含まれ、カーネルのメモリ情報が漏洩する可能性がある。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/014c062d23c63ec77ef2cf17a0d9363c7441cc94
- https://git.kernel.org/stable/c/06d58b8d2f053ced82e01efaeb6e7c82891eed58
- https://git.kernel.org/stable/c/5912cf1822fbe53ae275c147868740eb384a5d3e
- https://git.kernel.org/stable/c/63488dba65ef91373ef616575b32eb0eb21459f4
- https://git.kernel.org/stable/c/7ebc23ff03668042e0b0e4034bb1518d36198d9e

### [CVE-2026-74671](https://git.kernel.org/stable/c/27f3924061592d0ef6b04e16f48754b6cb6adf27)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74671
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:41 JST
- 更新日: 2026-08-23 01:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのIMA（Integrity Measurement Architecture）の `xattr_verify()` において、型変換の問題から計算結果がアンダーフローし、領域外読み取り（Out-of-bounds read）が発生する問題。
- 影響: 不正な拡張属性処理により領域外メモリの読み取りが発生し、システムがクラッシュまたはメモリ情報が漏洩する可能性がある。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/27f3924061592d0ef6b04e16f48754b6cb6adf27
- https://git.kernel.org/stable/c/5ff232d31106f45ac87c3b64e1d35a0667777797
- https://git.kernel.org/stable/c/7e515b6c9aab452a4f0734bd7208e4e780e164ca
- https://git.kernel.org/stable/c/a784b4732ac7e51862b9b210c2d8b2ab9e83568c
- https://git.kernel.org/stable/c/b6cb134707a2127d90a58d69dd818679cae8033c

### [CVE-2026-74690](https://git.kernel.org/stable/c/774394d27930ec4cf4cb3eed8ab6a4d20cb2430a)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74690
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:43 JST
- 更新日: 2026-08-23 01:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのs390/ISMデバイスドライバにおいて、デバイス終了処理（`ism_dev_exit()`）と割り込みハンドラが並行実行された際に、解放済みデータ構造へアクセスするUse-After-Freeが発生する問題。
- 影響: メモリ破損によるシステムのクラッシュや予期せぬ不具合が発生する可能性がある。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/774394d27930ec4cf4cb3eed8ab6a4d20cb2430a
- https://git.kernel.org/stable/c/b1896543ce59c4258625a35cf41e23a9a1f80ea2
- https://git.kernel.org/stable/c/fc3021284050ecb3bba8a7851340cedcb5037928

### [CVE-2026-74703](https://git.kernel.org/stable/c/2417a498cf3fe64d06faf87e236eda98dd4f04e0)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74703
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:44 JST
- 更新日: 2026-08-23 01:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのvhost-scsiにおいて、T10 PI使用時の不正なリクエストでデータ長計算が不正になり、ゼロ件のSGL処理によりBUG_ONが誘発される問題。
- 影響: 不正なリクエストによってカーネルパニックが引き起こされ、サービス拒否（DoS）状態に陥る可能性がある。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/2417a498cf3fe64d06faf87e236eda98dd4f04e0
- https://git.kernel.org/stable/c/d876c493fc4b811941bfeb4c80beb2dfc4bf025e
- https://git.kernel.org/stable/c/f8fe3f8d342da750dd10361bf66009fd3072926b

### [CVE-2026-74723](https://git.kernel.org/stable/c/0fa78ef637deb5dbe341582f88553a4bce496de0)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74723
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:47 JST
- 更新日: 2026-08-23 01:16:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのBtrfsファイルシステムにおいて、不正なLZO圧縮インラインエクステントを読み込む際にスラブ領域での境界外読み取り（slab-out-of-bounds read）が発生する問題。
- 影響: 悪意を持って作成されたイメージのマウント・読み込み時にシステムのクラッシュ（DoS）や情報漏洩が発生する可能性がある。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/0fa78ef637deb5dbe341582f88553a4bce496de0
- https://git.kernel.org/stable/c/fc50b475ad27f50b4dcc98fc4c44e8802bc1b248

### [CVE-2026-74727](https://git.kernel.org/stable/c/33ec10567fe14456063daf549fdf1a4f53448e4c)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74727
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-23 01:16:47 JST
- 更新日: 2026-08-23 01:16:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのovpn（OpenVPN）モジュールにおいて、ピアの削除と更新・再ハッシュ処理の間に競合状態が発生し、削除済みピアが再度テーブルに追加される問題。
- 影響: 不整合な状態が生じ、メモリ管理の異常やシステムの不安定化につながる可能性がある。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/33ec10567fe14456063daf549fdf1a4f53448e4c
- https://git.kernel.org/stable/c/66745480298775f188b2f5ad266643e85a90f73b
- https://git.kernel.org/stable/c/d20c181088984b6eaa8d7fe7cb5ab3510988df59

### [CVE-2026-66393](https://github.com/nltk/nltk/security/advisories/GHSA-rf74-v2fm-23pw)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-66393
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-23 00:16:19 JST
- 更新日: 2026-08-23 00:16:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NLTK（バージョン3.9.4未満）の `JSONTaggedDecoder.decode_obj()` において、再帰処理の制限が設けられていない問題。
- 影響: 深くネストされた不正なJSON構造を解析させることで `RecursionError` が発生し、Pythonプロセスがクラッシュしてサービス拒否（DoS）を引き起こす可能性がある。
- 推奨対応: NLTKをバージョン3.9.4以降へアップデートしてください。

#### References
- https://github.com/nltk/nltk/security/advisories/GHSA-rf74-v2fm-23pw
- https://www.vulncheck.com/advisories/nltk-before-denial-of-service-via-jsontaggeddecoder

### [CVE-2026-74586](https://git.kernel.org/stable/c/163847552a571bd55094291f4ffcdc1de0f14a7b)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74586
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-23 01:16:30 JST
- 更新日: 2026-08-23 01:16:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのSCTP実装において、ASCONFパラメータ処理時にピアが削除されても `asoc->new_transport` ポインタが消去されない問題。
- 影響: 削除済みトランスポートへのダングリングポインタが参照され、システムクラッシュや不安定化の原因となる可能性がある。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/163847552a571bd55094291f4ffcdc1de0f14a7b
- https://git.kernel.org/stable/c/291accf36febce751021888de5f15090f4875b56
- https://git.kernel.org/stable/c/31efa656cf6aface26e88f038c14f22ee6ca1500
- https://git.kernel.org/stable/c/3b539b317cd052236fed0350364ff1268996ba46
- https://git.kernel.org/stable/c/beb33f8ee1ca83acddb2a5ae80f3d22ec550b4c3

### [CVE-2026-4703](https://plugins.trac.wordpress.org/browser/ws-form/trunk/includes/class-ws-form-common.php#L7154)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-4703
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-23 01:16:29 JST
- 更新日: 2026-08-23 01:16:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用プラグイン「WS Form LITE」（1.10.80以下の全バージョン）において、フォーム送信メタデータの反シリアル化に起因するPHPオブジェクトインジェクションの脆弱性。
- 影響: サイト内に攻撃に利用可能なPOPチェーンを持つ他のプラグインやテーマが存在する場合、認証なしの遠隔攻撃者により任意ファイル削除やデータ取得、コード実行が行われる可能性がある。
- 推奨対応: プラグインを最新バージョンに更新してください。

#### References
- https://plugins.trac.wordpress.org/browser/ws-form/trunk/includes/class-ws-form-common.php#L7154
- https://plugins.trac.wordpress.org/browser/ws-form/trunk/includes/core/class-ws-form-submit.php#L1061
- https://plugins.trac.wordpress.org/changeset/3489609/
- https://www.wordfence.com/threat-intel/vulnerabilities/id/df36eae9-6f2b-432c-a765-57450939b344?source=cve

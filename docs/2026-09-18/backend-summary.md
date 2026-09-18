# Backend CVE Summary (2026-09-18)

## Overview

- 取得日時: 2026-09-18 09:10:12 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 22
- Critical: 2
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-85719](https://github.com/AsyncHttpClient/async-http-client/commit/4d887704dec22027310f66c81503226722e9bd23)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-85719
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-18 01:18:16 JST
- 更新日: 2026-09-18 01:18:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process HTTP responses. From 2.1.0 until 2.16.1 and 3.0.12, requests using an authenticated SOCKS proxy can expose the proxy's credentials to the origin because NettyRequestFactory and NettyRequestSender attach...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/AsyncHttpClient/async-http-client/commit/4d887704dec22027310f66c81503226722e9bd23
- https://github.com/AsyncHttpClient/async-http-client/commit/718ed2e86126663a88ea3db7a88cbbf93f0069b5
- https://github.com/AsyncHttpClient/async-http-client/commit/abaa8bd260beda3b85825ff95069ed11eaf4ca8d
- https://github.com/AsyncHttpClient/async-http-client/commit/be439b2ec773d12d61914c238d3e8eeaa6f0ba21
- https://github.com/AsyncHttpClient/async-http-client/security/advisories/GHSA-x5w6-vm3f-pp6f

### [CVE-2026-85717](https://github.com/AsyncHttpClient/async-http-client/commit/43db7bba81430cbd61ec2dc2c7be464e0ff6a0ff)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-85717
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-18 01:18:15 JST
- 更新日: 2026-09-18 01:18:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process HTTP responses. From 2.14.5 to 2.16.0 and from 3.0.9 to 3.0.11, a client configured with a client-wide Realm and redirect following can disclose credentials after a cross-origin redirect because the Int...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/AsyncHttpClient/async-http-client/commit/43db7bba81430cbd61ec2dc2c7be464e0ff6a0ff
- https://github.com/AsyncHttpClient/async-http-client/commit/b66757bec34def2e9867bb2b77bd848b1112abb4
- https://github.com/AsyncHttpClient/async-http-client/pull/2224
- https://github.com/AsyncHttpClient/async-http-client/security/advisories/GHSA-f8m2-889x-vw4x

### [CVE-2026-90076](https://git.kernel.org/stable/c/709f34f7c28dc4dd6c40343d101850f11e172312)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90076
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-18 02:16:56 JST
- 更新日: 2026-09-18 02:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: net/sched: fq: add overflow bounds to quantum and initial quantum fq_init() computes quantum = 2 * psched_mtu() and initial_quantum = 10 * psched_mtu() with no overflow check. A device with a huge MTU (e.g. dummy with max_mtu == 0 accepting MTU 2147483...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/709f34f7c28dc4dd6c40343d101850f11e172312
- https://git.kernel.org/stable/c/d16dac3925be95ad46e986d4b139c9898b6e227f
- https://git.kernel.org/stable/c/e35acd56f244d94355f9ab237c2ecc8fba5e6f04
- https://git.kernel.org/stable/c/f6b3e3848a5fca63438984acd6d9eceac80814c1

### [CVE-2026-85720](https://github.com/AsyncHttpClient/async-http-client/commit/9dba5ac988b7e750551f59b2eab550b60ac8a0d6)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-85720
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-18 02:16:51 JST
- 更新日: 2026-09-18 02:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The AsyncHttpClient (AHC) library allows Java applications to easily execute HTTP requests and asynchronously process HTTP responses. From 2.0.0 until 2.16.1 and 3.0.12, a request using an HTTP proxy to reach an HTTPS origin can expose preemptive origin credentials because NettyRequestFactory and NettyRequestSender.sen...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/AsyncHttpClient/async-http-client/commit/9dba5ac988b7e750551f59b2eab550b60ac8a0d6
- https://github.com/AsyncHttpClient/async-http-client/commit/d07dbc79f5cf378f63c246f6101d7579ace55acc
- https://github.com/AsyncHttpClient/async-http-client/pull/2234
- https://github.com/AsyncHttpClient/async-http-client/security/advisories/GHSA-xr57-gcx8-52hf

### [CVE-2026-90055](https://git.kernel.org/stable/c/1e964d414bfd9f8dfe9948d08e4b9dda4ed2e422)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90055
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-18 02:16:54 JST
- 更新日: 2026-09-18 02:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: usb: atm: usbatm: fix invalid ci_range initialization syzbot reported a shift-out-of-bounds in __vcc_connect(): UBSAN: shift-out-of-bounds in net/atm/common.c:382:32 shift exponent -1 is negative CPU: 0 UID: 0 PID: 5987 Comm: syz.0.18 Not tainted syzka...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/1e964d414bfd9f8dfe9948d08e4b9dda4ed2e422
- https://git.kernel.org/stable/c/561cbd6d49022c9a383e22a39c87a165a4d39f9c
- https://git.kernel.org/stable/c/75667703115154a4fd9cf259d4f826d8729cbcda
- https://git.kernel.org/stable/c/76bc7c3a44856744b64aa91d9afe6d9522a78c42
- https://git.kernel.org/stable/c/7baa0c92be39eb3da755ed6f200497a57078c47b

### [CVE-2026-90154](https://git.kernel.org/stable/c/0875872718b98e8530fbc634e5aa7dbd3253b80d)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90154
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-18 02:17:08 JST
- 更新日: 2026-09-18 02:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: ksmbd: scope session state changes to bound connections ksmbd_all_conn_set_status() treats every connection whose transient binding flag is set as belonging to the target SessionId. A logoff or session replacement can consequently move an unrelated con...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/0875872718b98e8530fbc634e5aa7dbd3253b80d
- https://git.kernel.org/stable/c/c50e628122aed077695669e25b842e778511a43d

### [CVE-2026-90068](https://git.kernel.org/stable/c/10a36512c21f861a03fba461a7ead09023df9c1b)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90068
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-18 02:16:55 JST
- 更新日: 2026-09-18 02:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: ASoC: dapm: Fix off-by-one check on the second enum channel The snd_soc_dapm_put_enum_double() rejects item[0] once it reaches e->items, but it lets item[1] be equal to it. Both go on to snd_soc_enum_item_to_val(), which indexes e->values with no bound...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/10a36512c21f861a03fba461a7ead09023df9c1b
- https://git.kernel.org/stable/c/14511c9b54ceeeef487409d73947c89ee8563590
- https://git.kernel.org/stable/c/32fc048391112559c34cb88d13594546939a4cd6
- https://git.kernel.org/stable/c/496081b4edc1f6e662418831c5b14cddd8d7920c
- https://git.kernel.org/stable/c/55126ef66298e43c69f192acebae8c7cc0022cf6

### [CVE-2026-90087](https://git.kernel.org/stable/c/2eafcf310f4e0ad4f387881db01116bbe3cc0b39)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90087
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-18 02:16:59 JST
- 更新日: 2026-09-18 02:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: Bluetooth: do not leak an hci_conn when a second LE connect is rejected create_le_conn_complete() decides whether the failed connection is still pending by comparing it against hci_lookup_le_connect(), which returns the first LE connection in BT_CONNEC...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/2eafcf310f4e0ad4f387881db01116bbe3cc0b39
- https://git.kernel.org/stable/c/7e1e4047200fd7519f9bdfe8a001437715e618b4

### [CVE-2026-90088](https://git.kernel.org/stable/c/3988cbb1be501dbff909a2ee024670e3c955a66d)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90088
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-18 02:16:59 JST
- 更新日: 2026-09-18 02:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: Bluetooth: RFCOMM: Validate MTU in rfcomm_apply_pn() to prevent infinite loop rfcomm_apply_pn() accepts the MTU value from a remote PN (Parameter Negotiation) frame without checking for zero. When the remote peer sends an MTU of zero, d->mtu is set to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/3988cbb1be501dbff909a2ee024670e3c955a66d
- https://git.kernel.org/stable/c/44c98fd082eafd49d55a8a4077ff488175b2fe24
- https://git.kernel.org/stable/c/9b2e5f1928c99224345a9ed8c5dae5fc74964d6d
- https://git.kernel.org/stable/c/aeee917a4878af95f0c63e18c5f22eaf6299c7b8
- https://git.kernel.org/stable/c/cbc2962da99b6b89345267d3aa74b4b573340548

### [CVE-2026-90095](https://git.kernel.org/stable/c/1f59015e958174e89be58cc8db16d70a60d17255)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90095
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-18 02:17:01 JST
- 更新日: 2026-09-18 02:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: fuse: Fix the condition to enable over-io-uring The existing condition in fuse_uring_cmd() is there only to avoid disabling io-uring for connections that already run with it, missing was a condition to refuse any IORING_OP_URING_CMD if the connection/c...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/1f59015e958174e89be58cc8db16d70a60d17255
- https://git.kernel.org/stable/c/8f9a725d89711ad027f6b7183586ef91528f106d

### [CVE-2026-90111](https://git.kernel.org/stable/c/235b42b5860189eb8c27c36435ad932cae65a734)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90111
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-18 02:17:03 JST
- 更新日: 2026-09-18 02:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: ip6mr: do not clone dst in ip6mr_cache_report() IPv6 input attaches a non-refcounted (NOREF) dst to skbs under RCU. When an ingress multicast packet misses MFC lookup, ip6mr_cache_unresolved() places the skb onto the unresolved queue, escaping the rece...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/235b42b5860189eb8c27c36435ad932cae65a734
- https://git.kernel.org/stable/c/4a674afaae4136c71943aa3e35d433676fd40e8f

### [CVE-2026-90125](https://git.kernel.org/stable/c/12092ed28434bf41e08d41e3c5269eb6b337fc02)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90125
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-18 02:17:04 JST
- 更新日: 2026-09-18 02:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: smb: client: fix request buffer leak in smb2_new_read_req() smb2_new_read_req() allocates the request buffer with smb2_plain_req_init() but only publishes it to the caller with *buf = req at the very end of the function. Two error returns sit in betwee...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/12092ed28434bf41e08d41e3c5269eb6b337fc02
- https://git.kernel.org/stable/c/442c5f1358ced0d4e716778ac06f1e323a7e4f21
- https://git.kernel.org/stable/c/58066940076b90c16e821fd6f9767cd979cbdb5e
- https://git.kernel.org/stable/c/73f6bdb0380486ab37fe12cd74de20abfaf5d3ae
- https://git.kernel.org/stable/c/deb6468f4164640e4dc875f008aa449cf55987a5

### [CVE-2026-90146](https://git.kernel.org/stable/c/03022dd874070768a7099f18b1944c633641315f)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90146
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-18 02:17:07 JST
- 更新日: 2026-09-18 02:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのXDP/BPF実装において、プログラムの各種チェックがBPF_LINK_UPDATE処理時にバイパスされる不備。
- 影響: 攻撃者やユーザーにより制限されたBPFプログラムがソフトウェアパス上に誤って適用され、システムが想定外の挙動を示す可能性がある。
- 推奨対応: 修正されたバージョンのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/03022dd874070768a7099f18b1944c633641315f
- https://git.kernel.org/stable/c/ad27ed7d2309419a129078d781504f486b1b469a
- https://git.kernel.org/stable/c/ea7b35dcc9430293b861bc7bad0c546f193c85f9

### [CVE-2026-90169](https://git.kernel.org/stable/c/06c7b1d731bc105a8644f1b70165ba8b9416cbab)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90169
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-18 02:17:10 JST
- 更新日: 2026-09-18 02:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのksmbd（SMB3サーバー）において、接続切断時に事前認証セッションオブジェクトが解放されないメモリリークの脆弱性。
- 影響: 接続の破棄に伴いメモリが枯渇し、サービス拒否（DoS）状態に陥る可能性がある。
- 推奨対応: 修正されたバージョンのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/06c7b1d731bc105a8644f1b70165ba8b9416cbab
- https://git.kernel.org/stable/c/8e2ebc77678832e981adc008d25cd8f67d08ebc4
- https://git.kernel.org/stable/c/a41a98ee16ae038751b6639decadaa3ce15ca18a
- https://git.kernel.org/stable/c/b62b1ebb25f0a19067ed5b1a86036b2dc98be44f
- https://git.kernel.org/stable/c/effcf48d79d8aa53113d8289e140746f25ceb62c

### [CVE-2026-85077](https://github.com/sanic-org/sanic/commit/47349d689d65fa1907977ac100e867894aeafb22)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-85077
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-18 00:16:54 JST
- 更新日: 2026-09-18 00:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SanicのHTTP/1.1レスポンス処理における改行文字（CR/LF）の検証不足によるヘッダーインジェクションの脆弱性。
- 影響: HTTPレスポンス分割、キャッシュポイズニング、セッション固定化、またはセキュリティヘッダーの無効化が行われる可能性がある。
- 推奨対応: Sanic 24.12.1 または 25.12.1 以降へアップデートしてください。

#### References
- https://github.com/sanic-org/sanic/commit/47349d689d65fa1907977ac100e867894aeafb22
- https://github.com/sanic-org/sanic/commit/9a95bb1c187558949606b915f5162c15f2db781b
- https://github.com/sanic-org/sanic/commit/a332796506c7c588b6930b02a8886e43eb8ea8d6
- https://github.com/sanic-org/sanic/pull/3164
- https://github.com/sanic-org/sanic/pull/3165

### [CVE-2026-85999](https://github.com/facelessuser/soupsieve/commit/cf198fcddc9230f06ed39f974eba0ce076b85cda)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-85999
- 関連キーワード: python, gin, express
- 影響製品: -
- 公開日: 2026-09-18 01:18:16 JST
- 更新日: 2026-09-18 01:18:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Soup SieveのCSSセレクター解析における、末尾空白およびコメント処理の正規表現による処理の非効率性。
- 影響: 攻撃者が制御するセレクターの解析時に過剰なCPUリソースが消費され、サービス拒否（DoS）が発生する可能性がある。
- 推奨対応: Soup Sieve 2.9 以降へアップデートしてください。

#### References
- https://github.com/facelessuser/soupsieve/commit/cf198fcddc9230f06ed39f974eba0ce076b85cda
- https://github.com/facelessuser/soupsieve/releases/tag/2.9
- https://github.com/facelessuser/soupsieve/security/advisories/GHSA-j934-xhv5-fg8f

### [CVE-2026-86000](https://github.com/facelessuser/soupsieve/commit/ce44e4996e6632871c18cdd7a7fb641be8ef34ef)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-86000
- 関連キーワード: python, gin, express
- 影響製品: -
- 公開日: 2026-09-18 01:18:16 JST
- 更新日: 2026-09-18 01:18:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Soup SieveのCSSセレクター解析における、識別子および属性値の正規表現パターンに関する破滅的バックトラッキングの脆弱性。
- 影響: 特定のセレクター解析時にCPU利用率が急増し、Python GILの占有やワーカーの枯渇によるサービス拒否（DoS）を引き起こす可能性がある。
- 推奨対応: Soup Sieve 2.9 以降へアップデートしてください。

#### References
- https://github.com/facelessuser/soupsieve/commit/ce44e4996e6632871c18cdd7a7fb641be8ef34ef
- https://github.com/facelessuser/soupsieve/releases/tag/2.9
- https://github.com/facelessuser/soupsieve/security/advisories/GHSA-gjv8-xp57-g29c
- https://github.com/facelessuser/soupsieve/security/advisories/GHSA-gjv8-xp57-g29c

### [CVE-2026-85078](https://github.com/sanic-org/sanic/commit/47349d689d65fa1907977ac100e867894aeafb22)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-85078
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-18 00:16:55 JST
- 更新日: 2026-09-18 05:18:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SanicのHTTP/1.1チャンクドボディ処理における、トレーラー部分の消費不備による脆弱性。
- 影響: リバースプロキシ等の後方に配置されている場合、HTTPリクエストスマグリングが引き起こされ、不正なリクエストが実行される可能性がある。
- 推奨対応: Sanic 25.12.1 以降へアップデートしてください。

#### References
- https://github.com/sanic-org/sanic/commit/47349d689d65fa1907977ac100e867894aeafb22
- https://github.com/sanic-org/sanic/commit/69a10d3b06babaa9e5f6d1af577364e9e53b6dea
- https://github.com/sanic-org/sanic/commit/a332796506c7c588b6930b02a8886e43eb8ea8d6
- https://github.com/sanic-org/sanic/pull/3164
- https://github.com/sanic-org/sanic/pull/3165

### [CVE-2026-61700](https://github.com/mariadb-corporation/mariadb-connector-j/commit/0205d8be947918566cd9ce5a9db149541bbc8dee)

> **Backend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-61700
- 関連キーワード: echo, mysql
- 影響製品: -
- 公開日: 2026-09-18 01:17:33 JST
- 更新日: 2026-09-18 01:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MariaDB Connector/Jにおける、`allowLocalInfile=false` 設定時でもサーバー主導の `LOCAL INFILE` パケットを強制処理してしまう脆弱性。
- 影響: 悪意あるサーバーまたは中間者攻撃により、アプリケーションが指定したローカルファイルの内容が外部に送信される可能性がある。
- 推奨対応: MariaDB Connector/J 2.7.14、3.3.5、3.4.3、または 3.5.9 以降へアップデートしてください。

#### References
- https://github.com/mariadb-corporation/mariadb-connector-j/commit/0205d8be947918566cd9ce5a9db149541bbc8dee
- https://github.com/mariadb-corporation/mariadb-connector-j/releases/tag/3.5.9
- https://github.com/mariadb-corporation/mariadb-connector-j/security/advisories/GHSA-wxmm-q36w-r9xj

### [CVE-2026-86863](https://github.com/pgadmin-org/pgadmin4/issues/10383)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-86863
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-18 01:18:17 JST
- 更新日: 2026-09-18 02:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pgAdmin 4のWebサーバー認証において、認証用ユーザー名をHTTPリクエストヘッダーからフォールバック取得してしまう不備。
- 影響: 未認証の第三者がHTTPヘッダーを偽造することで、任意のユーザー（管理者含む）として認証を回避して不当にログインできる可能性がある。
- 推奨対応: 修正されたバージョンのpgAdmin 4へアップデートしてください。

#### References
- https://github.com/pgadmin-org/pgadmin4/issues/10383

### [CVE-2026-76834](https://b2evolution.net/news/2022/03/26/2022-update-eol)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-76834
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-18 01:17:42 JST
- 更新日: 2026-09-18 01:17:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: b2evolution CMSにおけるシリアル化配列チェックのバイパス（CVE-2016-8901の不完全な修正）。
- 影響: 未認証の攻撃者が作成したシリアル化データを送信することで任意のPHPオブジェクトが生成され、条件次第でコード実行（RCE）につながる可能性がある。
- 推奨対応: 修正されたバージョンのb2evolution CMSへアップデートしてください。

#### References
- https://b2evolution.net/news/2022/03/26/2022-update-eol
- https://gist.github.com/axg11/3e29501c33f6e1e05ac2a00107afd64e
- https://github.com/b2evolution/b2evolution
- https://github.com/b2evolution/b2evolution/blob/7.2.5/htsrv/call_plugin.php#L49
- https://github.com/b2evolution/b2evolution/blob/7.2.5/inc/_core/_param.funcs.php#L2860

### [CVE-2026-86864](https://github.com/pgadmin-org/pgadmin4/issues/10384)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-86864
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-18 01:18:18 JST
- 更新日: 2026-09-18 02:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pgAdmin 4のバックアップツールにおける、`pg_dump` への引数渡し時のデータベース名パラメーター検証不足の脆弱性。
- 影響: コマンドラインオプションの注入により、指定ストレージ外の任意パスへファイルを作成・上書きされ、設定破損や権限昇格につながる可能性がある。
- 推奨対応: 修正されたバージョンのpgAdmin 4へアップデートしてください。

#### References
- https://github.com/pgadmin-org/pgadmin4/issues/10384

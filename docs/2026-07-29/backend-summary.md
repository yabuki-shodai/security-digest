# Backend CVE Summary (2026-07-29)

## Overview

- 取得日時: 2026-07-29 08:17:41 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 18
- Critical: 2
- High: 8
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-64863](https://github.com/goshs-labs/goshs/commit/0444ac6b1a8176ddae70d940adf7a26b2e5a6c29)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-64863
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 08:17:10 JST
- 更新日: 2026-07-29 08:17:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: goshs 2.1.4未満でWebDAV MOVEが--no-delete制御を回避し、ファイルの削除や上書きが可能。
- 影響: 不正なファイル操作によるデータ破壊や改ざんのリスク。
- 推奨対応: goshsを2.1.4以降に更新すること。

#### References
- https://github.com/goshs-labs/goshs/commit/0444ac6b1a8176ddae70d940adf7a26b2e5a6c29
- https://github.com/goshs-labs/goshs/releases/tag/v2.1.4
- https://github.com/goshs-labs/goshs/security/advisories/GHSA-hq33-8jgp-8qq3

### [CVE-2026-62325](https://github.com/goshs-labs/goshs/commit/32f4a0e1790a709f722d0f3b2341f139d003180a)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-62325
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 08:17:10 JST
- 更新日: 2026-07-29 08:17:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: goshs 2.1.3から2.1.4未満でSFTP認証ハンドラが未設定となり、認証なしでファイルアクセスが可能。
- 影響: 認証回避による不正ファイルアクセスのリスク。
- 推奨対応: goshsを2.1.4以降に更新すること。

#### References
- https://github.com/goshs-labs/goshs/commit/32f4a0e1790a709f722d0f3b2341f139d003180a
- https://github.com/goshs-labs/goshs/releases/tag/v2.1.4
- https://github.com/goshs-labs/goshs/security/advisories/GHSA-rjrw-mjq6-hpmm

### [CVE-2026-54650](https://github.com/bablilayoub/openhole/commit/a28c27adde2a7ed0c347b730c8707208c0f78ed3)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-54650
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-29 08:17:08 JST
- 更新日: 2026-07-29 08:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: openhole 0.1.1以前でパスのエンコード処理不備によりパス・トラバーサルが可能。
- 影響: トンネル経由でローカルサービスへの不正アクセスが発生する可能性。
- 推奨対応: openholeを0.1.2以降に更新すること。

#### References
- https://github.com/bablilayoub/openhole/commit/a28c27adde2a7ed0c347b730c8707208c0f78ed3
- https://github.com/bablilayoub/openhole/releases/tag/v0.1.2
- https://github.com/bablilayoub/openhole/security/advisories/GHSA-fh2f-xfxc-q9cc

### [CVE-2026-66750](https://github.com/theopaid/Insufficient-Access-Controls-Allow-for-Unauthorized-File-Downloads-Let-s-Chat-)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-66750
- 関連キーワード: go, gin, mongodb
- 影響製品: -
- 公開日: 2026-07-29 01:20:16 JST
- 更新日: 2026-07-29 03:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Rouille 0.3.3から3.6.2にHTTPリクエストスマグリング脆弱性が存在。
- 影響: 攻撃者がアクセス制御を回避し、任意のリクエストをバックエンドに送信可能。
- 推奨対応: Rouilleのアップデートや入力検証の強化を検討すること。

#### References
- https://github.com/theopaid/Insufficient-Access-Controls-Allow-for-Unauthorized-File-Downloads-Let-s-Chat-
- https://www.vulncheck.com/advisories/let-s-chat-broken-access-control-file-disclosure-via-get-files-route

### [CVE-2026-47725](https://github.com/forgekeep/nebula-mesh/releases/tag/v0.3.3)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-47725
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 04:17:34 JST
- 更新日: 2026-07-29 05:17:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: nebula-mesh 0.3.3未満でSameSite=LaxのセッションCookieが特定のCSRF攻撃を防げない。
- 影響: 第三者による不正な操作やログアウト強制のリスク。
- 推奨対応: nebula-meshを0.3.3以降に更新すること。

#### References
- https://github.com/forgekeep/nebula-mesh/releases/tag/v0.3.3
- https://github.com/forgekeep/nebula-mesh/security/advisories/GHSA-273q-qgh5-wrj6
- https://github.com/forgekeep/nebula-mesh/security/advisories/GHSA-273q-qgh5-wrj6

### [CVE-2026-66749](https://github.com/theopaid/Unchecked-Room-Lookup-Leads-to-Server-Crash-Let-s-Chat-)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-66749
- 関連キーワード: go, node.js
- 影響製品: -
- 公開日: 2026-07-29 01:20:16 JST
- 更新日: 2026-07-29 02:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Let's Chat 0.4.0から0.4.8にnull参照によるサーバークラッシュを引き起こす脆弱性が存在。
- 影響: 認証済み攻撃者によるサービス拒否（DoS）攻撃の可能性。
- 推奨対応: Let's Chatのアップデートを行うこと。

#### References
- https://github.com/theopaid/Unchecked-Room-Lookup-Leads-to-Server-Crash-Let-s-Chat-
- https://www.vulncheck.com/advisories/let-s-chat-denial-of-service-via-null-dereference-in-room-lookup

### [CVE-2026-67182](https://github.com/theopaid/HTTP-Request-Smuggling-Enables-Front-End-Access-Control-Bypass-rouille-)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-67182
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-07-29 02:17:07 JST
- 更新日: 2026-07-29 03:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Rouille 0.3.3 through 3.6.2 contains an HTTP request smuggling vulnerability that allows remote attackers to bypass access controls by injecting bare line feed characters (0x0A) into client-supplied request header values that are copied verbatim to upstream connections without validation. Attackers can craft a header v...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/theopaid/HTTP-Request-Smuggling-Enables-Front-End-Access-Control-Bypass-rouille-
- https://www.vulncheck.com/advisories/rouille-http-request-smuggling-via-proxy-header-injection

### [CVE-2026-48058](https://github.com/forgekeep/nebula-mesh/commit/ffdd67dbf221d9a5855c39fbe11b49c245048d85)

> **Backend** / **MEDIUM** / CVSS: **4.6** / KEV: **no**

- タイトル: CVE-2026-48058
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-29 04:17:34 JST
- 更新日: 2026-07-29 05:17:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: nebula-mesh 0.3.2未満でCookieにSecure属性が設定されておらず、セッションが盗聴される可能性。
- 影響: ネットワーク経由でセッション情報が漏洩するリスク。
- 推奨対応: nebula-meshを0.3.2以降に更新し、Secure属性を有効にすること。

#### References
- https://github.com/forgekeep/nebula-mesh/commit/ffdd67dbf221d9a5855c39fbe11b49c245048d85
- https://github.com/forgekeep/nebula-mesh/releases/tag/v0.3.2
- https://github.com/forgekeep/nebula-mesh/security/advisories/GHSA-rqfj-vv8r-xhqc
- https://github.com/forgekeep/nebula-mesh/security/advisories/GHSA-rqfj-vv8r-xhqc

### [CVE-2026-47427](https://github.com/github/github-mcp-server/commit/c88d2ecdd3bb07f7bdd75296e3ee676febf14f58)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-47427
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 01:18:14 JST
- 更新日: 2026-07-29 03:17:20 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: GitHub MCP ServerのCompletionsHandler関数がnilチェックなしでparams.Refにアクセスし、認証前にクラッシュを引き起こす可能性がある。
- 影響: 認証なしのリモートからのサービス拒否（DoS）を引き起こす可能性がある。
- 推奨対応: バージョン1.1.0以降にアップデートすること。

#### References
- https://github.com/github/github-mcp-server/commit/c88d2ecdd3bb07f7bdd75296e3ee676febf14f58
- https://github.com/github/github-mcp-server/pull/2502
- https://github.com/github/github-mcp-server/releases/tag/v1.1.0
- https://github.com/github/github-mcp-server/security/advisories/GHSA-w4q6-qw23-4rg7
- https://github.com/github/github-mcp-server/security/advisories/GHSA-w4q6-qw23-4rg7

### [CVE-2026-47726](https://github.com/forgekeep/nebula-mesh/commit/8baaace54c2a23e7c351b3efab5a31ab07b125dc)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-47726
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 04:17:34 JST
- 更新日: 2026-07-29 04:17:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: nebula-meshの監査ログ取得APIが管理者チェックを行わず、オペレーターAPIキーで全監査ログを取得可能。
- 影響: テナント間の活動情報漏洩や攻撃対象の推測につながる可能性がある。
- 推奨対応: バージョン0.3.2以降にアップデートすること。

#### References
- https://github.com/forgekeep/nebula-mesh/commit/8baaace54c2a23e7c351b3efab5a31ab07b125dc
- https://github.com/forgekeep/nebula-mesh/releases/tag/v0.3.2
- https://github.com/forgekeep/nebula-mesh/security/advisories/GHSA-qm33-p5p9-f8vg
- https://github.com/forgekeep/nebula-mesh/security/advisories/GHSA-qm33-p5p9-f8vg

### [CVE-2026-54638](https://github.com/gotd/td/commit/9d5d1f31ea5022d9798d84ccce15de2e91ba6baa)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-54638
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 08:17:08 JST
- 更新日: 2026-07-29 08:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: gotd/tdのproto.UnencryptedMessage.Decodeが攻撃者制御のデータ長を検証せずにメモリ割り当てを行う。
- 影響: 認証なしのリモートから過剰なメモリ割り当てによるサービス拒否（DoS）を引き起こす可能性がある。
- 推奨対応: バージョン0.145.1以降にアップデートすること。

#### References
- https://github.com/gotd/td/commit/9d5d1f31ea5022d9798d84ccce15de2e91ba6baa
- https://github.com/gotd/td/issues/1711
- https://github.com/gotd/td/releases/tag/v0.145.1
- https://github.com/gotd/td/security/advisories/GHSA-whmm-qj9r-wvr2

### [CVE-2026-54719](https://github.com/goshs-labs/goshs/commit/7cf911a26ace737e1a55b7dc073e307a25f7fd1d)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-54719
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 08:17:09 JST
- 更新日: 2026-07-29 08:17:09 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: goshsのbulkDownloadハンドラがACLや認証を適切に適用せず、認証なしで保護ファイルの読み取りが可能。
- 影響: 認証なしのファイル読み取りによる情報漏洩の可能性がある。
- 推奨対応: バージョン2.1.1以降にアップデートすること。

#### References
- https://github.com/goshs-labs/goshs/commit/7cf911a26ace737e1a55b7dc073e307a25f7fd1d
- https://github.com/goshs-labs/goshs/releases/tag/v2.1.1
- https://github.com/goshs-labs/goshs/security/advisories/GHSA-rmxw-pq4x-3fvh

### [CVE-2026-48025](https://github.com/forgekeep/nebula-mesh/commit/bca1d5914fbaf3517d3b86145a802c00de4a8122)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-48025
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 03:17:20 JST
- 更新日: 2026-07-29 03:17:20 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: nebula-meshで復号したCA秘密鍵の内容が関数終了時にゼロ化されず、プロセスヒープに残存する可能性がある。
- 影響: 秘密鍵のメモリ残留により情報漏洩リスクがある可能性がある。
- 推奨対応: 修正済みバージョンにアップデートし、秘密鍵のメモリ管理を確認すること。

#### References
- https://github.com/forgekeep/nebula-mesh/commit/bca1d5914fbaf3517d3b86145a802c00de4a8122
- https://github.com/forgekeep/nebula-mesh/releases/tag/v0.3.7
- https://github.com/forgekeep/nebula-mesh/security/advisories/GHSA-8h84-fhqq-q58v

### [CVE-2026-54332](https://github.com/gopacket/gopacket/commit/76119086f5936aacd7088bdf97d565501bb6c4cc)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-54332
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 02:16:51 JST
- 更新日: 2026-07-29 03:17:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: gopacketのsFlow ExtendedGatewayFlowデコーダが攻撃者制御の値で大容量メモリ割り当てを行う。
- 影響: 認証なしのリモートからのサービス拒否（DoS）を引き起こす可能性がある。
- 推奨対応: バージョン1.6.1以降にアップデートすること。

#### References
- https://github.com/gopacket/gopacket/commit/76119086f5936aacd7088bdf97d565501bb6c4cc
- https://github.com/gopacket/gopacket/releases/tag/v1.6.1
- https://github.com/gopacket/gopacket/security/advisories/GHSA-g6v3-7xmc-w563
- https://github.com/gopacket/gopacket/security/advisories/GHSA-g6v3-7xmc-w563

### [CVE-2026-54345](https://github.com/gopacket/gopacket/commit/145859d0eaee1a6f5925ffb93851c976449c3311)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-54345
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 02:16:51 JST
- 更新日: 2026-07-29 03:17:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: gopacketのDiameter AVPデコーダが不正なAVP長で大容量メモリ割り当てを行い、連続で送信されるとOOMを引き起こす。
- 影響: 認証なしのリモートからのサービス拒否（DoS）を引き起こす可能性がある。
- 推奨対応: バージョン1.6.1以降にアップデートすること。

#### References
- https://github.com/gopacket/gopacket/commit/145859d0eaee1a6f5925ffb93851c976449c3311
- https://github.com/gopacket/gopacket/releases/tag/v1.6.1
- https://github.com/gopacket/gopacket/security/advisories/GHSA-6r28-9ppf-4hj5
- https://github.com/gopacket/gopacket/security/advisories/GHSA-6r28-9ppf-4hj5

### [CVE-2026-66063](https://github.com/goshs-labs/goshs/commit/f3ef599e409151d1380866e47de8b1afb0bb54fa)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-66063
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 08:17:10 JST
- 更新日: 2026-07-29 08:17:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: goshsのmultipartアップロードでファイル名に「..」を拒否せず、認証なしでサーバ外のファイル作成が可能。
- 影響: 認証なしの任意ファイル作成によるセキュリティリスクがある可能性がある。
- 推奨対応: バージョン2.1.5以降にアップデートすること。

#### References
- https://github.com/goshs-labs/goshs/commit/f3ef599e409151d1380866e47de8b1afb0bb54fa
- https://github.com/goshs-labs/goshs/security/advisories/GHSA-wg2q-39h6-66x9

### [CVE-2026-66064](https://github.com/goshs-labs/goshs/commit/f3ef599e409151d1380866e47de8b1afb0bb54fa)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-66064
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-29 08:17:10 JST
- 更新日: 2026-07-29 08:17:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: goshsのsendFileハンドラがパスの正規化と認証ファイル名の取得に不整合があり、ACL保護を回避可能。
- 影響: 認証なしで保護ファイルへのアクセスが可能になる可能性がある。
- 推奨対応: バージョン2.1.5以降にアップデートすること。

#### References
- https://github.com/goshs-labs/goshs/commit/f3ef599e409151d1380866e47de8b1afb0bb54fa
- https://github.com/goshs-labs/goshs/pull/222
- https://github.com/goshs-labs/goshs/security/advisories/GHSA-964w-f6gj-5236

### [CVE-2026-54691](https://github.com/koxudaxi/datamodel-code-generator/commit/5fdba4a09f2d7a9996a504975b7ef7d63e3715bb)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-54691
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-29 07:17:40 JST
- 更新日: 2026-07-29 07:17:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: datamodel-code-generatorのhttp.get_bodyがホスト/IP検証なしにリダイレクト先を受け入れ、SSRFを引き起こす可能性がある。
- 影響: ループバックやプライベートネットワークへの不正アクセス（SSRF）リスクがある可能性がある。
- 推奨対応: バージョン0.61.0以降にアップデートすること。

#### References
- https://github.com/koxudaxi/datamodel-code-generator/commit/5fdba4a09f2d7a9996a504975b7ef7d63e3715bb
- https://github.com/koxudaxi/datamodel-code-generator/releases/tag/0.61.0
- https://github.com/koxudaxi/datamodel-code-generator/security/advisories/GHSA-rfr2-mq9m-x2qx

# Backend CVE Summary (2026-07-10)

## Overview

- 取得日時: 2026-07-10 08:23:44 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 21
- Critical: 1
- High: 9
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-15188](https://github.com/manjurulhoque/django-job-portal/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-15188
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-07-10 01:16:38 JST
- 更新日: 2026-07-10 02:16:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: manjurulhoque django-job-portalのEmployee Dashboard EndpointにあるEditEmployeeProfileAPIView関数で、role引数の操作により不適切なアクセス制御の脆弱性が確認されています。  
- 影響: リモートからの攻撃が可能で、権限のない操作が行われる恐れがあります。  
- 推奨対応: 最新のアップデートを適用し、開発元の対応状況を注視してください。

#### References
- https://github.com/manjurulhoque/django-job-portal/
- https://github.com/manjurulhoque/django-job-portal/issues/91
- https://vuldb.com/cve/CVE-2026-15188
- https://vuldb.com/submit/851436
- https://vuldb.com/vuln/377114

### [CVE-2026-33655](https://github.com/QuantumNous/new-api/commit/20399d3c8fcb4e3649d53163eb11940fd6763743)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-33655
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-10 08:17:04 JST
- 更新日: 2026-07-10 08:17:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: New APIの0.12.0-alpha.1以前のバージョンで、SSRF保護設定がホスト名のIPフィルタリングを適用せず、認証済みユーザーが内部IPアドレスを指す通知URLを設定可能でした。  
- 影響: 認証済みユーザーによる内部ネットワークへの不正アクセスや情報漏洩のリスクが存在します。  
- 推奨対応: バージョン0.12.0-alpha.1以降にアップデートし、ApplyIPFilterForDomain設定の適切な利用を検討してください。

#### References
- https://github.com/QuantumNous/new-api/commit/20399d3c8fcb4e3649d53163eb11940fd6763743
- https://github.com/QuantumNous/new-api/releases/tag/v0.12.0-alpha.1
- https://github.com/QuantumNous/new-api/security/advisories/GHSA-6qcr-qxgr-m7fv

### [CVE-2026-59832](https://github.com/siyuan-note/siyuan/commit/68cc0f537dfa4502496dfa794e71835421c25c09)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-59832
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-10 08:17:05 JST
- 更新日: 2026-07-10 08:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SiYuanの3.7.1以前のバージョンで、認証済みリクエストが/snippets/*filepath経路を通じて機密ファイルにアクセス可能なパス検証不備の脆弱性が存在します。  
- 影響: ワークスペースの秘密情報やドキュメントデータベースの不正読み取りが可能となる恐れがあります。  
- 推奨対応: バージョン3.7.1以降にアップデートし、パス検証の修正を適用してください。

#### References
- https://github.com/siyuan-note/siyuan/commit/68cc0f537dfa4502496dfa794e71835421c25c09
- https://github.com/siyuan-note/siyuan/releases/tag/v3.7.1
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-275h-v5h9-vr82

### [CVE-2026-57019](https://supportportal.juniper.net/JSA110079)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-57019
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-10 07:17:06 JST
- 更新日: 2026-07-10 07:17:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Juniper Networks Junos OSのMXシリーズにおいて、パケットフォワーディングエンジンで入力されたパケットサイズの不適切な検証により、隣接する未認証攻撃者がサービス拒否（DoS）を引き起こす可能性があります。  
- 影響: 特定のパケット受信時にFPCの重大エラーが発生し、FPCのリセットが行われるため、トラフィックに影響が及びます。  
- 推奨対応: Juniperから提供される修正パッチの適用や、影響を受けるバージョンの使用を避けることが推奨されます。

#### References
- https://supportportal.juniper.net/JSA110079

### [CVE-2026-50188](https://github.com/getkirby/kirby/commit/aa33414e1669e866cdd6f4decfae2a669e8bb828)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-50188
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-10 04:17:05 JST
- 更新日: 2026-07-10 05:16:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Kirby CMSのHttp Remoteクラスで、信頼されていないデータをHTTPヘッダーに含めた場合、改行文字を使ってリモートサービスに意図しないヘッダーを注入される可能性があります。  
- 影響: 悪意あるヘッダー注入により、リモートサービスへのリクエストが改変されるリスクがあります。  
- 推奨対応: Kirbyをバージョン4.9.4または5.4.4以降にアップデートし、Http Remoteクラスの脆弱性を修正してください。

#### References
- https://github.com/getkirby/kirby/commit/aa33414e1669e866cdd6f4decfae2a669e8bb828
- https://github.com/getkirby/kirby/commit/fad9cbd22c73ed0fbd3aaf62310a8dcacfc007cd
- https://github.com/getkirby/kirby/releases/tag/4.9.4
- https://github.com/getkirby/kirby/releases/tag/5.4.4
- https://github.com/getkirby/kirby/security/advisories/GHSA-4v4h-m2qq-ppgw

### [CVE-2026-59854](https://github.com/siyuan-note/siyuan/commit/914c5180a88d17f6d38716a56483327b367ef55f)

> **Backend** / **MEDIUM** / CVSS: **4.9** / KEV: **no**

- タイトル: CVE-2026-59854
- 関連キーワード: go, docker
- 影響製品: -
- 公開日: 2026-07-10 08:17:06 JST
- 更新日: 2026-07-10 08:17:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SiYuanの3.7.1以前のバージョンで、認証済み管理者やAPIトークンユーザーが特定の機密ファイルをコピーし外部に漏洩させる可能性がある脆弱性です。  
- 影響: ホームディレクトリ内の認証情報ファイルが不正に取得されるリスクがあります。  
- 推奨対応: バージョン3.7.1-alpha.2または3.7.1にアップデートして脆弱性を修正してください。

#### References
- https://github.com/siyuan-note/siyuan/commit/914c5180a88d17f6d38716a56483327b367ef55f
- https://github.com/siyuan-note/siyuan/commit/b54fee401799d987d2fd2888220938ad599b8c5e
- https://github.com/siyuan-note/siyuan/releases/tag/v3.7.1
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-vmm8-3ccv-ppvw

### [CVE-2026-11404](https://github.com/cesanta/mongoose)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-11404
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-10 01:16:34 JST
- 更新日: 2026-07-10 02:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Cesanta Mongoose 7.22以前のバージョンにおいて、TLSサーバー関数mg_tls_server_recv_hello()が攻撃者制御のsession_id_lenを検証せずにバッファインデックスとして使用し、範囲外読み取りが発生する脆弱性。  
- 影響: リモートの未認証攻撃者が細工したClientHelloを送信することで、HTTPSやMQTTS、WSSサービスのクラッシュを引き起こす可能性がある。  
- 推奨対応: 最新バージョンへのアップデートや、TLSハンドシェイク処理における入力検証の強化を検討すること。

#### References
- https://github.com/cesanta/mongoose
- https://github.com/cesanta/mongoose/commit/c288ac1f38424ffdd4d2fd5e1893fd4962642db3
- https://github.com/cesanta/mongoose/releases/tag/7.22
- https://www.vulncheck.com/advisories/cesanta-mongoose-out-of-bounds-read-in-mg-tls-builtin-clienthello-session-id-parsing

### [CVE-2026-60108](https://github.com/zeek/zeek/commit/93ff6950a90cfa9d00c1062cde429313a0402a01)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-60108
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-10 00:16:41 JST
- 更新日: 2026-07-10 04:40:42 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Zeek 8.0.9以前のFTPアナライザにおいて、AUTH GSSAPI交渉後の大きなADAT制御行によりメモリ消費が制御されず、プロセス終了を引き起こす脆弱性が存在します。  
- 影響: 認証されていないリモート攻撃者がサービス拒否（DoS）を引き起こし、Zeekセンサーの停止を招く可能性があります。  
- 推奨対応: Zeekをバージョン8.0.9以降にアップデートし、FTPアナライザの脆弱性を修正してください。

#### References
- https://github.com/zeek/zeek/commit/93ff6950a90cfa9d00c1062cde429313a0402a01
- https://github.com/zeek/zeek/releases/tag/v8.0.9
- https://www.vulncheck.com/advisories/zeek-uncontrolled-memory-consumption-dos-via-ftp-analyzer

### [CVE-2026-49256](https://github.com/discourse/discourse/releases/tag/v2026.1.5)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-49256
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-10 07:17:05 JST
- 更新日: 2026-07-10 07:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Discourse is an open-source discussion platform. Prior to 2026.6.0, 2026.5.1, 2026.4.2, and 2026.1.5, restricted tag and tag-group names attached to publicly readable categories as allowed_tags, allowed_tag_groups, or required tag groups could leak to anonymous and unauthorized users through category and group endpoint...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/discourse/discourse/releases/tag/v2026.1.5
- https://github.com/discourse/discourse/releases/tag/v2026.4.2
- https://github.com/discourse/discourse/releases/tag/v2026.5.1
- https://github.com/discourse/discourse/releases/tag/v2026.6.0
- https://github.com/discourse/discourse/security/advisories/GHSA-mwp7-572g-6qpx

### [CVE-2026-5005](https://siberguvenlik.gov.tr/guvenlik-bildirimleri/detay/tr-26-0524)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-5005
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-10 00:16:40 JST
- 更新日: 2026-07-10 01:21:30 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Improper neutralization of input during web page generation ('cross-site scripting') vulnerability in Twiser Informatics Technology Consulting, Trade and Education Inc. OKRs & Goals allows Stored XSS. This issue affects OKRs & Goals: from 28220 before 28398.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://siberguvenlik.gov.tr/guvenlik-bildirimleri/detay/tr-26-0524

### [CVE-2026-57024](https://supportportal.juniper.net/JSA110084)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-57024
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-10 07:17:07 JST
- 更新日: 2026-07-10 07:17:07 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A Use of Multiple Resources with Duplicate Identifier vulnerability in the IKE daemon (iked) of Juniper Networks Junos OS on MX with SPC3 and SRX Series allows an unauthenticated, network-based attacker to cause a Denial-of-Service (DoS). On an MX with SPC3 and SRX devices configured for VPN service, when a large numbe...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://supportportal.juniper.net/JSA110084

### [CVE-2026-57021](https://supportportal.juniper.net/JSA110081)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-57021
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-10 07:17:07 JST
- 更新日: 2026-07-10 07:17:07 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: An Out-of-bounds Write vulnerability in the http-gatekeeper (http-gk) of Juniper Networks Junos OS on SRX Series allows an unauthenticated, network-based attacker to cause a Denial-of-Service (DoS). If an SRX Series device is configured for remote-access VPN with pre-logon compliance check, a network-based attacker sen...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://supportportal.juniper.net/JSA110081

### [CVE-2026-61344](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-190-02.json)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-61344
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-10 03:16:58 JST
- 更新日: 2026-07-10 04:19:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The Superior Court of California Hearing Reminder Service at https://www.hrs.courts.ca.gov exposes an API endpoint that returns court reminder records containing potentially sensitive information without authentication.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-190-02.json
- https://www.cve.org/CVERecord?id=CVE-2026-61344
- https://www.hrs.courts.ca.gov

### [CVE-2026-54695](https://github.com/pipecat-ai/pipecat/commit/3032da53434c5ef01d368654b3551cf21c50dec9)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-54695
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-10 04:17:06 JST
- 更新日: 2026-07-10 04:22:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Pipecat is an open-source Python framework for building real-time voice and multimodal conversational agents. Prior to 1.4.0, the pipecat development runner registers a /ws WebSocket endpoint for telephony testing that accepts connections without authentication, reads an attacker-supplied callSid from a Twilio stream-s...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pipecat-ai/pipecat/commit/3032da53434c5ef01d368654b3551cf21c50dec9
- https://github.com/pipecat-ai/pipecat/commit/88440676996e5e548e1aecea5d565e1c48ccf6fa
- https://github.com/pipecat-ai/pipecat/pull/4660
- https://github.com/pipecat-ai/pipecat/releases/tag/v1.4.0
- https://github.com/pipecat-ai/pipecat/security/advisories/GHSA-j8cv-x86q-rj85

### [CVE-2026-55865](https://github.com/jg-rp/liquid/commit/26db8931cf35e8433c1ca506fc32c3bb62f743d4)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-55865
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-07-10 06:16:56 JST
- 更新日: 2026-07-10 06:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Python Liquid is a Python engine for the Liquid template language. Prior to 2.2.1, given a malformed {% case %} tag without an associated {% when %} or {% else %} block and no terminating {% endcase %} tag, Python Liquid hangs in an infinite loop at parse time because liquid.TokenStream.eof did not give the EOF token m...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jg-rp/liquid/commit/26db8931cf35e8433c1ca506fc32c3bb62f743d4
- https://github.com/jg-rp/liquid/releases/tag/v2.2.1
- https://github.com/jg-rp/liquid/security/advisories/GHSA-vq2f-vcc9-j8mv

### [CVE-2026-59214](https://github.com/open-webui/open-webui/security/advisories/GHSA-4r2p-27mh-5m22)

> **Backend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-59214
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-07-10 02:17:02 JST
- 更新日: 2026-07-10 04:22:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. Prior to 0.10.0, Open WebUI runs client-side Python with Pyodide in a same-origin web worker, allowing stored chat payloads that use pyodide.http.pyfetch or the js module fetch and XMLHttpRequest APIs to issue authenticated same-origi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-webui/open-webui/security/advisories/GHSA-4r2p-27mh-5m22

### [CVE-2026-59216](https://github.com/open-webui/open-webui/commit/386ac958144dbbbf0aa6e268070d72b681a318aa)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-59216
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-10 02:17:02 JST
- 更新日: 2026-07-10 04:22:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. Prior to 0.10.0, get_event_call delivered execute:python and execute:tool Socket.IO events to a client-supplied session_id after checking only that the session was connected, allowing authenticated users who learned another socket ID...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-webui/open-webui/commit/386ac958144dbbbf0aa6e268070d72b681a318aa
- https://github.com/open-webui/open-webui/pull/25763
- https://github.com/open-webui/open-webui/releases/tag/v0.10.0
- https://github.com/open-webui/open-webui/security/advisories/GHSA-74h3-cxq7-vc5q
- https://github.com/open-webui/open-webui/security/advisories/GHSA-74h3-cxq7-vc5q

### [CVE-2026-59726](https://github.com/ruvnet/ruflo/commit/d00a0a40cd8bdbca877ac7f675f416bdc69accd1)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-59726
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-07-10 03:16:57 JST
- 更新日: 2026-07-10 04:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Ruflo is an agent meta-harness for Claude Code and Codex. Prior to 3.16.3, ruflo's default docker-compose deployment exposed the MCP bridge POST /mcp and POST /mcp/:group endpoints without authentication, allowing an unauthenticated network attacker to invoke tools/call to terminal_execute, obtain a shell in the bridge...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/ruvnet/ruflo/commit/d00a0a40cd8bdbca877ac7f675f416bdc69accd1
- https://github.com/ruvnet/ruflo/pull/2521
- https://github.com/ruvnet/ruflo/releases/tag/v3.16.3
- https://github.com/ruvnet/ruflo/security/advisories/GHSA-c4hm-4h84-2cf3

### [CVE-2026-55605](https://github.com/arikusi/deepseek-mcp-server/blob/main/CHANGELOG.md#180---2026-06-14)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-55605
- 関連キーワード: express, docker
- 影響製品: -
- 公開日: 2026-07-10 07:17:06 JST
- 更新日: 2026-07-10 07:17:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: DeepSeek MCP Server is an MCP server for DeepSeek V4. Starting in version 1.4.2 and prior to version 1.8.0, the self-hosted HTTP transport of `@arikusi/deepseek-mcp-server` exposes `POST /mcp` without any authentication: `createMcpExpressApp` is called without an `authProvider` and no middleware guards the route, so an...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/arikusi/deepseek-mcp-server/blob/main/CHANGELOG.md#180---2026-06-14
- https://github.com/arikusi/deepseek-mcp-server/releases/tag/v1.8.0
- https://github.com/arikusi/deepseek-mcp-server/security/advisories/GHSA-72f3-6w86-7rv3

### [CVE-2026-53961](https://github.com/discourse/discourse/commit/3a3d315a85ef3c6aabfc7e7bb38702059784f06b)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-53961
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-07-10 07:17:05 JST
- 更新日: 2026-07-10 07:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Discourse is an open-source discussion platform. Prior to 2026.6.0, 2026.5.1, 2026.4.2, and 2026.1.5, the AWS SES bounce webhook at POST /webhooks/aws verified that SNS messages were signed by Amazon but did not bind them to trusted TopicArn values, allowing any AWS account holder to publish validly signed forged Bounc...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/discourse/discourse/commit/3a3d315a85ef3c6aabfc7e7bb38702059784f06b
- https://github.com/discourse/discourse/commit/61f12e13aa1b760f81d5ff60f12e3a7e77434b94
- https://github.com/discourse/discourse/commit/958f0cd831d65a49ec75f05343ca2c167679f0ea
- https://github.com/discourse/discourse/commit/aea35190791261bab258ebab05da279e78cdd0e6
- https://github.com/discourse/discourse/releases/tag/v2026.1.5

### [CVE-2026-55170](https://github.com/openfga/helm-charts/commit/96d5517a2693ff5def451dee7d6b9d1baeb281f8)

> **Backend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-55170
- 関連キーワード: gin, mysql
- 影響製品: -
- 公開日: 2026-07-10 07:17:05 JST
- 更新日: 2026-07-10 07:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenFGA is an authorization/permission engine built for developers. Prior to 1.18.0, when MySQL is being used as the datastore and authorization decisions rely on case-sensitive user strings, the tuple, changelog, and authorization_model identifier columns can compare case-distinct values such as user:Alice and user:al...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/openfga/helm-charts/commit/96d5517a2693ff5def451dee7d6b9d1baeb281f8
- https://github.com/openfga/helm-charts/releases/tag/openfga-0.3.9
- https://github.com/openfga/openfga/commit/a2e0dbefc3e01a95c785f81a3563bc6571b08b11
- https://github.com/openfga/openfga/releases/tag/v1.18.0
- https://github.com/openfga/openfga/security/advisories/GHSA-cf98-j28v-49v6

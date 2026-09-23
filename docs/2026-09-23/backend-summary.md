# Backend CVE Summary (2026-09-23)

## Overview

- 取得日時: 2026-09-23 09:24:03 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 15
- Critical: 1
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-57149](https://github.com/plone/plone.app.portlets/security/advisories/GHSA-rr49-f9g6-c9r5)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-57149
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-09-23 04:16:43 JST
- 更新日: 2026-09-23 05:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: plone.app.portlets.portlets provides a Plone-specific user interface for plone.portlets, as well as a standard set of portlets that ship with Plone. Starting in version 5.0.0 and prior to versions 5.0.8, 6.0.4, and 7.0.2, the Classic portlet (plone.app.portlets.portlets.classic) used its user-supplied template/macro fi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/plone/plone.app.portlets/security/advisories/GHSA-rr49-f9g6-c9r5

### [CVE-2026-75608](https://github.com/blakeblackshear/frigate/commit/520d9eeb7f0fe46021f29fb8169741dd1d429271)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-75608
- 関連キーワード: go, gin, docker, nginx
- 影響製品: -
- 公開日: 2026-09-23 01:17:54 JST
- 更新日: 2026-09-23 01:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Frigate is an open source network video recorder. Prior to 0.18.0, the prefix-matched location /api/go2rtc/api in docker/main/rootfs/usr/local/nginx/conf/nginx.conf requires authentication but does not require an administrator role for GET requests, exposing the proxied go2rtc API to viewer users. An authenticated view...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/blakeblackshear/frigate/commit/520d9eeb7f0fe46021f29fb8169741dd1d429271
- https://github.com/blakeblackshear/frigate/pull/22735
- https://github.com/blakeblackshear/frigate/releases/tag/v0.18.0
- https://github.com/blakeblackshear/frigate/security/advisories/GHSA-mgh5-cr9h-g6hr

### [CVE-2026-83599](https://github.com/netdata/netdata/commit/e3811f7ee6e9fdfc4cbcb9929cab3f5d71d722d7)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-83599
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-23 02:17:25 JST
- 更新日: 2026-09-23 03:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Netdata is an open source observability tool. Prior to 2.11.0, Netdata's unauthenticated WebSocket server negotiates permessage-deflate before authentication, and src/web/websocket/websocket-compression.c allows websocket_client_decompress_message() to grow decompressed output toward WS_MAX_DECOMPRESSED_SIZE without en...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/netdata/netdata/commit/e3811f7ee6e9fdfc4cbcb9929cab3f5d71d722d7
- https://github.com/netdata/netdata/pull/22828
- https://github.com/netdata/netdata/releases/tag/v2.11.0
- https://github.com/netdata/netdata/security/advisories/GHSA-c8p4-cg3j-f4h2

### [CVE-2026-88010](https://github.com/traefik/traefik/commit/ddc1bf4660b85fd61fafdd821eb8216fb1a0b130)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-88010
- 関連キーワード: go, traefik
- 影響製品: -
- 公開日: 2026-09-23 01:18:06 JST
- 更新日: 2026-09-23 01:18:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Traefik is an open source HTTP reverse proxy and load balancer. From 3.6.11 until 3.7.13, checkPassword in pkg/middlewares/auth/basic_auth.go constructs the BasicAuth singleflight key from the submitted password and stored secret. Concurrent requests for absent usernames therefore coalesce on one key while configured u...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/traefik/traefik/commit/ddc1bf4660b85fd61fafdd821eb8216fb1a0b130
- https://github.com/traefik/traefik/pull/13816
- https://github.com/traefik/traefik/releases/tag/v3.7.13
- https://github.com/traefik/traefik/security/advisories/GHSA-8fcf-v89g-xpg6

### [CVE-2026-77633](https://github.com/cloudreve/cloudreve/commit/7329602751c00bb4136fe9ad8b364d0df70773df)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-77633
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-23 01:17:55 JST
- 更新日: 2026-09-23 01:17:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CloudreveのPrepareUpload処理において、ストレージ容量チェックの競合状態が発生する脆弱性。
- 影響: 認証されたユーザーが並行リクエストによりクォータを超えるストレージ予約を行い、ホストストレージを枯渇させて他のユーザーへのサービス拒否（DoS）を引き起こす可能性があります。
- 推奨対応: Cloudreveをバージョン 4.18.0 以降に更新してください。

#### References
- https://github.com/cloudreve/cloudreve/commit/7329602751c00bb4136fe9ad8b364d0df70773df
- https://github.com/cloudreve/cloudreve/releases/tag/4.18.0
- https://github.com/cloudreve/cloudreve/security/advisories/GHSA-xj3h-wwxq-gfcj

### [CVE-2026-95653](https://github.com/concretecms-community-store/community_store)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-95653
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-23 01:18:18 JST
- 更新日: 2026-09-23 05:55:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Concrete CMS Community Store before 2.7.8 derives digital product download tokens from order creation timestamps instead of random values, making tokens predictable. Unauthenticated attackers can enumerate sequential order and file identifiers to calculate valid download tokens and retrieve digital goods purchased by o...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/concretecms-community-store/community_store
- https://github.com/concretecms-community-store/community_store/blob/v2.7.7/src/CommunityStore/Utilities/Download.php#L17
- https://github.com/concretecms-community-store/community_store/blob/v2.7.7/src/CommunityStore/Utilities/Download.php#L45
- https://github.com/concretecms-community-store/community_store/commit/a71138db250d5c207e49fe3f1287241f04e3f747
- https://github.com/concretecms-community-store/community_store/releases/tag/v2.7.8

### [CVE-2026-79913](https://github.com/cloudreve/cloudreve/commit/1c5cad6dec7ec3037c6479e3a26a3909995d16a2)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-79913
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-23 01:17:57 JST
- 更新日: 2026-09-23 03:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CloudreveのSSRF対策処理において、NAT64や6to4などのIPv4-in-IPv6遷移形式のデコード・検証が不足している脆弱性。
- 影響: リモートダウンロード権限を持つ認証済みユーザーにより、内部サービスへのアクセスやクラウドインスタンスのクレデンシャル等の機密情報が漏洩する可能性があります。
- 推奨対応: Cloudreveをバージョン 4.18.0 以降に更新してください。

#### References
- https://github.com/cloudreve/cloudreve/commit/1c5cad6dec7ec3037c6479e3a26a3909995d16a2
- https://github.com/cloudreve/cloudreve/releases/tag/4.18.0
- https://github.com/cloudreve/cloudreve/security/advisories/GHSA-jvh5-97xg-v99f

### [CVE-2026-76805](https://github.com/projectdiscovery/nuclei/commit/ccbfb12bd01447ba25f6e755dfb2bee677736da6)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-76805
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-09-23 02:17:25 JST
- 更新日: 2026-09-23 04:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NucleiのDAST/fuzzペイロード処理において、置換されたデータが複数回評価される脆弱性（CVE-2026-41645の不完全な修正）。
- 影響: -env-vars オプションが有効な場合、悪意のあるスキャン対象から返されたデータによってスキャンホストの環境変数（資格情報やAPIキーなど）が漏洩する可能性があります。
- 推奨対応: Nucleiを修正済みの最新バージョンに更新してください。

#### References
- https://github.com/projectdiscovery/nuclei/commit/ccbfb12bd01447ba25f6e755dfb2bee677736da6
- https://github.com/projectdiscovery/nuclei/pull/7499
- https://github.com/projectdiscovery/nuclei/releases/tag/v3.10.0
- https://github.com/projectdiscovery/nuclei/security/advisories/GHSA-jpvm-9frm-hjcq

### [CVE-2026-95701](https://github.com/MISP/MISP/commit/a2f7cba6e)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-95701
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-23 00:17:28 JST
- 更新日: 2026-09-23 01:18:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MISPの__statisticsOrgsメソッドにおいて、組織名をパス生成処理へ適切にサニタイズせず結合するディレクトリトラバーサルの脆弱性。
- 影響: 対象ディレクトリが存在する場合、認証されたユーザーにより任意のファイルパスの存在チェックなどに悪用される可能性がありますが、現在の配置構造では実行されない可能性があります。
- 推奨対応: MISPを修正済みバージョンへ更新してください。

#### References
- https://github.com/MISP/MISP/commit/a2f7cba6e

### [CVE-2026-77637](https://github.com/cloudreve/cloudreve/commit/bce08f88e9d8f881e78fd18e7a6598b31922c492)

> **Backend** / **LOW** / CVSS: **3.8** / KEV: **no**

- タイトル: CVE-2026-77637
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-23 01:17:55 JST
- 更新日: 2026-09-23 03:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cloudreveの特定の管理ツールルート（WOPI/mail）において、書き込み権限スコープのミドルウェア検証が欠落している脆弱性。
- 影響: 読み取り専用（Admin.Read）権限のAPIキーやOAuthアプリを用いて、WOPIエンドポイントの探索やテストメールの不正送信が行われる可能性があります。
- 推奨対応: Cloudreveをバージョン 4.18.0 以降に更新してください。

#### References
- https://github.com/cloudreve/cloudreve/commit/bce08f88e9d8f881e78fd18e7a6598b31922c492
- https://github.com/cloudreve/cloudreve/releases/tag/4.18.0
- https://github.com/cloudreve/cloudreve/security/advisories/GHSA-w89x-c962-c44g

### [CVE-2026-95685](https://github.com/MISP/MISP/commit/66aebfb1a)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-95685
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-23 00:17:26 JST
- 更新日: 2026-09-23 01:18:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MISPのEventReports機能におけるreplaceSuggestionInReportアクションのアクセス制御不備の脆弱性。
- 影響: perm_add権限を持たない認証済みユーザーがレポート内のサジェストデータを不当に変更し、共有脅威インテリジェンスの不整合や改ざんを引き起こす可能性があります。
- 推奨対応: MISPを修正済みバージョンへ更新してください。

#### References
- https://github.com/MISP/MISP/commit/66aebfb1a

### [CVE-2026-95703](https://github.com/MISP/MISP/commit/12eaadc9e)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-95703
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-23 00:17:28 JST
- 更新日: 2026-09-23 01:18:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MISPのOrganisationsController::__uploadLogoメソッドにおいて、is_uploaded_fileによる検証前にファイルパスの検証処理を行う脆弱性。
- 影響: サイト管理者権限を持つ攻撃者が任意のサーバーファイルパスの存在有無や画像タイプを推測できる可能性があります。
- 推奨対応: MISPを修正済みバージョンへ更新してください。

#### References
- https://github.com/MISP/MISP/commit/12eaadc9e

### [CVE-2026-77271](https://github.com/sooperset/mcp-atlassian/commit/b041733473f95119dd539542a43c280737a8e460)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-77271
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-23 03:17:19 JST
- 更新日: 2026-09-23 03:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MCP Atlassianにおいて、添付ファイル処理時の基準ディレクトリ指定が不十分で安全なパス検証を迂回できる脆弱性（CVE-2026-27825のバイパス）。
- 影響: 作業ディレクトリ内のPythonモジュールが上書きされ、アプリケーションの再読み込み時に任意のコードが実行される可能性があります。
- 推奨対応: MCP Atlassianをバージョン 0.22.0 以降に更新してください。

#### References
- https://github.com/sooperset/mcp-atlassian/commit/b041733473f95119dd539542a43c280737a8e460
- https://github.com/sooperset/mcp-atlassian/pull/1448
- https://github.com/sooperset/mcp-atlassian/releases/tag/v0.22.0
- https://github.com/sooperset/mcp-atlassian/security/advisories/GHSA-6vmq-24h2-pj7j

### [CVE-2026-81878](https://github.com/radareorg/radare2/commit/6727454b666b28c33837b219a5f91136461357c0)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-81878
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-09-23 01:18:02 JST
- 更新日: 2026-09-23 03:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: radare2のCPythonバイトコード（.pyc）マーシャルパーサーにおけるサイズ計算の整数オーバーフローの脆弱性。
- 影響: 作成された.pycファイルを読み込むことで、ヒープメモリの破損、サービス拒否（DoS）、または任意コード実行が発生する可能性があります。
- 推奨対応: radare2をバージョン 6.2.0 以降に更新してください。

#### References
- https://github.com/radareorg/radare2/commit/6727454b666b28c33837b219a5f91136461357c0
- https://github.com/radareorg/radare2/issues/26222
- https://github.com/radareorg/radare2/pull/26177
- https://github.com/radareorg/radare2/releases/tag/6.2.0
- https://github.com/radareorg/radare2/security/advisories/GHSA-9phv-v2w8-56j3

### [CVE-2026-85725](https://github.com/HKUDS/LightRAG/commit/89849c3ed0e0380345a6b5bade027cfb9a5bf32c)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-85725
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-09-23 02:17:27 JST
- 更新日: 2026-09-23 02:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LightRAGのverify_password処理において、平文パスワードの比較に通常の比較演算子を使用しているため、サイドチャネル（タイミング）攻撃が可能な脆弱性。
- 影響: ネットワーク上の攻撃者がログイン応答時間の違いを分析することで、設定された平文パスワードを推測・復元できる可能性があります。
- 推奨対応: LightRAGをバージョン 1.5.5 以降に更新するか、bcryptプレフィックス付きのパスワード設定を使用してください。

#### References
- https://github.com/HKUDS/LightRAG/commit/89849c3ed0e0380345a6b5bade027cfb9a5bf32c
- https://github.com/HKUDS/LightRAG/pull/3423
- https://github.com/HKUDS/LightRAG/releases/tag/v1.5.5
- https://github.com/HKUDS/LightRAG/security/advisories/GHSA-c759-cx9p-mrwq

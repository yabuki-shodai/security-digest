# Backend CVE Summary (2026-08-17)

## Overview

- 取得日時: 2026-08-17 20:43:24 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 30
- Critical: 22
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-74798](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-43jx-gxq4-jpjc)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-74798
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-17 20:16:39 JST
- 更新日: 2026-08-17 20:16:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SiYuan v3.7.4 未満の `database_clean` MCP ツールにおけるパス・トラバーサルの脆弱性。
- 影響: 認証された MCP クライアントにより、任意ファイルの読み取りおよび削除が行われる可能性があります。
- 推奨対応: SiYuan を v3.7.4 以降にアップデートしてください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-43jx-gxq4-jpjc
- https://www.vulncheck.com/advisories/siyuan-kernel-path-traversal-via-database-clean-mcp-tool

### [CVE-2026-15623](https://docs.cloud.google.com/chronicle/docs/soar/release-notes#May_23_2026)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-15623
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 16:17:12 JST
- 更新日: 2026-08-17 16:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Google Cloud SecOps (Chronicle SOAR) 6.3.85 未満のレガシーダッシュボードウィジェット API におけるブラインド SQL インジェクション。
- 影響: 認証された攻撃者が不正なパラメータを通じて意図しない SQL クエリを実行できる可能性があります。
- 推奨対応: バージョン 6.3.85 でパッチが適用されたため、利用者の追加対応は不要とされています。

#### References
- https://docs.cloud.google.com/chronicle/docs/soar/release-notes#May_23_2026

### [CVE-2026-19959](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWanTcpipSetup-34b53a41781f8047b36bd11dbcaa84dc?source=copy_link)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-19959
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 08:16:24 JST
- 更新日: 2026-08-17 08:16:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Edimax EW-7478APC 1.04 の `/goform/formWanTcpipSetup` における `pppUserName` パラメータ処理のスタックベースのバッファオーバーフロー。
- 影響: 遠隔の攻撃者により任意コードの実行や不具合が引き起こされる可能性があります（エクスプロイト公開済み）。
- 推奨対応: ベンダー未応答のため、該当インターフェースへのアクセス制限や機器の変更をご検討ください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWanTcpipSetup-34b53a41781f8047b36bd11dbcaa84dc?source=copy_link
- https://vuldb.com/cve/CVE-2026-19959
- https://vuldb.com/submit/872873
- https://vuldb.com/vuln/391136
- https://vuldb.com/vuln/391136/cti

### [CVE-2026-19961](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWlSiteSurvey-34b53a41781f804fb328d87416095401?source=copy_link)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-19961
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 08:16:25 JST
- 更新日: 2026-08-17 08:16:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Edimax EW-7478APC 1.04 の `/goform/formWlSiteSurvey` における `selSSID` パラメータ処理のバッファオーバーフロー。
- 影響: 遠隔の攻撃者により任意コードの実行等が行われる可能性があります（エクスプロイト公開済み）。
- 推奨対応: ベンダー未応答のため、信頼できないネットワークからの管理アクセスを制限してください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWlSiteSurvey-34b53a41781f804fb328d87416095401?source=copy_link
- https://vuldb.com/cve/CVE-2026-19961
- https://vuldb.com/submit/872875
- https://vuldb.com/vuln/391138
- https://vuldb.com/vuln/391138/cti

### [CVE-2026-74799](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-9cqq-p2hw-mj3f)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-74799
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 20:16:40 JST
- 更新日: 2026-08-17 20:16:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SiYuan 3.7.4 未満にて、`--mode` が `prod` 以外の場合にデバッグエンドポイント（pprof）が未認証で露出する脆弱性。
- 影響: 攻撃者にメモリダンプを参照され、AccessAuthCode や AI プロバイダーの API キーなどの機密情報が漏洩する可能性があります。
- 推奨対応: SiYuan 3.7.4 以降へ更新するか、実行モードを適切に `prod` へ設定してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-9cqq-p2hw-mj3f
- https://www.vulncheck.com/advisories/siyuan-before-unauthenticated-debug-endpoint-information-disclosure

### [CVE-2026-74868](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-phg7-xcr4-q5wg)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-74868
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 20:16:41 JST
- 更新日: 2026-08-17 20:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SiYuan 3.7.4 未満の Publish Service Basic 認証におけるレート制限およびアカウントロックアウトの欠如。
- 影響: 未認証の遠隔の攻撃者がブルートフォース攻撃を実施し、公開ノート等へ不正アクセスする可能性があります。
- 推奨対応: SiYuan 3.7.4 以降へアップデートしてください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-phg7-xcr4-q5wg
- https://www.vulncheck.com/advisories/siyuan-before-brute-force-authentication-via-publish-service

### [CVE-2026-19960](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWlbasic-34b53a41781f8097b9efd3042e977e09?source=copy_link)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-19960
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 08:16:24 JST
- 更新日: 2026-08-17 08:16:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Edimax EW-7478APC 1.04 の `/goform/formWlbasic` における `rootAPmac` パラメータのコマンドインジェクション。
- 影響: 遠隔の攻撃者により任意コマンドが実行される可能性があります（エクスプロイト公開済み）。
- 推奨対応: ベンダー未応答のため、外部からのアクセス制限等の緩和策を実施してください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-formWlbasic-34b53a41781f8097b9efd3042e977e09?source=copy_link
- https://vuldb.com/cve/CVE-2026-19960
- https://vuldb.com/submit/872874
- https://vuldb.com/vuln/391137
- https://vuldb.com/vuln/391137/cti

### [CVE-2026-19962](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-setWAN-34b53a41781f808aaf2bc972cc6d38d3?source=copy_link)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-19962
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 09:16:26 JST
- 更新日: 2026-08-17 09:16:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Edimax EW-7478APC 1.04 の `/goform/setWAN` における各種ユーザー名パラメータのコマンドインジェクション。
- 影響: 遠隔からの操作により任意コマンドが実行される可能性があります（エクスプロイト公開済み）。
- 推奨対応: ベンダー未応答のため、機器のネットワーク隔離や代替品への移行をご検討ください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-setWAN-34b53a41781f808aaf2bc972cc6d38d3?source=copy_link
- https://vuldb.com/cve/CVE-2026-19962
- https://vuldb.com/submit/872876
- https://vuldb.com/vuln/391139
- https://vuldb.com/vuln/391139/cti

### [CVE-2026-19963](https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-stainfo-34b53a41781f80ed8e15c109f7a50844?source=copy_link)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-19963
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 09:16:27 JST
- 更新日: 2026-08-17 09:16:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Edimax EW-7478APC 1.04 の `/goform/stainfo` における `interface` パラメータのコマンドインジェクション。
- 影響: 遠隔の攻撃者により任意コマンドが実行される可能性があります（エクスプロイト公開済み）。
- 推奨対応: ベンダー未応答のため、該当管理機能へのアクセスを制限してください。

#### References
- https://lavender-bicycle-a5a.notion.site/EDIMAX-EW-7478APC-stainfo-34b53a41781f80ed8e15c109f7a50844?source=copy_link
- https://vuldb.com/cve/CVE-2026-19963
- https://vuldb.com/submit/872877
- https://vuldb.com/vuln/391140
- https://vuldb.com/vuln/391140/cti

### [CVE-2026-19956](https://github.com/gomarble-ai/facebook-ads-mcp-server/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-19956
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-17 06:16:37 JST
- 更新日: 2026-08-17 06:16:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: gomarble-ai facebook-ads-mcp-server 0.1.0 の `fetch_pagination_url` 関数における SSRF の脆弱性。
- 影響: 遠隔の攻撃者がサーバーを介して不審な外部リクエストや内部ネットワークへのリクエストを送信できる可能性があります。
- 推奨対応: 提示されている修正パッチ（コミット `4e53875aa22e8991c2fa4a7660d86e1caba66659`）を適用してください。

#### References
- https://github.com/gomarble-ai/facebook-ads-mcp-server/
- https://github.com/gomarble-ai/facebook-ads-mcp-server/commit/4e53875aa22e8991c2fa4a7660d86e1caba66659
- https://github.com/gomarble-ai/facebook-ads-mcp-server/issues/29
- https://github.com/gomarble-ai/facebook-ads-mcp-server/pull/32
- https://vuldb.com/cve/CVE-2026-19956

### [CVE-2026-19978](https://github.com/jiantao88/android-mcp-server/)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-19978
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-17 13:16:54 JST
- 更新日: 2026-08-17 13:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw has been found in jiantao88 android-mcp-server up to cfb872b2446794193b58edd63f4dbf6af48a6292. The impacted element is the function child_process.exec of the file build/index.js of the component Command Execution. Executing a manipulation of the argument deviceId/packageName/permission/extras[].key/extras[].valu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jiantao88/android-mcp-server/
- https://github.com/jiantao88/android-mcp-server/commit/14e2bf27c88ba137e35cbb0c2a75f72b595bb98a
- https://github.com/jiantao88/android-mcp-server/issues/1
- https://vuldb.com/cve/CVE-2026-19978
- https://vuldb.com/submit/873898

### [CVE-2026-74895](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-623h-chj7-hfx8)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74895
- 関連キーワード: python, gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:44 JST
- 更新日: 2026-08-17 20:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 fail to apply sandbox restrictions in the default process isolation mode for plugin execution. Attackers can execute malicious plugins with unrestricted access to the filesystem, network, subprocess execution, and all Python modules.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-623h-chj7-hfx8
- https://www.vulncheck.com/advisories/openssl-encrypt-before-plugin-sandbox-bypass-via-process-isolation

### [CVE-2026-74899](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-m25m-ggxg-239c)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74899
- 関連キーワード: python, gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:44 JST
- 更新日: 2026-08-17 20:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a sandbox escape vulnerability in IsolatedPluginExecutor that exposes Python type objects in restricted exec() builtins. Attackers can traverse the Python class hierarchy via __class__.__mro__.__subclasses__() to access system functions and execute arbitrary OS commands.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-m25m-ggxg-239c
- https://www.vulncheck.com/advisories/openssl-encrypt-before-sandbox-escape-via-type-hierarchy

### [CVE-2026-74887](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-cx72-m6xj-3vf6)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-74887
- 関連キーワード: python, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:43 JST
- 更新日: 2026-08-17 20:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt before 1.4.0 imports Python's non-cryptographic 'random' module (Mersenne Twister PRNG) at line 15 of openssl_encrypt/modules/pqc.py. No direct calls to random.* were present in the code, so no cryptographic operation is currently affected; however, the import creates a hazard that future code could ina...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-cx72-m6xj-3vf6
- https://www.vulncheck.com/advisories/openssl-encrypt-before-insecure-random-import-in-pqc-module

### [CVE-2026-74874](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-vfgx-5q85-58q3)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-74874
- 関連キーワード: python, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:41 JST
- 更新日: 2026-08-17 20:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 use Python's non-cryptographic random module for steganographic pixel selection in the generate_pseudorandom_sequence function. Attackers who know the password can recover the Mersenne Twister state from approximately 624 outputs and predict pixel locations containing hidden data f...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-vfgx-5q85-58q3
- https://www.vulncheck.com/advisories/openssl-encrypt-before-weak-prng-steganography-pixel-selection

### [CVE-2026-19964](http://github.com/Jij-Inc/Jij-MCP-Server/issues/4)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-19964
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-17 09:16:27 JST
- 更新日: 2026-08-17 09:16:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was found in Jij-Inc Jij-MCP-Server 0.1.0. This affects the function PythonREPL.run of the file jij_mcp/python_repr.py of the component jm_check. The manipulation of the argument code results in code injection. It is possible to launch the attack remotely. The exploit has been made public and could be u...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- http://github.com/Jij-Inc/Jij-MCP-Server/issues/4
- https://vuldb.com/cve/CVE-2026-19964
- https://vuldb.com/submit/872906
- https://vuldb.com/vuln/391141
- https://vuldb.com/vuln/391141/cti

### [CVE-2026-74891](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-v4vm-4xf2-fhqj)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74891
- 関連キーワード: postgresql, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:44 JST
- 更新日: 2026-08-17 20:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain hardcoded database credentials in standalone server configuration files. Attackers on the same network can access PostgreSQL databases using well-known default credentials to retrieve sensitive data.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-v4vm-4xf2-fhqj
- https://www.vulncheck.com/advisories/openssl-encrypt-before-hardcoded-database-credentials

### [CVE-2026-74894](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-4g2c-wpgj-49w8)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74894
- 関連キーワード: gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:44 JST
- 更新日: 2026-08-17 20:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt before 1.4.0 contains an authentication bypass vulnerability in the verify_api_token function that accepts any non-empty Bearer token string without validation. Attackers can upload arbitrary public keys, enumerate all keys, and revoke keys belonging to any user by providing any Bearer token in the Auth...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-4g2c-wpgj-49w8
- https://www.vulncheck.com/advisories/openssl-encrypt-before-authentication-bypass-via-bearer-token

### [CVE-2026-74878](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-h45m-mgcp-q388)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74878
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:42 JST
- 更新日: 2026-08-17 20:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 use an in-memory rate limiter for TOTP brute-force protection that is not shared across workers and is lost on server restart. Attackers can distribute authentication attempts across multiple server instances or retry immediately after a restart to bypass rate limiting protections.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-h45m-mgcp-q388
- https://www.vulncheck.com/advisories/openssl-encrypt-before-totp-rate-limiter-bypass

### [CVE-2026-74890](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-rvc2-5jxq-gpcj)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-74890
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:43 JST
- 更新日: 2026-08-17 20:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain an authentication bypass vulnerability in CamelliaCipher that disables HMAC tag generation and verification when the PYTEST_CURRENT_TEST environment variable is set. Attackers with code execution can set this environment variable to produce unauthenticated ciphertext and by...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-rvc2-5jxq-gpcj
- https://www.vulncheck.com/advisories/openssl-encrypt-before-hmac-authentication-bypass-via-environment-variable

### [CVE-2026-74901](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-w4j7-wfgw-r52w)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74901
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:45 JST
- 更新日: 2026-08-17 20:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain an authentication bypass vulnerability in pqc.py where AES-GCM decryption failures trigger fallback to unauthenticated AES-CTR mode. Attackers can modify ciphertext in transit to bypass integrity verification and perform bit-flipping attacks without detection.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-w4j7-wfgw-r52w
- https://www.vulncheck.com/advisories/openssl-encrypt-before-authentication-bypass-via-aes-ctr-fallback

### [CVE-2026-74885](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-43r4-3hf9-m84q)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-74885
- 関連キーワード: gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:43 JST
- 更新日: 2026-08-17 20:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a logging bug in restore_hidden_modules() that logs module counts after clearing, always showing zero restored modules and corrupting audit trails. Additionally, a race condition exists between module hiding and import hook installation where another thread could re-import...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-43r4-3hf9-m84q
- https://www.vulncheck.com/advisories/openssl-encrypt-before-logging-bug-and-race-condition

### [CVE-2026-74886](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-9pgj-v69p-q586)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74886
- 関連キーワード: gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:43 JST
- 更新日: 2026-08-17 20:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a plugin sandbox bypass vulnerability where the PluginImportGuard blocks a different set of modules than the AST analyzer's DANGEROUS_MODULES set. Attackers can bypass AST analysis through string obfuscation or encoding to import unblocked dangerous modules like sys, shutil...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-9pgj-v69p-q586
- https://www.vulncheck.com/advisories/openssl-encrypt-before-plugin-import-guard-bypass

### [CVE-2026-74896](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-w7gr-9g4g-33mx)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74896
- 関連キーワード: gin, openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:44 JST
- 更新日: 2026-08-17 20:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a sandbox escape vulnerability in the DangerousPatternVisitor AST analyzer that fails to detect dunder attribute traversal techniques. Attackers can use __class__, __bases__, __subclasses__(), and __globals__ chains to access restricted functions and execute arbitrary syste...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-w7gr-9g4g-33mx
- https://www.vulncheck.com/advisories/openssl-encrypt-before-sandbox-escape-via-dunder-attribute-traversal

### [CVE-2026-74872](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-j48q-4c78-rhf9)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74872
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:41 JST
- 更新日: 2026-08-17 20:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain an arbitrary code execution vulnerability in the Whirlpool hash implementation that uses broad glob patterns to load .so modules without integrity verification. Attackers can place malicious .so files matching the whirlpool*py313*.so pattern in site-packages directories to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-j48q-4c78-rhf9
- https://www.vulncheck.com/advisories/openssl-encrypt-before-arbitrary-code-execution-via-whirlpool

### [CVE-2026-74875](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-425g-fjhq-5h92)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74875
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:41 JST
- 更新日: 2026-08-17 20:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 silently skip JSON schema validation when the jsonschema library is not installed, allowing malformed metadata to be accepted. Attackers can remove the jsonschema package or supply unknown metadata format versions to bypass all schema checks and process malicious data.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-425g-fjhq-5h92
- https://www.vulncheck.com/advisories/openssl-encrypt-before-schema-validation-bypass

### [CVE-2026-74876](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-8h88-gxp3-j7pg)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74876
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:42 JST
- 更新日: 2026-08-17 20:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a vulnerability in PublicKeyBundle.from_dict() that creates key bundles from untrusted data without verifying signatures. Attackers can call from_dict() followed by to_identity() without signature verification to encrypt data using attacker-controlled public keys, leaking s...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-8h88-gxp3-j7pg
- https://www.vulncheck.com/advisories/openssl-encrypt-before-unverified-key-bundle-encryption

### [CVE-2026-74880](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-4rh7-jwg9-m28m)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74880
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:42 JST
- 更新日: 2026-08-17 20:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 accept refresh tokens as URL query parameters in keyserver and telemetry server routes. Attackers can extract tokens from server logs, proxy logs, browser history, and HTTP Referer headers to gain unauthorized access.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-4rh7-jwg9-m28m
- https://www.vulncheck.com/advisories/openssl-encrypt-before-token-leakage-via-query-parameters

### [CVE-2026-74889](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-j9mh-57cc-665x)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74889
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:43 JST
- 更新日: 2026-08-17 20:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 use HKDF with no salt and static info parameter in key normalization functions, reducing entropy extraction and determinism. Attackers can exploit predictable key derivation with identical inputs to weaken cryptographic security against multi-target attacks.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-j9mh-57cc-665x
- https://www.vulncheck.com/advisories/openssl-encrypt-before-weak-key-derivation-via-hkdf

### [CVE-2026-74900](https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-p3gq-pcg9-qvfv)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-74900
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-08-17 20:16:45 JST
- 更新日: 2026-08-17 20:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openssl_encrypt versions before 1.4.0 contain a critical vulnerability in pqc.py where KEM decapsulation failures silently fall back to simulation mode, generating a deterministic shared secret from only 16 bytes of the private key and publicly available encapsulated key data. Attackers who obtain 16 bytes of the priva...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jahlives/openssl_encrypt/security/advisories/GHSA-p3gq-pcg9-qvfv
- https://www.vulncheck.com/advisories/openssl-encrypt-before-weak-shared-secret-via-pqc-simulation-mode

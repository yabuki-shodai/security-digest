# Backend CVE Summary (2026-07-24)

## Overview

- 取得日時: 2026-07-24 08:08:25 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 23
- Critical: 8
- High: 8
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-47724](https://github.com/forgekeep/nebula-mesh/commit/9d8bcd7667ecd0c2975cc71fb35a02fe131f76f2)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-47724
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-24 06:17:04 JST
- 更新日: 2026-07-24 06:17:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: nebula-mesh is a self-hosted control plane for Slack Nebula mesh virtual private network. Prior to version 0.3.4, the `/api/v1/*` route surface trusts the bearer token alone for authorisation on most endpoints. The codebase itself admits this at `internal/api/hosts.go:384`: "API trusts the bearer token for authorisatio...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/forgekeep/nebula-mesh/commit/9d8bcd7667ecd0c2975cc71fb35a02fe131f76f2
- https://github.com/forgekeep/nebula-mesh/security/advisories/GHSA-598g-h2vc-h5vg

### [CVE-2026-65604](https://github.com/zalando/skipper/security/advisories/GHSA-8qqm-fp2q-v734)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-65604
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-24 07:16:53 JST
- 更新日: 2026-07-24 07:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Skipper contains an incomplete fix for CVE-2026-50197 in which oversized request bodies bypass Open Policy Agent (OPA) deny-on-presence Rego policies. When a request body exceeds the configured maxBodyBytes limit, Skipper forwards the full payload to the upstream service while OPA evaluates against an empty parsed_body...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zalando/skipper/security/advisories/GHSA-8qqm-fp2q-v734
- https://www.vulncheck.com/advisories/skipper-incomplete-fix-for-cve-2026-50197-policy-bypass

### [CVE-2026-47722](https://github.com/forgekeep/nebula-mesh/commit/c1506f7344ab375a145a7449b193af3f19bb41ef)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-47722
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-24 05:17:08 JST
- 更新日: 2026-07-24 05:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: nebula-meshの0.3.2未満のバージョンで、ユーザー入力の`ListenHost`と`TunDevice`が適切に検証されず、テンプレートに直接埋め込まれる脆弱性が存在します。  
- 影響: 悪意ある入力により設定ファイル生成時に予期しない動作や情報漏洩のリスクがある可能性があります。  
- 推奨対応: バージョン0.3.2以降にアップデートし、入力値の検証が適切に行われるようにしてください。

#### References
- https://github.com/forgekeep/nebula-mesh/commit/c1506f7344ab375a145a7449b193af3f19bb41ef
- https://github.com/forgekeep/nebula-mesh/issues/126
- https://github.com/forgekeep/nebula-mesh/security/advisories/GHSA-7hp6-g3pq-3pc3

### [CVE-2026-50103](https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-06)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-50103
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-24 06:17:05 JST
- 更新日: 2026-07-24 06:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A NULL pointer dereference in the L2 GOOSE and R-GOOSE shared parser, which may allow a network-adjacent attacker to crash a subscribing application by sending a crafted GOOSE frame containing a malformed TLV value.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-204-06

### [CVE-2026-48530](https://gfi.ai/products-and-solutions/network-security-solutions/archiver/resources/documentation/product-releases)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-48530
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-24 01:17:25 JST
- 更新日: 2026-07-24 02:55:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: GFI Archiver 15.13未満において、認証済み攻撃者が分類ルールの設定画面で任意のスクリプトを注入可能な保存型クロスサイトスクリプティング脆弱性が存在します。  
- 影響: 攻撃者が注入したスクリプトが他ユーザーのブラウザで実行され、情報漏洩やセッション乗っ取りのリスクがあります。  
- 推奨対応: 可能な限り速やかにGFI Archiverをバージョン15.13以降にアップデートし、入力値の適切なエンコードを確認してください。

#### References
- https://gfi.ai/products-and-solutions/network-security-solutions/archiver/resources/documentation/product-releases
- https://www.vulncheck.com/advisories/gfi-archiver-stored-xss-via-categorizationpolicywizard-aspx

### [CVE-2026-16804](https://chromereleases.googleblog.com/2026/07/stable-channel-update-for-desktop_01320465736.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-16804
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-24 07:16:52 JST
- 更新日: 2026-07-24 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Use after free in Input in Google Chrome prior to 150.0.7871.186 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/07/stable-channel-update-for-desktop_01320465736.html
- https://issues.chromium.org/issues/524721670

### [CVE-2026-16805](https://chromereleases.googleblog.com/2026/07/stable-channel-update-for-desktop_01320465736.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-16805
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-24 07:16:52 JST
- 更新日: 2026-07-24 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Google ChromeのBlinkコンポーネントにおけるUse after freeの脆弱性で、細工されたHTMLページを通じてリモートから任意のコード実行が可能になる可能性があります。  
- 影響: 任意のコードがサンドボックス内で実行されるリスクがあり、ブラウザの安全性が損なわれる恐れがあります。  
- 推奨対応: 影響を受けるバージョンのChromeを最新バージョン（150.0.7871.186以降）にアップデートしてください。

#### References
- https://chromereleases.googleblog.com/2026/07/stable-channel-update-for-desktop_01320465736.html
- https://issues.chromium.org/issues/523292588

### [CVE-2026-16806](https://chromereleases.googleblog.com/2026/07/stable-channel-update-for-desktop_01320465736.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-16806
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-24 07:16:52 JST
- 更新日: 2026-07-24 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Use after free in WebMCP in Google Chrome prior to 150.0.7871.186 allowed a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/07/stable-channel-update-for-desktop_01320465736.html
- https://issues.chromium.org/issues/522064153

### [CVE-2026-16807](https://chromereleases.googleblog.com/2026/07/stable-channel-update-for-desktop_01320465736.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-16807
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-24 07:16:52 JST
- 更新日: 2026-07-24 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Out of bounds write in Codecs in Google Chrome prior to 150.0.7871.186 allowed a remote attacker to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/07/stable-channel-update-for-desktop_01320465736.html
- https://issues.chromium.org/issues/518237034

### [CVE-2026-16796](https://aws.amazon.com/security/security-bulletins/2026-065-aws/)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-16796
- 関連キーワード: python, aws
- 影響製品: -
- 公開日: 2026-07-24 06:17:03 JST
- 更新日: 2026-07-24 06:17:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: AWS Bedrock AgentCore Python SDKのinstall_packages()メソッドで引数区切り文字の不適切な無害化により、認証済みのリモートユーザーがCode Interpreterサンドボックス内で任意のコマンドを実行できる可能性があります。  
- 影響: 悪意のあるパッケージ名引数を用いたコマンドインジェクションにより、システムの制御が奪われるリスクがあります。  
- 推奨対応: SDKをバージョン1.18.1以降にアップグレードし、脆弱性の修正を適用してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-065-aws/
- https://github.com/aws/bedrock-agentcore-sdk-python/security/advisories/GHSA-j6g5-3hh3-pgw8
- https://pypi.org/project/bedrock-agentcore/1.18.1/

### [CVE-2026-47669](https://github.com/dbgate/dbgate/releases/tag/v7.1.9)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-47669
- 関連キーワード: gin, docker
- 影響製品: -
- 公開日: 2026-07-24 05:17:08 JST
- 更新日: 2026-07-24 05:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: DbGateの7.1.8以前のバージョンで、ZIP解凍時にファイルパスの検証が不十分なため、任意の場所にファイルを書き込める脆弱性が存在します。  
- 影響: 悪意あるZIPファイルにより、権限の高いユーザーとして任意のファイルを上書きされる可能性があり、特にDocker環境でroot権限で動作している場合は深刻です。  
- 推奨対応: バージョン7.1.9以降にアップデートし、信頼できないZIPファイルの取り扱いを避けることを推奨します。

#### References
- https://github.com/dbgate/dbgate/releases/tag/v7.1.9
- https://github.com/dbgate/dbgate/security/advisories/GHSA-h535-j5hr-mv56

### [CVE-2026-47752](https://github.com/Quenary/tugtainer/security/advisories/GHSA-g2cj-2x47-78vq)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-47752
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-07-24 03:16:53 JST
- 更新日: 2026-07-24 03:23:01 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Tugtainer is a self-hosted app for automating updates of Docker containers. Versions prior to 1.30.2 are vulnerable to Server-Side Template Injection (SSTI) in the notification template feature. The `title_template` and `body_template` fields are rendered using an unsandboxed `jinja2.Environment`, allowing any authenti...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Quenary/tugtainer/security/advisories/GHSA-g2cj-2x47-78vq
- https://github.com/Quenary/tugtainer/security/advisories/GHSA-g2cj-2x47-78vq

### [CVE-2026-16763](https://github.com/localstack/serverless-localstack/)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-16763
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-07-24 07:16:51 JST
- 更新日: 2026-07-24 07:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: localstack serverless-localstack 1.4.0以前のsrc/index.js内のConfiguration Handlerで、custom.localstack.docker.compose_file引数の操作によりOSコマンドインジェクションの脆弱性が存在します。  
- 影響: ローカル環境での攻撃が可能で、悪用されると任意のOSコマンドが実行される恐れがあります。  
- 推奨対応: 公式の修正対応を待つか、該当引数の入力値を厳密に検証し、信頼できる環境でのみ使用してください。

#### References
- https://github.com/localstack/serverless-localstack/
- https://github.com/localstack/serverless-localstack/issues/303
- https://vuldb.com/cve/CVE-2026-16763
- https://vuldb.com/submit/861028
- https://vuldb.com/vuln/382620

### [CVE-2026-16584](https://aws.amazon.com/security/security-bulletins/2026-063-aws/)

> **Backend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-16584
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-07-24 01:17:15 JST
- 更新日: 2026-07-24 04:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Improper handling of an initialization failure in AWS API MCP Server from 0.2.13 through 1.3.46 might allow an actor to bypass the user-configured security policy and execute AWS API operations that the policy was set to deny or gate. When initialization of the security policy enforcement data fails at server startup,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-063-aws/
- https://github.com/awslabs/mcp/security/advisories/GHSA-29w2-fq35-v728
- https://pypi.org/project/awslabs.aws-api-mcp-server/1.3.47/

### [CVE-2026-16756](https://aws.amazon.com/security/security-bulletins/2026-064-aws/)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-16756
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-07-24 04:16:53 JST
- 更新日: 2026-07-24 05:17:07 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Amazonのaws-smithy-http-serverのデフォルトのserve()パスにおいて、接続およびヘッダー読み取りのタイムアウト設定がなく、同時接続数の制限もないため、リモート攻撃者が多数の接続を開き部分的なリクエストを送信してサービス拒否を引き起こす可能性があります。  
- 影響: サーバーのソケットやタスクが枯渇し、サービス拒否（DoS）状態になるリスクがあります。  
- 推奨対応: aws-smithy-http-serverをバージョン0.66.5以降にアップグレードすることを推奨します。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-064-aws/
- https://crates.io/crates/aws-smithy-http-server/0.66.5
- https://github.com/smithy-lang/smithy-rs/security/advisories/GHSA-jvxp-qmx7-gjpx

### [CVE-2026-47769](https://github.com/Work90210/APIFold/commit/7f19b52280f414f57af2b79a95333d1c8fbeece5)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-47769
- 関連キーワード: postgresql, redis
- 影響製品: -
- 公開日: 2026-07-24 03:16:53 JST
- 更新日: 2026-07-24 04:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: APIFoldの特定エンドポイントが認証なしで任意のJSONを受け入れ、RedisやPostgreSQLに保存してしまう問題がありました。  
- 影響: 認証されていない攻撃者が有効なサーバースラッグを知っていれば、任意のペイロードを注入可能で、正規クライアントに偽のデータを提供する恐れがあります。  
- 推奨対応: 最新の修正コミット（7f19b52280f414f57af2b79a95333d1c8fbeece5）を適用し、署名検証を有効にしてください。

#### References
- https://github.com/Work90210/APIFold/commit/7f19b52280f414f57af2b79a95333d1c8fbeece5
- https://github.com/Work90210/APIFold/pull/235
- https://github.com/Work90210/APIFold/security/advisories/GHSA-x82h-9r8v-m672

### [CVE-2026-15981](https://plugins.trac.wordpress.org/browser/miniorange-saml-20-single-sign-on/tags/5.4.4/class-mo-saml-login-validate.php#L118)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-15981
- 関連キーワード: gin, openssl
- 影響製品: -
- 公開日: 2026-07-24 06:17:03 JST
- 更新日: 2026-07-24 06:17:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The SAML Single Sign On – SSO Login plugin for WordPress is vulnerable to Authentication Bypass in all versions up to, and including, 5.4.4. This is due to the mo_saml_validate_signature() function performing a loose boolean check on the raw tri-state integer returned by PHP's openssl_verify(), causing an error return...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://plugins.trac.wordpress.org/browser/miniorange-saml-20-single-sign-on/tags/5.4.4/class-mo-saml-login-validate.php#L118
- https://plugins.trac.wordpress.org/browser/miniorange-saml-20-single-sign-on/tags/5.4.4/class-mo-saml-login-validate.php#L541
- https://plugins.trac.wordpress.org/browser/miniorange-saml-20-single-sign-on/tags/5.4.4/class-mo-saml-utilities.php#L403
- https://plugins.trac.wordpress.org/browser/miniorange-saml-20-single-sign-on/tags/5.4.4/includes/lib/SAML2Core/class-mo-saml-xml-security-dsig.php#L938
- https://plugins.trac.wordpress.org/browser/miniorange-saml-20-single-sign-on/tags/5.4.4/includes/lib/SAML2Core/class-mo-saml-xml-security-key.php#L621

### [CVE-2026-6516](https://www.manageengine.com/products/active-directory-audit/cve-2026-6516.html)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-6516
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-24 03:17:02 JST
- 更新日: 2026-07-24 05:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Zohocorp ManageEngine ADAudit Plus versions before 8606 are affected by Unauthenticated Remote code execution due to the vulnerable agent API.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.manageengine.com/products/active-directory-audit/cve-2026-6516.html

### [CVE-2026-63359](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-204-01.json)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-63359
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-24 05:17:20 JST
- 更新日: 2026-07-24 05:17:20 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The Appriss Insights (Equifax) Victim Information Notification Exchange (VINE) applications allow an unauthenticated attacker to send a specially-crafted request to bypass the login page, access other users' credentials, take over other user accounts, access sensitive PII, and dump other information from the database.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-204-01.json
- https://www.cve.org/CVERecord?id=CVE-2026-63359

### [CVE-2026-63732](https://github.com/decolua/9router/security/advisories/GHSA-4922-8r65-fq26)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-63732
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-24 07:16:53 JST
- 更新日: 2026-07-24 07:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 9router 0.4.59 (fixed in 0.4.60) contains a chain of vulnerabilities: a hardcoded default password (123456) that authenticates any fresh installation, a bypass of the LOCAL_ONLY network gate via a spoofed Host header, and unvalidated arguments passed to child_process.spawn() when registering MCP plugins. A remote, unau...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/decolua/9router/security/advisories/GHSA-4922-8r65-fq26
- https://www.vulncheck.com/advisories/9router-before-remote-code-execution-via-default-password

### [CVE-2026-65701](https://github.com/geo-chen/oss/blob/main/so-vits-svc.md)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-65701
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-24 03:17:01 JST
- 更新日: 2026-07-24 04:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SoftVC VITS Singing Voice Conversion through commit 730930d contains a path traversal vulnerability in the full-song inference server that allows unauthenticated remote attackers to read and exfiltrate arbitrary files by supplying attacker-controlled filesystem paths through the audio_path field of an unauthenticated P...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/geo-chen/oss/blob/main/so-vits-svc.md
- https://www.vulncheck.com/advisories/softvc-vits-singing-voice-conversion-path-traversal-via-wav2wav-flask-route

### [CVE-2026-47743](https://github.com/shopperlabs/shopper/pull/511)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-47743
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-24 03:16:53 JST
- 更新日: 2026-07-24 04:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Shopper is a Headless e-commerce Admin Panel. Prior to 2.8.0, three related defects on admin Livewire components allowed data tampering, sensitive data disclosure, and stored XSS. First, several Livewire components in the admin panel exposed Eloquent model identifiers as public properties without the `#[Locked]` attrib...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/shopperlabs/shopper/pull/511
- https://github.com/shopperlabs/shopper/security/advisories/GHSA-hr9v-r8r2-hg7j

### [CVE-2026-15212](https://plugins.trac.wordpress.org/browser/wpo365-login/tags/43.2/Services/Ajax_Service.php#L805)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-15212
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-24 05:17:07 JST
- 更新日: 2026-07-24 05:17:07 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The WPO365 | Login plugin for WordPress is vulnerable to Cross-Site Request Forgery in versions up to, and including, 43.2. This is due to the Ajax_Service::verify_ajax_request() helper gating its wp_verify_nonce() call behind the boolean option 'enable_nonce_check', which is absent from the default 'wpo365_options' ar...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://plugins.trac.wordpress.org/browser/wpo365-login/tags/43.2/Services/Ajax_Service.php#L805
- https://plugins.trac.wordpress.org/changeset/3610759/wpo365-login
- https://www.wordfence.com/threat-intel/vulnerabilities/id/51d0ba58-614e-4284-ae0b-b0b76fc5c46d?source=cve

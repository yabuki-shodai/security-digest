# Backend CVE Summary (2026-09-10)

## Overview

- 取得日時: 2026-09-10 09:08:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 22
- Critical: 4
- High: 10
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-15913](https://www.fortra.com/security/advisories/product-security/fi-2026-011)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-15913
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-10 07:17:11 JST
- 更新日: 2026-09-10 07:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In versions prior to 7.10.2 a path traversal vulnerability in the /attachRemoteFiles endpoint of Fortra's GoAnywhere MFT allows Web Users with both Secure Folders and Secure Mail permissions to escape their sandboxed home directory, achieving arbitrary file read.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.fortra.com/security/advisories/product-security/fi-2026-011

### [CVE-2026-87011](https://github.com/open-webui/open-webui/commit/aeda6ff13a25d3b3ba1b303609f35382db22142c)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-87011
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-10 06:17:05 JST
- 更新日: 2026-09-10 06:17:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open WebUI is an extensible, feature-rich, and user-friendly self-hosted AI platform. From 0.9.0 until 0.11.1, the unauthenticated POST /oauth/backchannel-logout handler in backend/open_webui/utils/oauth.py fetched the OIDC discovery document and signing keys before validating a submitted logout token. Each request rep...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/open-webui/open-webui/commit/aeda6ff13a25d3b3ba1b303609f35382db22142c
- https://github.com/open-webui/open-webui/releases/tag/v0.11.1
- https://github.com/open-webui/open-webui/security/advisories/GHSA-3g9q-v48f-hh9w

### [CVE-2026-87921](https://github.com/Rizwan17/inventory-management-system/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-87921
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-10 07:18:47 JST
- 更新日: 2026-09-10 07:18:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was identified in Rizwan17 inventory-management-system up to bfe78a330d01bb26b9daec5dc9ecd5c77900e03f. Affected is the function update_record of the file includes/manage.php. The manipulation of the argument update_category/cid/update_brand/update_product leads to sql injection. The attack is possible t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Rizwan17/inventory-management-system/
- https://github.com/Rizwan17/inventory-management-system/issues/9
- https://vuldb.com/cve/CVE-2026-87921
- https://vuldb.com/submit/911127
- https://vuldb.com/vuln/401808

### [CVE-2026-87922](https://github.com/Rizwan17/inventory-management-system/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-87922
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-10 07:18:47 JST
- 更新日: 2026-09-10 07:18:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Rizwan17 inventory-management-systemのincludes/process.phpにおけるuserid処理の認証不備。
- 影響: リモートの攻撃者により、認証を回避してカテゴリの追加などの不正な操作が行われる可能性があります。
- 推奨対応: 開発者による公式な修正対応が完了していないため、該当コードの手動修正やアクセス制限、または安全な代替製品の利用を検討してください。

#### References
- https://github.com/Rizwan17/inventory-management-system/
- https://github.com/Rizwan17/inventory-management-system/issues/10
- https://vuldb.com/cve/CVE-2026-87922
- https://vuldb.com/submit/911128
- https://vuldb.com/vuln/401809

### [CVE-2026-80920](https://git.kernel.org/stable/c/40b6ccf68731809ceb85c6e9f0f8f2ed61c7aa5a)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80920
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-10 02:17:47 JST
- 更新日: 2026-09-10 02:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのio_uringにおいて、ウェイクアップハンドラからのeventfd通知処理時に発生する再帰呼び出しに関する不具合。
- 影響: 特定条件下（DEFER_TASKRUN）で不正なロック処理が発生し、システムパフォーマンス低下やクラッシュの原因となる可能性があります。
- 推奨対応: 修正パッチが適用された最新のLinuxカーネルに更新してください。

#### References
- https://git.kernel.org/stable/c/40b6ccf68731809ceb85c6e9f0f8f2ed61c7aa5a
- https://git.kernel.org/stable/c/b6bb334b0e9348887e3e55e1f494b0c3b8fbf59f
- https://git.kernel.org/stable/c/cd305ee3633a45fcf5f3a5d83f99f3cb77d87b6e
- https://git.kernel.org/stable/c/e22f4494cc9487d326e5e3067f33dea7c1e442b2

### [CVE-2026-87923](https://github.com/Rizwan17/inventory-management-system/)

> **Backend** / **MEDIUM** / CVSS: **5.0** / KEV: **no**

- タイトル: CVE-2026-87923
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-10 08:16:56 JST
- 更新日: 2026-09-10 08:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Rizwan17 inventory-management-systemのincludes/DBOperation.phpにおけるクロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 攻撃者によって送信された悪意あるスクリプトがユーザーのブラウザ上で実行され、セッション強奪や情報漏洩が発生する可能性があります。
- 推奨対応: 公式パッチが未提供のため、入力値の検証およびエスケープ処理を独自に実装するか、安全な代替ソフトウェアへの移行を検討してください。

#### References
- https://github.com/Rizwan17/inventory-management-system/
- https://github.com/Rizwan17/inventory-management-system/issues/12
- https://vuldb.com/cve/CVE-2026-87923
- https://vuldb.com/submit/911129
- https://vuldb.com/vuln/401810

### [CVE-2026-80917](https://git.kernel.org/stable/c/008cb88edb41f3c7c8e0ed763ff9f26719830984)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80917
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-10 02:17:46 JST
- 更新日: 2026-09-10 02:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルの32ビットCAMシステムにおいて、pci-host-cam-generic使用時に発生するNULLポインタ参照の脆弱性。
- 影響: PCIバスの列挙処理時にカーネルがクラッシュ（Oops）し、システムが停止する可能性があります。
- 推奨対応: 修正されたバージョン以降のLinuxカーネルへアップデートしてください。

#### References
- https://git.kernel.org/stable/c/008cb88edb41f3c7c8e0ed763ff9f26719830984
- https://git.kernel.org/stable/c/0916948026f623844acd08888f7cbedbf1c48d6b
- https://git.kernel.org/stable/c/0c55707bd5d0d7670704cfd0dda933809b052f67
- https://git.kernel.org/stable/c/5e52eb0290f66ba0732956dcb1e365b5ca3c5108
- https://git.kernel.org/stable/c/74456843f18ba7f3045974d7e8b88ab993152b8c

### [CVE-2026-80919](https://git.kernel.org/stable/c/4e9b4dee0777ec9c835a4746e2d30382dd9d1044)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80919
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-10 02:17:47 JST
- 更新日: 2026-09-10 02:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのamdgpuドライバーにおけるamdgpu_devcoredump_format処理内の再帰的ww_mutex取得によるロック検出問題。
- 影響: GPUエラーダンプ時に潜在的なデッドロックが発生し、システムが応答停止する可能性があります。
- 推奨対応: 修正パッチが含まれるLinuxカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/4e9b4dee0777ec9c835a4746e2d30382dd9d1044
- https://git.kernel.org/stable/c/7152b248dc3c8d5fa8629e99ed5655dd41b51562

### [CVE-2026-87874](https://access.redhat.com/security/cve/CVE-2026-87874)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-87874
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-09-10 02:17:53 JST
- 更新日: 2026-09-10 05:13:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Ansible community.generalコレクションのmemcachedキャッシュプラグインにおける不安全なデシリアライズ（pickle）の脆弱性。
- 影響: memcachedへのアクセス権を持つ攻撃者により改ざんされたキャッシュデータが配置され、Ansibleコントローラー上で任意のコードが実行される可能性があります。
- 推奨対応: community.generalコレクションを修正済みバージョンへアップデートし、memcachedインスタンスへのネットワークアクセスを適切に制限してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-87874
- https://bugzilla.redhat.com/show_bug.cgi?id=2530995

### [CVE-2026-87999](https://github.com/open-webui/open-webui/commit/e3e4bd87df6fc629e7e22081d980d55a7632b8b7)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-87999
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-10 07:18:48 JST
- 更新日: 2026-09-10 07:18:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open WebUI (0.11.1未満)におけるIPアドレス検証の不備に起因するサーバーサイドリクエストフォージェリ（SSRF）の脆弱性。
- 影響: 認証されたユーザーが内部リソース（Azureプラットフォームチャネル 168.63.129.16 等）にリクエストを送信し、データを入手できる可能性があります。
- 推奨対応: Open WebUI をバージョン 0.11.1 以降にアップデートしてください。

#### References
- https://github.com/open-webui/open-webui/commit/e3e4bd87df6fc629e7e22081d980d55a7632b8b7
- https://github.com/open-webui/open-webui/pull/27823
- https://github.com/open-webui/open-webui/releases/tag/v0.11.1
- https://github.com/open-webui/open-webui/security/advisories/GHSA-34r3-9m95-vq73

### [CVE-2026-87911](https://aws.amazon.com/security/security-bulletins/2026-104-aws/)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-87911
- 関連キーワード: postgresql, aws
- 影響製品: -
- 公開日: 2026-09-10 05:21:02 JST
- 更新日: 2026-09-10 05:21:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: awslabs postgres-mcp-server (1.1.7未満)のSQL検証機能におけるOSコマンドインジェクションの脆弱性。
- 影響: 読み取り専用モード動作時であっても、悪意あるSQL文（COPY ... TO PROGRAM等）を通じてPostgreSQLサーバーホスト上で任意のOSコマンドが実行される可能性があります。
- 推奨対応: postgres-mcp-server をバージョン 1.1.7 以降に更新してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-104-aws/
- https://github.com/awslabs/mcp/security/advisories/GHSA-fph8-pg5w-78fv
- https://pypi.org/project/awslabs.postgres-mcp-server/1.1.7/

### [CVE-2026-85788](https://aws.amazon.com/security/security-bulletins/2026-103-aws/)

> **Backend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-85788
- 関連キーワード: gin, mysql, aws
- 影響製品: -
- 公開日: 2026-09-10 02:17:49 JST
- 更新日: 2026-09-10 05:13:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: awslabs mysql-mcp-server (1.0.23未満)におけるSQLインラインコメントを利用した読み取り専用検証のバイパス脆弱性。
- 影響: 読み取り専用の制限が回避され、意図しないファイルの読み取りや書き込み操作が実行される可能性があります。
- 推奨対応: mysql-mcp-server をバージョン 1.0.23 以降に更新してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-103-aws/
- https://github.com/awslabs/mcp/releases?page=2#release-2026.07.20260702161703
- https://github.com/awslabs/mcp/security/advisories/GHSA-x25m-ph3m-3r9q

### [CVE-2026-87016](https://github.com/open-webui/open-webui/commit/73c1f5806aeb6345dad5de8f5aa26d1f3d0bef80)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-87016
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-09-10 07:18:46 JST
- 更新日: 2026-09-10 07:18:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open WebUI (0.6.41〜0.11.1未満、SQLite利用時)におけるOAuth/SCIM識別子検索時のSQL LIKE曖昧一致に起因する脆弱性。
- 影響: ワイルドカード文字を含むOAuth subjectにより、意図しない別ユーザー（管理者など）としてセッションが認識され、アカウントを乗っ取られる可能性があります。
- 推奨対応: Open WebUI をバージョン 0.11.1 以降にアップデートしてください。

#### References
- https://github.com/open-webui/open-webui/commit/73c1f5806aeb6345dad5de8f5aa26d1f3d0bef80
- https://github.com/open-webui/open-webui/pull/28624
- https://github.com/open-webui/open-webui/releases/tag/v0.11.1
- https://github.com/open-webui/open-webui/security/advisories/GHSA-wpmr-8h3q-fwj7

### [CVE-2026-47156](https://github.com/mantisbt/mantisbt/commit/e3571c319b1721b41b0dc4b5b5203cbdcbe0c2ee)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-47156
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-10 02:17:21 JST
- 更新日: 2026-09-10 02:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MantisBT（2.28.3以前）のSOAP APIにおける認証バイパスの脆弱性。`mci_check_login()`関数において、任意の有効な`cookie_string`を知っていればパスワードなしで他ユーザー（管理者含む）として認証可能。
- 影響: 未認証の攻撃者が管理者を含む他ユーザーになりすまし、システムを全権限で操作される可能性がある。
- 推奨対応: 修正版へのアップデートを実施するか、不要な場合は自己登録機能（$g_allow_signup）やSOAP APIの無効化・制限を検討してください。

#### References
- https://github.com/mantisbt/mantisbt/commit/e3571c319b1721b41b0dc4b5b5203cbdcbe0c2ee
- https://github.com/mantisbt/mantisbt/security/advisories/GHSA-c2xg-qjqw-2v98
- https://mantisbt.org/bugs/view.php?id=37121

### [CVE-2026-67403](https://helpcenter.sara.sage.com/hc/en-us/articles/52106283946651-June-R2-Release-2026)

> **Backend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-67403
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-10 01:17:04 JST
- 更新日: 2026-09-10 05:20:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cash CollectのSage AR Automation APIにおけるテナントレベルの不適切な認可制御の脆弱性。
- 影響: 認証済みユーザーが他テナントの識別子を指定することで、別テナントの管理リソースへ不正アクセスする可能性がある。
- 推奨対応: 提供元が配布する修正パッチまたは最新バージョンへの更新を行ってください。

#### References
- https://helpcenter.sara.sage.com/hc/en-us/articles/52106283946651-June-R2-Release-2026

### [CVE-2026-87929](https://github.com/EviL0rd/maxsite-cve4/blob/main/2026.09.08-maxsite-cms-hardcoded-session-key-auth-bypass.md)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-87929
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-10 02:17:53 JST
- 更新日: 2026-09-10 05:14:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MaxSite CMS（109.6以前）の設定ファイルに暗号化キーがハードコードされており変更されない脆弱性。
- 影響: 未認証の攻撃者が既知のキーを用いて管理者権限のセッションクッキーを偽造し、認証を迂回して管理者としてアクセスする可能性がある。
- 推奨対応: 最新バージョンへアップデートし、セッション暗号化キーをランダムな独自の値に変更してください。

#### References
- https://github.com/EviL0rd/maxsite-cve4/blob/main/2026.09.08-maxsite-cms-hardcoded-session-key-auth-bypass.md
- https://github.com/maxsite/cms
- https://github.com/maxsite/cms/blob/2ca0a0c7d1d71106a25dbb0f2aedaaefbf12802c/application/config/config.php#L230-L254
- https://github.com/maxsite/cms/blob/2ca0a0c7d1d71106a25dbb0f2aedaaefbf12802c/application/maxsite/common/core/init.php#L70-L96
- https://www.vulncheck.com/advisories/maxsite-cms-through-109.6-authentication-bypass-via-hardcoded-encryption-key

### [CVE-2026-26212](https://wordpress.com/plugins/rara-one-click-demo-import)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-26212
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-10 00:17:06 JST
- 更新日: 2026-09-10 05:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用Rara One Click Demo Importプラグイン（1.3.5未満）における任意ファイルアップロードの脆弱性。
- 影響: 管理者権限を持つ攻撃者がファイル検証を回避してPHPファイルをアップロードし、Webサーバー上でリモートコード実行（RCE）を行う可能性がある。
- 推奨対応: プラグインをバージョン 1.3.5 以降へアップデートしてください。

#### References
- https://wordpress.com/plugins/rara-one-click-demo-import
- https://www.vulncheck.com/advisories/rara-one-click-demo-import-arbitrary-file-upload-rce

### [CVE-2026-22591](https://github.com/eProsima/Fast-DDS/security/advisories/GHSA-7577-rf2r-j88m)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-22591
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-09-10 01:17:02 JST
- 更新日: 2026-09-10 05:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: eprosima Fast DDSのSQLフィルタリング機能における不適切なネスト処理の脆弱性。
- 影響: DDSドメイン内の攻撃者が、深層ネストされたフィルター式を含むサブメッセージを送信することで、他の参加者プロセスを遠隔からクラッシュ（DoS）させる可能性がある。
- 推奨対応: Fast DDSをバージョン 2.6.12、2.14.6、3.2.4、3.4.3 またはそれ以降へ更新してください。

#### References
- https://github.com/eProsima/Fast-DDS/security/advisories/GHSA-7577-rf2r-j88m

### [CVE-2026-87822](https://github.com/tdunning/t-digest)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-87822
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-10 00:17:27 JST
- 更新日: 2026-09-10 05:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: t-digest（3.1〜3.3）のデシリアライズ処理（`MergingDigest.fromBytes`）における入力検証不備の脆弱性。
- 影響: 攻撃者が細工したシリアライズデータを送信してNaN値を注入することで、マージ時のソート処理効率を極端に低下させ、深刻な処理遅延（DoS）を引き起こす可能性がある。
- 推奨対応: 修正されたバージョンへのライブラリアップデートを実施してください。

#### References
- https://github.com/tdunning/t-digest
- https://github.com/tdunning/t-digest/blob/8d5c1523c3d46925e9b3979a8d63c0b9d004ed1c/core/src/main/java/com/tdunning/math/stats/MergingDigest.java
- https://github.com/tdunning/t-digest/blob/8d5c1523c3d46925e9b3979a8d63c0b9d004ed1c/core/src/main/java/com/tdunning/math/stats/Sort.java
- https://github.com/tdunning/t-digest/issues/229
- https://www.vulncheck.com/advisories/t-digest-3.1-through-3.3-denial-of-service-via-nan-centroid-means-in-mergingdigest-frombytes

### [CVE-2026-82530](https://wordpress.org/plugins/ip2location-country-blocker/#developers)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-82530
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-10 00:17:11 JST
- 更新日: 2026-09-10 05:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用IP2Location Country Blockerプラグイン（2.45.0未満）におけるアクセス制御バイパスの脆弱性。
- 影響: 攻撃者が`X-Real-IP`ヘッダーを偽造することで、IPベースのアクセス制限を迂回して保護されたリソースへアクセスする可能性がある。
- 推奨対応: プラグインをバージョン 2.45.0 以降へアップデートしてください。

#### References
- https://wordpress.org/plugins/ip2location-country-blocker/#developers
- https://www.vulncheck.com/advisories/ip2location-country-blocker-access-control-bypass-via-x-real-ip-header

### [CVE-2026-83530](https://github.com/cel-expr/cel-go/pull/1302)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-83530
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-09-10 00:17:12 JST
- 更新日: 2026-09-10 01:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CEL（Common Expression Language）環境における式の長さ上限チェック前のメモリ割当不備の脆弱性。
- 影響: 設定された制限値を超える長い入力式が与えられた際、検証前に比例したメモリ割当が行われ、リソースを過剰に消費する可能性がある。
- 推奨対応: 修正パッチを適用するか、CELに渡す前に外部で入力長制限を行ってください。

#### References
- https://github.com/cel-expr/cel-go/pull/1302

### [CVE-2026-80916](https://git.kernel.org/stable/c/18799e858b407bf355383c9dd6c06477aa437134)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80916
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-10 02:17:46 JST
- 更新日: 2026-09-10 02:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのPREEMPT_RT構成におけるKCOV一時ストレージのデータ競合およびデータ破損の脆弱性。
- 影響: 割り込みスレッドの割り込みによってKCOV状態が上書き・破壊され、カーネルの正常な動作や測定に影響を与える可能性がある。
- 推奨対応: 修正が適用されたLinuxカーネルへアップデートしてください。

#### References
- https://git.kernel.org/stable/c/18799e858b407bf355383c9dd6c06477aa437134
- https://git.kernel.org/stable/c/22670d1552fe155822b2abf91f920925f7d067b4
- https://git.kernel.org/stable/c/2eed77fdcb0cc48e8eccb2bcd4b7f2c6d650e84c
- https://git.kernel.org/stable/c/5dc59fc959b2b5742985d7ef24bccd1868217dc2
- https://git.kernel.org/stable/c/8ed3ddf23d39bf5338406bd9f8863d44748cf6ce

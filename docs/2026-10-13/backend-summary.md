# Backend CVE Summary (2026-10-13)

## Overview

- 取得日時: 2026-10-13 11:59:56 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 14
- Critical: 5
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-108895](https://github.com/wudipjq/my_vuln/blob/main/Linksys3/vuln_69/69.md)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-108895
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-13 00:17:07 JST
- 更新日: 2026-10-13 00:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A weakness has been identified in Linksys E1700 1.0.0.4.003. The affected element is the function setDMZ of the file /goform/setDMZ. Executing a manipulation of the argument MAC_addr can lead to os command injection. The attack can be executed remotely. The exploit has been made available to the public and could be use...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/wudipjq/my_vuln/blob/main/Linksys3/vuln_69/69.md
- https://vuldb.com/cve/CVE-2026-108895
- https://vuldb.com/submit/973114
- https://vuldb.com/vuln/416687
- https://vuldb.com/vuln/416687/cti

### [CVE-2026-108896](https://github.com/wudipjq/my_vuln/blob/main/Linksys3/vuln_70/70.md)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-108896
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-13 00:17:07 JST
- 更新日: 2026-10-13 00:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was found in Linksys E1700 1.0.0.4.003. This affects the function setLinksysIpv6 of the file /goform/setLinksysIpv6. The manipulation of the argument _6rd_prefix/_6rd_prefix_len results in os command injection. The attack can be launched remotely. The exploit has been made public and could be used. The...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/wudipjq/my_vuln/blob/main/Linksys3/vuln_70/70.md
- https://vuldb.com/cve/CVE-2026-108896
- https://vuldb.com/submit/973115
- https://vuldb.com/vuln/416683
- https://vuldb.com/vuln/416683/cti

### [CVE-2026-108914](https://github.com/fizz-is-on-the-way/Iot_vuls/tree/main/BR-6208AC/BufferOverflow_formWlSiteSurvey)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-108914
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-13 02:17:13 JST
- 更新日: 2026-10-13 02:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw has been found in Edimax BR-6208AC 1.32. Affected by this issue is some unknown functionality of the file /goform/formWlSiteSurvey. This manipulation of the argument ifname causes buffer overflow. Remote exploitation of the attack is possible. The exploit has been published and may be used. The vendor was contac...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/fizz-is-on-the-way/Iot_vuls/tree/main/BR-6208AC/BufferOverflow_formWlSiteSurvey
- https://vuldb.com/cve/CVE-2026-108914
- https://vuldb.com/submit/977194
- https://vuldb.com/vuln/416726
- https://vuldb.com/vuln/416726/cti

### [CVE-2026-108899](https://github.com/carfeii/oss/blob/main/zoraxy.md#finding-1-path-exception-rules-for-basic-auth-zorxauth-and-captcha-match-on-raw-string-prefix-not-a-path-boundary)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-108899
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-13 01:17:03 JST
- 更新日: 2026-10-13 01:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: tobychui zoraxy の Path Exception Matcher コンポーネントにおける handleBasicAuth 関数の不適切な認可処理の脆弱性。
- 影響: 遠隔の攻撃者により認可制御を迂回される可能性がある。
- 推奨対応: バージョン 3.3.5-rc1 以降への更新が推奨される。

#### References
- https://github.com/carfeii/oss/blob/main/zoraxy.md#finding-1-path-exception-rules-for-basic-auth-zorxauth-and-captcha-match-on-raw-string-prefix-not-a-path-boundary
- https://github.com/tobychui/zoraxy/
- https://github.com/tobychui/zoraxy/commit/37cd0f27b17cd15cfa4af409bfec943146f5fdfe
- https://github.com/tobychui/zoraxy/pull/1291
- https://github.com/tobychui/zoraxy/releases/tag/v3.3.5-rc1

### [CVE-2026-109250](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-jhv5-m83m-hxhq)

> **Backend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-109250
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-13 02:17:16 JST
- 更新日: 2026-10-13 02:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreeRDP の collect_keys() 関数における PKCS#11 鍵列挙時のヒープバッファオーバーフローの脆弱性。
- 影響: ローカルの攻撃者が不正なスマートカードトークンを用いてヒープメモリを破損させる可能性がある。
- 推奨対応: FreeRDP 3.32.0 以降のバージョンへのアップデートが推奨される。

#### References
- https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-jhv5-m83m-hxhq
- https://www.vulncheck.com/advisories/freerdp-3.0.0-before-3.32.0-heap-buffer-overflow-via-pkcs-11-collect-keys

### [CVE-2026-109257](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-2hhg-8xx6-v73w)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-109257
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-13 02:17:17 JST
- 更新日: 2026-10-13 02:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreeRDP before 3.32.0 contains a double-free vulnerability in nsc_context_initialize_encode() that leaves dangling plane pointers after a partial buffer growth failure. Attackers using a crafted RDP client can negotiate NSCodec with a large desktop geometry to trigger allocation failure, crashing the server during cont...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-2hhg-8xx6-v73w
- https://www.vulncheck.com/advisories/freerdp-before-3.32.0-double-free-via-nscodec-plane-growth-failure

### [CVE-2026-109366](https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-4f6v-mj46-gxg3)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-109366
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-13 02:17:34 JST
- 更新日: 2026-10-13 02:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zebra の受信ゴシップダウンロードパスにおける不適切な整合性検証の脆弱性。
- 影響: 未認証のピアにより新しいブロックの破棄が強制され、マイニングバックエンドのブロック発見が遅延する可能性がある。
- 推奨対応: Zebra 6.4.0 以降のバージョンへのアップデートが推奨される。

#### References
- https://github.com/ZcashFoundation/zebra/security/advisories/GHSA-4f6v-mj46-gxg3
- https://www.vulncheck.com/advisories/zebra-before-6.4.0-gossiped-block-drop-via-forged-coinbase-scriptsig-height

### [CVE-2026-103526](https://kb.cert.org/vuls/id/162329)

> **Backend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-103526
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-13 00:17:06 JST
- 更新日: 2026-10-13 00:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Thelia の管理ログインおよびパスワード再設定エンドポイントにおける不適切な応答処理によるアカウント列挙の脆弱性。
- 影響: 未認証の攻撃者により、有効な管理者アカウント名を効率的に特定される可能性がある。
- 推奨対応: 適切なアクセス制御やレート制限の実装、または修正済みバージョンへの更新を推奨する。

#### References
- https://kb.cert.org/vuls/id/162329

### [CVE-2026-109243](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-q9p9-j22r-577p)

> **Backend** / **MEDIUM** / CVSS: **4.4** / KEV: **no**

- タイトル: CVE-2026-109243
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-13 02:17:15 JST
- 更新日: 2026-10-13 02:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreeRDP の crypto_write_pem 処理における秘密鍵書き込み時の不適切なアクセス権限割り当ての脆弱性。
- 影響: マルチユーザー環境のローカル攻撃者に、共有一時ディレクトリ内の PKINIT 秘密鍵を読み取られる可能性がある。
- 推奨対応: FreeRDP 3.32.0 以降のバージョンへのアップデートが推奨される。

#### References
- https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-q9p9-j22r-577p
- https://www.vulncheck.com/advisories/freerdp-3.0.0-before-3.32.0-insecure-permissions-on-soft-smartcard-private-key-file

### [CVE-2026-109293](https://github.com/open-webui/open-webui/security/advisories/GHSA-2h26-836q-4jh2)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-109293
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-13 02:17:22 JST
- 更新日: 2026-10-13 02:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open WebUI のツールエクスポート機能における情報漏洩の脆弱性。
- 影響: 認証済みの一般ユーザーに読み取り専用ツールのソースコードを取得され、埋め込まれた API キーなどの資格情報が漏洩する可能性がある。
- 推奨対応: Open WebUI 0.11.4 以降のバージョンへのアップデートが推奨される。

#### References
- https://github.com/open-webui/open-webui/security/advisories/GHSA-2h26-836q-4jh2
- https://www.vulncheck.com/advisories/open-webui-0.11.0-before-0.11.4-tool-source-disclosure-via-tool-export-endpoint

### [CVE-2026-109239](https://github.com/unclecode/crawl4ai/security/advisories/GHSA-f77g-77vp-r96v)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-109239
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-13 02:17:14 JST
- 更新日: 2026-10-13 02:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Crawl4AI の RobotsParser.can_fetch におけるブラインド SSRF（サーバーサイドリクエストフォージェリ）の脆弱性。
- 影響: 未認証の攻撃者により、Docker のエグレス制御を迂回して内部ネットワークやクラウドメタデータ等へアクセスされる可能性がある。
- 推奨対応: Crawl4AI 0.9.4 以降のバージョンへのアップデートが推奨される。

#### References
- https://github.com/unclecode/crawl4ai/security/advisories/GHSA-f77g-77vp-r96v
- https://www.vulncheck.com/advisories/crawl4ai-before-0.9.4-blind-ssrf-via-robotsparser-can-fetch-robots-txt-fetch

### [CVE-2026-103535](https://kb.cert.org/vuls/id/162329)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-103535
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-10-13 00:17:06 JST
- 更新日: 2026-10-13 00:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Thelia の翻訳エディタにおけるパストラバーサルおよび PHP コードインジェクションの複合的な脆弱性。
- 影響: 権限を持つ攻撃者により Web 参照可能なパスに任意の PHP ファイルを書き込まれ、リモートコード実行につながる可能性がある。
- 推奨対応: 適切な入力検証の実施および修正済みバージョンへの更新を推奨する。

#### References
- https://kb.cert.org/vuls/id/162329

### [CVE-2026-109372](https://github.com/zitadel/zitadel/security/advisories/GHSA-x4c7-fpcx-w9q6)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-109372
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-13 02:17:34 JST
- 更新日: 2026-10-13 02:17:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADEL の SAML ID プロバイダインテントコールバックにおける認証回避の脆弱性。
- 影響: 組織管理者権限を持つ攻撃者が、他の SAML プロバイダに紐づく任意のユーザーとしてセッションを取得する可能性がある。
- 推奨対応: ZITADEL 4.19.2 以降（3.x系は3.4.16以降などの修正版）へアップデートする。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-x4c7-fpcx-w9q6
- https://www.vulncheck.com/advisories/zitadel-3.0.0-before-4.19.2-account-takeover-via-saml-identity-provider-confusion

### [CVE-2026-109373](https://github.com/zitadel/zitadel/security/advisories/GHSA-jh92-5mrj-p2w2)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-109373
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-13 02:17:35 JST
- 更新日: 2026-10-13 02:17:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADEL の Login V2 UI における未署名セッションクッキー偽造による認証回避の脆弱性。
- 影響: 未認証の攻撃者にセッション ID を推測・偽造され、他ユーザーや管理者のアカウントを乗っ取られる可能性がある。
- 推奨対応: ZITADEL 4.19.2 以降のバージョンへのアップデートが推奨される。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-jh92-5mrj-p2w2
- https://www.vulncheck.com/advisories/zitadel-3.0.0-before-4.19.2-account-takeover-via-unsigned-login-v2-session-cookie

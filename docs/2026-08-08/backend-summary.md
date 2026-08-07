# Backend CVE Summary (2026-08-08)

## Overview

- 取得日時: 2026-08-08 07:51:11 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 17
- Critical: 1
- High: 8
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-58262](https://github.com/klever-io/klever-go/commit/a11cb28e495e608d8034dbe83a91e89d0c68e0f7)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-58262
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-08 07:16:59 JST
- 更新日: 2026-08-08 07:16:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Klever-Go is the Go implementation of the Klever blockchain protocol. Prior to 1.7.20, header signature verification counts the unused padding bits of the PubKeysBitmap toward the two-thirds validator quorum. These padding bits do not correspond to any validator and are ignored by the actual BLS aggregate-signature che...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/klever-io/klever-go/commit/a11cb28e495e608d8034dbe83a91e89d0c68e0f7
- https://github.com/klever-io/klever-go/security/advisories/GHSA-f9h7-4mmq-vgcq

### [CVE-2026-15972](https://discuss.hashicorp.com/t/hcsec-2026-25-multiple-vulnerabilities-impacting-hashicorp-consul/77629)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-15972
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-08 05:16:50 JST
- 更新日: 2026-08-08 05:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Consul Community Edition and Consul Enterprise 1.13.0 through 2.0.2 are vulnerable to an unauthenticated denial of service through unbounded connection acceptance on the external gRPC listeners. A remote attacker may exhaust agent file descriptors, goroutines, and memory by opening many incomplete connections, potentia...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://discuss.hashicorp.com/t/hcsec-2026-25-multiple-vulnerabilities-impacting-hashicorp-consul/77629

### [CVE-2026-65819](https://github.com/gopacket/gopacket/commit/210f25fb9b3ca1af2eb649936f78ad6991b6c9c5)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-65819
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-08 05:16:52 JST
- 更新日: 2026-08-08 05:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: gopacket provides packet processing capabilities for Go. Through version 1.7.0, multiple layer decoders use attacker-controlled lengths, counts, or offsets before validating them against packet buffers, allowing a crafted packet decoded through DecodingLayerParser or DecodeFromBytes to trigger an unrecovered panic and...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gopacket/gopacket/commit/210f25fb9b3ca1af2eb649936f78ad6991b6c9c5
- https://github.com/gopacket/gopacket/releases/tag/v1.7.0
- https://github.com/gopacket/gopacket/security/advisories/GHSA-8mcr-459q-5mx2

### [CVE-2026-71556](https://github.com/go-git/go-git/commit/008a78f2dd86f52544ddff8b8e8ddeecdf3f7aab)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-71556
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-08 02:17:10 JST
- 更新日: 2026-08-08 02:17:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: go-git is an extensible git implementation library written in pure Go. Prior to 5.19.2 and 6.0.0-alpha.5, worktree operations (including checkout, status, and add) resolve symbolic links inside the working tree without confining resolution to the worktree boundary, so a maliciously crafted repository containing a symli...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/go-git/go-git/commit/008a78f2dd86f52544ddff8b8e8ddeecdf3f7aab
- https://github.com/go-git/go-git/commit/661d1c7f101d34e002a3cfcf8dbea5b7421d07ac
- https://github.com/go-git/go-git/releases/tag/v5.19.2
- https://github.com/go-git/go-git/releases/tag/v6.0.0-alpha.5
- https://github.com/go-git/go-git/security/advisories/GHSA-hc8v-wwc9-vgxm

### [CVE-2026-46405](https://github.com/openbao/openbao/commit/0d82e0a5a3b6a93e8087bcbaf0b11326c12d4f4d)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-46405
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-08 07:16:58 JST
- 更新日: 2026-08-08 07:16:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenBao is an open source identity-based secrets management system. Prior to version 2.5.4, in OpenBao's Kerberos auth method on the `GET` handler, or when an `Authorization: Negotiate` header is supplied, the response is includes a `logical.Auth` object in addition to an error message. This results in tokens being cre...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/openbao/openbao/commit/0d82e0a5a3b6a93e8087bcbaf0b11326c12d4f4d
- https://github.com/openbao/openbao/pull/3150
- https://github.com/openbao/openbao/releases/tag/v2.5.4
- https://github.com/openbao/openbao/security/advisories/GHSA-7j6w-vvw2-5f9c

### [CVE-2026-64676](https://github.com/kata-containers/kata-containers/security/advisories/GHSA-h8jv-63p2-496x)

> **Backend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-64676
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-08 07:16:59 JST
- 更新日: 2026-08-08 07:16:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Kata Containers is an open source implementation of lightweight Virtual Machines (VMs) that perform like containers. In versions prior to 4.0.0, the kata-agent is vulnerable to an authorization bypass in confidential-guest memory management. In Confidential Containers (CoCo) deployments, the kata-agent enforces an OPA/...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/kata-containers/kata-containers/security/advisories/GHSA-h8jv-63p2-496x

### [CVE-2026-47364](https://cwe.mitre.org/data/definitions/200.html)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-47364
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-08 03:17:17 JST
- 更新日: 2026-08-08 04:17:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: On every successful login, the Datadog Android application calls FirebaseCrashlytics.setUserId with the signed-in user's Datadog UUID — a stable per-user identifier that is meaningful inside Datadog. This associates the Datadog user UUID with the device's Firebase installation ID on Google's backend. Separately, uncaug...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cwe.mitre.org/data/definitions/200.html
- https://firebase.google.com/docs/crashlytics/customize-crash-reports?platform=android#enable-opt-in-reporting
- https://trust.datadoghq.com/?tcuUid=2e8b8fa5-39ca-43f4-9f6a-aeafafb440ef

### [CVE-2026-71557](https://github.com/go-git/go-git/commit/4a0e66d555de5f9a30c31e2df64f445f42bd01e7)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-71557
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-08 02:17:10 JST
- 更新日: 2026-08-08 03:17:24 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: go-git is an extensible git implementation library written in pure Go. Prior to 5.19.2 and 6.0.0-alpha.5, reference names are not sanitized before being used to construct on-disk paths under the reference storage directory, so a maliciously crafted reference name (for example containing directory-traversal sequences) c...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/go-git/go-git/commit/4a0e66d555de5f9a30c31e2df64f445f42bd01e7
- https://github.com/go-git/go-git/commit/da9f7d8a0e98b475600177348d6ece384a370f36
- https://github.com/go-git/go-git/pull/2247
- https://github.com/go-git/go-git/pull/2254
- https://github.com/go-git/go-git/releases/tag/v5.19.2

### [CVE-2026-71852](https://github.com/py-pdf/pypdf/commit/51cb6acf9e8a35b77e90b4d87d28fe3e1416d7d7)

> **Backend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-71852
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-08 04:18:54 JST
- 更新日: 2026-08-08 04:18:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: pypdf is a free and open-source pure-python PDF library. Prior to 6.15.0, a crafted PDF can cause long runtimes and large memory consumption when pypdf/_font.py function Font._collect_cid_character_widths expands unusually large CID font /W width ranges or excessive width entries during text extraction. This issue is f...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/py-pdf/pypdf/commit/51cb6acf9e8a35b77e90b4d87d28fe3e1416d7d7
- https://github.com/py-pdf/pypdf/pull/3946
- https://github.com/py-pdf/pypdf/releases/tag/6.15.0
- https://github.com/py-pdf/pypdf/security/advisories/GHSA-fwg2-594c-jp42

### [CVE-2026-71870](https://github.com/py-pdf/pypdf/commit/afba8080e19d29a3c256a742b340995e695b35aa)

> **Backend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-71870
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-08 05:16:52 JST
- 更新日: 2026-08-08 05:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: pypdf is a free and open-source pure-python PDF library. Prior to 6.15.0, a crafted PDF can cause large memory consumption when pypdf/_cmap.py function parse_bfrange parses unusually large source-code or destination-string tokens in a font /ToUnicode CMap during text extraction. This issue is fixed in 6.15.0.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/py-pdf/pypdf/commit/afba8080e19d29a3c256a742b340995e695b35aa
- https://github.com/py-pdf/pypdf/pull/3944
- https://github.com/py-pdf/pypdf/releases/tag/6.15.0
- https://github.com/py-pdf/pypdf/security/advisories/GHSA-fp3f-mc75-235c

### [CVE-2026-56818](https://github.com/netty/netty/commit/5b68c61f37aa4a3045cba624cbea239655c9003b)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-56818
- 関連キーワード: redis
- 影響製品: -
- 公開日: 2026-08-08 03:17:19 JST
- 更新日: 2026-08-08 03:17:19 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Netty is an asynchronous, event-driven network application framework. Prior to 4.1.136.Final and 4.2.16.Final, the RedisArrayAggregator Redis codec clears retained partial aggregate state when the maxNestedArrayDepth limit is exceeded, but it does not clear the same state when the sibling maxElements limit is exceeded....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/netty/netty/commit/5b68c61f37aa4a3045cba624cbea239655c9003b
- https://github.com/netty/netty/commit/bb2ff68a1fb71cb4b0eb9a9e17b66c52aff680c6
- https://github.com/netty/netty/pull/17065
- https://github.com/netty/netty/security/advisories/GHSA-p9jm-q85p-7mcp

### [CVE-2026-19264](https://gadvisory.org/advisories/PSA-2026-TH12B7)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-19264
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-08 00:17:00 JST
- 更新日: 2026-08-08 03:17:13 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Postiz is an open-source social media scheduling tool. The route that serves locally stored media joins URL-supplied path segments onto the upload directory and streams the file without normalising the path or confining it to that directory, and the route requires no authentication. Raw dot-segments are collapsed befor...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gadvisory.org/advisories/PSA-2026-TH12B7
- https://github.com/gitroomhq/postiz-app/commit/7936062
- https://github.com/gitroomhq/postiz-app/releases/tag/v2.22.1

### [CVE-2026-64638](https://hackerone.com/reports/3877102)

> **Backend** / **HIGH** / CVSS: **8.9** / KEV: **no**

- タイトル: CVE-2026-64638
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-08 03:17:20 JST
- 更新日: 2026-08-08 04:18:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WordPress is vulnerable to a pre-auth reflected XSS vulnerability on the login screen. Via a specially crafted malicious third-party website hosted by an attacker, it is possible for this to be escalated to an RCE vulnerability with conditions outside of the attackers control. This requires successful social engineerin...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://hackerone.com/reports/3877102
- https://wordpress.org/news/2026/08/wordpress-7-0-3-release/

### [CVE-2026-11430](https://github.com/getgrav/grav)

> **Backend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-11430
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-08 04:17:34 JST
- 更新日: 2026-08-08 07:16:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Grav CMS's scheduler-webhook plugin contains an authentication bypass in the webhook token check. When the webhook feature is enabled but no webhookToken is configured, a compound conditional short-circuits and skips token validation, so an unauthenticated remote attacker who can reach POST /scheduler/webhook can trigg...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/getgrav/grav
- https://github.com/getgrav/grav/commit/694f1dae06d9061bbf0669c4291e3b206f998d71
- https://github.com/getgrav/grav/security/advisories/GHSA-xwv3-2mv2-w33x
- https://www.vulncheck.com/advisories/grav-cms-scheduler-webhook-authentication-bypass-via-null-short-circuit

### [CVE-2026-48169](https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-gv23-xrm3-8c62)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-48169
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-08 07:16:59 JST
- 更新日: 2026-08-08 07:16:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PraisonAI is a multi-agent teams system. Versions prior to 0.1.4 of the PraisonAI Platform API have two authorization failures that together break workspace isolation. The service layer for issues and projects performs global primary-key lookups without checking workspace ownership, so any authenticated user can read,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-gv23-xrm3-8c62
- https://github.com/pypa/advisory-database/tree/main/vulns/praisonai-platform/PYSEC-2026-2935.yaml

### [CVE-2026-17600](https://help.sonatype.com/en/sonatype-nexus-repository-3-95-0-release-notes.html)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-17600
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-08 02:17:00 JST
- 更新日: 2026-08-08 04:17:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Sonatype Nexus Repository 3 did not immediately terminate a user's active login session or revoke their cached permissions when that user's account was deleted, deactivated, or had its password changed. A user whose account was already logged in at the time of one of these actions could continue using their existing se...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://help.sonatype.com/en/sonatype-nexus-repository-3-95-0-release-notes.html
- https://support.sonatype.com/hc/en-us/articles/53888843674003/

### [CVE-2026-62996](https://github.com/smarty-php/smarty/commit/3c9f77a2e06ce319ae0092496af32cc8f3adc52e)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-62996
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-08 01:17:26 JST
- 更新日: 2026-08-08 03:17:19 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Smarty is a template engine for PHP, facilitating the separation of presentation (HTML/CSS) from application logic. From 5.0.0 until 5.8.4, Smarty's stream: resource-name handling does not adequately restrict which PHP stream wrappers and filter chains can be referenced from a template, allowing a php://filter-wrapped...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/smarty-php/smarty/commit/3c9f77a2e06ce319ae0092496af32cc8f3adc52e
- https://github.com/smarty-php/smarty/pull/1195
- https://github.com/smarty-php/smarty/releases/tag/v5.8.4
- https://github.com/smarty-php/smarty/security/advisories/GHSA-rjhh-76wf-8xmw
- https://github.com/smarty-php/smarty/security/advisories/GHSA-rjhh-76wf-8xmw

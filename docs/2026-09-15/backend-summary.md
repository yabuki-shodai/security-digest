# Backend CVE Summary (2026-09-15)

## Overview

- 取得日時: 2026-09-15 09:32:10 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 17
- Critical: 4
- High: 7
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-90806](https://github.com/Django-CRM/Django-CRM/commit/799bb1210238f402c0c4948c8eedb6e61cd0c8d7)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-90806
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-09-15 03:20:27 JST
- 更新日: 2026-09-15 05:56:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DjangoCRM（1.2以下）の一括ケース更新機能（BulkUpdateCasesView）における認可不備の脆弱性。
- 影響: 遠隔の攻撃者により権限チェックを回避され、一括更新処理を不正に操作される可能性があります。
- 推奨対応: DjangoCRM を 1.3.0 以降の修正済みバージョンへアップデートしてください。

#### References
- https://github.com/Django-CRM/Django-CRM/commit/799bb1210238f402c0c4948c8eedb6e61cd0c8d7
- https://github.com/Django-CRM/Django-CRM/issues/745
- https://github.com/Django-CRM/Django-CRM/pull/746
- https://github.com/Django-CRM/Django-CRM/releases/tag/v1.3.0
- https://vuldb.com/cve/CVE-2026-90806

### [CVE-2026-55837](https://github.com/dbt-labs/dbt-mcp/commit/b8bdb40f90ed29f6b36176c5f6c697aa27a035a9)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-55837
- 関連キーワード: fastapi
- 影響製品: -
- 公開日: 2026-09-15 02:17:48 JST
- 更新日: 2026-09-15 02:17:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: dbt-mcp（1.20.0未満）のローカルOAuthヘルパーにおける認証およびHostヘッダー検証不足の脆弱性。
- 影響: DNSリバインディング攻撃や同一マシン上の別プロセス経由でアクセス権限・リフレッシュトークンを窃取され、被害者権限でdbt Platformのプロジェクトやシークレット等を閲覧・改ざんされる可能性があります。
- 推奨対応: dbt-mcp を 1.20.0 以降の修正済みバージョンへアップデートしてください。

#### References
- https://github.com/dbt-labs/dbt-mcp/commit/b8bdb40f90ed29f6b36176c5f6c697aa27a035a9
- https://github.com/dbt-labs/dbt-mcp/pull/789
- https://github.com/dbt-labs/dbt-mcp/releases/tag/v1.20.0
- https://github.com/dbt-labs/dbt-mcp/security/advisories/GHSA-jr33-mw75-7j8f

### [CVE-2026-20353](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-20353
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-15 02:17:43 JST
- 更新日: 2026-09-15 06:00:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Secure Email Gateway および Secure Email and Web Manager における不適切なリソース有効期間制御（CWE-664）の脆弱性。
- 影響: リソースの不適切な制御により、システムの動作不良や予期しないリソース状態を引き起こす可能性があります。
- 推奨対応: Ciscoが提供する修正済みソフトウェアにアップデートしてください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm

### [CVE-2026-76440](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76440
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-15 02:17:50 JST
- 更新日: 2026-09-15 06:00:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Secure Email Gateway および Secure Email and Web Manager におけるパス・トラバーサル（CWE-23）の脆弱性。
- 影響: 攻撃者により不適切なファイルパス参照が行われ、制限されたファイルの閲覧やシステムへの悪影響が引き起こされる可能性があります。
- 推奨対応: Ciscoが提供する修正済みソフトウェアにアップデートしてください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm

### [CVE-2026-76441](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76441
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-15 02:17:50 JST
- 更新日: 2026-09-15 06:00:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Secure Email Gateway および Secure Email and Web Manager における不適切なアクセス制御（CWE-284）の脆弱性。
- 影響: 認可されていないユーザーにより保護された機能やデータへアクセスされ、不正な操作が行われる可能性があります。
- 推奨対応: Ciscoが提供する修正済みソフトウェアにアップデートしてください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm

### [CVE-2026-76443](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76443
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-15 02:17:50 JST
- 更新日: 2026-09-15 06:00:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Secure Email Gateway および Secure Email and Web Manager における入力データの中和不備（CWE-707）の脆弱性。
- 影響: 不適切な入力データ処理に起因して、意図しない命令の実行やインジェクション攻撃につながる可能性があります。
- 推奨対応: Ciscoが提供する修正済みソフトウェアにアップデートしてください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm

### [CVE-2026-53717](https://github.com/envoyproxy/gateway/commit/5a78db82b7cf4fc5bebbeda2c50952892038a464)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-53717
- 関連キーワード: go, gin, docker, kubernetes
- 影響製品: -
- 公開日: 2026-09-15 05:16:45 JST
- 更新日: 2026-09-15 05:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Envoy Gateway is an open source project for managing Envoy Proxy as a standalone or Kubernetes-based application gateway. Prior to 1.7.4 and 1.8.1, internal/wasm/imagefetcher.go follows tenant-controlled EnvoyExtensionPolicy spec.wasm[].code.image.url values to Docker or OCI Wasm layers, and extractWasmPluginBinary use...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/envoyproxy/gateway/commit/5a78db82b7cf4fc5bebbeda2c50952892038a464
- https://github.com/envoyproxy/gateway/commit/96e2b750868a459ace4b8b68e6a6e4fb0152b9b7
- https://github.com/envoyproxy/gateway/commit/b4737180c7e597490c6363075c565fa8cf24eead
- https://github.com/envoyproxy/gateway/pull/9171
- https://github.com/envoyproxy/gateway/pull/9172

### [CVE-2026-55253](https://github.com/langchain-ai/langchain-mongodb/commit/14a6cc39e67d23fd409cd13a9caae2c329df0a09)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-55253
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-15 03:17:55 JST
- 更新日: 2026-09-15 05:16:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LangChain MongoDB provides integrations between MongoDB, Atlas, LangChain, and LangGraph. Prior to langgraph-checkpoint-mongodb 0.3.0 and langgraph-store-mongodb 0.4.0, MongoDBSaver.list(), MongoDBSaver.alist(), and MongoDBStore.search() incorporate filter dictionaries into MongoDB queries without recursively rejecting...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/langchain-ai/langchain-mongodb/commit/14a6cc39e67d23fd409cd13a9caae2c329df0a09
- https://github.com/langchain-ai/langchain-mongodb/commit/240e7ecee432ea006d9fef6ea506bfd2e009a3f4
- https://github.com/langchain-ai/langchain-mongodb/commit/5465e4d3ea0ef5c88a666a6442bd853ff4bd70e5
- https://github.com/langchain-ai/langchain-mongodb/pull/384
- https://github.com/langchain-ai/langchain-mongodb/releases/tag/libs/langgraph-checkpoint-mongodb/v0.4.0

### [CVE-2026-82438](https://lists.apache.org/thread/2o7tl3hcdd865njxsn4d9cxp1frkctz3)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-82438
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-15 00:17:10 JST
- 更新日: 2026-09-15 05:58:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache StormのHTTPコンポーネント（UI, Logviewer, DRPC）におけるCORS不備およびJSONP処理の不適切な設定に関する脆弱性。
- 影響: 悪意ある外部Webページから認証済みユーザーのレスポンス（機密データ）を不正に読み取られる可能性があります。
- 推奨対応: Apache Stormを修正済みバージョンへ更新し、CORSおよびJSONP設定を見直してください。

#### References
- https://lists.apache.org/thread/2o7tl3hcdd865njxsn4d9cxp1frkctz3
- http://www.openwall.com/lists/oss-security/2026/09/13/17

### [CVE-2026-59570](https://help.zscaler.com/zscaler-client-connector/client-connector-app-release-summary-2026)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59570
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-15 00:17:06 JST
- 更新日: 2026-09-15 01:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: On affected versions of Zscaler client connector, a pre-installed peer app can tear down the Zscaler tunnel, force user logout, and toggle packet capture.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://help.zscaler.com/zscaler-client-connector/client-connector-app-release-summary-2026

### [CVE-2026-84445](https://github.com/grpc/grpc-go/commit/3822494d8ea03b992c089fd2a195f041762fffb7)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-84445
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-15 02:17:51 JST
- 更新日: 2026-09-15 02:17:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: gRPC-Go is the Go language implementation of gRPC. Prior to 1.82.2 and 1.83.2, servers created with xds.NewGRPCServer() allow internal/transport/http2_server.go to accept an RPC containing neither the :authority header nor the Host header, while RouteAndProcess in internal/xds/server/routing.go assumes that an authorit...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/grpc/grpc-go/commit/3822494d8ea03b992c089fd2a195f041762fffb7
- https://github.com/grpc/grpc-go/commit/8668b69c167df908b6b3666dcbf40992b9e932a4
- https://github.com/grpc/grpc-go/commit/93e31b48545e2a8aaeb6e06b47fb249f94e6297f
- https://github.com/grpc/grpc-go/issues/9354
- https://github.com/grpc/grpc-go/pull/9365

### [CVE-2026-47253](https://github.com/julien040/anyquery/commit/27f84fc168310455eaf81ec4ba87eed20298670c)

> **Backend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-47253
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-15 05:16:44 JST
- 更新日: 2026-09-15 05:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Anyquery is an SQL query engine built on top of SQLite. Prior to 0.4.5, the clear_plugin_cache(plugin) SQL scalar function in namespace/other_functions.go passes the caller-controlled plugin parameter through path.Join to os.RemoveAll without rejecting traversal segments. A low-privileged bearer-token holder can invoke...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/julien040/anyquery/commit/27f84fc168310455eaf81ec4ba87eed20298670c
- https://github.com/julien040/anyquery/releases/tag/0.4.5
- https://github.com/julien040/anyquery/security/advisories/GHSA-j9rx-rppg-6hh4
- https://github.com/julien040/anyquery/security/advisories/GHSA-j9rx-rppg-6hh4

### [CVE-2026-54452](https://github.com/doyensec/safeurl/commit/d8f1021ea535b276f92999f0ec865da40e467016)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-54452
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-15 02:17:47 JST
- 更新日: 2026-09-15 02:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: safeurl is a server-side request forgery protection library. Prior to 0.2.4, the privateNetworks list in ip.go omits the IPv6 ranges 64:ff9b:1::/48, 5f00::/16, 3fff::/20, and 100:0:0:1::/64. When an application enables IPv6 with EnableIPv6(true), an attacker-controlled destination in one of these ranges is not recogniz...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/doyensec/safeurl/commit/d8f1021ea535b276f92999f0ec865da40e467016
- https://github.com/doyensec/safeurl/pull/12
- https://github.com/doyensec/safeurl/releases/tag/v0.2.4
- https://github.com/doyensec/safeurl/security/advisories/GHSA-xgch-x3mx-cm3c

### [CVE-2026-54723](https://github.com/devpi/devpi/commit/b4ea49fed4a6233d63f8509c3bf7efafc9b2db17)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-54723
- 関連キーワード: python, go, gin, nginx
- 影響製品: -
- 公開日: 2026-09-15 03:17:53 JST
- 更新日: 2026-09-15 04:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: devpi is a Python package index staging server and packaging, testing, and release tool. Prior to 6.20.2 and 7.0.0b3, a server configured with the primary or deprecated master role allows an unauthenticated, modified GET request to the +changelog route because verify_primary does not reject a missing identity and there...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/devpi/devpi/commit/b4ea49fed4a6233d63f8509c3bf7efafc9b2db17
- https://github.com/devpi/devpi/releases/tag/server-6.20.2
- https://github.com/devpi/devpi/security/advisories/GHSA-m5pq-69xg-vcq3

### [CVE-2026-76442](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-76442
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-15 02:17:50 JST
- 更新日: 2026-09-15 06:00:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: As part of Cisco's ongoing commitment to proactive security and product quality, the Cisco Secure Email Gateway and Cisco Secure Email and Web Manager engineering team has conducted a comprehensive internal security review. This review resulted in software hardening releases that address multiple internally discovered...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm

### [CVE-2026-90805](https://github.com/subhajitkhan/online-clinic-management-system/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-90805
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-15 03:20:27 JST
- 更新日: 2026-09-15 05:56:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw has been found in subhajitkhan online-clinic-management-system up to e9ee77a8827a1446220fa07ee693dc4d9a29a578. This affects an unknown part of the file doctorlogin.php. Executing a manipulation of the argument doc_mail/doc_pswd can lead to sql injection. The attack can be executed remotely. The exploit has been...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/subhajitkhan/online-clinic-management-system/
- https://github.com/subhajitkhan/online-clinic-management-system/issues/3
- https://vuldb.com/cve/CVE-2026-90805
- https://vuldb.com/submit/920373
- https://vuldb.com/vuln/403307

### [CVE-2026-53495](https://github.com/containerd/containerd/commit/22ccf4314d1fe0834f8e28f10d37d5305ef9880c)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-53495
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-15 03:17:51 JST
- 更新日: 2026-09-15 03:17:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: containerd is an open-source container runtime. Prior to 1.7.35, 2.0.12, 2.2.8, and 2.3.5, containerd on Linux with the CRI plugin enabled can indefinitely block the drainExecSyncIO goroutine in internal/cri/server/container_execsync.go when CRI ExecSync is used by exec probes or lifecycle hooks that launch long-lived...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/containerd/containerd/commit/22ccf4314d1fe0834f8e28f10d37d5305ef9880c
- https://github.com/containerd/containerd/commit/5a2a3a759b0d2ad8c821b33c3afc20890daf6d81
- https://github.com/containerd/containerd/commit/9ec55f024041d0641f6d79841e45c8781141ddaa
- https://github.com/containerd/containerd/commit/eebea8c4c912f44b656c8295c9e6607a19b76650
- https://github.com/containerd/containerd/commit/ff39a972369e2f12fae561a58d658bbf8f2bc318

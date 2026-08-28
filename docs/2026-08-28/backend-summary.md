# Backend CVE Summary (2026-08-28)

## Overview

- 取得日時: 2026-08-28 15:04:40 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 12
- Critical: 0
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-19889](https://gitlab.com/gitlab-org/gitlab/-/work_items/614164)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-19889
- 関連キーワード: go, aws
- 影響製品: -
- 公開日: 2026-08-28 02:17:43 JST
- 更新日: 2026-08-28 05:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GitLab has remediated a vulnerability in the GitLab AI Gateway component affecting all versions of the AI Gateway from 18.9.0 to 19.0.12, 19.1 to 19.1.7, and 19.2 to 19.2.2 that could have allowed an authenticated user with Duo Agent Platform access to redirect model requests to an externally-controlled endpoint via cr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gitlab.com/gitlab-org/gitlab/-/work_items/614164
- https://hackerone.com/reports/3938027

### [CVE-2026-75159](https://www.mongodb.com/docs/bi-connector/current/release-notes/#mongodb-connector-for-bi-2.14.30)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-75159
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-08-28 02:19:54 JST
- 更新日: 2026-08-28 05:18:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An unauthenticated client that can reach a MongoDB Connector for BI deployment configured with Kerberos authentication may cause mongosqld to terminate when a crafted authentication exchange encounters a specific GSSAPI error-handling condition. This can interrupt BI Connector availability until the process restarts.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.mongodb.com/docs/bi-connector/current/release-notes/#mongodb-connector-for-bi-2.14.30

### [CVE-2026-30050](https://github.com/free5gc/free5gc/issues/776)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-30050
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-28 02:17:50 JST
- 更新日: 2026-08-28 05:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An issue in the ModifyAMFEventSubscriptionProcedure function (processor/event_exposure.go) of free5gc v4.1.0 allows attackers to cause a Denial of Service (DoS) via supplying a crafted PATCH request.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/free5gc/free5gc/issues/776

### [CVE-2026-5680](https://access.redhat.com/security/cve/CVE-2026-5680)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-5680
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-28 02:18:58 JST
- 更新日: 2026-08-28 02:18:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw was found in Undertow. A remote attacker could exploit this vulnerability by sending specially crafted WebSocket messages with permessage-deflate negotiated. This could lead to excessive memory consumption due to the PerMessageDeflateFunction.largerBuffer() method using exponential doubling, resulting in a Denia...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-5680
- https://bugzilla.redhat.com/show_bug.cgi?id=2455350

### [CVE-2026-75871](https://gitlab.com/gitlab-org/gitlab/-/work_items/616990)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-75871
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-28 02:20:01 JST
- 更新日: 2026-08-28 05:18:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GitLab has remediated a vulnerability in the GitLab AI Gateway component affecting all versions of the AI Gateway from 18.10 to 19.0.12, 19.1 to 19.1.7, and 19.2 to 19.2.2 that could have allowed an authenticated user with Duo Agent Platform access to redirect outbound model requests to an externally-controlled endpoin...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gitlab.com/gitlab-org/gitlab/-/work_items/616990
- https://hackerone.com/reports/3945100

### [CVE-2026-75573](https://www.mongodb.com/docs/bi-connector/current/release-notes/#mongodb-connector-for-bi-2.14.30)

> **Backend** / **MEDIUM** / CVSS: **4.4** / KEV: **no**

- タイトル: CVE-2026-75573
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-08-28 02:19:59 JST
- 更新日: 2026-08-28 05:18:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In MongoDB Connector for BI, mongodrdl may write a TLS private-key password to standard error when the password is supplied through both the connection URI and the corresponding command-line option. A local user with access to the captured command output and encrypted key file may use the disclosed password to access t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.mongodb.com/docs/bi-connector/current/release-notes/#mongodb-connector-for-bi-2.14.30

### [CVE-2025-62342](https://support.hcl-software.com/csm?id=kb_article&sysparm_article=KB0131777)

> **Backend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2025-62342
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-28 02:17:05 JST
- 更新日: 2026-08-28 05:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HCL IntelliOps Event Management (IEM) is affected by a Session Deletion Vulnerability. It may allow improper handling of user sessions, resulting in sessions not being fully terminated after logout or deletion.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://support.hcl-software.com/csm?id=kb_article&sysparm_article=KB0131777

### [CVE-2025-62343](https://support.hcl-software.com/csm?id=kb_article&sysparm_article=KB0131777)

> **Backend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2025-62343
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-28 02:17:05 JST
- 更新日: 2026-08-28 05:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HCL IntelliOps Event Management (IEM) is affected by an Admin Session Concurrency Vulnerability. it may allows user sessions to remain active after logout or session deletion.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://support.hcl-software.com/csm?id=kb_article&sysparm_article=KB0131777

### [CVE-2026-30064](https://github.com/free5gc/free5gc/issues/770)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-30064
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-28 02:17:51 JST
- 更新日: 2026-08-28 02:17:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper input validation in the buildFilter function (processor/processor.go) of free5gc v4.0.1 allows attackers to cause a Denial of Service (DoS) via a crafted input.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/free5gc/free5gc/issues/770

### [CVE-2026-30068](https://github.com/free5gc/free5gc/issues/765)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-30068
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-28 02:17:51 JST
- 更新日: 2026-08-28 02:17:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper input validation in the HandleUpdate function (/sbi/parameter_provision.go) of free5gc v4.0.1 allows attackers to cause a Denial of Service (DoS) via a crafted input.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/free5gc/free5gc/issues/765

### [CVE-2026-19854](https://grafana.com/security/security-advisories/cve-2026-19854)

> **Backend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-19854
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-28 02:17:43 JST
- 更新日: 2026-08-28 05:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: When the ClickHouse plugin uses Native protocol (the default) with PDC or secure SOCKS, it asks for TLS but the connection library ignores that and talks to ClickHouse in the clear. Username, password, queries, and results can be read on the hop after the proxy. The server certificate is never checked, and a configured...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://grafana.com/security/security-advisories/cve-2026-19854

### [CVE-2026-56652](https://cert.pl/en/posts/2026/08/CVE-2026-56651)

> **Backend** / **MEDIUM** / CVSS: **4.6** / KEV: **no**

- タイトル: CVE-2026-56652
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-28 02:18:51 JST
- 更新日: 2026-08-28 05:17:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dool in versions up to 1.3.8 is vulnerable to a CSV injection vulnerability when exporting data to a CSV file, as it fails to sanitize cell content beginning with special formula characters like =, +, -, or @. A local attacker can exploit this by running a process with a crafted name starting with =, which injects mali...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cert.pl/en/posts/2026/08/CVE-2026-56651
- https://github.com/scottchiefbaker/dool/pull/117

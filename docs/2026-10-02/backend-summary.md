# Backend CVE Summary (2026-10-02)

## Overview

- 取得日時: 2026-10-02 10:37:46 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 18
- Critical: 6
- High: 6
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-86345](https://access.redhat.com/security/cve/CVE-2026-86345)

> **Backend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-86345
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-02 09:17:04 JST
- 更新日: 2026-10-02 09:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw was found in 389-ds-base. The server does not discard plaintext bytes already buffered from a client connection when negotiating StartTLS, allowing an on-path attacker to inject a crafted LDAP message that is processed after the TLS upgrade and whose response is delivered to the client in place of the client's o...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-86345
- https://bugzilla.redhat.com/show_bug.cgi?id=2529332

### [CVE-2026-12423](https://access.redhat.com/errata/RHSA-2026:74503)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-12423
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-02 02:17:19 JST
- 更新日: 2026-10-02 09:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw was found in Foreman. The Red Hat Satellite /unattended/provision API endpoint is vulnerable to an authentication bypass due to a semantic logic flaw in host_verifier.rb. The application verifies the database state of a provisioning token rather than its actual presence in the incoming HTTP request. Because a ho...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/errata/RHSA-2026:74503
- https://access.redhat.com/errata/RHSA-2026:74504
- https://access.redhat.com/errata/RHSA-2026:74506
- https://access.redhat.com/security/cve/CVE-2026-12423
- https://bugzilla.redhat.com/show_bug.cgi?id=2488956

### [CVE-2026-101322](https://github.com/eclipse-basyx/basyx-aas-web-ui/pull/1557)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-101322
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-02 01:17:32 JST
- 更新日: 2026-10-02 05:37:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In Eclipse BaSyx AAS Web UI versions v2-241220 through releases before v2-260924, the shared request handler attached the selected infrastructure's `Authorization` header to outgoing requests without checking the destination origin. In deployments using authentication, an attacker could induce a user to open a crafted...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/eclipse-basyx/basyx-aas-web-ui/pull/1557
- https://github.com/eclipse-basyx/basyx-aas-web-ui/releases/tag/v2-260924
- https://gitlab.eclipse.org/security/cve-assignment/-/work_items/328

### [CVE-2026-104057](https://gist.github.com/mansurmavlankulov/022bc672583687ccb34dcf4cb31b6188)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-104057
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-02 04:17:19 JST
- 更新日: 2026-10-02 05:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Podgrab contains an unauthenticated denial-of-service vulnerability caused by unsynchronized concurrent access to shared maps (activePlayers and allConnections) in its WebSocket handler, where Wshandler and HandleWebsocketMessages goroutines read and write these maps without a mutex. A remote attacker can open multiple...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gist.github.com/mansurmavlankulov/022bc672583687ccb34dcf4cb31b6188
- https://www.vulncheck.com/advisories/podgrab-unauthenticated-dos-via-concurrent-map-access-in-websocket-handler

### [CVE-2026-79900](https://www.fortra.com/security/advisories/product-security/fi-2026-013)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-79900
- 関連キーワード: go, openssl
- 影響製品: -
- 公開日: 2026-10-02 00:17:31 JST
- 更新日: 2026-10-02 05:34:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: boks_ksllogsd accepts a checksum algorithm name in the MD field of an authenticated KSL start message. Affected releases verify that OpenSSL recognizes the digest name but do not verify that the value fits in a fixed 16-byte checksum context field before copying it. An authenticated KSL client can supply an oversized,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.fortra.com/security/advisories/product-security/fi-2026-013

### [CVE-2026-104020](https://aws.amazon.com/security/security-bulletins/2026-122-aws/)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-104020
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-02 06:17:18 JST
- 更新日: 2026-10-02 07:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Uncontrolled recursion in the Ion reader in Amazon Ion Python before 0.15.0 might allow a remote unauthenticated actor to crash the application using the library, resulting in a denial of service, via a crafted, deeply nested Ion value. To remediate this issue, users should upgrade to version 0.15.0 or later.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-122-aws/
- https://github.com/amazon-ion/ion-python/releases/tag/v0.15.0
- https://github.com/amazon-ion/ion-python/security/advisories/GHSA-93q6-f8hx-vv7f

### [CVE-2026-15911](https://support.confluent.io/hc/en-us/articles/54133146724244-CONFSA-2026-22-CVE-2026-15911-Confluent-Kafka-Python-Client-Vulnerability-TLS-Certificate-verification-disabled-by-default-in-HashiCorp-Vault-KMS-Integration)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-15911
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-02 04:17:19 JST
- 更新日: 2026-10-02 05:36:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Confluent Kafka Python client's HashiCorp Vault KMS integration could allow a remote attacker to obtain sensitive information due to improper TLS certificate validation.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://support.confluent.io/hc/en-us/articles/54133146724244-CONFSA-2026-22-CVE-2026-15911-Confluent-Kafka-Python-Client-Vulnerability-TLS-Certificate-verification-disabled-by-default-in-HashiCorp-Vault-KMS-Integration

### [CVE-2026-104002](https://aws.amazon.com/security/security-bulletins/2026-123-aws/)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-104002
- 関連キーワード: python, aws
- 影響製品: -
- 公開日: 2026-10-02 07:17:00 JST
- 更新日: 2026-10-02 07:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A fail-open error handling issue within the data masking utility of Powertools for AWS Lambda (Python) might allow actors to read sensitive field values that the application intended to mask. To remediate this issue, users should upgrade to version 3.35.0.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-123-aws/
- https://github.com/aws-powertools/powertools-lambda-python/releases/tag/v3.35.0
- https://github.com/aws-powertools/powertools-lambda-python/security/advisories/GHSA-3vxg-4xv2-jfh5

### [CVE-2026-77387](https://github.com/geopy/geopy/commit/5d09fa843f90ec80788b61552539c9fd3ae6c528)

> **Backend** / **MEDIUM** / CVSS: **4.0** / KEV: **no**

- タイトル: CVE-2026-77387
- 関連キーワード: python, express
- 影響製品: -
- 公開日: 2026-10-02 02:17:31 JST
- 更新日: 2026-10-02 03:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: geopy is a geocoding library for Python. Prior to 2.5.0, geopy.Point and Point.from_string() can spend excessive CPU time due to inefficient regular-expression behavior when an application passes a long malformed coordinate string without the 256-character input limit used by the fix. Geocoder reverse methods also reac...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/geopy/geopy/commit/5d09fa843f90ec80788b61552539c9fd3ae6c528
- https://github.com/geopy/geopy/issues/608
- https://github.com/geopy/geopy/pull/610
- https://github.com/geopy/geopy/releases/tag/2.5.0
- https://github.com/geopy/geopy/security/advisories/GHSA-mhvh-fq92-pfmr

### [CVE-2026-51886](https://gist.github.com/Ro1ME/c11b1e63e4e8fca6b25275144f25ec2a)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-51886
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-02 07:17:03 JST
- 更新日: 2026-10-02 07:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: langflow-ai langflow v1.9.3 is affected by: Code Injection. The impact is: execute arbitrary code (remote). The component is: src/backend/base/langflow/api/v1/validate.py:validate-post_validate_code-a-real-authenticated-http-post-to-api-v1. The attack vector is: Attack surface: HTTP or browser-backed service path. A pu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gist.github.com/Ro1ME/c11b1e63e4e8fca6b25275144f25ec2a
- https://github.com/langflow-ai/langflow/issues/13336

### [CVE-2026-55252](https://github.com/openrundev/openrun/commit/709da784fcf1311c85f30f3542cfa3601a78bbf0)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-55252
- 関連キーワード: docker, kubernetes
- 影響製品: -
- 公開日: 2026-10-02 05:17:26 JST
- 更新日: 2026-10-02 05:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenRun is an open-source, self-hosted GitOps platform for deploying web apps and internal tools to Docker or Kubernetes. Prior to version 0.17.7, the restrictions on redirect URLs in openrun can be bypassed by attackers, leading to open redirect attacks. This issue has been patched in version 0.17.7.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/openrundev/openrun/commit/709da784fcf1311c85f30f3542cfa3601a78bbf0
- https://github.com/openrundev/openrun/releases/tag/v0.17.7
- https://github.com/openrundev/openrun/security/advisories/GHSA-h5g6-xmh4-hc37

### [CVE-2026-97662](https://aws.amazon.com/security/security-bulletins/2026-121-aws/)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-97662
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-10-02 03:17:29 JST
- 更新日: 2026-10-02 05:36:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An argument injection issue in the diff scan operation in AWS security-agent-mcp-server before version 0.2.0 might allow context-dependent threat actors to create, overwrite, or truncate arbitrary files on the host outside the intended workspace directory via a crafted reference value supplied to the diff scan operatio...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-121-aws/
- https://pypi.org/project/awslabs.security-agent-mcp-server/0.2.0/

### [CVE-2026-103505](https://aws.amazon.com/security/security-bulletins/2026-120-aws/)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-103505
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-10-02 01:17:36 JST
- 更新日: 2026-10-02 05:36:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper neutralization of argument delimiters in the volume handling component in AWS EFS CSI Driver (aws-efs-csi-driver) v3.1.0 through v3.4.2 might allow remote authenticated users with PersistentVolume creation permissions to inject arbitrary mount options via comma-separated values in the mounttargetipmap volumeAt...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-120-aws/
- https://github.com/kubernetes-sigs/aws-efs-csi-driver/releases/tag/v3.5.0

### [CVE-2026-18397](https://www.thalesgroup.com/en/product-security-incident-response)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-18397
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-02 07:17:01 JST
- 更新日: 2026-10-02 07:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: This vulnerability enables unauthenticated remote code execution (RCE) on a victim's machine by exploiting a combination of cryptographic weaknesses and memory management issues in the SConnect native host component. The attack leverages an unrestricted messaging interface between an attacker-controlled web page and th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.thalesgroup.com/en/product-security-incident-response

### [CVE-2026-56662](https://github.com/GetSimpleCMS-CE/GetSimpleCMS-CE/security/advisories/GHSA-2rxv-4g4m-573w)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-56662
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-02 05:17:26 JST
- 更新日: 2026-10-02 05:23:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GetSimple CMS is a content management system (CMS), and GetSimple CMS CE is the community edition of that CMS. Prior to version 1.5, the UpdateCE update form contained no anti-CSRF token, and the POST handler performed no token or request-origin verification. A remote attacker can host a page that auto-submits a forged...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/GetSimpleCMS-CE/GetSimpleCMS-CE/security/advisories/GHSA-2rxv-4g4m-573w

### [CVE-2026-96658](https://access.redhat.com/errata/RHSA-2026:74503)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-96658
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-02 02:17:34 JST
- 更新日: 2026-10-02 09:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw was found in Foreman. An authenticated attacker with low-level permissions can achieve remote code execution (RCE) by bypassing the safemode sandbox within the templating engine. Due to improper handling of delegated methods, an attacker can append unauthorized functions to the allowed execution list, enabling t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/errata/RHSA-2026:74503
- https://access.redhat.com/errata/RHSA-2026:74504
- https://access.redhat.com/errata/RHSA-2026:74506
- https://access.redhat.com/security/cve/CVE-2026-96658
- https://bugzilla.redhat.com/show_bug.cgi?id=2534185

### [CVE-2026-103922](https://github.com/ionic-team/capacitor/commit/430356a91e1419fc66862dc09835081aa501677e)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-103922
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-02 03:17:12 JST
- 更新日: 2026-10-02 04:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Capacitor is a cross-platform native runtime for web applications. From 6.0.0 until 6.2.2, 7.6.9, 8.3.5, 8.4.3, and 8.5.1, the Android and iOS WebView navigation guard validates a target URL's host and scheme but not its path, allowing a victim who activates an untrusted link to navigate a frame to /_capacitor_http_int...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/ionic-team/capacitor/commit/430356a91e1419fc66862dc09835081aa501677e
- https://github.com/ionic-team/capacitor/commit/80b6c5e81d062e1e158914040f49e044d95b7ccb
- https://github.com/ionic-team/capacitor/commit/85ccc44151fdd5ae5e0d806d875766ef4b84ad5d
- https://github.com/ionic-team/capacitor/commit/af9a287fef45f0ac68ce640cb42fed2d06b0f1b4
- https://github.com/ionic-team/capacitor/commit/d5e3170ba0ff155fc542b7e6d16cff5201406540

### [CVE-2026-94620](https://github.com/foundation50/classroom50/commit/79112f33932d1b5c398a8801d97a8813d52d55ce)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-94620
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-02 01:18:08 JST
- 更新日: 2026-10-02 02:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Classroom 50 is a free and open-source tool for managing and grading programming assignments via GitHub. Prior to version 1.11.0, `gh teacher download` clones each student's assignment repository and then writes autograde artifacts (`result.json` and `results.json`) into the just-cloned working tree. The write followed...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/foundation50/classroom50/commit/79112f33932d1b5c398a8801d97a8813d52d55ce
- https://github.com/foundation50/classroom50/security/advisories/GHSA-qx2g-vpwq-466c

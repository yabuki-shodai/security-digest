# Backend CVE Summary (2026-09-16)

## Overview

- 取得日時: 2026-09-16 09:13:08 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 11
- Critical: 2
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-61549](https://github.com/woodpecker-ci/woodpecker/commit/5df9d52260626c074c6caafb2dc83d3bc6b53be1)

> **Backend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-61549
- 関連キーワード: go, gin, kubernetes
- 影響製品: -
- 公開日: 2026-09-16 00:17:20 JST
- 更新日: 2026-09-16 01:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Woodpecker is a CI/CD engine. From 1.0.0 until 3.16.0, pipeline/backend/kubernetes/backend_options.go defines backend_options.kubernetes.serviceAccountName, and the Kubernetes backend in pipeline/backend/kubernetes/pod.go copies that pipeline-step value directly into the pod specification without administrator authoriz...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/woodpecker-ci/woodpecker/commit/5df9d52260626c074c6caafb2dc83d3bc6b53be1
- https://github.com/woodpecker-ci/woodpecker/commit/609ba481b5e912f59aaae8ca7bc22b44523c5e37
- https://github.com/woodpecker-ci/woodpecker/pull/6792
- https://github.com/woodpecker-ci/woodpecker/releases/tag/v3.16.0
- https://github.com/woodpecker-ci/woodpecker/security/advisories/GHSA-qf34-295c-26v8

### [CVE-2026-91949](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-x7v6-xfx3-52j6)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-91949
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-16 01:17:48 JST
- 更新日: 2026-09-16 01:17:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreeRDP server versions before 3.31.0 contain a protocol negotiation bypass vulnerability that allows unauthenticated attackers to establish RDSTLS connections despite server policy disabling them. Attackers can send incompatible protocol requests, receive negotiation failures, then complete TLS handshake and enter RDS...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-x7v6-xfx3-52j6
- https://www.vulncheck.com/advisories/freerdp-3.0.0-through-3.30.0-protocol-negotiation-bypass

### [CVE-2026-19407](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes#March_31_2026)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-19407
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-09-16 01:17:08 JST
- 更新日: 2026-09-16 01:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Bucket Squatting in Google Cloud Gemini Enterprise Agent Platform SDK for Python versions prior to 1.166.1 allows an attacker to achieve Remote Code Execution (RCE) and tenant-project token theft.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes#March_31_2026

### [CVE-2026-55887](https://github.com/docker/mcp-gateway/commit/306d2d94a3b526f43281313321bf784f2d46a7fe)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-55887
- 関連キーワード: go, gin, docker
- 影響製品: -
- 公開日: 2026-09-16 01:17:16 JST
- 更新日: 2026-09-16 04:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MCP Gateway allows easy and secure running and deployment of MCP servers. From 0.21.0 until 0.42.2, Docker MCP Gateway YAML-unmarshalled the attacker-controlled io.docker.server.metadata OCI image label into the broad catalog.Server structure for direct docker:// references and catalog snapshot imports in pkg/oci/self_...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/docker/mcp-gateway/commit/306d2d94a3b526f43281313321bf784f2d46a7fe
- https://github.com/docker/mcp-gateway/commit/439b2200d9e26a4ff414aeb043785df45a78422b
- https://github.com/docker/mcp-gateway/pull/498
- https://github.com/docker/mcp-gateway/releases/tag/v0.42.2
- https://github.com/docker/mcp-gateway/security/advisories/GHSA-r2xf-7jw5-pjg6

### [CVE-2026-54637](https://github.com/dragonflyoss/dragonfly/commit/4f9bd93d22453e3f433f9d912bfeeca22760c237)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-54637
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-16 00:17:18 JST
- 更新日: 2026-09-16 00:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dragonfly is an open source P2P-based file distribution and image acceleration system. Prior to 2.4.4-rc.3, the scheduler's default unauthenticated v1 gRPC flow accepts attacker-controlled PeerHost.Ip and PeerHost.DownPort values through RegisterPeerTask and ReportPeerResult, storeHost copies those values into resource...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dragonflyoss/dragonfly/commit/4f9bd93d22453e3f433f9d912bfeeca22760c237
- https://github.com/dragonflyoss/dragonfly/releases/tag/v2.4.4-rc.3
- https://github.com/dragonflyoss/dragonfly/security/advisories/GHSA-chwm-m7g7-685g

### [CVE-2026-55149](https://github.com/vouch/vouch-proxy/commit/fa18ce30ba50a4863a436acad044c22965329c4f)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-55149
- 関連キーワード: go, gin, nginx
- 影響製品: -
- 公開日: 2026-09-16 02:17:21 JST
- 更新日: 2026-09-16 02:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vouch Proxy is an SSO and OAuth/OIDC login solution for Nginx using the auth_request module. Prior to 0.48.0, Cookie in pkg/cookie/cookie.go parses the total part count from an attacker-controlled multipart cookie name and passes the value to make([]string, numParts) without checking that the value is positive or reaso...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vouch/vouch-proxy/commit/fa18ce30ba50a4863a436acad044c22965329c4f
- https://github.com/vouch/vouch-proxy/releases/tag/v0.48.0
- https://github.com/vouch/vouch-proxy/security/advisories/GHSA-qqff-5854-px68

### [CVE-2026-91937](https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-wpvf-4vfx-rgxm)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-91937
- 関連キーワード: go, gin, mongodb
- 影響製品: -
- 公開日: 2026-09-16 01:17:45 JST
- 更新日: 2026-09-16 03:19:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Flowise before 3.1.4 fails to sanitize the overrideConfig.sessionId parameter before using it in MongoDB queries within the MongoDBMemory node. Unauthenticated attackers can submit MongoDB operator objects through the prediction API to read chat history records belonging to other users from the shared collection.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-wpvf-4vfx-rgxm
- https://www.vulncheck.com/advisories/flowise-before-3.1.4-nosql-injection-via-sessionid

### [CVE-2026-47780](https://github.com/free5gc/free5gc/security/advisories/GHSA-6gxq-gpr8-xgjp)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-47780
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-09-16 00:17:15 JST
- 更新日: 2026-09-16 01:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: free5GC is an open-source implementation of the 5G core network. In 4.2.3 and earlier, HandleCreateEeSubscriptions and HandleQueryeesubscriptions in free5gc/udr internal/sbi/api_datarepository.go validate the ueId path value with a regular expression whose final .+ alternative accepts every non-empty string instead of...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/free5gc/free5gc/security/advisories/GHSA-6gxq-gpr8-xgjp
- https://github.com/free5gc/free5gc/security/advisories/GHSA-6gxq-gpr8-xgjp

### [CVE-2026-55776](https://github.com/openbao/openbao/commit/bb17827f3e33779a10166f7d0e61b191c0facef9)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-55776
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-09-16 01:17:16 JST
- 更新日: 2026-09-16 01:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenBao is an open source identity-based secrets management system. Prior to 2.5.5, an authenticated OpenBao caller with write access to transit/keys/* could terminate the server process by setting derived to true while the type parameter selected rsa-, ecdsa-, or ed25519. The Transit policy creation path in builtin/lo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/openbao/openbao/commit/bb17827f3e33779a10166f7d0e61b191c0facef9
- https://github.com/openbao/openbao/commit/db57c62602b25da12951f3f0edb888e7c4da61e5
- https://github.com/openbao/openbao/pull/3309
- https://github.com/openbao/openbao/pull/3312
- https://github.com/openbao/openbao/releases/tag/v2.5.5

### [CVE-2026-58196](https://github.com/stacklok/toolhive/commit/4ea6afb9048ddec1d56875fa9e0da36d65c15966)

> **Backend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-58196
- 関連キーワード: go, aws
- 影響製品: -
- 公開日: 2026-09-16 01:17:16 JST
- 更新日: 2026-09-16 03:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ToolHive is a utility designed to simplify the deployment and management of Model Context Protocol (MCP) servers. Prior to 0.31.0, remote.Handler.Authenticate in pkg/auth/remote/handler.go invokes discovery.DetectAuthenticationFromServer in pkg/auth/discovery/discovery.go, whose host-side HTTP clients trust remote-serv...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/stacklok/toolhive/commit/4ea6afb9048ddec1d56875fa9e0da36d65c15966
- https://github.com/stacklok/toolhive/releases/tag/v0.31.0
- https://github.com/stacklok/toolhive/security/advisories/GHSA-pr64-jmmf-jp54
- https://github.com/stacklok/toolhive/security/advisories/GHSA-pr64-jmmf-jp54

### [CVE-2026-91964](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-2vf2-grvj-6g8x)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-91964
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-16 01:17:52 JST
- 更新日: 2026-09-16 01:17:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreeRDP versions before 3.31.0 contain a heap-based buffer overflow in nego_send_negotiation_request when processing Server Redirection PDU messages with attacker-controlled LoadBalanceInfo fields. A malicious RDP server can trigger the overflow by sending an arbitrary-length field that gets written to a fixed 512-byte...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-2vf2-grvj-6g8x
- https://www.vulncheck.com/advisories/freerdp-2.0.0-through-3.30.0-heap-buffer-overflow-via-routingtoken

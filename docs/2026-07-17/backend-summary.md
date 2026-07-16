# Backend CVE Summary (2026-07-17)

## Overview

- 取得日時: 2026-07-17 08:08:21 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 25
- Critical: 6
- High: 9
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-46621](https://github.com/yamcs/yamcs/commit/3c550348f866af4675d2ba4a51d8d12b7c7c6011)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-46621
- 関連キーワード: python, go, gin
- 影響製品: -
- 公開日: 2026-07-17 02:16:57 JST
- 更新日: 2026-07-17 04:16:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Yamcs is a mission control framework. Prior to 5.12.7, the Yamcs script evaluation engine for Python algorithms dynamically compiled and evaluated user-controlled algorithm text using Jython through the JSR-223 ScriptEngine API without enforcing a secure sandbox, so an authenticated user with the ChangeMissionDatabase...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/yamcs/yamcs/commit/3c550348f866af4675d2ba4a51d8d12b7c7c6011
- https://github.com/yamcs/yamcs/commit/4ff8fda642ea8c3309a4d3f379aa77b763148992
- https://github.com/yamcs/yamcs/releases/tag/yamcs-5.12.7
- https://github.com/yamcs/yamcs/releases/tag/yamcs-5.13.0
- https://github.com/yamcs/yamcs/security/advisories/GHSA-2g95-6x5q-xjwj

### [CVE-2026-44632](https://github.com/yamcs/yamcs/commit/3c550348f866af4675d2ba4a51d8d12b7c7c6011)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-44632
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-17 02:16:56 JST
- 更新日: 2026-07-17 02:35:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Yamcs is a mission control framework. Prior to 5.12.7, a server-side code injection vulnerability existed in the Yamcs algorithm evaluation engine org.yamcs.algorithms.JavaExprAlgorithmExecutionFactory, which dynamically compiled and evaluated user-controlled algorithm text through the Janino compiler without enforcing...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/yamcs/yamcs/commit/3c550348f866af4675d2ba4a51d8d12b7c7c6011
- https://github.com/yamcs/yamcs/commit/4ff8fda642ea8c3309a4d3f379aa77b763148992
- https://github.com/yamcs/yamcs/releases/tag/yamcs-5.12.7
- https://github.com/yamcs/yamcs/releases/tag/yamcs-5.13.0
- https://github.com/yamcs/yamcs/security/advisories/GHSA-524g-x36v-9wm6

### [CVE-2026-46512](https://github.com/mwtcmi/frogman/commit/36a05ffa2df1d256b6f6f7c3b66ef77ebe3e458a)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-46512
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-17 04:16:46 JST
- 更新日: 2026-07-17 04:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Frogman provides headless PBX control through MCP and HTTP API. Prior to 1.6.2, fm_dialplan_apply accepted template parameters including greeting, dest, url, extension, code, and file, and Tools/DialplanApply.php wrote Dialplan/Templates.php output to extensions_custom.conf while only Dialplan/TemplateBase.php:38-42 sa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mwtcmi/frogman/commit/36a05ffa2df1d256b6f6f7c3b66ef77ebe3e458a
- https://github.com/mwtcmi/frogman/releases/tag/v1.6.1
- https://github.com/mwtcmi/frogman/releases/tag/v1.6.2
- https://github.com/mwtcmi/frogman/security/advisories/GHSA-pxfc-q72v-jh8m

### [CVE-2026-44174](https://github.com/getkirby/kirby/releases/tag/4.9.1)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-44174
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-17 07:17:01 JST
- 更新日: 2026-07-17 07:17:01 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Kirby is an open-source content management system. Prior to 4.9.1 and 5.4.1, Kirby did not validate the model attributes that were used in its collection queries, allowing attackers to include arbitrary model methods in their queries. This includes methods with sensitive data such as password() (disclosing the password...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/getkirby/kirby/releases/tag/4.9.1
- https://github.com/getkirby/kirby/releases/tag/5.4.1
- https://github.com/getkirby/kirby/security/advisories/GHSA-86rh-h242-j8xp

### [CVE-2026-54526](https://github.com/argoproj/argo-workflows/commit/277e9cef0ad16d7eaaab253573d0695951a65dbd)

> **Backend** / **HIGH** / CVSS: **8.9** / KEV: **no**

- タイトル: CVE-2026-54526
- 関連キーワード: go, gin, kubernetes
- 影響製品: -
- 公開日: 2026-07-17 04:16:50 JST
- 更新日: 2026-07-17 04:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Argo Workflows is an open source container-native workflow engine for orchestrating parallel jobs on Kubernetes. Prior to 3.7.15 and 4.0.6, the allow-list fix for CVE-2026-31892 is incomplete because workflow/util/merge.go ValidateUserOverrides and SanitizeUserWorkflowSpec walk only the top-level fields of WorkflowSpec...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/argoproj/argo-workflows/commit/277e9cef0ad16d7eaaab253573d0695951a65dbd
- https://github.com/argoproj/argo-workflows/commit/358cc3968c8f06f1be0967e41df191088db0b662
- https://github.com/argoproj/argo-workflows/releases/tag/v3.7.15
- https://github.com/argoproj/argo-workflows/releases/tag/v4.0.6
- https://github.com/argoproj/argo-workflows/security/advisories/GHSA-48p8-g2fx-3wwm

### [CVE-2026-44981](https://github.com/crowdsecurity/crowdsec/commit/54a0dfe6c16b7687b0da6634e0b19ef0f5d9bb30)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-44981
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-17 05:16:44 JST
- 更新日: 2026-07-17 05:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CrowdSec offers crowdsourced protection against malicious IPs. From 1.7.0 until 1.7.8, the LAPI router used gin-contrib/gzip with DefaultDecompressHandle globally in pkg/apiserver/controllers/controller.go, causing /v1/watchers and /v1/watchers/login to decompress unauthenticated gzip-compressed JSON request bodies wit...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/crowdsecurity/crowdsec/commit/54a0dfe6c16b7687b0da6634e0b19ef0f5d9bb30
- https://github.com/crowdsecurity/crowdsec/commit/56d0d6915f7f25941dc5b4f484028646f6601a37
- https://github.com/crowdsecurity/crowdsec/security/advisories/GHSA-273h-gvwr-c3qj

### [CVE-2026-49998](https://github.com/centrifugal/centrifugo/commit/15d785015c6f318c1b68ea40b813699c9f8bd2c4)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-49998
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-17 05:16:45 JST
- 更新日: 2026-07-17 05:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Centrifugo is an open-source scalable real-time messaging server. Prior to 6.8.1, Centrifugo dynamic JWKS endpoint verification could reuse a key for one allowed issuer to verify a JWT for another allowed issuer because the JWKS cache and singleflight lookup were keyed only by JWT header kid, not by the resolved JWKS e...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/centrifugal/centrifugo/commit/15d785015c6f318c1b68ea40b813699c9f8bd2c4
- https://github.com/centrifugal/centrifugo/pull/1142
- https://github.com/centrifugal/centrifugo/releases/tag/v6.8.1
- https://github.com/centrifugal/centrifugo/security/advisories/GHSA-g6vg-wj8f-48cj

### [CVE-2026-62963](https://github.com/centrifugal/centrifugo/commit/46d40e4ac3a5446c9745f8b219197166ae12a6e5)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-62963
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-17 05:16:47 JST
- 更新日: 2026-07-17 05:16:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Centrifugo is an open-source scalable real-time messaging server. Prior to 6.8.4, Centrifugo unidirectional WebSocket transport with uni_websocket.compression enabled enforced uni_websocket.message_size_limit against compressed wire-frame length in internal/websocket/conn.go advanceFrame, but ReadMessage used io.ReadAl...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/centrifugal/centrifugo/commit/46d40e4ac3a5446c9745f8b219197166ae12a6e5
- https://github.com/centrifugal/centrifugo/pull/1162
- https://github.com/centrifugal/centrifugo/releases/tag/v6.8.4
- https://github.com/centrifugal/centrifugo/security/advisories/GHSA-q6mr-3g59-5m8x

### [CVE-2026-44982](https://github.com/crowdsecurity/crowdsec/commit/3d5c4d9b127091e9063b9b5eb785372a599a4435)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-44982
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-17 05:16:45 JST
- 更新日: 2026-07-17 05:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CrowdSec offers crowdsourced protection against malicious IPs. From 1.5.0 until 1.7.8, pkg/appsec/request.go NewParsedRequestFromRequest allocated a request body buffer from max(r.ContentLength, 0), so HTTP/1.1 requests using Transfer-Encoding: chunked and HTTP/2 requests without a content-length header produced an emp...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/crowdsecurity/crowdsec/commit/3d5c4d9b127091e9063b9b5eb785372a599a4435
- https://github.com/crowdsecurity/crowdsec/commit/57a793548671e6bbd2cde5562fe87b856ec9c642
- https://github.com/crowdsecurity/crowdsec/pull/4355
- https://github.com/crowdsecurity/crowdsec/releases/tag/v1.7.8
- https://github.com/crowdsecurity/crowdsec/security/advisories/GHSA-rw47-hm26-6wr7

### [CVE-2026-62309](https://github.com/coredns/coredns/commit/60a439dd4febfcd78e3779e952fe3fbf3c16bb1f)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-62309
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-17 05:16:47 JST
- 更新日: 2026-07-17 05:16:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CoreDNS is a DNS server written in Go. Prior to 1.14.4, a single 28-byte UDP datagram can crash the CoreDNS process when the proxyproto plugin is enabled because plugin/pkg/proxyproto/proxyproto.go PacketConn.ReadFrom handles a PROXY v2 header with non-UDP transport such as family byte 0x11, reassigns addr from a nil r...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/coredns/coredns/commit/60a439dd4febfcd78e3779e952fe3fbf3c16bb1f
- https://github.com/coredns/coredns/pull/8154
- https://github.com/coredns/coredns/releases/tag/v1.14.4
- https://github.com/coredns/coredns/security/advisories/GHSA-9rvv-m5g5-wc8r

### [CVE-2026-45795](https://github.com/JanssenProject/jans/commit/0cdd214870ee30eb2186261f21c85b9e9fc63b5c)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-45795
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-17 02:16:56 JST
- 更新日: 2026-07-17 04:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The Janssen Project is an open-source identity and access management (IAM) platform. Prior to 2.0.0, jans-auth-server accepts unsigned JWE request objects because JwtAuthorizationRequest skips inner signature validation when jwe.getSignedJWTPayload() returns null, and AuthzRequestService.processRequestObject() does not...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/JanssenProject/jans/commit/0cdd214870ee30eb2186261f21c85b9e9fc63b5c
- https://github.com/JanssenProject/jans/pull/13438
- https://github.com/JanssenProject/jans/releases/tag/v2.0.0
- https://github.com/JanssenProject/jans/security/advisories/GHSA-r3gj-4pj2-9j3j
- https://github.com/JanssenProject/jans/security/advisories/GHSA-r3gj-4pj2-9j3j

### [CVE-2026-62299](https://github.com/coredns/coredns/commit/fc447d0658b093edc8cd29a6b171216a44a644c2)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-62299
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-17 05:16:46 JST
- 更新日: 2026-07-17 05:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CoreDNS is a DNS server written in Go. Prior to 1.14.5, the CoreDNS rewrite plugin supports edns0 rewrite rules with an optional revert flag, and two response rules, edns0SetResponseRule and edns0ReplaceResponseRule[T] in plugin/rewrite/edns0.go, call res.IsEdns0() and immediately dereference the returned *dns.OPT with...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/coredns/coredns/commit/fc447d0658b093edc8cd29a6b171216a44a644c2
- https://github.com/coredns/coredns/pull/8190
- https://github.com/coredns/coredns/releases/tag/v1.14.5
- https://github.com/coredns/coredns/security/advisories/GHSA-9pmm-cxww-rrr7

### [CVE-2026-62994](https://github.com/coredns/coredns/commit/ab318db7b4a3a19273852ed627f54888198c8efb)

> **Backend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-62994
- 関連キーワード: go, gin, kubernetes
- 影響製品: -
- 公開日: 2026-07-17 05:16:47 JST
- 更新日: 2026-07-17 05:16:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CoreDNS is a DNS server written in Go. From 1.9.4 until 1.14.5, a network DNS client allowed to request AXFR for a CoreDNS zone can trigger a panic when CoreDNS is configured with k8s_external headless-service zone transfers and Kubernetes contains a headless service endpoint with no declared ports; plugin/kubernetes/o...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/coredns/coredns/commit/ab318db7b4a3a19273852ed627f54888198c8efb
- https://github.com/coredns/coredns/pull/8207
- https://github.com/coredns/coredns/releases/tag/v1.14.5
- https://github.com/coredns/coredns/security/advisories/GHSA-74w3-63xv-x9mv

### [CVE-2026-46377](https://github.com/TomWright/dasel/commit/5fc1172287df89860caf139b146007d7ed12178c)

> **Backend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-46377
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-17 04:16:46 JST
- 更新日: 2026-07-17 04:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dasel is a command-line tool and library for querying, modifying, and transforming data structures. From 3.0.0 until 3.10.1, the escape sequence handler in (*Tokenizer).parseCurRune in selector/lexer/tokenize.go increments past a trailing backslash in a quoted string such as "\ or '\ and then reads p.src[pos] without a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/TomWright/dasel/commit/5fc1172287df89860caf139b146007d7ed12178c
- https://github.com/TomWright/dasel/releases/tag/v3.10.1
- https://github.com/TomWright/dasel/security/advisories/GHSA-m5j3-4634-c2vq
- https://github.com/TomWright/dasel/security/advisories/GHSA-m5j3-4634-c2vq

### [CVE-2026-46378](https://github.com/TomWright/dasel/commit/95f8dd3af12958bf6ca2a737b3ec0267280f86ed)

> **Backend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-46378
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-17 04:16:46 JST
- 更新日: 2026-07-17 04:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Dasel is a command-line tool and library for querying, modifying, and transforming data structures. From 3.0.0 until 3.10.1, the selector lexer matchRegexPattern closure in (*Tokenizer).parseCurRune in selector/lexer/tokenize.go loops while tokenizing an unterminated regex literal such as r/ because peekRuneEqual retur...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/TomWright/dasel/commit/95f8dd3af12958bf6ca2a737b3ec0267280f86ed
- https://github.com/TomWright/dasel/security/advisories/GHSA-m6xr-fvfg-5g64

### [CVE-2026-45568](https://github.com/openziti/zrok/commit/7c1dc3ecd1c89d8cd2e845a72c3878bd2d31b4fe)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-45568
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-17 02:16:56 JST
- 更新日: 2026-07-17 02:35:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: zrok is software for sharing web services, files, and network resources. Prior to 2.0.3, zrok's Python SDK ProxyShare Flask proxy route accepts an absolute URL in the request path and passes it to urllib.parse.urljoin, allowing the requested path to replace the configured target host and causing requests.request to ret...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/openziti/zrok/commit/7c1dc3ecd1c89d8cd2e845a72c3878bd2d31b4fe
- https://github.com/openziti/zrok/releases/tag/v2.0.3
- https://github.com/openziti/zrok/security/advisories/GHSA-jh67-hwqw-m5r7

### [CVE-2026-15737](https://aws.amazon.com/security/security-bulletins/2026-058-aws/)

> **Backend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-15737
- 関連キーワード: python, gin, aws
- 影響製品: -
- 公開日: 2026-07-17 03:16:42 JST
- 更新日: 2026-07-17 04:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: AWS Bedrock AgentCore Python SDK is an open-source Python library that provides client tools for building AI agents on the Amazon Bedrock AgentCore platform. Unintended logging of sensitive user content in the OpenTelemetry instrumentation in AWS Bedrock AgentCore Python SDK versions 1.4.8 and 1.5.0 might allow a local...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-058-aws/
- https://github.com/aws/bedrock-agentcore-sdk-python/security/advisories/GHSA-hqf8-7w95-9r33
- https://pypi.org/project/bedrock-agentcore/1.5.1/

### [CVE-2026-59862](https://github.com/microsoft/kiota/releases/tag/v1.32.0)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59862
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-17 00:16:35 JST
- 更新日: 2026-07-17 04:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Kiota is an OpenAPI based HTTP Client code generator. Prior to 1.32.0, Kiota's Python generator let attacker-controlled enum value descriptions from x-ms-enum.values[].description flow through KiotaBuilder.SetEnumOptions into Documentation.DescriptionTemplate and PythonConventionService.RemoveInvalidDescriptionCharacte...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/microsoft/kiota/releases/tag/v1.32.0
- https://github.com/microsoft/kiota/security/advisories/GHSA-7f3j-j7jj-r3vr

### [CVE-2026-46338](https://github.com/facelessuser/pymdown-extensions/commit/63b7835776d703d6c339cf2110d9888f676efc0c)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-46338
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-17 04:16:45 JST
- 更新日: 2026-07-17 04:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PyMdown Extensions is a set of extensions for the Python-Markdown markdown project. From 10.0.1 until 10.21.3, pymdownx.snippets uses a string-prefix containment check in SnippetPreprocessor.get_snippet_path() in pymdownx/snippets.py when `restrict_base_path: True`, allowing markdown snippet directives to read files fr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/facelessuser/pymdown-extensions/commit/63b7835776d703d6c339cf2110d9888f676efc0c
- https://github.com/facelessuser/pymdown-extensions/releases/tag/10.21.3
- https://github.com/facelessuser/pymdown-extensions/security/advisories/GHSA-62q4-447f-wv8h

### [CVE-2026-44180](https://github.com/jupyter-server/enterprise_gateway/releases/tag/v3.3.0)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-44180
- 関連キーワード: docker, kubernetes
- 影響製品: -
- 公開日: 2026-07-17 07:17:02 JST
- 更新日: 2026-07-17 07:17:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Jupyter Enterprise Gateway launches remote Jupyter Notebook kernels across distributed clusters like Apache Spark, Kubernetes, and Docker Swarm. Versions 2.0.0rc1 and above prior to 3.3.0 have a prohibited UID and GID feature that by default prevents launching kernels with UID or GID 0 (root), and this restriction can...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jupyter-server/enterprise_gateway/releases/tag/v3.3.0
- https://github.com/jupyter-server/enterprise_gateway/security/advisories/GHSA-chq7-94j8-cj28

### [CVE-2026-33692](https://github.com/WWBN/AVideo/commit/7f418de1a95ab87bb8c8c3eb3702d71c351e098d)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-33692
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-07-17 06:17:20 JST
- 更新日: 2026-07-17 06:17:20 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WWBN AVideo is an open source video platform. Versions prior to 29.0 expose .env files to unauthenticated users through the official Docker compose configuration. The official docker-compose.yml mounts the entire project root directory as the Apache document root, causing the .env file — which contains database credent...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/WWBN/AVideo/commit/7f418de1a95ab87bb8c8c3eb3702d71c351e098d
- https://github.com/WWBN/AVideo/security/advisories/GHSA-wf69-r4mx-43rr

### [CVE-2026-33731](https://github.com/WWBN/AVideo/commit/033e83ae904cacb99495dbea7cbcfb3738cf42e4)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-33731
- 関連キーワード: gin, aws
- 影響製品: -
- 公開日: 2026-07-17 06:17:20 JST
- 更新日: 2026-07-17 06:17:20 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WWBN AVideo is an open source video platform. In versions prior to 29.0, the Authorize.Net webhook handler at plugin/AuthorizeNet/webhook.php contains a signature verification bypass that allows an attacker to forge webhook requests with arbitrary payment amounts and target user IDs. By supplying a valid transaction ID...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/WWBN/AVideo/commit/033e83ae904cacb99495dbea7cbcfb3738cf42e4
- https://github.com/WWBN/AVideo/security/advisories/GHSA-95jh-7r58-xmxw

### [CVE-2025-45870](https://github.com/netero1010/Vulnerability-Disclosure/blob/main/CVE-2025-45870/README.md)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2025-45870
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-07-17 02:16:53 JST
- 更新日: 2026-07-17 02:46:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LogicalDOC Enterprise up to and for v9.1.1 is vulnerable to Local File Inclusion (LFI) in the OnlyOfficeEditor servlet class, allowing authenticated user to exploit path traversal flaws in the fileExt parameter, enabling unauthorized access to sensitive files outside the designated directories.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/netero1010/Vulnerability-Disclosure/blob/main/CVE-2025-45870/README.md
- https://www.logicaldoc.com/

### [CVE-2026-53536](https://github.com/activepieces/activepieces/commit/2cb6148010a6c2a22900f4c8b08d75cc5c921d1c)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-53536
- 関連キーワード: gin, postgresql
- 影響製品: -
- 公開日: 2026-07-17 04:16:50 JST
- 更新日: 2026-07-17 04:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Activepieces is an open source AI workflow automation platform. Prior to 0.83.0, the /v1/step-files/signed download endpoint verified the supplied JWT against the shared signing secret but did not check the token's audience, and combined with a missing null-check on the decoded fileId, this allowed any caller holding a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/activepieces/activepieces/commit/2cb6148010a6c2a22900f4c8b08d75cc5c921d1c
- https://github.com/activepieces/activepieces/commit/afe852f60e39fcc6273d41e11f0765586b5a0e49
- https://github.com/activepieces/activepieces/releases/tag/0.83.0
- https://github.com/activepieces/activepieces/security/advisories/GHSA-9723-fmff-mc24

### [CVE-2026-45336](https://github.com/StratonWebDesigners/HireFlow/releases/tag/v1.3)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-45336
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-17 03:16:43 JST
- 更新日: 2026-07-17 03:16:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: HireFlow is a web-based interview management system for managing candidates, scheduling interviews, and tracking hiring progress. In 1.2 and earlier, app.py assigns a hard-coded Flask secret_key used to sign session cookies, allowing unauthenticated attackers who know the public source value to forge cookies containing...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/StratonWebDesigners/HireFlow/releases/tag/v1.3
- https://github.com/StratonWebDesigners/HireFlow/security/advisories/GHSA-x53g-jr84-jrv5

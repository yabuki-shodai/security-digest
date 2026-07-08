# Backend CVE Summary (2026-07-08)

## Overview

- 取得日時: 2026-07-08 13:53:56 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 11
- Critical: 0
- High: 10
- KEV掲載: 0
- 日本語AI要約: 未使用

## CVEs

### [CVE-2026-55427](https://github.com/coder/coder/pull/26154)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-55427
- 概要: Coder allows organizations to provision remote development environments via Terraform. Prior to versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2, `coder config-ssh` wrote server-supplied SSH settings (`HostnameSuffix`, `SSHConfigOptions`) into the user's `~/.ssh/config` without sanitizing embedded newlines or restricting directives so a malicious or compromised Coder server could inject arbitrary SSH configuration. Practical exploitation requires control of the server-supplied values through a malicious or compromised deployment, a man-in-the-middle position or admin access to the `HostnameSuffix` and `SSHConfigOptions` settings. The fix in versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2 validates `H...
- 関連キーワード: go, terraform
- 影響製品: -
- 公開日: 2026-07-08 09:16:33 JST
- 更新日: 2026-07-08 09:16:33 JST
- 出典: NVD
- 参照:
  - https://github.com/coder/coder/pull/26154
  - https://github.com/coder/coder/releases/tag/v2.29.17
  - https://github.com/coder/coder/releases/tag/v2.32.7
  - https://github.com/coder/coder/releases/tag/v2.33.8
  - https://github.com/coder/coder/releases/tag/v2.34.2

### [CVE-2026-13020](https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/june-2026-arcgis-security-bulletin)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-13020
- 概要: A Weak Password Recovery Mechanism for Forgotten Password exists in Esri Portal for ArcGIS versions 12.1 and earlier on Windows, Linux and Kubernetes. A remote, unauthorized attacker may assume ownership of a user’s account by manipulating this mechanism. ArcGIS Administrators should configure an email server with ArcGIS Enterprise to facilitate user self-service password recovery. The ability for an administrator to reset a user’s password remains unchanged.
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-07-08 02:16:35 JST
- 更新日: 2026-07-08 03:16:34 JST
- 出典: NVD
- 参照:
  - https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/june-2026-arcgis-security-bulletin

### [CVE-2026-55436](https://github.com/coder/coder/pull/26131)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-55436
- 概要: Coder allows organizations to provision remote development environments via Terraform. Starting in version 2.30.0 and prior to versions 2.32.7, 2.33.8, and 2.34.2, the AI Bridge Proxy (`aibridgeproxyd`) created a goproxy server whose default transport set `InsecureSkipVerify: true` and only assigned a secure transport when an upstream proxy was configured. In the default configuration (no upstream proxy), outbound HTTPS to the Coder access URL accepted any TLS certificate. Practical exploitation requires an on-path (man-in-the-middle) position between the AI Bridge Proxy and the Coder server. Deployments where they are co-located over loopback are effectively unaffected. The fix in versions...
- 関連キーワード: go, terraform
- 影響製品: -
- 公開日: 2026-07-08 10:16:27 JST
- 更新日: 2026-07-08 10:16:27 JST
- 出典: NVD
- 参照:
  - https://github.com/coder/coder/pull/26131
  - https://github.com/coder/coder/releases/tag/v2.32.7
  - https://github.com/coder/coder/releases/tag/v2.33.8
  - https://github.com/coder/coder/releases/tag/v2.34.2
  - https://github.com/coder/coder/security/advisories/GHSA-84rm-42xw-mx52

### [CVE-2026-45796](https://github.com/coder/coder/commit/57b11d405f17492aa789d4b9ff33366f961a37f8)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-45796
- 概要: Coder allows organizations to provision remote development environments via Terraform. Versions prior tp 2.24.5, 2.29.13, 2.30.8, 2.31.12, 2.32.2, and 2.33.3 are vulnerable to unauthenticated semi-blind Server-Side Request Forgery (SSRF) via the Azure instance identity endpoint (`POST /api/v2/workspaceagents/azure-instance-identity`). An external attacker can force the Coder server to issue HTTP GET requests to arbitrary internal or external hosts by submitting a crafted PKCS#7 signature. The server does not return the target's response body, but error messages in the API response reveal whether the target is reachable and what type of failure occurred. Versions 2.24.5, 2.29.13, 2.30.8, 2.31...
- 関連キーワード: terraform
- 影響製品: -
- 公開日: 2026-07-08 07:16:52 JST
- 更新日: 2026-07-08 07:16:52 JST
- 出典: NVD
- 参照:
  - https://github.com/coder/coder/commit/57b11d405f17492aa789d4b9ff33366f961a37f8
  - https://github.com/coder/coder/pull/25274
  - https://github.com/coder/coder/releases/tag/v2.24.5
  - https://github.com/coder/coder/releases/tag/v2.29.13
  - https://github.com/coder/coder/releases/tag/v2.30.8

### [CVE-2026-55429](https://github.com/coder/coder/pull/26103)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-55429
- 概要: Coder allows organizations to provision remote development environments via Terraform. Prior to versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2, `UpsertWorkspaceApp` overwrites an existing app's `agent_id` on a primary-key conflict and `insertAgentApp` accepts the app ID from the provisioner's `CompleteJob` payload without verifying it belongs to the workspace being built. `CompleteJob` runs under `dbauthz.AsProvisionerd` so the authorization layer does not block the cross-workspace upsert. Exploitation requires elevated access as a template author or external provisioner operator. The fix in versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2 verifies that any existing `workspace_apps` row matching the...
- 関連キーワード: terraform
- 影響製品: -
- 公開日: 2026-07-08 09:16:33 JST
- 更新日: 2026-07-08 09:16:33 JST
- 出典: NVD
- 参照:
  - https://github.com/coder/coder/pull/26103
  - https://github.com/coder/coder/releases/tag/v2.29.17
  - https://github.com/coder/coder/releases/tag/v2.32.7
  - https://github.com/coder/coder/releases/tag/v2.33.8
  - https://github.com/coder/coder/releases/tag/v2.34.2

### [CVE-2026-53511](https://github.com/kovidgoyal/calibre/commit/712f4e1ff5c1e798c335bef3bacc4efdee052e9c)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-53511
- 概要: calibre is an e-book manager. Prior to 9.10.0, a malicious EPUB, OPF, or PDF file can execute arbitrary Python code when its metadata is read by calibre, including through Add books or Edit books, by embedding a custom column definition with a python: template in calibre:user_metadata that is passed unsanitized to exec() in the template formatter. This issue is fixed in version 9.10.0.
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-08 06:17:26 JST
- 更新日: 2026-07-08 06:17:26 JST
- 出典: NVD
- 参照:
  - https://github.com/kovidgoyal/calibre/commit/712f4e1ff5c1e798c335bef3bacc4efdee052e9c
  - https://github.com/kovidgoyal/calibre/releases/tag/v9.10.0
  - https://github.com/kovidgoyal/calibre/security/advisories/GHSA-2j4m-2q7x-2c47

### [CVE-2026-49229](https://github.com/actualbudget/actual/commit/c8cb8a223a4faf1c2e1dcb0795a79a93f7b19e80)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-49229
- 概要: Actual is a local-first personal finance app. Prior to 26.6.0, in OpenID multi-user mode, disabling a user only blocks future OpenID login for that identity, while existing Actual session tokens for the disabled user remain valid. The shared session validation path accepts any existing token row that has not expired without checking whether the associated user is still enabled, allowing a disabled user to continue calling authenticated server endpoints. This issue is fixed in version 26.6.0.
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-08 07:16:52 JST
- 更新日: 2026-07-08 07:16:52 JST
- 出典: NVD
- 参照:
  - https://github.com/actualbudget/actual/commit/c8cb8a223a4faf1c2e1dcb0795a79a93f7b19e80
  - https://github.com/actualbudget/actual/releases/tag/v26.6.0
  - https://github.com/actualbudget/actual/security/advisories/GHSA-cq9c-6w48-qmfg

### [CVE-2026-55428](https://github.com/coder/coder/pull/26144)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-55428
- 概要: Coder allows organizations to provision remote development environments via Terraform. Prior to versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2, the tailnet coordinator validates that an agent's `Addresses` derive from its authenticated UUID but applies no equivalent check to `AllowedIPs`. The coordinator forwards agent-supplied `AllowedIPs` verbatim to tunnel peers which install them into the WireGuard peer configuration. The fix in versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2 validates each `AllowedIPs` prefix against the authenticating agent's UUID just like `Addresses`. As a workaround, monitor coordinator logs for agents advertising unexpected `AllowedIPs` prefixes.
- 関連キーワード: terraform
- 影響製品: -
- 公開日: 2026-07-08 09:16:33 JST
- 更新日: 2026-07-08 09:16:33 JST
- 出典: NVD
- 参照:
  - https://github.com/coder/coder/pull/26144
  - https://github.com/coder/coder/releases/tag/v2.29.17
  - https://github.com/coder/coder/releases/tag/v2.32.7
  - https://github.com/coder/coder/releases/tag/v2.33.8
  - https://github.com/coder/coder/releases/tag/v2.34.2

### [CVE-2026-55431](https://github.com/coder/coder/pull/26146)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-55431
- 概要: Coder allows organizations to provision remote development environments via Terraform. Prior to versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2, `coder open app` opens external workspace-app URLs without validating the scheme or host. When an external app URL contains the `$SESSION_TOKEN` placeholder the CLI replaces it with the user's real session token before handing the URL to the OS open handler. Practical exploitation requires the victim to run `coder open app` against a workspace whose external app definition the attacker controls. Only a malicious template author can control external app URLs. The fix in versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2 applies a URL-scheme allowlist in the CLI...
- 関連キーワード: terraform
- 影響製品: -
- 公開日: 2026-07-08 10:16:27 JST
- 更新日: 2026-07-08 10:16:27 JST
- 出典: NVD
- 参照:
  - https://github.com/coder/coder/pull/26146
  - https://github.com/coder/coder/releases/tag/v2.29.17
  - https://github.com/coder/coder/releases/tag/v2.32.7
  - https://github.com/coder/coder/releases/tag/v2.33.8
  - https://github.com/coder/coder/releases/tag/v2.34.2

### [CVE-2026-55077](https://github.com/coder/coder/pull/25709)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-55077
- 概要: Coder allows organizations to provision remote development environments via Terraform. Prior to versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2, the `PUT /api/v2/users/{user}/password` endpoint authorized only `ActionUpdatePersonal` and did not prevent a `user-admin` from resetting an `owner` account's password. It also did not require the current password when an admin reset another user's password. Exploitation requires the privileged `user-admin` role so practical risk is limited to deployments that grant `user-admin` to less trusted operators. The fix in versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2 prevents non-owner users from resetting the password of an account that holds the `owner` role....
- 関連キーワード: terraform
- 影響製品: -
- 公開日: 2026-07-08 08:16:55 JST
- 更新日: 2026-07-08 08:16:55 JST
- 出典: NVD
- 参照:
  - https://github.com/coder/coder/pull/25709
  - https://github.com/coder/coder/releases/tag/v2.29.17
  - https://github.com/coder/coder/releases/tag/v2.32.7
  - https://github.com/coder/coder/releases/tag/v2.33.8
  - https://github.com/coder/coder/releases/tag/v2.34.2

### [CVE-2026-7017](https://github.com/Perl-Toolchain-Gang/HTTP-Tiny/commit/84984ef3930ddd4afcf5eb83b40d3cee200739c3.patch)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-7017
- 概要: HTTP::Tiny versions before 0.095 for Perl forward credential headers to cross-origin redirect targets. When the server returns a 3xx redirect, `_maybe_redirect` follows the `Location:` header and `_prepare_headers_and_cb` re-merges the caller's `headers` argument into the new request, without checking whether the redirect target shares an origin with the original URL. Caller-supplied `Authorization`, `Cookie` and `Proxy-Authorization` headers are therefore re-sent to whatever host the redirect names, across scheme, host or port boundaries, and including `https` to `http` downgrades that expose them in plaintext on the wire. The HTTP::Tiny POD note that "Authorization headers will not be incl...
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-08 04:16:55 JST
- 更新日: 2026-07-08 06:17:29 JST
- 出典: NVD
- 参照:
  - https://github.com/Perl-Toolchain-Gang/HTTP-Tiny/commit/84984ef3930ddd4afcf5eb83b40d3cee200739c3.patch
  - https://github.com/Perl-Toolchain-Gang/HTTP-Tiny/commit/8f32ca89e21c3ad0422adc698fa6ad17a193f55f.patch
  - https://github.com/Perl-Toolchain-Gang/HTTP-Tiny/commit/e7a03aedf2395158f2b0d3bad2df943349227bb3.patch
  - https://github.com/Perl-Toolchain-Gang/HTTP-Tiny/pull/36
  - https://metacpan.org/release/HAARG/HTTP-Tiny-0.095-TRIAL/changes

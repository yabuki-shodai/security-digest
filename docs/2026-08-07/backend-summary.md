# Backend CVE Summary (2026-08-07)

## Overview

- 取得日時: 2026-08-07 10:32:55 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 26
- Critical: 4
- High: 4
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-65578](https://patchstack.com/database/wordpress/theme/agora/vulnerability/wordpress-agora-theme-1-9-php-object-injection-vulnerability?_s_id=cve)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-65578
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 00:17:19 JST
- 更新日: 2026-08-07 07:18:16 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Unauthenticated PHP Object Injection in Agora <= 1.9 versions.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://patchstack.com/database/wordpress/theme/agora/vulnerability/wordpress-agora-theme-1-9-php-object-injection-vulnerability?_s_id=cve

### [CVE-2026-19111](https://aws.amazon.com/security/security-bulletins/2026-077-aws/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-19111
- 関連キーワード: go, gin, mongodb
- 影響製品: -
- 公開日: 2026-08-07 07:16:55 JST
- 更新日: 2026-08-07 07:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Insecure direct object reference in the mongodb_memory, elasticsearch_memory, and mem0_memory tools in Amazon Strands Agents Tools before 0.8.3 might allow remote authenticated users to access, modify, or delete memories belonging to other tenants by influencing the LLM to emit tool calls with a forged namespace parame...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-077-aws/
- https://github.com/strands-agents/tools/security/advisories/GHSA-mpxq-953j-42m4
- https://pypi.org/project/strands-agents-tools/0.8.3/

### [CVE-2026-68750](https://cna.erlef.org/cves/CVE-2026-68750.html)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-68750
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-07 01:16:51 JST
- 更新日: 2026-08-07 07:18:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Inefficient Algorithmic Complexity vulnerability in the traversal engine in rrrene html_sanitize_ex allows an unauthenticated remote attacker to exhaust server CPU and memory via a flat run of sibling elements in sanitized HTML. The list clause of HtmlSanitizeEx.Traverser.traverse/2 recurses on the tail of a sibling li...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-68750.html
- https://github.com/rrrene/html_sanitize_ex/commit/9f5ccedbed230930813f992a1e6906fcf485981e
- https://github.com/rrrene/html_sanitize_ex/security/advisories/GHSA-463q-p2fr-mh9p
- https://osv.dev/vulnerability/EEF-CVE-2026-68750

### [CVE-2026-28180](https://patchstack.com/database/wordpress/plugin/woocommerce-mercadopago/vulnerability/wordpress-mercado-pago-payments-for-woocommerce-plugin-8-9-0-insecure-direct-object-references-idor-vulnerability?_s_id=cve)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-28180
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 00:16:53 JST
- 更新日: 2026-08-07 01:16:42 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Unauthenticated Insecure Direct Object References (IDOR) in Mercado Pago payments for WooCommerce <= 8.9.0 versions.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://patchstack.com/database/wordpress/plugin/woocommerce-mercadopago/vulnerability/wordpress-mercado-pago-payments-for-woocommerce-plugin-8-9-0-insecure-direct-object-references-idor-vulnerability?_s_id=cve

### [CVE-2026-19139](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19139
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:55 JST
- 更新日: 2026-08-07 07:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Race in CredentialProvider in Google Chrome on Windows prior to 151.0.7922.109 allowed a local attacker to perform OS-level privilege escalation via a malicious file. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/511731805

### [CVE-2026-19141](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19141
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:56 JST
- 更新日: 2026-08-07 07:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Use after free in Resources in Google Chrome on Android prior to 151.0.7922.109 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/513602949

### [CVE-2026-19152](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19152
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:57 JST
- 更新日: 2026-08-07 07:16:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Insufficient policy enforcement in Navigation in Google Chrome prior to 151.0.7922.109 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/531165110

### [CVE-2026-19044](https://github.com/LeeSinLiang/godot-mcp/)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-19044
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 00:16:48 JST
- 更新日: 2026-08-07 01:16:41 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A flaw has been found in LeeSinLiang godot-mcp 0.1.0. Affected by this vulnerability is the function executeOperation of the file src/index.ts of the component create_scene/add_node. This manipulation of the argument projectPath causes command injection. The attack needs to be launched locally. The project was informed...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/LeeSinLiang/godot-mcp/
- https://github.com/LeeSinLiang/godot-mcp/issues/1
- https://vuldb.com/cve/CVE-2026-19044
- https://vuldb.com/submit/863832
- https://vuldb.com/vuln/386486

### [CVE-2026-19137](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19137
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:55 JST
- 更新日: 2026-08-07 07:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Use after free in WebGL in Google Chrome on Android prior to 151.0.7922.109 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Critical)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/499602793

### [CVE-2026-19138](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19138
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:55 JST
- 更新日: 2026-08-07 07:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Heap buffer overflow in CrashReporting in Google Chrome prior to 151.0.7922.109 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/500097298

### [CVE-2026-19140](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19140
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:56 JST
- 更新日: 2026-08-07 07:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Use after free in GPU in Google Chrome prior to 151.0.7922.109 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/513044017

### [CVE-2026-19142](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19142
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:56 JST
- 更新日: 2026-08-07 07:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Use after free in Views in Google Chrome prior to 151.0.7922.109 allowed a remote attacker who convinced a user to engage in specific UI gestures to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/515428251

### [CVE-2026-19143](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19143
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:56 JST
- 更新日: 2026-08-07 07:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Insufficient validation of untrusted input in WebAPKs in Google Chrome on Android prior to 151.0.7922.109 allowed a local attacker to potentially perform a sandbox escape via a malicious file. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/517772612

### [CVE-2026-19144](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19144
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:56 JST
- 更新日: 2026-08-07 07:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Use after free in HTML in Google Chrome prior to 151.0.7922.109 allowed a remote attacker to potentially exploit heap corruption via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/520167277

### [CVE-2026-19145](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19145
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:56 JST
- 更新日: 2026-08-07 07:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Use after free in Translate in Google Chrome prior to 151.0.7922.109 allowed a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/521878431

### [CVE-2026-19146](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19146
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:56 JST
- 更新日: 2026-08-07 07:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Uninitialized Use in GPU in Google Chrome on Android prior to 151.0.7922.109 allowed a remote attacker who had compromised the renderer process to obtain potentially sensitive information from process memory via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/523713150

### [CVE-2026-19147](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19147
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:56 JST
- 更新日: 2026-08-07 07:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Use after free in Aura in Google Chrome on Linux prior to 151.0.7922.109 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/524439798

### [CVE-2026-19148](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19148
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:57 JST
- 更新日: 2026-08-07 07:16:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Out of bounds write in GPU in Google Chrome on Linux prior to 151.0.7922.109 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/524460000

### [CVE-2026-19149](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19149
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:57 JST
- 更新日: 2026-08-07 07:16:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Use after free in Aura in Google Chrome on Linux prior to 151.0.7922.109 allowed a remote attacker to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Critical)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/524824288

### [CVE-2026-19150](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19150
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:57 JST
- 更新日: 2026-08-07 07:16:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Inappropriate implementation in V8 in Google Chrome prior to 151.0.7922.109 allowed a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/526380803

### [CVE-2026-19151](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19151
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-07 07:16:57 JST
- 更新日: 2026-08-07 07:16:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Use after free in V8 in Google Chrome prior to 151.0.7922.109 allowed a remote attacker to execute arbitrary code inside a sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_01193673229.html
- https://issues.chromium.org/issues/530663440

### [CVE-2026-53975](https://github.com/openchamber/openchamber)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-53975
- 関連キーワード: node.js, docker
- 影響製品: -
- 公開日: 2026-08-07 00:16:55 JST
- 更新日: 2026-08-07 01:16:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenChamber 1.11.7 contains an unauthenticated remote code execution vulnerability that allows remote attackers to execute arbitrary shell commands by sending crafted POST requests to the /api/fs/exec endpoint, which passes commands verbatim to Node.js spawn() without any allowlist, blocklist, or argument validation. T...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/openchamber/openchamber
- https://github.com/openchamber/openchamber/commit/f1b9506132faf6c564a2694c7f33b94421a49b4a
- https://www.vulncheck.com/advisories/openchamber-unauthenticated-rce-via-api-fs-exec

### [CVE-2026-53985](https://github.com/sgoudelis/ground-station)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-53985
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-07 01:16:43 JST
- 更新日: 2026-08-07 07:17:42 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Ground Station prior to 0.6.0 contains an unauthenticated denial-of-service vulnerability in the Socket.IO server's service_control event handler that allows any unauthenticated network peer to forcibly terminate the ground-station process by sending a single restart_service command. Attackers can connect to the Socket...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/sgoudelis/ground-station
- https://github.com/sgoudelis/ground-station/commit/2ecde82a8814cbea18883ce023bf45cbf06172eb
- https://github.com/sgoudelis/ground-station/security/advisories/GHSA-mjp8-x6h7-229q

### [CVE-2026-11976](https://wpscan.com/vulnerability/d1250410-b919-4a90-8cf2-04031f9e5e2b/)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-11976
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-07 07:16:45 JST
- 更新日: 2026-08-07 07:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The official MonsterInsights Pro update distribution bucket (`monster-insights.s3.amazonaws.com`) was compromised. Both the current release (10.2.2) and the version MonsterInsights rolled back to (10.2.0) contain a malicious file, `class-system-check.php`. Three distinct variants were observed on 2026-06-11, all sharin...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://wpscan.com/vulnerability/d1250410-b919-4a90-8cf2-04031f9e5e2b/

### [CVE-2026-34501](https://lists.apache.org/thread/o8h6c7cq86fplxlnry6c3rn9x0ovq8mv)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-34501
- 関連キーワード: redis
- 影響製品: -
- 公開日: 2026-08-07 00:16:54 JST
- 更新日: 2026-08-07 07:17:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Heap-based Buffer Overflow vulnerability in Apache Portable Runtime Utility redis client. This issue affects Apache Portable Runtime Utility: from 1.6.0 through 1.6.3. Users are recommended to upgrade to version 1.6.4, which fixes the issue.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://lists.apache.org/thread/o8h6c7cq86fplxlnry6c3rn9x0ovq8mv
- http://www.openwall.com/lists/oss-security/2026/08/06/11

### [CVE-2026-14812](https://wpscan.com/vulnerability/0115a640-7139-4ef9-81be-6ee5c755a601/)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-14812
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-07 07:16:46 JST
- 更新日: 2026-08-07 07:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The Premium SEO WordPress plugin is malicious: it ships an unauthenticated backdoor that creates a hidden administrator account and, in some builds, also enables remote code execution, server-side request forgery and arbitrary front-end script/content injection, giving an unauthenticated attacker full control of the af...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://wpscan.com/vulnerability/0115a640-7139-4ef9-81be-6ee5c755a601/

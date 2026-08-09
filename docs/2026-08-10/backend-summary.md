# Backend CVE Summary (2026-08-10)

## Overview

- 取得日時: 2026-08-10 07:45:07 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 4
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-19359](https://github.com/nxp-auto-goldvip/gvip/releases/tag/goldvip-1.15.0)

> **Backend** / **MEDIUM** / CVSS: **5.8** / KEV: **no**

- タイトル: CVE-2026-19359
- 関連キーワード: go, gin, aws
- 影響製品: -
- 公開日: 2026-08-10 02:16:21 JST
- 更新日: 2026-08-10 02:16:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A security vulnerability has been detected in nxp-auto-goldvip gvip up to 1.4.0. Affected by this issue is the function SitewiseCustomFunction of the component Lambda Function Handler. Such manipulation leads to improper access controls. The attack can be launched remotely. Upgrading to version 1.15.0 can resolve this...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nxp-auto-goldvip/gvip/releases/tag/goldvip-1.15.0
- https://vuldb.com/cve/CVE-2026-19359
- https://vuldb.com/submit/866022
- https://vuldb.com/vuln/387213
- https://vuldb.com/vuln/387213/cti

### [CVE-2026-15534](https://github.com/Perl/perl5/commit/54cf3d44cbbedd17d774e9a37921963e8fd5d0cb.patch)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-15534
- 関連キーワード: go, gin, express
- 影響製品: -
- 公開日: 2026-08-10 03:16:42 JST
- 更新日: 2026-08-10 07:16:30 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Perl versions through 5.45.1 have out-of-bounds heap reads and writes during regular expression matching via an undersized superlinear cache in S_regmatch. The regex engine's superlinear cache holds one bit per subject position for each participating WHILEM node, so the bit count is the subject length plus one times th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Perl/perl5/commit/54cf3d44cbbedd17d774e9a37921963e8fd5d0cb.patch
- https://github.com/Perl/perl5/commit/568e6fd238867bb9e99fa3f47cba3169009239e0.patch
- http://www.openwall.com/lists/oss-security/2026/08/09/12
- http://www.openwall.com/lists/oss-security/2026/08/09/13

### [CVE-2026-19365](https://github.com/Ichigo3766/image-gen-mcp/)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-19365
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-10 04:17:00 JST
- 更新日: 2026-08-10 04:17:00 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability was identified in Ichigo3766 image-gen-mcp 0.1.0. The impacted element is an unknown function of the file src/index.ts of the component upscale_images. Such manipulation of the argument output_path leads to path traversal. The attack must be carried out locally. The project was informed of the problem e...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Ichigo3766/image-gen-mcp/
- https://github.com/Ichigo3766/image-gen-mcp/issues/6
- https://vuldb.com/cve/CVE-2026-19365
- https://vuldb.com/submit/866261
- https://vuldb.com/vuln/387219

### [CVE-2026-69659](https://cna.erlef.org/cves/CVE-2026-69659.html)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-69659
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-10 03:16:43 JST
- 更新日: 2026-08-10 03:16:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Uncontrolled Resource Consumption vulnerability in ash-project ash allows an attacker to exhaust the memory of the node via a crafted keyset pagination cursor. Read actions with keyset pagination deserialize the client-supplied page[:after] or page[:before] cursor in decode_values/2 in lib/ash/page/keyset.ex, which bas...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-69659.html
- https://github.com/ash-project/ash/commit/1816b103af975221210478d61db20adcea700319
- https://github.com/ash-project/ash/security/advisories/GHSA-j35q-v8h8-7mwq
- https://osv.dev/vulnerability/EEF-CVE-2026-69659

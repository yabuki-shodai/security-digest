# Frontend CVE Summary (2026-07-17)

## Overview

- 取得日時: 2026-07-17 08:08:21 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 5
- Critical: 2
- High: 3
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-53597](https://github.com/microsoft/prompty/commit/c27402da2487075be577f06aa79df627fb9d6853)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-53597
- 関連キーワード: typescript, javascript, gin
- 影響製品: -
- 公開日: 2026-07-17 01:19:12 JST
- 更新日: 2026-07-17 02:18:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Prompty is a markdown file format (.prompty) for LLM prompts. From 2.0.0-alpha.1 until 2.0.0-beta.3, the @prompty/core TypeScript loader in runtime/typescript/packages/core/src/core/loader.ts used gray-matter without overriding executable js and javascript frontmatter engines, allowing an attacker-controlled .prompty f...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/microsoft/prompty/commit/c27402da2487075be577f06aa79df627fb9d6853
- https://github.com/microsoft/prompty/security/advisories/GHSA-c4gh-rv8h-q9vw

### [CVE-2026-63397](https://github.com/remorses/genql)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-63397
- 関連キーワード: typescript, javascript, graphql
- 影響製品: -
- 公開日: 2026-07-17 05:16:47 JST
- 更新日: 2026-07-17 05:16:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: remorses/genql before version 6.3.4 allows an authenticated attacker with control of the GraphQL schema that is passed to genql to inject arbitrary JavaScript or TypeScript. The malicious code is injected into the generated schema.ts file and executes when the genql client is bundled and imported.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/remorses/genql
- https://github.com/remorses/genql/releases/tag/%40genql%2Fcli%406.3.4
- https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-197-01.json
- https://www.cve.org/CVERecord?id=CVE-2026-63397

### [CVE-2026-46562](https://github.com/yamcs/yamcs/commit/3c550348f866af4675d2ba4a51d8d12b7c7c6011)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-46562
- 関連キーワード: javascript, go, gin
- 影響製品: -
- 公開日: 2026-07-17 02:16:56 JST
- 更新日: 2026-07-17 04:16:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Yamcs is a mission control framework. Prior to 5.12.7, the Nashorn ScriptEngine used to evaluate user-supplied JavaScript algorithm text in yamcs-core/src/main/java/org/yamcs/algorithms/ScriptAlgorithmExecutorFactory.java was constructed without a ClassFilter, so a user with the ChangeMissionDatabase privilege could ov...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/yamcs/yamcs/commit/3c550348f866af4675d2ba4a51d8d12b7c7c6011
- https://github.com/yamcs/yamcs/commit/4ff8fda642ea8c3309a4d3f379aa77b763148992
- https://github.com/yamcs/yamcs/releases/tag/yamcs-5.12.7
- https://github.com/yamcs/yamcs/releases/tag/yamcs-5.13.0
- https://github.com/yamcs/yamcs/security/advisories/GHSA-vmwp-vh32-rj75

### [CVE-2026-46515](https://github.com/mwtcmi/frogman/commit/55ea257d5c24bc01c814a607faa7e76e86b111ec)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-46515
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-07-17 04:16:46 JST
- 更新日: 2026-07-17 04:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Frogman provides headless PBX control through MCP and HTTP API. Prior to 1.6.3, PERM_READ access was sufficient to call fm_list_managers, fm_list_pinsets, fm_show_context, fm_get_mcp_config, fm_backup_status, fm_whos_calling, fm_run_saved_query, and fm_diagnose_trunk, exposing AMI manager secrets, outbound dial PINs, f...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mwtcmi/frogman/commit/55ea257d5c24bc01c814a607faa7e76e86b111ec
- https://github.com/mwtcmi/frogman/commit/b8a8bfc12b564bcb77caef952873b9ffd4a98b00
- https://github.com/mwtcmi/frogman/issues/13
- https://github.com/mwtcmi/frogman/issues/25
- https://github.com/mwtcmi/frogman/releases/tag/v1.6.3

### [CVE-2026-45368](https://github.com/getkirby/kirby/releases/tag/5.4.1)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-45368
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-17 07:17:02 JST
- 更新日: 2026-07-17 07:17:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Kirby is an open-source content management system. In versions prior to 4.9.1 and 5.4.1, the underlying URL methods for the KirbyTags and image blocks components did not filter out malicious URL values that resolve to script execution. The vulnerability affects four first-party Kirby renderers that produce `<a href="…"...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/getkirby/kirby/releases/tag/5.4.1
- https://github.com/getkirby/kirby/security/advisories/GHSA-qvjf-922g-pj44

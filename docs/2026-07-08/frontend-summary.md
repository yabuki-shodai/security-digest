# Frontend CVE Summary (2026-07-08)

## Overview

- 取得日時: 2026-07-08 13:53:56 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: 未使用

## CVEs

### [CVE-2026-54698](https://github.com/hasura/graphql-engine/security/advisories/GHSA-r27x-gc74-qmxh)

> **Frontend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-54698
- 概要: Hasura is an open-source product that provides users GraphQL or REST APIs. Prior to 2.49.2 and 2.45.5, a user can use a where clause on a table computed field (returning SETOF some_table) to infer row values that ought to be filtered for their role based on some_table's row-level permissions. While such rows cannot be returned directly, like predicates on strings for instance allow values to be brute forced efficiently with the where clause as an oracle. This issue is fixed in versions 2.49.2 and 2.45.5.
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-07-08 07:16:53 JST
- 更新日: 2026-07-08 07:16:53 JST
- 出典: NVD
- 参照:
  - https://github.com/hasura/graphql-engine/security/advisories/GHSA-r27x-gc74-qmxh

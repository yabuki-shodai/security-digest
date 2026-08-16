# Backend CVE Summary (2026-08-17)

## Overview

- 取得日時: 2026-08-17 07:32:43 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-19956](https://github.com/gomarble-ai/facebook-ads-mcp-server/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-19956
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-17 06:16:37 JST
- 更新日: 2026-08-17 06:16:37 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability has been found in gomarble-ai facebook-ads-mcp-server 0.1.0. The impacted element is the function fetch_pagination_url of the file server.py. Such manipulation leads to server-side request forgery. The attack can be launched remotely. The name of the patch is 4e53875aa22e8991c2fa4a7660d86e1caba66659. Ap...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gomarble-ai/facebook-ads-mcp-server/
- https://github.com/gomarble-ai/facebook-ads-mcp-server/commit/4e53875aa22e8991c2fa4a7660d86e1caba66659
- https://github.com/gomarble-ai/facebook-ads-mcp-server/issues/29
- https://github.com/gomarble-ai/facebook-ads-mcp-server/pull/32
- https://vuldb.com/cve/CVE-2026-19956

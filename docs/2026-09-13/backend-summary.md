# Backend CVE Summary (2026-09-13)

## Overview

- 取得日時: 2026-09-13 08:57:49 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 0
- High: 1
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-90486](https://github.com/openstatusHQ/openstatus/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-90486
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-13 08:17:01 JST
- 更新日: 2026-09-13 08:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openstatusの resolve-custom-domain-rewrite.ts におけるサーバーサイドリクエストフォージェリ（SSRF）の脆弱性。
- 影響: リモートの第三者により、内部リクエストの送信や不適切な通信が行われる可能性があります。
- 推奨対応: 修正コミット（86f370c9c20074c3c3fdec53a359874b8e670fd4）を適用した最新バージョンへ更新してください。

#### References
- https://github.com/openstatusHQ/openstatus/
- https://github.com/openstatusHQ/openstatus/commit/86f370c9c20074c3c3fdec53a359874b8e670fd4
- https://github.com/openstatusHQ/openstatus/pull/2551
- https://vuldb.com/cve/CVE-2026-90486
- https://vuldb.com/submit/888087

# Frontend CVE Summary (2026-10-26)

## Overview

- 取得日時: 2026-10-26 09:13:39 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-114214](https://cna.erlef.org/cves/CVE-2026-114214.html)

> **Frontend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-114214
- 関連キーワード: graphql, gin
- 影響製品: -
- 公開日: 2026-10-26 05:16:31 JST
- 更新日: 2026-10-26 05:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ashライブラリにおけるthroughリレーションシップ処理時の不適切な認可の脆弱性。
- 影響: リモートの攻撃者が制限やページネーション操作を悪用し、元のレコードに関連しない宛先レコードを閲覧・列挙できる可能性があります。
- 推奨対応: 影響を受けるバージョンを確認し、修正済みライブラリへ更新してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-114214.html
- https://github.com/ash-project/ash/commit/24f41e23dcbd9d07cde270a8141490e8f79251f5
- https://github.com/ash-project/ash/commit/e37463307304b26bc8fd606322e5c4d8f7f060e5
- https://github.com/ash-project/ash/security/advisories/GHSA-g2h4-xp57-q863
- https://osv.dev/vulnerability/EEF-CVE-2026-114214

# Backend CVE Summary (2026-10-26)

## Overview

- 取得日時: 2026-10-26 09:13:39 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 2
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-115627](https://cna.erlef.org/cves/CVE-2026-115627.html)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-115627
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-26 05:16:32 JST
- 更新日: 2026-10-26 05:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ash_postgresにおけるラテラルジョイン時の属性マルチテナンシー未適用による不適切な認可の脆弱性。
- 影響: 他テナントの結合行を経由して、本来アクセス権のない他テナントの宛先レコードが取得される可能性があります。
- 推奨対応: ash_postgresをバージョン2.15.2以降にアップデートしてください。

#### References
- https://cna.erlef.org/cves/CVE-2026-115627.html
- https://github.com/ash-project/ash/security/advisories/GHSA-gr2r-f49c-9gm2
- https://github.com/ash-project/ash_postgres/commit/7115bec58678f13b1ac2fb4822a0ba1aea9dbec5
- https://github.com/ash-project/ash_postgres/commit/8c25c945c39a45299193fe70b09fc2fa2aacac7b
- https://osv.dev/vulnerability/EEF-CVE-2026-115627

### [CVE-2026-116058](https://vuldb.com/cve/CVE-2026-116058)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-116058
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-26 01:16:50 JST
- 更新日: 2026-10-26 01:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Alfresco ActivitiのJuelScriptEngine.eval関数におけるコードインジェクションの脆弱性。
- 影響: リモートの攻撃者により任意コードを実行される可能性があります。
- 推奨対応: 最新版の確認および適用、または関連機能へのアクセス制限を検討してください。

#### References
- https://vuldb.com/cve/CVE-2026-116058
- https://vuldb.com/submit/997843
- https://vuldb.com/vuln/426142
- https://vuldb.com/vuln/426142/cti

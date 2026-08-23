# Backend CVE Summary (2026-08-24)

## Overview

- 取得日時: 2026-08-24 07:33:51 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 3
- Critical: 0
- High: 1
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-78141](https://candle-throne-f75.notion.site/Tenda-CH22-formexeCommand-396df0aa11858036b0cdf7a7562d4a67)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-78141
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-24 07:16:32 JST
- 更新日: 2026-08-24 07:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tenda CH22 1.0.0.1の/goform/exeCommandにおけるcmdinput引数の不適切な処理により、コマンドインジェクションが発生する脆弱性。
- 影響: リモートの攻撃者により任意コマンドを実行される可能性があります。また、概念実証（PoC）等のエクスプロイトが公開されています。
- 推奨対応: ベンダーが提供する修正プログラムの適用や、不要な外部アクセスの制限などの対策を検討してください。

#### References
- https://candle-throne-f75.notion.site/Tenda-CH22-formexeCommand-396df0aa11858036b0cdf7a7562d4a67
- https://vuldb.com/cve/CVE-2026-78141
- https://vuldb.com/submit/882284
- https://vuldb.com/vuln/394524
- https://vuldb.com/vuln/394524/cti

### [CVE-2026-19565](https://metacpan.org/release/PAULDOOM/Apache-AppSamurai-1.01/source/lib/Apache/AppSamurai.pm#L1446-1533)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-19565
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-24 05:16:50 JST
- 更新日: 2026-08-24 07:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Perl向けApache::AppSamurai::Util（1.01以下）のCreateSessionAuthKeyにおけるセッション認証キー生成処理の不備により、予測可能なキーが生成される脆弱性。
- 影響: セッションの作成時刻を知る攻撃者により、セッションキーやIDが予測され、セッションの不正利用等につながる可能性があります。
- 推奨対応: 修正済みバージョンへの更新や、適切な鍵源（Keysource）設定の適用を検討してください。

#### References
- https://metacpan.org/release/PAULDOOM/Apache-AppSamurai-1.01/source/lib/Apache/AppSamurai.pm#L1446-1533
- https://metacpan.org/release/PAULDOOM/Apache-AppSamurai-1.01/source/lib/Apache/AppSamurai/Util.pm#L106-135
- http://www.openwall.com/lists/oss-security/2026/08/23/4

### [CVE-2026-78140](https://github.com/d0ctorsec/CVE-Reports/blob/main/CVE-UJCMS-v10.1.3-FreeMarker-SSTI/CVE-UJCMS-v10.1.3-FreeMarker-SSTI.md)

> **Backend** / **MEDIUM** / CVSS: **5.8** / KEV: **no**

- タイトル: CVE-2026-78140
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-24 05:16:50 JST
- 更新日: 2026-08-24 05:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dromara UJCMS 10.1.3以下のWebFileTemplateControllerにおける入力処理の不備により、テンプレートエンジン内の特殊要素が不適切に処理される脆弱性。
- 影響: リモートの攻撃者により不正な操作を行われる可能性があります。また、公開されたエクスプロイトが存在します。
- 推奨対応: 修正版へのアップデートや該当機能へのアクセス制御などの回避策を検討してください。

#### References
- https://github.com/d0ctorsec/CVE-Reports/blob/main/CVE-UJCMS-v10.1.3-FreeMarker-SSTI/CVE-UJCMS-v10.1.3-FreeMarker-SSTI.md
- https://vuldb.com/cve/CVE-2026-78140
- https://vuldb.com/submit/882065
- https://vuldb.com/vuln/394523
- https://vuldb.com/vuln/394523/cti

# Frontend CVE Summary (2026-11-06)

## Overview

- 取得日時: 2026-11-06 11:18:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 3
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-106715](https://github.com/Siestazzz/myVulnDB/blob/main/Mobile/NewsBreak_26.21.0/report.en.md)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-106715
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-11-06 00:17:16 JST
- 更新日: 2026-11-06 00:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Android版NewsBreakにおけるWebView JavaScriptブリッジのオリジン検証不備。
- 影響: ユーザーが特製ディープリンクを開くことで、アカウント情報やセッショントークンが漏洩する可能性があります。
- 推奨対応: 修正済みバージョンへのアプリのアップデート、およびディープリンク受信時のオリジン検証ロジックの見直しが推奨されます。

#### References
- https://github.com/Siestazzz/myVulnDB/blob/main/Mobile/NewsBreak_26.21.0/report.en.md
- https://github.com/Siestazzz/myVulnDB/tree/main/Mobile/NewsBreak_26.21.0

### [CVE-2026-106716](https://github.com/Siestazzz/myVulnDB/blob/main/Mobile/ReelShort_3.8.55/report.en.md)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-106716
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-11-06 00:17:17 JST
- 更新日: 2026-11-06 00:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Android版ReelShortにおけるディープリンク経由のオリジン未検証WebViewロードおよびJavaScriptブリッジの露出。
- 影響: ユーザーが特製リンクを開くことで、ユーザーメタデータや暗号化された資格情報が漏洩する可能性があります。
- 推奨対応: アプリを修正版へ更新し、WebViewにおけるページのオリジン検証およびJavaScriptブリッジのアクセス制限を実施することが推奨されます。

#### References
- https://github.com/Siestazzz/myVulnDB/blob/main/Mobile/ReelShort_3.8.55/report.en.md
- https://github.com/Siestazzz/myVulnDB/tree/main/Mobile/ReelShort_3.8.55

### [CVE-2026-106714](https://github.com/Siestazzz/myVulnDB/blob/main/Mobile/Chewy_26.23.0/report.en.md)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-106714
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-06 00:17:16 JST
- 更新日: 2026-11-06 00:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Android版ChewyのハイブリッドWebViewにおけるディープリンクのホスト検証不備。
- 影響: ユーザーが特製リンクを開くことで、登録されているペットのプロファイル情報がアクセスされ漏洩する可能性があります。
- 推奨対応: アプリを最新の修正版へ更新し、ディープリンクのホスト検証ロジックを強化することが推奨されます。

#### References
- https://github.com/Siestazzz/myVulnDB/blob/main/Mobile/Chewy_26.23.0/report.en.md
- https://github.com/Siestazzz/myVulnDB/tree/main/Mobile/Chewy_26.23.0

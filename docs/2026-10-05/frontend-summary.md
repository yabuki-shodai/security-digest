# Frontend CVE Summary (2026-10-05)

## Overview

- 取得日時: 2026-10-05 09:50:02 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 1
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-105089](https://github.com/WWBN/AVideo/commit/c4adfde13d1f18e3a415722471efdcd8ab480035)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-105089
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-05 01:16:30 JST
- 更新日: 2026-10-05 01:16:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WWBN AVideo（バージョン29.2.0以前）における、動画のtrailer1 URL処理に起因する蓄積型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: アップロード権限を持つユーザーによって注入された悪意あるスクリプトが、閲覧者のブラウザ上で実行される可能性があります。
- 推奨対応: 修正版へのアップデートや、適切に入力値を検証・エスケープする対策が推奨されます。

#### References
- https://github.com/WWBN/AVideo/commit/c4adfde13d1f18e3a415722471efdcd8ab480035
- https://github.com/WWBN/AVideo/security/advisories/GHSA-6wfr-c7fw-4xvw
- https://www.vulncheck.com/advisories/wwbn-avideo-through-29.2.0-stored-xss-via-trailer1-in-youphpflix2-templates

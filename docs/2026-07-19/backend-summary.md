# Backend CVE Summary (2026-07-19)

## Overview

- 取得日時: 2026-07-19 08:05:03 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 5
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-16124](https://github.com/nextlevelbuilder/goclaw/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-16124
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-19 01:17:12 JST
- 更新日: 2026-07-19 01:17:12 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: nextlevelbuilder GoClaw 3.15.0-beta.32以前のCheckSSRF/isPrivateIP関数にサーバーサイドリクエスト偽造（SSRF）の脆弱性が存在します。  
- 影響: リモートから悪用される可能性があり、不正なリクエスト送信による情報漏えいやサービス妨害のリスクがあります。  
- 推奨対応: バージョン3.15.0-beta.33へアップグレードし、該当コンポーネントの修正パッチを適用してください。

#### References
- https://github.com/nextlevelbuilder/goclaw/
- https://github.com/nextlevelbuilder/goclaw/commit/12a0168271827650ddb0026d6277fbadf3dcf3ea
- https://github.com/nextlevelbuilder/goclaw/issues/1218
- https://github.com/nextlevelbuilder/goclaw/pull/1269
- https://github.com/nextlevelbuilder/goclaw/releases/tag/v3.15.0-beta.33

### [CVE-2026-16121](https://github.com/nextlevelbuilder/goclaw/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-16121
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-19 00:17:32 JST
- 更新日: 2026-07-19 00:17:32 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: nextlevelbuilder GoClaw 3.13.2以前のisSafeBin関数に認可不備の脆弱性が存在します。  
- 影響: リモートから不正な操作が可能となる恐れがあり、攻撃コードも公開されています。  
- 推奨対応: 最新バージョンへのアップデートやアクセス制御の見直しを検討してください。

#### References
- https://github.com/nextlevelbuilder/goclaw/
- https://github.com/nextlevelbuilder/goclaw/issues/1206
- https://github.com/nextlevelbuilder/goclaw/issues/1214
- https://vuldb.com/cve/CVE-2026-16121
- https://vuldb.com/submit/856827

### [CVE-2026-16122](https://github.com/nextlevelbuilder/goclaw/)

> **Backend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-16122
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-19 00:17:33 JST
- 更新日: 2026-07-19 00:17:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: nextlevelbuilder GoClaw 3.13.2以前のextractBin/RequestApproval/matchesAllowlist関数に認可不備の脆弱性が存在します。  
- 影響: 不正な操作により誤った認可が行われ、権限のない操作が可能になる恐れがあります。  
- 推奨対応: 最新バージョンへのアップデートや該当機能の利用制限を検討してください。

#### References
- https://github.com/nextlevelbuilder/goclaw/
- https://github.com/nextlevelbuilder/goclaw/issues/1216
- https://github.com/nextlevelbuilder/goclaw/issues/1216#issuecomment-4760050291
- https://vuldb.com/cve/CVE-2026-16122
- https://vuldb.com/submit/856856

### [CVE-2026-16123](https://github.com/nextlevelbuilder/goclaw/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-16123
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-19 00:17:33 JST
- 更新日: 2026-07-19 00:17:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: nextlevelbuilder GoClaw 3.13.2以前のToolsInvokeHandler.ServeHTTP関数に認可欠如の脆弱性が存在します。  
- 影響: リモートからの攻撃により認可が回避され、不正操作が可能になる恐れがあります。  
- 推奨対応: 最新バージョンへのアップデートやアクセス制御の強化を検討してください。

#### References
- https://github.com/nextlevelbuilder/goclaw/
- https://github.com/nextlevelbuilder/goclaw/issues/1217
- https://github.com/nextlevelbuilder/goclaw/issues/1217#issuecomment-4759982122
- https://vuldb.com/cve/CVE-2026-16123
- https://vuldb.com/submit/856857

### [CVE-2026-57848](https://github.com/stoatchat/for-android)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-57848
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-19 05:17:30 JST
- 更新日: 2026-07-19 05:17:30 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Stoat for AndroidのShareTargetActivityが外部から渡されたURIを検証せずに内部ストレージのファイルを添付ファイルとして送信してしまう脆弱性です。  
- 影響: 攻撃者が悪意あるインテントを送信することで、ユーザーの内部データ（データベースや認証トークンなど）が不正に送信される可能性があります。  
- 推奨対応: アプリ側で受信するURIの検証・フィルタリングを実装し、不正なファイルアクセスを防ぐことが望ましいです。

#### References
- https://github.com/stoatchat/for-android
- https://github.com/stoatchat/for-android/commit/50d5f5143940809ebb5a61e5f507c956c33aa970
- https://www.vulncheck.com/advisories/stoat-for-android-internal-file-disclosure-via-exported-sharetargetactivity-uri-validation

# Backend CVE Summary (2026-10-22)

## Overview

- 取得日時: 2026-10-22 09:38:23 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 11
- Critical: 5
- High: 6
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-114136](https://github.com/encode/django-rest-framework/commit/3c2634599b26a9f789b03045118dbc276117611a)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-114136
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-10-22 05:17:25 JST
- 更新日: 2026-10-22 05:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Django REST frameworkのJSONParserにおいて、Content-Typeのcharsetにバイト変換コーデック（bz2等）を許容してしまう問題。
- 影響: サイズ制限チェック後に圧縮されたリクエストが展開され、小規模なデータで大量のメモリが消費される結果、DoS状態を引き起こす可能性があります。
- 推奨対応: Django REST frameworkをバージョン3.18.2以降に更新してください。

#### References
- https://github.com/encode/django-rest-framework/commit/3c2634599b26a9f789b03045118dbc276117611a
- https://github.com/encode/django-rest-framework/releases/tag/3.18.2
- https://github.com/encode/django-rest-framework/security/advisories/GHSA-3547-9m27-7rxg

### [CVE-2026-114138](https://github.com/encode/django-rest-framework/commit/148ab6523922d5a0c110f76615935e5220b63029)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-114138
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-10-22 06:17:56 JST
- 更新日: 2026-10-22 06:17:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Django REST frameworkのコンテンツネゴシエーション処理における過剰なリソース消費の脆弱性。
- 影響: 未認証の遠隔攻撃者により、大量・複雑なAcceptヘッダーを含むリクエストを通じてCPUが高負荷となり、サービス拒否（DoS）を引き起こされる可能性がある。
- 推奨対応: Django REST framework 3.18.2 以降に更新する。

#### References
- https://github.com/encode/django-rest-framework/commit/148ab6523922d5a0c110f76615935e5220b63029
- https://github.com/encode/django-rest-framework/releases/tag/3.18.2
- https://github.com/encode/django-rest-framework/security/advisories/GHSA-33wh-fxxf-88vv

### [CVE-2026-114137](https://github.com/encode/django-rest-framework/commit/af3fabfd517307fbc5d500fba1ab8f6e25f220b0)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-114137
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-10-22 06:17:56 JST
- 更新日: 2026-10-22 06:17:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Django REST frameworkの TokenProxy.delete() が誤ったキーを用いて削除処理を行う不具合。
- 影響: トークン失効処理を行っても実際にはデータベースからトークンが削除されず、有効なまま残ることで意図しないアクセス権限が継続する可能性がある。
- 推奨対応: Django REST framework 3.18.2 以降に更新する。

#### References
- https://github.com/encode/django-rest-framework/commit/af3fabfd517307fbc5d500fba1ab8f6e25f220b0
- https://github.com/encode/django-rest-framework/releases/tag/3.18.2
- https://github.com/encode/django-rest-framework/security/advisories/GHSA-xw6w-gcfp-cf8m

### [CVE-2026-20043](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-snort3-ybgmhTQe)

> **Backend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-20043
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-22 02:18:27 JST
- 更新日: 2026-10-22 03:54:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Snort 3における境界外書き込み（CWE-787）の脆弱性。
- 影響: メモリ破損を引き起こし、任意のコード実行やシステムの停止につながる可能性がある。
- 推奨対応: Ciscoが提供する修正済みのSnort 3バージョンに更新する。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-snort3-ybgmhTQe

### [CVE-2026-76473](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voice-hardening-twgbH9e3)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76473
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-22 02:19:06 JST
- 更新日: 2026-10-22 03:54:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Unified CMなどの複数製品における、不適切なリソース制御（CWE-74）に関する脆弱性。
- 影響: リソースの不適切な制御により、システムの整合性や運用に影響を与える可能性がある。
- 推奨対応: Ciscoが提供する修正済みのソフトウェアバージョンに更新する。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voice-hardening-twgbH9e3

### [CVE-2026-113788](https://github.com/uselagoon/lagoon/releases/tag/v2.33.2)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-113788
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-10-22 01:17:26 JST
- 更新日: 2026-10-22 01:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Lagoon coreのsshサービスにおける任意のコード実行が可能な脆弱性。
- 影響: ユーザーアカウントを持つ攻撃者によって任意のコードが実行され、管理者権限への昇格などに繋がる可能性がある。
- 推奨対応: Lagoon v2.33.2（lagoon-core helm chart v1.62.2）以降に更新する。または回避策としてLagoon coreのsshサービスを無効化する。

#### References
- https://github.com/uselagoon/lagoon/releases/tag/v2.33.2
- https://github.com/uselagoon/lagoon/security/advisories/GHSA-f8mw-q232-qjfp

### [CVE-2026-76474](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voice-hardening-twgbH9e3)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76474
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-22 02:19:07 JST
- 更新日: 2026-10-22 03:54:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Unified CMなどの複数製品における、不適切な認証（CWE-287）に関する脆弱性。
- 影響: 認証の迂回や不正アクセスを許してしまう可能性がある。
- 推奨対応: Ciscoが提供する修正済みのソフトウェアバージョンに更新する。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voice-hardening-twgbH9e3

### [CVE-2026-76475](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voice-hardening-twgbH9e3)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-76475
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-22 02:19:07 JST
- 更新日: 2026-10-22 03:54:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Unified CMなどの複数製品における、Webページ生成時の入力中和不足（CWE-79）に関する脆弱性。
- 影響: Webコンテキスト上で任意のスクリプトが実行される可能性がある。
- 推奨対応: Ciscoが提供する修正済みのソフトウェアバージョンに更新する。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voice-hardening-twgbH9e3

### [CVE-2026-113870](https://www.mongodb.com/docs/compass/release-notes/#mongodb-compass-14915)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-113870
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-22 04:17:00 JST
- 更新日: 2026-10-22 04:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Compassにおける、BSON値の不十分なエスケープ処理に関する脆弱性。
- 影響: 細工されたビューを編集用に開いた際、Compassを実行しているユーザーの権限で任意コードが実行される可能性がある。
- 推奨対応: 修正されたバージョンのMongoDB Compassに更新する。

#### References
- https://www.mongodb.com/docs/compass/release-notes/#mongodb-compass-14915

### [CVE-2026-20236](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-snort3-ybgmhTQe)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-20236
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-22 02:18:28 JST
- 更新日: 2026-10-22 03:54:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Snort 3における不正確な計算（CWE-682）に関する脆弱性。
- 影響: 計算結果の誤りにより、システムの誤動作や不具合を引き起こす可能性がある。
- 推奨対応: Ciscoが提供する修正済みのSnort 3バージョンに更新する。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-snort3-ybgmhTQe

### [CVE-2026-20291](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-snort3-ybgmhTQe)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-20291
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-22 02:18:28 JST
- 更新日: 2026-10-22 03:54:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Snort 3における不適切な特権管理（CWE-269）の脆弱性。
- 影響: 本来制限されるべき権限の昇格や不正な操作が行われる可能性がある。
- 推奨対応: Ciscoが提供する修正済みのSnort 3バージョンに更新する。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-snort3-ybgmhTQe

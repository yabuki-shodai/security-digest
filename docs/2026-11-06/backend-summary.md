# Backend CVE Summary (2026-11-06)

## Overview

- 取得日時: 2026-11-06 11:18:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 6
- Critical: 0
- High: 1
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-81734](https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-81734
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-11-06 00:17:23 JST
- 更新日: 2026-11-06 00:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache OFBizのProductEventsにおける認可欠如の脆弱性。
- 影響: カタログ閲覧権限のみを持つ認証済み攻撃者が、製品やカテゴリ関連付けデータを不正に作成・変更・削除できる可能性があります。
- 推奨対応: Apache OFBiz 24.09.08 以降へアップデートすることが推奨されます。

#### References
- https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz

### [CVE-2026-81808](https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-81808
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-11-06 00:17:26 JST
- 更新日: 2026-11-06 00:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache OFBizのProductSearchEventsにおける認可欠如の脆弱性。
- 影響: カタログ閲覧権限のみを持つ認証済み攻撃者が、検索結果に対する製品カテゴリや機能の関連付けを一括で変更・削除・追加できる可能性があります。
- 推奨対応: Apache OFBiz 24.09.08 以降へアップデートすることが推奨されます。

#### References
- https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz

### [CVE-2026-119744](https://community.thinlinc.com/t/thinlinc-4-15-1-through-4-20-1-security-release/1985)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-119744
- 関連キーワード: gin, aws
- 影響製品: -
- 公開日: 2026-11-06 00:17:20 JST
- 更新日: 2026-11-06 02:17:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cendio ThinLincのWebクライアント（tlwebaccess）における複数ステップ認証の迂回脆弱性。
- 影響: 認証済みの攻撃者がrootを含む他の任意ユーザーになりすまし、不正アクセスや権限昇格を行う可能性があります。
- 推奨対応: 影響を受けるバージョン（4.1.0〜4.20.0）を使用している場合は、修正済みバージョンへアップデートすることが推奨されます。

#### References
- https://community.thinlinc.com/t/thinlinc-4-15-1-through-4-20-1-security-release/1985
- https://community.thinlinc.com/t/urgent-thinlinc-security-issue/1970
- https://www.vulncheck.com/advisories/cendio-thinlinc-improper-authentication-via-web-access

### [CVE-2026-81815](https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-81815
- 関連キーワード: gin, postgresql, mysql
- 影響製品: -
- 公開日: 2026-11-06 00:17:26 JST
- 更新日: 2026-11-06 00:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MySQL/MariaDBを使用したApache OFBiz環境におけるperformFindサービスのSQLインジェクション脆弱性。
- 影響: 遠隔の未認証の攻撃者により、対象エンティティから任意の行データが参照・漏洩させられる可能性があります。
- 推奨対応: Apache OFBiz 24.09.08 以降へアップデートすることが推奨されます。

#### References
- https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz

### [CVE-2026-73578](https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-73578
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-11-06 00:17:22 JST
- 更新日: 2026-11-06 00:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache OFBizのRequestHandler.renderViewにおけるアクセス制御（認可）のバイパス脆弱性。
- 影響: 遠隔の未認証の攻撃者が保護されたビューの認証要求を迂回し、関連する業務データを閲覧できる可能性があります。
- 推奨対応: Apache OFBiz 24.09.08 以降へアップデートすることが推奨されます。

#### References
- https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz

### [CVE-2026-74841](https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74841
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-11-06 00:17:22 JST
- 更新日: 2026-11-06 00:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache OFBizのマルチテナント環境における非実在テナント名キャッシュ処理に起因するリソース管理の不備。
- 影響: 未認証の攻撃者が無効なテナントIDを大量送信することでメモリやデータベースの負荷を著しく増大させ、サービス拒否（DoS）を引き起こす可能性があります。
- 推奨対応: 修正パッチの適用や最新版へのアップデートなど、制限処理を含む対策を講じることが推奨されます。

#### References
- https://lists.apache.org/thread.html/7b2syzksp7klt9fvhdg0olldvs2g83lz

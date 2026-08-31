# Backend CVE Summary (2026-08-31)

## Overview

- 取得日時: 2026-08-31 09:28:59 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 12
- Critical: 1
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-82556](https://codeberg.org/forgejo/forgejo/commit/b313bb83f5ff22bcc0378e0e0ca7bbd58303f168)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-82556
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-31 03:17:00 JST
- 更新日: 2026-08-31 03:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was found in Forgejo up to 15.0.4. This issue affects the function net.LookupIP of the file services/migrations/allowlist/is_migrate_allowed.go of the component Repository Migration Handler. Performing a manipulation results in server-side request forgery. The attack can be initiated remotely. The explo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://codeberg.org/forgejo/forgejo/commit/b313bb83f5ff22bcc0378e0e0ca7bbd58303f168
- https://codeberg.org/forgejo/forgejo/issues/13433
- https://codeberg.org/forgejo/forgejo/pulls/13490
- https://vuldb.com/cve/CVE-2026-82556
- https://vuldb.com/submit/891889

### [CVE-2026-82650](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-9jfx-rc58-h23j)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-82650
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-31 00:16:45 JST
- 更新日: 2026-08-31 00:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SiYuan 3.8.0 contains a path traversal / sensitive file exposure vulnerability in the RenderTemplate function (kernel/model/template.go), reachable via the POST /api/template/render endpoint (kernel/api/template.go). The endpoint restricts the supplied path only to the workspace directory (util.IsAbsPathInWorkspace) bu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-9jfx-rc58-h23j
- https://www.vulncheck.com/advisories/siyuan-before-3.8.1-path-traversal-via-api-template-render

### [CVE-2026-82651](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-3cm4-ccvw-6xr6)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-82651
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-31 00:16:45 JST
- 更新日: 2026-08-31 00:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SiYuan before v3.8.1 does not apply the IsForbiddenAbsPath guard (introduced in GHSA-c8r8-95hg-mp34) to the /history/*path and /repo/diff/*path endpoints in kernel/server/serve.go. These routes require admin authentication but construct file paths independently, so an authenticated administrator can retrieve historical...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-3cm4-ccvw-6xr6
- https://www.vulncheck.com/advisories/siyuan-before-3.8.1-missing-authorization-via-history-and-repo-diff

### [CVE-2026-78699](https://cna.erlef.org/cves/CVE-2026-78699.html)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-78699
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-08-31 01:16:42 JST
- 更新日: 2026-08-31 01:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ash_postgresにおけるマルチテナント名変更処理の戻り値未検証の脆弱性。
- 影響: テナント名変更時にエラーを無視して処理が続行され、衝突した既存テナントのスキーマにリポイントされて他テナントのデータアクセスが可能になる。
- 推奨対応: 対象ライブラリの最新版へのアップデート、または rename_tenant/3 の戻り値チェック処理の修正を行う。

#### References
- https://cna.erlef.org/cves/CVE-2026-78699.html
- https://github.com/ash-project/ash_postgres/commit/8544ab15fe45784553c2d2da8ee1a388eee0174b
- https://github.com/ash-project/ash_postgres/security/advisories/GHSA-6fqq-j9c4-5766
- https://osv.dev/vulnerability/EEF-CVE-2026-78699

### [CVE-2026-82553](https://github.com/sambitraj/STUDENT-MANAGEMENT-SYSTEM/issues/6)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-82553
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-08-31 02:16:39 JST
- 更新日: 2026-08-31 02:16:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Student Management Systemのダッシュボード機能における不適切な認可の脆弱性。
- 影響: 遠隔の攻撃者が roll_no パラメータを操作することで、認証・認可を回避して他者のデータに不正アクセスする可能性がある。
- 推奨対応: 処理実行時におけるアクセス権限検証の実装、および公式修正の確認と適用を行う。

#### References
- https://github.com/sambitraj/STUDENT-MANAGEMENT-SYSTEM/issues/6
- https://vuldb.com/cve/CVE-2026-82553
- https://vuldb.com/submit/891600
- https://vuldb.com/vuln/397069
- https://vuldb.com/vuln/397069/cti

### [CVE-2026-82645](https://github.com/WWBN/AVideo/security/advisories/GHSA-c4w3-h888-7ccv)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-82645
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-31 00:16:44 JST
- 更新日: 2026-08-31 00:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AVideoにおける暗号化トークン検証不備による認証バイパスおよび配信資格情報漏洩の脆弱性。
- 影響: 未認証の攻撃者が暗号化オラクル等を利用してトークンを偽造し、任意ユーザーの外部配信プラットフォーム用資格情報（stream_key, stream_url）を取得できる。
- 推奨対応: 修正パッチの適用、ならびに該当エンドポイント（getLiveKey.json.php）における適切なユーザー検証と暗号化処理の更新を行う。

#### References
- https://github.com/WWBN/AVideo/security/advisories/GHSA-c4w3-h888-7ccv
- https://www.vulncheck.com/advisories/avideo-unauthenticated-stream-credential-disclosure-via-forgeable-token

### [CVE-2026-82644](https://github.com/WWBN/AVideo/security/advisories/GHSA-6893-mcgv-9p2x)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-82644
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-31 00:16:44 JST
- 更新日: 2026-08-31 00:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WWBN AVideoのレートリミット処理におけるボット判定起因の制限回避の脆弱性。
- 影響: User-Agentヘッダーの省略や変更によって試行回数のカウントが無視され、無制限のブルートフォース（パスワード推測）攻撃が可能になる。
- 推奨対応: enforceRateLimit() および isBot() の処理ロジックを修正した最新コードへ更新する。

#### References
- https://github.com/WWBN/AVideo/security/advisories/GHSA-6893-mcgv-9p2x
- https://www.vulncheck.com/advisories/wwbn-avideo-brute-force-rate-limiting-bypass-via-missing-user-agent

### [CVE-2026-82657](https://github.com/Admidio/admidio/security/advisories/GHSA-mg9h-42f8-2pmm)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-82657
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-31 00:16:46 JST
- 更新日: 2026-08-31 00:16:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AdmidioにおけるRSSフィードエンドポイントのアクセス制御不備の脆弱性。
- 影響: 未認証の第三者が rss/forum.php や rss/announcements.php にアクセスし、制限されたフォーラム投稿や告知情報を取得できる。
- 推奨対応: Admidio 5.0.12 以降のバージョンへアップデートする。

#### References
- https://github.com/Admidio/admidio/security/advisories/GHSA-mg9h-42f8-2pmm
- https://www.vulncheck.com/advisories/admidio-before-5.0.12-authentication-bypass-via-rss-feeds

### [CVE-2026-82550](https://github.com/magma/magma/issues/16023)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-82550
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-31 01:16:43 JST
- 更新日: 2026-08-31 01:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linux Foundation MagmaのNGSetupRequestハンドラーにおける不適切な入力検証の脆弱性。
- 影響: 引数 NG-IoT-DefaultPagingDRX の操作により、リクエスト処理の不具合やサービス障害などが引き起こされる可能性がある。
- 推奨対応: 公式リポジトリ等の修正パッチ情報を確認し、入力検証ロジックの修正を適用する。

#### References
- https://github.com/magma/magma/issues/16023
- https://vuldb.com/cve/CVE-2026-82550
- https://vuldb.com/submit/891576
- https://vuldb.com/vuln/397066
- https://vuldb.com/vuln/397066/cti

### [CVE-2026-82643](https://github.com/WWBN/AVideo/security/advisories/GHSA-gxxj-32wm-g48f)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-82643
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-31 00:16:44 JST
- 更新日: 2026-08-31 00:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WWBN AVideoの認証プレ承認APIにおけるレート制限不足およびGETリクエスト処理の脆弱性。
- 影響: 攻撃者が無制限に認証試行を行い、大量の2要素認証メールの送信引き起こしやパスワード推測攻撃を実行できる。
- 推奨対応: 最新版へアップデートし、資格情報送信におけるGETメソッドの制限およびレートリミットを導入する。

#### References
- https://github.com/WWBN/AVideo/security/advisories/GHSA-gxxj-32wm-g48f
- https://www.vulncheck.com/advisories/wwbn-avideo-unauthenticated-rate-limit-bypass-via-preauthorize-json-php

### [CVE-2026-82647](https://github.com/WWBN/AVideo/security/advisories/GHSA-7h9v-f3gg-r3mq)

> **Backend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-82647
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-31 00:16:45 JST
- 更新日: 2026-08-31 00:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WWBN AVideoのメール送信処理におけるクロスサイトリクエストフォージェリ（CSRF）の脆弱性。
- 影響: 認証済み管理者を悪意のあるページへ誘導することで、サイトの正規アドレスから任意のメールを送信させられ、フィッシングに悪用される。
- 推奨対応: 最新バージョンへ更新し、sendEmail.json.php でのオリジン検証・CSRFトークン検証を強化する。

#### References
- https://github.com/WWBN/AVideo/security/advisories/GHSA-7h9v-f3gg-r3mq
- https://www.vulncheck.com/advisories/wwbn-avideo-cross-site-request-forgery-via-sendemail-json-php

### [CVE-2026-82555](https://github.com/b1uerry/cves/blob/main/TOTOLINK/N600R/TOTOLINK_N600R_predictable-token/poc.py)

> **Backend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-82555
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-31 03:17:00 JST
- 更新日: 2026-08-31 03:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TOTOLINK N600Rの認証ハンドラーにおける不十分なランダム性の脆弱性。
- 影響: 認証処理で生成される値の予測可能性が高まり、攻撃に悪用される可能性がある（ただし攻撃の複雑性は高い）。
- 推奨対応: 最新の修正済みファームウェアへの更新を検討する。

#### References
- https://github.com/b1uerry/cves/blob/main/TOTOLINK/N600R/TOTOLINK_N600R_predictable-token/poc.py
- https://github.com/b1uerry/cves/tree/main/TOTOLINK/N600R/TOTOLINK_N600R_predictable-token
- https://vuldb.com/cve/CVE-2026-82555
- https://vuldb.com/submit/891698
- https://vuldb.com/vuln/397071

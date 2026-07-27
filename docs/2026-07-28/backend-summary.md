# Backend CVE Summary (2026-07-28)

## Overview

- 取得日時: 2026-07-28 08:16:47 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 14
- Critical: 4
- High: 4
- KEV掲載: 1
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-16812](https://www.arista.com/en/support/advisories-notices/security-advisory/24364-security-advisory-0144)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **yes**

- タイトル: CVE-2026-16812: Arista VeloCloud Orchestrator On-Prem OS Command Injection Vulnerability
- 関連キーワード: go
- 影響製品: Arista VeloCloud Orchestrator
- 公開日: 2026-07-28 01:17:03 JST
- 更新日: 2026-07-28 05:16:39 JST
- 出典: NVD / CISA KEV

#### GitHub Models要約

- 日本語要約: Arista VeloCloud Orchestrator On-Premにて、リモート攻撃者が内部機能にアクセス可能なOSコマンドインジェクションの脆弱性。
- 影響: 機密性、完全性、可用性の侵害やホストの制御奪取の恐れ。既にホステッド版は修正済み。
- 推奨対応: 最新のパッチを適用し、リモートアクセス制御を強化すること。

#### References
- https://www.arista.com/en/support/advisories-notices/security-advisory/24364-security-advisory-0144
- https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-16812
- https://www.arista.com/en/support/advisories-notices/security-advisory/24364-security-advisory-0144 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-16812

### [CVE-2026-55953](https://cna.erlef.org/cves/CVE-2026-55953.html)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-55953
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-28 01:17:49 JST
- 更新日: 2026-07-28 04:17:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Erlang/OTP sslクライアントでTLS 1.2以下において、サーバーが選択した暗号スイートの検証不足により匿名暗号スイートが許可される脆弱性。
- 影響: 中間者攻撃により証明書検証が回避され、通信の機密性が損なわれる恐れ。
- 推奨対応: TLS 1.3の利用やライブラリの修正パッチ適用を検討すること。

#### References
- https://cna.erlef.org/cves/CVE-2026-55953.html
- https://github.com/erlang/otp/commit/064e236414614f9085cbbbd6eacf0e43c02d1b4b
- https://github.com/erlang/otp/commit/0a82596d425abe43dc2e0b3d74aa1557ef74051c
- https://github.com/erlang/otp/commit/e6ff938116b2872bccc478af7fefb56627285b77
- https://github.com/erlang/otp/security/advisories/GHSA-c6cw-pr89-w882

### [CVE-2026-16481](https://github.com/googleapis/mcp-toolbox/pull/3453)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-16481
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-28 04:17:14 JST
- 更新日: 2026-07-28 05:16:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: googleapis/mcp-toolboxのcloud-healthcare-fhir-fetch-pageでSSRFと認証情報漏洩の脆弱性。認証済みHTTPリクエストに攻撃者制御のURLが指定可能。
- 影響: OAuthトークンやサービスアカウントの資格情報が漏洩し、PHIなどの機密情報が危険にさらされる可能性。
- 推奨対応: 入力URLの検証強化とツールのアップデートを推奨。

#### References
- https://github.com/googleapis/mcp-toolbox/pull/3453

### [CVE-2026-59251](https://cna.erlef.org/cves/CVE-2026-59251.html)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-59251
- 関連キーワード: go, openssl
- 影響製品: -
- 公開日: 2026-07-28 01:18:03 JST
- 更新日: 2026-07-28 04:17:18 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Erlang/OTPの証明書パス検証でリソース制限がなく、細工された証明書チェーンによりDoSを引き起こす可能性。
- 影響: メモリ枯渇によりVM全体が停止する恐れ。
- 推奨対応: 証明書検証処理の改善やアップデート適用を検討すること。

#### References
- https://cna.erlef.org/cves/CVE-2026-59251.html
- https://github.com/erlang/otp/commit/f04c6bba38de1cf1b1836a7d9a9fbe239bd939e8
- https://github.com/erlang/otp/commit/f8580fc117098c08165f46c26fd0750c5cfb2a90
- https://github.com/erlang/otp/security/advisories/GHSA-622p-qfh6-c352
- https://osv.dev/vulnerability/EEF-CVE-2026-59251

### [CVE-2026-66397](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-mh9w-5hr8-3272)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-66397
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-28 01:18:12 JST
- 更新日: 2026-07-28 04:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: phpMyFAQ 4.1.6未満で、category更新時のexisting_imageフィールドにおけるパストラバーサル検証不足により、認証済み攻撃者が任意ファイル削除を行える。
- 影響: database.phpの削除によりインストールゲートが無効化され、公開セットアップウィザードから新しいスーパ管理者アカウント作成が可能になる。
- 推奨対応: phpMyFAQを4.1.6以降にアップデートする。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-mh9w-5hr8-3272
- https://www.vulncheck.com/advisories/phpmyfaq-before-path-traversal-via-category-image-deletion
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-mh9w-5hr8-3272

### [CVE-2026-66427](https://patchstack.com/database/wordpress/plugin/wp-google-places-review-slider/vulnerability/wordpress-wp-google-review-slider-plugin-18-4-sql-injection-vulnerability?_s_id=cve)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-66427
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-28 00:17:10 JST
- 更新日: 2026-07-28 02:46:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WP Google Review Slider 18.4以前で管理者権限のSQLインジェクション脆弱性が存在する。
- 影響: 管理者権限を持つ攻撃者による不正なSQL操作が可能になる可能性がある。
- 推奨対応: WP Google Review Sliderを最新バージョンに更新する。

#### References
- https://patchstack.com/database/wordpress/plugin/wp-google-places-review-slider/vulnerability/wordpress-wp-google-review-slider-plugin-18-4-sql-injection-vulnerability?_s_id=cve

### [CVE-2026-59729](https://github.com/withastro/astro/commit/5240e26c9dd91f9bc7140dcfacdb48d5a132830d)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-59729
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-28 05:16:40 JST
- 更新日: 2026-07-28 05:16:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Astro 7.0.6未満で、renderHTMLElementの属性名のエスケープ不足によりXSSが発生する可能性がある。
- 影響: 悪意ある属性名によりクロスサイトスクリプティング攻撃が可能になる。
- 推奨対応: Astroを7.0.6以降にアップデートする。

#### References
- https://github.com/withastro/astro/commit/5240e26c9dd91f9bc7140dcfacdb48d5a132830d
- https://github.com/withastro/astro/pull/17251
- https://github.com/withastro/astro/releases/tag/astro@7.0.6
- https://github.com/withastro/astro/security/advisories/GHSA-f48w-9m4c-m7f5

### [CVE-2026-66428](https://patchstack.com/database/wordpress/plugin/wp-google-places-review-slider/vulnerability/wordpress-wp-google-review-slider-plugin-18-4-cross-site-request-forgery-csrf-vulnerability?_s_id=cve)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-66428
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-28 00:17:10 JST
- 更新日: 2026-07-28 02:46:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WP Google Review Slider 18.4以前で認証なしのCSRF脆弱性が存在する。
- 影響: 攻撃者がユーザーの権限で不正なリクエストを実行できる可能性がある。
- 推奨対応: WP Google Review Sliderを最新バージョンに更新する。

#### References
- https://patchstack.com/database/wordpress/plugin/wp-google-places-review-slider/vulnerability/wordpress-wp-google-review-slider-plugin-18-4-cross-site-request-forgery-csrf-vulnerability?_s_id=cve

### [CVE-2026-17531](https://github.com/unitedbyai/droidclaw/)

> **Backend** / **MEDIUM** / CVSS: **5.0** / KEV: **no**

- タイトル: CVE-2026-17531
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-28 02:16:35 JST
- 更新日: 2026-07-28 05:25:13 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: unitedbyai droidclaw 0.5.3以前で、Unsigned Scheduled Callbackの認可回避脆弱性が存在する可能性がある。
- 影響: リモートからの攻撃により認可を回避される恐れがあるが、攻撃は難しいとされる。
- 推奨対応: 開発元の対応状況を確認し、アップデートがあれば適用する。

#### References
- https://github.com/unitedbyai/droidclaw/
- https://github.com/unitedbyai/droidclaw/issues/18
- https://vuldb.com/cve/CVE-2026-17531
- https://vuldb.com/submit/862537
- https://vuldb.com/vuln/383396

### [CVE-2026-47078](https://cna.erlef.org/cves/CVE-2026-47078.html)

> **Backend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-47078
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-28 01:17:07 JST
- 更新日: 2026-07-28 04:17:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Erlang OTPのstdlib zipモジュールで、相対パストラバーサルにより意図しないディレクトリ外へのファイル書き込みが可能な脆弱性がある。
- 影響: 悪意あるzipファイルにより任意の場所にファイルを書き込まれる可能性がある。
- 推奨対応: OTPを29.0.4以降など修正済みバージョンに更新する。

#### References
- https://cna.erlef.org/cves/CVE-2026-47078.html
- https://github.com/erlang/otp/commit/8a933c9c7835b06776d31d17b79b7336627d887a
- https://github.com/erlang/otp/security/advisories/GHSA-rf72-wp7h-jg3x
- https://osv.dev/vulnerability/EEF-CVE-2026-47078
- https://www.erlang.org/doc/system/versions.html#order-of-versions

### [CVE-2026-65925](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-65925
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-28 05:16:41 JST
- 更新日: 2026-07-28 06:17:16 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: JFrog ArtifactoryのCargoリモートリポジトリ読み取り権限を持つユーザーが、意図しないURLへのリクエストをArtifactoryに実行させる可能性がある。
- 影響: 不正なリクエストにより情報漏洩やサービスの誤動作が発生する可能性がある。
- 推奨対応: アクセス権限の見直しや最新のセキュリティパッチ適用を検討する。

#### References
- https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases
- https://docs.jfrog.com/releases/docs/jfrog-security-advisories

### [CVE-2026-48051](https://github.com/papra-hq/papra/security/advisories/GHSA-5g86-85rp-f9hx)

> **Backend** / **LOW** / CVSS: **3.5** / KEV: **no**

- タイトル: CVE-2026-48051
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-07-28 03:16:55 JST
- 更新日: 2026-07-28 03:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Papra 26.5.0未満で、WebhookのSSRF保護がリダイレクト先を検証せず、認証済みユーザーが内部ネットワークへのHTTPリクエストを誘発可能。
- 影響: 内部ネットワークへの不正アクセスや情報漏洩のリスクがある。
- 推奨対応: Papraを26.5.0以降にアップデートする。

#### References
- https://github.com/papra-hq/papra/security/advisories/GHSA-5g86-85rp-f9hx

### [CVE-2025-50455](https://github.com/threatlance-org/security-advisories/blob/main/CVE-2025-50455/advisory.md)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2025-50455
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-07-28 01:16:58 JST
- 更新日: 2026-07-28 03:16:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: EasyAppointments 1.5.1以前の/customers/searchエンドポイントのorder_byパラメータにSQLインジェクションが存在する。
- 影響: 時間ベースのクエリ実行やスキーマ列挙、条件によってはリモートコード実行の可能性がある。
- 推奨対応: EasyAppointmentsを最新バージョンに更新し、入力検証を強化する。

#### References
- https://github.com/threatlance-org/security-advisories/blob/main/CVE-2025-50455/advisory.md
- https://github.com/threatlance-org/security-advisories/blob/main/CVE-2025-50455/poc.py
- https://www.linkedin.com/posts/michael-chesang_cve-securityadvisory-appsec-activity-7360754900827365376-Z-IY
- https://github.com/threatlance-org/security-advisories/blob/main/CVE-2025-50455/advisory.md

### [CVE-2026-55579](https://github.com/pheditor/pheditor/releases/tag/2.0.6)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-55579
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-28 03:16:56 JST
- 更新日: 2026-07-28 05:32:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Pheditor 2.0.1から2.0.6未満で、ハードコードされたデフォルトパスワードadminが存在し、初回ログイン時の変更強制がない。
- 影響: 攻撃者が管理者権限でファイル操作やリモートコード実行を行える可能性がある。
- 推奨対応: Pheditorを2.0.6以降にアップデートし、デフォルトパスワードの変更を徹底する。

#### References
- https://github.com/pheditor/pheditor/releases/tag/2.0.6
- https://github.com/pheditor/pheditor/security/advisories/GHSA-p4h7-p9rj-2pq2
- https://github.com/pheditor/pheditor/security/advisories/GHSA-p4h7-p9rj-2pq2

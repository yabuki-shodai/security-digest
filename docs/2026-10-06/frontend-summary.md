# Frontend CVE Summary (2026-10-06)

## Overview

- 取得日時: 2026-10-06 11:14:16 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 15
- Critical: 1
- High: 9
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-104974](https://github.com/makeplane/plane/commit/1e8f3630c7697129b61eb57f2453f0bf09224920)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-104974
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-10-06 03:17:32 JST
- 更新日: 2026-10-06 05:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Planeにおける無効化されたユーザーアカウントの自動再有効化の脆弱性。アカウントが非アクティブ（is_active=False）に設定されていても既存の認証情報でログインが可能であり、認証成功時に通知なくis_activeがTrueに更新されます。
- 影響: 無効化されたユーザーによる不正ログインや、管理者の意図しないアカウントの再有効化が発生する可能性があります。
- 推奨対応: Planeをバージョン1.4.0以降へアップデートしてください。

#### References
- https://github.com/makeplane/plane/commit/1e8f3630c7697129b61eb57f2453f0bf09224920
- https://github.com/makeplane/plane/commit/6c9dbb50434d16ea00a00d1574723dfd0c3d2446
- https://github.com/makeplane/plane/pull/9290
- https://github.com/makeplane/plane/pull/9304
- https://github.com/makeplane/plane/releases/tag/v1.4.0

### [CVE-2026-105639](https://github.com/makeplane/plane/commit/6220ba990b2276a1a1979d1d5df68f650b8b47ad)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-105639
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-10-06 04:17:18 JST
- 更新日: 2026-10-06 04:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Planeのサインアップ処理におけるメール検証不足およびAPIでの招待トークン不適切な露出。メールアドレスの所有権確認なしでアカウントが作成でき、APIを介して保留中の招待トークンを取得可能です。
- 影響: 未認証の第三者が標的のメールアドレスでアカウントを作成し、保留中の招待トークンを取得・承諾してワークスペースへ不正に参加する可能性があります。
- 推奨対応: Planeをバージョン1.4.0以降へアップデートしてください。

#### References
- https://github.com/makeplane/plane/commit/6220ba990b2276a1a1979d1d5df68f650b8b47ad
- https://github.com/makeplane/plane/pull/9297
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-4vj8-p63v-8p24

### [CVE-2026-105632](https://github.com/makeplane/plane/commit/e1ef42023ab66b5e722a8750e1bc5ba0d413a3ee)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-105632
- 関連キーワード: vite, graphql
- 影響製品: -
- 公開日: 2026-10-06 03:17:36 JST
- 更新日: 2026-10-06 05:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PlaneのGraphQL joinProjectミューテーションにおける権限検証の不足。リゾルバーがターゲットプロジェクトの可視性（ネットワーク設定）を検証しないため、非公開プロジェクトへの参加制限が機能しません。
- 影響: ワークスペース内の低権限ユーザーが未招待の非公開プロジェクトに参加し、機密データを閲覧・変更できる可能性があります。
- 推奨対応: Planeをバージョン1.4.0以降へアップデートしてください。

#### References
- https://github.com/makeplane/plane/commit/e1ef42023ab66b5e722a8750e1bc5ba0d413a3ee
- https://github.com/makeplane/plane/pull/9333
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-45hc-q4mw-jhxm
- https://github.com/makeplane/plane/security/advisories/GHSA-45hc-q4mw-jhxm

### [CVE-2026-105635](https://github.com/makeplane/plane/commit/4b52dce76e8aa97a8d87166fa8f4441c1cf646b1)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-105635
- 関連キーワード: vite, gin
- 影響製品: -
- 公開日: 2026-10-06 04:17:17 JST
- 更新日: 2026-10-06 04:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Planeのプロジェクト招待エンドポイントにおける不適切なアクセス制御およびトークン検証不足。未認証の呼び出しに対して招待レコード（トークン等）が返却され、承諾エンドポイントでトークンが検証されません。
- 影響: 攻撃者が招待情報のUUIDから宛先メールアドレスを特定してアカウントを登録し、本来の受信者になりすましてプロジェクト招待を不当に承諾する可能性があります。
- 推奨対応: Planeをバージョン1.4.0以降へアップデートしてください。

#### References
- https://github.com/makeplane/plane/commit/4b52dce76e8aa97a8d87166fa8f4441c1cf646b1
- https://github.com/makeplane/plane/pull/9305
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-2r58-hgv7-635q
- https://github.com/makeplane/plane/security/advisories/GHSA-2r58-hgv7-635q

### [CVE-2026-104978](https://github.com/makeplane/plane/commit/14a4c22f94eac1582439e41112213f976c6a6cf7)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-104978
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-10-06 03:17:33 JST
- 更新日: 2026-10-06 03:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Planeにおける招待一覧情報の不適切なアクセス制御とメール検証なしの招待承諾処理。未登録のメールアドレス宛ての招待情報を取得し、メール所有権の確認なしで承認できます。
- 影響: 攻撃者が未登録の宛先メールアドレスでアカウントを作成し、保留中の招待を横取りして対象のワークスペースやプロジェクトへ参加する可能性があります。
- 推奨対応: Planeをバージョン1.4.0以降へアップデートしてください。

#### References
- https://github.com/makeplane/plane/commit/14a4c22f94eac1582439e41112213f976c6a6cf7
- https://github.com/makeplane/plane/pull/9308
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-g36h-p63v-g9c7

### [CVE-2026-105675](https://github.com/TryGhost/Ghost/commit/4fb587e4d49667f929b87f7d6a873ae5e9cc087f)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-105675
- 関連キーワード: vite, node.js
- 影響製品: -
- 公開日: 2026-10-06 05:17:14 JST
- 更新日: 2026-10-06 05:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Ghostにおけるスタッフ招待参照時の不適切なアクセス制御。招待参照権限を持つスタッフユーザーが、保留中の招待に割り当てられたシークレットトークンを取得できます。
- 影響: 低権限のスタッフユーザーが自分より上位の権限を持つ保留中の招待を承諾し、権限昇格を行う可能性があります。
- 推奨対応: Ghostをバージョン6.64.0以降へアップデートしてください。

#### References
- https://github.com/TryGhost/Ghost/commit/4fb587e4d49667f929b87f7d6a873ae5e9cc087f
- https://github.com/TryGhost/Ghost/pull/30760
- https://github.com/TryGhost/Ghost/releases/tag/v6.64.0
- https://github.com/TryGhost/Ghost/security/advisories/GHSA-v6q3-xqxm-6f5v

### [CVE-2026-105688](https://github.com/penpot/penpot/commit/5efd9cc3c5689485322f57b644b83a3bd2e33cee)

> **Frontend** / **MEDIUM** / CVSS: **6.7** / KEV: **no**

- タイトル: CVE-2026-105688
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-10-06 05:17:18 JST
- 更新日: 2026-10-06 05:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Penpotにおけるチーム招待作成・不当承諾時の権限チェック不足（role-ceiling checkの欠落）。オーナー以外のチーム管理者がオーナー権限を持つ招待を作成・適用できます。
- 影響: チーム管理者が別アカウントへオーナー権限を付与して昇格させ、チームの完全な管理権限を不正に取得する可能性があります。
- 推奨対応: Penpotをバージョン2.18.0以降へアップデートしてください。

#### References
- https://github.com/penpot/penpot/commit/5efd9cc3c5689485322f57b644b83a3bd2e33cee
- https://github.com/penpot/penpot/releases/tag/2.18.0
- https://github.com/penpot/penpot/security/advisories/GHSA-mx4v-cmxq-644v

### [CVE-2026-105630](https://github.com/makeplane/plane/commit/9dff20e04808286acb372119d88c666b802b1d50)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-105630
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-06 03:17:36 JST
- 更新日: 2026-10-06 04:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PlaneにおけるSVG添付ファイルの取り扱い不備による蓄積型クロスサイトスクリプティング（Stored XSS）。アップロードされたSVGのContent-Typeが保持され、`Content-Disposition: inline`で提供されます。
- 影響: MinIOが同一オリジンで運用されている場合、SVG内のスクリプトが同一コンテキストで実行され、管理者等のセッション奪取やアカウント乗っ取りにつながる可能性があります。
- 推奨対応: Planeをバージョン1.4.0以降へアップデートしてください。

#### References
- https://github.com/makeplane/plane/commit/9dff20e04808286acb372119d88c666b802b1d50
- https://github.com/makeplane/plane/pull/9312
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-ch8j-vr4r-qf6h
- https://github.com/makeplane/plane/security/advisories/GHSA-ch8j-vr4r-qf6h

### [CVE-2026-102282](https://github.com/cthackers/adm-zip/commit/6a63c339b83c52915483efacda517660a7a7bf87)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-102282
- 関連キーワード: javascript, gin, node.js, docker
- 影響製品: -
- 公開日: 2026-10-06 02:17:08 JST
- 更新日: 2026-10-06 02:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: adm-zipライブラリにおける解凍時の特殊パーミッション（setuid/setgid/sticky）のフィルタリング不足。`keepOriginalPermission=true`使用時にアーカイブ内のUnix権限ビットがそのまま適用されます。
- 影響: DockerビルドやCI環境などでroot権限により解凍された場合、setuid属性が付与されたファイルが生成され、低権限ユーザーによる実行経由で権限昇格につながる可能性があります。
- 推奨対応: adm-zipをバージョン0.6.1以降へアップデートしてください。

#### References
- https://github.com/cthackers/adm-zip/commit/6a63c339b83c52915483efacda517660a7a7bf87
- https://github.com/cthackers/adm-zip/releases/tag/v0.6.1
- https://github.com/cthackers/adm-zip/security/advisories/GHSA-j5f4-cc29-5x44

### [CVE-2026-105392](https://github.com/lybbn/django-vue-lyadmin/)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-105392
- 関連キーワード: vue, django, go
- 影響製品: -
- 公開日: 2026-10-06 05:17:10 JST
- 更新日: 2026-10-06 05:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Lybbn Django-Vue-Lyadminにおける暗号鍵（SECRET_KEY）のハードコード。`backend/application/settings.py`内でデフォルトのキーがそのまま使用されています。
- 影響: 遠隔の第三者によりJWT署名の偽造や認証の回避が行われ、システムへ不正アクセスされる可能性があります。
- 推奨対応: 本番環境へのデプロイ前に`settings.py`内の`SECRET_KEY`を安全なランダム値に手動で変更してください。

#### References
- https://github.com/lybbn/django-vue-lyadmin/
- https://github.com/lybbn/django-vue-lyadmin/issues/3
- https://vuldb.com/cve/CVE-2026-105392
- https://vuldb.com/submit/982747
- https://vuldb.com/vuln/413586

### [CVE-2026-104979](https://github.com/makeplane/plane/commit/0d58adb69d859fc94c43b9d68fadd77e810d5ed1)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-104979
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-06 03:17:33 JST
- 更新日: 2026-10-06 05:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Plane is an open-source project management tool. Prior to 1.4.0, IntakeIssuePublicViewSet.create in Plane v1.3.1 writes description_html through Issue.objects.create(...) without calling validate_html_content from nh3. Any authenticated user, including a new user with no workspace memberships, can plant arbitrary HTML...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/makeplane/plane/commit/0d58adb69d859fc94c43b9d68fadd77e810d5ed1
- https://github.com/makeplane/plane/pull/9287
- https://github.com/makeplane/plane/releases/tag/v1.4.0
- https://github.com/makeplane/plane/security/advisories/GHSA-hh2r-3hwp-mvq3
- https://github.com/makeplane/plane/security/advisories/GHSA-hh2r-3hwp-mvq3

### [CVE-2026-102426](https://www.joomshaper.com/joomla-extensions/sp-page-builder-pro)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-102426
- 関連キーワード: javascript, echo
- 影響製品: -
- 公開日: 2026-10-06 01:17:04 JST
- 更新日: 2026-10-06 02:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla Extension - joomshaper.com - Reflected XSS in the Dynamic Content Filter addon in SP Page Builder Pro 3.0.0 - 5.6.1p2 - The slider minimum and maximum values are taken from the dc_filter_<fieldId> request parameter, split on the delimiter "l-r", HTML-escaped inside the data-value attribute, and then echoed witho...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.joomshaper.com/joomla-extensions/sp-page-builder-pro

### [CVE-2026-105694](https://github.com/penpot/penpot/commit/c4dd04353fcf06c3e10a64e3d8e43945508ae98c)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-105694
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-06 05:17:19 JST
- 更新日: 2026-10-06 05:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Penpot is an open-source design and prototyping platform. Prior to 2.18.0, authenticated users with file-edit permission can upload SVG media whose scripts, event-handler attributes, and foreignObject elements are stored without sanitization and served as image/svg+xml from the Penpot origin. A victim who navigates to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/penpot/penpot/commit/c4dd04353fcf06c3e10a64e3d8e43945508ae98c
- https://github.com/penpot/penpot/pull/10989
- https://github.com/penpot/penpot/pull/11044
- https://github.com/penpot/penpot/releases/tag/2.18.0
- https://github.com/penpot/penpot/security/advisories/GHSA-wrcr-m7p8-m2c4

### [CVE-2026-102295](https://access.redhat.com/security/cve/CVE-2026-102295)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-102295
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-06 03:17:31 JST
- 更新日: 2026-10-06 04:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A flaw was found in Quay. A cross-site scripting (XSS) vulnerability in the OAuth callback handler allows a remote attacker to execute arbitrary JavaScript code within a user's browser session. By tricking a logged-in user into visiting a specially crafted link, an attacker can exploit improper input sanitization to ru...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-102295
- https://bugzilla.redhat.com/show_bug.cgi?id=2542699

### [CVE-2026-89039](https://grafana.com/security/security-advisories/cve-2026-89039)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-89039
- 関連キーワード: playwright
- 影響製品: -
- 公開日: 2026-10-06 00:17:23 JST
- 更新日: 2026-10-06 05:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A caller who can invoke the convert_playwright_script prompt in mcp-k6 can pass a bare file path as the playwright_script argument and receive the contents of any file readable by the user running the server, including SSH keys and cloud credentials in that user's home directory (path traversal). The working-directory...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://grafana.com/security/security-advisories/cve-2026-89039

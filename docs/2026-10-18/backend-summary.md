# Backend CVE Summary (2026-10-18)

## Overview

- 取得日時: 2026-10-18 08:59:00 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 18
- Critical: 0
- High: 6
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-111891](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-6vf7-mrj2-7c37)

> **Backend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-111891
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-18 04:16:30 JST
- 更新日: 2026-10-18 04:16:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: phpMyFAQのグループ権限APIにおけるスコープ検証不足に伴う権限昇格の脆弱性。
- 影響: 限定されたスコープの管理者がグループに全般的なアクセス権を付与し、自らそのグループに参加することで、全言語・カテゴリでの操作権限を獲得する可能性があります。
- 推奨対応: phpMyFAQ 4.2.0-beta 以降の修正済みバージョンへ更新することが推奨されます。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-6vf7-mrj2-7c37
- https://www.vulncheck.com/advisories/phpmyfaq-from-4.2.0-alpha.2-before-4.2.0-beta-privilege-escalation-via-group-permissions-api

### [CVE-2026-111893](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-gv7w-78f6-mcmh)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-111893
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-18 04:16:30 JST
- 更新日: 2026-10-18 04:16:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: phpMyFAQのGroupControllerにおけるカテゴリ制限設定の検証不備による権限昇格の脆弱性。
- 影響: 制限付き管理者が特定のAPIリクエストを送信することで、グループに対して範囲外のカテゴリ権限を付与し、アクセス制御を迂回する可能性があります。
- 推奨対応: phpMyFAQ 4.2.0-beta 以降の修正済みバージョンへ更新することが推奨されます。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-gv7w-78f6-mcmh
- https://www.vulncheck.com/advisories/phpmyfaq-4.2.0-alpha-before-4.2.0-beta-privilege-escalation-via-group-category-restrictions-api

### [CVE-2026-111897](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-hj8v-cg6r-gg6q)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-111897
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-18 04:16:31 JST
- 更新日: 2026-10-18 04:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: phpMyFAQの添付ファイル管理機能における不適切な認可処理の脆弱性。
- 影響: 権限が限定された編集者が任意のレコードIDを指定することで、担当外のFAQにあるファイルを改ざんまたは削除できる可能性があります。
- 推奨対応: phpMyFAQ 4.2.0-beta 以降の修正済みバージョンへ更新することが推奨されます。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-hj8v-cg6r-gg6q
- https://www.vulncheck.com/advisories/phpmyfaq-4.2.0-alpha-before-4.2.0-beta-authorization-bypass-in-attachment-administration-endpoints

### [CVE-2026-111928](https://github.com/coder/coder/security/advisories/GHSA-7v78-w67v-pm2g)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-111928
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-18 04:16:35 JST
- 更新日: 2026-10-18 04:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Coderのアクセス制御ルールにおける組織所属チェックの不備による認可回避の脆弱性。
- 影響: 組織から削除されたユーザーの個別アクセス設定が残存し、削除後もAPI経由で過去の組織リソース（テンプレート等）へアクセスし続けられる可能性があります。
- 推奨対応: Coder 2.34.8 以降の修正済みバージョンへ更新することが推奨されます。

#### References
- https://github.com/coder/coder/security/advisories/GHSA-7v78-w67v-pm2g
- https://www.vulncheck.com/advisories/coder-2.0.0-before-2.34.8-authorization-bypass-via-user-level-acl-in-rbac-policy

### [CVE-2026-111916](https://github.com/Admidio/admidio/security/advisories/GHSA-552r-jc93-7qr3)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-111916
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-18 04:16:34 JST
- 更新日: 2026-10-18 04:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AdmidioのRSSフィード出力処理におけるカテゴリ閲覧制限フィルターの欠落による情報漏洩の脆弱性。
- 影響: 未認証の第三者がWebリンク用のRSSフィードを取得することで、アクセス制限されたカテゴリのリンク情報や作成者名などを閲覧できる可能性があります。
- 推奨対応: Admidio 5.0.16 以降の修正済みバージョンへ更新することが推奨されます。

#### References
- https://github.com/Admidio/admidio/security/advisories/GHSA-552r-jc93-7qr3
- https://www.vulncheck.com/advisories/admidio-before-5.0.16-information-disclosure-via-rss-links-php-weblinks-feed

### [CVE-2026-111920](https://github.com/go-vikunja/vikunja/security/advisories/GHSA-pjr3-86v4-5p7w)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-111920
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-18 04:16:34 JST
- 更新日: 2026-10-18 04:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vikunjaにおけるプロジェクトアクセス権限計算の不備による不適切なアクセス制御の脆弱性。
- 影響: 親プロジェクトで書き込み権限を持つ協力者が、閲覧専用に設定されたサブプロジェクトのタスクや内容を変更できてしまう可能性があります。
- 推奨対応: 修正内容が含まれる最新バージョンへの更新、または権限設定の再確認が推奨されます。

#### References
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-pjr3-86v4-5p7w
- https://www.vulncheck.com/advisories/vikunja-2.6.0-broken-access-control-via-inherited-project-permissions

### [CVE-2026-111932](https://github.com/coder/coder/security/advisories/GHSA-h58c-xccx-75m3)

> **Backend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-111932
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-18 04:16:36 JST
- 更新日: 2026-10-18 04:16:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Coderの外観設定項目における出力エスケープ不足に伴う蓄積型HTMLインジェクションの脆弱性。
- 影響: Owner権限を持つ攻撃者が意図しないHTMLを注入し、ダッシュボードや他ユーザー宛ての通知メール上で不正な表示を発生させる可能性があります。
- 推奨対応: Coder 2.29.17、2.32.7、2.33.8、2.34.2 以降の修正済みバージョンへ更新することが推奨されます。

#### References
- https://github.com/coder/coder/security/advisories/GHSA-h58c-xccx-75m3
- https://www.vulncheck.com/advisories/coder-before-2.34.2-stored-html-injection-via-appearance-settings

### [CVE-2026-111884](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-7554-gx6g-xx77)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-111884
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-18 04:16:29 JST
- 更新日: 2026-10-18 04:16:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: phpMyFAQのアカウントメールアドレス変更処理における現在のパスワード再認証の欠如による脆弱性。
- 影響: セッションを乗っ取られた場合、現在のパスワードなしでメールアドレスを変更され、パスワードリセット機能を通じてアカウントを奪取される可能性があります。
- 推奨対応: phpMyFAQ 4.1.9 または 4.2.0-beta 以降の修正済みバージョンへ更新することが推奨されます。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-7554-gx6g-xx77
- https://www.vulncheck.com/advisories/phpmyfaq-before-4.1.9-and-4.2.0-alpha-before-4.2.0-beta-missing-current-password-step-up-on-e-mail-change-enables-account-takeover

### [CVE-2026-111895](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-6hhv-gc4g-f4r7)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-111895
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-18 04:16:31 JST
- 更新日: 2026-10-18 04:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: phpMyFAQのMicrosoft Entra ID認証フローにおける認証バイパスの脆弱性。可変なクレームに基づくユーザー紐付けと例外処理の不備に起因します。
- 影響: 攻撃者によりスーパー管理者を含むローカルアカウントが乗っ取られる可能性があります。
- 推奨対応: phpMyFAQ 4.0.0 または 4.2.0-beta 以降の修正済みバージョンへアップデートしてください。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-6hhv-gc4g-f4r7
- https://www.vulncheck.com/advisories/phpmyfaq-3.2.0-before-4.0.0-and-4.0.2-before-4.2.0-beta-account-takeover-via-entra-id-preferred-username

### [CVE-2026-111914](https://github.com/Admidio/admidio/security/advisories/GHSA-5f29-r7rj-43mf)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-111914
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-18 04:16:33 JST
- 更新日: 2026-10-18 04:16:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Admidioの『modules/inventory/inventory_data.php』におけるアクセス制御欠如の脆弱性。
- 影響: モジュールが無効化されている場合でも、認証済みユーザーにより在庫項目や保管者名などの情報が閲覧される可能性があります。
- 推奨対応: Admidio 5.0.16 以降のバージョンへアップデートしてください。

#### References
- https://github.com/Admidio/admidio/security/advisories/GHSA-5f29-r7rj-43mf
- https://github.com/Admidio/admidio/security/advisories/GHSA-qfjf-c48f-x87g
- https://www.vulncheck.com/advisories/admidio-5.0.11-before-5.0.16-broken-access-control-via-inventory-data-php

### [CVE-2026-111929](https://github.com/coder/coder/security/advisories/GHSA-hrhj-hpwc-9hmc)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-111929
- 関連キーワード: terraform
- 影響製品: -
- 公開日: 2026-10-18 04:16:35 JST
- 更新日: 2026-10-18 04:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Coderのプロビジョナーデモンにおける『DownloadFile』gRPCハンドラの認可バイパスの脆弱性。
- 影響: 組織スコープのキーを持つ攻撃者により、他組織のTerraformモジュールアーカイブが取得され、インフラ構成情報や機密情報が漏洩する可能性があります。
- 推奨対応: Coder 2.34.8 以降のバージョンへアップデートしてください。

#### References
- https://github.com/coder/coder/security/advisories/GHSA-hrhj-hpwc-9hmc
- https://www.vulncheck.com/advisories/coder-2.30.0-before-2.34.8-cross-organization-file-disclosure-via-downloadfile-rpc

### [CVE-2026-111934](https://github.com/coder/coder/security/advisories/GHSA-vprw-xcrv-287h)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-111934
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-18 04:16:36 JST
- 更新日: 2026-10-18 04:16:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Coderの『ExtractRealIPAddress』ミドルウェアにおけるIPアドレス偽装の脆弱性。クライアントが送信した『X-Forwarded-For』ヘッダーを誤って信頼することに起因します。
- 影響: ログイン等のエンドポイントにおけるレート制限が回避されブルートフォース攻撃を許す可能性や、監査ログのIPアドレスが偽装される可能性があります。
- 推奨対応: Coder 2.34.7 以降のバージョンへアップデートしてください。

#### References
- https://github.com/coder/coder/security/advisories/GHSA-vprw-xcrv-287h
- https://www.vulncheck.com/advisories/coder-before-2.34.7-ip-spoofing-via-x-forwarded-for-header

### [CVE-2024-58398](https://github.com/coder/coder/commit/69c1d981e3131e50d52b01f6a360abadaad699e6)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2024-58398
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-18 04:16:27 JST
- 更新日: 2026-10-18 04:16:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CoderのログインページにおけるリダイレクトURLの検証不備によるオープンリダイレクトの脆弱性。
- 影響: 悪意のあるリンクを経由してユーザーが外部の攻撃者所有サイトに転送され、フィッシング被害に遭う可能性があります。
- 推奨対応: Coder 2.14.4、2.15.3、2.16.1 以降の修正済みバージョンへアップデートしてください。

#### References
- https://github.com/coder/coder/commit/69c1d981e3131e50d52b01f6a360abadaad699e6
- https://github.com/coder/coder/security/advisories/GHSA-wcx9-ccpj-hx3c
- https://www.vulncheck.com/advisories/coder-2.3.1-before-2.16.1-open-redirect-via-login-page-redirect-parameter

### [CVE-2026-111896](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-95fm-rwq4-rxrf)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-111896
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-18 04:16:31 JST
- 更新日: 2026-10-18 04:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: phpMyFAQの『SvgSanitizer』における単一パス処理の不備に起因する格納型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 悪意のあるSVGファイルがアップロードされ、閲覧者のブラウザ上で任意のスクリプトが実行される可能性があります。
- 推奨対応: phpMyFAQ 4.2.0-beta 以降のバージョンへアップデートしてください。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-95fm-rwq4-rxrf
- https://www.vulncheck.com/advisories/phpmyfaq-4.2.0-alpha-before-4.2.0-beta-stored-xss-via-svg-upload-sanitizer-bypass

### [CVE-2026-111900](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-h76j-35m7-3mwq)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-111900
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-18 04:16:31 JST
- 更新日: 2026-10-18 04:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: phpMyFAQの『attachment.php』における認可検証の不備。親FAQの公開状態やアクセス権限を確認していません。
- 影響: 認証されたユーザーにより、下書き状態のFAQに紐付く添付ファイルが不正にダウンロードされる可能性があります。
- 推奨対応: phpMyFAQ 4.1.9 または 4.2.0-beta 以降のバージョンへアップデートしてください。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-h76j-35m7-3mwq
- https://www.vulncheck.com/advisories/phpmyfaq-before-4.1.9-and-4.2.0-alpha-before-4.2.0-beta-draft-faq-attachment-disclosure-via-attachment-php

### [CVE-2026-111930](https://github.com/coder/coder/security/advisories/GHSA-cvrm-2xxr-hpcv)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-111930
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-18 04:16:35 JST
- 更新日: 2026-10-18 04:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Coderの『GET /api/v2/workspaces/{id}/acl』エンドポイントにおける不適切な認可処理の脆弱性。
- 影響: ワークスペースの利用権限を持つユーザーにより、グループメンバーのメールアドレスやステータス等の情報が収集される可能性があります。
- 推奨対応: Coder 2.34.8 以降のバージョンへアップデートしてください。

#### References
- https://github.com/coder/coder/security/advisories/GHSA-cvrm-2xxr-hpcv
- https://www.vulncheck.com/advisories/coder-from-2.26.0-before-2.34.8-information-disclosure-via-workspace-acl-endpoint

### [CVE-2026-111931](https://github.com/coder/coder/security/advisories/GHSA-98qx-9p2x-c4wh)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-111931
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-18 04:16:36 JST
- 更新日: 2026-10-18 04:16:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Coderの『handleAPIKeySmuggling』におけるパス検証不足に起因するオープンリダイレクトの脆弱性。
- 影響: 信頼されたサブドメイン上の特定のパスを介して、ユーザーが悪意のある外部サイトへ誘導される可能性があります。
- 推奨対応: Coder 2.34.8 以降のバージョンへアップデートしてください。

#### References
- https://github.com/coder/coder/security/advisories/GHSA-98qx-9p2x-c4wh
- https://www.vulncheck.com/advisories/coder-2.0.0-before-2.34.8-open-redirect-via-workspace-app-proxy

### [CVE-2026-111933](https://github.com/coder/coder/security/advisories/GHSA-8fxq-53rx-ph5f)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-111933
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-18 04:16:36 JST
- 更新日: 2026-10-18 04:16:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Coderにおけるパスワード検証処理の不備によるユーザー列挙の脆弱性。空のパスワードハッシュに対して固定値のハッシュを代用していることに起因します。
- 影響: 未認証の攻撃者が応答コードの違いを利用して、有効なアカウントの存在やSSO利用状況を特定できる可能性があります。
- 推奨対応: Coder 2.29.17、2.32.7、2.33.8、2.34.2 以降の修正済みバージョンへアップデートしてください。

#### References
- https://github.com/coder/coder/security/advisories/GHSA-8fxq-53rx-ph5f
- https://www.vulncheck.com/advisories/coder-before-2.34.2-user-enumeration-via-login-placeholder-hash

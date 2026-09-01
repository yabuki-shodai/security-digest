# Backend CVE Summary (2026-09-01)

## Overview

- 取得日時: 2026-09-01 10:14:49 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 20
- Critical: 5
- High: 12
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-53552](https://github.com/zhenorzz/goploy/security/advisories/GHSA-26rh-24rg-j3vv)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-53552
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 04:16:50 JST
- 更新日: 2026-09-01 04:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Goploy 1.17.5以前におけるネームスペース所有権検証の欠如による認可バイパスの脆弱性。
- 影響: 権限を持つユーザーが他ネームスペースのファイルを操作・削除したり、GitリモートURLを書き換えて次回デプロイ時にリモートコード実行（RCE）を引き起こす可能性があります。
- 推奨対応: Goploy 1.18.0以降の修正済みバージョンへアップデートすることが推奨されます。

#### References
- https://github.com/zhenorzz/goploy/security/advisories/GHSA-26rh-24rg-j3vv

### [CVE-2026-76133](https://github.com/cisagov/CSAF/blob/develop/csaf_files/OT/white/2026/icsa-26-237-06.json)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76133
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 01:19:12 JST
- 更新日: 2026-09-01 04:18:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Ebyte製品における非推奨ハッシュアルゴリズムの使用に伴う脆弱性。
- 影響: 認証通信の予測や操作により暗号メカニズムの信頼性が低下し、不正アクセスを許す可能性があります。
- 推奨対応: ベンダーから提供される最新のファームウェアや修正の適用を検討してください。

#### References
- https://github.com/cisagov/CSAF/blob/develop/csaf_files/OT/white/2026/icsa-26-237-06.json
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-237-06

### [CVE-2026-61640](https://github.com/ellite/Wallos/commit/b75f13d0ffa3ed7e77e8e79e4b9fd3fc528c98d3)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-61640
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 06:17:17 JST
- 更新日: 2026-09-01 06:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Wallos 4.9.6未満のOIDC設定処理におけるSSRF（サーバーサイドリクエストフォージェリ）の脆弱性。
- 影響: 管理者が設定するOIDC URLの検証が不十分なため、内部ネットワークへのアクセスやクラウドメタデータの取得に悪用される可能性があります。
- 推奨対応: Wallos 4.9.6以降にアップデートすることが推奨されます。

#### References
- https://github.com/ellite/Wallos/commit/b75f13d0ffa3ed7e77e8e79e4b9fd3fc528c98d3
- https://github.com/ellite/Wallos/pull/1092
- https://github.com/ellite/Wallos/releases/tag/v4.9.6
- https://github.com/ellite/Wallos/security/advisories/GHSA-x9x5-gh69-q7cm

### [CVE-2026-72001](https://github.com/fosrl/pangolin/releases/tag/1.22.0)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-72001
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 04:17:10 JST
- 更新日: 2026-09-01 04:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Pangolin 1.22.0未満の共有リンク認証処理における認証バイパスの脆弱性。
- 影響: 単一の有効な共有リンクを持つ攻撃者が任意のリソースに認証可能となり、SSOやパスワード等の認証設定を回避して不正アクセスを行う可能性があります。
- 推奨対応: Pangolin 1.22.0以降にアップデートすることが推奨されます。

#### References
- https://github.com/fosrl/pangolin/releases/tag/1.22.0
- https://www.vulncheck.com/advisories/pangolin-authentication-bypass-via-share-link-endpoint

### [CVE-2026-77348](https://github.com/ellite/Wallos/commit/11eaf402e841a628c68a805694227ce66c45f6f3)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-77348
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 07:17:20 JST
- 更新日: 2026-09-01 07:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Wallos 5.0.0未満のエンドポイントにおけるプロキシ設定の未無効化に伴うSSRF関連の脆弱性。
- 影響: 未認証のエンドポイントでHTTPプロキシ環境変数がそのまま処理され、リクエストの改ざんや不適切な通信を引き起こす可能性があります。
- 推奨対応: Wallos 5.0.0以降にアップデートすることが推奨されます。

#### References
- https://github.com/ellite/Wallos/commit/11eaf402e841a628c68a805694227ce66c45f6f3
- https://github.com/ellite/Wallos/releases/tag/v5.0.0
- https://github.com/ellite/Wallos/security/advisories/GHSA-f8j2-qm83-r2w4
- https://github.com/ellite/Wallos/security/advisories/GHSA-hhjq-82f8-m6rc

### [CVE-2026-53553](http://github.com/zhenorzz/goploy/releases/tag/v1.18.0)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-53553
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 04:16:51 JST
- 更新日: 2026-09-01 05:17:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Goploy 1.18.0未満のバックエンドAPIにおけるパストラバーサルの脆弱性。
- 影響: クライアント側から渡されるファイルパスの検証が不十分なため、意図しないファイルにアクセスされる可能性があります。
- 推奨対応: Goploy 1.18.0以降にアップデートすることが推奨されます。

#### References
- http://github.com/zhenorzz/goploy/releases/tag/v1.18.0
- https://github.com/zhenorzz/goploy/commit/d51aa15ebc0a474d9d71d6c453a0fe798dd5e007
- https://github.com/zhenorzz/goploy/security/advisories/GHSA-4g5x-hcwm-82jw
- https://github.com/zhenorzz/goploy/security/advisories/GHSA-4g5x-hcwm-82jw

### [CVE-2026-61639](https://github.com/ellite/Wallos/commit/b75f13d0ffa3ed7e77e8e79e4b9fd3fc528c98d3)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-61639
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 06:17:17 JST
- 更新日: 2026-09-01 06:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Wallos 4.9.6未満のデータベース復元機能におけるパストラバーサルおよび任意ファイル書き込みの脆弱性。
- 影響: 悪意のあるZIPファイルを解凍させることでWebルート等に任意ファイルを設置され、Webシェルの実行等につながる可能性があります。
- 推奨対応: Wallos 4.9.6以降にアップデートすることが推奨されます。

#### References
- https://github.com/ellite/Wallos/commit/b75f13d0ffa3ed7e77e8e79e4b9fd3fc528c98d3
- https://github.com/ellite/Wallos/pull/1092
- https://github.com/ellite/Wallos/releases/tag/v4.9.6
- https://github.com/ellite/Wallos/security/advisories/GHSA-3vg2-cxpg-m43g

### [CVE-2026-82808](https://github.com/xryj920/chrome_extensions/blob/main/The%20Inbox%20Foundry%20Limited%20ActiveInbox%207.10.24%20ships%20a%20hardcoded%20Google%20OAuth%20client%20secret%20in%20the%20Chrome%20extension%20bundle)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-82808
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 02:17:46 JST
- 更新日: 2026-09-01 05:56:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Chrome向けActiveInbox拡張機能 7.10.24以下におけるハードコードされた資格情報の脆弱性。
- 影響: 公開されたGoogle OAuth Client Secretが攻撃者に悪用される可能性があります。
- 推奨対応: 拡張機能を最新版へ更新するか、ベンダーの最新情報を確認してください。

#### References
- https://github.com/xryj920/chrome_extensions/blob/main/The%20Inbox%20Foundry%20Limited%20ActiveInbox%207.10.24%20ships%20a%20hardcoded%20Google%20OAuth%20client%20secret%20in%20the%20Chrome%20extension%20bundle
- https://vuldb.com/cve/CVE-2026-82808
- https://vuldb.com/submit/874121
- https://vuldb.com/vuln/397227
- https://vuldb.com/vuln/397227/cti

### [CVE-2026-82815](https://github.com/BiBi8BoBo/megaease_easeprobe-unvalidated-X-Forwarded-For-header)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-82815
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 03:17:24 JST
- 更新日: 2026-09-01 03:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MegaEase EaseProbe 2.3.0以下におけるIPヘッダー処理の不備によるアクセス制御バイパスの脆弱性。
- 影響: X-Forwarded-For等のHTTPヘッダーを偽装されることで、IPベースのアクセス制限を回避される可能性があります。
- 推奨対応: 最新版へのアップデートや、前段のリバースプロキシでのヘッダー検証・削除を検討してください。

#### References
- https://github.com/BiBi8BoBo/megaease_easeprobe-unvalidated-X-Forwarded-For-header
- https://vuldb.com/cve/CVE-2026-82815
- https://vuldb.com/submit/875371
- https://vuldb.com/vuln/397232
- https://vuldb.com/vuln/397232/cti

### [CVE-2026-82908](https://drive.google.com/file/d/10o_-3GOMAvl3tDqQIWYw45rv7MpxYitk/view)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-82908
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 06:17:54 JST
- 更新日: 2026-09-01 06:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MSI Dragon Center 2.0.155.0以下における整数オーバーフローの脆弱性。
- 影響: ローカルの攻撃者が特定ドライバの関数引数を操作することで、システムの異常動作や権限昇格等を引き起こす可能性があります。
- 推奨対応: 最新バージョンへの更新またはアクセス権限の制限を検討してください。

#### References
- https://drive.google.com/file/d/10o_-3GOMAvl3tDqQIWYw45rv7MpxYitk/view
- https://vuldb.com/cve/CVE-2026-82908
- https://vuldb.com/submit/877502
- https://vuldb.com/vuln/397288
- https://vuldb.com/vuln/397288/cti

### [CVE-2026-82957](https://vuldb.com/cve/CVE-2026-82957)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-82957
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 07:17:34 JST
- 更新日: 2026-09-01 07:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was found in hyperledger-firefly firefly up to 1.4.0. The impacted element is the function ValidateOptions of the file internal/events/webhooks/webhooks.go of the component Webhook Subscription. Performing a manipulation of the argument url results in server-side request forgery. Remote exploitation of...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://vuldb.com/cve/CVE-2026-82957
- https://vuldb.com/submit/879847
- https://vuldb.com/vuln/397306
- https://vuldb.com/vuln/397306/cti

### [CVE-2026-53508](https://github.com/oasdiff/oasdiff/pull/832)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-53508
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 04:16:50 JST
- 更新日: 2026-09-01 04:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: oasdiff is a command-line and Go package that compares and detects breaking changes in OpenAPI specs. From version 1.13.2 through version 1.18.0, oasdiff did not enforce --allow-external-refs=false (library: openapi3.Loader.IsExternalRefsAllowed = false) when loading a spec from a git revision (the rev:path form, e.g....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/oasdiff/oasdiff/pull/832
- https://github.com/oasdiff/oasdiff/pull/974
- https://github.com/oasdiff/oasdiff/pull/975
- https://github.com/oasdiff/oasdiff/security/advisories/GHSA-2jcc-mxv7-p3f9

### [CVE-2026-82834](https://drive.google.com/file/d/1qRWtrUHfr-huJlr-Tb8zFj3pIg8Jnwhk/view?usp=drive_link)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-82834
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-01 05:17:15 JST
- 更新日: 2026-09-01 05:56:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security flaw has been discovered in Doccano Open Source Annotation Tools for Machine Learning Practitioners and Auto Labeling Pipeline Module to Annotate a Document Automatically up to 1.8.5. This affects the function LabelList of the file /v1/projects/1/category-types of the component Bulk-Delete Endpoint. Performi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://drive.google.com/file/d/1qRWtrUHfr-huJlr-Tb8zFj3pIg8Jnwhk/view?usp=drive_link
- https://vuldb.com/cve/CVE-2026-82834
- https://vuldb.com/submit/876639
- https://vuldb.com/vuln/397246
- https://vuldb.com/vuln/397246/cti

### [CVE-2026-82397](https://github.com/tornadoweb/tornado/commit/8d6363ed7b69d5f0da806efe34d256627a2191de)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-82397
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-01 07:17:22 JST
- 更新日: 2026-09-01 07:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tornado is a Python web framework and asynchronous networking library. Prior to 6.5.8, Tornado parses application/x-www-form-urlencoded request bodies with urllib.parse.parse_qs in tornado/escape.py without passing max_num_fields. RequestHandler._execute in tornado/web.py parses the body before handler dispatch through...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/tornadoweb/tornado/commit/8d6363ed7b69d5f0da806efe34d256627a2191de
- https://github.com/tornadoweb/tornado/pull/3704
- https://github.com/tornadoweb/tornado/releases/tag/v6.5.8
- https://github.com/tornadoweb/tornado/security/advisories/GHSA-mpf4-983q-p7j4

### [CVE-2026-82398](https://github.com/py-pdf/pypdf/commit/4959848e057e37c218dccad7465259210923faaa)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-82398
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-01 07:17:23 JST
- 更新日: 2026-09-01 07:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pypdf is a free and open-source pure-python PDF library. Prior to 6.15.0, an attacker can craft a PDF that causes long runtimes when the pypdf/_utils.py function read_until_whitespace reads a stream containing a long run of bytes without whitespace. The function repeatedly performs immutable bytes concatenation in a on...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/py-pdf/pypdf/commit/4959848e057e37c218dccad7465259210923faaa
- https://github.com/py-pdf/pypdf/pull/3947
- https://github.com/py-pdf/pypdf/releases/tag/6.15.0
- https://github.com/py-pdf/pypdf/security/advisories/GHSA-fc8x-2rww-xw9m

### [CVE-2026-79748](https://github.com/samanhappy/mcphub/pull/770)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-79748
- 関連キーワード: gin, docker
- 影響製品: -
- 公開日: 2026-09-01 03:17:20 JST
- 更新日: 2026-09-01 04:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MCPHub is a unified hub for centrally managing and dynamically orchestrating multiple MCP servers/APIs into separate endpoints with flexible routing strategies. Prior to version 0.12.15, the POST /api/servers and PUT /api/servers/:name endpoints in MCPHub create/update MCP server configurations and then immediately spa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/samanhappy/mcphub/pull/770
- https://github.com/samanhappy/mcphub/releases/tag/v0.12.15
- https://github.com/samanhappy/mcphub/security/advisories/GHSA-mx89-jjx9-gjr8
- https://github.com/samanhappy/mcphub/security/advisories/GHSA-mx89-jjx9-gjr8

### [CVE-2026-75132](https://www.vulncheck.com/advisories/wapt-server-sql-injection-via-api-v3-hosts-endpoint)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-75132
- 関連キーワード: express, postgresql
- 影響製品: -
- 公開日: 2026-09-01 01:19:11 JST
- 更新日: 2026-09-01 01:19:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WAPT Server versions 2.6.1.17834 and earlier contains a SQL injection vulnerability in the `columns` parameter of the GET `/api/v3/hosts` endpoint. A remote authenticated user with read-only privileges can inject arbitrary PostgreSQL expressions into the SQL query constructed by WAPT. By exploiting the injection point,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.vulncheck.com/advisories/wapt-server-sql-injection-via-api-v3-hosts-endpoint
- https://www.wapt.fr/en/doc/wapt-changelog.html

### [CVE-2026-75133](https://wordpress.org/plugins/keep-backup-daily/#developers)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-75133
- 関連キーワード: gin, mysql
- 影響製品: -
- 公開日: 2026-09-01 01:19:11 JST
- 更新日: 2026-09-01 04:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Keep Backup Daily plugin for WordPress before 2.1.4 contains a sensitive information exposure vulnerability that allows unauthenticated attackers to trigger a full MySQL database dump by accessing the publicly exposed `kbd_cron_process` parameter without authentication. Attackers can predict the partially predictable d...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://wordpress.org/plugins/keep-backup-daily/#developers
- https://www.vulncheck.com/advisories/keep-backup-daily-wordpress-plugin-sensitive-information-exposure-via-kbd-cron-process

### [CVE-2026-66047](https://profilepress.com/changelog/)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-66047
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-01 00:17:37 JST
- 更新日: 2026-09-01 00:17:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ProfilePress (wp-user-avatar) WordPress plugin before 4.17.2 contains an unauthenticated remote code execution vulnerability that allows unauthenticated attackers to install and activate arbitrary plugins by brute-forcing a weak 32-bit connect token via the ppress_connect_process AJAX handler. Attackers can supply a ca...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://profilepress.com/changelog/
- https://wordpress.org/plugins/wp-user-avatar/
- https://www.vulncheck.com/advisories/profilepress-wordpress-plugin-unauthenticated-arbitrary-plugin-installation-rce

### [CVE-2026-82954](https://vuldb.com/cve/CVE-2026-82954)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-82954
- 関連キーワード: gin, traefik
- 影響製品: -
- 公開日: 2026-09-01 07:17:34 JST
- 更新日: 2026-09-01 07:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was detected in Dokploy up to 0.29.7. This issue affects the function writeTraefikConfigInPath of the file packages/server/src/utils/traefik/application.ts of the component Settings. The manipulation of the argument path results in path traversal. The attack can be launched remotely. The exploit is now...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://vuldb.com/cve/CVE-2026-82954
- https://vuldb.com/submit/879844
- https://vuldb.com/vuln/397303
- https://vuldb.com/vuln/397303/cti

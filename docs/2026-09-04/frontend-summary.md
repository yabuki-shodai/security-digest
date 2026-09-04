# Frontend CVE Summary (2026-09-04)

## Overview

- 取得日時: 2026-09-04 09:00:25 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 10
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-49455](https://github.com/wakujs/waku/releases/tag/v1.0.0-beta.1)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-49455
- 関連キーワード: react, gin
- 影響製品: -
- 公開日: 2026-09-04 04:17:28 JST
- 更新日: 2026-09-04 04:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Waku（1.0.0-beta.1未満）のRSCリクエストディスパッチャにおけるOriginおよびSec-Fetch-Siteヘッダーの検証不備の脆弱性。
- 影響: クロスオリジンの攻撃者が認証済みユーザーのブラウザを介して意図しないサーバーアクションを実行させ、状態を変更させる可能性があります。
- 推奨対応: Waku を 1.0.0-beta.1 以降の修正済みバージョンにアップデートしてください。

#### References
- https://github.com/wakujs/waku/releases/tag/v1.0.0-beta.1
- https://github.com/wakujs/waku/security/advisories/GHSA-75w3-gmqx-993q

### [CVE-2026-49456](https://github.com/wakujs/waku/pull/2090)

> **Frontend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-49456
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-09-04 04:17:28 JST
- 更新日: 2026-09-04 04:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Waku（1.0.0-beta.1未満）の `unstable_redirect()` ヘルパーにおけるURL検証不足によるオープンリダイレクトの脆弱性。
- 影響: 悪意のあるリンクを経由してユーザーを外部ドメインへ誘導され、フィッシングや認証情報・OAuthトークンの窃取につながる可能性があります。
- 推奨対応: Waku を 1.0.0-beta.1 以降の修正済みバージョンにアップデートしてください。

#### References
- https://github.com/wakujs/waku/pull/2090
- https://github.com/wakujs/waku/releases/tag/v1.0.0-beta.1
- https://github.com/wakujs/waku/security/advisories/GHSA-43fc-v873-qw85

### [CVE-2026-85242](https://github.com/Lookyloo/PlaywrightCapture/commit/b912a04f7b190807b5e14e497048896bc5016fb9)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-85242
- 関連キーワード: playwright
- 影響製品: -
- 公開日: 2026-09-04 02:17:30 JST
- 更新日: 2026-09-04 03:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PlaywrightCaptureのファビコン取得機能におけるリダイレクト検証不足によるSSRFの脆弱性。
- 影響: 攻撃者が外部ファビコンURLのリダイレクトを悪用し、内部ネットワークやループバックアドレス等の非公開リソースへリクエストを発生させる可能性があります。
- 推奨対応: リダイレクト先に対しても内部アドレス制限が適用される修正済みバージョンへの更新を行ってください。

#### References
- https://github.com/Lookyloo/PlaywrightCapture/commit/b912a04f7b190807b5e14e497048896bc5016fb9

### [CVE-2026-85227](https://github.com/MISP/MISP/commit/de51a16db)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-85227
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-04 00:17:41 JST
- 更新日: 2026-09-04 01:45:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MISPのイベント属性フィルタリングクエリビルダーにおける不適切なHTMLエスケープ処理による反射型XSSの脆弱性。
- 影響: 細工されたURLを認証済みユーザーにクリックさせることで、ユーザーのセッション権限上で任意のJavaScriptを実行される可能性があります。
- 推奨対応: MISPを修正済みバージョンへアップデートしてください。

#### References
- https://github.com/MISP/MISP/commit/de51a16db

### [CVE-2026-56126](https://docs.netgate.com/downloads/pfSense-SA-26_09.packages.asc)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-56126
- 関連キーワード: javascript, echo
- 影響製品: -
- 公開日: 2026-09-04 00:17:30 JST
- 更新日: 2026-09-04 00:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pfSense Plus（26.07未満）およびCE（2.9.0未満）の `/status_monitoring.php` におけるグラフ設定パラメータのサニタイズ不足による格納型XSSの脆弱性。
- 影響: 特権を持つ攻撃者が悪意のあるスクリプトを全体設定に保存し、対象ページを閲覧した全ユーザーのブラウザ上で実行させる可能性があります。
- 推奨対応: pfSense Plus 26.07 以降、または pfSense CE 2.9.0 以降へ更新してください。

#### References
- https://docs.netgate.com/downloads/pfSense-SA-26_09.packages.asc
- https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html
- https://docs.netgate.com/pfsense/en/latest/releases/26-07.html
- https://www.vulncheck.com/advisories/pfsense-plus-ce-stored-xss-via-status-monitoring-php

### [CVE-2026-82024](https://wordpress.org/plugins/learnpress/#developers)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-82024
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-04 03:17:24 JST
- 更新日: 2026-09-04 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LearnPress WordPressプラグイン（4.4.6未満）におけるクイズ問題の回答タイトル入力不備による格納型XSSの脆弱性。
- 影響: 講師権限を持つユーザーが不審なスクリプトを挿入し、該当クイズを閲覧した受講生や管理者のブラウザ上で実行させる可能性があります。
- 推奨対応: LearnPress プラグインを 4.4.6 以降に更新してください。

#### References
- https://wordpress.org/plugins/learnpress/#developers
- https://www.vulncheck.com/advisories/learnpress-wordpress-plugin-stored-xss-via-quiz-question-answer-titles

### [CVE-2026-85230](https://github.com/MISP/MISP/commit/f04b10001)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-85230
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-04 00:17:41 JST
- 更新日: 2026-09-04 01:45:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MISPダッシュボードの ButtonWidget 設定における保存時のURL検証不足による不正なURL設定の永続化の脆弱性。
- 影響: `javascript:` スキーム等を含むURLが保存され、描画時にユーザーのセッション権限でスクリプトが実行される可能性があります。
- 推奨対応: MISPを修正済みバージョンへアップデートし、設定保存時のURL検証機能を有効化・強化してください。

#### References
- https://github.com/MISP/MISP/commit/f04b10001

### [CVE-2026-56127](https://docs.netgate.com/downloads/pfSense-SA-26_10.webgui.asc)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-56127
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-04 00:17:30 JST
- 更新日: 2026-09-04 00:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pfSense Plus（26.07未満）およびCE（2.9.0未満）の `/firewall_rules_edit.php` におけるルール説明欄のサニタイズ不足による格納型XSSの脆弱性。
- 影響: 挿入されたスクリプトがファイアウォールログ画面（`/status_logs_filter.php`）を閲覧したユーザーのブラウザ上で実行される可能性があります。
- 推奨対応: pfSense Plus 26.07 以降、または pfSense CE 2.9.0 以降へ更新してください。

#### References
- https://docs.netgate.com/downloads/pfSense-SA-26_10.webgui.asc
- https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html
- https://docs.netgate.com/pfsense/en/latest/releases/26-07.html
- https://www.vulncheck.com/advisories/pfsense-plus-ce-stored-xss-via-firewall-rules-edit-php

### [CVE-2026-56128](https://docs.netgate.com/downloads/pfSense-SA-26_11.webgui.asc)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-56128
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-04 00:17:30 JST
- 更新日: 2026-09-04 03:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pfSense Plus（26.07未満）およびCE（2.9.0未満）の `/firewall_schedule_edit.php` におけるスケジュール説明欄のサニタイズ不足による格納型XSSの脆弱性。
- 影響: 挿入されたスクリプトがルール一覧画面（`/firewall_rules.php`）を閲覧したユーザーのブラウザ上で実行される可能性があります。
- 推奨対応: pfSense Plus 26.07 以降、または pfSense CE 2.9.0 以降へ更新してください。

#### References
- https://docs.netgate.com/downloads/pfSense-SA-26_11.webgui.asc
- https://docs.netgate.com/pfsense/en/latest/releases/2-9-0.html
- https://docs.netgate.com/pfsense/en/latest/releases/26-07.html
- https://www.vulncheck.com/advisories/pfsense-plus-ce-stored-xss-via-firewall-schedule-edit-php

### [CVE-2026-84185](https://access.redhat.com/security/cve/CVE-2026-84185)

> **Frontend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-84185
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-04 06:17:22 JST
- 更新日: 2026-09-04 06:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: jwcryptoライブラリのGeneral JSON Serialization JWS署名検証におけるキーID (kid) 識別不備の脆弱性。
- 影響: 有効な鍵を持つ攻撃者がキーIDによる識別処理を不当に回避し、認可チェックを突破できる可能性があります。
- 推奨対応: jwcrypto ライブラリを修正済みバージョンへ更新してください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-84185
- https://bugzilla.redhat.com/show_bug.cgi?id=2526729

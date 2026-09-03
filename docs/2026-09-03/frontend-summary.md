# Frontend CVE Summary (2026-09-03)

## Overview

- 取得日時: 2026-09-03 09:08:08 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 14
- Critical: 3
- High: 8
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-84856](https://github.com/hackerguopeng/cve/tree/main/Rowboat_PreAuth_Body_Buffer_DoS_Report)

> **Frontend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-84856
- 関連キーワード: next.js
- 影響製品: -
- 公開日: 2026-09-03 05:17:42 JST
- 更新日: 2026-09-03 05:17:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: rowboat（0.9.1以前）のComposio Webhookエンドポイントにおける処理不備
- 影響: 遠隔の攻撃者により、サービス拒否（DoS）状態に陥らされる可能性があります。また、実証コードが公開されていると報告されています。
- 推奨対応: rowboat を 0.9.2 以降のバージョンへ更新してください。

#### References
- https://github.com/hackerguopeng/cve/tree/main/Rowboat_PreAuth_Body_Buffer_DoS_Report
- https://github.com/rowboatlabs/rowboat/releases/tag/v0.9.2
- https://vuldb.com/cve/CVE-2026-84856
- https://vuldb.com/submit/886260
- https://vuldb.com/vuln/398131

### [CVE-2026-78689](https://my.f5.com/manage/s/article/K000162602)

> **Frontend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-78689
- 関連キーワード: javascript, go, gin, nginx
- 影響製品: -
- 公開日: 2026-09-03 01:17:25 JST
- 更新日: 2026-09-03 04:23:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NGINX JavaScript (njs) および QuickJS (qjs) の XML モジュールにおける名前空間プレフィックスリスト解析の不備
- 影響: 外部から制御されたプレフィックスリストによりヒープでの境界外書き込みが発生し、ワーカープロセスのクラッシュ（DoS）やメモリ漏洩が引き起こされる可能性があります。
- 推奨対応: 影響を受ける NGINX および njs モジュールを最新の修正済みバージョンへ更新してください。

#### References
- https://my.f5.com/manage/s/article/K000162602

### [CVE-2026-53649](https://github.com/BishopFox/joro/releases/tag/1.1.1)

> **Frontend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-53649
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-03 03:19:59 JST
- 更新日: 2026-09-03 03:19:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joro（1.1.1未満）のローカルAPIにおける認証欠如および不適切なCORS設定
- 影響: オペレーターが悪意のあるWebページを閲覧することで、オペレーターの権限で任意のプラグインが実行され、リモートコード実行（RCE）につながる可能性があります。
- 推奨対応: Joro をバージョン 1.1.1 以降へアップデートしてください。

#### References
- https://github.com/BishopFox/joro/releases/tag/1.1.1
- https://github.com/BishopFox/joro/security/advisories/GHSA-xqhv-chqm-fhcc

### [CVE-2026-53611](https://github.com/AS203038/looking-glass/releases/tag/1.3.5)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-53611
- 関連キーワード: svelte, go, express
- 影響製品: -
- 公開日: 2026-09-03 01:17:18 JST
- 更新日: 2026-09-03 03:19:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Looking Glass（1.3.5未満）の入力検証処理における正規表現の不備
- 影響: 遠隔の攻撃者により、OSコマンド注入攻撃が実行される可能性があります。
- 推奨対応: Looking Glass をバージョン 1.3.5 以降へ更新してください。

#### References
- https://github.com/AS203038/looking-glass/releases/tag/1.3.5
- https://github.com/AS203038/looking-glass/security/advisories/GHSA-8hgf-p844-425m

### [CVE-2026-18329](https://my.f5.com/manage/s/article/K000162599)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-18329
- 関連キーワード: javascript, gin, nginx
- 影響製品: -
- 公開日: 2026-09-03 01:17:14 JST
- 更新日: 2026-09-03 03:19:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NGINX JavaScript (njs) および QuickJS (qjs) エンジンの `js_access` ハンドラにおける非同期アクセス制御エラー処理の不備
- 影響: 例外発生時にアクセス制限が解除される（フェイルオープン）可能性があり、未認証の第三者によって保護されたリソースへアクセスされる恐れがあります。
- 推奨対応: 影響を受ける NGINX JavaScript エンジンを対策済みバージョンへアップデートしてください。

#### References
- https://my.f5.com/manage/s/article/K000162599

### [CVE-2026-84649](https://www.jenkins.io/security/advisory/2026-09-02/#SECURITY-3878)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-84649
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-03 01:17:29 JST
- 更新日: 2026-09-03 03:21:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Jenkinsに含まれるStaplerにおける、動的JavaScriptリソース内へのCSRFトークン埋め込み問題
- 影響: 同一サイトを制御する攻撃者によりCSRFトークンが取得され、該当ユーザーのセッションで不正な操作が行われる可能性があります。
- 推奨対応: Jenkins および Stapler を修正済みバージョンへアップデートしてください。

#### References
- https://www.jenkins.io/security/advisory/2026-09-02/#SECURITY-3878

### [CVE-2026-84665](https://www.jenkins.io/security/advisory/2026-09-02/#SECURITY-3989)

> **Frontend** / **HIGH** / CVSS: **8.0** / KEV: **no**

- タイトル: CVE-2026-84665
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-03 01:17:31 JST
- 更新日: 2026-09-03 03:21:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Jenkins SonarQube Scanner プラグイン（2.18.3以前）におけるダッシュボードリンクのURLスキーム検証不備
- 影響: Item/Configure 権限を持つ攻撃者により `javascript:` スキームが挿入され、蓄積型クロスサイトスクリプティング（XSS）が引き起こされる可能性があります。
- 推奨対応: Jenkins SonarQube Scanner プラグインを修正済みバージョンへ更新してください。

#### References
- https://www.jenkins.io/security/advisory/2026-09-02/#SECURITY-3989

### [CVE-2026-84673](https://www.jenkins.io/security/advisory/2026-09-02/#SECURITY-4104)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-84673
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-03 01:17:31 JST
- 更新日: 2026-09-03 02:18:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Jenkins Customizable Header プラグイン（295.v2544b_ca_19b_97以前）におけるStaplerデータバインディングの不備
- 影響: プラグインの外観設定が上書きされ、インラインJavaScriptを含むSVGアイコンを配置されることで、蓄積型クロスサイトスクリプティング（XSS）が発生する可能性があります。
- 推奨対応: Jenkins Customizable Header プラグインを最新バージョンへ更新してください。

#### References
- https://www.jenkins.io/security/advisory/2026-09-02/#SECURITY-4104

### [CVE-2026-78222](https://my.f5.com/manage/s/article/K000162603)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-78222
- 関連キーワード: javascript, gin, nginx
- 影響製品: -
- 公開日: 2026-09-03 01:17:23 JST
- 更新日: 2026-09-03 04:23:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NGINX JavaScript の `ngx.fetch()` における不正なHTTPレスポンス処理の不備
- 影響: レスポンス内容を制御できる攻撃者により、NGINXワーカープロセスをクラッシュさせられ、サービス拒否（DoS）が引き起こされる可能性があります。
- 推奨対応: 影響を受ける NGINX JavaScript モジュールを対策済みバージョンへアップデートしてください。

#### References
- https://my.f5.com/manage/s/article/K000162603

### [CVE-2026-79990](https://github.com/craftcms/cms)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-79990
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-09-03 00:17:42 JST
- 更新日: 2026-09-03 03:21:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Craft CMS の GraphQL エントリミューテーションにおけるサイト範囲フィルタリングの迂回不備
- 影響: 特定サイトのアクセス権を持つトークンを用いて、アクセス権限のない他サイトのエントリをスコープ外で作成・変更・削除される可能性があります。
- 推奨対応: Craft CMS を修正済みバージョンへ更新してください。

#### References
- https://github.com/craftcms/cms
- https://github.com/craftcms/cms/releases/tag/5.10.11
- https://github.com/craftcms/cms/security/advisories/GHSA-3wcr-p33w-528f
- https://www.hckrt.com/hacktivity/HCKRT-XEQKMX

### [CVE-2026-79991](https://github.com/craftcms/cms)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-79991
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-09-03 00:17:42 JST
- 更新日: 2026-09-03 03:21:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Craft CMSのGraphQLミューテーション（saveEntry、deleteEntry）において、サイト権限のチェックが迂回される脆弱性。
- 影響: 特定のサイト権限を持つ攻撃者が、許可されていない別サイトのエントリを作成、変更、または削除できる可能性があります。
- 推奨対応: Craft CMSを修正パッチが適用された最新バージョンへアップデートしてください。

#### References
- https://github.com/craftcms/cms
- https://github.com/craftcms/cms/releases/tag/5.10.13
- https://github.com/craftcms/cms/security/advisories/GHSA-4mgp-5vf2-7c9m
- https://www.hckrt.com/hacktivity/HCKRT-B5BSMM

### [CVE-2026-75134](https://github.com/Elymaro/CVE/blob/main/WordPress/CVE-2026-75134.md)

> **Frontend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-75134
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-03 05:17:36 JST
- 更新日: 2026-09-03 05:17:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用SEOWritingプラグイン（バージョン1.12.5以下）における、iframeのonload属性の過剰な許可に起因する格納型XSSの脆弱性。
- 影響: 投稿者権限を持つユーザーが悪意のあるJavaScriptを挿入し、それを閲覧した上位権限ユーザーのセッション奪取や権限昇格を引き起こす可能性があります。
- 推奨対応: プラグインを修正済みの最新バージョンへ更新してください。

#### References
- https://github.com/Elymaro/CVE/blob/main/WordPress/CVE-2026-75134.md
- https://wordpress.org/plugins/seowriting/
- https://www.vulncheck.com/advisories/seowriting-wordpress-plugin-stored-xss-via-iframe-onload

### [CVE-2026-66842](https://my.f5.com/manage/s/article/K000162521)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-66842
- 関連キーワード: mui
- 影響製品: -
- 公開日: 2026-09-03 01:17:18 JST
- 更新日: 2026-09-03 04:23:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: F5 BIG-IPの管理インタフェース（TMUI）における、認証済みユーザーによる管理者アカウント作成を許してしまう不適切なアクセス制御の脆弱性。
- 影響: 管理ネットワークにアクセスできる任意のロールの認証済み攻撃者が、管理者アカウントを作成して権限昇格する可能性があります。
- 推奨対応: 修正済みバージョンへアップデートするか、TMUI（管理インタフェース）へのネットワークアクセスを制限してください。

#### References
- https://my.f5.com/manage/s/article/K000162521

### [CVE-2026-19698](https://wpscan.com/vulnerability/0e6cd37e-3004-498d-8d8d-21617138888a/)

> **Frontend** / **LOW** / CVSS: **3.5** / KEV: **no**

- タイトル: CVE-2026-19698
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-03 00:17:37 JST
- 更新日: 2026-09-03 00:17:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用GutenKitプラグイン（2.5.1未満）において、スタイル設定のエスケープ処理不備による任意CSS注入の脆弱性。
- 影響: 投稿者以上の権限を持つユーザーによって任意CSSが注入され、Webサイトの改ざんや外部リソースの不正読み込みが行われる可能性があります。
- 推奨対応: GutenKitプラグインをバージョン2.5.1以降に更新してください。

#### References
- https://wpscan.com/vulnerability/0e6cd37e-3004-498d-8d8d-21617138888a/

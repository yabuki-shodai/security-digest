# Frontend CVE Summary (2026-07-14)

## Overview

- 取得日時: 2026-07-14 08:07:46 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 2
- High: 3
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-59801](https://github.com/decolua/9router/security/advisories/GHSA-vjc7-jrh9-9j86)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-59801
- 関連キーワード: next.js
- 影響製品: -
- 公開日: 2026-07-14 07:16:48 JST
- 更新日: 2026-07-14 07:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 9Router 0.4.41以前のバージョンにおいて、認証ミドルウェアが欠如したAPIエンドポイントへの未認証アクセスにより、リモート攻撃者がプロバイダ管理機能を操作可能な脆弱性が存在します。  
- 影響: 攻撃者は認証情報やOAuthトークン、APIキーの一部を取得したり、AIトラフィックを攻撃者制御下のサーバーにリダイレクトしたり、全プロバイダ接続の削除によるサービス拒否を引き起こす可能性があります。  
- 推奨対応: 速やかに認証ミドルウェアを適用し、APIエンドポイントへのアクセス制御を強化するとともに、影響を受けるバージョンの使用を中止またはアップデートしてください。

#### References
- https://github.com/decolua/9router/security/advisories/GHSA-vjc7-jrh9-9j86
- https://www.vulncheck.com/advisories/9router-unauthenticated-api-exposure-via-api-providers

### [CVE-2026-62327](https://github.com/decolua/9router/security/advisories/GHSA-vjc7-jrh9-9j86)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-62327
- 関連キーワード: next.js
- 影響製品: -
- 公開日: 2026-07-14 07:16:52 JST
- 更新日: 2026-07-14 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 9Router 0.4.41以前のバージョンにおいて、認証なしで/api/usage/statsエンドポイントにアクセスすることで、接続されたAIプロバイダーのAPIキーが平文で漏洩する脆弱性が存在します。  
- 影響: 攻撃者は認証を回避してAPIキーを取得し、不正利用や課金詐欺、クォータの枯渇を引き起こす可能性があります。  
- 推奨対応: 速やかに認証ミドルウェアを適用し、該当バージョンからのアップデートやパッチ適用を行うことが望ましいです。

#### References
- https://github.com/decolua/9router/security/advisories/GHSA-vjc7-jrh9-9j86
- https://www.vulncheck.com/advisories/9router-unauthenticated-api-key-exposure-via-api-usage-stats

### [CVE-2026-62187](https://github.com/openclaw/openclaw/security/advisories/GHSA-2q7j-2vhx-56g8)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-62187
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-07-14 07:16:49 JST
- 更新日: 2026-07-14 07:16:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenClaw Feishu tools（npmパッケージ@openclaw/feishu）バージョン2026.6.6以前で、アカウントごとの無効化設定が無視される脆弱性が存在します。  
- 影響: 低権限の呼び出し元や特定の入力経路から、本来より強い認可が必要な操作を不正に実行される可能性があります。  
- 推奨対応: バージョン2026.6.9以降にアップデートし、設定や入力経路の管理を見直すことを推奨します。

#### References
- https://github.com/openclaw/openclaw/security/advisories/GHSA-2q7j-2vhx-56g8
- https://www.vulncheck.com/advisories/openclaw-feishu-tools-authorization-bypass

### [CVE-2026-58411](https://github.com/ChurchCRM/CRM/security/advisories/GHSA-p6j6-vrpg-4pp8)

> **Frontend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-58411
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-14 07:16:48 JST
- 更新日: 2026-07-14 07:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ChurchCRMの7.4.0未満のバージョンにおいて、ユーザー入力の不適切なエンコードによりクロスサイトスクリプティング（XSS）脆弱性が存在します。  
- 影響: セッション情報の窃取やアカウント乗っ取り、管理者権限の不正取得などのリスクがあり、機密情報の漏洩や不正操作が発生する可能性があります。  
- 推奨対応: 影響を受けるバージョンを使用している場合は、速やかにバージョン7.4.0以降へアップデートすることを推奨します。

#### References
- https://github.com/ChurchCRM/CRM/security/advisories/GHSA-p6j6-vrpg-4pp8

### [CVE-2026-58500](https://github.com/appium/appium-mcp/commit/e222bbbd6fe2b656a320efcd143563f08061a83d)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-58500
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-14 07:16:48 JST
- 更新日: 2026-07-14 07:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: MCP Appiumの1.85.10未満のバージョンで、createLocatorGeneratorUI関数が攻撃者制御の属性を適切にエスケープせずにHTMLテンプレートに埋め込むため、任意のHTMLやJavaScriptが注入される可能性があります。  
- 影響: 攻撃者はMCPクライアント上でスクリプトを実行し、不正にスクリーンショット取得やページソースの読み取りなどのMCPツールを操作できる恐れがあります。  
- 推奨対応: 影響を受けるバージョンを使用している場合は、1.85.10以降にアップデートし、適切な入力検証とエスケープ処理を実施してください。

#### References
- https://github.com/appium/appium-mcp/commit/e222bbbd6fe2b656a320efcd143563f08061a83d
- https://github.com/appium/appium-mcp/security/advisories/GHSA-x975-rgx4-5fh4

### [CVE-2026-49971](https://github.com/plank/laravel-mediable/commit/65046b2162fac23ec5d5e8fbdff01a9a0804003e)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-49971
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-14 04:17:10 JST
- 更新日: 2026-07-14 04:28:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Laravel-Mediable 7.0.0未満において、SVGファイルの不適切なサニタイズにより、認証済み・未認証ユーザーが任意のJavaScriptを実行可能な永続的なクロスサイトスクリプティング（XSS）脆弱性が存在します。  
- 影響: 攻撃者は悪意あるスクリプトをアップロードし、被害者がファイルを開くとセッション情報の窃取やアカウント乗っ取りが発生する可能性があります。  
- 推奨対応: Laravel-Mediableを7.0.0以降にアップデートし、SVGファイルのアップロード時に適切なサニタイズ処理を実施してください。

#### References
- https://github.com/plank/laravel-mediable/commit/65046b2162fac23ec5d5e8fbdff01a9a0804003e
- https://github.com/plank/laravel-mediable/releases/tag/7.0.0
- https://www.vulncheck.com/advisories/laravel-mediable-stored-xss-via-svg-file-upload

### [CVE-2026-58487](https://github.com/hedgedoc/hedgedoc/security/advisories/GHSA-6c2w-8w96-3pcv)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-58487
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-14 07:16:48 JST
- 更新日: 2026-07-14 07:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: HedgeDocの1.11.0以前のバージョンで、登録メールアドレスのローカルパートの不適切な処理により、保存型HTMLインジェクションが発生する可能性があります。  
- 影響: 攻撃者は特殊なメールアドレスを登録し、他ユーザーの閲覧するページに任意のHTMLを注入でき、ページ内容の改変や外部リソースの埋め込みが可能です。  
- 推奨対応: HedgeDocをバージョン1.11.0以降にアップデートし、メールアドレスの処理と表示の安全性を確保してください。

#### References
- https://github.com/hedgedoc/hedgedoc/security/advisories/GHSA-6c2w-8w96-3pcv

### [CVE-2026-58228](https://cna.erlef.org/cves/CVE-2026-58228.html)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-58228
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-14 04:17:30 JST
- 更新日: 2026-07-14 05:37:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: phoenix_live_viewのURL検証に不備があり、攻撃者がJavaScriptを実行できるクロスサイトスクリプティングの脆弱性が存在します。  
- 影響: 悪意あるURLが安全な相対パスとして誤認され、ユーザーのブラウザで任意のスクリプトが実行される可能性があります。  
- 推奨対応: phoenix_live_viewをバージョン1.2.7以降にアップデートし、ユーザー入力のURL検証を強化してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-58228.html
- https://github.com/phoenixframework/phoenix_live_view/commit/86165533e311469a1b62093fd182d9d874de8106
- https://github.com/phoenixframework/phoenix_live_view/security/advisories/GHSA-5cgh-g58j-m9cq
- https://osv.dev/vulnerability/EEF-CVE-2026-58228
- https://github.com/phoenixframework/phoenix_live_view/security/advisories/GHSA-5cgh-g58j-m9cq

### [CVE-2026-61501](https://github.com/rejetto/hfs/releases/tag/v3.2.1)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-61501
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-14 03:16:30 JST
- 更新日: 2026-07-14 04:28:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Rejetto HFS 3.0.0から3.2.0までの管理パネルで、ログエントリがHTMLとして適切にサニタイズされず表示される問題があり、リモートの未認証攻撃者が悪意あるJavaScriptを実行可能です。  
- 影響: 管理者のブラウザ上でスクリプトが実行され、アカウント作成やサーバー上でのコード実行が管理者権限で行われる恐れがあります。  
- 推奨対応: 最新バージョンへのアップデートや、ログ表示時の適切なサニタイズ対策を検討してください。

#### References
- https://github.com/rejetto/hfs/releases/tag/v3.2.1
- https://www.vulncheck.com/advisories/rejetto-hfs-stored-xss-in-admin-log-viewer

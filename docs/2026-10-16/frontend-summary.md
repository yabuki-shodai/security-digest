# Frontend CVE Summary (2026-10-16)

## Overview

- 取得日時: 2026-10-16 09:19:16 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 16
- Critical: 0
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-100409](https://github.com/opennextjs/opennextjs-aws/pull/1199)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-100409
- 関連キーワード: next.js
- 影響製品: -
- 公開日: 2026-10-16 02:17:07 JST
- 更新日: 2026-10-16 03:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenNext Cloudflareにおけるパーセントエンコードされたパス名処理の不整合に伴う認可迂回の脆弱性
- 影響: 未認証の第三者が保護されたルートのキャッシュコンテンツを認可なしで取得する可能性があります。
- 推奨対応: バージョン 1.20.2 以降に更新してください。

#### References
- https://github.com/opennextjs/opennextjs-aws/pull/1199
- https://github.com/opennextjs/opennextjs-aws/pull/1200
- https://github.com/opennextjs/opennextjs-cloudflare/commit/38ea40b669be272ddf09a7df7e70c69d0b57404b
- https://github.com/opennextjs/opennextjs-cloudflare/releases/tag/@opennextjs/cloudflare@1.20.2
- https://github.com/opennextjs/opennextjs-cloudflare/security/advisories/GHSA-2vc4-c4r6-p6v6

### [CVE-2026-104827](https://github.com/reactphp/http/commit/2558622d0b76227c60c61eac8a61572cb6638e8c)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-104827
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-10-16 04:17:14 JST
- 更新日: 2026-10-16 04:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ReactPHP react/http におけるレスポンスヘッダーバッファのサイズ制限不備によるサービス拒否（DoS）の脆弱性
- 影響: 悪意あるリモートサーバーからのデータ受信によりPHPのメモリ制限が枯渇し、アプリケーションプロセスがクラッシュする可能性があります。
- 推奨対応: バージョン 1.11.1 以降に更新してください。

#### References
- https://github.com/reactphp/http/commit/2558622d0b76227c60c61eac8a61572cb6638e8c
- https://github.com/reactphp/http/releases/tag/v1.11.1
- https://github.com/reactphp/http/security/advisories/GHSA-g4f2-2pf3-2pwj

### [CVE-2026-103936](https://github.com/libp2p/js-libp2p/commit/68794c8e2e67d5f38da59e379dc051b2789e46f6)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-103936
- 関連キーワード: javascript, go, node.js
- 影響製品: -
- 公開日: 2026-10-16 03:17:22 JST
- 更新日: 2026-10-16 03:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JavaScript版 libp2p の WebRTC コンポーネントにおける未検証入力によるプロセス強制終了の脆弱性
- 影響: 外部からの単一のUDPパケットによりプロセスが例外終了（SIGABRT）し、サービス拒否（DoS）が発生する可能性があります。
- 推奨対応: バージョン 6.0.28 以降に更新してください。

#### References
- https://github.com/libp2p/js-libp2p/commit/68794c8e2e67d5f38da59e379dc051b2789e46f6
- https://github.com/libp2p/js-libp2p/pull/3584
- https://github.com/libp2p/js-libp2p/releases/tag/webrtc-v6.0.28
- https://github.com/libp2p/js-libp2p/security/advisories/GHSA-x3m2-6mg8-vj7f

### [CVE-2026-57568](https://github.com/LycheeOrg/Lychee/commit/f0604ead5889bfed404d6f5e1a9205f945172c7e)

> **Frontend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-57568
- 関連キーワード: javascript, vue, gin
- 影響製品: -
- 公開日: 2026-10-16 02:17:23 JST
- 更新日: 2026-10-16 06:08:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Lycheeにおける Markdown 内の不適切なリンク許可に起因する格納型クロスサイトスクリプティング（XSS）の脆弱性
- 影響: 閲覧者が表示されたリンクをクリックすることで、ユーザーのブラウザ上で攻撃者のJavaScriptが実行され、セッション情報が漏洩する等の可能性があります。
- 推奨対応: バージョン 7.6.0 以降に更新してください。

#### References
- https://github.com/LycheeOrg/Lychee/commit/f0604ead5889bfed404d6f5e1a9205f945172c7e
- https://github.com/LycheeOrg/Lychee/pull/4377
- https://github.com/LycheeOrg/Lychee/releases/tag/v7.6.0
- https://github.com/LycheeOrg/Lychee/security/advisories/GHSA-pgfr-x389-5p2h

### [CVE-2026-55414](https://github.com/nl-portal/nl-portal-backend-libraries/commit/5ea04ef6445443e22e40a23fbed447e618b70c3f)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-55414
- 関連キーワード: graphql, go
- 影響製品: -
- 公開日: 2026-10-16 03:17:27 JST
- 更新日: 2026-10-16 04:17:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NL Portal Backend Librariesにおける GraphQL Resolver のアクセス制御不備および不適切な URL 検証の脆弱性
- 影響: 未認証の攻撃者により、構成されたホスト上のエンドポイントへ権限トークンを含むリクエストが誘導される可能性があります。
- 推奨対応: 修正されたバージョンへアップグレードしてください。

#### References
- https://github.com/nl-portal/nl-portal-backend-libraries/commit/5ea04ef6445443e22e40a23fbed447e618b70c3f
- https://github.com/nl-portal/nl-portal-backend-libraries/pull/700
- https://github.com/nl-portal/nl-portal-backend-libraries/releases/tag/3.0.4.RELEASE
- https://github.com/nl-portal/nl-portal-backend-libraries/security/advisories/GHSA-xm3x-9cfw-jhx4
- https://github.com/nl-portal/nl-portal-backend-libraries/security/advisories/GHSA-xm3x-9cfw-jhx4

### [CVE-2026-54683](https://github.com/nl-portal/nl-portal-backend-libraries/commit/6e738a876ff9f581991b5b070706100b5516e183)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-54683
- 関連キーワード: graphql, go, gin
- 影響製品: -
- 公開日: 2026-10-16 03:17:27 JST
- 更新日: 2026-10-16 03:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NL Portal Backend Librariesにおけるドキュメント取得時の所有権チェック不備（IDOR）の脆弱性
- 影響: ログイン済みのユーザーが他人のドキュメント識別子を指定することで、個人情報等を含む機密ドキュメントを閲覧する可能性があります。
- 推奨対応: バージョン 3.0.3 以降に更新してください。

#### References
- https://github.com/nl-portal/nl-portal-backend-libraries/commit/6e738a876ff9f581991b5b070706100b5516e183
- https://github.com/nl-portal/nl-portal-backend-libraries/commit/e326e6db862f71f76dd46d3b17cbb5fa6f2fba02
- https://github.com/nl-portal/nl-portal-backend-libraries/pull/684
- https://github.com/nl-portal/nl-portal-backend-libraries/pull/690
- https://github.com/nl-portal/nl-portal-backend-libraries/releases/tag/3.0.3.RELEASE

### [CVE-2026-106149](https://www.telerik.com/kendo-jquery-ui/documentation/knowledge-base/kb-security-menu-xss-cve-2026-106149)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-106149
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-16 00:17:21 JST
- 更新日: 2026-10-16 04:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Progress Kendo UI for jQuery の Menu コンポーネントにおける HTML 属性構築時の無害化不足による XSS の脆弱性
- 影響: 攻撃者がデータソースのフィールドを操作することで JavaScript イベントハンドラが注入され、ユーザー操作時に任意スクリプトが実行される可能性があります。
- 推奨対応: バージョン v2026.3.1015 以降に更新してください。

#### References
- https://www.telerik.com/kendo-jquery-ui/documentation/knowledge-base/kb-security-menu-xss-cve-2026-106149

### [CVE-2026-106701](https://github.com/elunez/eladmin)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-106701
- 関連キーワード: vue
- 影響製品: -
- 公開日: 2026-10-16 04:17:18 JST
- 更新日: 2026-10-16 04:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ELADMIN v2.7 以前における WebSocketServer 等のコンポーネントに起因するクロスサイトスクリプティング（XSS）の脆弱性
- 影響: ユーザーのブラウザ上で不正なスクリプトが実行され、情報漏洩や意図しない操作が行われる可能性があります。
- 推奨対応: 最新版へのアップデートまたは適切なエスケープ処理を実装してください。

#### References
- https://github.com/elunez/eladmin
- https://github.com/tao0845/CVE-Request/blob/main/CVE-2026-106701.md

### [CVE-2026-106707](https://github.com/tao0845/CVE-Request/blob/main/CVE-2026-106707.md)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-106707
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-16 03:17:23 JST
- 更新日: 2026-10-16 04:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: XXL-JOB におけるジョブログ一覧ページでの格納型クロスサイトスクリプティング（XSS）の脆弱性
- 影響: 権限を持つ攻撃者により注入された JavaScript が、ジョブログを閲覧したユーザーのブラウザ上で実行される可能性があります。
- 推奨対応: 修正済みバージョンへのアップデートまたは入力値の検証・無害化を行ってください。

#### References
- https://github.com/tao0845/CVE-Request/blob/main/CVE-2026-106707.md
- https://github.com/xuxueli/xxl-job

### [CVE-2026-59994](https://github.com/espocrm/espocrm/commit/f9fd47622df04617728643b4b8f1a22563cbc6e7)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-59994
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-16 00:17:36 JST
- 更新日: 2026-10-16 00:17:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: EspoCRM における受信メール通知生成時の無害化不備による HTML/JavaScript 注入の脆弱性
- 影響: 悪意あるメールを受信した際、通知メール内でスクリプトまたはHTMLがレンダリングされ、意図しないコードが実行される可能性があります。
- 推奨対応: バージョン 9.3.9 以降に更新してください。

#### References
- https://github.com/espocrm/espocrm/commit/f9fd47622df04617728643b4b8f1a22563cbc6e7
- https://github.com/espocrm/espocrm/releases/tag/9.3.9
- https://github.com/espocrm/espocrm/security/advisories/GHSA-3rh4-9hcq-g79m

### [CVE-2026-102527](https://github.com/nuxt-modules/og-image/commit/e6c5b53ce7f434ab8cbc91298dccfb2b515c56a5)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-102527
- 関連キーワード: vue, nuxt
- 影響製品: -
- 公開日: 2026-10-16 02:17:08 JST
- 更新日: 2026-10-16 02:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nuxt OG Image (6.2.5〜6.7.0未満) における、未署名リクエストの受容およびキャッシュキー生成処理の不備。
- 影響: 未認証の攻撃者が特定のパラメータを操作してキャッシュをポイズニングし、正規のOpen Graph画像として偽装画像をユーザーに表示させる可能性があります。
- 推奨対応: Nuxt OG Image をバージョン 6.7.0 以降に更新してください。

#### References
- https://github.com/nuxt-modules/og-image/commit/e6c5b53ce7f434ab8cbc91298dccfb2b515c56a5
- https://github.com/nuxt-modules/og-image/pull/638
- https://github.com/nuxt-modules/og-image/releases/tag/v6.7.0
- https://github.com/nuxt-modules/og-image/security/advisories/GHSA-2x6f-rp82-ppmj

### [CVE-2026-53575](https://github.com/espocrm/espocrm/commit/ce73338ea7b463914e1271f16f8f73131ace886f)

> **Frontend** / **LOW** / CVSS: **2.7** / KEV: **no**

- タイトル: CVE-2026-53575
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-16 00:17:35 JST
- 更新日: 2026-10-16 01:18:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: EspoCRM (9.3.9未満) の applicationName 設定におけるCSP nonceインジェクションの脆弱性。
- 影響: 認証された管理者が不正なコンテンツを挿入することで、ユーザーのセッション上で任意のJavaScriptを実行させ、未保存入力データ等の漏洩を引き起こす可能性があります。
- 推奨対応: EspoCRM をバージョン 9.3.9 以降に更新してください。

#### References
- https://github.com/espocrm/espocrm/commit/ce73338ea7b463914e1271f16f8f73131ace886f
- https://github.com/espocrm/espocrm/releases/tag/9.3.9
- https://github.com/espocrm/espocrm/security/advisories/GHSA-f34h-xxmv-j9xp

### [CVE-2026-106150](https://www.telerik.com/kendo-jquery-ui/documentation/knowledge-base/kb-security-cross-site-scripting-splitter-window-tooltip-cve-2026-106150)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-106150
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-16 00:17:22 JST
- 更新日: 2026-10-16 04:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Progress Kendo UI for jQuery における Splitter、Window、Tooltip コンポーネントの iframe Markup 生成時における入力サニタイズ不足。
- 影響: 低権限の攻撃者がJavaScriptイベントハンドラ等を注入し、ユーザーのブラウザ上で任意のスクリプトを実行させ、データの機密性や完全性を損なう可能性があります。
- 推奨対応: Progress Kendo UI for jQuery をバージョン 2026.3.1015 以降に更新してください。

#### References
- https://www.telerik.com/kendo-jquery-ui/documentation/knowledge-base/kb-security-cross-site-scripting-splitter-window-tooltip-cve-2026-106150

### [CVE-2026-106151](https://www.telerik.com/kendo-jquery-ui/documentation/knowledge-base/kb-security-validator-message-xss-cve-2026-106151)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-106151
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-16 00:17:22 JST
- 更新日: 2026-10-16 04:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Progress Kendo UI for jQuery (2012.2.710〜2026.3.1015未満) の Validator コンポーネントにおいて、data-msg-* 属性の検証メッセージをHTMLとして解析してしまう脆弱性。
- 影響: 検証メッセージを操作可能な攻撃者が、フォーム検証実行時に任意のJavaScriptを実行させ、データの機密性や完全性を損なう可能性があります。
- 推奨対応: Progress Kendo UI for jQuery をバージョン 2026.3.1015 以降に更新してください。

#### References
- https://www.telerik.com/kendo-jquery-ui/documentation/knowledge-base/kb-security-validator-message-xss-cve-2026-106151

### [CVE-2026-106153](https://www.telerik.com/kendo-jquery-ui/documentation/knowledge-base/kb-security-calendar-month-template-xss-cve-2026-106153)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-106153
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-16 00:17:22 JST
- 更新日: 2026-10-16 04:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Progress Kendo UI for jQuery (2026.3.1015未満) の Calendar および MultiViewCalendar コンポーネントにおけるURLサニタイズとHTML属性エンコードの不備。
- 影響: 低権限の攻撃者がJavaScript URLやイベントハンドラを注入し、カレンダー操作時に任意スクリプトを実行させ、データの機密性や完全性を損なう可能性があります。
- 推奨対応: Progress Kendo UI for jQuery をバージョン 2026.3.1015 以降に更新してください。

#### References
- https://www.telerik.com/kendo-jquery-ui/documentation/knowledge-base/kb-security-calendar-month-template-xss-cve-2026-106153

### [CVE-2026-110878](https://github.com/aureuserp/aureuserp)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-110878
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-16 04:17:24 JST
- 更新日: 2026-10-16 04:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Aureus ERP (1.6.0以下) の RuleForm.php および RuleInfolist.php における蓄積型（Stored）クロスサイトスクリプト（XSS）の脆弱性。
- 影響: 認証された攻撃者が不正な文字列を保存し、それを閲覧・編集した管理者や担当者のセッション文脈で任意のスクリプトを実行させる可能性があります。
- 推奨対応: 修正された最新バージョンへアップデートするか、入力および表示時の適切なエスケープ処理を行ってください。

#### References
- https://github.com/aureuserp/aureuserp
- https://github.com/aureuserp/aureuserp/blob/b33fa04643a936885f83b5ad39a62260ef27a7a0/plugins/webkul/inventories/src/Filament/Clusters/Configurations/Resources/RuleResource/Schemas/RuleForm.php#L121-L153
- https://github.com/aureuserp/aureuserp/blob/b33fa04643a936885f83b5ad39a62260ef27a7a0/plugins/webkul/inventories/src/Filament/Clusters/Configurations/Resources/RuleResource/Schemas/RuleInfolist.php#L24-L43
- https://github.com/aureuserp/aureuserp/pull/1619
- https://hackmd.io/@leediay/Bk4Vpz0ife

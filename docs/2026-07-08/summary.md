# CVE Digest Summary (2026-07-08)

## Overview

- 取得日時: 2026-07-08 13:28:29 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 新規掲載件数: 14
- フロントエンド関連: 14
- KEV掲載: 0
- Critical: 0
- 日本語要約: GitHub Models

## Frontend Priority

### [CVE-2026-56812](https://cna.erlef.org/cves/CVE-2026-56812.html)

> **フロントエンド最優先** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-56812
- AI要約: PhoenixframeworkのPresence JavaScriptクライアントにおいて、攻撃者が存在キーを操作し永続的なクライアント側DoSを引き起こせる脆弱性です。クライアント側の状態同期処理の検証不足が原因です。
- 関連キーワード: javascript, prototype pollution
- 影響製品: -
- 公開日: 2026-07-08 01:16:40 JST
- 更新日: 2026-07-08 02:16:36 JST
- 出典: NVD
- 参照:
  - https://cna.erlef.org/cves/CVE-2026-56812.html
  - https://github.com/phoenixframework/phoenix/commit/7f7b971c1ea0994e3fbd1c11ddb05e780bd38ad8
  - https://github.com/phoenixframework/phoenix/commit/89a1c4be161e436241e12b2378a719904b9bd96f
  - https://github.com/phoenixframework/phoenix/commit/b90b22521465ece00eb5a19d5aa2b9465b209c85
  - https://github.com/phoenixframework/phoenix/commit/beffc4da1e787e572121f68902c63daf4fe7d9c2

### [CVE-2025-12799](https://access.redhat.com/errata/RHSA-2026:36342)

> **フロントエンド最優先** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2025-12799
- AI要約: Jastowにおいて、特定の設定でURL内の未エスケープ文字を適切に処理できずXSS攻撃を受ける可能性があります。入力の適切な検証とエスケープが必要です。
- 関連キーワード: xss
- 影響製品: -
- 公開日: 2026-07-08 02:16:34 JST
- 更新日: 2026-07-08 09:16:31 JST
- 出典: NVD
- 参照:
  - https://access.redhat.com/errata/RHSA-2026:36342
  - https://access.redhat.com/errata/RHSA-2026:36343
  - https://access.redhat.com/errata/RHSA-2026:36344
  - https://access.redhat.com/errata/RHSA-2026:36345
  - https://access.redhat.com/security/cve/CVE-2025-12799

### [CVE-2026-48949](https://developer.joomla.org/security-centre/1057-20260703-core-xss-in-mfa-method-management.html)

> **フロントエンド最優先** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-48949
- AI要約: MFA管理画面における入力検証不足によりXSS脆弱性が存在します。ユーザー入力の適切な検証とエスケープが推奨されます。
- 関連キーワード: xss
- 影響製品: -
- 公開日: 2026-07-08 04:16:53 JST
- 更新日: 2026-07-08 04:16:53 JST
- 出典: NVD
- 参照:
  - https://developer.joomla.org/security-centre/1057-20260703-core-xss-in-mfa-method-management.html

### [CVE-2026-48950](https://developer.joomla.org/security-centre/1058-20260704-core-xss-in-com-templates.html)

> **フロントエンド最優先** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-48950
- AI要約: com_templatesのファイル管理画面でエスケープ処理が不足しておりXSS攻撃のリスクがあります。表示時の適切なエスケープ対応が必要です。
- 関連キーワード: xss
- 影響製品: -
- 公開日: 2026-07-08 04:16:53 JST
- 更新日: 2026-07-08 04:16:53 JST
- 出典: NVD
- 参照:
  - https://developer.joomla.org/security-centre/1058-20260704-core-xss-in-com-templates.html

### [CVE-2026-48951](https://developer.joomla.org/security-centre/1059-20260705-core-xss-in-various-modalreturn-layouts.html)

> **フロントエンド最優先** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-48951
- AI要約: 複数コンポーネントのmodalreturnレイアウトにおいてエスケープ不足によるXSS脆弱性が報告されています。ユーザー入力の適切なエスケープを実施してください。
- 関連キーワード: xss
- 影響製品: -
- 公開日: 2026-07-08 04:16:53 JST
- 更新日: 2026-07-08 04:16:53 JST
- 出典: NVD
- 参照:
  - https://developer.joomla.org/security-centre/1059-20260705-core-xss-in-various-modalreturn-layouts.html

### [CVE-2026-48952](https://developer.joomla.org/security-centre/1060-20260706-core-xss-in-com-installer.html)

> **フロントエンド最優先** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-48952
- AI要約: com_installerの更新リスト画面でエスケープ処理が不十分なためXSS攻撃が可能です。入力値の適切なエスケープが必要です。
- 関連キーワード: xss
- 影響製品: -
- 公開日: 2026-07-08 04:16:53 JST
- 更新日: 2026-07-08 04:16:53 JST
- 出典: NVD
- 参照:
  - https://developer.joomla.org/security-centre/1060-20260706-core-xss-in-com-installer.html

### [CVE-2026-48953](https://developer.joomla.org/security-centre/1061-20260707-core-xss-in-the-generic-image-output-layout.html)

> **フロントエンド最優先** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-48953
- AI要約: 汎用画像出力レイアウトにおけるエスケープ不足によりXSS脆弱性が存在します。表示内容の適切なサニタイズを推奨します。
- 関連キーワード: xss
- 影響製品: -
- 公開日: 2026-07-08 04:16:53 JST
- 更新日: 2026-07-08 04:16:53 JST
- 出典: NVD
- 参照:
  - https://developer.joomla.org/security-centre/1061-20260707-core-xss-in-the-generic-image-output-layout.html

### [CVE-2026-48954](https://developer.joomla.org/security-centre/1062-20260708-core-xss-through-language-overrides.html)

> **フロントエンド最優先** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-48954
- AI要約: 言語オーバーライド機能で検証不足によりXSS攻撃が可能な脆弱性があります。入力値の検証とエスケープ強化が必要です。
- 関連キーワード: xss
- 影響製品: -
- 公開日: 2026-07-08 04:16:54 JST
- 更新日: 2026-07-08 04:16:54 JST
- 出典: NVD
- 参照:
  - https://developer.joomla.org/security-centre/1062-20260708-core-xss-through-language-overrides.html

### [CVE-2026-55647](https://github.com/dataease/dataease/commit/9565812980da781eda04c0a3632bf5dc8b0469f6)

> **フロントエンド最優先** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-55647
- AI要約: DataEaseのダッシュボードテキストコンポーネントでサーバー側のHTMLサニタイズが不十分なため、認証ユーザーによる任意のHTML/JS注入が可能です。バージョン2.10.24で修正済みです。
- 関連キーワード: vue
- 影響製品: -
- 公開日: 2026-07-08 06:17:28 JST
- 更新日: 2026-07-08 06:17:28 JST
- 出典: NVD
- 参照:
  - https://github.com/dataease/dataease/commit/9565812980da781eda04c0a3632bf5dc8b0469f6
  - https://github.com/dataease/dataease/commit/adab5f1e8954ff91830a3b2f052a42a139d978e1
  - https://github.com/dataease/dataease/security/advisories/GHSA-4v63-24fg-pfg7

### [CVE-2026-12948](https://www.digi.com/resources/security)

> **フロントエンド最優先** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-12948
- AI要約: Digi製品のWeb管理インターフェースにおいて、認証済み管理者がシステム設定フィールドにスクリプトを注入できる保存型XSS脆弱性があります。管理画面の入力検証強化が必要です。
- 関連キーワード: xss
- 影響製品: -
- 公開日: 2026-07-08 00:16:42 JST
- 更新日: 2026-07-08 01:16:37 JST
- 出典: NVD
- 参照:
  - https://www.digi.com/resources/security

### [CVE-2026-36162](https://docs.liquidfiles.com/release_notes/version_4-2-x.html)

> **フロントエンド最優先** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-36162
- AI要約: LiquidFiles v4.2.7のアップロードファイル共有APIにて、認証ユーザーがNameパラメータに悪意あるスクリプトを注入可能な保存型XSS脆弱性があります。入力値の適切なサニタイズが必要です。
- 関連キーワード: javascript, xss
- 影響製品: -
- 公開日: 2026-07-08 08:16:54 JST
- 更新日: 2026-07-08 08:16:54 JST
- 出典: NVD
- 参照:
  - https://docs.liquidfiles.com/release_notes/version_4-2-x.html
  - https://securing.pl/en/bypassing-csp-to-exploit-stored-xss-in-liquidfiles/

### [CVE-2026-55592](https://github.com/lissy93/dashy/commit/4bc620e21cc8e3466f32b8bc40614b0d0eb5648b)

> **フロントエンド最優先** / **LOW** / CVSS: **3.9** / KEV: **no**

- タイトル: CVE-2026-55592
- AI要約: DashyのワークスペースビューでURLクエリパラメータを検証せずiframeのsrcに設定するため、javascript:スキームを利用したXSS攻撃が可能です。バージョン4.3.7で修正済みです。
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-08 06:17:27 JST
- 更新日: 2026-07-08 06:17:27 JST
- 出典: NVD
- 参照:
  - https://github.com/lissy93/dashy/commit/4bc620e21cc8e3466f32b8bc40614b0d0eb5648b
  - https://github.com/lissy93/dashy/releases/tag/4.3.7
  - https://github.com/lissy93/dashy/security/advisories/GHSA-58mp-4qr3-vmrc

### [CVE-2026-55430](https://github.com/coder/coder/pull/26204)

> **フロントエンド最優先** / **MEDIUM** / CVSS: **5.8** / KEV: **no**

- タイトル: CVE-2026-55430
- AI要約: CoderのワークスペースアプリプロキシがX-Forwarded-Hostヘッダーを適切に検証せず、サブドメインルーティング環境でのヘッダー偽装による攻撃が可能です。指定バージョンで修正されています。
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-08 10:16:27 JST
- 更新日: 2026-07-08 10:16:27 JST
- 出典: NVD
- 参照:
  - https://github.com/coder/coder/pull/26204
  - https://github.com/coder/coder/releases/tag/v2.29.17
  - https://github.com/coder/coder/releases/tag/v2.32.7
  - https://github.com/coder/coder/releases/tag/v2.33.8
  - https://github.com/coder/coder/releases/tag/v2.34.2

### [CVE-2026-36163](https://docs.liquidfiles.com/release_notes/version_4-2-x.html)

> **フロントエンド最優先** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-36163
- AI要約: LiquidFiles v4.2.7のファイルビューエンドポイントにHTMLインジェクションがあり、認証ユーザーが悪意あるHTMLファイルをアップロードしてJavaScriptを実行可能です。アップロードファイルの検証強化が必要です。
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-08 08:16:54 JST
- 更新日: 2026-07-08 08:16:54 JST
- 出典: NVD
- 参照:
  - https://docs.liquidfiles.com/release_notes/version_4-2-x.html
  - https://securing.pl/en/bypassing-csp-to-exploit-stored-xss-in-liquidfiles/

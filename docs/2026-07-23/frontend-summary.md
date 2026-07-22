# Frontend CVE Summary (2026-07-23)

## Overview

- 取得日時: 2026-07-23 08:13:34 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 7
- Critical: 0
- High: 3
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-13066](https://jira.mongodb.org/browse/SERVER-127694)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-13066
- 関連キーワード: javascript, go, gin, mongodb
- 影響製品: -
- 公開日: 2026-07-23 05:16:44 JST
- 更新日: 2026-07-23 05:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: MongoDBのサーバーサイドJavaScriptエンジンにおけるBSONシリアライズ時のDBPointerオブジェクトの不適切な処理により、内部プロセスメモリの内容がクライアントに返される可能性があります。  
- 影響: サーバーサイドJavaScriptを使用しているMongoDBの環境で、意図しない情報漏洩が発生する恐れがあります。  
- 推奨対応: MongoDBのアップデートを適用し、サーバーサイドJavaScriptの利用状況を確認して影響を最小限に抑えることを検討してください。

#### References
- https://jira.mongodb.org/browse/SERVER-127694

### [CVE-2026-13078](https://jira.mongodb.org/browse/SERVER-128832)

> **Frontend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-13078
- 関連キーワード: javascript, go, gin, mongodb
- 影響製品: -
- 公開日: 2026-07-23 05:16:46 JST
- 更新日: 2026-07-23 05:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: MongoDB ServerのMozJSスクリプトエンジンにより、認証済みユーザーが任意のファイルを読み取れる脆弱性が存在します。  
- 影響: 認証ユーザーがMongoDBサーバープロセスの権限でホストの任意ファイルを読み取れる可能性があります。  
- 推奨対応: MongoDBの公式アップデート適用やアクセス権限の見直しを検討してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128832

### [CVE-2026-13071](https://jira.mongodb.org/browse/SERVER-128473)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-13071
- 関連キーワード: javascript, go, express
- 影響製品: -
- 公開日: 2026-07-23 05:16:45 JST
- 更新日: 2026-07-23 05:16:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 認証済みの読み取り権限ユーザーが、特定の集約式を通じてサーバー側JavaScriptを実行し、mongodプロセスを異常終了させる可能性があります。  
- 影響: 不適切なメモリ処理により、mongodプロセスの停止やサービスの中断が発生する恐れがあります。  
- 推奨対応: 最新のパッチ適用やアクセス権限の見直しを行い、特に集約式の使用を制限することを検討してください。

#### References
- https://jira.mongodb.org/browse/SERVER-128473

### [CVE-2026-64796](https://regularlabs.com/)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64796
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-23 06:18:10 JST
- 更新日: 2026-07-23 06:18:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Free版では記事のPHP実行時に作成者と最終変更者の両方がスーパーユーザーである必要がなく、Pro版ではCSSやJavaScript、PHPの権限管理が一貫して適用されていません。  
- 影響: 権限設定の不備により、意図しないスクリプト実行やファイルアクセスが発生する可能性があります。  
- 推奨対応: 権限設定の見直しと、最新のセキュリティパッチ適用を検討してください。

#### References
- https://regularlabs.com/

### [CVE-2026-64828](https://codecanyon.net/item/tabletrack-the-complete-saas-restaurant-management-solution/55116396)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-64828
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-23 01:18:50 JST
- 更新日: 2026-07-23 02:16:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Froiden TableTrack 1.3.10以前に、注文メモ欄を通じた保存型クロスサイトスクリプティングの脆弱性が存在します。  
- 影響: 攻撃者は認証なしで悪意あるスクリプトを注入し、管理者のブラウザで実行される可能性があり、セッショントークンの窃取や不正な管理操作が行われる恐れがあります。  
- 推奨対応: 最新バージョンへのアップデートや、入力値の適切なサニタイズを実施し、管理画面でのスクリプト実行を防止してください。

#### References
- https://codecanyon.net/item/tabletrack-the-complete-saas-restaurant-management-solution/55116396
- https://github.com/aaronamran/CVE-Disclosures/tree/main/CVE-2026/CVE-2026-64828
- https://www.vulncheck.com/advisories/froiden-tabletrack-stored-xss-via-order-notes-field

### [CVE-2026-63281](https://regularlabs.com/)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63281
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-23 06:18:09 JST
- 更新日: 2026-07-23 06:18:09 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 管理者のサマリー画面で保存された条件値がHTMLやJavaScriptを実行する可能性があります。  
- 影響: 管理者権限でのクロスサイトスクリプティング（XSS）攻撃のリスクが考えられます。  
- 推奨対応: 入力値の適切なサニタイズやエスケープ処理を実施し、不審なスクリプトの実行を防止してください。

#### References
- https://regularlabs.com/

### [CVE-2026-64795](https://regularlabs.com/)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64795
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-23 06:18:10 JST
- 更新日: 2026-07-23 06:18:10 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: タグで提供されたカスタムHTMLやモジュールの内容・タイトルの上書き、デコードされたモーダルやツールチップの値により、安全でないマークアップが実行される可能性があります。  
- 影響: コンテンツ作成者が訪問者のブラウザ上でJavaScriptを実行できるため、クロスサイトスクリプティング（XSS）のリスクがあります。  
- 推奨対応: コンテンツの入力検証とサニタイズを強化し、不審なスクリプトの挿入を防ぐ対策を検討してください。

#### References
- https://regularlabs.com/

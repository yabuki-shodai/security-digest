# Frontend CVE Summary (2026-07-19)

## Overview

- 取得日時: 2026-07-19 08:05:03 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 2
- Critical: 0
- High: 1
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-12228](https://huntr.com/bounties/25623635-5ceb-4062-8289-02089e6d97c1)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-12228
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-19 06:17:03 JST
- 更新日: 2026-07-19 06:17:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: parisneo/lollmsの`POST /api/prompts/share`エンドポイントに保存型XSS脆弱性があり、攻撃者が悪意あるスクリプトを送信して他ユーザーのブラウザで実行可能です。  
- 影響: 認証済みユーザーが悪意あるメッセージを送信し、被害者の権限で任意のJavaScriptが実行され、アカウント乗っ取りやデータ漏洩のリスクがあります。  
- 推奨対応: サーバー側での適切な入力サニタイズを実装し、フロントエンドのサニタイザーを強化するか、脆弱な機能の利用を控えることを検討してください。

#### References
- https://huntr.com/bounties/25623635-5ceb-4062-8289-02089e6d97c1

### [CVE-2026-57857](https://www.flow.cl/)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-57857
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-19 06:17:03 JST
- 更新日: 2026-07-19 06:17:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WordPressのFlow Paymentプラグイン3.0.8において、WooCommerceのチェックアウトページで反射型クロスサイトスクリプティングの脆弱性が存在します。  
- 影響: 攻撃者が細工したURLを通じてJavaScriptコードを実行でき、ユーザーのブラウザ上で任意のスクリプトが動作する可能性があります。  
- 推奨対応: プラグインのアップデートや、入力値の適切なサニタイズおよびエスケープ処理を実施し、不審なURLの利用を避けることを推奨します。

#### References
- https://www.flow.cl/
- https://www.vulncheck.com/advisories/flow-payment-plugin-for-wordpress-reflected-cross-site-scripting-via-error-message-parameter

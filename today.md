# CVE Digest Dashboard (2026-10-31)

## Overview

- Total: 30
- Critical件数: 6
- High件数: 8
- KEV件数: 0
- Frontend件数: 19
- Backend件数: 11
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-31/frontend-summary.md)
- [Backend Summary](docs/2026-10-31/backend-summary.md)

## Today TOP5

- [CVE-2026-61730](https://github.com/socfortress/CoPilot/commit/bfa630b65d554670c7462a32ce6fd4e3cbd0254c) CVE-2026-61730 / CRITICAL / backend
- [CVE-2026-61826](https://github.com/morpheus65535/bazarr/commit/4bd29252feebd0803e84cc3ce1bdd24c3a076ed4) CVE-2026-61826 / CRITICAL / backend
- [CVE-2026-93327](https://docs.cloud.google.com/support/bulletins) CVE-2026-93327 / CRITICAL / backend
- [CVE-2026-61728](https://github.com/socfortress/CoPilot/commit/461e8f84794aee8ada588de3bad79430dc9f4f3d) CVE-2026-61728 / CRITICAL / frontend
- [CVE-2026-61737](https://github.com/huajian123/ng-antd-admin/commit/23e92ff9176074ee534af3ea3700b3652a9726a9) CVE-2026-61737 / CRITICAL / frontend

## Geminiによる今日の総括

## 今日のまとめ
本日掲載された脆弱性では、認証・認可の実装漏れ（ハンドラーでの認証欠落やデフォルト設定・シークレットの残留）や、入力値の不十分なエスケープによるXSS・SQLインジェクションが目立ちます。特にCVSS 9.0以上のCRITICAL件数が多く、未認証での設定変更、クラウド構成情報の漏洩、サンドボックス脱出によるOSコマンド実行など、重大な影響を及ぼす問題が含まれています。

## 優先して確認すべき3〜5件
1. **CVE-2026-61826（CVSS 10.0 / Bazarr）**
   ハンドラーへの認証チェック（`@authenticate`）欠落により、未認証の第三者がAPIキーの書き換えや認証解除を自由に行える状態になっています。
2. **CVE-2026-61737（CVSS 9.8 / ng-antd-admin）**
   ハードコードされたデフォルトJWTシークレットにより、攻撃者がトークンを偽造して管理者を含む任意ユーザーになりすませます。
3. **CVE-2026-61730（CVSS 9.3 / SOCFortress CoPilot）**
   静的ファイル配信経路の認証欠落により、AWS/Azure/GCPのIAM情報やリソース構成を含むレポートが外部から閲覧可能です。
4. **CVE-2026-119978（CVSS 9.0 / Flowise）**
   モジュールの読み込み処理を悪用したサンドボックス（vm2）脱出により、認証されたユーザーがOSコマンドを実行可能です。
5. **CVE-2026-119655 / CVE-2026-119656（CVSS 8.7 / CoreShop）**
   `ORDER BY` 句に対する入力検証の不備により、未認証で盲目的（Blind）SQLインジェクションを実行され、アカウント等の抽出に繋がります。

## 開発者向けコメント
* **認証ガードの全系適用とデフォルト値の排除**: APIエンドポイントごとの認証チェック漏れや、デフォルトのJWTシークレット・認証情報（`admin/admin`等）の放置が即座に深刻な侵害につながっています。本番起動時にデフォルト鍵の使用を拒否する仕組みや、CIでの認証漏れ検証を検討してください。
* **出力エスケープと動的クエリ生成の再点検**: Vueの`v-html`やBladeの未エスケープ出力によるStored XSS、および`ORDER BY`句への直接文字列結合によるSQLiが複数発生しています。フレームワークの安全な出力機構（自動エスケープ）の標準使用と、動的ソート指定時のホワイトリスト検証を徹底してください。

# CVE Digest Dashboard (2026-07-29)

## Overview

- Total: 30
- Critical件数: 4
- High件数: 17
- KEV件数: 0
- Frontend件数: 12
- Backend件数: 18
- GitHub Models総括: GitHub Models

## Links

- [Frontend Summary](docs/2026-07-29/frontend-summary.md)
- [Backend Summary](docs/2026-07-29/backend-summary.md)

## Today TOP5

- [CVE-2026-54658](https://github.com/hypequery/hypequery/blob/main/packages/clickhouse/CHANGELOG.md#202) CVE-2026-54658 / CRITICAL / frontend
- [CVE-2026-64863](https://github.com/goshs-labs/goshs/commit/0444ac6b1a8176ddae70d940adf7a26b2e5a6c29) CVE-2026-64863 / CRITICAL / backend
- [CVE-2026-62325](https://github.com/goshs-labs/goshs/commit/32f4a0e1790a709f722d0f3b2341f139d003180a) CVE-2026-62325 / CRITICAL / backend
- [CVE-2026-67174](https://github.com/Pivotick/Pivotick/commit/67c597cdf7f6910f97a4c73905a7b845e0d039f1) CVE-2026-67174 / CRITICAL / frontend
- [CVE-2026-54650](https://github.com/bablilayoub/openhole/commit/a28c27adde2a7ed0c347b730c8707208c0f78ed3) CVE-2026-54650 / HIGH / backend

## GitHub Modelsによる今日の総括

## 今日のまとめ
本日のCVEでは、特にGo言語製のバックエンド関連ツールやPythonのdatamodel-code-generatorに多数の高リスク脆弱性が報告されています。SQLインジェクションやクロスサイトスクリプティング（XSS）、サーバーサイドリクエストフォージェリ（SSRF）、認証回避、リモートコード実行など、多様な攻撃手法が含まれており、開発・運用環境での早急な対応が求められます。

## 優先して確認すべき3〜5件
1. **CVE-2026-54658 (CRITICAL, CVSS 9.8)**  
   HypequeryのSQLインジェクション。パラメータ置換時のエスケープ不備により任意SQL実行が可能。2.0.2で修正済み。

2. **CVE-2026-67174 (CRITICAL, CVSS 9.2)**  
   PivotickのDOMベースXSS。信頼できない文字列をinnerHTMLに直接挿入し任意スクリプト実行を許す。

3. **CVE-2026-62325 (CRITICAL, CVSS 9.1)**  
   goshsのSFTP認証バイパス。認証設定ミスにより無認証でファイルアクセス可能。2.1.4で修正。

4. **CVE-2026-54653 (HIGH, CVSS 8.8)**  
   datamodel-code-generatorのPythonコード実行。攻撃者制御のdefault_factoryが評価される問題。

5. **CVE-2026-64863 (CRITICAL, CVSS 9.1)**  
   goshsのWebDAV MOVEによるファイル削除・上書き。--no-deleteオプションが無効化される問題。

## 開発者向けコメント
- SQLインジェクションやXSSは、ユーザー入力の適切なエスケープ・サニタイズを徹底してください。特にテンプレートやinnerHTML操作時は信頼できるデータのみを使用しましょう。
- datamodel-code-generator関連の脆弱性は、外部からのスキーマやテンプレートデータを安易に信頼しないことが重要です。バージョンアップで修正済みのため、最新版への更新を推奨します。
- goshsのようなファイルサーバーでは認証設定やパス処理の不備が致命的な問題を招きます。設定の見直しと最新バージョン適用を急いでください。
- SSRFやHTTPリクエストスマグリングなど、ネットワーク経由の攻撃に対しては、入力検証と通信制限を強化し、信頼できるホストのみアクセス許可する設計を心がけましょう。
- 脆弱性の多いライブラリやツールを利用する際は、セキュリティパッチの適用を怠らず、CI/CDパイプラインに脆弱性検査を組み込むことを推奨します。

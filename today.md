# CVE Digest Dashboard (2026-07-18)

## Overview

- Total: 30
- Critical件数: 3
- High件数: 11
- KEV件数: 0
- Frontend件数: 12
- Backend件数: 18
- GitHub Models総括: GitHub Models

## Links

- [Frontend Summary](docs/2026-07-18/frontend-summary.md)
- [Backend Summary](docs/2026-07-18/backend-summary.md)

## Today TOP5

- [CVE-2026-9586](https://labs.sra.io/posts/switchvox/) CVE-2026-9586 / CRITICAL / backend
- [CVE-2026-9135](https://www.ibm.com/support/pages/node/7278920) CVE-2026-9135 / CRITICAL / backend
- [CVE-2026-54466](https://github.com/faye/websocket-driver-node/commit/5b197ca874dab58e96cacad8a3c256797d804680) CVE-2026-54466 / CRITICAL / frontend
- [CVE-2026-42168](https://github.com/abhishek-ram/django-pyas2) CVE-2026-42168 / UNKNOWN / backend
- [CVE-2026-54335](https://github.com/feathersjs/feathers/commit/28b3c03c63bdbff53115fdaa46c56980e7942acc) CVE-2026-54335 / LOW / frontend

## GitHub Modelsによる今日の総括

## 今日のまとめ
本日のCVEでは、JavaScript/TypeScriptを中心としたフロントエンドのクロスサイトスクリプティング（XSS）やプロトタイプ汚染、SVGアップロードのサニタイズ不足などの脆弱性が多数報告されています。一方、バックエンドではGo言語製ライブラリやフレームワークにおけるSQLインジェクション、OSコマンドインジェクション、認証バイパス、オープンリダイレクト、ファイルパス検証不備などの深刻な問題が目立ちます。特にSangoma Switchvox SMB Editionの複数の高リスク脆弱性や、IBM Langflow OSSのコードインジェクションは注意が必要です。

## 優先して確認すべき3〜5件
1. **CVE-2026-9586 (CRITICAL, CVSS 9.3)**  
   Sangoma Switchvox SMB Editionの未認証SQLインジェクション。リモートから任意SQL実行・RCEの恐れあり。

2. **CVE-2026-54466 (CRITICAL, CVSS 9.2)**  
   websocket-driverの整数オーバーフローによりDoS攻撃が可能。

3. **CVE-2026-9135 (CRITICAL, CVSS 9.9)**  
   IBM Langflow OSSのコードインジェクション。セキュリティ制御を回避し任意コード実行の危険。

4. **CVE-2026-9585 (HIGH, CVSS 8.6)**  
   Sangoma Switchvox SMB Editionの未認証リフレクトXSS。悪意あるスクリプト実行の可能性。

5. **CVE-2026-63094 (HIGH, CVSS 8.1)**  
   SigNozのSSO認証フローにおけるオープンリダイレクト。セッションハイジャックのリスク。

## 開発者向けコメント
- フロントエンドでは、ユーザー入力の適切なサニタイズとエスケープが依然として重要です。特にXSS対策としてHTMLテンプレートの安全なレンダリングや、JSON由来のオブジェクトマージ時のプロトタイプ汚染に注意してください。
- バックエンドでは、SQLインジェクションやOSコマンドインジェクションの防止にパラメータ化クエリや入力検証を徹底し、認証・認可の欠如による権限昇格を防ぐ設計が求められます。
- 外部ライブラリやフレームワークのアップデートを速やかに適用し、特に認証関連やファイル操作周りの脆弱性は優先的に対処してください。
- SSOやOAuth連携を利用する場合は、リダイレクト先の検証を厳格に行い、オープンリダイレクトを防止することが重要です。
- CI/CDパイプラインにセキュリティスキャンを組み込み、依存関係の脆弱性を早期に検知・修正する運用を推奨します。

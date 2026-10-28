# CVE Digest Dashboard (2026-10-28)

## Overview

- Total: 30
- Critical件数: 3
- High件数: 16
- KEV件数: 0
- Frontend件数: 6
- Backend件数: 24
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-28/frontend-summary.md)
- [Backend Summary](docs/2026-10-28/backend-summary.md)

## Today TOP5

- [CVE-2026-116692](https://github.com/mlflow/mlflow/commit/a732443e695c3c677680c54320efc394c81654ab) CVE-2026-116692 / CRITICAL / backend
- [CVE-2026-106076](https://www.veeam.com/kb4957) CVE-2026-106076 / CRITICAL / backend
- [CVE-2026-112352](https://www.sunhillo.com/product/sureline/) CVE-2026-112352 / CRITICAL / backend
- [CVE-2026-118132](https://github.com/ChatGPTNextWeb/NextChat) CVE-2026-118132 / UNKNOWN / frontend
- [CVE-2026-116676](https://github.com/runatlantis/atlantis/commit/8dd22b4d0a9d7c129fdbf6a3398dd1c4cf8c3a59) CVE-2026-116676 / HIGH / backend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載されたCVEは、AI/ML基盤（MLflow、MCP SDK）、認証/CI/CDツール（Authlib、Atlantis）、フロントエンド/エディタライブラリ（CKEditor 5、TinyMCE）、Webサーバ・ミドルウェアなど多岐にわたります。特にMLflowや認証バイパス、CI/CD環境での任意コード実行（RCE）につながる高深刻度な脆弱性や、リダイレクト時のクレデンシャル漏洩、依存ライブラリ経由のプロトタイプ汚染など、開発者が直接扱うライブラリ群の不具合が目立ちます。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-116692（CVSS 9.8 / CRITICAL）: MLflow の逆シリアル化による RCE**
   - **概要:** サードパーティスコアラー処理時のモジュール指定検証の不備により、攻撃者が配置した悪意のあるモジュールを読み込ませることで、任意コード実行（RCE）が可能です。
2. **CVE-2026-112352（CVSS 9.1 / CRITICAL）: Sunhillo SureLine の認証バイパスおよび RCE**
   - **概要:** セッションクッキーが平文ユーザー名のみで検証される脆弱性。ユーザー名を偽装したクッキーを送信することで認証を回避し、root権限でのコマンド実行が可能です。
3. **CVE-2026-106076（CVSS 9.0 / CRITICAL）: Veeam Backup for M365 の SQL インジェクション**
   - **概要:** 構成データベースに対するSQLインジェクションにより、クロステナントでのデータ読み書きや、PostgreSQLサービスアカウント権限での任意コード実行が可能です。
4. **CVE-2026-116676（CVSS 8.8 / HIGH）: Atlantis のワークスペース名注入による RCE**
   - **概要:** プルリクエスト由来のワークスペース名に対する検証不足により、シェル特殊文字を含めることで `atlantis plan` 実行時に任意コマンドが実行される危険性があります。
5. **CVE-2026-116672（CVSS 8.8 / HIGH）: Authlib の OAuth クライアント検証迂回**
   - **概要:** クライアント構成エンドポイントにおいて、リクエスト送信者の資格情報が対象の `client_id` に属しているかの検証が漏れており、他クライアントへのなりすましが可能です。

---

## 開発者向けコメント

- **AI/LLMエコシステムの検証漏れに注意:** MLflowでのRCE（CVE-2026-116692）だけでなく、Model Context Protocol (MCP) SDK等において Audience（`aud`）検証の不足（CVE-2026-116684）、リダイレクト時のヘッダー・本文漏洩（CVE-2026-116685）、`$ref` 解釈によるSSRF/ローカルファイル読み取り（CVE-2026-116686）が相次いでいます。AI連携コンポーネントを導入する際は設定値とトークン検証範囲を再確認してください。
- **依存ライブラリと型チェックの穴:** `CKEditor 5` で使われている `es-toolkit` のプロトタイプ汚染（CVE-2026-116688）や、`follow-redirects`（CVE-2026-116689）で別レルムの配列判定に `instanceof Array` を使用していたための資格情報漏洩など、外部ライブラリの選定・更新およびJavaScriptの型判定処理には注意が必要です。
- **入力長・リクエストサイズの制限徹底:** `dd-trace`（CVE-2026-116693）のクエリ文字列正規表現によるReDoSや、`Knative pkg`（CVE-2026-54462）のボディサイズ制限漏れによるメモリ圧迫など、入力制限を設けない処理が容易にDoSを引き起こします。リクエストのサイズ制限やタイムアウト設定を必ず導入してください。

# CVE Digest Dashboard (2026-08-20)

## Overview

- Total: 30
- Critical件数: 20
- High件数: 6
- KEV件数: 0
- Frontend件数: 19
- Backend件数: 11
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-20/frontend-summary.md)
- [Backend Summary](docs/2026-08-20/backend-summary.md)

## Today TOP5

- [CVE-2026-62681](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6) CVE-2026-62681 / CRITICAL / frontend
- [CVE-2026-71868](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6) CVE-2026-71868 / CRITICAL / frontend
- [CVE-2026-71869](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6) CVE-2026-71869 / CRITICAL / frontend
- [CVE-2026-71871](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6) CVE-2026-71871 / CRITICAL / frontend
- [CVE-2026-72716](https://github.com/orval-labs/orval/commit/8ef1bfdf3f9bcaf9dabfbe2e42887f1c0e159ab6) CVE-2026-72716 / CRITICAL / frontend

## Geminiによる今日の総括

## 今日のまとめ

本日の脆弱性一覧では、TypeScript/JavaScriptコード生成ツール「**Orval**」におけるコードインジェクション群（CVSS 9.3）や、**Cisco製品群**における認証回避・SQLi等の最深刻な脆弱性（CVSS 10.0）が目立ちます。

また、API基盤やファイル処理ツール（Grav API Plugin、Gotenberg、Algernonなど）において、SSRF、CORS設定不備、OS固有のパス処理問題に起因する脆弱性が複数報告されています。

---

## 優先して確認すべき3〜5件

1. **Orval: コード生成時の任意JavaScript実行脆弱性群（CVE-2026-62681, CVE-2026-71868 等）**
   * **CVSS:** 9.3 (CRITICAL)
   * **概要:** OpenAPI/Swagger仕様書内のパスやデフォルト値等のエスケープ不備により、生成されたコードやZodスキーマのインポート/呼び出し時に任意のJSが評価・実行されます。開発・CI・アプリ環境に影響します。
   * **対応:** Orval 8.21.0 以降へアップデート。

2. **Cisco Crosswork / Secure Workload: 認証回避・SQLi・ファイル操作の脆弱性群（CVE-2026-20030, CVE-2026-20315, CVE-2026-20357 等）**
   * **CVSS:** 10.0 (CRITICAL)
   * **概要:** 認証の欠如や不適切なアクセス制御、SQLインジェクション、ファイルシステムの外部制御など、複数の極めて深刻な脆弱性が確認されています。
   * **対応:** Cisco公式の修正リリースを適用。

3. **Grav API Plugin: Webhook機能におけるSSRFおよびファイル読み取り（CVE-2026-62668）**
   * **CVSS:** 9.4 (CRITICAL)
   * **概要:** Webhook URLの検証不足およびcURLプロトコル制限の欠如により、ローカルファイルの取得や内部ネットワークへの攻撃リクエストが可能になります。
   * **対応:** 1.0.6 以降に更新。

4. **Gotenberg: Linux環境におけるパスサニタイズ不備（CVE-2026-44829）**
   * **CVSS:** 8.8 (HIGH)
   * **概要:** Linux環境でWindows形式の親ディレクトリパス（`\`）が含まれるファイル名が適切に処理されず、生成されるZipアーカイブのファイルパス構造が改ざんされる恐れがあります。
   * **対応:** 修正済みバージョン（8.32.0より後のバージョン）へアップデート。

---

## 開発者向けコメント

* **コード生成ツール（ビルド時リスク）の警戒:** 外部OpenAPI定義からクライアントコードを生成する際、不十分なエスケープにより**開発環境やCI/CDパイプライン上で任意のコードが実行されるリスク**があります。開発ツールのバージョン更新と、信頼できない定義ファイルの読み込み回避を徹底してください。
* **クロスプラットフォーム対応のパス処理:** GotenbergやAlgernonの例のように、Linux/Windows間でのパス区切り文字（`/` と `\`）の違いや、NTFS代替データストリーム（`::$DATA`）の考慮漏れは、ディレクトリトラバーサルやファイル検証回避の原因になります。ファイル名・パス検証ロジックの見直しを推奨します。

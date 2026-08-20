# CVE Digest Dashboard (2026-08-21)

## Overview

- Total: 30
- Critical件数: 5
- High件数: 9
- KEV件数: 0
- Frontend件数: 7
- Backend件数: 23
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-21/frontend-summary.md)
- [Backend Summary](docs/2026-08-21/backend-summary.md)

## Today TOP5

- [CVE-2026-71485](https://github.com/centrifugal/centrifugo/commit/84d38cea1dd2efa24375a148817a974c8727f4b0) CVE-2026-71485 / CRITICAL / backend
- [CVE-2026-73251](https://github.com/cesanta/mongoose/commit/2988bc9df3a5efc9539471cb7455975fa25df483) CVE-2026-73251 / CRITICAL / backend
- [CVE-2026-73253](https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71) CVE-2026-73253 / CRITICAL / backend
- [CVE-2026-73257](https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71) CVE-2026-73257 / CRITICAL / backend
- [CVE-2026-73256](https://github.com/cesanta/mongoose/commit/a9df523f76f43a38bd53b4232b9cfd4c16869e71) CVE-2026-73256 / CRITICAL / backend

## Geminiによる今日の総括

掲載されたCVE一覧を根拠に、セキュリティアナリストの視点で以下のように総括します。

---

## 今日のまとめ
本日公開された脆弱性では、組み込みWeb/ネットワークライブラリである**Mongoose**における複数のCRITICAL脆弱性（TLS証明書検証バイパス、HTTPリクエストスマグリング等）や、リアルタイム通信基盤**Centrifugo**でのヘッダー転送起因によるCRITICAL脆弱性が目立ちます。また、フロントエンド・Webアプリ周辺では**Plate**（リッチテキストエディタ）でのSSRFや**deepmerge-ts**でのスタックオーバーフローによるDoS、**django CMS**における複数の認可制御の不備などが報告されています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-73251 (Mongoose) | CVSS 9.3 (CRITICAL)**
   - **内容:** TLS証明書検証の不備。複数証明書のCAバンドル設定時、偽造された証明書でもCommon Nameの一致のみで通過し、中間者攻撃によるサーバー偽装が可能になります（v7.23未満が対象）。
2. **CVE-2026-71485 (Centrifugo) | CVSS 9.1 (CRITICAL)**
   - **内容:** クライアント側から送信されたヘッダーがバックエンドへ転送され、信頼されたヘッダー/メタデータとして処理される脆弱性（v6.9.0未満で修正）。
3. **CVE-2026-73257 (Mongoose) | CVSS 9.1 (CRITICAL)**
   - **内容:** `Content-Length` と `Transfer-Encoding: chunked` の両方を不適切に受理することで発生するHTTP desynchronization（CL.TE）の脆弱性。リクエストの割り込みや改ざんのリスクがあります。
4. **CVE-2026-65842 (Plate / `@platejs/docx-io`) | CVSS 8.2 (HIGH)**
   - **内容:** HTMLからDOCXへの変換処理において、攻撃者制御のリモート画像URLを無検証でフェッチするためSSRFが発生。内部ネットワークへのアクセスや応答データの漏洩につながります（v53.3.2未満で修正）。
5. **CVE-2026-40345 (deepmerge-ts) | CVSS 8.2 (HIGH)**
   - **内容:** TypeScriptオブジェクトの再帰結合（deepmerge）時に自己参照を適切に追跡できず、スタックオーバーフロー（`RangeError`）を誘発してアプリケーションを停止させられるDoS脆弱性（v8.0.0未満で修正）。

---

## 開発者向けコメント

* **通信・インフラライブラリの即時アップデート:** MongooseやCentrifugoといった基盤系ライブラリに影響度の高い脆弱性が集まっています。該当コンポーネントを使用している場合は、修正済みバージョンへの早期更新を行ってください。
* **クライアントヘッダーの信頼性検証:** クライアントから送られるプロキシヘッダー（`X-Forwarded-For`等）やカスタムヘッダーを、認証・認可やレート制限の基準としてそのまま信頼しないよう設計・検証を徹底してください。
* **コンテンツ変換・レンダリング時の境界防御:** HTML/Markdownのレンダリングやファイル変換（HTML→DOCX等）を行う際は、リモートリソースの自動取得（SSRFの原因）を制限することや、HTML/SVGサニタイズ処理が適切に差し込まれているかをコードレビュー等で確認してください。

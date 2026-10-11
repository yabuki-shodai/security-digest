# Frontend CVE Summary (2026-10-11)

## Overview

- 取得日時: 2026-10-11 09:55:16 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 1
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-108551](https://github.com/ferdikoomen/openapi-typescript-codegen)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-108551
- 関連キーワード: typescript, javascript
- 影響製品: -
- 公開日: 2026-10-11 00:16:58 JST
- 更新日: 2026-10-11 00:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openapi-typescript-codegen (0.31.0以下) において、OpenAPIドキュメント内の文字に対するエスケープ処理不足によるコードインジェクションの脆弱性が存在します。
- 影響: 生成されたクライアントのインポート時やサービスメソッド呼び出し時に、任意のJavaScriptを実行される可能性があります。
- 推奨対応: ライブラリを修正済みバージョンへアップデートするか、信頼できないOpenAPIドキュメントの処理を避けてください。

#### References
- https://github.com/ferdikoomen/openapi-typescript-codegen
- https://github.com/ferdikoomen/openapi-typescript-codegen/blob/v0.31.0/src/templates/core/OpenAPI.hbs#L20-L23
- https://github.com/ferdikoomen/openapi-typescript-codegen/blob/v0.31.0/src/templates/exportService.hbs#L89-L110
- https://github.com/ferdikoomen/openapi-typescript-codegen/issues/2809
- https://www.vulncheck.com/advisories/openapi-typescript-codegen-through-0.31.0-code-injection-via-handlebars-templates

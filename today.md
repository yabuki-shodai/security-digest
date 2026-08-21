# CVE Digest Dashboard (2026-08-22)

## Overview

- Total: 30
- Critical件数: 2
- High件数: 12
- KEV件数: 0
- Frontend件数: 18
- Backend件数: 12
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-22/frontend-summary.md)
- [Backend Summary](docs/2026-08-22/backend-summary.md)

## Today TOP5

- [CVE-2026-48755](https://github.com/lxc/incus/security/advisories/GHSA-v6mj-8pf4-hhw4) CVE-2026-48755 / CRITICAL / backend
- [CVE-2026-62283](https://github.com/nezhahq/nezha/commit/6661d6a7fc1c269f55c7f4e775082ad23fbe0f54) CVE-2026-62283 / CRITICAL / backend
- [CVE-2026-55850](https://github.com/element-hq/element-web/commit/7949980a7e3c7e397d7afe899ef1b0563c417b0e) CVE-2026-55850 / MEDIUM / frontend
- [CVE-2026-50288](https://github.com/asymmetric-effort/specifyjs/commit/25d1fb491d99479efdf501f5f75e0bb80c908f0a) CVE-2026-50288 / HIGH / frontend
- [CVE-2026-50290](https://github.com/asymmetric-effort/specifyjs/commit/25d1fb491d99479efdf501f5f75e0bb80c908f0a) CVE-2026-50290 / MEDIUM / frontend

## Geminiによる今日の総括

## 今日のまとめ

本日の脆弱性一覧では、コンテナ管理ツール（Incus）やモニタリング基盤（Nezha Monitoring）におけるCVSS 9.9のCRITICALな脆弱性を筆頭に、ライブラリやフレームワークにおける入力検証不備が多く報告されています。主な影響範囲は、ホスト上での任意コマンド実行、他ユーザーのターミナル/ファイルへの不正アクセス、メモリ枯渇によるDoS、および各種XSSやパストラバーサルです。

## 優先して確認すべき3〜5件

* **CVE-2026-48755 (CVSS 9.9 / CRITICAL) - Incus**
  バックアップ圧縮アルゴリズムの入力検証不備による引数注入の脆弱性。ホスト上での任意ファイル書き込みおよび任意コマンド実行につながる恐れがあります。
* **CVE-2026-62283 (CVSS 9.9 / CRITICAL) - Nezha Monitoring**
  WebSocketストリーム識別子（UUID）の所有権チェック不足。ライブストリームUUIDを知り得た認証済みユーザーが、他ユーザーのターミナルやファイル転送セッションに接続可能です。
* **CVE-2026-50288 (CVSS 8.7 / HIGH) - SpecifyJS**
  `new URL()` のパース失敗時にエラーを投げずに処理を通過させてしまう不具合。HTTPSバリデーションがサイレントにバイパスされるリスクがあります。
* **CVE-2026-77354 (CVSS 8.7 / HIGH) - kin-openapi**
  OpenAPIのクエリ解釈時、スキーマ検証（`maxItems`）を行う前に大きなインデックス値に基づいて配列メモリを割り当ててしまい、リソース枯渇（DoS）を引き起こします。

## 開発者向けコメント

* **例外処理で失敗を飲み込まない**: URLパースやデータ変換時の例外をキャッチした際、サイレントに処理を続行させず、確実にエラーとして拒否する実装を徹底してください。
* **リソース割り当て前の入力検証**: メモリ確保や重い処理を行うAPIでは、スキーマバリデーションや上限値チェックをリソース割り当てより前に実行する順序設計が必要です。
* **外部コマンド・パス操作の無害化**: ユーザー入力をCLI引数やファイルシステムパスに渡す際は、引数注入やトラバーサルを防ぐため、ホワイトリスト検証や専用のセーフAPIを使用してください。

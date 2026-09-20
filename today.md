# CVE Digest Dashboard (2026-09-20)

## Overview

- Total: 9
- Critical件数: 0
- High件数: 7
- KEV件数: 0
- Frontend件数: 0
- Backend件数: 4
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-20/frontend-summary.md)
- [Backend Summary](docs/2026-09-20/backend-summary.md)

## Today TOP5

- [CVE-2026-93993](https://github.com/mistralai/mistral-vibe) CVE-2026-93993 / HIGH / security
- [CVE-2026-93988](https://github.com/Qloapps/QloApps) CVE-2026-93988 / HIGH / security
- [CVE-2026-93990](https://github.com/libexpat/libexpat) CVE-2026-93990 / HIGH / security
- [CVE-2026-94054](https://lists.exim.org/lurker/message/20260918.121220.0f87338e.en.html) CVE-2026-94054 / HIGH / security
- [CVE-2026-94056](https://lists.exim.org/lurker/message/20260918.121220.0f87338e.en.html) CVE-2026-94056 / HIGH / security

## Geminiによる今日の総括

## 今日のまとめ

本日掲載された脆弱性は計9件です。そのうち7件が「HIGH」の深刻度として評価されています。
主な影響として、Mistral Vibeにおけるリモートコード実行（RCE）、ExpatでのUTF-16サロゲート検証不備によるXMLインジェクション、Argo Workflowsでの認可バイパスによる情報漏洩、GopeedやQloAppsにおけるパストラバーサル、Eximでのメモリ制御不備（境界外書き込み・未初期化メモリ読み取り）などが含まれています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-93993**（Mistral Vibe | CVSS 8.8 | HIGH）
   - **概要**: worktree作成時に信頼検証を行う前にgit hooksを実行してしまう脆弱性。攻撃者のリポジトリ（post-checkoutフック）を読み込むことで、任意のシェルコマンドを実行される（RCE）リスクがあります。バージョン2.25.5未満が対象。
2. **CVE-2026-93990**（Expat | CVSS 8.7 | HIGH）
   - **概要**: UTF-16入力における上位サロゲートに続く下位サロゲートの検証不備。不正なサロゲートシーケンスによって構文文字がパーサーから隠蔽され、XMLインジェクション攻撃を許す可能性があります。バージョン2.8.4以下が対象。
3. **CVE-2026-93991**（Argo Workflows | CVSS 8.3 | HIGH）
   - **概要**: `ListArchivedWorkflows`において`NotEquals`演算子を使用した場合にクラスタースコープのアクセス検証が適用されない脆弱性。ネームスペーススコープの権限を持つ攻撃者が他ネームスペースのアーカイブ情報を取得可能になります。バージョン4.1.0〜4.1.3が対象。
4. **CVE-2026-93992**（Gopeed | CVSS 8.1 | HIGH）
   - **概要**: アーカイブ解凍処理におけるパストラバーサルの脆弱性。AutoExtract機能が有効な場合、展開先ディレクトリ外への任意ファイル書き込みが行われるリスクがあります。バージョン2.0.0-beta.3以下が対象。
5. **CVE-2026-94054** / **CVE-2026-94056**（Exim | CVSS 7.0 / 7.5 | HIGH）
   - **概要**: 攻撃者が制御するProxy-Protocol使用時に、境界外書き込み（94054）やスタック上の未初期化メモリ読み取り（94056）が発生します。バージョン4.100.1未満が対象。

---

## 開発者向けコメント

* **外部データ・リポジトリ処理の安全化**: Gitフックの自動実行やアーカイブの自動解凍（AutoExtract）など、利便性のための自動化処理が攻撃経路（RCEや任意ファイル書き込み）になっています。処理実行前の適切な信頼検証および解凍時のパスバリデーションを徹底してください。
* **パーサー・文字コード処理の更新**: XMLパーサー（Expat）のような基盤ライブラリの文字コード検証不備は、アプリケーション層でのインジェクションにつながります。依存ライブラリのパッチ適用状況を確認してください。
* **認可ロジック（否定条件）の検証**: Argo Workflowsの例のように、「〜以外（NotEquals）」といった否定演算子を用いたクエリやフィルター処理において、アクセス制御チェックが正しく適用されているか設計・コードレビューで確認することが推奨されます。

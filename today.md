# CVE Digest Dashboard (2026-11-02)

## Overview

- Total: 30
- Critical件数: 13
- High件数: 7
- KEV件数: 0
- Frontend件数: 9
- Backend件数: 9
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-11-02/frontend-summary.md)
- [Backend Summary](docs/2026-11-02/backend-summary.md)

## Today TOP5

- [CVE-2026-120230](https://github.com/pipiyyb/cve/blob/main/WAVLINK_WN701AE_del_vlan_group.md) CVE-2026-120230 / CRITICAL / security
- [CVE-2026-120231](https://github.com/senxitoyshuyi-ui/HACKALL/blob/main/WAVLINK%20WN553X1-B%20Router/WAVLINK_WN553X1-B_openvpn_cli_command_injection.md) CVE-2026-120231 / CRITICAL / security
- [CVE-2026-120238](https://github.com/senxitoyshuyi-ui/HACKALL/blob/main/WAVLINK%20WN553X1-B%20Router/WAVLINK_WN553X1-B_ovpn_file_command_injection.md) CVE-2026-120238 / CRITICAL / security
- [CVE-2026-120239](https://github.com/senxitoyshuyi-ui/HACKALL/blob/main/WAVLINK%20WN553X1-B%20Router/WAVLINK_WN553X1-B_wireguard_cli_command_injection.md) CVE-2026-120239 / CRITICAL / security
- [CVE-2026-120240](https://github.com/senxitoyshuyi-ui/HACKALL/blob/main/WAVLINK%20WN553X1-B%20Router/WAVLINK_WN553X1-B_wireguard_cli_group_command_injection.md) CVE-2026-120240 / CRITICAL / security

## Geminiによる今日の総括

## 今日のまとめ

本日掲載された脆弱性には、生成AI向けUIライブラリ「Prefab UI」における最高深刻度（CVSS 10.0）のサンドボックス回避、Webフレームワーク「Apache Wicket」における多数のエスケープ漏れやセッション管理不備（XSS、セッション固定化など）、「ag-ui-protocol」におけるDoSや情報漏洩、各種ルーター機器（WAVLINK、Linksys）でのリモートOSコマンドインジェクションおよびバッファオーバーフローが含まれます。

## 優先して確認すべき3〜5件

1. **CVE-2026-120338**（Prefab UI | CVSS 10.0: CRITICAL）
   - **内容**: Pyodide/Deno上でPythonを実行するサンドボックスにて、Denoが制限なし権限（`--allow-read`等）で起動され、Deno APIが露出しているため、制限を回避してファイルアクセス等の任意操作が可能です。
2. **CVE-2026-83559**（Apache Wicket | CVSS 7.4: HIGH）
   - **内容**: `JavaScriptUtils#escapeQuotes()` がバックスラッシュ自体のエスケープを行わないため、JavaScript文字列リテラルへの埋め込み時にエスケープが破綻する不備が存在します。
3. **CVE-2026-82840**（Apache Wicket | CVSS 7.2: HIGH）
   - **内容**: `AuthenticatedWebSession.signIn()` による認証時にコンテナセッションIDの更新が行われず、セッション固定化攻撃を受けるリスクがあります。
4. **CVE-2026-120276** ほか（WAVLINK / Linksys 機器 | CVSS 10.0: CRITICAL）
   - **内容**: Web管理インターフェースやCLIハンドラーの引数（`group_name`など）の不備により、リモートからOSコマンドインジェクションやバッファオーバーフローが実行可能な状態になっています。

## 開発者向けコメント

- **実行環境のサンドボックス権限確認**: Prefab UIの事例のように、WebAssemblyやサブプロセスでコードを実行させる場合は、起動引数（Denoの`--allow-*`フラグなど）の最小権限化と、グローバルオブジェクトへの不要なAPI露出を防ぐ実装を徹底してください。
- **文字列エスケープの仕様見直し**: 単一・二重引用符のみを置換するような独自エスケープ処理は、バックスラッシュの挿入によって無効化される危険があります。コンテキストに応じた適切なエンコーディング処理を使用しているかコードベースを確認してください。
- **セッション更新の実装**: ログイン認証成功時には必ずセッションIDを再発行し、セッション固定化攻撃を防御する構造になっているか確認してください。

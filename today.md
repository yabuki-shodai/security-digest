# CVE Digest Dashboard (2026-09-21)

## Overview

- Total: 14
- Critical件数: 4
- High件数: 7
- KEV件数: 0
- Frontend件数: 0
- Backend件数: 8
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-21/frontend-summary.md)
- [Backend Summary](docs/2026-09-21/backend-summary.md)

## Today TOP5

- [CVE-2026-88856](https://www.OrdaSoft.com/) CVE-2026-88856 / CRITICAL / security
- [CVE-2026-88857](https://www.OrdaSoft.com/) CVE-2026-88857 / CRITICAL / security
- [CVE-2026-94089](https://github.com/Walnut1337/CVE/blob/main/poc/poc_crash.py) CVE-2026-94089 / CRITICAL / security
- [CVE-2026-88854](https://www.OrdaSoft.com/) CVE-2026-88854 / CRITICAL / backend
- [CVE-2026-94038](https://github.com/NonceGeek/dim-sum-app/) CVE-2026-94038 / HIGH / security

## Geminiによる今日の総括

## 今日のまとめ
本日掲載されたCVEでは、CMS拡張機能（Joomlaプラグイン）におけるRCEや未認証SQLインジェクション、ルータ製品における最高深刻度（CVSS 10.0）のスタックバッファオーバーフローが目立ちます。また、機械学習ライブラリにおける不安全なデシリアライズや、Web/API層におけるSSRF・Path Traversalなど、実装上の入力検証不備に起因する脆弱性が多数報告されています。公表済みエクスプロイトが存在する案件も多いため、迅速な把握と対処が求められます。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-94089 (CVSS 10.0: CRITICAL)**
   * **対象**: D-Link DIR-868L 認証ハンドラ
   * **概要**: `strcpy` の不備に起因するスタックベースのバッファオーバーフロー。リモートから認証ID/パスワード引数を操作することで任意コード実行やDoSを引き起こす可能性があります。

2. **CVE-2026-88854 / CVE-2026-88856 / CVE-2026-88857 (CVSS 9.3〜9.4: CRITICAL)**
   * **対象**: OrdaSoft Joomla Gallery 拡張機能 (< 6.2.7)
   * **概要**: 未認証でのSQLインジェクション（CVE-2026-88854）のほか、任意PHP関数の直呼び出し（CVE-2026-88856）や拡張子検証なしのファイルアップロード（CVE-2026-88857）によるRCEが複合的に存在します。

3. **CVE-2026-94093 (CVSS 7.5: HIGH)**
   * **対象**: stable-baselines3 (<= 2.9.0)
   * **概要**: モデル/リプレイバッファ読み込み時の不安全なデシリアライズ。セキュリティ強化（PyTorchの `weights_only=True`）が後の変更で先祖返り（Revert）したことで、リモートからの不審なモデル読み込みによる攻撃リスクが生じています。

4. **CVE-2026-94044 (CVSS 7.5: HIGH)**
   * **対象**: 03-lovepreetSingh MCP (ファイル作成API)
   * **概要**: `filePath` / `content` 引数の検証不備によるPath Traversal。リモートから意図しないディレクトリ構造へファイルが書き込まれるリスクがあります。

---

## 開発者向けコメント

* **サニタイズ処理とフレームワークの安全な利用**
  SQLiやPath Traversal（CVE-2026-88854, CVE-2026-94044）の多くは、フレームワークの不適切な関数使用や独自フィルターの過信、文字列の直接結合が原因です。プレースホルダーを用いた安全なデータバインドとパスの正規化・境界チェックを徹底してください。

* **デシリアライズ処理の回帰テスト・設定保持**
  MLモデル等のデータロード処理（CVE-2026-94093）では、セーフモード設定の解除やPRの先祖返りによって脆弱性が再発するリスクがあります。セキュリティに関わる設定値はテスト等で固定・監視する仕組みを推奨します。

* **アップロード機能における多層防御**
  ファイルアップロード処理（CVE-2026-88857）では、クライアント側のファイル名やContent-Typeを一切信用せず、サーバー側でのホワイトリスト形式の拡張子検証および実行権限のないディレクトリへのランダム名保存を徹底してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近24時間ではBleepingComputerから2件を収集しました。重要度HIGHは0件です。

- **MEDIUM** [Malicious npm packages evade install-script defenses at runtime](https://www.bleepingcomputer.com/news/security/malicious-npm-packages-evade-install-script-defenses-at-runtime/) — BleepingComputer
- **MEDIUM** [Researchers escape OpenAI Codex sandbox to run commands on host](https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

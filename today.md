# CVE Digest Dashboard (2026-08-31)

## Overview

- Total: 29
- Critical件数: 5
- High件数: 11
- KEV件数: 0
- Frontend件数: 7
- Backend件数: 12
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-31/frontend-summary.md)
- [Backend Summary](docs/2026-08-31/backend-summary.md)

## Today TOP5

- [CVE-2026-82592](https://github.com/Robots10/IoT_vlu/blob/main/reports/Dlink/formDiskFormat/formDiskFormat.md) CVE-2026-82592 / CRITICAL / security
- [CVE-2026-82593](https://github.com/Robots10/IoT_vlu/blob/main/reports/Dlink/formLtefotaUpgradeFibocom/formLtefotaUpgradeFibocom.md) CVE-2026-82593 / CRITICAL / security
- [CVE-2026-82653](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-hvwp-43j9-4xgf) CVE-2026-82653 / CRITICAL / security
- [CVE-2026-82654](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-hf87-qh3j-3p88) CVE-2026-82654 / CRITICAL / security
- [CVE-2026-82645](https://github.com/WWBN/AVideo/security/advisories/GHSA-c4w3-h888-7ccv) CVE-2026-82645 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ

本日公開された脆弱性では、**Ash Framework (Elixir/GraphQL/PostgreSQL)** におけるマルチテナンシーや認可制御の破綻・クエリ制限の迂回、ならびに **AVideo** や **SiYuan** などのオープンソース製品における認証回避、蓄積型XSS、パススルー不備が目立ちます。また、ルーターやIoT機器向けファームウェアでのバッファオーバーフローやコマンド注入も報告されています。

特に開発フレームワークやライブラリに起因する脆弱性は、依存パッケージを利用するサービス全般に影響するため注意が必要です。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-82645 (AVideo) | CVSS 9.2 (Critical)**
   * **概要:** `getLiveKey.json.php` において `token` パラメータを指定すると認証・所有権チェックが回避され、未認証で外部プラットフォーム（YouTube, Twitch等）の配信資格情報が漏洩する。
2. **CVE-2026-82653 / CVE-2026-82654 (SiYuan) | CVSS 9.3 (Critical)**
   * **概要:** パッケージ名やブロック名、メモ欄などの描画時にエスケープ処理が不足しており、UI上で任意JavaScriptが実行される蓄積型XSS脆弱性（v3.8.1未満が影響）。
3. **CVE-2026-81636 (ash_graphql) | CVSS 8.7 (High)**
   * **概要:** Relay接続やキーセットページネーション利用時に GraphQL のクエリ複雑度制限（query-complexity limit）を迂回され、未認証の攻撃者によって無制限なDB読み込み（リソース枯渇・DoS）を引き起こされる。
4. **CVE-2026-78699 (ash_postgres) | CVSS 7.2 (High)**
   * **概要:** テナント名変更処理で SQL エラーの戻り値を検証せず無条件に成功扱いとするため、同名の既存テナントが存在する場合にスキーマが誤って付け替わり、他テナントのデータへアクセス可能になる。
5. **CVE-2026-82655 (Admidio) | CVSS 8.7 (High)**
   * **概要:** `lists_show.php` の `relation_type_list` パラメータに対する入力検証不足により、未認証の攻撃者がブラインドSQLインジェクションを実行しハッシュ等のデータを抽出可能。

---

## 開発者向けコメント

* **エラー・戻り値の無視を行わない:** `ash_postgres` (CVE-2026-78699) の事例のように、DB操作関数の戻り値（`{:error, _}` など）を検証せずに処理を継続すると、データ不整合やマルチテナントの隔離境界破壊など重大なセキュリティ障害につながります。
* **GraphQLクエリ制限と認可ロジックの網羅性:** GraphQLの実装では、Offset形式だけでなく Relay や Keyset などあらゆるページネーションパターンに対して複雑度制限（Complexity Limit）が機能しているか再確認してください。また、サブスクリプションやインメモリ評価時もデータ境界ポリシーが適切に適用されているか注意が必要です。
* **安易な例外処理・ボット判定によるガード迂回:** AVideo (CVE-2026-82644, CVE-2026-82645) のように「User-Agentが未設定ならボットとみなしてキャッシュ書き込み（カウンタ）をスキップする」「特定トークンがあればアクセス制御を解除する」といった安易な例外ロジックは、レート制限や認証の完全な迂回手法として悪用されます。
* **UI描画時のエスケープ徹底:** ユーザーが入力した識別子やタイトル名を DOM（`innerHTML` 等）にそのまま展開しないよう、フレームワーク標準のエスケープ機構を徹底してください。

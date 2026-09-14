# CVE Digest Dashboard (2026-09-14)

## Overview

- Total: 26
- Critical件数: 1
- High件数: 13
- KEV件数: 0
- Frontend件数: 7
- Backend件数: 13
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-14/frontend-summary.md)
- [Backend Summary](docs/2026-09-14/backend-summary.md)

## Today TOP5

- [CVE-2026-81648](https://wpscan.com/vulnerability/9b1490a0-1381-4d22-8086-f75aade4e898/) CVE-2026-81648 / CRITICAL / backend
- [CVE-2026-36453](https://github.com/rhymix/rhymix/commit/f131a616eb990e2b070a8381c3106ae979d40989) CVE-2026-36453 / HIGH / security
- [CVE-2026-90566](http://github.com/Rizwan17/inventory-management-system/issues/16) CVE-2026-90566 / HIGH / security
- [CVE-2026-90579](https://github.com/cheshire-cat-ai/core/issues/1137) CVE-2026-90579 / HIGH / security
- [CVE-2026-90593](https://github.com/embedded-graphics/embedded-graphics/) CVE-2026-90593 / HIGH / security

## Geminiによる今日の総括

## 今日のまとめ
本日公開されたCVEでは、WordPressプラグインにおける認可不備や未認証操作（CVSS 10.0を含む）、AIフレームワークやWeb APIにおける認証・認可の欠如、ならびにC/Rustやフロントエンドコンポーネントにおける処理上の欠陥（NULLポインタ参照、整数オーバーフロー、XSS等）が多く報告されています。

## 優先して確認すべき3〜5件

* **CVE-2026-81648 (CVSS 10.0 / CRITICAL)**
  * **対象:** CryptoPayment Gateway WordPress プラグイン (1.2.1 - 1.2.2)
  * **概要:** AJAXエンドポイントにおける認可チェックが欠落しており、未認証の攻撃者が任意ファイルの削除、決済設定の上書き、クリアテキストで保存されたウォレット資格情報の取得などの管理者操作を実行できます。
* **CVE-2026-74933 (CVSS 8.8 / HIGH)**
  * **対象:** GenieWords WordPress プラグイン (1.5.27 - 1.5.34)
  * **概要:** REST APIおよびAJAXアクションでの認可チェック欠如と出力時のデコード処理により、未認証ユーザーが設定の上書きや全フロントエンドページへの任意スクリプト注入（XSS）を行えます。
* **CVE-2026-37008 (CVSS 8.1 / HIGH)**
  * **対象:** CrewAI (コミット `fb2323b` より前)
  * **概要:** Pythonモジュール名のインポート制限（ブロックリスト方式）の抽象化レベルが不適切なため、`ctypes.CDLL(None)` などを用いてインポート文に依存せずにCライブラリを読み込み、サンドボックスを迂回される可能性があります。
* **CVE-2026-15891 (CVSS 7.5 / HIGH)**
  * **対象:** MQTT-SN クライアント実装 (`subsys/net/lib/mqtt_sn/mqtt_sn.c`)
  * **概要:** PINGREQ再試行超過時の処理で、リスト取得マクロの戻り値を代入せずに処理を継続したため、NULLのままのポインタ参照（`gw->gw_id`）が発生し、メモリ解放処理へ渡される不具合が存在します。
* **CVE-2026-36453 (CVSS 7.4 / HIGH)**
  * **対象:** Rhymix (2.1.31 未満)
  * **概要:** 拡張変数を介した安全でない直接オブジェクト参照（IDOR）の欠陥により、任意ファイルへのアクセスが可能となります。

## 開発者向けコメント

* **APIエンドポイント・AJAXの認可検証の徹底:** 多くのコンポーネントやプラグインにおいて、エンドポイント追加時の認可チェック（能力検証やNonce検証）漏れが深刻な影響を引き起こしています。処理の先頭で必ず適切な権限確認を行ってください。
* **ブロックリスト方式によるサンドボックス実装の回避:** 言語機能（特にPython等の動的言語）のサンドボックス化において、モジュール名などの単なるブロックリスト指定はランタイム全体をカバーできず迂回されやすいため、設計の再検討が必要です。
* **マクロ呼び出しとポインタ評価の確認:** C言語等の低レイヤ実装において、評価マクロの戻り値を受け取り忘れるなどの単純な実装ミスがNULLポインタ参照やクラッシュにつながるため、静的解析やレビューでの確認が重要です。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

国家機関の再編やAIリスクに関する警告が出される中、実際のアプリ脆弱性を悪用したサイバー攻撃が確認されています。特にWindows向け入力ソフトの脆弱性を突いたバックドア感染など、実害を伴うスパイ活動への注意が必要です。安全対策の強化と脆弱性への迅速な対応が求められています。

- **HIGH** [Hackers exploit Tencent app flaw to deploy GrayRabbit malware](https://www.bleepingcomputer.com/news/security/hackers-exploit-tencent-app-flaw-to-deploy-grayrabbit-malware/) — BleepingComputer
- **MEDIUM** [Anthropic CEO Dario Amodei Says AI Industry Needs to Give Safety Measures Time to Catch Up](https://www.securityweek.com/anthropic-ceo-dario-amodei-says-ai-industry-needs-to-give-safety-measures-time-to-catch-up/) — SecurityWeek
- **LOW** [Thorough reorganization at NSA will create five 'mission centers,' including cyber and AI](https://therecord.media/nsa-reorganization-five-mission-centers) — The Record

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

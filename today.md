# CVE Digest Dashboard (2026-10-24)

## Overview

- Total: 30
- Critical件数: 3
- High件数: 17
- KEV件数: 0
- Frontend件数: 9
- Backend件数: 21
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-24/frontend-summary.md)
- [Backend Summary](docs/2026-10-24/backend-summary.md)

## Today TOP5

- [CVE-2026-46652](https://github.com/intranda/goobi-viewer-core/commit/5281245708447ae3419cb42492fbb8af731a2ce5) CVE-2026-46652 / CRITICAL / backend
- [CVE-2026-46651](https://github.com/intranda/goobi-viewer-core/commit/5281245708447ae3419cb42492fbb8af731a2ce5) CVE-2026-46651 / CRITICAL / backend
- [CVE-2026-55486](https://github.com/intranda/goobi-viewer-core/commit/0e488c6b02a28c1d1a747dfe3958ad2bbcff2d0b) CVE-2026-55486 / CRITICAL / frontend
- [CVE-2026-115774](https://github.com/twisted/twisted/commit/3d125548bcbe955007cb97f480bb699a5e074741) CVE-2026-115774 / MEDIUM / frontend
- [CVE-2026-115569](https://github.com/fallow-rs/fallow/commit/75c0c60948a53ddfe042e65b446343989f4c5649) CVE-2026-115569 / LOW / frontend

## Geminiによる今日の総括

## 今日のまとめ
本日の脆弱性一覧では、**Goobi viewerにおける複数の深刻な脆弱性（RCEにつながるパストラバーサル、未認証WebSocketアクセス、認証回避など）**や、**Hugging Face DatasetsにおけるPickleの不安全な逆シリアル化（任意コード実行）**が顕著です。
また、Happy DOMでのJavaScriptコード実行リスクや、GraphQL Scalars・pypdf・Twistedにおける各種DoS（ReDoSやメモリ枯渇）、ElectronでのTLS証明書検証不備など、開発ライブラリやエコシステム全体に及ぶ影響が報告されています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-46652 / CVE-2026-46651 (Goobi viewer | CVSS 9.8 - CRITICAL)**
   - **概要:** サーバーからの `Content-Disposition` ヘッダーを検証せずにパス解決へ渡すことによる任意ファイル上書き（パストラバーサル）と、WebSocketに対する未認証アクセス。
   - **対策:** バージョン `26.05` 以上へアップデートしてください。

2. **CVE-2026-55486 (Goobi viewer | CVSS 9.3 - CRITICAL)**
   - **概要:** IIIF Auth 2.0 エンドポイントにおける `origin` パラメータの検証不足により、CSPレスポンスヘッダの改ざんおよび HTML/postMessage へのスクリプト注入（XSS/CSPバイパス）が可能。
   - **対策:** バージョン `26.05` 以上へアップデートしてください。

3. **CVE-2026-57845 (Hugging Face Datasets | CVSS 8.8 - HIGH)**
   - **概要:** 非推奨の pandas ビルダー経由で外部データセットを読み込む際、`pandas.read_pickle()` が呼び出され、悪意のある Pickle オブジェクトによる任意コード実行が起こる。
   - **対策:** 信頼できないデータセットの読み込みを避け、ライブラリの利用構成を見直してください。

4. **CVE-2026-115895 (Happy DOM | CVSS 8.8 - HIGH)**
   - **概要:** JavaScript評価 (`enableJavaScriptEvaluation`) が有効な環境で、不整合なESMインポートエイリアスをパース・挿入させることで、コンパイル後のコード実行に繋がる問題。
   - **対策:** 修正済みバージョン（21.0.5以降など）への更新を行ってください。

---

## 開発者向けコメント

- **不安全な逆シリアル化の回避:** Pythonの Pickle など、コード実行につながる不安全なフォーマットを自動処理する機能（Hugging Face Datasetsの例など）は利用を避けるか、厳格なデータバリデーションを行ってください。
- **外部データ（ファイル名・HTTPヘッダー）の無条件信頼の禁止:** ダウンロード時の `Content-Disposition` ヘッダーから得たファイル名には必ずパス文字 (`../` 等) の除去や正規化を行ってください。また、`Host` や `Origin` ヘッダーをそのままURL生成やセキュリティ検証（CSP/CORS）に使う場合は、事前に許可リスト（allowlist）で検証する実装を徹底してください。
- **WebSocketやAPIの認証チェック再確認:** WebSocket接続開始時（ハンドシェイク時）にセッションやログイン状態の検証が漏れていないか、また設定未完了時にデフォルトで「空文字トークン」を許可してしまうような実装がないかコードレビューを行ってください。
- **ReDoS・DoS対策:** 組み込みパーサーやカスタムスカラー（GraphQL Scalars、pypdf、Twistedなど）の処理速度低下・メモリ枯渇リスクに対し、依存パッケージのバージョン更新および入力サイズ制限を設けることが推奨されます。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近の主要傾向として、パッチ未提供のPHPのRCE脆弱性や患者情報の流出を伴うデータ侵害など重大な脅威が相次いで報告されています。また、攻撃者がAIツールを低コストで悪用し大規模攻撃やヘルプデスク騙りを行う手法の巧妙化が目立ちます。さらに、各種ランサムウェアや国家背景の攻撃といった多様なセキュリティインシデントへの警戒が広がっています。

- **HIGH** [Abandoned Popcorn Time app exposed millions of devices to RCE attacks](https://www.bleepingcomputer.com/news/security/abandoned-popcorn-time-app-exposed-millions-of-device-to-rce-attacks/) — BleepingComputer
- **HIGH** [Exposed to PHP2Shell? Cyber Experts Weigh in With Advice](https://www.darkreading.com/application-security/exposed-php2shell-cyber-experts-advice) — Dark Reading
- **HIGH** [AI Tools Are Generating Massive Attacks for Little Cost](https://www.darkreading.com/cybersecurity-operations/ai-tools-massive-attacks-little-cost) — Dark Reading
- **HIGH** [Quest Diagnostics confirms data breach exposed patient records](https://www.bleepingcomputer.com/news/security/quest-diagnostics-confirms-data-breach-exposed-patient-records/) — BleepingComputer
- **HIGH** [PHP shares mitigation for new RCE vulnerability with no patch](https://www.bleepingcomputer.com/news/security/php-shares-mitigation-for-new-and-unpatched-rce-vulnerability/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

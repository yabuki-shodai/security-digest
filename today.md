# CVE Digest Dashboard (2026-11-04)

## Overview

- Total: 30
- Critical件数: 3
- High件数: 10
- KEV件数: 0
- Frontend件数: 6
- Backend件数: 24
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-11-04/frontend-summary.md)
- [Backend Summary](docs/2026-11-04/backend-summary.md)

## Today TOP5

- [CVE-2026-38600](https://github.com/Den-Sec/security-research/blob/master/advisories/gohttpserver/VDR-001-zipslip.md) CVE-2026-38600 / CRITICAL / backend
- [CVE-2026-44266](https://github.com/enspirit/elo/commit/51b869963fbe445c18328714a7ccfbd76b21ba38) CVE-2026-44266 / CRITICAL / frontend
- [CVE-2026-44267](https://github.com/enspirit/elo/commit/2136da1f64eec8ebf99890d3100be9394534b842) CVE-2026-44267 / CRITICAL / frontend
- [CVE-2026-111211](https://docs.djangoproject.com/en/dev/releases/security/) CVE-2026-111211 / MEDIUM / backend
- [CVE-2026-108147](https://docs.djangoproject.com/en/dev/releases/security/) CVE-2026-108147 / MEDIUM / backend

## Geminiによる今日の総括

## 今日のまとめ
本日は、ノーコード向け式言語「Elo」や軽量ファイルサーバ「gohttpserver」における**CVSS 9.8（CRITICAL）のリモートコード実行（RCE）脆弱性**をはじめ、Djangoフレームワークにおける複数の脆弱性（SSRF、DoS、ファイル読み取りなど）が掲載されています。また、MongoDB Database ToolsやDocker Sandboxなど、インフラ・開発周辺ツールでの認証バイパスやパス検証の不備も目立ちます。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-44267 (CVSS 9.8 / CRITICAL - Elo)**
   JavaScriptトランスパイル時のメタプロパティ検証不備により、`.constructor.constructor` を経由して任意のJavaScriptコードを実行される恐れがあります（ver 1.0.1未満が対象）。

2. **CVE-2026-44266 (CVSS 9.8 / CRITICAL - Elo)**
   Rubyバックエンドのエミッターにおいて文字列内の `#` エスケープ漏れがあり、Rubyの式展開を利用した任意コード実行が可能です（ver 1.0.1未満が対象）。

3. **CVE-2026-38600 (CVSS 9.8 / CRITICAL - gohttpserver)**
   `/upload` エンドポイントにおける Zip Slip 脆弱性により、不正なZipアーカイブをアップロードされることで任意ファイルが書き換えられます（v1.3.0以下が対象）。

4. **CVE-2026-119675 (CVSS 8.6 / HIGH - MongoDB Database Tools)**
   `mongorestore` のコレクション名検証不備により、リストア処理を通じて管理者（root）を含む未承認のデータベースアカウントが作成されるリスクがあります。

5. **Django 関連の一連の脆弱性 (CVE-2026-108147, CVE-2026-114582 等)**
   Django 5.2/6.0/6.1系において、ファイルアップロード時のメモリ過剰消費（DoS）や、GIS/GDAL機能経由のSSRF・ローカルファイル読み取り問題が報告されています。修正バージョンへの更新が必要です。

---

## 開発者向けコメント

* **コード生成・パーサー処理のエスケープ徹底**: Eloの脆弱性に見られるように、独自の式言語やDSLを別言語（JS/Ruby/Python等）へコード生成する際は、メタプロパティ参照の制限や文字列補完構文のエスケープ漏れが直ちにRCEに直結します。入出力の型検証と安全な構文木評価の徹底が必要です。
* **ファイルアップロード・解凍処理（Zip Slip）の再確認**: アーカイブ解凍処理では、展開先パスが許可されたディレクトリ内に収まっているかを必ずチェックしてください。
* **フレームワークおよび運用ツールの迅速な更新**: DjangoやMongoDB Tools、Docker周辺ツール、サードパーティ製Webライブラリなどの依存コンポーネントについて、修正パッチが適用されたバージョンへ早期にマイグレーションしてください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近24時間では、セキュリティ製品の自動更新インフラ侵害や暗号資産取引所からの巨額流出など、重大なサイバー攻撃が報告されています。また、欧州全域におけるスーパーの冷蔵制御システム侵害や、クラウド上の大規模言語モデルを悪用した不正利用など、物理インフラや新技術を標的とした被害が目立ちます。さらに、政府機関や開発者向けプラットフォームを対象としたデータ漏洩事件も確認されています。

- **HIGH** [Philippine Migrant Worker Data Likely Leaked in 69GB Government Breach](https://www.darkreading.com/cyberattacks-data-breaches/philippine-migrant-worker-data-69gb-government-breach) — Dark Reading
- **HIGH** [Hackers hijack cPGuard autoupdate to deploy backdoor, steal data](https://www.bleepingcomputer.com/news/security/hackers-hijack-cpguard-autoupdate-to-deploy-backdoor-steal-data/) — BleepingComputer
- **HIGH** [Binance says fake job interview led to $6.3 billion crypto heist](https://www.bleepingcomputer.com/news/security/binance-says-fake-job-interview-led-to-63-billion-crypto-heist/) — BleepingComputer
- **HIGH** [Google: LLMjacking attacks rack up $1 million in cloud AI charges](https://www.bleepingcomputer.com/news/security/google-llmjacking-attacks-rack-up-1-million-in-cloud-ai-charges/) — BleepingComputer
- **HIGH** [British businesses caught in Europe-wide supermarket fridge attacks](https://therecord.media/british-businesses-caught-in-europe-wide-supermarket-fridge-attacks) — The Record

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

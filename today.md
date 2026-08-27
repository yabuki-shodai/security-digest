# CVE Digest Dashboard (2026-08-27)

## Overview

- Total: 30
- Critical件数: 6
- High件数: 10
- KEV件数: 0
- Frontend件数: 8
- Backend件数: 22
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-27/frontend-summary.md)
- [Backend Summary](docs/2026-08-27/backend-summary.md)

## Today TOP5

- [CVE-2026-54523](https://github.com/kyverno/kyverno/commit/0919553c0ea1904f8d891280c92018da97946a06) CVE-2026-54523 / CRITICAL / backend
- [CVE-2026-19485](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/) CVE-2026-19485 / CRITICAL / backend
- [CVE-2026-80428](https://github.com/ILIAS-eLearning/ILIAS) CVE-2026-80428 / CRITICAL / backend
- [CVE-2026-75062](https://github.com/google/langfun) CVE-2026-75062 / CRITICAL / backend
- [CVE-2026-54569](https://github.com/senaite/senaite.core/commit/a24d65e99a17ac43c5374ed9f0a60d0fe60d2f74) CVE-2026-54569 / CRITICAL / frontend

## Geminiによる今日の総括

## 今日のまとめ
本日の脆弱性一覧では、**未認証でリモートコード実行（RCE）が可能となる深刻な脆弱性**（SENAITE.CORE、ILIAS、Google langfunなど）や、管理・実行環境の設定不備（NebulaGraph、Kyverno）が目立ちます。また、LLM・AI周辺ツール（langfun、whichllm）でのインジェクションや、リッチテキスト・フロントエンドライブラリにおけるDOM/XSS脆弱性も確認されています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-54569**（SENAITE.CORE / CVSS 9.8 / CRITICAL）
   - **概要:** JSON APIでの認可不備と不安全な式評価が組み合わさり、未認証の第三者によるリモートコード実行（RCE）が可能です。
2. **CVE-2026-80428**（ILIAS / CVSS 9.8 / CRITICAL）
   - **概要:** Shibbolethバックチャンネルのログアウト処理にて、未認証でセッションデータの不安全なデシリアライズ（`unserialize`）が行われ、任意のオブジェクトが生成される危険性があります。
3. **CVE-2026-81032**（NebulaGraph / CVSS 9.8 / CRITICAL）
   - **概要:** ランタイム設定を扱う内部HTTPサービスが認証なしで外部全インターフェースにバインドされており、証明書パス等の取得や設定変更が可能です。
4. **CVE-2026-75062**（Google langfun / CVSS 9.2 / CRITICAL）
   - **概要:** `lf.query` において、モデルが生成したコードをサンドボックスなしで評価してしまうEval Injectionが発生し、未認証RCEにつながります。
5. **CVE-2026-54523**（Kyverno / CVSS 9.6 / CRITICAL）
   - **概要:** CELコンパイラの名前空間スコープ検証漏れにより、名前空間限定ポリシーから任意名前空間のリソースへアクセス・操作が可能になります。

---

## 開発者向けコメント
* **未認証APIおよび管理用サービスのバインド設定見直し:** 認証を挟まないエンドポイントやデフォルトで全アドレスに開くWebサービス（NebulaGraphやSENAITEのケース）がないか、インフラ・アプリ両面で点検してください。
* **動的コード評価（`eval` / `unserialize`）の排除:** AI・LLMからの出力や外部リポジトリ上のファイル名（langfun, whichllm）など、外部入力を動的に評価・デシリアライズするコードはRCEの温床になります。安全なパース手法に切り替えてください。
* **フロントエンド描画処理の安全化:** `dangerouslySetInnerHTML`（FiftyOne）やリッチテキストエディタ（SunEditor）を通じたHTMLパース時のDOM操作において、不要なスクリプト実行やエスケープ漏れがないか確認しましょう。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

WordPressテーマの未認証RCE脆弱性やNVIDIA GPUに対する攻撃手法、車載システムを標的とするマルウェアなど、多様なプラットフォームにおける深刻な技術的脅威が報告されています。また、医療機器大手へのサイバー攻撃による業務影響や、米政府機関を狙った中国のハッキングツールの摘発など、重要インフラや国家安全保障に関わる事案が目立ちます。さらに、プラットフォーム企業に対する大規模な訴訟和解など、プライバシー保護や安全対策の強化に向けた動きも進んでいます。

- **HIGH** [Critical Avada WordPress theme flaw enables zero-click RCE](https://www.bleepingcomputer.com/news/security/critical-avada-wordpress-theme-flaw-enables-zero-click-rce/) — BleepingComputer
- **HIGH** [Medical device firm Boston Scientific says cyberattack has disrupted shipment processes](https://therecord.media/boston-scientific-cyberattack-disrupts-shipment-processes) — The Record
- **HIGH** [New GPUThor attack defeats NVIDIA ECC protection for root access](https://www.bleepingcomputer.com/news/security/new-gputhor-attack-defeats-nvidia-ecc-protection-for-root-access/) — BleepingComputer
- **HIGH** [Android Malware Hijacks Update System for Car Head Units](https://www.darkreading.com/cyberattacks-data-breaches/android-malware-hijacks-update-system-car-head-units) — Dark Reading
- **HIGH** [US takes down alleged Chinese hacking tools used against Federal Reserve, DOJ and Senate](https://therecord.media/qscan-qtrouter-us-takedown-alleged-china-hacking-tools) — The Record

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

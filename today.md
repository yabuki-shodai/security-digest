# CVE Digest Dashboard (2026-10-26)

## Overview

- Total: 7
- Critical件数: 0
- High件数: 4
- KEV件数: 0
- Frontend件数: 1
- Backend件数: 2
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-26/frontend-summary.md)
- [Backend Summary](docs/2026-10-26/backend-summary.md)

## Today TOP5

- [CVE-2026-116060](https://github.com/hubdk01/cve/issues/11) CVE-2026-116060 / HIGH / security
- [CVE-2026-116061](https://github.com/hubdk01/cve/issues/12) CVE-2026-116061 / HIGH / security
- [CVE-2026-116062](https://github.com/hubdk01/cve/issues/13) CVE-2026-116062 / HIGH / security
- [CVE-2026-116094](https://github.com/yy-t1/security-reports/tree/main/web/EyouCMS1.8.2/remote_file_to_local()%E7%BC%BA%E5%A4%B1%20SSRF%20%E6%A0%A1%E9%AA%8C%E5%AF%BC%E8%87%B4%E5%89%8D%E5%8F%B0%20SSRF) CVE-2026-116094 / HIGH / security
- [CVE-2026-114214](https://cna.erlef.org/cves/CVE-2026-114214.html) CVE-2026-114214 / MEDIUM / frontend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載された7件の脆弱性には、認可の不備（Ash / AshPostgres）、コードインジェクション（Alfresco Activiti）、SQLインジェクション（SourceCodester）、およびSSRF（EyouCMS）が含まれています。複数の脆弱性において公開エクスプロイトが存在しているほか、開発元から応答が得られていないケース（Alfresco ActivitiおよびEyouCMS）が報告されています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-116094 (CVSS 7.5 / HIGH)**
   * **概要:** EyouCMS (1.8.3以下) の `remote_file_to_local` 関数におけるSSRF脆弱性。
   * **ポイント:** エクスプロイトが公開されており、開発元の応答が確認されていません。

2. **CVE-2026-116060 / CVE-2026-116061 / CVE-2026-116062 (CVSS 7.5 / HIGH)**
   * **概要:** SourceCodester Performance Indicator System 1.0 の各処理（`adddealer.php`、`edit_dealer.php`、`save_profile.php`）における `Contact` 引数を介したSQLインジェクション。
   * **ポイント:** すべて公開エクスプロイトが存在します。

3. **CVE-2026-116058 (CVSS 6.5 / MEDIUM)**
   * **概要:** Alfresco Activiti (7.21.0-rc.692以下) の `JuelScriptEngine.eval` におけるリモートコードインジェクション。
   * **ポイント:** 開発元への問い合わせに対し応答が得られていない状態です。

4. **CVE-2026-114214 / CVE-2026-115627 (CVSS 6.0 / MEDIUM)**
   * **概要:** `ash` および `ash_postgres` ライブラリにおける不適切な認可の脆弱性。
   * **ポイント:** リレーション（`through` や `many_to_many`）やラテラルジョインのロード時に、無関係なレコードや他テナントの結合行を経由してデータがロードされる危険性があります。

---

## 開発者向けコメント

* **公開エクスプロイトへの対応:** SourceCodesterやEyouCMSの脆弱性は具体的に攻撃可能な状態（実証コードあり）として公開されているため、利用している場合は該当機能へのアクセス制限などの直接的な回避策を直ちに講じてください。
* **未修正・未応答コンポーネントの対策:** Alfresco ActivitiやEyouCMSのようにベンダ未応答の脆弱性については、公式パッチの提供を待つ間に該当機能（スクリプト評価やリモートファイル取得など）の実行権限絞り込みやWAF等での監視強化が必要です。
* **ORM・データロード処理の検証:** Ash/AshPostgresで発生している問題のように、複雑なリレーションロードやマルチテナント境界でのフィルタリング漏れは意図しないデータ露出につながります。データレイヤーにおける認可ロジックが正しく適用されているか見直してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

AIエージェントの活用および脅威に関するニュースが報告されています。ダウンロードフォルダ内の指示ファイルを利用してAIコーディングエージェントを騙し、不正なパッケージをインストールさせる攻撃手法が確認されました。また、AIエージェントを活用してアラート調査を行うセキュリティ企業が資金調達を実施したことが発表されています。

- **MEDIUM** [AI coding agents hijacked using AGENTS.md file in Downloads folder](https://www.bleepingcomputer.com/news/security/ai-coding-agents-hijacked-using-agentsmd-file-in-downloads-folder/) — BleepingComputer
- **LOW** [Former Unit 8200 Officers Raise $34 Million for Agentic SecOps Startup Mave](https://www.securityweek.com/former-unit-8200-officers-raise-34-million-for-agentic-secops-startup-mave/) — SecurityWeek

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

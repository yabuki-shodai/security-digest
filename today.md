# CVE Digest Dashboard (2026-10-27)

## Overview

- Total: 30
- Critical件数: 3
- High件数: 5
- KEV件数: 0
- Frontend件数: 5
- Backend件数: 25
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-27/frontend-summary.md)
- [Backend Summary](docs/2026-10-27/backend-summary.md)

## Today TOP5

- [CVE-2026-102649](https://github.com/padok-team/burrito/commit/1d48432a4a0126429c99f5fa42567bf3711d1ca1) CVE-2026-102649 / CRITICAL / backend
- [CVE-2026-93328](https://github.com/googleapis/mcp-toolbox/pull/3454) CVE-2026-93328 / CRITICAL / backend
- [CVE-2026-77055](https://boneio.eu/en/docs/black) CVE-2026-77055 / CRITICAL / backend
- [CVE-2026-116467](https://github.com/ggml-org/llama.cpp/) CVE-2026-116467 / MEDIUM / frontend
- [CVE-2026-115930](https://www.mongodb.com/docs/mongodb-shell/changelog/) CVE-2026-115930 / HIGH / frontend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載されたCVEには、CVSSスコアが最大9.9に達するCRITICALな脆弱性が複数含まれています。特にKubernetes/Terraform連携ツール（Burrito）における署名検証のスキップ、データベース用MCPツールにおけるファイル漏洩・上書き、イメージの初期権限過剰によるroot昇格といったインフラ・運用関連の深刻な脆弱性が目立ちます。また、vLLMなどのAI/LLM推論エンジンやモデルロード処理における任意コード実行リスクも確認されています。

## 優先して確認すべき3〜5件

- **CVE-2026-102649 (CVSS 9.9 / CRITICAL): Burrito (Terraform K8s operator)**
  - `webhookSecret` が未設定または空の場合、未署名のGitHub/GitLabイベントを受け入れて認証検証をスキップしてしまいます。バージョン0.13.0未満が影響を受けます。
- **CVE-2026-93328 (CVSS 9.3 / CRITICAL): Google Cloud MCP Toolbox for Databases**
  - パストラバーサルと認可欠如により、未認証のリモート攻撃者がホストファイルを外部ストレージに流出させたり、任意ローカルファイルを上書きできます。
- **CVE-2026-77055 (CVSS 9.3 / CRITICAL): boneIO (black_debian_images)**
  - `boneio` サービスアカウントにパスワードなしのsudo権限やdockerグループ所属などの過剰な権限が付与されており、ローカル攻撃者がroot権限へ昇格可能です（1.6.0で修正）。
- **CVE-2026-115912 (CVSS 7.5 / HIGH): vLLM**
  - 共有メモリ上のマルチモーダルデータ処理で値が信頼され、`pickle.loads()` に渡されることで任意のPythonコードが実行可能になります（0.32.0未満が影響）。

## 開発者向けコメント

- **オーケストレーション・MCPツールのバージョン確認と権限見直し**: BurritoやGoogle Cloud MCP Toolbox、Cloud Run MCPを利用している場合は、即座に修正バージョンへアップデートし、Webhookのシークレット設定やバケット設定を再点検してください。
- **コンテナ・OSイメージの最小権限原則の徹底**: boneIOの事例にある通り、不要なsudo権限やdockerグループ権限がサービスアカウントに付与されていないか、ベースイメージやマイグレーション処理を確認してください。
- **AI/LLM・データ処理ライブラリの更新と安全なデシリアライズ**: vLLM（`pickle.loads`関連）やLeRobot（動的クラス生成）など、AI周辺ライブラリでのコード実行リスクが報告されています。修正版へのアップデートを行うとともに、不審なオブジェクトの復元や動的ロードを防ぐ構成を徹底してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

AIを悪用した大規模なデータ窃取やAIエージェントの隙を突く新たな攻撃など、AIに関連するサイバー脅威が顕著になっています。同時に、開発者リポジトリを狙ったサプライチェーン攻撃や大学での大規模な個人情報漏えいなど、実害を伴う侵害事案が多発しています。これらに伴い、サービス提供元によるパスワード強制リセットやAI企業に対する法的訴訟などの対応が進んでいます。

- **HIGH** [University of Copenhagen data breach exposes data of 525,000 people](https://www.bleepingcomputer.com/news/security/university-of-copenhagen-data-breach-exposes-data-of-525-000-people/) — BleepingComputer
- **HIGH** [Former pentester used ARTEX AI to steal 8.2 million data records](https://www.bleepingcomputer.com/news/security/former-pentester-used-artex-ai-to-steal-82-million-data-records/) — BleepingComputer
- **HIGH** [In-the-Wild Attack Abuses AI Agents' Trust in Markdown](https://www.darkreading.com/application-security/in-the-wild-attack-ai-agents-trust-markdown) — Dark Reading
- **HIGH** [DreamHost forces password resets in ongoing "incident"](https://www.bleepingcomputer.com/news/security/dreamhost-forces-email-ftp-sftp-password-resets-in-ongoing-incident/) — BleepingComputer
- **HIGH** ['Gheist' Weaponizes GitHub Tokens to Steal Cloud Secrets](https://www.darkreading.com/cyberattacks-data-breaches/gheist-stolen-github-tokens-cloud-secrets) — Dark Reading

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

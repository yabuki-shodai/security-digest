# CVE Digest Dashboard (2026-08-29)

## Overview

- Total: 30
- Critical件数: 7
- High件数: 9
- KEV件数: 0
- Frontend件数: 9
- Backend件数: 21
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-29/frontend-summary.md)
- [Backend Summary](docs/2026-08-29/backend-summary.md)

## Today TOP5

- [CVE-2026-55068](https://github.com/free5gc/free5gc/issues/1056) CVE-2026-55068 / CRITICAL / backend
- [CVE-2026-54754](https://github.com/klever-io/klever-go/commit/8bcc600b0ac88070740c63c7ce1c8a968dd85251) CVE-2026-54754 / CRITICAL / backend
- [CVE-2026-54755](https://github.com/klever-io/klever-go/commit/8bcc600b0ac88070740c63c7ce1c8a968dd85251) CVE-2026-54755 / CRITICAL / backend
- [CVE-2026-82277](https://github.com/argoproj/argo-rollouts) CVE-2026-82277 / CRITICAL / backend
- [CVE-2026-55378](https://github.com/js-recon/js-recon/commit/447876c4bfa9ec5bc98cbc65d7a3e5f889412491) CVE-2026-55378 / CRITICAL / frontend

## Geminiによる今日の総括

## 今日のまとめ

本日公開された脆弱性には、CI/CDパイプラインでのコマンド注入、認証・認可の欠如による運用ツールの不正操作、IPアドレス検証ロジックの不備に伴うSSRF、各種Webフレームワークや管理ツールにおけるアクセス制御不全（IDOR）など、幅広いレイヤーの不具合が含まれています。特にインフラ運用ツールや開発パイプラインのセキュリティ設定ミス・入力検証不足は影響度が大きいため、迅速な対応が必要です。

## 優先して確認すべき3〜5件

1. **CVE-2026-82277 (Argo Rollouts | CVSS: 9.8)**
   * **概要:** ダッシュボードが認証・認可・CSRF保護なしで全ネットワークインターフェースにバインドされており、同一ネットワーク上の攻撃者がRolloutの促進・中断・イメージ変更等の変更操作を実行可能です。
   * **対策:** 最新版へのアップデートと、外部露出を制限するアクセス制御の設定を確認してください。

2. **CVE-2026-55378 (JS Recon | CVSS: 9.3)**
   * **概要:** GitHub Actionsのワークフロー内で、PRのブランチ名やリポジトリ名（`github.head_ref`等）を適切にエスケープせずシェルコマンドに展開しているため、任意コード実行が可能です。
   * **対策:** ワークフロー定義ファイルで信頼できない入力を環境変数経由で渡すか、スクリプト内で安全に処理する形式へ修正されたバージョン（1.3.1-beta.2以降）へ更新してください。

3. **CVE-2026-55634 (Pimcore | CVSS: 9.9)**
   * **概要:** クラス定義のインポート用エンドポイントにおいてフィールド名の許可リスト（allowlist）検証がなく、生成されるPHPプロパティや `ALTER TABLE` 識別子へ直接挿入されることでコード/SQL実行に至る恐れがあります。
   * **対策:** Pimcoreを修正済みバージョン（11.5.19 / 12.3.10 / 2026.1.6 以降）へ即時アップデートしてください。

4. **CVE-2026-55245 (Bifrost | CVSS: 8.7)**
   * **概要:** AIゲートウェイの `isPublicIP` 関数において、Carrier-Grade NATや特定のIPv6アドレス範囲（6to4, NAT64等）をプライベートIPと認識できず、内部ネットワークへのSSRFを許す脆弱性です。
   * **対策:** 1.5.17 以降へ更新し、内部ネットワーク範囲の判定ロジックを最新化してください。

## 開発者向けコメント

* **CI/CDワークフローの安全な記述:** `github.head_ref` やPRタイトルなど、外部から制御可能な値をシェルコマンドへ直接埋め込む処理はコマンド注入の原因になります。必ず環境変数（`env`）を経由させて参照してください。
* **ネットワーク範囲判定（SSRF対策）の厳格化:** IPアドレスのバリデーションを独自実装する際は、一般的なプライベートIP（10.0.0.0/8等）だけでなく、CGNAT（100.64.0.0/10）やIPv6移行用アドレス（6to4、NAT64等）が考慮されているか再点検が必要です。
* **管理ツールのデフォルトバインド設定:** デバッグ・管理用ダッシュボードを起動する際は、無条件に `0.0.0.0` にバインドせず、適切な認証機能およびネットワークアクセス制御を標準で有効化する設計を徹底しましょう。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

印刷管理ソフトPaperCutの活発な悪用やWordPressプラグインにおける最高深刻度のRCEなど、重大なソフトウェア脆弱性が相次ぎ報告されています。また、大規模な患者データの窃取被害や、約700のAIエージェントによる高度な攻撃など、進化・拡大するサイバー脅威の実態が判明しました。これに伴い、AIを活用した脆弱性発見への対応や攻撃的セキュリティへの投資など、防御側にも迅速な修復と新たな対策が求められています。

- **HIGH** [McKesson discloses breach after ShinyHunters claims patient data theft](https://www.bleepingcomputer.com/news/security/mckesson-discloses-breach-after-shinyhunters-claims-patient-data-theft/) — BleepingComputer
- **HIGH** [Hundreds of OpenAI Agents Invaded Hugging Face Servers](https://www.darkreading.com/cyberattacks-data-breaches/hundreds-openai-agents-invaded-hugging-face-servers) — Dark Reading
- **HIGH** [PaperCut releases second emergency patch for exploited flaws](https://www.bleepingcomputer.com/news/security/papercut-releases-second-emergency-patch-for-exploited-flaws/) — BleepingComputer
- **HIGH** [GiveWP WordPress donation plugin flaw lets hackers execute server commands](https://www.bleepingcomputer.com/news/security/givewp-wordpress-donation-plugin-flaw-lets-hackers-execute-server-commands/) — BleepingComputer
- **HIGH** [PaperCut warns of hackers using printer management software flaw in attacks](https://therecord.media/papercut-warns-of-hackers-using-printer-management-vulnerabilities) — The Record

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

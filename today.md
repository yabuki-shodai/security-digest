# CVE Digest Dashboard (2026-09-22)

## Overview

- Total: 30
- Critical件数: 3
- High件数: 14
- KEV件数: 0
- Frontend件数: 9
- Backend件数: 21
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-22/frontend-summary.md)
- [Backend Summary](docs/2026-09-22/backend-summary.md)

## Today TOP5

- [CVE-2026-77521](https://github.com/1Panel-dev/MaxKB/commit/594f50f2ea80a502d1c955371ba0438b277c30ea) CVE-2026-77521 / CRITICAL / backend
- [CVE-2026-86473](https://github.com/apache/airflow/pull/72649) CVE-2026-86473 / CRITICAL / backend
- [CVE-2026-58491](https://github.com/warp-tech/warpgate/commit/eab0548f018d95b5f96f8e913527000e05ed93a2) CVE-2026-58491 / CRITICAL / frontend
- [CVE-2026-61629](https://github.com/lucasdillmann/nginx-ignition/commit/0c988fc1277c7d291725e8373313f8486fa1b31a) CVE-2026-61629 / HIGH / backend
- [CVE-2026-77560](https://github.com/tinyauthapp/tinyauth/commit/80bc87188ec3aabc5104c249eaa7b997973b9275) CVE-2026-77560 / HIGH / backend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載された脆弱性では、AIアシスタント、クラウドアシスタント・インフラ管理ツール（KubeEdge, Apache Airflow）、および認証・アクセス制御・踏み台システム（Warpgate, Tinyauth, HomeBox）に関する重大な問題が目立ちます。
特に、AIツールのシェル実行機能による権限不備（CVSS 10.0）、SSOリダイレクト処理でのXSS（CVSS 9.3）、Bearerトークンのログアウト時無効化漏れ（CVSS 9.1）、KubeEdgeにおけるOSコマンド注入（CVSS 8.8）など、認証迂回や任意コード・コマンド実行に直接つながる最高評価の脆弱性が複数報告されています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-77521（MaxKB | CVSS: 10.0 / CRITICAL）**
   * **概要**: オープンソースAIアシスタント「MaxKB」において、`SandboxShellBackend` が人間の承認なしにシェル実行ツールを露出させている問題。信頼できないチャットや取り込みコンテンツによって意図しない任意コマンドが実行される可能性があります。
   * **対策**: 2.10.5-lts 以降へ更新してください。

2. **CVE-2026-58491（Warpgate | CVSS: 9.3 / CRITICAL）**
   * **概要**: SSH/HTTPS/MySQLの踏み台ホスト「Warpgate」のSSOエンドポイント（`/@warpgate/api/sso/providers/:name/start`）において、攻撃者が制御可能な `next` パラメータがHTMLエスケープ処理されずにレスポンスへ出力される蓄積型XSSの脆弱性。被害者がリンクを踏むことで、認証済みセッション内でJavaScriptが実行されます。
   * **対策**: 0.25.5 以降へ更新してください。

3. **CVE-2026-86473（Apache Airflow | CVSS: 9.1 / CRITICAL）**
   * **概要**: Core APIのログアウト処理にて、`Authorization` Bearerヘッダーとして提示された認証トークンが失効されず、`_token` クッキーのみが失効される不具合。ユーザーがログアウトしても、既存のBearerトークンは有効期限（デフォルト24時間）まで利用可能なままとなります。
   * **対策**: 適切な修正バージョンへの更新、またはBearerトークンの運用方法の確認が必要です。

4. **CVE-2026-62182 / CVE-2026-62371（KubeEdge | CVSS: 8.8 / HIGH）**
   * **概要**: エッジコンピューティング基盤「KubeEdge」にて、`ConfigUpdateJob` や `NodeUpgradeJob` の処理時にユーザー入力値（`updateFields`, `spec.version`, `spec.image` 等）をシェルコマンドにエスケープなしで文字列結合して実行している問題。権限を持つユーザーがシェルメタ文字を含めることでOSコマンドを注入できます。
   * **対策**: 1.21.2、1.22.2、1.23.1 以降の修正バージョンへ更新してください。

---

## 開発者向けコメント

本日掲載された脆弱性から見られる主な開発上の教訓は以下の通りです：

* **シェルコマンド呼び出し時のエスケープ不足と文字列結合の危険性**
  KubeEdge（CVE-2026-62182, CVE-2026-62371）の例にあるように、ユーザー入力をそのままシステムシェルに渡す設計はOSコマンド注入の原因となります。可能であればシェルを経由せず、引数配列として外部プロセスを実行するAPI（例: Goの `exec.Command` でシェルを介さない形式）を使用してください。

* **認証・セッション無効化の確実な実装**
  Apache Airflow（CVE-2026-86473）のように、Cookie認証とBearerヘッダー認証の双方が存在する環境で、特定の認証方式しか無効化処理を行わないような実装漏れに注意してください。認証ロジックを変更・拡張する際は、すべての認証トークンタイプに対して無効化処理が機能するか検証が必要です。

* **サードパーティ機能・AI統合機能の認可チェック**
  MaxKB（CVE-2026-77521）のようなAI統合アプリケーションでは、モデルが生成した指示やツール呼び出し（MCP tool / Sandbox Shell等）に対して「人間による承認（human-in-the-loop）」や最小権限原則を強制するガードレールを明示的に組み込むことが不可欠です。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

CISAによるLinuxカーネル脆弱性の能動的悪用警告や、WordPress Coreにおける「Click2Shell」脆弱性のPoC公開など、深刻なシステム脅威が報告されています。また、BigCommerceを狙ったサプライチェーン侵害や偽LastPassインストーラーによるセキュリティ製品回避型マルウェアなど、巧妙な攻撃事例が相次いでいます。さらに、EUによるGoogleへの巨額のプライバシー制裁金や、ハックされたランサムウェアグループによる被害者の再脅迫リスクなど、データ保護を巡る懸念も拡大しています。

- **HIGH** [BigCommerce alerts merchants of data breach linked to Ribon apps](https://www.bleepingcomputer.com/news/security/bigcommerce-alerts-merchants-of-data-breach-linked-to-ribon-apps/) — BleepingComputer
- **HIGH** [CISA alerts of active exploitation of three Linux kernel flaws](https://www.bleepingcomputer.com/news/security/cisa-alerts-of-active-exploitation-of-three-linux-kernel-flaws/) — BleepingComputer
- **HIGH** [ShinyHunters Hacked Clop. Now What About Clop's Victims?](https://www.darkreading.com/cyberattacks-data-breaches/shinyhunters-hacked-clop-what-about-clops-victims) — Dark Reading
- **HIGH** [WordPress Click2Shell flaw lets hackers execute PHP on the server](https://www.bleepingcomputer.com/news/security/wordpress-click2shell-flaw-lets-hackers-execute-php-on-the-server/) — BleepingComputer
- **HIGH** [Fake LastPass Installers Push Kernel-Level EDR Killer, ‘Rapuncel’ Stealer](https://www.securityweek.com/fake-lastpass-installers-push-kernel-level-edr-killer-rapuncel-stealer/) — SecurityWeek

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

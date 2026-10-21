# CVE Digest Dashboard (2026-10-21)

## Overview

- Total: 30
- Critical件数: 6
- High件数: 4
- KEV件数: 0
- Frontend件数: 14
- Backend件数: 16
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-21/frontend-summary.md)
- [Backend Summary](docs/2026-10-21/backend-summary.md)

## Today TOP5

- [CVE-2026-105772](https://github.com/google/adk-js/commit/710b4ebed118b0ded8fc257e5d0099e6b2008bc0) CVE-2026-105772 / CRITICAL / frontend
- [CVE-2026-113708](https://argo-cd.readthedocs.io/en/stable/user-guide/kustomize/#custom-kustomize-versions) CVE-2026-113708 / CRITICAL / backend
- [CVE-2026-113709](https://argo-cd.readthedocs.io/en/stable/user-guide/kustomize/#kustomizing-helm-charts) CVE-2026-113709 / CRITICAL / backend
- [CVE-2026-113672](https://argo-cd.readthedocs.io/en/stable/user-guide/tool_detection/#disable-built-in-tools) CVE-2026-113672 / CRITICAL / backend
- [CVE-2026-113678](https://github.com/froxlor/froxlor/blob/2.3.14/lib/Froxlor/Http/Statistics.php#L144-L162) CVE-2026-113678 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ

本日の脆弱性情報では、**Argo CD** におけるコマンド実行や機密ファイル閲覧につながる超高深刻度（CVSS 9.9）の脆弱性が相次いで公表されたほか、**Google ADK** や **MCP TypeScript SDK** といったAI/エージェント開発向けSDK、ならびに **Vite / Vitest** などの開発ツールにおけるパストラバーサルやアクセス制御の不備が目立ちます。

---

## 優先して確認すべき3〜5件

1. **Argo CD の一連の任意コード実行・情報漏洩の脆弱性（CVE-2026-113708 / CVE-2026-113709 / CVE-2026-113672）**
   - **概要**: CVSS 9.9 (CRITICAL)。Kustomizeのオプション注入、Helmの悪意あるプラグイン読み込み、Jsonnetでのルート外ファイル参照により、`argocd-repo-server` 内での任意コマンド実行や機密ファイル（トークンや秘密鍵など）の閲覧が可能になります。
   - **対策**: パッチ済みバージョン（3.3.15 / 3.4.10 / 3.5.4 / 3.6.0-rc2 以降）へ至急アップデートしてください。

2. **Google ADK TypeScript のパストラバーサル（CVE-2026-105772）**
   - **概要**: CVSS 9.1 (CRITICAL)。`FileArtifactService` 利用時に `userId` や `sessionId` パラメータに対する検証不足により、リモートの第三者がストレージ外のファイルを読み書きできる可能性があります。
   - **対策**: `@google/adk` を 0.6.0 以降にアップデートしてください。

3. **FlexGet の解凍処理におけるパストラバーサル（CVE-2026-113613）**
   - **概要**: CVSS 9.2 (CRITICAL)。`decompress` プラグインがアーカイブ内の `../` パスを適切に処理せず、プラグインディレクトリ等に任意ファイルを配置されてコード実行に繋がる恐れがあります。
   - **対策**: FlexGet を 3.20.7 以降に更新してください。

4. **MCP TypeScript SDK のタスクセッション分離不備（CVE-2026-111767）**
   - **概要**: CVSS 8.6 (HIGH)。`taskStore`（InMemoryTaskStore）において作成元セッションの確認が行われておらず、同一ストアを共有する別クライアントのタスク参照やキャンセルが可能です。
   - **対策**: MCP TypeScript SDK を 1.32.0 以降に更新してください。

5. **Vite / Vitest 開発サーバー関連のアクセス制御回避（CVE-2026-112950, CVE-2026-112948 等）**
   - **概要**: CVSS 4.7〜6.5 (MEDIUM)。Windows環境でのパス区切り文字解釈や `server.fs.deny` の迂回により、開発サーバー経由で意図しないローカルファイル（.envファイルやシークレットトークン等）が露出するリスクがあります。
   - **対策**: Vite / Vitest を最新版へ更新し、開発サーバーを外部ネットワークに不要に公開しないよう設定してください。

---

## 開発者向けコメント

CI/CD基盤（Argo CD）における脆弱性は、デプロイ環境全体の奪取につながるため、運用チームは緊急でのパッチ適用が必要です。

また、AI/LLM開発用エコシステム（Google ADK, MCP SDK）やフロントエンド開発・テストツール（Vite, Vitest）における「パス検証不足」や「セッション・バウンダリの欠如」を狙った脆弱性が多数報告されています。依存ライブラリのバージョン管理を徹底するとともに、開発環境用サーバーやAPIが想定外のネットワークへ露出しないよう、ネットワーク設定およびアクセス制御を見直してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

PHPの重大な脆弱性に対する緊急パッチ予告や、開発プラットフォームでの大規模な情報漏えいなど、開発・運用基盤に関わる深刻な事象が報告されています。また、脆弱な秘密鍵に起因するCA証明書のブロック対応や、600以上の被害を出しているSafePayランサムウェアに関する当局の警告も出されています。さらに、内部脅威事件や過去のデータ侵害に対する法的和解など、多岐にわたるセキュリティ事案が判明しました。

- **HIGH** [Mozilla, Google, Apple block compromised eMudhra CA certificates](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/) — BleepingComputer
- **HIGH** [Tech Giants Block eMudhra Certificates Tied to 8 Compromised Keys](https://www.darkreading.com/cyber-risk/tech-giants-emudhra-certificates-compromised-keys) — Dark Reading
- **HIGH** [PHP warns admins of two critical flaws, emergency patches coming tomorrow](https://www.bleepingcomputer.com/news/security/php-warns-admins-of-two-critical-flaws-emergency-patches-coming-tomorrow/) — BleepingComputer
- **HIGH** [FBI says SafePay ransomware gang ‘among most active’ with more than 600 victims since 2024](https://therecord.media/fbi-says-safepay-ransomware-gang-among-most-active-600-victims) — The Record
- **HIGH** [Zeabur shutting down after second security breach in two months](https://www.bleepingcomputer.com/news/security/zeabur-shutting-down-after-second-security-breach-in-two-months/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

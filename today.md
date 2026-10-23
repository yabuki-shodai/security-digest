# CVE Digest Dashboard (2026-10-23)

## Overview

- Total: 30
- Critical件数: 1
- High件数: 18
- KEV件数: 0
- Frontend件数: 8
- Backend件数: 22
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-23/frontend-summary.md)
- [Backend Summary](docs/2026-10-23/backend-summary.md)

## Today TOP5

- [CVE-2026-114607](https://github.com/better-auth/better-auth/commit/ac54bfd67821a7607533af2059858b12bc54e26a) CVE-2026-114607 / CRITICAL / frontend
- [CVE-2026-94482](https://github.com/vercel/next.js/releases/tag/v15.5.28) CVE-2026-94482 / HIGH / frontend
- [CVE-2026-114644](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0) CVE-2026-114644 / HIGH / backend
- [CVE-2026-114653](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0) CVE-2026-114653 / HIGH / backend
- [CVE-2026-115450](https://github.com/MarcosCamara01/ecommerce-template/commit/e6b364cd668f2ba875cfa7f6d55c63e771715df7) CVE-2026-115450 / HIGH / backend

## Geminiによる今日の総括

## 今日のまとめ
本日公開されたCVEでは、TypeScript向け認証ライブラリ「Better Auth」における深刻な認証バイパス（CVSS 9.1）や、Next.jsのApp Routerにおけるリソース枯渇DoSが注目されます。さらに、MongoDB C# Driverにおける大量の脆弱性（LINQインジェクション、接続共有による他者権限実行、暗号化失敗など）や、Pythonエコシステム（dnspython、msgpack、Mistune）における入力パース時のCPU/メモリ枯渇DoSが相次いで報告されています。

## 優先して確認すべき3〜5件
1. **CVE-2026-114607 (Better Auth) - CVSS 9.1 / CRITICAL**
   - **概要:** Magic LinkとOAuthを併用している特定設定下で、OAuthのstate値をMagic Linkトークンとして受容し、認証をバイパスされる恐れがあります。
2. **CVE-2026-94482 (Next.js) - CVSS 8.2 / HIGH**
   - **概要:** App RouterかつServer Actionsを有効化している環境で、細工されたリクエストにより過度なCPU消費が発生し、サービス停止（DoS）に追い込まれます（v15.5.28 / v16.4.1で修正）。
3. **MongoDB C# Driver 一連の脆弱性 (CVE-2026-114644, 114649, 114648 等) - CVSS 8.2 / HIGH**
   - **概要:** LINQクエリ内のキー未検証によるデータ不正アクセス、TLS証明書比較不備による他ユーザーとしてのDB操作実行、BSONデシリアライズ時の無制限メモリ増大など複数の重大な問題が存在します。
4. **CVE-2026-114605 (dnspython) - CVSS 7.5 / HIGH**
   - **概要:** DNS圧縮ポインタチェーンの処理ループ制限が不足しており、悪意あるDNS応答メッセージによりCPUが高負荷状態に陥りDoSを引き起こします（v2.9.0で修正）。

## 開発者向けコメント
認証周り（Better Auth）およびWebフレームワーク（Next.js）の脆弱性は攻撃者から狙われやすいため、対象バージョンを使用している場合は速やかにライブラリの更新を行ってください。また、.NET環境でMongoDBを利用している開発チームは、ドライバーのバージョンアップを優先課題として扱う必要があります。Python環境でもパーサー類（DNS、MessagePack、Markdown）にDoS脆弱性が多発しているため、依存ライブラリ全般のセキュリティパッチ適用状況の点検を推奨します。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近24時間ではBleepingComputer、Dark Reading、The Recordから10件を収集しました。重要度HIGHは5件です。

- **HIGH** [Toronto crime tips org freezes operations after details of data breach come to light](https://therecord.media/toronto-crime-tips-org-freezes-ops-after-breach) — The Record
- **HIGH** [Microsoft Links Storm-0940 to ConnectWise Supply Chain Attack](https://www.darkreading.com/cyberattacks-data-breaches/microsoft-storm-0940-connectwise-supply-chain-attack) — Dark Reading
- **HIGH** [Capcom confirms data breach affecting 11.7 million accounts](https://www.bleepingcomputer.com/news/security/capcom-confirms-data-breach-affecting-117-million-accounts/) — BleepingComputer
- **HIGH** [Arista patches new VeloCloud Orchestrator zero-day exploited in attacks](https://www.bleepingcomputer.com/news/security/arista-patches-new-velocloud-orchestrator-zero-day-exploited-in-attacks/) — BleepingComputer
- **HIGH** [Microsoft blames ConnectWise attacks on Chinese state hacker using ARTEX AI agents](https://therecord.media/china-cyber-connectwise-ai) — The Record

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

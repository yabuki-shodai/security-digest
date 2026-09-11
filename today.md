# CVE Digest Dashboard (2026-09-11)

## Overview

- Total: 30
- Critical件数: 3
- High件数: 20
- KEV件数: 0
- Frontend件数: 10
- Backend件数: 20
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-11/frontend-summary.md)
- [Backend Summary](docs/2026-09-11/backend-summary.md)

## Today TOP5

- [CVE-2026-88007](https://github.com/traefik/traefik/commit/ff39c47d7459dec9cd8de63c1a4e7aa7315bdc1c) CVE-2026-88007 / CRITICAL / backend
- [CVE-2026-88018](https://github.com/rclone/rclone/commit/90595f34f27f569be6b27c57fe5ab65057d323bd) CVE-2026-88018 / CRITICAL / backend
- [CVE-2026-88044](https://github.com/rclone/rclone/commit/739403963abf6f58003c2becd5f7c4ad0d644153) CVE-2026-88044 / CRITICAL / backend
- [CVE-2026-88032](https://jira.mongodb.org/browse/JAVA-6276) CVE-2026-88032 / HIGH / frontend
- [CVE-2026-88056](https://github.com/angular/angular/commit/3e924cc8dbbb57f23b262cb8f0d7e2bd0673034c) CVE-2026-88056 / HIGH / frontend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載された23件の脆弱性ダイジェストでは、**rclone** および **Traefik** における重大な認証バイパスやコネクション共有の脆弱性（CVSS 9.0以上が複数件）が顕著です。また、各種主要言語（Python, Java, Rust, C#, PHP, Ruby, C/C++, Go）の **MongoDB ドライバー/ライブラリ** におけるGridFSデータクエリ誤解釈の共通問題や、**Angular (SSR)** に関連するURL検証・エスケープ不備の脆弱性が多数含まれています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-88018 (rclone / CVSS 9.8: CRITICAL)**
   - `--auth-proxy` 構成時にアクセスキー検証が不十分となり、空のシークレットに対してSigV4署名がパスして認証バイパスが可能になる脆弱性。
2. **CVE-2026-88007 (Traefik / CVSS 9.1: CRITICAL)**
   - HTTP/3有効時に、バックエンドのNTLM/Negotiate認証接続が別クライアント間で共有・再利用され、他人のセッション情報が閲覧可能になる問題。
3. **CVE-2026-88044 (rclone / CVSS 9.1: CRITICAL)**
   - S3/FTPサーバーのRCインターフェース構築時にグローバル設定が参照され、認証プロキシ設定が無視されて認証未実施状態になる問題。
4. **CVE-2026-88009 (Traefik / CVSS 8.8: HIGH)**
   - HTTP/1リクエストの `URL.Opaque` 処理不備により、正規化と転送先URLに乖離が生じ、パスベースの認可やルーティング制限を迂回される脆弱性。
5. **CVE-2026-88056, CVE-2026-88058, CVE-2026-88060 (Angular / 各CVSS 8.6: HIGH)**
   - `@angular/platform-server`（SSR）において、URL検証時の先頭空白除去や、DOM serialization時のエスケープ不足に起因する脆弱性群。

---

## 開発者向けコメント

* **プロキシ・ストレージ利用環境（Traefik / rclone）:** HTTP/3やS3/FTPの認証プロキシ機能を使用している場合、認証回避や別ユーザーの接続乗っ取りが発生する可能性があるため、最優先でバージョンアップを実施してください。
* **MongoDB利用アプリケーション:** GridFSやLaravel統合パッケージを使用している環境において、入力値がデータ検索条件として誤解釈され、ファイルの不正取得や一括削除につながるリスク（CVSS 8.1〜8.3）が広範囲の言語向けドライバーで発生しています。ライブラリの更新を行ってください。
* **Angular SSR環境:** AngularのSSR（Server-Side Rendering）機能を利用したフロントエンド開発では、エスケープ漏れやURLパーサー検証回避の影響を受けるため、修正済みバージョン（20.3.30, 21.2.22, 22.1.4 等）への更新を推奨します。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

ランサムウェアとスパイウェアの機能を兼ね備えた新たなAndroidマルウェアの発生や、1億5千件規模の免許証スキャンデータの漏えいなど、深刻なサイバー脅威が報告されています。また、Microsoft Graph APIを悪用した企業データ侵入や、Windows Server等の更新プログラムによる障害など、実運用における影響度の高い課題が目立ちます。さらに米財務省による詐欺情報共有の呼びかけや人事・M&Aなど業界動向も報じられました。

- **HIGH** [New Android malware encrypts files, steals data, and harasses victims](https://www.bleepingcomputer.com/news/security/new-android-malware-encrypts-files-steals-data-and-harasses-victims/) — BleepingComputer
- **HIGH** [Voice Callers Exploit BYOD to Reach Microsoft 365, Corporate Data](https://www.darkreading.com/threat-intelligence/voice-callers-exploit-byod-microsoft-365-corporate-data) — Dark Reading
- **HIGH** [September Windows Server updates break Remote Desktop Services](https://www.bleepingcomputer.com/news/microsoft/september-windows-server-updates-break-remote-desktop-services/) — BleepingComputer
- **HIGH** [IDScan confirms breach after hackers offer 153 million driver’s license scans for sale](https://therecord.media/idscan-data-breach-notice-drivers-licenses) — The Record
- **MEDIUM** [Treasury urges banks to file cyber scam reports, noting nearly $13 billion in losses since 2023](https://therecord.media/treasury-urges-banks-report-cyber-scams) — The Record

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

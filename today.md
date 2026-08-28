# CVE Digest Dashboard (2026-08-28)

## Overview

- Total: 23
- Critical件数: 3
- High件数: 13
- KEV件数: 0
- Frontend件数: 0
- Backend件数: 12
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-28/frontend-summary.md)
- [Backend Summary](docs/2026-08-28/backend-summary.md)

## Today TOP5

- [CVE-2026-57499](https://github.com/limanmys/core/security/advisories/GHSA-3jrp-54r2-9g63) CVE-2026-57499 / CRITICAL / security
- [CVE-2026-16279](https://www.3ds.com/trust-center/security/security-advisories/cve-2026-16279) CVE-2026-16279 / CRITICAL / security
- [CVE-2026-78251](https://support.dji.com/help/content?customId=en-us03400011149&amp;spaceId=34&amp;re=US&amp;lang=en) CVE-2026-78251 / CRITICAL / security
- [CVE-2026-30046](https://github.com/open5gs/open5gs/issues/4264) CVE-2026-30046 / HIGH / security
- [CVE-2026-30047](https://github.com/open5gs/open5gs/issues/4201) CVE-2026-30047 / HIGH / security

## Geminiによる今日の総括

## 今日のまとめ
本日公開された脆弱性には、CRITICAL（最大CVSS 9.3）からHIGHの重大な問題が複数含まれています。特にLimanにおけるOSコマンドインジェクションや3DPassportの認可不備、GitLab AI Gatewayでのクラウド認証情報・秘密鍵漏洩といった深刻なリスクが報告されています。また、通信暗号化の無視（ClickHouseプラグイン）や、5G関連ソフトウェア（free5gc, Open5GS）、rsyslog・Undertow等のミドルウェアに対するDoS攻撃につながる実装上の不備も多くみられます。

## 優先して確認すべき3〜5件
1. **CVE-2026-57499**（CVSS 9.1 / CRITICAL）
   * **概要**: Limanサーバー管理ソフトのログローテーション設定におけるOSコマンドインジェクション。`ip_address` パラメータのサニタイズ不足により、認証済み管理者が任意コマンドを実行可能です。
2. **CVE-2026-75871**（CVSS 8.2 / HIGH）
   * **概要**: GitLab AI Gatewayにおいて、インラインフロー設定によるHTTP Hostヘッダの書き換えを許し、外部エンドポイントへリクエストがリダイレクトされる脆弱性。Google Cloud Vertex AIの認証情報や秘密署名鍵が漏洩する恐れがあります（同影響のCVE-2026-19889も要確認）。
3. **CVE-2026-16279**（CVSS 9.3 / CRITICAL）
   * **概要**: 3DSwymer（3DPassport）における不適切な認可の脆弱性。攻撃者によって一部のユーザーアカウントへアクセスされる可能性があります。
4. **CVE-2026-78002**（CVSS 7.5 / HIGH）
   * **概要**: rsyslogのRainerScript `replace()` 関数におけるバッファサイズ計算誤りに起因するヒープバッファオーバーフロー。悪意あるsyslogメッセージ受信によるDoSを引き起こします。

## 開発者向けコメント
本日のCVE一覧から、開発において特に意識すべきポイントは以下の3点です。

* **外部パラメータの安全な処理とコマンド生成の回避**
  パラメータをシェルコマンドに直接挿入する実装（CVE-2026-57499）や、ファイルパスの正規化を行わずにファイルアクセス処理に渡す実装（CVE-2026-40526）は極めて危険です。コマンド実行を避けるか、厳密なエスケープ・検証を徹底してください。
* **プロキシ・リダイレクト処理での認証情報漏洩防止**
  AIプロキシやゲートウェイ等の開発において、リクエストヘッダやメタデータによる送信先の変更を許すと、クラウド（AWS/GCP）のアクセストークンや秘密鍵が外部に漏洩する原因になります（CVE-2026-75871等）。宛先バリデーションを厳格に行ってください。
* **通信・ログ出力時の機密データ保護**
  接続ライブラリの利用時に暗号化（TLS）要求が正しく反映されず平文送信されるケース（CVE-2026-19854）や、コマンドラインオプションとURIの併用時に標準エラー出力（stderr）へパスワードが出力されるケース（CVE-2026-75573）が確認されています。暗号化通信の確実な動作検証と、ログ出力内容の監査を実施してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近24時間ではBleepingComputer、Dark Reading、SecurityWeek、The Recordから10件を収集しました。重要度HIGHは1件です。

- **HIGH** [PaperCut warns of NG, MF flaw exploited in zero-day attacks](https://www.bleepingcomputer.com/news/security/papercut-warns-of-ng-mf-flaw-exploited-in-zero-day-attacks/) — BleepingComputer
- **MEDIUM** [Nearly 700 rogue AI agents coordinated in the Hugging Face attack](https://www.bleepingcomputer.com/news/security/nearly-700-rogue-ai-agents-coordinated-in-the-hugging-face-attack/) — BleepingComputer
- **MEDIUM** [White House bans foreign-made equipment for power generation over cyber backdoor concerns](https://therecord.media/trump-cyber-electricity-parts) — The Record
- **MEDIUM** [Chinese Routers Sold Worldwide Contain Backdoors](https://www.darkreading.com/vulnerabilities-threats/chinese-routers-sold-worldwide-backdoors) — Dark Reading
- **MEDIUM** [Manchester Airports Group says hackers stole travelers' data](https://www.bleepingcomputer.com/news/security/manchester-airports-group-says-hackers-stole-travelers-data/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

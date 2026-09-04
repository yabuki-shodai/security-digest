# CVE Digest Dashboard (2026-09-04)

## Overview

- Total: 30
- Critical件数: 4
- High件数: 12
- KEV件数: 0
- Frontend件数: 10
- Backend件数: 20
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-04/frontend-summary.md)
- [Backend Summary](docs/2026-09-04/backend-summary.md)

## Today TOP5

- [CVE-2026-85394](https://github.com/advisories/GHSA-6c5p-j8vq-pqhj) CVE-2026-85394 / CRITICAL / backend
- [CVE-2026-85042](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html) CVE-2026-85042 / CRITICAL / backend
- [CVE-2026-85047](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html) CVE-2026-85047 / CRITICAL / backend
- [CVE-2026-85050](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html) CVE-2026-85050 / CRITICAL / backend
- [CVE-2026-49455](https://github.com/wakujs/waku/releases/tag/v1.0.0-beta.1) CVE-2026-49455 / MEDIUM / frontend

## Geminiによる今日の総括

## 今日のまとめ
本日公開されたCVEでは、`python-jose` や `node-forge`、`jwcrypto` といった暗号・認証ライブラリにおける署名検証や鍵識別の不備（過去の修正不備含む）が目立ちます。また、Reactフレームワーク「Waku」でのリクエスト検証欠陥や、MongoDB C DriverでのDouble Free、Google Chromeのブラウザエンジンにおける多数の任意コード実行脆弱性、WebアプリケーションのXSSやSSRFが掲載されています。

## 優先して確認すべき3〜5件

- **CVE-2026-85394（python-jose | CVSS 9.3: CRITICAL）**  
  HMAC初期化時に非対称鍵の検証（DER符号化公開鍵の処理）を正しく行わないため、公開鍵を所持する攻撃者によるHS256トークンの偽造が可能。CVE-2024-33663の不完全な修正。
- **CVE-2026-85393（node-forge | CVSS 8.7: HIGH）**  
  RSA PKCS#1 v1.5署名検証時にDigestAlgorithmシーケンス内の要素数を検証しないため、低指数RSA鍵において任意のメッセージに対する有効な署名を偽造可能。CVE-2026-33894の不完全な修正。
- **CVE-2026-49455（Waku | CVSS 6.5: MEDIUM）**  
  Reactフレームワーク「Waku」のRSCリクエストディスパッチャが `Origin` や `Sec-Fetch-Site` ヘッダーを検証せずにサーバーアクションを実行するため、クロスオリジン攻撃による状態変更処理の呼び出しが可能。
- **CVE-2026-84185（jwcrypto | CVSS 5.9: MEDIUM）**  
  JOSE規格を実装する `jwcrypto` でGeneral JSON Serialization JWSの検証時、特定鍵ID（`kid`）の識別ミスによりセット内の別鍵による署名を受け入れてしまい、認可バイパスが発生する。

## 開発者向けコメント
認証や署名検証を担うエコシステム（JWT/JOSE関連ライブラリ）での脆弱性が顕著です。特に `python-jose` や `node-forge` のように過去の修正が不十分だったケースが含まれているため、ライブラリのバージョンアップ状況および利用している署名検証ロジックを至急確認してください。また、ReactのServer Actions等を利用するフロントエンド/フルスタック開発においては、フレームワーク側で `Origin` ヘッダー等の検証が適切に行われているバージョン（Waku 1.0.0-beta.1以降など）へ更新することが求められます。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

大規模なデータ漏洩や開発基盤への侵入によるサプライチェーン攻撃、ネットワーク機器の深刻な脆弱性修正など、重大な影響を及ぼす事案が相次いで報告されています。また、大企業を狙う偽M&A詐欺や標的型スパイウェア攻撃、主要AIサービスの大規模障害など多様な脅威が発生しています。露出した管理者キーの悪用や基盤インフラの侵害に対するセキュリティ対策の徹底が求められます。

- **HIGH** [Coder's registry infrastructure compromised to push malicious modules](https://www.bleepingcomputer.com/news/security/coders-registry-infrastructure-compromised-to-push-malicious-modules/) — BleepingComputer
- **HIGH** [HPE patches critical ArubaOS-CX remote code execution flaw](https://www.bleepingcomputer.com/news/security/hpe-patches-critical-arubaos-cx-remote-code-execution-flaw/) — BleepingComputer
- **HIGH** [Manchester Airports Group Data on 8.8 Million People Leaked After Ransom Refusal](https://www.securityweek.com/manchester-airports-group-data-on-8-8-million-people-leaked-after-ransom-refusal/) — SecurityWeek
- **MEDIUM** [French hospital fined €500,000 after breach exposes data of 727,000](https://www.bleepingcomputer.com/news/security/french-hospital-fined-500-000-after-breach-exposes-data-of-727-000/) — BleepingComputer
- **MEDIUM** [Large Enterprises Targeted in Fake Merger & Acquisition Scams](https://www.darkreading.com/cyberattacks-data-breaches/large-enterprises-fake-merger-acquisition-scams) — Dark Reading

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

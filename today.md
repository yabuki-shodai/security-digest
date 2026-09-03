# CVE Digest Dashboard (2026-09-03)

## Overview

- Total: 30
- Critical件数: 5
- High件数: 20
- KEV件数: 0
- Frontend件数: 14
- Backend件数: 16
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-03/frontend-summary.md)
- [Backend Summary](docs/2026-09-03/backend-summary.md)

## Today TOP5

- [CVE-2026-20274](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM) CVE-2026-20274 / CRITICAL / backend
- [CVE-2026-20279](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM) CVE-2026-20279 / CRITICAL / backend
- [CVE-2026-78689](https://my.f5.com/manage/s/article/K000162602) CVE-2026-78689 / CRITICAL / frontend
- [CVE-2026-53649](https://github.com/BishopFox/joro/releases/tag/1.1.1) CVE-2026-53649 / CRITICAL / frontend
- [CVE-2026-53611](https://github.com/AS203038/looking-glass/releases/tag/1.3.5) CVE-2026-53611 / CRITICAL / frontend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載された30件のCVEでは、インフラ基盤（Cisco IOS XRなど）のセキュリティ更新に加え、Webアプリケーションフレームワーク、リバースプロキシ（NGINX njs）、開発・AI関連ツールにおける脆弱性が多数確認されました。

特に、正規表現の不備によるOSコマンドインジェクション（CVSS 9.8）や、ローカルAPIにおける無認証およびワイルドカードCORSに起因するリモートコード実行（CVSS 9.6）、NGINX JavaScriptモジュールでのメモリ破壊やアクセス制御のFail-Open（認可回避）など、認証・認可および入力検証の基本設計に関するCRITICAL/HIGHレベルの脆弱性が顕著です。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-53611 (CVSS 9.8 / CRITICAL)**
   - **対象**: Looking Glass (1.3.5未満)
   - **概要**: 入力検証レイヤーにおける正規表現のアンカー指定漏れ（固定されていない正規表現）により、OSコマンドインジェクションが発生します。バージョン1.3.5への修正パッチが提供されています。
2. **CVE-2026-53649 (CVSS 9.6 / CRITICAL)**
   - **対象**: Joro (1.1.1未満)
   - **概要**: デフォルトのプロキシモードで127.0.0.1:9090に起動するローカルAPIが無認証かつワイルドカードCORSを許容しているため、閲覧中の外部WebサイトからクロスオリジンJavaScript経由で特権プラグインをアップロード・実行される恐れがあります。
3. **CVE-2026-78689 (CVSS 9.2 / CRITICAL)**
   - **対象**: NGINX JavaScript (njs / QuickJS)
   - **概要**: XMLモジュールの接頭辞リストパーサー（`xml.exclusiveC14n()`）において、外部から制御可能なXMLプレフィックスリストを渡すことでヒープ領域外への書き込み（Out-of-bounds write）が発生します。
4. **CVE-2026-18329 (CVSS 8.8 / HIGH)**
   - **対象**: NGINX JavaScript (njs / QuickJS)
   - **概要**: `js_access` ハンドラーで非同期リクエストボディ処理中に例外が発生した場合、明確な拒否を返す前に評価が失敗し、アクセス制御が「Fail-Open（許可状態）」になって認証回避が発生します。
5. **CVE-2026-84381 (CVSS 8.1 / HIGH)**
   - **対象**: HTTPX2 (2.10.0未満)
   - **概要**: SOCKS5プロキシ経由で `wss://` を利用した際、TLSハンドシェイクが正しく開始されず通信が平文で送信されるため、認証ヘッダーやクッキーなどの情報が漏洩するリスクがあります。バージョン2.10.0で修正されています。

---

## 開発者向けコメント

- **CORSとローカルAPIの結合リスク**: 
  `Joro`（CVE-2026-53649）や `Windows ML CLI`（CVE-2026-84452）のように、「ローカル実行用」として提供されているAPIであっても、無認証かつワイルドカードCORS（`Access-Control-Allow-Origin: *`）を設定していると、悪意ある外部Webサイトを閲覧したユーザーのブラウザを経由してローカルのAPIが不正操作されます。ローカルAPIであってもオリジン検証と適切な認証を徹底してください。
- **入力検証の正規表現とFail-Closedな認可設計**: 
  入力検証で正規表現を用いる際は、先頭と末尾のアンカー（`^...$`）を確実に指定し、不完全なマッチによるコマンド注入（CVE-2026-53611）を防いでください。また、エラーや例外発生時にデフォルトでアクセスを許可してしまう「Fail-Open」の実装（CVE-2026-18329）を避け、エラー時は必ず拒否する「Fail-Closed」の原則で認可ロジックを設計することが重要です。
- **セキュリティ解析における除外設定の穴**: 
  Tencent AI-Infra-Guardやclaude-skill-antivirus（CVE-2026-84809〜84811）では、Pythonのコンパイル済みバイトコード（`.pyc`）や特定ファイルをスキャン対象外としていたため、バイパス手法が存在しました。静的解析や検証ツールを構築・利用する際は、スキップルールが悪用されないか見直す必要があります。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

SonicWallやJFrog Artifactory、Sangomaなどの脆弱性に対する実際の悪用攻撃が相次いで報告されています。また、WordPressプラグインの影響による多数のサイトへの危険や、950万人を超える規模の医療情報漏洩など深刻な被害も発生しています。AIを活用した防御ツールや攻撃者のAI利用動向、ビッシング攻撃といった多様な脅威トレンドも観測されています。

- **HIGH** [Hackers exploit Sangoma Switchvox flaw to deploy reverse shells](https://www.bleepingcomputer.com/news/security/hackers-exploit-sangoma-switchvox-flaw-to-deploy-reverse-shells/) — BleepingComputer
- **HIGH** [SonicWall SMA 1000 Zero-Days Enable Unauthenticated RCE](https://www.darkreading.com/vulnerabilities-threats/sonicwall-sma-1000-zero-days-unauthenticated-rce) — Dark Reading
- **HIGH** [WordPress backup plugin flaw exposes millions of sites to takeover attacks](https://www.bleepingcomputer.com/news/security/wordpress-backup-plugin-flaw-exposes-millions-of-sites-to-takeover-attacks/) — BleepingComputer
- **HIGH** [Health data of more than 9.5 million people leaked from Aesto record system](https://therecord.media/health-data-aesto-cyberattack-leak) — The Record
- **HIGH** [Hackers exploit critical JFrog Artifactory flaw to forge admin tokens](https://www.bleepingcomputer.com/news/security/hackers-exploit-critical-jfrog-artifactory-flaw-to-forge-admin-tokens/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

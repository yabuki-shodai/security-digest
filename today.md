# CVE Digest Dashboard (2026-11-03)

## Overview

- Total: 30
- Critical件数: 5
- High件数: 16
- KEV件数: 0
- Frontend件数: 9
- Backend件数: 21
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-11-03/frontend-summary.md)
- [Backend Summary](docs/2026-11-03/backend-summary.md)

## Today TOP5

- [CVE-2026-105769](https://github.com/chainguard-forks/kaniko/pull/495) CVE-2026-105769 / CRITICAL / backend
- [CVE-2026-120447](https://github.com/bufanyun/hotgo/blob/269b2f9e435cf8ff6b18d53bc053a905f4e02d11/server/internal/logic/sys/sms_log.go) CVE-2026-120447 / CRITICAL / backend
- [CVE-2026-120459](https://github.com/mpdavis/python-jose/blob/3.5.0/jose/backends/cryptography_backend.py) CVE-2026-120459 / CRITICAL / backend
- [CVE-2026-119085](https://aws.amazon.com/security/security-bulletins/2026-162-aws/) CVE-2026-119085 / CRITICAL / backend
- [CVE-2026-102435](https://plugins.svn.wordpress.org/ultimate-addons-for-contact-form-7/tags/3.5.52/addons/pdf-generator/pdf-generator.php) CVE-2026-102435 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ
本日のダイジェストでは、認証バイパス（JWT検証の不備）、CI/CDビルドツールにおけるトークン漏洩、テンプレートインジェクションによるクラウド権限奪取など、**ライブラリや開発・運用ツールに潜むCRITICALレベルの脆弱性**が目立ちます。特にWebアプリケーションの認証基盤やコンテナビルドパイプラインの安全確認が急務です。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-120459 (python-jose)**
   * **CVSS / 深刻度**: 9.1 / CRITICAL
   * **カテゴリ**: backend
   * **概要**: HMACシークレットが空（長さ0）の場合にJWT検証を通過させてしまう脆弱性。攻撃者が任意のクレームを持つトークンを偽造し、認証をバイパスできます。

2. **CVE-2026-105769 (kaniko)**
   * **CVSS / 深刻度**: 9.3 / CRITICAL
   * **カテゴリ**: backend
   * **概要**: レジストリ判定の正規表現の不備により、攻撃者が所有する特定ドメイン（例: `*.azurecr.io` を含むホスト）へAzure ADアクセストークンが送信され、認証情報が漏洩します。

3. **CVE-2026-119085 (Amazon Virtual Engineering Workbench)**
   * **CVSS / 深刻度**: 9.4 / CRITICAL
   * **カテゴリ**: backend
   * **概要**: テンプレートエンジンに対する不適切な中和処理により、任意コード実行が可能。Publishing LambdaのIAMロール権限を悪用され、全テナントのデータやリソースへアクセスされる恐れがあります。

4. **CVE-2026-120447 (HotGo)**
   * **CVSS / 深刻度**: 9.2 / CRITICAL
   * **カテゴリ**: backend
   * **概要**: SMSログイン送信エンドポイントでユーザー側が検証コードを指定できる実装不備。電話番号を知っている攻撃者が任意コードを設定して管理者アカウント等を奪取可能です。

---

## 開発者向けコメント

* **認証ライブラリ・ロジックの緊急確認**: `python-jose` を利用して認証を実装している場合は、空の鍵に対するバリデーション処理を確認するか、修正バージョンへ速やかにアップデートしてください。
* **CI/CD環境のクレデンシャル保護**: `kaniko` を含むコンテナビルドツールで外部レジストリへイメージをプッシュする際、アクセストークンが必要以上に広い範囲に送信されないようバージョン更新およびアクセス権限の最小化を行ってください。
* **入力値バリデーションと認可チェックの徹底**: 今回はファイル削除APIでのパストラバーサル（GoFound）や、権限チェック不足（Munshi）による不必要なデータ削除の脆弱性も報告されています。破壊的処理を行うAPIエンドポイントでは、入力値の正規化と厳密な所有権チェックを徹底してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近では、Googleらによる130万台以上のAndroid TVを標的とした大規模ボットネットの解体や、AIを活用した200以上の組織への自動化攻撃が報告されています。また、暗号資産取引所からの多額の資金流出や政府機関・大学を狙った攻撃など、多様な領域で実際の被害が発生しています。英国NCSCも放置された脆弱性を突く攻撃の急増を警告しており、脅威の広範化と高度化が懸念されます。

- **HIGH** [Tech Firms Dismantle Botnet That Turned 1.3M TV Boxes Into Proxies](https://krebsonsecurity.com/2026/11/tech-firms-dismantle-botnet-that-turned-1-3m-tv-boxes-into-proxies/) — Krebs on Security
- **HIGH** [Largest crypto exchange in Brazil confirms cyberattack as millions flow out of platform](https://therecord.media/mercado-bitcoin-brazil-cryptocurrency-heist) — The Record
- **HIGH** [Chinese hackers use ARTEX AI in automated attacks against 200 orgs](https://www.bleepingcomputer.com/news/security/chinese-hackers-use-artex-ai-in-automated-attacks-against-200-orgs/) — BleepingComputer
- **HIGH** [Michigan State cyber incident claimed by ransomware gang behind recent hospital attack](https://therecord.media/michigan-state-university-byod-gang-cyber-incident) — The Record
- **HIGH** [Google disrupts million-device XCPE Android malware botnet, bans TV box maker](https://www.bleepingcomputer.com/news/security/google-disrupts-million-device-xcpe-android-malware-botnet-bans-tv-box-maker/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

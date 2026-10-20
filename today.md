# CVE Digest Dashboard (2026-10-20)

## Overview

- Total: 30
- Critical件数: 5
- High件数: 8
- KEV件数: 0
- Frontend件数: 7
- Backend件数: 23
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-20/frontend-summary.md)
- [Backend Summary](docs/2026-10-20/backend-summary.md)

## Today TOP5

- [CVE-2026-109437](https://github.com/CognicellAI/Cognition/releases/tag/v0.13.0) CVE-2026-109437 / CRITICAL / frontend
- [CVE-2026-111057](https://github.com/mljar/mercury/commit/8c467129037ee9df269d543ac217ffd33b97bf3f) CVE-2026-111057 / CRITICAL / backend
- [CVE-2026-112393](https://github.com/python-pillow/Pillow/commit/11582e5ffbdceb973d5ee593f3105af5a9852b40) CVE-2026-112393 / CRITICAL / backend
- [CVE-2026-111058](https://github.com/mljar/mercury/commit/73a40ceb0becf057f495a5738ad7f5a5222a53e1) CVE-2026-111058 / CRITICAL / backend
- [CVE-2026-112776](https://github.com/craftcms/cms/security/advisories/GHSA-7rr3-4jcm-x526) CVE-2026-112776 / CRITICAL / frontend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載されたCVEでは、**Pythonエコシステム（Mercury、Pillow、AIOHTTP、docTR）やWeb API/CMSにおける深刻な脆弱性**が目立ちます。特にCVSS 9.0を超えるCRITICALな脆弱性が複数含まれており、認証バイパスや設定・実装上の不備から未認証でリモートコード実行（RCE）が可能になるケースが報告されています。また、AIOHTTPやPillowなど広範囲で利用されるライブラリで多数のDoSやメモリ関連の不具合が修正されています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-111057 (Mercury / CVSS 10.0 / CRITICAL)**
   - **概要:** 配列定義内のカンマ欠落によりブロックリストの正規表現が正しく機能せず、未認証の攻撃者がJupyter ServerのターミナルAPIにアクセスしてOSコマンドを実行可能。
2. **CVE-2026-109437 (Cognition / CVSS 9.8 / CRITICAL)**
   - **概要:** REST/SSE APIに認証が設定されておらず、デフォルトでローカルシェル実行となっているため、未認証の攻撃者がPOSTリクエスト経由で任意のシェルコマンドを実行（RCE）可能。
3. **CVE-2026-111058 (Mercury / CVSS 9.8 / CRITICAL)**
   - **概要:** デフォルトのトークンなしデプロイにおいて`/api/kernels`エンドポイントの保護が不足しており、未認証で任意のPythonコードを実行可能。
4. **CVE-2026-112776 (Craft CMS / CVSS 9.8 / CRITICAL)**
   - **概要:** GraphQLトークンのサイトスコープチェック（`requireAllowedSite()`）が強制されない認可バイパスが存在し、別サイトのコンテンツ作成・削除や共通アセットの削除が可能。
5. **CVE-2026-112393 (Pillow / CVSS 9.2 / CRITICAL)**
   - **概要:** `_tiffWriteProc`での圧縮TIFFデータ保存処理におけるヒープバッファオーバーフローおよびメモリ漏洩の脆弱性。

---

## 開発者向けコメント

* **Pythonおよびデータ/AI系ライブラリの緊急アップデート:**
  MercuryやPillow、docTR、AIOHTTPなどの広く使われているPythonライブラリでRCEやDoS、ファイルディスクリプタ枯渇などの深刻な脆弱性が公表されています。特にAIOHTTPはバージョン`3.14.4`へ、Pillowは`13.0.0`へ、Mercuryは`3.2.6`へ至急アップグレードしてください。
* **APIのデフォルト認証と認可ロジックの再確認:**
  CognitionのようにAPI認証が欠落しているケースや、Craft CMSのようにトークンの範囲（スコープ）チェックが漏れているケースが散見されます。エンドポイントを露出させる際は、認証の必須化および適切なアクセス制御ロジックが働いているかを点検してください。
* **モデル・チェックポイント読み込みの安全化:**
  docTR（CVE-2026-112304）の事例のように、`torch.load`で`weights_only=True`を指定しない不安全なデシリアライズは、不正なPickleコードの実行につながります。機械学習モデルやチェックポイントを読み込む処理の実装を見直してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近24時間ではBleepingComputer、Dark Reading、The Recordから10件を収集しました。重要度HIGHは2件です。

- **HIGH** [Nikkei discloses third data breach in a month, 1.8M records exposed](https://www.bleepingcomputer.com/news/security/nikkei-discloses-third-data-breach-in-a-month-18m-records-exposed/) — BleepingComputer
- **HIGH** [ConnectWise suspends Cloud Backup service after supply chain attack](https://therecord.media/connectwise-suspends-cloud-backup-service-supply-chain-attack) — The Record
- **MEDIUM** [WordPress SEO plugin Rank Math compromised to backdoor websites](https://www.bleepingcomputer.com/news/security/wordpress-seo-plugin-rank-math-compromised-to-backdoor-websites/) — BleepingComputer
- **MEDIUM** [Researchers Infiltrate Microsoft Tech Support Scam Operation](https://www.darkreading.com/threat-intelligence/microsoft-tech-support-scam-operation) — Dark Reading
- **MEDIUM** ['AdFection' Turns Ad Impressions Into Zero-Click Spyware Delivery](https://www.darkreading.com/data-privacy/adfection-online-ads-spyware-delivery) — Dark Reading

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

# CVE Digest Dashboard (2026-10-25)

## Overview

- Total: 8
- Critical件数: 3
- High件数: 4
- KEV件数: 0
- Frontend件数: 0
- Backend件数: 4
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-25/frontend-summary.md)
- [Backend Summary](docs/2026-10-25/backend-summary.md)

## Today TOP5

- [CVE-2026-114820](https://www.oracle.com/security-alerts/alert-cve-2026-114820.html) CVE-2026-114820 / CRITICAL / security
- [CVE-2026-115933](https://gadvisory.org/advisories/PSA-2026-YT2HMH) CVE-2026-115933 / CRITICAL / security
- [CVE-2026-115557](http://www.openwall.com/lists/oss-security/2026/10/20/29) CVE-2026-115557 / CRITICAL / backend
- [CVE-2026-115969](https://drive.google.com/drive/folders/1-ENuA8hKauFSTrn55IRYPQBeKwMV9xwR?usp=sharing) CVE-2026-115969 / HIGH / security
- [CVE-2026-115970](https://drive.google.com/drive/folders/1ni6zbp75v4803pGCG_GGZwEkA0CtaLjl?usp=sharing) CVE-2026-115970 / HIGH / security

## Geminiによる今日の総括

## 今日のまとめ
本日掲載された8件のCVEでは、CVSS 9.0以上の非常に高いスコアを持つ脆弱性が複数含まれています。具体的には、リモートからのOSコマンドインジェクション（CVE-2026-115995）、トークン署名処理の欠陥による認証不備（CVE-2026-115933）、PythonやOracle Java SE/GraalVMといった言語ランタイム・標準ライブラリにおける問題（CVE-2026-115557, CVE-2026-114820）などが報告されています。また、開発が終了し非推奨・オフラインとなった製品（Travisun Opptrix）の脆弱性も含まれています。

## 優先して確認すべき3〜5件
1. **CVE-2026-115995 (CVSS 10.0 / HIGH)**
   Unitree Robotics Unitree Go2 の `gpt_thread.py` におけるリモートからのOSコマンドインジェクションの脆弱性。バージョン 1.1.11.5 へのアップグレードが必要です。
2. **CVE-2026-115933 (CVSS 9.9 / CRITICAL)**
   Postiz におけるトークン処理の欠陥。共通シークレットの使用およびトークン用途の識別子不足により、攻撃者が任意のクレームを含む有効な署名トークンを取得し、セッションや組織招待等を偽装できるリスクがあります。
3. **CVE-2026-115557 (CVSS 9.4 / CRITICAL)**
   Python の `ssl` モジュールに関する問題。侵害された既知の証明書拒否リスト（denylist）が追加され、SSLContext ポリシー設定に関わらず自動拒否する対応が行われています。
4. **CVE-2026-114820 (CVSS 9.1 / CRITICAL)**
   Oracle Java SE および GraalVM の JSSE コンポーネントに存在する脆弱性。ネットワーク経由での未認証攻撃者による容易な利用が懸念されます。

## 開発者向けコメント
利用中の言語ランタイム（PythonやJava/GraalVM）に重要な修正が含まれているため、修正版の適用環境を確認してください。また、認証・認可トークンの実装において、同一シークレットの使い回しやトークン種別（セッション用、パスワードリセット用など）の検証漏れ（CVE-2026-115933）は深刻なセキュリティリスクに直結するため、実装の再確認が推奨されます。なお、Travisun Opptrix のようにプロジェクト自体が廃止・非公開化されたコンポーネントを利用している場合は、迅速に撤去または代替品へ移行してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

古い脆弱性を悪用してSecure Bootを回避し、セキュリティ製品を妨害する新しいUEFIブートキット「BlackX」が報告されました。このブートキットは2026年初頭の諜報キャンペーンで展開され、実際の悪用が確認されています。高度な攻撃手法を用いたスパイ活動に対する警戒が必要です。

- **HIGH** [BlackX UEFI bootkit exploits Baton Drop flaw to bypass Secure Boot](https://www.bleepingcomputer.com/news/security/blackx-uefi-bootkit-exploits-baton-drop-flaw-to-bypass-secure-boot/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

# CVE Digest Dashboard (2026-09-15)

## Overview

- Total: 30
- Critical件数: 5
- High件数: 13
- KEV件数: 0
- Frontend件数: 13
- Backend件数: 17
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-15/frontend-summary.md)
- [Backend Summary](docs/2026-09-15/backend-summary.md)

## Today TOP5

- [CVE-2026-20353](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm) CVE-2026-20353 / CRITICAL / backend
- [CVE-2026-76440](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm) CVE-2026-76440 / CRITICAL / backend
- [CVE-2026-76441](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm) CVE-2026-76441 / CRITICAL / backend
- [CVE-2026-76443](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm) CVE-2026-76443 / CRITICAL / backend
- [CVE-2026-61534](https://github.com/confetti/yayson/commit/e460162d5a3ebac86424bead7424957c36f8dff9) CVE-2026-61534 / CRITICAL / frontend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載された脆弱性には、Cisco製品における複数の深刻な脆弱性（CVSS 9.8）をはじめ、JavaScript/Node.js環境におけるプロトタイプ汚染（Yayson, gettext-converter）、gRPC-GoでのDoS（クラッシュ）、LangChain MongoDBでのNoSQLインジェクション、WebSocketを介した任意ファイル読み取り（DeepWiki-Open）などが含まれています。サードパーティ製ライブラリにおける入力検証の不備や境界値の取り扱い不備に起因する脆弱性が多数を占めています。

---

## 優先して確認すべき3〜5件

1. **Cisco製品群の脆弱性（CVE-2026-76440, CVE-2026-76441, CVE-2026-76443, CVE-2026-20353）**
   - **Severity**: CRITICAL (CVSS 9.8)
   - **概要**: Cisco Secure Email Gateway / Web Managerにおけるパストラバーサルや不適切なアクセス制御、無害化不備などの脆弱性。対象製品を利用している場合は速やかなアップデートが必要です。
2. **CVE-2026-61534 (Yayson)**
   - **Severity**: CRITICAL (CVSS 9.1)
   - **概要**: JSON:API解析ライブラリにおけるプロトタイプ汚染の脆弱性。攻撃者が `__proto__` を含むタイプ名を送信することで `Object.prototype` を汚染される恐れがあります（バージョン 4.3.0 で修正）。
3. **CVE-2026-90946 (DeepWiki-Open)**
   - **Severity**: HIGH (CVSS 8.7)
   - **概要**: 未認証のWebSocketエンドポイント (`/ws/chat`) で任意パスが指定可能となっており、ハードコードされた認証情報を含むサーバー上の任意ファイルが読み取られるリスクがあります。
4. **CVE-2026-84445 (gRPC-Go)**
   - **Severity**: HIGH (CVSS 8.7)
   - **概要**: `:authority` および `Host` ヘッダーを含まないリクエスト処理時にスライス参照の範囲外アクセスによるパニックが発生し、リモートからサーバーをクラッシュ（DoS）させられる可能性があります。
5. **CVE-2026-55253 (LangChain MongoDB)**
   - **Severity**: HIGH (CVSS 7.7)
   - **概要**: フィルター引数内で `$` プレフィックスを持つキーが再帰的に除外されないため、攻撃者がMongoDBクエリ言語（NoSQL）を注入できる状態になっていました。

---

## 開発者向けコメント

* **オブジェクトキーとプロトタイプ汚染の対策**: JavaScriptライブラリ（Yayson、gettext-converter）に見られるように、外部からの入力値をプレーンオブジェクトのキーとして直接扱う実装はプロトタイプ汚染を引き起こします。入力キーにおける `__proto__` や `constructor` の検証・拒否、または `Map` オブジェクトの採用を徹底してください。
* **入力値の妥当性検証とサニタイズ**: LangChain MongoDBでのNoSQLインジェクションやArgos SDKでのCIパラメータ経由のコマンド注入（`execSync`）など、信頼できない入力値がバックエンドやシェルコマンドに直接渡る実装が散見されます。演算子や特殊文字の無害化・検証処理を実装してください。
* **依存ライブラリの最新化**: gRPC-Goやcontainred、devpiなどの基盤ライブラリ・ツールにも脆弱性が報告されています。利用している依存パッケージのバージョンを確認し、修正版への更新を推奨します。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

GitLabにおける最高深刻度の脆弱性や、露出したVite開発サーバーを狙う大規模スキャンなど、開発・クラウド基盤を標的とした深刻な脅威が報告されています。また、日本のデジタル庁におけるVPN脆弱性を原因とした個人情報漏えいや、Cisco脆弱性を連鎖悪用する攻撃グループ「Sandworm」など、実被害を伴う攻撃も相次いでいます。さらに、今月のセキュリティ更新に起因する障害に対処するため、Microsoftが緊急の帯域外アップデートを配信しています。

- **HIGH** ['Sandworm' Chains Cisco Vulnerabilities to Deploy Cyclops Blink](https://www.darkreading.com/cyberattacks-data-breaches/sandworm-chains-cisco-vulnerabilities-cyclops-blink) — Dark Reading
- **HIGH** [Japan's Digital Agency says VPN flaw exposed 246,000 personnel records](https://www.bleepingcomputer.com/news/security/japans-digital-agency-says-vpn-flaw-exposed-246-000-personnel-records/) — BleepingComputer
- **HIGH** [Maximum Severity GitLab Flaw Puts Supply Chains at Risk](https://www.darkreading.com/cyberattacks-data-breaches/maximum-severity-gitlab-flaw-supply-chains-risk) — Dark Reading
- **HIGH** [Hackers target exposed Vite dev servers to steal AWS, Azure secrets](https://www.bleepingcomputer.com/news/security/hackers-target-exposed-vite-dev-servers-to-steal-aws-azure-secrets/) — BleepingComputer
- **MEDIUM** [Microsoft releases emergency Windows updates to fix RDS failures](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-emergency-windows-updates-to-fix-rds-failures/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

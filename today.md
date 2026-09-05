# CVE Digest Dashboard (2026-09-05)

## Overview

- Total: 30
- Critical件数: 4
- High件数: 8
- KEV件数: 0
- Frontend件数: 4
- Backend件数: 26
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-05/frontend-summary.md)
- [Backend Summary](docs/2026-09-05/backend-summary.md)

## Today TOP5

- [CVE-2026-85684](https://github.com/datalab-to/marker) CVE-2026-85684 / CRITICAL / backend
- [CVE-2026-85694](https://github.com/lavague-ai/LaVague) CVE-2026-85694 / CRITICAL / backend
- [CVE-2026-85625](https://github.com/crcn/sift.js) CVE-2026-85625 / CRITICAL / frontend
- [CVE-2026-19274](https://www.ibm.com/support/pages/node/7286070) CVE-2026-19274 / CRITICAL / backend
- [CVE-2026-85692](https://github.com/ccfos/nightingale) CVE-2026-85692 / HIGH / backend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載された脆弱性には、Kubernetesオペレーターの権限侵害、AI/LLM関連ライブラリでのコード実行やSQLインジェクション、FastAPIやJavaScriptライブラリでのパス・トラバーサルやコード実行といった影響度の高い（CRITICAL / HIGH）脆弱性が複数含まれています。その他にも、Linuxカーネル関連のバグやWebアプリケーションにおけるアクセス制御の不備・XSSなどが多数報告されています。

## 優先して確認すべき3〜5件

* **CVE-2026-19274**（CVSS 9.6 / CRITICAL）: **IBM Instana Agent Operator**
  KubernetesのクラスタスコープのRBACオブジェクトが名前空間なしのCR名のみで識別されているため、悪意のある同一名のCRによって他テナントのクラスタレベルRBAC権限の乗っ取りや削除・破棄が行える脆弱性。
* **CVE-2026-85625**（CVSS 9.2 / CRITICAL）: **sift (sift.js)**
  `for...in`によるプロトタイプチェーンの走査と`new Function`を用いた`$where`の評価により、他でプロトタイプ汚染が存在する場合に任意のJavaScriptが実行される脆弱性。
* **CVE-2026-85694**（CVSS 9.2 / CRITICAL）: **LaVague**
  Webページの内容を利用した間接的なプロンプトインジェクションにより、LLMが生成した未検証のPythonコードを実行してしまうリモートコード実行（RCE）の脆弱性。
* **CVE-2026-85684**（CVSS 9.1 / CRITICAL）: **marker**
  FastAPIの`/marker/upload`ハンドラにおいてファイル名のサニタイズが行われておらず、ディレクトリ・トラバーサルによってシステムの任意位置へのファイル書き込みおよび削除が可能な脆弱性。

## 開発者向けコメント

* **AI/LLM連携の安全性確保**: LLMが処理する入力データ（間接的なプロンプトインジェクションの可能性）や、LLMが生成したコード・クエリの扱い（`eval`や未パラメータ化SQLへの挿入など）には十分な検証とサニタイズを実施してください。
* **入力検証とパス制御**: ファイルアップロードやファイル参照を実装する際は、ディレクトリ・トラバーサル対策としてファイル名やパスの厳格な検証を行ってください。
* **権限設計とアクセス制御**: Kubernetesのオペレーター開発におけるリソース識別管理や、マルチテナント/複数ユーザー環境での所有権検証（SupabaseやPDF参照等のアクセス制御）を再確認し、認可の漏れを防ぐ構造にしてください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

Citrix NetScalerの脆弱性に対する実際の悪用発生やHPE製品のクリティカルなRCEパッチ公開など、インフラ製品の脆弱性対応が急務となっています。また、1億5,300万人規模のデータ侵害疑惑やパスキー認証の回避手法など、データ管理や認証技術を巡る脅威も浮き彫りになりました。これに対し、AIを用いた自律型攻撃への懸念が高まる一方で、重要インフラ防衛に向けた支援策や国際連携などの対抗策も進められています。

- **HIGH** [IDScan sued over alleged data breach affecting 153 million drivers](https://www.bleepingcomputer.com/news/security/idscan-sued-over-alleged-data-breach-affecting-153-million-drivers/) — BleepingComputer
- **HIGH** [HPE Patches Critical RCE Vulnerabilities in AOS-CX](https://www.securityweek.com/hpe-patches-critical-rce-vulnerabilities-in-aos-cx/) — SecurityWeek
- **HIGH** [Critical Citrix NetScaler auth bypass now leveraged in attacks](https://www.bleepingcomputer.com/news/security/hackers-target-critical-citrix-netscaler-auth-bypass-in-attacks/) — BleepingComputer
- **MEDIUM** [In Other News: Microsoft’s Cloud Patches, Hacked Dropbox Accounts, Guardio’s $1.1B Valuation](https://www.securityweek.com/in-other-news-microsofts-cloud-patches-hacked-dropbox-accounts-guardios-1-1b-valuation/) — SecurityWeek
- **MEDIUM** [OpenAI Pledges $1 Billion to Bring Frontier AI to Critical Infrastructure Defenders](https://www.securityweek.com/openai-pledges-1-billion-to-bring-frontier-ai-to-critical-infrastructure-defenders/) — SecurityWeek

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

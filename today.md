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

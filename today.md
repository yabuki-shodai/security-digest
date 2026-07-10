# CVE Digest Dashboard (2026-07-10)

## Overview

- Total: 2
- Critical件数: 1
- High件数: 1
- KEV件数: 0
- Frontend件数: 0
- Backend件数: 2
- GitHub Models総括: GitHub Models

## Links

- [Frontend Summary](docs/2026-07-10/frontend-summary.md)
- [Backend Summary](docs/2026-07-10/backend-summary.md)

## Today TOP5

- [CVE-2026-54769](https://github.com/langroid/langroid/security/advisories/GHSA-q9p7-wqxg-mrhc) CVE-2026-54769 / CRITICAL / backend
- [CVE-2026-15317](https://github.com/sipeed/picoclaw/) CVE-2026-15317 / HIGH / backend

## GitHub Modelsによる今日の総括

## 今日のまとめ
本日は、サーバーサイドリクエストフォージェリ（SSRF）やサンドボックス回避によるリモートコード実行（RCE）など、リモート攻撃に直結する重大な脆弱性が報告されました。特に、Go言語のWebツールとPythonの大規模言語モデルフレームワークに影響する問題が含まれています。

## 優先して確認すべき3〜5件
1. CVE-2026-54769（CRITICAL, CVSS 10.0）  
   Langroidフレームワークにおけるサンドボックス回避によるRCE。バージョン0.65.2未満が対象。  
2. CVE-2026-15317（HIGH, CVSS 7.5）  
   Sipeed PicoClawのWebFetchTool.Execute関数におけるSSRF。リモートからの攻撃が可能。

## 開発者向けコメント
- Langroidの脆弱性は、Pythonの`eval()`関数のサンドボックス制御が不完全であることに起因します。外部からの入力を評価する際は、信頼できる環境でのみ実行し、可能な限り`eval()`の使用を避けるか安全な代替手段を検討してください。  
- Sipeed PicoClawのSSRF問題は、外部リクエストの入力検証不足が原因です。外部URLの取り扱い時はホワイトリストやアクセス制限を設け、不正なリクエストを防止してください。  
- いずれの脆弱性も公開済みのため、速やかなアップデートと影響範囲の確認を推奨します。

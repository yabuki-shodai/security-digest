# CVE Digest Dashboard (2026-09-12)

## Overview

- Total: 30
- Critical件数: 2
- High件数: 6
- KEV件数: 0
- Frontend件数: 6
- Backend件数: 24
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-12/frontend-summary.md)
- [Backend Summary](docs/2026-09-12/backend-summary.md)

## Today TOP5

- [CVE-2026-3869](https://download.se.com/files?p_Doc_Ref=SEVD-2026-251-04&p_enDocType=Security+and+Safety+Notice&p_File_Name=SEVD-2026-251-04.pdf) CVE-2026-3869 / CRITICAL / backend
- [CVE-2026-54072](https://github.com/authorizerdev/authorizer/security/advisories/GHSA-h29v-hj44-q8cv) CVE-2026-54072 / CRITICAL / frontend
- [CVE-2026-68497](https://github.com/FasterXML/jackson-databind/commit/a99b7e74c8928f43f6975773a8c862c8316178bd) CVE-2026-68497 / HIGH / backend
- [CVE-2026-89090](https://aws.amazon.com/security/security-bulletins/2026-110-aws/) CVE-2026-89090 / HIGH / backend
- [CVE-2026-89099](https://jira.mongodb.org/browse/SERVER-134063) CVE-2026-89099 / HIGH / backend

## Geminiによる今日の総括

## 今日のまとめ

本日の脆弱性情報では、**OAuth認証サーバーにおけるトークン奪取につながる欠陥**や**GraphQL/API層での認可制御の不備**、さらには**SQLインジェクション**や**SDK・DBのクラッシュ（DoS）問題**が目立ちます。特に、認証基盤や各種フレームワーク・ライブラリのセキュリティ構成に関する確認が重要です。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-54072 (CRITICAL, CVSS 9.3) - Authorizer 認証サーバー**
   - **概要:** `/authorize` エンドポイントで `redirect_uri` の検証が行われず、リダイレクト時にアクセストークンやリフレッシュトークンが外部へ漏洩する。
   - **対策:** 2.2.1 以降へアップデート。

2. **CVE-2026-3869 (CRITICAL, CVSS 9.2) - PLC 認証メカニズム**
   - **概要:** 認証アルゴリズムの実装不備（CWE-303）により、機密性・完全性・利用可能性が脅かされる可能性がある。
   - **対策:** 関連機器・プロジェクトのアクセス制御および修正パッチの確認。

3. **CVE-2026-72708 (HIGH, CVSS 8.7) - SPIP (CMS)**
   - **概要:** サイトマップ用エスケープ処理の欠陥により、未認証の攻撃者が任意SQLを実行できる Blind SQL Injection 脆弱性。
   - **対策:** SPIP 4.4.18 以降へアップデート。

4. **CVE-2026-89090 (HIGH, CVSS 8.2) - AWS SDK for Go v2**
   - **概要:** 不正なイベントストリームデータを受信した際、未復旧のパニック（Go panic）が発生し、アプリプロセスが停止する。
   - **対策:** `release-2026-03-23` 以降に更新。

5. **CVE-2026-49463 (MEDIUM, CVSS 6.5) / CVE-2026-49462 (MEDIUM, CVSS 5.3) - NL Portal (GraphQL)**
   - **概要:** GraphQLリゾルバでのユーザー別認可チェックの欠如（他人のドキュメント等の参照）および本番環境でのGraphiQL/スキーマ参照の露出。
   - **対策:** 3.0.1 以降への更新とイントロスペクション設定の確認。

---

## 開発者向けコメント

- **OAuth/認証リダイレクトの再確認:** `redirect_uri` のドメイン検証漏れは、認証トークンがそのまま第三者に渡る重大な欠陥となります。ホワイトリスト検証が確実に行われているか再点検してください。
- **GraphQLにおける認可とデバッグ機能制御:** スキーマ定義だけでなく、各リゾルバ層で「認証済みユーザーがそのオブジェクトへのアクセス権を持つか（BOLA対策）」を個別に検証してください。また、本番環境での GraphiQL ツールやスキーマイントロスペクションの無効化も徹底しましょう。
- **サードパーティライブラリの例外ハンドリング:** SDKや共通ライブラリ（AWS SDK, jackson-databind等）のデータパース時にアプリ全体が落とされないよう、最新版への追従と適切なエラー処理を行ってください。

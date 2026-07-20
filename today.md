# CVE Digest Dashboard (2026-07-21)

## Overview

- Total: 30
- Critical件数: 6
- High件数: 7
- KEV件数: 0
- Frontend件数: 20
- Backend件数: 10
- GitHub Models総括: GitHub Models

## Links

- [Frontend Summary](docs/2026-07-21/frontend-summary.md)
- [Backend Summary](docs/2026-07-21/backend-summary.md)

## Today TOP5

- [CVE-2026-54051](https://github.com/Jovancoding/Network-AI/commit/379f77656b578144e03415c5b134d8309a4b5792) CVE-2026-54051 / CRITICAL / frontend
- [CVE-2026-46412](https://github.com/BeProduct/beproduct-org-nestjs-auth/security/advisories/GHSA-6xwp-cp5h-q856) CVE-2026-46412 / CRITICAL / frontend
- [CVE-2026-35048](https://github.com/Piwigo/Piwigo/security/advisories/GHSA-gphq-34pv-gvf3) CVE-2026-35048 / CRITICAL / backend
- [CVE-2026-53595](https://github.com/freescout-help-desk/freescout/security/advisories/GHSA-jqj5-r72v-v29g) CVE-2026-53595 / CRITICAL / frontend
- [CVE-2026-35198](https://github.com/heyform/heyform/commit/cc97d27a57ae400fec23abf5dcf6f9533c3b5db3) CVE-2026-35198 / CRITICAL / frontend

## GitHub Modelsによる今日の総括

## 今日のまとめ
本日のCVEでは、特にTypeScript/Node.js製のNetwork-AIに多数の脆弱性が報告されており、権限管理の不備やパス操作の不適切な検証、クロスサイトスクリプティング（XSS）など多岐にわたる問題が含まれています。また、認証不要でのアカウント乗っ取りや任意コード実行の脆弱性も複数見られ、特にnpmパッケージのマルウェア混入やPHP設定ファイルへのコード注入など、開発者の注意が必要な重大な問題が散見されます。

## 優先して確認すべき3〜5件
1. **CVE-2026-46412**（@beproduct/nestjs-auth）  
   - npmパッケージの悪意あるバージョン公開によるトークン・認証情報の窃取。  
   - クリティカル（CVSS 10.0）

2. **CVE-2026-54051**（Network-AI）  
   - コマンド実行のallowlist回避による任意コマンド実行。  
   - クリティカル（CVSS 9.9）

3. **CVE-2026-53595**（FreeScout）  
   - 認証不要でアカウント乗っ取り可能な認証バイパス。  
   - クリティカル（CVSS 9.4）

4. **CVE-2026-35048**（Piwigo）  
   - インストーラーの設定ファイルに未検証のPHPコード注入。  
   - クリティカル（CVSS 9.8）

5. **CVE-2026-39878**（Chamilo LMS）  
   - 未認証者による管理者アカウント乗っ取り可能なストアドXSS。  
   - クリティカル（CVSS 9.3）

## 開発者向けコメント
- 依存パッケージの信頼性を常に確認し、特にnpmなどの公開リポジトリからのパッケージは署名や公式ソースの検証を徹底してください。  
- 権限チェックの不備や認証バイパスは重大なリスクを伴うため、ユーザー権限の検証を厳格に実装し、サーバーサイドでのアクセス制御を強化しましょう。  
- コマンド実行やファイル操作においては、allowlistの実装方法やパスの正規化・検証を厳密に行い、シェルインジェクションやディレクトリトラバーサルを防止してください。  
- クロスサイトスクリプティング（XSS）対策として、ユーザー入力の適切なサニタイズとエスケープを徹底し、CSP（Content Security Policy）の導入も検討してください。  
- 脆弱性情報は速やかにキャッチアップし、可能な限り早期にパッチ適用やバージョンアップを行うことが重要です。

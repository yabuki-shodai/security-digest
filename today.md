# CVE Digest Dashboard (2026-08-18)

## Overview

- Total: 30
- Critical件数: 6
- High件数: 16
- KEV件数: 0
- Frontend件数: 8
- Backend件数: 22
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-18/frontend-summary.md)
- [Backend Summary](docs/2026-08-18/backend-summary.md)

## Today TOP5

- [CVE-2026-71479](https://github.com/QuantumNous/new-api/commit/c9943d37ad93477dd937fc4901cc3c4e0fd8aaab) CVE-2026-71479 / CRITICAL / backend
- [CVE-2026-55674](https://github.com/discourse/discourse/security/advisories/GHSA-qx4v-rg4v-pm2g) CVE-2026-55674 / CRITICAL / frontend
- [CVE-2026-19478](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/) CVE-2026-19478 / CRITICAL / frontend
- [CVE-2026-47686](https://github.com/patriksimek/vm2/commit/7e3faaf550f4ab975bf4cdde183fcec49b056d8e) CVE-2026-47686 / CRITICAL / backend
- [CVE-2026-47698](https://github.com/patriksimek/vm2/commit/a85acb61f81402c6eabf32760aa11272af6d0f9e) CVE-2026-47698 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ
未認証でリモートコード実行（RCE）が可能な脆弱性（Joomla拡張、Node.js用サンドボックス`vm2`）や、基幹ツールにおける深刻な認証・認可の不備（GitLab、Discourse）など、CRITICALおよびHIGH評価の脆弱性が多数公開されました。また、ライブラリ層（Pythonの`sqlparse`におけるDoSやコード注入など）の脆弱性も多く含まれており、依存関係の確認と早期アップデートが求められます。

## 優先して確認すべき3〜5件
1. **CVE-2026-74253 (Joomla Regular Labs Sourcerer / CVSS 10.0 - CRITICAL)**
   - **概要:** 未認証の攻撃者が `{source}` ブロックを介して任意のコードを実行できる脆弱性。
   - **対応:** Sourcerer 14.0.0 未満を使用している場合は直ちに更新してください。

2. **CVE-2026-47686 / CVE-2026-47698 (Node.js vm2 / CVSS 9.9・9.8 - CRITICAL)**
   - **概要:** `Error.cause` の処理不備やプロトタイプチェーン操作により、サンドボックスを脱出してホスト上で任意コマンドを実行可能。
   - **対応:** `vm2` を 3.11.6 以降へアップデートしてください。

3. **CVE-2026-19478 (GitLab CE/EE / CVSS 9.4 - CRITICAL)**
   - **概要:** 未認証ユーザーが GraphQL ディレクティブを悪用し、パブリックプロジェクトやユーザーデータをリモートで変更・削除できる脆弱性。
   - **対応:** GitLab を指定の修正バージョン（18.11.11, 19.0.8, 19.1.6, 19.2.4 以降）へ更新してください。

4. **CVE-2026-55674 (Discourse / CVSS 9.3 - CRITICAL)**
   - **概要:** 特定のCookie値に対するエスケープ処理不足により、NonceベースのCSPをバイパスして任意JavaScriptを実行可能な未認証XSS。
   - **対応:** 修正済みバージョン（2026.1.6, 2026.5.2, 2026.6.1, 2026.7.0等）へ更新してください。

## 開発者向けコメント
- **動的実行・サンドボックス利用の再見直し**: Node.js環境（`vm2`）やPython（`eval()` の使用例など）での動的評価処理は極めて高リスクです。該当モジュールのアップデートを実施するとともに、不要な評価処理の削除を検討してください。
- **GraphQL / APIの境界検証強化**: GETリクエスト経由のミューテーション実行（CVE-2026-19650）やディレクティブの制御不足（CVE-2026-19478）など、API層での想定外の操作を防止する権限チェックとバリデーションを徹底してください。
- **間接依存ライブラリの更新**: `sqlparse` など、テキスト解析ライブラリに対する crafted 入力による CPU 高負荷（DoS）脆弱性が散見されます。`npm` や `pip` の依存関係ツリーを確認し、ライブラリ全体の最新化を行ってください。

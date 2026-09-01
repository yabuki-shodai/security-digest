# CVE Digest Dashboard (2026-09-01)

## Overview

- Total: 30
- Critical件数: 5
- High件数: 16
- KEV件数: 0
- Frontend件数: 10
- Backend件数: 20
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-01/frontend-summary.md)
- [Backend Summary](docs/2026-09-01/backend-summary.md)

## Today TOP5

- [CVE-2026-53552](https://github.com/zhenorzz/goploy/security/advisories/GHSA-26rh-24rg-j3vv) CVE-2026-53552 / CRITICAL / backend
- [CVE-2026-76133](https://github.com/cisagov/CSAF/blob/develop/csaf_files/OT/white/2026/icsa-26-237-06.json) CVE-2026-76133 / CRITICAL / backend
- [CVE-2026-79748](https://github.com/samanhappy/mcphub/pull/770) CVE-2026-79748 / CRITICAL / backend
- [CVE-2026-66047](https://profilepress.com/changelog/) CVE-2026-66047 / CRITICAL / backend
- [CVE-2026-82954](https://vuldb.com/cve/CVE-2026-82954) CVE-2026-82954 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載された脆弱性では、CI/CD・デプロイ自動化ツール（Dokploy、Goploy）、マルチMCP管理基盤（MCPHub）、認証・アクセス制御基盤（Pangolin）など、インフラや開発運用を担うツールにおける**リモートコード実行（RCE）や認証・認可バイパス**の深刻な脆弱性が複数報告されています。

また、フロントエンド・Node.js生態系で広く使われるパッケージマネージャー**pnpm**におけるパストラバーサル（任意ファイル書き込み）や、Pythonの標準的なWebフレームワーク**Tornado**におけるリクエスト解析起因のDoSなど、開発・運用環境双方に影響する脆弱性が含まれています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-79748（MCPHub）- CVSS 9.9（CRITICAL）**
   * **概要**: サーバー設定エンドポイントにおいて管理者権限チェックが欠落しており、管理者以外の認証済みユーザーが任意コマンド（`child_process.spawn`）を実行可能。
   * **対策**: バージョン 0.12.15 以降へアップデート。

2. **CVE-2026-82954（Dokploy）- CVSS 9.9（CRITICAL）**
   * **概要**: SettingsコンポーネントにおけるTraefik設定書き込み処理のパラメータ操作により、リモートから任意のパストラバーサルが可能。
   * **対策**: 修正版バージョンへの更新または適切な入力検証の実装。

3. **CVE-2026-53552（Goploy）- CVSS 9.6（CRITICAL）**
   * **概要**: APIエンドポイントでリクエストされたIDの所有・ネームスペース検証が欠落しており、同一システム上の他プロジェクトのファイル取得・編集・削除が可能。
   * **対策**: バージョン 1.18.0 以降へアップデート。

4. **CVE-2026-72001（Pangolin）- CVSS 8.6（HIGH）**
   * **概要**: 共有リンク認証エンドポイントのトークン検証時にリソース識別子が漏れるため、有効な共有リンクを1つ保持していれば、他組織を含む任意のリソースに認証を回避してアクセス可能。
   * **対策**: バージョン 1.22.0 以降へアップデート。

5. **CVE-2026-82393 / CVE-2026-82392（pnpm）- CVSS 7.5 / 7.1（HIGH）**
   * **概要**: `package.json` の名前フィールドや `pnpm-lock.yaml` のキー検証不足により、`pnpm install` 実行時に `node_modules` 外へ任意ファイルを解凍・書き込みされる危険性。
   * **対策**: pnpm を 10.34.5 または 11.11.0 以降へアップデート。

---

## 開発者向けコメント

* **開発環境・CIパイプラインの保護（pnpmの更新）**:
  悪意ある依存パッケージやロックファイルによって、開発機やCI実行環境上の任意パスへファイルが書き込まれる恐れがあります。プロジェクトで利用する `pnpm` のバージョンを早急に更新してください。

* **デプロイ・管理ツールのアクセス制御再点検**:
  GoployやMCPHubのように、アクセス制御（テナント分離や管理者権限チェック）の欠落によって他データの不正操作や任意コード実行につながる事例が目立ちます。自作APIのエンドポイントでも「ユーザーが所有するリソースか」の認可チェック（IDOR対策）が漏れていないか見直してください。

* **リクエスト解析処理の制限設定（Tornado等）**:
  Tornado（CVE-2026-82397）のように、フォームデータの解析時に最大フィールド数（`max_num_fields`）制限を設けていない場合、大量のパラメータを送信されるだけでCPU枯渇（DoS）を引き起こします。Webフレームワークのリクエスト制限設定が適切か確認してください。

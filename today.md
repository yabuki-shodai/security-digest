# CVE Digest Dashboard (2026-09-16)

## Overview

- Total: 30
- Critical件数: 3
- High件数: 16
- KEV件数: 0
- Frontend件数: 19
- Backend件数: 11
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-16/frontend-summary.md)
- [Backend Summary](docs/2026-09-16/backend-summary.md)

## Today TOP5

- [CVE-2026-91931](https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-vcwp-f9rq-3887) CVE-2026-91931 / CRITICAL / frontend
- [CVE-2026-61549](https://github.com/woodpecker-ci/woodpecker/commit/5df9d52260626c074c6caafb2dc83d3bc6b53be1) CVE-2026-61549 / CRITICAL / backend
- [CVE-2026-91949](https://github.com/FreeRDP/FreeRDP/security/advisories/GHSA-x7v6-xfx3-52j6) CVE-2026-91949 / CRITICAL / backend
- [CVE-2026-59160](https://github.com/DerYeger/yeger/commit/a6c41db6b575cccdd8ff89dbe8ce1792ad062852) CVE-2026-59160 / HIGH / frontend
- [CVE-2026-91983](https://github.com/go-vikunja/vikunja/security/advisories/GHSA-9rg3-v78m-26q8) CVE-2026-91983 / MEDIUM / frontend

## Geminiによる今日の総括

## 今日のまとめ

本日掲載された脆弱性では、CI/CDツール（Woodpecker）やAI/MCP（Model Context Protocol）関連フレームワーク（Flowise、MCP Gateway等）、リモートデスクトップ基盤（FreeRDP）において、**CRITICAL（緊急）およびHIGH（高）**の深刻度を持つ脆弱性が多数報告されています。特に、パイプライン構成やコンテナメタデータ（OCIラベル）、外部入力（npxパッケージ名等）の不適切な処理に起因する任意コード実行（RCE）や権限昇格リスクに注意が必要です。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-91949（FreeRDP | CVSS 9.3 | CRITICAL）**
   - **概要**: 未認証の攻撃者がプロトコルネゴシエーションの失敗を悪用してRDSTLS接続を確立し、事前認証トランスポートの制限を迂回できる脆弱性。
2. **CVE-2026-91931（Flowise | CVSS 9.0 | CRITICAL）**
   - **概要**: Custom MCPノードのパラメータに任意のnpxパッケージ名を渡すことで、サーバー上でリモートコード実行（RCE）が可能になる脆弱性。
3. **CVE-2026-61549（Woodpecker CI/CD | CVSS 9.0 | CRITICAL）**
   - **概要**: Kubernetesバックエンドにおいて、パイプライン設定内の`serviceAccountName`が管理者検証なしでポッド仕様にコピーされ、リポジトリへのPush権限を持つユーザーが任意のServiceAccount権限を奪取できる脆弱性。
4. **CVE-2026-55887（MCP Gateway | CVSS 8.7 | HIGH）**
   - **概要**: 攻撃者が制御可能なOCIイメージラベルのパース処理不備により、`docker run`コマンドの引数（VolumesやExtraHostsなど）を改ざん・注入される脆弱性。

---

## 開発者向けコメント

AI/MCP連携ツールやCI/CD基盤など、高度な自動化権限を持つミドルウェアのセキュリティアップデートを最優先で実施してください。
開発においては、**「パイプライン定義ファイル」や「コンテナイメージのメタデータ（OCIラベル等）」などの設定値を安易に信用せず、実行権限の適用前に対象の権限チェックや入力値のバリデーションを厳格に行うこと**が必要です。また、npx等の外部パッケージ動的実行や、Kubernetes ServiceAccountの引き継ぎ設定に対する最小権限原則の徹底を推奨します。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

プラグインを標的とした悪用中の脆弱性やサプライチェーン攻撃によるバックドア設置など、実際の攻撃事例が相次いで報告されています。また、大手エネルギー企業における顧客データの漏洩や、イランのサイバースパイによる標的型ハッキングなど具体的な被害も確認されました。さらに、Microsoftによるパッチ適用後の緊急修正や新たなMaaSプラットフォームの登場など、多様なセキュリティ動向が見られます。

- **HIGH** [Acronis warns of actively exploited flaw in its cPanel backup plugin](https://www.bleepingcomputer.com/news/security/acronis-warns-of-actively-exploited-flaw-in-its-cpanel-backup-plugin/) — BleepingComputer
- **HIGH** [Malcious Admin Menu Editor Pro plugin backdoors 1,500 WordPress sites](https://www.bleepingcomputer.com/news/security/malcious-admin-menu-editor-pro-plugin-backdoors-1-500-wordpress-sites/) — BleepingComputer
- **HIGH** [CenterPoint Energy confirms customer data stolen in cyberattack](https://www.bleepingcomputer.com/news/security/centerpoint-energy-confirms-customer-data-stolen-in-cyberattack/) — BleepingComputer
- **MEDIUM** [Microsoft Issues Emergency Fixes After Massive Patch Tuesday](https://www.darkreading.com/application-security/microsoft-emergency-fixes-patch-tuesday) — Dark Reading
- **MEDIUM** [VectraRAT Can Hack Windows Enterprises for $250 per Month](https://www.darkreading.com/endpoint-security/vectrarat-hack-windows-enterprises) — Dark Reading

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

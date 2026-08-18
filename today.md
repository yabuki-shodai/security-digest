# CVE Digest Dashboard (2026-08-19)

## Overview

- Total: 30
- Critical件数: 5
- High件数: 16
- KEV件数: 0
- Frontend件数: 12
- Backend件数: 18
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-19/frontend-summary.md)
- [Backend Summary](docs/2026-08-19/backend-summary.md)

## Today TOP5

- [CVE-2026-12564](https://access.redhat.com/security/cve/CVE-2026-12564) CVE-2026-12564 / CRITICAL / backend
- [CVE-2026-52723](https://github.com/fbeta-GmbH/ePA3-Service-OpenSource/commit/197c8c7fc41675f19c7f448696a2bc63fab9db5b) CVE-2026-52723 / CRITICAL / backend
- [CVE-2026-73366](https://patchstack.com/database/wordpress/plugin/google-maps-easy/vulnerability/wordpress-easy-google-maps-plugin-1-13-0-php-object-injection-vulnerability?_s_id=cve) CVE-2026-73366 / CRITICAL / backend
- [CVE-2026-75926](https://github.com/gohugoio/hugo) CVE-2026-75926 / CRITICAL / frontend
- [CVE-2026-45118](https://github.com/mybb/mybb/releases/tag/mybb_1840) CVE-2026-45118 / CRITICAL / frontend

## Geminiによる今日の総括

## 今日のまとめ
本日掲載された脆弱性には、Webアプリケーションにおける入力検証不備（PHP Object Injection、XSS、オープンリダイレクト）、ビルドツールやワークフロー・LLMエージェントでの権限迂回および任意コード実行（RCE）、Kubernetesサービスアカウントトークンや証明書を巡る認証・資格情報漏洩などが含まれています。特に開発パイプラインや自動化ツールにおける実行権限・分離モデルの不備に注意が必要です。

## 優先して確認すべき3〜5件

1. **CVE-2026-73366**（CVSS 9.8 / CRITICAL）
   - **対象**: Easy Google Maps
   - **内容**: 未認証の攻撃者による PHP Object Injection が可能となる脆弱性。システム上で悪意のあるコードを実行される恐れがあります。
2. **CVE-2026-12564**（CVSS 9.6 / CRITICAL）
   - **対象**: AAP Controller (awx_plugins)
   - **内容**: HashiCorp Vault 認証プラグインのテスト時に、Kubernetes サービスアカウントトークンが攻撃者制御のURLへ送信される問題。Kubernetes 制御プレーンへの不正アクセスにつながるリスクがあります。
3. **CVE-2026-75926**（CVSS 9.3 / CRITICAL）
   - **対象**: Hugo
   - **内容**: TailwindCSS のデフォルト許可設定により Node.js のパーミッションモデルが迂回され、ビルド処理中にプロジェクト外のファイルシステムへアクセスされる可能性があります。
4. **CVE-2026-71539**（CVSS 8.9 / HIGH）
   - **対象**: n8n
   - **内容**: Gitクローン処理時のシンボリックリンク操作により、悪意あるリポジトリがカスタムノードとして読み込まれ、サーバー上で任意コードが実行される危険性があります。
5. **CVE-2026-75858**（CVSS 8.5 / HIGH）
   - **対象**: CodeWhale
   - **内容**: `rlm_eval` ツールの承認要件設定の誤りにより、ユーザーの承認プロンプトを経由せずにモデル由来の任意の Python コードが実行されるリスクがあります。

## 開発者向けコメント

* **開発・ビルドツールの実行権限の再確認**: Hugo や n8n、CodeWhale などのツール・ライブラリで、サブプロセスやスクリプトを実行する際の権限分離（パーミッションモデルや承認フロー）が意図通り機能しているか確認してください。
* **トークンや秘密情報の外部送信防止**: Kubernetes のサービスアカウントトークンや API キーなど、重要な認証情報を取り扱う処理において、宛先 URL やサーバー証明書（CVE-2026-52723 等）の検証が欠落していないかを徹底してください。
* **入力検証・エスケープ処理の再点検**: オープンリダイレクトからの JavaScript 注入（CVE-2026-45118）や、プロファイルフィールド・マークダウンパース時のエスケープ漏れ（CVE-2026-45116, CVE-2026-55839）など、UI 側の XSS 対策も改めて見直しが必要です。

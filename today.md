# CVE Digest Dashboard (2026-08-30)

## Overview

- Total: 15
- Critical件数: 3
- High件数: 8
- KEV件数: 0
- Frontend件数: 0
- Backend件数: 8
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-30/frontend-summary.md)
- [Backend Summary](docs/2026-08-30/backend-summary.md)

## Today TOP5

- [CVE-2026-82460](https://github.com/coderaiser/cloudcmd) CVE-2026-82460 / CRITICAL / security
- [CVE-2026-15369](https://woocommerce.com/products/custom-user-registration-fields-for-woocommerce/) CVE-2026-15369 / CRITICAL / backend
- [CVE-2026-82466](https://github.com/jeremyevans/rodauth) CVE-2026-82466 / CRITICAL / backend
- [CVE-2026-82463](https://github.com/pac4j/pac4j) CVE-2026-82463 / HIGH / security
- [CVE-2026-82472](https://github.com/documenso/documenso) CVE-2026-82472 / HIGH / security

## Geminiによる今日の総括

## 今日のまとめ
本日は、認証・認可バイパス（Rodauth, pac4j, WordPressプラグイン等）やディレクトリトラバーサル（Cloud Commander, cohttp）、未認証での権限昇格やリソース操作など、影響度の高い脆弱性（CRITICALおよびHIGH）が多数報告されています。特に認証ライブラリやWeb API、管理ツールの適切なバージョンアップと入力・パス検証の強化が求められます。

## 優先して確認すべき3〜5件
* **CVE-2026-15369 (CVSS 9.8 / CRITICAL)**: Custom User Registration Fields for WooCommerceプラグインにおける未認証からの特権昇格。チェックアウトAPIを介して任意ロールが付与される恐れがあります。
* **CVE-2026-82460 (CVSS 9.8 / CRITICAL)**: Cloud Commanderにおけるディレクトリトラバーサル。パス正規化不足により、ルートディレクトリ外のファイル読み書きや操作が可能です。
* **CVE-2026-82466 (CVSS 9.4 / CRITICAL)**: Rodauthの`webauthn_login`ルートにおける認証バイパス。ログイン済みユーザーが任意のアカウントとして認証を通過できてしまいます。
* **CVE-2026-82461 / CVE-2026-82463 (CVSS 8.6 / HIGH)**: pac4jにおけるOIDCアクセストークンの署名・issuer未検証および認可ロジック反転。権限昇格や認証バイパスに繋がります。
* **CVE-2026-82474 (CVSS 8.5 / HIGH)**: Sudoにおける`execveat`/`fexecve`呼び出し時のポリシーバイパス。許可された特定のコマンドから禁止プログラムを実行される可能性があります。

## 開発者向けコメント
* **認証・ライブラリの更新**: Rodauth（2.46.0 / 2.47.0以降）、pac4j（6.5.6以降）、Cloud Commander（19.20.2以降）など、認証フレームワークや管理ツールを速やかに最新版へアップデートしてください。
* **入力検証・パス正規化の徹底**: オープンリダイレクトやディレクトリトラバーサルを防ぐため、バックスラッシュや先頭のダブルスラッシュ（`//`）、相対パス記法に対する正規化処理とバリデーションを徹底してください。
* **未認証APIエンドポイントの再確認**: ファイルアップロード（Documenso）やタスク状態報告（KubeEdge）など、認証・認可が欠落したエンドポイントによるDoSや改ざんリスクを点検してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

大手企業を標的としたサイバー攻撃による個人情報の漏えい事案が公表されています。一方で、Webブラウザにおけるトラッキング防止を目的とした新たなプライバシー保護機能の導入が発表されました。また、AIツールの利用制限変更といったサービス運用に関する動きも見られます。

- **HIGH** [Hasbro Data Breach Exposed Employee Personal Information](https://www.securityweek.com/hasbro-data-breach-exposed-employee-personal-information/) — SecurityWeek
- **LOW** [Anthropic is cutting Claude Code's current weekly limits by 17%](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-is-cutting-claude-codes-current-weekly-limits-by-17-percent/) — BleepingComputer
- **LOW** [Brave browser adds email aliases to help users evade tracking](https://www.bleepingcomputer.com/news/security/brave-browser-adds-email-aliases-to-help-users-evade-tracking/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

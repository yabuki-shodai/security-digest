# CVE Digest Dashboard (2026-09-28)

## Overview

- Total: 30
- Critical件数: 7
- High件数: 13
- KEV件数: 2
- Frontend件数: 3
- Backend件数: 17
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-28/frontend-summary.md)
- [Backend Summary](docs/2026-09-28/backend-summary.md)

## Today TOP5

- [CVE-2026-88772](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096&articleTitle=Citrix_NetScaler_ADC_and_Citrix_NetScaler_Gateway_Security_Bulletin_for_CVE_2026_88771_CVE_2026_88772_CVE_2026_88773_CVE_2026_88774_CVE_2026_88775_CVE_2026_88776_CVE_2026_88777_and_CVE_2026_88778) CVE-2026-88772: Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability / CRITICAL / security
- [CVE-2026-88771](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) CVE-2026-88771: Citrix NetScaler Improper Input Validation Vulnerability / CRITICAL / security
- [CVE-2026-101084](https://github.com/obot-platform/obot/security/advisories/GHSA-vw82-7fv8-r6gp) CVE-2026-101084 / CRITICAL / security
- [CVE-2026-100886](https://github.com/heapframe/seetong-ts81xxd3x-rce) CVE-2026-100886 / CRITICAL / security
- [CVE-2026-88773](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096) CVE-2026-88773 / CRITICAL / security

## Geminiによる今日の総括

## 今日のまとめ
本日公開された脆弱性では、**Citrix NetScaler**における悪用確認済み（KEV掲載）のクリティカルな脆弱性や、**Obot**・**Nezha**などの管理/AIプラットフォームにおける認証回避・OAuthリダイレクト奪取・SSRFが目立ちます。さらに、**pnpm**などのパッケージマネージャや開発環境ツールにおける設定展開・パス検証不備も報告されており、インフラから開発環境まで幅広い層で迅速な確認と対処が必要です。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-88771 / CVE-2026-88772 | Citrix NetScaler ADC / Gateway**
   * **Severity:** CRITICAL (CVSS 9.5) / **KEV対象**
   * **概要:** 不適切な入力検証およびメモリバッファオーバーフローにより、未認証の攻撃者による任意コマンド実行（RCE）やDoSが可能です。既に悪用が確認されているため、最優先でアップデートを適用してください。
2. **CVE-2026-100886 | Seetong 機器 (T8108, T8116等)**
   * **Severity:** CRITICAL (CVSS 10.0)
   * **概要:** デバッグサービスにおける不適切な認証実装により、リモートから認証をバイパスされる恐れがあります。
3. **CVE-2026-101065 | Obot**
   * **Severity:** CRITICAL (CVSS 9.8)
   * **概要:** Dockerクイックスタート設定時に認証がデフォルトで無効化され、全インターフェース（0.0.0.0:8080）に開放される問題。未認証の第三者に完全な管理者権限を取得される危険があります。
4. **CVE-2026-101090 | Nezha**
   * **Severity:** CRITICAL (CVSS 9.8)
   * **概要:** OAuth2リダイレクト処理におけるHostヘッダインジェクション。攻撃者が偽装したHostヘッダによりOAuthログインリダイレクト先を誘導・奪取される可能性があります。
5. **CVE-2026-101043 | pnpm**
   * **Severity:** HIGH (CVSS 8.3)
   * **概要:** リポジトリ管理下にある `pnpm-workspace.yaml` 内のプロキシ設定で環境変数プレースホルダーが不用意に展開される問題。悪意あるリポジトリを読み込んだ際に意図しないリクエスト送信が発生するリスクがあります。

---

## 開発者向けコメント
* **ビルド・開発ツールの安全確保:** `pnpm` や `Fleet` などの開発・運用ツールにおいて、設定ファイルの自動展開やパス連結時の検証不足による脆弱性が報告されています。信頼できないリポジトリや設定ファイルを扱う際はツールを最新化し、ローカル環境やCI/CDパイプラインを保護してください。
* **OAuth実装とHostヘッダの検証:** HTTP Hostヘッダを動的にリダイレクトURIへ反映する実装や、動的OAuthクライアント登録におけるURI検証不足は、認証情報奪取（アカウントハイジャック）に直結します。厳格なホワイトリスト検証や設定値のフォールバックを徹底してください。
* **デフォルト設定とネットワーク露出の警戒:** 開発用コンテナやクイックスタート手順で「認証なし＋全インターフェース公開（0.0.0.0）」となっている構成がないか、本番・検証環境のデプロイ設定を再確認しましょう。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近24時間では、Citrix NetScalerのゼロデイ脆弱性やMicrosoft SharePointの脆弱性が実際の攻撃で悪用されていることが確認されました。また、Cloudflareにおいて顧客データが露出するクロステナントの欠陥が修正されるなど、重大な問題への対処が進んでいます。あわせて、OpenAIやAnthropicによるAI関連の新たな機能拡張やエコシステムの展開も報じられています。

- **HIGH** [Citrix confirms two NetScaler RCE zero-days exploited in attacks](https://www.bleepingcomputer.com/news/security/citrix-admins-warned-to-shut-down-netscalers-over-2-exploited-zero-days/) — BleepingComputer
- **HIGH** [Cloudflare fixes Containers cross-tenant flaw exposing customer data](https://www.bleepingcomputer.com/news/security/cloudflare-fixes-containers-cross-tenant-flaw-exposing-customer-data/) — BleepingComputer
- **HIGH** [Microsoft SharePoint Flaw CVE-2026-65660 Now Exploited in Attacks](https://www.securityweek.com/microsoft-sharepoint-flaw-cve-2026-65660-now-exploited-in-attacks/) — SecurityWeek
- **LOW** [OpenAI is preparing “o,” an always-on ChatGPT assistant that could handle email](https://www.bleepingcomputer.com/news/artificial-intelligence/openai-is-preparing-o-an-always-on-chatgpt-assistant-that-could-handle-email/) — BleepingComputer
- **LOW** [Anthropic turns Claude into an AI marketplace with 2,000+ plugins and connectors](https://www.bleepingcomputer.com/news/artificial-intelligence/anthropic-turns-claude-into-an-ai-marketplace-with-2-000-plus-plugins-and-connectors/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

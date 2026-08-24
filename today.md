# CVE Digest Dashboard (2026-08-25)

## Overview

- Total: 30
- Critical件数: 4
- High件数: 24
- KEV件数: 0
- Frontend件数: 5
- Backend件数: 25
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-08-25/frontend-summary.md)
- [Backend Summary](docs/2026-08-25/backend-summary.md)

## Today TOP5

- [CVE-2026-71914](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/) CVE-2026-71914 / CRITICAL / backend
- [CVE-2026-71921](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/) CVE-2026-71921 / CRITICAL / backend
- [CVE-2026-71933](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/) CVE-2026-71933 / CRITICAL / backend
- [CVE-2026-76835](https://github.com/oauth2-proxy/oauth2-proxy) CVE-2026-76835 / CRITICAL / backend
- [CVE-2026-55468](https://github.com/wagtail/wagtail/commit/5608cfb714a130412f862beab53c78de02b79975) CVE-2026-55468 / MEDIUM / backend

## Geminiによる今日の総括

## 今日のまとめ
本日の脆弱性一覧では、**DrayTek製ネットワーク機器（VigorAP/VigorSwitch）における事前認証なしの任意コマンド実行（CRITICAL）を含む多数の脆弱性**が過半数を占めています。
開発・インフラ運用者向けとしては、**OAuth2 Proxyにおける認証バイパス**、**JavaScriptライブラリ（libp2p）でのメモリ枯渇DoS**、**Jinja等のHTMLエスケープをすり抜けるJavaScriptコンテキストでのXSS**、**APIアクセス制御不備によるコンテンツ漏洩**などが報告されており、認証境界の設定とコンテキストに応じた適切な出力処理が求められます。

---

## 優先して確認すべき3〜5件
- **CVE-2026-76835 (CRITICAL / CVSS 9.3)**：**OAuth2 Proxyにおける認証バイパス**
  - **概要**: デフォルトのリバースプロキシ構成において、クライアントが送信した `X-Forwarded-Uri` ヘッダーを優先して評価してしまうため、認証不要パスの判定（`skip_auth`）を悪用して認証を迂回される可能性があります。
- **CVE-2026-71914 / CVE-2026-71921 (CRITICAL / CVSS 9.8)**：**DrayTek VigorAP / VigorSwitch の事前認証なしRCE**
  - **概要**: UDPメッセージ（`dray_apm`）や `setget.cgi` の入力検証不足により、認証なしの遠隔攻撃者によって root 権限で任意のOSコマンドを実行されるリスクがあります。
- **CVE-2026-77384 (HIGH / CVSS 7.5)**：**libp2p (JavaScript) における DoS**
  - **概要**: 予約更新処理（RESERVEリクエスト）時に abort リスナーが無制限に登録・増加する実装不備があり、リバースプロキシ/リレイサーバーのメモリが圧迫されて DoS 状態に陥ります（v4.2.9で修正）。
- **CVE-2026-78391 (HIGH / CVSS 8.8)**：**RansomLook における Stored XSS**
  - **概要**: 外部フィード由来のデータをインライン JavaScript の `onclick` ハンドラへ埋め込む際、Jinja の HTML 自動エスケープのみに依存していたため XSS が発生。コンテキストに応じたエンコード不足の典型例です。

---

## 開発者向けコメント
- **HTMLエスケープとJSコンテキストの混同に注意**
  Jinjaなどのテンプレートエンジンの「HTML自動エスケープ」は、`<script>` タブ内や `onclick` などのインラインJavaScript属性内では効果が不十分です（CVE-2026-78391, CVE-2026-71503）。JavaScriptコンテキストに動的データを埋め込む際は、専用のJSエンコーダーを使用するか、`data-*` 属性経由でDOM取得する構造へ改修してください。
- **リバースプロキシ構成と信頼するヘッダーの再確認**
  プロキシ配下で動くアプリケーションにおいて、`X-Forwarded-Uri` や `Set-Cookie`（CRLF関連）などのヘッダー処理は認証回避やインジェクションの標的になりやすい部分です（CVE-2026-76835, CVE-2026-39915）。ヘッダーの信頼境界が正しく設定されているか構成を見直しましょう。
- **イベントリスナーとリソースの解放漏れ**
  Node.js / JavaScript 環境でのリクエスト処理において、ループやリクエスト受信ごとに `addEventListener` や `on` を登録し直すと、メモリリークおよび DoS の原因になります（CVE-2026-77384）。再利用時は古いリスナーの破棄（`removeEventListener` や `AbortController` の適切な取り扱い）を徹底してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

CISAが緊急対処を求めたZimbraの脆弱性やWordPressプラグインの認証バイパスなど、実際に悪用されている脆弱性への迅速な対応が強く求められています。未修正のルーターにおけるNATバイパス問題や、ランサムウェア前兆となる高度なマルウェアの登場など、新たなセキュリティ上の脅威も報告されています。さらに、セキュリティ企業を標的にしたソーシャルエンジニアリング攻撃やマルウェアの検知回避手法の巧妙化にも警戒が必要です。

- **HIGH** [Exploited Zimbra Flaw Highlights Shrinking Window to Patch](https://www.darkreading.com/vulnerabilities-threats/zimbra-flaw-exploitation-shrinking-window-patch) — Dark Reading
- **HIGH** [Unpatched Calix flaw lets hackers bypass NAT to expose internal devices](https://www.bleepingcomputer.com/news/security/unpatched-calix-flaw-lets-hackers-bypass-nat-to-expose-internal-devices/) — BleepingComputer
- **HIGH** [Hackers target WordPress sites in miniOrange auth bypass attacks](https://www.bleepingcomputer.com/news/security/hackers-target-wordpress-sites-in-miniorange-auth-bypass-attacks/) — BleepingComputer
- **HIGH** [Tricky 'SynkLoader' Multitool May Herald Ransomware](https://www.darkreading.com/threat-intelligence/tricky-synkloader-multitool-ransomware) — Dark Reading
- **MEDIUM** [Foul Language: WordlistLoader Disguises Malware as Ordinary Text](https://www.darkreading.com/data-privacy/wordlistloader-disguises-malware-ordinary-text) — Dark Reading

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

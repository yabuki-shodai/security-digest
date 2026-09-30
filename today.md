# CVE Digest Dashboard (2026-09-30)

## Overview

- Total: 30
- Critical件数: 11
- High件数: 17
- KEV件数: 0
- Frontend件数: 9
- Backend件数: 21
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-30/frontend-summary.md)
- [Backend Summary](docs/2026-09-30/backend-summary.md)

## Today TOP5

- [CVE-2026-95311](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0856730748.html) CVE-2026-95311 / CRITICAL / backend
- [CVE-2026-95277](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0856730748.html) CVE-2026-95277 / CRITICAL / backend
- [CVE-2026-95281](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0856730748.html) CVE-2026-95281 / CRITICAL / backend
- [CVE-2026-95283](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0856730748.html) CVE-2026-95283 / CRITICAL / backend
- [CVE-2026-95299](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_0856730748.html) CVE-2026-95299 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ

本日公開された脆弱性では、**Chromiumエンジンにおける多数の深刻なメモリ破壊（任意コード実行リスク）**と、**Electronフレームワークにおけるサンドボックス回避・特権昇格の不備**が目立ちます。また、OpenSSLやlibsoupといったネットワーク/TLS/WebSocket基盤ライブラリの脆弱性や、プロキシヘッダー・シンボリックリンク検証の不備による入力検証系の問題も含まれています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-95311 ほか（Chromium関連の任意コード実行群）** / CVSS 9.6 (CRITICAL)
   - **概要:** Google Chrome/ChromiumにおけるUAF（Use-After-Free）やバッファオーバーフローなどの脆弱性。クラフトされたHTMLページにより、サンドボックス外で任意コードが実行される恐れがあります。
2. **CVE-2026-102676（Electron）** / CVSS 8.3 (HIGH)
   - **概要:** Node.js統合が無効な親環境であっても、`<webview>` 内のWeb Workerで `nodeIntegrationInWorker` が有効化できてしまい、意図しない高い権限を奪取される恐れがあります。
3. **CVE-2026-102242（Google MCP Toolbox for Databases）** / CVSS 8.6 (HIGH)
   - **概要:** `allowedLocalRoots` のパス検証時にシンボリックリンクが正規化されない不備（CWE-59/CWE-22）。攻撃者が許可ディレクトリ外のローカルファイルにアクセス・上書きできる可能性があります。
4. **CVE-2026-72897（OpenSSL）** / CVSS 7.5 (HIGH)
   - **概要:** ハンドシェイク途中に `SSL_set_SSL_CTX()` を呼び出してコンテキストを切り替えるTLSサーバーにて、境界外メモリ読み取り（OOB read）が発生する問題です。
5. **CVE-2026-102559 / CVE-2026-102560（libsoup）** / CVSS 8.6 (HIGH)
   - **概要:** 大容量のWebSocketフレーム送信処理において、サイズ計算の切り捨て・ラップアラウンドが発生し、ヒープバッファオーバーフローを引き起こす脆弱性です。

---

## 開発者向けコメント

- **デスクトップアプリ（Electron）開発者:** Electronのパッチバージョンへの更新を速やかに行ってください。特に `<webview>` や `preload` 処理、サンドボックス境界の構成に依存しているアプリは挙動の検証が必要です。
- **ブラウザ・組み込みWebプラットフォーム開発者:** Chromiumエンジンの更新（バージョン154.0.8037.57以降への追従）を優先してください。
- **バックエンド・基盤開発者:** TLS接続切り替えを行うサーバー（OpenSSL利用）やWebSocket通信（libsoup利用）を行っているシステムはライブラリをアップデートしてください。また、ファイルパス検証におけるシンボリックリンクの事前解決や、`X-Forwarded-Host` 等のHTTPヘッダーの無検証な信頼を避ける実装を再確認してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

Apple製品におけるゼロデイ脆弱性の悪用やカスタムChatGPTを悪用したマルウェア感染攻撃など、実際の攻撃事例が報告されています。また、OpenAIエージェントによる政府サイト侵入やAI開発ツールのコード実行脆弱性など、AI技術に関するセキュリティ上の問題も顕著です。その他、サイバー犯罪グループの捜査状況やソフトウェアの機能更新などの動向が含まれています。

- **HIGH** [Apple Zero-Day Vulnerability Weaponized in Targeted Attacks](https://www.darkreading.com/cyberattacks-data-breaches/apple-zero-day-vulnerability-weaponized-targeted-attacks) — Dark Reading
- **HIGH** [Custom ChatGPTs push ClickFix attacks to deploy RAT malware](https://www.bleepingcomputer.com/news/security/custom-chatgpts-push-clickfix-attacks-to-deploy-rat-malware/) — BleepingComputer
- **HIGH** [OpenAI apologizes for agents breaching Australian government websites without authorization](https://therecord.media/openai-apologizes-australia-medicare-breach) — The Record
- **MEDIUM** [Unsloth Studio Flaw Turns Routine Model Inspection Into Code Execution](https://www.darkreading.com/application-security/unsloth-studio-flaw-model-inspection-code-execution) — Dark Reading
- **MEDIUM** [FBI tells ShinyHunters members to turn themselves in after recent arrest](https://www.bleepingcomputer.com/news/security/fbi-tells-shinyhunters-members-to-turn-themselves-in-after-recent-arrest/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

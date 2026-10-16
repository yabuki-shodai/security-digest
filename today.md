# CVE Digest Dashboard (2026-10-16)

## Overview

- Total: 30
- Critical件数: 0
- High件数: 10
- KEV件数: 0
- Frontend件数: 16
- Backend件数: 14
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-16/frontend-summary.md)
- [Backend Summary](docs/2026-10-16/backend-summary.md)

## Today TOP5

- [CVE-2026-100409](https://github.com/opennextjs/opennextjs-aws/pull/1199) CVE-2026-100409 / HIGH / frontend
- [CVE-2026-104827](https://github.com/reactphp/http/commit/2558622d0b76227c60c61eac8a61572cb6638e8c) CVE-2026-104827 / HIGH / frontend
- [CVE-2026-77470](https://github.com/LycheeOrg/Lychee/commit/24e6e11f1da131ed20b192d7d7b7ca9084451a2f) CVE-2026-77470 / HIGH / backend
- [CVE-2026-58391](https://github.com/opnsense/core/commit/5e6313f50546474031805039e209830b63b2b0e4) CVE-2026-58391 / MEDIUM / backend
- [CVE-2026-100350](https://github.com/getkin/kin-openapi/commit/d090e36b2f1c42c898ba2a687a8f6e25f5ca727f) CVE-2026-100350 / MEDIUM / backend

## Geminiによる今日の総括

## 今日のまとめ

本日は、Go言語向けOpenAPI処理ライブラリ（`kin-openapi`）における多数のDoSおよび認可バイパス脆弱性をはじめ、フロントエンド・Webフレームワーク周辺で高深刻度な脆弱性が相次いで報告されました。特に、URLパス解釈の不一致によるアクセス制御の迂回や、決済・レスポンス処理における入力検証不備による影響に注意が必要です。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-77470 (CVSS 8.3 - HIGH / Lychee)**
   - **概要**: 決済処理APIにおいて、追加パラメータの結合時にサーバー側の計算済みパラメータ（金額やリターンURL等）が上書き可能なロジック欠陥。
   - **影響**: 未認証の購入者により決済金額の改ざんや不正なリダイレクトが行われるリスク。

2. **CVE-2026-100409 (CVSS 7.5 - HIGH / OpenNext Cloudflare)**
   - **概要**: パーセントエンコードされたパスの扱いについて、アクセス制御ミドルウェアとキャッシュキー生成処理で解釈の不一致が発生。
   - **影響**: 認可ミドルウェアを迂回し、未認証の攻撃者が保護されたルートのキャッシュ情報を取得可能。

3. **CVE-2026-100351 (CVSS 7.4 - HIGH / kin-openapi)**
   - **概要**: `ValidationHandler` とルーター（`gorilla/mux`）間でエンコードされたパスのデコード処理タイミングが異なり、ルートのルーティング不一致が発生。
   - **影響**: 保護されたパラメーター付きルートへのリクエスト制限が迂回される可能性。

4. **CVE-2026-104827 (CVSS 7.5 - HIGH / react/http)**
   - **概要**: クライアントからのレスポンスヘッダー受信用バッファにサイズ上限が設定されていない。
   - **影響**: 悪意のあるサーバーからの無限ストリーミングによりメモリが枯渇し、アプリケーションがDoS状態に陥る。

5. **CVE-2026-109841 (CVSS 5.9 - MEDIUM / undici)**
   - **概要**: Node.js用HTTPクライアントにおいて、SRI（サブリソース統合）ハッシュのアルゴリズム名の大文字・小文字チェック不備。
   - **影響**: 大文字を含む有効なSRIトークンが未認識扱いとなり、結果として改ざん検証（SRIチェック）がスキップされる。

---

## 開発者向けコメント

- **APIライブラリ・ミドルウェアのバージョン確認**: `kin-openapi` を利用中のGoプロジェクトは、DoSや認可バイパスが複数報告されているため、速やかに修正版（0.149.0以上）へ更新してください。
- **URL解釈・キャッシュ処理の整合性チェック**: フロントエンドやエッジサーバー（Next.js/Cloudflareなど）で認証・認可とキャッシュ参照を行っている場合、パスのエンコード・正規化順序に起因するバイパスがないか構成を見直しましょう。
- **外部リクエスト処理のリソース・検証強化**: HTTPクライアント（`react/http` や `undici`）を使用している場合は、最新版へ更新してバッファ上限の適用とセキュリティ検証機構（SRI等）の正常動作を確保してください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近24時間では、Nextcloud連携アプリのRCE脆弱性の悪用やArch Linuxリポジトリへの悪質なパッケージ投入など、実効性のある攻撃手法が報告されています。また、ターゲット広告を介したゼロクリック・スパイウェアや34カ国に及ぶ機器乗っ取り、政府請負業者への攻撃による裁判所業務の停止など、影響範囲の広い深刻な被害が発生しています。一方で、OSレベルでのAI防御機能の追加や詐欺対策データベースの公開など、対策側の動きも見られます。

- **HIGH** [Federal bankruptcy courts dealing with outages after contractor cyberattack](https://therecord.media/federal-bankruptcy-courts-dealing-with-cyberattack-outage) — The Record
- **HIGH** [Hackers exploit Collabora RCE flaw to backdoor Nextcloud servers](https://www.bleepingcomputer.com/news/security/hackers-exploit-collabora-rce-flaw-to-backdoor-nextcloud-servers/) — BleepingComputer
- **HIGH** [Zero-click spyware infecting devices through online ads, researchers say](https://therecord.media/spyware-citizen-lab-advertising) — The Record
- **HIGH** [Hackers hijack D-Link, Ubiquiti devices to resell your stolen bandwidth](https://www.bleepingcomputer.com/news/security/hackers-hijack-d-link-ubiquiti-devices-to-resell-your-stolen-bandwidth/) — BleepingComputer
- **HIGH** [Fake Arch Linux packages push malware with root privileges](https://www.bleepingcomputer.com/news/security/fake-arch-linux-packages-push-malware-with-root-privileges/) — BleepingComputer

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

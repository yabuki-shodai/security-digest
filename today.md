# CVE Digest Dashboard (2026-11-05)

## Overview

- Total: 30
- Critical件数: 3
- High件数: 9
- KEV件数: 0
- Frontend件数: 16
- Backend件数: 14
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-11-05/frontend-summary.md)
- [Backend Summary](docs/2026-11-05/backend-summary.md)

## Today TOP5

- [CVE-2026-115770](https://github.com/pocket-id/pocket-id/commit/43aaccd5bfacb76283b11ce039fb3f0716196fcb) CVE-2026-115770 / CRITICAL / backend
- [CVE-2026-97693](https://github.com/xerrors/Yuxi/commit/b5b5713e6e639dd4ed2ebce41579a3c458347663) CVE-2026-97693 / CRITICAL / backend
- [CVE-2026-107846](https://github.com/bitcoinjs/bitcoinjs-lib/commit/009f165edfbf925cad8964b2dce478d18dd19449) CVE-2026-107846 / CRITICAL / frontend
- [CVE-2026-122224](https://github.com/catborise/webvirtcloud/commit/1227674d8f5a5230e5c654267773aca4ebc5c717) CVE-2026-122224 / HIGH / backend
- [CVE-2026-63655](https://github.com/tsparticles/tsparticles/commit/25fb70e7f527a91568adaef576570289083f243b) CVE-2026-63655 / HIGH / frontend

## Geminiによる今日の総括

## 今日のまとめ
本日公開されたCVEは、Webアプリケーションから開発環境ツール、認証・プロキシインフラ、暗号化ライブラリまで多岐にわたります。特に高スコアの脆弱性として、**コンテナ実行環境の分離不備による他テナント攻撃（Yuxi）**、**メール検証トークンの不備による認証バイパス（Pocket ID）**、**暗号検証ロジックの不備（bitcoinjs-lib）**、**プロキシ接続プール再利用によるなりすまし（Traefik）**などが報告されています。また、開発者が日常的に使用する `nvm` に複数の脆弱性が発見された点にも注意が必要です。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-97693 (Yuxi | CVSS 9.9 CRITICAL)**
   - **内容**: Dockerサンドボックスの不十分な隔離により、悪意あるユーザーが他テナントのサンドボックスAPIやファイル、シークレットにアクセスし、コマンド実行が可能な状態になる。
   - **対策**: バージョン 0.7.1 以降へアップデートし、サンドボックス間のアクセス制限を強化する。

2. **CVE-2026-115770 (Pocket ID | CVSS 9.6 CRITICAL)**
   - **内容**: メールアドレス変更時に既存の検証トークンが無効化されないため、攻撃者が自身で取得したトークンを使って変更後の任意アドレスを検証済みに偽装できる。
   - **対策**: バージョン 2.12.0 以降へ更新し、アドレス変更時にトークンを無効化する。

3. **CVE-2026-107846 (bitcoinjs-lib | CVSS 9.3 CRITICAL)**
   - **内容**: `fastMerkleRoot` で奇数ノードのパディング時に隣接重複ハッシュを検出できず、不正なMerkle rootを正当と判定してしまう。
   - **対策**: 修正済みバージョン（5.2.1 / 6.1.8 / 7.0.2 以降）へ修正依存関係を更新する。

4. **CVE-2026-121966 (Traefik | CVSS 8.7 HIGH)**
   - **内容**: ForwardAuth のサブリクエストが全クライアント共通の接続プールを使用するため、未認証の攻撃者が他ユーザーの認証済み接続（NTLM/Negotiate）を再利用してバックエンドにアクセス可能。
   - **対策**: Traefik 2.11.60 または 3.7.16 以降へアップグレードする。

5. **CVE-2026-121747 (nvm | CVSS 6.7 MEDIUM)**
   - **内容**: `.nvmrc` がシンボリックリンクであるか検証しないため、悪意あるリポジトリを `nvm use` 等で読み込むと任意ファイルの内容がエラーメッセージ経由で出力・漏洩する。
   - **対策**: nvm 0.40.8 より新しい修正版への更新、または信頼できないリポジトリでの `.nvmrc` 存在確認。

---

## 開発者向けコメント

* **認証・状態管理ロジックの再検証**: 接続プールのセッション再利用（Traefik）や、メール変更時のトークン有効期限管理（Pocket ID）、クライアント側JSによるブルートフォース制限（ProSoft）など、サーバーサイドでの適切な状態分離と検証を徹底してください。
* **リポジトリ経由のローカル開発環境攻撃に注意**: `nvm` の脆弱性に代表されるように、悪意ある設定ファイル（`.nvmrc` など）を含むリポジトリをチェックアウトしてコマンドを実行するだけで情報漏洩や意図しない挙動が引き起こされるリスクがあります。開発ツールの最新化を推奨します。
* **デスクトップ・コンテナ基盤の境界防御**: Tauriアプリケーション（Readest）やDockerサンドボックス（Yuxi）のように、フロントエンドや隔離環境からバックエンド・ホスト側へのファイルパス指定・APIアクセスに対しては、適切なスコープ制限と入力検証を必ず設けてください。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

直近24時間では、航空会社や金融機関、医療関連施設、ゲームランチャーなどを標的としたサプライチェーン攻撃や第三者プロバイダ経由の被害が目立っています。また、ネットワーク機器のゼロデイ脆弱性の悪用やRailsの深刻な脆弱性、130万台規模のボットネット解体など、基盤やインフラに関わる重大な事象も報告されています。認証情報の窃盗や巨額の不正送金など実害を伴うインシデントが多く確認されており、厳重な警戒が必要です。

- **HIGH** [Critical Rails Bug Threatens to Derail Vulnerable Servers](https://www.darkreading.com/application-security/critical-rails-bug-derail-vulnerable-servers) — Dark Reading
- **HIGH** [More Asian airlines announce data breaches after attack on Spanish IT provider Amadeus](https://therecord.media/asian-airlines-announce-data-breach-it-provider-incident) — The Record
- **HIGH** [Zyxel fixes zero-day exploited to hack nearly 1,000 network switches](https://www.bleepingcomputer.com/news/security/zyxel-fixes-zero-day-exploited-to-hack-nearly-1-000-network-switches/) — BleepingComputer
- **HIGH** [DreamHost confirms data breach exposed FTP logins and webmail sessions](https://www.bleepingcomputer.com/news/security/dreamhost-confirms-data-breach-exposed-ftp-logins-and-webmail-sessions/) — BleepingComputer
- **HIGH** [French bank confirms cyber heist, hackers suspected to have stolen an estimated $133 million](https://therecord.media/french-bank-confirms-cyber-heist) — The Record

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

# Frontend CVE Summary (2026-09-28)

## Overview

- 取得日時: 2026-09-28 09:37:04 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 3
- Critical: 0
- High: 2
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-101043](https://github.com/pnpm/pnpm/security/advisories/GHSA-vx52-2968-3vc6)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-101043
- 関連キーワード: npm, pnpm
- 影響製品: -
- 公開日: 2026-09-28 03:16:29 JST
- 更新日: 2026-09-28 03:16:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pnpmの特定のバージョンにおいて、pnpm-workspace.yamlで定義されたプロキシ設定内の環境変数プレースホルダー（${VAR}）が意図せず展開される脆弱性。
- 影響: 悪意あるリポジトリをクローンしてpnpmコマンドを実行した場合、NPM_TOKENなどの環境変数がプロキシのホスト名等に展開され、攻撃者のサーバーへ機密情報が漏洩する可能性があります。
- 推奨対応: pnpmを修正済みバージョン（11.11.0以降、または10.34.5以降）に更新してください。

#### References
- https://github.com/pnpm/pnpm/security/advisories/GHSA-vx52-2968-3vc6
- https://www.vulncheck.com/advisories/pnpm-11.0.0-before-11.11.0-environment-variable-exfiltration-via-proxy-settings

### [CVE-2026-101044](https://github.com/pnpm/pnpm/security/advisories/GHSA-2rx9-3g3h-c2jv)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-101044
- 関連キーワード: npm, pnpm
- 影響製品: -
- 公開日: 2026-09-28 03:16:30 JST
- 更新日: 2026-09-28 03:16:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pnpmに含まれるRust製コンポーネント「pacquet」において、ロックファイル内のエイリアス・名前パスに対するパス検証が不十分な脆弱性。
- 影響: 悪意のあるロックファイルを用いてインストールを実行すると、パストラバーサル（../../等）によりプロジェクトやnode_modulesの範囲外にディレクトリやシンボリックリンクが作成される可能性があります。
- 推奨対応: pnpmをpacquetの修正が含まれる12.0.0-alpha.5以降に更新してください。

#### References
- https://github.com/pnpm/pnpm/security/advisories/GHSA-2rx9-3g3h-c2jv
- https://www.vulncheck.com/advisories/pacquet-before-12.0.0-alpha.5-path-traversal-via-lockfile-alias

### [CVE-2026-101061](https://github.com/universal-tool-calling-protocol/python-utcp/security/advisories/GHSA-ppx3-28rw-8fpf)

> **Frontend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-101061
- 関連キーワード: graphql, gin
- 影響製品: -
- 公開日: 2026-09-28 03:16:32 JST
- 更新日: 2026-09-28 03:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: utcp-gqlおよびutcp-websocketにおけるSSRF（Server-Side Request Forgery）の脆弱性（CVE-2026-44661の不完全な修正に起因）。
- 影響: 攻撃者が悪意のあるツールURLを送信することで内部サービスやクラウドメタデータエンドポイントへの接続を強制され、APIキーやOAuthトークンが外部へ漏洩する可能性があります。
- 推奨対応: utcp-gqlおよびutcp-websocketをバージョン1.1.1以降に更新してください。

#### References
- https://github.com/universal-tool-calling-protocol/python-utcp/security/advisories/GHSA-ppx3-28rw-8fpf
- https://www.vulncheck.com/advisories/utcp-gql-and-utcp-websocket-before-1.1.1-ssrf-via-url-validation-bypass

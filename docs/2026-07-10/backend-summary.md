# Backend CVE Summary (2026-07-10)

## Overview

- 取得日時: 2026-07-10 09:44:55 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 2
- Critical: 1
- High: 1
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-15317](https://github.com/sipeed/picoclaw/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-15317
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-10 09:16:33 JST
- 更新日: 2026-07-10 09:16:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Sipeed PicoClaw 0.2.9以前のWebFetchTool.Execute関数にサーバーサイドリクエスト偽造（SSRF）の脆弱性が存在します。  
- 影響: リモートから悪意あるリクエストを送信され、内部ネットワークへの不正アクセスや情報漏洩のリスクがあります。  
- 推奨対応: 最新バージョンへのアップデートや、外部からの入力を適切に検証・制限する対策を検討してください。

#### References
- https://github.com/sipeed/picoclaw/
- https://github.com/sipeed/picoclaw/issues/3078
- https://vuldb.com/cve/CVE-2026-15317
- https://vuldb.com/submit/852877
- https://vuldb.com/vuln/377257

### [CVE-2026-54769](https://github.com/langroid/langroid/security/advisories/GHSA-q9p7-wqxg-mrhc)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-54769
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-10 09:16:33 JST
- 更新日: 2026-07-10 09:16:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Langroidの0.65.2未満のバージョンにおいて、`TableChatAgent`と`VectorStore`の機能で不完全なサンドボックス処理によりリモートコード実行（RCE）が可能な脆弱性が存在します。  
- 影響: 攻撃者は認証なしに任意のコードを実行でき、ホストシステムの完全な制御を奪われる恐れがあります。  
- 推奨対応: 速やかにLangroidをバージョン0.65.2以降にアップデートし、外部からの入力を安全に処理する対策を講じてください。

#### References
- https://github.com/langroid/langroid/security/advisories/GHSA-q9p7-wqxg-mrhc

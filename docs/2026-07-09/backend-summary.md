# Backend CVE Summary (2026-07-09)

## Overview

- 取得日時: 2026-07-09 08:20:57 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 3
- Critical: 0
- High: 1
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-45045](https://github.com/gofiber/fiber/commit/1403cc8292da3220e9316960b4030cc722a0f396)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-45045
- 関連キーワード: go, gin, fiber, express
- 影響製品: -
- 公開日: 2026-07-09 05:16:50 JST
- 更新日: 2026-07-09 05:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: FiberフレームワークのBalancerForwardプロキシヘルパーがX-Real-IPヘッダーの追加処理に誤りがあり、攻撃者が任意のIPを上流サーバーに送信可能です。  
- 影響: ロギングやレート制限、アクセス制御に誤ったIP情報が利用されるリスクがあります。  
- 推奨対応: Fiberをバージョン3.3.0または2.52.14以降にアップデートしてください。

#### References
- https://github.com/gofiber/fiber/commit/1403cc8292da3220e9316960b4030cc722a0f396
- https://github.com/gofiber/fiber/commit/33c9501288ab47a429c8b5e701493f0c3c0af37d
- https://github.com/gofiber/fiber/pull/4260
- https://github.com/gofiber/fiber/pull/4495
- https://github.com/gofiber/fiber/releases/tag/v2.52.14

### [CVE-2026-44332](https://github.com/gofiber/fiber/commit/c7ac00edd19f9669b1aebbec6e229658baaa059e)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-44332
- 関連キーワード: go, fiber, express
- 影響製品: -
- 公開日: 2026-07-09 05:16:49 JST
- 更新日: 2026-07-09 05:16:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: FiberフレームワークのBasicAuthミドルウェアで、存在しないユーザー名に対してパスワードハッシュ比較をスキップする短絡評価により、リモートからのユーザー名列挙が可能になる問題が報告されています。  
- 影響: 攻撃者が応答時間の差異を利用して有効なユーザー名を特定できる可能性があります。  
- 推奨対応: バージョン3.3.0以降にアップデートし、修正されたAuthorizer関数を使用してください。

#### References
- https://github.com/gofiber/fiber/commit/c7ac00edd19f9669b1aebbec6e229658baaa059e
- https://github.com/gofiber/fiber/pull/4245
- https://github.com/gofiber/fiber/releases/tag/v3.3.0
- https://github.com/gofiber/fiber/security/advisories/GHSA-g5vh-55hw-rxm8

### [CVE-2026-59803](https://github.com/smallnest/rpcx/commit/047aec18efa7d037105e2b72c36dd2ae05e1acc6)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-59803
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-09 05:16:55 JST
- 更新日: 2026-07-09 05:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: rpcx 1.9.3以前のバージョンにおいて、認証前にgzip圧縮されたメッセージの解凍処理で、展開後のサイズ制限がなく大量のメモリ消費を引き起こすDoS脆弱性が存在します。  
- 影響: 攻撃者が小さな圧縮メッセージを送信することで、サービスのメモリ枯渇や停止を引き起こす可能性があります。  
- 推奨対応: 最新の修正コミット（047aec1）を適用し、脆弱なバージョンの使用を中止してください。

#### References
- https://github.com/smallnest/rpcx/commit/047aec18efa7d037105e2b72c36dd2ae05e1acc6
- https://github.com/smallnest/rpcx/issues/942
- https://github.com/smallnest/rpcx/pull/943
- https://www.vulncheck.com/advisories/rpcx-denial-of-service-via-gzip-decompression-bomb-in-wire-protocol

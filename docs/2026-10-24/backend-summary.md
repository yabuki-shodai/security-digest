# Backend CVE Summary (2026-10-24)

## Overview

- 取得日時: 2026-10-24 09:34:25 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 21
- Critical: 2
- High: 12
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-46652](https://github.com/intranda/goobi-viewer-core/commit/5281245708447ae3419cb42492fbb8af731a2ce5)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-46652
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-24 00:17:31 JST
- 更新日: 2026-10-24 01:28:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The Goobi viewer is a web application that allows digitised material to be displayed in a web browser. From version 24.03 to before version 26.05, ExternalFilesDownloader.getFilename() extracts the destination filename from a server-supplied Content-Disposition response header and passes it directly to Path.resolve() w...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/intranda/goobi-viewer-core/commit/5281245708447ae3419cb42492fbb8af731a2ce5
- https://github.com/intranda/goobi-viewer-core/releases/tag/v26.05
- https://github.com/intranda/goobi-viewer-core/security/advisories/GHSA-r386-2frm-w3v6

### [CVE-2026-46651](https://github.com/intranda/goobi-viewer-core/commit/5281245708447ae3419cb42492fbb8af731a2ce5)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-46651
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-24 00:17:31 JST
- 更新日: 2026-10-24 01:28:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Goobi viewer の WebSocket エンドポイント (/tasks/download/monitor.socket) において、未認証のユーザーからのダウンロードリクエストを受け付けてしまう問題。
- 影響: 未認証の第三者により、不正なダウンロードタスクの要求や操作が行われる可能性があります。
- 推奨対応: Goobi viewer をバージョン 26.05 以降に更新してください。

#### References
- https://github.com/intranda/goobi-viewer-core/commit/5281245708447ae3419cb42492fbb8af731a2ce5
- https://github.com/intranda/goobi-viewer-core/commit/b8943ee963e2aa1131da2212eaf85c5a2d90214f
- https://github.com/intranda/goobi-viewer-core/releases/tag/v26.05
- https://github.com/intranda/goobi-viewer-core/security/advisories/GHSA-79jg-3m2m-jgc8

### [CVE-2026-79979](https://github.com/zephyrproject-rtos/zephyr/commit/d732e9f808f16911d06769b3f756246f3528669f)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-79979
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-24 05:17:27 JST
- 更新日: 2026-10-24 05:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: arm64 MMU バックエンドの TLB 無効化処理において、カーネル空間用の ASID 0 およびグローバルエントリのみが無効化され、メモリドメイン固有の ASID や非グローバルページが処理されない問題。
- 影響: 古い変換キャッシュ（TLB）が残存し、メモリ分離の破綻や不正なメモリアクセスが発生する可能性があります。
- 推奨対応: 修正パッチの適用またはカーネル/ファームウェアの最新版への更新を検討してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/d732e9f808f16911d06769b3f756246f3528669f
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-6pqm-hfxf-48qv

### [CVE-2026-115478](https://github.com/The-40-Thieves/obsidian-tc/blob/v1.31.4/CHANGELOG.md)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-115478
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-24 00:17:30 JST
- 更新日: 2026-10-24 00:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: obsidian-tc のエンティティ操作ツールにおいて、SQLite からノートを再生成する際に所有権検証やライフサイクル失敗時の整合性保護が不十分な問題。
- 影響: 既存のノートや他エンティティのファイル内容が上書きされたり、データ不整合が発生する可能性があります。
- 推奨対応: obsidian-tc を修正された最新バージョン（1.31.4より新しいバージョン等）へ更新してください。

#### References
- https://github.com/The-40-Thieves/obsidian-tc/blob/v1.31.4/CHANGELOG.md
- https://github.com/The-40-Thieves/obsidian-tc/commit/99f7914ca0fbeed92e7c4d39cc8c3e5830dab133
- https://github.com/The-40-Thieves/obsidian-tc/pull/978
- https://github.com/The-40-Thieves/obsidian-tc/releases/tag/v1.31.4
- https://github.com/The-40-Thieves/obsidian-tc/security/advisories/GHSA-r3g7-r4hr-m258

### [CVE-2026-55459](https://github.com/intranda/goobi-viewer-core/commit/73e2ccb63c36392d46f8d21644592efd6cf87933)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-55459
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-24 00:17:33 JST
- 更新日: 2026-10-24 01:28:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Goobi viewer の OpenID トークン検証処理において、aud（受領者）クレームの適切な暗号的検証が行われず、手動チェックも単一文字列比較のみとなっている問題。
- 影響: 別サービス向けに発行されたトークンを悪用し、他のユーザーになりすまして認証を突破される可能性があります。
- 推奨対応: Goobi viewer をバージョン 26.05 以降に更新してください。

#### References
- https://github.com/intranda/goobi-viewer-core/commit/73e2ccb63c36392d46f8d21644592efd6cf87933
- https://github.com/intranda/goobi-viewer-core/releases/tag/v26.05
- https://github.com/intranda/goobi-viewer-core/security/advisories/GHSA-7vrv-qh6g-gfx7

### [CVE-2026-79980](https://github.com/zephyrproject-rtos/zephyr/commit/6a96770a1ea8c38a54a45f892c3e97be0f7dac41)

> **Backend** / **MEDIUM** / CVSS: **5.6** / KEV: **no**

- タイトル: CVE-2026-79980
- 関連キーワード: go, gin, aws
- 影響製品: -
- 公開日: 2026-10-24 05:17:27 JST
- 更新日: 2026-10-24 05:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DHCPv4 クライアントの実装において、トランザクション ID (xid) がランダムではなく、連番で更新・再利用されている問題。
- 影響: トランザクション ID が予測可能となり、攻撃者による偽の DHCP レスポンスの注入（スプーフィング）を受ける可能性があります。
- 推奨対応: 該当ライブラリ/ファームウェアの修正パッチの適用または最新版への更新を行ってください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/6a96770a1ea8c38a54a45f892c3e97be0f7dac41
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-p2q6-38x2-wmc8

### [CVE-2026-115477](https://github.com/The-40-Thieves/obsidian-tc/blob/v1.31.4/CHANGELOG.md)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-115477
- 関連キーワード: go, echo
- 影響製品: -
- 公開日: 2026-10-24 00:17:29 JST
- 更新日: 2026-10-24 00:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: obsidian-tc において、人間による確認が必要なツール呼び出しの再送信時、確認の拒否やキャンセルが発生していても状態 ID (requestState) の照合のみで実行を許可してしまう問題。
- 影響: ユーザーの明示的な承認なしに、意図しない破壊的な操作が実行される可能性があります。
- 推奨対応: obsidian-tc を修正された最新バージョン（1.31.4より新しいバージョン等）へ更新してください。

#### References
- https://github.com/The-40-Thieves/obsidian-tc/blob/v1.31.4/CHANGELOG.md
- https://github.com/The-40-Thieves/obsidian-tc/commit/101c91c656e2c2b88bcf3696a5da035f8c032c71
- https://github.com/The-40-Thieves/obsidian-tc/issues/967
- https://github.com/The-40-Thieves/obsidian-tc/pull/969
- https://github.com/The-40-Thieves/obsidian-tc/releases/tag/v1.31.4

### [CVE-2026-115778](https://github.com/twisted/twisted/commit/073ba878c6c07d569cb61abc5ae76d46eff1b529)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-115778
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-10-24 06:17:23 JST
- 更新日: 2026-10-24 06:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Twisted の Telnet 実装において、サブネゴシエーション受信バッファに上限が設定されていない問題。
- 影響: 未認証の攻撃者が終了子を含まないデータを送信し続けることでメモリが枯渇し、プロセス停止（DoS）が発生する可能性があります。
- 推奨対応: Twisted をバージョン 26.10.0rc1 以降に更新してください。

#### References
- https://github.com/twisted/twisted/commit/073ba878c6c07d569cb61abc5ae76d46eff1b529
- https://github.com/twisted/twisted/commit/5d91cc66a3591faba758a80a1479e0103602facc
- https://github.com/twisted/twisted/pull/12750
- https://github.com/twisted/twisted/releases/tag/twisted-26.10.0rc1
- https://github.com/twisted/twisted/security/advisories/GHSA-cwm5-jh59-mwxr

### [CVE-2026-79982](https://github.com/zephyrproject-rtos/zephyr/commit/0419defd2391652edc27689d206fcd9c48439d4a)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-79982
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-24 05:17:28 JST
- 更新日: 2026-10-24 05:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Bluetooth HCI USB トランスポート処理において、パケットを固定サイズバッファにコピーする際に長さを検証していない問題。
- 影響: 過大なパケット受信時にバッファオーバーフローが発生し、メモリ破壊やDoS（サービス拒否）、場合によってはコード実行につながる可能性があります。
- 推奨対応: 長さを検証する修正パッチの適用、または修正済みバージョンへの更新を行ってください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/0419defd2391652edc27689d206fcd9c48439d4a
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-w5px-w97v-c3hj

### [CVE-2026-55457](https://github.com/intranda/goobi-viewer-core/commit/419dc7320e1ec45e83dcb440871b50181f04716d)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-55457
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-24 00:17:33 JST
- 更新日: 2026-10-24 01:28:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Goobi viewer において、認証トークン未設定時に空文字列を返し、アクセスリクエストの検証時に設定値が空でないかの確認を行わない問題。
- 影響: 空のトークンパラメータ (?token=) を付与することで、保護された API エンドポイントの認証をバイパスされる可能性があります。
- 推奨対応: Goobi viewer をバージョン 26.05 以降に更新してください。

#### References
- https://github.com/intranda/goobi-viewer-core/commit/419dc7320e1ec45e83dcb440871b50181f04716d
- https://github.com/intranda/goobi-viewer-core/releases/tag/v26.05
- https://github.com/intranda/goobi-viewer-core/security/advisories/GHSA-4qpq-f4r6-7cc6

### [CVE-2026-46346](https://github.com/intranda/goobi-viewer-core/commit/9c2c83f00f497c11ab6aaa0bd5a68173cd446eef)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-46346
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-24 00:17:31 JST
- 更新日: 2026-10-24 06:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Goobi viewer（26.05未満）において、リクエスト時間に基づく予測可能なパスワードリセットトークンが生成される脆弱性。
- 影響: 攻撃者にメールアドレスを知られている場合、トークンをブルートフォース推測されてアカウントのパスワードを不正にリセットされる可能性がある。
- 推奨対応: Goobi viewerをバージョン26.05以降に更新してください。

#### References
- https://github.com/intranda/goobi-viewer-core/commit/9c2c83f00f497c11ab6aaa0bd5a68173cd446eef
- https://github.com/intranda/goobi-viewer-core/releases/tag/v26.05
- https://github.com/intranda/goobi-viewer-core/security/advisories/GHSA-gj5g-4rxf-8rmq

### [CVE-2026-46347](https://github.com/intranda/goobi-viewer-core/commit/1fa7a30a3a7699a82ea0df9c1a8997b2894d7841)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-46347
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-24 00:17:31 JST
- 更新日: 2026-10-24 01:28:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Goobi viewer のパスワードリセット機能において、生成される一時パスワードのエントロピーが不足している（予測可能である）問題。
- 影響: リセット発生時、生成時刻を推測されることでパスワードをブルートフォース攻撃され、アカウントが乗っ取られる可能性があります。
- 推奨対応: Goobi viewer をバージョン 26.05 以降に更新してください。

#### References
- https://github.com/intranda/goobi-viewer-core/commit/1fa7a30a3a7699a82ea0df9c1a8997b2894d7841
- https://github.com/intranda/goobi-viewer-core/commit/9c2c83f00f497c11ab6aaa0bd5a68173cd446eef
- https://github.com/intranda/goobi-viewer-core/releases/tag/v26.05
- https://github.com/intranda/goobi-viewer-core/security/advisories/GHSA-hw9w-7r6g-2fjc

### [CVE-2026-55465](https://github.com/intranda/goobi-viewer-core/commit/46fb8759caa91b5ba9f0c387e5a0d0d3875bf633)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-55465
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-24 00:17:33 JST
- 更新日: 2026-10-24 01:28:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Goobi viewer（22.04〜26.05未満）の空間検索エンドポイントにおける、Solrクエリのパラメータエスケープ不備によるインジェクションの脆弱性。
- 影響: アクセス制限フィルターをバイパスされ、制限された地理参照レコードを取得される可能性がある。
- 推奨対応: Goobi viewerをバージョン26.05以降に更新してください。

#### References
- https://github.com/intranda/goobi-viewer-core/commit/46fb8759caa91b5ba9f0c387e5a0d0d3875bf633
- https://github.com/intranda/goobi-viewer-core/releases/tag/v26.05
- https://github.com/intranda/goobi-viewer-core/security/advisories/GHSA-v5h4-qrx3-qg3h

### [CVE-2026-55463](https://github.com/intranda/goobi-viewer-core/commit/8714ca81065d2c2c6e614a1ee6753de65cbe3412)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-55463
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-24 00:17:33 JST
- 更新日: 2026-10-24 01:28:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Goobi viewer（4.11.0〜26.05未満）のWebSocketエンドポイントにおける、認証およびOrigin検証の不備。
- 影響: 未認証の攻撃者に接続を許し、ページロック情報の汚染や偽メッセージの送信によってレビュー作業を妨害される可能性がある。
- 推奨対応: Goobi viewerをバージョン26.05以降に更新してください。

#### References
- https://github.com/intranda/goobi-viewer-core/commit/8714ca81065d2c2c6e614a1ee6753de65cbe3412
- https://github.com/intranda/goobi-viewer-core/releases/tag/v26.05
- https://github.com/intranda/goobi-viewer-core/security/advisories/GHSA-h5m9-fpvw-qr36

### [CVE-2026-55442](https://github.com/intranda/goobi-viewer-core/commit/330da2f8255a9ed2200ba46b98bb9b6a88748a4e)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-55442
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-24 00:17:32 JST
- 更新日: 2026-10-24 01:28:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Goobi viewer（23.03〜26.05未満）のクエリサニタイズ処理における、二重中括弧によるフィルタバイパスの脆弱性。
- 影響: サニタイズ処理を回避され、意図しないSolrローカルパラメータが実行される可能性がある。
- 推奨対応: Goobi viewerをバージョン26.05以降に更新してください。

#### References
- https://github.com/intranda/goobi-viewer-core/commit/330da2f8255a9ed2200ba46b98bb9b6a88748a4e
- https://github.com/intranda/goobi-viewer-core/commit/5a59ffa5d76169a4ad3cc396023ad4a4eca217da
- https://github.com/intranda/goobi-viewer-core/releases/tag/v26.05
- https://github.com/intranda/goobi-viewer-core/security/advisories/GHSA-2r24-qxpf-cj65

### [CVE-2026-55444](https://github.com/intranda/goobi-viewer-core/commit/e8d987f8478b86559ef3ea236be0d86e08948f6b)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-55444
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-24 00:17:32 JST
- 更新日: 2026-10-24 01:28:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Goobi viewer（26.05未満）のレガシーRSSサーブレットにおける、入力検証不備によるSolrインジェクションの脆弱性。
- 影響: アクセス制限フィルターを無効化され、本来アクセス制限のあるレコードがRSSフィードに含まれる可能性がある。
- 推奨対応: Goobi viewerをバージョン26.05以降に更新してください。

#### References
- https://github.com/intranda/goobi-viewer-core/commit/e8d987f8478b86559ef3ea236be0d86e08948f6b
- https://github.com/intranda/goobi-viewer-core/commit/fcdae14b06e99f3320a02d45a6be7fc6e5c69a6e
- https://github.com/intranda/goobi-viewer-core/releases/tag/v26.05
- https://github.com/intranda/goobi-viewer-core/security/advisories/GHSA-763m-wjm9-6873

### [CVE-2026-115572](https://github.com/py-pdf/pypdf/commit/68a0e5046cc9e14a6c24a21a713f3c7fbde18b4b)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-115572
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-24 05:17:20 JST
- 更新日: 2026-10-24 05:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pypdf（6.21.2未満）において、存在しないオブジェクトを繰り返し参照する悪意のあるPDFの解析時に発生する処理遅延の脆弱性。
- 影響: ファイル解析時にフルファイルのリカバリが繰り返し発生し、極端な処理遅延（DoS状態）に陥る可能性がある。
- 推奨対応: pypdfをバージョン6.21.2以降に更新してください。

#### References
- https://github.com/py-pdf/pypdf/commit/68a0e5046cc9e14a6c24a21a713f3c7fbde18b4b
- https://github.com/py-pdf/pypdf/pull/4240
- https://github.com/py-pdf/pypdf/releases/tag/6.21.2
- https://github.com/py-pdf/pypdf/security/advisories/GHSA-6c7f-9265-g8fw

### [CVE-2026-115580](https://github.com/py-pdf/pypdf/commit/a3061e34b169d34478d520f5f049c53cfb1482b2)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-115580
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-24 05:17:21 JST
- 更新日: 2026-10-24 05:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pypdf（6.21.2未満）において、実際の容量を超える宣言エントリ数を持つクロスリファレンステーブルを含むPDFの解析時の問題。
- 影響: ファイルオープン時に過剰な処理が発生し、サービス拒否（DoS）状態に陥る可能性がある。
- 推奨対応: pypdfをバージョン6.21.2以降に更新してください。

#### References
- https://github.com/py-pdf/pypdf/commit/a3061e34b169d34478d520f5f049c53cfb1482b2
- https://github.com/py-pdf/pypdf/pull/4239
- https://github.com/py-pdf/pypdf/releases/tag/6.21.2
- https://github.com/py-pdf/pypdf/security/advisories/GHSA-gmh7-3g9r-mjh5

### [CVE-2026-115585](https://github.com/py-pdf/pypdf/commit/68a0e5046cc9e14a6c24a21a713f3c7fbde18b4b)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-115585
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-24 05:17:21 JST
- 更新日: 2026-10-24 05:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pypdf（6.21.2未満）における不完全な修正に起因し、悪意のあるクロスリファレンスストリーム処理時に過剰な再読み込みが発生する問題。
- 影響: リカバリキャッシュが存在する場合でも不必要な全ストリーム再読み込みが発生し、長時間の処理遅延（DoS状態）を引き起こす可能性がある。
- 推奨対応: pypdfをバージョン6.21.2以降に更新してください。

#### References
- https://github.com/py-pdf/pypdf/commit/68a0e5046cc9e14a6c24a21a713f3c7fbde18b4b
- https://github.com/py-pdf/pypdf/pull/4240
- https://github.com/py-pdf/pypdf/releases/tag/6.21.2
- https://github.com/py-pdf/pypdf/security/advisories/GHSA-jr96-gvgh-j3r4

### [CVE-2026-57845](https://github.com/SaiTeja-Erukude/CVE-2026-57845-hf-datasets-rce)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-57845
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-24 01:16:52 JST
- 更新日: 2026-10-24 04:45:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Hugging Face Datasets（5.1.0以下）の非推奨なpandasビルダーにおける不安全なデシリアライズの脆弱性。
- 影響: 悪意のあるpickleファイルを含むデータセットをロードした際、被害者プロセスの権限で任意コードを実行される可能性がある。
- 推奨対応: Hugging Face Datasetsを修正済みバージョンへ更新するか、信頼できないデータセットでの非推奨なpandasビルダー利用を回避してください。

#### References
- https://github.com/SaiTeja-Erukude/CVE-2026-57845-hf-datasets-rce
- https://github.com/huggingface/datasets/pull/8879
- https://www.vulncheck.com/advisories/hugging-face-datasets-pickle-deserialization-rce-via-pandas-builder

### [CVE-2026-115775](https://github.com/twisted/twisted/commit/8873814bec8288e2466fad4d2c4d64039beb88b0)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-115775
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-24 06:17:23 JST
- 更新日: 2026-10-24 06:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Twisted（26.10.0rc1未満）のExpatElementStreamパーサーにおける、要素数・バイト数の上限欠如による不備。
- 影響: 未認証のリモート攻撃者により単一の接続でサーバーメモリを枯渇させられ、プロセスを異常終了（DoS）させられる可能性がある。
- 推奨対応: Twistedをバージョン26.10.0rc1以降に更新してください。

#### References
- https://github.com/twisted/twisted/commit/8873814bec8288e2466fad4d2c4d64039beb88b0
- https://github.com/twisted/twisted/pull/12751
- https://github.com/twisted/twisted/releases/tag/twisted-26.10.0rc1
- https://github.com/twisted/twisted/security/advisories/GHSA-3476-c5c2-fr73

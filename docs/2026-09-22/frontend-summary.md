# Frontend CVE Summary (2026-09-22)

## Overview

- 取得日時: 2026-09-22 09:45:37 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 1
- High: 1
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-58491](https://github.com/warp-tech/warpgate/commit/eab0548f018d95b5f96f8e913527000e05ed93a2)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-58491
- 関連キーワード: javascript, gin, mysql
- 影響製品: -
- 公開日: 2026-09-22 04:17:06 JST
- 更新日: 2026-09-22 04:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Warpgate 0.25.5 未満における SSO エンドポイントのパラメータ処理の不備による XSS およびオープンリダイレクトの脆弱性。
- 影響: 認証済みセッションデータの取得、被害者の権限での API 操作、悪意のあるサイトへの転送が行われる可能性があります。
- 推奨対応: Warpgate を 0.25.5 以降へアップデートしてください。

#### References
- https://github.com/warp-tech/warpgate/commit/eab0548f018d95b5f96f8e913527000e05ed93a2
- https://github.com/warp-tech/warpgate/releases/tag/v0.25.5
- https://github.com/warp-tech/warpgate/security/advisories/GHSA-3c3w-75j2-7h74

### [CVE-2026-46650](https://github.com/laurent22/joplin/commit/9fdc2d4adbd7b7326a2d0dcc32e12b705bfc285e)

> **Frontend** / **MEDIUM** / CVSS: **4.4** / KEV: **no**

- タイトル: CVE-2026-46650
- 関連キーワード: javascript, gin, express
- 影響製品: -
- 公開日: 2026-09-22 07:16:56 JST
- 更新日: 2026-09-22 07:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joplin 3.7.2 未満における内部リソース URL 検証の不備により、`javascript:` URL が許可される脆弱性。
- 影響: 公開共有されたノートのリンクを被害者が開いた際、Joplin Server オリジンで任意のスクリプトが実行され、情報漏洩や不正なリクエスト送信が引き起こされる可能性があります。
- 推奨対応: Joplin を 3.7.2 以降にアップデートしてください。

#### References
- https://github.com/laurent22/joplin/commit/9fdc2d4adbd7b7326a2d0dcc32e12b705bfc285e
- https://github.com/laurent22/joplin/pull/15435
- https://github.com/laurent22/joplin/security/advisories/GHSA-x9vj-jrqf-9wcm

### [CVE-2026-68919](https://github.com/gocd/gocd/commit/a03eeeaa4a85edfc9053e743610547d4fcf7aea6)

> **Frontend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-68919
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-09-22 00:17:30 JST
- 更新日: 2026-09-22 00:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GoCD 13.3.0 から 26.1.0 未満におけるパッケージマテリアルコメントの処理不備による格納型クロスサイトスクリプティング（Stored XSS）の脆弱性。
- 影響: 影響を受けるページを閲覧したユーザーのブラウザ上で任意の JavaScript が実行され、特権セッションの漏洩や不正操作につながる可能性があります。
- 推奨対応: GoCD を 26.1.0 以降へアップデートしてください。

#### References
- https://github.com/gocd/gocd/commit/a03eeeaa4a85edfc9053e743610547d4fcf7aea6
- https://github.com/gocd/gocd/releases/tag/26.1.0
- https://github.com/gocd/gocd/security/advisories/GHSA-pp5x-wgv2-g37p
- https://www.gocd.org/releases/#26-1-0

### [CVE-2026-91165](https://github.com/warp-tech/warpgate/commit/e94425a08f501383a67316673749dcbd637c6ce3)

> **Frontend** / **LOW** / CVSS: **2.4** / KEV: **no**

- タイトル: CVE-2026-91165
- 関連キーワード: javascript, gin, mysql
- 影響製品: -
- 公開日: 2026-09-22 04:17:15 JST
- 更新日: 2026-09-22 05:17:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Warpgate 0.27.6 未満の `form_post` SSO リターン処理におけるレスポンス内スクリプト挿入の不備。
- 影響: SSO フロー完了時に挿入された HTML/スクリプトが実行される可能性があります。
- 推奨対応: Warpgate を 0.27.6 以降へアップデートしてください。

#### References
- https://github.com/warp-tech/warpgate/commit/e94425a08f501383a67316673749dcbd637c6ce3
- https://github.com/warp-tech/warpgate/releases/tag/v0.27.6
- https://github.com/warp-tech/warpgate/security/advisories/GHSA-vvpj-p7j8-4rv4

### [CVE-2026-36472](https://github.com/CuteNews/cutenews-2.0)

> **Frontend** / **MEDIUM** / CVSS: **5.2** / KEV: **no**

- タイトル: CVE-2026-36472
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-22 01:17:08 JST
- 更新日: 2026-09-22 01:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CuteNews v.2.1.2 における `__referer` 値の不十分なエスケープ処理によるクロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 被害者がリンクをクリックすることで、認証済みセッション上で任意の JavaScript が実行される可能性があります。
- 推奨対応: 修正パッチの適用または安全なバージョンへの更新を検討してください。

#### References
- https://github.com/CuteNews/cutenews-2.0
- https://github.com/CuteNews/cutenews-2.0/blob/master/core/core.php
- https://github.com/UmbraDeorum/cutenews-2.0-CVEs-2026-Disclosure

### [CVE-2026-45381](https://github.com/Tautulli/Tautulli/commit/3bee54087370fc275b13565a9e58235341bb4cf7)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-45381
- 関連キーワード: javascript, python
- 影響製品: -
- 公開日: 2026-09-22 05:17:25 JST
- 更新日: 2026-09-22 05:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tautulli 2.17.2 未満の `/search` エンドポイントにおけるクエリパラメータ（バックスラッシュ未対応）のエスケープ不備による XSS 脆弱性。
- 影響: 細工されたリンクを認証済みユーザーが踏むことで、Tautulli の Web コンテキスト上でスクリプトが実行される可能性があります。
- 推奨対応: Tautulli を 2.17.2 以降へアップデートしてください。

#### References
- https://github.com/Tautulli/Tautulli/commit/3bee54087370fc275b13565a9e58235341bb4cf7
- https://github.com/Tautulli/Tautulli/releases/tag/v2.17.2
- https://github.com/Tautulli/Tautulli/security/advisories/GHSA-mjvc-6cc2-6ffr

### [CVE-2026-49995](https://github.com/Tautulli/Tautulli/commit/12761b2d01e78f22e54e8ad8d3133931147cbb77)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-49995
- 関連キーワード: javascript, python
- 影響製品: -
- 公開日: 2026-09-22 05:17:25 JST
- 更新日: 2026-09-22 05:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tautulli 2.17.2 未満のニュースレター設定（cron フィールド）における不十分なエンコードによる格納型 XSS 脆弱性。
- 影響: 悪意のある cron 値が保存され、管理者が設定モーダルを開いた際に任意の JavaScript が永続的に実行される可能性があります。
- 推奨対応: Tautulli を 2.17.2 以降へアップデートしてください。

#### References
- https://github.com/Tautulli/Tautulli/commit/12761b2d01e78f22e54e8ad8d3133931147cbb77
- https://github.com/Tautulli/Tautulli/releases/tag/v2.17.2
- https://github.com/Tautulli/Tautulli/security/advisories/GHSA-r6pg-vqxj-v75j

### [CVE-2026-58504](https://github.com/jgraph/drawio/commit/7976c02e1b10b1687c028d82782f9f5d90a885d6)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-58504
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-22 02:17:36 JST
- 更新日: 2026-09-22 02:17:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: draw.io 30.2.5 未満における特定セルの処理および HTML エンコード不足による XSS（CVE-2026-46642 の迂回）の脆弱性。
- 影響: 細工された `.drawio` ファイルを開くことで任意の JavaScript が実行され、図面データやストレージ情報の漏洩が発生する可能性があります。
- 推奨対応: draw.io を 30.2.5 以降へアップデートしてください。

#### References
- https://github.com/jgraph/drawio/commit/7976c02e1b10b1687c028d82782f9f5d90a885d6
- https://github.com/jgraph/drawio/releases/tag/v30.2.5
- https://github.com/jgraph/drawio/security/advisories/GHSA-c76x-r78m-phwx

### [CVE-2026-78847](https://blog.checo.cc/en/posts/Security/1)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-78847
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-22 07:16:58 JST
- 更新日: 2026-09-22 07:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: gray-matter（検証バージョン 4.0.3）において js/javascript 言語のフロントマター解析に `eval()` を使用している問題。
- 影響: 悪意のあるフロントマターの解析時に、任意の JavaScript コードが実行される可能性があります。
- 推奨対応: 利用を中止するか、修正バージョンへの変更・評価関数の見直しを検討してください。

#### References
- https://blog.checo.cc/en/posts/Security/1
- https://github.com/jonschlinkert/gray-matter/issues/112
- https://github.com/jonschlinkert/gray-matter/issues/131
- https://github.com/jonschlinkert/gray-matter/issues/182

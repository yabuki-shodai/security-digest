# Frontend CVE Summary (2026-07-28)

## Overview

- 取得日時: 2026-07-28 08:16:47 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 16
- Critical: 0
- High: 6
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-64642](https://github.com/vercel/next.js/commit/6bf4df14508ad6c0cd46af50c6051ee42f2d9151)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-64642
- 関連キーワード: next.js, react, turbopack
- 影響製品: -
- 公開日: 2026-07-28 03:16:59 JST
- 更新日: 2026-07-28 03:16:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Next.jsの特定バージョンで、App RouterとTurbopackを使用しconfig.i18n.localesに単一エントリがある場合、認証をバイパスできる可能性がある。
- 影響: 認証を回避され、不正アクセスのリスクがある。
- 推奨対応: Next.jsをバージョン16.2.11以降に更新する。

#### References
- https://github.com/vercel/next.js/commit/6bf4df14508ad6c0cd46af50c6051ee42f2d9151
- https://github.com/vercel/next.js/pull/96014
- https://github.com/vercel/next.js/releases/tag/v16.2.11
- https://github.com/vercel/next.js/security/advisories/GHSA-6gpp-xcg3-4w24

### [CVE-2026-64645](https://github.com/vercel/next.js/commit/35f501357e9b0fe7c950b0d6aa8fcf5343f707e9)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-64645
- 関連キーワード: next.js, react, gin
- 影響製品: -
- 公開日: 2026-07-28 03:16:59 JST
- 更新日: 2026-07-28 03:16:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Next.jsの特定バージョンで、rewrites()やredirects()の外部ホスト名がリクエスト制御入力から構築される場合、任意のホスト名を指定可能。
- 影響: Server-Side Request Forgeryやオープンリダイレクトのリスクがある。
- 推奨対応: Next.jsをバージョン15.5.21または16.2.11以降に更新する。

#### References
- https://github.com/vercel/next.js/commit/35f501357e9b0fe7c950b0d6aa8fcf5343f707e9
- https://github.com/vercel/next.js/commit/d3033266c6dff23f7be71e19341fe3a8c6e2c599
- https://github.com/vercel/next.js/releases/tag/v15.5.21
- https://github.com/vercel/next.js/releases/tag/v16.2.11
- https://github.com/vercel/next.js/security/advisories/GHSA-p9j2-gv94-2wf4

### [CVE-2026-64641](https://github.com/vercel/next.js/commit/019628571641dec57aaf349ba0c360e3964e6f12)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-64641
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-07-28 03:16:58 JST
- 更新日: 2026-07-28 04:17:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Next.jsの特定バージョンで、App RouterとServer Actionを使用した場合、特定のリクエストによりCPU使用率が過剰に上昇し、同一プロセスの他リクエスト処理が阻害される可能性がある。
- 影響: サービスの可用性低下やDoSのリスクがある。
- 推奨対応: Next.jsをバージョン15.5.21または16.2.11以降に更新する。

#### References
- https://github.com/vercel/next.js/commit/019628571641dec57aaf349ba0c360e3964e6f12
- https://github.com/vercel/next.js/pull/96013
- https://github.com/vercel/next.js/releases/tag/v15.5.21
- https://github.com/vercel/next.js/releases/tag/v16.2.11
- https://github.com/vercel/next.js/security/advisories/GHSA-m99w-x7hq-7vfj

### [CVE-2026-64649](https://github.com/vercel/next.js/commit/b51206321854193208c0805ba42acc49287f942b)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-64649
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-07-28 05:16:40 JST
- 更新日: 2026-07-28 05:16:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Next.jsの特定バージョンで、Server Actionがリクエストを転送またはリダイレクトする際に、攻撃者が悪意あるホストへリクエストを送信可能。
- 影響: Server-Side Request Forgeryや認証回避のリスクがある。
- 推奨対応: Next.jsをバージョン15.5.21または16.2.11以降に更新し、信頼できるホストヘッダーを固定する。

#### References
- https://github.com/vercel/next.js/commit/b51206321854193208c0805ba42acc49287f942b
- https://github.com/vercel/next.js/commit/e3e5666ccead3a15162793d697af5e48b7cc0498
- https://github.com/vercel/next.js/releases/tag/v15.5.21
- https://github.com/vercel/next.js/releases/tag/v16.2.11
- https://github.com/vercel/next.js/security/advisories/GHSA-89xv-2m56-2m9x

### [CVE-2026-64644](https://github.com/vercel/next.js/commit/93cb90891402fa4c47798d03cb9e05c13233766c)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-64644
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-07-28 03:16:59 JST
- 更新日: 2026-07-28 04:17:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Next.jsの特定バージョンで、自己ホスティング環境のデフォルト画像ローダー使用時に、リモート画像の最適化設定によりCPU過負荷が発生する可能性がある。
- 影響: CPUリソースの枯渇によるサービス障害のリスクがある。
- 推奨対応: Next.jsをバージョン15.5.21または16.2.11以降に更新し、該当設定を確認する。

#### References
- https://github.com/vercel/next.js/commit/93cb90891402fa4c47798d03cb9e05c13233766c
- https://github.com/vercel/next.js/pull/96006
- https://github.com/vercel/next.js/releases/tag/v15.5.21
- https://github.com/vercel/next.js/releases/tag/v16.2.11
- https://github.com/vercel/next.js/security/advisories/GHSA-q8wf-6r8g-63ch

### [CVE-2026-64643](https://github.com/vercel/next.js/commit/1b0c3ae912a3ad925c60065cc8d55b070fa8bcd3)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-64643
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-07-28 03:16:59 JST
- 更新日: 2026-07-28 04:17:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Next.jsの特定バージョンで、App RouterやServer Actionsを使用するアプリケーションで、認証をバイパスしてサーバーアクションIDが漏洩する可能性がある。
- 影響: 情報漏洩により攻撃の足掛かりとなる可能性がある。
- 推奨対応: Next.jsをバージョン15.5.21または16.2.11以降に更新する。

#### References
- https://github.com/vercel/next.js/commit/1b0c3ae912a3ad925c60065cc8d55b070fa8bcd3
- https://github.com/vercel/next.js/commit/ff12a6124e1504f17b62de948b8a553fdecaef7b
- https://github.com/vercel/next.js/releases/tag/v15.5.21
- https://github.com/vercel/next.js/releases/tag/v16.2.11
- https://github.com/vercel/next.js/security/advisories/GHSA-955p-x3mx-jcvp

### [CVE-2026-64646](https://github.com/vercel/next.js/commit/57c31f724d746e86a9e8b92aa8be538a922446a4)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-64646
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-07-28 04:17:21 JST
- 更新日: 2026-07-28 06:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Next.jsの特定バージョンで、App RouterとEdgeランタイムを使用するServer Actionがメモリ過剰消費を引き起こす可能性がある。
- 影響: サービスの可用性低下やリソース枯渇のリスクがある。
- 推奨対応: Next.jsをバージョン15.5.21または16.2.11以降に更新する。

#### References
- https://github.com/vercel/next.js/commit/57c31f724d746e86a9e8b92aa8be538a922446a4
- https://github.com/vercel/next.js/commit/9a4651e754f70b12e397694ffc41f44c3ba8cc17
- https://github.com/vercel/next.js/releases/tag/v15.5.21
- https://github.com/vercel/next.js/releases/tag/v16.2.11
- https://github.com/vercel/next.js/security/advisories/GHSA-4c39-4ccg-62r3

### [CVE-2026-64647](https://github.com/vercel/next.js/commit/025bf4a5f7b47fb7758c4ebf1c931a61c451c082)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-64647
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-07-28 04:17:21 JST
- 更新日: 2026-07-28 05:16:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Next.jsの特定バージョンで、リクエストボディの文字コードがUTF-8以外の場合、サーバーサイドフェッチが異なるリクエストのレスポンスを誤って返す可能性がある。
- 影響: 機密データの漏洩リスクがある。
- 推奨対応: Next.jsをバージョン15.5.21または16.2.11以降に更新し、リクエストの文字コードを確認する。

#### References
- https://github.com/vercel/next.js/commit/025bf4a5f7b47fb7758c4ebf1c931a61c451c082
- https://github.com/vercel/next.js/pull/96008
- https://github.com/vercel/next.js/releases/tag/v15.5.21
- https://github.com/vercel/next.js/releases/tag/v16.2.11
- https://github.com/vercel/next.js/security/advisories/GHSA-4633-3j49-mh5q

### [CVE-2026-64648](https://github.com/vercel/next.js/commit/062f66700b52a5d6bba2c0605d55577ab7ad262c)

> **Frontend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-64648
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-07-28 05:16:40 JST
- 更新日: 2026-07-28 05:16:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Next.jsの特定バージョンで、fetch呼び出し時に異なるinitオブジェクトを使用すると、キャッシュされた異なるリクエストのレスポンスが返される可能性がある。
- 影響: 機密データの漏洩リスクがある。
- 推奨対応: Next.jsをバージョン15.5.21または16.2.11以降に更新し、fetchの使用方法を見直す。

#### References
- https://github.com/vercel/next.js/commit/062f66700b52a5d6bba2c0605d55577ab7ad262c
- https://github.com/vercel/next.js/commit/73b94872bc343d09494b50394d8c08eb9fc8e56a
- https://github.com/vercel/next.js/releases/tag/v15.5.21
- https://github.com/vercel/next.js/releases/tag/v16.2.11
- https://github.com/vercel/next.js/security/advisories/GHSA-68g3-v927-f742

### [CVE-2026-56747](https://docs.cribl.io/stream/release-notes/release-v4182/#security-fixes)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-56747
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-28 05:16:39 JST
- 更新日: 2026-07-28 06:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Cribl Stream 4.18.2未満で、JSON Pointer-to-accessorコンパイラのコード生成制御不備により、認証済み攻撃者が任意のJavaScriptを実行可能。
- 影響: サーバー上での任意コード実行のリスクがある。
- 推奨対応: Cribl Streamをバージョン4.18.2以降に更新する。

#### References
- https://docs.cribl.io/stream/release-notes/release-v4182/#security-fixes
- https://trust.cribl.io/notifications

### [CVE-2026-59239](https://github.com/Roskus/prospero-flow-crm/commit/32efcd5c395ee55119fb9aea502a9d06e4c5adb8)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-59239
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-28 03:16:57 JST
- 更新日: 2026-07-28 04:17:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Roskus Prospero Flow CRMのメールモジュールにおいて、認証済みの低権限ユーザーが保存型XSSを利用し、他ユーザーのブラウザで任意のJavaScriptを実行可能。
- 影響: 管理者を含むユーザーのセッション乗っ取りやアカウントの不正取得の恐れ。
- 推奨対応: バージョン5.4.4以降にアップデートし、メール本文のサニタイズを適切に行うこと。

#### References
- https://github.com/Roskus/prospero-flow-crm/commit/32efcd5c395ee55119fb9aea502a9d06e4c5adb8
- https://github.com/Roskus/prospero-flow-crm/releases
- https://secur0.com/en/cna/cve-list/cve-2026-59239-stored-xss-in-prospero-flow-crm-email-body-allows-administrator-account-takeover

### [CVE-2026-54272](https://github.com/beaugunderson/ip-address/security/advisories/GHSA-22jq-vg5j-6vgg)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-54272
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-28 03:16:56 JST
- 更新日: 2026-07-28 03:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: JavaScriptのip-addressライブラリでIPv4マップド/NAT64 IPv6アドレスの誤分類によりSSRFが発生する可能性。
- 影響: 不正なIPv6アドレス処理により、サーバーサイドリクエスト偽造攻撃が可能となる恐れ。
- 推奨対応: 該当バージョンからのアップデートを検討し、IPv6アドレスの正しい分類を適用すること。

#### References
- https://github.com/beaugunderson/ip-address/security/advisories/GHSA-22jq-vg5j-6vgg
- https://github.com/beaugunderson/ip-address/security/advisories/GHSA-22jq-vg5j-6vgg

### [CVE-2026-59727](https://github.com/withastro/astro/commit/7ba0bb1dc7516e88caff9abd7767322af44b0294)

> **Frontend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-59727
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-28 05:16:40 JST
- 更新日: 2026-07-28 05:16:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Astroフレームワークで特定のtransitionディレクティブに攻撃者制御の入力を渡すと、反射型XSSが発生する可能性。
- 影響: 悪意あるHTML/JavaScriptがサーバー出力に注入される恐れ。
- 推奨対応: バージョン7.0.4以降に更新し、信頼できない入力をtransitionディレクティブに直接渡さないこと。

#### References
- https://github.com/withastro/astro/commit/7ba0bb1dc7516e88caff9abd7767322af44b0294
- https://github.com/withastro/astro/pull/17212
- https://github.com/withastro/astro/releases/tag/astro@7.0.4
- https://github.com/withastro/astro/security/advisories/GHSA-7pw4-f3q4-r2p2

### [CVE-2026-66029](https://codecanyon.net/item/ekushey-project-manager-crm/9492104)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-66029
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-28 03:17:00 JST
- 更新日: 2026-07-28 03:17:00 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Ekushey Project Manager CRMで認証済みクライアントユーザーがクライアント名フィールドに悪意あるスクリプトを保存可能な保存型XSS。
- 影響: スタッフや管理者のブラウザでスクリプトが実行され、セッション乗っ取り等のリスク。
- 推奨対応: 入力値のサニタイズを実施し、ソフトウェアのアップデートを検討すること。

#### References
- https://codecanyon.net/item/ekushey-project-manager-crm/9492104
- https://github.com/aaronamran/CVE-Disclosures/tree/main/CVE-2026/CVE-2026-66029
- https://www.vulncheck.com/advisories/ekushey-project-manager-crm-stored-xss-via-client-name-field

### [CVE-2026-66030](https://codecanyon.net/item/ekushey-project-manager-crm/9492104)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-66030
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-28 03:17:00 JST
- 更新日: 2026-07-28 04:17:22 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Ekushey Project Manager CRMで認証済みクライアントユーザーがチケットタイトルに悪意あるスクリプトを保存可能な保存型XSS。
- 影響: スタッフや管理者のブラウザでスクリプトが実行される恐れ。
- 推奨対応: 入力値の適切なサニタイズとソフトウェアの更新を推奨。

#### References
- https://codecanyon.net/item/ekushey-project-manager-crm/9492104
- https://github.com/aaronamran/CVE-Disclosures/tree/main/CVE-2026/CVE-2026-66030
- https://www.vulncheck.com/advisories/ekushey-project-manager-crm-stored-xss-via-ticket-title-field

### [CVE-2026-66031](https://codecanyon.net/item/ekushey-project-manager-crm/9492104)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-66031
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-28 04:17:22 JST
- 更新日: 2026-07-28 04:17:22 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Ekushey Project Manager CRMで認証済みクライアントユーザーが返信チケットフィールドに悪意あるスクリプトを保存可能な保存型XSS。
- 影響: スタッフや管理者のブラウザで悪意あるスクリプトが実行される可能性。
- 推奨対応: 入力のサニタイズ強化とアップデートの適用を推奨。

#### References
- https://codecanyon.net/item/ekushey-project-manager-crm/9492104
- https://github.com/aaronamran/CVE-Disclosures/tree/main/CVE-2026/CVE-2026-66031
- https://www.vulncheck.com/advisories/ekushey-project-manager-crm-stored-xss-via-reply-ticket-field

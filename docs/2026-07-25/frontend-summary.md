# Frontend CVE Summary (2026-07-25)

## Overview

- 取得日時: 2026-07-25 08:12:50 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 4
- Critical: 0
- High: 2
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-12496](https://www.loytec.com/support/product-security/advisories/8522-dibt-cve-20260526-0004-unauthenticated-stored-xxs-in-opc-xml-da-server-statistics-high)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-12496
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-25 00:17:08 JST
- 更新日: 2026-07-25 00:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Loytec製品のOPC XML-DAサーバー統計機能におけるStored XSS。認証不要の攻撃者が細工したUser-Agentヘッダーで管理者のブラウザで任意のJavaScriptを実行可能。
- 影響: セッションハイジャック、資格情報窃取、デバイス再設定のリスク。
- 推奨対応: 該当製品のアップデート適用やUser-Agentヘッダーの検証強化を検討。

#### References
- https://www.loytec.com/support/product-security/advisories/8522-dibt-cve-20260526-0004-unauthenticated-stored-xxs-in-opc-xml-da-server-statistics-high

### [CVE-2026-55730](https://www.loytec.com/support/product-security/advisories/8527-dibt-cve-20260601-0002-reflected-cross-site-scripting-xss-high)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-55730
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-25 00:18:31 JST
- 更新日: 2026-07-25 00:18:31 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Loytec LWEB-802のリフレクトXSS。認証不要の攻撃者が細工したリンクのパラメータで被害者のブラウザで任意のJavaScriptを実行可能。
- 影響: 被害者の権限で不正操作が可能となる恐れ。
- 推奨対応: LWEB-802を5.0.8以降に更新し、入力検証を強化すること。

#### References
- https://www.loytec.com/support/product-security/advisories/8527-dibt-cve-20260601-0002-reflected-cross-site-scripting-xss-high

### [CVE-2026-57531](https://github.com/Milkdown/milkdown/commit/db1ae721854a0ab2f188b83cf8695702966640f1)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-57531
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-25 05:18:03 JST
- 更新日: 2026-07-25 05:18:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Milkdownの@milkdown/plugin-emojiにDOMベースのXSS。攻撃者が細工した内容を被害者が貼り付けると任意のJavaScriptが実行される可能性。
- 影響: ホストアプリケーションのオリジンでスクリプトが実行されるリスク。
- 推奨対応: Milkdownを7.21.3以降に更新し、貼り付け処理のサニタイズを強化すること。

#### References
- https://github.com/Milkdown/milkdown/commit/db1ae721854a0ab2f188b83cf8695702966640f1
- https://github.com/Milkdown/milkdown/pull/2410
- https://github.com/Milkdown/milkdown/releases/tag/v7.21.3
- https://www.npmjs.com/package/@milkdown/plugin-emoji
- https://www.vulncheck.com/advisories/milkdown-dom-xss-via-innerhtml-assignment

### [CVE-2026-57530](https://github.com/Milkdown/milkdown/commit/db1ae721854a0ab2f188b83cf8695702966640f1)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-57530
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-25 05:18:02 JST
- 更新日: 2026-07-25 05:18:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Milkdownの@milkdown/preset-commonmarkおよび@milkdown/componentsに保存型XSS。ドキュメント書き込み権限を持つ攻撃者が悪意あるJavaScriptを埋め込み可能。
- 影響: ユーザーがドキュメントを開くかリンクをクリックするとスクリプトが実行される恐れ。
- 推奨対応: Milkdownを7.21.3以降に更新し、URL検証とサニタイズ処理を改善すること。

#### References
- https://github.com/Milkdown/milkdown/commit/db1ae721854a0ab2f188b83cf8695702966640f1
- https://github.com/Milkdown/milkdown/pull/2410
- https://github.com/Milkdown/milkdown/releases/tag/v7.21.3
- https://www.npmjs.com/package/@milkdown/components
- https://www.npmjs.com/package/@milkdown/preset-commonmark

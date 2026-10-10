# Frontend CVE Summary (2026-10-10)

## Overview

- 取得日時: 2026-10-10 10:42:46 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 5
- Critical: 1
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-108096](https://aws.amazon.com/security/security-bulletins/2026-133-aws/)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-108096
- 関連キーワード: npm, graphql, go, aws
- 影響製品: -
- 公開日: 2026-10-10 03:17:06 JST
- 更新日: 2026-10-10 03:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: @aws-amplify/graphql-index-transformer における不適切な認可制御の脆弱性。
- 影響: 認証済みのリモート攻撃者が作成したクエリを通じて、同一アプリケーション内の他ユーザーが所有するレコードを読み取る可能性がある。
- 推奨対応: @aws-amplify/graphql-index-transformer 3.1.2（または関連コンストラクトの修正版）以降にアップデートし、バックエンドを再デプロイする。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-133-aws/
- https://github.com/aws-amplify/amplify-category-api/security/advisories/GHSA-69c4-mvf5-5xm3
- https://www.npmjs.com/package/@aws-amplify/data-construct/v/1.17.4
- https://www.npmjs.com/package/@aws-amplify/graphql-api-construct/v/1.21.4
- https://www.npmjs.com/package/@aws-amplify/graphql-index-transformer/v/3.1.2

### [CVE-2026-108261](https://github.com/tinacms/tinacms/commit/b57dbf4b56201aef15cd92caa49fd12ab96bbecf)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-108261
- 関連キーワード: graphql, gin
- 影響製品: -
- 公開日: 2026-10-10 06:17:04 JST
- 更新日: 2026-10-10 06:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: tinacms および @tinacms/app の管理プレビューにおけるクロスオリジン検証不備の脆弱性。
- 影響: 未認証の攻撃者が誘導用リンクを送信し、ログイン中の編集者に攻撃者制御のオリジンを信頼されたプレビューとして読み込ませることで、GraphQL経由でコンテンツの不法閲覧や改ざんを行う可能性がある。
- 推奨対応: tinacms 3.14.0 および @tinacms/app 2.5.14 以降へアップデートする。

#### References
- https://github.com/tinacms/tinacms/commit/b57dbf4b56201aef15cd92caa49fd12ab96bbecf
- https://github.com/tinacms/tinacms/pull/7522
- https://github.com/tinacms/tinacms/releases/tag/@tinacms/app@2.5.14
- https://github.com/tinacms/tinacms/releases/tag/tinacms@3.14.0
- https://github.com/tinacms/tinacms/security/advisories/GHSA-x34j-47hf-4xg7

### [CVE-2026-108259](https://github.com/tinacms/tinacms/commit/d030d414d39e15de79bf36e4c728d57205e71dde)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-108259
- 関連キーワード: javascript, gin, express
- 影響製品: -
- 公開日: 2026-10-10 06:17:04 JST
- 更新日: 2026-10-10 06:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: @tinacms/cli における Git ブランチ名文字列の未検証挿入（コードインジェクション）の脆弱性。
- 影響: 悪意あるブランチ名が含まれるプレビュービルド実行時、ビルドプロセスの権限で任意コードが実行され、環境変数や資格情報の漏洩、成果物の改ざん等が発生する可能性がある。
- 推奨対応: TinaCMS をバージョン 3.0.0 以降へアップデートする。

#### References
- https://github.com/tinacms/tinacms/commit/d030d414d39e15de79bf36e4c728d57205e71dde
- https://github.com/tinacms/tinacms/pull/7526
- https://github.com/tinacms/tinacms/releases/tag/@tinacms/cli@3.0.0
- https://github.com/tinacms/tinacms/security/advisories/GHSA-pwhx-cvv3-qj5c

### [CVE-2026-104081](https://github.com/kalcaddle/KodExplorer/releases/tag/4.55)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-104081
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-10 00:17:06 JST
- 更新日: 2026-10-10 03:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KodExplorer の解凍処理（unzip_pre_name 関数）におけるパストラバーサルの脆弱性。
- 影響: 認証済み攻撃者が作成された ZIP アーカイブを解凍することで任意ファイルを上書きし、格納型 XSS や PHP ファイルアップロードを経由したリモートコード実行（RCE）につながる可能性がある。
- 推奨対応: KodExplorer をバージョン 4.55 以降にアップデートする。

#### References
- https://github.com/kalcaddle/KodExplorer/releases/tag/4.55
- https://www.vulncheck.com/advisories/kodexplorer-path-traversal-via-unzip-pre-name-zip-extraction

### [CVE-2016-20098](https://github.com/toolbox-team/reddit-moderator-toolbox)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2016-20098
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-10 02:16:38 JST
- 更新日: 2026-10-10 05:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Moderator Toolbox の removalreasons モジュールにおける格納型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: Wiki 編集権限を持つ攻撃者が悪意ある JavaScript を埋め込み、閲覧したモデレーターのセッション権限で意図しない操作を実行させる可能性がある。
- 推奨対応: Moderator Toolbox をバージョン 4.0.14 以降にアップデートする。

#### References
- https://github.com/toolbox-team/reddit-moderator-toolbox
- https://github.com/toolbox-team/reddit-moderator-toolbox/commit/26f45ba21d84cecb92b1a820896ad3bf5254376e
- https://www.vulncheck.com/advisories/moderator-toolbox-before-4.0.14-stored-xss-via-removal-reasons-configuration

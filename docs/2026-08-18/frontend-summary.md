# Frontend CVE Summary (2026-08-18)

## Overview

- 取得日時: 2026-08-18 07:36:00 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 2
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-45790](https://github.com/Dokploy/dokploy/commit/a07106d649991ea09892220873ea3243766c3e08)

> **Frontend** / **HIGH** / CVSS: **8.0** / KEV: **no**

- タイトル: CVE-2026-45790
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-08-18 07:17:14 JST
- 更新日: 2026-08-18 07:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dokployにおける組織メンバー招待およびアカウント作成処理の権限管理不備
- 影響: 権限を持つ攻撃者が所有者（owner）ロールでの招待を行い、組織を永久に乗っ取る可能性があります。
- 推奨対応: Dokployをバージョン 0.29.6 以降に更新してください。

#### References
- https://github.com/Dokploy/dokploy/commit/a07106d649991ea09892220873ea3243766c3e08
- https://github.com/Dokploy/dokploy/pull/4475
- https://github.com/Dokploy/dokploy/releases/tag/v0.29.6
- https://github.com/Dokploy/dokploy/security/advisories/GHSA-fm9p-wmpw-gxjh

### [CVE-2026-44846](https://github.com/jumpserver/jumpserver/commit/1803be11a410eb99cd171d47053b697a119c4a50)

> **Frontend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-44846
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-08-18 06:16:45 JST
- 更新日: 2026-08-18 06:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JumpServerにおけるユーザー招待APIのロール設定ロジックの不備
- 影響: 招待権限を持つユーザーが既存メンバーの権限を上書きし、特権昇格や管理者の権限降格を引き起こす可能性があります。
- 推奨対応: JumpServerをバージョン 4.10.17 以降に更新してください。

#### References
- https://github.com/jumpserver/jumpserver/commit/1803be11a410eb99cd171d47053b697a119c4a50
- https://github.com/jumpserver/jumpserver/pull/16662
- https://github.com/jumpserver/jumpserver/releases/tag/v4.10.17
- https://github.com/jumpserver/jumpserver/security/advisories/GHSA-j836-99w5-523r

### [CVE-2026-55674](https://github.com/discourse/discourse/security/advisories/GHSA-qx4v-rg4v-pm2g)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-55674
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-18 01:16:58 JST
- 更新日: 2026-08-18 01:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Discourseにおけるクッキー処理の不備に起因するクロスサイトスクリプティング（XSS）の脆弱性
- 影響: 未認証の攻撃者がCSPを回避し、訪問者のブラウザ上で任意のJavaScriptを実行させる可能性があります。
- 推奨対応: Discourseを 2026.1.6、2026.5.2、2026.6.1、または 2026.7.0 以降の修正バージョンに更新してください。

#### References
- https://github.com/discourse/discourse/security/advisories/GHSA-qx4v-rg4v-pm2g

### [CVE-2026-19478](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/)

> **Frontend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-19478
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-08-18 05:16:41 JST
- 更新日: 2026-08-18 06:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GitLab CE/EEにおけるGraphQLディレクティブの処理不備
- 影響: 未認証の遠隔攻撃者により、公開プロジェクトやユーザーデータが変更または削除される可能性があります。
- 推奨対応: GitLab CE/EEを 18.11.11、19.0.8、19.1.6、19.2.4 以降の修正バージョンに更新してください。

#### References
- https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/
- https://gitlab.com/gitlab-org/gitlab/-/work_items/611377
- https://hackerone.com/reports/3926431

### [CVE-2026-75531](https://github.com/pandora-analysis/pandora/commit/77a84a039e2079dba7ea0342816c9813099d75d0)

> **Frontend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-75531
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-18 06:16:59 JST
- 更新日: 2026-08-18 06:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PandoraにおけるURLオブザーバブル描画時の格納型クロスサイトスクリプティング（XSS）の脆弱性
- 影響: 被害者が特定の操作を行った際に任意のJavaScriptが実行され、セッション情報漏洩や不正操作が行われる可能性があります。
- 推奨対応: 修正パッチを適用するか、対策が講じられた最新バージョンへ更新してください。

#### References
- https://github.com/pandora-analysis/pandora/commit/77a84a039e2079dba7ea0342816c9813099d75d0

### [CVE-2026-74234](https://legora.com/)

> **Frontend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-74234
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-08-18 05:16:46 JST
- 更新日: 2026-08-18 05:16:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LegoraにおけるMermaidダイアグラム解析時のコード評価不備に起因するクロスサイトスクリプティング（XSS）の脆弱性
- 影響: 悪意のあるダイアグラム描画時に任意のJavaScriptが実行され、特にアドイン環境等でローカルストレージ内のセッショントークンが強奪される可能性があります。
- 推奨対応: Legoraを 2026-08-14 以降の修正バージョンに更新してください。

#### References
- https://legora.com/
- https://www.vulncheck.com/advisories/legora-2026-08-14-xss-via-mermaid-gray-matter-javascript-engine

### [CVE-2026-19650](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-19650
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-08-18 05:16:41 JST
- 更新日: 2026-08-18 06:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GitLab CE/EEのGraphQLマルチプレックスリクエスト処理におけるアクセス制御の不備
- 影響: 未認証の攻撃者がGETリクエスト経由で任意のデータ変更（mutation）を実行できる可能性があります。
- 推奨対応: GitLab CE/EEを 18.11.11、19.0.8、19.1.6、19.2.4 以降の修正バージョンに更新してください。

#### References
- https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/
- https://gitlab.com/gitlab-org/gitlab/-/work_items/612617
- https://hackerone.com/reports/3903669

### [CVE-2026-16046](https://mattermost.com/security-updates)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-16046
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-08-18 00:16:54 JST
- 更新日: 2026-08-18 00:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mattermostにおける終了済みプレイブックに対する実行状態検証の不備
- 影響: 参加者がAPI経由で完了済みプレイブックのチェックリストやレトロスペクティブ等の内容を書き換える可能性があります。
- 推奨対応: Mattermostを 11.7.7 や 10.11.22 など、脆弱性が修正されたバージョンに更新してください。

#### References
- https://mattermost.com/security-updates

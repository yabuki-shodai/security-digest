# Backend CVE Summary (2026-11-01)

## Overview

- 取得日時: 2026-11-01 10:02:41 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 3
- Critical: 0
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-120207](https://github.com/thelia-modules/Page/blob/2.0.3/Controller/Admin/PageImageController.php#L117)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-120207
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-01 03:17:08 JST
- 更新日: 2026-11-01 03:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Thelia Page Module 2.0.4 未満のバックオフィス削除ルートにおける、CSRFトークンおよび権限チェックの欠如によるクロスサイトリクエストフォージェリ（CSRF）の脆弱性。
- 影響: ログイン済みの管理者を細工されたGETリクエストへ誘導することで、ページタグ、ドキュメント、画像などのデータが削除される可能性があります。
- 推奨対応: Thelia Page Module を 2.0.4 以降の修正済みバージョンへアップデートしてください。

#### References
- https://github.com/thelia-modules/Page/blob/2.0.3/Controller/Admin/PageImageController.php#L117
- https://github.com/thelia-modules/Page/commit/e7206a7c35c945cc8fe529fe95a9b30402f0fb60
- https://github.com/thelia/thelia/security/advisories/GHSA-whqr-4v2h-6jhc
- https://www.vulncheck.com/advisories/thelia-page-module-before-2.0.4-csrf-via-page-tag-document-and-image-delete-routes

### [CVE-2026-120202](https://github.com/highflame-ai/ramparts)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-120202
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-11-01 03:17:08 JST
- 更新日: 2026-11-01 03:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highflame ramparts 0.8.1 から 0.8.10 における、ネストされたディレクトリや .pyc ファイルの走査スキップに起因するセキュリティスキャン回避の脆弱性。
- 影響: スキャンを通過した未検証の .pyc ファイルがCPythonでの実行時に読み込まれ、意図しない悪意のあるコードが実行される可能性があります。
- 推奨対応: Highflame ramparts を修正済みバージョンへ更新するか、影響を受けるディレクトリ内のファイルを適切に確認・管理してください。

#### References
- https://github.com/highflame-ai/ramparts
- https://github.com/highflame-ai/ramparts/blob/v0.8.10/src/skills.rs#L898
- https://github.com/highflame-ai/ramparts/issues/154
- https://www.vulncheck.com/advisories/highflame-ramparts-0.8.1-through-0.8.10-skill-bundle-scan-bypass-via-nested-pyc

### [CVE-2026-120203](https://gist.github.com/LioTree/028af150fd991cf9924dd2c7d5912e54)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-120203
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-11-01 03:17:08 JST
- 更新日: 2026-11-01 03:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ShowDoc 2.8.14 以上 3.9.6 未満の Mock 機能における、mockjs テンプレート評価時のコードインジェクションの脆弱性。
- 影響: 認証された攻撃者により、eval() を介して任意のシェルコマンドを実行される可能性があり、公式 Docker 環境等では root 権限で実行される恐れがあります。
- 推奨対応: ShowDoc を 3.9.6 以降へアップデートしてください。

#### References
- https://gist.github.com/LioTree/028af150fd991cf9924dd2c7d5912e54
- https://github.com/star7th/showdoc
- https://github.com/star7th/showdoc/blob/v3.9.5/mock/index.js#L42
- https://github.com/star7th/showdoc/commit/5a2087a3f408f5266f61e9e2fb98845ef4788288
- https://www.vulncheck.com/advisories/showdoc-2.8.14-before-3.9.6-code-injection-via-mock-templates

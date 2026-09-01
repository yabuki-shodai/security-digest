# Frontend CVE Summary (2026-09-01)

## Overview

- 取得日時: 2026-09-01 10:14:49 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 10
- Critical: 0
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-82392](https://github.com/pnpm/pnpm/commit/51300fd41c5e4c8f47635108e373cc3d1f324fa7)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-82392
- 関連キーワード: npm, pnpm
- 影響製品: -
- 公開日: 2026-09-01 06:17:54 JST
- 更新日: 2026-09-01 06:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pnpmにおける `pnpm-lock.yaml` から取得したパッケージ名の検証不備。
- 影響: `pnpm install` 実行時にパッケージの内容が `node_modules` 外に展開され、ビルドスクリプトが許可されている場合に任意コードが実行される可能性があります。
- 推奨対応: pnpm を 10.34.5 または 11.11.0 以降のバージョンに更新してください。

#### References
- https://github.com/pnpm/pnpm/commit/51300fd41c5e4c8f47635108e373cc3d1f324fa7
- https://github.com/pnpm/pnpm/commit/78e29fe5583a1e5d69ea05e414eff310f78d5ed9
- https://github.com/pnpm/pnpm/pull/12872
- https://github.com/pnpm/pnpm/pull/12890
- https://github.com/pnpm/pnpm/releases/tag/v10.34.5

### [CVE-2026-82393](https://github.com/pnpm/pnpm/commit/51300fd41c5e4c8f47635108e373cc3d1f324fa7)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-82393
- 関連キーワード: npm, pnpm
- 影響製品: -
- 公開日: 2026-09-01 07:17:22 JST
- 更新日: 2026-09-01 07:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pnpmにおけるスコープ付きパッケージ名に対するパス移動（Path Traversal）の検証不備。
- 影響: `pnpm install` 実行時に `node_modules` 外の任意のファイルを上書きされ、任意コードが実行される可能性があります。
- 推奨対応: pnpm を 10.34.5 または 11.11.0 以降のバージョンに更新してください。

#### References
- https://github.com/pnpm/pnpm/commit/51300fd41c5e4c8f47635108e373cc3d1f324fa7
- https://github.com/pnpm/pnpm/commit/78e29fe5583a1e5d69ea05e414eff310f78d5ed9
- https://github.com/pnpm/pnpm/pull/12872
- https://github.com/pnpm/pnpm/pull/12890
- https://github.com/pnpm/pnpm/releases/tag/v10.34.5

### [CVE-2026-81891](https://github.com/Studio-42/elFinder/commit/191372c1bbebbd36fb55af79a84b9984861390ff)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-81891
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-01 06:17:52 JST
- 更新日: 2026-09-01 06:17:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: elFinderにおけるアーカイブ解凍時のMIMEタイプ検証回避の不備。
- 影響: アップロード制限を回避してPHPファイルが解凍・配置され、リモートで任意コードが実行される可能性があります。
- 推奨対応: elFinder を 2.1.70 以降のバージョンに更新してください。

#### References
- https://github.com/Studio-42/elFinder/commit/191372c1bbebbd36fb55af79a84b9984861390ff
- https://github.com/Studio-42/elFinder/commit/dd73e702820c146a192969800ee674ecdb208365
- https://github.com/Studio-42/elFinder/releases/tag/2.1.70
- https://github.com/Studio-42/elFinder/security/advisories/GHSA-gxmj-r5rf-ggwq

### [CVE-2026-81889](https://github.com/Studio-42/elFinder/commit/191372c1bbebbd36fb55af79a84b9984861390ff)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-81889
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-01 06:17:52 JST
- 更新日: 2026-09-01 06:17:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: elFinderのURLアップロード処理におけるDNSリバインディングを利用したSSRF脆弱性。
- 影響: 内部ネットワーク上のリソースの取得やレスポンスの閲覧、意図しないリクエスト送信が行われる可能性があります。
- 推奨対応: elFinder を 2.1.70 以降のバージョンに更新してください。

#### References
- https://github.com/Studio-42/elFinder/commit/191372c1bbebbd36fb55af79a84b9984861390ff
- https://github.com/Studio-42/elFinder/commit/6d997386cd0f1abab4706c220b46b0aea0ecff51
- https://github.com/Studio-42/elFinder/releases/tag/2.1.70
- https://github.com/Studio-42/elFinder/security/advisories/GHSA-8x3q-jpjh-qh5c

### [CVE-2026-81890](https://github.com/Studio-42/elFinder/commit/31284facd033e081b2b69c08873b39c8a413b762)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-81890
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-01 06:17:52 JST
- 更新日: 2026-09-01 06:17:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: elFinderの `netmount` コマンドにおけるCSRFトークン検証の欠落。
- 影響: クロスサイトリクエストを通じて攻撃者指定のFTPマウントが被害者のセッションに登録される可能性があります。
- 推奨対応: elFinder を 2.1.70 以降のバージョンに更新してください。

#### References
- https://github.com/Studio-42/elFinder/commit/31284facd033e081b2b69c08873b39c8a413b762
- https://github.com/Studio-42/elFinder/commit/36d40fff12222ad4c229d8889d8ed3fd3dbf0415
- https://github.com/Studio-42/elFinder/releases/tag/2.1.70
- https://github.com/Studio-42/elFinder/security/advisories/GHSA-9hjf-w35w-6vx2

### [CVE-2026-82396](https://github.com/sulu/sulu/commit/d061094f5b7bb1d5e974544fce30bede9c7adf8e)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-82396
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-01 07:17:22 JST
- 更新日: 2026-09-01 07:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Suluのメディアダウンロードエンドポイントにおけるスクリプト可能MIMEタイプの処理不備。
- 影響: アップロードされたHTMLやXML等のファイルが同一オリジンで表示され、閲覧したユーザーのセッション下で格納型XSSが実行される可能性があります。
- 推奨対応: Sulu を 2.6.25 または 3.0.8 以降のバージョンに更新してください。

#### References
- https://github.com/sulu/sulu/commit/d061094f5b7bb1d5e974544fce30bede9c7adf8e
- https://github.com/sulu/sulu/releases/tag/2.6.25
- https://github.com/sulu/sulu/releases/tag/3.0.8
- https://github.com/sulu/sulu/security/advisories/GHSA-pp4x-ccxq-6r33

### [CVE-2026-82835](https://drive.google.com/file/d/1TsEsDvwPsN6tfcc1VgN1YRSEE9yVY1pK/view?usp=drive_link)

> **Frontend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-82835
- 関連キーワード: vue, django, go
- 影響製品: -
- 公開日: 2026-09-01 05:17:15 JST
- 更新日: 2026-09-01 05:56:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: caoqianming django-vue-admin 1.0の `/api/file/` エンドポイントにおける不適切なアクセス制御。
- 影響: 遠隔の攻撃者により制限された機能へ不正アクセスされる可能性があります。
- 推奨対応: 利用を控えるか、適切なアクセス制限の設定および開発者による修正を確認してください。

#### References
- https://drive.google.com/file/d/1TsEsDvwPsN6tfcc1VgN1YRSEE9yVY1pK/view?usp=drive_link
- https://vuldb.com/cve/CVE-2026-82835
- https://vuldb.com/submit/876660
- https://vuldb.com/vuln/397247
- https://vuldb.com/vuln/397247/cti

### [CVE-2025-63607](https://gist.github.com/7Horrus/7c419516b064f6bac638736819e24583)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2025-63607
- 関連キーワード: javascript, echo
- 影響製品: -
- 公開日: 2026-09-01 06:17:06 JST
- 更新日: 2026-09-01 06:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TechStore 1.0の `contact_display` における `id` パラメータの無検証出力による反射型XSS脆弱性。
- 影響: 被害者のブラウザ上で攻撃者が挿入した任意のJavaScriptを実行される可能性があります。
- 推奨対応: 出力時のエスケープ処理を実装するか、修正版の適用を検討してください。

#### References
- https://gist.github.com/7Horrus/7c419516b064f6bac638736819e24583

### [CVE-2026-51153](https://gist.github.com/kurokoleung/9fc51b02c85c2f466bf4ea72c62ba343)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-51153
- 関連キーワード: javascript, python
- 影響製品: -
- 公開日: 2026-09-01 01:18:34 JST
- 更新日: 2026-09-01 05:59:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: QDにおけるタスクログ出力処理のエスケープ不備に起因する格納型XSS脆弱性。
- 影響: HARテンプレートを介して挿入された悪意のあるスクリプトが、タスク実行時に被害者のブラウザ上で実行される可能性があります。
- 推奨対応: 修正されたバージョンに更新するか、出力時の適切なエンコード処理を適用してください。

#### References
- https://gist.github.com/kurokoleung/9fc51b02c85c2f466bf4ea72c62ba343
- https://qd-today.github.io/qd/

### [CVE-2026-81887](https://github.com/livewire/livewire/commit/11ebe646f7e81dde2d714815da8b3019d058561e)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-81887
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-01 06:17:52 JST
- 更新日: 2026-09-01 06:17:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Livewireのクエリ文字列パーサーにおけるプロトタイプ汚染に起因するXSS脆弱性。
- 影響: 操作されたURLをユーザーが開くことで、アプリケーションのオリジン上で任意のJavaScriptが実行される可能性があります。
- 推奨対応: Livewire を 3.8.3 または 4.3.4 以降のバージョンに更新してください。

#### References
- https://github.com/livewire/livewire/commit/11ebe646f7e81dde2d714815da8b3019d058561e
- https://github.com/livewire/livewire/pull/10467
- https://github.com/livewire/livewire/releases/tag/v3.8.3
- https://github.com/livewire/livewire/releases/tag/v4.3.4
- https://github.com/livewire/livewire/security/advisories/GHSA-g3hc-697w-wm82

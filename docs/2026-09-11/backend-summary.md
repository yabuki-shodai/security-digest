# Backend CVE Summary (2026-09-11)

## Overview

- 取得日時: 2026-09-11 09:04:03 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 20
- Critical: 3
- High: 16
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-88007](https://github.com/traefik/traefik/commit/ff39c47d7459dec9cd8de63c1a4e7aa7315bdc1c)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-88007
- 関連キーワード: go, traefik
- 影響製品: -
- 公開日: 2026-09-11 00:17:56 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TraefikのHTTP/3有効時におけるConnContextの処理不備により、接続に紐づく認証（NTLM/Negotiate等）においてバックエンドトランスポートが正しく分離されない問題。
- 影響: 無関係な第三者が被害者の認証済みバックエンド接続を再利用し、認証情報なしで被害者向けデータの閲覧や成りすましを行う可能性があります。
- 推奨対応: Traefik 2.11.57 または 3.7.13 以降への更新が推奨されます。

#### References
- https://github.com/traefik/traefik/commit/ff39c47d7459dec9cd8de63c1a4e7aa7315bdc1c
- https://github.com/traefik/traefik/pull/13812
- https://github.com/traefik/traefik/releases/tag/v2.11.57
- https://github.com/traefik/traefik/releases/tag/v3.7.13
- https://github.com/traefik/traefik/security/advisories/GHSA-qqjf-53cj-pwvv

### [CVE-2026-88018](https://github.com/rclone/rclone/commit/90595f34f27f569be6b27c57fe5ab65057d323bd)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-88018
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-11 01:18:08 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: rcloneの `serve s3` コマンドにおいて `--auth-proxy` 設定時に `--auth-key` が未設定の場合、空のシークレットでSigV4署名が検証されてしまう問題。
- 影響: 未認証のネットワーク上の攻撃者が任意のアクセスキーと空のシークレットを用いて署名し、バックエンドへアクセスできる可能性があります。
- 推奨対応: rclone 1.75.1 以降への更新が推奨されます。

#### References
- https://github.com/rclone/rclone/commit/90595f34f27f569be6b27c57fe5ab65057d323bd
- https://github.com/rclone/rclone/releases/tag/v1.75.1
- https://github.com/rclone/rclone/security/advisories/GHSA-xwwr-4h3p-r22c
- https://github.com/rclone/rclone/security/advisories/GHSA-xwwr-4h3p-r22c

### [CVE-2026-88044](https://github.com/rclone/rclone/commit/739403963abf6f58003c2becd5f7c4ad0d644153)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-88044
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-11 02:17:08 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: rcloneのRC（Remote Control）インターフェース（serve/start）において、S3およびFTPコンストラクタがリクエストローカルの認証プロキシ設定ではなくグローバル設定を参照してしまう問題。
- 影響: リクエストローカルの認証プロキシが無視され、匿名アクセス等の固定ファイルシステムへ意図せずフォールバックする可能性があります。
- 推奨対応: rclone 1.75.1 以降への更新が推奨されます。

#### References
- https://github.com/rclone/rclone/commit/739403963abf6f58003c2becd5f7c4ad0d644153
- https://github.com/rclone/rclone/releases/tag/v1.75.1
- https://github.com/rclone/rclone/security/advisories/GHSA-p569-5gjg-9cmj
- https://github.com/rclone/rclone/security/advisories/GHSA-p569-5gjg-9cmj

### [CVE-2026-88009](https://github.com/traefik/traefik/commit/58d1e9ca204526823211e30fd4634101c59d58e9)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-88009
- 関連キーワード: go, gin, traefik
- 影響製品: -
- 公開日: 2026-09-11 01:18:07 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TraefikにおけるルートレスHTTP/1リクエストターゲットの処理不備により、内部的なパス検証・認可処理とバックエンドへ転送されるパス表現との間に乖離が生じる問題。
- 影響: 仮想ホスト間のルーティング迂回、パス単位の認可回避、アクセスログの記録回避などが引き起こされる可能性があります。
- 推奨対応: Traefik 2.11.57 または 3.7.13 以降への更新が推奨されます。

#### References
- https://github.com/traefik/traefik/commit/58d1e9ca204526823211e30fd4634101c59d58e9
- https://github.com/traefik/traefik/pull/13796
- https://github.com/traefik/traefik/releases/tag/v2.11.57
- https://github.com/traefik/traefik/releases/tag/v3.7.13
- https://github.com/traefik/traefik/security/advisories/GHSA-f52w-8j3h-j724

### [CVE-2026-88026](https://jira.mongodb.org/browse/CSHARP-6177)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-88026
- 関連キーワード: go, gin, express, mongodb
- 影響製品: -
- 公開日: 2026-09-11 03:18:12 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB C# DriverのLINQクエリ変換機能における正規表現メタ文字の不適切な中和処理。
- 影響: 認証済みユーザーにより生成される正規表現フィルタが改変され、意図しない範囲のレコードが取得される可能性があります。
- 推奨対応: 修正されたバージョンへの更新、または入力データの適切なサニタイズを検討してください。

#### References
- https://jira.mongodb.org/browse/CSHARP-6177

### [CVE-2026-88011](https://github.com/traefik/traefik/commit/0331801c72329e0eaeb850e53ccce87c57fbecf8)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-88011
- 関連キーワード: go, gin, nginx, traefik
- 影響製品: -
- 公開日: 2026-09-11 01:18:07 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Traefikにおけるドット区切りヘッダーの不適切な処理により、アンダースコアへ変換を行うバックエンド（CGI、WSGI、PHP、NGINX等）との間でヘッダー名の認識の乖離が生じる問題。
- 影響: Traefikが設定したアイデンティティヘッダーがクライアント提供の値で上書きされ、成りすましが行われる可能性があります。
- 推奨対応: Traefik 2.11.56 または 3.7.12 以降への更新、および aliasHeadersStrategy を delete や reject に設定することが推奨されます。

#### References
- https://github.com/traefik/traefik/commit/0331801c72329e0eaeb850e53ccce87c57fbecf8
- https://github.com/traefik/traefik/pull/13720
- https://github.com/traefik/traefik/releases/tag/v2.11.56
- https://github.com/traefik/traefik/releases/tag/v3.7.12
- https://github.com/traefik/traefik/security/advisories/GHSA-rf44-j88r-hh8c

### [CVE-2026-88029](https://jira.mongodb.org/browse/PYTHON-5994)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-88029
- 関連キーワード: python, go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 03:18:13 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Python DriverのGridFSコンポーネントにおいて、特殊要素の中和処理が不十分であり、ファイル識別子が検索条件（クエリ）として解釈される問題。
- 影響: 認証済みユーザーにより、意図しないファイル内容の閲覧、GridFSバケット内の全ファイルデータの削除、または意図しないファイルのリネームが行われる可能性があります。
- 推奨対応: 修正されたバージョンへの更新、または入力データの検証を行ってください。

#### References
- https://jira.mongodb.org/browse/PYTHON-5994

### [CVE-2026-89011](https://github.com/isomorphic-git/isomorphic-git/commit/b3db111885230bac9a648e0a2312c65ca66f76eb)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-89011
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-11 05:17:31 JST
- 更新日: 2026-09-11 05:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: isomorphic-gitの `getRemoteInfo` 関数におけるプロトタイプ汚染の脆弱性。リファレンス交渉中に `__proto__` を含むリファレンス名を受信することで発生します。
- 影響: 悪意のあるGitサーバーへ接続した際、後続のネットワーク処理が攻撃者のプロキシを経由するよう改ざんされ、認証情報が窃取される可能性があります。
- 推奨対応: isomorphic-git 1.42.0 以降への更新が推奨されます。

#### References
- https://github.com/isomorphic-git/isomorphic-git/commit/b3db111885230bac9a648e0a2312c65ca66f76eb
- https://github.com/isomorphic-git/isomorphic-git/pull/2426
- https://github.com/isomorphic-git/isomorphic-git/releases/tag/v1.42.0
- https://github.com/isomorphic-git/isomorphic-git/security/advisories/GHSA-83vg-jxvh-fx76
- https://www.vulncheck.com/advisories/isomorphic-git-prototype-pollution-via-getremoteinfo

### [CVE-2026-88017](https://github.com/rclone/rclone/commit/c6af0b57c2b4af848bc968c2b407354476184b99)

> **Backend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-88017
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-11 01:18:08 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: rclone (1.64.0〜1.75.0) のFTP auth-proxyにおける資格情報管理の不備。パスワードがセッションではなくサーバー全体で保持される問題が存在します。
- 影響: 同名ユーザーによる別セッションのログイン時に認証情報が上書きされ、先行セッションから他者のバックエンド権限でオブジェクトの読み書き・削除が行われる可能性があります。
- 推奨対応: rcloneをバージョン1.75.1以降にアップデートしてください。

#### References
- https://github.com/rclone/rclone/commit/c6af0b57c2b4af848bc968c2b407354476184b99
- https://github.com/rclone/rclone/releases/tag/v1.75.1
- https://github.com/rclone/rclone/security/advisories/GHSA-c476-6w5q-jw77

### [CVE-2026-88022](https://jira.mongodb.org/browse/PHPLARA-260)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-88022
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 03:18:12 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB integration for Laravelにおいて、等価フィルタに渡された配列がリテラル値ではなくクエリ演算子条件として解釈される問題。
- 影響: 攻撃者が演算子構造を持つ配列を処理させることで、意図しないドキュメントの取得や削除が行われる可能性があります。
- 推奨対応: 修正されたバージョンへの更新、または該当APIへ渡す入力の検証を行ってください。

#### References
- https://jira.mongodb.org/browse/PHPLARA-260

### [CVE-2026-88023](https://jira.mongodb.org/browse/PHPLIB-1929)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-88023
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 03:18:12 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB PHP LibraryのGridFSコンポーネントにおいて、特殊要素の中和処理が不十分であり、ファイル識別子が検索条件（クエリ）として解釈される問題。
- 影響: 認証済みユーザーにより、意図しないファイル内容の閲覧、GridFSバケット内の全ファイルデータの削除、または意図しないファイルのリネームが行われる可能性があります。
- 推奨対応: 修正されたバージョンへの更新、または入力データの検証を行ってください。

#### References
- https://jira.mongodb.org/browse/PHPLIB-1929

### [CVE-2026-88024](https://jira.mongodb.org/browse/RUST-2469)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-88024
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 03:18:12 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Rust DriverのGridFSコンポーネントにおけるクエリロジックの不適切な中和処理の脆弱性。ファイル識別子がクエリ条件として誤解釈される可能性があります。
- 影響: 認証されたユーザーにより、意図しないファイルの閲覧や、バケット内の全ファイルチャンク削除によるデータ閲覧不能を引き起こされる可能性があります。
- 推奨対応: MongoDB Rust Driverを修正済みの最新バージョンへ更新してください。

#### References
- https://jira.mongodb.org/browse/RUST-2469

### [CVE-2026-88025](https://jira.mongodb.org/browse/CSHARP-6190)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-88025
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 03:18:12 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB C# DriverのGridFSコンポーネントにおけるクエリロジックの不適切な中和処理の脆弱性。ファイル識別子がクエリ条件として誤解釈される可能性があります。
- 影響: 認証されたユーザーにより、意図しないファイルの閲覧、全ファイルチャンク削除、または対象外ファイルのリネームを引き起こされる可能性があります。
- 推奨対応: MongoDB C# Driverを修正済みの最新バージョンへ更新してください。

#### References
- https://jira.mongodb.org/browse/CSHARP-6190

### [CVE-2026-88027](https://jira.mongodb.org/browse/PHPLARA-265)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-88027
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 03:18:13 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Laravel向けMongoDB統合パッケージにおける埋め込みドキュメント処理のクエリ不適切処理の脆弱性。レコード識別子がクエリ条件として誤解釈される可能性があります。
- 影響: 認証されたユーザーにより、埋め込みドキュメントの全削除や意図しないドキュメントの上書きが行われる可能性があります。
- 推奨対応: MongoDB Integration for Laravelパッケージを修正済みバージョンに更新してください。

#### References
- https://jira.mongodb.org/browse/PHPLARA-265

### [CVE-2026-88028](https://jira.mongodb.org/browse/PHPLARA-265)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-88028
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 03:18:13 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Laravel向けMongoDB統合パッケージにおけるポリモーフィック関連処理のクエリ不適切処理の脆弱性。リレーション識別子がクエリ条件として誤解釈される可能性があります。
- 影響: 認証されたユーザーにより、アプリケーションが意図しない対象のドキュメントを返却させられる可能性があります。
- 推奨対応: MongoDB Integration for Laravelパッケージを修正済みバージョンに更新してください。

#### References
- https://jira.mongodb.org/browse/PHPLARA-265

### [CVE-2026-88030](https://jira.mongodb.org/browse/RUBY-3941)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-88030
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 03:18:13 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Ruby DriverのGridFSコンポーネントにおけるクエリロジックの不適切な中和処理の脆弱性。ファイル識別子がクエリ条件として誤解釈される可能性があります。
- 影響: 認証されたユーザーにより、意図しないファイルの閲覧や、バケット内の全ファイルチャンク削除を引き起こされる可能性があります。
- 推奨対応: MongoDB Ruby Driverを修正済みの最新バージョンへ更新してください。

#### References
- https://jira.mongodb.org/browse/RUBY-3941

### [CVE-2026-88031](https://jira.mongodb.org/browse/GODRIVER-4081)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-88031
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 03:18:13 JST
- 更新日: 2026-09-11 04:54:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Go DriverのGridFSコンポーネントにおけるクエリロジックの不適切な中和処理の脆弱性。ファイル識別子がクエリ条件として誤解釈される可能性があります。
- 影響: 認証されたユーザーにより、バケット内のすべてのGridFSファイルチャンクが削除され、保存データの読み取りが不能になる可能性があります。
- 推奨対応: MongoDB Go Driverを修正済みの最新バージョンへ更新してください。

#### References
- https://jira.mongodb.org/browse/GODRIVER-4081

### [CVE-2026-88033](https://jira.mongodb.org/browse/JAVA-6283)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-88033
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 04:17:40 JST
- 更新日: 2026-09-11 04:44:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB Java DriverのGridFSコンポーネントにおけるクエリロジックの不適切な中和処理の脆弱性。ファイル識別子がクエリ条件として誤解釈される可能性があります。
- 影響: 認証されたユーザーにより、意図しないファイルの閲覧、全ファイルチャンク削除、または対象外ファイルのリネームを引き起こされる可能性があります。
- 推奨対応: MongoDB Java Driverを修正済みの最新バージョンへ更新してください。

#### References
- https://jira.mongodb.org/browse/JAVA-6283

### [CVE-2026-88034](https://jira.mongodb.org/browse/CXX-3556)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-88034
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 04:17:40 JST
- 更新日: 2026-09-11 04:44:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB C++ DriverのGridFSコンポーネントにおけるクエリロジックの不適切な中和処理の脆弱性。ファイル識別子がクエリ条件として誤解釈される可能性があります。
- 影響: 認証されたユーザーにより、意図しないファイルの閲覧や、バケット内の全ファイルチャンク削除を引き起こされる可能性があります。
- 推奨対応: MongoDB C++ Driverを修正済みの最新バージョンへ更新してください。

#### References
- https://jira.mongodb.org/browse/CXX-3556

### [CVE-2026-88036](https://jira.mongodb.org/browse/CDRIVER-6427)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-88036
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-09-11 04:17:41 JST
- 更新日: 2026-09-11 04:44:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB C DriverのGridFSコンポーネントにおけるクエリロジックの不適切な中和処理の脆弱性。ファイル識別子がクエリ条件として誤解釈される可能性があります。
- 影響: 認証されたユーザーにより、意図しないファイルの閲覧や、バケット内の全ファイルチャンク削除を引き起こされる可能性があります。
- 推奨対応: MongoDB C Driverを修正済みの最新バージョンへ更新してください。

#### References
- https://jira.mongodb.org/browse/CDRIVER-6427

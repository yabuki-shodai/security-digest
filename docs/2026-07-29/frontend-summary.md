# Frontend CVE Summary (2026-07-29)

## Overview

- 取得日時: 2026-07-29 08:17:41 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 12
- Critical: 2
- High: 9
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-54658](https://github.com/hypequery/hypequery/blob/main/packages/clickhouse/CHANGELOG.md#202)

> **Frontend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-54658
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-07-29 08:17:08 JST
- 更新日: 2026-07-29 08:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: HypequeryのescapeValue()関数がシングルクォート前のバックスラッシュを適切にエスケープせず、SQLインジェクションを引き起こす可能性がある。
- 影響: 攻撃者が細工したクエリパラメータを用いて任意のSQLを実行できる可能性がある。
- 推奨対応: バージョン2.0.2以降にアップデートすること。

#### References
- https://github.com/hypequery/hypequery/blob/main/packages/clickhouse/CHANGELOG.md#202
- https://github.com/hypequery/hypequery/commit/4dfa9d77d70a08b970e722268b75ca7d13db0bdf
- https://github.com/hypequery/hypequery/releases/tag/@hypequery/clickhouse@2.0.2
- https://github.com/hypequery/hypequery/security/advisories/GHSA-6wcc-39rp-hh9p

### [CVE-2026-67174](https://github.com/Pivotick/Pivotick/commit/67c597cdf7f6910f97a4c73905a7b845e0d039f1)

> **Frontend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-67174
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-29 00:17:51 JST
- 更新日: 2026-07-29 01:20:18 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PivotickのUI要素解決およびアイコンレンダリングでDOMベースのXSS脆弱性が存在する可能性がある。
- 影響: 攻撃者が細工したグラフやプロパティ、SVGアイコンを用いて任意のスクリプトを実行できる可能性がある。
- 推奨対応: 信頼できないデータの取り扱いに注意し、可能な限りサニタイズを行うこと。

#### References
- https://github.com/Pivotick/Pivotick/commit/67c597cdf7f6910f97a4c73905a7b845e0d039f1

### [CVE-2026-54653](https://github.com/koxudaxi/datamodel-code-generator/commit/17fc235e234cbcfaaadef8c74cb72c9687db0d1d)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-54653
- 関連キーワード: graphql, python, express
- 影響製品: -
- 公開日: 2026-07-29 07:17:40 JST
- 更新日: 2026-07-29 07:17:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: datamodel-code-generatorが攻撃者制御のdefault_factory値を保持し、生成モデルのインポート時にPythonコードが実行される可能性がある。
- 影響: 悪意あるコードが生成モデルのインポート時に実行されるリスクがある。
- 推奨対応: バージョン0.60.2以降にアップデートすること。

#### References
- https://github.com/koxudaxi/datamodel-code-generator/commit/17fc235e234cbcfaaadef8c74cb72c9687db0d1d
- https://github.com/koxudaxi/datamodel-code-generator/releases/tag/0.60.2
- https://github.com/koxudaxi/datamodel-code-generator/security/advisories/GHSA-386q-5hp3-95m9

### [CVE-2026-16771](https://kb.cert.org/vuls/id/141367)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-16771
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-29 04:17:32 JST
- 更新日: 2026-07-29 05:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Arris BGW210-700ゲートウェイの管理エンドポイントでサーバー側認証が欠如し、クライアント側の制御のみで保護されている。
- 影響: LAN内の未認証攻撃者が設定情報の閲覧や変更、診断操作を実行できる可能性がある。
- 推奨対応: ファームウェアのアップデートや管理アクセス制御の強化を検討すること。

#### References
- https://kb.cert.org/vuls/id/141367
- https://www.kb.cert.org/vuls/id/141367

### [CVE-2026-54621](https://github.com/koxudaxi/datamodel-code-generator/commit/aec47bc414779f4a9992b3919c8f7663afd6c988)

> **Frontend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-54621
- 関連キーワード: graphql, python
- 影響製品: -
- 公開日: 2026-07-29 07:17:39 JST
- 更新日: 2026-07-29 07:17:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: datamodel-code-generatorがGraphQL Unionの説明に含まれる改行を適切に無害化せず、生成モデルにPythonコード注入が可能。
- 影響: 攻撃者制御のスキーマ内容により生成モデルのインポート時に任意コードが実行される可能性がある。
- 推奨対応: バージョン0.60.1以降にアップデートすること。

#### References
- https://github.com/koxudaxi/datamodel-code-generator/commit/aec47bc414779f4a9992b3919c8f7663afd6c988
- https://github.com/koxudaxi/datamodel-code-generator/releases/tag/0.60.1
- https://github.com/koxudaxi/datamodel-code-generator/security/advisories/GHSA-j884-q54q-mmx3

### [CVE-2026-54656](https://github.com/koxudaxi/datamodel-code-generator/commit/a43d02906111a2fdcaf13ee5b62eb2da85376f19)

> **Frontend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-54656
- 関連キーワード: graphql, python
- 影響製品: -
- 公開日: 2026-07-29 07:17:40 JST
- 更新日: 2026-07-29 07:17:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: datamodel-code-generatorが--extra-template-dataからのバリデータを安全に検証せず、生成Pydantic v2モデルでコード実行が可能。
- 影響: 生成モデルのインポート時に悪意あるPythonコードが実行されるリスクがある。
- 推奨対応: バージョン0.60.2以降にアップデートすること。

#### References
- https://github.com/koxudaxi/datamodel-code-generator/commit/a43d02906111a2fdcaf13ee5b62eb2da85376f19
- https://github.com/koxudaxi/datamodel-code-generator/releases/tag/0.60.2
- https://github.com/koxudaxi/datamodel-code-generator/security/advisories/GHSA-8m8r-38jm-f355

### [CVE-2026-55415](https://github.com/koxudaxi/datamodel-code-generator/commit/577d49569c2254c371a97e495020ae2238a73b84)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-55415
- 関連キーワード: graphql, python
- 影響製品: -
- 公開日: 2026-07-29 07:17:48 JST
- 更新日: 2026-07-29 07:17:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: datamodel-code-generatorが攻撃者制御のスキーマ拡張で改行を利用し、インポート文からのコード実行を許す可能性がある。
- 影響: 生成モデルのインポート時に任意のPythonコードが実行されるリスクがある。
- 推奨対応: バージョン0.64.0以降にアップデートすること。

#### References
- https://github.com/koxudaxi/datamodel-code-generator/commit/577d49569c2254c371a97e495020ae2238a73b84
- https://github.com/koxudaxi/datamodel-code-generator/releases/tag/0.64.0
- https://github.com/koxudaxi/datamodel-code-generator/security/advisories/GHSA-5578-w22f-pfx9

### [CVE-2026-54545](https://github.com/pionxzh/wakaru/commit/1d30383b20a6f768786b8ada2f1b0945de13c316)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-54545
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-29 01:18:59 JST
- 更新日: 2026-07-29 01:18:59 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: wakaruの@wakaru/cli 1.4.0未満で、ファイル名のサニタイズが不十分でパス・トラバーサルが可能。
- 影響: 悪意あるバンドル実行時に出力ディレクトリ外へのファイル書き込みや環境次第でコード実行の可能性。
- 推奨対応: @wakaru/cliを1.4.0以降に更新すること。

#### References
- https://github.com/pionxzh/wakaru/commit/1d30383b20a6f768786b8ada2f1b0945de13c316
- https://github.com/pionxzh/wakaru/releases/tag/v1.4.0
- https://github.com/pionxzh/wakaru/security/advisories/GHSA-7wpj-vvmv-pgm8

### [CVE-2026-54690](https://github.com/koxudaxi/datamodel-code-generator/commit/5fdba4a09f2d7a9996a504975b7ef7d63e3715bb)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-54690
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-07-29 07:17:40 JST
- 更新日: 2026-07-29 07:17:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: datamodel-code-generatorが攻撃者制御のHTTP/HTTPS $refを無警告で参照し、SSRFを引き起こす可能性がある。
- 影響: 外部サーバーへの不正なリクエスト送信が可能となるリスクがある。
- 推奨対応: バージョン0.61.0以降にアップデートすること。

#### References
- https://github.com/koxudaxi/datamodel-code-generator/commit/5fdba4a09f2d7a9996a504975b7ef7d63e3715bb
- https://github.com/koxudaxi/datamodel-code-generator/releases/tag/0.61.0
- https://github.com/koxudaxi/datamodel-code-generator/security/advisories/GHSA-954p-556p-r752

### [CVE-2026-55389](https://github.com/koxudaxi/datamodel-code-generator/commit/2ff4a72b4550a2b2069754c5b075b1655067e5fb)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-55389
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-07-29 07:17:48 JST
- 更新日: 2026-07-29 07:17:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: datamodel-code-generatorがローカルファイル参照の制限を適切に行わず、任意のローカルファイル読み取りが可能となる可能性がある。
- 影響: 攻撃者がローカルファイルの内容を読み取れるリスクがある。
- 推奨対応: バージョン0.62.0以降にアップデートすること。

#### References
- https://github.com/koxudaxi/datamodel-code-generator/commit/2ff4a72b4550a2b2069754c5b075b1655067e5fb
- https://github.com/koxudaxi/datamodel-code-generator/releases/tag/0.62.0
- https://github.com/koxudaxi/datamodel-code-generator/security/advisories/GHSA-8359-h9fx-j6v9

### [CVE-2026-55391](https://github.com/koxudaxi/datamodel-code-generator/commit/25c8b7e497419eb20b230fa3318c04f9bebc5a6f)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-55391
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-07-29 07:17:48 JST
- 更新日: 2026-07-29 07:17:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: datamodel-code-generatorがDNSリバインディングを利用されallow_private_network=Falseを回避され、内部サービスへのアクセスを許す可能性がある。
- 影響: 内部ネットワーク上のサービスに不正アクセスされるリスクがある。
- 推奨対応: バージョン0.63.0以降にアップデートすること。

#### References
- https://github.com/koxudaxi/datamodel-code-generator/commit/25c8b7e497419eb20b230fa3318c04f9bebc5a6f
- https://github.com/koxudaxi/datamodel-code-generator/releases/tag/0.63.0
- https://github.com/koxudaxi/datamodel-code-generator/security/advisories/GHSA-vx7x-vcc2-c44g

### [CVE-2026-7775](https://www.ibm.com/support/pages/node/7280847)

> **Frontend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-7775
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-29 01:20:21 JST
- 更新日: 2026-07-29 02:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: IBM Sterling製品におけるストアドXSS脆弱性で、特権ユーザーがWeb UIに任意のJavaScriptを埋め込める。
- 影響: 信頼されたセッション内で認証情報漏洩などのリスクがある。
- 推奨対応: 製品のアップデートや適切な入力検証を行うこと。

#### References
- https://www.ibm.com/support/pages/node/7280847

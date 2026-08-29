# Frontend CVE Summary (2026-08-29)

## Overview

- 取得日時: 2026-08-29 12:41:04 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 3
- High: 1
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-55378](https://github.com/js-recon/js-recon/commit/447876c4bfa9ec5bc98cbc65d7a3e5f889412491)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-55378
- 関連キーワード: javascript, github actions
- 影響製品: -
- 公開日: 2026-08-29 05:18:27 JST
- 更新日: 2026-08-29 05:18:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JS ReconのGitHub Actionsワークフロー（PR Branch Checker）において、信頼できないブランチ名やリポジトリ名がシェルコマンドに展開される。
- 影響: 外部からのプルリクエストを通じてGitHub Actionsランナー上で任意コマンドを実行され、権限を持つGITHUB_TOKENが不当に使用される可能性がある。
- 推奨対応: JS Reconをバージョン1.3.1-beta.2以降に更新する。

#### References
- https://github.com/js-recon/js-recon/commit/447876c4bfa9ec5bc98cbc65d7a3e5f889412491
- https://github.com/js-recon/js-recon/pull/121
- https://github.com/js-recon/js-recon/releases/tag/v1.3.1-beta.2
- https://github.com/js-recon/js-recon/security/advisories/GHSA-w9cj-mg3x-qjm4

### [CVE-2026-55634](https://github.com/advisories/GHSA-r2f4-ff2p-xc64)

> **Frontend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-55634
- 関連キーワード: esbuild, gin
- 影響製品: -
- 公開日: 2026-08-29 05:18:29 JST
- 更新日: 2026-08-29 07:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Pimcoreのクラス定義インポート処理においてフィールド名の検証が不足しており、コード生成時およびSQLステートメントへのインジェクションが可能。
- 影響: 認証されたユーザーにより生成クラスへ任意のPHPコードやSQL識別子が挿入され、コード実行やデータベース操作が行われる可能性がある。
- 推奨対応: Pimcoreをバージョン11.5.19、12.3.10、2026.1.6以降に更新する。

#### References
- https://github.com/advisories/GHSA-r2f4-ff2p-xc64
- https://github.com/pimcore/pimcore/commit/a4f8c3cfee58b7d5fe4873d67782eff58dae9b9d
- https://github.com/pimcore/pimcore/pull/19183
- https://github.com/pimcore/pimcore/releases/tag/v2026.1.6
- https://github.com/pimcore/pimcore/security/advisories/GHSA-9x44-4gxf-8c25

### [CVE-2026-55248](https://github.com/plone/plone.app.portlets/commit/09da52ef7b297daa8e0cfd2361e47c37d9b073ad)

> **Frontend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-55248
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-29 05:18:27 JST
- 更新日: 2026-08-29 07:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: plone.app.portletsのRSSポートレット処理において、フィードURLやレスポンスの検証・制限が不十分。
- 影響: 過大なデータ取得によるメモリ枯渇（DoS）、内部ネットワークへのSSRF探査、悪意あるJavaScript URLによるXSS実行の恐れがある。
- 推奨対応: plone.app.portletsをバージョン5.0.8、6.0.4、7.0.2以降に更新する。

#### References
- https://github.com/plone/plone.app.portlets/commit/09da52ef7b297daa8e0cfd2361e47c37d9b073ad
- https://github.com/plone/plone.app.portlets/commit/9f16b6fb10211916686c6c346ea174bf517e3fbd
- https://github.com/plone/plone.app.portlets/commit/a3b2c2887165b308cd915cbb87b8276f90a76680
- https://github.com/plone/plone.app.portlets/commit/df5e256baee55083cbd6b9a2623675d4cb26b6cd
- https://github.com/plone/plone.app.portlets/security/advisories/GHSA-x5g3-w747-2h8q

### [CVE-2026-82291](https://github.com/heyform/heyform)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-82291
- 関連キーワード: graphql, gin
- 影響製品: -
- 公開日: 2026-08-29 05:20:20 JST
- 更新日: 2026-08-29 05:20:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HeyFormにおいて、CORSレスポンスでリクエストのOriginをそのまま許可しつつ認証情報の共有（credentials）を有効にしている設定不備が存在する。
- 影響: 悪意ある外部ページを閲覧したログイン中ユーザーのコンテキストで、GraphQLクエリを通じたデータ閲覧や設定改ざんが行われる可能性がある。
- 推奨対応: HeyFormをバージョン3.0.0-rc.8以降に更新する。

#### References
- https://github.com/heyform/heyform
- https://github.com/heyform/heyform/blob/v3.0.0-rc.7/packages/server/src/main.ts
- https://github.com/heyform/heyform/commit/bf9d738ca70ae5641c0c7372982b00365c5144d4
- https://github.com/heyform/heyform/security/advisories/GHSA-fg7j-rmgr-rc9g
- https://www.vulncheck.com/advisories/heyform-reflects-any-origin-in-cors-responses-while-allowing-credentials

### [CVE-2026-55834](https://github.com/pocket-id/pocket-id/commit/8a7577497131229badb35cb4b3a4227b1300afff)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-55834
- 関連キーワード: javascript, svelte, gin
- 影響製品: -
- 公開日: 2026-08-29 05:18:30 JST
- 更新日: 2026-08-29 07:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Pocket IDのフロントエンドにおいて、静的認証が完了しない際のリダイレクト処理でバックエンドの許可リスト検証が行われていない。
- 影響: 未認証の攻撃者により犠牲者のブラウザが任意のHTTP/HTTPSオリジンへリダイレクトされ、フィッシング等の標的とされる可能性がある。
- 推奨対応: Pocket IDをバージョン2.9.0以降に更新する。

#### References
- https://github.com/pocket-id/pocket-id/commit/8a7577497131229badb35cb4b3a4227b1300afff
- https://github.com/pocket-id/pocket-id/releases/tag/v2.9.0
- https://github.com/pocket-id/pocket-id/security/advisories/GHSA-2wvm-8mvp-22qv
- https://github.com/pocket-id/pocket-id/security/advisories/GHSA-2wvm-8mvp-22qv

### [CVE-2026-38725](https://gist.github.com/mug33nn/050d6f99c2e0965fbf7d71fe8ba4f527)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-38725
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-29 01:17:47 JST
- 更新日: 2026-08-29 05:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PrestaShop向けxipblogモジュールにおいて、ajax.phpのパラメータに対するサニタイズ不足により格納型XSSが存在する。
- 影響: 管理者がバックオフィスでコメントを閲覧した際に管理者権限でスクリプトが実行され、ショップ全体が乗っ取られる恐れがある。
- 推奨対応: xipblogモジュールを修正済みの最新バージョンに更新する。

#### References
- https://gist.github.com/mug33nn/050d6f99c2e0965fbf7d71fe8ba4f527
- https://github.com/xpert-idea/xipblog
- https://gist.github.com/mug33nn/050d6f99c2e0965fbf7d71fe8ba4f527

### [CVE-2026-55549](https://github.com/yamcs/yamcs/commit/4d47d5cdcf5d92c2c5bbbc19feada422923332e3)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-55549
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-29 05:18:28 JST
- 更新日: 2026-08-29 05:18:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Yamcsの認可エンドポイントにおいて、redirect_uriパラメータのHTMLエスケープが不十分なため反射型XSSが発生する。
- 影響: 誘導されたユーザーのブラウザ上でJavaScriptが実行され、認証情報の奪取やアカウントの乗っ取りにつながる恐れがある。
- 推奨対応: Yamcsをバージョン5.9.4以降に更新する。

#### References
- https://github.com/yamcs/yamcs/commit/4d47d5cdcf5d92c2c5bbbc19feada422923332e3
- https://github.com/yamcs/yamcs/releases/tag/yamcs-5.9.4
- https://github.com/yamcs/yamcs/security/advisories/GHSA-rxpg-wjf8-qv9c

### [CVE-2026-55566](https://github.com/yamcs/yamcs/commit/8e18e279d8ce761c21f4f67bbd06a1bff804d297)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-55566
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-29 05:18:29 JST
- 更新日: 2026-08-29 07:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Yamcsの/extルート処理において、プラグインIDの検証なしにinnerHTMLへ描画するためXSSが発生する。
- 影響: 細工されたURLを開いたユーザーの権限で任意のJavaScriptが実行され、情報の閲覧や不正操作が行われる恐れがある。
- 推奨対応: Yamcsをバージョン5.12.8または5.13.2以降に更新する。

#### References
- https://github.com/yamcs/yamcs/commit/8e18e279d8ce761c21f4f67bbd06a1bff804d297
- https://github.com/yamcs/yamcs/commit/ecf34a4e2ccbe085e6ceff0253595b24d5ecb4aa
- https://github.com/yamcs/yamcs/releases/tag/yamcs-5.12.8
- https://github.com/yamcs/yamcs/releases/tag/yamcs-5.13.2
- https://github.com/yamcs/yamcs/security/advisories/GHSA-9272-wg2r-7xmx

### [CVE-2026-50980](http://osbil.com)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-50980
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-29 05:18:03 JST
- 更新日: 2026-08-29 05:18:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: oPanelのDNSルックアップ/管理コンポーネントにおいて、悪意あるDNS TXTレコードの処理に起因するXSS脆弱性が存在する。
- 影響: 任意JavaScriptの実行やセッションハイジャックが行われる可能性がある。
- 推奨対応: oPanelをバージョンv1.20.25以降に更新する。

#### References
- http://osbil.com
- http://womopanel.com
- https://github.com/bugresearch/CVE-2026-50980

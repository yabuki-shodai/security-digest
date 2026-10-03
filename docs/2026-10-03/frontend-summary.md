# Frontend CVE Summary (2026-10-03)

## Overview

- 取得日時: 2026-10-03 10:07:04 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 22
- Critical: 2
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-94483](https://github.com/vercel/next.js/commit/e002ad68bd676bb0ed0c87bb22e3590304763e0b)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-94483
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-10-03 01:16:51 JST
- 更新日: 2026-10-03 02:55:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Next.js is a React framework for building full-stack web applications. From 16.0.0 until 16.3.8, Image Optimization can follow attacker-controlled DNS resolution for a remote URL that matches images.remotePatterns, allowing the optimized image fetch to reach private IP addresses after the URL passes the allow-list chec...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vercel/next.js/commit/e002ad68bd676bb0ed0c87bb22e3590304763e0b
- https://github.com/vercel/next.js/releases/tag/v16.3.8
- https://github.com/vercel/next.js/security/advisories/GHSA-cjq9-62q9-8jv4

### [CVE-2026-94484](https://github.com/vercel/next.js/commit/52c94abdd2ea5f416f5e8353ea8a2edd3fe311b8)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-94484
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-10-03 01:16:51 JST
- 更新日: 2026-10-03 02:55:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Next.js is a React framework for building full-stack web applications. From 15.0.0 until 15.5.27 and 16.3.8, applications with a root-level catch-all page and statically generated or Incremental Static Regeneration routes can use a shared response cache key that is insufficiently scoped to the source route. A single un...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vercel/next.js/commit/52c94abdd2ea5f416f5e8353ea8a2edd3fe311b8
- https://github.com/vercel/next.js/commit/719e4c67d6e92df60246f95e1d96e2dd60789a52
- https://github.com/vercel/next.js/releases/tag/v15.5.27
- https://github.com/vercel/next.js/releases/tag/v16.3.8
- https://github.com/vercel/next.js/security/advisories/GHSA-mcj8-r9mp-w47p

### [CVE-2026-94485](https://github.com/vercel/next.js/commit/2d9f50a409312696145b82b3157aadb6b1fef476)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-94485
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-10-03 01:16:51 JST
- 更新日: 2026-10-03 02:55:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Next.js is a React framework for building full-stack web applications. From 16.0.0 until 16.3.8, the `next dev` development server exposes a Model Context Protocol endpoint without reliably restricting cross-site requests. A malicious website visited by a developer can reach the endpoint and read the project's disk loc...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vercel/next.js/commit/2d9f50a409312696145b82b3157aadb6b1fef476
- https://github.com/vercel/next.js/releases/tag/v16.3.8
- https://github.com/vercel/next.js/security/advisories/GHSA-f87g-xv8r-7p7x

### [CVE-2026-94543](https://github.com/vercel/next.js/commit/52c94abdd2ea5f416f5e8353ea8a2edd3fe311b8)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-94543
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-10-03 01:16:52 JST
- 更新日: 2026-10-03 02:55:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Next.js is a React framework for building full-stack web applications. From 15.0.0 until 15.5.27 and 16.3.8, self-hosted applications using the Pages Router with statically generated or Incremental Static Regeneration pages can key a response cache entry without sufficiently binding it to the source route. A request ca...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vercel/next.js/commit/52c94abdd2ea5f416f5e8353ea8a2edd3fe311b8
- https://github.com/vercel/next.js/commit/719e4c67d6e92df60246f95e1d96e2dd60789a52
- https://github.com/vercel/next.js/releases/tag/v15.5.27
- https://github.com/vercel/next.js/releases/tag/v16.3.8
- https://github.com/vercel/next.js/security/advisories/GHSA-4jqv-mc3x-m676

### [CVE-2026-94486](https://github.com/vercel/next.js/commit/2d9f50a409312696145b82b3157aadb6b1fef476)

> **Frontend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-94486
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-10-03 01:16:51 JST
- 更新日: 2026-10-03 02:55:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Next.js is a React framework for building full-stack web applications. From 16.0.0 until 16.3.8, the next dev development server exposes a Model Context Protocol endpoint without reliably restricting cross-site requests. A malicious website visited by a developer can reach the endpoint and read the project's disk locat...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vercel/next.js/commit/2d9f50a409312696145b82b3157aadb6b1fef476
- https://github.com/vercel/next.js/releases/tag/v16.3.8
- https://github.com/vercel/next.js/security/advisories/GHSA-39w2-rjm5-chcv

### [CVE-2026-94544](https://github.com/vercel/next.js/commit/bd9214f9a32854a011bf5fe58e481dffe1bbf598)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-94544
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-10-03 01:16:52 JST
- 更新日: 2026-10-03 02:55:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Next.js is a React framework for building full-stack web applications. From 16.3.0 until 16.3.8, pending use cache fills for the same key are shared without separating Draft Mode requests from regular requests. An overlapping regular request can receive unauthenticated unpublished content from an editor's Draft Mode fi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vercel/next.js/commit/bd9214f9a32854a011bf5fe58e481dffe1bbf598
- https://github.com/vercel/next.js/releases/tag/v16.3.8
- https://github.com/vercel/next.js/security/advisories/GHSA-3w37-wq28-93x7

### [CVE-2026-104854](https://github.com/nrwl/nx/commit/3298fd8b2dd066167eb3cc0410643994a59b0bba)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-104854
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-10-03 02:17:04 JST
- 更新日: 2026-10-03 03:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nx is a monorepo solution for TypeScript and polyglot codebases. From 14.6.0 until 22.7.9 and 23.1.2, Nx creates Unix domain sockets for its daemon and isolated plugin workers in shared temporary locations without owner-only directory and socket permissions. Another unprivileged local account on a shared build server,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nrwl/nx/commit/3298fd8b2dd066167eb3cc0410643994a59b0bba
- https://github.com/nrwl/nx/commit/63e1abb287a3d69f8ba981828a1de325d0d3dc68
- https://github.com/nrwl/nx/commit/71c2253b6aac23b008e192c4e2642c42a5e07545
- https://github.com/nrwl/nx/pull/36370
- https://github.com/nrwl/nx/releases/tag/22.7.9

### [CVE-2026-104859](https://github.com/nrwl/nx/commit/6d60eed061f050e0d5af509a1f5a07c707f09865)

> **Frontend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-104859
- 関連キーワード: typescript, docker
- 影響製品: -
- 公開日: 2026-10-03 03:17:02 JST
- 更新日: 2026-10-03 03:44:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nx is a monorepo solution for TypeScript and polyglot codebases. From 21.4.0 until 22.7.8 and from 23.0.0 until 23.1.1, the @nx/docker release pipeline builds docker tag, image lookup, and docker push invocations as shell command strings. The release.docker.repositoryName and registryUrl configuration values are interp...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nrwl/nx/commit/6d60eed061f050e0d5af509a1f5a07c707f09865
- https://github.com/nrwl/nx/commit/b587441fd8da28c5db37edb0826554e0060dc81b
- https://github.com/nrwl/nx/pull/36505
- https://github.com/nrwl/nx/security/advisories/GHSA-6vc5-vf29-ffr2

### [CVE-2026-104853](https://github.com/nrwl/nx/commit/38cd82a0c05e8212e538bdb87ccb198d6504e58f)

> **Frontend** / **MEDIUM** / CVSS: **5.8** / KEV: **no**

- タイトル: CVE-2026-104853
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-10-03 02:17:03 JST
- 更新日: 2026-10-03 03:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nx is a monorepo solution for TypeScript and polyglot codebases. From 13.10.0 until 22.7.10 and 23.2.1, Nx migration planning reads the nx-migrations.migrations value from a target package manifest without validating that it is a contained relative path. A hostile direct dependency or a package introduced through a tru...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nrwl/nx/commit/38cd82a0c05e8212e538bdb87ccb198d6504e58f
- https://github.com/nrwl/nx/commit/95474ab457e8e1dbdbefad29040c166105a8fb90
- https://github.com/nrwl/nx/commit/de37c5ebd1852fac700d70726326236ac398af3f
- https://github.com/nrwl/nx/pull/36887
- https://github.com/nrwl/nx/releases/tag/22.7.10

### [CVE-2026-104848](https://github.com/tinylibs/tinypool/commit/24df4e730e7d0857a6d226c9b58f8924227404fd)

> **Frontend** / **CRITICAL** / CVSS: **9.5** / KEV: **no**

- タイトル: CVE-2026-104848
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-10-03 02:17:03 JST
- 更新日: 2026-10-03 03:33:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tinypool is a minimal Node.js worker thread pool implementation. Prior to 2.1.1, Tinypool constructs ThreadPool.options from a normal options object and reads the execArgv and env worker options in dist/index.js, allowing values inherited from a polluted Object.prototype to be copied into own properties and passed to w...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/tinylibs/tinypool/commit/24df4e730e7d0857a6d226c9b58f8924227404fd
- https://github.com/tinylibs/tinypool/pull/134
- https://github.com/tinylibs/tinypool/releases/tag/v2.1.1
- https://github.com/tinylibs/tinypool/security/advisories/GHSA-5gmw-xhrv-c9v3
- https://github.com/tinylibs/tinypool/security/advisories/GHSA-5gmw-xhrv-c9v3

### [CVE-2026-104849](https://github.com/tinylibs/tinypool/commit/f41411a3e23324c674f35a19a3240f7a7c40ffbf)

> **Frontend** / **CRITICAL** / CVSS: **9.5** / KEV: **no**

- タイトル: CVE-2026-104849
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-10-03 02:17:03 JST
- 更新日: 2026-10-03 03:33:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tinypool 2.1.2未満において、pool.run()に渡されるoptionsオブジェクトの自プロパティチェックが不十分なため、プロトタイプ汚染の影響を受ける脆弱性。
- 影響: 事前にプロトタイプが汚染されている場合、攻撃者が指定したJavaScriptモジュールの読み込みを誘発され、ホストプロセスの権限でタスクデータの参照や改ざんが行われる可能性があります。
- 推奨対応: Tinypool をバージョン 2.1.2 以降に更新してください。

#### References
- https://github.com/tinylibs/tinypool/commit/f41411a3e23324c674f35a19a3240f7a7c40ffbf
- https://github.com/tinylibs/tinypool/pull/135
- https://github.com/tinylibs/tinypool/releases/tag/v2.1.2
- https://github.com/tinylibs/tinypool/security/advisories/GHSA-85c8-ppgw-ccpr

### [CVE-2026-102626](https://fluidattacks.com/advisories/golden)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-102626
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-03 03:16:59 JST
- 更新日: 2026-10-03 04:16:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LimeSurvey Community Edition 7.4.0において、Date/Time質問のdate_min属性値をインラインJavaScriptに埋め込む際のコンテキストエンコードが不十分な脆弱性。
- 影響: アンケート作成権限を持つ認証済みユーザーにより不審な値が設定された場合、該当質問を閲覧した別ユーザーのブラウザ上でJavaScriptが実行される可能性があります。
- 推奨対応: 信頼できないユーザーへのアンケート作成権限の制限を検討し、修正バージョンが提供されている場合はアップデートを適用してください。

#### References
- https://fluidattacks.com/advisories/golden
- https://github.com/LimeSurvey/LimeSurvey/
- https://github.com/LimeSurvey/LimeSurvey/commit/32e54f14f0b4ddc2d8144daaabf7e23c3bbfb8e8

### [CVE-2026-104847](https://github.com/ProseMirror/prosemirror-view/commit/20dc0a911a79f8fc6640dbbea5e7d68d3c4784b7)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-104847
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-03 01:16:47 JST
- 更新日: 2026-10-03 03:44:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ProseMirrorのprosemirror-view 1.42.3未満におけるペースト処理において、HTMLのクリップボードスライスコンテキストに含まれる属性の検証が不十分な脆弱性。
- 影響: 悪意あるHTMLをユーザーがエディタにペーストした際、ブラウザ内で攻撃者制御のJavaScriptが実行される可能性があります。
- 推奨対応: prosemirror-view をバージョン 1.42.3 以降に更新してください。

#### References
- https://github.com/ProseMirror/prosemirror-view/commit/20dc0a911a79f8fc6640dbbea5e7d68d3c4784b7
- https://github.com/ProseMirror/prosemirror-view/commit/2e91a612bbc1248e55b4f6061fc93fe459f977c1
- https://github.com/ProseMirror/prosemirror-view/security/advisories/GHSA-c8x8-7fp4-3x9w
- https://github.com/ProseMirror/prosemirror-view/security/advisories/GHSA-c8x8-7fp4-3x9w
- https://github.com/ProseMirror/prosemirror-view/security/advisories/GHSA-c8x8-7fp4-3x9w

### [CVE-2026-104872](https://github.com/open-telemetry/opentelemetry-js-contrib/commit/27e172a9e0d549559056ccd58f27d13467454156)

> **Frontend** / **MEDIUM** / CVSS: **5.8** / KEV: **no**

- タイトル: CVE-2026-104872
- 関連キーワード: javascript, go, mysql
- 影響製品: -
- 公開日: 2026-10-03 05:17:01 JST
- 更新日: 2026-10-03 05:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenTelemetry JavaScript Contribのデータベース計装パッケージにおいて、DB接続のユーザー名をdb.userスパン属性としてデフォルトで全操作に付与してしまう問題。
- 影響: オブザーバビリティのバックエンドに意図せずデータベースアカウント名が送信され、サービス構成や環境情報が露出する可能性があります。
- 推奨対応: 影響を受ける各計装パッケージ（@opentelemetry/instrumentation-*）を修正済みバージョンへ更新してください。

#### References
- https://github.com/open-telemetry/opentelemetry-js-contrib/commit/27e172a9e0d549559056ccd58f27d13467454156
- https://github.com/open-telemetry/opentelemetry-js-contrib/commit/5b7dd0e102e940d653e04b08b5a1b721a8271037
- https://github.com/open-telemetry/opentelemetry-js-contrib/pull/3585
- https://github.com/open-telemetry/opentelemetry-js-contrib/security/advisories/GHSA-qqmp-wf37-98f9

### [CVE-2026-104900](https://github.com/MISP/MISP/commit/2a2981a27)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-104900
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-03 01:16:47 JST
- 更新日: 2026-10-03 02:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MISPのリモートイベントプレビュー表示において、カウントフィールドの値がHTMLエンコードされずにレンダリングされる蓄積型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 連携されたリモートサーバー上のイベントを介して、プレビューを閲覧したローカルユーザーのセッション内で任意スクリプトが実行される可能性があります。
- 推奨対応: MISPを修正済みバージョンへ更新してください。

#### References
- https://github.com/MISP/MISP/commit/2a2981a27

### [CVE-2026-104901](https://github.com/MISP/MISP/commit/bd5e80c84)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-104901
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-03 01:16:47 JST
- 更新日: 2026-10-03 02:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MISP 2.5.48未満のID Translator機能において、連携リモートサーバーから返されるイベントIDの出力エンコードが不十分なクロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 悪意あるリモートサーバーから返却されたイベントIDにより、ID Translatorページを閲覧したユーザーのブラウザで任意スクリプトが実行され、セッションハイジャック等に繋がる可能性があります。
- 推奨対応: MISP をバージョン 2.5.48 以降に更新してください。

#### References
- https://github.com/MISP/MISP/commit/bd5e80c84

### [CVE-2026-104906](https://github.com/MISP/MISP/commit/1bed4ca0c)

> **Frontend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-104906
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-03 01:16:48 JST
- 更新日: 2026-10-03 02:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MISPのTAXIIオブジェクトビューアにおいて、リモートTAXIIオブジェクトの文字列プロパティをHTMLエンコードせずに表示するクロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 悪意あるTAXIIオブジェクトを閲覧した認証済みユーザーのセッション内で任意のJavaScriptが実行され、セッション情報やAPIキーなどが窃取される可能性があります。
- 推奨対応: MISPを修正済みバージョンへ更新してください。

#### References
- https://github.com/MISP/MISP/commit/1bed4ca0c

### [CVE-2026-104907](https://github.com/MISP/MISP/commit/70ad174dd)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-104907
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-03 01:16:48 JST
- 更新日: 2026-10-03 02:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MISPのリモートイベントプレビューページにおいて、タグIDがJavaScriptのonclick属性内で適切にサニタイズされていないクロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 悪意あるタグIDを含むイベントの該当要素とユーザーがインタラクションした際、JavaScriptの文字列リテラルを抜け出して任意スクリプトが実行される可能性があります。
- 推奨対応: MISPを修正済みバージョンへ更新してください。

#### References
- https://github.com/MISP/MISP/commit/70ad174dd

### [CVE-2026-103918](https://github.com/middleapi/orpc/commit/26314dfb443237c495116c5794d3d30a7a22c570)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-103918
- 関連キーワード: zod, gin
- 影響製品: -
- 公開日: 2026-10-03 05:17:00 JST
- 更新日: 2026-10-03 05:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: oRPCの@orpc/zod（1.14.10未満）において、プロパティ収集時にプロトタイプチェーンを参照するため、__proto__などの入力によるプロトタイプ操作が可能な脆弱性。
- 影響: リクエストを介してプロトタイプ値の置換や、バリデーション前の未処理TypeErrorを誘発され、該当リクエストの処理が失敗する可能性があります。
- 推奨対応: oRPC（@orpc/zod）をバージョン 1.14.10 以降に更新してください。

#### References
- https://github.com/middleapi/orpc/commit/26314dfb443237c495116c5794d3d30a7a22c570
- https://github.com/middleapi/orpc/pull/1727
- https://github.com/middleapi/orpc/releases/tag/v1.14.10
- https://github.com/middleapi/orpc/security/advisories/GHSA-gcgf-fh7c-8gf2

### [CVE-2026-104479](https://github.com/mindstellar/shopclass)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-104479
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-03 09:16:36 JST
- 更新日: 2026-10-03 09:16:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Shopclass before 6.2.0 contains a stored cross-site scripting vulnerability that allows self-registered non-admin users to inject scripts into item listing descriptions when frontend TinyMCE is enabled. Attackers can submit malicious JavaScript, which ItemActions.php saves without tag stripping, causing it to execute i...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mindstellar/shopclass
- https://github.com/mindstellar/shopclass/commit/c196f70906522c9b9172c24f1b42cd0a02357422
- https://www.vulncheck.com/advisories/shopclass-before-6.2.0-stored-xss-via-listing-description-field

### [CVE-2026-104871](https://github.com/angular/angular-cli/commit/645e41a47d21b7651837a4250de99af0509626e2)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-104871
- 関連キーワード: angular, gin
- 影響製品: -
- 公開日: 2026-10-03 05:17:00 JST
- 更新日: 2026-10-03 06:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Windows環境下のAngular SSRにおいて、事前レンダリングページ取得時にバックスラッシュを含む相対URLのパス検証が不十分となる脆弱性。
- 影響: 未認証の第三者により、ディレクトリ名のプレフィックスを共有する近隣ディレクトリ内の事前レンダリングHTMLページが取得される可能性があります。
- 推奨対応: 使用中のプロジェクトに応じて、@angular/ssr 関連パッケージを修正済みバージョン（20.3.36, 21.2.23, 22.1.7など）に更新してください。

#### References
- https://github.com/angular/angular-cli/commit/645e41a47d21b7651837a4250de99af0509626e2
- https://github.com/angular/angular-cli/commit/70748ca8e76fe4b42798719410336119d943e755
- https://github.com/angular/angular-cli/commit/bb72145f9ab45aee29f523236b3a25cd0813a841
- https://github.com/angular/angular-cli/commit/c3e5982e49705f0f6a913cb94622b4c555d2d914
- https://github.com/angular/angular-cli/releases/tag/v20.3.36

### [CVE-2026-104475](https://github.com/idurar/idurar-erp-crm)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-104475
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-03 09:16:35 JST
- 更新日: 2026-10-03 09:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IDURAR ERP CRM through 4.1.1 contains a stored cross-site scripting vulnerability that allows authenticated users to inject scripts by uploading unsanitized SVG files. Attackers can upload JavaScript-laden SVGs via the profile update or settings upload endpoints, which execute in victims' browsers when served from the...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/idurar/idurar-erp-crm
- https://github.com/idurar/idurar-erp-crm/blob/4.1.1/backend/src/middlewares/uploadMiddleware/utils/fileFilterMiddleware.js
- https://github.com/idurar/idurar-erp-crm/issues/1414
- https://www.vulncheck.com/advisories/idurar-erp-crm-through-4.1.1-stored-xss-via-svg-upload

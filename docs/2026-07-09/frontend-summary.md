# Frontend CVE Summary (2026-07-09)

## Overview

- 取得日時: 2026-07-09 08:20:57 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 27
- Critical: 1
- High: 10
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-56669](https://gist.github.com/jviide/ea040eabe7bac058326174e2cd42dfd9)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-56669
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-07-09 06:16:50 JST
- 更新日: 2026-07-09 06:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Elysiaフレームワークの1.4.29未満のバージョンで、multipart/form-dataの処理時にCPU負荷が二次的に増加し、CPU枯渇を引き起こす可能性があります。  
- 影響: 大量のユニークなキー・バリューペアを含むリクエストでCPUリソースが過剰に消費され、サービス拒否状態になる恐れがあります。  
- 推奨対応: バージョン1.4.29以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://gist.github.com/jviide/ea040eabe7bac058326174e2cd42dfd9
- https://github.com/elysiajs/elysia/commit/8358ff9efbcedf9534995f5977f26b9ceab59329
- https://github.com/elysiajs/elysia/releases/tag/1.4.29
- https://github.com/elysiajs/elysia/security/advisories/GHSA-9643-4qgh-g8mx

### [CVE-2026-55849](https://github.com/CycloneDX/cyclonedx-node-npm/commit/9f646253f4263d8644dadb86e5597fad996f688f)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-55849
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-07-09 07:17:15 JST
- 更新日: 2026-07-09 07:17:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: @cyclonedx/cyclonedx-npmの2.1.0から5.0.0未満のバージョンで、--workspace引数が適切にサニタイズされず任意のOSコマンドが実行される可能性があります。  
- 影響: ユーザー権限で任意のOSコマンドが実行されるため、システムの不正操作や情報漏洩のリスクがあります。  
- 推奨対応: バージョン5.0.0以降にアップデートし、npm_execpathが未設定の場合のコマンド実行を回避してください。

#### References
- https://github.com/CycloneDX/cyclonedx-node-npm/commit/9f646253f4263d8644dadb86e5597fad996f688f
- https://github.com/CycloneDX/cyclonedx-node-npm/pull/1476
- https://github.com/CycloneDX/cyclonedx-node-npm/releases/tag/v5.0.0
- https://github.com/CycloneDX/cyclonedx-node-npm/security/advisories/GHSA-v75r-vx73-82pj

### [CVE-2026-54527](https://github.com/jupyterlab/jupyterlab-git/commit/c6d37b88f36aa59aee317930b95e427fb9d6b09b)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-54527
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 06:16:49 JST
- 更新日: 2026-07-09 06:16:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: JupyterLab Gitの0.30.0b3から0.54.0未満のバージョンで、リネームされたファイル名をinnerHTMLに直接渡す脆弱性により、悪意あるファイル名でJavaScriptが実行される可能性があります。  
- 影響: 攻撃者が細工したファイル名を用いて、被害者のGit履歴表示時に任意のスクリプトを実行できるリモートコード実行のリスクがあります。  
- 推奨対応: バージョン0.54.0以降にアップデートし、脆弱性の修正を適用することを推奨します。

#### References
- https://github.com/jupyterlab/jupyterlab-git/commit/c6d37b88f36aa59aee317930b95e427fb9d6b09b
- https://github.com/jupyterlab/jupyterlab-git/releases/tag/v0.54.0
- https://github.com/jupyterlab/jupyterlab-git/security/advisories/GHSA-f962-v9hr-pfg5

### [CVE-2026-55596](https://github.com/udecode/plate/commit/6214914ca811adf22d0ad503154494216eed68ba)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-55596
- 関連キーワード: javascript, shadcn/ui
- 影響製品: -
- 公開日: 2026-07-09 06:16:50 JST
- 更新日: 2026-07-09 06:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Plateの53.0.0から53.1.4までのバージョンで、メディア埋め込み機能が不正なjavascript: iframeソースを検証せずにレンダリングしてしまう脆弱性が存在します。  
- 影響: 攻撃者が細工したドキュメントを通じて、悪意のあるiframeを埋め込み、ユーザーの環境で任意のスクリプトを実行される可能性があります。  
- 推奨対応: 53.1.4以降のバージョンにアップデートし、メディアURLのプロトコル検証が適切に行われるようにしてください。

#### References
- https://github.com/udecode/plate/commit/6214914ca811adf22d0ad503154494216eed68ba
- https://github.com/udecode/plate/pull/5014
- https://github.com/udecode/plate/releases/tag/v53.1.4
- https://github.com/udecode/plate/security/advisories/GHSA-qj6x-xx2h-8hvv

### [CVE-2026-59892](https://github.com/open-telemetry/opentelemetry-js/commit/b1c196d49d54caae59741cca0a9d57d101d7ea88)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59892
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-07-09 02:17:27 JST
- 更新日: 2026-07-09 05:16:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenTelemetry JavaScriptの@opentelemetry/propagator-jaegerが、decodeURIComponent()のエラー処理を適切に行わず、不正なパーセントエンコード値によりNode.jsプロセスが異常終了する可能性があります。  
- 影響: 認証されていないリモート攻撃者が細工したHTTPヘッダーを送信することで、サービスの停止（DoS）を引き起こす恐れがあります。  
- 推奨対応: バージョン2.9.0以降にアップデートし、修正済みの@opentelemetry/propagator-jaegerを使用してください。

#### References
- https://github.com/open-telemetry/opentelemetry-js/commit/b1c196d49d54caae59741cca0a9d57d101d7ea88
- https://github.com/open-telemetry/opentelemetry-js/releases/tag/v2.9.0
- https://github.com/open-telemetry/opentelemetry-js/security/advisories/GHSA-45rx-2jwx-cxfr
- https://github.com/open-telemetry/opentelemetry-js/security/advisories/GHSA-45rx-2jwx-cxfr

### [CVE-2026-49866](https://github.com/libp2p/js-libp2p/commit/773dd80ded24dbd6b19e675c89fd2f3b45f2d899)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-49866
- 関連キーワード: javascript, go, node.js
- 影響製品: -
- 公開日: 2026-07-09 06:16:49 JST
- 更新日: 2026-07-09 06:16:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: libp2pのJavaScript実装で、16.0.0以前のバージョンにおいて、無制限のIHAVEおよびIWANTメッセージID配列が同期的に大量処理され、Node.jsのイベントループをブロックする問題があります。  
- 影響: 大量のメッセージID処理によりNode.jsアプリケーションが応答不能になる可能性があります。  
- 推奨対応: libp2pをバージョン16.0.0以降にアップデートして問題を解消してください。

#### References
- https://github.com/libp2p/js-libp2p/commit/773dd80ded24dbd6b19e675c89fd2f3b45f2d899
- https://github.com/libp2p/js-libp2p/pull/3520
- https://github.com/libp2p/js-libp2p/releases/tag/gossipsub-v16.0.0
- https://github.com/libp2p/js-libp2p/security/advisories/GHSA-cwc9-cp4j-mcvv

### [CVE-2026-59923](https://github.com/lepture/mistune/commit/c7101fcbb6e8790e8e39157c5ca2238fc6dd6cbc)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-59923
- 関連キーワード: javascript, python, gin
- 影響製品: -
- 公開日: 2026-07-09 02:17:27 JST
- 更新日: 2026-07-09 02:17:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: MistuneのHTMLRenderer.safe_url()がパーセントエンコードされたjavascript URIを適切にブロックせず、悪意あるMarkdownリンクや画像を通じてスクリプトが実行される可能性があります。  
- 影響: 攻撃者が細工したMarkdownを用いてクロスサイトスクリプティング（XSS）攻撃を仕掛けるリスクがあります。  
- 推奨対応: Mistuneをバージョン3.3.0以降にアップデートし、修正済みの安全なURL処理を利用してください。

#### References
- https://github.com/lepture/mistune/commit/c7101fcbb6e8790e8e39157c5ca2238fc6dd6cbc
- https://github.com/lepture/mistune/releases/tag/v3.3.0
- https://github.com/lepture/mistune/security/advisories/GHSA-8c25-4j27-2rv3
- https://github.com/lepture/mistune/security/advisories/GHSA-8c25-4j27-2rv3

### [CVE-2026-59929](https://github.com/lepture/mistune/commit/c7101fcbb6e8790e8e39157c5ca2238fc6dd6cbc)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-59929
- 関連キーワード: javascript, python, gin
- 影響製品: -
- 公開日: 2026-07-09 02:17:28 JST
- 更新日: 2026-07-09 02:17:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Mistuneの3.3.0未満のバージョンにおいて、安全なURLフィルターが一部のスキームを適切にブロックせず、悪意のあるスクリプトが実行される可能性があります。  
- 影響: 悪意のあるURLスキームを通じて、影響を受けるユーザーエージェントでスクリプトが実行されるリスクがあります。  
- 推奨対応: Mistuneをバージョン3.3.0以降にアップデートし、該当の安全なURLフィルターの問題を修正してください。

#### References
- https://github.com/lepture/mistune/commit/c7101fcbb6e8790e8e39157c5ca2238fc6dd6cbc
- https://github.com/lepture/mistune/releases/tag/v3.3.0
- https://github.com/lepture/mistune/security/advisories/GHSA-qfrw-5rxm-mhh2

### [CVE-2026-55575](https://github.com/harttle/liquidjs/commit/8a0c74a7fcb1671aa1dcb71ec82ba0602dc90d04)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-55575
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-09 05:16:53 JST
- 更新日: 2026-07-09 05:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LiquidJSのpop配列フィルターがメモリ制限を適切に考慮せず、大量の配列をクローンすることでメモリ過剰消費を引き起こす可能性があります。  
- 影響: 攻撃者が制御する大規模な配列をテンプレートに渡すことで、メモリ制限を超えるリソース消費が発生し、サービスの安定性に影響を与える恐れがあります。  
- 推奨対応: LiquidJSをバージョン10.27.1以降にアップデートし、メモリ制限の適切な適用を確保してください。

#### References
- https://github.com/harttle/liquidjs/commit/8a0c74a7fcb1671aa1dcb71ec82ba0602dc90d04
- https://github.com/harttle/liquidjs/pull/907
- https://github.com/harttle/liquidjs/releases/tag/v10.27.1
- https://github.com/harttle/liquidjs/security/advisories/GHSA-g357-x5c3-c72p

### [CVE-2026-35211](https://github.com/OpenCTI-Platform/opencti/commit/b134ccedf9e68386723cb42197f8e1d60c3bdbd9)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-35211
- 関連キーワード: graphql, gin
- 影響製品: -
- 公開日: 2026-07-09 06:16:48 JST
- 更新日: 2026-07-09 06:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenCTIのGraphQL APIにおいて、認証済みユーザーがElasticsearchのスクリプトを検証なしに実行できる脆弱性が存在します。  
- 影響: 悪意のあるスクリプトによりCPUリソースが過剰消費され、サービスの遅延や拒否が発生する可能性があります。  
- 推奨対応: バージョン7.260401.0以降にアップデートし、脆弱性を修正してください。

#### References
- https://github.com/OpenCTI-Platform/opencti/commit/b134ccedf9e68386723cb42197f8e1d60c3bdbd9
- https://github.com/OpenCTI-Platform/opencti/pull/15284
- https://github.com/OpenCTI-Platform/opencti/releases/tag/7.260401.0
- https://github.com/OpenCTI-Platform/opencti/security/advisories/GHSA-qpp6-p693-rmm4

### [CVE-2026-59871](https://github.com/isaacs/node-tar/commit/e02a4e9e013c4be95302e2eb2047a942b883c27b)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-59871
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-07-09 01:16:33 JST
- 更新日: 2026-07-09 02:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: node-tarの7.5.18未満のバージョンで、すべて数字のPAXパスおよびリンクパス値がJavaScriptの数値に変換され、パス処理時にTypeErrorが発生する問題があります。  
- 影響: 不適切なパス処理により、アプリケーションで例外が発生し正常な動作が妨げられる可能性があります。  
- 推奨対応: node-tarをバージョン7.5.18以降にアップデートして問題を解消してください。

#### References
- https://github.com/isaacs/node-tar/commit/e02a4e9e013c4be95302e2eb2047a942b883c27b
- https://github.com/isaacs/node-tar/releases/tag/v7.5.18
- https://github.com/isaacs/node-tar/security/advisories/GHSA-w8wr-v893-vjvp
- https://github.com/isaacs/node-tar/security/advisories/GHSA-w8wr-v893-vjvp

### [CVE-2026-55878](https://github.com/symfony/ux/commit/7b4ddf3764bf269a1b5fde5bf03c4bce568694e4)

> **Frontend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-55878
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 07:17:16 JST
- 更新日: 2026-07-09 07:17:16 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Symfony UXのux:installコマンドにおいて、相対パスの検証不備により、悪意あるレシピキットが任意のファイルを書き込みまたは読み取り可能な脆弱性が存在します。  
- 影響: 悪意のあるユーザーが任意のファイル操作を行い、システムの機密情報漏洩や改ざんが発生する恐れがあります。  
- 推奨対応: Symfony UXをバージョン2.36.1以降または3.2.0以降にアップデートし、脆弱性を修正してください。

#### References
- https://github.com/symfony/ux/commit/7b4ddf3764bf269a1b5fde5bf03c4bce568694e4
- https://github.com/symfony/ux/releases/tag/v2.36.1
- https://github.com/symfony/ux/releases/tag/v3.2.0
- https://github.com/symfony/ux/security/advisories/GHSA-p9xj-fpr2-jf2q

### [CVE-2026-59262](https://github.com/toeverything/AFFiNE)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-59262
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-07-09 01:16:31 JST
- 更新日: 2026-07-09 05:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: AFFiNEのhistories GraphQLフィールドがDoc.Read権限を適切に検証せず、認証済みのワークスペースメンバーがアクセス権のない文書の編集履歴を取得可能です。  
- 影響: 不正に文書の編集履歴やユーザー名、メールアドレス、タイムスタンプなどの機密情報が漏洩する恐れがあります。  
- 推奨対応: Doc.Read権限の検証を強化し、アクセス制御を適切に実装することを推奨します。

#### References
- https://github.com/toeverything/AFFiNE
- https://github.com/toeverything/AFFiNE/commit/1f0bcd01a37a522393fc1b288395e3a72a79ccad
- https://github.com/toeverything/AFFiNE/issues/15179
- https://www.vulncheck.com/advisories/affine-unauthorized-document-edit-history-access-via-graphql-histories-field
- https://github.com/toeverything/AFFiNE/issues/15179

### [CVE-2026-59802](https://github.com/pglombardo/PasswordPusher/security/advisories/GHSA-76c2-66pg-fj2f)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-59802
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 05:16:55 JST
- 更新日: 2026-07-09 05:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PasswordPusher 2.8.1未満のバージョンで、valid_url関数の検証不足によりdata URIスキームを含むURLプッシュが許可され、悪意あるJavaScriptが実行される可能性があります。  
- 影響: 攻撃者は信頼されたPasswordPusherドメインを利用してフィッシングや認証情報の窃取を行う恐れがあります。  
- 推奨対応: PasswordPusherを2.8.1以降にアップデートし、不審なURLプッシュを警戒してください。

#### References
- https://github.com/pglombardo/PasswordPusher/security/advisories/GHSA-76c2-66pg-fj2f
- https://www.vulncheck.com/advisories/passwordpusher-redirect-based-xss-via-data-uri-in-url-push-payload

### [CVE-2026-59869](https://github.com/nodeca/js-yaml/commit/24f13e79ee1343a7e30bd6f6c9d9cdbf0ac9b2b7)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59869
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 01:16:33 JST
- 更新日: 2026-07-09 01:16:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: js-yamlの3.0.0～3.14.xおよび4.0.0～4.2.xで、マージキーを連鎖的に使用したマッピングの解析時にCPU時間が二次関数的に増加する問題があります。  
- 影響: 大きなYAMLドキュメントの解析時にCPU負荷が著しく増加し、サービスのパフォーマンス低下やDoS攻撃のリスクが考えられます。  
- 推奨対応: js-yamlをバージョン3.15.0または4.3.0以降にアップデートしてください。

#### References
- https://github.com/nodeca/js-yaml/commit/24f13e79ee1343a7e30bd6f6c9d9cdbf0ac9b2b7
- https://github.com/nodeca/js-yaml/commit/59423c6f8cdc78742ac00e25a4dd39ef16b702e4
- https://github.com/nodeca/js-yaml/releases/tag/3.15.0
- https://github.com/nodeca/js-yaml/releases/tag/4.3.0
- https://github.com/nodeca/js-yaml/security/advisories/GHSA-52cp-r559-cp3m

### [CVE-2026-59897](https://github.com/honojs/hono/commit/aa921770d09bc35970362d5a2630a878f6d982fd)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-59897
- 関連キーワード: javascript, gin, aws
- 影響製品: -
- 公開日: 2026-07-09 02:17:27 JST
- 更新日: 2026-07-09 02:17:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: HonoのAWS API Gateway v1アダプター（4.3.3～4.12.27未満）で、X-Forwarded-Forヘッダーの値が部分一致による重複排除により一部削除される問題があります。  
- 影響: 完全なX-Forwarded-Forチェーンを利用するレート制限や監査ログ、プロキシチェーン検証などのミドルウェアやアプリケーションロジックが不完全なデータを受け取る可能性があります。  
- 推奨対応: バージョン4.12.27以降にアップデートし、ヘッダーの重複排除処理が正確に行われるようにしてください。

#### References
- https://github.com/honojs/hono/commit/aa921770d09bc35970362d5a2630a878f6d982fd
- https://github.com/honojs/hono/releases/tag/v4.12.27
- https://github.com/honojs/hono/security/advisories/GHSA-xgm2-5f3f-mvvc

### [CVE-2026-59930](https://github.com/lepture/mistune/commit/c4093c4742ed0d10d9332fb8edb455869b7b581b)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-59930
- 関連キーワード: javascript, python, gin
- 影響製品: -
- 公開日: 2026-07-09 02:17:28 JST
- 更新日: 2026-07-09 02:17:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: MistuneのtocプラグインおよびTableOfContentsディレクティブが、見出しIDを予測可能なtoc_N形式で生成し、攻撃者が同一ページ内のナビゲーションやCSS、JavaScriptの動作を妨害できる可能性があります。  
- 影響: 攻撃者による同一ページ内のリダイレクトやスタイル・スクリプトの制御が発生する恐れがあります。  
- 推奨対応: Mistuneをバージョン3.3.0以降にアップデートし、修正済みのプラグインを利用してください。

#### References
- https://github.com/lepture/mistune/commit/c4093c4742ed0d10d9332fb8edb455869b7b581b
- https://github.com/lepture/mistune/releases/tag/v3.3.0
- https://github.com/lepture/mistune/security/advisories/GHSA-2hm2-hc3v-44h9

### [CVE-2026-55877](https://github.com/symfony/ux/commit/3a4964ec3700f0af4e13f7bfbf8bb3174c3e79d1)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-55877
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 07:17:15 JST
- 更新日: 2026-07-09 07:17:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Symfony UXのux_icon()関数が未検証のSVGやJSONをそのままHTMLに埋め込むため、クロスサイトスクリプティング（XSS）が発生する可能性があります。  
- 影響: 悪意のあるSVGファイルやIconifyのJSONレスポンスに含まれるスクリプトが実行され、ウェブアプリケーションのセキュリティが損なわれる恐れがあります。  
- 推奨対応: Symfony UXをバージョン2.36.1以上または3.2.0以上にアップデートし、脆弱性の修正を適用してください。

#### References
- https://github.com/symfony/ux/commit/3a4964ec3700f0af4e13f7bfbf8bb3174c3e79d1
- https://github.com/symfony/ux/releases/tag/v2.36.1
- https://github.com/symfony/ux/releases/tag/v3.2.0
- https://github.com/symfony/ux/security/advisories/GHSA-6v8j-33hc-mv84

### [CVE-2026-57439](https://github.com/gchq/CyberChef/commit/85db3be5d0096859b810f0e8d3e151d5dc9b948f)

> **Frontend** / **MEDIUM** / CVSS: **5.0** / KEV: **no**

- タイトル: CVE-2026-57439
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 01:16:31 JST
- 更新日: 2026-07-09 02:17:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CyberChefのSeries Chart操作で、ユーザー提供のCSV解析時に__proto__キーを受け入れることでプロトタイプ汚染が発生し、悪意あるJavaScriptの注入が可能になる問題です。  
- 影響: 悪意のあるスクリプトがHTML出力に注入される可能性があり、クロスサイトスクリプティング（XSS）攻撃のリスクがあります。  
- 推奨対応: CyberChefをバージョン11.2.0以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/gchq/CyberChef/commit/85db3be5d0096859b810f0e8d3e151d5dc9b948f
- https://github.com/gchq/CyberChef/issues/2568
- https://github.com/gchq/CyberChef/pull/2569
- https://github.com/gchq/CyberChef/releases/tag/v11.2.0
- https://github.com/gchq/CyberChef/security/advisories/GHSA-fx6f-382r-j72c

### [CVE-2026-58191](https://github.com/appium/appium/security/advisories/GHSA-3wgp-x9p5-c7cc)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-58191
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-09 06:16:52 JST
- 更新日: 2026-07-09 06:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Appiumの10.7.0以前のバージョンで、特定のルートにおいてエスケープされていない入力がHTMLに反映されるため、反射型クロスサイトスクリプティングが発生する可能性があります。  
- 影響: 攻撃者がサーバー上で任意のJavaScriptを実行できるリスクがあり、情報漏洩やセッション乗っ取りの恐れがあります。  
- 推奨対応: Appiumをバージョン10.7.0以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/appium/appium/security/advisories/GHSA-3wgp-x9p5-c7cc

### [CVE-2026-59868](https://github.com/nodeca/js-yaml/commit/3105455b81dee69e0fd36e09ac0b2ccfdb54adc1)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-59868
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 01:16:33 JST
- 更新日: 2026-07-09 01:16:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: js-yamlのバージョン5.0.0から5.2.0未満で、マージキーを有効にした際に特定のマッピングチェーンでCPU使用率が二次関数的に増加する問題が報告されています。  
- 影響: 大きなYAMLドキュメントの解析時にCPU負荷が異常に高くなり、パフォーマンス低下やサービスの遅延が発生する可能性があります。  
- 推奨対応: js-yamlをバージョン5.2.0以降にアップデートし、マージキー使用時のパフォーマンス問題を回避してください。

#### References
- https://github.com/nodeca/js-yaml/commit/3105455b81dee69e0fd36e09ac0b2ccfdb54adc1
- https://github.com/nodeca/js-yaml/releases/tag/5.2.0
- https://github.com/nodeca/js-yaml/security/advisories/GHSA-g796-fgmg-93mv

### [CVE-2026-59870](https://github.com/nodeca/js-yaml/commit/39f3211a2f01b3c6982710cf21434ab7060acefe)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-59870
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 01:16:33 JST
- 更新日: 2026-07-09 02:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: js-yamlの5.0.0から5.2.1未満のバージョンで、YAML11_SCHEMAの!!omapタグ処理において重複キー検出が非効率でCPU負荷が高くなる問題があります。  
- 影響: 特定の順序付きマップ文書を解析する際にCPU使用率が急増し、サービスのパフォーマンス低下やDoSの可能性があります。  
- 推奨対応: バージョン5.2.1以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/nodeca/js-yaml/commit/39f3211a2f01b3c6982710cf21434ab7060acefe
- https://github.com/nodeca/js-yaml/releases/tag/5.2.1
- https://github.com/nodeca/js-yaml/security/advisories/GHSA-724g-mxrg-4qvm
- https://github.com/nodeca/js-yaml/security/advisories/GHSA-724g-mxrg-4qvm

### [CVE-2026-59876](https://github.com/protobufjs/protobuf.js/commit/9f97fe413072d3beb52c74e62d88ea8adc9444d8)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-59876
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 01:16:34 JST
- 更新日: 2026-07-09 01:16:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: protobufjsのText Format拡張機能で、文字列キーのマップエントリを通常のプロパティ割り当てで解析する際に、キーが__proto__の場合にマップオブジェクトのプロトタイプが変更される問題がありました。  
- 影響: 悪意のある入力によりマップオブジェクトのプロトタイプが書き換えられ、予期しない動作やセキュリティリスクが発生する可能性があります。  
- 推奨対応: protobufjsをバージョン8.6.5以降にアップデートし、この問題の修正を適用してください。

#### References
- https://github.com/protobufjs/protobuf.js/commit/9f97fe413072d3beb52c74e62d88ea8adc9444d8
- https://github.com/protobufjs/protobuf.js/pull/2335
- https://github.com/protobufjs/protobuf.js/releases/tag/protobufjs-v8.6.5
- https://github.com/protobufjs/protobuf.js/security/advisories/GHSA-jfj6-75fj-8934

### [CVE-2026-59877](https://github.com/protobufjs/protobuf.js/commit/10fba6d54815ceecca8a06b9a6db490c8f5d2217)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-59877
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 01:16:34 JST
- 更新日: 2026-07-09 02:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: protobufjsの特定バージョンで、不完全な.protoスキーマにより無限ループが発生する可能性があります。  
- 影響: 悪意のある.protoファイルを処理すると、parseやRoot.load、Root.loadSyncが無限ループに陥る恐れがあります。  
- 推奨対応: protobufjsをバージョン7.6.5または8.6.6以降にアップデートしてください。

#### References
- https://github.com/protobufjs/protobuf.js/commit/10fba6d54815ceecca8a06b9a6db490c8f5d2217
- https://github.com/protobufjs/protobuf.js/commit/fa5c73add738ceb471e74da8cc2f3727c3d0a69f
- https://github.com/protobufjs/protobuf.js/pull/2352
- https://github.com/protobufjs/protobuf.js/releases/tag/protobufjs-v7.6.5
- https://github.com/protobufjs/protobuf.js/releases/tag/protobufjs-v8.6.6

### [CVE-2026-59895](https://github.com/honojs/hono/commit/cd3f6f7194f0e5c9d4b26ae0cf232018d0f388fc)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-59895
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 02:17:27 JST
- 更新日: 2026-07-09 05:16:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Honoフレームワークのcx()関数が、クラス名をHTMLエスケープせずに既にエスケープ済みと誤認し、サーバーサイドレンダリング時に任意のマークアップ注入を許す可能性があります。  
- 影響: 悪意のあるクラス名がJSXのclass属性を突破し、クロスサイトスクリプティング（XSS）などの脆弱性を引き起こす恐れがあります。  
- 推奨対応: Honoをバージョン4.12.27以降にアップデートし、cx()の脆弱性修正を適用してください。

#### References
- https://github.com/honojs/hono/commit/cd3f6f7194f0e5c9d4b26ae0cf232018d0f388fc
- https://github.com/honojs/hono/releases/tag/v4.12.27
- https://github.com/honojs/hono/security/advisories/GHSA-w62v-xxxg-mg59

### [CVE-2026-59896](https://github.com/honojs/hono/commit/fab3b13639339cbd5ba1166a5b23d9ac30c5f64f)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-59896
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-09 02:17:27 JST
- 更新日: 2026-07-09 03:16:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Honoの4.11.8から4.12.27未満のバージョンで、サーバーサイドレンダリング時にリクエストごとのコンテキスト値が分離されず、異なるリクエストのデータが非同期コンポーネント内で誤って使用される可能性があります。  
- 影響: 複数リクエスト間でコンテキストデータが混在し、情報漏洩や不整合が発生するリスクがあります。  
- 推奨対応: バージョン4.12.27以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/honojs/hono/commit/fab3b13639339cbd5ba1166a5b23d9ac30c5f64f
- https://github.com/honojs/hono/releases/tag/v4.12.27
- https://github.com/honojs/hono/security/advisories/GHSA-hvrm-45r6-mjfj

### [CVE-2026-6352](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-1-2-released/)

> **Frontend** / **LOW** / CVSS: **2.7** / KEV: **no**

- タイトル: CVE-2026-6352
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-07-09 06:16:54 JST
- 更新日: 2026-07-09 06:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: GitLab EEの特定バージョンにおいて、監査者レベルの認証ユーザーが特定のGraphQL操作でコンプライアンス違反記録を不適切に変更できる問題が修正されました。  
- 影響: 監査者権限を持つユーザーによる不正なコンプライアンス違反記録の改ざんの可能性があります。  
- 推奨対応: 対象バージョンを使用している場合は、18.11.7、19.0.4、19.1.2以降のバージョンへアップデートを検討してください。

#### References
- https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-1-2-released/
- https://gitlab.com/gitlab-org/gitlab/-/work_items/596789
- https://hackerone.com/reports/3631344

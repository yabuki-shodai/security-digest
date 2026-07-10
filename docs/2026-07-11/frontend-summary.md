# Frontend CVE Summary (2026-07-11)

## Overview

- 取得日時: 2026-07-11 08:10:55 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 10
- Critical: 0
- High: 4
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-56312](https://github.com/Cap-go/capgo/security/advisories/GHSA-whc5-fvr7-g5v3)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-56312
- 関連キーワード: vite, go
- 影響製品: -
- 公開日: 2026-07-11 00:16:42 JST
- 更新日: 2026-07-11 02:17:00 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Capgo 12.128.2以前のaccept_invitationエンドポイントにおいて、captcha検証前にユーザーアカウントを作成できる不適切な検証の脆弱性が存在します。  
- 影響: 攻撃者が無効なcaptchaトークンを用いたPOSTリクエストでアカウントを不正作成し、招待リンクを消費される可能性があります。  
- 推奨対応: 最新バージョンへのアップデートや、captcha検証の適切な実装を検討してください。

#### References
- https://github.com/Cap-go/capgo/security/advisories/GHSA-whc5-fvr7-g5v3
- https://www.vulncheck.com/advisories/capgo-account-creation-before-captcha-validation-in-accept-invitation-endpoint

### [CVE-2026-56667](https://github.com/zitadel/zitadel/commit/038265925a3b05ac1df8aad461ab071983e9eb85)

> **Frontend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-56667
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-11 03:16:24 JST
- 更新日: 2026-07-11 06:16:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ZITADELのLogin V2 OIDCおよびSAMLのエラーパスで、isSafeRedirectUriチェックが適用されず、悪意あるJavaScriptやdata URIが実行される可能性があります。  
- 影響: 組織やインスタンス管理者が悪意あるリダイレクトURIを設定すると、ユーザーのブラウザで任意のコードが実行される恐れがあります。  
- 推奨対応: ZITADELをバージョン4.15.3以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/zitadel/zitadel/commit/038265925a3b05ac1df8aad461ab071983e9eb85
- https://github.com/zitadel/zitadel/releases/tag/v4.15.3
- https://github.com/zitadel/zitadel/security/advisories/GHSA-5wcj-9wj4-j65h

### [CVE-2026-55665](https://github.com/gristlabs/grist-core/commit/5d0a90a162b5125fce7e8a86fb137eee5199dbde)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-55665
- 関連キーワード: javascript, python, gin
- 影響製品: -
- 公開日: 2026-07-11 06:16:56 JST
- 更新日: 2026-07-11 06:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Gristの1.7.15以前のバージョンにおいて、リンクのhrefにスキーム検証がなく、悪意あるJavaScriptが実行されるクロスサイトスクリプティング脆弱性が2件存在します。  
- 影響: 攻撃者は被害者の認証済みセッションでスクリプトを実行し、データの読み取り・変更や共有設定の変更、所有者権限の昇格が可能になる恐れがあります。  
- 推奨対応: 速やかにGristをバージョン1.7.15以降にアップデートし、脆弱性を修正してください。

#### References
- https://github.com/gristlabs/grist-core/commit/5d0a90a162b5125fce7e8a86fb137eee5199dbde
- https://github.com/gristlabs/grist-core/releases/tag/v1.7.15
- https://github.com/gristlabs/grist-core/security/advisories/GHSA-7f6v-vghq-34xq

### [CVE-2026-57214](https://github.com/rabbitmq/rabbitmq-server/commit/b0027b6c1ae5b869d876e211efe6189ffd92b5c2)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-57214
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-11 06:16:58 JST
- 更新日: 2026-07-11 06:16:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: RabbitMQの管理UIで、x-internal-purpose引数が適切にエスケープされず、JavaScriptが実行される可能性があります。  
- 影響: 権限を持つユーザーが他のユーザーのブラウザでスクリプトを実行できるクロスサイトスクリプティング（XSS）のリスクがあります。  
- 推奨対応: RabbitMQをバージョン4.2.5以降にアップデートし、適切なエスケープ処理が行われた状態にしてください。

#### References
- https://github.com/rabbitmq/rabbitmq-server/commit/b0027b6c1ae5b869d876e211efe6189ffd92b5c2
- https://github.com/rabbitmq/rabbitmq-server/commit/b267a290dd89e42c6e0256f46fc273a8adb7f3ec
- https://github.com/rabbitmq/rabbitmq-server/pull/15606
- https://github.com/rabbitmq/rabbitmq-server/pull/15608
- https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.2.5

### [CVE-2026-29519](https://github.com/L4V4D0/CVE-2026-29519-Lucee-Reflected-XSS)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-29519
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-11 00:16:39 JST
- 更新日: 2026-07-11 02:56:00 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Lucee CFML Serverの複数バージョンにおいて、URLパス解析時の反射型クロスサイトスクリプティング脆弱性が存在し、未認証の攻撃者が悪意あるJavaScriptを実行可能です。  
- 影響: 攻撃者は被害者のブラウザで任意のスクリプトを実行し、セッションハイジャックや管理インターフェースへの不正操作が行われる恐れがあります。  
- 推奨対応: 最新のセキュリティパッチ適用や、URLパスの適切なエンコード処理を実施し、不審なリンクのクリックを避けることが望まれます。

#### References
- https://github.com/L4V4D0/CVE-2026-29519-Lucee-Reflected-XSS
- https://www.vulncheck.com/advisories/lucee-cfml-server-reflected-xss-via-url-path-parsing

### [CVE-2026-55466](https://github.com/grokability/snipe-it/commit/000cea0a622d586366cf60d2240c7c2a4b17c955)

> **Frontend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-55466
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-11 05:16:46 JST
- 更新日: 2026-07-11 05:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Snipe-ITの8.6.2以前のバージョンで、SVGファイルのアップロード処理に不備があり、低権限ユーザーが悪意のあるXHTMLやXMLをアップロードして同一オリジンでJavaScriptを実行される可能性があります。  
- 影響: 悪意のあるスクリプトがブラウザ上で実行されることで、クロスサイトスクリプティング（XSS）攻撃のリスクがあります。  
- 推奨対応: Snipe-ITをバージョン8.6.2以降にアップデートし、SVGファイルの適切なサニタイズと安全なインライン表示を確保してください。

#### References
- https://github.com/grokability/snipe-it/commit/000cea0a622d586366cf60d2240c7c2a4b17c955
- https://github.com/grokability/snipe-it/releases/tag/v8.6.2
- https://github.com/grokability/snipe-it/security/advisories/GHSA-jhph-5q74-pmfx

### [CVE-2026-57167](https://github.com/Chocobozzz/PeerTube/commit/45394d701b08e87d72b8f0c1866b881f2becbde3)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-57167
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-11 02:17:01 JST
- 更新日: 2026-07-11 03:56:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PeerTubeの8.2.2以前のバージョンで、動画視聴ページのメタデータ処理において不適切なエスケープにより、任意のHTMLやJavaScriptが実行される可能性があります。  
- 影響: 悪意ある動画を視聴したユーザーのブラウザ上でスクリプトが実行され、クロスサイトスクリプティング（XSS）攻撃が発生する恐れがあります。  
- 推奨対応: 影響を受けるバージョンを使用している場合は、PeerTubeを8.2.2以降にアップデートしてください。

#### References
- https://github.com/Chocobozzz/PeerTube/commit/45394d701b08e87d72b8f0c1866b881f2becbde3
- https://github.com/Chocobozzz/PeerTube/releases/tag/v8.2.2
- https://github.com/Chocobozzz/PeerTube/security/advisories/GHSA-jxwq-h9xv-hr28

### [CVE-2026-57213](https://github.com/rabbitmq/rabbitmq-server/commit/33dedfe4fd53ff009cc67ab36358d0624c6b2e53)

> **Frontend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-57213
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-11 06:16:58 JST
- 更新日: 2026-07-11 06:16:58 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: RabbitMQのrabbitmq_federation_managementプラグインで、consumer_tagフィールドがHTMLエスケープされずに表示されるため、フェデレーション設定権限を持つユーザーがXSS攻撃を実行可能です。  
- 影響: フェデレーションのアップストリームやポリシーを設定できるユーザーが、他のユーザーのブラウザ上で任意のJavaScriptを実行できる可能性があります。  
- 推奨対応: RabbitMQをバージョン3.13.14、4.0.19、4.1.10、または4.2.5以降にアップデートし、該当プラグインの脆弱性修正を適用してください。

#### References
- https://github.com/rabbitmq/rabbitmq-server/commit/33dedfe4fd53ff009cc67ab36358d0624c6b2e53
- https://github.com/rabbitmq/rabbitmq-server/commit/c2d0d69edf01efbd6e87dfb250c373a32da957f8
- https://github.com/rabbitmq/rabbitmq-server/pull/15708
- https://github.com/rabbitmq/rabbitmq-server/pull/15711
- https://github.com/rabbitmq/rabbitmq-server/releases/tag/v4.2.5

### [CVE-2026-61456](https://github.com/getgrav/grav/security/advisories/GHSA-7vhm-8x52-2r5p)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-61456
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-11 00:16:51 JST
- 更新日: 2026-07-11 02:41:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Grav APIプラグイン（1.0.3未満）で、POST /api/v1/mediaエンドポイント経由のSVGファイルのサニタイズが不十分で、認証済み攻撃者が任意のJavaScriptを含むSVGをアップロード可能です。  
- 影響: 管理者が悪意あるSVGをブラウザで開くと、スクリプトが実行されクッキーの窃取やセッションハイジャックが発生する恐れがあります。  
- 推奨対応: Grav APIプラグインをバージョン1.0.3以降に更新し、SVGファイルの適切なサニタイズを行うことを推奨します。

#### References
- https://github.com/getgrav/grav/security/advisories/GHSA-7vhm-8x52-2r5p
- https://www.vulncheck.com/advisories/grav-before-stored-xss-via-svg-upload-api
- https://github.com/getgrav/grav/security/advisories/GHSA-7vhm-8x52-2r5p

### [CVE-2026-55464](https://github.com/grokability/snipe-it/commit/006981cccffce1739e24d3b680b676f772f40e2d)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-55464: snipeitapp snipe-it
- 関連キーワード: javascript
- 影響製品: snipeitapp snipe-it
- 公開日: 2026-07-11 04:17:24 JST
- 更新日: 2026-07-11 05:11:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: snipeitappのSnipe-IT（8.6.2未満）において、Markdownのリンクにjavascript: URIが適切にサニタイズされず、assets.edit権限を持つユーザーが悪意あるスクリプトを埋め込める脆弱性が存在します。  
- 影響: 悪意あるリンクをクリックしたユーザーのブラウザで任意のJavaScriptが実行される可能性があり、情報漏洩や操作の乗っ取りリスクがあります。  
- 推奨対応: 影響を受けるバージョンを使用している場合は、8.6.2以降にアップデートし、権限管理を見直すことを推奨します。

#### References
- https://github.com/grokability/snipe-it/commit/006981cccffce1739e24d3b680b676f772f40e2d
- https://github.com/grokability/snipe-it/releases/tag/v8.6.2
- https://github.com/grokability/snipe-it/security/advisories/GHSA-r52f-r9v5-66xr

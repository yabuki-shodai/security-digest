# Frontend CVE Summary (2026-07-16)

## Overview

- 取得日時: 2026-07-16 08:09:14 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 26
- Critical: 5
- High: 15
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-55445](https://github.com/whyour/qinglong/commit/6bec52dca158481258315ba0fc2f11206df7b719)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-55445
- 関連キーワード: typescript, javascript, python, express
- 影響製品: -
- 公開日: 2026-07-16 07:17:26 JST
- 更新日: 2026-07-16 07:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Qinglongの2.20.1未満のバージョンにおいて、認証前のパス検証不備により、認証されていない攻撃者が管理者の認証情報をリセット可能な脆弱性が存在します。  
- 影響: 攻撃者が管理者権限を奪取し、システムの制御を乗っ取るリスクがあります。  
- 推奨対応: バージョン2.20.1以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/whyour/qinglong/commit/6bec52dca158481258315ba0fc2f11206df7b719
- https://github.com/whyour/qinglong/pull/2941
- https://github.com/whyour/qinglong/security/advisories/GHSA-v667-gc2r-2xm7

### [CVE-2026-53512](https://github.com/better-auth/better-auth/commit/1f2ff4215c4affff0b140b0c0a712c0dde35659c)

> **Frontend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-53512
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-07-16 03:16:47 JST
- 更新日: 2026-07-16 05:29:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Better Authの1.6.11未満のバージョンで、oidcProviderおよびmcpプラグインがclient_secretを検証せずにrefresh_tokenを使った認証を許可し、不正にアクセストークンを発行される可能性があります。  
- 影響: 攻撃者が有効なrefresh_tokenを持っている場合、不正にアクセストークンや更新済みのrefresh_tokenを取得できるため、認証の安全性が重大に損なわれます。  
- 推奨対応: Better Authをバージョン1.6.11以降にアップデートし、@better-auth/oauth-providerパッケージの影響はないものの、関連プラグインの利用を見直してください。

#### References
- https://github.com/better-auth/better-auth/commit/1f2ff4215c4affff0b140b0c0a712c0dde35659c
- https://github.com/better-auth/better-auth/pull/9576
- https://github.com/better-auth/better-auth/releases/tag/v1.6.11
- https://github.com/better-auth/better-auth/security/advisories/GHSA-pw9m-5jxm-xr6h

### [CVE-2026-53513](https://github.com/better-auth/better-auth/commit/37f60cb176cb53147da7dfd5ec15afa5b486e81e)

> **Frontend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-53513
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-07-16 03:16:47 JST
- 更新日: 2026-07-16 05:54:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Better Authの@better-auth/ssoプラグインで、skipDiscovery: true設定時に外部から制御可能なOIDCエンドポイントを検証せず保存し、サーバーサイドリクエスト偽造やアカウント連携のリスクがある脆弱性。  
- 影響: 悪意ある攻撃者が任意のOIDCエンドポイントを指定し、サーバー側で不正なリクエストを実行させる可能性がある。  
- 推奨対応: バージョン1.6.11以降にアップデートし、信頼できないOIDCエンドポイントの入力を避けること。

#### References
- https://github.com/better-auth/better-auth/commit/37f60cb176cb53147da7dfd5ec15afa5b486e81e
- https://github.com/better-auth/better-auth/pull/9574
- https://github.com/better-auth/better-auth/releases/tag/v1.6.11
- https://github.com/better-auth/better-auth/security/advisories/GHSA-5rr4-8452-hf4v

### [CVE-2026-53514](https://github.com/better-auth/better-auth/commit/23094a628f007f801be6d26e5b15dc5fc6fc4eb8)

> **Frontend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-53514
- 関連キーワード: typescript, vite, gin
- 影響製品: -
- 公開日: 2026-07-16 03:16:47 JST
- 更新日: 2026-07-16 05:29:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Better Authの特定バージョンにおいて、招待IDが外部から取得可能で、メール検証が有効でない場合、未検証のセッションユーザーが組織招待を不正に受諾できる脆弱性が存在します。  
- 影響: 不正なユーザーが招待を受け入れ、組織への不正アクセスが可能になるリスクがあります。  
- 推奨対応: バージョン1.6.11以降にアップデートし、招待時のメール検証設定を有効にすることを検討してください。

#### References
- https://github.com/better-auth/better-auth/commit/23094a628f007f801be6d26e5b15dc5fc6fc4eb8
- https://github.com/better-auth/better-auth/pull/9577
- https://github.com/better-auth/better-auth/releases/tag/v1.6.11
- https://github.com/better-auth/better-auth/security/advisories/GHSA-fmh4-wcc4-5jm3

### [CVE-2026-45337](https://github.com/better-auth/better-auth/commit/99a254a79b59d5a3f5ca2123260118cddb5beed7)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-45337
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-07-16 03:16:45 JST
- 更新日: 2026-07-16 05:29:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Better AuthのdeviceAuthorizationプラグインにおいて、認証済みセッションが任意の保留中デバイスコードの所有者とみなされる脆弱性が存在します。  
- 影響: 攻撃者が有効なuser_codeを知ると、自身のアカウントにデバイスを紐付けたり、正当な認証フローを拒否できる可能性があります。  
- 推奨対応: バージョン1.6.11以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/better-auth/better-auth/commit/99a254a79b59d5a3f5ca2123260118cddb5beed7
- https://github.com/better-auth/better-auth/pull/9573
- https://github.com/better-auth/better-auth/releases/tag/v1.6.11
- https://github.com/better-auth/better-auth/security/advisories/GHSA-cq3f-vc6p-68fh

### [CVE-2026-53515](https://github.com/better-auth/better-auth/commit/86765f1597378f5c3deed1b80ca91faac0a6bf00)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-53515
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-07-16 03:16:47 JST
- 更新日: 2026-07-16 05:54:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Better Authの@better-auth/ssoプラグイン（バージョン1.2.10～1.6.11）において、組織メンバーであれば誰でも新しいSSOプロバイダーを追加できる認証の不備が存在します。  
- 影響: 攻撃者がOIDCやSAMLプロバイダーを悪用し、組織のSSO設定を不正に変更される可能性があります。  
- 推奨対応: バージョン1.6.11以降にアップデートし、管理者権限のチェックが適切に行われるようにしてください。

#### References
- https://github.com/better-auth/better-auth/commit/86765f1597378f5c3deed1b80ca91faac0a6bf00
- https://github.com/better-auth/better-auth/pull/9220
- https://github.com/better-auth/better-auth/releases/tag/v1.6.11
- https://github.com/better-auth/better-auth/security/advisories/GHSA-gv74-j8m3-fg5f

### [CVE-2026-53517](https://github.com/better-auth/better-auth/commit/c6918ecc9e3a75892169415d7f6c95b591b6a52d)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-53517
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-07-16 03:16:48 JST
- 更新日: 2026-07-16 05:54:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Better AuthのOAuth2トークン更新処理で、同一リフレッシュトークンを使った並行リクエストが無効化チェックを回避し、複数のリフレッシュトークンが発行される問題が1.4.8-beta.7から1.6.11未満のバージョンで発生します。  
- 影響: 不正なトークンの多重発行により認証の整合性が損なわれる可能性があり、セキュリティリスクが高いと考えられます。  
- 推奨対応: バージョン1.6.11以降にアップデートし、該当のOAuthプラグインを含む環境では速やかに修正を適用してください。

#### References
- https://github.com/better-auth/better-auth/commit/c6918ecc9e3a75892169415d7f6c95b591b6a52d
- https://github.com/better-auth/better-auth/releases/tag/v1.6.11
- https://github.com/better-auth/better-auth/security/advisories/GHSA-392p-2q2v-4372

### [CVE-2026-53518](https://github.com/better-auth/better-auth/commit/b4bc65a007784b2eb0efb459e5fa6fd8055d3ec9)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-53518
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-07-16 03:16:48 JST
- 更新日: 2026-07-16 05:29:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Better AuthのTypeScriptライブラリで、認可コードを単一使用として処理する際に競合状態が発生し、複数のアクセストークンやリフレッシュトークンが発行される脆弱性が存在します。  
- 影響: 認可コードの多重利用により、不正に複数のトークンが発行される可能性があり、認証の信頼性が損なわれる恐れがあります。  
- 推奨対応: バージョン1.6.11以降にアップデートし、該当の非原子的な処理を修正したバージョンを利用してください。

#### References
- https://github.com/better-auth/better-auth/commit/b4bc65a007784b2eb0efb459e5fa6fd8055d3ec9
- https://github.com/better-auth/better-auth/releases/tag/v1.6.11
- https://github.com/better-auth/better-auth/security/advisories/GHSA-7w99-5wm4-3g79

### [CVE-2026-48795](https://github.com/adonisjs/bodyparser/commit/8a85eb0c2061b0caca10faedbfc2cf24b56cf9f6)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-48795
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-07-16 07:16:50 JST
- 更新日: 2026-07-16 07:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: AdonisJSの@adonisjs/bodyparserで、ネストされたmultipartフィールドによりObject.prototypeが汚染される脆弱性が一部修正されていなかった問題です。  
- 影響: 悪意ある入力によりObject.prototypeが汚染され、予期しない動作やセキュリティリスクが発生する可能性があります。  
- 推奨対応: バージョン10.1.5または11.0.3以降にアップデートし、修正済みの状態にすることを推奨します。

#### References
- https://github.com/adonisjs/bodyparser/commit/8a85eb0c2061b0caca10faedbfc2cf24b56cf9f6
- https://github.com/adonisjs/bodyparser/commit/aa96908f7b3f64c19e15d2d2d916b69137bdf469
- https://github.com/adonisjs/bodyparser/releases/tag/v10.1.5
- https://github.com/adonisjs/bodyparser/releases/tag/v11.0.3
- https://github.com/adonisjs/core/security/advisories/GHSA-qcm7-3vpr-hj5h

### [CVE-2026-53516](https://github.com/better-auth/better-auth/commit/da7e50beee849c59a2ed1ec6b3a38cc6ab9fb563)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-53516
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-07-16 03:16:47 JST
- 更新日: 2026-07-16 05:29:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Better AuthのOAuthコールバック処理で、OAuthプロバイダがemail_verified: trueを主張するとローカルのemailVerifiedフィールドを確認せずにアカウント連携が許可される脆弱性が存在します。  
- 影響: 攻撃者が被害者のメールアドレスを事前登録することで、被害者のOAuthアカウントを攻撃者のアカウントに不正に紐付け可能です。  
- 推奨対応: バージョン1.6.11以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/better-auth/better-auth/commit/da7e50beee849c59a2ed1ec6b3a38cc6ab9fb563
- https://github.com/better-auth/better-auth/pull/9578
- https://github.com/better-auth/better-auth/releases/tag/v1.6.11
- https://github.com/better-auth/better-auth/security/advisories/GHSA-g38m-r43w-p2q7

### [CVE-2026-46421](https://github.com/cap-js/cds-dbs/security/advisories/GHSA-pvw4-cvr4-97p8)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-46421
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-07-16 04:17:17 JST
- 更新日: 2026-07-16 05:29:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SAP Cloud Application Programming ModelのSQLデータベースサービス用パッケージにマルウェアが含まれたバージョンが公開され、資格情報の窃取と自己拡散が行われました。  
- 影響: インストールされた場合、npmトークンやクラウド認証情報、SSHキー、GitHubのPATなど、マシン上の全ての資格情報が漏洩した可能性があります。  
- 推奨対応: 影響を受けたパッケージを指定バージョン以上にアップグレードし、漏洩の可能性がある全ての資格情報を速やかにローテーションしてください。

#### References
- https://github.com/cap-js/cds-dbs/security/advisories/GHSA-pvw4-cvr4-97p8
- https://me.sap.com/notes/3747787
- https://www.sap.com/documents/2026/05/8203a8b9-4d7f-0010-bca6-c68f7e60039b.html
- https://www.stepsecurity.io/blog/a-mini-shai-hulud-has-appeared

### [CVE-2026-15895](https://aws.amazon.com/security/security-bulletins/2026-057-aws/)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-15895
- 関連キーワード: npm, aws
- 影響製品: -
- 公開日: 2026-07-16 04:16:58 JST
- 更新日: 2026-07-16 05:16:56 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: AWSのjsii-diffパッケージ（1.131.0未満）において、npmパッケージ読み込み時のコマンドインジェクション脆弱性が報告されています。  
- 影響: 攻撃者が細工したパッケージ指定子を利用して任意のOSコマンドを実行できる可能性があります。  
- 推奨対応: jsii-diffをバージョン1.131.0以降にアップグレードすることを推奨します。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-057-aws/
- https://github.com/aws/jsii/releases/tag/v1.131.0

### [CVE-2026-54458](https://github.com/WWBN/AVideo/commit/8be71e53ccbe9b84b30870db386fb4d2b11e1c16)

> **Frontend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-54458
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-16 07:17:19 JST
- 更新日: 2026-07-16 07:17:19 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WWBN AVideoのYPTSocketプラグインに保存型DOMクロスサイトスクリプティングの脆弱性があり、認証済み管理者のページで任意のJavaScriptが実行される可能性があります。  
- 影響: 認証済み管理者のクッキーやCSRFトークンの漏洩、管理者権限の不正取得などが発生する恐れがあります。  
- 推奨対応: 影響を受けるバージョンからのアップデートや、プラグインの利用停止、入力値の適切な検証・サニタイズを検討してください。

#### References
- https://github.com/WWBN/AVideo/commit/8be71e53ccbe9b84b30870db386fb4d2b11e1c16
- https://github.com/WWBN/AVideo/security/advisories/GHSA-8whc-2wmv-ww35

### [CVE-2026-49279](https://github.com/WWBN/AVideo/commit/3e0b3ce2bfa766183ff0ae227439394db57b1a23)

> **Frontend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-49279
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-16 07:16:52 JST
- 更新日: 2026-07-16 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WWBN AVideoのバージョン29.0以下に、MessageSQLite WebSocketハンドラのautoEvalCodeOnHTMLパラメータを悪用したStored XSS脆弱性が存在します。  
- 影響: 認証済み攻撃者が任意のJavaScriptを他ユーザーのブラウザで実行し、セッションハイジャックや管理者権限の不正操作が可能になる恐れがあります。  
- 推奨対応: 最新のパッチを適用し、WebSocketメッセージ処理の脆弱性を修正することを推奨します。

#### References
- https://github.com/WWBN/AVideo/commit/3e0b3ce2bfa766183ff0ae227439394db57b1a23
- https://github.com/WWBN/AVideo/security/advisories/GHSA-2fhx-q92v-5fhv

### [CVE-2026-40501](https://gist.github.com/Mundi-Xu/99af1b08275fd437cfb79bfe481e68b7)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-40501
- 関連キーワード: javascript, gin, node.js
- 影響製品: -
- 公開日: 2026-07-16 03:16:45 JST
- 更新日: 2026-07-16 06:02:41 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Cherry Studio 1.2.2から1.9.12にかけて、SearchServiceの脆弱性により、悪意あるJavaScriptがリモートで実行される可能性があります。  
- 影響: 攻撃者はNode.jsの完全な権限で任意のコードを実行でき、ファイルシステムやプロセス情報にアクセスされる恐れがあります。  
- 推奨対応: 最新の修正コミット1518530を適用し、nodeIntegrationを無効化、contextIsolationを有効化する設定を検討してください。

#### References
- https://gist.github.com/Mundi-Xu/99af1b08275fd437cfb79bfe481e68b7
- https://github.com/CherryHQ/cherry-studio/commit/151853035e8e417a51559ebfc243eda98361a882
- https://www.vulncheck.com/advisories/cherry-studio-rce-via-searchservice-nodeintegration-misconfiguration

### [CVE-2026-63175](https://github.com/Lookyloo/PlaywrightCapture/commit/1e354b9d8566f49dbb331410be24c7c295645d43)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-63175
- 関連キーワード: playwright, python, gin
- 影響製品: -
- 公開日: 2026-07-16 07:17:38 JST
- 更新日: 2026-07-16 07:17:38 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PlaywrightCaptureがキャプチャ固有の設定や実行時データをクラスレベルの可変変数として保持しており、同一Pythonプロセス内の複数のCaptureオブジェクト間で状態が共有される問題です。  
- 影響: 認証クッキーや資格情報、ブラウザストレージ、リクエストデータの漏洩や、他ユーザーの認証コンテキストでのリクエスト実行による不正アクセスの可能性があります。  
- 推奨対応: Captureの設定とリクエストデータをインスタンス変数として初期化し、キャプチャ間の状態を分離するアップデートを適用してください。

#### References
- https://github.com/Lookyloo/PlaywrightCapture/commit/1e354b9d8566f49dbb331410be24c7c295645d43

### [CVE-2026-45738](https://github.com/argoproj/argo-cd/commit/00f83c41dcfd879f34f8e0248c860d704b41cf0f)

> **Frontend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-45738
- 関連キーワード: javascript, go, gin, kubernetes
- 影響製品: -
- 公開日: 2026-07-16 05:17:05 JST
- 更新日: 2026-07-16 05:29:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Argo CDの特定バージョンにおいて、アプリケーションの書き込み権限を持つユーザーが悪意あるリンク注釈を設定でき、UIのSummaryタブでJavaScriptが実行される可能性があります。  
- 影響: 認証済みの高権限ユーザーのセッションで任意のJavaScriptが実行され、セキュリティリスクが生じる恐れがあります。  
- 推奨対応: Argo CDをバージョン3.2.12、3.3.10、または3.4.2以降にアップデートし、リンク注釈のURL検証が適切に行われるようにしてください。

#### References
- https://github.com/argoproj/argo-cd/commit/00f83c41dcfd879f34f8e0248c860d704b41cf0f
- https://github.com/argoproj/argo-cd/commit/35ea43c537d6e8948e67f347317fc4f88b325122
- https://github.com/argoproj/argo-cd/commit/c8df5ff7acc403adcee1256da5d87081cd52f0a6
- https://github.com/argoproj/argo-cd/releases/tag/v3.2.12
- https://github.com/argoproj/argo-cd/releases/tag/v3.3.10

### [CVE-2026-45805](https://github.com/penpot/penpot/commit/798ee46b4a84ee6dfc756b001f33acbe0280d62f)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-45805
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-16 01:16:45 JST
- 更新日: 2026-07-16 03:15:13 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Penpotの2.15.0以前のバージョンにおいて、認証なしでJavaScriptコードをサーバー上で実行可能な脆弱な/excuteエンドポイントが存在します。  
- 影響: ネットワーク上の攻撃者が任意のJavaScriptをサーバーで実行できるため、リモートコード実行のリスクがあります。  
- 推奨対応: Penpotをバージョン2.15.0以降にアップデートし、脆弱なエンドポイントの利用を停止してください。

#### References
- https://github.com/penpot/penpot/commit/798ee46b4a84ee6dfc756b001f33acbe0280d62f
- https://github.com/penpot/penpot/issues/9518
- https://github.com/penpot/penpot/releases/tag/2.15.0
- https://github.com/penpot/penpot/security/advisories/GHSA-22qr-rp27-j9wm
- https://github.com/penpot/penpot/security/advisories/GHSA-22qr-rp27-j9wm

### [CVE-2026-50182](https://github.com/WWBN/AVideo/commit/f50fc033b7adb36f1ffd6640e7826468bdafdec3)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-50182
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-16 07:16:54 JST
- 更新日: 2026-07-16 07:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WWBN AVideoの29.0未満のバージョンにおいて、YouTubeAPIギャラリーページネーションの$_GET['search']パラメータが適切に処理されず、認証なしで反射型XSSが発生する脆弱性が存在します。  
- 影響: 攻撃者は細工したURLを用いて任意のJavaScriptを実行でき、管理者権限の乗っ取りや不正操作が可能になる恐れがあります。  
- 推奨対応: 最新バージョンへのアップデートを行い、該当の修正コミット(f50fc033b7adb36f1ffd6640e7826468bdafdec3)を適用してください。

#### References
- https://github.com/WWBN/AVideo/commit/f50fc033b7adb36f1ffd6640e7826468bdafdec3
- https://github.com/WWBN/AVideo/security/advisories/GHSA-hgjh-6wj8-gcgf

### [CVE-2026-50183](https://github.com/WWBN/AVideo/commit/7292129eaee5f609beae103b5cb387d55f17b877)

> **Frontend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-50183
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-16 07:16:54 JST
- 更新日: 2026-07-16 07:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WWBN AVideoのYouTubeAPIプラグイン（バージョン29.0以下）に、YouTube動画のタイトルを適切にエスケープしないことで発生する保存型クロスサイトスクリプティング（XSS）の脆弱性があります。  
- 影響: 悪意あるYouTubeアップローダーが動画タイトルにスクリプトを埋め込み、サイト訪問者のブラウザで任意のJavaScriptを実行可能で、管理者権限の乗っ取りも発生する恐れがあります。  
- 推奨対応: 最新バージョンへのアップデートや、YouTubeAPIから取得したタイトルのHTMLエスケープを適切に行う対策を実施してください。

#### References
- https://github.com/WWBN/AVideo/commit/7292129eaee5f609beae103b5cb387d55f17b877
- https://github.com/WWBN/AVideo/security/advisories/GHSA-66q5-cj5g-wrfx

### [CVE-2026-54443](https://github.com/lissy93/dashy/releases/tag/3.2.0)

> **Frontend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-54443
- 関連キーワード: javascript, vue, gin
- 影響製品: -
- 公開日: 2026-07-16 04:17:50 JST
- 更新日: 2026-07-16 05:17:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: DashyのRSSウィジェットがRSSアイテムのリンク値を適切にサニタイズせず、悪意あるjavascript: URIが実行される可能性があります。  
- 影響: 攻撃者が細工したRSSフィードを通じて、ユーザーのクリック時に任意のスクリプトが実行されるリスクがあります。  
- 推奨対応: Dashyをバージョン3.2.0以降にアップデートし、RSSウィジェットの脆弱性を修正してください。

#### References
- https://github.com/lissy93/dashy/releases/tag/3.2.0
- https://github.com/lissy93/dashy/security/advisories/GHSA-2x3v-qmgm-r8hv
- https://github.com/lissy93/dashy/security/advisories/GHSA-2x3v-qmgm-r8hv

### [CVE-2026-59954](https://github.com/apolloconfig/apollo/commit/310809d557e01c6803051736cd525e333ffe00ec)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59954
- 関連キーワード: apollo
- 影響製品: -
- 公開日: 2026-07-16 02:16:50 JST
- 更新日: 2026-07-16 03:16:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Apollo ConfigServiceの2.5.2未満のバージョンで、アクセキー認証時に非正規のappId変種が認証に利用可能で、不正アクセスの恐れがあります。  
- 影響: 認証済みでないユーザーが保護された設定データにアクセスできる可能性があります。  
- 推奨対応: バージョン2.5.2以降にアップデートし、認証処理の修正を適用してください。

#### References
- https://github.com/apolloconfig/apollo/commit/310809d557e01c6803051736cd525e333ffe00ec
- https://github.com/apolloconfig/apollo/releases/tag/v2.5.2
- https://github.com/apolloconfig/apollo/security/advisories/GHSA-4w3q-qpfq-v992

### [CVE-2026-59955](https://github.com/apolloconfig/apollo/commit/310809d557e01c6803051736cd525e333ffe00ec)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59955
- 関連キーワード: apollo
- 影響製品: -
- 公開日: 2026-07-16 02:16:51 JST
- 更新日: 2026-07-16 04:18:34 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Apollo ConfigServiceの2.5.2未満のバージョンで、認証処理の不備により未承認のユーザーが生の設定データにアクセスできる可能性があります。  
- 影響: 不正アクセスにより機密設定情報が漏洩するリスクがあります。  
- 推奨対応: バージョン2.5.2以降にアップデートし、認証処理の修正を適用してください。

#### References
- https://github.com/apolloconfig/apollo/commit/310809d557e01c6803051736cd525e333ffe00ec
- https://github.com/apolloconfig/apollo/releases/tag/v2.5.2
- https://github.com/apolloconfig/apollo/security/advisories/GHSA-h4pc-58cc-hc95

### [CVE-2026-9007](https://www.thalesgroup.com/en/search/cybersecurity/cybersecurity-services/CVE-2026-9007)

> **Frontend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-9007
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-16 01:16:52 JST
- 更新日: 2026-07-16 06:00:31 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: HCL Notesの特定バージョンにおいて、ウェブページ生成時の入力処理不備により反射型クロスサイトスクリプティング（XSS）が発生する可能性があります。  
- 影響: 攻撃者が他ユーザーのコンテキストで任意のJavaScriptを実行できるリスクがあります。  
- 推奨対応: 最新のセキュリティパッチ適用や入力検証の強化を検討してください。

#### References
- https://www.thalesgroup.com/en/search/cybersecurity/cybersecurity-services/CVE-2026-9007

### [CVE-2025-32781](https://github.com/apolloconfig/apollo/commit/362735ded4f13b62f6ab9df135d7096066e8e291)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2025-32781
- 関連キーワード: apollo
- 影響製品: -
- 公開日: 2026-07-16 02:16:45 JST
- 更新日: 2026-07-16 03:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Apollo Portal 2.5.0未満のバージョンで、認証済みユーザーが特定のリリースIDを用いて他のアプリケーションやネームスペースの設定情報を閲覧できる権限検証の不備が存在します。  
- 影響: 低権限ユーザーが他のサービスの機密設定情報を不正に取得できる可能性があります。  
- 推奨対応: Apollo Portalをバージョン2.5.0以降にアップデートし、権限検証の修正を適用してください。

#### References
- https://github.com/apolloconfig/apollo/commit/362735ded4f13b62f6ab9df135d7096066e8e291
- https://github.com/apolloconfig/apollo/pull/5378
- https://github.com/apolloconfig/apollo/releases/tag/v2.5.0
- https://github.com/apolloconfig/apollo/security/advisories/GHSA-jxpj-9j24-w337

### [CVE-2026-41580](https://github.com/Stirling-Tools/Stirling-PDF/releases/tag/v2.0.0)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-41580
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-16 01:16:45 JST
- 更新日: 2026-07-16 05:22:12 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Stirling-PDFの2.0.0未満のバージョンにおいて、PDFのタイトルや著者情報を適切にエンコードせずに表示する脆弱性があり、悪意あるPDFでクロスサイトスクリプティングが発生する可能性があります。  
- 影響: 攻撃者が細工したPDFを閲覧したユーザーのブラウザ上で任意のJavaScriptが実行されるリスクがあります。  
- 推奨対応: Stirling-PDFをバージョン2.0.0以降にアップデートし、適切なエンコード処理が行われていることを確認してください。

#### References
- https://github.com/Stirling-Tools/Stirling-PDF/releases/tag/v2.0.0
- https://github.com/Stirling-Tools/Stirling-PDF/security/advisories/GHSA-rjjx-43g5-mp76
- https://github.com/Stirling-Tools/Stirling-PDF/security/advisories/GHSA-rjjx-43g5-mp76

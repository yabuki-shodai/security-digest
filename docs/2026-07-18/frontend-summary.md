# Frontend CVE Summary (2026-07-18)

## Overview

- 取得日時: 2026-07-18 08:02:25 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 12
- Critical: 1
- High: 2
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-54335](https://github.com/feathersjs/feathers/commit/28b3c03c63bdbff53115fdaa46c56980e7942acc)

> **Frontend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-54335
- 関連キーワード: typescript, javascript
- 影響製品: -
- 公開日: 2026-07-18 07:17:44 JST
- 更新日: 2026-07-18 07:17:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Feathersjsのバージョン5.0.44以前において、_.merge関数がJSON.parseで生成されたオブジェクトの__proto__などの特殊キーを誤ってマージし、プロトタイプ汚染が発生する可能性があります。  
- 影響: 悪意ある入力により全てのプレーンオブジェクトのプロトタイプが汚染され、予期しない動作やセキュリティリスクが生じる恐れがあります。  
- 推奨対応: Feathersjsをバージョン5.0.45以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/feathersjs/feathers/commit/28b3c03c63bdbff53115fdaa46c56980e7942acc
- https://github.com/feathersjs/feathers/pull/3690
- https://github.com/feathersjs/feathers/releases/tag/v5.0.45
- https://github.com/feathersjs/feathers/security/advisories/GHSA-28xv-ph75-77wh

### [CVE-2026-54466](https://github.com/faye/websocket-driver-node/commit/5b197ca874dab58e96cacad8a3c256797d804680)

> **Frontend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-54466
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-18 06:17:08 JST
- 更新日: 2026-07-18 06:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: websocket-driverの0.7.5未満のバージョンで、WebSocketプロトコルのドラフト版フレーム形式において、長さヘッダーの不正な大きさの整数が精度喪失を引き起こし、ペイロードの誤解析を招く脆弱性が存在します。  
- 影響: 悪意あるクライアントからの細工されたデータにより、サーバー側でのメッセージ解析が誤り、予期しない動作やサービスの不安定化が発生する可能性があります。  
- 推奨対応: websocket-driverをバージョン0.7.5以降にアップデートし、脆弱性修正を適用してください。

#### References
- https://github.com/faye/websocket-driver-node/commit/5b197ca874dab58e96cacad8a3c256797d804680
- https://github.com/faye/websocket-driver-node/security/advisories/GHSA-xv26-6w52-cph6

### [CVE-2026-9585](https://labs.sra.io/posts/switchvox/)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-9585
- 関連キーワード: javascript, go, gin
- 影響製品: -
- 公開日: 2026-07-18 02:17:17 JST
- 更新日: 2026-07-18 03:04:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Sangoma Switchvox SMB Edition 8.3において、認証なしで発生するリフレクト型クロスサイトスクリプティング（XSS）脆弱性が存在します。  
- 影響: 攻撃者が悪意のあるスクリプトを被害者のブラウザ上で実行できる可能性があります。  
- 推奨対応: 公式のセキュリティアップデートを適用し、入力値の適切なサニタイズを実施してください。

#### References
- https://labs.sra.io/posts/switchvox/
- https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026

### [CVE-2026-9588](https://labs.sra.io/posts/switchvox/)

> **Frontend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-9588
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-07-18 02:17:18 JST
- 更新日: 2026-07-18 03:04:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Sangoma Switchvox SMB Edition 8.3の留守番電話通知テンプレート機能に保存型XSS脆弱性が存在します。  
- 影響: 認証ユーザーが悪意あるJavaScriptをテンプレートに埋め込み、他ユーザーに悪影響を及ぼす可能性があります。  
- 推奨対応: 最新のパッチ適用やテンプレート入力の適切なサニタイズを検討してください。

#### References
- https://labs.sra.io/posts/switchvox/
- https://sangomakb.atlassian.net/wiki/spaces/Switchvox/pages/1802371073/Switchvox+-+Release+Notes+Version+8.4.0.2+July+14+2026

### [CVE-2026-48015](https://github.com/shopware/shopware/commit/745a3ea3b77d4fe0f78c595ef527d8453a134497)

> **Frontend** / **MEDIUM** / CVSS: **4.9** / KEV: **no**

- タイトル: CVE-2026-48015
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-18 03:17:16 JST
- 更新日: 2026-07-18 04:17:15 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Shopwareの特定バージョンで、SVGファイルのアップロード時に内容のサニタイズが行われず、悪意あるJavaScriptが実行される可能性があります。  
- 影響: 悪意あるSVGファイルをアップロードすると、Shopwareドメイン内でスクリプトが実行されるリスクがあります。  
- 推奨対応: バージョン6.6.10.18または6.7.10.1以降にアップデートし、SVGファイルの安全な処理を確保してください。

#### References
- https://github.com/shopware/shopware/commit/745a3ea3b77d4fe0f78c595ef527d8453a134497
- https://github.com/shopware/shopware/commit/fd6d39bdb62dfa06fe62c7c87b37607d84094cda
- https://github.com/shopware/shopware/releases/tag/v6.6.10.18
- https://github.com/shopware/shopware/releases/tag/v6.7.10.1
- https://github.com/shopware/shopware/security/advisories/GHSA-xvhc-gm7j-mhmc

### [CVE-2026-49211](https://github.com/symfony/ux/commit/725ab3d40689c91ff19ad2d01940a30007769214)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-49211
- 関連キーワード: javascript, express
- 影響製品: -
- 公開日: 2026-07-18 02:17:15 JST
- 更新日: 2026-07-18 03:00:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Symfony UXのAutocompleteコンポーネントで、SQL LIKEワイルドカードが適切にエスケープされず、未認証ユーザーが広範な検索やブラインドブールオラクル攻撃を行える可能性があります。  
- 影響: 公開されているBaseEntityAutocompleteTypeエンドポイントを通じて、任意のカラムに対する情報漏洩や不正な検索が発生する恐れがあります。  
- 推奨対応: Symfony UXをバージョン2.36.0以降または3.1.0以降にアップデートし、修正済みのバージョンを利用してください。

#### References
- https://github.com/symfony/ux/commit/725ab3d40689c91ff19ad2d01940a30007769214
- https://github.com/symfony/ux/releases/tag/v2.36.0
- https://github.com/symfony/ux/releases/tag/v3.1.0
- https://github.com/symfony/ux/security/advisories/GHSA-946h-jp5c-8fvh

### [CVE-2026-49210](https://github.com/symfony/ux/commit/fbc5e9a1bda7e4556be21bb1d970f382760ed9a9)

> **Frontend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-49210
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-18 02:17:15 JST
- 更新日: 2026-07-18 03:00:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Symfony UXのLiveComponentで、子コンポーネントのタグ名を検証せずにHTMLに埋め込む脆弱性があり、任意のHTMLやスクリプトが挿入される可能性があります。  
- 影響: 悪意あるユーザーが任意のHTMLやJavaScriptを挿入でき、クロスサイトスクリプティング（XSS）攻撃のリスクがあります。  
- 推奨対応: Symfony UXをバージョン2.36.0以上または3.1.0以上にアップデートし、脆弱性修正を適用してください。

#### References
- https://github.com/symfony/ux/commit/fbc5e9a1bda7e4556be21bb1d970f382760ed9a9
- https://github.com/symfony/ux/releases/tag/v2.36.0
- https://github.com/symfony/ux/releases/tag/v3.1.0
- https://github.com/symfony/ux/security/advisories/GHSA-38x5-rcv4-xf7x

### [CVE-2026-49208](https://github.com/symfony/ux/commit/d24d78fda6df2d5964312255943ebf3a217b79a2)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-49208
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-18 02:17:15 JST
- 更新日: 2026-07-18 03:00:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Symfony UXのLivePropでDateTimeInterface型のプロパティに明示的なフォーマットが設定されていない場合、クライアントからの相対日時文字列が不正に処理される可能性があります。  
- 影響: 悪意のある入力により、時間に基づくビジネスロジックの検証を回避される恐れがあります。  
- 推奨対応: Symfony UXをバージョン2.36.0以降または3.1.0以降にアップデートし、明示的な日時フォーマットを設定してください。

#### References
- https://github.com/symfony/ux/commit/d24d78fda6df2d5964312255943ebf3a217b79a2
- https://github.com/symfony/ux/releases/tag/v2.36.0
- https://github.com/symfony/ux/releases/tag/v3.1.0
- https://github.com/symfony/ux/security/advisories/GHSA-89g7-22c8-3j23

### [CVE-2026-49209](https://github.com/symfony/ux/commit/95e878d5257f13d6d652ca95e3ef6bb0934d674f)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-49209
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-18 02:17:15 JST
- 更新日: 2026-07-18 03:17:16 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Symfony UXのBatchActionControllerで、認証済みクライアントが大量のアクションを含むリクエストを送信すると、サーバーのCPUやメモリ、データベース接続が枯渇する可能性があります。  
- 影響: サーバーリソースの過剰消費によるサービス拒否（DoS）状態が発生する恐れがあります。  
- 推奨対応: Symfony UXをバージョン2.36.0または3.1.0以降にアップデートし、リクエストのアクション数制限を適切に設定してください。

#### References
- https://github.com/symfony/ux/commit/95e878d5257f13d6d652ca95e3ef6bb0934d674f
- https://github.com/symfony/ux/releases/tag/v2.36.0
- https://github.com/symfony/ux/releases/tag/v3.1.0
- https://github.com/symfony/ux/security/advisories/GHSA-mm82-c99c-h2cf

### [CVE-2026-49212](https://github.com/symfony/ux/commit/a224b5af3e2e33ee14ac71356ae0e0877900a81c)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-49212
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-18 02:17:15 JST
- 更新日: 2026-07-18 03:17:16 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Symfony UXのLiveComponentHydratorで、HMACがコンポーネント名やスロット識別子を含まず、異なるコンポーネント間で署名済みデータのリプレイが可能になる問題。  
- 影響: 悪意あるユーザーが読み取り専用のプロパティを他のコンポーネントに設定できる可能性がある。  
- 推奨対応: Symfony UXをバージョン2.36.0以上または3.1.0以上にアップデートすること。

#### References
- https://github.com/symfony/ux/commit/a224b5af3e2e33ee14ac71356ae0e0877900a81c
- https://github.com/symfony/ux/releases/tag/v2.36.0
- https://github.com/symfony/ux/releases/tag/v3.1.0
- https://github.com/symfony/ux/security/advisories/GHSA-34w5-c283-j9fg

### [CVE-2026-49215](https://github.com/symfony/ux/commit/aed7493db2b4b7bf1f9c79b33cda544f06904b27)

> **Frontend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-49215
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-18 02:17:16 JST
- 更新日: 2026-07-18 04:17:16 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Symfony UXのLiveComponentSubscriberにおいて、特定のAcceptヘッダーを悪用したクロスオリジンの偽造リクエストが可能な脆弱性が存在します。  
- 影響: SameSite=Noneやcredentials: 'include'を使用するアプリケーションで、攻撃者が被害者のセッションを利用して不正なLiveActionリクエストを送信できる可能性があります。  
- 推奨対応: Symfony UXをバージョン2.36.0以降または3.1.0以降にアップデートし、該当の脆弱性を修正してください。

#### References
- https://github.com/symfony/ux/commit/aed7493db2b4b7bf1f9c79b33cda544f06904b27
- https://github.com/symfony/ux/releases/tag/v2.36.0
- https://github.com/symfony/ux/releases/tag/v3.1.0
- https://github.com/symfony/ux/security/advisories/GHSA-4m4j-hmqq-3gxm

### [CVE-2026-49216](https://github.com/symfony/ux/commit/842ae54bc74de389299f975f01aafae272cb0019)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-49216
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-18 02:17:16 JST
- 更新日: 2026-07-18 03:00:02 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Symfony UXのsymfony/ux-autocompleteにおいて、AJAXレスポンスの項目をHTMLテンプレートリテラルに直接埋め込むことで、攻撃者が制御するマークアップが実行される可能性があります。  
- 影響: 悪意のあるユーザーが提供したドロップダウン値により、クロスサイトスクリプティング（XSS）が発生し、他のユーザーのブラウザで任意のスクリプトが実行される恐れがあります。  
- 推奨対応: symfony/ux-autocompleteをバージョン2.36.0以降または3.1.0以降にアップデートし、適切なサニタイズ処理を適用してください。

#### References
- https://github.com/symfony/ux/commit/842ae54bc74de389299f975f01aafae272cb0019
- https://github.com/symfony/ux/releases/tag/v2.36.0
- https://github.com/symfony/ux/releases/tag/v3.1.0
- https://github.com/symfony/ux/security/advisories/GHSA-mwqm-4fw3-cjvr

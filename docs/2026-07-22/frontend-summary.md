# Frontend CVE Summary (2026-07-22)

## Overview

- 取得日時: 2026-07-22 08:08:14 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 7
- Critical: 0
- High: 5
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-44907](https://github.com/react/react/security/advisories/GHSA-wx67-qw84-cm4g)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-44907
- 関連キーワード: react, webpack, turbopack
- 影響製品: -
- 公開日: 2026-07-22 02:17:08 JST
- 更新日: 2026-07-22 05:25:45 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 特殊に細工されたHTTPリクエストを送信することで、react-server-dom関連パッケージにおいてサービス拒否（DoS）状態を引き起こす脆弱性が存在します。  
- 影響: react-server-dom-webpack、react-server-dom-parcel、react-server-dom-turbopackの特定バージョンで過剰なCPU使用率が発生し、サービスの可用性が低下する可能性があります。  
- 推奨対応: 該当パッケージのバージョンを確認し、ベンダーからの修正パッチやアップデートが提供されている場合は速やかに適用することを検討してください。

#### References
- https://github.com/react/react/security/advisories/GHSA-wx67-qw84-cm4g

### [CVE-2026-46681](https://github.com/nevware21/ts-utils/commit/5e887f4e2fbee7160c8f501634c45e6a229e83bb)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-46681
- 関連キーワード: typescript, javascript
- 影響製品: -
- 公開日: 2026-07-22 00:16:35 JST
- 更新日: 2026-07-22 01:17:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: @nevware21/ts-utilsの_copyProps関数が、Object.hasOwnPropertyチェックを行わず危険なキーをフィルタリングしないため、プロトタイプ汚染の脆弱性が存在します。  
- 影響: 悪意のある入力によりアプリケーション内の全オブジェクトのプロトタイプチェーンが汚染され、予期しない動作やセキュリティリスクが発生する可能性があります。  
- 推奨対応: バージョン0.14.0以降にアップデートし、_copyProps関数の脆弱性修正を適用してください。

#### References
- https://github.com/nevware21/ts-utils/commit/5e887f4e2fbee7160c8f501634c45e6a229e83bb
- https://github.com/nevware21/ts-utils/security/advisories/GHSA-x7j8-49r8-mr43
- https://github.com/nevware21/ts-utils/security/advisories/GHSA-x7j8-49r8-mr43

### [CVE-2026-47687](https://github.com/FOGProject/fogproject/security/advisories/GHSA-hg23-3w27-2rf2)

> **Frontend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-47687
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-22 06:16:50 JST
- 更新日: 2026-07-22 06:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: FOGの特定バージョンで、未エスケープのユーザー入力が管理画面のドロップダウンに反映され、認証不要の攻撃者が任意のJavaScriptを管理者のブラウザで実行可能な脆弱性が存在します。  
- 影響: 管理者権限を持つユーザーのブラウザでクロスサイトスクリプティング（XSS）が発生し、情報漏洩やセッション乗っ取りのリスクがあります。  
- 推奨対応: FOGをバージョン1.5.10.1832または1.6.0-beta.2313以降にアップデートし、未エスケープの入力処理を修正してください。

#### References
- https://github.com/FOGProject/fogproject/security/advisories/GHSA-hg23-3w27-2rf2

### [CVE-2026-55081](https://github.com/dhis2/dhis2-core/pull/24158)

> **Frontend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-55081
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-22 04:17:10 JST
- 更新日: 2026-07-22 04:44:19 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: DHIS2のOpenAPI HTMLエンドポイントで、`scope`クエリパラメータの値が適切にサニタイズされずに反映されるため、クロスサイトスクリプティング（XSS）が発生する可能性があります。  
- 影響: 攻撃者が細工したURLをユーザーに開かせることで、ユーザーのブラウザ上で任意のJavaScriptが実行される恐れがあります。  
- 推奨対応: DHIS2を2.42.5.1、2.43.0.1以降のパッチ適用済みバージョンに更新し、セキュリティ修正を適用してください。

#### References
- https://github.com/dhis2/dhis2-core/pull/24158
- https://github.com/dhis2/dhis2-core/pull/24159
- https://github.com/dhis2/dhis2-core/pull/24160
- https://github.com/dhis2/dhis2-core/pull/24161
- https://github.com/dhis2/dhis2-core/pull/24162

### [CVE-2026-47671](https://github.com/nhost/nhost/commit/e407511627d2c2c1137a70e9ca1ca31095d23479)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-47671
- 関連キーワード: graphql, gin
- 影響製品: -
- 公開日: 2026-07-22 05:17:01 JST
- 更新日: 2026-07-22 05:17:01 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Nhost CLIの1.46.0未満のバージョンで、ローカル開発環境の`nhost configserver`が認証不備と緩いCORS設定により、ローカルの機密情報が外部から読み書き可能になる問題。  
- 影響: 開発者のローカル環境にあるプロジェクト管理用の秘密情報やJWT署名キー、Webhook秘密情報などが漏洩・改ざんされる恐れがある。  
- 推奨対応: Nhost CLIをバージョン1.46.0以降にアップデートし、ローカル開発環境の設定を見直すこと。

#### References
- https://github.com/nhost/nhost/commit/e407511627d2c2c1137a70e9ca1ca31095d23479
- https://github.com/nhost/nhost/pull/4302
- https://github.com/nhost/nhost/releases/tag/cli@1.46.0
- https://github.com/nhost/nhost/security/advisories/GHSA-64cj-qvx5-m4f3

### [CVE-2026-47689](https://github.com/FOGProject/fogproject/security/advisories/GHSA-fqgf-j2gh-92cm)

> **Frontend** / **MEDIUM** / CVSS: **4.6** / KEV: **no**

- タイトル: CVE-2026-47689
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-22 06:16:50 JST
- 更新日: 2026-07-22 06:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: FOGの特定バージョンにおいて、HTMLエスケープ処理が不十分なため、未認証の攻撃者がMACアドレスを知っていれば悪意あるスクリプトを管理者のブラウザで実行可能な脆弱性が存在します。  
- 影響: 管理者のブラウザ上で任意のHTML/JavaScriptが実行され、情報漏洩や操作の乗っ取りリスクがあります。  
- 推奨対応: バージョン1.5.10.1832または1.6.0-beta.2313以降にアップデートし、適切な入力検証とエスケープ処理を適用してください。

#### References
- https://github.com/FOGProject/fogproject/security/advisories/GHSA-fqgf-j2gh-92cm

### [CVE-2026-65056](https://github.com/geo-chen/oss/blob/main/mcp-webresearch.md)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-65056
- 関連キーワード: playwright
- 影響製品: -
- 公開日: 2026-07-22 06:16:54 JST
- 更新日: 2026-07-22 06:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: mcp-webresearch 0.1.7にサーバーサイドリクエストフォージェリ（SSRF）の脆弱性があり、内部ネットワークのサービスに不正アクセスされる可能性があります。  
- 影響: 攻撃者が内部のクラウドメタデータサービスなどにアクセスし、機密情報や認証情報が漏洩する恐れがあります。  
- 推奨対応: URLのプロトコルだけでなく、プライベートIPや予約済みIPレンジのフィルタリングを実装し、最新バージョンへのアップデートやアクセス制御の強化を検討してください。

#### References
- https://github.com/geo-chen/oss/blob/main/mcp-webresearch.md
- https://www.npmjs.com/package/@mzxrai/mcp-webresearch
- https://www.vulncheck.com/advisories/mcp-webresearch-server-side-request-forgery-in-visit-page-due-to-missing-internal-ip-filtering

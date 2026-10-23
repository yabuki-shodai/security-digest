# Backend CVE Summary (2026-10-23)

## Overview

- 取得日時: 2026-10-23 09:35:54 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 22
- Critical: 0
- High: 12
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-114644](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-114644
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:38 JST
- 更新日: 2026-10-23 07:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The MongoDB C# Driver's BSON library contains an uncontrolled resource consumption weakness in its deserialization handling of one BSON value type. An application that deserializes untrusted content with the library retains data derived from that content for the lifetime of the process, with no limit on how much accumu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0
- https://github.com/mongodb/mongo-csharp-driver/security/advisories/GHSA-x24v-h3xm-qf9x
- https://jira.mongodb.org/browse/CSHARP-6162

### [CVE-2026-114653](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-114653
- 関連キーワード: go, express, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:39 JST
- 更新日: 2026-10-23 07:18:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A client-side encryption schema construction component in the MongoDB C# Driver places caller-supplied field identifiers into a position that is interpreted as a pattern expression, without normalizing or validating them. As a result, an application that designates certain fields for client-side field-level encryption...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0
- https://github.com/mongodb/mongo-csharp-driver/security/advisories/GHSA-ggmm-wc43-vphh
- https://jira.mongodb.org/browse/CSHARP-6174

### [CVE-2026-115450](https://github.com/MarcosCamara01/ecommerce-template/commit/e6b364cd668f2ba875cfa7f6d55c63e771715df7)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-115450
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-23 01:17:35 JST
- 更新日: 2026-10-23 02:40:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: External Control of Assumed-Immutable Web Parameter (CWE-472) in the cart and checkout flow of MarcosCamara01 Ecommerce Template allows an authenticated user with no special privileges to be charged the price of one product while placing an order for another, because POST /api/user/cart accepts variantId, which determi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/MarcosCamara01/ecommerce-template/commit/e6b364cd668f2ba875cfa7f6d55c63e771715df7
- https://secur0.com/en/cna/cve-list/cve-2026-115450-price-manipulation-stripe-checkout

### [CVE-2026-114648](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-114648
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:38 JST
- 更新日: 2026-10-23 07:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The MongoDB C# Driver does not neutralize dot and dollar characters in dictionary keys, field names and array-filter identifiers used in LINQ queries before placing them into the field paths it sends to the server. An application user whose input reaches these positions can redirect a query or update to fields the appl...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0
- https://github.com/mongodb/mongo-csharp-driver/security/advisories/GHSA-2xqr-fxmx-2cmf
- https://jira.mongodb.org/browse/CSHARP-6181

### [CVE-2026-114649](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-114649
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:38 JST
- 更新日: 2026-10-23 06:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The MongoDB C# Driver compares TLS client certificates by issuer and serial number only when deciding whether two clients can share cached connections. In an application that creates clients from certificates supplied by different users, a user who provides a certificate copying another user's issuer and serial number,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0
- https://github.com/mongodb/mongo-csharp-driver/security/advisories/GHSA-6gjm-424r-3jh2
- https://jira.mongodb.org/browse/CSHARP-6184

### [CVE-2026-114652](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-114652
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:39 JST
- 更新日: 2026-10-23 06:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A data-query-logic neutralization weakness in the update-statement construction component of the MongoDB C# Driver can cause application-supplied values to be interpreted as query/update logic rather than as literal data. An application user who can influence the content of values that the application passes into the a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0
- https://github.com/mongodb/mongo-csharp-driver/security/advisories/GHSA-7gfh-w7g4-x3p9
- https://jira.mongodb.org/browse/CSHARP-6168

### [CVE-2026-114610](https://github.com/py-pdf/fpdf2/commit/d7bd1061205d50da6a541dadfdb9d66beb763f2f)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-114610
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-10-23 03:17:28 JST
- 更新日: 2026-10-23 03:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: fpdf2 is a PDF creation library for Python. From 2.5.0 until 2.8.8, fpdf2's SVGObject.build_xref() passes nested SVG <use> references to GraphicsContext.add_item(), whose default clone=True deep-copy behavior copies the complete referenced graphics tree during FPDF.image() processing. Repeating references at each nesti...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/py-pdf/fpdf2/commit/d7bd1061205d50da6a541dadfdb9d66beb763f2f
- https://github.com/py-pdf/fpdf2/pull/1889
- https://github.com/py-pdf/fpdf2/releases/tag/2.8.8
- https://github.com/py-pdf/fpdf2/security/advisories/GHSA-wqw6-wpr3-45rh

### [CVE-2026-114647](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-114647
- 関連キーワード: go, gin, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:38 JST
- 更新日: 2026-10-23 07:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB C# DriverのFindOneAndReplace処理における、$`で始まるフィールド名の検証不足。
- 影響: 置換ではなく更新演算子が適用され、一致したドキュメントの内容が予期せず変更される可能性があります。
- 推奨対応: 修正版ドライバに更新するか、ユーザー入力のフィールド名に$`が含まれないよう入力検証を実施してください。

#### References
- https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0
- https://github.com/mongodb/mongo-csharp-driver/security/advisories/GHSA-68cj-624m-mxj3
- https://jira.mongodb.org/browse/CSHARP-6186

### [CVE-2026-114651](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-114651
- 関連キーワード: go, gin, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:39 JST
- 更新日: 2026-10-23 06:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A memory-handling weakness in the BSON deserialization component of the MongoDB C# Driver may cause data left over from previously processed content to be returned when specially crafted serialized input is parsed. An unauthenticated party able to supply serialized data to an application that maps certain primitive col...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0
- https://github.com/mongodb/mongo-csharp-driver/security/advisories/GHSA-f8xm-c88f-wq46
- https://jira.mongodb.org/browse/CSHARP-6170

### [CVE-2026-115347](https://github.com/lepture/mistune/security/advisories/GHSA-f32h-38gf-rg5r)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-115347
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-23 04:17:40 JST
- 更新日: 2026-10-23 04:17:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mistune before 3.3.0 contains an inefficient algorithmic complexity vulnerability in parse_link_text that allows remote attackers to cause denial of service through unbalanced square brackets. Attackers can submit markdown containing long runs of unmatched brackets to mistune.html(), triggering repeated forward scans t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/lepture/mistune/security/advisories/GHSA-f32h-38gf-rg5r
- https://www.vulncheck.com/advisories/mistune-before-3.3.0-quadratic-denial-of-service-via-parse-link-text

### [CVE-2026-115348](https://github.com/lepture/mistune/security/advisories/GHSA-x2gr-6qf2-fc9x)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-115348
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-23 04:17:40 JST
- 更新日: 2026-10-23 04:17:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mistune from 3.0.0 before 3.3.0 contains an algorithmic complexity vulnerability in the inline link parser's parse_link_text function that allows unauthenticated attackers to exhaust CPU with unbalanced brackets. Attackers can submit Markdown containing many unbalanced '[' or '![' characters, forcing repeated unbounded...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/lepture/mistune/security/advisories/GHSA-x2gr-6qf2-fc9x
- https://www.vulncheck.com/advisories/mistune-before-3.3.0-quadratic-time-dos-via-parse-link-text

### [CVE-2026-115349](https://github.com/lepture/mistune/security/advisories/GHSA-3q64-rw38-243v)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-115349
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-23 04:17:40 JST
- 更新日: 2026-10-23 04:17:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mistune from 3.0.0 before 3.3.0 contains an algorithmic complexity denial of service vulnerability in the parse_link_text function in src/mistune/helpers.py. Attackers can submit markdown with deeply nested square brackets triggering quadratic parsing time, exhausting server CPU with small crafted requests.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/lepture/mistune/security/advisories/GHSA-3q64-rw38-243v
- https://www.vulncheck.com/advisories/mistune-3.0.0-before-3.3.0-denial-of-service-via-nested-bracket-parsing

### [CVE-2026-115352](https://github.com/lepture/mistune/security/advisories/GHSA-xrpv-r66x-8p7j)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-115352
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-23 04:17:41 JST
- 更新日: 2026-10-23 04:17:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mistune before 3.3.0 contains an algorithmic complexity vulnerability in the inline link parser that allows unauthenticated attackers to exhaust CPU by submitting long runs of unmatched '[' characters. Attackers can send small markdown payloads that trigger O(N^2) parse_link_text and parse_link_label probing, occupying...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/lepture/mistune/security/advisories/GHSA-xrpv-r66x-8p7j
- https://www.vulncheck.com/advisories/mistune-before-3.3.0-quadratic-time-dos-via-unmatched-brackets-in-inline-parser

### [CVE-2026-115388](https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-c9gc-w9vx-w86p)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-115388
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-23 04:17:46 JST
- 更新日: 2026-10-23 04:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Wasmtimeのwasmtime-wasi-httpにおけるWASIp2送信HTTPボディの書き込み上限チェック不備。
- 影響: 悪意のあるゲストが大きなバッファを書き込むことでホストのメモリが圧迫され、DoS（サービス拒否）状態に陥る可能性があります。
- 推奨対応: Wasmtimeを 36.0.16、37.0.0（48.0.3以上）、49.0.1 以降の修正バージョンへ更新してください。

#### References
- https://github.com/bytecodealliance/wasmtime/security/advisories/GHSA-c9gc-w9vx-w86p
- https://www.vulncheck.com/advisories/wasmtime-before-36.0.16-37.0.0-before-48.0.3-and-49.0.0-before-49.0.1-memory-exhaustion-dos-via-wasmtime-wasi-http-outgoing-body-write

### [CVE-2026-114643](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-114643
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:37 JST
- 更新日: 2026-10-23 07:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB C# DriverにおけるGeoJSON追加メンバーと予約語の重複未チェック。
- 影響: 同じレコードで異なる値が解釈されたり、データが読み取り不能になってアプリケーション処理が中断する可能性があります。
- 推奨対応: 修正版ドライバへ更新するか、追加メンバーに予約語（type, coordinates等）が使用されないようバリデーションを行ってください。

#### References
- https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0
- https://github.com/mongodb/mongo-csharp-driver/security/advisories/GHSA-mqvm-xxqr-vqw5
- https://jira.mongodb.org/browse/CSHARP-6179

### [CVE-2026-114645](https://github.com/mongodb/mongo-c-driver/releases/tag/1.30.14)

> **Backend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-114645
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:38 JST
- 更新日: 2026-10-23 06:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Windows環境向けMongoDB C DriverのKerberos/SSPI認証コードにおける32ビット整数ラップアラウンド。
- 影響: 極端に長い認証情報が指定された場合にヒープバッファオーバーフローが発生し、メモリ破壊やアプリのDoSを引き起こす可能性があります。
- 推奨対応: 修正版ドライバへ更新するか、クライアント設定に渡す認証情報の長さを制限してください。

#### References
- https://github.com/mongodb/mongo-c-driver/releases/tag/1.30.14
- https://github.com/mongodb/mongo-c-driver/releases/tag/2.5.7
- https://github.com/mongodb/mongo-c-driver/security/advisories/GHSA-g9mw-2cwh-6hh9
- https://jira.mongodb.org/browse/CDRIVER-6421

### [CVE-2026-114646](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-114646
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:38 JST
- 更新日: 2026-10-23 07:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB C# DriverのBSONシリアル化処理におけるデータサイズ宣言の検証欠如。
- 影響: 未認証の攻撃者がDBコマンドへ要素を挿入・削除させ、データの不正改ざんや意図しない情報漏洩を引き起こす可能性があります。
- 推奨対応: 修正版ドライバへ更新し、外部から供給されるバイナリデータの事前検証を徹底してください。

#### References
- https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0
- https://github.com/mongodb/mongo-csharp-driver/security/advisories/GHSA-5chr-phc4-wcj2
- https://jira.mongodb.org/browse/CSHARP-6157

### [CVE-2026-114650](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-114650
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:38 JST
- 更新日: 2026-10-23 07:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB .NET/C# ドライバのクライアントサイドフィールドレベル暗号化（CSFLE）処理における内部エンコーディング変換の不備。
- 影響: 暗号化ルールが正しく認識されず、暗号化対象の機密データが平文のままデータベースに保存される可能性があります。
- 推奨対応: 修正版ドライバへ更新し、暗号化設定およびテキストエンコーディング構成を確認してください。

#### References
- https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0
- https://github.com/mongodb/mongo-csharp-driver/security/advisories/GHSA-jvpx-6w8x-h6rg
- https://jira.mongodb.org/browse/CSHARP-6180

### [CVE-2026-114654](https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-114654
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-23 04:17:39 JST
- 更新日: 2026-10-23 07:18:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MongoDB C# DriverのBSON処理における数値型変換処理の不備による整合性チェックの回避。
- 影響: 不正なバイナリデータが保存され、その後の読み込み時にエラーが発生したり、データが誤って短く解釈される可能性があります。
- 推奨対応: 修正版ドライバへ更新してください。

#### References
- https://github.com/mongodb/mongo-csharp-driver/releases/tag/v3.13.0
- https://github.com/mongodb/mongo-csharp-driver/security/advisories/GHSA-5h2q-6c9r-7x25
- https://jira.mongodb.org/browse/CSHARP-6166

### [CVE-2026-114655](https://github.com/mongodb/libmongocrypt/releases/tag/1.21.1)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-114655
- 関連キーワード: go, aws
- 影響製品: -
- 公開日: 2026-10-23 04:17:40 JST
- 更新日: 2026-10-23 06:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libmongocryptにおけるKMS（AWS/Azure/GCP）リクエスト構築時のパラメータ検証・サニタイズ不足。
- 影響: キーボルトへの書き込み権限を持つユーザーがKMSリクエスト構造を改ざんし、意図しない鍵管理操作を実行させる可能性があります。
- 推奨対応: 修正版のlibmongocryptへ更新してください。

#### References
- https://github.com/mongodb/libmongocrypt/releases/tag/1.21.1
- https://github.com/mongodb/libmongocrypt/security/advisories/GHSA-7mvq-mg47-m88j
- https://jira.mongodb.org/browse/MONGOCRYPT-963

### [CVE-2026-114605](https://github.com/rthalley/dnspython/commit/b485e460c266540a1a09ca6d8d1d7b685b1d3023)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-114605
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-23 02:16:58 JST
- 更新日: 2026-10-23 02:40:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: dnspythonのDNS圧縮ポインタ解析処理における無限ループ対策（ホップ制限）の欠如。
- 影響: 悪意のあるDNSメッセージを解析する際、過度なポインタ追跡が発生してCPUが高負荷となり、DoS状態に陥る可能性があります。
- 推奨対応: dnspython 2.9.0 以降のバージョンへ更新してください。

#### References
- https://github.com/rthalley/dnspython/commit/b485e460c266540a1a09ca6d8d1d7b685b1d3023
- https://github.com/rthalley/dnspython/releases/tag/v2.9.0
- https://github.com/rthalley/dnspython/security/advisories/GHSA-45c3-73f7-pv4m

### [CVE-2026-114613](https://github.com/msgpack/msgpack-python/commit/620b0eb4c89cd72d4098564537624d9dbb2ce141)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-114613
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-23 04:17:37 JST
- 更新日: 2026-10-23 04:17:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MessagePack Python C拡張（msgpack._cmsgpack）におけるデシリアライズ失敗時のメモリリーク。
- 影響: 不正な入力を繰り返しデシリアライズすることでメモリが解放されずに増大し、DoS状態に陥る可能性があります。
- 推奨対応: msgpack 1.2.3 以降のバージョンへ更新してください。

#### References
- https://github.com/msgpack/msgpack-python/commit/620b0eb4c89cd72d4098564537624d9dbb2ce141
- https://github.com/msgpack/msgpack-python/releases/tag/v1.2.3
- https://github.com/msgpack/msgpack-python/security/advisories/GHSA-j586-36cw-2gc2

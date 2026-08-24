# Frontend CVE Summary (2026-08-25)

## Overview

- 取得日時: 2026-08-25 07:38:59 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 5
- Critical: 0
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-78391](https://github.com/RansomLook/RansomLook/commit/7efb59253f23552538f9a11c9bf21e7bcfcc1319)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-78391
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-25 00:16:48 JST
- 更新日: 2026-08-25 00:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RansomLookの暗号通貨ウォレット詳細画面において、外部由来のデータに対する検証およびJavaScriptコンテキストでの適切なエスケープ処理が不足している不具合が存在します。
- 影響: ユーザーが影響を受けるウォレットのCSVエクスポートボタンをクリックした際、任意のJavaScriptが実行される可能性があります。
- 推奨対応: 入力データの適切な検証とJavaScript出力時のエスケープ処理を実施するか、修正版への更新を検討してください。

#### References
- https://github.com/RansomLook/RansomLook/commit/7efb59253f23552538f9a11c9bf21e7bcfcc1319

### [CVE-2026-39915](https://tim-doc.atlassian.net/wiki/spaces/eng/pages/230981636/Release+Notes)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-39915
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-25 00:16:38 JST
- 更新日: 2026-08-25 02:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TIM Flow（バージョン26.0.6未満）の `rt` URLパラメータにCRLFインジェクションの脆弱性が存在します。
- 影響: 攻撃者が任意のHTTPヘッダやボディを注入し、セッショントークンの窃取やアカウント情報の改ざんを引き起こす可能性があります。
- 推奨対応: TIM Flowをバージョン26.0.6以降へアップデートしてください。

#### References
- https://tim-doc.atlassian.net/wiki/spaces/eng/pages/230981636/Release+Notes
- https://www.vulncheck.com/advisories/tim-flow-crlf-injection-via-rt-parameter

### [CVE-2026-77384](https://github.com/libp2p/js-libp2p/commit/4bb8fbe8d3f3590e4af51a1f5f7de56fffa5804d)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-77384
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-25 07:17:19 JST
- 更新日: 2026-08-25 07:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JavaScript版libp2p（4.2.9未満）の予約更新処理において、リクエストごとにイベントリスナーが無制限に登録される不具合が存在します。
- 影響: 遠隔の対話相手から繰り返しリクエストを受信することでメモリやリスナーが肥大化し、リレーサーバーがサービス拒否（DoS）状態に陥る可能性があります。
- 推奨対応: libp2pをバージョン4.2.9以降へアップデートしてください。

#### References
- https://github.com/libp2p/js-libp2p/commit/4bb8fbe8d3f3590e4af51a1f5f7de56fffa5804d
- https://github.com/libp2p/js-libp2p/releases/tag/circuit-relay-v2-v4.2.9
- https://github.com/libp2p/js-libp2p/security/advisories/GHSA-x787-gh7p-hmq7

### [CVE-2026-78414](https://support.networkoptix.com/hc/en-us/articles/42950508518679-Security-Advisory-Cross-Site-Scripting-XSS-in-Merge-with-Another-Site-Dropdown)

> **Frontend** / **HIGH** / CVSS: **8.0** / KEV: **no**

- タイトル: CVE-2026-78414
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-25 00:16:48 JST
- 更新日: 2026-08-25 06:17:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Network Optix Nx Witness VMS（6.1.3未満）のWeb管理画面において、サイト名にスクリプトが挿入されるクロスサイトスクリプティング（XSS）の脆弱性が存在します。
- 影響: 隣接ネットワーク上の攻撃者により、認証済み管理者のブラウザで任意のJavaScriptが実行され、セッショントークンが窃取されてアカウントを乗っ取られる可能性があります。
- 推奨対応: Nx Witness VMSをバージョン6.1.3以降へアップデートしてください。

#### References
- https://support.networkoptix.com/hc/en-us/articles/42950508518679-Security-Advisory-Cross-Site-Scripting-XSS-in-Merge-with-Another-Site-Dropdown

### [CVE-2026-71503](https://codeant.ai/security-research/cve-2026-71503-reflected-xss-via-the-type-parameter)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-71503
- 関連キーワード: javascript, echo
- 影響製品: -
- 公開日: 2026-08-25 04:16:49 JST
- 更新日: 2026-08-25 05:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dolibarr（24.0.0未満）の管理用テンプレートにおいて、`type` パラメータに対するJavaScriptコンテキストのエンコード不足およびCSP未設定による反射型XSSの脆弱性が存在します。
- 影響: 管理者が細工されたURLを開いた場合、そのセッション内で任意コードが実行され、永続的な管理者アカウントが作成される可能性があります。
- 推奨対応: Dolibarrをバージョン24.0.0以降へアップデートしてください。

#### References
- https://codeant.ai/security-research/cve-2026-71503-reflected-xss-via-the-type-parameter
- https://github.com/Dolibarr/dolibarr/commit/3094b0aa3b500ff51020b660a7e66ffcb9d1cd91
- https://github.com/Dolibarr/dolibarr/releases/tag/24.0.0
- https://www.vulncheck.com/advisories/dolibarr-reflected-xss-via-extra-fields-administration-template

# Backend CVE Summary (2026-10-16)

## Overview

- 取得日時: 2026-10-16 09:19:16 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 14
- Critical: 0
- High: 7
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-77470](https://github.com/LycheeOrg/Lychee/commit/24e6e11f1da131ed20b192d7d7b7ca9084451a2f)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-77470
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-16 02:17:27 JST
- 更新日: 2026-10-16 06:08:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Lychee (7.7.1未満) のチェックアウト処理における、パラメータオーバーライド（上書き）の脆弱性。
- 影響: 未認証の購入者が支払い金額などのパラメータを改ざんし、不正に低い金額で注文を正常完了させる可能性があります。
- 推奨対応: Lychee をバージョン 7.7.1 以降に更新してください。

#### References
- https://github.com/LycheeOrg/Lychee/commit/24e6e11f1da131ed20b192d7d7b7ca9084451a2f
- https://github.com/LycheeOrg/Lychee/pull/4514
- https://github.com/LycheeOrg/Lychee/releases/tag/v7.7.1
- https://github.com/LycheeOrg/Lychee/security/advisories/GHSA-476v-jr53-8rxc
- https://github.com/LycheeOrg/Lychee/security/advisories/GHSA-476v-jr53-8rxc

### [CVE-2026-58391](https://github.com/opnsense/core/commit/5e6313f50546474031805039e209830b63b2b0e4)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-58391
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-16 01:18:18 JST
- 更新日: 2026-10-16 06:08:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OPNsense (26.1.11未満) の Firewall Rules および NAT ビューにおける、title 属性生成時の引用符エスケープ不備（XSS）。
- 影響: 権限を持つユーザーが不正な属性を注入し、対象ルールを閲覧した管理者のセッション上でJavaScriptを実行させ、CSRFトークンの取得や不正操作を行わせる可能性があります。
- 推奨対応: OPNsense をバージョン 26.1.11 以降に更新してください。

#### References
- https://github.com/opnsense/core/commit/5e6313f50546474031805039e209830b63b2b0e4
- https://github.com/opnsense/core/commit/fb3b8a07f407ce281b1dde748706acbb0bc514ce
- https://github.com/opnsense/core/security/advisories/GHSA-2xrm-p255-p43h
- https://hackerask.com/posts/opnsense

### [CVE-2026-100350](https://github.com/getkin/kin-openapi/commit/d090e36b2f1c42c898ba2a687a8f6e25f5ca727f)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-100350
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-10-16 01:17:30 JST
- 更新日: 2026-10-16 04:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kin-openapi (0.145.0〜0.146.0未満) の deepObject クエリ解析における、正規表現の不必要な繰り返し再コンパイル処理。
- 影響: 未認証のリモート攻撃者が多数のクエリキーを含むリクエストを送信することで、過剰なCPU・メモリリソースを消費させ（DoS）、パフォーマンスを低減させる可能性があります。
- 推奨対応: kin-openapi をバージョン 0.146.0 以降に更新してください。

#### References
- https://github.com/getkin/kin-openapi/commit/d090e36b2f1c42c898ba2a687a8f6e25f5ca727f
- https://github.com/getkin/kin-openapi/releases/tag/v0.146.0
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-h4r5-mxv5-8mjc
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-h4r5-mxv5-8mjc

### [CVE-2026-109841](https://cna.openjsf.org/security-advisories.html)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-109841
- 関連キーワード: go, node.js
- 影響製品: -
- 公開日: 2026-10-16 04:17:21 JST
- 更新日: 2026-10-16 05:38:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Node.js 用 HTTP クライアント undici の fetch() 実装における、Subresource Integrity (SRI) トークンの大文字小文字検証不備。
- 影響: 大文字や混合ケースのSRIトークンが無視され、改ざんされたレスポンスが検証を通過して完全性が損なわれる可能性があります。
- 推奨対応: undici をバージョン 7.30.1 または 8.12.2 以降に更新してください。

#### References
- https://cna.openjsf.org/security-advisories.html
- https://github.com/nodejs/undici/security/advisories/GHSA-f72v-6w45-q472

### [CVE-2026-100349](https://github.com/getkin/kin-openapi/commit/f5441d67f855ed34d975b3b85665764644ab1459)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-100349
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-16 01:17:30 JST
- 更新日: 2026-10-16 01:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kin-openapi (0.146.0未満) の openapi3filter.ValidateResponse において、schema ではなく content が宣言されたレスポンスヘッダーの検証時に nil スキーマが処理関数へ引き渡される問題。
- 影響: レスポンス検証時に nil ポインタ参照によるパニックが発生し、サービスの可用性に影響（DoS）を及ぼす可能性がある。
- 推奨対応: kin-openapi をバージョン 0.146.0 以降に更新する。

#### References
- https://github.com/getkin/kin-openapi/commit/f5441d67f855ed34d975b3b85665764644ab1459
- https://github.com/getkin/kin-openapi/releases/tag/v0.146.0
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-74vm-87hj-r66f

### [CVE-2026-100351](https://github.com/getkin/kin-openapi/commit/eda80e2676e9f577ceed2dd80e64f16083edb041)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-100351
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-16 01:17:31 JST
- 更新日: 2026-10-16 02:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kin-openapi (0.144.0 以上 0.147.0 未満) の openapi3filter.ValidationHandler と gorilla/mux ルーターとの間で、デコード済みパスの評価不一致が発生する問題。
- 影響: エンコードされたパス区切り文字を含むリクエストにより、保護されたルートの認証機能（AuthenticationFunc）をバイパスしてアクセスされる可能性がある。
- 推奨対応: kin-openapi をバージョン 0.147.0 以降に更新する。

#### References
- https://github.com/getkin/kin-openapi/commit/eda80e2676e9f577ceed2dd80e64f16083edb041
- https://github.com/getkin/kin-openapi/releases/tag/v0.147.0
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-23vg-4cjm-66q5
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-23vg-4cjm-66q5

### [CVE-2026-100352](https://github.com/getkin/kin-openapi/commit/4487f198ab8be0c37d6ca72c54f5dca4dc25270e)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-100352
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-16 01:17:31 JST
- 更新日: 2026-10-16 01:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kin-openapi (0.148.0未満) の OpenAPI 3.1 バリデーションにおいて、YAML の NaN や infinity 数値に対するガード処理が行われずに依存ライブラリへ渡される問題。
- 影響: 未認証のリモート攻撃者が特定の YAML リクエストを送信することで nil 参照パニックを誘発し、プロセス停止などの DoS 状態を引き起こす可能性がある。
- 推奨対応: kin-openapi をバージョン 0.148.0 以降に更新する。

#### References
- https://github.com/getkin/kin-openapi/commit/4487f198ab8be0c37d6ca72c54f5dca4dc25270e
- https://github.com/getkin/kin-openapi/releases/tag/v0.148.0
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-rj39-cv6w-8wv7

### [CVE-2026-100353](https://github.com/getkin/kin-openapi/commit/9814d1f2b212f3508bf52296aa9e248b2122a5a9)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-100353
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-16 02:17:07 JST
- 更新日: 2026-10-16 02:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kin-openapi (0.136.0 以上 0.149.0 未満) の openapi3filter において、特定の配列スキーマ処理時に nil ガードが欠落している問題。
- 影響: 未認証のリモート攻撃者が配列クエリパラメータや複合リクエストボディを送信することで nil ポインタパニック（DoS）を引き起こす可能性がある。
- 推奨対応: kin-openapi をバージョン 0.149.0 以降に更新する。

#### References
- https://github.com/getkin/kin-openapi/commit/9814d1f2b212f3508bf52296aa9e248b2122a5a9
- https://github.com/getkin/kin-openapi/releases/tag/v0.149.0
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-vrcc-3ch7-hppw

### [CVE-2026-100354](https://github.com/getkin/kin-openapi/commit/9245cef66c840e27a08409a8a5cd0ee930c5bcff)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-100354
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-16 02:17:07 JST
- 更新日: 2026-10-16 04:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kin-openapi (0.149.0未満) の実行時検証において、allOf/anyOf/oneOf による循環参照の検出処理が欠如している問題。
- 影響: 循環参照を含むリクエストまたはレスポンス処理時に無限再帰が発生し、スタックオーバーフローにより Go プロセス全体が強制終了（DoS）する可能性がある。
- 推奨対応: kin-openapi をバージョン 0.149.0 以降に更新する。

#### References
- https://github.com/getkin/kin-openapi/commit/9245cef66c840e27a08409a8a5cd0ee930c5bcff
- https://github.com/getkin/kin-openapi/releases/tag/v0.149.0
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-g8cf-rcjf-c8cf
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-g8cf-rcjf-c8cf

### [CVE-2026-97394](https://github.com/getkin/kin-openapi/commit/30e292371a89ca6d1f91a9553e0aa518b49f838d)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-97394
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-16 01:18:25 JST
- 更新日: 2026-10-16 01:18:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kin-openapi (0.136.0 以上 0.143.0 未満) の openapi3filter において、items キーワードを持たない OpenAPI 3.1 配列スキーマの処理時に nil ポインタを参照してしまう問題。
- 影響: 未認証のリモート攻撃者が該当する操作へリクエストを送信することで、デコード時に nil ポインタパニック（DoS）を発生させる可能性がある。
- 推奨対応: kin-openapi をバージョン 0.143.0 以降に更新する。

#### References
- https://github.com/getkin/kin-openapi/commit/30e292371a89ca6d1f91a9553e0aa518b49f838d
- https://github.com/getkin/kin-openapi/releases/tag/v0.143.0
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-p6wj-qrr4-pgh5

### [CVE-2026-102631](https://bugs.launchpad.net/ubuntu/+source/authd/+bug/2168531)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-102631
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-16 02:17:10 JST
- 更新日: 2026-10-16 02:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: authd (0.7.1未満) の UpdateUser 処理において、IDプロバイダ（IdP）の Provider ID による照合に失敗した際のユーザー名フォールバック処理が不適切である問題。
- 影響: IdPで再割り当てされた電子メールアドレスを持つ新規ユーザーが、旧ユーザーのローカル UID やホームディレクトリ、認証情報（SSHキー等）にアクセス・改ざん可能になる恐れがある。
- 推奨対応: authd をバージョン 0.7.1 以降に更新する。回避策として、IdPアカウント削除時に対応するローカルアカウントをロックまたは削除する。

#### References
- https://bugs.launchpad.net/ubuntu/+source/authd/+bug/2168531
- https://github.com/canonical/authd/pull/2067
- https://ubuntu.com/security/CVE-2026-102631

### [CVE-2026-58395](https://github.com/opnsense/core/commit/631e14721b311badc1d3c0d29321e4d42585156b)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-58395
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-10-16 01:18:18 JST
- 更新日: 2026-10-16 06:08:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OPNsense (26.1.11未満) の ApiMutableModelControllerBase::delBase() において、URLからの削除トークンを検証前に XPath 式に直接挿入してしまう不具合。
- 影響: モジュール削除権限を持つユーザーが特工されたトークンを送信することで、権限外のモジュールを含む設定情報（名前、UUID等）を漏洩させる可能性がある。
- 推奨対応: OPNsense をバージョン 26.1.11 以降に更新する。

#### References
- https://github.com/opnsense/core/commit/631e14721b311badc1d3c0d29321e4d42585156b
- https://github.com/opnsense/core/commit/d7054cef69f72588feac1091254960835be19dfe
- https://github.com/opnsense/core/security/advisories/GHSA-98h6-479q-9q3w
- https://hackerask.com/posts/opnsense
- https://github.com/opnsense/core/security/advisories/GHSA-98h6-479q-9q3w

### [CVE-2026-100347](https://github.com/getkin/kin-openapi/commit/f1a5b523b82868d2d9be2e116b4e942892be72c3)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-100347
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-16 01:17:30 JST
- 更新日: 2026-10-16 02:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kin-openapi (0.145.0未満) の openapi3filter.ValidationHandler において、既存の静的パスに対して非標準または未対応の HTTP メソッドが送信された際の処理に問題がある不具合。
- 影響: 未認証のリモート攻撃者が特定メソッドを繰り返し送信することで認証前にパニックを誘発し、接続切断や大量のログ出力（DoS）を引き起こす可能性がある。
- 推奨対応: kin-openapi をバージョン 0.145.0 以降に更新する。

#### References
- https://github.com/getkin/kin-openapi/commit/f1a5b523b82868d2d9be2e116b4e942892be72c3
- https://github.com/getkin/kin-openapi/releases/tag/v0.145.0
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-fh4f-47mf-f2gj
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-fh4f-47mf-f2gj

### [CVE-2026-105660](https://cna.erlef.org/cves/CVE-2026-105660.html)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-105660
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-16 04:17:16 JST
- 更新日: 2026-10-16 04:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Bandit (Elixir HTTP サーバー) において、HTTP/1 リクエストターゲットの authority に含まれるホスト名およびポートの構文検証が不十分な不具合。
- 影響: 未認証のリモート攻撃者が RFC 3986 規格外の不適切なホスト値や制御文字、範囲外ポートをアプリケーション側（conn.host 等）へ注入できる可能性がある。
- 推奨対応: 修正済みの最新バージョンへ更新するか、アプリケーション側で適切な入力検証を実施する。

#### References
- https://cna.erlef.org/cves/CVE-2026-105660.html
- https://github.com/mtrudel/bandit/commit/0e3edda0edf6322e9164b827c6d3ddecd080ff2e
- https://github.com/mtrudel/bandit/commit/6ea80210137b3f69caf65f67398934259dc365d0
- https://github.com/mtrudel/bandit/security/advisories/GHSA-v53v-9hvg-37jf
- https://osv.dev/vulnerability/EEF-CVE-2026-105660

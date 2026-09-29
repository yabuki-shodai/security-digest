# Frontend CVE Summary (2026-09-29)

## Overview

- 取得日時: 2026-09-29 10:51:14 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 16
- Critical: 0
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-101100](https://github.com/ag-ui-protocol/ag-ui/)

> **Frontend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-101100
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-09-29 03:17:16 JST
- 更新日: 2026-09-29 06:03:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ag-uiのFilterToolCallsMiddlewareにおける処理後の不完全なクリーンアップの脆弱性。
- 影響: 遠隔の攻撃者により特定操作が行われた場合、データや内部状態のクリーンアップが不完全になる可能性がある。
- 推奨対応: バージョン2026-09-08以降への更新、または指定の修正パッチの適用を検討してください。

#### References
- https://github.com/ag-ui-protocol/ag-ui/
- https://github.com/ag-ui-protocol/ag-ui/commit/c346119fe870b70f5c19738ee5119f3e1456e59d
- https://github.com/ag-ui-protocol/ag-ui/issues/2443
- https://github.com/ag-ui-protocol/ag-ui/pull/2494
- https://github.com/ag-ui-protocol/ag-ui/releases/tag/release/2026-09-08

### [CVE-2026-101903](https://github.com/axios/axios/commit/d19040bda7a8be2f82c3c6e1a5bc03917daee39a)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-101903
- 関連キーワード: javascript, gin, node.js, express
- 影響製品: -
- 公開日: 2026-09-29 03:17:18 JST
- 更新日: 2026-09-29 03:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Axiosにおける正規表現のバックトラッキングに起因するサービス拒否（DoS）の脆弱性。
- 影響: 不正な形式のデータURLを処理する際、JavaScriptの正規表現エンジンで過度なバックトラッキングが発生し、Node.jsのイベントループがブロックされてサービス不能に陥る可能性がある。
- 推奨対応: Axiosをバージョン1.20.0以降へ更新してください。

#### References
- https://github.com/axios/axios/commit/d19040bda7a8be2f82c3c6e1a5bc03917daee39a
- https://github.com/axios/axios/pull/11141
- https://github.com/axios/axios/releases/tag/v1.20.0
- https://github.com/axios/axios/security/advisories/GHSA-c29m-xwm3-cm6r
- https://github.com/axios/axios/security/advisories/GHSA-c29m-xwm3-cm6r

### [CVE-2026-75600](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-79rg-3xp6-rqq6)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-75600
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-09-29 03:17:24 JST
- 更新日: 2026-09-29 03:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreePBXのGraphQL APIモジュールにおけるコマンド注入による任意のシェルコマンド実行の脆弱性。
- 影響: APIモジュールへのアクセス権を持つ認証済み攻撃者が、ホストパラメータを介して不正なコマンドを注入し、サービス実行権限（通常はasterisk）で任意のコマンドを実行する可能性がある。
- 推奨対応: FreePBXをバージョン17.0.9以降へ更新してください。

#### References
- https://github.com/FreePBX/security-reporting/security/advisories/GHSA-79rg-3xp6-rqq6

### [CVE-2026-101916](https://github.com/grpc/grpc-node/commit/2a84ec8b01b9db68ed9d2b117a53a81449edb8ee)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-101916
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-29 06:17:13 JST
- 更新日: 2026-09-29 06:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: @grpc/grpc-jsにおけるクライアント証明書の検証処理不備による不適切な認証の脆弱性。
- 影響: requireClientCertificateがfalseに設定されている場合、未認証の証明書が認証済みとして誤認識され、アクセス制御がバイパスされる可能性がある。
- 推奨対応: @grpc/grpc-jsをバージョン1.13.6または1.14.5以降へ更新してください。

#### References
- https://github.com/grpc/grpc-node/commit/2a84ec8b01b9db68ed9d2b117a53a81449edb8ee
- https://github.com/grpc/grpc-node/commit/b4e0079c6d22a2adedfcac748e0bc083f783bc7c
- https://github.com/grpc/grpc-node/releases/tag/@grpc/grpc-js%401.14.5
- https://github.com/grpc/grpc-node/security/advisories/GHSA-m9gg-hp2v-232j

### [CVE-2026-48100](https://github.com/polybase/payy/security/advisories/GHSA-fhxc-63vg-9gwr)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-48100
- 関連キーワード: rollup
- 影響製品: -
- 公開日: 2026-09-29 02:17:49 JST
- 更新日: 2026-09-29 03:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Payy zk-rollupにおける検証回路の未検証公開入力に起因する健全性判定の欠陥。
- 影響: 証明者が不正なバーンメッセージを含む証明を作成・送信することで、契約から資金が不正に引き出される可能性がある。
- 推奨対応: Payyをバージョン1.3.0以降へ更新してください。

#### References
- https://github.com/polybase/payy/security/advisories/GHSA-fhxc-63vg-9gwr
- https://github.com/polybase/payy/security/advisories/GHSA-fhxc-63vg-9gwr

### [CVE-2026-101111](https://www.ordasoft.com/)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-101111
- 関連キーワード: javascript, echo
- 影響製品: -
- 公開日: 2026-09-29 04:16:47 JST
- 更新日: 2026-09-29 04:16:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla用拡張機能Book Library (Free)における反射型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: リクエストパラメータのエスケープ漏れにより、攻撃者の用意したURLをアクセスさせることで任意のHTMLやJavaScriptが実行される可能性がある。
- 推奨対応: Book Library (Free)をバージョン6.4.6以降へ更新してください。

#### References
- https://www.ordasoft.com/

### [CVE-2026-102333](https://github.com/cle-b/httpdbg)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-102333
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-29 08:17:01 JST
- 更新日: 2026-09-29 08:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: httpdbgのWebインターフェースにおけるURLスキームの検証不備に起因するクロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 記録された`javascript:`スキームのリンクをユーザーがクリックすることで、攻撃者のスクリプトが実行され、キャプチャされたリクエスト・レスポンスデータやトークンが窃取される可能性がある。
- 推奨対応: httpdbgをバージョン2.2.1以降へ更新してください。

#### References
- https://github.com/cle-b/httpdbg
- https://github.com/cle-b/httpdbg/blob/v2.2.0/httpdbg/hooks/recordhttp2.py#L88-L97
- https://github.com/cle-b/httpdbg/blob/v2.2.0/httpdbg/webapp/static/index.htm#L302
- https://github.com/cle-b/httpdbg/commit/121845b41c19ddaf30b51be0797bc2ff4847d8b3
- https://github.com/cle-b/httpdbg/issues/220

### [CVE-2026-102372](https://gestsup.fr/index.php?page=changelog)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-102372
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-29 10:16:44 JST
- 更新日: 2026-09-29 10:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GestSupのIMAPコネクタにおけるメール本文のサニタイズ不足による格納型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 未認証の攻撃者が悪意のあるメールを送信することで、チケット内に任意のJavaScriptを挿入し、閲覧した管理者のブラウザ上でスクリプトを実行させてデータの窃取や不正操作を行う可能性がある。
- 推奨対応: GestSupをバージョン3.2.62以降へ更新してください。

#### References
- https://gestsup.fr/index.php?page=changelog
- https://gestsup.fr/index.php?page=download
- https://gestsup.fr/index.php?page=download&channel=stable&version=3.2.62&type=patch
- https://www.vulncheck.com/advisories/gestsup-before-3.2.62-stored-xss-via-email-body-in-login-imap-connector

### [CVE-2026-100370](https://github.com/rhukster/dom-sanitizer/commit/10f97807e4501d60f63987f2e76a38cdbf312dcb)

> **Frontend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-100370
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-29 06:17:10 JST
- 更新日: 2026-09-29 06:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DOMSanitizer is a DOM/SVG/MathML Sanitizer for PHP 7.3+. Prior to version 1.0.15, the isDangerousUrl() method is responsible for rejecting dangerous URL values in the href and xlink:href attributes. The weakness is that "javascript:" is rejected as a scheme, while "data:" is rejected only when the literal substring onl...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/rhukster/dom-sanitizer/commit/10f97807e4501d60f63987f2e76a38cdbf312dcb
- https://github.com/rhukster/dom-sanitizer/commit/fb8f758b41134fc5fb2f563666f2330c69e31f94
- https://github.com/rhukster/dom-sanitizer/releases/tag/1.0.15
- https://github.com/rhukster/dom-sanitizer/security/advisories/GHSA-wcj2-r6vg-rm97
- https://github.com/rhukster/dom-sanitizer/security/advisories/GHSA-wcj2-r6vg-rm97

### [CVE-2026-101910](https://github.com/beaugunderson/ip-address/commit/ab3dc88bcf5374344168a2ba075ca7ac4ff257f8)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-101910
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-29 03:17:20 JST
- 更新日: 2026-09-29 04:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ip-addressライブラリにおける特定IPv6範囲（NAT64）のプライベート判定漏れによる認可バイパスの脆弱性。
- 影響: NAT64ローカル使用範囲のアドレスが外部アドレスとして誤認識され、信頼境界やアクセス制限の判定をバイパスされる可能性がある。
- 推奨対応: ip-addressをバージョン10.5.1以降へ更新してください。

#### References
- https://github.com/beaugunderson/ip-address/commit/ab3dc88bcf5374344168a2ba075ca7ac4ff257f8
- https://github.com/beaugunderson/ip-address/releases/tag/v10.5.1
- https://github.com/beaugunderson/ip-address/security/advisories/GHSA-2vr4-cq9g-pvrc
- https://github.com/beaugunderson/ip-address/security/advisories/GHSA-2vr4-cq9g-pvrc

### [CVE-2026-101911](https://github.com/beaugunderson/ip-address/commit/469ead1231b4cc059f2150c626e1e0c2895c0134)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-101911
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-29 03:17:20 JST
- 更新日: 2026-09-29 03:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ip-address is a library for parsing and manipulating IPv4 and IPv6 addresses in JavaScript. Prior to 10.7.1, the Address6 constructor, Address6.isValid, and parse code in src/ipv6.ts accept unbounded strings and expand invalid characters through RE_BAD_CHARACTERS into large diagnostics. Material impact occurs only when...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/beaugunderson/ip-address/commit/469ead1231b4cc059f2150c626e1e0c2895c0134
- https://github.com/beaugunderson/ip-address/commit/8b34a21e0839b37c094066816fb2c2c48a2adcf5
- https://github.com/beaugunderson/ip-address/releases/tag/v10.7.1
- https://github.com/beaugunderson/ip-address/security/advisories/GHSA-h3mg-xc3c-68pw

### [CVE-2026-101912](https://github.com/beaugunderson/ip-address/commit/1343629d57fea413644a5c9d41ff1e59619f3f28)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-101912
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-29 03:17:21 JST
- 更新日: 2026-09-29 05:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ip-address is a library for parsing and manipulating IPv4 and IPv6 addresses in JavaScript. Prior to 10.7.1, the isInSubnet and isHostInSubnet methods in src/common.ts compare masked binary strings without validating that both operands use the same IP family. A cross-family containment check whose leading address bits...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/beaugunderson/ip-address/commit/1343629d57fea413644a5c9d41ff1e59619f3f28
- https://github.com/beaugunderson/ip-address/releases/tag/v10.7.1
- https://github.com/beaugunderson/ip-address/security/advisories/GHSA-j6r3-76f7-8jcv
- https://github.com/beaugunderson/ip-address/security/advisories/GHSA-j6r3-76f7-8jcv

### [CVE-2026-101913](https://github.com/beaugunderson/ip-address/commit/d03e960c7cc3179ef25c8a44b4f94dd499625546)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-101913
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-29 03:17:21 JST
- 更新日: 2026-09-29 04:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ip-address is a library for parsing and manipulating IPv4 and IPv6 addresses in JavaScript. Prior to 10.5.1, the Address6 isLinkLocal method in src/ipv6.ts recognizes only fe80::/64 instead of the complete fe80::/10 IPv6 link-local range. An attacker-controlled address elsewhere in fe80::/10 can therefore pass a trust-...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/beaugunderson/ip-address/commit/d03e960c7cc3179ef25c8a44b4f94dd499625546
- https://github.com/beaugunderson/ip-address/releases/tag/v10.5.1
- https://github.com/beaugunderson/ip-address/security/advisories/GHSA-rpw4-54j3-4h4q
- https://github.com/beaugunderson/ip-address/security/advisories/GHSA-rpw4-54j3-4h4q

### [CVE-2026-101914](https://github.com/grpc/grpc-node/commit/6cf64b596da03f1942a6b168998f0670217a99c4)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-101914
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-29 05:17:09 JST
- 更新日: 2026-09-29 05:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: @grpc/grpc-jsのRBACパス照合における完全一致と前方一致の処理不備による誤認可の脆弱性。
- 影響: 大文字小文字を区別しない照合において、メソッド名が他のメソッド名のプレフィックスとなっている場合、不適切なアクセスルールが適用されて不正なアクセスを許可してしまう可能性がある。
- 推奨対応: @grpc/grpc-jsをバージョン1.13.1または1.14.1以降へ更新してください。

#### References
- https://github.com/grpc/grpc-node/commit/6cf64b596da03f1942a6b168998f0670217a99c4
- https://github.com/grpc/grpc-node/commit/a6c5b31180cc8cea94d0a5ea215ce31a49e0409f
- https://github.com/grpc/grpc-node/commit/f32f3712e44581d8dfc8359bd8d30096662f4c75
- https://github.com/grpc/grpc-node/releases/tag/@grpc/grpc-js-xds%401.13.1
- https://github.com/grpc/grpc-node/releases/tag/@grpc/grpc-js-xds%401.14.1

### [CVE-2026-102374](https://gestsup.fr/index.php?page=changelog)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-102374
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-29 10:16:44 JST
- 更新日: 2026-09-29 10:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GestSup versions before 3.2.62 contain a stored cross-site scripting vulnerability in the IMAP OAuth connector that double-decodes MIME-encoded email subjects after HTML escaping. Unauthenticated attackers can send crafted emails to monitored mailboxes with nested MIME encoded-words to inject JavaScript that executes i...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gestsup.fr/index.php?page=changelog
- https://gestsup.fr/index.php?page=download
- https://gestsup.fr/index.php?page=download&channel=stable&version=3.2.62&type=patch
- https://www.vulncheck.com/advisories/gestsup-before-3.2.62-stored-xss-via-double-decoded-email-subject-in-oauth-imap-connector

### [CVE-2026-101915](https://github.com/grpc/grpc-node/commit/350de32860428cc62473a00bee4035360690ffea)

> **Frontend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-101915
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-29 05:17:09 JST
- 更新日: 2026-09-29 05:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: @grpc/grpc-js implements the core functionality of gRPC purely in JavaScript, without a C++ addon. Prior to 1.13.6 and 1.14.5, when an application method handler throws an uncaught error, the server includes its error message in the status message sent to the client. The thrown error message is transmitted to the clien...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/grpc/grpc-node/commit/350de32860428cc62473a00bee4035360690ffea
- https://github.com/grpc/grpc-node/commit/7c5c5181159c6ddd292805881ef2cdec29bb475f
- https://github.com/grpc/grpc-node/commit/e8329b122ca99ba10877e990c2f6edd40224fd0d
- https://github.com/grpc/grpc-node/releases/tag/@grpc/grpc-js%401.13.6
- https://github.com/grpc/grpc-node/releases/tag/@grpc/grpc-js%401.14.5

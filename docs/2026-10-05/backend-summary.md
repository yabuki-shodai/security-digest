# Backend CVE Summary (2026-10-05)

## Overview

- 取得日時: 2026-10-05 09:50:02 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 15
- Critical: 7
- High: 6
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-105216](https://github.com/micro/go-micro)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-105216
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-05 03:16:34 JST
- 更新日: 2026-10-05 03:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: go-micro（バージョン6.0.0未満）における、共有TLSヘルパーでデフォルトで証明書検証が無効化されている不適切な証明書検証の脆弱性。
- 影響: 中間者（MitM）攻撃者により通信が傍受・改ざんされ、認証トークンや認証情報などの機密データが漏洩する可能性があります。
- 推奨対応: go-micro 6.0.0 以降へのアップデートが推奨されます。

#### References
- https://github.com/micro/go-micro
- https://github.com/micro/go-micro/blob/v5.30.0/internal/util/tls/tls.go#L43-L67
- https://github.com/micro/go-micro/commit/c7657f73f45cf839e643db10f28703eeab7299c3
- https://github.com/micro/go-micro/issues/2963
- https://www.vulncheck.com/advisories/go-micro-before-6.0.0-disabled-tls-certificate-verification-via-tls-config-helper

### [CVE-2026-105222](https://github.com/alexpechkarev/google-maps)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-105222
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-05 08:16:59 JST
- 更新日: 2026-10-05 08:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Laravelパッケージ「alexpechkarev/google-maps」（バージョン12.16以前）における、デフォルトでTLS証明書検証が無効化されている脆弱性。
- 影響: 通信経路上にいる攻撃者によってGoogle Maps Webサービスへのリクエストが傍受され、APIキーの窃取やレスポンスの改ざんが行われる可能性があります。
- 推奨対応: 修正プログラムの適用、または設定ファイルでTLS証明書検証を有効にする対策が推奨されます。

#### References
- https://github.com/alexpechkarev/google-maps
- https://github.com/alexpechkarev/google-maps/blob/v12.14/src/WebService.php#L267-L269
- https://github.com/alexpechkarev/google-maps/blob/v12.16/src/config/googlemaps.php#L28
- https://github.com/alexpechkarev/google-maps/issues/123
- https://www.vulncheck.com/advisories/alexpechkarev-google-maps-through-12.16-disabled-tls-certificate-verification-via-ssl-verify-peer

### [CVE-2026-105218](https://github.com/go-pay/gopay)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-105218
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-05 03:16:34 JST
- 更新日: 2026-10-05 03:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: gopay（バージョン1.5.119未満）のdefaultClient()においてTLS証明書検証が無効化されている脆弱性。
- 影響: 中間者攻撃者により決済プロバイダーAPIの通信が傍受・改ざんされ、加盟店の認証情報や取引データの漏洩、決済・返金応答の改ざんが行われる可能性があります。
- 推奨対応: gopay 1.5.119 以降へのアップデートが推奨されます。

#### References
- https://github.com/go-pay/gopay
- https://github.com/go-pay/gopay/blob/v1.5.118/pkg/xhttp/client.go#L15-L37
- https://github.com/go-pay/gopay/commit/f6df04fd4f64a2ad2c303ba063b6502bfdd259fd
- https://github.com/go-pay/gopay/issues/540
- https://www.vulncheck.com/advisories/gopay-before-1.5.119-disabled-tls-certificate-verification-in-xhttp-client

### [CVE-2026-105214](https://github.com/zitadel/zitadel/security/advisories/GHSA-93hm-8q29-c8cr)

> **Backend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-105214
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-05 00:16:32 JST
- 更新日: 2026-10-05 00:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zitadel（バージョン4.16.2未満）の組織ドメインHTTP検証処理におけるサーバーサイドリクエストフォージェリ（SSRF）の脆弱性。
- 影響: 攻撃者によりサーバーから内部リソースやクラウドメタデータアドレスへリクエストが送信され、内部ポートスキャンやネットワーク情報の取得が行われる可能性があります。
- 推奨対応: Zitadel 4.16.2 以降へのアップデートが推奨されます。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-93hm-8q29-c8cr
- https://www.vulncheck.com/advisories/zitadel-before-4.16.2-ssrf-via-organization-domain-http-verification

### [CVE-2026-105163](https://github.com/advisories/GHSA-mf7q-r4rv-jv94)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-105163
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-05 07:16:58 JST
- 更新日: 2026-10-05 07:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: crossplane-runtime（バージョン2.2.2および2.3.2以前）のImageConfigコンポーネントにおけるTOCTOU（Time-of-Check Time-of-Use）の脆弱性。
- 影響: 遠隔の攻撃者によって確認時と使用時のタイミングの隙を悪用され、予期しない動作を引き起こされる可能性があります。
- 推奨対応: crossplane-runtime 2.2.3、2.3.3、または 2.4.0-rc.1 以降へのアップデートが推奨されます。

#### References
- https://github.com/advisories/GHSA-mf7q-r4rv-jv94
- https://github.com/crossplane/crossplane-runtime/
- https://github.com/crossplane/crossplane-runtime/commit/bee99c6cd6ca81878acca2940a2f0a02169fc208
- https://github.com/crossplane/crossplane-runtime/pull/1038
- https://github.com/crossplane/crossplane-runtime/releases/tag/v2.2.3

### [CVE-2026-105158](https://gitee.com/RainyGao/DocSys/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-105158
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-10-05 00:16:31 JST
- 更新日: 2026-10-05 00:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RainyGao DocSys（バージョン2.02.85以前）のデータベース管理機能におけるSQLインジェクションの脆弱性。
- 影響: 遠隔の攻撃者によってurl引数を操作され、データベース上で不正なSQL命令を実行される可能性があります。
- 推奨対応: 入力値の制限などの緩和策を実施し、公式からの修正アップデートの提供を監視することが推奨されます。

#### References
- https://gitee.com/RainyGao/DocSys/
- https://gitee.com/RainyGao/DocSys/issues/IK8NEU
- https://vuldb.com/cve/CVE-2026-105158
- https://vuldb.com/submit/953425
- https://vuldb.com/vuln/413377

### [CVE-2026-105211](https://github.com/zitadel/zitadel/security/advisories/GHSA-3gwm-5wx8-4gm6)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-105211
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-05 00:16:32 JST
- 更新日: 2026-10-05 00:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADEL（バージョン4.17.1未満）のLogin V2における不適切なOTPコード処理に起因する認証バイパスの脆弱性。
- 影響: 未認証の攻撃者がサーバーレスポンスからOTPコードを取得し、多要素認証を突破して管理者アカウント等を含むアカウント乗っ取りを行う可能性があります。
- 推奨対応: ZITADEL 4.17.1 以降へのアップデートが推奨されます。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-3gwm-5wx8-4gm6
- https://www.vulncheck.com/advisories/zitadel-before-4.17.1-authentication-bypass-via-login-v2-otp-returncode

### [CVE-2026-105215](https://github.com/zitadel/zitadel/security/advisories/GHSA-738m-7888-jfv8)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-105215
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-05 00:16:32 JST
- 更新日: 2026-10-05 00:16:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADEL（バージョン3.4.14未満、および4.xの4.16.2未満）のLogin V1 UIにおける認証バイパスの脆弱性。
- 影響: 未認証の攻撃者により被害者の外部IdPアイデンティティに紐づくアカウントが事前に作成され、正規ユーザーのログインセッションをのっとられる可能性があります。
- 推奨対応: ZITADEL 3.4.14 または 4.16.2 以降へのアップデートが推奨されます。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-738m-7888-jfv8
- https://www.vulncheck.com/advisories/zitadel-before-4.16.2-account-pre-hijacking-via-forged-external-idp-callback

### [CVE-2026-105221](https://github.com/defunkt/gist)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-105221
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-05 08:16:59 JST
- 更新日: 2026-10-05 08:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RubyGem「gist」（バージョン6.1.0未満）におけるTLS証明書検証の不備（VERIFY_NONEの適用）による脆弱性。
- 影響: 通信経路上の攻撃者によりGitHub API通信が傍受・改ざんされ、OAuthトークンやログイン情報の窃取、gistの閲覧・改ざんが行われる可能性があります。
- 推奨対応: gist 6.1.0 以降へのアップデートが推奨されます。

#### References
- https://github.com/defunkt/gist
- https://github.com/defunkt/gist/blob/v6.0.0/lib/gist.rb#L466-L468
- https://github.com/defunkt/gist/commit/07ccc1a6d46e9d36f0e85d0b1c5d795890ae6bcf
- https://github.com/defunkt/gist/issues/373
- https://www.vulncheck.com/advisories/gist-rubygem-before-6.1.0-disabled-tls-certificate-verification

### [CVE-2026-105207](https://github.com/zitadel/zitadel/security/advisories/GHSA-g8gj-gq47-xgf4)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-105207
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-05 00:16:31 JST
- 更新日: 2026-10-05 00:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADELにおける外部Identity Provider（IdP）連携時の検証不備の脆弱性。
- 影響: 未認証の攻撃者が被害者のログイン名を知ることで、自身の外部IdPアカウントを被害者のアカウントに紐付け、不正ログインする可能性があります。
- 推奨対応: 修正済みのバージョン（3.4.16以降および4.17.3以降など）へ更新してください。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-g8gj-gq47-xgf4
- https://www.vulncheck.com/advisories/zitadel-before-4.17.3-account-takeover-via-external-idp-linking

### [CVE-2026-105212](https://github.com/zitadel/zitadel/security/advisories/GHSA-45f2-5q3r-xgg6)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-105212
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-05 00:16:32 JST
- 更新日: 2026-10-05 00:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADELのLogin UIにおける、一次認証前のPasskey等登録に起因する認証バイパスの脆弱性。
- 影響: 未認証の攻撃者が被害者のログイン名のみで自身の認証器を登録し、パスワードやMFAを迂回して被害者としてログインする可能性があります。
- 推奨対応: 修正済みのバージョン（3.4.14以降および4.16.2以降）へ更新してください。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-45f2-5q3r-xgg6
- https://www.vulncheck.com/advisories/zitadel-before-3.4.14-and-4.16.2-account-takeover-via-passkey-enrollment

### [CVE-2026-105219](https://github.com/mwilliamson/mammoth.js)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-105219
- 関連キーワード: node.js, express
- 影響製品: -
- 公開日: 2026-10-05 03:16:34 JST
- 更新日: 2026-10-05 03:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mammoth.jsのスタイルマップトークナイザーにおける正規表現の不備によるReDoSの脆弱性。
- 影響: 悪意のある.docxファイルを処理させることでNode.jsのイベントループがブロックされ、サービス拒否（DoS）状態に陥る可能性があります。
- 推奨対応: Mammoth.jsをバージョン1.12.3以降へ更新してください。

#### References
- https://github.com/mwilliamson/mammoth.js
- https://github.com/mwilliamson/mammoth.js/blob/1.12.2/lib/styles/parser/tokeniser.js#L6-L30
- https://github.com/mwilliamson/mammoth.js/commit/dc49225425c2c07de0a6dc3529f2386c82a032b4
- https://github.com/mwilliamson/mammoth.js/issues/487
- https://www.vulncheck.com/advisories/mammoth-js-1.3.0-before-1.12.3-redos-via-style-map-tokeniser

### [CVE-2026-105208](https://github.com/zitadel/zitadel/security/advisories/GHSA-jh3m-cr2x-qp88)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-105208
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-05 00:16:31 JST
- 更新日: 2026-10-05 00:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADELにおけるIdP intentトークンの暗号化強度不備（改ざん可能）による脆弱性。
- 影響: 認証済み攻撃者が自身のトークンを改ざんし、他人のIdPトークンを窃取したりセッションをハイジャックする可能性があります。
- 推奨対応: 修正済みのバージョン（3.4.16以降および4.17.3以降など）へ更新してください。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-jh3m-cr2x-qp88
- https://www.vulncheck.com/advisories/zitadel-before-4.17.3-session-hijacking-via-forgeable-idp-intent-tokens

### [CVE-2026-105210](https://github.com/zitadel/zitadel/security/advisories/GHSA-72q5-mv5c-vxv4)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-105210
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-05 00:16:32 JST
- 更新日: 2026-10-05 00:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADELのLogin V1 UIにおける二要素認証登録処理の認証欠落の脆弱性。
- 影響: 攻撃者が被害者のログイン名のみでTOTPやU2F等の二要素認証を不正登録・上書きし、アカウントの乗っ取りやユーザーの列挙を行う可能性があります。
- 推奨対応: 修正済みのバージョン（3.4.15以降および4.17.1以降）へ更新してください。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-72q5-mv5c-vxv4
- https://www.vulncheck.com/advisories/zitadel-before-4.17.1-unauthenticated-mfa-enrollment-via-login-v1-init-handlers

### [CVE-2026-105213](https://github.com/zitadel/zitadel/security/advisories/GHSA-558c-v5wc-9w4q)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-105213
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-05 00:16:32 JST
- 更新日: 2026-10-05 00:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADELにおける非アクティブ化された組織の検証不備の脆弱性。
- 影響: 無効化された組織のユーザーであっても、有効な資格情報やトークンを保持していればセッションの作成やログインが継続して行える可能性があります。
- 推奨対応: 修正済みのバージョン（4.17.1以降）へ更新してください。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-558c-v5wc-9w4q
- https://www.vulncheck.com/advisories/zitadel-before-4.17.1-authentication-bypass-via-login-v2-for-deactivated-organizations

# Backend CVE Summary (2026-08-30)

## Overview

- 取得日時: 2026-08-30 09:13:32 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 2
- High: 2
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-82464](https://github.com/pac4j/pac4j)

> **Backend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-82464
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-30 02:17:58 JST
- 更新日: 2026-08-30 02:17:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pac4j-coreのDefaultLogoutLogic.perform()におけるオープンリダイレクトの脆弱性
- 影響: バックスラッシュで始まる外部ホストURLを含むログアウトリンクを悪用され、ログアウト後に悪意のある外部サイトへ誘導される可能性があります。
- 推奨対応: pac4j-coreをバージョン 6.5.6 以降へアップデートしてください。

#### References
- https://github.com/pac4j/pac4j
- https://github.com/pac4j/pac4j/blob/pac4j-parent-6.5.5/pac4j-core/src/main/java/org/pac4j/core/engine/DefaultLogoutLogic.java
- https://github.com/pac4j/pac4j/commit/2270c3ff70e93cc43831e75702acd5135531237e
- https://www.pac4j.org/blog/security-advisory-pac4j-core-oidc-saml.html
- https://www.vulncheck.com/advisories/pac4j-core-before-6.5.6-open-redirect-via-backslash-logout

### [CVE-2026-82465](https://github.com/pac4j/pac4j)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-82465
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-30 02:17:58 JST
- 更新日: 2026-08-30 02:17:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pac4j-samlのSAML2LogoutValidator.validateLogoutRequest()におけるSAML LogoutRequestメッセージの署名検証不備
- 影響: 未認証の第三者が識別子（メールアドレス等）を推測し、未署名のLogoutRequestを送信することで、対象ユーザーのSAMLセッションを強制終了させる可能性があります。
- 推奨対応: pac4j-samlをバージョン 6.5.6 以降へアップデートしてください。

#### References
- https://github.com/pac4j/pac4j
- https://github.com/pac4j/pac4j/blob/pac4j-parent-6.5.5/pac4j-saml/src/main/java/org/pac4j/saml/logout/impl/SAML2LogoutValidator.java
- https://github.com/pac4j/pac4j/commit/2270c3ff70e93cc43831e75702acd5135531237e
- https://www.pac4j.org/blog/security-advisory-pac4j-core-oidc-saml.html
- https://www.vulncheck.com/advisories/pac4j-saml-before-6.5.6-session-destruction-via-unsigned-logoutrequest

### [CVE-2026-15369](https://woocommerce.com/products/custom-user-registration-fields-for-woocommerce/)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-15369
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-30 05:16:31 JST
- 更新日: 2026-08-30 05:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPressプラグイン「Custom User Registration Fields for WooCommerce」のチェックアウト処理における権限昇格の脆弱性
- 影響: 未認証の攻撃者がチェックアウトAPIリクエストのロール指定値を改ざんすることで、管理者などの高権限アカウントを作成できる可能性があります。
- 推奨対応: プラグインを修正済みバージョンへアップデートしてください。

#### References
- https://woocommerce.com/products/custom-user-registration-fields-for-woocommerce/
- https://www.wordfence.com/threat-intel/vulnerabilities/id/715723e7-5820-4a64-848f-f89b5b73a681?source=cve

### [CVE-2026-82466](https://github.com/jeremyevans/rodauth)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-82466
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-30 02:17:58 JST
- 更新日: 2026-08-30 02:17:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Rodauthのwebauthn_loginルートにおけるアカウント識別子解決ロジック不備による認証バイパス
- 影響: ログイン済みのユーザーがクレデンシャル検証を迂回し、任意のアカウントとして認証・乗っ取りを行う可能性があります。
- 推奨対応: Rodauthをバージョン 2.46.0 以降へアップデートしてください。

#### References
- https://github.com/jeremyevans/rodauth
- https://github.com/jeremyevans/rodauth/commit/35d74a9f07b2005a8ea75fc11a6539c04f3c2840
- https://github.com/jeremyevans/rodauth/security/advisories/GHSA-3pvr-v35r-4r75
- https://www.vulncheck.com/advisories/rodauth-before-2.46.0-authentication-bypass-via-webauthn-login

### [CVE-2026-75807](https://plugins.trac.wordpress.org/browser/miniorange-saml-20-single-sign-on/tags/5.4.6/class-mo-saml-login-validate.php#L236)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-75807
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-30 03:16:36 JST
- 更新日: 2026-08-30 03:16:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPressプラグイン「SAML Single Sign On – SSO Login」のACSハンドラーにおける署名検証前の証明書上書き不備
- 影響: 未認証の攻撃者がIdP署名証明書を上書きし、偽造したSAMLアサーションを用いて管理者を含む任意のユーザーとしてログインする可能性があります。
- 推奨対応: プラグインを修正済みバージョンへアップデートしてください。

#### References
- https://plugins.trac.wordpress.org/browser/miniorange-saml-20-single-sign-on/tags/5.4.6/class-mo-saml-login-validate.php#L236
- https://plugins.trac.wordpress.org/browser/miniorange-saml-20-single-sign-on/tags/5.4.6/class-mo-saml-login-validate.php#L292
- https://plugins.trac.wordpress.org/browser/miniorange-saml-20-single-sign-on/tags/5.4.6/class-mo-saml-utilities.php#L739
- https://plugins.trac.wordpress.org/browser/miniorange-saml-20-single-sign-on/tags/5.4.6/mo-saml-settings-page.php#L141
- https://www.wordfence.com/threat-intel/vulnerabilities/id/9baea072-2c07-40b6-8410-2ebe752b0874?source=cve

### [CVE-2026-82474](https://github.com/sudo-project/sudo)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-82474
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-30 02:17:59 JST
- 更新日: 2026-08-30 02:17:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Sudoのptraceベースインターセプトモードにおけるexecveatシステムコールへのポリシーチェック適用漏れ
- 影響: 特定コマンドの実行権限を持つユーザーが制限を迂回し、実行を禁止されているプログラムを実行できる可能性があります。
- 推奨対応: Sudoを修正済みバージョン（1.9.17p2より後のバージョン）へアップデートしてください。

#### References
- https://github.com/sudo-project/sudo
- https://github.com/sudo-project/sudo/blob/v1.9.17p2/src/exec_ptrace.c
- https://github.com/sudo-project/sudo/commit/71fbe42dcd5a1c8f799540583a2dfb2ae6221edf
- https://www.vulncheck.com/advisories/sudo-through-1.9-17p2-intercept-policy-bypass-via-execveat

### [CVE-2026-82468](https://github.com/jeremyevans/rodauth)

> **Backend** / **MEDIUM** / CVSS: **4.9** / KEV: **no**

- タイトル: CVE-2026-82468
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-30 02:17:59 JST
- 更新日: 2026-08-30 02:17:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RodauthのJSONリクエストContent-Type検証不備によるCSRF保護バイパスの脆弱性
- 影響: 攻撃者がクロスオリジンフォーム投稿を利用してCSRF検証を迂回し、被害者を攻撃者制御のアカウントへ強制認証させる可能性があります。
- 推奨対応: Rodauthをバージョン 2.47.0 以降へアップデートしてください。

#### References
- https://github.com/jeremyevans/rodauth
- https://github.com/jeremyevans/rodauth/commit/3e0d7ab2d49a5733d1afcaaf1062b8a8258aa57a
- https://github.com/jeremyevans/rodauth/security/advisories/GHSA-hh2f-xw94-5p79
- https://www.vulncheck.com/advisories/rodauth-before-2.47.0-csrf-protection-bypass-via-content-type

### [CVE-2026-82467](https://github.com/jeremyevans/rodauth)

> **Backend** / **MEDIUM** / CVSS: **4.9** / KEV: **no**

- タイトル: CVE-2026-82467
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-30 02:17:59 JST
- 更新日: 2026-08-30 02:17:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Rodauthのログイン後リダイレクトパス処理におけるプロトコル相対パスの検証不備
- 影響: 攻撃者が先頭に二重スラッシュを含むパスを挿入することで、認証後のユーザーを悪意のある外部サイトへリダイレクトさせる可能性があります。
- 推奨対応: Rodauthをバージョン 2.47.0 以降へアップデートしてください。

#### References
- https://github.com/jeremyevans/rodauth
- https://github.com/jeremyevans/rodauth/commit/295044a92e358479afdf84f905dd5efe89c39aea
- https://github.com/jeremyevans/rodauth/security/advisories/GHSA-h9m4-vm9w-h43m
- https://www.vulncheck.com/advisories/rodauth-before-2.47.0-open-redirect-via-return-to-path

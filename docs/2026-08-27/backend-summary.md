# Backend CVE Summary (2026-08-27)

## Overview

- 取得日時: 2026-08-27 12:06:15 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 22
- Critical: 5
- High: 6
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-54553](https://github.com/jowilf/starlette-admin/commit/3d9639d12ffc30b0b92d45ad6aae5fefabc948f3)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-54553
- 関連キーワード: python, fastapi
- 影響製品: -
- 公開日: 2026-08-27 00:16:49 JST
- 更新日: 2026-08-27 01:16:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Starlette-Admin is a fast, beautiful and extensible administrative interface framework for FastAPI and Starlette applications. Prior to 0.16.1, the list API does not validate user-supplied order_by and structured where field names against the configured sortable_fields and searchable_fields allowlists. An authenticated...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jowilf/starlette-admin/commit/3d9639d12ffc30b0b92d45ad6aae5fefabc948f3
- https://github.com/jowilf/starlette-admin/commit/57a1a76d45dfed16f580677303c5fd25220bd36b
- https://github.com/jowilf/starlette-admin/commit/af05b45cd90944b726949fd650ab9d19f1abafc3
- https://github.com/jowilf/starlette-admin/commit/d2a25ebbaf213d4c2cfc87187e34309ca6e30a51
- https://github.com/jowilf/starlette-admin/pull/776

### [CVE-2026-54523](https://github.com/kyverno/kyverno/commit/0919553c0ea1904f8d891280c92018da97946a06)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-54523
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-27 00:16:48 JST
- 更新日: 2026-08-27 01:16:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Kyverno is a policy engine designed for cloud native platform engineering teams. From 1.18.0 until 1.18.2, the NamespacedMutatingPolicy CEL compiler exposes the generator library to matchConditions, allowing a namespace-scoped policy to invoke generator.apply(namespace, resources) with an arbitrary target namespace. Th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/kyverno/kyverno/commit/0919553c0ea1904f8d891280c92018da97946a06
- https://github.com/kyverno/kyverno/commit/5164bcdeda5b57678bc2d7a03ecc2cbb02982dae
- https://github.com/kyverno/kyverno/pull/16238
- https://github.com/kyverno/kyverno/releases/tag/v1.18.2
- https://github.com/kyverno/kyverno/security/advisories/GHSA-79gf-7frw-68m9

### [CVE-2026-19485](https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-19485
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-27 04:16:49 JST
- 更新日: 2026-08-27 05:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A Predictable Resource Name vulnerability in BigQuery Import Staging in Google Cloud Vertex AI Search for Commerce versions prior to 2026-04-27 on Google Cloud Platform allows an attacker knowing the victim's project number to obtain read/write access to staged data and error logs using predictable bucket names. This v...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://unit42.paloaltonetworks.com/hijacking-vertex-ai-model/

### [CVE-2026-80428](https://github.com/ILIAS-eLearning/ILIAS)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-80428
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-27 01:16:45 JST
- 更新日: 2026-08-27 01:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ILIAS deserialises stored session data for an unauthenticated caller. The Shibboleth back-channel endpoint at components/ILIAS/AuthShibboleth/resources/shib_logout.php runs in a context that ilInitialisation exempts from authentication, and its logout-notification handler locates the session to terminate by reading eve...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/ILIAS-eLearning/ILIAS
- https://github.com/ILIAS-eLearning/ILIAS/commit/f36934a6f937d0fe837ca6e642986458b4069a95
- https://www.vulncheck.com/advisories/ilias-before-9.22-10.10-and-11.3-unauthenticated-php-object-injection-via-shibboleth-logout-endpoint

### [CVE-2026-75062](https://github.com/google/langfun)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-75062
- 関連キーワード: python, go, express
- 影響製品: -
- 公開日: 2026-08-27 00:16:55 JST
- 更新日: 2026-08-27 01:16:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper Neutralization of Directives in Dynamically Evaluated Code ('Eval Injection') in the default lf.query Python protocol in Google langfun versions prior to 0.1.2 allows remote unauthenticated attackers to execute arbitrary Python code in the context of the host application via crafted prompt inputs that cause th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/google/langfun
- https://github.com/google/langfun/issues/725
- https://github.com/google/langfun/issues/725

### [CVE-2026-46369](https://github.com/nimiq/core-rs-albatross/commit/a530b2434ebca6e3716f07c73079786fcc6f2e41)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-46369
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-27 05:17:23 JST
- 更新日: 2026-08-27 05:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nimiq is a Rust implementation of the Nimiq Proof-of-Stake protocol based on the Albatross consensus algorithm. Through 1.5.0, the validity store uses a strict lower-bound comparison that expires a stored transaction too early relative to Transaction::is_valid_at, allowing a remote attacker to replay the same signed tr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nimiq/core-rs-albatross/commit/a530b2434ebca6e3716f07c73079786fcc6f2e41
- https://github.com/nimiq/core-rs-albatross/pull/3772
- https://github.com/nimiq/core-rs-albatross/security/advisories/GHSA-3763-qp59-59vf

### [CVE-2026-81027](https://github.com/songquanpeng/one-api)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-81027
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-27 01:16:45 JST
- 更新日: 2026-08-27 03:17:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: one-api gates one of its two channel-pinning paths and not the other. middleware/auth.go permits a request to name a specific channel either through a suffix on the API key or through a URL path parameter. The suffix path is reached only after model.IsAdmin succeeds and otherwise rejects the caller, while the path-para...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/songquanpeng/one-api
- https://github.com/songquanpeng/one-api/blob/v0.6.10/middleware/auth.go
- https://github.com/songquanpeng/one-api/issues/2410
- https://www.vulncheck.com/advisories/one-api-through-0.6.10-missing-authorization-on-url-parameter-channel-pinning
- https://github.com/songquanpeng/one-api/issues/2410

### [CVE-2026-81034](https://github.com/gravitl/netmaker)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-81034
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-27 01:16:46 JST
- 更新日: 2026-08-27 04:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Netmaker disables certificate verification on the connection to the configured mail server. The sender in pro/email/smtp.go assigns a TLS configuration whose skip-verify field is set to true unconditionally, directly beneath a comment stating that the setting should be false in production. No configuration value govern...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gravitl/netmaker
- https://github.com/gravitl/netmaker/blob/v1.6.0/pro/email/smtp.go
- https://github.com/gravitl/netmaker/issues/4062
- https://www.vulncheck.com/advisories/netmaker-through-1.6.0-improper-certificate-validation-in-smtp-client
- https://github.com/gravitl/netmaker/issues/4062

### [CVE-2026-68000](https://github.com/fangtang7/CVE/blob/main/MCMS/MCMS6.2.0-SQLinjection.md)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-68000
- 関連キーワード: go, gin, express
- 影響製品: -
- 公開日: 2026-08-27 05:17:57 JST
- 更新日: 2026-08-27 05:17:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The front-end interface /cms/category/list of MCMS <=6.2.0 is vulnerable to SQL injection. The size parameter is directly concatenated into the LIMIT clause of SQL through FreeMarker ${size} without being parameterized and bound. The built-in SqlInjectionUtil employs regular expression blacklist filtering, yet keywords...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/fangtang7/CVE/blob/main/MCMS/MCMS6.2.0-SQLinjection.md

### [CVE-2026-81033](https://github.com/automatisch/automatisch)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-81033
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-27 01:16:46 JST
- 更新日: 2026-08-27 01:16:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Automatisch reveals whether an address is registered through the response to its forgot-password request. The controller at packages/backend/src/controllers/internal/api/v1/users/forgot-password.js looks the address up and chains a not-found throw onto the query, so an address with no account raises an error that the g...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/automatisch/automatisch
- https://github.com/automatisch/automatisch/blob/v0.15.0/packages/backend/src/controllers/internal/api/v1/users/forgot-password.js
- https://github.com/automatisch/automatisch/issues/2713
- https://www.vulncheck.com/advisories/automatisch-through-0.15.0-user-enumeration-via-forgot-password-response-discrepancy

### [CVE-2026-56547](https://support.hcl-software.com/csm?id=kb_article&sysparm_article=KB0132221)

> **Backend** / **LOW** / CVSS: **3.5** / KEV: **no**

- タイトル: CVE-2026-56547
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-27 05:17:54 JST
- 更新日: 2026-08-27 05:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The Apple profile generated for the Apple built-in Mail, Calendar and Contacts account to synchronize with HCL Traveler requires the Logon Name and Mail Address to be embedded in them. The values cannot be changed later on, so the Apple profile generation page asks for those values and reflects them back in the generat...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://support.hcl-software.com/csm?id=kb_article&sysparm_article=KB0132221

### [CVE-2026-74740](https://git.kernel.org/stable/c/1ec48b6715c29b20105e3485206602cff6c51ae5)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74740
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-27 00:16:52 JST
- 更新日: 2026-08-27 00:16:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: net/sched: act_api: fix TOCTOU NULL deref on a->goto_chain tcf_action_exec() handles TC_ACT_GOTO_CHAIN by first checking rcu_access_pointer(a->goto_chain) and then calling tcf_action_goto_chain_exec(), which does a second, independent rcu_dereference_b...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/1ec48b6715c29b20105e3485206602cff6c51ae5
- https://git.kernel.org/stable/c/6b70886ebc428eed43a069c8944a931b5fb3f4e4
- https://git.kernel.org/stable/c/91d55fd1fdb85c8371ca8793c788ea7d5192383a
- https://git.kernel.org/stable/c/abceabc4408fca6a9dd52611f5d197dec9390d63
- https://git.kernel.org/stable/c/f60b396ee174206fe08ebf997d16cd3801b77b22

### [CVE-2026-74750](https://git.kernel.org/stable/c/0f77ed5ee91946ea63e29f2e0ff9dc9e722d8da3)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74750
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-27 00:16:54 JST
- 更新日: 2026-08-27 00:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのovpnモジュールにおけるキー・スロット解放処理の不具合。スリープが許容されないRCUコールバック内で暗号化リソースの解放を行っていたため、ワークキューによる遅延解放処理へ修正されました。
- 影響: 特定の暗号化実装使用時にシステムが不安定化する、またはクラッシュする可能性があります。
- 推奨対応: 修正済みカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/0f77ed5ee91946ea63e29f2e0ff9dc9e722d8da3
- https://git.kernel.org/stable/c/2da3dfa1ddfe55a065f484750c83660e3bd4ac00

### [CVE-2026-80565](https://git.kernel.org/stable/c/1ece8e16c085e8cd60ecbdb641269aaa53d31da4)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80565
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-27 00:17:11 JST
- 更新日: 2026-08-27 00:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのcrypto/qceにおけるdevm_qce_register_algsのエラー処理不具合。登録失敗時のクリーンアップ処理で同じ解除関数を誤って繰り返し呼び出していたため、登録済みのアルゴリズムのみを正しく解除するよう修正されました。
- 影響: アルゴリズムの登録失敗時に不適切な解除処理が行われ、カーネルの不安定化やエラーを引き起こす可能性があります。
- 推奨対応: 修正済みカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/1ece8e16c085e8cd60ecbdb641269aaa53d31da4
- https://git.kernel.org/stable/c/4e88b4fda48282f3fd504b4d4f5d2d4f996b76ce
- https://git.kernel.org/stable/c/9c75402286409f5e1a75e4a445555c84066f89db
- https://git.kernel.org/stable/c/a134e4b8102c077286818ee112b9f925db613d4c
- https://git.kernel.org/stable/c/c7dc487aade12c692add3221673c9bdf32dc24f5

### [CVE-2026-80581](https://git.kernel.org/stable/c/17661c67b206612cb3ba65d5ae726cd2015d0a53)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80581
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-27 00:17:14 JST
- 更新日: 2026-08-27 00:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのASoC SOF (Sound Open Firmware) におけるIPCタイムアウトおよびファームウェアクラッシュ時の状態管理の不具合。エラー発生時にもパイプラインのトリガー処理を継続し、内部状態を適切にリセットできるよう修正されました。
- 影響: オーディオ機能の内部状態が不正なままとなり、DSP再起動後の正常動作が阻害される可能性があります。
- 推奨対応: 修正済みカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/17661c67b206612cb3ba65d5ae726cd2015d0a53
- https://git.kernel.org/stable/c/6b512a5330ef1a41db7aff4b80c4e952b8d52f17
- https://git.kernel.org/stable/c/f2435a46dfa1a5693cf2664afd022db66ee58121

### [CVE-2026-58474](https://github.com/Andyyyy64/whichllm/commit/77e8dc9e8b45212c694d631d758623e17a00859e)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-58474
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-08-27 03:16:42 JST
- 更新日: 2026-08-27 05:17:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: whichllm (0.5.16未満) のrunおよびsnippetコマンドにおけるコードインジェクションの脆弱性。HuggingFaceリポジトリのGGUFファイル名をエスケープせずに直接Pythonソースコードへ挿入する処理に起因します。
- 影響: 悪意を持って細工されたリポジトリを参照させられることで、モデルのダウンロード前に攻撃者の任意のコードがローカル環境で実行される可能性があります。
- 推奨対応: whichllm をバージョン 0.5.16 以降に更新してください。

#### References
- https://github.com/Andyyyy64/whichllm/commit/77e8dc9e8b45212c694d631d758623e17a00859e
- https://github.com/Andyyyy64/whichllm/pull/147
- https://github.com/Andyyyy64/whichllm/releases/tag/v0.5.16
- https://www.vulncheck.com/advisories/whichllm-code-injection-via-run-and-snippet-commands

### [CVE-2026-48786](http://github.com/fleetdm/fleet/commit/6a481477e8ac4bef43b5826e6240b867ac3b2379)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-48786
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-27 04:16:50 JST
- 更新日: 2026-08-27 05:17:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Fleet (4.87.0未満) のターゲット検索エンドポイントにおける情報漏洩の脆弱性。低権限のObserverロール等のユーザーに対して、登録シークレットや認証情報を含むチーム設定がサニタイズされずに返却されていました。
- 影響: 認証済みの低権限ユーザーが漏洩した登録シークレットを用いて不正なホストをチームに登録したり、AWSアクセスキーなどの機密情報を取得したりする可能性があります。
- 推奨対応: Fleet をバージョン 4.87.0 以降に更新してください。

#### References
- http://github.com/fleetdm/fleet/commit/6a481477e8ac4bef43b5826e6240b867ac3b2379
- https://github.com/fleetdm/fleet/releases/tag/fleet-v4.87.0
- https://github.com/fleetdm/fleet/security/advisories/GHSA-88p2-jj8w-j8qg

### [CVE-2026-80551](https://git.kernel.org/stable/c/08ef2a82115690d6e229615872ac1731af732497)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-80551
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-27 00:17:09 JST
- 更新日: 2026-08-27 00:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのs390/vfio_ccwにおけるIDAW (Indirect Data Address Word) 読み取り処理の不具合。最初に読み取ったIDAWアドレスが、以降の読み取り時にも変更されていないか確認する検証が追加されました。
- 影響: 競合等により不整合なIDAWが使用され、データ処理の異常やカーネルの不安定化が生じる可能性があります。
- 推奨対応: 修正済みカーネルバージョンへ更新してください。

#### References
- https://git.kernel.org/stable/c/08ef2a82115690d6e229615872ac1731af732497
- https://git.kernel.org/stable/c/0d46c2565f173bcddcdcaf44a4f69789a20535e2
- https://git.kernel.org/stable/c/565bef268d75bf7df665bce6923a88cd0eb74592
- https://git.kernel.org/stable/c/fc59e9482117ebdccd6dc7fa8082f8b980fd021e

### [CVE-2026-81032](https://github.com/vesoft-inc/nebula)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-81032
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-27 01:16:46 JST
- 更新日: 2026-08-27 03:17:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NebulaGraphのランタイム設定用Web APIにおける未認証アクセスの脆弱性。認証やアクセス制限なしで起動し、設定値の閲覧および変更を可能とするルートが公開されています。
- 影響: 未認証の第三者によって証明書やパスワードファイルのパスなどの機密情報を閲覧されたり、トランスポートセキュリティの無効化など設定を任意に変更されたりする可能性があります。
- 推奨対応: NebulaGraphを修正バージョンに更新し、Web APIのポートへのアクセス制限や設定を見直してください。

#### References
- https://github.com/vesoft-inc/nebula
- https://github.com/vesoft-inc/nebula/blob/v3.8.0/src/webservice/SetFlagsHandler.cpp
- https://github.com/vesoft-inc/nebula/blob/v3.8.0/src/webservice/WebService.cpp
- https://github.com/vesoft-inc/nebula/issues/6157
- https://www.vulncheck.com/advisories/nebulagraph-through-3.8.0-unauthenticated-read-and-modification-of-runtime-configuration

### [CVE-2026-80427](https://github.com/nfriedly/node-bestzip)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-80427
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-27 01:16:44 JST
- 更新日: 2026-08-27 02:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: bestzipにおけるコマンドインジェクションの脆弱性。zipユーティリティへ引数を引き渡す際、オプションとファイルを区切るデリミタ（--）が付与されていないため、ハイフンで始まるパスがzipオプションとして解釈される問題が存在します。
- 影響: 外部からの信頼できないファイルパスをbestzipに渡した場合、zipのテスト機能等を経由して任意のコマンドを実行される可能性があります。
- 推奨対応: bestzip を 2.2.6 または 3.0.2 以降に更新してください。

#### References
- https://github.com/nfriedly/node-bestzip
- https://github.com/nfriedly/node-bestzip/security/advisories/GHSA-p87m-9567-rgcc
- https://www.npmjs.com/package/bestzip
- https://www.vulncheck.com/advisories/bestzip-before-2.2.6-and-3.0-x-before-3.0.2-argument-injection-via-missing-option-delimiter
- https://github.com/nfriedly/node-bestzip/security/advisories/GHSA-p87m-9567-rgcc

### [CVE-2026-54256](https://github.com/wintercms/winter/commit/9cb0ae5f9d837db141ab111c6a7de8eed9603d25)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-54256
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-27 03:16:40 JST
- 更新日: 2026-08-27 03:16:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Winter CMS (1.2.12以下) のFileUploadフォームウィジェットにおけるアクセス制御不備の脆弱性。送信された `file_id` パラメータに対する権限・所有権チェックが不十分なため、グローバルなファイルテーブルから任意レコードが参照されます。
- 影響: 認証済みのバックエンドユーザーが、他のユーザーや別レコードに属する添付ファイルのタイトル等の変更や参照を行う可能性があります。
- 推奨対応: Winter CMS をバージョン 1.2.13 以降に更新してください。

#### References
- https://github.com/wintercms/winter/commit/9cb0ae5f9d837db141ab111c6a7de8eed9603d25
- https://github.com/wintercms/winter/security/advisories/GHSA-3277-h8g9-qj5f

### [CVE-2026-54511](https://github.com/dahlia/logtape/commit/7a6e5b9ddf7915edfff78fa129bc17c979b2a623)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-54511
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-27 00:16:48 JST
- 更新日: 2026-08-27 00:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LogTapeの `@logtape/syslog` パッケージにおける制御文字のエスケープ漏れおよび文法検証不足の脆弱性。構造化データ値に含まれる制御文字や不正なキー文字が適切に無効化されません。
- 影響: 攻撃者によって入力された制御文字によりsyslogフレームが途中で切断され、任意のホストや優先度を偽装した偽のsyslogレコードを挿入される可能性があります。
- 推奨対応: `@logtape/syslog` をバージョン 1.3.11, 2.0.14, 2.1.5 またはそれ以降に更新してください。

#### References
- https://github.com/dahlia/logtape/commit/7a6e5b9ddf7915edfff78fa129bc17c979b2a623
- https://github.com/dahlia/logtape/releases/tag/1.3.11
- https://github.com/dahlia/logtape/releases/tag/2.0.14
- https://github.com/dahlia/logtape/releases/tag/2.1.5
- https://github.com/dahlia/logtape/security/advisories/GHSA-8h6h-x5pq-56fq

# Backend CVE Summary (2026-10-15)

## Overview

- 取得日時: 2026-10-15 09:28:40 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 19
- Critical: 3
- High: 8
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-100169](https://github.com/prowler-cloud/prowler/commit/0f31f1a3c2daa05b4d77a78f451e3fbfb3fe3411)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-100169
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-10-15 01:17:28 JST
- 更新日: 2026-10-15 01:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper Authentication in the social account linking path of the Prowler API in Prowler from 5.4.0 before 5.35.0 allows a remote unauthenticated attacker to obtain persistent access to the account of a user who has not yet registered, because ProwlerSocialAccountAdapter.pre_social_login() in api/src/backend/api/adapte...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/prowler-cloud/prowler/commit/0f31f1a3c2daa05b4d77a78f451e3fbfb3fe3411
- https://github.com/prowler-cloud/prowler/pull/12013
- https://github.com/prowler-cloud/prowler/releases/tag/5.35.0
- https://github.com/prowler-cloud/prowler/security/advisories/GHSA-h8m9-jgf8-vwvp
- https://secur0.com/en/cna/cve-list/cve-2026-100169-prowler-account-pre-hijacking

### [CVE-2026-110593](https://github.com/Django-CRM/Django-CRM/blob/v1.14.5/backend/accounts/tasks.py#L45)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-110593
- 関連キーワード: python, django, go
- 影響製品: -
- 公開日: 2026-10-15 00:17:10 JST
- 更新日: 2026-10-15 01:17:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: BottleCRM through 1.14.5 contains a server-side template injection vulnerability in the send_email Celery task, which compiles the user-supplied AccountEmail message_body with django.template.Template(). Authenticated organization members can submit template tags through POST /api/accounts/<id>/create_mail/ to disclose...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Django-CRM/Django-CRM/blob/v1.14.5/backend/accounts/tasks.py#L45
- https://github.com/Django-CRM/Django-CRM/issues/826
- https://www.vulncheck.com/advisories/bottlecrm-through-1.14.5-server-side-template-injection-via-account-email-create-mail

### [CVE-2026-91156](https://github.com/discourse/discourse/commit/046fb7bfd68a5b95e63dda88c3c73877c5cf9d5e)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-91156
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-15 01:17:56 JST
- 更新日: 2026-10-15 03:19:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Discourse is an open-source discussion platform. Prior to 2026.9.0, 2026.8.1, 2026.7.3, and 2026.1.9, MessageBus audience calculation could deliver messages from a read-restricted category chat channel to an authenticated user who could view the category but was not allowed to use Chat under the site's group restrictio...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/discourse/discourse/commit/046fb7bfd68a5b95e63dda88c3c73877c5cf9d5e
- https://github.com/discourse/discourse/commit/87b31bf60a7827f075634254379a1dcbaba409cb
- https://github.com/discourse/discourse/commit/ba74bb404ab4439f5b1f0204e848d62099db8ae1
- https://github.com/discourse/discourse/commit/cac1f26f275cec3dc1dd51dfdac2b3d1a4ec50f8
- https://github.com/discourse/discourse/security/advisories/GHSA-gh4f-qr62-vx8q

### [CVE-2026-91157](https://github.com/discourse/discourse/commit/16017732981fdb3ee65d7b3c69c573610bf02aab)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-91157
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-15 01:17:56 JST
- 更新日: 2026-10-15 01:17:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Discourse is an open-source discussion platform. Prior to 2026.9.0, 2026.8.1, 2026.7.3, and 2026.1.9, sites with secure uploads enabled did not reconcile existing upload security metadata when a previously public category became read-restricted or when category permissions changed during a bulk import. Media and attach...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/discourse/discourse/commit/16017732981fdb3ee65d7b3c69c573610bf02aab
- https://github.com/discourse/discourse/commit/83f5f9f1df7ddc79ec0950e1b2038ba659635708
- https://github.com/discourse/discourse/commit/98f1c021d0e956cded5239a5d8a6afe2b9e1b7e7
- https://github.com/discourse/discourse/commit/b2fb98394b2636b29e850f06b0029f8ca8b48458
- https://github.com/discourse/discourse/security/advisories/GHSA-298h-xgw6-4pv3

### [CVE-2026-110607](https://github.com/BizSpringSource/bizspring-shop-opensource)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-110607
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-15 00:17:12 JST
- 更新日: 2026-10-15 03:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: BizSpring Shop through commit cf22d39daaf1 contains a payment verification bypass vulnerability that allows authenticated buyers to mark orders paid by calling the PaymentController.testPostPay handler. Attackers can generate a payment log via /member/payment/load and request /member/payment/test_post_pay_{paymentLogSn...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/BizSpringSource/bizspring-shop-opensource
- https://github.com/BizSpringSource/bizspring-shop-opensource/blob/cf22d39daaf17f430d8fc1fb698a2f6e515e1808/bizspring-open/bizspring-business/bizspring-order/src/main/java/cn/bizspring/cloud/order/admin/controller/shop/PaymentController.java#L76-L84
- https://github.com/BizSpringSource/bizspring-shop-opensource/blob/cf22d39daaf17f430d8fc1fb698a2f6e515e1808/bizspring-open/bizspring-business/bizspring-order/src/main/java/cn/bizspring/cloud/order/admin/service/impl/PaymentLogServiceImpl.java#L143-L169
- https://github.com/bizspring-open/BizSpring-Java-Mall
- https://github.com/bizspring-open/BizSpring-Java-Mall/blob/369e88c5cda36ddcea56742c335ee1bfe50e8156/bizspring-java/bizspring-business/bizspring-order/src/main/java/cn/bizspring/cloud/order/admin/controller/shop/PaymentController.java#L76-L84

### [CVE-2026-110609](https://github.com/dromara/skyeye)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-110609
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-15 00:17:12 JST
- 更新日: 2026-10-15 02:18:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dromara Skyeye through commit 65d3ddcede70 contains an sql injection vulnerability that allows authenticated low-privileged users to inject SQL via the keyword parameter in the queryErpOrderItem MyBatis statement using raw ${} substitution. Attackers can send crafted keyword values to the queryWarehousingDetails or que...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dromara/skyeye
- https://github.com/dromara/skyeye/blob/65d3ddcede701d33ea5416e47c9b656e47d56401/skyeye-erp/erp-pro/src/main/java/com/skyeye/controller/StatisticsController.java#L33-L45
- https://github.com/dromara/skyeye/blob/65d3ddcede701d33ea5416e47c9b656e47d56401/skyeye-erp/erp-pro/src/main/resources/mapper/erp/StatisticsMapper.xml#L29-L31
- https://hackmd.io/@1ExmmukzRMWN7B4gQ4W-4Q/skyeye-erp-statistics-keyword-sqli
- https://www.vulncheck.com/advisories/dromara-skyeye-through-commit-65d3ddcede70-sql-injection-via-keyword-parameter

### [CVE-2026-89077](https://community.progress.com/s/article/MOVEit-Transfer-Critical-Security-Bulletin---September-2026)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-89077
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-15 01:17:56 JST
- 更新日: 2026-10-15 04:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Incorrect implementation of authentication algorithm vulnerability in Progress MOVEit Transfer (SFTP module). This issue affects MOVEit Transfer: before 2025.1.6 and from 2026.0.0 before 2026.0.4.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://community.progress.com/s/article/MOVEit-Transfer-Critical-Security-Bulletin---September-2026

### [CVE-2026-100394](https://github.com/nezhahq/nezha/commit/c893aa57867d8a3d608e2f2f16d1594c9766cdf3)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-100394
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-15 01:17:28 JST
- 更新日: 2026-10-15 01:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nezha Monitoring is a self-hostable, lightweight, servers and websites monitoring and O&M tool. From 2.2.7 until 2.2.11, ServiceSentinel.worker in service/singleton/servicesentinel.go checked an owned service under servicesLock and later dereferenced pointer-valued serviceStatusToday and serviceCurrentStatusData entrie...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nezhahq/nezha/commit/c893aa57867d8a3d608e2f2f16d1594c9766cdf3
- https://github.com/nezhahq/nezha/releases/tag/v2.2.11
- https://github.com/nezhahq/nezha/releases/tag/v2.3.0
- https://github.com/nezhahq/nezha/security/advisories/GHSA-qjpp-gffx-2wm9

### [CVE-2026-110735](https://axeghost.offprint.app/a/3mvs6zo4blo23-three-memory-safety-bugs-in-godots-untrusted-file-parsers)

> **Backend** / **LOW** / CVSS: **2.5** / KEV: **no**

- タイトル: CVE-2026-110735
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-15 01:17:44 JST
- 更新日: 2026-10-15 01:17:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Godot Engine through 4.7.2 has a heap out-of-bounds write exists in the binary resource loader (core/io/resource_format_binary.cpp, ResourceLoaderBinary::get_unicode_string). A string length is read from the resource file into a signed 32-bit integer and compared against the destination buffer size with a signed compar...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://axeghost.offprint.app/a/3mvs6zo4blo23-three-memory-safety-bugs-in-godots-untrusted-file-parsers
- https://github.com/godotengine/godot/issues/123608

### [CVE-2026-110736](https://axeghost.offprint.app/a/3mvs6zo4blo23-three-memory-safety-bugs-in-godots-untrusted-file-parsers)

> **Backend** / **LOW** / CVSS: **3.6** / KEV: **no**

- タイトル: CVE-2026-110736
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-15 01:17:44 JST
- 更新日: 2026-10-15 01:17:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Godot Engine through 4.7.2 has an out-of-bounds read in the optimized translation loader (core/string/optimized_translation.cpp, OptimizedTranslation::get_message). Offsets read from the hash table of a crafted .translation resource are used as indices into the bucket table without bounds validation; only a single sent...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://axeghost.offprint.app/a/3mvs6zo4blo23-three-memory-safety-bugs-in-godots-untrusted-file-parsers
- https://github.com/godotengine/godot/issues/123608

### [CVE-2026-70407](https://blog.gitea.com/release-of-1.27.3/)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-70407
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-15 00:17:22 JST
- 更新日: 2026-10-15 01:17:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Gitea's organization-list API does not enforce the read:organization token scope. A token limited to another category, such as read:misc, can retrieve organization metadata visible to its owner. For a site administrator's token, the response can include Limited and private organizations, bypassing the intended restrict...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://blog.gitea.com/release-of-1.27.3/
- https://github.com/go-gitea/gitea/pull/39041
- https://github.com/go-gitea/gitea/pull/39058
- https://github.com/go-gitea/gitea/releases/tag/v1.27.3
- https://github.com/go-gitea/gitea/security/advisories/GHSA-ww9q-7j5q-hrv5

### [CVE-2026-110619](https://github.com/fatedier/frp)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-110619
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-15 00:17:14 JST
- 更新日: 2026-10-15 02:18:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: frp 0.41.0 through 0.71.1 contains a missing authentication vulnerability that allows unauthenticated remote attackers to access pprof debug endpoints because handlers are registered on the root mux outside Basic Authentication. Attackers can query /debug/pprof/ endpoints on frps dashboard or frpc admin listeners to ob...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/fatedier/frp
- https://github.com/fatedier/frp/blob/v0.71.1/pkg/util/http/server.go#L124-L130
- https://github.com/fatedier/frp/blob/v0.71.1/server/api_router.go#L27-L32
- https://hackmd.io/@1ExmmukzRMWN7B4gQ4W-4Q/HyZWPT3jfe
- https://www.vulncheck.com/advisories/frp-0.41.0-through-0.71.1-missing-authentication-for-pprof-debug-endpoints

### [CVE-2026-110734](https://axeghost.offprint.app/a/3mvs6zo4blo23-three-memory-safety-bugs-in-godots-untrusted-file-parsers)

> **Backend** / **LOW** / CVSS: **2.5** / KEV: **no**

- タイトル: CVE-2026-110734
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-15 01:17:44 JST
- 更新日: 2026-10-15 03:17:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Godot Engine through 4.7.2 has a heap out-of-bounds write in the Radiance HDR (.hdr) image decoder (modules/hdr/image_loader_hdr.cpp). The run-length decoding loop expands RLE instructions read from the file into a buffer sized from the image dimensions, without validating that an instruction's repeat/copy count fits t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://axeghost.offprint.app/a/3mvs6zo4blo23-three-memory-safety-bugs-in-godots-untrusted-file-parsers
- https://github.com/godotengine/godot/issues/123608

### [CVE-2026-110636](https://github.com/revolunet/pypdftk)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-110636
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-15 00:17:16 JST
- 更新日: 2026-10-15 00:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pypdftk through 0.5 contains an OS command injection vulnerability in fill_form(), dump_data_fields(), and pdftk_cmd_util() that builds shell commands from caller-supplied paths. Attackers controlling pdf_path or out_file can inject shell metacharacters interpreted by subprocess.Popen with shell=True to execute OS comm...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/revolunet/pypdftk
- https://github.com/revolunet/pypdftk/blob/1d3b40c3b42fb3cc6b0192d34aba2c21a1efd369/pypdftk.py#L87-L123
- https://github.com/revolunet/pypdftk/issues/56
- https://github.com/revolunet/pypdftk/pull/57
- https://www.vulncheck.com/advisories/pypdftk-through-0.5-os-command-injection-via-pdf-and-output-paths

### [CVE-2026-110650](https://github.com/anshulkharb/thumbnail/blob/23b2e30509c936872a3bafac65b4aa48777e794c/thumbnail/thumbnail.py#L100-L114)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-110650
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-15 00:17:18 JST
- 更新日: 2026-10-15 06:17:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The thumbnail Python package through 1.5 contains an OS command injection vulnerability in generate_thumbnail() that allows attackers to execute commands by supplying shell metacharacters in file paths. Attackers who control a file name passed to generate_thumbnail, such as an uploaded file, can inject commands into os...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/anshulkharb/thumbnail/blob/23b2e30509c936872a3bafac65b4aa48777e794c/thumbnail/thumbnail.py#L100-L114
- https://github.com/anshulkharb/thumbnail/pull/9
- https://www.vulncheck.com/advisories/thumbnail-through-1.5-os-command-injection-via-generate-thumbnail-file-paths
- https://github.com/anshulkharb/thumbnail/pull/9

### [CVE-2026-103929](https://github.com/jdx/mise/commit/c6cd7a9a2ca580918562566126646e5d04317895)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-103929
- 関連キーワード: python, terraform
- 影響製品: -
- 公開日: 2026-10-15 01:17:30 JST
- 更新日: 2026-10-15 01:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: mise manages dev tools like node, python, cmake, and terraform. Prior to 2026.7.14, in the default non-safe mode, mise loads .mise.toml [settings] from an untrusted local project before trust approval and strip_local_only_settings removes only fields marked global_only. The unix_default_file_shell_args, unix_default_in...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jdx/mise/commit/c6cd7a9a2ca580918562566126646e5d04317895
- https://github.com/jdx/mise/pull/11293
- https://github.com/jdx/mise/releases/tag/v2026.7.14
- https://github.com/jdx/mise/security/advisories/GHSA-g74g-rg72-j2p3

### [CVE-2026-86002](https://github.com/dokku/dokku/commit/1a376c362215a5c7044a08b3e3905b1a5fddc821)

> **Backend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-86002
- 関連キーワード: gin, docker
- 影響製品: -
- 公開日: 2026-10-15 01:17:54 JST
- 更新日: 2026-10-15 03:19:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dokku is a docker-powered platform as a service. In Dokku versions before 0.38.25, a user with app-level Dokku access and remote SSH access to execute docker-options commands can store arbitrary strings through the docker-options plugin, and those strings are later concatenated into DOCKER_ARGS and processed by Bash ev...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dokku/dokku/commit/1a376c362215a5c7044a08b3e3905b1a5fddc821
- https://github.com/dokku/dokku/pull/8848
- https://github.com/dokku/dokku/releases/tag/v0.38.25
- https://github.com/dokku/dokku/security/advisories/GHSA-fccf-j7qf-2xp9

### [CVE-2026-110719](https://github.com/Portkey-AI/gateway)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-110719
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-15 01:17:44 JST
- 更新日: 2026-10-15 01:17:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Portkey AI Gateway 1.14.0 through 1.15.2 contains a server-side request forgery vulnerability that allows unauthenticated attackers to reach loopback and Docker host services because isValidCustomHost trusts localhost-style hosts when TRUSTED_CUSTOM_HOSTS is unset. Attackers can send /v1 requests with a crafted x-portk...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Portkey-AI/gateway
- https://github.com/Portkey-AI/gateway/blob/ca7712947ec8c0887803990b746740d36011c697/src/middlewares/requestValidator/index.ts#L289
- https://hackmd.io/@1ExmmukzRMWN7B4gQ4W-4Q/BJypv-aiMg
- https://www.vulncheck.com/advisories/portkey-ai-gateway-1.14.0-through-1.15.2-ssrf-via-x-portkey-custom-host-header

### [CVE-2026-73802](https://blog.gitea.com/release-of-runner-3.0.0/)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-73802
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-15 00:17:24 JST
- 更新日: 2026-10-15 01:04:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Gitea Runner passes workflow-controlled container options into Docker job container configuration while privileged mode is disabled. Host namespace settings, expanded capabilities, and security profile overrides can remain effective despite Privileged being forced false. A workflow author able to run jobs on an affecte...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://blog.gitea.com/release-of-runner-3.0.0/
- https://gitea.com/gitea/runner/releases/tag/v3.0.0
- https://github.com/go-gitea/gitea/security/advisories/GHSA-x4q3-gcj3-m6cf

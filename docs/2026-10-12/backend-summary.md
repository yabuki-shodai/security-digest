# Backend CVE Summary (2026-10-12)

## Overview

- 取得日時: 2026-10-12 10:15:24 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 12
- Critical: 0
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-19577](https://github.com/zephyrproject-rtos/zephyr/commit/b0b0e8973d1967114adbb9ed1611d448b5a46519)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-19577
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-12 03:16:58 JST
- 更新日: 2026-10-12 03:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: net_route_ipv6_packet() in subsys/net/ip/route_ipv6.c resolved the nexthop's link-layer address with net_nbr_get_lladdr(nbr->idx) without first checking whether the neighbor cache entry actually had a linked link-layer address. An unresolved neighbor carries idx == NET_NBR_LLADDR_UNKNOWN (0xff), and net_nbr_get_lladdr(...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/b0b0e8973d1967114adbb9ed1611d448b5a46519
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-vv76-4m89-95q5

### [CVE-2026-19735](https://github.com/zephyrproject-rtos/zephyr/commit/700888e3ecff8474f4fe7dfa8782b8869053222b)

> **Backend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-19735
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-12 03:16:58 JST
- 更新日: 2026-10-12 03:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The RFC 6528 initial-sequence-number implementation in subsys/net/ip/tcp.c derived every TCP ISN from SHA-256(unique_key || four-tuple) plus a uptime-derived offset, where unique_key is a 128-bit secret filled once by sys_csrand_get(). The return value of that call was discarded and the once guard was latched to true e...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/700888e3ecff8474f4fe7dfa8782b8869053222b
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-37mc-2q9v-fp64

### [CVE-2026-108772](https://glacier-tarsal-711.notion.site/abstruse-worker_cache_path_traversal-3d0b25e24b368035a445c1f09b0b34f6?source=copy_link)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-108772
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-12 08:16:56 JST
- 更新日: 2026-10-12 08:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security vulnerability has been detected in bleenco abstruse up to 2.1.0. This issue affects the function filepath.Join of the file server/api/worker/download_cache.go of the component Cache Endpoint. Such manipulation of the argument File leads to path traversal. The attack can be launched remotely. The exploit has...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://glacier-tarsal-711.notion.site/abstruse-worker_cache_path_traversal-3d0b25e24b368035a445c1f09b0b34f6?source=copy_link
- https://vuldb.com/cve/CVE-2026-108772
- https://vuldb.com/submit/958032
- https://vuldb.com/vuln/416553
- https://vuldb.com/vuln/416553/cti

### [CVE-2026-108773](https://vuldb.com/cve/CVE-2026-108773)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-108773
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-12 08:16:56 JST
- 更新日: 2026-10-12 08:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was detected in erzhongxmu JEEWMS up to 2026.09.27-W39. Impacted is the function docheck of the file src/main/java/com/zzjee/wm/controller/WmOmNoticeHController.java. Performing a manipulation of the argument goodscode results in sql injection. The attack may be initiated remotely. The exploit is now pu...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://vuldb.com/cve/CVE-2026-108773
- https://vuldb.com/submit/959588
- https://vuldb.com/vuln/416554
- https://vuldb.com/vuln/416554/cti

### [CVE-2026-19576](https://github.com/zephyrproject-rtos/zephyr/commit/42b52d571eb2113012c135276693042fd372fdea)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-19576
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-12 03:16:58 JST
- 更新日: 2026-10-12 03:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The Goodix GT9xx input driver in drivers/input/input_gt911.c reads the touch point count from the controller's status register and masks it with GT911_TOUCH_POINTS_MSK (0x0F), yielding a value of 0..15. In gt911_process() that value is used directly as the loop bound for filling point_reg[], a stack array sized to CONF...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/42b52d571eb2113012c135276693042fd372fdea
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-p7qh-fvwx-f7vr

### [CVE-2026-19736](https://github.com/zephyrproject-rtos/zephyr/commit/2c132efaf03a5d45aeaf7b0531c1107db7a36a3d)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-19736
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-10-12 03:16:58 JST
- 更新日: 2026-10-12 03:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The NXP MCUX TRNG entropy driver in drivers/entropy/entropy_mcux_trng.c passed the caller's byte count straight to the vendor SDK routine TRNG_GetRandomData(). On i.MX RT5xx and RT6xx parts the SDK compiles its TRNG_SW_HEALTH_TESTS variant, which always copies whole 32-bit words and draws entropy rounded up to a multip...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/2c132efaf03a5d45aeaf7b0531c1107db7a36a3d
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-3f6q-3949-rqph

### [CVE-2026-108879](https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_caller_identity_subjects.py)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-108879
- 関連キーワード: redis
- 影響製品: -
- 公開日: 2026-10-12 00:16:54 JST
- 更新日: 2026-10-12 00:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JeecgBoot through 3.9.5 contains an insecure direct object reference vulnerability in AiragBaseApiController that allows authenticated users to read other users' AI chat variables via the username parameter. Attackers can send POST requests to /airag/api/getChatVariable with a target appId, username, and variable name...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_caller_identity_subjects.py
- https://github.com/jeecgboot/JeecgBoot/blob/e3b9dc0aefe1943d9772b026f64ed671a7c82802/jeecg-boot/jeecg-boot-module/jeecg-boot-module-airag/src/main/java/org/jeecg/modules/airag/llm/controller/AiragBaseApiController.java#L47-L54
- https://www.vulncheck.com/advisories/jeecgboot-through-3.9.5-idor-via-airag-api-getchatvariable-username-parameter

### [CVE-2026-19669](https://github.com/zephyrproject-rtos/zephyr/commit/0d65ce46dda0626164503c50f37e6e1f59d310a9)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-19669
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-12 03:16:58 JST
- 更新日: 2026-10-12 03:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The user-mode syscall verifiers z_vrfy_fuel_gauge_get_props() and z_vrfy_fuel_gauge_set_props() in drivers/fuel_gauge/fuel_gauge_syscall_handlers.c declared two variable-length arrays, union fuel_gauge_prop_val k_vals[len] and fuel_gauge_prop_t k_props[len], sized directly by the caller-supplied len argument. len is an...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/0d65ce46dda0626164503c50f37e6e1f59d310a9
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-6ghg-cmrw-8gw5

### [CVE-2026-108883](https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_sys_thirdapp_edit_config_post.py)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-108883
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-12 00:16:55 JST
- 更新日: 2026-10-12 00:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JeecgBoot through 3.9.5 contains a missing authorization vulnerability in the editThirdAppConfig handler that allows any authenticated user to modify third-party application configurations. Low-privileged attackers can replace client id, client secret, agent id and corp id of DingTalk, WeCom or Feishu integrations to r...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_sys_thirdapp_edit_config_post.py
- https://github.com/jeecgboot/JeecgBoot/blob/e3b9dc0aefe1943d9772b026f64ed671a7c82802/jeecg-boot/jeecg-module-system/jeecg-system-biz/src/main/java/org/jeecg/modules/system/controller/ThirdAppController.java#L412-L438
- https://www.vulncheck.com/advisories/jeecgboot-through-3.9.5-missing-authorization-via-sys-thirdapp-editthirdappconfig

### [CVE-2026-108878](https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_app_query_by_id.py)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-108878
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-12 00:16:54 JST
- 更新日: 2026-10-12 00:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JeecgBootのAiragAppControllerにおける認可チェックの欠如
- 影響: 認証済みの低権限ユーザーが他ユーザーのAIアプリケーション設定（プロンプトやモデルID等）を閲覧・取得できる可能性があります。
- 推奨対応: JeecgBootを修正済みバージョンへ更新するか、該当エンドポイントに厳格な認可処理を追加してください。

#### References
- https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_app_query_by_id.py
- https://github.com/jeecgboot/JeecgBoot/blob/e3b9dc0aefe1943d9772b026f64ed671a7c82802/jeecg-boot/jeecg-boot-module/jeecg-boot-module-airag/src/main/java/org/jeecg/modules/airag/app/controller/AiragAppController.java#L196-L203
- https://www.vulncheck.com/advisories/jeecgboot-through-3.9.5-missing-authorization-via-airag-app-querybyid

### [CVE-2026-108882](https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_c324_sys_position_remove_user.py)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-108882
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-12 00:16:55 JST
- 更新日: 2026-10-12 00:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JeecgBootのSysPositionControllerにおける認可チェックの欠如
- 影響: 認証済みの低権限ユーザーがログを残さずに任意のユーザーの役職割り当てを削除できる可能性があります。
- 推奨対応: JeecgBootを修正済みバージョンへ更新するか、該当コントローラーに適切なアクセス制御を実装してください。

#### References
- https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_c324_sys_position_remove_user.py
- https://github.com/jeecgboot/JeecgBoot/blob/e3b9dc0aefe1943d9772b026f64ed671a7c82802/jeecg-boot/jeecg-module-system/jeecg-system-biz/src/main/java/org/jeecg/modules/system/controller/SysPositionController.java#L400-L405
- https://www.vulncheck.com/advisories/jeecgboot-through-3.9.5-missing-authorization-via-sys-position-removepositionuser

### [CVE-2026-18418](https://github.com/zephyrproject-rtos/zephyr/commit/fc065f79a568a6c6cc14b89795bd60e5eabd6f02)

> **Backend** / **LOW** / CVSS: **3.4** / KEV: **no**

- タイトル: CVE-2026-18418
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-12 03:16:58 JST
- 更新日: 2026-10-12 03:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: zbusプロキシエージェントにおけるNUL終端されていない配列のログ出力処理
- 影響: 拒否されたIPCフレーム処理時のログ出力においてOutOfBounds参照が生じ、メモリ不具合や情報漏洩を引き起こす可能性があります。
- 推奨対応: 関連する実装・修正パッチを適用し、文字列出力時のNUL終端検証を強化してください。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/fc065f79a568a6c6cc14b89795bd60e5eabd6f02
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-48w8-fjhj-r9w8

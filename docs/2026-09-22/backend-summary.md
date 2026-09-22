# Backend CVE Summary (2026-09-22)

## Overview

- 取得日時: 2026-09-22 09:45:37 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 21
- Critical: 2
- High: 13
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-77521](https://github.com/1Panel-dev/MaxKB/commit/594f50f2ea80a502d1c955371ba0438b277c30ea)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-77521
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 06:17:10 JST
- 更新日: 2026-09-22 06:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MaxKB 2.10.5-lts 未満における SandboxShellBackend のシェルコマンド実行制御不備によるリモートコード実行（RCE）の脆弱性。
- 影響: 信頼できない入力やチャット経由で人間による承認なしにシェルコマンドが実行され、システムが侵害される可能性があります。
- 推奨対応: MaxKB を 2.10.5-lts 以降へアップデートしてください。

#### References
- https://github.com/1Panel-dev/MaxKB/commit/594f50f2ea80a502d1c955371ba0438b277c30ea
- https://github.com/1Panel-dev/MaxKB/releases/tag/v2.10.5-lts
- https://github.com/1Panel-dev/MaxKB/security/advisories/GHSA-f36j-f34j-h3rx

### [CVE-2026-86473](https://github.com/apache/airflow/pull/72649)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-86473
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 00:17:32 JST
- 更新日: 2026-09-22 04:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache AirflowのCore APIログアウトエンドポイントにおいて、Authorization bearerヘッダーによるログアウト時にトークンが無効化されない不具合。
- 影響: ログアウト後もトークンが有効なままとなり、トークンを保持する第三者によりセッションが継続利用される可能性があります。
- 推奨対応: Apache Airflow 3.3.2 以降へアップグレードしてください。

#### References
- https://github.com/apache/airflow/pull/72649
- https://lists.apache.org/thread/k9z1p0q1ng8m68nlnv9d1fqzscrfm7vr
- http://www.openwall.com/lists/oss-security/2026/09/21/5

### [CVE-2026-61629](https://github.com/lucasdillmann/nginx-ignition/commit/0c988fc1277c7d291725e8373313f8486fa1b31a)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-61629
- 関連キーワード: go, golang, gin, nginx
- 影響製品: -
- 公開日: 2026-09-22 00:17:30 JST
- 更新日: 2026-09-22 00:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: nginx-ignition (2.29.0～2.40.0) のgin i18nミドルウェアにおいて、Accept-Languageヘッダーの解析処理で区切り文字（'_'）に対する適切な制限が行われない不具合。
- 影響: 未認証の攻撃者が大量の区切り文字を含むAccept-Languageヘッダーを送信することで、CPUリソースが過剰に消費され、サービス拒否（DoS）状態が引き起こされる可能性があります。
- 推奨対応: 修正された最新バージョンへのアップデートや、適切なリクエストヘッダー制限の設定を検討してください。

#### References
- https://github.com/lucasdillmann/nginx-ignition/commit/0c988fc1277c7d291725e8373313f8486fa1b31a
- https://github.com/lucasdillmann/nginx-ignition/commit/cbaf0fc16ed873f7178a2ca9b0d00a696e44b485
- https://github.com/lucasdillmann/nginx-ignition/security/advisories/GHSA-jr34-h97m-9hpx

### [CVE-2026-77560](https://github.com/tinyauthapp/tinyauth/commit/80bc87188ec3aabc5104c249eaa7b997973b9275)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-77560
- 関連キーワード: go, gin, docker
- 影響製品: -
- 公開日: 2026-09-22 02:18:52 JST
- 更新日: 2026-09-22 06:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tinyauth (5.1.2未満) において、転送されたホスト名の大文字小文字の比較処理の不備により、アクセス制御ルックアップがスキップされる脆弱性。
- 影響: 認証済みの低権限ユーザーがホスト名の大文字小文字を変更してアクセスすることで、アプリ単位のアクセス制限を迂回して不正アクセスする可能性があります。
- 推奨対応: Tinyauth 5.1.2 以降へアップデートしてください。

#### References
- https://github.com/tinyauthapp/tinyauth/commit/80bc87188ec3aabc5104c249eaa7b997973b9275
- https://github.com/tinyauthapp/tinyauth/commit/e75605b2c534ec83525a33603e16d76baca13399
- https://github.com/tinyauthapp/tinyauth/pull/1000
- https://github.com/tinyauthapp/tinyauth/pull/1028
- https://github.com/tinyauthapp/tinyauth/releases/tag/v5.1.2

### [CVE-2026-62182](https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.21.md)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-62182
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 03:17:09 JST
- 更新日: 2026-09-22 03:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KubeEdge (1.21.0～1.21.1, 1.22.0～1.22.1, 1.23.0) のConfigUpdateJob処理において、ユーザー入力値が不十分に検証されたままシステムシェルで実行される不具合。
- 影響: ConfigUpdateJobの作成・変更権限を持つユーザーが、ターゲットのエッジノード上で任意のコマンドを実行できる可能性があります。
- 推奨対応: KubeEdge 1.21.2、1.22.2、または 1.23.1 以降へアップグレードしてください。

#### References
- https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.21.md
- https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.22.md
- https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.23.md
- https://github.com/kubeedge/kubeedge/commit/14f65fc6207787f266cbcb0dceac7f09a81bab2b
- https://github.com/kubeedge/kubeedge/commit/6309a335c8e5e3c154b6bb0a09292f5c7dc598dc

### [CVE-2026-62369](https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.21.md)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-62369
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 03:17:09 JST
- 更新日: 2026-09-22 03:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KubeEdge (1.16.0～1.21.1, 1.22.0～1.22.1, 1.23.0) のkeadmにおける解凍処理（DecompressTarGz）でのパス・トラバーサルの脆弱性。
- 影響: Windows環境での展開時に、意図しないディレクトリへファイルが書き込み・上書きされ、設定や実行ファイルの改ざん、コード実行に繋がる可能性があります。
- 推奨対応: KubeEdge 1.21.2、1.22.2、または 1.23.1 以降へアップグレードしてください。

#### References
- https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.21.md
- https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.22.md
- https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.23.md
- https://github.com/kubeedge/kubeedge/commit/47767b7f2649afcfa3a856e87d556f7777e0428d
- https://github.com/kubeedge/kubeedge/commit/a524a66a1ae1691eb8ff16b6ff9a93fb370d4047

### [CVE-2026-62371](https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.21.md)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-62371
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 02:17:37 JST
- 更新日: 2026-09-22 04:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KubeEdge (1.12.0～1.21.1, 1.22.0～1.22.1, 1.23.0) のNodeUpgradeJobハンドラにおいて、入力パラメータが不十分に検証されたままシェルコマンドへ結合される不具合。
- 影響: NodeUpgradeJobの作成・更新権限を持つユーザーが、ターゲットのエッジノード上で任意のコマンドを実行できる可能性があります。
- 推奨対応: KubeEdge 1.21.2、1.22.2、または 1.23.1 以降へアップグレードしてください。

#### References
- https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.21.md
- https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.22.md
- https://github.com/kubeedge/kubeedge/blob/master/CHANGELOG/CHANGELOG-1.23.md
- https://github.com/kubeedge/kubeedge/commit/552af457a4c7ce80ea1678ab5889f475b36ea103
- https://github.com/kubeedge/kubeedge/commit/657b745bebcdd7a221eb34c0aac13231ef12c37f

### [CVE-2026-75939](https://access.redhat.com/security/cve/CVE-2026-75939)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-75939
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 00:17:31 JST
- 更新日: 2026-09-22 00:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openshift/oc-mirrorにおいて、PGPリリースイメージの署名検証処理に欠陥があり、完全な検証が行われる前に処理が終了する不具合。
- 影響: 攻撃者によって偽造された署名が受け入れられ、悪意のあるペイロードがレジストリにミラーリングされてソフトウェア展開の完全性が損なわれる可能性があります。
- 推奨対応: 修正版へのアップデートを実施し、通信経路の適切なセキュリティ対策を行ってください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-75939
- https://bugzilla.redhat.com/show_bug.cgi?id=2517976

### [CVE-2026-52741](https://github.com/gocd/gocd/commit/1adba7ded0b9ef57e29f1de876a882199e5da1d4)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-52741
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-09-22 00:17:28 JST
- 更新日: 2026-09-22 00:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GoCD (18.3.0～26.0.0) において、コミットコメントからトラッキングツールリンクを生成する際のエスケープ処理不足による脆弱性。
- 影響: コミット権限を持つ攻撃者が悪意あるコメントを投稿することで、Compare Pipelineページを閲覧したユーザーのブラウザ上で蓄積型XSSが実行され、セッション悪用などが生じる可能性があります。
- 推奨対応: GoCD 26.1.0 以降へアップグレードしてください。

#### References
- https://github.com/gocd/gocd/commit/1adba7ded0b9ef57e29f1de876a882199e5da1d4
- https://github.com/gocd/gocd/pull/14356
- https://github.com/gocd/gocd/releases/tag/26.1.0
- https://github.com/gocd/gocd/security/advisories/GHSA-hj3c-q23m-fxcg
- https://www.gocd.org/releases/#26-1-0

### [CVE-2026-61647](https://github.com/roomi-fields/notebooklm-mcp/security/advisories/GHSA-jjhp-8crj-mppq)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-61647
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-22 06:17:07 JST
- 更新日: 2026-09-22 06:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NotebookLM MCP (1.6.0～2.0.2) のバッチ処理エンドポイントにおけるパス・トラバーサルの脆弱性。
- 影響: 攻撃者が指定したパラメータにより、サーバープロセスが書き込み権限を持つ任意のディレクトリへファイルが生成される可能性があります。
- 推奨対応: バージョン 2.0.3 以降へアップグレードし NOTEBOOKLM_VAULT_ROOT を設定してください。適用できない場合は最小権限での実行やアクセス制限を行ってください。

#### References
- https://github.com/roomi-fields/notebooklm-mcp/security/advisories/GHSA-jjhp-8crj-mppq

### [CVE-2026-93340](https://github.com/GladysAssistant/Gladys/releases/tag/v5.1.0)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-93340
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-22 07:16:59 JST
- 更新日: 2026-09-22 07:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Gladys Assistant (5.1.0未満) のforgot_passwordエンドポイントにおけるOriginパラメータの検証不足によるパスワードリセットリンクポイズニングの脆弱性。
- 影響: 未認証の攻撃者が悪意あるOriginを指定したリクエストを送信することで、リセットトークンを取得し、管理者を含むアカウントを乗っ取る可能性があります。
- 推奨対応: Gladys Assistant 5.1.0 以降へアップデートしてください。

#### References
- https://github.com/GladysAssistant/Gladys/releases/tag/v5.1.0
- https://gladysassistant.com/blog/gladys-5-1-integration-widgets-and-scenes/
- https://www.vulncheck.com/advisories/gladys-assistant-password-reset-link-poisoning-via-forgot-password-endpoint

### [CVE-2026-55625](https://github.com/gocd/gocd/commit/f0dda0fb8af4cff5e2f4bf52b753fb41a7ec8918)

> **Backend** / **MEDIUM** / CVSS: **4.9** / KEV: **no**

- タイトル: CVE-2026-55625
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-22 00:17:29 JST
- 更新日: 2026-09-22 00:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GoCD is a continuous deliver server. From 16.1.0 until 26.1.0, the internal material connection test APIs at /go/api/admin/internal/material_test and /go/api/internal/config_repos/*/material_test accept an arbitrary existing pipeline and pipeline-group context without sufficient validation. A pipeline group administrat...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gocd/gocd/commit/f0dda0fb8af4cff5e2f4bf52b753fb41a7ec8918
- https://github.com/gocd/gocd/releases/tag/26.1.0
- https://github.com/gocd/gocd/security/advisories/GHSA-4557-94j8-5p66
- https://www.gocd.org/releases/#26-1-0

### [CVE-2026-48826](https://github.com/sysadminsmedia/homebox/commit/ed3216a80998dfd81d4418700696244144883160)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-48826
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 03:17:08 JST
- 更新日: 2026-09-22 06:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HomeBox is a home inventory and organization system. Prior to 0.26.0, HandleWipeInventory in backend/app/api/handlers/v1/v1_ctrl_actions.go authorizes POST /v1/actions/wipe-inventory through the global ctx.User.IsOwner value instead of the caller's role in the active group, while the active group is selected through th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/sysadminsmedia/homebox/commit/ed3216a80998dfd81d4418700696244144883160
- https://github.com/sysadminsmedia/homebox/releases/tag/v0.26.0
- https://github.com/sysadminsmedia/homebox/security/advisories/GHSA-559j-7w3w-4fr7

### [CVE-2026-48975](https://github.com/sysadminsmedia/homebox/commit/ed3216a80998dfd81d4418700696244144883160)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-48975
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 03:17:08 JST
- 更新日: 2026-09-22 04:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HomeBox is a home inventory and organization system. Prior to 0.26.0, MaintenanceEntryRepository.Update and MaintenanceEntryRepository.Delete in backend/internal/data/repo/repo_maintenance_entry.go use UpdateOneID(id) and DeleteOneID(id) without verifying that the maintenance entry belongs to the authenticated user's a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/sysadminsmedia/homebox/commit/ed3216a80998dfd81d4418700696244144883160
- https://github.com/sysadminsmedia/homebox/releases/tag/v0.26.0
- https://github.com/sysadminsmedia/homebox/security/advisories/GHSA-7mr6-2wxw-27j9

### [CVE-2026-48976](https://github.com/sysadminsmedia/homebox/commit/ed3216a80998dfd81d4418700696244144883160)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-48976
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 03:17:08 JST
- 更新日: 2026-09-22 03:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HomeBox is a home inventory and organization system. Prior to 0.26.0, NotifierRepository.Update in backend/internal/data/repo/repo_notifier.go updates a notifier through UpdateOneID(id) without requiring the record's user ID to match the authenticated user. An authenticated user who supplies another tenant's notifier U...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/sysadminsmedia/homebox/commit/ed3216a80998dfd81d4418700696244144883160
- https://github.com/sysadminsmedia/homebox/releases/tag/v0.26.0
- https://github.com/sysadminsmedia/homebox/security/advisories/GHSA-mc8h-5c5v-37p7

### [CVE-2026-61687](https://github.com/hatchet-dev/hatchet/commit/f90464189ad642251e09412d0f99fde353036428)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-61687
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 01:17:09 JST
- 更新日: 2026-09-22 06:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Hatchet is a platform for orchestrating background tasks, AI agents, and durable workflows at scale. Prior to 0.91.1, ValidateOAuthState clears the oauth_state_ session value to an empty string after a successful OAuth callback and later accepts an empty state parameter as equal, allowing an unauthenticated attacker to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/hatchet-dev/hatchet/commit/f90464189ad642251e09412d0f99fde353036428
- https://github.com/hatchet-dev/hatchet/security/advisories/GHSA-phg3-3g28-wq9v

### [CVE-2026-55473](https://github.com/sysadminsmedia/homebox/commit/42c52f7f7566b7fbd8017352187af20f552a4471)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-55473
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 03:17:08 JST
- 更新日: 2026-09-22 03:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HomeBox is a home inventory and organization system. Prior to 0.26.0, the default-on BlockBogonNets and BlockCloudMetadata notifier SSRF protections in backend/internal/sys/validate/notifier_url.go do not inspect IPv4 destinations embedded in the NAT64 prefixes 64:ff9b::/96 and 64:ff9b:1::/48. An authenticated user can...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/sysadminsmedia/homebox/commit/42c52f7f7566b7fbd8017352187af20f552a4471
- https://github.com/sysadminsmedia/homebox/releases/tag/v0.26.0
- https://github.com/sysadminsmedia/homebox/security/advisories/GHSA-r9pf-rg22-655m

### [CVE-2026-55870](https://github.com/gocd/gocd/commit/19c415d918bb50cb5a3ab7c28e01f4dd51ecb6a5)

> **Backend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-55870
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-22 00:17:30 JST
- 更新日: 2026-09-22 06:17:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GoCD is a continuous deliver server. Prior to 26.1.0, GoCD can return unmasked credentials that administrators stored in the userinfo portion of source control material URLs through several read-only APIs available to regular authenticated users. Although GoCD recommends dedicated username and password fields or secret...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gocd/gocd/commit/19c415d918bb50cb5a3ab7c28e01f4dd51ecb6a5
- https://github.com/gocd/gocd/releases/tag/26.1.0
- https://github.com/gocd/gocd/security/advisories/GHSA-5m25-5j77-c887
- https://www.gocd.org/releases/#26-1-0

### [CVE-2026-59168](https://github.com/TomWright/dasel/commit/4c91d0d02dc59ce8404709b1bfed7a6fabe62f68)

> **Backend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-59168
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 02:17:36 JST
- 更新日: 2026-09-22 06:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dasel is a command-line tool and library for querying, modifying, and transforming data structures. From 3.0.0 until 3.11.1, parsing/json/json_reader.go decodeValue, decodeObject, and decodeArray, and parsing/xml/reader.go parseElement, recurse once per input nesting level without a depth guard. Deeply nested attacker-...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/TomWright/dasel/commit/4c91d0d02dc59ce8404709b1bfed7a6fabe62f68
- https://github.com/TomWright/dasel/releases/tag/v3.11.1
- https://github.com/TomWright/dasel/security/advisories/GHSA-cqxr-jxr2-85pq

### [CVE-2026-62866](https://github.com/TomWright/dasel/commit/eee03aec28d4a33d6138098d065b7b37b85e3c55)

> **Backend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-62866
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-22 02:17:38 JST
- 更新日: 2026-09-22 03:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Dasel is a command-line tool and library for querying, modifying, and transforming data structures. From 3.0.0 until 3.11.2, selector/lexer/tokenize.go parseCurRune advances the input index across trailing whitespace and then reads the source at the exhausted index without an end-of-input check. A selector ending in wh...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/TomWright/dasel/commit/eee03aec28d4a33d6138098d065b7b37b85e3c55
- https://github.com/TomWright/dasel/releases/tag/v3.11.2
- https://github.com/TomWright/dasel/security/advisories/GHSA-65gg-g7rw-6cpc
- https://github.com/TomWright/dasel/security/advisories/GHSA-65gg-g7rw-6cpc

### [CVE-2026-77582](https://github.com/tinyauthapp/tinyauth/commit/c22925c2fba981875d0a2b09dd3ee41c0ae4c310)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-77582
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-22 02:18:53 JST
- 更新日: 2026-09-22 02:18:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tinyauth is an authentication and authorization server. Prior to 5.1.0, Tinyauth exposes a remotely observable timing difference between authentication attempts for existing and nonexistent local usernames. internal/controller/user_controller.go loginHandler and internal/middleware/context_middleware.go basicAuth retur...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/tinyauthapp/tinyauth/commit/c22925c2fba981875d0a2b09dd3ee41c0ae4c310
- https://github.com/tinyauthapp/tinyauth/pull/1004
- https://github.com/tinyauthapp/tinyauth/releases/tag/v5.1.0
- https://github.com/tinyauthapp/tinyauth/security/advisories/GHSA-456h-ww26-f758

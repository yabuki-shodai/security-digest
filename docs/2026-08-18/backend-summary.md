# Backend CVE Summary (2026-08-18)

## Overview

- 取得日時: 2026-08-18 07:36:00 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 22
- Critical: 4
- High: 12
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-71479](https://github.com/QuantumNous/new-api/commit/c9943d37ad93477dd937fc4901cc3c4e0fd8aaab)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-71479
- 関連キーワード: go, express
- 影響製品: -
- 公開日: 2026-08-18 01:17:44 JST
- 更新日: 2026-08-18 04:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: New APIにおけるクォータ計算処理の数値オーバーフローの脆弱性
- 影響: 低権限ユーザーがマイナス課金を発生させてアカウントクレジットに変換し、上位サービスの資金を不当に消費・枯渇させる可能性があります。
- 推奨対応: New APIをバージョン 1.0.0-rc.18 以降に更新してください。

#### References
- https://github.com/QuantumNous/new-api/commit/c9943d37ad93477dd937fc4901cc3c4e0fd8aaab
- https://github.com/QuantumNous/new-api/commit/d0bd8aac742d1e160a5ca61743fe35f4fff880e8
- https://github.com/QuantumNous/new-api/releases/tag/v1.0.0-rc.18
- https://github.com/QuantumNous/new-api/security/advisories/GHSA-8r8v-xf7q-rcpr

### [CVE-2026-35219](https://github.com/Budibase/budibase/commit/cc07563a6b0fc0f91c51aae295952b1295546a90)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-35219
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-18 06:16:44 JST
- 更新日: 2026-08-18 06:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Budibaseの自動化ステップにおけるIPブラックリスト制限の欠如（SSRF）
- 影響: 認証済みユーザーがサーバー経由でリクエストを送信し、内部サービスやクラウドのメタデータにアクセスする可能性があります。
- 推奨対応: Budibaseをバージョン 3.41.3 以降に更新してください。

#### References
- https://github.com/Budibase/budibase/commit/cc07563a6b0fc0f91c51aae295952b1295546a90
- https://github.com/Budibase/budibase/pull/19328
- https://github.com/Budibase/budibase/releases/tag/3.41.3
- https://github.com/Budibase/budibase/security/advisories/GHSA-5fpj-28rv-84r7

### [CVE-2026-64868](https://github.com/QuantumNous/new-api/commit/d2f7f9ee3adf3ef66798783a60d7bc712451c85c)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-64868
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-18 01:17:22 JST
- 更新日: 2026-08-18 02:16:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: New API is a large language mode (LLM) gateway and artificial intelligence (AI) asset management system. Prior to 1.0.0-rc.11, POST /api/stripe/webhook, POST /api/creem/webhook, and POST /api/waffo/webhook read and log full request bodies before signature validation in router/api-router.go and the payment controllers,...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/QuantumNous/new-api/commit/d2f7f9ee3adf3ef66798783a60d7bc712451c85c
- https://github.com/QuantumNous/new-api/pull/5244
- https://github.com/QuantumNous/new-api/releases/tag/v1.0.0-rc.11
- https://github.com/QuantumNous/new-api/security/advisories/GHSA-v828-m3pf-vq9q

### [CVE-2026-59829](https://github.com/discourse/discourse/commit/4df0e54f59361c78606b578ad12a2c39b4dd9f59)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-59829
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-18 01:17:01 JST
- 更新日: 2026-08-18 04:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Discourse is an open-source discussion platform. Prior to 2026.1.6, 2026.5.2, 2026.6.1, and 2026.7.1, on sites with category group moderation enabled, the review queue could include an excerpt (and permalink) of the private message attached to a flag, even when the reviewing category moderator was not a participant in...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/discourse/discourse/commit/4df0e54f59361c78606b578ad12a2c39b4dd9f59
- https://github.com/discourse/discourse/commit/58e45dc7c92d19d5294c73fbcd3833c73dc51754
- https://github.com/discourse/discourse/commit/74c8522a197658c69b0adefa182f601ce85dcefa
- https://github.com/discourse/discourse/commit/e56bd3ec58ae387946220821d1ce214eed02d1b9
- https://github.com/discourse/discourse/pull/41527

### [CVE-2026-54336](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-x6rg-36j6-76vr)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-54336
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-18 06:16:45 JST
- 更新日: 2026-08-18 06:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JumpServer is an open source bastion host and an operation and maintenance security audit system. From 4.8.0 until 4.10.17, an authenticated user with SFTP permission to an authorized asset can submit crafted traversal paths through the KoKo Web Terminal SFTP feature, causing AssetDir.GetRealPath() in pkg/srvconn/sftp_...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/jumpserver/jumpserver/security/advisories/GHSA-x6rg-36j6-76vr
- https://github.com/jumpserver/koko/commit/02fabebe27dacce89114fba122c667a946fd12ea
- https://github.com/jumpserver/koko/releases/tag/v4.10.17

### [CVE-2026-64865](https://github.com/QuantumNous/new-api/commit/dfc0d6324b40c1d6c2972e524409f933541bfb0f)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-64865
- 関連キーワード: go, redis
- 影響製品: -
- 公開日: 2026-08-18 01:17:22 JST
- 更新日: 2026-08-18 01:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: New API is a large language mode (LLM) gateway and artificial intelligence (AI) asset management system. Prior to 1.0.0-rc.16, repeated PUT /api/user/self requests that update language or sidebar_modules can race relay billing because controller/user.go calls User.Update and updateUserCache performs a full RedisHSetObj...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/QuantumNous/new-api/commit/dfc0d6324b40c1d6c2972e524409f933541bfb0f
- https://github.com/QuantumNous/new-api/releases/tag/v1.0.0-rc.16
- https://github.com/QuantumNous/new-api/security/advisories/GHSA-j6gc-4893-qwmp

### [CVE-2026-64866](https://github.com/QuantumNous/new-api/commit/0936e2504655a5cbf7bc3c388f6d3e2bb24916d3)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-64866
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-18 01:17:22 JST
- 更新日: 2026-08-18 07:17:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: New API is a large language mode (LLM) gateway and artificial intelligence (AI) asset management system. From 0.9.1.3 until 1.0.0-rc.7, AdminResetPasskey in controller/passkey.go lacks the canManageTargetRole authorization check for DELETE /api/user/:id/reset_passkey, allowing a lower-privileged administrator to remove...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/QuantumNous/new-api/commit/0936e2504655a5cbf7bc3c388f6d3e2bb24916d3
- https://github.com/QuantumNous/new-api/pull/4929
- https://github.com/QuantumNous/new-api/releases/tag/v1.0.0-rc.7
- https://github.com/QuantumNous/new-api/security/advisories/GHSA-p845-629j-rcj6

### [CVE-2026-67966](https://github.com/H0111mes/Tenda-W20E-Vulnerability-Disclosure)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-67966
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-18 06:16:47 JST
- 更新日: 2026-08-18 06:16:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tenda W20E V16.01.0.6(2782) /goform/telnet endpoint allows unauthenticated remote attackers to activate the Telnet daemon and obtain root shell access.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/H0111mes/Tenda-W20E-Vulnerability-Disclosure

### [CVE-2026-34398](https://github.com/FreeCAD/FreeCAD/commit/871ee19b76224910332bbfbd39eebbede967998b)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-34398
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-18 06:16:44 JST
- 更新日: 2026-08-18 06:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreeCAD is a free and open-source multiplatform 3D parametric modeler. From 0.19 until 1.1.1, src/Mod/BIM/bimcommands/BimProjectManager.py in the BIM Project Manager Load Template flow passes attacker-controlled FCStd Meta property values for wpposition, wpu, wpv, and wpaxis directly to eval(), allowing arbitrary Pytho...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FreeCAD/FreeCAD/commit/871ee19b76224910332bbfbd39eebbede967998b
- https://github.com/FreeCAD/FreeCAD/commit/9ed351cc4700db0a94c46f020c34c58bbf1bdaba
- https://github.com/FreeCAD/FreeCAD/pull/28610
- https://github.com/FreeCAD/FreeCAD/releases/tag/1.1.1
- https://github.com/FreeCAD/FreeCAD/security/advisories/GHSA-8rfj-7956-6gwf

### [CVE-2026-34399](https://github.com/FreeCAD/FreeCAD/releases/tag/1.1.1)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-34399
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-18 06:16:44 JST
- 更新日: 2026-08-18 06:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreeCAD is a free and open-source multiplatform 3D parametric modeler. From 0.19 until 1.1.1, FreeCAD's BIM Workbench contains an eval() call on untrusted data from SVG template files. When a user creates a TechDraw page from a malicious SVG template, arbitrary Python code executes. The vulnerable code is in src/Mod/BI...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FreeCAD/FreeCAD/releases/tag/1.1.1
- https://github.com/FreeCAD/FreeCAD/security/advisories/GHSA-chv4-vm6r-wjqj

### [CVE-2026-34789](https://github.com/FreeCAD/FreeCAD/commit/81b73925ce22610542367301d8eff4259eb9596e)

> **Backend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-34789
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-18 06:16:44 JST
- 更新日: 2026-08-18 06:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FreeCAD is a free and open-source multiplatform 3D parametric modeler. Prior to 1.1.2, src/App/PropertyPythonObject.cpp in PropertyPythonObject::Restore() passes the attacker-controlled module attribute from serialized PropertyPythonObject XML directly to PyImport_ImportModule() while restoring a crafted FCStd document...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/FreeCAD/FreeCAD/commit/81b73925ce22610542367301d8eff4259eb9596e
- https://github.com/FreeCAD/FreeCAD/commit/983037f3003dc31f48db36705b86fb3fbe026295
- https://github.com/FreeCAD/FreeCAD/commit/e2dc6c8172673642c6856b8b3a5a6accefb18279
- https://github.com/FreeCAD/FreeCAD/releases/tag/1.1.2
- https://github.com/FreeCAD/FreeCAD/security/advisories/GHSA-493w-pp4h-h77v

### [CVE-2026-71491](https://github.com/andialbrecht/sqlparse/commit/ef2012a5eeb491e604dea2b00d516904a3830c87)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-71491
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-08-18 03:18:12 JST
- 更新日: 2026-08-18 07:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: sqlparse is a non-validating SQL parser module for Python. Prior to 0.6.0, group_comments in sqlparse/engine/grouping.py repeatedly rescans comment-only statements before the MAX_GROUPING_TOKENS guard, causing quadratic CPU consumption through sqlparse.parse() and sqlparse.format(sql, strip_comments=True). This issue i...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/andialbrecht/sqlparse/commit/ef2012a5eeb491e604dea2b00d516904a3830c87
- https://github.com/andialbrecht/sqlparse/security/advisories/GHSA-f2ff-p2ww-7p4p

### [CVE-2026-54284](https://github.com/andialbrecht/sqlparse/commit/939b129e24c0ad5d51368b1aa72fffcaca76f06f)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-54284
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-18 03:17:11 JST
- 更新日: 2026-08-18 05:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: sqlparseにおけるTokenList構築および文字列変換時のネストされたトークンサブツリー処理の不具合
- 影響: 解析やフォーマット処理時に過剰なCPU消費が発生し、サービス拒否（DoS）状態に陥る可能性があります。
- 推奨対応: sqlparse 0.6.0 以降へアップデートしてください。

#### References
- https://github.com/andialbrecht/sqlparse/commit/939b129e24c0ad5d51368b1aa72fffcaca76f06f
- https://github.com/andialbrecht/sqlparse/security/advisories/GHSA-pwgv-4x5q-6m9f
- https://github.com/andialbrecht/sqlparse/security/advisories/GHSA-pwgv-4x5q-6m9f

### [CVE-2026-59893](https://github.com/andialbrecht/sqlparse/commit/d1d80602741f77ec78e5a04ce4719244cf32352e)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-59893
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-18 03:17:35 JST
- 更新日: 2026-08-18 04:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: sqlparseにおける未一致の文字区切りやコメントの走査処理に関する不具合
- 影響: 特定の入力処理において繰り返しスキャンが発生し、過剰なCPU消費によるサービス拒否（DoS）を引き起こす可能性があります。
- 推奨対応: sqlparse 0.6.0 以降へアップデートしてください。

#### References
- https://github.com/andialbrecht/sqlparse/commit/d1d80602741f77ec78e5a04ce4719244cf32352e
- https://github.com/andialbrecht/sqlparse/security/advisories/GHSA-prg7-hcfm-mfcr
- https://github.com/andialbrecht/sqlparse/security/advisories/GHSA-prg7-hcfm-mfcr

### [CVE-2026-59894](https://github.com/andialbrecht/sqlparse/security/advisories/GHSA-3496-9g83-7v6x)

> **Backend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-59894
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-18 03:17:35 JST
- 更新日: 2026-08-18 07:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: sqlparseのPython/PHP出力フォーマット処理におけるバックスラッシュのエスケープ不足
- 影響: 生成されたコードを実行または読み込む後続処理において、任意のPythonまたはPHPコードが注入・実行される可能性があります。
- 推奨対応: sqlparse 0.6.0 以降へアップデートしてください。

#### References
- https://github.com/andialbrecht/sqlparse/security/advisories/GHSA-3496-9g83-7v6x

### [CVE-2025-27770](https://github.com/uptrain-ai/uptrain/blob/a31cc14eddcb6c0b0b12cbed15f086d98c441c6f/uptrain/dashboard/backend/app.py#L691C22-L691C36)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2025-27770
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-18 01:16:46 JST
- 更新日: 2026-08-18 01:16:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: UpTrainの `/create_project` エンドポイントにおけるパラメータ検証不足によるリモートコード実行の脆弱性
- 影響: 認証されたユーザーにより、UpTrainを実行しているホスト環境（主にDockerコンテナ内）で任意のコードを実行される可能性があります。
- 推奨対応: 現時点で公式パッチは未公開です。アクセス制限やネットワーク分離などの緩和策を実施してください。

#### References
- https://github.com/uptrain-ai/uptrain/blob/a31cc14eddcb6c0b0b12cbed15f086d98c441c6f/uptrain/dashboard/backend/app.py#L691C22-L691C36
- https://securitylab.github.com/advisories/GHSL-2024-198_GHSL-2024-199_Uptrain/

### [CVE-2025-27771](https://github.com/uptrain-ai/uptrain/blob/a31cc14eddcb6c0b0b12cbed15f086d98c441c6f/uptrain/dashboard/backend/app.py#L773C22-L773C30)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2025-27771
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-18 01:16:46 JST
- 更新日: 2026-08-18 07:16:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: UpTrainの `/add_prompts` エンドポイントにおけるパラメータ検証不足によるリモートコード実行の脆弱性
- 影響: 認証されたユーザーにより、UpTrainを実行しているホスト環境（主にDockerコンテナ内）で任意のコードを実行される可能性があります。
- 推奨対応: 現時点で公式パッチは未公開です。アクセス制御を徹底するなどの緩和策を実施してください。

#### References
- https://github.com/uptrain-ai/uptrain/blob/a31cc14eddcb6c0b0b12cbed15f086d98c441c6f/uptrain/dashboard/backend/app.py#L773C22-L773C30
- https://securitylab.github.com/advisories/GHSL-2024-200_GHSL-2024-201_Uptrain/

### [CVE-2025-27772](https://github.com/uptrain-ai/uptrain/blob/a31cc14eddcb6c0b0b12cbed15f086d98c441c6f/uptrain/dashboard/backend/app.py#L773)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2025-27772
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-08-18 01:16:46 JST
- 更新日: 2026-08-18 05:16:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: UpTrainの `/new_run` エンドポイントにおけるパラメータ検証不足によるリモートコード実行の脆弱性
- 影響: 認証されたユーザーにより、UpTrainを実行しているホスト環境（主にDockerコンテナ内）で任意のコードを実行される可能性があります。
- 推奨対応: 現時点で公式パッチは未公開です。アクセス権限の見直しなど緩和策の実施を推奨します。

#### References
- https://github.com/uptrain-ai/uptrain/blob/a31cc14eddcb6c0b0b12cbed15f086d98c441c6f/uptrain/dashboard/backend/app.py#L773
- https://securitylab.github.com/advisories/GHSL-2024-200_GHSL-2024-201_Uptrain/

### [CVE-2026-64657](https://github.com/Budibase/budibase/commit/67572a82c3850964f388bfd969779dc025a80224)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-64657
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-08-18 06:16:46 JST
- 更新日: 2026-08-18 06:16:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: BudibaseのPostgreSQLデータソース設定におけるSQLインジェクションの脆弱性
- 影響: 認証された管理者がデータソースのテストや保存を行う際、任意のSQLコマンドを実行される可能性があります。
- 推奨対応: Budibase 3.39.19 以降へアップデートしてください。

#### References
- https://github.com/Budibase/budibase/commit/67572a82c3850964f388bfd969779dc025a80224
- https://github.com/Budibase/budibase/security/advisories/GHSA-qqf5-x7mj-v43p

### [CVE-2026-47686](https://github.com/patriksimek/vm2/commit/7e3faaf550f4ab975bf4cdde183fcec49b056d8e)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-47686
- 関連キーワード: node.js
- 影響製品: -
- 公開日: 2026-08-18 06:16:45 JST
- 更新日: 2026-08-18 06:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: vm2の例外ハンドラ処理における `Error.cause` のサニタイズ不備によるサンドボックス回避の脆弱性
- 影響: サンドボックス内のコードからホストオブジェクトにアクセスされ、任意のホストコマンドを実行される可能性があります。
- 推奨対応: vm2 3.11.6 以降へアップデートしてください。

#### References
- https://github.com/patriksimek/vm2/commit/7e3faaf550f4ab975bf4cdde183fcec49b056d8e
- https://github.com/patriksimek/vm2/releases/tag/3.11.6
- https://github.com/patriksimek/vm2/security/advisories/GHSA-m283-3h24-438v

### [CVE-2026-47698](https://github.com/patriksimek/vm2/commit/a85acb61f81402c6eabf32760aa11272af6d0f9e)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-47698
- 関連キーワード: node.js
- 影響製品: -
- 公開日: 2026-08-18 06:16:45 JST
- 更新日: 2026-08-18 06:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: vm2におけるプロトタイプ操作制限の不足によるサンドボックス回避の脆弱性
- 影響: サンドボックス内のコードがプロトタイプチェーンを切断し、任意のホストコマンドを実行できる可能性があります。
- 推奨対応: vm2 3.11.6 以降へアップデートしてください。

#### References
- https://github.com/patriksimek/vm2/commit/a85acb61f81402c6eabf32760aa11272af6d0f9e
- https://github.com/patriksimek/vm2/releases/tag/3.11.6
- https://github.com/patriksimek/vm2/security/advisories/GHSA-cfcw-xp6x-25gj

### [CVE-2026-74253](https://regularlabs.com/)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-74253
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-18 03:18:14 JST
- 更新日: 2026-08-18 03:18:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla向け拡張機能Regular Labs Sourcererにおける未検証の入力処理に起因する脆弱性
- 影響: 未認証の第三者によって、リモートで任意のコードを実行（RCE）される可能性があります。
- 推奨対応: Regular Labs Sourcerer 14.0.0 以降へアップデートしてください。

#### References
- https://regularlabs.com/

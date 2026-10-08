# Backend CVE Summary (2026-10-08)

## Overview

- 取得日時: 2026-10-08 10:51:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 26
- Critical: 12
- High: 14
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-107204](https://github.com/LMCache/LMCache)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-107204
- 関連キーワード: python, fastapi
- 影響製品: -
- 公開日: 2026-10-08 01:17:45 JST
- 更新日: 2026-10-08 02:16:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LMCache の /run_script エンドポイントにおける未認証のリモートコード実行（RCE）の脆弱性。
- 影響: 未認証の攻撃者が任意コードやOSコマンドを実行し、システムを侵害できる可能性があります。
- 推奨対応: LMCache を最新版にアップデートするか、対象エンドポイントへのアクセスを制限・無効化してください。

#### References
- https://github.com/LMCache/LMCache
- https://github.com/LMCache/LMCache/blob/v0.5.5/lmcache/v1/internal_api_server/common/run_script_api.py#L54-L76
- https://github.com/LMCache/LMCache/blob/v0.5.5/lmcache/v1/multiprocess/http_apis/common_api.py#L41-L46
- https://github.com/LMCache/LMCache/issues/5510
- https://www.vulncheck.com/advisories/lmcache-through-0.5.5-unauthenticated-rce-via-run-script-endpoint

### [CVE-2026-76500](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-apic-UOXWtfh)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76500
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:17:01 JST
- 更新日: 2026-10-08 02:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Application Policy Infrastructure Controller (APIC) におけるリソース管理の不備（CWE-664）に関する脆弱性。
- 影響: リソースの適切なライフサイクル制御が行われず、不正な操作やシステム障害を引き起こす可能性があります。
- 推奨対応: シスコが提供する修正済みソフトウェア（ハードニングリリース）へ更新してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-apic-UOXWtfh

### [CVE-2026-76455](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76455
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:16:57 JST
- 更新日: 2026-10-08 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco NX-OS における不適切なアクセス制御（CWE-284）の脆弱性。
- 影響: 本来制限されるべきリソースや機能へ不正アクセスされる可能性があります。
- 推奨対応: シスコが提供する修正済みソフトウェアへのアップデートを実施してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR

### [CVE-2026-76464](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-76464
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:16:59 JST
- 更新日: 2026-10-08 04:17:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco ネットワーク製品における不適切なバッファ管理の脆弱性 (CWE-119)。
- 影響: バッファ処理の不備による影響が生じる可能性があるが、詳細な攻撃シナリオは不明。
- 推奨対応: Ciscoから提供されるセキュリティ修正版ソフトウェアを適用する。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH

### [CVE-2026-76480](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ssm-Ph77wdhf)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76480
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:17:00 JST
- 更新日: 2026-10-08 02:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco License On-Prem (旧 SSM On-Prem) における認証欠如・不備（CWE-306）の脆弱性。
- 影響: 未認証の第三者によって特定の機能や情報へアクセスされる可能性があります。
- 推奨対応: シスコが提供する修正版ソフトウェアへアップデートしてください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ssm-Ph77wdhf

### [CVE-2026-76482](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ssm-Ph77wdhf)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-76482
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:17:00 JST
- 更新日: 2026-10-08 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco License On-Prem (旧 SSM On-Prem) における不適切な入力検証（CWE-347）の脆弱性。
- 影響: 検証不備を突かれてセキュリティ制限の迂回や不正処理が行われる可能性があります。
- 推奨対応: シスコのアドバイザリを確認し、修正済みソフトウェアへアップデートしてください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ssm-Ph77wdhf

### [CVE-2026-76483](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ssm-Ph77wdhf)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-76483
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:17:00 JST
- 更新日: 2026-10-08 04:17:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco License On-Prem (旧 SSM On-Prem) における認証情報の不十分な保護に関する脆弱性 (CWE-522)。
- 影響: 認証情報が漏洩または不正アクセスされる可能性がある。
- 推奨対応: 修正済みのソフトウェアバージョンへ更新する。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ssm-Ph77wdhf

### [CVE-2026-76498](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-apic-UOXWtfh)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76498
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:17:01 JST
- 更新日: 2026-10-08 04:17:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Application Policy Infrastructure Controller (APIC) における不適切なアクセス制御（CWE-284）の脆弱性。
- 影響: 権限のないユーザーにより不正なリソースアクセスや設定操作が行われる可能性があります。
- 推奨対応: シスコから提供されている修正済みソフトウェアを適用してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-apic-UOXWtfh

### [CVE-2026-76499](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-apic-UOXWtfh)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76499
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:17:01 JST
- 更新日: 2026-10-08 03:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco Application Policy Infrastructure Controller (APIC) における入力データの不適切な無害化の脆弱性 (CWE-707)。
- 影響: 不適切なデータ処理に起因するセキュリティ上の影響が生じる可能性があるが、詳細は不明。
- 推奨対応: Ciscoが提供する修正済みソフトウェアへのアップデートを実施する。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-apic-UOXWtfh

### [CVE-2026-76485](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ngoam-rce-LWKQ4BU)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76485
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-08 02:17:01 JST
- 更新日: 2026-10-08 02:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco NX-OS の VXLAN OAM (NGOAM) 機能におけるIPトラフィック入力検証不足の脆弱性。
- 影響: 未認証の遠隔攻撃者が細工したパケットを送信することで、root権限での任意コード実行やプロセスクラッシュによるDoS（再起動）を引き起こす可能性がある。
- 推奨対応: NGOAM機能の利用状況を確認し、修正済みソフトウェアを適用する。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ngoam-rce-LWKQ4BU

### [CVE-2026-76486](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ngoam-rce-LWKQ4BU)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76486
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-08 02:17:01 JST
- 更新日: 2026-10-08 02:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco NX-OS の VXLAN OAM (NGOAM) 機能におけるIPトラフィック入力検証不足の脆弱性。
- 影響: 未認証の遠隔攻撃者により、root権限での任意コード実行や機器の再起動（DoS）が引き起こされる可能性がある。
- 推奨対応: Ciscoが提供する修正版ソフトウェアへアップデートする。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ngoam-rce-LWKQ4BU

### [CVE-2026-76501](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ngoam-rce-LWKQ4BU)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-76501
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-08 02:17:02 JST
- 更新日: 2026-10-08 02:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco NX-OS の SRv6 OAM (NGOAM) 機能におけるIPトラフィック入力検証不足の脆弱性。
- 影響: 未認証の遠隔攻撃者が特製パケットを送信することで、root権限での任意コード実行や機器の再起動（DoS）を引き起こす可能性がある。
- 推奨対応: 修正済みソフトウェアへのアップデートを実施する。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ngoam-rce-LWKQ4BU

### [CVE-2026-76467](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-76467
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:16:59 JST
- 更新日: 2026-10-08 02:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco ネットワーク製品におけるリソースライフサイクルの不適切な制御に関する脆弱性 (CWE-664)。
- 影響: リソース管理の不備に伴う影響が発生する可能性があるが、悪用の詳細は不明。
- 推奨対応: 修正済みソフトウェアの適用を行う。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH

### [CVE-2026-95595](https://patchstack.com/database/wordpress/plugin/disable-remove-google-fonts/vulnerability/wordpress-disable-and-remove-google-fonts-gdpr-dsgvo-friendly-plugin-2-0-2-cross-site-scripting-xss-vulnerability?_s_id=cve)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-95595
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:17:03 JST
- 更新日: 2026-10-08 05:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPressプラグイン「Disable and Remove Google Fonts」における反射型クロスサイトスクリプティング (XSS) の脆弱性。
- 影響: 攻撃者によってユーザーのブラウザ上で任意のスクリプトを実行される可能性がある。
- 推奨対応: プラグインを最新バージョン（2.0.2より後の修正版）へ更新する。

#### References
- https://patchstack.com/database/wordpress/plugin/disable-remove-google-fonts/vulnerability/wordpress-disable-and-remove-google-fonts-gdpr-dsgvo-friendly-plugin-2-0-2-cross-site-scripting-xss-vulnerability?_s_id=cve

### [CVE-2026-107212](https://github.com/qax-os/excelize/commit/01a9ff32fb3c1f873cf01205e1b8a3285b0e1d23)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-107212
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-08 03:17:18 JST
- 更新日: 2026-10-08 03:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Go言語用ライブラリ Excelize における行数制限チェック不備によるリソース消費の脆弱性。
- 影響: 細工されたExcelファイルを読み込むことで意図しないループが発生し、CPUコアを占有されてDoS状態に陥る可能性がある。
- 推奨対応: レビュー時点で修正版未公開のため、信頼できないファイルの処理を控えるか、修正版公開後に速やかに更新する。

#### References
- https://github.com/qax-os/excelize/commit/01a9ff32fb3c1f873cf01205e1b8a3285b0e1d23
- https://github.com/qax-os/excelize/pull/2438
- https://github.com/qax-os/excelize/security/advisories/GHSA-jw42-f3rr-4cc3

### [CVE-2026-107215](https://github.com/qax-os/excelize/commit/5f636f9dcde55911f14290060b017f0cc88cd694)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-107215
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-08 03:17:19 JST
- 更新日: 2026-10-08 03:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Go言語用ライブラリ Excelize におけるOLE複合ファイルの処理時における過剰なメモリ割り当ての脆弱性。
- 影響: 不正なストリームサイズを持つファイルを解析した際、アプリのパニックやメモリ枯渇（DoS）が発生する可能性がある。
- 推奨対応: レビュー時点で修正版未公開のため、不審なファイルの入力を制限し、修正版がリリースされ次第アップデートする。

#### References
- https://github.com/qax-os/excelize/commit/5f636f9dcde55911f14290060b017f0cc88cd694
- https://github.com/qax-os/excelize/pull/2396
- https://github.com/qax-os/excelize/security/advisories/GHSA-x2q3-8cjh-766f

### [CVE-2026-76453](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-76453
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:16:57 JST
- 更新日: 2026-10-08 02:16:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco NX-OSにおける入力データの不適切な無効化（CWE-707）の脆弱性。
- 影響: 悪意ある入力処理により、システムの正常な動作が阻害されたり不正な挙動が発生したりする可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェアバージョンへのアップデートを検討してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR

### [CVE-2026-76456](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-76456
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:16:57 JST
- 更新日: 2026-10-08 04:17:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco NX-OSにおけるコマンドで使用される特殊エレメントの不適切な入力確認（CWE-20）の脆弱性。
- 影響: 不正なコマンド入力により、意図しない操作やシステムへの影響が発生する可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェアバージョンへのアップデートを検討してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR

### [CVE-2026-76457](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-76457
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:16:58 JST
- 更新日: 2026-10-08 03:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco NX-OSにおける境界外読み取り（CWE-125）の脆弱性。
- 影響: システムメモリからの不適切な情報漏洩や、サービス拒否（DoS）が発生する可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェアバージョンへのアップデートを検討してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR

### [CVE-2026-76458](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-76458
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:16:58 JST
- 更新日: 2026-10-08 02:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco NX-OSにおける例外状況の不適切な処理（CWE-703）の脆弱性。
- 影響: エラーハンドリングの不備により、システムの異常終了やサービス拒否（DoS）が発生する可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェアバージョンへのアップデートを検討してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR

### [CVE-2026-76459](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-76459
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:16:58 JST
- 更新日: 2026-10-08 02:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco NX-OSにおける境界外書き込み（CWE-787）の脆弱性。
- 影響: メモリ破損が引き起こされ、サービス拒否（DoS）状態や任意のコード実行に繋がる可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェアバージョンへのアップデートを検討してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR

### [CVE-2026-76463](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-76463
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:16:58 JST
- 更新日: 2026-10-08 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Ciscoネットワーク製品における不適切なアクセス制御（CWE-284）の脆弱性。
- 影響: 本来アクセスが制限されている機能やデータに不正アクセスされる可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェアバージョンへのアップデートを検討してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH

### [CVE-2026-76468](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-76468
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:16:59 JST
- 更新日: 2026-10-08 02:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Ciscoネットワーク製品における不適切な入力確認（CWE-20）の脆弱性。
- 影響: 検証されていない入力データにより、システムの誤作動や不安定な状態が引き起こされる可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェアバージョンへのアップデートを検討してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH

### [CVE-2026-76470](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-76470
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:17:00 JST
- 更新日: 2026-10-08 04:17:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Ciscoネットワーク製品における誤った計算処理（CWE-682）の脆弱性。
- 影響: 数値計算の過誤により、データの不整合やシステムの不具合、検証の迂回が発生する可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェアバージョンへのアップデートを検討してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH

### [CVE-2026-76472](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-76472
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:17:00 JST
- 更新日: 2026-10-08 02:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Ciscoネットワーク製品における特殊エレメントの不適切な無効化（CWE-74）の脆弱性。
- 影響: インジェクション攻撃などにより、意図しない処理やコマンドが実行される可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェアバージョンへのアップデートを検討してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH

### [CVE-2026-76484](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ssm-Ph77wdhf)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-76484
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-08 02:17:01 JST
- 更新日: 2026-10-08 03:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco License On-Prem（旧SSM On-Prem）におけるコードインジェクション保護の不足（CWE-94）の脆弱性。
- 影響: 第三者により任意のコードが実行され、システムが侵害される可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェアバージョンへのアップデートを検討してください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ssm-Ph77wdhf

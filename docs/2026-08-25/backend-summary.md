# Backend CVE Summary (2026-08-25)

## Overview

- 取得日時: 2026-08-25 07:38:59 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 25
- Critical: 4
- High: 20
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-55468](https://github.com/wagtail/wagtail/commit/5608cfb714a130412f862beab53c78de02b79975)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-55468
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-08-25 06:17:41 JST
- 更新日: 2026-08-25 06:17:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WagtailのPages admin APIにおいて、適切なアクセス制御が行われていない不具合が存在します。
- 影響: Wagtail管理権限を持つユーザーが、本来制限されているドラフトや公開ページのコンテンツを取得できる可能性があります。
- 推奨対応: Wagtailを修正済みバージョン（7.0.9、7.3.4、7.4.3、8.0rc2以降）へアップデートしてください。

#### References
- https://github.com/wagtail/wagtail/commit/5608cfb714a130412f862beab53c78de02b79975
- https://github.com/wagtail/wagtail/commit/aef935530d5289406ca325b42747af15f3b28ac4
- https://github.com/wagtail/wagtail/commit/d99d2bec2b0aca46d88014416432c717240cd559
- https://github.com/wagtail/wagtail/commit/e2fa629b7a51ec29d59e45eead930feee0d3c4b3
- https://github.com/wagtail/wagtail/security/advisories/GHSA-3vrh-m9w7-v94f

### [CVE-2026-71914](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-71914
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:03 JST
- 更新日: 2026-08-25 05:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorAPの `dray_apm` コンポーネントにおいて、UDPメッセージの検証不足によるコマンドインジェクションの脆弱性が存在します。
- 影響: 遠隔の攻撃者が作成したメッセージを送信することで、root権限で任意コマンドを実行する可能性があります。
- 推奨対応: ベンダーの提供する最新の修正ファームウェアへアップデートしてください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorap-multiple-models-pre-authentication-os-command-injection-via-dray-apm

### [CVE-2026-71921](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-71921
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:07 JST
- 更新日: 2026-08-25 03:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchの `setget.cgi` において、`pass` フィールドのフィルタリング不足による事前認証コマンドインジェクションの脆弱性が存在します。
- 影響: 遠隔の未認証の攻撃者が細工した入力を送信することで、root権限で任意コマンドを実行する可能性があります。
- 推奨対応: ベンダーの提供する最新の修正ファームウェアへアップデートしてください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-pre-authentication-os-command-injection-via-setget-cgi

### [CVE-2026-71933](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-71933
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:18 JST
- 更新日: 2026-08-25 03:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchの複数のsyslog機能において、認可チェックが不足している脆弱性が存在します。
- 影響: 遠隔の攻撃者が設定変更、サービスの再起動、設定保存、ログ消去などの不正な操作を行う可能性があります。
- 推奨対応: ベンダーの提供する最新の修正ファームウェアへアップデートしてください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-missing-authorization-in-syslog-functions

### [CVE-2026-76835](https://github.com/oauth2-proxy/oauth2-proxy)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-76835
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:21 JST
- 更新日: 2026-08-25 05:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OAuth2 Proxyにおいて、デフォルトのリバースプロキシ構成時に信頼されたプロキシ設定が広範（全IP）になり、`X-Forwarded-Uri` ヘッダーを無条件に信頼してしまう脆弱性が存在します。
- 影響: 未認証の攻撃者がヘッダーを偽装することで、保護されたパスへのアクセス制限や認証をバイパスする可能性があります。
- 推奨対応: `trusted_proxy_ip` を適切に設定して信頼するプロキシ範囲を制限するか、対策済みバージョンへアップデートしてください。

#### References
- https://github.com/oauth2-proxy/oauth2-proxy
- https://github.com/oauth2-proxy/oauth2-proxy/blob/v7.15.4/pkg/apis/middleware/scope.go
- https://github.com/oauth2-proxy/oauth2-proxy/issues/3506
- https://github.com/oauth2-proxy/oauth2-proxy/security/advisories/GHSA-7x63-xv5r-3p2x
- https://www.vulncheck.com/advisories/oauth2-proxy-through-authentication-bypass-via-x-forwarded-uri-under-the-default-trusted-proxy-set

### [CVE-2026-71904](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71904
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:01 JST
- 更新日: 2026-08-25 05:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorAPのtr069TestInform関数において、event_codeフィールドに対する不十分なフィルタリングに起因するOSコマンドインジェクションの脆弱性が存在します。
- 影響: Web管理画面の有効な管理者権限を持つ攻撃者により、root権限で任意のコマンドを実行される可能性があります。
- 推奨対応: Web管理インタフェースのアクセス制限、管理者アカウントの認証情報の管理強化、および修正ファームウェアの適用を行ってください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorap-multiple-models-os-command-injection-via-tr069testinform

### [CVE-2026-71905](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71905
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:01 JST
- 更新日: 2026-08-25 04:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorAPのExportSettings関数において、backupkey、backuptype、realtimeの各フィールドに対する不十分なフィルタリングに起因するOSコマンドインジェクションの脆弱性が存在します。
- 影響: Web管理画面の有効な管理者権限を持つ攻撃者により、root権限で任意のコマンドを実行される可能性があります。
- 推奨対応: 管理インタフェースへのアクセスを信頼できるネットワークのみに限定し、最新のファームウェアへ更新してください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorap-multiple-models-os-command-injection-via-exportsettings

### [CVE-2026-71906](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71906
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:02 JST
- 更新日: 2026-08-25 03:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorAPのsetLan関数において、lanIpおよびlanNetmaskフィールドに対する不十分な入力検証に起因するOSコマンドインジェクションの脆弱性が存在します。
- 影響: Web管理画面の有効な管理者権限を持つ攻撃者により、root権限で任意のコマンドを実行される可能性があります。
- 推奨対応: 管理者資格情報の保護を徹底し、ベンダーから提供される修正版ファームウェアを適用してください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorap-multiple-models-os-command-injection-via-setlan

### [CVE-2026-71907](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71907
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:02 JST
- 更新日: 2026-08-25 04:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorAPのsetcamset関数において、selectSlavesフィールドに対する不十分なフィルタリングに起因するOSコマンドインジェクションの脆弱性が存在します。
- 影響: Web管理画面の有効な管理者権限を持つ攻撃者により、root権限で任意のコマンドを実行される可能性があります。
- 推奨対応: 管理インタフェースの分離と強固な認証の設定を行い、最新ファームウェアへのアップデートを実施してください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorap-multiple-models-os-command-injection-via-setcamset

### [CVE-2026-71908](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71908
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:02 JST
- 更新日: 2026-08-25 03:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorAPのmesh_start_speed_test関数において、meshdevice_indexおよびmeshdevice_ipフィールドに対する不十分な無害化処理に起因するOSコマンドインジェクションの脆弱性が存在します。
- 影響: Web管理画面の有効な管理者権限を持つ攻撃者により、root権限で任意のコマンドを実行される可能性があります。
- 推奨対応: Web管理機能への不要な外部アクセスを遮断し、公式のセキュリティパッチまたは修正版ファームウェアを適用してください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorap-multiple-models-os-command-injection-via-mesh-start-speed-test

### [CVE-2026-71909](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71909
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:02 JST
- 更新日: 2026-08-25 05:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorAPのInquierTime関数において、timeフィールドに対する不十分なフィルタリングに起因するOSコマンドインジェクションの脆弱性が存在します。
- 影響: Web管理画面の有効な管理者権限を持つ攻撃者により、root権限で任意のコマンドを実行される可能性があります。
- 推奨対応: 管理者アカウントの管理徹底および修正されたファームウェアへの速やかなアップデートを推奨します。

#### References
- https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorap-multiple-models-os-command-injection-via-inquiertime

### [CVE-2026-71910](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71910
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:02 JST
- 更新日: 2026-08-25 04:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorAPのapautotest関数において、CMD0、CMD3、CMD6の各フィールドに対する不十分な検証に起因するOSコマンドインジェクションの脆弱性が存在します。
- 影響: Web管理画面の有効な管理者権限を持つ攻撃者により、root権限で任意のコマンドを実行される可能性があります。
- 推奨対応: Web管理機能のアクセス権限を見直し、ベンダー推奨の修正版ファームウェアを適用してください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorap-multiple-models-os-command-injection-via-apautotest

### [CVE-2026-71911](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71911
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:02 JST
- 更新日: 2026-08-25 03:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorAPのsetLan関数において、lanVlanId0、lanIp、lanNetmaskのフィールドを伴うメモリコピー処理時の長さチェック不足によるバッファオーバーフローの脆弱性が存在します。
- 影響: Web管理画面の有効な管理者権限を持つ攻撃者により、サービス拒否（DoS）状態を引き起こされたり、任意のコマンドを実行される可能性があります。
- 推奨対応: Web管理画面へのアクセスを信頼できる送信元に制限し、最新のファームウェアへ更新してください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorap-multiple-models-buffer-overflow-via-setlan

### [CVE-2026-71912](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71912
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:03 JST
- 更新日: 2026-08-25 04:16:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorAPのapautotest関数において、CMD6フィールドのメモリコピー処理時の長さチェック不足によるバッファオーバーフローの脆弱性が存在します。
- 影響: Web管理画面の有効な管理者権限を持つ攻撃者により、サービス拒否（DoS）状態を引き起こされたり、任意のコマンドを実行される可能性があります。
- 推奨対応: 管理権限の適切な管理とアクセス制御を行い、ベンダーから提供される修正プログラムを適用してください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorap-multiple-models-buffer-overflow-via-apautotest

### [CVE-2026-71913](https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71913
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:03 JST
- 更新日: 2026-08-25 03:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorAPのupload_settings.cgiインターフェースにおけるrestorekeyフィールドの不十分なフィルタリングに起因するコマンドインジェクションの脆弱性。
- 影響: 有効なWeb管理者の認証情報を持つ攻撃者により、ルート権限で任意のコマンドを実行される可能性がある。
- 推奨対応: 最新の修正パッチの適用、Web管理画面へのアクセス制限、および管理者アカウントの厳重な管理。

#### References
- https://www.draytek.com/about/security-advisory/multiple-remote-code-execution-and-buffer-overflow-vulnerabilities-in-vigorap-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorap-multiple-models-os-command-injection-via-upload-settings-cgi

### [CVE-2026-71915](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71915
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:03 JST
- 更新日: 2026-08-25 04:16:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchのjsonstatus関数におけるusescript、usefile、optionフィールドの不十分なフィルタリングに起因するコマンドインジェクションの脆弱性。
- 影響: 有効なWeb管理者の認証情報を持つ攻撃者により、ルート権限で任意のコマンドを実行される可能性がある。
- 推奨対応: 修正ファームウェアへのアップデート、管理インターフェースへのアクセス制限の実施。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-os-command-injection-via-jsonstatus

### [CVE-2026-71916](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71916
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:03 JST
- 更新日: 2026-08-25 03:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchのcommandTable関数におけるparameterフィールド内の危険な文字（バックティック、改行、シングルクォート等）のフィルタリング不足に起因するコマンドインジェクションの脆弱性。
- 影響: 有効なWeb管理者の認証情報を持つ攻撃者により、ルート権限で任意のコマンドを実行される可能性がある。
- 推奨対応: ベンダーが提供する最新ファームウェアの適用、および管理画面への接続元IPアドレス制限。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-os-command-injection-via-commandtable

### [CVE-2026-71917](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71917
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:06 JST
- 更新日: 2026-08-25 04:16:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchのpingtrace関数におけるhostフィールドの検証不足に起因するコマンドインジェクションの脆弱性。
- 影響: 有効なWeb管理者の認証情報を持つ攻撃者により、ルート権限で任意のコマンドを実行される可能性がある。
- 推奨対応: アップデートによる修正パッチの適用、管理用認証情報の強力な設定と管理。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-os-command-injection-via-pingtrace

### [CVE-2026-71918](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71918
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:06 JST
- 更新日: 2026-08-25 03:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchのwebBackupAction関数におけるoption、key、pw_encode、pathN、valueNフィールドの不十分なフィルタリングに起因するコマンドインジェクションの脆弱性。
- 影響: 有効なWeb管理者の認証情報を持つ攻撃者により、ルート権限で任意のコマンドを実行される可能性がある。
- 推奨対応: 修正済みファームウェアの適用と、管理インターフェースの不要な外部公開の停止。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-os-command-injection-via-webbackupaction

### [CVE-2026-71919](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71919
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:06 JST
- 更新日: 2026-08-25 05:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchのsysreboot関数におけるconfig、act、pathN、valueNフィールドの不十分なフィルタリングに起因するコマンドインジェクションの脆弱性。
- 影響: 有効なWeb管理者の認証情報を持つ攻撃者により、ルート権限で任意のコマンドを実行される可能性がある。
- 推奨対応: 最新バージョンへのファームウェア更新、管理権限の適切な制限。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-os-command-injection-via-sysreboot

### [CVE-2026-71922](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-71922
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:07 JST
- 更新日: 2026-08-25 04:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchのsetget.cgiインタフェースにおいて、passフィールド不在時の検証不備による認証前のヌルポインタ参照の脆弱性が存在します。
- 影響: 遠隔の第三者が細工したリクエストを送信することでサービスを停止させ、拒否攻撃（DoS）を引き起こす可能性があります。
- 推奨対応: ベンダーが提供する最新ファームウェアへのアップデートおよび対象インタフェースへのアクセス制限を検討してください。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-pre-authentication-null-pointer-dereference-via-setget-cgi

### [CVE-2026-71923](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71923
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:07 JST
- 更新日: 2026-08-25 03:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchのauth_set関数におけるusernameおよびpasswordフィールドの不十分なフィルタリングに起因するコマンドインジェクションの脆弱性。
- 影響: 有効なWeb管理者の認証情報を持つ攻撃者により、ルート権限で任意のコマンドを実行される可能性がある。
- 推奨対応: ベンダー提供のアップデート適用、Web管理画面への信頼できるネットワークからの接続制限。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-os-command-injection-via-auth-set

### [CVE-2026-71924](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71924
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:07 JST
- 更新日: 2026-08-25 05:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchのgetVid関数におけるusernameおよびpasswordフィールドの不十分なフィルタリングに起因するコマンドインジェクションの脆弱性。
- 影響: 有効なWeb管理者の認証情報を持つ攻撃者により、ルート権限で任意のコマンドを実行される可能性がある。
- 推奨対応: 最新の修正パッチの適用、管理者資格情報の安全な管理。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-os-command-injection-via-getvid

### [CVE-2026-71925](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71925
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:07 JST
- 更新日: 2026-08-25 04:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchのgetDetail関数におけるusernameおよびpasswordフィールドの不十分なフィルタリングに起因するコマンドインジェクションの脆弱性。
- 影響: 有効なWeb管理者の認証情報を持つ攻撃者により、ルート権限で任意のコマンドを実行される可能性がある。
- 推奨対応: 最新ファームウェアの適用、および管理インターフェースのアクセス制御強化。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-os-command-injection-via-getdetail

### [CVE-2026-71926](https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-71926
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-25 03:17:07 JST
- 更新日: 2026-08-25 03:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DrayTek VigorSwitchのsetDevice関数におけるusername、password、locationフィールドのサニタイズ不足に起因するコマンドインジェクションの脆弱性。
- 影響: 有効なWeb管理者の認証情報を持つ攻撃者により、ルート権限で任意のコマンドを実行される可能性がある。
- 推奨対応: 修正済みファームウェアへの更新、および管理用アカウントのパスワード管理徹底。

#### References
- https://www.draytek.com/about/security-advisory/multiple-vulnerabilities-in-vigorswitch-series-august-2026/
- https://www.vulncheck.com/advisories/draytek-vigorswitch-multiple-models-os-command-injection-via-setdevice

# Backend CVE Summary (2026-09-03)

## Overview

- 取得日時: 2026-09-03 09:08:08 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 16
- Critical: 2
- High: 12
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-53635](https://github.com/openedx/openedx-platform/commit/59bb6d669e4fdc24d96afb809e12119372d9e257)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-53635
- 関連キーワード: django, go, gin
- 影響製品: -
- 公開日: 2026-09-03 02:17:45 JST
- 更新日: 2026-09-03 04:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open edX Platformの orphaned エンドポイント（set_course_mode_price）においてコースレベルの権限検証が欠如している脆弱性。
- 影響: コース権限を持たない任意のログインユーザーが、全コースの価格や通貨設定を上書き変更できる可能性があります。
- 推奨対応: 修正コミット（59bb6d6）以降のコードを適用してください。

#### References
- https://github.com/openedx/openedx-platform/commit/59bb6d669e4fdc24d96afb809e12119372d9e257
- https://github.com/openedx/openedx-platform/commit/f25bbc4d52bd827c8f04c73de427e2e16a144c73
- https://github.com/openedx/openedx-platform/commit/fd93ef5f9940f4ad6f50cf7faecad8d9cf2d3336
- https://github.com/openedx/openedx-platform/security/advisories/GHSA-rqq6-w4pv-7pjv
- https://github.com/openedx/openedx-platform/security/advisories/GHSA-rqq6-w4pv-7pjv

### [CVE-2026-53636](https://github.com/openedx/openedx-platform/commit/0a92cf25de8844bf840ffd5d18dcfd940031a2ba)

> **Backend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-53636
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-09-03 02:17:45 JST
- 更新日: 2026-09-03 04:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open edX PlatformのLTI Provider機能において、OAuthナンスおよびタイムスタンプの検証が行われない脆弱性。
- 影響: 攻撃者がキャプチャした有効なLTI起動リクエストを無制限に再送（リプレイ攻撃）できる可能性があります。
- 推奨対応: 修正コミット（3a5ac85）以降のコードを適用してください。

#### References
- https://github.com/openedx/openedx-platform/commit/0a92cf25de8844bf840ffd5d18dcfd940031a2ba
- https://github.com/openedx/openedx-platform/commit/3a5ac856c79557c5c74d8b3e6578f289d7cceecd
- https://github.com/openedx/openedx-platform/commit/50af17b05d82a8c7e8e690cc2783a8a0ba330bc3
- https://github.com/openedx/openedx-platform/security/advisories/GHSA-6gm5-c49g-p3h9
- https://github.com/openedx/openedx-platform/security/advisories/GHSA-6gm5-c49g-p3h9

### [CVE-2026-20274](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-20274
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-03 02:17:32 JST
- 更新日: 2026-09-03 04:23:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco IOS XR Softwareにおける不適切なリソース制御（CWE-664）に関する脆弱性。
- 影響: リソース管理の不備により、サービスの停止や不具合が発生する可能性があります。
- 推奨対応: Ciscoが提供するセキュリティ強化済み（Hardening）ソフトウェアへアップデートしてください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM

### [CVE-2026-20279](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-20279
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-03 02:17:33 JST
- 更新日: 2026-09-03 04:23:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco IOS XR Softwareにおける不適切なアクセス制御（CWE-284）に関する脆弱性。
- 影響: 本来制限されるべき機能や情報に不正アクセスされる可能性があります。
- 推奨対応: Ciscoが提供するセキュリティ強化済み（Hardening）ソフトウェアへアップデートしてください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM

### [CVE-2026-20275](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-20275
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-03 02:17:32 JST
- 更新日: 2026-09-03 04:23:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco IOS XR Softwareにおける不適切な計算処理（CWE-682）に関する脆弱性。
- 影響: 内部計算の誤りにより、システムの予期しない挙動や不具合を引き起こす可能性があります。
- 推奨対応: Ciscoが提供するセキュリティ強化済み（Hardening）ソフトウェアへアップデートしてください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM

### [CVE-2026-20276](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-20276
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-03 02:17:32 JST
- 更新日: 2026-09-03 04:23:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco IOS XR Softwareにおける不十分な制御フロー管理（CWE-691）に関する脆弱性。
- 影響: 詳細な影響は公表されていませんが、意図しない処理の実行やシステムの不整合が生じる可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェア（ハーデニングリリース）への更新を行ってください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM

### [CVE-2026-20277](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-20277
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-03 02:17:33 JST
- 更新日: 2026-09-03 03:19:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco IOS XR Softwareにおける保護メカニズムの失敗（CWE-693）に関する脆弱性。
- 影響: 詳細な影響は公表されていませんが、セキュリティ制限の迂回や保護機能の無効化が起こる可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェア（ハーデニングリリース）への更新を行ってください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM

### [CVE-2026-20278](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-20278
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-03 02:17:33 JST
- 更新日: 2026-09-03 04:23:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco IOS XR Softwareにおける入力データの不適切な無害化処理（CWE-707）に関する脆弱性。
- 影響: 入力構造の解析エラー等により、システムの不安定化や不正な動作が引き起こされる可能性があります。
- 推奨対応: Ciscoが提供するセキュリティ強化済み（Hardening）ソフトウェアへアップデートしてください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM

### [CVE-2026-20280](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-20280
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-03 02:17:33 JST
- 更新日: 2026-09-03 04:23:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cisco IOS XR Softwareにおける例外条件の不適切な検証・取り扱い（CWE-703）に関する脆弱性。
- 影響: 詳細な影響は公表されていませんが、システムの安定性低下や予期せぬ動作が発生する可能性があります。
- 推奨対応: Ciscoから提供される修正済みソフトウェア（ハーデニングリリース）への更新を行ってください。

#### References
- https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxr-qg64NcM

### [CVE-2026-52833](https://github.com/nuclio/nuclio/commit/4c78040c759068e927f3ed7c6507543c15d4ae56)

> **Backend** / **HIGH** / CVSS: **8.0** / KEV: **no**

- タイトル: CVE-2026-52833
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-03 02:17:45 JST
- 更新日: 2026-09-03 04:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NuclioのJavaランタイムにおけるbuild.gradleファイル生成時のエスケープ処理不足によるコード挿入の脆弱性。
- 影響: Gradleの設定フェーズ中に任意のGroovyステートメントが追加実行され、任意コード実行に至る可能性があります。
- 推奨対応: Nuclioをバージョン 1.16.5 以降へアップデートしてください。

#### References
- https://github.com/nuclio/nuclio/commit/4c78040c759068e927f3ed7c6507543c15d4ae56
- https://github.com/nuclio/nuclio/pull/4149
- https://github.com/nuclio/nuclio/releases/tag/1.16.5
- https://github.com/nuclio/nuclio/security/advisories/GHSA-3v79-m2cg-89ww
- https://github.com/nuclio/nuclio/security/advisories/GHSA-3v79-m2cg-89ww

### [CVE-2026-84857](https://github.com/outlookgp/CVE/tree/main/AIChat_Serve_Request_Body_DoS_Report)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-84857
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-03 05:17:42 JST
- 更新日: 2026-09-03 05:17:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: sigoden aichatのAPIエンドポイント（src/serve.rs）における制御不能なメモリ割り当ての脆弱性。
- 影響: リモートの攻撃者によってメモリが過剰に消費され、サービス拒否（DoS）状態に陥る可能性があります。
- 推奨対応: 公式な修正情報やアップデートを確認し、必要に応じてAPIエンドポイントへのアクセス制限を実施してください。

#### References
- https://github.com/outlookgp/CVE/tree/main/AIChat_Serve_Request_Body_DoS_Report
- https://vuldb.com/cve/CVE-2026-84857
- https://vuldb.com/submit/886265
- https://vuldb.com/vuln/398132
- https://vuldb.com/vuln/398132/cti

### [CVE-2026-84809](https://github.com/Tencent/AI-Infra-Guard)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-84809
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-03 02:18:05 JST
- 更新日: 2026-09-03 02:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tencent AI-Infra-Guardのskill-scanコンポーネントがコンパイル済みPythonバイトコード（__pycache__等）をスキャン対象外とする問題。
- 影響: 悪意のあるバイトコードがセキュリティ検査をすり抜け、スキルのインストール・インポート時に任意のコードが実行される可能性があります。
- 推奨対応: 修正されたバージョンへの更新、またはスキャン対象にバイトコードが含まれるよう運用の見直しを行ってください。

#### References
- https://github.com/Tencent/AI-Infra-Guard
- https://github.com/Tencent/AI-Infra-Guard/blob/v4.6.0/skill-scan/skill_scan/tools/dir/dir_actions.py
- https://github.com/Tencent/AI-Infra-Guard/blob/v4.6.0/skill-scan/skill_scan/utils/pre_scan.py
- https://github.com/Tencent/AI-Infra-Guard/commit/7e0f749e3c023e5c6ab7b32fe97b3f6f2e8aeb04
- https://github.com/Tencent/AI-Infra-Guard/issues/531

### [CVE-2026-84810](https://github.com/claude-world/claude-skill-antivirus)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-84810
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-03 02:18:05 JST
- 更新日: 2026-09-03 04:18:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: claude-skill-antivirusがローカルスキルの検査時にSKILL.mdのみを読み込み、実行ファイルやスクリプトを解析しない問題。
- 影響: 悪意のあるコードが含まれるスキルが「安全」と誤判定され、実行される可能性があります。
- 推奨対応: ツールの修正版の適用、またはスキル導入前に手動でのコードレビューを実施してください。

#### References
- https://github.com/claude-world/claude-skill-antivirus
- https://github.com/claude-world/claude-skill-antivirus/blob/v2.1.3/src/scanner/index.js
- https://github.com/claude-world/claude-skill-antivirus/blob/v2.1.3/src/utils/downloader.js
- https://github.com/claude-world/claude-skill-antivirus/issues/33
- https://www.vulncheck.com/advisories/claude-skill-antivirus-analysis-bypass-via-manifest-only-local-directory-scan

### [CVE-2026-84811](https://github.com/agentverus/agentverus-scanner)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-84811
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-03 02:18:05 JST
- 更新日: 2026-09-03 02:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: agentverus-scannerが付属コード内のコンパイル済みPythonバイトコード解析を行わない問題。
- 影響: スキャン結果が「認証済み」と表示されても、インポート時に悪意のあるバイトコードが実行される可能性があります。
- 推奨対応: 修正版スキャナーへのアップデート、またはバイトコードの混入を警戒した事前チェックを行ってください。

#### References
- https://github.com/agentverus/agentverus-scanner
- https://github.com/agentverus/agentverus-scanner/blob/v0.8.1/src/scanner/analyzers/semantic.ts
- https://github.com/agentverus/agentverus-scanner/blob/v0.8.1/src/scanner/companion-code.ts
- https://github.com/agentverus/agentverus-scanner/issues/27
- https://www.vulncheck.com/advisories/agentverus-scanner-companion-code-analysis-bypass-via-excluded-python-bytecode

### [CVE-2026-84381](https://github.com/pydantic/httpx2/commit/fb008dd700b761d955210d9692475c3e2f379453)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-84381
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-09-03 04:18:08 JST
- 更新日: 2026-09-03 04:18:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HTTPX2（httpcore2）において、SOCKS5プロキシ経由のwss接続時にTLS暗号化が開始されない脆弱性。
- 影響: WebSocket通信（ハンドシェイク、認証情報、Cookie等）が平文で送信され、通信の盗聴や改ざんが行われる可能性があります。
- 推奨対応: HTTPX2およびhttpcore2をバージョン 2.10.0 以降へアップデートしてください。

#### References
- https://github.com/pydantic/httpx2/commit/fb008dd700b761d955210d9692475c3e2f379453
- https://github.com/pydantic/httpx2/pull/1104
- https://github.com/pydantic/httpx2/releases/tag/v2.10.0
- https://github.com/pydantic/httpx2/security/advisories/GHSA-7mj9-2mp8-4m2p

### [CVE-2026-84452](https://github.com/microsoft/winml-cli/commit/f4073e0ef4700a25b623487e7e45c421ca0b9993)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-84452
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-09-03 05:17:41 JST
- 更新日: 2026-09-03 05:17:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Windows ML CLIのlocalhost APIにおける未認証アクセスおよびワイルドカードCORS設定によるパラメータ検証不足の脆弱性。
- 影響: 悪意のあるWebサイトを経由してリモートリポジトリからコードが読み込まれ、サーバーユーザー権限で任意のコードが実行される可能性があります。
- 推奨対応: Windows ML CLIをバージョン 0.4.0 以降へアップデートしてください。

#### References
- https://github.com/microsoft/winml-cli/commit/f4073e0ef4700a25b623487e7e45c421ca0b9993
- https://github.com/microsoft/winml-cli/pull/1321
- https://github.com/microsoft/winml-cli/security/advisories/GHSA-96p9-rh4f-92cf

# Backend CVE Summary (2026-10-25)

## Overview

- 取得日時: 2026-10-25 09:16:39 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 4
- Critical: 1
- High: 2
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-115995](https://unitree-firmware.oss-cn-hangzhou.aliyuncs.com/firmware/release/package_1.1.11.5_GO2_Edu_Max_Pro_X_1761128358872.upk)

> **Backend** / **HIGH** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-115995
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-25 08:16:58 JST
- 更新日: 2026-10-25 08:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Unitree Robotics Unitree Go2 の chat_go コンポーネント（gpt_thread.py の set_volume 関数）における OS コマンドインジェクションの脆弱性。
- 影響: リモートの攻撃者が引数を操作することにより、対象機器上で任意の OS コマンドを実行する可能性があります。
- 推奨対応: Unitree Go2 をバージョン 1.1.11.5 以降へアップデートしてください。

#### References
- https://unitree-firmware.oss-cn-hangzhou.aliyuncs.com/firmware/release/package_1.1.11.5_GO2_Edu_Max_Pro_X_1761128358872.upk
- https://vuldb.com/cve/CVE-2026-115995
- https://vuldb.com/submit/990502
- https://vuldb.com/vuln/426093
- https://vuldb.com/vuln/426093/cti

### [CVE-2026-115973](https://vuldb.com/cve/CVE-2026-115973)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-115973
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-25 04:17:04 JST
- 更新日: 2026-10-25 04:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Faveo Helpdesk 2.0.3 の ForgotPasswordController.php における弱いパスワード回復処理の脆弱性。
- 影響: リモートの攻撃者によってパスワードリセット機能を悪用され、アカウントを不正に回復・制御される可能性があります。
- 推奨対応: 開発元が提供する最新の修正情報を確認し、アップデートを適用してください。

#### References
- https://vuldb.com/cve/CVE-2026-115973
- https://vuldb.com/submit/986184
- https://vuldb.com/vuln/426054
- https://vuldb.com/vuln/426054/cti

### [CVE-2026-115996](https://vuldb.com/cve/CVE-2026-115996)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-115996
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-25 08:16:58 JST
- 更新日: 2026-10-25 08:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Unitree Robotics Unitree Go2 の chat_go コンポーネント（websocket.py の WebSocketClient.connect 関数）における TLS サーバー証明書の検証無効化の脆弱性。
- 影響: 中間者攻撃（MitM）などの攻撃により、通信内容の盗聴や改ざんが行われる可能性があります（攻撃の難易度は高と評価されています）。
- 推奨対応: 開発元が提供する修正済みバージョンへの更新を行ってください。

#### References
- https://vuldb.com/cve/CVE-2026-115996
- https://vuldb.com/submit/990504
- https://vuldb.com/vuln/426094
- https://vuldb.com/vuln/426094/cti

### [CVE-2026-115557](http://www.openwall.com/lists/oss-security/2026/10/20/29)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-115557
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-25 00:17:33 JST
- 更新日: 2026-10-25 03:16:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Python の ssl モジュールにおいて、既知の侵害された証明書を拒否するブラックリストが追加されたことによるセキュリティ改善。
- 影響: SSLContext の設定に関わらず侵害された証明書が自動的に拒否され、該当証明書を用いた通信が拒否される可能性があります。
- 推奨対応: 最新の Python リリースへの更新を実施し、証明書検証動作の影響を確認してください。

#### References
- http://www.openwall.com/lists/oss-security/2026/10/20/29
- https://emudhra.we-have-a-problem.com/
- https://github.com/python/cpython/issues/160040
- https://github.com/python/cpython/pull/160042
- https://mail.python.org/archives/list/security-announce@python.org/thread/FNAJMZV6XQYLVPABNINDMF3VF66AYLW4/

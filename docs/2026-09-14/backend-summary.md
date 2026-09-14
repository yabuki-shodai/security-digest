# Backend CVE Summary (2026-09-14)

## Overview

- 取得日時: 2026-09-14 09:07:11 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 13
- Critical: 1
- High: 7
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-89050](https://wpscan.com/vulnerability/da063797-1c68-4164-a94b-9e9b628bcd75/)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-89050
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-14 06:17:02 JST
- 更新日: 2026-09-14 06:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Quads Ads Manager for Google AdSense（WordPressプラグイン）3.0.5 未満において、決済ゲートウェイでの支払い完了確認を行わずに注文を「支払い済み」とする脆弱性。
- 影響: 未支払いのまま広告枠を取得・掲載される可能性があります。
- 推奨対応: プラグインを 3.0.5 以降の最新バージョンへアップデートしてください。

#### References
- https://wpscan.com/vulnerability/da063797-1c68-4164-a94b-9e9b628bcd75/

### [CVE-2026-35867](https://github.com/Orcust-Automaton/Vulnerability/blob/main/LB-Link/AC1900_AZ2/bs_SetLimitCli_info.md)

> **Backend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-35867
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-14 07:16:59 JST
- 更新日: 2026-09-14 07:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LB-LINK ルーター AC1900_AZ2 V1.0.2 の libshare.so 内 bs_SetLimitCli_info 関数に、シェルメタ文字を介したコマンドインジェクションの脆弱性。
- 影響: 管理者権限を持たない攻撃者でも、該当の POST リクエストを送信することで任意のコマンドを実行できる可能性があります。
- 推奨対応: 該当エンドポイントへのアクセスを制限し、修正されたファームウェアが提供されているか確認してください。

#### References
- https://github.com/Orcust-Automaton/Vulnerability/blob/main/LB-Link/AC1900_AZ2/bs_SetLimitCli_info.md

### [CVE-2026-29811](https://github.com/usmannasir/cyberpanel/commit/0a099b1b193946555fbdd387a28486b1521f9961)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-29811
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-14 05:16:51 JST
- 更新日: 2026-09-14 05:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CyberPanel 2.4.4 未満におけるドメイン判定処理の実装上の問題
- 影響: 誤ったフィルタリング処理により、別名ドメインの検出動作に予期しない不具合や不整合が発生する可能性（具体的なセキュリティ上の悪用影響は不明）。
- 推奨対応: CyberPanel 2.4.4 以降へアップデートする。

#### References
- https://github.com/usmannasir/cyberpanel/commit/0a099b1b193946555fbdd387a28486b1521f9961

### [CVE-2026-37008](https://docs.python.org/3/library/ctypes.html)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-37008
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-14 06:17:01 JST
- 更新日: 2026-09-14 06:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CrewAI (コミット fb2323b 未満) において、Python のインポートレベルのブロックリストによる制限が不十分でサンドボックスを回避できる脆弱性。
- 影響: Python インタプリタの完全な実行環境にアクセスされ、制限を回避して C ライブラリの呼出し等の任意処理を実行される可能性があります。
- 推奨対応: fb2323b 以降のコミットを含むバージョンへアップデートし、プロセス分離等による堅牢なサンドボックス構造を採用してください。

#### References
- https://docs.python.org/3/library/ctypes.html
- https://github.com/crewAIInc/crewAI/commit/fb2323b3deb3ec62b3965526857e77a2264e4cd0
- https://yerangamage.com/cves/detail/?slug=crewai-sandbox-escape

### [CVE-2026-81648](https://wpscan.com/vulnerability/9b1490a0-1381-4d22-8086-f75aade4e898/)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-81648
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-14 06:17:01 JST
- 更新日: 2026-09-14 06:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CryptoPayment Gateway WordPress プラグイン（1.2.1-1.2.2）の AJAX エンドポイントにおける認可チェックの欠如
- 影響: 未認証の攻撃者が任意のサーバーファイル削除、決済設定の上書き、ウォレット資格情報の平文取得など、管理者権限の操作を実行可能。
- 推奨対応: 修正済みバージョンへアップデートするか、該当プラグインの使用を停止する。

#### References
- https://wpscan.com/vulnerability/9b1490a0-1381-4d22-8086-f75aade4e898/

### [CVE-2026-15891](https://github.com/zephyrproject-rtos/zephyr/commit/bd21e954c36be105a374bbc090623810f1a17ee3)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-15891
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-09-14 08:16:27 JST
- 更新日: 2026-09-14 08:16:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MQTT-SN クライアント keepalive ハンドラにおける NULL ポインタ参照およびメモリ破壊の脆弱性
- 影響: ゲートウェイ切断時にシステムクラッシュやカーネルパニックを引き起こすか、メモリ割り当てのフリーリストを破壊する可能性がある。
- 推奨対応: 修正パッチを適用するか、問題を修正したライブラリバージョンへ更新する。

#### References
- https://github.com/zephyrproject-rtos/zephyr/commit/bd21e954c36be105a374bbc090623810f1a17ee3
- https://github.com/zephyrproject-rtos/zephyr/security/advisories/GHSA-c4g8-4f9p-4746

### [CVE-2026-74933](https://wpscan.com/vulnerability/23dc45bb-e7b6-4cae-81ce-2c6394afb454/)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-74933
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-14 06:17:01 JST
- 更新日: 2026-09-14 06:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GenieWords WordPress プラグイン（1.5.27-1.5.34）における認可不備および不適切なデータ出力処理
- 影響: 未認証の第三者によりプラグイン設定が上書きされ、全フロントエンドページで実行される任意のスクリプト（XSS）が注入される可能性がある。
- 推奨対応: 修正済みバージョンへアップデートする。

#### References
- https://wpscan.com/vulnerability/23dc45bb-e7b6-4cae-81ce-2c6394afb454/

### [CVE-2026-85129](https://wpscan.com/vulnerability/a50f6ec1-4297-453e-b45f-6fd889b6b0d2/)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-85129
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-14 06:17:02 JST
- 更新日: 2026-09-14 06:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Hoo Companion WordPress プラグイン 1.0.2 のインポート機能における認可・検証およびサニタイズの欠如
- 影響: 未認証の攻撃者により既存テーマ設定が破棄され、閲覧者のブラウザ上で実行される任意のスクリプト（XSS）が注入される可能性がある。
- 推奨対応: 修正版へアップデートするか、プラグインの使用を停止する。

#### References
- https://wpscan.com/vulnerability/a50f6ec1-4297-453e-b45f-6fd889b6b0d2/

### [CVE-2026-88793](https://wpscan.com/vulnerability/7f695b0c-5dbc-4f3e-9b3f-c3558b1729ad/)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-88793
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-14 06:17:02 JST
- 更新日: 2026-09-14 06:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: YouTube Embed WordPress プラグイン（10.0-10.3）の AJAX アクションにおける認可欠如およびエスケープ不足
- 影響: 未認証の攻撃者によって保存型XSSが注入され、管理者を含む他ユーザーのセッション上で任意スクリプトが実行される可能性がある。
- 推奨対応: プラグインを修正済みバージョンへアップデートする。

#### References
- https://wpscan.com/vulnerability/7f695b0c-5dbc-4f3e-9b3f-c3558b1729ad/

### [CVE-2026-88802](https://wpscan.com/vulnerability/cac1846c-bbf4-4ad2-8dfb-d7025034a9a7/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-88802
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-14 06:17:02 JST
- 更新日: 2026-09-14 06:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MDJM Event Management（1.7.8.5未満）および Mobile Events Manager（1.4.8.3以下）におけるデータ削除権限検証の欠如
- 影響: 未認証の攻撃者により、ゴミ箱を経由することなく任意の投稿、固定ページ、メディア添付ファイルを永久に削除される可能性がある。
- 推奨対応: 対象プラグインを修正済みバージョンへアップデートする。

#### References
- https://wpscan.com/vulnerability/cac1846c-bbf4-4ad2-8dfb-d7025034a9a7/

### [CVE-2026-90581](https://github.com/cym1102/nginxWebUI/)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-90581
- 関連キーワード: gin, nginx
- 影響製品: -
- 公開日: 2026-09-14 05:16:51 JST
- 更新日: 2026-09-14 05:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: nginxWebUI（4.4.2以下）の MainController.autoUpdate におけるコードインジェクションの脆弱性
- 影響: リモートの攻撃者が url 引数を操作することで任意のコードを実行できる可能性がある（実証コード公開済み）。
- 推奨対応: 修正パッチ（Pull Request）の適用または対応バージョンへの更新を行う。

#### References
- https://github.com/cym1102/nginxWebUI/
- https://github.com/cym1102/nginxWebUI/issues/213
- https://github.com/cym1102/nginxWebUI/pull/215
- https://vuldb.com/cve/CVE-2026-90581
- https://vuldb.com/submit/913328

### [CVE-2026-29812](https://github.com/usmannasir/cyberpanel/commit/0a099b1b193946555fbdd387a28486b1521f9961)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-29812
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-14 05:16:51 JST
- 更新日: 2026-09-14 05:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CyberPanel 2.4.4 未満における子ドメイン操作アクションの監査ログ欠如
- 影響: 子ドメイン一覧を変更・操作する操作が発生した際、ログが記録されないため事後調査や監査が困難となる。
- 推奨対応: CyberPanel 2.4.4 以降へアップデートする。

#### References
- https://github.com/usmannasir/cyberpanel/commit/0a099b1b193946555fbdd387a28486b1521f9961

### [CVE-2026-90575](https://github.com/JdExploit/small-crm-login-unserialize)

> **Backend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-90575
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-14 03:16:50 JST
- 更新日: 2026-09-14 03:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PHPGurukul Small CRM 4.0 の /crm/login.php における不適切なデシリアライゼーションの脆弱性
- 影響: リモートの攻撃者が geopluginURL 引数を操作してデシリアライズ処理を悪用する可能性がある（攻撃難易度は高いがPoC公開済み）。
- 推奨対応: 不適切な unserialize 呼び出し箇所を修正したコードへの変更やパッチ適用を行う。

#### References
- https://github.com/JdExploit/small-crm-login-unserialize
- https://phpgurukul.com/
- https://vuldb.com/cve/CVE-2026-90575
- https://vuldb.com/submit/913188
- https://vuldb.com/vuln/403160

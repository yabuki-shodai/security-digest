# Backend CVE Summary (2026-09-21)

## Overview

- 取得日時: 2026-09-21 09:11:22 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 1
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-88855](https://www.OrdaSoft.com/)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-88855
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-21 03:16:54 JST
- 更新日: 2026-09-21 03:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OrdaSoft Joomla Gallery 拡張機能（6.2.7 未満）の saveGallery() における SQL インジェクションの脆弱性。入力値のサニタイズ処理が不十分なため発生します。
- 影響: 認証済みの管理者権限（core.manage）を持つユーザーにより、パスワードハッシュの抽出を含むデータベースへの完全な読み書きが行われる可能性があります。
- 推奨対応: OrdaSoft Joomla Gallery を 6.2.7 以降の修正済みバージョンへ更新してください。

#### References
- https://www.OrdaSoft.com/

### [CVE-2026-94039](https://github.com/vas3k/TaxHacker/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-94039
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-21 02:16:52 JST
- 更新日: 2026-09-21 02:16:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: vas3k TaxHacker（0.8.5 以前）の /apps/invoices/actions.ts における businessLogo 引数の処理不備による SSRF（サーバーサイドリクエストフォージェリ）の脆弱性。
- 影響: 遠隔の攻撃者により、SSRF 攻撃が実行される可能性があります。公開済みのエクスプロイトが存在します。
- 推奨対応: 開発元による修正の確認・適用、または影響を受ける入力機能のアクセス制限や検証を強化してください。

#### References
- https://github.com/vas3k/TaxHacker/
- https://github.com/vas3k/TaxHacker/issues/186
- https://vuldb.com/cve/CVE-2026-94039
- https://vuldb.com/submit/947878
- https://vuldb.com/vuln/407968

### [CVE-2026-94045](https://github.com/newbee-ltd/newbee-mall/)

> **Backend** / **MEDIUM** / CVSS: **4.0** / KEV: **no**

- タイトル: CVE-2026-94045
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-21 04:17:13 JST
- 更新日: 2026-09-21 04:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: newbee-mall（1.0.0 以前）の Goods Save エンドポイントにおける引数処理不備による持続型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 遠隔の攻撃者により悪意のあるスクリプトを実行される可能性があります。公開済みのエクスプロイトが存在します。
- 推奨対応: ファイルアップロード時の検証強化および静的リソースパスにおける適切なエスケープ処理の実施、または修正パッチの適用を行ってください。

#### References
- https://github.com/newbee-ltd/newbee-mall/
- https://github.com/newbee-ltd/newbee-mall/issues/126
- https://vuldb.com/cve/CVE-2026-94045
- https://vuldb.com/submit/949263
- https://vuldb.com/vuln/407974

### [CVE-2026-94043](https://github.com/free5gc/amf/commit/e323b01464355781b8b8d5dd695e05cbc00a62f2)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-94043
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-21 04:17:12 JST
- 更新日: 2026-09-21 04:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Free5GC（4.2.3 以前）の Gmm Handler（handler.go）における競合状態（レースコンディション）の脆弱性。
- 影響: 遠隔の攻撃者により、サービスの誤動作や意図しない処理が発生する可能性があります。
- 推奨対応: 提供されている修正パッチ（e323b01464355781b8b8d5dd695e05cbc00a62f2）を適用してください。

#### References
- https://github.com/free5gc/amf/commit/e323b01464355781b8b8d5dd695e05cbc00a62f2
- https://github.com/free5gc/amf/pull/238
- https://github.com/free5gc/free5gc/
- https://github.com/free5gc/free5gc/issues/1109
- https://vuldb.com/cve/CVE-2026-94043

### [CVE-2026-94042](https://github.com/AdithyaYelloju/Restaurant-Management-System/issues/3)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-94042
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-09-21 03:16:54 JST
- 更新日: 2026-09-21 03:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AdithyaYelloju Restaurant Management System（コミット 7f0e7e84 以前）の admin/add_table.php における SQL インジェクションの脆弱性。
- 影響: 遠隔の攻撃者により、データベース内の情報の閲覧や改ざんが行われる可能性があります。公開済みのエクスプロイトが存在します。
- 推奨対応: 該当箇所のプレースホルダ処理への修正やサニタイズの強化、または最新のリポジトリコードの適用を行ってください。

#### References
- https://github.com/AdithyaYelloju/Restaurant-Management-System/issues/3
- https://vuldb.com/cve/CVE-2026-94042
- https://vuldb.com/submit/948799
- https://vuldb.com/vuln/407971
- https://vuldb.com/vuln/407971/cti

### [CVE-2026-88854](https://www.OrdaSoft.com/)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-88854
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-21 03:16:53 JST
- 更新日: 2026-09-21 03:16:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OrdaSoft Joomla Gallery 拡張機能（6.2.7 未満）の検索エンドポイントにおける未認証 SQL インジェクションの脆弱性。
- 影響: 未認証の遠隔の第三者により、データベース内の任意の情報が取得・閲覧される可能性があります。
- 推奨対応: OrdaSoft Joomla Gallery を 6.2.7 以降の修正済みバージョンへ更新してください。

#### References
- https://www.OrdaSoft.com/

### [CVE-2026-94036](https://pastebin.com/gzKNCCPV)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-94036
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-21 01:16:55 JST
- 更新日: 2026-09-21 01:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: D-Link DIR-X1860 および DIR-X1860Z（ファームウェア 1.0.2.220120.165402 以前）の routerd 成分における不適切なアクセス制御の脆弱性。
- 影響: 同一ローカルネットワーク上の攻撃者により、アクセス制御を回避される可能性があります。公開済みのエクスプロイトが存在します。
- 推奨対応: 開発元が提供する最新ファームウェアへアップデートしてください。

#### References
- https://pastebin.com/gzKNCCPV
- https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10513
- https://vuldb.com/cve/CVE-2026-94036
- https://vuldb.com/submit/947565
- https://vuldb.com/vuln/407965

### [CVE-2026-94093](https://github.com/DLR-RM/stable-baselines3/)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-94093
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-21 08:17:03 JST
- 更新日: 2026-09-21 08:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DLR-RM stable-baselines3（2.9.0 以前）のモデル読み込み処理（save_util.py）における不安全なデシリアライズ（pickle）の脆弱性。
- 影響: 信頼できないモデルファイルを読み込んだ際、遠隔から任意コードを実行される可能性があります。公開済みのエクスプロイトが存在します。
- 推奨対応: 信頼できないソースからのモデルの読み込みを避け、修正済みのバージョンを使用してください。

#### References
- https://github.com/DLR-RM/stable-baselines3/
- https://github.com/DLR-RM/stable-baselines3/issues/2281
- https://vuldb.com/cve/CVE-2026-94093
- https://vuldb.com/submit/952734
- https://vuldb.com/vuln/408021

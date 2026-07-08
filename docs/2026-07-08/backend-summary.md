# Backend CVE Summary (2026-07-08)

## Overview

- 取得日時: 2026-07-08 14:11:12 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-53877](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-53877
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-07-08 00:16:48 JST
- 更新日: 2026-07-08 01:16:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Django 6.0.7未満および5.2.16未満のバージョンで、`django.contrib.gis.gdal.GDALRaster`がバイトオブジェクトから構築される際にメモリの過剰読み取りが発生し、隣接メモリの情報漏洩やサービス障害を引き起こす可能性があります。  
- 影響: メモリ情報の漏洩やセグメンテーションフォルトによるサービスの低下が発生する恐れがあります。  
- 推奨対応: Djangoを6.0.7以降または5.2.16以降にアップデートし、該当機能の利用時は注意してください。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://groups.google.com/g/django-announce
- https://www.djangoproject.com/weblog/2026/jul/07/security-releases/

### [CVE-2026-53878](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-53878
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-07-08 00:16:48 JST
- 更新日: 2026-07-08 01:16:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Django 6.0.7および5.2.16未満のバージョンで、DomainNameValidatorがドメイン名内の改行を禁止しておらず、HTTPレスポンスに改行を含む値を使用するとヘッダーインジェクションの可能性がある問題。  
- 影響: Django自体のHttpResponseは改行を禁止しているため直接の影響は限定的だが、改行を含む値をHTTPレスポンスに含めるアプリケーションでリスクがある。  
- 推奨対応: Djangoを6.0.7または5.2.16以降にアップデートし、入力値の改行を適切に検証・除去することを推奨。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://groups.google.com/g/django-announce
- https://www.djangoproject.com/weblog/2026/jul/07/security-releases/

### [CVE-2026-48588](https://docs.djangoproject.com/en/dev/releases/security/)

> **Backend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-48588
- 関連キーワード: django, go
- 影響製品: -
- 公開日: 2026-07-08 00:16:47 JST
- 更新日: 2026-07-08 01:16:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Django 6.0.7未満および5.2.16未満で、UpdateCacheMiddlewareやcache_pageデコレータがクッキーに依存するレスポンスを誤って共有キャッシュに保存し、関連のないクッキーを持つリクエストでプライベートデータが読み取られる可能性があります。  
- 影響: リモート攻撃者が共有キャッシュから他ユーザーのプライベートデータを取得できる恐れがあります。  
- 推奨対応: Djangoを6.0.7以降または5.2.16以降にアップデートし、該当ミドルウェアやデコレータの利用状況を確認してください。

#### References
- https://docs.djangoproject.com/en/dev/releases/security/
- https://groups.google.com/g/django-announce
- https://www.djangoproject.com/weblog/2026/jul/07/security-releases/

### [CVE-2026-46700](https://github.com/actualbudget/actual/commit/3494f78c9459ed9c412e28b500b675ba5eb72d4e)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-46700
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-08 06:17:25 JST
- 更新日: 2026-07-08 06:17:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Actualの26.6.0以前のバージョンにおいて、GET /secret/:nameエンドポイントが管理者権限を適切に検証せず、認証済みの非管理者ユーザーが管理者用の秘密情報を参照可能な脆弱性が存在します。  
- 影響: 認証済みの非管理者ユーザーが銀行連携の秘密情報などの機密データを取得できる可能性があります。  
- 推奨対応: バージョン26.6.0以降にアップデートし、管理者権限の検証が適切に行われることを確認してください。

#### References
- https://github.com/actualbudget/actual/commit/3494f78c9459ed9c412e28b500b675ba5eb72d4e
- https://github.com/actualbudget/actual/pull/7862
- https://github.com/actualbudget/actual/releases/tag/v26.6.0
- https://github.com/actualbudget/actual/security/advisories/GHSA-3f62-qv96-4p78

### [CVE-2026-59709](https://github.com/ghostfolio/ghostfolio)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-59709
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-08 00:16:49 JST
- 更新日: 2026-07-08 00:16:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: GhostfolioのPUT /api/v1/portfolio/holding/:dataSource/:symbol/tagsエンドポイントで、Impersonation-Idヘッダー処理時にAccess.permissionsフィールドの検証が不十分で、読み取り専用権限者が保有銘柄のタグを変更可能です。  
- 影響: 有効な読み取り専用共有トークンを持つ攻撃者が、被害者のポートフォリオ保有銘柄のタグを追加・削除でき、分類やレポートの整合性が損なわれる可能性があります。  
- 推奨対応: アクセス権限の検証を強化し、読み取り専用ユーザーがタグ変更できないように修正することを検討してください。

#### References
- https://github.com/ghostfolio/ghostfolio
- https://github.com/ghostfolio/ghostfolio/commit/697ef59e3b58bebc5c21a9e482e4f5643390f316
- https://github.com/ghostfolio/ghostfolio/issues/7196
- https://www.vulncheck.com/advisories/ghostfolio-unauthorized-portfolio-holding-tag-modification-via-missing-permission-check

### [CVE-2026-50179](https://github.com/actualbudget/actual/commit/068185751c03b42e726e3c60b718413d5f96c306)

> **Backend** / **MEDIUM** / CVSS: **4.2** / KEV: **no**

- タイトル: CVE-2026-50179
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-08 07:16:52 JST
- 更新日: 2026-07-08 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Actualの26.6.0以前のバージョンで、CSVエクスポート機能がユーザー入力を適切に無害化せず、スプレッドシートで悪意ある数式として解釈される可能性があります。  
- 影響: 悪意のある数式により、取引データの漏洩や攻撃者が指定したスプレッドシート表示が行われるリスクがあります。  
- 推奨対応: バージョン26.6.0以降にアップデートし、CSVエクスポート機能の修正を適用してください。

#### References
- https://github.com/actualbudget/actual/commit/068185751c03b42e726e3c60b718413d5f96c306
- https://github.com/actualbudget/actual/releases/tag/v26.6.0
- https://github.com/actualbudget/actual/security/advisories/GHSA-xqjm-27pc-rvwm

### [CVE-2026-55079](https://github.com/coder/coder/pull/25710)

> **Backend** / **MEDIUM** / CVSS: **4.9** / KEV: **no**

- タイトル: CVE-2026-55079
- 関連キーワード: go, terraform
- 影響製品: -
- 公開日: 2026-07-08 09:16:33 JST
- 更新日: 2026-07-08 09:16:33 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CoderのTerraformを用いたリモート開発環境構築機能で、`FileSize`の上限チェックが不十分なため、過剰なメモリ割り当てが発生する可能性があります。  
- 影響: 悪意あるユーザーが大きなファイルサイズを指定することで、メモリ消費が増大し、サービスの安定性に影響を与える恐れがあります。  
- 推奨対応: バージョン2.29.7以降、2.32.7、2.33.8、2.34.2へのアップデートを推奨し、また暫定的に信頼できるサービスアカウントのみがプロビジョナーデーモンにアクセスできるよう制限してください。

#### References
- https://github.com/coder/coder/pull/25710
- https://github.com/coder/coder/releases/tag/v2.29.17
- https://github.com/coder/coder/releases/tag/v2.32.7
- https://github.com/coder/coder/releases/tag/v2.33.8
- https://github.com/coder/coder/releases/tag/v2.34.2

### [CVE-2026-14380](https://github.com/perl5-dbi/dbi/commit/b73d5d9901767fc1d16b6661ef08fbed4532e259.patch)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-14380
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-08 08:16:53 JST
- 更新日: 2026-07-08 10:16:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: PerlのDBIモジュール1.650未満のバージョンで、Profile属性に不正なコードが注入される脆弱性が存在します。  
- 影響: 攻撃者が任意のPerlコードを実行でき、システムコマンドの実行も可能になる恐れがあります。  
- 推奨対応: DBIモジュールを最新バージョンに更新し、Profile属性に外部からの入力を直接渡さないように注意してください。

#### References
- https://github.com/perl5-dbi/dbi/commit/b73d5d9901767fc1d16b6661ef08fbed4532e259.patch
- https://github.com/perl5-dbi/dbi/security/advisories/GHSA-ch8w-hxc2-v557
- https://metacpan.org/release/HMBRAND/DBI-1.650/changes
- http://www.openwall.com/lists/oss-security/2026/07/07/16

### [CVE-2026-46672](https://github.com/actualbudget/actual/commit/068185751c03b42e726e3c60b718413d5f96c306)

> **Backend** / **MEDIUM** / CVSS: **4.6** / KEV: **no**

- タイトル: CVE-2026-46672
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-08 06:17:25 JST
- 更新日: 2026-07-08 06:17:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ActualのCLIツールでCSV出力時に、CSVの数式インジェクションを防ぐ処理が不十分で、ユーザー制御可能な文字列がExcel等で自動評価される可能性があります。  
- 影響: 悪意あるCSVデータにより、データの漏洩や任意の数式実行が発生する恐れがあります。  
- 推奨対応: バージョン26.6.0以降にアップデートし、CSV出力時の数式インジェクション対策を適用してください。

#### References
- https://github.com/actualbudget/actual/commit/068185751c03b42e726e3c60b718413d5f96c306
- https://github.com/actualbudget/actual/pull/7859
- https://github.com/actualbudget/actual/releases/tag/v26.6.0
- https://github.com/actualbudget/actual/security/advisories/GHSA-7gh7-258j-4mpq

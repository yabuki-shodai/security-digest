# Backend CVE Summary (2026-09-27)

## Overview

- 取得日時: 2026-09-27 09:30:10 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 5
- High: 2
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-82901](https://plugins.trac.wordpress.org/browser/ultimate-addons-for-contact-form-7/tags/3.5.48/addons/pdf-generator/pdf-generator.php#L608)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-82901
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-27 04:16:28 JST
- 更新日: 2026-09-27 08:16:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用 Ultra Addons for Contact Form 7 プラグイン（3.5.50以下）における不適切なファイルタイプ検証の脆弱性。
- 影響: PDF Generatorモジュールが有効な場合、未認証の攻撃者により任意ファイルがアップロードされ、リモートコード実行（RCE）につながる可能性がある。
- 推奨対応: プラグインを修正済みバージョンに更新するか、PDF Generatorモジュールを無効化してください。

#### References
- https://plugins.trac.wordpress.org/browser/ultimate-addons-for-contact-form-7/tags/3.5.48/addons/pdf-generator/pdf-generator.php#L608
- https://plugins.trac.wordpress.org/browser/ultimate-addons-for-contact-form-7/tags/3.5.48/addons/pdf-generator/pdf-generator.php#L807
- https://plugins.trac.wordpress.org/browser/ultimate-addons-for-contact-form-7/tags/3.5.48/addons/signature/ultimate-signature.php#L133
- https://plugins.trac.wordpress.org/browser/ultimate-addons-for-contact-form-7/tags/3.5.48/addons/signature/ultimate-signature.php#L192
- https://plugins.trac.wordpress.org/browser/ultimate-addons-for-contact-form-7/tags/3.5.48/addons/signature/ultimate-signature.php#L300

### [CVE-2026-85984](https://plugins.trac.wordpress.org/browser/miniorange-otp-verification/tags/5.5.5/includes/js/loginform.js#L176)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-85984
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-27 03:16:31 JST
- 更新日: 2026-09-27 08:16:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用 miniOrange OTP Login プラグイン（5.5.5以下）における認証バイパスの脆弱性。
- 影響: 未認証の攻撃者が既知の管理者ユーザー名を送信することで、パスワードやOTP検証なしに管理者としてログインできる可能性がある。
- 推奨対応: プラグインを最新バージョンに更新してください。

#### References
- https://plugins.trac.wordpress.org/browser/miniorange-otp-verification/tags/5.5.5/includes/js/loginform.js#L176
- https://plugins.trac.wordpress.org/browser/miniorange-otp-verification/tags/5.5.5/views/forms/mowploginform.php#L134
- https://plugins.trac.wordpress.org/changeset/3687601/miniorange-otp-verification
- https://www.wordfence.com/threat-intel/vulnerabilities/id/2895f0c2-41b6-4b11-9865-3bded4402aa9?source=cve

### [CVE-2026-97160](https://up.lomart.fr/)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-97160
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-27 00:16:55 JST
- 更新日: 2026-09-27 08:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla用 UP プラグイン拡張機能（5.0.0〜5.2.0、6.0.0〜6.0.29）におけるPHPコマンドインジェクションの脆弱性。
- 影響: 特権を持つ認証済みユーザーにより、サーバー上で任意のPHPコマンドを実行される可能性がある。
- 推奨対応: プラグインを修正済みバージョンにアップデートしてください。

#### References
- https://up.lomart.fr/

### [CVE-2026-97161](https://up.lomart.fr/)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-97161
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-27 00:16:55 JST
- 更新日: 2026-09-27 08:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla用 UP プラグイン拡張機能（5.0.0〜5.2.0、6.0.0〜6.0.29）におけるパストラバーサルおよびファイルアクセスの脆弱性。
- 影響: 不適切なファイルアクセス制御により、本来アクセスできないシステムファイルが閲覧または操作される可能性がある。
- 推奨対応: プラグインを修正済みバージョンにアップデートしてください。

#### References
- https://up.lomart.fr/

### [CVE-2026-97163](https://up.lomart.fr/)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-97163
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-27 00:16:55 JST
- 更新日: 2026-09-27 08:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla用 UP プラグイン拡張機能（5.0.0〜5.2.0、6.0.0〜6.0.29）における未認証のリモートコードインストールの脆弱性。
- 影響: 認証なしでリモートから不正なコードや拡張機能がインストールされ、システムが完全に侵害される可能性がある。
- 推奨対応: プラグインを修正済みバージョンにアップデートしてください。

#### References
- https://up.lomart.fr/

### [CVE-2026-77203](https://plugins.trac.wordpress.org/browser/groups/tags/4.5.0/lib/views/class-groups-shortcodes.php#L463)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-77203
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-27 03:16:29 JST
- 更新日: 2026-09-27 08:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用 Groups – Memberships and Access Control プラグイン（4.6.0以下）における不適切な権限検証による権限昇格の脆弱性。
- 影響: 購読者レベル以上の認証済み攻撃者が管理者グループ等へ自己登録し、最終的に管理者権限を取得できる可能性がある。
- 推奨対応: プラグインを修正済みバージョンに更新してください。

#### References
- https://plugins.trac.wordpress.org/browser/groups/tags/4.5.0/lib/views/class-groups-shortcodes.php#L463
- https://plugins.trac.wordpress.org/browser/groups/tags/4.5.0/lib/views/class-groups-shortcodes.php#L521
- https://plugins.trac.wordpress.org/browser/groups/tags/4.5.0/lib/views/class-groups-shortcodes.php#L586
- https://plugins.trac.wordpress.org/browser/groups/tags/4.5.0/lib/views/class-groups-shortcodes.php#L624
- https://plugins.trac.wordpress.org/browser/groups/tags/4.5.0/lib/wp/class-groups-wordpress.php#L248

### [CVE-2026-97162](https://up.lomart.fr/)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-97162
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-27 00:16:55 JST
- 更新日: 2026-09-27 08:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Joomla用 UP プラグイン拡張機能（5.0.0〜5.2.0、6.0.0〜6.0.29）における複数のSQLインジェクションの脆弱性。
- 影響: データベース内の情報の閲覧、改ざん、または消失につながる可能性がある。
- 推奨対応: プラグインを修正済みバージョンにアップデートしてください。

#### References
- https://up.lomart.fr/

### [CVE-2026-72662](https://discuss.elastic.co/t/kibana-8-19-22-9-4-6-security-update-esa-2026-103/390679)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-72662
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-27 06:16:55 JST
- 更新日: 2026-09-27 08:16:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KibanaのTimeline機能におけるアクセス制御不備による認可バイパスの脆弱性（CWE-639）。
- 影響: 同一スペース内の認証済みユーザーが、他ユーザーの所有する下書きTimelineオブジェクトを閲覧・変更・削除できる可能性がある。
- 推奨対応: Kibanaを修正済みバージョンに更新してください。

#### References
- https://discuss.elastic.co/t/kibana-8-19-22-9-4-6-security-update-esa-2026-103/390679

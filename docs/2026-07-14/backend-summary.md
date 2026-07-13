# Backend CVE Summary (2026-07-14)

## Overview

- 取得日時: 2026-07-14 08:07:46 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 19
- Critical: 2
- High: 8
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-62185](https://github.com/argoproj/argo-helm/security/advisories/GHSA-47m3-95c7-g2g8)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-62185
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-14 07:16:49 JST
- 更新日: 2026-07-14 07:16:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Argo CD Helm Chart 10.0.0未満ではデフォルトでネットワークポリシーが適用されず、クラスタ内の任意のPodがrepo-serverや他のArgo APIにアクセス可能です。  
- 影響: 不正アクセスによりクラスタの乗っ取りやリモートコード実行のリスクがあります。  
- 推奨対応: Argo CD Helm Chartを10.0.0以降にアップデートし、ネットワークポリシーの適切な設定を行うことを推奨します。

#### References
- https://github.com/argoproj/argo-helm/security/advisories/GHSA-47m3-95c7-g2g8
- https://www.vulncheck.com/advisories/argo-cd-helm-chart-missing-network-policy-rce

### [CVE-2026-58409](https://github.com/ChurchCRM/CRM/security/advisories/GHSA-37mf-vq43-5qp9)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-58409
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 06:16:48 JST
- 更新日: 2026-07-14 06:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ChurchCRMの7.4.0未満のバージョンで、管理者が悪意あるPHPウェブシェルを含むプラグインZIPをインストールすることでリモートコード実行が可能です。  
- 影響: 認証済み管理者によるサーバー上での任意コード実行が発生し、システムの完全な制御を奪われる恐れがあります。  
- 推奨対応: 速やかにChurchCRMをバージョン7.4.0以降にアップデートし、信頼できないプラグインのインストールを避けてください。

#### References
- https://github.com/ChurchCRM/CRM/security/advisories/GHSA-37mf-vq43-5qp9

### [CVE-2026-61500](https://github.com/rejetto/hfs/releases/tag/v3.2.1)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-61500
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 03:16:29 JST
- 更新日: 2026-07-14 04:28:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Rejetto HFS 3.0.0から3.2.0で、セッションCookieの署名鍵が暗号的でないMath.random()から生成され、ログイン時にその出力が未認証クライアントに漏洩します。  
- 影響: 攻撃者はログイン応答を収集して署名鍵を復元し、管理者セッションCookieを偽造して完全な管理権限とリモートコード実行を獲得する可能性があります。  
- 推奨対応: 可能な限り速やかにアップデートを適用し、暗号的に安全な乱数生成器を使用したバージョンに移行してください。

#### References
- https://github.com/rejetto/hfs/releases/tag/v3.2.1
- https://www.vulncheck.com/advisories/rejetto-hfs-session-forgery-via-predictable-signing-key

### [CVE-2026-49972](https://github.com/plank/laravel-mediable/commit/49e3583bed13423611b3391f89e6b002571eed73)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-49972
- 関連キーワード: gin, nginx
- 影響製品: -
- 公開日: 2026-07-14 04:17:10 JST
- 更新日: 2026-07-14 04:28:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Laravel-Mediable 7.0.0未満において、二重拡張子を悪用したファイルアップロードの脆弱性により、認証なしでリモートコード実行が可能となる問題です。  
- 影響: 不適切に設定されたApacheやnginxサーバーで、悪意あるPHPコードが実行されるリスクがあります。  
- 推奨対応: Laravel-Mediableを7.0.0以降にアップデートし、サーバーのファイル実行設定を見直すことを推奨します。

#### References
- https://github.com/plank/laravel-mediable/commit/49e3583bed13423611b3391f89e6b002571eed73
- https://github.com/plank/laravel-mediable/releases/tag/7.0.0
- https://www.vulncheck.com/advisories/laravel-mediable-file-upload-rce-via-extension-bypass

### [CVE-2026-55773](https://github.com/cedar-policy/cedar-java/security/advisories/GHSA-qmch-v2q9-wg4p)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-55773
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-07-14 05:16:48 JST
- 更新日: 2026-07-14 05:21:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CedarJavaのtoCedarExpr()メソッドが特殊文字を適切にエスケープしないため、ユーザー入力を用いてポリシーテキストを動的生成する際にCedar式のインジェクションが可能となる脆弱性です。  
- 影響: 悪意ある入力により、許可条件を無条件化したり禁止条件を無効化するなど、認可ロジックの改ざんが発生する恐れがあります。  
- 推奨対応: CedarJavaをバージョン2.3.6、3.4.1、または4.9.0以降にアップデートし、ユーザー入力を直接toCedarExpr()に渡さないように注意してください。

#### References
- https://github.com/cedar-policy/cedar-java/security/advisories/GHSA-qmch-v2q9-wg4p

### [CVE-2026-62194](https://github.com/openclaw/openclaw/security/advisories/GHSA-7vrr-rp4x-4g76)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-62194
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 07:16:50 JST
- 更新日: 2026-07-14 07:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenClaw 2026.5.20から2026.6.9未満のバージョンにおいて、プラグインインストールコマンドに権限昇格の脆弱性が存在します。  
- 影響: 低権限のユーザーが誤設定された入力パスや有効化された機能を悪用し、不正に権限を取得して操作を実行できる可能性があります。  
- 推奨対応: 影響を受けるバージョンから2026.6.9以降の修正版へアップデートし、プラグインインストール機能の設定を見直すことを推奨します。

#### References
- https://github.com/openclaw/openclaw/security/advisories/GHSA-7vrr-rp4x-4g76
- https://www.vulncheck.com/advisories/openclaw-privilege-escalation-via-plugin-install

### [CVE-2026-62184](https://github.com/openwrt/luci/commit/d9bbc372e29618a8807b693a1ccf6d0e42cd196c)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-62184
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 07:16:49 JST
- 更新日: 2026-07-14 07:16:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: luci-app-banipのログ解析において、awkベースのパーサがログ行の最初のIPv4アドレスを無条件に抽出する脆弱性が存在します。  
- 影響: 認証不要のリモート攻撃者が任意のIPアドレスをユーザー名フィールドに注入し、誤ったIPをブロックさせる可能性があります。  
- 推奨対応: luci-app-banipのログ解析処理を修正し、正確なIP抽出を行うか、アップデートが提供されていれば適用してください。

#### References
- https://github.com/openwrt/luci/commit/d9bbc372e29618a8807b693a1ccf6d0e42cd196c
- https://github.com/openwrt/luci/security/advisories/GHSA-r6hx-4f83-vp8m
- https://www.vulncheck.com/advisories/luci-app-banip-log-monitor-ip-extraction-bypass

### [CVE-2026-62196](https://github.com/openclaw/openclaw/security/advisories/GHSA-fh38-965w-f6c3)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-62196
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 07:16:51 JST
- 更新日: 2026-07-14 07:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenClaw 2026.3.22から2026.6.6未満のバージョンにおいて、WhatsAppグループIDが送信者の許可リストを不正に通過できる認可回避の脆弱性が存在します。  
- 影響: 低権限の攻撃者が、本来より高い権限を必要とする操作を実行できる可能性があります。  
- 推奨対応: 影響を受けるバージョンからのアップデートまたはパッチ適用を検討し、グループIDの検証方法を見直すことが推奨されます。

#### References
- https://github.com/openclaw/openclaw/security/advisories/GHSA-fh38-965w-f6c3
- https://www.vulncheck.com/advisories/openclaw-authorization-bypass-via-whatsapp-group-ids

### [CVE-2026-62240](https://github.com/crewAIInc/crewAI/commit/5d4851eac797cafc45b726f65747fe2c9520fc42)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-62240
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 07:16:52 JST
- 更新日: 2026-07-14 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: CrewAI 1.15.1未満のvalidate_url関数にサーバーサイドリクエストフォージェリ（SSRF）の脆弱性が存在し、攻撃者が内部サービスやクラウドメタデータにアクセス可能です。  
- 影響: 内部ネットワークへの不正アクセスや機密情報の漏洩リスクがあります。  
- 推奨対応: 速やかにCrewAIをバージョン1.15.1以上にアップデートし、URL検証の強化を行ってください。

#### References
- https://github.com/crewAIInc/crewAI/commit/5d4851eac797cafc45b726f65747fe2c9520fc42
- https://github.com/crewAIInc/crewAI/issues/6520
- https://github.com/crewAIInc/crewAI/pull/6331
- https://github.com/crewAIInc/crewAI/releases/tag/1.15.1
- https://www.vulncheck.com/advisories/crewai-ssrf-filter-bypass-via-http-redirect-in-scrape-tools

### [CVE-2026-62328](https://github.com/decolua/9router/security/advisories/GHSA-vjc7-jrh9-9j86)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-62328
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 07:16:52 JST
- 更新日: 2026-07-14 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: 9Router 0.4.41以前のバージョンに認証なしで機密情報が漏洩する脆弱性が存在し、リモート攻撃者が保護されていないAPI経由でユーザーデータにアクセス可能です。  
- 影響: 攻撃者はリクエストログやAI会話履歴、ユーザーのメールアドレスなどの機密情報を取得できる可能性があります。  
- 推奨対応: 影響を受けるバージョンの使用を避け、APIエンドポイントに適切な認証・認可を実装することが推奨されます。

#### References
- https://github.com/decolua/9router/security/advisories/GHSA-vjc7-jrh9-9j86
- https://www.vulncheck.com/advisories/9router-unauthenticated-information-disclosure-via-api-usage-endpoints

### [CVE-2026-58488](https://github.com/hedgedoc/hedgedoc/security/advisories/GHSA-2f9f-w8xq-276v)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-58488
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 07:16:48 JST
- 更新日: 2026-07-14 07:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: HedgeDocの1.11.0未満のバージョンで、IPアドレスの偽装により/loginおよび/registerルートのレート制限を回避できる脆弱性が存在します。  
- 影響: 攻撃者がログイン試行を大量に行ったり、複数のアカウントを不正に作成する可能性があります。  
- 推奨対応: HedgeDocをバージョン1.11.0以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/hedgedoc/hedgedoc/security/advisories/GHSA-2f9f-w8xq-276v

### [CVE-2026-61502](https://github.com/rejetto/hfs/releases/tag/v3.2.1)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-61502
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 03:16:30 JST
- 更新日: 2026-07-14 04:28:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Rejetto HFS 3.0.0から3.2.0において、GETメソッドで状態変更APIリクエストを受け入れ、GETリクエストをanti-CSRFヘッダー検査から除外する脆弱性が存在します。  
- 影響: リモート攻撃者が管理者のブラウザを操作してアカウント作成や設定変更などの管理操作を実行し、コード実行に至る可能性があります。  
- 推奨対応: 影響を受けるバージョンの使用を避け、可能であればアップデートや設定変更でGETメソッドによる状態変更を防ぐ対策を検討してください。

#### References
- https://github.com/rejetto/hfs/releases/tag/v3.2.1
- https://www.vulncheck.com/advisories/rejetto-hfs-cross-site-request-forgery-via-get-requests

### [CVE-2026-12385](https://plugins.trac.wordpress.org/browser/smart-slider-3/tags/3.5.1.37/Nextend/Framework/Content/ControllerAjaxContent.php#L15)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-12385
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 05:16:42 JST
- 更新日: 2026-07-14 05:21:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WordPressのSmart Slider 3プラグイン（3.5.1.37以下）において、認証済みの寄稿者以上の権限を持つユーザーが「keyword」パラメータを通じて非公開や下書き投稿のタイトルや内容の抜粋を取得できる情報漏洩の脆弱性が存在します。  
- 影響: 寄稿者以上の権限を持つユーザーが管理者や編集者の非公開投稿情報を不正に閲覧可能となるリスクがあります。  
- 推奨対応: プラグインを最新バージョンに更新し、不要な権限の付与を見直すことを検討してください。

#### References
- https://plugins.trac.wordpress.org/browser/smart-slider-3/tags/3.5.1.37/Nextend/Framework/Content/ControllerAjaxContent.php#L15
- https://plugins.trac.wordpress.org/browser/smart-slider-3/tags/3.5.1.37/Nextend/Framework/Content/ControllerAjaxContent.php#L22
- https://plugins.trac.wordpress.org/browser/smart-slider-3/tags/3.5.1.37/Nextend/Framework/Content/WordPress/WordPressContent.php#L20
- https://plugins.trac.wordpress.org/browser/smart-slider-3/tags/3.5.1.37/Nextend/Framework/Content/WordPress/WordPressContent.php#L45
- https://plugins.trac.wordpress.org/browser/smart-slider-3/tags/3.5.1.37/Nextend/Framework/Form/WordPress/PlatformForm.php#L22

### [CVE-2026-12536](https://themeforest.net/item/avada-responsive-multipurpose-theme/2833226)

> **Backend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-12536
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 05:16:42 JST
- 更新日: 2026-07-14 05:21:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: WordPressのAvada (Fusion) Builderプラグイン（バージョン3.15.5まで）において、‘Module Title’パラメータの不十分な入力検証により、永続的なクロスサイトスクリプティング（Stored XSS）が発生する可能性があります。  
- 影響: 認証されたContributor以上の権限を持つ攻撃者が任意のスクリプトを注入し、他ユーザーが該当ページを閲覧した際にスクリプトが実行されるリスクがあります。  
- 推奨対応: プラグインを最新バージョンに更新し、入力の適切なサニタイズと出力のエスケープが行われているか確認してください。

#### References
- https://themeforest.net/item/avada-responsive-multipurpose-theme/2833226
- https://www.wordfence.com/threat-intel/vulnerabilities/id/6199b852-3270-4456-934b-68c3ef11b9e5?source=cve

### [CVE-2026-61503](https://github.com/rejetto/hfs/releases/tag/v3.2.1)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-61503
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 03:16:30 JST
- 更新日: 2026-07-14 04:28:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Rejetto HFS 3.0.0から3.2.0にかけて、ログインエンドポイントが存在するユーザー名に応じて異なる応答を返す問題があり、リモートの未認証攻撃者が有効なアカウント名を特定可能です。  
- 影響: 有効なアカウント名の特定により、パスワード推測やセッション偽造攻撃のリスクが高まる可能性があります。  
- 推奨対応: ソフトウェアのアップデートやログイン応答の情報漏洩を防ぐ設定の適用を検討し、不審なアクセスの監視を強化してください。

#### References
- https://github.com/rejetto/hfs/releases/tag/v3.2.1
- https://www.vulncheck.com/advisories/rejetto-hfs-username-enumeration-via-login-response-differences

### [CVE-2026-62193](https://github.com/openclaw/openclaw/security/advisories/GHSA-wgq8-x5wm-g4rw)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-62193
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 07:16:50 JST
- 更新日: 2026-07-14 07:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenClaw 2026.6.5から2026.6.8までのプラグインインストールラッパーにおいて、認可チェックをスキップする脆弱性が存在します。  
- 影響: 低権限の呼び出し元が意図しない権限で操作を実行または永続化できる可能性があります。  
- 推奨対応: 2026.6.9以降のバージョンにアップデートし、影響を受ける機能の設定を見直してください。

#### References
- https://github.com/openclaw/openclaw/security/advisories/GHSA-wgq8-x5wm-g4rw
- https://www.vulncheck.com/advisories/openclaw-authentication-bypass-via-plugin-install

### [CVE-2026-13221](https://github.com/Perl/perl5/commit/03f74bbbd3a68350d926ee93d56ee4808c28c4c7.patch)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-13221
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-07-14 02:16:48 JST
- 更新日: 2026-07-14 05:16:42 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Perl 5.43.9以前のバージョンで、65535を超える固定文字列の分岐を含む正規表現が誤ったマッチ結果を返す問題があります。  
- 影響: 正規表現の誤判定により、アクセス制御やフィルタリングの判断が誤る可能性があります。  
- 推奨対応: 大量の分岐を含む正規表現の使用を避け、Perlのアップデートやパッチ適用を検討してください。

#### References
- https://github.com/Perl/perl5/commit/03f74bbbd3a68350d926ee93d56ee4808c28c4c7.patch
- https://github.com/Perl/perl5/issues/23388
- http://www.openwall.com/lists/oss-security/2026/07/13/5

### [CVE-2026-51538](https://gist.github.com/MrAlaskan/8156ca3acd6754a9f66efede0a1351f2)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-51538
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 07:16:47 JST
- 更新日: 2026-07-14 07:16:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: EIPStackGroup OpENer 2.3.0において、セッションハンドルの所有者確認が不十分なため、他のクライアントの有効なセッションハンドルを悪用してアクセス制御を回避される可能性があります。  
- 影響: ネットワーク上の攻撃者が正当なセッションハンドルを使い、不正に権限を取得するリスクがあります。  
- 推奨対応: セッションハンドルと発信元TCP接続の強い紐付けを実装し、アクセス制御の検証を強化することが望ましいです。

#### References
- https://gist.github.com/MrAlaskan/8156ca3acd6754a9f66efede0a1351f2
- https://github.com/EIPStackGroup/OpENer/issues/565

### [CVE-2026-51821](https://github.com/sign9981/CVE/issues/2)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-51821
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-14 07:16:47 JST
- 更新日: 2026-07-14 07:16:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Shenzhou Shihan Video Conference System v1.0の/user/getUserLoginエンドポイントにSQLインジェクションの脆弱性が存在し、リモート攻撃者が任意のコードを実行できる可能性があります。  
- 影響: 攻撃者によるデータベース操作やシステムの不正制御が懸念されますが、詳細な影響範囲は不明です。  
- 推奨対応: ベンダーからの修正パッチ適用や入力値の適切な検証・サニタイズを実施し、アクセス制御の強化を検討してください。

#### References
- https://github.com/sign9981/CVE/issues/2
- https://www.cnblogs.com/goww/p/19942271

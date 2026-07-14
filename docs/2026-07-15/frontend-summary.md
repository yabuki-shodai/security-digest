# Frontend CVE Summary (2026-07-15)

## Overview

- 取得日時: 2026-07-15 08:07:55 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 0
- High: 2
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-11403](https://help.sonatype.com/en/sonatype-nexus-repository-3-93-0-release-notes.html)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-11403
- 関連キーワード: npm, docker
- 影響製品: -
- 公開日: 2026-07-15 01:16:44 JST
- 更新日: 2026-07-15 01:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Sonatype Nexus Repository Managerのフォーマット固有APIキー生成に脆弱性があり、リモート攻撃者が対象ユーザーとしてリポジトリ操作に不正アクセスする可能性があります。  
- 影響: NuGet、Docker、npmのAPIキーが有効で、対象ユーザーがアクティブなAPIキーを持つ場合に悪用される恐れがあります。  
- 推奨対応: フォーマット固有APIキーの設定を見直し、最新のセキュリティパッチを適用することを推奨します。

#### References
- https://help.sonatype.com/en/sonatype-nexus-repository-3-93-0-release-notes.html
- https://support.sonatype.com/hc/en-us/articles/52347011450515/

### [CVE-2026-15697](https://github.com/svgdotjs/svg.js/)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-15697
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-07-15 01:16:46 JST
- 更新日: 2026-07-15 01:42:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: svgdotjsのsvg.js（バージョン3.2.5以前）において、EventTarget.on関数でオブジェクトのプロトタイプ属性が不適切に変更される脆弱性が報告されています。  
- 影響: リモートからの操作により、オブジェクトのプロトタイプ汚染が発生し、予期しない動作やセキュリティリスクが生じる可能性があります。  
- 推奨対応: 公式の修正が提供されていないため、影響を受けるバージョンの使用を控え、アップデートやパッチの公開を待つことが望ましいです。

#### References
- https://github.com/svgdotjs/svg.js/
- https://github.com/svgdotjs/svg.js/issues/1343
- https://vuldb.com/cve/CVE-2026-15697
- https://vuldb.com/submit/856013
- https://vuldb.com/vuln/378244

### [CVE-2026-60118](https://github.com/HiEventsDev/Hi.Events/commit/9eec95e6176f500b71bf633986243045ca78cefb)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-60118
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-07-15 01:17:04 JST
- 更新日: 2026-07-15 05:18:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Hi.Events 1.11.0未満において、サーバー側の可視性制御が欠如しており、認証されていない攻撃者が隠されたチケットを不正に購入できる脆弱性が存在します。  
- 影響: 攻撃者は非公開のVIPチケットや招待制チケット、割引チケットを不正に購入可能で、チケット販売の制限が回避される恐れがあります。  
- 推奨対応: Hi.Eventsをバージョン1.11.0以降にアップデートし、サーバー側の可視性制御が適切に行われていることを確認してください。

#### References
- https://github.com/HiEventsDev/Hi.Events/commit/9eec95e6176f500b71bf633986243045ca78cefb
- https://github.com/HiEventsDev/Hi.Events/pull/1259
- https://github.com/HiEventsDev/Hi.Events/releases/tag/v.1.11.0-beta
- https://github.com/HiEventsDev/Hi.Events/security/advisories/GHSA-2h54-cprv-vj74
- https://www.vulncheck.com/advisories/hi-events-beta-hidden-ticket-enumeration-via-order-creation-endpoint

### [CVE-2026-9292](https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1787.html)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-9292
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-15 01:17:05 JST
- 更新日: 2026-07-15 01:46:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: FactoryTalk® DataMosaix™ Private CloudのWorkflows設定における不適切な入力無害化により、認証済みの高権限攻撃者が永続的なクロスサイトスクリプティング（XSS）を実行可能です。  
- 影響: 悪意あるスクリプトが他のユーザーのブラウザで実行され、アカウント乗っ取りや認証情報の窃取、悪意あるサイトへのリダイレクトが発生する可能性があります。  
- 推奨対応: 影響を受ける製品のアップデート適用や、Workflows設定への入力検証強化、権限管理の見直しを検討してください。

#### References
- https://www.rockwellautomation.com/en-us/trust-center/security-advisories/advisory.SD1787.html

### [CVE-2026-36214](https://enhancesoft.com/)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-36214
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-15 02:16:46 JST
- 更新日: 2026-07-15 02:16:46 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: osTicketのバージョン1.10から1.17.7および1.18.0から1.18.3において、Bootstrap Tooltipコンポーネントの脆弱性と不十分なHTMLサニタイズにより、保存型XSSが発生する可能性があります。  
- 影響: リモートの攻撃者がAgentまたはAdminセッション内で任意のJavaScriptを実行できる恐れがあります。  
- 推奨対応: 最新バージョンへのアップデートや、HTML入力の適切なサニタイズを実施し、脆弱性の影響を軽減してください。

#### References
- https://enhancesoft.com/
- https://github.com/WesWrench/CVE-2026-36214
- https://github.com/osTicket/osTicket/commit/5afdf5450ff5c7d218447014b7abbb5f1e6dd42f
- https://github.com/osTicket/osTicket/releases/tag/v1.17.8
- https://github.com/osTicket/osTicket/releases/tag/v1.18.4

### [CVE-2026-52838](https://github.com/alextselegidis/easyappointments/commit/629a0415f54f75556c17f4f5d9c77fda1fdbdeae)

> **Frontend** / **LOW** / CVSS: **2.6** / KEV: **no**

- タイトル: CVE-2026-52838
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-15 01:17:00 JST
- 更新日: 2026-07-15 02:17:03 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Easy!Appointmentsの1.6.0未満のバージョンで、管理者が予約無効メッセージに悪意あるスクリプトを埋め込めるため、未認証ユーザーに対して保存型XSSが発生する可能性があります。  
- 影響: 未認証の訪問者が公開予約ページを閲覧すると、悪意あるスクリプトが実行されるリスクがあります。  
- 推奨対応: バージョン1.6.0以降にアップデートし、管理者が入力するメッセージのサニタイズを適切に行うことを推奨します。

#### References
- https://github.com/alextselegidis/easyappointments/commit/629a0415f54f75556c17f4f5d9c77fda1fdbdeae
- https://github.com/alextselegidis/easyappointments/security/advisories/GHSA-996f-334j-67g7
- https://github.com/alextselegidis/easyappointments/security/advisories/GHSA-996f-334j-67g7

### [CVE-2026-52837](https://github.com/alextselegidis/easyappointments/commit/725eafa647308846ce887657db12771a829e42ef)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-52837
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-15 00:17:04 JST
- 更新日: 2026-07-15 01:42:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Easy!Appointmentsのバージョン1.5.2以前では、認証なしで予約変更画面に顧客情報がJavaScriptとして埋め込まれ、appointment_hashを知る者が顧客データを閲覧可能です。  
- 影響: 顧客の個人情報が漏洩するリスクがあり、プライバシー侵害や情報漏洩につながる可能性があります。  
- 推奨対応: バージョン1.6.0以降にアップデートし、appointment_hashの取り扱いや認証処理の強化を検討してください。

#### References
- https://github.com/alextselegidis/easyappointments/commit/725eafa647308846ce887657db12771a829e42ef
- https://github.com/alextselegidis/easyappointments/security/advisories/GHSA-xgr6-pqjv-3pf8

### [CVE-2026-58475](https://www.vulncheck.com/advisories/sustainable-irrigation-platform-stored-xss-via-program-name)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-58475: dan-in-ca sustainable irrigation platform
- 関連キーワード: javascript
- 影響製品: dan-in-ca sustainable irrigation platform
- 公開日: 2026-07-15 00:17:06 JST
- 更新日: 2026-07-15 04:15:17 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: dan-in-caのSustainable Irrigation Platform（バージョン5.2.16以前）に、認証なしで悪意あるJavaScriptをプログラム名に埋め込める保存型クロスサイトスクリプティング（XSS）脆弱性があります。  
- 影響: 攻撃者は任意のJavaScriptをユーザーのブラウザ上で実行でき、情報漏洩やセッションハイジャックのリスクがあります。  
- 推奨対応: 最新バージョンへのアップデートや、入力値の適切なエンコード、パスフレーズの設定・変更を検討してください。

#### References
- https://www.vulncheck.com/advisories/sustainable-irrigation-platform-stored-xss-via-program-name
- https://www.zeroscience.mk/#/advisories/ZSL-2026-5994

### [CVE-2026-60119](https://github.com/HiEventsDev/Hi.Events/commit/1e36b070771801ed7113255ef7b3a7f271a2a794)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-60119
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-15 01:17:04 JST
- 更新日: 2026-07-15 05:18:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Hi.Events 1.11.0未満において、イベントタイトルに悪意あるスクリプトを埋め込むことでクロスサイトスクリプティング（XSS）が発生する脆弱性が存在します。  
- 影響: 認証済みのイベント作成・編集権限を持つ攻撃者が任意のJavaScriptを注入でき、公開イベントページを閲覧する全ユーザーに対して攻撃が可能となる恐れがあります。  
- 推奨対応: Hi.Eventsをバージョン1.11.0以降にアップデートし、イベントタイトルの入力値を適切にエスケープする対策を実施してください。

#### References
- https://github.com/HiEventsDev/Hi.Events/commit/1e36b070771801ed7113255ef7b3a7f271a2a794
- https://github.com/HiEventsDev/Hi.Events/pull/1260
- https://github.com/HiEventsDev/Hi.Events/releases/tag/v.1.11.0-beta
- https://github.com/HiEventsDev/Hi.Events/security/advisories/GHSA-2ggx-79g6-2jmj
- https://www.vulncheck.com/advisories/hi-events-beta-xss-via-event-title-json-stringify-injection

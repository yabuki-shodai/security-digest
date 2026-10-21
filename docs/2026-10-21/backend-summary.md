# Backend CVE Summary (2026-10-21)

## Overview

- 取得日時: 2026-10-21 09:33:56 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 16
- Critical: 5
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-113708](https://argo-cd.readthedocs.io/en/stable/user-guide/kustomize/#custom-kustomize-versions)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-113708
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-10-21 04:17:33 JST
- 更新日: 2026-10-21 04:59:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Argo CDにおけるKustomizeのURL引数処理不備に起因する、`argocd-repo-server`内でのコマンド実行の脆弱性。
- 影響: 攻撃者が悪意のあるKustomizationをリポジトリにコミットまたはアップロードすることで、`repo-server`権限で任意のコマンドを実行され、認証情報などが読み取られる可能性があります。
- 推奨対応: Argo CDを修正済みバージョン（3.3.15、3.4.10、3.5.4、3.6.0-rc2など）へアップデートしてください。

#### References
- https://argo-cd.readthedocs.io/en/stable/user-guide/kustomize/#custom-kustomize-versions
- https://github.com/argoproj/argo-cd/commit/25badeb7a1e154805340bb7237e0ce671f3772dd
- https://github.com/argoproj/argo-cd/pull/12299
- https://github.com/argoproj/argo-cd/releases/tag/v3.3.15
- https://github.com/argoproj/argo-cd/releases/tag/v3.4.10

### [CVE-2026-113709](https://argo-cd.readthedocs.io/en/stable/user-guide/kustomize/#kustomizing-helm-charts)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-113709
- 関連キーワード: go, gin, kubernetes
- 影響製品: -
- 公開日: 2026-10-21 04:17:33 JST
- 更新日: 2026-10-21 04:59:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Argo CDにおいてKustomizeの`--enable-helm`が有効な場合、リポジトリ制御下のディレクトリからHelmプラグインが自動読み込み・実行される脆弱性。
- 影響: 攻撃者が作成したリポジトリやファイル構成により、`repo-server`権限で任意のプログラムが実行され、認証情報などのデータが漏洩する可能性があります。
- 推奨対応: Argo CDを修正済みバージョン（3.3.15、3.4.10、3.5.4、3.6.0-rc2など）へアップデートしてください。

#### References
- https://argo-cd.readthedocs.io/en/stable/user-guide/kustomize/#kustomizing-helm-charts
- https://github.com/argoproj/argo-cd/commit/b6d5c23bce2f8a46c52975ba438a3b93d242d96c
- https://github.com/argoproj/argo-cd/pull/6059
- https://github.com/argoproj/argo-cd/releases/tag/v3.3.15
- https://github.com/argoproj/argo-cd/releases/tag/v3.4.10

### [CVE-2026-113672](https://argo-cd.readthedocs.io/en/stable/user-guide/tool_detection/#disable-built-in-tools)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-113672
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-10-21 03:17:20 JST
- 更新日: 2026-10-21 04:59:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Argo CDの`repo-server`における`.jsonnet`ファイルのインポート処理制限不備に起因する、パストラバーサルおよびリソース消費の脆弱性。
- 影響: サーバー上の任意の読み取り可能ファイル（秘密情報や環境変数）の漏洩や、メモリ枯渇によるサービス拒否（DoS）が引き起こされる可能性があります。
- 推奨対応: Argo CDを修正済みバージョン（3.3.15、3.4.10、3.5.4、3.6.0-rc2など）へアップデートしてください。

#### References
- https://argo-cd.readthedocs.io/en/stable/user-guide/tool_detection/#disable-built-in-tools
- https://github.com/argoproj/argo-cd/commit/27471d524958878e7acc5131fb466b292079cd05
- https://github.com/argoproj/argo-cd/pull/561
- https://github.com/argoproj/argo-cd/releases/tag/v3.3.15
- https://github.com/argoproj/argo-cd/releases/tag/v3.4.10

### [CVE-2026-113678](https://github.com/froxlor/froxlor/blob/2.3.14/lib/Froxlor/Http/Statistics.php#L144-L162)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-113678
- 関連キーワード: go, echo
- 影響製品: -
- 公開日: 2026-10-21 01:17:12 JST
- 更新日: 2026-10-21 01:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Froxlor（2.3.15未満）の`Statistics::makeChownWithNewStats`におけるシンボリックリンク追跡の脆弱性。
- 影響: 認証された顧客ユーザーが任意ディレクトリの所有権を不正に取得し、root権限への昇格が行われる可能性があります。
- 推奨対応: Froxlorをバージョン2.3.15以降にアップデートしてください。

#### References
- https://github.com/froxlor/froxlor/blob/2.3.14/lib/Froxlor/Http/Statistics.php#L144-L162
- https://github.com/froxlor/froxlor/commit/0805a7e16a223d528b51d8cacfaff54217b9d8f8
- https://github.com/froxlor/froxlor/releases/tag/2.3.15
- https://github.com/froxlor/froxlor/security/advisories/GHSA-vwjv-x8ff-4cvv
- https://www.vulncheck.com/advisories/froxlor-before-2.3.15-symlink-following-privilege-escalation-via-traffic-cron

### [CVE-2026-113666](https://github.com/apostrophecms/apostrophe/commit/9500b8b0e1d630d5e07fbb5fd2c25ed0943845ce)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-113666
- 関連キーワード: go, node.js, postgresql, mongodb
- 影響製品: -
- 公開日: 2026-10-21 03:17:20 JST
- 更新日: 2026-10-21 04:53:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ApostropheCMS（4.33.0未満）およびdb-connect（1.1.0未満）において、特定のアダプター使用時にプロトタイプチェーンを経由して共有メンバーを削除可能な脆弱性。
- 影響: 下書き閲覧権限を持つユーザーによってプロセスの整合性が損なわれ、永続的なサービス拒否（DoS）が発生する可能性があります。
- 推奨対応: db-connectを1.1.0以降、ApostropheCMSを4.33.0以降へアップデートしてください。

#### References
- https://github.com/apostrophecms/apostrophe/commit/9500b8b0e1d630d5e07fbb5fd2c25ed0943845ce
- https://github.com/apostrophecms/apostrophe/commit/f84fd41cbf6c22eb8d0008fc9c25df1f7130b350
- https://github.com/apostrophecms/apostrophe/releases/tag/@apostrophecms/db-connect@1.1.0
- https://github.com/apostrophecms/apostrophe/releases/tag/apostrophe@4.33.0
- https://github.com/apostrophecms/apostrophe/security/advisories/GHSA-j5rq-xfvr-p969

### [CVE-2026-113665](https://github.com/apostrophecms/apostrophe/commit/9500b8b0e1d630d5e07fbb5fd2c25ed0943845ce)

> **Backend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-113665
- 関連キーワード: go, node.js, mongodb
- 影響製品: -
- 公開日: 2026-10-21 03:17:19 JST
- 更新日: 2026-10-21 04:53:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ApostropheCMS（4.33.0未満）の通知モジュールにおけるRESTエンドポイントの不適切なアクセス制御の脆弱性。
- 影響: 未認証の攻撃者が通知IDを取得した場合、他のユーザーの通知を変更または改ざん・削除する可能性があります。
- 推奨対応: ApostropheCMSをバージョン4.33.0以降にアップデートしてください。

#### References
- https://github.com/apostrophecms/apostrophe/commit/9500b8b0e1d630d5e07fbb5fd2c25ed0943845ce
- https://github.com/apostrophecms/apostrophe/commit/f84fd41cbf6c22eb8d0008fc9c25df1f7130b350
- https://github.com/apostrophecms/apostrophe/releases/tag/apostrophe@4.33.0
- https://github.com/apostrophecms/apostrophe/security/advisories/GHSA-vwwx-px9w-crrc

### [CVE-2026-113397](https://fw.draytek.com.tw/Vigor2960/Firmware/v1.5.1.7/Vigor2960_v1.5.1.7.zip)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-113397
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-21 00:17:18 JST
- 更新日: 2026-10-21 04:27:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security vulnerability has been detected in DrayTek Vigor2960 1.5.1.6 Revision 8218. This affects the function ruequest_certificate of the file /cgi-bin/mainfunction.cgi of the component IPsec Handler. Such manipulation of the argument option leads to command injection. The attack can be launched remotely. The exploi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://fw.draytek.com.tw/Vigor2960/Firmware/v1.5.1.7/Vigor2960_v1.5.1.7.zip
- https://github.com/yikesoftware/DrayTek_Vigor2960_Security_Analysis/tree/main/cases/DRV2960-0014-authenticated-request-certificate-command-injection
- https://vuldb.com/cve/CVE-2026-113397
- https://vuldb.com/submit/992250
- https://vuldb.com/vuln/422673

### [CVE-2026-95109](https://github.com/eclipse-threadx/threadx/security/advisories/GHSA-fvp6-37q5-c648)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-95109
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-21 01:17:18 JST
- 更新日: 2026-10-21 04:48:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The Cortex-A7 MMU Modules port validates a caller-supplied buffer by translating **one address** — the first byte. The common Module Manager hands its range check the module instance, the start address and the complete byte size; the Cortex-A7 implementation discarded the instance and the size and asked the MMU a singl...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/eclipse-threadx/threadx/security/advisories/GHSA-fvp6-37q5-c648

### [CVE-2026-113603](https://github.com/x402-foundation/x402/blob/go/v2.28.0/go/extensions/signinwithx/server.go)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-113603
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-21 01:17:10 JST
- 更新日: 2026-10-21 05:06:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The x402 SIWX server extension in @x402/extensions 2.3.1 through 2.28.0, x402 PyPI 2.11.0 through 2.25.0, and Go module 2.16.0 through 2.28.0 contains an authorization bypass vulnerability that allows paying clients to unlock unpaid routes by supplying a mismatched PaymentPayload.resource URL. Attackers can pay for the...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/x402-foundation/x402/blob/go/v2.28.0/go/extensions/signinwithx/server.go
- https://github.com/x402-foundation/x402/blob/npm-@x402/extensions@v2.28.0/typescript/packages/extensions/src/sign-in-with-x/hooks.ts
- https://github.com/x402-foundation/x402/blob/pypi-x402@v2.25.0/python/x402/extensions/sign_in_with_x/hooks.py
- https://github.com/x402-foundation/x402/issues/3838
- https://github.com/x402-foundation/x402/pull/3840

### [CVE-2012-20005](https://github.com/projectdiscovery/nuclei-templates/blob/main/http/vulnerabilities/wordpress/wp-socialfit-xss.yaml)

> **Backend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2012-20005
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-21 06:17:12 JST
- 更新日: 2026-10-21 06:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SocialFit plugin for WordPress through 1.2.2 contains a reflected cross-site scripting vulnerability that allows unauthenticated attackers to inject scripts via the unsanitized msg parameter. Attackers can craft GET requests to /wp-content/plugins/socialfit/popup.php with service=googleplus and malicious msg values to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/projectdiscovery/nuclei-templates/blob/main/http/vulnerabilities/wordpress/wp-socialfit-xss.yaml
- https://wordpress.org/plugins/socialfit/
- https://www.exploit-db.com/exploits/37481
- https://www.vulncheck.com/advisories/socialfit-wordpress-plugin-1.2.2-reflected-xss-via-popup-php-msg-parameter

### [CVE-2026-113466](https://github.com/zast-ai/vulnerability-reports/blob/main/minio/unauth_admin_takeover.md)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-113466
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-21 00:17:19 JST
- 更新日: 2026-10-21 04:27:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A security vulnerability has been detected in MinIO up to RELEASE.2025-10-15T17-29-55Z. This issue affects the function globalDeploymentID/SessionTokenAuthenticate of the file cmd/common-main.go of the component Embedded Console. Such manipulation leads to use of hard-coded cryptographic key . It is possible to launch...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zast-ai/vulnerability-reports/blob/main/minio/unauth_admin_takeover.md
- https://vuldb.com/cve/CVE-2026-113466
- https://vuldb.com/submit/1004925
- https://vuldb.com/vuln/422691
- https://vuldb.com/vuln/422691/cti

### [CVE-2026-113595](https://github.com/Sharkord/sharkord/blob/v0.0.25/apps/server/src/routers/others/change-logo.ts)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-113595
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-21 01:17:08 JST
- 更新日: 2026-10-21 05:11:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Sharkord before 0.0.26 contains a missing authorization vulnerability in the others.changeLogo tRPC mutation that allows any authenticated member to modify the server logo without the MANAGE_SETTINGS permission. Attackers can remove the current logo and replace it with an uploaded image that is published to every conne...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Sharkord/sharkord/blob/v0.0.25/apps/server/src/routers/others/change-logo.ts
- https://github.com/Sharkord/sharkord/commit/fd15061eaf366c7150325780a2d7b4b452f1134f
- https://github.com/Sharkord/sharkord/issues/387
- https://github.com/Sharkord/sharkord/issues/851
- https://github.com/Sharkord/sharkord/releases/tag/v0.0.26

### [CVE-2026-113597](https://github.com/blinkospace/blinko/blob/1.8.8/server/routerTrpc/tag.ts)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-113597
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-21 01:17:08 JST
- 更新日: 2026-10-21 05:11:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Blinko through 1.8.8 contains an insecure direct object reference vulnerability in the tag tRPC router that allows authenticated users to read and modify other users' tags by supplying arbitrary tag IDs. Attackers can enumerate sequential IDs via fullTagNameById, updateTagIcon, and updateTagOrder to reveal private note...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/blinkospace/blinko/blob/1.8.8/server/routerTrpc/tag.ts
- https://github.com/blinkospace/blinko/issues/1112
- https://github.com/blinkospace/blinko/pull/1171
- https://www.vulncheck.com/advisories/blinko-through-1.8.8-idor-via-tag-trpc-router-procedures

### [CVE-2026-113867](https://bugzilla.mozilla.org/show_bug.cgi?id=2080073)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-113867
- 関連キーワード: go, echo
- 影響製品: -
- 公開日: 2026-10-21 05:17:19 JST
- 更新日: 2026-10-21 05:17:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Thunderbird did not escape attribute values when serializing outgoing XMPP stanzas. Because values from incoming requests were echoed back in automatic replies, a remote XMPP user could send a crafted request that caused Thunderbird to inject arbitrary stanzas into the user's connection, which the server would then pro...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://bugzilla.mozilla.org/show_bug.cgi?id=2080073
- https://www.mozilla.org/security/advisories/mfsa2026-114/
- https://www.mozilla.org/security/advisories/mfsa2026-115/

### [CVE-2026-86413](https://curl.se/docs/CVE-2026-86413.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-86413
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-21 05:17:25 JST
- 更新日: 2026-10-21 05:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: When using an *ambient user* in a first transfer doing Negotiate authentication and asked to follow redirects, curl could pass on its credential details to an unrelated second origin when asked to redirect there.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://curl.se/docs/CVE-2026-86413.html
- https://curl.se/docs/CVE-2026-86413.json
- https://hackerone.com/reports/3993549

### [CVE-2026-113613](https://github.com/Flexget/Flexget/blob/v3.20.6/flexget/components/archives/decompress.py#L74-L77)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-113613
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-21 01:17:11 JST
- 更新日: 2026-10-21 05:11:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FlexGet before 3.20.7 contains a path traversal vulnerability in the decompress plugin that allows remote attackers to write arbitrary files by supplying malicious archive member paths. Attackers can deliver zip or rar archives with ../ sequences or absolute paths through a feed, writing Python files into the plugins d...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/Flexget/Flexget/blob/v3.20.6/flexget/components/archives/decompress.py#L74-L77
- https://github.com/Flexget/Flexget/commit/38fa748461e20befee942f5c79d8a098edea5c1f
- https://github.com/Flexget/Flexget/releases/tag/v3.20.7
- https://github.com/Flexget/Flexget/security/advisories/GHSA-6v57-v478-59v9
- https://www.vulncheck.com/advisories/flexget-before-3.20.7-path-traversal-zip-slip-via-decompress-plugin

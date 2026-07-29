# Backend CVE Summary (2026-07-30)

## Overview

- 取得日時: 2026-07-30 08:09:26 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 20
- Critical: 3
- High: 6
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-54680](https://github.com/kube-logging/logging-operator/commit/cf437d7f1e056c78740bf5716ac8bdebcf002425)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-54680
- 関連キーワード: go, gin, kubernetes
- 影響製品: -
- 公開日: 2026-07-30 02:16:52 JST
- 更新日: 2026-07-30 02:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: KubernetesのLogging operatorで、Fluentd設定においてCRD文字列をエスケープせずに直接書き込む問題により、Flowリソース作成者が任意コマンドを実行可能になる脆弱性。
- 影響: Fluentd集約器内で任意のコマンドが実行される可能性がある。
- 推奨対応: バージョン6.6.0以降にアップデートすること。

#### References
- https://github.com/kube-logging/logging-operator/commit/cf437d7f1e056c78740bf5716ac8bdebcf002425
- https://github.com/kube-logging/logging-operator/releases/tag/6.6.0
- https://github.com/kube-logging/logging-operator/security/advisories/GHSA-mjqf-28ph-426h

### [CVE-2026-67192](https://www.vulncheck.com/advisories/xlight-ftp-server-pre-auth-stack-buffer-overflow-via-ssh-gcm-cipher)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-67192
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-30 01:17:57 JST
- 更新日: 2026-07-30 05:17:11 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Xlight FTP Server 3.9.5未満で、GCM暗号交渉時に不正なSSHパケットを送信することで認証前にスタックバッファオーバーフローが発生する脆弱性。
- 影響: 認証前にリモートコード実行が可能になる恐れがある。
- 推奨対応: バージョン3.9.5以降にアップデートすること。

#### References
- https://www.vulncheck.com/advisories/xlight-ftp-server-pre-auth-stack-buffer-overflow-via-ssh-gcm-cipher
- https://www.xlightftpd.com/whatsnew.htm

### [CVE-2026-54693](https://github.com/zitadel/zitadel/commit/90f310212d3a5075084a603bf61fed549c92956d)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-54693
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-30 02:16:53 JST
- 更新日: 2026-07-30 03:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ZITADELのメール・電話番号自己管理APIで、必要な権限なしに検証コードを要求できる問題により、他人のメールや電話番号を不正に所有できる脆弱性。
- 影響: メールや電話番号の所有権を不正に主張し、セキュリティポリシーを回避される可能性がある。
- 推奨対応: バージョン3.4.11および4.15.1以降にアップデートすること。

#### References
- https://github.com/zitadel/zitadel/commit/90f310212d3a5075084a603bf61fed549c92956d
- https://github.com/zitadel/zitadel/commit/a1748b2f0326ddf7be0de44b4f980ae2c07c0151
- https://github.com/zitadel/zitadel/commit/ed09b3df7f43e870423e4d8f2757e6894481604f
- https://github.com/zitadel/zitadel/releases/tag/v3.4.11
- https://github.com/zitadel/zitadel/releases/tag/v4.15.1

### [CVE-2026-59247](https://cna.erlef.org/cves/CVE-2026-59247.html)

> **Backend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-59247
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-30 00:16:26 JST
- 更新日: 2026-07-30 01:17:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Gleamで依存関係解決時に署名検証済みリポジトリのメタデータと異なる未署名APIレスポンスを使用するため、中間者攻撃により偽造パッケージ内容が注入される可能性がある。
- 影響: 中間者攻撃により依存パッケージの改ざんが可能になる恐れがある。
- 推奨対応: 詳細な対策は不明だが、信頼できる通信経路の確保を検討すること。

#### References
- https://cna.erlef.org/cves/CVE-2026-59247.html
- https://github.com/gleam-lang/gleam/commit/c9c0d48c123c8abae6db8dd61b25ccb427ed3d35
- https://github.com/gleam-lang/gleam/security/advisories/GHSA-4vvc-458m-r82g
- https://github.com/hexpm/specifications/blob/main/registry-v2.md
- https://osv.dev/vulnerability/EEF-CVE-2026-59247

### [CVE-2026-67437](https://github.com/OliveTin/OliveTin/commit/ec114e95d297b806c3ca0c37bc139b3c9c517b3f)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-67437
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-30 06:17:47 JST
- 更新日: 2026-07-30 06:17:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OliveTinのOAuth2ログイン処理で、状態管理マップのエントリが期限切れや削除されずに蓄積され、未認証者によるメモリ枯渇とサービス拒否を引き起こす脆弱性。
- 影響: メモリ枯渇によるサービス拒否が発生する可能性がある。
- 推奨対応: バージョン3000.17.0以降にアップデートすること。

#### References
- https://github.com/OliveTin/OliveTin/commit/ec114e95d297b806c3ca0c37bc139b3c9c517b3f
- https://github.com/OliveTin/OliveTin/releases/tag/3000.17.0
- https://github.com/OliveTin/OliveTin/security/advisories/GHSA-xpxj-f2fm-rqch

### [CVE-2026-54078](https://github.com/veraPDF/veraPDF-validation/commit/94caa46c1a594512247fbd46c808edae39469542)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-54078
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-30 01:17:53 JST
- 更新日: 2026-07-30 04:16:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: veraPDF-validationで、悪意あるPDFのリッチテキストエントリによりXML外部実体参照(XXE)が発生し、ローカルファイル内容が検証レポートに反映される脆弱性。
- 影響: ローカルファイルの内容漏洩が発生する可能性がある。
- 推奨対応: バージョン1.30.2および1.31.71以降にアップデートすること。

#### References
- https://github.com/veraPDF/veraPDF-validation/commit/94caa46c1a594512247fbd46c808edae39469542
- https://github.com/veraPDF/veraPDF-validation/commit/cacd9436d0de40b0e58cc7d2dbb06451619e61ec
- https://github.com/veraPDF/veraPDF-validation/pull/730
- https://github.com/veraPDF/veraPDF-validation/security/advisories/GHSA-3jh7-wm29-q568

### [CVE-2026-15831](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-1-released/)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-15831
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-30 05:17:01 JST
- 更新日: 2026-07-30 05:17:01 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: GitLab EEで認証済みユーザーがトークン生成時の認可不備により管理者設定のツールガバナンスポリシーを回避できる可能性がある問題。
- 影響: 管理者設定のポリシーが回避される恐れがある。
- 推奨対応: バージョン19.1.3および19.2.1以降にアップデートすること。

#### References
- https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-1-released/
- https://gitlab.com/gitlab-org/gitlab/-/work_items/605484

### [CVE-2026-64560](https://git.kernel.org/stable/c/920f893f735e92ba3a1cd9256899a186b161928d)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-64560
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-30 02:16:53 JST
- 更新日: 2026-07-30 02:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxカーネルのposix-cpu-timersで、非リーダーexec()の競合によりUse-After-Freeが発生する可能性がある問題が修正された。
- 影響: Use-After-Freeにより予期しない動作やクラッシュが発生する恐れがある。
- 推奨対応: 最新のLinuxカーネルにアップデートすること。

#### References
- https://git.kernel.org/stable/c/920f893f735e92ba3a1cd9256899a186b161928d
- https://git.kernel.org/stable/c/ad1cafa1bdaa71da85d71cac053838bbe97852b6

### [CVE-2026-67438](https://github.com/OliveTin/OliveTin/commit/995ff79736f2bccc364448a3ece84087b550b232)

> **Backend** / **MEDIUM** / CVSS: **6.6** / KEV: **no**

- タイトル: CVE-2026-67438
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-30 06:17:48 JST
- 更新日: 2026-07-30 06:17:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OliveTinで正規表現カスタム引数が安全でないと判定されず、シェルコマンドに埋め込まれOSコマンドインジェクションが可能になる脆弱性。
- 影響: OSコマンドインジェクションにより任意コマンド実行の恐れがある。
- 推奨対応: バージョン3000.17.0以降にアップデートすること。

#### References
- https://github.com/OliveTin/OliveTin/commit/995ff79736f2bccc364448a3ece84087b550b232
- https://github.com/OliveTin/OliveTin/releases/tag/3000.17.0
- https://github.com/OliveTin/OliveTin/security/advisories/GHSA-xc5w-4v5w-7x65

### [CVE-2026-67439](https://github.com/OliveTin/OliveTin/commit/e421780c9885aa5024d2f47b4ed4898f2f18eb90)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-67439
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-30 06:17:48 JST
- 更新日: 2026-07-30 06:17:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OliveTinでログ出力閲覧権限を持たないユーザーが、実行権限のみでアクションのログを閲覧可能な問題。
- 影響: 権限外のログ情報が漏洩する可能性がある。
- 推奨対応: バージョン3000.17.0以降にアップデートすること。

#### References
- https://github.com/OliveTin/OliveTin/commit/e421780c9885aa5024d2f47b4ed4898f2f18eb90
- https://github.com/OliveTin/OliveTin/releases/tag/3000.17.0
- https://github.com/OliveTin/OliveTin/security/advisories/GHSA-jm28-2wcr-qf3h

### [CVE-2026-67436](https://github.com/Linuxfabrik/monitoring-plugins/commit/ffb0a81308cbfc018da857a89e0d07a67bf89fc3)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-67436
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-07-30 05:17:12 JST
- 更新日: 2026-07-30 05:17:12 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxfabrik monitoring-pluginsのredfish-*プラグインが、BMCからの悪意あるリダイレクトにより認証済みRedfishリクエストの認証情報を漏洩する可能性がある。
- 影響: X-Auth-TokenやHTTP Basic認証情報が不正に取得される恐れがある。
- 推奨対応: バージョン6.0.0以降にアップデートすることを推奨。

#### References
- https://github.com/Linuxfabrik/monitoring-plugins/commit/ffb0a81308cbfc018da857a89e0d07a67bf89fc3
- https://github.com/Linuxfabrik/monitoring-plugins/security/advisories/GHSA-96fx-pqc3-28xv

### [CVE-2026-46678](https://github.com/pydantic/pydantic-ai/releases/tag/v1.99.0)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-46678
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-30 06:17:47 JST
- 更新日: 2026-07-30 06:17:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Pydantic AIでforce_download='allow-local'を使用した場合、IPv6変換形式を使ったクラウドメタデータIPのブロック回避により短期認証情報が漏洩する可能性がある。
- 影響: クラウドIAMの短期認証情報が漏洩する恐れがあるが、特定の設定と条件下でのみ影響。
- 推奨対応: 信頼できない入力に対してforce_download='allow-local'を安易に使用しないこと。

#### References
- https://github.com/pydantic/pydantic-ai/releases/tag/v1.99.0
- https://github.com/pydantic/pydantic-ai/security/advisories/GHSA-cqp8-fcvh-x7r3

### [CVE-2026-54249](https://github.com/pydantic/pydantic-ai/security/advisories/GHSA-h7p7-w5gc-xj3w)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-54249
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-30 06:17:47 JST
- 更新日: 2026-07-30 06:17:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Pydantic AIのUIアダプターで、検証されていないUploadedFile参照によりサーバー側のファイルが不正に読み取られる可能性がある。
- 影響: 攻撃者がサーバーや他テナントのファイルにアクセスできる恐れがあるが、有効なファイル識別子が必要。
- 推奨対応: 信頼できないファイル識別子の取り扱いに注意し、最新バージョンへの更新を検討。

#### References
- https://github.com/pydantic/pydantic-ai/security/advisories/GHSA-h7p7-w5gc-xj3w

### [CVE-2026-65975](https://github.com/pydantic/pydantic-ai/security/advisories/GHSA-jpr8-2v3g-wgf9)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-65975
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-30 06:17:47 JST
- 更新日: 2026-07-30 06:17:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Pydantic AIのUIアダプターで、クライアントから送信された未解決ツール呼び出しが誤って実行される可能性がある。
- 影響: 本来実行されるべきでないツール呼び出しが実行される恐れがある。
- 推奨対応: 影響バージョンを避け、修正済みバージョンにアップデートすることを推奨。

#### References
- https://github.com/pydantic/pydantic-ai/security/advisories/GHSA-jpr8-2v3g-wgf9

### [CVE-2026-67433](https://github.com/Linuxfabrik/monitoring-plugins/commit/6df1f574aa9dc6541e092f1ce482ecc1315cded0)

> **Backend** / **MEDIUM** / CVSS: **5.8** / KEV: **no**

- タイトル: CVE-2026-67433
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-07-30 05:17:12 JST
- 更新日: 2026-07-30 05:17:12 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Linuxfabrik monitoring-pluginsのログファイルチェックで、/tmpの予測可能なパスにシンボリックリンクを設置され、root権限でのチェック時に任意のファイルが操作される可能性がある。
- 影響: ローカルユーザーによる権限昇格やファイル操作のリスクがある。
- 推奨対応: 最新バージョンへのアップデートや適切なファイル権限管理を推奨。

#### References
- https://github.com/Linuxfabrik/monitoring-plugins/commit/6df1f574aa9dc6541e092f1ce482ecc1315cded0
- https://github.com/Linuxfabrik/monitoring-plugins/security/advisories/GHSA-w2gg-hx6w-24w3

### [CVE-2026-67435](https://github.com/Linuxfabrik/lib/commit/6573ff9347e541200305d278d2663d2e54e052ff)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-67435
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-07-30 05:17:12 JST
- 更新日: 2026-07-30 06:17:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: linuxfabrik-libのlib.url.fetch()がクロスオリジンリダイレクト時に認証ヘッダーを送信し、悪意あるサーバーに認証情報が漏洩する可能性がある。
- 影響: X-Auth-Tokenなどの認証情報が不正に取得される恐れがある。
- 推奨対応: バージョン6.0.0以降に更新することを推奨。

#### References
- https://github.com/Linuxfabrik/lib/commit/6573ff9347e541200305d278d2663d2e54e052ff
- https://github.com/Linuxfabrik/lib/releases/tag/v6.0.0
- https://github.com/Linuxfabrik/monitoring-plugins/security/advisories/GHSA-4jc5-g844-4x33

### [CVE-2026-62995](https://github.com/authlib/joserfc/security/advisories/GHSA-5jhw-7jv7-qcqq)

> **Backend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-62995
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-07-30 04:16:50 JST
- 更新日: 2026-07-30 04:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: joserfcライブラリがJOSE仕様に準拠しないJWTのトレーリングパディングを許容し、JWTの改変が可能となる問題がある。
- 影響: トークンの取り消しやリプレイ防止機能の回避につながる可能性がある。
- 推奨対応: バージョン1.7.2以降に更新し、JWTの取り扱いに注意すること。

#### References
- https://github.com/authlib/joserfc/security/advisories/GHSA-5jhw-7jv7-qcqq

### [CVE-2026-54574](https://github.com/termux/proot-distro/commit/a96d7a9667f38e45d812614852ee3915d1c0ae45)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-54574
- 関連キーワード: gin, docker
- 影響製品: -
- 公開日: 2026-07-30 02:16:52 JST
- 更新日: 2026-07-30 05:17:04 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: proot-distroの古いバージョンで、tarアーカイブ内のシンボリックリンク検証が不十分であり、悪意あるアーカイブによりホストファイルシステムへの書き込みが可能となる。
- 影響: ホストシステムのファイル改ざんや不正書き込みのリスクがある。
- 推奨対応: バージョン5.1.5以降にアップデートすることを推奨。

#### References
- https://github.com/termux/proot-distro/commit/a96d7a9667f38e45d812614852ee3915d1c0ae45
- https://github.com/termux/proot-distro/releases/tag/v5.1.5
- https://github.com/termux/proot-distro/security/advisories/GHSA-9xq3-3fqg-4vg7
- https://github.com/termux/proot-distro/security/advisories/GHSA-9xq3-3fqg-4vg7

### [CVE-2025-67406](https://github.com/um-dsp/TaintRadar/blob/main/sql_injection_cves/advocate/20250811-advocate-office-management-system-activate_case.php-id-sqli/20250811-advocate-office-management-system-activate_case.php-id-sqli.md)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2025-67406
- 関連キーワード: mysql
- 影響製品: -
- 公開日: 2026-07-30 07:16:51 JST
- 更新日: 2026-07-30 07:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Advocate office management system 1.0のactivate_case.phpのidパラメータにSQLインジェクションの脆弱性が存在する可能性がある。
- 影響: 不正なSQLクエリによりデータ漏洩や任意コード実行のリスクがある可能性がある。
- 推奨対応: 入力値の適切な検証とサニタイズを行い、脆弱性の修正を検討すること。

#### References
- https://github.com/um-dsp/TaintRadar/blob/main/sql_injection_cves/advocate/20250811-advocate-office-management-system-activate_case.php-id-sqli/20250811-advocate-office-management-system-activate_case.php-id-sqli.md

### [CVE-2026-65887](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-65887
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-07-30 00:16:28 JST
- 更新日: 2026-07-30 00:16:28 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: JoomlaのGridbox拡張機能で、認証なしに任意ユーザーパスワードをリセットできる脆弱性が存在する（スーパ管理者は除く）。
- 影響: 攻撃者が他ユーザーとしてログインし、不正操作が可能となる恐れがある。
- 推奨対応: バージョン2.20.2以降に更新し、パスワードリセット機能の安全性を確保すること。

#### References
- https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/
- https://www.balbooa.com/gridbox

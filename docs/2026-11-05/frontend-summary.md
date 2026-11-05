# Frontend CVE Summary (2026-11-05)

## Overview

- 取得日時: 2026-11-05 11:18:45 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 16
- Critical: 1
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-63655](https://github.com/tsparticles/tsparticles/commit/25fb70e7f527a91568adaef576570289083f243b)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-63655
- 関連キーワード: typescript, node.js, docker
- 影響製品: -
- 公開日: 2026-11-05 07:18:07 JST
- 更新日: 2026-11-05 07:18:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: @tsparticles/mcp-serverのHTTPモードにおいて、リクエストボディの累積サイズ制限を行わずにメモリへ蓄積する問題。
- 影響: 遠隔の攻撃者が巨大なデータを送信することでNode.jsのメモリを枯渇させ、サービス拒否（DoS）を引き起こす可能性があります。
- 推奨対応: バージョン 4.3.1 以降へアップデートしてください。

#### References
- https://github.com/tsparticles/tsparticles/commit/25fb70e7f527a91568adaef576570289083f243b
- https://github.com/tsparticles/tsparticles/commit/7b3a9488d4201fe9ddd5fec05f4a2ae65d3627ea
- https://github.com/tsparticles/tsparticles/pull/5875
- https://github.com/tsparticles/tsparticles/releases/tag/v4.3.1
- https://github.com/tsparticles/tsparticles/security/advisories/GHSA-447x-qqwf-m7xq

### [CVE-2026-76893](https://github.com/tsparticles/tsparticles/commit/d3b5672bd61bb847abfa21193c34eabf7aba6896)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-76893
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-11-05 07:18:07 JST
- 更新日: 2026-11-05 07:18:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: @tsparticles/mcp-serverのHTTPモードにおいて、単一のStreamableHTTPServerTransportが全クライアント間で再利用される問題。
- 影響: 未認証のクライアントが初期化リクエストを送信して状態を占有することで、他のクライアントがプロセス再起動まで接続できなくなる可能性があります。
- 推奨対応: バージョン 4.3.2 以降へアップデートしてください。

#### References
- https://github.com/tsparticles/tsparticles/commit/d3b5672bd61bb847abfa21193c34eabf7aba6896
- https://github.com/tsparticles/tsparticles/pull/5888
- https://github.com/tsparticles/tsparticles/security/advisories/GHSA-h7c4-q426-7jh9

### [CVE-2026-121747](https://github.com/nvm-sh/nvm/commit/67268ebcb6e1a26ae3d71b3710d6333bb7358662)

> **Frontend** / **MEDIUM** / CVSS: **6.7** / KEV: **no**

- タイトル: CVE-2026-121747
- 関連キーワード: npm, gin, node.js
- 影響製品: -
- 公開日: 2026-11-05 07:17:54 JST
- 更新日: 2026-11-05 07:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Node Version Manager (nvm) において、.nvmrc ファイルがシンボリックリンクであるかの検証が行われない問題。
- 影響: 悪意のあるシンボリックリンクを含むリポジトリでコマンドが実行されると、リンク先のファイル内容がエラー出力等に表示され、機密情報が漏洩する可能性があります。
- 推奨対応: 信頼できないリポジトリでの使用を避けるか、最新の修正状況を確認し対策版を利用してください。

#### References
- https://github.com/nvm-sh/nvm/commit/67268ebcb6e1a26ae3d71b3710d6333bb7358662
- https://github.com/nvm-sh/nvm/commit/c314f1cbb3c301c587a4e4f96511d31f1134ffd1
- https://github.com/nvm-sh/nvm/security/advisories/GHSA-j6ch-mq5c-3h4x

### [CVE-2026-121749](https://github.com/nvm-sh/nvm/commit/bce663e3873fadbe8ebbc6e07e8d76fb12d5d69e)

> **Frontend** / **MEDIUM** / CVSS: **4.6** / KEV: **no**

- タイトル: CVE-2026-121749
- 関連キーワード: npm, gin, node.js
- 影響製品: -
- 公開日: 2026-11-05 07:17:54 JST
- 更新日: 2026-11-05 07:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Node Version Manager (nvm) において、.nvmrc のバージョン指定文字列が grep にフラグなしで渡される問題。
- 影響: ハイフンで始まる悪意のある文字列によって grep オプションが誤認識され、ローカルファイルの内容が読み取られて外部ログやミラーへ漏洩する可能性があります。
- 推奨対応: 影響を受けるバージョン（0.5.0〜0.40.8）の使用を避け、修正版へ更新してください。

#### References
- https://github.com/nvm-sh/nvm/commit/bce663e3873fadbe8ebbc6e07e8d76fb12d5d69e
- https://github.com/nvm-sh/nvm/security/advisories/GHSA-xmxw-6r9w-89gc

### [CVE-2026-121748](https://github.com/nvm-sh/nvm/commit/4049296ca8eef2067517d8cfd5ef5c0e615daa10)

> **Frontend** / **LOW** / CVSS: **3.6** / KEV: **no**

- タイトル: CVE-2026-121748
- 関連キーワード: npm, gin, node.js
- 影響製品: -
- 公開日: 2026-11-05 07:17:54 JST
- 更新日: 2026-11-05 07:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Node Version Manager (nvm) において、.npmrc に prefix が設定されている際の削除処理で意図しないファイルが指定される問題。
- 影響: ~/.bashrc などの重要ファイルが誤って上書き・破損されたり、共有環境で権限設定が不用意に変更されたりする可能性があります。
- 推奨対応: バージョン 0.41.0 以降へアップデートしてください。

#### References
- https://github.com/nvm-sh/nvm/commit/4049296ca8eef2067517d8cfd5ef5c0e615daa10
- https://github.com/nvm-sh/nvm/security/advisories/GHSA-ccgf-7gv4-xg5h

### [CVE-2026-121750](https://github.com/nvm-sh/nvm/commit/1f99e4c20bb92c5737b92512446acf8e303b1edd)

> **Frontend** / **LOW** / CVSS: **3.1** / KEV: **no**

- タイトル: CVE-2026-121750
- 関連キーワード: npm, gin, node.js
- 影響製品: -
- 公開日: 2026-11-05 07:17:54 JST
- 更新日: 2026-11-05 07:17:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Node Version Manager (nvm) において、チェックサム検証に失敗したアーカイブがキャッシュに残存する問題。
- 影響: 検証失敗後に nvm install --offline を実行すると、不正または破損したアーカイブが検証なしでインストールされ、コード実行に繋がる可能性があります。
- 推奨対応: バージョン 0.41.0 以降へアップデートしてください。

#### References
- https://github.com/nvm-sh/nvm/commit/1f99e4c20bb92c5737b92512446acf8e303b1edd
- https://github.com/nvm-sh/nvm/security/advisories/GHSA-262q-c465-prmr

### [CVE-2026-107846](https://github.com/bitcoinjs/bitcoinjs-lib/commit/009f165edfbf925cad8964b2dce478d18dd19449)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-107846
- 関連キーワード: javascript, gin, node.js
- 影響製品: -
- 公開日: 2026-11-05 04:17:18 JST
- 更新日: 2026-11-05 04:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: bitcoinjs-lib において、Merkleツリー計算時に隣接する重複ハッシュの検証が不十分な問題。
- 影響: 攻撃者が重複トランザクションを挿入しても同一のMerkleルートが生成され、二重処理やブロック拒否などの不整合を引き起こす可能性があります。
- 推奨対応: 修正済みバージョン（5.2.1、6.1.8、7.0.2 以降など）へアップデートしてください。

#### References
- https://github.com/bitcoinjs/bitcoinjs-lib/commit/009f165edfbf925cad8964b2dce478d18dd19449
- https://github.com/bitcoinjs/bitcoinjs-lib/commit/b79c7714c0687473dc6e25c69fc5fc597302c7a0
- https://github.com/bitcoinjs/bitcoinjs-lib/commit/f3434d1e4bb5e0784fe769c4cd08a243576232a1
- https://github.com/bitcoinjs/bitcoinjs-lib/security/advisories/GHSA-8vv3-6qpc-gpw6

### [CVE-2026-119746](https://assets.belden.com/asset/3be80067-b211-423d-9be4-4e31bd43fbc9/PSIRT-9-Login-Lockout-Resets-in-ICX35.pdf)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-119746
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-11-05 01:17:45 JST
- 更新日: 2026-11-05 04:17:25 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ProSoft Technology ICX35 デバイスのWeb管理画面において、アカウントロックアウト機能がクライアント側JavaScriptのみで制御されている問題。
- 影響: 攻撃者がクッキーを削除することで認証試行制限を回避し、ブルートフォース攻撃を継続できる可能性があります。
- 推奨対応: ファームウェアバージョン 1.14.158 以降へ更新してください。

#### References
- https://assets.belden.com/asset/3be80067-b211-423d-9be4-4e31bd43fbc9/PSIRT-9-Login-Lockout-Resets-in-ICX35.pdf
- https://www.vulncheck.com/advisories/prosoft-icx35-login-lockout-bypass-via-client-side-cookies

### [CVE-2026-57567](https://github.com/readest/readest/commit/4025c4d7b52c8c174ec1d4c02c2a864cce249604)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-57567
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-11-05 07:18:07 JST
- 更新日: 2026-11-05 07:18:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Readest のデスクトップ向けTauriビルドにおいて、ファイル入出力コマンドのパス検証およびトラバーサル対策が不十分な問題。
- 影響: アプリ内で悪意あるJavaScriptが実行された場合、プロセスの権限範囲内で任意のファイルが読み取られたり書き換えられたりする可能性があります。
- 推奨対応: バージョン 0.11.10 以降へアップデートしてください。

#### References
- https://github.com/readest/readest/commit/4025c4d7b52c8c174ec1d4c02c2a864cce249604
- https://github.com/readest/readest/commit/446c2c72de198de2dfcd63589f549ca517961d15
- https://github.com/readest/readest/pull/4639
- https://github.com/readest/readest/pull/4651
- https://github.com/readest/readest/releases/tag/v0.11.10

### [CVE-2026-102345](https://github.com/zammad/zammad/commit/fe8fb9bd6c61f9136c93ef00cc08904bca0edecc)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-102345
- 関連キーワード: vue
- 影響製品: -
- 公開日: 2026-11-05 04:17:17 JST
- 更新日: 2026-11-05 04:17:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Zammad is a web based open source helpdesk/customer support system. Prior to 7.1.2, the new Vue-based ticket interface can render ticket article content without the expected output encoding. An authenticated user can store markup in an article that is interpreted when another user views the ticket, enabling stored cros...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/zammad/zammad/commit/fe8fb9bd6c61f9136c93ef00cc08904bca0edecc
- https://github.com/zammad/zammad/security/advisories/GHSA-4x3x-65c5-8hx4

### [CVE-2026-54380](https://github.com/je-lv/vitafit-security-research)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-54380
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-05 07:18:06 JST
- 更新日: 2026-11-05 07:18:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: VitaFit クラウドAPIにおいて、SVG画像のアップロード時にスクリプト実行制限や適切なレスポンスヘッダー処理が欠けている問題。
- 影響: 認証された攻撃者が悪意のあるJavaScriptを含むSVGを配置し、被害者が直接閲覧した際に格納型クロスサイトスクリプティング（XSS）が実行される可能性があります。
- 推奨対応: 2026-10-30 以降の修正済みAPI環境を適用してください。

#### References
- https://github.com/je-lv/vitafit-security-research
- https://play.google.com/store/apps/details?id=com.vt.vitafit
- https://www.vulncheck.com/advisories/vitafit-cloud-api-stored-xss-via-svg-file-upload

### [CVE-2025-71453](https://0xbro.red/posts/vtenext-25-02-a-three-way-path-to-rce/)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2025-71453
- 関連キーワード: javascript, echo
- 影響製品: -
- 公開日: 2026-11-05 06:17:39 JST
- 更新日: 2026-11-05 06:17:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: vtenext before 25.02.2 contains a reflected cross-site scripting vulnerability in modules/Home/HomeWidgetBlockList.php that echoes unsanitized widgetId keys from the widgetInfoList JSON parameter. Attackers can induce a logged-in user to submit a crafted POST request with HTML in widgetId keys, executing JavaScript in...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://0xbro.red/posts/vtenext-25-02-a-three-way-path-to-rce/
- https://blog.sicuranext.com/vtenext-25-02-a-three-way-path-to-rce/
- https://usermanual.vtenext.com/books/release-notes-history/page/vtenext-25022-release-note
- https://www.vulncheck.com/advisories/vtenext-before-25.02.2-reflected-xss-via-widgetinfolist-in-homewidgetblocklist

### [CVE-2026-120421](https://gitlab.eclipse.org/security/cve-assignment/-/work_items/536)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-120421
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-05 00:17:41 JST
- 更新日: 2026-11-05 05:19:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In Eclipse Mojarra versions 2.2.0 through 4.0.28, 4.1.0 through 4.1.19, and 5.0.0-M1 through 5.0.0-M11, when URL client window mode is enabled (`jakarta.faces.CLIENT_WINDOW_MODE=url`), the client window id from the `jfwid` or `jakarta.faces.ClientWindow` request parameter is appended to generated URLs without URL-encod...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://gitlab.eclipse.org/security/cve-assignment/-/work_items/536
- https://gitlab.eclipse.org/security/vulnerability-reports/-/work_items/1332

### [CVE-2026-121008](https://github.com/dbsrgits/sql-abstract/commit/85a75fcde3e09da5181dee07a4eccba76ad94305.patch)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-121008
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-11-05 00:17:41 JST
- 更新日: 2026-11-05 00:17:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SQL::Abstract::Tree versions before 2.000001_04 for Perl allow cross-site scripting via unescaped SQL text and bind values in the html profile. The html profile wraps keywords and placeholders in span elements and breaks lines with br elements, so its output is meant to go into a page as is. The format method does not...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dbsrgits/sql-abstract/commit/85a75fcde3e09da5181dee07a4eccba76ad94305.patch
- https://metacpan.org/release/GETTY/SQL-Abstract-2.000001_04/changes

### [CVE-2026-122016](https://github.com/yangzongzhuan/RuoYi-Vue/)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-122016
- 関連キーワード: vue
- 影響製品: -
- 公開日: 2026-11-05 07:17:55 JST
- 更新日: 2026-11-05 07:17:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: A vulnerability was determined in yangzongzhuan RuoYi-Vue up to 3.9.2. This issue affects the function SysPermissionService.getMenuPermission of the file SysPermissionService.java of the component Permission Service. This manipulation of the argument perms causes improper privilege management. The attack may be initiat...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/yangzongzhuan/RuoYi-Vue/
- https://github.com/yangzongzhuan/RuoYi-Vue/issues/206
- https://vuldb.com/cve/CVE-2026-122016
- https://vuldb.com/submit/1024636
- https://vuldb.com/vuln/431084

### [CVE-2026-121632](https://github.com/gshank/data-muform/pull/18)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-121632
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-11-05 00:17:42 JST
- 更新日: 2026-11-05 04:17:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Data::MuForm versions through 0.05 for Perl render attribute values and option labels into HTML without escaping. process_attrs writes each attribute value into the markup as is. The select, radio group and checkbox group renderers pass each option to it, so an option's value becomes an unescaped attribute. Option and...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gshank/data-muform/pull/18
- https://metacpan.org/release/GSHANK/Data-MuForm-0.05/source/lib/Data/MuForm/Renderer/Base.pm#L202-228
- http://www.openwall.com/lists/oss-security/2026/11/04/4

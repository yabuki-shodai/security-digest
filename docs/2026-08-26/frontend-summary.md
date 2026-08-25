# Frontend CVE Summary (2026-08-26)

## Overview

- 取得日時: 2026-08-26 07:39:48 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 0
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-55571](https://github.com/djust-org/djust/commit/1ae8aa9246b80477de7ddc4d90319a3b267bef04)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-55571
- 関連キーワード: react, django, go, gin
- 影響製品: -
- 公開日: 2026-08-26 02:17:32 JST
- 更新日: 2026-08-26 03:17:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Django向けLiveViewライブラリ「djust」において、接続拒否時にWebSocketを正しく閉じない不具合。
- 影響: 未認証のクライアントが接続を保持し、認証なしでイベントハンドラーを実行して機密データの閲覧や変更を行う可能性がある。
- 推奨対応: djust を 1.0.4 以降のバージョンへ更新する。

#### References
- https://github.com/djust-org/djust/commit/1ae8aa9246b80477de7ddc4d90319a3b267bef04
- https://github.com/djust-org/djust/pull/1780
- https://github.com/djust-org/djust/releases/tag/v1.0.4
- https://github.com/djust-org/djust/security/advisories/GHSA-xx4j-w367-7247
- https://github.com/djust-org/djust/security/advisories/GHSA-xx4j-w367-7247

### [CVE-2026-55637](https://github.com/GeiserX/genieacs-mcp/commit/577306d78190622eee97e362b042a69499ef373f)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-55637
- 関連キーワード: npm, go, gin
- 影響製品: -
- 公開日: 2026-08-26 03:17:56 JST
- 更新日: 2026-08-26 04:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: GenieACS向けMCPサーバー「genieacs-mcp」におけるHost/Originヘッダーの検証不足および未認証HTTPリスナーの生成不具合。
- 影響: 悪意のあるWebサイトからのDNSリバインディング攻撃により、CPE管理状態の変更や設定情報の閲覧・操作が行われる可能性がある。
- 推奨対応: genieacs-mcp を 0.3.2 以降のバージョンへ更新する。

#### References
- https://github.com/GeiserX/genieacs-mcp/commit/577306d78190622eee97e362b042a69499ef373f
- https://github.com/GeiserX/genieacs-mcp/pull/26
- https://github.com/GeiserX/genieacs-mcp/releases/tag/v0.3.2
- https://github.com/GeiserX/genieacs-mcp/security/advisories/GHSA-cmwv-wf9p-p8wx
- https://github.com/GeiserX/genieacs-mcp/security/advisories/GHSA-cmwv-wf9p-p8wx

### [CVE-2026-55663](https://github.com/versatica/mediasoup/commit/9c1a90a8f9206b965e727d134846fb42df4980a7)

> **Frontend** / **MEDIUM** / CVSS: **5.6** / KEV: **no**

- タイトル: CVE-2026-55663
- 関連キーワード: npm, echo
- 影響製品: -
- 公開日: 2026-08-26 04:16:51 JST
- 更新日: 2026-08-26 04:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WebRTCライブラリ「mediasoup」のSCTPスタックにおいて、状態クッキーの認証に固定のマジック値を使用している不具合。
- 影響: オンパス攻撃者によりCOOKIE-ECHOが偽造され、不正なSCTPアソシエーションが確立される可能性がある。
- 推奨対応: npmパッケージは 3.20.6 以降、Rust crateは 0.22.5 以降へ更新する。

#### References
- https://github.com/versatica/mediasoup/commit/9c1a90a8f9206b965e727d134846fb42df4980a7
- https://github.com/versatica/mediasoup/pull/1829
- https://github.com/versatica/mediasoup/releases/tag/3.20.6
- https://github.com/versatica/mediasoup/security/advisories/GHSA-p7x2-g5cq-fhmq
- https://github.com/versatica/mediasoup/security/advisories/GHSA-p7x2-g5cq-fhmq

### [CVE-2026-55099](https://github.com/collective/icalendar/commit/b6b2608ae3af6de40695b4e40f71847485aa0b49)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-55099
- 関連キーワード: vite, python, gin
- 影響製品: -
- 公開日: 2026-08-26 05:16:56 JST
- 更新日: 2026-08-26 06:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Python向けiCalendarライブラリ「icalendar」において、ネストされたコンポーネントの比較処理で計算量が爆発的に増大する不具合。
- 影響: 悪意を持って作成された小さな.icsファイルの比較処理により、CPUリソースが占有されサービス拒否（DoS）が発生する可能性がある。
- 推奨対応: icalendar を 7.1.3 以降のバージョンへ更新する。

#### References
- https://github.com/collective/icalendar/commit/b6b2608ae3af6de40695b4e40f71847485aa0b49
- https://github.com/collective/icalendar/commit/cad40cd112c93fd142ec12cc5b37445a849b8a79
- https://github.com/collective/icalendar/releases/tag/v7.1.3
- https://github.com/collective/icalendar/security/advisories/GHSA-cv84-9p8j-fj68
- http://www.openwall.com/lists/oss-security/2026/06/23/8

### [CVE-2026-55557](https://github.com/That1Drifter/browse-mcp/blob/v0.8.2/CHANGELOG.md#082---2026-06-13)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-55557
- 関連キーワード: playwright, gin
- 影響製品: -
- 公開日: 2026-08-26 02:17:32 JST
- 更新日: 2026-08-26 04:16:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ブラウザ操作MCPサーバー「browse-mcp」において、保存先パスの検証が不十分な不具合。
- 影響: 悪意のあるクライアントやプロンプトインジェクションにより任意のパスにファイルを出力され、ホスト上でコード実行につながる可能性がある。
- 推奨対応: browse-mcp を 0.8.2 以降のバージョンへ更新する。

#### References
- https://github.com/That1Drifter/browse-mcp/blob/v0.8.2/CHANGELOG.md#082---2026-06-13
- https://github.com/That1Drifter/browse-mcp/commit/5352a4a56f626254b445bfa07e4bb48c5aad15c1
- https://github.com/That1Drifter/browse-mcp/pull/58
- https://github.com/That1Drifter/browse-mcp/releases/tag/v0.8.2
- https://github.com/That1Drifter/browse-mcp/security/advisories/GHSA-m9mq-7m7q-xc6p

### [CVE-2026-74932](https://wpscan.com/vulnerability/f1eebb4a-cfd1-419e-852d-e5a949437afb/)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-74932
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-26 05:17:03 JST
- 更新日: 2026-08-26 05:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPressプラグイン「WP Fastest Cache」におけるHostヘッダーの検証不足およびキャッシュキーへの未含める不具合。
- 影響: 未認証の攻撃者によるWebキャッシュポイズニングが発生し、サイト訪問者のブラウザ上で任意のJavaScriptが実行される可能性がある。
- 推奨対応: WP Fastest Cache を 1.5.1 以降のバージョンへ更新する。

#### References
- https://wpscan.com/vulnerability/f1eebb4a-cfd1-419e-852d-e5a949437afb/

### [CVE-2026-80051](https://github.com/graphql-go/graphql/blob/v0.8.1/scalars.go#L307-L315)

> **Frontend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-80051
- 関連キーワード: graphql, go
- 影響製品: -
- 公開日: 2026-08-26 03:18:07 JST
- 更新日: 2026-08-26 05:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Go向けGraphQLライブラリ「github.com/graphql-go/graphql」におけるスカラ変数の型検証不足の不具合。
- 影響: 宣言と異なる型の入力や極度にネストされた値により、回復不能なスタックオーバーフロー（DoS）が引き起こされる可能性がある。
- 推奨対応: 最新版への修正適用、または受け取るパラメータのバリデーションを強化する。

#### References
- https://github.com/graphql-go/graphql/blob/v0.8.1/scalars.go#L307-L315
- https://www.openwall.com/lists/oss-security/2026/08/25/2

### [CVE-2026-79773](https://github.com/wintercms/winter/commit/e09c8d3526f3583cb6c3476a021b885088ecd4bd)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-79773
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-26 01:17:28 JST
- 更新日: 2026-08-26 02:18:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Winter CMSのJavascriptImporterフィルターにおけるローカルファイルインクルード（LFI）の脆弱性。
- 影響: 資産管理権限を持つユーザーがテーマ外の感傷的なファイル（.env等）を読み込み、未認証の外部ユーザーへ環境変数やDB認証情報が漏洩する可能性がある。
- 推奨対応: Winter CMS を 1.2.13 以降のバージョンへ更新する。

#### References
- https://github.com/wintercms/winter/commit/e09c8d3526f3583cb6c3476a021b885088ecd4bd
- https://github.com/wintercms/winter/commit/fd673f4f32140c97c68b1ed705764b819747fbdf
- https://github.com/wintercms/winter/security/advisories/GHSA-2223-f22x-24cq
- https://www.vulncheck.com/advisories/winter-cms-before-local-file-inclusion-via-javascript

# Frontend CVE Summary (2026-09-14)

## Overview

- 取得日時: 2026-09-14 09:07:11 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 7
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2025-64059](https://drive.google.com/file/d/1gbzdiaZEGTPwUPKLengVRO2Nijc6OVuy/view?usp=sharing)

> **Frontend** / **LOW** / CVSS: **1.8** / KEV: **no**

- タイトル: CVE-2025-64059
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-14 04:16:52 JST
- 更新日: 2026-09-14 04:16:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Grav 1.7.50.2のホームページエディタにて管理者がJavaScriptを入力可能な問題。ただし管理者は元々コード実行等の権限を持つためStored XSSとしての妥当性には異議があります。
- 影響: 管理者権限による悪意のあるスクリプトの挿入可能性があるが、本来の権限範囲内の動作である可能性があり影響は限定的とされています。
- 推奨対応: 管理者アカウントの保護と権限管理を徹底し、公式の見解やアップデート情報を確認してください。

#### References
- https://drive.google.com/file/d/1gbzdiaZEGTPwUPKLengVRO2Nijc6OVuy/view?usp=sharing

### [CVE-2026-90570](https://gitee.com/linlinjava/litemall/)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-90570
- 関連キーワード: vue, go
- 影響製品: -
- 公開日: 2026-09-14 02:16:57 JST
- 更新日: 2026-09-14 02:16:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: linlinjava litemall (1.4.0〜1.8.0) の Product Detail コンポーネントにおいて、detail引数の処理不備によりクロスサイトスクリプティング (XSS) が発生する脆弱性。
- 影響: リモートの攻撃者により、ユーザーのブラウザ上で不正なスクリプトを実行される可能性があります。
- 推奨対応: 入力値の検証および出力時の適切なエスケープ処理を実装し、プロジェクトからの修正情報の公開を確認してください。

#### References
- https://gitee.com/linlinjava/litemall/
- https://gitee.com/linlinjava/litemall/issues/IK5SVR
- https://vuldb.com/cve/CVE-2026-90570
- https://vuldb.com/submit/912674
- https://vuldb.com/vuln/403155

### [CVE-2026-90527](https://gitee.com/quequnlong/shiyi-blog/)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-90527
- 関連キーワード: vue
- 影響製品: -
- 公開日: 2026-09-14 00:16:28 JST
- 更新日: 2026-09-14 00:16:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: quequnlong shiyi-blog 1.2.1 以前の Add Message API において、body.content 引数の不備によりクロスサイトスクリプティング (XSS) が発生する脆弱性。
- 影響: リモートの攻撃者によって悪意のあるスクリプトが実行され、セッション情報の奪取等の被害を受ける可能性があります。
- 推奨対応: メッセージ入力に対する無害化（サニタイズ）とエスケープ処理を行い、修正パッチの適用を検討してください。

#### References
- https://gitee.com/quequnlong/shiyi-blog/
- https://gitee.com/quequnlong/shiyi-blog/issues/IK5RF6
- https://vuldb.com/cve/CVE-2026-90527
- https://vuldb.com/submit/912534
- https://vuldb.com/vuln/403117

### [CVE-2026-90528](https://gitee.com/TDuckApp/tduck-platform/)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-90528
- 関連キーワード: vue
- 影響製品: -
- 公開日: 2026-09-14 00:16:28 JST
- 更新日: 2026-09-14 00:16:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TDuckApp tduck-platform 5.3 以前の Form Write View において、submitShowCustomPageContent 引数の不備によるクロスサイトスクリプティング (XSS) の脆弱性。
- 影響: リモートから悪意のあるスクリプトを実行され、ユーザー環境に影響を及ぼす可能性があります。
- 推奨対応: 該当機能における入出力処理のサニタイズ・エスケープを徹底し、修正版の更新情報を確認してください。

#### References
- https://gitee.com/TDuckApp/tduck-platform/
- https://gitee.com/TDuckApp/tduck-platform/issues/IK5RJD
- https://vuldb.com/cve/CVE-2026-90528
- https://vuldb.com/submit/912535
- https://vuldb.com/vuln/403118

### [CVE-2026-90564](https://gitee.com/quequnlong/shiyi-blog/)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-90564
- 関連キーワード: vue
- 影響製品: -
- 公開日: 2026-09-14 01:16:51 JST
- 更新日: 2026-09-14 01:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: quequnlong shiyi-blog 1.0.0〜1.2.1 の chat sendMsg エンドポイントにおいて、chat_msg 引数の処理不備により XSS が発生する脆弱性。
- 影響: 遠隔からチャットメッセージを介して任意のスクリプトを実行される可能性があります。
- 推奨対応: チャットメッセージの送信・表示処理で適切にエスケープを行い、今後の修正パッチを確認してください。

#### References
- https://gitee.com/quequnlong/shiyi-blog/
- https://gitee.com/quequnlong/shiyi-blog/issues/IK5RVL
- https://vuldb.com/cve/CVE-2026-90564
- https://vuldb.com/submit/912553
- https://vuldb.com/vuln/403149

### [CVE-2026-90567](https://gitee.com/quequnlong/shiyi-blog/)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-90567
- 関連キーワード: vue
- 影響製品: -
- 公開日: 2026-09-14 01:16:52 JST
- 更新日: 2026-09-14 01:16:52 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: quequnlong shiyi-blog 1.2.1 以前の Search コンポーネント（highlightKeyword）において、title/summary 引数の処理不備による XSS 脆弱性。
- 影響: 検索結果のキーワード強調表示を介して、リモートから不正なスクリプトが実行される可能性があります。
- 推奨対応: ハイライト処理時の HTML エスケープ処理を正しく実装してください。

#### References
- https://gitee.com/quequnlong/shiyi-blog/
- https://gitee.com/quequnlong/shiyi-blog/issues/IK5SPD
- https://vuldb.com/cve/CVE-2026-90567
- https://vuldb.com/submit/912671
- https://vuldb.com/vuln/403152

### [CVE-2026-90569](https://gitee.com/linlinjava/litemall/)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-90569
- 関連キーワード: vue
- 影響製品: -
- 公開日: 2026-09-14 02:16:57 JST
- 更新日: 2026-09-14 02:16:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: linlinjava litemall 1.5.0〜1.8.0 の Admin Topic Handler において、パラメータ操作によるクロスサイトスクリプティング (XSS) 脆弱性。
- 影響: 遠隔の攻撃者により、ブラウザ上で不正なスクリプトを実行される可能性があります。
- 推奨対応: トピック入力・検証処理におけるサニタイズ処理を実施し、プロジェクトの更新情報を確認してください。

#### References
- https://gitee.com/linlinjava/litemall/
- https://gitee.com/linlinjava/litemall/issues/IK5SUU
- https://vuldb.com/cve/CVE-2026-90569
- https://vuldb.com/submit/912673
- https://vuldb.com/vuln/403154

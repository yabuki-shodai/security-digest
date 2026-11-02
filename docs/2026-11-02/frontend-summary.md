# Frontend CVE Summary (2026-11-02)

## Overview

- 取得日時: 2026-11-02 10:28:26 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 1
- High: 5
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-120235](https://github.com/ag-ui-protocol/ag-ui/)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-120235
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-11-02 01:18:14 JST
- 更新日: 2026-11-02 01:18:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ag-ui-protocol ag-ui (0.0.58以下) の SSE Parser コンポーネント内 `parseSSEStream` 関数における不備。
- 影響: 遠隔からリソースを不当に消費させられる可能性がある。
- 推奨対応: 提示されているパッチ (9e7b2b00bce215bbf731f1e6094f63812527c432) を適用し、修正版へアップデートする。

#### References
- https://github.com/ag-ui-protocol/ag-ui/
- https://github.com/ag-ui-protocol/ag-ui/commit/9e7b2b00bce215bbf731f1e6094f63812527c432
- https://github.com/ag-ui-protocol/ag-ui/issues/2522
- https://github.com/ag-ui-protocol/ag-ui/pull/2627
- https://github.com/ag-ui-protocol/ag-ui/releases/tag/release/2026-10-30

### [CVE-2026-120237](https://github.com/ag-ui-protocol/ag-ui/)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-120237
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-11-02 03:17:13 JST
- 更新日: 2026-11-02 03:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ag-ui-protocol ag-ui (0.0.58以下) の Interrupt expiry コンポーネント内 `isInterruptExpired` 関数における不備。
- 影響: 遠隔からの攻撃によりリソースを過剰に消費させられる可能性がある。
- 推奨対応: 修正用プルリクエストの承認・リリース状況を確認のうえ、対応バージョンへ更新する。

#### References
- https://github.com/ag-ui-protocol/ag-ui/
- https://github.com/ag-ui-protocol/ag-ui/issues/2525
- https://github.com/ag-ui-protocol/ag-ui/pull/3241
- https://vuldb.com/cve/CVE-2026-120237
- https://vuldb.com/submit/1015179

### [CVE-2026-120233](https://github.com/ag-ui-protocol/ag-ui/)

> **Frontend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-120233
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-11-02 01:18:14 JST
- 更新日: 2026-11-02 01:18:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ag-ui-protocol ag-ui (0.0.58以下) の HttpAgent コンポーネントにおける脆弱性。
- 影響: 遠隔からの攻撃により機密情報が漏洩する可能性がある。
- 推奨対応: 修正用プルリクエストの承認・リリース状況を確認のうえ、最新版へアップデートする。

#### References
- https://github.com/ag-ui-protocol/ag-ui/
- https://github.com/ag-ui-protocol/ag-ui/issues/2520
- https://github.com/ag-ui-protocol/ag-ui/pull/2575
- https://vuldb.com/cve/CVE-2026-120233
- https://vuldb.com/submit/1015143

### [CVE-2026-120338](https://github.com/PrefectHQ/prefab)

> **Frontend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-120338
- 関連キーワード: javascript, python
- 影響製品: -
- 公開日: 2026-11-02 01:18:14 JST
- 更新日: 2026-11-02 01:18:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: prefab-ui (0.14.0〜0.20.2) の Generative UI サンドボックスにおける Deno サブプロセス起動時の過剰な権限付与および API 露出。
- 影響: 未認証の遠隔の攻撃者がサーバーOSユーザー権限で任意のファイル読み書きおよび永続的なコード実行を行う可能性がある。
- 推奨対応: 修正されたバージョンへ直ちにアップデートし、設定を見直す。

#### References
- https://github.com/PrefectHQ/prefab
- https://github.com/PrefectHQ/prefab/commit/030f074f85e0b1be0dd44b0283185aecb26337a2
- https://github.com/PrefectHQ/prefab/pull/538
- https://github.com/PrefectHQ/prefab/releases/tag/v0.14.0
- https://github.com/PrefectHQ/prefab/releases/tag/v0.20.2

### [CVE-2026-111089](https://lists.apache.org/thread.html/xyp4sm5mm7s618fktstb22577qxbmqw8)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-111089
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-11-02 08:17:28 JST
- 更新日: 2026-11-02 08:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache Wicket におけるリソースバンドルから取得したテキストの JavaScript・属性出力時のエスケープ不足。
- 影響: 引用符を含むテキストによりブラウザ上で意図しないスクリプトが実行される（XSS）可能性がある。
- 推奨対応: エスケープ処理が修正されたバージョンの Apache Wicket へアップデートする。

#### References
- https://lists.apache.org/thread.html/xyp4sm5mm7s618fktstb22577qxbmqw8

### [CVE-2026-82956](https://lists.apache.org/thread.html/fs3vdddt9bwshdstj952psj49s5w4vqm)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-82956
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-11-02 08:17:29 JST
- 更新日: 2026-11-02 08:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache Wicket の AjaxNewWindowNotifyingBehavior における windowName パラメータ出力時のエスケープ不足。
- 影響: ページ描画時に任意の JavaScript が実行される（XSS）可能性がある。
- 推奨対応: 修正済みの Apache Wicket バージョンへ更新する。

#### References
- https://lists.apache.org/thread.html/fs3vdddt9bwshdstj952psj49s5w4vqm

### [CVE-2026-83559](https://lists.apache.org/thread.html/77kc85ztkxdpp7wg7cv61c4539j9s1g3)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-83559
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-11-02 08:17:29 JST
- 更新日: 2026-11-02 08:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache Wicket の JavaScriptUtils#escapeQuotes() におけるバックスラッシュ自体のエスケープ漏れ。
- 影響: エスケープ処理が正しく機能せず、閲覧中のユーザーのセッション上で任意スクリプトが実行される可能性がある。
- 推奨対応: 修正されたバージョンへアップデートするか、対象メソッドの直接使用を見直す。

#### References
- https://lists.apache.org/thread.html/77kc85ztkxdpp7wg7cv61c4539j9s1g3

### [CVE-2026-84231](https://lists.apache.org/thread.html/39kz9838w25797bpkxn1hvfsm8jtc4zv)

> **Frontend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-84231
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-11-02 08:17:30 JST
- 更新日: 2026-11-02 08:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache Wicket の ExternalLink および PopupSettings における URL 連結時のエスケープ不備。
- 影響: onclick 属性等に生成される JavaScript リテラルが不当に終了し、クロスサイトスクリプティング（XSS）が引き起こされる可能性がある。
- 推奨対応: 修正済みの Apache Wicket バージョンへ更新する。

#### References
- https://lists.apache.org/thread.html/39kz9838w25797bpkxn1hvfsm8jtc4zv

### [CVE-2026-95863](https://lists.apache.org/thread.html/5wg754b873tlnsc268myrwcoy9lt046v)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-95863
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-11-02 08:17:30 JST
- 更新日: 2026-11-02 08:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache Wicket における markup id および input name の JavaScript リテラル出力時のエスケープ不足。
- 影響: 単一引用符やバックスラッシュを含む入力により文字列リテラルが閉じられ、任意のスクリプトが実行される可能性がある。
- 推奨対応: 修正済みの Apache Wicket バージョンへ更新する。

#### References
- https://lists.apache.org/thread.html/5wg754b873tlnsc268myrwcoy9lt046v

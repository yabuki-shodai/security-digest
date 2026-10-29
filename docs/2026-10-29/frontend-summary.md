# Frontend CVE Summary (2026-10-29)

## Overview

- 取得日時: 2026-10-29 10:45:21 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 22
- Critical: 1
- High: 15
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-63190](https://github.com/fearlessgeekmedia/FearlessCMS/commit/59fb22cf989b5ba14c387c3212e15b146e02cf9a)

> **Frontend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-63190
- 関連キーワード: javascript, gin, docker
- 影響製品: -
- 公開日: 2026-10-29 05:18:37 JST
- 更新日: 2026-10-29 05:18:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FearlessCMS (v0.1.4未満) のデバッグ用PHPスクリプトにおいて、認証チェックや入力検証が欠落しており、URIパスの非正規化を利用した認証回避が可能。
- 影響: 未認証の第三者により任意のファイル書き込み、Webサイトの改ざん、およびXSS（クロスサイトスクリピング）が実行される可能性がある。
- 推奨対応: FearlessCMS をバージョン 0.1.4 以降に更新する。

#### References
- https://github.com/fearlessgeekmedia/FearlessCMS/commit/59fb22cf989b5ba14c387c3212e15b146e02cf9a
- https://github.com/fearlessgeekmedia/FearlessCMS/security/advisories/GHSA-3mq8-hrhf-7hv6
- https://github.com/fearlessgeekmedia/FearlessCMS/tree/0.1.4

### [CVE-2026-116795](https://github.com/le0pard/re2js/commit/dfdd947785dfa113bdc97416375c246a39458395)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-116795
- 関連キーワード: javascript, gin, express
- 影響製品: -
- 公開日: 2026-10-29 03:17:14 JST
- 更新日: 2026-10-29 03:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RE2JS (2.2.0〜2.8.7未満) において、LOOKBEHINDS（後読み）を有効にして繰り返しマッチングを行う処理に不備があり、計算量が二次関数的に増大する。
- 影響: 攻撃者が操作した入力テキストにより処理時間が著しく増大し、単一スレッドが占有されてサービス拒否 (DoS) が発生する可能性がある。
- 推奨対応: RE2JS をバージョン 2.8.7 以降に更新する。

#### References
- https://github.com/le0pard/re2js/commit/dfdd947785dfa113bdc97416375c246a39458395
- https://github.com/le0pard/re2js/pull/59
- https://github.com/le0pard/re2js/releases/tag/2.8.7
- https://github.com/le0pard/re2js/security/advisories/GHSA-gg6h-894w-4m9c

### [CVE-2026-118244](https://github.com/highcharts/highcharts/commit/abde7c576793bf50b0e0636e59b49630de6dd0d5)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-118244
- 関連キーワード: javascript, gin, aws
- 影響製品: -
- 公開日: 2026-10-29 03:17:15 JST
- 更新日: 2026-10-29 03:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts JS において、DOMParserのフォールバック処理時に許可リスト適用前で生HTMLが読み込まれる不備が存在する。
- 影響: 印刷実行時などの特定条件下で、ホストページのオリジンにおいて意図しないスクリプトが実行される（XSS）可能性がある。
- 推奨対応: Highcharts JS をバージョン 12.6.1 または 13.1.0 以降に更新する。

#### References
- https://github.com/highcharts/highcharts/commit/abde7c576793bf50b0e0636e59b49630de6dd0d5
- https://github.com/highcharts/highcharts/releases/tag/v13.1.0
- https://github.com/highcharts/highcharts/security/advisories/GHSA-65hg-cf3f-5m39

### [CVE-2026-116796](https://github.com/highcharts/highcharts/commit/6cf359fb144aa51fdc105e2b9bbd013439b02c88)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-116796
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-29 03:17:14 JST
- 更新日: 2026-10-29 03:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HighchartsにおけるSVGアンカー属性 `xlink:href` に対するURLスキーム検証の欠落
- 影響: テキストオプションを制御可能な攻撃者が `javascript:` URLを挿入し、エクスポートや再レンダリングされたSVGのリンクをユーザーが有効化することで、ドキュメントのオリジン上でスクリプトが実行される可能性がある。
- 推奨対応: Highcharts 11.4.9、12.6.2、または 13.1.1 以降へアップデートしてください。

#### References
- https://github.com/highcharts/highcharts/commit/6cf359fb144aa51fdc105e2b9bbd013439b02c88
- https://github.com/highcharts/highcharts/releases/tag/v13.1.1
- https://github.com/highcharts/highcharts/security/advisories/GHSA-mw4f-gj5x-6xr4

### [CVE-2026-116797](https://github.com/highcharts/highcharts/commit/52abd4f8f8db87dd20eab7c01444112380e30e98)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-116797
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-29 03:17:14 JST
- 更新日: 2026-10-29 05:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts Grid Pro (2.0.0〜3.2.0未満) の入力レンダラーにおいて、属性マップを検証せずに `setAttribute` でそのまま複製・設定してしまう。
- 影響: 列設定を制御された場合、ユーザーがセルに入力・ホバー・編集を開始した際などにホストページのオリジンでスクリプトが実行される（XSS）可能性がある。
- 推奨対応: Highcharts Grid Pro をバージョン 3.2.0 以降に更新する。

#### References
- https://github.com/highcharts/highcharts/commit/52abd4f8f8db87dd20eab7c01444112380e30e98
- https://github.com/highcharts/highcharts/security/advisories/GHSA-5ghw-9mgr-jvx2

### [CVE-2026-118242](https://github.com/highcharts/highcharts/commit/8fc970658fee6601625b42da29d27c3ef7c45e30)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-118242
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-29 03:17:14 JST
- 更新日: 2026-10-29 03:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts Grid (2.3.0〜3.2.0未満) において、SVGアイコン生成時に属性名の検証を行わず全キーを `setAttribute` で設定してしまう。
- 影響: アイコン設定を制御された場合、ユーザーがソートやページネーションアイコンを操作・ホバーした際にホストページのオリジンでスクリプトが実行される（XSS）可能性がある。
- 推奨対応: Highcharts Grid をバージョン 3.2.0 以降に更新する。

#### References
- https://github.com/highcharts/highcharts/commit/8fc970658fee6601625b42da29d27c3ef7c45e30
- https://github.com/highcharts/highcharts/security/advisories/GHSA-6g3c-p4fg-xv47

### [CVE-2026-118245](https://github.com/highcharts/highcharts/commit/98d3652cdc4f66fbccbbb8b4184ecd8f647f74de)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-118245
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-29 03:17:15 JST
- 更新日: 2026-10-29 03:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts Dashboards (1.0.0〜4.2.2未満) において、`chartConstructor` プロパティの妥当性検証が不十分な問題が存在する。
- 影響: ダッシュボード設定を制御可能な攻撃者により、ボード描画時にホストページのオリジンで任意のスクリプトが実行される（XSS）可能性がある。
- 推奨対応: Highcharts Dashboards をバージョン 4.2.2 以降に更新する。

#### References
- https://github.com/highcharts/highcharts/commit/98d3652cdc4f66fbccbbb8b4184ecd8f647f74de
- https://github.com/highcharts/highcharts/releases/tag/dashboards-v4.2.2
- https://github.com/highcharts/highcharts/security/advisories/GHSA-grj7-r4jv-pw9j

### [CVE-2026-118246](https://github.com/highcharts/highcharts/commit/b0fafdaaee7d0cac2ecfeb0eaf37b11cd40594ef)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-118246
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-29 03:17:15 JST
- 更新日: 2026-10-29 03:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts において、パンくずリスト（breadcrumbs.style）の属性適用時に属性名のフィルタリングが行われない。
- 影響: グラフ設定を制御された場合、ユーザーがパンくずリストのボタンを操作・ホバーした際にホストページのオリジンでスクリプトが実行される（XSS）可能性がある。
- 推奨対応: Highcharts をバージョン 11.4.9、12.6.1、または 13.1.0 以降に更新する。

#### References
- https://github.com/highcharts/highcharts/commit/b0fafdaaee7d0cac2ecfeb0eaf37b11cd40594ef
- https://github.com/highcharts/highcharts/releases/tag/v13.1.0
- https://github.com/highcharts/highcharts/security/advisories/GHSA-35rr-xwfh-x789

### [CVE-2026-118251](https://github.com/highcharts/highcharts/commit/9534773d0f41400aac0945bf8aaebc38dfc72aff)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-118251
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-29 04:17:29 JST
- 更新日: 2026-10-29 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts において、クレジット表記のリンク先（`credits.href`）に対するURLスキームの検証が欠落している。
- 影響: ユーザーがクレジットラベルをクリックした際、`javascript:` スキームなどを介してホストページのオリジンでスクリプトが実行される（XSS）可能性がある。
- 推奨対応: Highcharts をバージョン 11.4.9、12.6.1、または 13.1.0 以降に更新する。

#### References
- https://github.com/highcharts/highcharts/commit/9534773d0f41400aac0945bf8aaebc38dfc72aff
- https://github.com/highcharts/highcharts/pull/25315
- https://github.com/highcharts/highcharts/releases/tag/v13.1.0
- https://github.com/highcharts/highcharts/security/advisories/GHSA-5793-x2q3-c3q7

### [CVE-2026-118252](https://github.com/highcharts/highcharts/commit/e65f8c21b9974dcccfa1c600a375d836acef4a7d)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-118252
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-29 04:17:29 JST
- 更新日: 2026-10-29 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts Dashboards (1.0.0〜4.2.3未満) の編集モードサイドバーにおいて、言語文字列がテキストではなくHTMLとしてパースされる。
- 影響: 言語設定を制御された場合、ユーザーが編集モードのサイドバーを開いてラベルを描画した際にホストページのオリジンでスクリプトが実行される（XSS）可能性がある。
- 推奨対応: Highcharts Dashboards をバージョン 4.2.3 以降に更新する。

#### References
- https://github.com/highcharts/highcharts/commit/e65f8c21b9974dcccfa1c600a375d836acef4a7d
- https://github.com/highcharts/highcharts/releases/tag/dashboards-v4.2.3
- https://github.com/highcharts/highcharts/security/advisories/GHSA-rcqf-f6h2-ccg9

### [CVE-2026-118253](https://github.com/highcharts/highcharts/commit/f97213bab745e40f628720c21f4e8b31ee3e768b)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-118253
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-29 04:17:29 JST
- 更新日: 2026-10-29 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts Dashboardsの編集モードにおける、全画面表示用言語ラベルの不適切なHTML解析処理
- 影響: 言語設定を操作可能な攻撃者により、全画面コントロール描画時にホスティングページ上で任意のスクリプト（XSS）が実行される可能性がある。
- 推奨対応: Highcharts Dashboards 4.2.3 以降の修正バージョンへアップデートしてください。

#### References
- https://github.com/highcharts/highcharts/commit/f97213bab745e40f628720c21f4e8b31ee3e768b
- https://github.com/highcharts/highcharts/releases/tag/dashboards-v4.2.3
- https://github.com/highcharts/highcharts/security/advisories/GHSA-58g7-7f52-h92c

### [CVE-2026-118254](https://github.com/highcharts/highcharts/commit/1e8ded84d52191883965641b863cf0c73eb759aa)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-118254
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-29 04:17:29 JST
- 更新日: 2026-10-29 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts Grid (2.0.0〜3.2.0未満) において、ページネーションの言語設定文字列がテキストではなくマークアップ（HTML）としてDOMに挿入される。
- 影響: 言語設定を制御された場合、ページネーションコントロール描画時にホストページのオリジンでスクリプトが実行される（XSS）可能性がある。
- 推奨対応: Highcharts Grid をバージョン 3.2.0 以降に更新する。

#### References
- https://github.com/highcharts/highcharts/commit/1e8ded84d52191883965641b863cf0c73eb759aa
- https://github.com/highcharts/highcharts/releases/tag/grid-v3.2.0
- https://github.com/highcharts/highcharts/security/advisories/GHSA-r5wg-q8fc-p6w2

### [CVE-2026-118255](https://github.com/highcharts/highcharts/commit/45b74403acafbe9f621c4a343506721d9129e991)

> **Frontend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-118255
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-10-29 04:17:29 JST
- 更新日: 2026-10-29 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts Gridにおける credits.href のURLスキーム検証不足
- 影響: Grid設定を制御可能な攻撃者が `javascript:` URLを指定することで、ユーザーがリンクをクリックした際にページオリジン上で任意のスクリプトが実行され、データやセッション情報が侵害される可能性がある。
- 推奨対応: Highcharts Grid Pro 3.2.0 以降へアップデートしてください。

#### References
- https://github.com/highcharts/highcharts/commit/45b74403acafbe9f621c4a343506721d9129e991
- https://github.com/highcharts/highcharts/pull/25351
- https://github.com/highcharts/highcharts/releases/tag/grid-v3.2.0
- https://github.com/highcharts/highcharts/security/advisories/GHSA-6hgp-fmhr-mrg4

### [CVE-2026-118257](https://github.com/intlify/vue-i18n/commit/43391d20e7c85403cb59bdb21b5d542819f54042)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-118257
- 関連キーワード: vue, gin
- 影響製品: -
- 公開日: 2026-10-29 04:17:30 JST
- 更新日: 2026-10-29 04:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vue I18nの `sanitizeTranslatedHtml()` における iframe srcdoc 属性の不十分なサニタイズ
- 影響: `escapeParameter` を有効にし `v-html` で翻訳を表示している場合、ブラウザによる属性値のデコードを経て同一オリジンのネストされたドキュメント内で任意のスクリプトが実行される可能性がある。
- 推奨対応: Vue I18n 11.4.14 または 12.0.0-alpha.5 以降へアップデートしてください（非サポートバージョンを利用中の場合はサポート対象版へ移行してください）。

#### References
- https://github.com/intlify/vue-i18n/commit/43391d20e7c85403cb59bdb21b5d542819f54042
- https://github.com/intlify/vue-i18n/pull/2679
- https://github.com/intlify/vue-i18n/releases/tag/v11.4.14
- https://github.com/intlify/vue-i18n/releases/tag/v12.0.0-alpha.5
- https://github.com/intlify/vue-i18n/security/advisories/GHSA-83rm-6c8r-g728

### [CVE-2026-118029](https://aws.amazon.com/security/security-bulletins/2026-153-aws/)

> **Frontend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-118029
- 関連キーワード: swr, aws
- 影響製品: -
- 公開日: 2026-10-29 01:17:07 JST
- 更新日: 2026-10-29 01:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Unverified ownership of the default query result location in the Athena module in AWS SDK for pandas (awswrangler) before 3.16.1 might allow remote actors to read Athena query results and tamper with result sets returned to the caller via a pre-created S3 bucket. To remediate this issue, users should upgrade to version...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-153-aws/
- https://github.com/aws/aws-sdk-pandas/releases/tag/3.16.1

### [CVE-2026-118249](https://github.com/highcharts/highcharts/commit/d3357705c8f348904441327e32f50ab528c3a205)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-118249
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-29 03:17:16 JST
- 更新日: 2026-10-29 03:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HighchartsにおけるポイントオブジェクトのキーをカラムIDとして直接使用することによるプロトタイプ汚染
- 影響: `__proto__` や `constructor` キーを通じて `Object.prototype` などに意図しない書き込みが発生し、ページ全体のJavaScript動作や描画処理に影響を及ぼす可能性がある。
- 推奨対応: Highcharts 13.1.0 以降へアップデートしてください。

#### References
- https://github.com/highcharts/highcharts/commit/d3357705c8f348904441327e32f50ab528c3a205
- https://github.com/highcharts/highcharts/pull/25321
- https://github.com/highcharts/highcharts/releases/tag/v13.1.0
- https://github.com/highcharts/highcharts/security/advisories/GHSA-gfvx-2c2g-38wq

### [CVE-2026-118250](https://github.com/highcharts/highcharts/commit/fd4ee8140732618bbe71295aba55398fb1f8fa9e)

> **Frontend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-118250
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-29 03:17:16 JST
- 更新日: 2026-10-29 03:17:16 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highchartsの `series.keys` パス処理におけるセグメント検証不足によるプロトタイプ汚染
- 影響: `series.keys` を制御できる攻撃者が `__proto__` を経由して `Object.prototype` に任意のプロパティを設定し、ページ上のアプリケーション動作を混乱させる可能性がある。
- 推奨対応: Highcharts 11.4.9、12.6.1、または 3.1.0 以降の対応バージョンへアップデートしてください。

#### References
- https://github.com/highcharts/highcharts/commit/fd4ee8140732618bbe71295aba55398fb1f8fa9e
- https://github.com/highcharts/highcharts/pull/25313
- https://github.com/highcharts/highcharts/releases/tag/v13.1.0
- https://github.com/highcharts/highcharts/security/advisories/GHSA-rmqc-xvr3-v46c

### [CVE-2026-118652](https://github.com/labstack/echo/commit/b838391e2eade87ae7e5a09d7bb5087bec271ec1)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-118652
- 関連キーワード: javascript, go, echo
- 影響製品: -
- 公開日: 2026-10-29 05:17:22 JST
- 更新日: 2026-10-29 05:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Go言語向けWebフレームワーク Echo の `Context.JSONP` および `Context.JSONPBlob` におけるコールバック値の不十分な検証・エスケープ処理
- 影響: 攻撃者が制御可能な入力をコールバックとして受け取るルートが存在する場合、反射型クロスサイトスクリプティング（Reflected XSS）が引き起こされる可能性がある。
- 推奨対応: Echo 4.16.0 または 5.4.0 以降へアップデートしてください。

#### References
- https://github.com/labstack/echo/commit/b838391e2eade87ae7e5a09d7bb5087bec271ec1
- https://github.com/labstack/echo/commit/fc410094b2f3415cf2bf5204082137b205bfd5af
- https://github.com/labstack/echo/releases/tag/v4.16.0
- https://github.com/labstack/echo/releases/tag/v5.4.0
- https://github.com/labstack/echo/security/advisories/GHSA-h9g5-28mm-hx3g

### [CVE-2026-118243](https://github.com/highcharts/highcharts/commit/ade5a41a700212f09133223ca990a3737d1d9ec6)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-118243
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-29 03:17:15 JST
- 更新日: 2026-10-29 03:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts Dashboardsにおけるデータプール設定処理の不備によるプロトタイプ汚染の脆弱性。
- 影響: Object.prototypeが汚染され、同期状態の破損や同期機能の停止が発生する可能性があります。
- 推奨対応: Highcharts Dashboardsをバージョン4.2.2以降にアップデートしてください。

#### References
- https://github.com/highcharts/highcharts/commit/ade5a41a700212f09133223ca990a3737d1d9ec6
- https://github.com/highcharts/highcharts/releases/tag/dashboards-v4.2.2
- https://github.com/highcharts/highcharts/security/advisories/GHSA-jqgh-w3cc-7jqw

### [CVE-2026-118247](https://github.com/highcharts/highcharts/commit/02dd9349aeb6f4cc9c98806120d917ed316b4c74)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-118247
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-29 03:17:15 JST
- 更新日: 2026-10-29 03:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts DataTableの単一セル書き込み処理における信頼できないカラムIDの受容によるプロトタイプ汚染
- 影響: 不正なカラムIDを通じて `Object.prototype` などに値が書き込まれ、ページ全体のデータ参照やアプリケーションの制御フロー、描画処理に悪影響を及ぼす可能性がある。
- 推奨対応: Highcharts Dashboards 4.2.2 以降や Grid Pro 3.2.0 以降など、該当コンポーネントの修正バージョンへアップデートしてください。

#### References
- https://github.com/highcharts/highcharts/commit/02dd9349aeb6f4cc9c98806120d917ed316b4c74
- https://github.com/highcharts/highcharts/releases/tag/dashboards-v4.2.2
- https://github.com/highcharts/highcharts/releases/tag/grid-v3.2.0
- https://github.com/highcharts/highcharts/security/advisories/GHSA-c75x-9x9h-28rm

### [CVE-2026-118248](https://github.com/highcharts/highcharts/commit/05efb9849130461fe61992ea8f58d22edaad978b)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-118248
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-29 03:17:15 JST
- 更新日: 2026-10-29 03:17:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Highcharts Dashboardsの編集モードにおける `editableOptions` プロパティパス処理の検証不足によるプロトタイプ汚染
- 影響: `__proto__` や `constructor` を含むパスにより `Object.prototype` に値が書き込まれ、ページ全体のJavaScript処理に意図しない影響を与える可能性がある。
- 推奨対応: Highcharts Dashboards 4.2.2 以降へアップデートしてください。

#### References
- https://github.com/highcharts/highcharts/commit/05efb9849130461fe61992ea8f58d22edaad978b
- https://github.com/highcharts/highcharts/releases/tag/dashboards-v4.2.2
- https://github.com/highcharts/highcharts/security/advisories/GHSA-wg5j-9wp8-2ggm

### [CVE-2026-118256](https://github.com/intlify/vue-i18n/commit/d657ce8f4b3b6b198a8f6e3d09e2b57a5d019fb8)

> **Frontend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-118256
- 関連キーワード: vue, gin
- 影響製品: -
- 公開日: 2026-10-29 04:17:30 JST
- 更新日: 2026-10-29 04:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vue I18nにおいて、エスケープ有効時にリスト値と名前付き値を同時に渡すと名前付き値のエスケープ処理がスキップされる脆弱性。
- 影響: 悪意のあるマークアップやスクリプトの挿入、XSS攻撃につながる可能性があります。
- 推奨対応: Vue I18nをバージョン11.4.14または12.0.0-alpha.5以降にアップデートしてください。

#### References
- https://github.com/intlify/vue-i18n/commit/d657ce8f4b3b6b198a8f6e3d09e2b57a5d019fb8
- https://github.com/intlify/vue-i18n/pull/2680
- https://github.com/intlify/vue-i18n/security/advisories/GHSA-8rc2-428q-7ww3

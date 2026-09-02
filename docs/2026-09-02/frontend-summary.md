# Frontend CVE Summary (2026-09-02)

## Overview

- 取得日時: 2026-09-02 09:04:07 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 16
- Critical: 0
- High: 13
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-83619](https://github.com/xmldom/xmldom/commit/3abb0934f5a8a84d83a1f9cde0f2bd04c08b2a09)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83619
- 関連キーワード: javascript, npm, node.js, express
- 影響製品: -
- 公開日: 2026-09-02 00:17:40 JST
- 更新日: 2026-09-02 04:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldom（0.7.0〜0.8.15未満）のlib/sax.jsにおいて、終了タグ名のトリム処理に使用される正規表現のバックトラックに起因する脆弱性。
- 影響: 悪意のある小規模なXML入力を解析させることで、Node.jsのイベントループが停止し、サービス拒否（DoS）が発生する可能性があります。
- 推奨対応: @xmldom/xmldom バージョン 0.8.15 以降に更新してください。

#### References
- https://github.com/xmldom/xmldom/commit/3abb0934f5a8a84d83a1f9cde0f2bd04c08b2a09
- https://github.com/xmldom/xmldom/pull/1072
- https://github.com/xmldom/xmldom/releases/tag/0.8.15
- https://github.com/xmldom/xmldom/security/advisories/GHSA-x4fp-j954-r2f4

### [CVE-2026-83606](https://github.com/xmldom/xmldom/commit/73df6b8bdbd86f904b9e8c3ab9c49aa54ef2802e)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83606
- 関連キーワード: javascript, gin, node.js, express
- 影響製品: -
- 公開日: 2026-09-02 00:17:38 JST
- 更新日: 2026-09-02 00:17:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldom（0.9.0-beta.9〜0.9.11未満）のlib/grammar.jsにおいて、処理命令（PI）の解析処理で二次多項式時間のバックトラックが発生する脆弱性。
- 影響: 閉じタグ（?>）を欠いた特定のXML入力を解析させることで、Node.jsのイベントループが停止し、サービス拒否（DoS）が発生する可能性があります。
- 推奨対応: @xmldom/xmldom バージョン 0.9.11 以降に更新してください。

#### References
- https://github.com/xmldom/xmldom/commit/73df6b8bdbd86f904b9e8c3ab9c49aa54ef2802e
- https://github.com/xmldom/xmldom/pull/1039
- https://github.com/xmldom/xmldom/releases/tag/0.9.11
- https://github.com/xmldom/xmldom/security/advisories/GHSA-g53g-w8rj-fmg7
- https://github.com/xmldom/xmldom/security/advisories/GHSA-g53g-w8rj-fmg7

### [CVE-2026-83608](https://github.com/xmldom/xmldom/commit/57aec90ac57b4408ae7c5d1746bf2a693b5ed90e)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83608
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-02 00:17:38 JST
- 更新日: 2026-09-02 00:17:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldomにおけるDocumentType.nameプロパティの検証不足により、<!DOCTYPE ...>宣言を不正に終了させられる脆弱性。
- 影響: シリアライズ時に意図しないマークアップが注入され、XML構造が破壊されるなどの影響を受ける可能性があります。
- 推奨対応: @xmldom/xmldom バージョン 0.8.15 または 0.9.12 以降に更新してください（旧xmldomパッケージへの修正対応はありません）。

#### References
- https://github.com/xmldom/xmldom/commit/57aec90ac57b4408ae7c5d1746bf2a693b5ed90e
- https://github.com/xmldom/xmldom/commit/85f12eb4d14b44de33216cfb72b50af4d24e9fdd
- https://github.com/xmldom/xmldom/pull/1071
- https://github.com/xmldom/xmldom/pull/1072
- https://github.com/xmldom/xmldom/releases/tag/0.8.15

### [CVE-2026-83613](https://github.com/xmldom/xmldom/commit/2c548f200cfec991cd5846627ef8f03542309213)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83613
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-09-02 00:17:39 JST
- 更新日: 2026-09-02 00:17:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldomにおいて、DOMParser.parseFromString()実行時に属性の挿入処理（NamedNodeMap.setNamedItem）が線形探索を行うため、処理時間が二次多項式的に増大する脆弱性。
- 影響: 多数の属性を持つXML入力を処理する際、Node.jsのイベントループが停止してサービス拒否（DoS）が発生する可能性があります。
- 推奨対応: @xmldom/xmldom バージョン 0.8.15 または 0.9.12 以降に更新してください（旧xmldomパッケージへの修正対応はありません）。

#### References
- https://github.com/xmldom/xmldom/commit/2c548f200cfec991cd5846627ef8f03542309213
- https://github.com/xmldom/xmldom/commit/cfb09b5dbeb035fdfedc9f01e2bbaf226bf47cf3
- https://github.com/xmldom/xmldom/pull/1071
- https://github.com/xmldom/xmldom/pull/1072
- https://github.com/xmldom/xmldom/releases/tag/0.8.15

### [CVE-2026-83616](https://github.com/xmldom/xmldom/commit/1cde3e31a07c41c87cfd368d6946aa477f16b4f9)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83616
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-02 00:17:40 JST
- 更新日: 2026-09-02 01:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldomのDocument.createProcessingInstructionにおけるターゲット名の不十分な検証により、処理命令の境界が破られる脆弱性。
- 影響: 不正な文字を含むターゲット名によって処理命令の境界を抜け出し、任意のXML構造を注入される可能性があります。
- 推奨対応: @xmldom/xmldom バージョン 0.8.15 または 0.9.12 以降に更新してください（旧xmldomパッケージへの修正対応はありません）。

#### References
- https://github.com/xmldom/xmldom/commit/1cde3e31a07c41c87cfd368d6946aa477f16b4f9
- https://github.com/xmldom/xmldom/commit/3b694872bcb5c7e3cbadba961a4be2488750ce5b
- https://github.com/xmldom/xmldom/pull/1071
- https://github.com/xmldom/xmldom/pull/1072
- https://github.com/xmldom/xmldom/releases/tag/0.8.15

### [CVE-2026-83617](https://github.com/xmldom/xmldom/commit/7b2ec67e1750daadd0bb06c92e875e726544a362)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83617
- 関連キーワード: javascript, express
- 影響製品: -
- 公開日: 2026-09-02 00:17:40 JST
- 更新日: 2026-09-02 01:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldom（0.9.11〜0.9.12未満）のrequireWellFormed: true検証において、複数行フラグを持つ正規表現が使用されているため、改行コードを含む不正な要素名・属性名をすり抜けてしまう脆弱性。
- 影響: 厳格なシリアライズ設定による保護をバイパスされ、要素タグや属性名へ任意マークアップが注入される可能性があります。
- 推奨対応: @xmldom/xmldom バージョン 0.9.12 以降に更新してください。

#### References
- https://github.com/xmldom/xmldom/commit/7b2ec67e1750daadd0bb06c92e875e726544a362
- https://github.com/xmldom/xmldom/pull/1071
- https://github.com/xmldom/xmldom/releases/tag/0.9.12
- https://github.com/xmldom/xmldom/security/advisories/GHSA-jxjr-3g7g-3944
- https://github.com/xmldom/xmldom/security/advisories/GHSA-jxjr-3g7g-3944

### [CVE-2026-83618](https://github.com/xmldom/xmldom/commit/7b2ec67e1750daadd0bb06c92e875e726544a362)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83618
- 関連キーワード: javascript, express
- 影響製品: -
- 公開日: 2026-09-02 00:17:40 JST
- 更新日: 2026-09-02 00:17:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldom（0.9.10〜0.9.12未満）のrequireWellFormed: true検証において、DocumentTypeのpublicIdおよびsystemId検証用正規表現が複数行フラグを保持している脆弱性。
- 影響: 改行コードを含む不正な値により厳格シリアライズの制限を回避され、<!DOCTYPE ...>宣言内にマークアップを注入される可能性があります。
- 推奨対応: @xmldom/xmldom バージョン 0.9.12 以降に更新してください。

#### References
- https://github.com/xmldom/xmldom/commit/7b2ec67e1750daadd0bb06c92e875e726544a362
- https://github.com/xmldom/xmldom/pull/1071
- https://github.com/xmldom/xmldom/releases/tag/0.9.12
- https://github.com/xmldom/xmldom/security/advisories/GHSA-vr34-hp96-76pp

### [CVE-2026-84232](https://access.redhat.com/security/cve/CVE-2026-84232)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-84232
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-02 01:17:36 JST
- 更新日: 2026-09-02 06:03:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pulpcoreのコンテンツ配信アプリにおいて、ローカルストレージ利用時にファイルが元のContent-TypeでかつContent-Disposition: attachmentヘッダーなしで配信される不具合。
- 影響: 悪意のあるユーザーがアップロードしたJavaScriptを含むHTMLやSVGがブラウザで実行され、格納型クロスサイトスクリプティング（XSS）が発生する可能性があります。
- 推奨対応: 修正されたバージョンのpulpcoreへ更新するか、レスポンスヘッダーの設定等をご確認ください。

#### References
- https://access.redhat.com/security/cve/CVE-2026-84232
- https://bugzilla.redhat.com/show_bug.cgi?id=2526807

### [CVE-2026-83605](https://github.com/xmldom/xmldom/commit/cba1321218b069182695813fa7565653708e172e)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83605
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-02 00:17:38 JST
- 更新日: 2026-09-02 00:17:38 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldomにおいて、Element.setAttribute()等で指定された属性名が適切に検証されない脆弱性。
- 影響: シリアライズ時に意図しない属性やイベントハンドラが注入され、ブラウザ環境でレンダリングされた場合にクロスサイトスクリプティング（XSS）等につながる可能性があります。
- 推奨対応: @xmldom/xmldom バージョン 0.8.14 または 0.9.11 以降に更新してください（旧xmldomパッケージへの修正対応はありません）。

#### References
- https://github.com/xmldom/xmldom/commit/cba1321218b069182695813fa7565653708e172e
- https://github.com/xmldom/xmldom/commit/d8212e632507eaf1d9f609657dd4c56abeb12d44
- https://github.com/xmldom/xmldom/pull/1043
- https://github.com/xmldom/xmldom/pull/1050
- https://github.com/xmldom/xmldom/releases/tag/0.8.14

### [CVE-2026-83607](https://github.com/xmldom/xmldom/commit/cba1321218b069182695813fa7565653708e172e)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83607
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-02 00:17:38 JST
- 更新日: 2026-09-02 01:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldomのDocument.createElement()において、要素タグ名に対する検証が不十分な脆弱性。
- 影響: 攻撃者制御のタグ名により任意属性や要素、処理命令がシリアライズ出力へ注入され、ブラウザで読み込まれた際にクロスサイトスクリプティング（XSS）が発生する可能性があります。
- 推奨対応: @xmldom/xmldom バージョン 0.8.14 または 0.9.11 以降に更新してください（旧xmldomパッケージへの修正対応はありません）。

#### References
- https://github.com/xmldom/xmldom/commit/cba1321218b069182695813fa7565653708e172e
- https://github.com/xmldom/xmldom/commit/d8212e632507eaf1d9f609657dd4c56abeb12d44
- https://github.com/xmldom/xmldom/pull/1043
- https://github.com/xmldom/xmldom/pull/1050
- https://github.com/xmldom/xmldom/releases/tag/0.8.14

### [CVE-2026-83609](https://github.com/xmldom/xmldom/commit/7b2ec67e1750daadd0bb06c92e875e726544a362)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83609
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-02 00:17:38 JST
- 更新日: 2026-09-02 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldomのQName検証処理において、正規表現のmultilineフラグ指定により改行コードを含む不正なXML名が検証をすり抜ける問題。
- 影響: シリアライズ時に意図しないXMLマークアップが注入される可能性がある。
- 推奨対応: @xmldom/xmldom バージョン 0.9.12 以降へ更新する。

#### References
- https://github.com/xmldom/xmldom/commit/7b2ec67e1750daadd0bb06c92e875e726544a362
- https://github.com/xmldom/xmldom/pull/1071
- https://github.com/xmldom/xmldom/releases/tag/0.9.12
- https://github.com/xmldom/xmldom/security/advisories/GHSA-3px3-54cx-rmw9

### [CVE-2026-83612](https://github.com/xmldom/xmldom/commit/7ced40c06c28d151e996a97045018c3559ae4707)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83612
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-02 00:17:39 JST
- 更新日: 2026-09-02 01:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldomのHTMLモード解析において、大文字小文字が混在した生テキスト要素の閉じタグ処理に不備がある問題。
- 影響: 解析処理の不安定化と出力の急増を招き、CPUおよびメモリ消費によるサービス拒否（DoS）が発生する可能性がある。
- 推奨対応: @xmldom/xmldom バージョン 0.9.12 以降へ更新する。

#### References
- https://github.com/xmldom/xmldom/commit/7ced40c06c28d151e996a97045018c3559ae4707
- https://github.com/xmldom/xmldom/pull/1071
- https://github.com/xmldom/xmldom/releases/tag/0.9.12
- https://github.com/xmldom/xmldom/security/advisories/GHSA-6mj3-qw4j-hgrw
- https://github.com/xmldom/xmldom/security/advisories/GHSA-6mj3-qw4j-hgrw

### [CVE-2026-83614](https://github.com/xmldom/xmldom/commit/0748720b620555f8c222782dcab575cf0cf403b4)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83614
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-02 00:17:39 JST
- 更新日: 2026-09-02 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldomのタグ名再スキャン処理およびnormalize()処理において、計算量が二次時間（O(N^2)）となる問題。
- 影響: 悪意ある入力の解析や処理呼び出しにより、サービス拒否（DoS）が引き起こされる可能性がある。
- 推奨対応: @xmldom/xmldom バージョン 0.8.15 または 0.9.12 以降へ更新する。（非推奨の旧xmldomパッケージには修正版がないため移行を検討する）

#### References
- https://github.com/xmldom/xmldom/commit/0748720b620555f8c222782dcab575cf0cf403b4
- https://github.com/xmldom/xmldom/commit/f40ccb861eee0acbf5ee4feb9a34932e87b329c9
- https://github.com/xmldom/xmldom/pull/1071
- https://github.com/xmldom/xmldom/pull/1072
- https://github.com/xmldom/xmldom/releases/tag/0.8.15

### [CVE-2026-83615](https://github.com/xmldom/xmldom/commit/954370f58c046223faf95ba77efcbc8ce014409d)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-83615
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-02 00:17:39 JST
- 更新日: 2026-09-02 00:17:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldomのXML解析処理において、名前空間マップが過剰に保持・複製される問題。
- 影響: 深くネストされた名前空間を持つXML文書の解析時にメモリ使用量が急増し、ヒープ枯渇によるサービス拒否（DoS）を引き起こす可能性がある。
- 推奨対応: @xmldom/xmldom バージョン 0.8.15 または 0.9.12 以降へ更新する。（非推奨の旧xmldomパッケージには修正版がないため移行を検討する）

#### References
- https://github.com/xmldom/xmldom/commit/954370f58c046223faf95ba77efcbc8ce014409d
- https://github.com/xmldom/xmldom/commit/dabffe884e864eeecb1f515c716f875e1bc47ec1
- https://github.com/xmldom/xmldom/pull/1071
- https://github.com/xmldom/xmldom/pull/1072
- https://github.com/xmldom/xmldom/releases/tag/0.8.15

### [CVE-2026-83610](https://github.com/xmldom/xmldom/commit/4664386e4f4d99d17b416a151dbe8323e245284b)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-83610
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-02 00:17:39 JST
- 更新日: 2026-09-02 00:17:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldomのcreateEntityReferenceにおいて無効な名前が検証なく許可され、そのままシリアライズされる問題。
- 影響: 実体参照の境界が壊れ、再パース時に攻撃者によって制御されたXMLマークアップが生成される可能性がある。
- 推奨対応: @xmldom/xmldom バージョン 0.8.15 または 0.9.12 以降へ更新する。（非推奨の旧xmldomパッケージには修正版がないため移行を検討する）

#### References
- https://github.com/xmldom/xmldom/commit/4664386e4f4d99d17b416a151dbe8323e245284b
- https://github.com/xmldom/xmldom/commit/6c3fb5ffeafe7901ec928ce9010988dd716c94a0
- https://github.com/xmldom/xmldom/pull/1071
- https://github.com/xmldom/xmldom/pull/1072
- https://github.com/xmldom/xmldom/releases/tag/0.8.15

### [CVE-2026-83611](https://github.com/xmldom/xmldom/commit/4430189660b0d380ee9c9ee7550a1358688e8828)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-83611
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-02 00:17:39 JST
- 更新日: 2026-09-02 00:17:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: xmldomのDOMParser.parseFromString()において、不正な形式の終了タグ以降のコンテンツを適切に検証せずサイレントに破棄・受け入れる問題。
- 影響: 信頼前の構文妥当性チェックをバイパスされる可能性がある。
- 推奨対応: @xmldom/xmldom バージョン 0.8.15 または 0.9.12 以降へ更新する。（非推奨の旧xmldomパッケージには修正版がないため移行を検討する）

#### References
- https://github.com/xmldom/xmldom/commit/4430189660b0d380ee9c9ee7550a1358688e8828
- https://github.com/xmldom/xmldom/commit/7b2ec67e1750daadd0bb06c92e875e726544a362
- https://github.com/xmldom/xmldom/pull/1071
- https://github.com/xmldom/xmldom/pull/1072
- https://github.com/xmldom/xmldom/releases/tag/0.8.15

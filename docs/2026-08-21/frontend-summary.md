# Frontend CVE Summary (2026-08-21)

## Overview

- 取得日時: 2026-08-21 07:39:17 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 7
- Critical: 0
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-40345](https://github.com/RebeccaStevens/deepmerge-ts/commit/398492757b3f22a0d7d89b09ce1ae9cd32806c9a)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-40345
- 関連キーワード: typescript, javascript, gin, node.js
- 影響製品: -
- 公開日: 2026-08-21 02:17:29 JST
- 更新日: 2026-08-21 02:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: deepmerge-tsにおける循環参照オブジェクトマージ時のスタックオーバーフローの脆弱性。8.0.0未満のバージョンで自己参照を持つプロパティ同士を再帰的にマージする際、無限再帰が発生します。
- 影響: 攻撃者が制御する自己参照オブジェクトを処理させることで、Node.jsでRangeErrorが発生し、プロセスがクラッシュまたは繰り返しのワーカー再起動を引き起こす可能性があります。
- 推奨対応: deepmerge-ts 8.0.0 以降へアップデートしてください。

#### References
- https://github.com/RebeccaStevens/deepmerge-ts/commit/398492757b3f22a0d7d89b09ce1ae9cd32806c9a
- https://github.com/RebeccaStevens/deepmerge-ts/pull/707
- https://github.com/RebeccaStevens/deepmerge-ts/releases/tag/v8.0.0
- https://github.com/RebeccaStevens/deepmerge-ts/security/advisories/GHSA-ggr8-5vv4-36mx

### [CVE-2026-68921](https://github.com/dicebear/dicebear/commit/922946d738c4e77ab6c412e27ede75941fec4b59)

> **Frontend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-68921
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-08-21 06:17:07 JST
- 更新日: 2026-08-21 06:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DiceBearにおけるSVG属性へのエスケープ処理不足によるクロスサイトスクリプティング（XSS）の脆弱性。一部のオプション値（rotate, fontSize, fontWeight）がXMLエスケープされずに挿入されます。
- 影響: 生成されたSVGが直接表示されたりインライン挿入されたりした際、任意のSVGマークアップやスクリプトを実行される可能性があります。
- 推奨対応: @dicebear/core および @dicebear/initials を 9.4.3 以降へアップデートしてください。

#### References
- https://github.com/dicebear/dicebear/commit/922946d738c4e77ab6c412e27ede75941fec4b59
- https://github.com/dicebear/dicebear/releases/tag/v9.4.3
- https://github.com/dicebear/dicebear/security/advisories/GHSA-gcr2-9v8m-gq45

### [CVE-2026-72861](https://github.com/appwrite/templates)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-72861
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-08-21 05:17:46 JST
- 更新日: 2026-08-21 05:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Appwriteのgithub-issue-botテンプレートにおけるWebhook署名検証の論理不備。X-Hub-Signature-256ヘッダーが存在しない場合にHMAC検証をスキップして成功と判定してしまいます。
- 影響: 未認証の第三者が署名のないリクエストを送信し、設定されたGITHUB_TOKENを使用して任意のGitHubリポジトリやIssueにコメントを投稿できる可能性があります。
- 推奨対応: 該当テンプレートのコードを更新し、ヘッダーが存在しない場合の検証ロジックを修正してください。

#### References
- https://github.com/appwrite/templates
- https://github.com/appwrite/templates/blob/1.1.2/node-typescript/github-issue-bot/src/github.ts
- https://github.com/appwrite/templates/blob/1.1.2/node/github-issue-bot/src/github.js
- https://github.com/appwrite/templates/blob/1.1.2/node/github-issue-bot/src/main.js
- https://github.com/appwrite/templates/issues/350

### [CVE-2026-73220](https://github.com/cvat-ai/cvat/commit/33aaa1987ea89a4d229bf4c19fcbe6b04ed55b42)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-73220
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-21 00:18:37 JST
- 更新日: 2026-08-21 02:19:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CVATの音声タスク注釈ガイド表示における格納型クロスサイトスクリプティング（XSS）の脆弱性。Markdownの描画処理でサニタイズプラグインが適用されていません。
- 影響: 悪意あるスクリプトを含んだ注釈ガイドが保存され、他のユーザーがそれを開いた際に被害者の権限で任意のAPIリクエストが実行される可能性があります。
- 推奨対応: CVAT 2.70.0 以降へアップデートしてください。

#### References
- https://github.com/cvat-ai/cvat/commit/33aaa1987ea89a4d229bf4c19fcbe6b04ed55b42
- https://github.com/cvat-ai/cvat/pull/10893
- https://github.com/cvat-ai/cvat/releases/tag/v2.70.0
- https://github.com/cvat-ai/cvat/security/advisories/GHSA-chxx-45vm-qhc9

### [CVE-2026-65842](https://github.com/udecode/plate/commit/21aa59926f4bbd421027354823cca09c6700ed73)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-65842
- 関連キーワード: shadcn/ui
- 影響製品: -
- 公開日: 2026-08-21 02:19:23 JST
- 更新日: 2026-08-21 02:19:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Plate (@platejs/docx-io) におけるHTMLからDOCX変換時のSSRF（サーバーサイドリクエストフォージェリ）の脆弱性。リモート画像URLの取得処理で入力値の不十分な検証が行われています。
- 影響: 内部ネットワークリソースへのリクエストを誘発され、生成されたDOCXファイル経由で応答内容が漏洩したり、リソースが過剰消費されたりする可能性があります。
- 推奨対応: @platejs/docx-io（または関連パッケージ）を 53.3.2 以降へアップデートしてください。

#### References
- https://github.com/udecode/plate/commit/21aa59926f4bbd421027354823cca09c6700ed73
- https://github.com/udecode/plate/pull/5053
- https://github.com/udecode/plate/releases/tag/v53.3.2
- https://github.com/udecode/plate/security/advisories/GHSA-4q39-2jhr-7qx8

### [CVE-2026-54616](https://github.com/M2Team/NanaZip/commit/733e8570d2ba96c3e52aab44f5fd886775d5952f)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-54616
- 関連キーワード: swr
- 影響製品: -
- 公開日: 2026-08-21 02:18:18 JST
- 更新日: 2026-08-21 05:17:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NanaZipにおけるSquashfsデータのデコード処理に伴う境界外読み取りの脆弱性。LZ4デコードの負のエラー値を誤処理し、不正なバッファサイズを信頼して処理を継続します。
- 影響: ヒープ領域のメモリデータが抽出されたファイルに漏洩する可能性や、プロセスがクラッシュする可能性があります。
- 推奨対応: NanaZip 安定版 6.0.1698.0 以降、またはプレビュー版 6.5.1742.0 以降へアップデートしてください。

#### References
- https://github.com/M2Team/NanaZip/commit/733e8570d2ba96c3e52aab44f5fd886775d5952f
- https://github.com/M2Team/NanaZip/commit/ce0322a1932e16a53e4a13e48bc61804c7826956
- https://github.com/M2Team/NanaZip/releases/tag/6.0.1698.0
- https://github.com/M2Team/NanaZip/releases/tag/6.5.1742.0
- https://github.com/M2Team/NanaZip/security/advisories/GHSA-95x5-qvvm-hmfp

### [CVE-2026-67446](https://github.com/axllent/mailpit/commit/6bcb6337838b542d53c348e38c7977f569b6db35)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-67446
- 関連キーワード: vue, go, gin
- 影響製品: -
- 公開日: 2026-08-21 06:17:07 JST
- 更新日: 2026-08-21 06:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mailpitにおける画像サムネイル生成時のリソース消費（DoS）の脆弱性。添付画像を全デコードする前にサイズやメモリ使用量の検証が行われません。
- 影響: 解像度が極端に大きい悪意ある画像を送信・閲覧させることで、CPUやメモリを大量消費させサービスを停止・遅延させる可能性があります。
- 推奨対応: Mailpit 1.30.4 以降へアップデートしてください。

#### References
- https://github.com/axllent/mailpit/commit/6bcb6337838b542d53c348e38c7977f569b6db35
- https://github.com/axllent/mailpit/releases/tag/v1.30.4
- https://github.com/axllent/mailpit/security/advisories/GHSA-75mr-qw9x-3r39

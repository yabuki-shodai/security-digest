# Backend CVE Summary (2026-08-26)

## Overview

- 取得日時: 2026-08-26 07:39:48 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 22
- Critical: 6
- High: 9
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-55580](https://github.com/sonirico/mcp-shell/commit/f31377fce6ec31114e5a4398c0e5270552bce09f)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-55580
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-26 01:16:55 JST
- 更新日: 2026-08-26 02:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: シェル実行MCPサーバー「mcp-shell」において、設定ファイル未指定時にセキュリティ検証が無効化される不具合。
- 影響: デフォルト構成等で起動した場合、接続元（LLM等）から制限なく任意のOSコマンドを実行される可能性がある。
- 推奨対応: mcp-shell を 0.6.0 以降へ更新し、セキュリティ設定ファイルを適切に適用して起動する。

#### References
- https://github.com/sonirico/mcp-shell/commit/f31377fce6ec31114e5a4398c0e5270552bce09f
- https://github.com/sonirico/mcp-shell/pull/16
- https://github.com/sonirico/mcp-shell/releases/tag/v0.6.0
- https://github.com/sonirico/mcp-shell/security/advisories/GHSA-f5pj-2738-996m
- https://github.com/sonirico/mcp-shell/security/advisories/GHSA-f5pj-2738-996m

### [CVE-2026-55581](https://github.com/sonirico/mcp-shell/commit/f31377fce6ec31114e5a4398c0e5270552bce09f)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-55581
- 関連キーワード: go, docker
- 影響製品: -
- 公開日: 2026-08-26 01:16:55 JST
- 更新日: 2026-08-26 04:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: シェル実行MCPサーバー「mcp-shell」において、コマンド検証時にシェル実行オプション（`-c`）がチェックされない不具合。
- 影響: 許可リスト内のバイパス指定（例: `/bin/bash -c`）を利用され、制限を潜り抜けて任意のシェルコマンドを実行される可能性がある。
- 推奨対応: mcp-shell を 0.6.0 以降のバージョンへ更新する。

#### References
- https://github.com/sonirico/mcp-shell/commit/f31377fce6ec31114e5a4398c0e5270552bce09f
- https://github.com/sonirico/mcp-shell/pull/16
- https://github.com/sonirico/mcp-shell/releases/tag/v0.6.0
- https://github.com/sonirico/mcp-shell/security/advisories/GHSA-3x77-wg38-92r3
- https://github.com/sonirico/mcp-shell/security/advisories/GHSA-3x77-wg38-92r3

### [CVE-2026-55582](https://github.com/sonirico/mcp-shell/commit/f31377fce6ec31114e5a4398c0e5270552bce09f)

> **Backend** / **HIGH** / CVSS: **8.4** / KEV: **no**

- タイトル: CVE-2026-55582
- 関連キーワード: go, docker
- 影響製品: -
- 公開日: 2026-08-26 01:16:55 JST
- 更新日: 2026-08-26 01:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: mcp-shell 0.6.0 未満において、`shell_exec` ツールで使用される `/usr/bin/git` の引数に対する制限・検証が不足している不具合。
- 影響: MCP 接続を持つ攻撃者が git のエイリアス機能を悪用し、mcp-shell プロセスの権限で任意の OS コマンドを実行できる可能性があります。
- 推奨対応: mcp-shell を 0.6.0 以降のバージョンに更新してください。

#### References
- https://github.com/sonirico/mcp-shell/commit/f31377fce6ec31114e5a4398c0e5270552bce09f
- https://github.com/sonirico/mcp-shell/pull/16
- https://github.com/sonirico/mcp-shell/releases/tag/v0.6.0
- https://github.com/sonirico/mcp-shell/security/advisories/GHSA-74hp-mggr-hv58

### [CVE-2026-55609](https://github.com/BruceJqs/public_exp/issues/32)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-55609
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-26 04:16:50 JST
- 更新日: 2026-08-26 04:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: sublinear-time-solver（1.6.0 未満）および consciousness-explorer（1.1.2 未満）の MCP ツールにおけるファイルパスパラメータの検証不足（ディレクトリトラバーサル）。
- 影響: MCP ツールを呼び出せる攻撃者により、サーバープロセスがアクセス可能な任意のファイルの閲覧、書き込み、上書きが行われ、情報漏洩やサービス停止を引き起こす可能性があります。
- 推奨対応: consciousness-explorer を 1.1.2 以降、sublinear-time-solver を 1.6.0 以降に更新してください。

#### References
- https://github.com/BruceJqs/public_exp/issues/32
- https://github.com/ruvnet/sublinear-time-solver/commit/a701296e363192be863e79d788fa268095e3d229
- https://github.com/ruvnet/sublinear-time-solver/commit/ea9a212b69e4449ec443fe088a7aec7546f70b4a
- https://github.com/ruvnet/sublinear-time-solver/issues/19
- https://github.com/ruvnet/sublinear-time-solver/pull/20

### [CVE-2026-79775](https://github.com/rclone/rclone/security/advisories/GHSA-6jcg-q3wp-x2f4)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-79775
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-26 01:17:29 JST
- 更新日: 2026-08-26 02:18:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: rclone v1.72.0〜v1.74.4 の SquashFS パーサーにおける、スーパーブロックおよびメタデータ値の検証不足。
- 影響: 悪意を持って作成された SquashFS イメージの読み込み時にパニックや無限ループが引き起こされ、rclone プロセスや SFTP サーバー全体が停止する（DoS）可能性があります。
- 推奨対応: rclone を v1.75.0 以降に更新してください。

#### References
- https://github.com/rclone/rclone/security/advisories/GHSA-6jcg-q3wp-x2f4
- https://www.vulncheck.com/advisories/rclone-archive-backend-squashfs-parser-denial-of-service
- https://github.com/rclone/rclone/security/advisories/GHSA-6jcg-q3wp-x2f4

### [CVE-2026-79777](https://github.com/rclone/rclone/security/advisories/GHSA-gwfq-86j8-7qhv)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-79777
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-26 01:17:29 JST
- 更新日: 2026-08-26 01:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: rclone v1.75.0 未満の Remote Control (RC) API エラー応答における、パニック時の Go スタックトレース出力。
- 影響: 意図的にパニックを発生させることで、内部ファイルパス、モジュールバージョン、メモリ構造などの機密情報が攻撃者に漏洩する可能性があります。
- 推奨対応: rclone を v1.75.0 以降に更新してください。

#### References
- https://github.com/rclone/rclone/security/advisories/GHSA-gwfq-86j8-7qhv
- https://www.vulncheck.com/advisories/rclone-before-information-disclosure-via-rc-api

### [CVE-2026-79778](https://github.com/rclone/rclone/security/advisories/GHSA-3x6r-wxxg-53vv)

> **Backend** / **MEDIUM** / CVSS: **6.0** / KEV: **no**

- タイトル: CVE-2026-79778
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-26 01:17:29 JST
- 更新日: 2026-08-26 02:18:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: rclone v1.75.0 未満の WebDAV TUS 作成ハンドラーにおける、トランスポートエラー確認前の nil レスポンス参照。
- 影響: アップロード中の接続リセット等によりパニックが発生し、長期実行中のプロセスが不意に停止するなどの DoS 状態に陥る可能性があります。
- 推奨対応: rclone を v1.75.0 以降に更新してください。

#### References
- https://github.com/rclone/rclone/security/advisories/GHSA-3x6r-wxxg-53vv
- https://www.vulncheck.com/advisories/rclone-before-denial-of-service-via-tus-nil-response-panic
- https://github.com/rclone/rclone/security/advisories/GHSA-3x6r-wxxg-53vv

### [CVE-2026-55546](https://github.com/QWED-AI/qwed-mcp/commit/362e61892052e250c56cb1ee852024d6f98c467b)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-55546
- 関連キーワード: python, gin, express
- 影響製品: -
- 公開日: 2026-08-26 01:16:55 JST
- 更新日: 2026-08-26 04:16:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: QWED-MCP 0.2.1 未満の `verify_math_expression()` において、入力文字列を十分な名前空間制限なしに SymPy の `parse_expr()` に渡してしまう問題。
- 影響: ダウンストリーム連携で信頼できない入力が渡された場合、qwed-mcp プロセスの権限で任意の OS コマンド実行やデータ奪取が行われる可能性があります。
- 推奨対応: QWED-MCP を 0.2.1 以降に更新してください。

#### References
- https://github.com/QWED-AI/qwed-mcp/commit/362e61892052e250c56cb1ee852024d6f98c467b
- https://github.com/QWED-AI/qwed-mcp/pull/22
- https://github.com/QWED-AI/qwed-mcp/releases/tag/v0.2.1
- https://github.com/QWED-AI/qwed-mcp/security/advisories/GHSA-mw6r-2hvm-4rp2
- https://github.com/QWED-AI/qwed-mcp/security/advisories/GHSA-mw6r-2hvm-4rp2

### [CVE-2026-45018](https://github.com/Chainlit/chainlit/blob/2.12.0/docs/security-advisory-2026-mcp.md#spl-2026-001--command-injection-via-mcp-stdio)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-45018
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-26 05:16:55 JST
- 更新日: 2026-08-26 05:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Chainlit 2.4.0rc0〜2.12.0 未満で MCP 機能が有効な場合、未認証でアクセス可能な `POST /mcp` エンドポイントでコマンド引数の検証が不十分な不具合。
- 影響: 未認証の遠隔攻撃者が `npx` などの実行可能ファイルの引数を悪用し、Chainlit プロセスの権限で任意シェルコマンドを実行する可能性があります。
- 推奨対応: Chainlit を 2.12.0 以降に更新してください。

#### References
- https://github.com/Chainlit/chainlit/blob/2.12.0/docs/security-advisory-2026-mcp.md#spl-2026-001--command-injection-via-mcp-stdio
- https://github.com/Chainlit/chainlit/commit/0565fd0eccb915fce159929598b053ed79f6e0c9
- https://github.com/Chainlit/chainlit/releases/tag/2.12.0
- https://github.com/Chainlit/chainlit/security/advisories/GHSA-w3fx-mc44-mf6j
- https://github.com/Chainlit/chainlit/security/advisories/GHSA-w3fx-mc44-mf6j

### [CVE-2026-78379](https://aws.amazon.com/security/security-bulletins/2026-089-aws/)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-78379
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-26 04:16:54 JST
- 更新日: 2026-08-26 05:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Amazon Strands Agents Tools 0.8.5 未満の `python_repl` ツールにおける、LLM プロンプト入力の無害化処理の不備。
- 影響: 人間の承認（同意）プロセスをバイパスされ、エージェントが動作するホスト上で任意の Python コードを実行される可能性があります。
- 推奨対応: Amazon Strands Agents Tools を 0.8.5 以降に更新してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-089-aws/
- https://pypi.org/project/strands-agents-tools/0.8.5/

### [CVE-2026-55585](https://github.com/QWED-AI/qwed-verification/commit/6066b68c0c4f4cc2c3771824822aaa864d082ef8)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-55585
- 関連キーワード: python, express
- 影響製品: -
- 公開日: 2026-08-26 02:17:32 JST
- 更新日: 2026-08-26 02:17:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: QWED 5.1.2 未満において、`POST /verify/math` やバッチ処理で数式文字列のサニタイズや名前空間の制限を怠ったまま SymPy の `parse_expr()` を実行する問題。
- 影響: 有効な API キーを持つ攻撃者によって、API サーバープロセス上で任意の Python コードやコマンドを実行される可能性があります。
- 推奨対応: qwed を 5.1.2 以降に更新してください。

#### References
- https://github.com/QWED-AI/qwed-verification/commit/6066b68c0c4f4cc2c3771824822aaa864d082ef8
- https://github.com/QWED-AI/qwed-verification/commit/dc9d4db72ca4b4ae3f96d0e6a0c27a9e38a06f61
- https://github.com/QWED-AI/qwed-verification/pull/200
- https://github.com/QWED-AI/qwed-verification/security/advisories/GHSA-q27q-98j4-9pfv

### [CVE-2026-45019](https://github.com/Chainlit/chainlit/blob/2.12.0/docs/security-advisory-2026-mcp.md#spl-2026-002--ssrf-via-mcp-streamable-http--sse)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-45019
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-08-26 05:16:55 JST
- 更新日: 2026-08-26 05:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Chainlit 2.4.0rc0〜2.12.0 未満で MCP 機能が有効な場合、未認証の `POST /mcp` エンドポイントで渡される URL やヘッダーの不完全な検証による SSRF の不具合。
- 影響: 攻撃者によって、Chainlit サーバーから内部ネットワークやクラウドメタデータエンドポイント等への不正なリクエストを発生させられる可能性があります。
- 推奨対応: Chainlit を 2.12.0 以降に更新してください。

#### References
- https://github.com/Chainlit/chainlit/blob/2.12.0/docs/security-advisory-2026-mcp.md#spl-2026-002--ssrf-via-mcp-streamable-http--sse
- https://github.com/Chainlit/chainlit/commit/0565fd0eccb915fce159929598b053ed79f6e0c9
- https://github.com/Chainlit/chainlit/releases/tag/2.12.0
- https://github.com/Chainlit/chainlit/security/advisories/GHSA-hvfh-5mj3-5f3j

### [CVE-2026-55620](https://github.com/GOVCERT-LU/eml_parser/commit/746a69f86443eb0b6a47f77db3cfe727c21f92b3)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-55620
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-26 04:16:50 JST
- 更新日: 2026-08-26 04:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: eml_parserのReceivedヘッダー解析処理において、ネストされた括弧コメントの除去に使用される正規表現の処理時間に二乗時間の計算量が向上する不備が存在します。
- 影響: 細工されたEMLファイルを処理させることで高負荷なCPU消費が発生し、サービスの遅延や応答停止を引き起こす可能性があります。
- 推奨対応: eml_parser 3.0.2以降にアップデートしてください。

#### References
- https://github.com/GOVCERT-LU/eml_parser/commit/746a69f86443eb0b6a47f77db3cfe727c21f92b3
- https://github.com/GOVCERT-LU/eml_parser/pull/90
- https://github.com/GOVCERT-LU/eml_parser/releases/tag/v3.0.2
- https://github.com/GOVCERT-LU/eml_parser/security/advisories/GHSA-g7gc-gmgp-wgqg

### [CVE-2026-77357](https://github.com/mesop-dev/mesop/commit/2b8e7f2c349c9e2eec202f46b07bada83061ce2d)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-77357
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-26 06:17:46 JST
- 更新日: 2026-08-26 06:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mesopのデバッグモードで提供されるGET /hot-reloadエンドポイントにおいて、ユーザー指定のパラメータ処理に起因するループ処理の制限不備が存在します。
- 影響: 未認証の第三者によりワーカープールが枯渇させられ、サーバーの応答停止やクラッシュを引き起こす可能性があります。
- 推奨対応: Mesop 1.3.3以降にアップデートするか、本番環境でのデバッグモードの使用を控えてください。

#### References
- https://github.com/mesop-dev/mesop/commit/2b8e7f2c349c9e2eec202f46b07bada83061ce2d
- https://github.com/mesop-dev/mesop/releases/tag/v1.3.3
- https://github.com/mesop-dev/mesop/security/advisories/GHSA-8p72-497j-83mx

### [CVE-2026-55618](https://github.com/GOVCERT-LU/eml_parser/commit/746a69f86443eb0b6a47f77db3cfe727c21f92b3)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-55618
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-26 04:16:50 JST
- 更新日: 2026-08-26 04:16:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: eml_parserのclean_found_uri関数において、HTMLエンティティのデコード前にURL検証が行われるため、エンコードされた一部の正規URLが不当に除外される処理の不備が存在します。
- 影響: セキュリティ製品等において悪意のあるURLやドメインが抽出漏れし、脅威の検知や解析を回避される可能性があります。
- 推奨対応: eml_parser 3.0.2以降にアップデートしてください。

#### References
- https://github.com/GOVCERT-LU/eml_parser/commit/746a69f86443eb0b6a47f77db3cfe727c21f92b3
- https://github.com/GOVCERT-LU/eml_parser/pull/90
- https://github.com/GOVCERT-LU/eml_parser/releases/tag/v3.0.2
- https://github.com/GOVCERT-LU/eml_parser/security/advisories/GHSA-fxgq-9m89-cxj9

### [CVE-2026-55619](https://github.com/GOVCERT-LU/eml_parser/commit/746a69f86443eb0b6a47f77db3cfe727c21f92b3)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-55619
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-26 04:16:50 JST
- 更新日: 2026-08-26 05:16:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: eml_parserのヘッダー解析処理において、深層にネストされたコメント構造に対するRecursionError例外が捕捉されない問題が存在します。
- 影響: 攻撃者によって細工されたEMLファイルを受け取った際、メール解析パイプライン全体が停止させられる可能性があります。
- 推奨対応: eml_parser 3.0.2以降にアップデートしてください。

#### References
- https://github.com/GOVCERT-LU/eml_parser/commit/746a69f86443eb0b6a47f77db3cfe727c21f92b3
- https://github.com/GOVCERT-LU/eml_parser/pull/90
- https://github.com/GOVCERT-LU/eml_parser/releases/tag/v3.0.2
- https://github.com/GOVCERT-LU/eml_parser/security/advisories/GHSA-m66c-fw79-6359

### [CVE-2026-62986](https://github.com/AcademySoftwareFoundation/openexr/commit/36ff0968de08d7ae80792f9f53402f93433207bb)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-62986
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-26 04:16:52 JST
- 更新日: 2026-08-26 05:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PyOpenEXRにおいて、プレフィックス付きチャンネルのオフセット計算に誤りがあり、未初期化メモリがPython側に返却される不備が存在します。
- 影響: 細工されたEXRファイルを処理した際に、ヒープ領域に存在する古いデータや機密情報が漏洩する可能性があります。
- 推奨対応: 修正されたバージョンのPyOpenEXR（OpenEXR）へアップデートしてください。

#### References
- https://github.com/AcademySoftwareFoundation/openexr/commit/36ff0968de08d7ae80792f9f53402f93433207bb
- https://github.com/AcademySoftwareFoundation/openexr/commit/5105809507ba572d8cad12ec9f5a5c9d378354b9
- https://github.com/AcademySoftwareFoundation/openexr/commit/5a534e2228c853034e5cb9d2599ebf82f48f51b0
- https://github.com/AcademySoftwareFoundation/openexr/security/advisories/GHSA-pf59-r2mc-x746

### [CVE-2026-68514](https://github.com/AcademySoftwareFoundation/openexr/commit/c1f3ec0d91cfa5a8035ecd00920835ac76e01640)

> **Backend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-68514
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-26 05:17:02 JST
- 更新日: 2026-08-26 05:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PyOpenEXRにおいて、特定構成のレイヤー名・チャンネル名を持つディープスキャンラインEXRファイルを読み込む際のメモリ割り当て計算に不備が存在します。
- 影響: 細工されたファイルを読み込ませることでヒープ領域外への書き込みが発生し、クラッシュや任意のコード実行につながる可能性があります。
- 推奨対応: 修正されたバージョンのPyOpenEXR（OpenEXR）へアップデートしてください。

#### References
- https://github.com/AcademySoftwareFoundation/openexr/commit/c1f3ec0d91cfa5a8035ecd00920835ac76e01640
- https://github.com/AcademySoftwareFoundation/openexr/commit/d134e3cd81a2e343f2919e86bf949f576b1ab16a
- https://github.com/AcademySoftwareFoundation/openexr/security/advisories/GHSA-mw28-66qc-c883

### [CVE-2026-15310](https://github.com/python/cpython/issues/156002)

> **Backend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-15310
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-08-26 00:16:30 JST
- 更新日: 2026-08-26 03:17:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Pythonにおける特定の圧縮方式（bzip/LZMA/Zstandard）を用いたZIPファイルの展開処理において、ファイル側のサイズ指定に基づくメモリ事前割り当て処理に不備が存在します。
- 影響: 細工されたZIPファイルを解凍した際に過剰なメモリが消費され、メモリ枯渇やサービス停止を引き起こす可能性があります。
- 推奨対応: 修正版のPython環境への更新や、信頼できないZIPファイルの展開処理の見直しを検討してください。

#### References
- https://github.com/python/cpython/issues/156002
- https://github.com/python/cpython/pull/156003
- https://mail.python.org/archives/list/security-announce@python.org/thread/YUHXURX2WZGKGNA4ANYBQS2VZRYQ5JNK/

### [CVE-2026-79782](https://github.com/rclone/rclone/security/advisories/GHSA-gx4c-2hqx-cw2r)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-79782
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-26 01:17:30 JST
- 更新日: 2026-08-26 01:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: rcloneにおいて、S3リダイレクトに伴い同一ホスト上でHTTPSからHTTPへ通信が切り替わる際、認証用ヘッダーが削除されない不備が存在します。
- 影響: 暗号化されていない平文のHTTP通信を盗聴されることで、AWS STSセッショントークンなどの認証情報が漏洩する可能性があります。
- 推奨対応: rclone 1.74.4以降にアップデートしてください。

#### References
- https://github.com/rclone/rclone/security/advisories/GHSA-gx4c-2hqx-cw2r
- https://www.vulncheck.com/advisories/rclone-before-security-token-disclosure-via-https-to-http-redirect

### [CVE-2026-79787](https://github.com/Alluxio/alluxio)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-79787
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-08-26 04:16:54 JST
- 更新日: 2026-08-26 04:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AlluxioのS3 RESTプロキシのデフォルト設定において、AWS Signature Version 4の署名検証が行われない不備が存在します。
- 影響: 未認証の第三者が認証ヘッダー内のユーザー名を偽装し、任意アカウントの権限でデータの参照・書き込み・削除を行う可能性があります。
- 推奨対応: 最新版へのアップデートまたは署名検証を有効化する設定の見直しを行ってください。

#### References
- https://github.com/Alluxio/alluxio
- https://github.com/Alluxio/alluxio/blob/v2.9.5/core/server/proxy/src/main/java/alluxio/proxy/s3/S3RestUtils.java
- https://github.com/Alluxio/alluxio/issues/18755
- https://www.vulncheck.com/advisories/alluxio-through-2.9.5-s3-rest-proxy-authentication-bypass-via-unverified-request-signature
- https://github.com/Alluxio/alluxio/issues/18755

### [CVE-2026-55536](https://github.com/MervinPraison/PraisonAI/commit/2f9677abb2ea68eab864ee8b6a828fd0141612e1)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-55536
- 関連キーワード: gin, express
- 影響製品: -
- 公開日: 2026-08-26 01:16:54 JST
- 更新日: 2026-08-26 01:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PraisonAIのBrowser ServerにおけるChrome拡張機能のオリジン検証（正規表現のチェック）にアンカーが不足している不備が存在します。
- 影響: 第三者がオリジン検証を迂回してWebSocket接続を確立し、不正なブラウザ自動化操作を実行する可能性があります。
- 推奨対応: praisonai 4.6.58以降にアップデートしてください。

#### References
- https://github.com/MervinPraison/PraisonAI/commit/2f9677abb2ea68eab864ee8b6a828fd0141612e1
- https://github.com/MervinPraison/PraisonAI/releases/tag/v4.6.58
- https://github.com/MervinPraison/PraisonAI/security/advisories/GHSA-6g6r-q6gw-w8fg

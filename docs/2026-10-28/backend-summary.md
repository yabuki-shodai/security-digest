# Backend CVE Summary (2026-10-28)

## Overview

- 取得日時: 2026-10-28 10:14:49 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 24
- Critical: 3
- High: 14
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-116676](https://github.com/runatlantis/atlantis/commit/8dd22b4d0a9d7c129fdbf6a3398dd1c4cf8c3a59)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-116676
- 関連キーワード: go, golang, terraform
- 影響製品: -
- 公開日: 2026-10-28 03:17:35 JST
- 更新日: 2026-10-28 03:17:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Atlantisにおけるワークスペース名の処理不備によるコマンドインジェクションの脆弱性。
- 影響: プルリクエストのワークスペース名にシェルメタ文字を含めることで、Atlantisのサービスアカウント権限で任意コマンドが実行される可能性があります。
- 推奨対応: Atlantisを修正済みバージョン（0.47.1より後のバージョンなど）へアップデートしてください。

#### References
- https://github.com/runatlantis/atlantis/commit/8dd22b4d0a9d7c129fdbf6a3398dd1c4cf8c3a59
- https://github.com/runatlantis/atlantis/commit/f04df0d53f0544d9eb6f5026dd8b74fbefd82ac8
- https://github.com/runatlantis/atlantis/pull/6792
- https://github.com/runatlantis/atlantis/releases/tag/v0.47.1
- https://github.com/runatlantis/atlantis/security/advisories/GHSA-rjh2-4xgw-p2hj

### [CVE-2026-116682](https://github.com/gtsteffaniak/filebrowser/commit/3c8c02414eefd3351ffe437fa39ff6eb150ffa67)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-116682
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-28 03:17:36 JST
- 更新日: 2026-10-28 03:17:36 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FileBrowser Quantumにおけるシンボリックリンクの不適切な検証による不認可ファイルアクセスの脆弱性。
- 影響: 許可されたスコープ外にあるサーバー上のファイルへアクセス・閲覧・ダウンロードされる可能性があります。
- 推奨対応: バージョン1.5.2-stableまたは2.0.1-beta以降へアップデートしてください。

#### References
- https://github.com/gtsteffaniak/filebrowser/commit/3c8c02414eefd3351ffe437fa39ff6eb150ffa67
- https://github.com/gtsteffaniak/filebrowser/commit/4126edeb07a015c3809a89249b283e07a4e50c38
- https://github.com/gtsteffaniak/filebrowser/pull/2795
- https://github.com/gtsteffaniak/filebrowser/pull/2800
- https://github.com/gtsteffaniak/filebrowser/releases/tag/v1.5.2-stable

### [CVE-2026-54462](https://github.com/knative/pkg/commit/52dbd5ece63fe6d2d340ecbebec160550f460818)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-54462
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-28 02:17:01 JST
- 更新日: 2026-10-28 02:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Knative pkgのWebフック受信部におけるリクエストサイズ制限欠如によるサービス拒否（DoS）の脆弱性。
- 影響: 過大なPOSTリクエストによりコントローラーがメモリ枯渇（OOM）を起こし、アドミッション制御機能が停止する可能性があります。
- 推奨対応: 修正が含まれる更新の適用、またはWebフック前でのリクエストサイズ制限の導入を検討してください。

#### References
- https://github.com/knative/pkg/commit/52dbd5ece63fe6d2d340ecbebec160550f460818
- https://github.com/knative/pkg/pull/3363
- https://github.com/knative/pkg/security/advisories/GHSA-2hw4-c9m4-f2fj

### [CVE-2026-116692](https://github.com/mlflow/mlflow/commit/a732443e695c3c677680c54320efc394c81654ab)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-116692
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-28 06:18:05 JST
- 更新日: 2026-10-28 06:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MLflowにおけるサードパーティ製スコアラーの不適切なデシリアライズに伴う任意コード実行の脆弱性。
- 影響: 攻撃者が配置したPythonモジュールが読み込まれ、サーバープロセス権限で任意コードが実行される可能性があります。認証が無効な環境では未認証で悪用される恐れがあります。
- 推奨対応: MLflowをバージョン3.17.0以降にアップデートしてください。

#### References
- https://github.com/mlflow/mlflow/commit/a732443e695c3c677680c54320efc394c81654ab
- https://github.com/mlflow/mlflow/pull/25906
- https://github.com/mlflow/mlflow/releases/tag/v3.17.0
- https://github.com/mlflow/mlflow/security/advisories/GHSA-26p8-2jq9-3vq9

### [CVE-2026-116672](https://github.com/authlib/authlib/commit/1bd2a313492ce0a4d0571c150730907aa3fc91ff)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-116672
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-28 02:16:59 JST
- 更新日: 2026-10-28 06:31:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Authlib (0.15〜1.9.1未満) の ClientConfigurationEndpoint 実装において、アクセストークンと対象クライアントの紐付け検証が不足している脆弱性。
- 影響: 有効なトークンを持つ攻撃者が他クライアントの登録情報を閲覧・変更・削除でき、認可コードの奪取やDoSに繋がる可能性があります。
- 推奨対応: Authlib 1.9.1 以降に更新してください。

#### References
- https://github.com/authlib/authlib/commit/1bd2a313492ce0a4d0571c150730907aa3fc91ff
- https://github.com/authlib/authlib/releases/tag/v1.9.1
- https://github.com/authlib/authlib/security/advisories/GHSA-c73q-w75p-j82v

### [CVE-2026-116684](https://github.com/modelcontextprotocol/python-sdk/commit/0c9136841ff092987a20700ff9c2c9789bda2f40)

> **Backend** / **MEDIUM** / CVSS: **6.8** / KEV: **no**

- タイトル: CVE-2026-116684
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-28 05:17:13 JST
- 更新日: 2026-10-28 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Model Context Protocol Python SDK (1.10.0〜1.30.0未満、2.2.0未満) の TokenVerifier における aud (オーディエンス) の検証不備。
- 影響: 他サービス向けに発行された有効なトークンを用いて意図しない MCP サーバーへ認証・アクセスされる（リソース混同）可能性があります。
- 推奨対応: バージョン 1.30.0 または 2.2.0 以降に更新してください。

#### References
- https://github.com/modelcontextprotocol/python-sdk/commit/0c9136841ff092987a20700ff9c2c9789bda2f40
- https://github.com/modelcontextprotocol/python-sdk/commit/8c2fa6eabacde869d75568e33b9d466b58c2f512
- https://github.com/modelcontextprotocol/python-sdk/pull/3447
- https://github.com/modelcontextprotocol/python-sdk/pull/3451
- https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0

### [CVE-2026-57203](https://github.com/asterisk/asterisk/commit/022407ec47adebe27b7ec8bcf5626e5a02fe1551)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-57203
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-28 07:17:27 JST
- 更新日: 2026-10-28 07:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Asterisk の ast_loggrabber が書き込み権限のゆるい /tmp ディレクトリから Python スクリプトを実行する脆弱性。
- 影響: サーバー上にローカルアクセスを持つ攻撃者が悪意あるスクリプトを配置し、管理者がツール実行時に権限昇格やコード実行を行う可能性があります。
- 推奨対応: Asterisk 20.20.1, 21.12.3, 22.10.1, 23.4.1、または Certified Asterisk 20.7-cert11, 22.8-cert3 以降に更新してください。

#### References
- https://github.com/asterisk/asterisk/commit/022407ec47adebe27b7ec8bcf5626e5a02fe1551
- https://github.com/asterisk/asterisk/commit/a51c4e3d6bccce4bc4226c43e78952573a62f165
- https://github.com/asterisk/asterisk/commit/ba8e5bdecd5280fc0ab230df59e41ea21b3a052f
- https://github.com/asterisk/asterisk/commit/bd63fe121d0e86867863bd98b5771e592273b035
- https://github.com/asterisk/asterisk/commit/c0fc2ae54cb6289a48a80333432f5fdf5a40c7de

### [CVE-2026-116685](https://github.com/modelcontextprotocol/python-sdk/commit/2106335745563b2321b8c73fef2c12903d00aa6e)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-116685
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-28 05:17:13 JST
- 更新日: 2026-10-28 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Model Context Protocol Python SDK (1.8.0〜1.30.0未満、2.2.0未満) の HTTP クライアント等で、異オリジンへのリダイレクト時に認証情報等が転送される問題。
- 影響: リダイレクト先を攻撃者に制御された場合、カスタム認証ヘッダーやリクエストボディが漏洩する可能性があります。
- 推奨対応: バージョン 1.30.0 または 2.2.0 以降に更新してください。

#### References
- https://github.com/modelcontextprotocol/python-sdk/commit/2106335745563b2321b8c73fef2c12903d00aa6e
- https://github.com/modelcontextprotocol/python-sdk/commit/c6762e821c527925f0b617db216d00fbd1d0bf99
- https://github.com/modelcontextprotocol/python-sdk/pull/3397
- https://github.com/modelcontextprotocol/python-sdk/pull/3448
- https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0

### [CVE-2026-116686](https://github.com/modelcontextprotocol/python-sdk/commit/5ebdfed4060d8e5b11b8e2348f86bad4d1fb8836)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-116686
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-28 05:17:13 JST
- 更新日: 2026-10-28 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Model Context Protocol Python SDK (1.10.0〜1.30.0未満、2.2.0未満) が outputSchema 内の未解決 $ref を同期的に外部取得する脆弱性。
- 影響: 悪意あるサーバーからのレスポンスにより、盲目的リクエスト送信（SSRF）、ローカルファイル読み取り、またはセッションのハング（DoS）が引き起こされる可能性があります。
- 推奨対応: バージョン 1.30.0 または 2.2.0 以降に更新してください。

#### References
- https://github.com/modelcontextprotocol/python-sdk/commit/5ebdfed4060d8e5b11b8e2348f86bad4d1fb8836
- https://github.com/modelcontextprotocol/python-sdk/commit/6705402e246dc4eb1fcdf4d9902b78d3c9c36e1b
- https://github.com/modelcontextprotocol/python-sdk/pull/3394
- https://github.com/modelcontextprotocol/python-sdk/pull/3396
- https://github.com/modelcontextprotocol/python-sdk/releases/tag/v1.30.0

### [CVE-2026-116694](https://github.com/open-telemetry/opentelemetry-python/commit/65c4eeb87cd3815dc795d3b5485e9ea0d5affcc7)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-116694
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-28 06:18:05 JST
- 更新日: 2026-10-28 06:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenTelemetry Python (1.45.0未満) の JaegerPropagator.extract() における uberctx-* バゲッジ値のサイズ・件数制限の欠如。
- 影響: 過剰または巨大な値を送信されることで過剰な CPU 利用とメモリ割り当てが発生し、DoS 状態に陥る可能性があります。
- 推奨対応: バージョン 1.45.0 以降に更新してください。

#### References
- https://github.com/open-telemetry/opentelemetry-python/commit/65c4eeb87cd3815dc795d3b5485e9ea0d5affcc7
- https://github.com/open-telemetry/opentelemetry-python/pull/5556
- https://github.com/open-telemetry/opentelemetry-python/releases/tag/v1.45.0
- https://github.com/open-telemetry/opentelemetry-python/security/advisories/GHSA-f5m9-jfrj-jjj7

### [CVE-2026-116679](https://github.com/m1k1o/neko/commit/395ca1a6f62b7b0e270e654d366a2d57b8042efd)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-116679
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-28 03:17:35 JST
- 更新日: 2026-10-28 03:17:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Neko (3.0.0〜3.1.5未満) のレガシーモードにおける LegacyIsHost() のホスト状態判定不備。
- 影響: 権限のない接続ユーザーがレガシー制御チャネル経由でマウスやキーボード操作を送信できる可能性があります。
- 推奨対応: バージョン 3.1.5 以降に更新してください。

#### References
- https://github.com/m1k1o/neko/commit/395ca1a6f62b7b0e270e654d366a2d57b8042efd
- https://github.com/m1k1o/neko/pull/675
- https://github.com/m1k1o/neko/releases/tag/v3.1.5
- https://github.com/m1k1o/neko/security/advisories/GHSA-5cp7-fp4j-wwcv

### [CVE-2026-115413](https://aws.amazon.com/security/security-bulletins/2026-152-aws/)

> **Backend** / **HIGH** / CVSS: **7.8** / KEV: **no**

- タイトル: CVE-2026-115413
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-10-28 04:17:10 JST
- 更新日: 2026-10-28 04:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AWS API MCP Server (1.6.0未満) の OAuth 認証モードにおけるトークンオーディエンス検証の欠如。
- 影響: 同一 IdP の別アプリ向けアクセストークンを悪用し、ローカルユーザーがサーバー側の AWS 権限で操作を実行する可能性があります。
- 推奨対応: バージョン 1.6.0 以降に更新し、想定されるトークンオーディエンスやクライアント ID を設定してください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-152-aws/
- https://github.com/awslabs/mcp/security/advisories/GHSA-4prq-p2x5-w9fh
- https://pypi.org/project/awslabs.aws-api-mcp-server/1.6.0/

### [CVE-2026-106076](https://www.veeam.com/kb4957)

> **Backend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-106076
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-10-28 02:16:56 JST
- 更新日: 2026-10-28 02:16:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Veeam Backup for Microsoft 365 の構成データベースにおける SQL インジェクションの脆弱性。
- 影響: 認証済みの組織移管ピアにより、他テナントの構成データの読み書きや、PostgreSQL サービスアカウント権限でのリモートコード実行が行われる可能性があります。
- 推奨対応: ベンダーが提供する最新の修正パッチまたはアップデートを適用してください。

#### References
- https://www.veeam.com/kb4957

### [CVE-2026-57190](https://github.com/asterisk/asterisk/commit/046a8b0b50623d80926c1adc2eca1c9c17e258ed)

> **Backend** / **HIGH** / CVSS: **7.0** / KEV: **no**

- タイトル: CVE-2026-57190
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-10-28 07:17:27 JST
- 更新日: 2026-10-28 07:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Asterisk の CEL バックエンド (cel_pgsql, cel_tds) における未検証データ処理に起因する SQL インジェクションの脆弱性。
- 影響: CELGenUserEvent 経由で不適切なデータが渡された場合、任意の SQL コマンドが実行される可能性があります。
- 推奨対応: Asterisk 20.20.1, 21.12.3, 22.10.1, 23.4.1、または Certified Asterisk 20.7-cert11, 22.8-cert3 以降に更新し、ダイヤルプランで適切な入力検証を行ってください。

#### References
- https://github.com/asterisk/asterisk/commit/046a8b0b50623d80926c1adc2eca1c9c17e258ed
- https://github.com/asterisk/asterisk/commit/0a86e45e8cde7630276f8363de45f71d1635d2f4
- https://github.com/asterisk/asterisk/commit/88c65757b56c716b5a175f35941be22e038b256f
- https://github.com/asterisk/asterisk/commit/8bf7746d01221d6d2bcfcd46ba7a1cff066a1a8b
- https://github.com/asterisk/asterisk/commit/8cb6dfd41debb2259ec3a33ccfa78f1d902e4c22

### [CVE-2026-112352](https://www.sunhillo.com/product/sureline/)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-112352
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-28 05:17:12 JST
- 更新日: 2026-10-28 05:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Sunhillo SureLine（9.1.5未満）における認証バイパスの脆弱性。セッションクッキーにランダム識別子や整合性保護がなく、平文のユーザー名のみで管理される実装に起因します。
- 影響: 未認証の遠隔の攻撃者が管理者等のセッションクッキーを偽造することで認証を回避し、最終的にroot権限で任意コマンドを実行する可能性があります。
- 推奨対応: Sunhillo SureLine 9.1.5 以降へアップデートしてください。

#### References
- https://www.sunhillo.com/product/sureline/
- https://www.vulncheck.com/advisories/sunhillo-sureline-authentication-bypass-via-session-cookie

### [CVE-2026-103593](https://psirt.watchguard.com/CVE-2026-103593)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-103593
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-28 01:17:28 JST
- 更新日: 2026-10-28 01:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WatchGuard Fireware OSのロギングサービスにおけるスタックベースのバッファオーバーフローの脆弱性。
- 影響: 隣接ネットワーク上の攻撃者が細工した証明書を提示することで、root権限で任意のコードを実行する可能性があります。
- 推奨対応: ログサーバーへの通信経路および証明書の検証状態を確認し、ベンダー提供の修正版を適用してください。

#### References
- https://psirt.watchguard.com/CVE-2026-103593

### [CVE-2026-116675](https://github.com/tinymce/tinymce/commit/bd1ab5ef024c648c3f9c0b409e54a6c227c7d8a2)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-116675
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-28 02:16:59 JST
- 更新日: 2026-10-28 02:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TinyMCE（7.9.3〜7.9.3、8.5.1〜8.9.2）のmediaプラグインにおけるサニタイズ不備の脆弱性。data-mce-objectを通じて作成された要素の処理に起因します。
- 影響: mediaプラグインが有効な環境において、処理時に悪意のあるスクリプトが実行され、格納型クロスサイトスクリプティング（Stored XSS）が発生する可能性があります。
- 推奨対応: TinyMCE 7.9.4 または 8.9.3 以降へアップデートしてください。

#### References
- https://github.com/tinymce/tinymce/commit/bd1ab5ef024c648c3f9c0b409e54a6c227c7d8a2
- https://github.com/tinymce/tinymce/releases/tag/8.9.3
- https://github.com/tinymce/tinymce/security/advisories/GHSA-mf2p-h6hf-fcwm
- https://www.tiny.cloud/docs/tinymce/7/7.9.4-release-notes/#overview
- https://www.tiny.cloud/docs/tinymce/latest/8.9.3-release-notes/#overview

### [CVE-2026-116683](https://github.com/ctfer-io/terraform-provider-ctfd/commit/b4acaef1df23ea3ca36936fc2d8ef8d157a58e04)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-116683
- 関連キーワード: terraform
- 影響製品: -
- 公開日: 2026-10-28 04:17:11 JST
- 更新日: 2026-10-28 04:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CTFd Terraform Provider（0.1.5〜2.8.1）において、`ctfd_team.password` が平文状態でTerraformステートに保存される問題。
- 影響: Terraformステートファイルへのアクセス権を持つユーザーが、追加の復号手順なしでチームのパスワードを取得する可能性があります。
- 推奨対応: CTFd Terraform Provider 2.8.2 以降へアップデートしてください。

#### References
- https://github.com/ctfer-io/terraform-provider-ctfd/commit/b4acaef1df23ea3ca36936fc2d8ef8d157a58e04
- https://github.com/ctfer-io/terraform-provider-ctfd/pull/376
- https://github.com/ctfer-io/terraform-provider-ctfd/releases/tag/v2.8.2
- https://github.com/ctfer-io/terraform-provider-ctfd/security/advisories/GHSA-vg84-c5mg-76xh

### [CVE-2026-116690](https://github.com/mlflow/mlflow/commit/81730a2ce4ebcd60d5d18f68c96f422ad7e30772)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-116690
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-28 05:17:14 JST
- 更新日: 2026-10-28 05:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MLflow（3.10.0〜3.17.0未満）におけるモデルバージョンのソースパス検証不備に関する脆弱性。スキームのない相対パスが許容される問題に起因します。
- 影響: 遠隔の攻撃者がサーバー上のローカルパスを保存先として登録し、API経由でMLflowプロセスがアクセス可能なサーバー上の任意ファイルを閲覧する可能性があります。
- 推奨対応: MLflow 3.17.0 以降へアップデートしてください。

#### References
- https://github.com/mlflow/mlflow/commit/81730a2ce4ebcd60d5d18f68c96f422ad7e30772
- https://github.com/mlflow/mlflow/pull/25870
- https://github.com/mlflow/mlflow/releases/tag/v3.17.0
- https://github.com/mlflow/mlflow/security/advisories/GHSA-m65p-9j7q-6w33

### [CVE-2026-57201](https://github.com/asterisk/asterisk/commit/2d7b8c8dc13d9ead8b6f36cc38b6dd91cd4abd3a)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-57201
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-28 02:17:02 JST
- 更新日: 2026-10-28 02:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AsteriskのH.323 `ooTrace()` トレースログ機能におけるスタックバッファオーバーフローの脆弱性。境界チェックのない `vsprintf` の使用に起因します。
- 影響: chan_ooh323ドライバーが有効な環境において、遠隔の攻撃者が細工したパケットを送信することでAsteriskプロセスをクラッシュ（DoS）させる可能性があります。
- 推奨対応: Asterisk 20.20.1, 21.12.3, 22.10.1, 23.4.1 または Certified Asterisk 20.7-cert11, 22.8-cert3 以降へアップデートしてください。

#### References
- https://github.com/asterisk/asterisk/commit/2d7b8c8dc13d9ead8b6f36cc38b6dd91cd4abd3a
- https://github.com/asterisk/asterisk/commit/33f62e351642edd9c58ef97b0002132722546af9
- https://github.com/asterisk/asterisk/commit/875ac7413de0b7068cd12d0da2f140cd06ba9357
- https://github.com/asterisk/asterisk/commit/ac0a64dec6d4231bf005a68da6af3e02bb311634
- https://github.com/asterisk/asterisk/commit/bf0c9a906892bc0f91fa753476e326919e4e30e5

### [CVE-2026-116693](https://github.com/DataDog/dd-trace-js/commit/5eeee790c93036a50549056fc890028cb4c86b1b)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-116693
- 関連キーワード: node.js, express
- 影響製品: -
- 公開日: 2026-10-28 06:18:05 JST
- 更新日: 2026-10-28 06:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Node.js用Datadog APMクライアント（dd-trace 2.0.0〜5.131.0、6.0.0〜6.20.0）における正規表現バックトラッキングの脆弱性。
- 影響: 攻撃者が細工したURLクエリ文字列を送信することでCPU使用率が高騰し、リクエスト処理が遅延または停止してサービス不可（DoS）に陥る可能性があります。
- 推奨対応: dd-trace 5.131.1 または 6.20.1 以降へアップデートしてください。

#### References
- https://github.com/DataDog/dd-trace-js/commit/5eeee790c93036a50549056fc890028cb4c86b1b
- https://github.com/DataDog/dd-trace-js/commit/cf4e68a45fa1442c9850f2086c81901258e821b8
- https://github.com/DataDog/dd-trace-js/pull/10675
- https://github.com/DataDog/dd-trace-js/releases/tag/v5.131.1
- https://github.com/DataDog/dd-trace-js/releases/tag/v6.20.1

### [CVE-2026-111107](https://psirt.watchguard.com/CVE-2026-111107)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-111107
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-28 01:17:29 JST
- 更新日: 2026-10-28 01:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WatchGuard Fireware OSの管理インターフェースにおける NULL ポインタ参照の脆弱性。
- 影響: 未認証の遠隔の攻撃者が細工したログインリクエストを送信することで管理サービスをクラッシュさせ、既存の管理者セッション切断や機器管理の妨害を引き起こす可能性があります（通信トラフィック処理には影響しません）。
- 推奨対応: 管理インターフェースへのネットワークアクセスを制限し、ベンダー提供の修正版へアップデートしてください。

#### References
- https://psirt.watchguard.com/CVE-2026-111107

### [CVE-2026-111583](https://www.teamviewer.com/en/resources/trust-center/security-bulletins/tv-2026-1012/)

> **Backend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-111583
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-28 01:17:29 JST
- 更新日: 2026-10-28 01:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Windows用 TeamViewer Full Client / Host（15.82未満）のインフラ設定ファイル処理における不適切なアクセス制御の脆弱性。
- 影響: ローカルの低権限認証済みユーザーが細工した設定ファイルを配置することで、サービス有効化時にSYSTEM権限で任意コマンドを実行する可能性があります。
- 推奨対応: TeamViewer 15.82 以降へアップデートしてください。

#### References
- https://www.teamviewer.com/en/resources/trust-center/security-bulletins/tv-2026-1012/

### [CVE-2026-112355](https://wordpress.org/plugins/memberfindme/#developers)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-112355
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-28 05:17:13 JST
- 更新日: 2026-10-28 05:17:13 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用 MembershipWorks プラグイン（6.17未満）の REST API におけるアクセス制限不備の脆弱性。
- 影響: 未認証の遠隔攻撃者が REST API 経由でコンテンツ取得リクエストを行うことで、会員限定コンテンツの本文を閲覧・取得する可能性があります。
- 推奨対応: MembershipWorks プラグイン 6.17 以降へアップデートしてください。

#### References
- https://wordpress.org/plugins/memberfindme/#developers
- https://www.vulncheck.com/advisories/membershipworks-wordpress-plugin-information-disclosure-via-wordpress-rest-api

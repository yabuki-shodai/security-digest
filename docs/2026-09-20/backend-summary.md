# Backend CVE Summary (2026-09-20)

## Overview

- 取得日時: 2026-09-20 09:06:16 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 4
- Critical: 0
- High: 2
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-93991](https://github.com/argoproj/argo-workflows)

> **Backend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-93991
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-20 08:17:10 JST
- 更新日: 2026-09-20 08:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Argo Workflows (4.1.0～4.1.3) の ListArchivedWorkflows において、metadata.namespace フィールドに NotEquals 演算子が使用された際にクラスターレベルのアクセス検証が不適切となる認可バイパスの脆弱性。
- 影響: ネームスペース権限を持つ攻撃者が否定演算子を利用することで、他ネームスペースのアーカイブ済みワークフロー情報（引数やパラメータ、アノテーション等）を取得できる可能性があります。
- 推奨対応: 修正されたバージョンへのアップデートを実施してください。

#### References
- https://github.com/argoproj/argo-workflows
- https://github.com/argoproj/argo-workflows/commit/a40972386c097ddf816d2e60e13f058bedca53d9
- https://github.com/argoproj/argo-workflows/releases/tag/v4.1.4
- https://github.com/argoproj/argo-workflows/security/advisories/GHSA-q65w-j2vp-47c4
- https://www.vulncheck.com/advisories/argo-workflows-4.1.0-through-4.1.3-cross-namespace-disclosure-via-negated-selector

### [CVE-2026-93992](https://github.com/GopeedLab/gopeed)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-93992
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-20 08:17:10 JST
- 更新日: 2026-09-20 08:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Gopeed (2.0.0-beta.3 以前) のアーカイブ解凍処理において、ディレクトリトラバーサルシーケンスの検証不備によるパストラバーサルの脆弱性。
- 影響: AutoExtract 機能が有効な環境で悪意のあるアーカイブを展開した場合、抽出先ディレクトリの外部へ任意のファイルが書き込まれる可能性があります。
- 推奨対応: 修正版へのアップデートまたは AutoExtract 機能の有効化設定を見直してください。

#### References
- https://github.com/GopeedLab/gopeed
- https://github.com/GopeedLab/gopeed/blob/a5cd53f94c18ac65add684b1113fa5f0b47cc4da/pkg/download/extract.go#L284-L296
- https://github.com/GopeedLab/gopeed/blob/a5cd53f94c18ac65add684b1113fa5f0b47cc4da/pkg/download/extract_7z.go#L45-L53
- https://github.com/GopeedLab/gopeed/commit/38750d8505274e55cf11aa77f0694c71dd82f519
- https://github.com/GopeedLab/gopeed/issues/1525

### [CVE-2026-93956](https://github.com/olivier-ls/php-fts/)

> **Backend** / **MEDIUM** / CVSS: **4.0** / KEV: **no**

- タイトル: CVE-2026-93956
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-20 08:17:09 JST
- 更新日: 2026-09-20 08:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: olivier-ls PHP-FTS (1.1.2 以前) の SearchEngine::buildHighlights 関数における Query 引数の不適切な処理によるクロスサイトスクリプティング (XSS) の脆弱性。
- 影響: リモートの攻撃者によって悪意のあるスクリプトを実行される可能性があります。すでに概念実証コード (PoC) が公開されていると報告されています。
- 推奨対応: 1.1.3 以降の修正済みバージョンへアップグレードしてください。

#### References
- https://github.com/olivier-ls/php-fts/
- https://github.com/olivier-ls/php-fts/commit/0b2fae333d6b022da7ed4c43e2d41aa03f91dff3
- https://github.com/olivier-ls/php-fts/issues/1
- https://github.com/olivier-ls/php-fts/tags
- https://github.com/sumo166/CVE-apply/blob/main/olivier-ls/PHP-FTS/SearchEngine%20buildHighlights%20Stored%20XSS%20(CWE-79)_cve.md

### [CVE-2026-82560](https://github.com/rra/podlators/commit/70510174f69eb54aa6d617bde4e1402cd9b7c61f.patch)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-82560
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-20 01:16:32 JST
- 更新日: 2026-09-20 06:16:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Perl の Pod::Text (6.1.1 未満) において、=over のネストが出力幅に達した POD ドキュメントの処理時に無限ループが発生する問題。
- 影響: 攻撃者が作成した POD ドキュメントを処理させることで、CPU およびメモリが過剰に消費され、サービス不可状態 (DoS) に陥る可能性があります。
- 推奨対応: Pod::Text を 6.1.1 以降へアップデートしてください。

#### References
- https://github.com/rra/podlators/commit/70510174f69eb54aa6d617bde4e1402cd9b7c61f.patch
- https://metacpan.org/release/RRA/podlators-v6.1.0/source/lib/Pod/Text.pm#L245-261
- https://metacpan.org/release/RRA/podlators-v6.1.1/changes
- http://www.openwall.com/lists/oss-security/2026/09/19/6

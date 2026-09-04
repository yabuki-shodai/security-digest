# Frontend CVE Summary (2026-09-05)

## Overview

- 取得日時: 2026-09-05 08:58:46 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 4
- Critical: 1
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-85625](https://github.com/crcn/sift.js)

> **Frontend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-85625
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-05 00:17:42 JST
- 更新日: 2026-09-05 00:17:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: sift (sift.js) 17.1.3 において、クエリキーの評価処理でプロトタイプチェーンを探索するため、$where 演算子が意図せず実行される問題が存在します。
- 影響: プロトタイプ汚染や信頼できないクエリの入力により、任意のJavaScriptコードを実行される可能性があります。
- 推奨対応: ライブラリの更新、信頼できないクエリ入力の制限、およびプロトタイプ汚染対策の実施が推奨されます。

#### References
- https://github.com/crcn/sift.js
- https://github.com/crcn/sift.js/blob/v17.1.3/src/core.ts
- https://github.com/crcn/sift.js/issues/276
- https://www.vulncheck.com/advisories/sift-17.1.3-prototype-pollution-remote-code-execution-via-where

### [CVE-2026-75170](https://github.com/SilviaMun/vulnerability-research/tree/main/CVE-2026-75170)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-75170
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-05 01:17:59 JST
- 更新日: 2026-09-05 01:17:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HubCore 14.1.1 の /loginController/doLogin エンドポイントにおける language POST パラメータの検証不足によるXSS脆弱性です。
- 影響: 未認証の遠隔の攻撃者により、応答内で任意のスプリクトを実行される可能性があります。
- 推奨対応: 開発元が提供する修正パッチの適用や、入力値の検証および出力時の適切なエスケープ処理の実施が推奨されます。

#### References
- https://github.com/SilviaMun/vulnerability-research/tree/main/CVE-2026-75170
- https://hubcore.ai/

### [CVE-2026-79418](https://drive.google.com/file/d/1mp-uS-tAthH9FAObfx1D3lOM7IIjRsmE/view?usp=sharing)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-79418
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-05 01:18:00 JST
- 更新日: 2026-09-05 01:18:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: EMX Tecnologia Gestao X 8.4 以下の Help Chat 機能における入力処理の不備による格納型XSS脆弱性です。
- 影響: 認証された攻撃者により、他ユーザーのセッションハイジャックやアカウント乗っ取り、不正操作が行われる可能性があります。
- 推奨対応: 修正版へのアップデートおよび入力値のサニタイズ処理の確認・適用が推奨されます。

#### References
- https://drive.google.com/file/d/1mp-uS-tAthH9FAObfx1D3lOM7IIjRsmE/view?usp=sharing
- https://emxtecnologia.com.br/gestao-x-business-suite/

### [CVE-2026-79419](https://drive.google.com/file/d/1QVH1MRo3G4KqmBORkhXITzcYmO_BDjWc/view)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-79419
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-05 01:18:00 JST
- 更新日: 2026-09-05 01:18:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: EMX Tecnologia Gestao X Business Suite 8.4 以下の /Configuracao/Imagens.aspx エンドポイントにおける mensagem パラメータのサニタイズ不備による反射型XSS脆弱性です。
- 影響: 未認証の攻撃者により、被害者のブラウザ上で任意のJavaScriptを実行される可能性があります。
- 推奨対応: 最新バージョンへの更新および該当パラメータに対する入力検証・エスケープ処理の実施が推奨されます。

#### References
- https://drive.google.com/file/d/1QVH1MRo3G4KqmBORkhXITzcYmO_BDjWc/view
- https://emxtecnologia.com.br/gestao-x-business-suite/

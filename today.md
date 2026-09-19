# CVE Digest Dashboard (2026-09-19)

## Overview

- Total: 30
- Critical件数: 3
- High件数: 11
- KEV件数: 0
- Frontend件数: 9
- Backend件数: 21
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-19/frontend-summary.md)
- [Backend Summary](docs/2026-09-19/backend-summary.md)

## Today TOP5

- [CVE-2023-54399](https://cn-sec.com/archives/1861976.html) CVE-2023-54399 / CRITICAL / backend
- [CVE-2026-93762](https://jira.mongodb.org/browse/MONGOID-5973) CVE-2026-93762 / CRITICAL / backend
- [CVE-2026-93765](https://jira.mongodb.org/browse/MONGOID-5973) CVE-2026-93765 / CRITICAL / backend
- [CVE-2026-93559](https://github.com/Forget-C/Jellyfish/issues/37) CVE-2026-93559 / HIGH / backend
- [CVE-2026-84992](https://github.com/imzbf/md-editor-v3/commit/2c07360420e74087f5bc63032ab155d93e0a0b10) CVE-2026-84992 / MEDIUM / frontend

## Geminiによる今日の総括

## 今日のまとめ
本日公表された脆弱性では、**Mongoid (ODM) に関連する無制限リフレクションやクエリ評価不備（CVSS 9.8 を含む）** が多発している点が最も特筆されます。また、**Hongjing e-HR** での認証不要な SQL インジェクションや **zot** コンテナレジストリにおける削除権限バイパスなど、重大なデータ侵害につながるバックエンドの脆弱性が報告されています。さらに、フロントエンドや Node.js ライブラリ領域でも **adm-zip** の DoS (メモリ枯渇) や各種コンポーネントでの XSS / 不適切な URL スキーム許容が確認されています。

---

## 優先して確認すべき3〜5件

1. **CVE-2023-54399 (CVSS 9.8 / CRITICAL)**
   - **対象**: Hongjing e-HR (8.2 未満)
   - **概要**: `/servlet/codesettree` の `categories` パラメータにおける SQL インジェクションの脆弱性。未認証のリモート攻撃者が任意データを閲覧可能で、資格情報テーブルの漏洩リスクがあります。
2. **CVE-2026-93762 (CVSS 9.8 / CRITICAL)**
   - **対象**: Mongoid
   - **概要**: 埋め込みドキュメント処理における安全でないリフレクションの脆弱性。外部からの入力フィールド名により、未認証の第三者が格納データの一覧取得や永久削除を引き起こす恐れがあります。
3. **CVE-2026-93765 (CVSS 9.1 / CRITICAL)**
   - **対象**: Mongoid
   - **概要**: 永続化レイヤーにおける安全でないリフレクション。外部から供給されたキーの処理不備により、意図しない内部メソッドが呼び出され、レコードの削除やアプリケーションの応答停止につながります。
4. **CVE-2026-61833 (CVSS 8.1 / HIGH)**
   - **対象**: zot (OCI コンテナレジストリ)
   - **概要**: Bearer 認証処理において DELETE リクエストに対する独立した削除権限チェックが行われず、特定の認証トークンを持つユーザーが権限を越えてマニフェストや Blob を削除できる問題です。
5. **CVE-2026-77301 (CVSS 7.5 / HIGH)**
   - **対象**: adm-zip (0.6.1 未満)
   - **概要**: ZIP エントリの展開前サイズを検証せずにメモリ割り当て (`Buffer.alloc`) を行うため、細工された小さな ZIP ファイルにより過剰なメモリが消費され DoS に陥ります。

---

## 開発者向けコメント

- **Mongoid 利用箇所の急務な点検とアップデート**: 本日 Mongoid に関して、リフレクションによるコード実行・データ削除（CVE-2026-93762, CVE-2026-93765）、JS インジェクション（CVE-2026-93759）、IDOR（CVE-2026-93758）など複数の危険な脆弱性が提示されました。ライブラリの更新に加え、外部からの入力をそのままクエリや埋め込みフィールド名に渡していないかコードを確認してください。
- **アーカイブ・ドキュメント処理ライブラリの安全対策**: `adm-zip` のように非圧縮サイズを信用してメモリ割り当てを行う脆弱性や、ドキュメントプレビューにおける unsafe URL scheme（`javascript:` 等）の非エスケープ（CVE-2026-91127）が確認されています。入力ファイルの妥当性検証およびライブラリのバージョンアップを実施してください。
- **HTTP メソッド別の認可・アクセス制御の再確認**: `zot` の事例のように、GET/HEAD 以外の HTTP メソッド（特に DELETE 等）に対する権限検証漏れや、マルチテナント間での識別子照合漏れ（CVE-2026-81505）を防ぐため、API エンドポイントごとのアクセス制御処理を再確認することを推奨します。

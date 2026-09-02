# CVE Digest Dashboard (2026-09-02)

## Overview

- Total: 30
- Critical件数: 1
- High件数: 22
- KEV件数: 0
- Frontend件数: 16
- Backend件数: 14
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-02/frontend-summary.md)
- [Backend Summary](docs/2026-09-02/backend-summary.md)

## Today TOP5

- [CVE-2026-78012](https://pyramidsolutions.com/netstax-v-5-6-1-protecting-against-silent-buffer-overflow-in-ethernet-ip-stack-explicit-messages/) CVE-2026-78012 / CRITICAL / backend
- [CVE-2026-83619](https://github.com/xmldom/xmldom/commit/3abb0934f5a8a84d83a1f9cde0f2bd04c08b2a09) CVE-2026-83619 / HIGH / frontend
- [CVE-2026-49329](https://access.redhat.com/security/cve/CVE-2026-49329) CVE-2026-49329 / HIGH / backend
- [CVE-2026-84304](https://github.com/grpc/grpc-go/commit/7354d9c8debb4bcf2225bf429857078de310c176) CVE-2026-84304 / HIGH / backend
- [CVE-2026-84308](https://github.com/phpseclib/phpseclib/commit/fb56bc5bb9009b54a6c26b31aeec8ed944f17373) CVE-2026-84308 / MEDIUM / backend

## Geminiによる今日の総括

## 今日のまとめ
JavaScript向けの標準XML解析ライブラリである **`xmldom`（`@xmldom/xmldom`）において大量の脆弱性（DoS、検証バイパス、マークアップインジェクション等）**が一括して公表されました。
また、**gRPC-Go** でのメモリ枯渇DoSやアクセス制御回避、**ModelScope** や **Fooocus** などのAI/ML・データ処理関連ツールにおける不安全な読み込み・評価（RCE）、および **NetStaX EtherNet/IP Stack** での最高深刻度（CVSS 9.8）のバッファオーバーフローが報告されています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-78012 (CVSS 9.8 - CRITICAL): NetStaX EtherNet/IP Stack のバッファオーバーフロー**
   - **概要:** クラス3の明示的メッセージの受信バッファオーバーフローにより、メモリ破壊、デバイスのクラッシュ、および潜在的なリモート攻撃が可能です。
2. **CVE-2026-84202 (CVSS 8.8 - HIGH): ModelScope の PyYAML 不安全デシリアライズによる RCE**
   - **概要:** PyYAML の不安全な `yaml.Loader` を使用しているため、悪意あるモデル設定ファイルを読み込むだけで任意の Python コードが実行されるリスクがあります。
3. **CVE-2026-84304 (CVSS 8.7 - HIGH) / CVE-2026-84303 (CVSS 6.3 - MEDIUM): gRPC-Go のDoSおよびRBACバイパス**
   - **概要:** v1.83.1 未満において、大量の1バイト HTTP/2 DATA フレーム処理によるヒープメモリ枯渇（DoS）が発生します。また、xDS RBAC フィルタでヘッダー名の大文字・小文字比較の不備により拒否ポリシーが回避される脆弱性も含まれます。
4. **CVE-2026-83619 ほか多数 (CVSS 8.7 - HIGH): `@xmldom/xmldom` の複数の脆弱性**
   - **概要:** 正規表現の二次バックトラックによる DoS、タグ名や属性名の検証不備によるマークアップインジェクションが広範囲のバージョンに存在します。修正版（`0.8.15` / `0.9.12` 等）への更新が必要です。
5. **CVE-2026-83551 (CVSS 8.5 - HIGH): Amazon SageMaker Python SDK の HMAC 鍵平文保存**
   - **概要:** API 応答内に HMAC 署名鍵が平文保存されているため、同 AWS アカウント内の別ユーザーのパイプライン実行コンテキストで任意コード実行が可能になります（v3.11.0 / v2.256.0 未満が影響）。

---

## 開発者向けコメント

* **`xmldom` および `gRPC-Go` 依存パッケージの緊急更新:** Node.js/JavaScript 環境で `@xmldom/xmldom` を利用しているプロジェクトは、最新版（`0.8.15` または `0.9.12` 以降）へ即座にアップデートしてください。Go バックエンド環境も `gRPC-Go` を `1.83.1` 以上へ更新することを推奨します。
* **AI/ML ライブラリのデータパース処理見直し:** YAML パース時の `yaml.SafeLoader` 利用や、画像 EXIF 等のメタデータ解析時の `eval()` 排除など、信頼できない入力に対する処理を再点検してください。
* **認証・認可ヘッダーの正規化処理:** 通信フレームワークやプロキシを通る際、ヘッダー名の大文字小文字の扱いによってセキュリティポリシーを不適用（Fail Open）にされないよう、システム全体のインターフェース検証が必要です。

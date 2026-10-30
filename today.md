# CVE Digest Dashboard (2026-10-30)

## Overview

- Total: 30
- Critical件数: 7
- High件数: 10
- KEV件数: 0
- Frontend件数: 3
- Backend件数: 20
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-30/frontend-summary.md)
- [Backend Summary](docs/2026-10-30/backend-summary.md)

## Today TOP5

- [CVE-2026-61991](https://patchstack.com/database/wordpress/plugin/ajax-load-more-cache/vulnerability/wordpress-ajaxloadmore-cache-plugin-3-1-1-remote-code-execution-rce-vulnerability?_s_id=cve) CVE-2026-61991 / CRITICAL / security
- [CVE-2026-119145](https://github.com/frappe/frappe/security/advisories/GHSA-9pp9-wgp9-3p3j) CVE-2026-119145 / CRITICAL / security
- [CVE-2026-62001](https://patchstack.com/database/wordpress/theme/marcell/vulnerability/wordpress-marcell-theme-1-2-14-php-object-injection-vulnerability?_s_id=cve) CVE-2026-62001 / CRITICAL / security
- [CVE-2026-107327](https://www.ibm.com/support/pages/node/7293016) CVE-2026-107327 / CRITICAL / security
- [CVE-2026-107328](https://www.ibm.com/support/pages/node/7293016) CVE-2026-107328 / CRITICAL / security

## Geminiによる今日の総括

## 今日のまとめ

本日掲載された30件のCVEでは、CVSS 9.0以上の最高警戒レベル（CRITICAL）を含む深刻な脆弱性が多数報告されています。特に**IBM Langflow OSS**、**Frappe**、**ZITADEL**、**Crawl4AI**といったプロダクト・ライブラリ群において複数の脆弱性が同時に公開されています。攻撃手法としては、未認証でのリモートコード実行（RCE）、認証バイパス、PHP Object Injection、パス・トラバーサル、SSTI（サーバーサイド・テンプレート・インジェクション）などが目立ちます。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-61991 (CVSS 10.0 / CRITICAL)**
   * **対象:** AjaxLoadMore Cache（<= 3.1.1）
   * **概要:** 未認証の第三者によるリモートコード実行（RCE）が可能な脆弱性。最高深刻度として即時対応が必要です。
2. **CVE-2026-119145 (CVSS 9.9 / CRITICAL)**
   * **対象:** Frappe（15.121.0未満、および16.xの16.34.0未満）
   * **概要:** ファイルアップロード処理におけるパス・トラバーサルの欠陥により、意図しないディレクトリへのファイル書き込みを通じたRCEが可能です。
3. **CVE-2026-107327 / CVE-2026-107328 / CVE-2026-107329 (CVSS 9.9 / CRITICAL)**
   * **対象:** IBM Langflow OSS（1.0.0 〜 1.12.4）
   * **概要:** 認可欠如や`eval`/`exec`等のコード評価処理・生成制御の不備により、リモートの認証済み攻撃者による任意のコード実行が可能です。
4. **CVE-2026-62001 (CVSS 9.8 / CRITICAL)**
   * **対象:** Marcell（<= 1.2.14）
   * **概要:** 未認証で悪用可能なPHP Object Injectionの脆弱性が存在します。
5. **CVE-2026-119128 (CVSS 9.1 / CRITICAL)**
   * **対象:** ZITADEL（4.0.0以上 4.19.5未満）
   * **概要:** Login V2 UIにおける認証バイパス。認証手段を持たないユーザーに対して第一資格情報を勝手に設定し、アカウント乗っ取りが行われるリスクがあります。

---

## 開発者向けコメント

* **アップグレードの実施:** ZITADEL、Frappe、Crawl4AI、IBM Langflow OSS、Wasmtime、Parse Serverなどの依存パッケージを使用している場合は、記載の修正済みバージョンへ速やかにアップデートしてください。
* **入力値の検証と動的評価の回避:** コード内で `eval` や `exec` を使用した動的実行、テンプレートエンジンへの不適切なユーザー入力の直接渡しの排除（SSTI対策）、およびファイルアップロード時のパス検証を徹底してください。
* **デシリアライズおよび認証ロジックの再確認:** PHPのオブジェクト注入やPickle形式データ読み込み（CVE-2026-119120等）に伴うリスクを把握し、信頼できない入力値の処理ロジックを見直すことが重要です。

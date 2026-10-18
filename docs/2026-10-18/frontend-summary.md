# Frontend CVE Summary (2026-10-18)

## Overview

- 取得日時: 2026-10-18 08:59:00 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 2
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-111894](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-fg92-v5rr-4xjq)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-111894
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-18 04:16:31 JST
- 更新日: 2026-10-18 04:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: phpMyFAQにおけるコンテンツクリーンアップ処理の不備に起因する蓄積型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 認証された作成者が不正なiframeをFAQやニュースに埋め込むことで、閲覧者のブラウザ上で任意のJavaScriptを実行し、フィッシングや強制リダイレクトを引き起こす可能性があります。
- 推奨対応: phpMyFAQ 4.1.9 または 4.2.0-beta 以降の修正済みバージョンへ更新することが推奨されます。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-fg92-v5rr-4xjq
- https://www.vulncheck.com/advisories/phpmyfaq-3.2.1-before-4.1.9-and-4.2.0-alpha-before-4.2.0-beta-stored-xss-via-iframe-data-uri

### [CVE-2026-111903](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-j3v5-p957-w6gq)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-111903
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-18 04:16:32 JST
- 更新日: 2026-10-18 04:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: phpMyFAQのSvgSanitizerにおけるXML DTDカスタムエンティティの無効化不備による蓄積型XSSの脆弱性。
- 影響: FAQ編集権限を持つユーザーが特製SVGをアップロードすることでサニタイズを迂回し、リンクをクリックした管理者などのセッションを乗っ取る可能性があります。
- 推奨対応: phpMyFAQ 4.2.0-beta 以降の修正済みバージョンへ更新することが推奨されます。

#### References
- https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-j3v5-p957-w6gq
- https://www.vulncheck.com/advisories/phpmyfaq-4.2.0-alpha-before-4.2.0-beta-stored-xss-via-svg-dtd-entity-bypass

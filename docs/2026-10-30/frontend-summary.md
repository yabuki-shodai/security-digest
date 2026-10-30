# Frontend CVE Summary (2026-10-30)

## Overview

- 取得日時: 2026-10-30 10:53:37 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 3
- Critical: 0
- High: 1
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-107041](https://f-droid.org/packages/com.oasisfeng.island.fdroid/)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-107041
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-10-30 01:17:49 JST
- 更新日: 2026-10-30 01:30:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Oasis Feng Island (versionCode 51801) の FeatureActionActivity コンポーネントにおける不適切な権限設定の脆弱性。
- 影響: 未認証の攻撃者によってデバイスが強制的にフリーズさせられ、サービス拒否 (DoS) 状態に陥る可能性があります。
- 推奨対応: 適切なアクセス権限の設定または修正されたバージョンへの更新が推奨されます。

#### References
- https://f-droid.org/packages/com.oasisfeng.island.fdroid/
- https://github.com/FFG0d/fdroid-android-advisories/blob/main/advisories/CVE-2026-107041.md
- https://github.com/oasisfeng/island

### [CVE-2026-119127](https://github.com/zitadel/zitadel/security/advisories/GHSA-mchc-246r-6m76)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-119127
- 関連キーワード: vite, gin
- 影響製品: -
- 公開日: 2026-10-30 01:18:05 JST
- 更新日: 2026-10-30 01:18:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ZITADEL の Login V2 UI におけるホストヘッダーインジェクションの脆弱性。
- 影響: 未認証の攻撃者により各種確認リンクが偽装され、認証コードの不正取得を通じて管理者を含むアカウントが乗っ取られる可能性があります。
- 推奨対応: ZITADEL 4.19.5 以降のバージョンへアップデートしてください。

#### References
- https://github.com/zitadel/zitadel/security/advisories/GHSA-mchc-246r-6m76
- https://www.vulncheck.com/advisories/zitadel-4.0.0-before-4.19.5-account-takeover-via-login-v2-host-header-injection

### [CVE-2026-119121](https://github.com/unclecode/crawl4ai/security/advisories/GHSA-qj46-wp7m-rgj8)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-119121
- 関連キーワード: javascript, docker
- 影響製品: -
- 公開日: 2026-10-30 01:18:04 JST
- 更新日: 2026-10-30 03:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Crawl4AI の Docker API サーバーにおける JavaScript インジェクションの脆弱性。
- 影響: 認証された API クライアントによりクロール対象ページ内で任意の JavaScript を実行され、データやページ状態が改ざんされる可能性があります。
- 推奨対応: Crawl4AI 0.9.5 以降のバージョンへアップデートしてください。

#### References
- https://github.com/unclecode/crawl4ai/security/advisories/GHSA-qj46-wp7m-rgj8
- https://www.vulncheck.com/advisories/crawl4ai-0.9.0-before-0.9.5-javascript-injection-via-css-selector-and-wait-for

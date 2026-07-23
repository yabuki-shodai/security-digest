# Frontend CVE Summary (2026-07-24)

## Overview

- 取得日時: 2026-07-24 08:08:25 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 7
- Critical: 5
- High: 0
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2025-71389](https://github.com/advisories/GHSA-9qr9-h5gf-34mp)

> **Frontend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2025-71389
- 関連キーワード: next.js, react
- 影響製品: -
- 公開日: 2026-07-24 07:16:51 JST
- 更新日: 2026-07-24 07:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Cal.com (calcom/cal.diy) before 5.9.9 is vulnerable to unauthenticated remote code execution because it bundles a version of Next.js whose React Server Components (RSC) request handling deserializes attacker-controlled input. A remote attacker can send a crafted RSC request to the server and cause arbitrary code to be...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/advisories/GHSA-9qr9-h5gf-34mp
- https://github.com/calcom/cal.diy/pull/25592
- https://github.com/calcom/cal.diy/security/advisories/GHSA-qjx2-5xqp-cpf4
- https://www.vulncheck.com/advisories/cal-com-before-remote-code-execution-via-rsc

### [CVE-2024-58353](https://github.com/calcom/cal.diy/commit/00689fda0a30b8f933c096f02c1fe092a4206def)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2024-58353
- 関連キーワード: javascript, react
- 影響製品: -
- 公開日: 2026-07-24 07:16:51 JST
- 更新日: 2026-07-24 07:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Cal.com (repository calcom/cal.diy) in versions <= 4.7.15 is vulnerable to cross-site scripting (XSS) on the publicly accessible single booking view (e.g., /booking/<id>). Booking question (form field) labels are rendered via React's dangerouslySetInnerHTML without proper input sanitization or CSP, so an attacker who c...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/calcom/cal.diy/commit/00689fda0a30b8f933c096f02c1fe092a4206def
- https://github.com/calcom/cal.diy/security/advisories/GHSA-vgj7-76cw-h6f8
- https://www.vulncheck.com/advisories/cal-com-through-cross-site-scripting-via-booking-questions

### [CVE-2024-58355](https://github.com/calcom/cal.diy/commit/00689fda0a30b8f933c096f02c1fe092a4206def)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2024-58355
- 関連キーワード: javascript, react
- 影響製品: -
- 公開日: 2026-07-24 07:16:51 JST
- 更新日: 2026-07-24 07:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Cal.com (calcom/cal.diy) 4.7.15以前のバージョンに、ユーザー入力を適切にサニタイズしないstored XSS脆弱性が存在します。  
- 影響: 攻撃者が悪意あるイベントタイプを作成し、被害者が特別に細工された予約URLを開くと任意のHTML/JavaScriptが実行される可能性があります。  
- 推奨対応: バージョン4.7.16以降にアップデートし、脆弱性の修正を適用してください。

#### References
- https://github.com/calcom/cal.diy/commit/00689fda0a30b8f933c096f02c1fe092a4206def
- https://github.com/calcom/cal.diy/security/advisories/GHSA-vgj7-76cw-h6f8
- https://www.vulncheck.com/advisories/cal-com-through-cross-site-scripting-via-booking-questions-2

### [CVE-2024-58354](https://github.com/calcom/cal.diy/commit/9aa60fae41a6b6b101c86bf430754b439f440871)

> **Frontend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2024-58354
- 関連キーワード: yarn, github actions
- 影響製品: -
- 公開日: 2026-07-24 07:16:51 JST
- 更新日: 2026-07-24 07:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: cal.com (calcom repository, later renamed cal.diy) is affected by a repository takeover vulnerability in its GitHub Actions workflows. The workflow pr.yml uses the pull_request_target trigger with the repository's default write permissions and passes them down to check-types.yml. check-types.yml then performs a 'danger...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/calcom/cal.diy/commit/9aa60fae41a6b6b101c86bf430754b439f440871
- https://github.com/calcom/cal.diy/security/advisories/GHSA-p3f6-52gv-cj7m
- https://www.vulncheck.com/advisories/cal-com-repository-takeover-via-pull-request-target-workflow

### [CVE-2026-47668](https://github.com/dbgate/dbgate/releases/tag/v7.1.9)

> **Frontend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-47668
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-07-24 03:16:53 JST
- 更新日: 2026-07-24 04:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: DbGate 7.1.8以前のバージョンにおいて、JSONスクリプトの`functionName`パラメータにコードインジェクションが可能で、リモートコード実行の脆弱性が存在します。  
- 影響: 悪意ある攻撃者がリモートから任意のコードを実行できるため、システムの完全な制御を奪われる恐れがあります。  
- 推奨対応: 速やかにDbGateをバージョン7.1.9以降にアップデートし、該当の脆弱性修正を適用してください。

#### References
- https://github.com/dbgate/dbgate/releases/tag/v7.1.9
- https://github.com/dbgate/dbgate/security/advisories/GHSA-8v3q-9vmx-36vc
- https://github.com/runZeroInc/nuclei-templates/blob/main/http/vulnerabilities/dbgate-unauth-rce.yaml
- https://github.com/dbgate/dbgate/security/advisories/GHSA-8v3q-9vmx-36vc

### [CVE-2026-48012](https://github.com/shopware/shopware/releases/tag/v6.7.10.1)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-48012
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-24 05:17:08 JST
- 更新日: 2026-07-24 05:17:08 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Shopware is an open commerce platform. Versions 6.7.3.0 through 6.7.10.0 have an open redirect in Shopware's public SSO entry point at `GET /api/oauth/sso/auth`. When the endpoint is reached without the expected SSO session state, the application falls back to the request's `Referer` header and uses that value as the r...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/shopware/shopware/releases/tag/v6.7.10.1
- https://github.com/shopware/shopware/security/advisories/GHSA-4x3x-869w-xx3m

### [CVE-2026-65697](https://github.com/geo-chen/oss/blob/main/fathom.md)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-65697
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-24 02:16:29 JST
- 更新日: 2026-07-24 04:17:05 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Fathom Lite 1.3.1以前に、認証不要の/collectエンドポイントで悪意あるjavascript: URIを注入可能な保存型クロスサイトスクリプティング脆弱性があります。  
- 影響: 攻撃者はダッシュボード上でスクリプトを実行し、セッションハイジャックやアカウント乗っ取りが発生する可能性があります。  
- 推奨対応: 最新バージョンへのアップデートや、入力値の適切な検証・サニタイズを実施してください。

#### References
- https://github.com/geo-chen/oss/blob/main/fathom.md
- https://www.vulncheck.com/advisories/fathom-lite-stored-xss-via-collect-endpoint

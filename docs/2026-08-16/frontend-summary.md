# Frontend CVE Summary (2026-08-16)

## Overview

- 取得日時: 2026-08-16 07:33:39 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 3
- Critical: 3
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-73043](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-rwh7-gm74-67h6)

> **Frontend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-73043
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-08-16 07:16:54 JST
- 更新日: 2026-08-16 07:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SiYuan versions before v3.7.4 contain a remote code execution vulnerability in the Template calculation operator, which renders user-authored Go templates and stores output verbatim without sanitization. Attackers can inject malicious HTML and JavaScript into template calculations that execute in the desktop client ren...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-rwh7-gm74-67h6
- https://www.vulncheck.com/advisories/siyuan-before-remote-code-execution-via-template-calculation

### [CVE-2026-73050](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-m7cc-jh9q-wxg8)

> **Frontend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-73050
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-16 07:16:54 JST
- 更新日: 2026-08-16 07:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SiYuan versions before v3.7.4 fail to validate or escape the color field in attribute-view select options, allowing stored cross-site scripting through eight unescaped render sites. Attackers can inject event-handler attributes by including quotation marks in the color value, executing arbitrary JavaScript when viewing...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-m7cc-jh9q-wxg8
- https://www.vulncheck.com/advisories/siyuan-before-stored-xss-via-select-option-color

### [CVE-2026-73052](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-g3jx-227v-x2x4)

> **Frontend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-73052
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-16 07:16:55 JST
- 更新日: 2026-08-16 07:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SiYuan before v3.7.4 stores attribute-view field names without HTML escaping and interpolates them directly into option elements via innerHTML in the sort menu. Attackers can inject markup by renaming a database field to execute arbitrary JavaScript when users open the sort menu, with Node integration enabled in the de...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-g3jx-227v-x2x4
- https://www.vulncheck.com/advisories/siyuan-before-stored-xss-via-attribute-view-field-names

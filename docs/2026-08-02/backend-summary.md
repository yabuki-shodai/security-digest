# Backend CVE Summary (2026-08-02)

## Overview

- 取得日時: 2026-08-02 08:05:58 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 0
- High: 1
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-55735](https://cna.erlef.org/cves/CVE-2026-55735.html)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-55735
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-02 04:16:42 JST
- 更新日: 2026-08-02 04:16:42 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Improper Verification of Cryptographic Signature in ueberauth guardian allows an unauthenticated attacker to revoke a victim's session with a forged token. Guardian.revoke/3 in lib/guardian.ex decodes the supplied token with peek/1, which performs no signature verification (it only base64-decodes the JWT header and pay...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-55735.html
- https://github.com/ueberauth/guardian/commit/2bd7a8c29770d423d855c0a4965caa6c3e486901
- https://github.com/ueberauth/guardian/security/advisories/GHSA-7975-hp3r-5qhv
- https://osv.dev/vulnerability/EEF-CVE-2026-55735

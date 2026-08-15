# Backend CVE Summary (2026-08-16)

## Overview

- 取得日時: 2026-08-16 07:33:39 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 5
- High: 1
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-74764](https://github.com/pandora-analysis/pandora/commit/186b58d41e04248a154d274fffb5813e7fa2012e)

> **Backend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-74764
- 関連キーワード: python, go
- 影響製品: -
- 公開日: 2026-08-16 07:16:55 JST
- 更新日: 2026-08-16 07:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Pandora contains a path traversal vulnerability in its TAR archive extraction functionality. When processing a submitted TAR archive, the extractor passed archive member names directly to Python's tarfile.TarFile.extract() without applying an extraction filter. An attacker able to submit a specially crafted TAR archive...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/pandora-analysis/pandora/commit/186b58d41e04248a154d274fffb5813e7fa2012e

### [CVE-2026-19898](https://github.com/VictoriaMetrics/VictoriaMetrics/)

> **Backend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-19898
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-16 01:16:39 JST
- 更新日: 2026-08-16 01:16:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability was found in VictoriaMetrics up to 1.146.0. Impacted is the function requestHandler of the file app/vmauth/main.go of the component VMAuth Authentication Endpoint. Performing a manipulation results in improper restriction of excessive authentication attempts. The attack is possible to be carried out rem...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/VictoriaMetrics/VictoriaMetrics/
- https://github.com/VictoriaMetrics/VictoriaMetrics/commit/119ba0fb5be8024d50c5ba946599b2e69e8803ea
- https://github.com/VictoriaMetrics/VictoriaMetrics/issues/11180
- https://github.com/VictoriaMetrics/VictoriaMetrics/releases/tag/v1.147.0
- https://github.com/VictoriaMetrics/VictoriaMetrics/security/advisories/GHSA-c7pm-322g-r9gf

### [CVE-2026-19598](https://plugins.trac.wordpress.org/browser/pods/tags/3.3.9/includes/general.php#L400)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-19598
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-16 03:16:23 JST
- 更新日: 2026-08-16 03:16:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The Pods – Custom Content Types and Fields plugin for WordPress is vulnerable to Privilege Escalation via Authorization Bypass in all versions up to, and including, 3.3.9. The vulnerability exists because the pods_admin AJAX router funnels every access check — including the method allowlist, nonce verification, login e...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://plugins.trac.wordpress.org/browser/pods/tags/3.3.9/includes/general.php#L400
- https://www.wordfence.com/threat-intel/vulnerabilities/id/3628032a-3121-45a7-8a78-cfcd8ba6af2f?source=cve

### [CVE-2026-18855](https://plugins.trac.wordpress.org/browser/link-library/tags/7.9.4/link-library-admin.php#L7865)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-18855
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-16 04:16:32 JST
- 更新日: 2026-08-16 04:16:32 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: The Link Library plugin for WordPress is vulnerable to arbitrary file deletion due to insufficient file path validation in the ll_delete_link_fields function in all versions up to, and including, 7.9.4 This makes it possible for unauthenticated attackers to delete arbitrary files on the server, which can easily lead to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://plugins.trac.wordpress.org/browser/link-library/tags/7.9.4/link-library-admin.php#L7865
- https://plugins.trac.wordpress.org/browser/link-library/tags/7.9.4/link-library-admin.php#L7874
- https://plugins.trac.wordpress.org/browser/link-library/tags/7.9.4/link-library.php#L2288
- https://plugins.trac.wordpress.org/browser/link-library/tags/7.9.4/usersubmission.php#L476
- https://plugins.trac.wordpress.org/browser/link-library/tags/7.9.4/usersubmission.php#L52

### [CVE-2026-73046](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-w3xh-mmmh-r54v)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-73046
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-16 07:16:54 JST
- 更新日: 2026-08-16 07:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SiYuan before v3.7.4 improperly restricts excessive authentication attempts in the CheckAuth() middleware. The HTTP Basic Authentication branch, which guards nearly the entire /api/* surface, accepts the workspace access code (Conf.AccessAuthCode) as the Basic Auth password but never consults the CAPTCHA/lockout gate o...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-w3xh-mmmh-r54v
- https://www.vulncheck.com/advisories/siyuan-before-authentication-bypass-via-http-basic-auth

### [CVE-2026-73041](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-fqpw-c3pj-w8g9)

> **Backend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-73041
- 関連キーワード: node.js
- 影響製品: -
- 公開日: 2026-08-16 07:16:53 JST
- 更新日: 2026-08-16 07:16:53 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SiYuan versions before v3.7.4 fail to validate or escape annotation fields written to disk by the setFileAnnotation endpoint. Attackers can inject malicious markup into annotation fields that execute as script in the PDF renderer with full Node.js access when a user opens an annotated PDF.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-fqpw-c3pj-w8g9
- https://www.vulncheck.com/advisories/siyuan-before-remote-code-execution-via-pdf-annotations

### [CVE-2026-73047](https://github.com/siyuan-note/siyuan/security/advisories/GHSA-v97v-gxxg-rhmq)

> **Backend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-73047
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-16 07:16:54 JST
- 更新日: 2026-08-16 07:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: siyuan versions <= 3.7.3 (fixed in v3.7.4) contain a server-side template injection vulnerability in the attribute-view Template calculation feature (introduced in v3.7.0-beta.1). The feature's template engine uses Sprig's unmodified function map, which still exposes the env, expandenv, and getHostByName functions that...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/siyuan-note/siyuan/security/advisories/GHSA-v97v-gxxg-rhmq
- https://www.vulncheck.com/advisories/siyuan-before-server-side-template-injection-via-attribute-view

### [CVE-2026-19897](https://github.com/man-group/dtale/issues/961)

> **Backend** / **LOW** / CVSS: **3.7** / KEV: **no**

- タイトル: CVE-2026-19897
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-16 01:16:38 JST
- 更新日: 2026-08-16 01:16:38 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability has been found in mangroup dtale up to 3.22.0. This issue affects the function Login of the file dtale/auth.py of the component Login Endpoint. Such manipulation leads to improper restriction of excessive authentication attempts. The attack can be executed remotely. This attack is characterized by high...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/man-group/dtale/issues/961
- https://vuldb.com/cve/CVE-2026-19897
- https://vuldb.com/submit/870673
- https://vuldb.com/vuln/390087
- https://vuldb.com/vuln/390087/cti

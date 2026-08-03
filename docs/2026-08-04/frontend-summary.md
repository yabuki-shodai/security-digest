# Frontend CVE Summary (2026-08-04)

## Overview

- 取得日時: 2026-08-04 08:16:00 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 13
- Critical: 1
- High: 4
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-18648](https://github.com/actuator/me.bluemail.mail)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-18648
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-08-04 06:16:37 JST
- 更新日: 2026-08-04 06:16:37 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability was detected in Blix Email Blue Mail Calendar App 2.2.305. Impacted is the function FileDirectory.getDataColumn/FileDirectory.getFileFromUri of the component react-native-receive-sharing-intent. The manipulation of the argument _display_name results in path traversal. The attack is only possible with lo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/actuator/me.bluemail.mail
- https://vuldb.com/cve/CVE-2026-18648
- https://vuldb.com/submit/855049
- https://vuldb.com/vuln/385567
- https://vuldb.com/vuln/385567/cti

### [CVE-2026-69149](https://github.com/angular/angular/pull/69675)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-69149
- 関連キーワード: typescript, javascript, angular
- 影響製品: -
- 公開日: 2026-08-04 02:16:45 JST
- 更新日: 2026-08-04 06:16:41 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 20.3.27, 21.2.19, and 22.0.7, a Cross-Site Scripting (XSS) vulnerability exists in @angular/platform-server's DOM emulation dependency (domino) when serializing the content of fal...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/angular/angular/pull/69675
- https://github.com/angular/angular/pull/69714
- https://github.com/angular/angular/pull/69929
- https://github.com/angular/angular/pull/69930
- https://github.com/angular/angular/security/advisories/GHSA-vpx6-8pjr-4g3v

### [CVE-2026-68945](https://github.com/angular/angular/commit/6867f77ec779a0a24f6339ad6c775f444202103c)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-68945
- 関連キーワード: typescript, javascript, angular
- 影響製品: -
- 公開日: 2026-08-04 02:16:45 JST
- 更新日: 2026-08-04 02:38:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 20.3.27, 21.2.19, and 22.0.2, HttpTransferCache comma-joins repeated request parameters, allowing semantically distinct HttpClient requests to use the same transfer-cache key and...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/angular/angular/commit/6867f77ec779a0a24f6339ad6c775f444202103c
- https://github.com/angular/angular/commit/948a8d6831e8920b54663ec79421da95210e0e35
- https://github.com/angular/angular/commit/a64e2883e9dc4abdac70209129be303de79e5b2b
- https://github.com/angular/angular/commit/a6c7fc5c13e6e494a4c9bd8e773b8d4b2a99b20c
- https://github.com/angular/angular/pull/68571

### [CVE-2026-69151](https://github.com/angular/angular/commit/417a4071a776464d549509ed3aec121dbd2fda5e)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-69151
- 関連キーワード: typescript, javascript, angular
- 影響製品: -
- 公開日: 2026-08-04 02:16:45 JST
- 更新日: 2026-08-04 07:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Angular is a development platform for building mobile and desktop web applications using TypeScript/JavaScript and other languages. Prior to 20.3.27, 21.2.19, and 22.0.1, the Angular compiler i18n pipeline permits i18n-onerror and other i18n-on event-handler attributes, allowing a lower-trust translation file to replac...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/angular/angular/commit/417a4071a776464d549509ed3aec121dbd2fda5e
- https://github.com/angular/angular/commit/6c41f5ca01c0ae045fc7d929b72853a11eb55865
- https://github.com/angular/angular/pull/68821
- https://github.com/angular/angular/pull/69306
- https://github.com/angular/angular/security/advisories/GHSA-jj27-h5hq-8x99

### [CVE-2026-48063](https://github.com/WhiskeySockets/Baileys/commit/3beb08eecfcb4e65722e674034bd84fb11a9de35)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-48063
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-04 06:16:39 JST
- 更新日: 2026-08-04 06:16:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Baileys is a cocket-based TS/JavaScript API for WhatsApp Web. In versions prior to both 6.7.22 and 7.0.0-rc12, any Baileys session can be sent a malicious payload via the placeholderResendMessage and trigger a fake messages.upsert event with a fake message key and payload. This allows anyone to spoof messages. The same...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/WhiskeySockets/Baileys/commit/3beb08eecfcb4e65722e674034bd84fb11a9de35
- https://github.com/WhiskeySockets/Baileys/security/advisories/GHSA-qvv5-jq5g-4cgg

### [CVE-2026-67617](https://github.com/theopaid/Stored-XSS-via-Content-Tag-Names-Microweber-)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-67617
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-08-04 07:16:50 JST
- 更新日: 2026-08-04 07:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Microweber CMS through 2.0.20 contains a stored cross-site scripting vulnerability in the content tagging system that allows admin-authenticated attackers to inject arbitrary JavaScript by submitting malicious payloads via the tag_names parameter of the GET /api/save_content_admin endpoint, bypassing three independent...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/theopaid/Stored-XSS-via-Content-Tag-Names-Microweber-
- https://www.vulncheck.com/advisories/microweber-cms-stored-xss-via-tag-names-parameter

### [CVE-2026-69192](https://github.com/beaugunderson/ip-address/commit/56368cb3d66c73ba0ee9b6b834fd31b22c2fd71e)

> **Frontend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-69192
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-04 05:17:29 JST
- 更新日: 2026-08-04 05:17:29 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ip-address is a library for parsing and manipulating IPv4 and IPv6 addresses in JavaScript. Prior to 10.3.1, Address4 accepts an octet written with a leading zero and decodes it as decimal, while the WHATWG URL host parser, inet_aton, and getaddrinfo all decode a leading zero as octal. The library and the network stack...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/beaugunderson/ip-address/commit/56368cb3d66c73ba0ee9b6b834fd31b22c2fd71e
- https://github.com/beaugunderson/ip-address/releases/tag/v10.3.1
- https://github.com/beaugunderson/ip-address/security/advisories/GHSA-mwp4-54f8-5fhr

### [CVE-2026-38446](https://github.com/fr3akhacks/cve-disclosures/blob/master/osTicket/CVE-2026-38446.md)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-38446
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-04 04:16:46 JST
- 更新日: 2026-08-04 05:17:22 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A stored cross-site scripting (XSS) vulnerability exists in osTicket 1.18.3 due to improper sanitization of the thread entry title field. User-controlled input in the title is stored without adequate HTML escaping and later rendered in multiple staff-facing templates without proper output encoding. An attacker can inje...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/fr3akhacks/cve-disclosures/blob/master/osTicket/CVE-2026-38446.md
- https://github.com/osTicket/osTicket/blob/v1.18.3/include/staff/templates/reply-expand.tmpl.php
- https://github.com/osTicket/osTicket/blob/v1.18.3/include/staff/templates/thread-entries.tmpl.php
- https://github.com/osTicket/osTicket/blob/v1.18.3/include/staff/templates/thread-entry.tmpl.php#L84
- https://github.com/osTicket/osTicket/commit/1e39bf1cf78fa298285f19b98f6a6dbb6808de19

### [CVE-2026-69198](https://github.com/beaugunderson/ip-address/commit/488fe9bc7c35363b4b090494fc38c266d217740d)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-69198
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-04 05:17:30 JST
- 更新日: 2026-08-04 05:17:30 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: ip-address is a library for parsing and manipulating IPv4 and IPv6 addresses in JavaScript. From 10.1.1 until 10.2.2, every special-use classification method is built on isInSubnet, which short-circuits to false whenever the address's own subnet mask is shorter than the reference range's mask. That mask comes verbatim...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/beaugunderson/ip-address/commit/488fe9bc7c35363b4b090494fc38c266d217740d
- https://github.com/beaugunderson/ip-address/releases/tag/v10.2.2
- https://github.com/beaugunderson/ip-address/security/advisories/GHSA-4xrf-jv44-h6hh

### [CVE-2026-52520](https://github.com/LING12138-sg/MyCVE-Report)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-52520
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-04 06:16:40 JST
- 更新日: 2026-08-04 06:16:40 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Emlog CMS <= 2.6.14 contains a stored cross-site scripting (XSS) vulnerability in the article publishing module (/admin/article.php). A remote authenticated attacker can inject arbitrary JavaScript code via the article content. When an administrator reviews or previews the submitted article in the backend, the maliciou...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/LING12138-sg/MyCVE-Report
- https://github.com/emlog/emlog

### [CVE-2026-49131](https://docs.opnsense.org/releases/CE_26.1.html#june-02-2026)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-49131
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-04 06:16:39 JST
- 更新日: 2026-08-04 06:16:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OPNsense before 26.1.9 contains a stored cross-site scripting vulnerability that allows authenticated attackers with firewall rule management privileges to inject arbitrary HTML or JavaScript by embedding payloads in the firewall rule description field via the filter API endpoint. The unsanitized description value is p...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.opnsense.org/releases/CE_26.1.html#june-02-2026
- https://github.com/opnsense/core/commit/b11d6b340716e240868ab19a369e058a46f0876f
- https://www.vulncheck.com/advisories/opnsense-stored-xss-via-firewall-rule-description-field

### [CVE-2026-49132](https://docs.opnsense.org/releases/CE_26.1.html#june-02-2026)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-49132
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-04 06:16:39 JST
- 更新日: 2026-08-04 06:16:39 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OPNsense before 26.1.9 contains a stored cross-site scripting vulnerability that allows authenticated attackers to inject arbitrary HTML or JavaScript by embedding payloads in the certificate description field via the trust certificate API. The unsanitized description value is persisted and later rendered in the Dashbo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://docs.opnsense.org/releases/CE_26.1.html#june-02-2026
- https://github.com/opnsense/core/commit/12b021ff11db38705e92ac4c9af5e07d602da6ba
- https://www.vulncheck.com/advisories/opnsense-stored-xss-via-certificate-description-field

### [CVE-2026-67612](https://jivasecurity.com/writeups/openemr-portal-template-stored-xss)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-67612
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-04 02:16:44 JST
- 更新日: 2026-08-04 02:16:44 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: OpenEMR through 8.2.0 contains a stored cross-site scripting vulnerability in the patient portal template system that allows authenticated administrators to inject arbitrary HTML and JavaScript by storing malicious payloads through the template save mode, which only filters literal PHP open tags. Attackers can exploit...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jivasecurity.com/writeups/openemr-portal-template-stored-xss
- https://www.vulncheck.com/advisories/openemr-stored-xss-via-import-template-php-template-management

# Backend CVE Summary (2026-10-09)

## Overview

- 取得日時: 2026-10-09 11:04:25 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 12
- Critical: 0
- High: 7
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-107383](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/2314c03b785db482599d2befd06f4992e5fc46b3)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-107383
- 関連キーワード: go, node.js, mysql
- 影響製品: -
- 公開日: 2026-10-09 04:17:00 JST
- 更新日: 2026-10-09 05:25:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MariaDB Connector/Node.js is used to connect applications developed on Node.js to MariaDB and MySQL databases. Prior to 3.2.5, 3.3.4, 3.4.7, and 3.5.4, the GeoJSON Polygon and MultiPolygon binary encoders size a Buffer.allocUnsafe() allocation from each ring's numeric length before confirming that the ring is an array....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/2314c03b785db482599d2befd06f4992e5fc46b3
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/a4aa048b57dc47309b80e5cc25a4a8eedb32fd9f
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/b2ca628864b0fc2e3e94ea96910f6b693ad5bd30
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/faa27d1b2b7753a54000f586d5148089b60d1284
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/releases/tag/3.2.5

### [CVE-2026-106429](https://jira.mongodb.org/browse/MONGOCRYPT-986)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-106429
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-09 04:16:58 JST
- 更新日: 2026-10-09 05:49:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An integer underflow in the KMS endpoint-parsing logic of MongoDB libmongocrypt can cause an allocation failure that terminates the application process. This can occur when an authenticated user modifies a key document in the key vault collection, or when an application accepts a KMS endpoint containing a colon after i...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/MONGOCRYPT-986

### [CVE-2026-106433](https://jira.mongodb.org/browse/MONGOCRYPT-964)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-106433
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-09 04:16:59 JST
- 更新日: 2026-10-09 05:49:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper state management in MongoDB libmongocrypt can cause provider-specific data to be treated as an incompatible type when cleaning up a key document containing duplicate masterKey fields. An authenticated actor who can modify key vault documents, or a server that returns such a key document, can cause invalid memo...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/MONGOCRYPT-964

### [CVE-2026-106435](https://jira.mongodb.org/browse/PYTHON-6110)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-106435
- 関連キーワード: python, go, express, mongodb
- 影響製品: -
- 公開日: 2026-10-09 06:17:51 JST
- 更新日: 2026-10-09 06:33:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The MongoDB Python Driver's binary accelerator can read outside a buffer when an application decodes malformed BSON containing a truncated regular-expression element without a trailing NUL byte. An actor who can supply BSON to the documented decode or decode_all API can cause the application process to terminate when t...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/PYTHON-6110

### [CVE-2026-107324](https://jira.mongodb.org/browse/GODRIVER-4102)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-107324
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-09 04:17:00 JST
- 更新日: 2026-10-09 05:49:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An integer overflow in BSON value-length handling in the MongoDB Go Driver can cause a runtime panic when an application validates or accesses a malformed BSON document. An unauthenticated actor who can supply BSON bytes to an affected application may terminate an unprotected application process, causing a denial of se...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/GODRIVER-4102

### [CVE-2026-107325](https://jira.mongodb.org/browse/GODRIVER-4136)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-107325
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-09 04:17:00 JST
- 更新日: 2026-10-09 05:49:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper validation of a BSON array length in the MongoDB Go Driver can cause an out-of-bounds index and runtime panic when an application calls bson.RawArray.Validate or bsoncore.Array.Validate on a malformed four-byte array. An unauthenticated actor who can supply raw BSON array data to an affected application may te...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/GODRIVER-4136

### [CVE-2026-107382](https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/784ca3d757194a05f202d84b0c762321e76a7915)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-107382
- 関連キーワード: go, gin, node.js, mysql
- 影響製品: -
- 公開日: 2026-10-09 04:17:00 JST
- 更新日: 2026-10-09 05:25:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MariaDB Connector/Node.js is used to connect applications developed on Node.js to MariaDB and MySQL databases. From 3.3.0 until 3.5.4, the zero-configuration TLS fingerprint-validation path calls Ed25519PasswordAuth.hash() through Authentication.validateFingerPrint, but Ed25519PasswordAuth.hash() references a seed iden...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/commit/784ca3d757194a05f202d84b0c762321e76a7915
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/releases/tag/3.5.4
- https://github.com/mariadb-corporation/mariadb-connector-nodejs/security/advisories/GHSA-cx2f-j9fh-8g68
- https://hackerone.com/reports/3835450
- https://jira.mariadb.org/browse/CONJS-356

### [CVE-2026-82335](https://www.ibm.com/support/pages/node/7291674)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-82335
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-09 05:17:36 JST
- 更新日: 2026-10-09 05:49:50 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Guardium Data Protection 12.0, 12.1, 12.2 is vulnerable to a heap-based buffer overflow in the MongoDB protocol parser. A remote attacker could send a specially crafted MongoDB SCRAM username containing an excessive length and cause memory corruption, potentially resulting in denial of service or arbitrary code exe...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7291674

### [CVE-2026-107707](https://blog.quarkslab.com/milking-the-last-drop-of-intego-time-for-windows-to-get-its-lpe.html)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-107707
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-09 05:17:35 JST
- 更新日: 2026-10-09 06:35:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Intego Antivirus for Windows through 3.0.0.1 contains a link following vulnerability in its optimization module that allows local unprivileged users to delete arbitrary folders as SYSTEM. Attackers can replace a scanned duplicate file's directory with a junction to C:\Config.msi and abuse Windows Installer rollback to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://blog.quarkslab.com/milking-the-last-drop-of-intego-time-for-windows-to-get-its-lpe.html
- https://www.intego.com/
- https://www.vulncheck.com/advisories/intego-antivirus-through-3.0.0.1-local-privilege-escalation-via-optimization-module-junction

### [CVE-2026-106428](https://jira.mongodb.org/browse/CDRIVER-6370)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-106428
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-09 04:16:58 JST
- 更新日: 2026-10-09 05:49:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An out-of-bounds read in SCRAM authentication response parsing in the MongoDB C Driver can read one byte beyond a fixed-size buffer when processing a malformed server-final message. A server or network intermediary able to provide this message before server-signature verification can cause the application using the dri...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/CDRIVER-6370

### [CVE-2026-106436](https://jira.mongodb.org/browse/PHPC-2739)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-106436
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-09 05:17:31 JST
- 更新日: 2026-10-09 05:49:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The BSON encoder in the MongoDB PHP Driver does not check some return values after a document exceeds libbson's size limit. This can leave the encoder in an invalid state. An unauthenticated actor who can cause an affected application to encode an unusually large data structure can terminate the PHP worker or cause the...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/PHPC-2739

### [CVE-2026-106437](https://jira.mongodb.org/browse/CDRIVER-6423)

> **Backend** / **MEDIUM** / CVSS: **6.2** / KEV: **no**

- タイトル: CVE-2026-106437
- 関連キーワード: go, mongodb
- 影響製品: -
- 公開日: 2026-10-09 04:16:59 JST
- 更新日: 2026-10-09 05:49:23 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The BSON buffer-reservation API in the MongoDB C Driver can record a length smaller than the five-byte BSON minimum. Later append or comparison operations can underflow unsigned length calculations and read or write outside the document buffer. An actor who can influence the length supplied by an embedding application...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://jira.mongodb.org/browse/CDRIVER-6423

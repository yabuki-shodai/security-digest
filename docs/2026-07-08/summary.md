# CVE Digest Summary (2026-07-08)

- 取得日時: 2026-07-08 13:21:18 JST
- 対象: 今日JSTに公開されたCVE、または今日CISA KEVに追加されたCVEのみ
- 新規掲載件数: 30
- 出力対象: 新規CVEのみ

## Critical

### CVE-2026-56843

- 重要度: CRITICAL
- CVSS: 9.9
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 10:16:28 JST
- 更新日: 2026-07-08 10:16:28 JST
- 出典: NVD
- 概要: Incorrect authorization in the XML-RPC API of WebPros Plesk before 18.0.78.4 allows a low-privileged authenticated customer to look up domains they do not own, because ownership is enforced only for certain lookup filters and schema validation is bypassed for legacy protocol versions. This results in cross-tenant discl...
- 参照:
  - https://support.plesk.com/hc/en-us/articles/41178305151255-Vulnerability-in-Plesk-XML-API-Cleartext-FTP-Password-Exposure

### CVE-2026-59800

- 重要度: CRITICAL
- CVSS: 9.8
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 04:16:55 JST
- 更新日: 2026-07-08 05:16:29 JST
- 出典: NVD
- 概要: 9Router before 0.4.44 contains an OS command injection vulnerability in the unauthenticated POST /api/tunnel/tailscale-install endpoint (this route is not covered by the dashboard middleware matcher, so no authorization check is applied). The sudoPassword field from the request body is written to the stdin of a 'sudo -...
- 参照:
  - https://github.com/decolua/9router/security/advisories/GHSA-g6g7-pvmx-m74p
  - https://www.vulncheck.com/advisories/9router-os-command-injection-via-sudopassword-parameter-in-tailscale-install-endpoint
  - https://github.com/decolua/9router/security/advisories/GHSA-g6g7-pvmx-m74p

### CVE-2026-59707

- 重要度: CRITICAL
- CVSS: 9.2
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:29 JST
- 更新日: 2026-07-08 06:17:29 JST
- 出典: NVD
- 概要: LocalAI contains an unauthenticated server-side request forgery vulnerability in the POST /models/apply endpoint that allows attackers to fetch arbitrary internal URLs. The endpoint passes unsanitized gallery URL fields directly to gallery.GetGalleryConfigFromURLWithContext without proper validation, enabling attackers...
- 参照:
  - https://github.com/mudler/LocalAI
  - https://github.com/mudler/LocalAI/commit/f9b968e19d7cbc556d59dceb2e0e450b828a3fda
  - https://github.com/mudler/LocalAI/issues/10665
  - https://www.vulncheck.com/advisories/localai-server-side-request-forgery-via-post-models-apply

### CVE-2026-13019

- 重要度: CRITICAL
- CVSS: 9.8
- KEV掲載: no
- 関連キーワード: linux
- 影響製品: -
- 公開日: 2026-07-08 02:16:35 JST
- 更新日: 2026-07-08 03:16:34 JST
- 出典: NVD
- 概要: Esri Portal for ArcGIS versions 12.1 and earlier on Windows, Linux and Kubernetes have a missing authentication for critical function vulnerability allows a remote, unauthenticated attacker to access an unprotected API.
- 参照:
  - https://www.esri.com/arcgis-blog/products/trust-arcgis/administration/june-2026-arcgis-security-bulletin

### CVE-2026-59705

- 重要度: CRITICAL
- CVSS: 9.8
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 08:16:55 JST
- 更新日: 2026-07-08 08:16:55 JST
- 出典: NVD
- 概要: mem0's openmemory/api component contains an unauthenticated access vulnerability that allows unauthenticated attackers to read, write, and delete arbitrary user memories by accessing API routers registered without authentication middleware. Attackers can supply arbitrary user_id parameters or directly access memory ret...
- 参照:
  - https://github.com/mem0ai/mem0
  - https://github.com/mem0ai/mem0/commit/a3154d59e52386d4e1189c1f5f44819868f76514
  - https://github.com/mem0ai/mem0/issues/6080
  - https://www.vulncheck.com/advisories/mem0-openmemory-api-unauthenticated-access-via-memory-endpoints

### CVE-2026-58473

- 重要度: CRITICAL
- CVSS: 9.3
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:29 JST
- 更新日: 2026-07-08 06:17:29 JST
- 出典: NVD
- 概要: Cognee before 1.2.0 contains an improper access control vulnerability that allows unauthenticated attackers to overwrite the global LLM provider configuration by self-registering an account and calling the settings endpoint, which performs no admin or superuser check. Attackers can redirect all LLM operations instance-...
- 参照:
  - https://github.com/topoteretes/cognee/commit/d10b1b77e2157c6238fd4d1acb1923a048991699
  - https://github.com/topoteretes/cognee/issues/3084
  - https://github.com/topoteretes/cognee/releases/tag/v1.2.0
  - https://www.vulncheck.com/advisories/cognee-unauthorized-llm-configuration-overwrite-via-api-v1-settings

### CVE-2026-59706

- 重要度: CRITICAL
- CVSS: 9.3
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 07:16:54 JST
- 更新日: 2026-07-08 07:16:54 JST
- 出典: NVD
- 概要: mem0 contains unauthenticated config API endpoints that expose LLM API keys in plaintext and allow server-side request forgery via attacker-controlled ollama_base_url parameter. Unauthenticated attackers can retrieve stored secrets like OpenAI API keys via GET /api/v1/config/ or trigger SSRF attacks by setting ollama_b...
- 参照:
  - https://github.com/mem0ai/mem0
  - https://github.com/mem0ai/mem0/commit/a3154d59e52386d4e1189c1f5f44819868f76514
  - https://github.com/mem0ai/mem0/issues/6081
  - https://www.vulncheck.com/advisories/mem0-server-side-request-forgery-and-plaintext-api-key-exposure-via-unauthenticated-config-endpoints

### CVE-2026-46354

- 重要度: CRITICAL
- CVSS: 9.1
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 07:16:52 JST
- 更新日: 2026-07-08 07:16:52 JST
- 出典: NVD
- 概要: Coder allows organizations to provision remote development environments via Terraform. In versions prior tp 2.24.5, 2.29.13, 2.30.8, 2.31.12, 2.32.2, and 2.33.3, `azureidentity.Validate()` verifies that the PKCS#7 signer certificate chains to a trusted Azure CA but never verifies the PKCS#7 signature itself. An attacke...
- 参照:
  - https://github.com/coder/coder/pull/25286
  - https://github.com/coder/coder/releases/tag/v2.24.5
  - https://github.com/coder/coder/releases/tag/v2.29.13
  - https://github.com/coder/coder/releases/tag/v2.30.8
  - https://github.com/coder/coder/releases/tag/v2.31.12

## High

### CVE-2026-55633

- 重要度: HIGH
- CVSS: 8.7
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:27 JST
- 更新日: 2026-07-08 06:17:27 JST
- 出典: NVD
- 概要: DataEase is an open source data visualization and analysis tool. Prior to 2.10.24, a bypass of the H2 zip protocol and file dropper fix allows an authenticated attacker to upload a zip archive disguised with a .ttf extension through FontManage.saveFile and then exploit it through the zip protocol to achieve remote code...
- 参照:
  - https://github.com/dataease/dataease/commit/265b31179f1427c059f739841f2e39aaa6d1b937
  - https://github.com/dataease/dataease/commit/8892a6945b0b7a329a156155270fae58afa895bc
  - https://github.com/dataease/dataease/releases/tag/v2.10.24
  - https://github.com/dataease/dataease/security/advisories/GHSA-8x36-774q-pwqg

### CVE-2026-44454

- 重要度: HIGH
- CVSS: 8.1
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:25 JST
- 更新日: 2026-07-08 07:16:52 JST
- 出典: NVD
- 概要: Coder allows organizations to provision remote development environments via Terraform. Prior to versions 2.29.7 and 2.30.2, the `dotfiles` registry module passed unsanitized user input to shell commands, allowing arbitrary code execution inside a provisioned workspace. Any user who supplied a crafted `dotfiles_uri` val...
- 参照:
  - https://github.com/coder/coder/commit/60e3ab7632f42415d283b9fd5622ee53a4639ceb
  - https://github.com/coder/coder/pull/22011
  - https://github.com/coder/coder/releases/tag/v2.29.7
  - https://github.com/coder/coder/releases/tag/v2.30.2
  - https://github.com/coder/coder/security/advisories/GHSA-m3cr-vc2j-pm27

### CVE-2026-55408

- 重要度: HIGH
- CVSS: 8.4
- KEV掲載: no
- 関連キーワード: node.js
- 影響製品: -
- 公開日: 2026-07-08 07:16:53 JST
- 更新日: 2026-07-08 07:16:53 JST
- 出典: NVD
- 概要: Koodo Reader is an ebook reader. In version 2.3.0 and earlier, Koodo Reader is vulnerable to remote code execution through malicious EPUB files because the open-book IPC handler enables nodeIntegrationInSubFrames and EPUB chapter content is rendered with unsanitized innerHTML. An attacker can craft an EPUB book that, w...
- 参照:
  - https://github.com/koodo-reader/koodo-reader/security/advisories/GHSA-mjr7-w4jq-2rq9

### CVE-2026-55075

- 重要度: HIGH
- CVSS: 7.4
- KEV掲載: no
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-07-08 07:16:53 JST
- 更新日: 2026-07-08 07:16:53 JST
- 出典: NVD
- 概要: Coder allows organizations to provision remote development environments via Terraform. Prior to versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2, two flaws in Coder's OIDC login chained into account takeover. Email-based user matching fell back to linking by email without checking for an existing link to a different IdP sub...
- 参照:
  - https://github.com/coder/coder/pull/25712
  - https://github.com/coder/coder/pull/25713
  - https://github.com/coder/coder/releases/tag/v2.29.17
  - https://github.com/coder/coder/releases/tag/v2.32.7
  - https://github.com/coder/coder/releases/tag/v2.33.8

### CVE-2026-14904

- 重要度: HIGH
- CVSS: 7.1
- KEV掲載: no
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-07-08 02:16:35 JST
- 更新日: 2026-07-08 03:16:35 JST
- 出典: NVD
- 概要: AWS Research and Engineering Studio (RES) is an open-source solution that enables researchers and engineers to create and manage secure virtual desktops and computing resources on AWS. Improper link resolution before file access issue (CWE-59) in the Auth.GetUserPrivateKey API. An authenticated remote user could read a...
- 参照:
  - https://aws.amazon.com/security/security-bulletins/2026-053-aws/
  - https://github.com/aws/res/releases/tag/2026.06

### CVE-2026-23697

- 重要度: HIGH
- CVSS: 8.8
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 02:16:35 JST
- 更新日: 2026-07-08 04:16:51 JST
- 出典: NVD
- 概要: Vtiger CRM before 8.4.0 contains an authenticated file upload vulnerability that allows low-privileged users to achieve remote code execution by uploading a .phar file containing arbitrary PHP code through the Documents module, bypassing the extension denylist in config.inc.php which omits the .phar extension. The uplo...
- 参照:
  - https://jivasecurity.com/writeups/vtiger-rce-phar-upload-cve-2026-23697
  - https://www.vtiger.com/
  - https://www.vulncheck.com/advisories/vtiger-crm-authenticated-file-upload-rce-via-documents-module

### CVE-2026-56811

- 重要度: HIGH
- CVSS: 8.7
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 01:16:40 JST
- 更新日: 2026-07-08 02:16:36 JST
- 出典: NVD
- 概要: Allocation of Resources Without Limits or Throttling vulnerability in phoenixframework phoenix (Phoenix.Socket module) allows an unauthenticated attacker to cause a denial of service against any endpoint that mounts a Phoenix socket with a reachable channel transport (WebSocket or LongPoll). This vulnerability is assoc...
- 参照:
  - https://cna.erlef.org/cves/CVE-2026-56811.html
  - https://github.com/phoenixframework/phoenix/commit/16e295d2fccab185d1292322e2bee5d46c725c8a
  - https://github.com/phoenixframework/phoenix/commit/a612100cd8a4279091abc1a2ef8fb98a6d01c0a1
  - https://github.com/phoenixframework/phoenix/commit/c498ba8cf49f6accbbd0c643a5340b58db891218
  - https://github.com/phoenixframework/phoenix/commit/d19ca0a8d9f82c130b7ed339b9f033433e2dea5e

### CVE-2026-50529

- 重要度: HIGH
- CVSS: 8.7
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:26 JST
- 更新日: 2026-07-08 06:17:26 JST
- 出典: NVD
- 概要: DataEase is an open source data visualization and analysis tool. Prior to 2.10.24, the /de2api/share/proxyInfo share interface generates and returns X-DE-LINK-TOKEN before validating the share password or ticket, allowing unauthenticated attackers who know a protected share UUID to obtain a valid link token for subsequ...
- 参照:
  - https://github.com/dataease/dataease/commit/c4e85a981e53c95b1ea73757db31e3025efdc410
  - https://github.com/dataease/dataease/releases/tag/v2.10.24
  - https://github.com/dataease/dataease/security/advisories/GHSA-7287-qqj9-phr6

### CVE-2026-53729

- 重要度: HIGH
- CVSS: 8.7
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:26 JST
- 更新日: 2026-07-08 06:17:26 JST
- 出典: NVD
- 概要: DataEase is an open source data visualization and analysis tool. Prior to 2.10.24, any authenticated user can download (/exportCenter/download/{id}), delete (/exportCenter/delete), retry (/exportCenter/retry/{id}), or generate download links (/exportCenter/generateDownloadUri/{id}) for export tasks belonging to other u...
- 参照:
  - https://github.com/dataease/dataease/commit/57e90bdcc21c3fa2ec57184671603ad88a5b941b
  - https://github.com/dataease/dataease/releases/tag/v2.10.24
  - https://github.com/dataease/dataease/security/advisories/GHSA-9423-78gr-xjj5

### CVE-2026-53730

- 重要度: HIGH
- CVSS: 8.7
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:26 JST
- 更新日: 2026-07-08 06:17:26 JST
- 出典: NVD
- 概要: DataEase is an open source data visualization and analysis tool. Prior to 2.10.24, the /de2api/datasetData/previewSql endpoint lacks the mandatory @DePermit permission validation annotation, allowing any authenticated user to specify datasourceId=-1, access the built-in engine database, execute arbitrary SQL statements...
- 参照:
  - https://github.com/dataease/dataease/commit/7b47af38b8fa017c9eecb00a4a49264663189e7b
  - https://github.com/dataease/dataease/security/advisories/GHSA-2jmq-vffm-4qmj

### CVE-2026-53751

- 重要度: HIGH
- CVSS: 8.7
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:26 JST
- 更新日: 2026-07-08 06:17:26 JST
- 出典: NVD
- 概要: DataEase is an open source data visualization and analysis tool. Prior to 2.10.24, the H2 database JDBC URL validation logic can be bypassed with special Unicode characters whose case-conversion behavior differs between DataEase validation and H2 parsing, allowing attackers to smuggle dangerous parameters such as init...
- 参照:
  - https://github.com/dataease/dataease/commit/2204258118eac6160a6636ca20dbedb0d3f95747
  - https://github.com/dataease/dataease/releases/tag/v2.10.24
  - https://github.com/dataease/dataease/security/advisories/GHSA-xjhm-r8p8-c2cg

### CVE-2026-55635

- 重要度: HIGH
- CVSS: 8.7
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:27 JST
- 更新日: 2026-07-08 06:17:27 JST
- 出典: NVD
- 概要: DataEase is an open source data visualization and analysis tool. Prior to 2.10.24, chart quota and Y-axis filters embed attacker-controlled filter values directly into generated SQL in Quota2SQLObj.getYWheres() without applying the SQL literal validation and escaping used by other filter paths, allowing an authenticate...
- 参照:
  - https://github.com/dataease/dataease/commit/4463e21cb73d3d4bb8af89a0cb71ee403e4b808a
  - https://github.com/dataease/dataease/security/advisories/GHSA-p758-rx6v-hc8g

### CVE-2026-23698

- 重要度: HIGH
- CVSS: 8.6
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 02:16:36 JST
- 更新日: 2026-07-08 03:16:35 JST
- 出典: NVD
- 概要: Vtiger CRM through 8.4.0 contains an authenticated remote code execution vulnerability in the admin module import feature that allows administrator-level attackers to upload arbitrary PHP files by submitting a crafted zip archive through the ModuleManager import function, which extracts contents directly into the modul...
- 参照:
  - https://jivasecurity.com/writeups/vtiger-rce-module-import-cve-2026-23698
  - https://www.vtiger.com/
  - https://www.vulncheck.com/advisories/vtiger-crm-authenticated-rce-via-module-import-file-upload

### CVE-2026-55418

- 重要度: HIGH
- CVSS: 8.6
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 07:16:53 JST
- 更新日: 2026-07-08 07:16:53 JST
- 出典: NVD
- 概要: FastGPT is an open source AI knowledge base platform. Prior to v4.15.0-beta5, two FastGPT file handlers authorize an unrelated resource and then sign or read an S3 object using a key taken directly from the request, without checking that the key belongs to the caller's team. Because S3 object keys are global within the...
- 参照:
  - https://github.com/labring/FastGPT/commit/decb6d2fb1417fb9e2bca145d2dcc9cbcf06396c
  - https://github.com/labring/FastGPT/pull/7104
  - https://github.com/labring/FastGPT/releases/tag/v4.15.0-beta5
  - https://github.com/labring/FastGPT/security/advisories/GHSA-6rxv-p43w-mmx5

### CVE-2026-57851

- 重要度: HIGH
- CVSS: 8.5
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 02:16:36 JST
- 更新日: 2026-07-08 03:16:39 JST
- 出典: NVD
- 概要: MSI Feature Manager contains a local privilege escalation vulnerability in the KernCoreLib64.sys kernel driver that allows any locally logged-on user to perform arbitrary physical memory read/write and unrestricted I/O port operations by accessing exposed IOCTL handlers without administrator privileges. Attackers can e...
- 参照:
  - https://github.com/readmsr/MSI_FeatureManager_CVE
  - https://www.vulncheck.com/advisories/msi-gamegaraj-kerncorelib64-sys-privilege-escalation-via-ioctl-handlers

### CVE-2026-58583

- 重要度: HIGH
- CVSS: 8.4
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:29 JST
- 更新日: 2026-07-08 06:17:29 JST
- 出典: NVD
- 概要: FluxInk (formerly Sunia SPB Peripheral) Color Management Driver (TcnPeripheral64.sys) 1.0.7.2 allows local privilege escalation for a standard user account via arbitrary physical memory mapping at \Device\PhysicalMemory. Fixed in version 1.0.7.6. The fixed driver is currently available in the Windows 11 25H2 HLK (Hardw...
- 参照:
  - https://github.com/b3s3da/TcnPeripheral64_PoC
  - https://github.com/b3s3da/TcnPeripheral64_PoC/security/advisories/GHSA-x4rw-h4v2-v83h
  - https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/IT/white/2026/va-26-188-01.json
  - https://www.cve.org/CVERecord?id=CVE-2026-58583

### CVE-2026-49471

- 重要度: HIGH
- CVSS: 8.3
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:25 JST
- 更新日: 2026-07-08 06:17:25 JST
- 出典: NVD
- 概要: Serena is a powerful MCP toolkit for coding that provides semantic retrieval and editing capabilities. Prior to v1.5.2, Serena's built-in web dashboard exposes an unauthenticated Flask API on a fixed, predictable port, with no authentication, no CSRF protection, and no Host header validation. A DNS rebinding attack all...
- 参照:
  - https://github.com/oraios/serena/commit/016ccbe1c095a3eed7967737ac1d4df2754f5d96
  - https://github.com/oraios/serena/releases/tag/v1.5.2
  - https://github.com/oraios/serena/security/advisories/GHSA-37h2-6p4f-mp3q

### CVE-2026-57172

- 重要度: HIGH
- CVSS: 8.3
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:28 JST
- 更新日: 2026-07-08 06:17:28 JST
- 出典: NVD
- 概要: DataEase is an open source data visualization and analysis tool. Prior to 2.10.24, ShareSecretManage uses a hardcoded default share link signature key, allowing an attacker who can obtain a passwordless share for a resource and user to use the known key link-pwd-fit2cloud to forge linkToken JWTs, bypass TokenFilter ver...
- 参照:
  - https://github.com/dataease/dataease/commit/356e83b518603f5612104760ced80aae8fc5d675
  - https://github.com/dataease/dataease/security/advisories/GHSA-7cpg-f4cj-7pgm

### CVE-2026-55076

- 重要度: HIGH
- CVSS: 7.4
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 08:16:55 JST
- 更新日: 2026-07-08 08:16:55 JST
- 出典: NVD
- 概要: Coder allows organizations to provision remote development environments via Terraform. Prior to versions 2.29.7, 2.32.7, 2.33.8, and 2.34.2, Coder's OIDC callback checked `email_verified` with a direct Go `bool` type assertion. When an IdP returned the claim as a non-boolean (for example the string `"false"`) or omitte...
- 参照:
  - https://github.com/coder/coder/pull/25712
  - https://github.com/coder/coder/pull/25713
  - https://github.com/coder/coder/releases/tag/v2.29.17
  - https://github.com/coder/coder/releases/tag/v2.32.7
  - https://github.com/coder/coder/releases/tag/v2.33.8

### CVE-2026-50007

- 重要度: HIGH
- CVSS: 7.2
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:25 JST
- 更新日: 2026-07-08 06:17:25 JST
- 出典: NVD
- 概要: Actual is an open-source personal finance application. Prior to 26.7.0, a missing authorization issue allows a shared user with user_access on a budget file to perform owner-only file management actions. A non-owner shared user can call file-management endpoints intended for higher-privilege users, including /delete-us...
- 参照:
  - https://github.com/actualbudget/actual/commit/18a8dc03c48eeb2e8252669a80673e6a9933b5fd
  - https://github.com/actualbudget/actual/commit/3b9e79ed5ee795a80bbae214d6ebb2755289d7f2
  - https://github.com/actualbudget/actual/pull/7977
  - https://github.com/actualbudget/actual/pull/8333
  - https://github.com/actualbudget/actual/security/advisories/GHSA-23vm-ffgg-qvjr

### CVE-2026-55631

- 重要度: HIGH
- CVSS: 7.2
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:27 JST
- 更新日: 2026-07-08 06:17:27 JST
- 出典: NVD
- 概要: DataEase is an open source data visualization and analysis tool. Prior to 2.10.24, the font management module allows authenticated users to submit an arbitrary fileTransName when creating a font record; when the record is later deleted, the backend concatenates that stored value with the font storage directory and pass...
- 参照:
  - https://github.com/dataease/dataease/commit/8892a6945b0b7a329a156155270fae58afa895bc
  - https://github.com/dataease/dataease/releases/tag/v2.10.24
  - https://github.com/dataease/dataease/security/advisories/GHSA-r99p-w8fc-93g6

### CVE-2026-50530

- 重要度: HIGH
- CVSS: 7.1
- KEV掲載: no
- 関連キーワード: -
- 影響製品: -
- 公開日: 2026-07-08 06:17:26 JST
- 更新日: 2026-07-08 06:17:26 JST
- 出典: NVD
- 概要: DataEase is an open source data visualization and analysis tool. Prior to 2.10.24, a share mode chart data interface only validates that sceneId matches the resourceId in the link token and fails to validate whether tableId and field IDs in the request body belong to the shared resource, allowing an attacker with a val...
- 参照:
  - https://github.com/dataease/dataease/commit/c4e85a981e53c95b1ea73757db31e3025efdc410
  - https://github.com/dataease/dataease/releases/tag/v2.10.24
  - https://github.com/dataease/dataease/security/advisories/GHSA-qcf4-345v-6vg9

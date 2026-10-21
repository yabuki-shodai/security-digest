# Frontend CVE Summary (2026-10-21)

## Overview

- 取得日時: 2026-10-21 09:33:56 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 14
- Critical: 1
- High: 1
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-105772](https://github.com/google/adk-js/commit/710b4ebed118b0ded8fc257e5d0099e6b2008bc0)

> **Frontend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-105772
- 関連キーワード: typescript, go
- 影響製品: -
- 公開日: 2026-10-21 03:17:16 JST
- 更新日: 2026-10-21 05:06:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Path Traversal (CWE-22) in FileArtifactService in Google ADK TypeScript (@google/adk) versions 0.4.0 before 0.6.0 allows a remote unauthenticated attacker to read files matching the artifact directory layout or write files (when an agent tool invokes saveArtifact) outside the intended artifact storage root via crafted...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/google/adk-js/commit/710b4ebed118b0ded8fc257e5d0099e6b2008bc0
- https://github.com/google/adk-js/commit/8c0eaa160a43c1d791d5838a5de6ac87d905cf70
- https://github.com/google/adk-js/pull/210
- https://github.com/google/adk-js/security/advisories/GHSA-8hc4-6xx6-3rh3

### [CVE-2026-112949](https://github.com/vitest-dev/vitest/commit/15cc006aa9f8683dc5f7e895d011fa7dc751ce35)

> **Frontend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-112949
- 関連キーワード: typescript, javascript, vite, vitest, gin
- 影響製品: -
- 公開日: 2026-10-21 01:17:05 JST
- 更新日: 2026-10-21 04:56:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vitest is a Vite-native testing framework for JavaScript and TypeScript projects. From 2.1.0-beta.7 until 4.1.12 and 5.0.3, an unauthenticated non-browser WebSocket client that can reach a development server using interceptorPlugin can register a manual mock whose attacker-controlled url createManualModuleSource insert...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vitest-dev/vitest/commit/15cc006aa9f8683dc5f7e895d011fa7dc751ce35
- https://github.com/vitest-dev/vitest/commit/b825313243dc55757e8d7c0f9e7a792135e13473
- https://github.com/vitest-dev/vitest/releases/tag/v4.1.12
- https://github.com/vitest-dev/vitest/releases/tag/v5.0.3
- https://github.com/vitest-dev/vitest/security/advisories/GHSA-qxg6-89mg-rqv8

### [CVE-2026-112950](https://github.com/vitest-dev/vitest/commit/15cc006aa9f8683dc5f7e895d011fa7dc751ce35)

> **Frontend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-112950
- 関連キーワード: typescript, javascript, vite, vitest, gin
- 影響製品: -
- 公開日: 2026-10-21 01:17:05 JST
- 更新日: 2026-10-21 04:56:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vitest is a Vite-native testing framework for JavaScript and TypeScript projects. From 4.1.11 until 4.1.12 and 5.0.3, isFileLoadingAllowed and the filesystem read interpret backslashes differently on Windows in packages/mocker/src/node/interceptorPlugin.ts. When a client can reach the Vite dev server on Windows and reg...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vitest-dev/vitest/commit/15cc006aa9f8683dc5f7e895d011fa7dc751ce35
- https://github.com/vitest-dev/vitest/commit/b825313243dc55757e8d7c0f9e7a792135e13473
- https://github.com/vitest-dev/vitest/releases/tag/v4.1.12
- https://github.com/vitest-dev/vitest/releases/tag/v5.0.3
- https://github.com/vitest-dev/vitest/security/advisories/GHSA-xp26-3454-mjgp

### [CVE-2026-111767](https://github.com/modelcontextprotocol/typescript-sdk/commit/727075b5bbeb77fbea22041b36b72a73042160fa)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-111767
- 関連キーワード: typescript
- 影響製品: -
- 公開日: 2026-10-21 04:17:30 JST
- 更新日: 2026-10-21 04:53:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MCP TypeScript SDK is the official TypeScript SDK for Model Context Protocol servers and clients. From version 1.24.0 to before version 1.32.0, the experimental tasks feature (taskStore) did not check which session created a task. Clients sharing one InMemoryTaskStore could list, read and cancel each other's tasks. Thi...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/modelcontextprotocol/typescript-sdk/commit/727075b5bbeb77fbea22041b36b72a73042160fa
- https://github.com/modelcontextprotocol/typescript-sdk/pull/2925
- https://github.com/modelcontextprotocol/typescript-sdk/security/advisories/GHSA-22jm-h49p-29qw

### [CVE-2026-112944](https://github.com/vitejs/launch-editor/commit/f6e6701bb1f16f2dd242b321374f1b6cca6eb6d4)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-112944
- 関連キーワード: vite, gin, node.js
- 影響製品: -
- 公開日: 2026-10-21 00:17:17 JST
- 更新日: 2026-10-21 04:55:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: launch-editor allows users to open files with line numbers in editor from Node.js. Prior to 2.14.2, when an attacker can create a filesystem entry beginning with plus or minus in the working directory, an affected editor is selected, and the path can remain relative or is converted to a relative WSL path, launchEditor...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vitejs/launch-editor/commit/f6e6701bb1f16f2dd242b321374f1b6cca6eb6d4
- https://github.com/vitejs/launch-editor/pull/156
- https://github.com/vitejs/launch-editor/releases/tag/v2.14.2
- https://github.com/vitejs/launch-editor/security/advisories/GHSA-r825-w8mm-5pxw

### [CVE-2026-112947](https://github.com/vitejs/vite/commit/b6c6d2fb3f853aab4092dc25f0d6816a96c23dff)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-112947
- 関連キーワード: javascript, vite, gin
- 影響製品: -
- 公開日: 2026-10-21 01:17:05 JST
- 更新日: 2026-10-21 04:56:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vite is a frontend tooling framework for JavaScript. From 8.2.0 until 8.2.4 and 8.3.3, the first 4 bytes of files outside of server.fs setting can be returned to the browser by a request containing ?vite-wasm-instance. Requests containing the ?vite-wasm-instance query are handled by the internal Wasm plugin's load hook...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vitejs/vite/commit/b6c6d2fb3f853aab4092dc25f0d6816a96c23dff
- https://github.com/vitejs/vite/commit/ba8b7ab43b4afa5d0292ab4b6e3a7b5033cc9c73
- https://github.com/vitejs/vite/pull/23655
- https://github.com/vitejs/vite/security/advisories/GHSA-vfpm-58rq-9qcg

### [CVE-2026-112948](https://github.com/vitest-dev/vitest/commit/28dc1edfb6ba5a181fe208576989063795aeadb3)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-112948
- 関連キーワード: javascript, vite, vitest
- 影響製品: -
- 公開日: 2026-10-21 01:17:05 JST
- 更新日: 2026-10-21 04:56:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vitest is a testing framework powered by Vite. From 5.0.0-beta.6 until 5.0.5, Vitest dev servers can misapply server.fs.deny because project servers replace Vite's defaults and the root server adds .vitest-secret-token after Vite compiles its matcher. An attacker who can reach an affected UI, Browser Mode, or API serve...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vitest-dev/vitest/commit/28dc1edfb6ba5a181fe208576989063795aeadb3
- https://github.com/vitest-dev/vitest/pull/11578
- https://github.com/vitest-dev/vitest/releases/tag/v5.0.5
- https://github.com/vitest-dev/vitest/security/advisories/GHSA-p458-7748-mcp3

### [CVE-2026-112946](https://github.com/vitejs/vite/commit/170b92791421bcd484f7325936d989a82d6bd4aa)

> **Frontend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-112946
- 関連キーワード: javascript, vite
- 影響製品: -
- 公開日: 2026-10-21 01:17:05 JST
- 更新日: 2026-10-21 04:56:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vite is a frontend tooling framework for JavaScript. Prior to 6.4.4, 7.3.7, 8.1.6, 8.2.4, and 8.3.3, import analysis can record a root-relative browser URL in safeModulePaths instead of the cleaned resolved module identifier. On a network-accessible, non-Windows development server, an imported project file whose URL ma...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vitejs/vite/commit/170b92791421bcd484f7325936d989a82d6bd4aa
- https://github.com/vitejs/vite/commit/45c0e3392a298626955a0ab93a8e51232daac721
- https://github.com/vitejs/vite/commit/c3e06f92e969952466b4e2f5801e85e1e00cd905
- https://github.com/vitejs/vite/commit/e570d8d016096b5f8f6f09808376ca6cf73f27d0
- https://github.com/vitejs/vite/commit/f0d76c7da13d5e794807b82f0b86c1931a8438e3

### [CVE-2026-112945](https://github.com/vitejs/vite/commit/7dafd8e56f152403a3230608fa4005273c2e9e17)

> **Frontend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-112945
- 関連キーワード: javascript, vite
- 影響製品: -
- 公開日: 2026-10-21 01:17:05 JST
- 更新日: 2026-10-21 04:56:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vite is a frontend tooling framework for JavaScript. Prior to 6.4.4, 7.3.7, 8.1.6, 8.2.4, and 8.3.3, applications using custom middleware are vulnerable when they pass an unchanged browser request URL to server.transformIndexHtml. getHtmlFilename uses the query-bearing request URL to resolve an existing local file whil...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vitejs/vite/commit/7dafd8e56f152403a3230608fa4005273c2e9e17
- https://github.com/vitejs/vite/pull/23653
- https://github.com/vitejs/vite/security/advisories/GHSA-9jrq-w75r-8gcw

### [CVE-2026-113712](https://github.com/cachethq/cachet/security/advisories/GHSA-x397-5hrv-j9m9)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-113712
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-21 04:17:33 JST
- 更新日: 2026-10-21 04:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cachet is an open-source status page system. Versions 2.4.1 and earlier have a stored Cross-Site Scripting (XSS) vulnerability in the incident creation form, allowing an authenticated attacker to inject malicious HTML/JavaScript that executes in the browser of any user who views the status page, potentially leading to...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/cachethq/cachet/security/advisories/GHSA-x397-5hrv-j9m9
- https://github.com/cachethq/core/commit/23adbb88ffa819f92be4a905ff1d812670d980a2
- https://github.com/cachethq/core/commit/57b44a8bac0b250b0d5751e93e0349070d14606e

### [CVE-2014-125132](https://codevigilant.com/disclosure/wp-plugin-blogroll-fun-a3-cross-site-scripting-xss/)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2014-125132
- 関連キーワード: javascript, gin, echo
- 影響製品: -
- 公開日: 2026-10-21 06:17:12 JST
- 更新日: 2026-10-21 06:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPressプラグイン「Blogroll Fun」（0.8.5未満）における、`blogroll.php`の`k`パラメータに対する不適切な入力処理に起因する反射型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 未認証の攻撃者が作成した悪意のあるリクエストを介して、被害者のブラウザ上で任意のJavaScriptを実行される可能性があります。
- 推奨対応: プラグインをバージョン0.8.5以降にアップデートしてください。

#### References
- https://codevigilant.com/disclosure/wp-plugin-blogroll-fun-a3-cross-site-scripting-xss/
- https://github.com/projectdiscovery/nuclei-templates/blob/main/http/vulnerabilities/wordpress/wp-blogroll-fun-xss.yaml
- https://wordpress.org/plugins/blogroll-fun/
- https://www.acunetix.com/vulnerabilities/web/wordpress-plugin-blogroll-fun-show-last-post-and-last-update-time-cross-site-scripting-0-8-4/
- https://www.vulncheck.com/advisories/blogroll-fun-wordpress-plugin-0.8.5-reflected-xss-via-blogroll-php

### [CVE-2026-28330](https://documentation.solarwinds.com/en/success_center/orionplatform/content/core-secure-configuration.htm)

> **Frontend** / **MEDIUM** / CVSS: **4.6** / KEV: **no**

- タイトル: CVE-2026-28330
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-21 02:17:39 JST
- 更新日: 2026-10-21 04:59:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SolarWinds Observability Self-Hostedにおける格納型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 認証された攻撃者が悪意のあるコンテンツやスクリプトを注入し、該当ページを閲覧した他の認証済みユーザーのブラウザ上でそれを実行させる可能性があります。
- 推奨対応: ベンダーが提供する最新の修正バージョンへのアップデートを検討してください。

#### References
- https://documentation.solarwinds.com/en/success_center/orionplatform/content/core-secure-configuration.htm
- https://documentation.solarwinds.com/en/success_center/orionplatform/content/release_notes/hco_2026-4_release_notes.htm
- https://www.solarwinds.com/trust-center/security-advisories/CVE-2026-28330

### [CVE-2014-125131](https://github.com/projectdiscovery/nuclei-templates/blob/main/http/vulnerabilities/dedecms/dedecms-config-xss.yaml)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2014-125131
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-21 06:17:12 JST
- 更新日: 2026-10-21 06:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: DedeCMS 5.6および5.7の`/include/dialog/config.php`における、`adminDirHand`パラメータの処理に起因する反射型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 未認証の攻撃者が送信したリクエストにより、被害者のブラウザ上で任意のJavaScriptが実行される可能性があります。
- 推奨対応: 修正されたバージョンへのアップデートまたは該当箇所への入力サニタイズ対策を実施してください。

#### References
- https://github.com/projectdiscovery/nuclei-templates/blob/main/http/vulnerabilities/dedecms/dedecms-config-xss.yaml
- https://www.cnblogs.com/milantgh/p/3615853.html
- https://www.dedecms.com/
- https://www.vulncheck.com/advisories/dedecms-5.6-5.7-reflected-xss-via-admindirhand-in-config-php

### [CVE-2026-113683](https://github.com/jcrodriguez-dis/moodle-mod_vpl/blob/V4.5.0/similarity/diff.class.php#L412-L419)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-113683
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-10-21 01:17:13 JST
- 更新日: 2026-10-21 05:11:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Moodle向けプラグイン「VPL（Virtual Programming Lab）」（5.0.0未満）の`similarity/diff.php`におけるパラメータエンコード不備による反射型クロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 攻撃者が作成したリンクを特定の権限を持つユーザーが開いた場合、そのセッション下で意図しない操作の実行やデータ漏洩が発生する可能性があります。
- 推奨対応: VPLをバージョン5.0.0以降にアップデートしてください。

#### References
- https://github.com/jcrodriguez-dis/moodle-mod_vpl/blob/V4.5.0/similarity/diff.class.php#L412-L419
- https://github.com/jcrodriguez-dis/moodle-mod_vpl/commit/5dd7fe00df2816b692f8ea262c6fa8cdee0b26b7
- https://github.com/jcrodriguez-dis/moodle-mod_vpl/releases/tag/V5.0.0
- https://www.vulncheck.com/advisories/vpl-for-moodle-before-5.0.0-reflected-xss-via-similarity-diff-php-filename

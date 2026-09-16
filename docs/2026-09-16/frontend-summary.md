# Frontend CVE Summary (2026-09-16)

## Overview

- 取得日時: 2026-09-16 09:13:08 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 19
- Critical: 1
- High: 11
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-59160](https://github.com/DerYeger/yeger/commit/a6c41db6b575cccdd8ff89dbe8ce1792ad062852)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-59160
- 関連キーワード: next.js, npm
- 影響製品: -
- 公開日: 2026-09-16 02:17:23 JST
- 更新日: 2026-09-16 03:17:26 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Yeger monorepoのturbo-graphパッケージ（2.8.9未満）において、/api/run エンドポイントが無認証かつタスク許可リストなしで全インターフェース上に公開され、クエリパラメータ経由で任意タスク名をspawn()に渡してしまう問題。
- 影響: 隣接ネットワーク上の攻撃者が、対象リポジトリのturbo.jsonに定義された任意のタスクを開発者権限で実行でき、シークレット漏洩やファイル変更、サービス妨害を引き起こす可能性があります。
- 推奨対応: turbo-graph を 2.8.9 以降にアップデートしてください。

#### References
- https://github.com/DerYeger/yeger/commit/a6c41db6b575cccdd8ff89dbe8ce1792ad062852
- https://github.com/DerYeger/yeger/releases/tag/@yeger/turbo-graph@2.8.9
- https://github.com/DerYeger/yeger/security/advisories/GHSA-2r5q-h53f-9rp3
- https://github.com/DerYeger/yeger/security/advisories/GHSA-2r5q-h53f-9rp3

### [CVE-2026-91983](https://github.com/go-vikunja/vikunja/security/advisories/GHSA-9rg3-v78m-26q8)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-91983
- 関連キーワード: react
- 影響製品: -
- 公開日: 2026-09-16 01:17:55 JST
- 更新日: 2026-09-16 01:17:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vikunja 2.6.0 未満のタスク読み取りエンドポイントにおいて、クエリパラメータ（expand）に対する認可検証が不十分であり、APIトークンスコープをバイパスできる脆弱性。
- 影響: 限定されたスコープのトークンを持つ攻撃者が、コメントやリアクション、タイムエントリなどの制限された情報へアクセスする可能性があります。
- 推奨対応: Vikunja を 2.6.0 以降にアップデートしてください。

#### References
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-9rg3-v78m-26q8
- https://www.vulncheck.com/advisories/vikunja-before-2.6.0-api-token-scope-bypass-via-expand-parameter
- https://github.com/go-vikunja/vikunja/security/advisories/GHSA-9rg3-v78m-26q8

### [CVE-2026-59973](https://github.com/agentfront/frontmcp/commit/96a78eaa5c6c4bc51cced557d83d1a03344cb03d)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-59973
- 関連キーワード: typescript, gin
- 影響製品: -
- 公開日: 2026-09-16 01:17:18 JST
- 更新日: 2026-09-16 01:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: FrontMCP（mcp-from-openapi 2.3.0-2.5.0未満、frontmcp 1.2.1-1.5.0未満など）において、OpenAPI仕様読込時の外部$refガードによるIPアドレス検証やリダイレクト処理が不十分であるため発生するSSRF脆弱性。
- 影響: 認証済みユーザーが内部ネットワークや管理用API、メタデータサービス宛てのリクエストを発生させ、内部情報の露出を引き起こす可能性があります。
- 推奨対応: mcp-from-openapi を 2.5.0 以降、frontmcp および @frontmcp/adapters を 1.5.0 以降にアップデートしてください。

#### References
- https://github.com/agentfront/frontmcp/commit/96a78eaa5c6c4bc51cced557d83d1a03344cb03d
- https://github.com/agentfront/frontmcp/pull/496
- https://github.com/agentfront/frontmcp/releases/tag/v1.5.0
- https://github.com/agentfront/frontmcp/security/advisories/GHSA-65h7-9wrw-629c
- https://github.com/agentfront/mcp-from-openapi/commit/be3409cce6e97642696d4ee5a4e4e2712490b277

### [CVE-2026-91931](https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-vcwp-f9rq-3887)

> **Frontend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-91931
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-09-16 01:17:43 JST
- 更新日: 2026-09-16 01:17:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Flowise 3.1.4 未満の Custom MCP ノードにおいて、mcpServerConfig パラメータ経由で供給された npx パッケージ名を適切に制限せず実行してしまう脆弱性。
- 影響: 認証された攻撃者が任意のnpmパッケージを指定してnpxを実行させることで、Flowiseサーバー上で任意のコードを実行する可能性があります。
- 推奨対応: Flowise を 3.1.4 以降にアップデートしてください。

#### References
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-vcwp-f9rq-3887
- https://www.vulncheck.com/advisories/flowise-before-3.1.4-remote-code-execution-via-custom-mcp-npx

### [CVE-2026-91929](https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-7x8x-vv46-4579)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-91929
- 関連キーワード: vite
- 影響製品: -
- 公開日: 2026-09-16 01:17:43 JST
- 更新日: 2026-09-16 01:17:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Flowise 3.1.4 未満のエンプラ向けエンドポイントにおいて、操作実行前にリソース所有権を検証しないクロスプラットフォーム認可の欠陥。
- 影響: Enterpriseアクセス権を持つ攻撃限のあるユーザーが、任意のワークスペース削除、他組織への侵入、ロール変更、SSOシークレットの不正利用を行う可能性があります。
- 推奨対応: Flowise を 3.1.4 以降にアップデートしてください。

#### References
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-7x8x-vv46-4579
- https://www.vulncheck.com/advisories/flowise-before-3.1.4-cross-tenant-authorization-bypass

### [CVE-2026-91938](https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-9cvr-5wv9-2gxr)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-91938
- 関連キーワード: playwright
- 影響製品: -
- 公開日: 2026-09-16 01:17:45 JST
- 更新日: 2026-09-16 01:17:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Flowise 3.1.4 未満の Cheerio、Playwright、Puppeteer ドキュメントローダーノードにおいて、SSRF対策を回避して任意URLへアクセス可能な脆弱性。
- 影響: 攻撃者が任意のURLを指定することで、クラウドメタデータや内部ネットワークリソースの内容をドキュメントテキストとして取得する可能性があります。
- 推奨対応: Flowise を 3.1.4 以降にアップデートしてください。

#### References
- https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-9cvr-5wv9-2gxr
- https://www.vulncheck.com/advisories/flowise-before-3.1.4-server-side-request-forgery-via-document-loaders

### [CVE-2026-81897](https://documentation.concretecms.org/developers/introduction/version-history/953-release-notes)

> **Frontend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-81897
- 関連キーワード: javascript, express
- 影響製品: -
- 公開日: 2026-09-16 02:17:27 JST
- 更新日: 2026-09-16 02:17:27 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Concrete CMS 9.5.3 未満のExpressエンティティフォームダッシュボードにおいて、save_controlアクションのAnti-CSRFトークン検証および出力エスケープが不足している脆弱性。
- 影響: 管理者をCSRF攻撃に誘導して悪意あるマークアップを保存させ、後から該当項目を開いた管理者のブラウザ上で持続型XSSを実行させる可能性があります。
- 推奨対応: Concrete CMS を 9.5.3 以降にアップデートしてください。

#### References
- https://documentation.concretecms.org/developers/introduction/version-history/953-release-notes

### [CVE-2026-18111](https://documentation.concretecms.org/developers/introduction/version-history/953-release-notes)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-18111
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-16 02:17:11 JST
- 更新日: 2026-09-16 02:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Concrete CMS（9.5.3未満、および8.5.21未満）の複数のブロックにおいて、外部リンクURLの検証とエスケープが不十分なため発生する格納型XSSの脆弱性。
- 影響: ページ編集権限を持つユーザーが悪意のあるリンクを埋め込み、ページを閲覧・編集したユーザーのセッションでJavaScriptを実行させて権限昇格やアカウント乗っ取りを引き起こす可能性があります。
- 推奨対応: Concrete CMS を 9.5.3 以降（8系の場合は8.5.21以降）にアップデートしてください。

#### References
- https://documentation.concretecms.org/developers/introduction/version-history/953-release-notes

### [CVE-2026-55690](https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/commit/9215564bf28a0ceb40be550a55ab78efc0accc56)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-55690
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-16 02:17:22 JST
- 更新日: 2026-09-16 05:17:21 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MediaWiki EmbedVideo 拡張機能（4.1.0未満）において、未定義のサービス名が例外テキスト経由でエスケープされずにHTML出力される問題による格納型XSS脆弱性。
- 影響: ページ編集が可能なユーザーがエラー出力経由でスクリプトを保存し、閲覧者のブラウザ上で任意のJavaScriptを実行させる可能性があります。
- 推奨対応: EmbedVideo 拡張機能を 4.1.0 以降にアップデートしてください。

#### References
- https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/commit/9215564bf28a0ceb40be550a55ab78efc0accc56
- https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/releases/tag/v4.1.0
- https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/security/advisories/GHSA-c29q-5xm7-5p62

### [CVE-2026-55692](https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/commit/370156335b325bb81d14d89edf0a1f2643d50a84)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-55692
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-09-16 02:17:22 JST
- 更新日: 2026-09-16 04:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MediaWiki EmbedVideo 拡張機能（4.1.0未満）において、生成される属性値に対するシングルクォートのエスケープ不足によりHTML属性が脱出可能な格納型XSS脆弱性。
- 影響: ページ編集権限を持つユーザーがイベントハンドラ属性などを注入し、閲覧者のブラウザ上で任意のJavaScriptを実行させる可能性があります。
- 推奨対応: EmbedVideo 拡張機能を 4.1.0 以降にアップデートしてください。

#### References
- https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/commit/370156335b325bb81d14d89edf0a1f2643d50a84
- https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/releases/tag/v4.1.0
- https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/security/advisories/GHSA-5c7p-g73q-rpg5
- https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/security/advisories/GHSA-5c7p-g73q-rpg5

### [CVE-2026-53966](https://github.com/xwiki/xwiki-platform/commit/1ddb954767e50782be960b953b012c1242f6843b)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-53966
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-16 00:17:17 JST
- 更新日: 2026-09-16 04:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: XWiki Platform is a generic wiki platform. From 13.4-rc-1 until 16.10.17, 17.4.10, 17.10.4, and 18.1.0-rc-1, the Live Data edit REST API allows a user who can edit a page to change that page's rights without executing the normal document-saving authorization checks. The user can grant script right and then execute pote...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/xwiki/xwiki-platform/commit/1ddb954767e50782be960b953b012c1242f6843b
- https://github.com/xwiki/xwiki-platform/commit/448b0f074cc6711410eb2647c4740454c92d1626
- https://github.com/xwiki/xwiki-platform/commit/778b82b4806ce7ebddb775f953545ff73b841f8b
- https://github.com/xwiki/xwiki-platform/commit/fbad7dac8f46c560577e41b9259cbbbbd343e6fc
- https://github.com/xwiki/xwiki-platform/releases/tag/xwiki-platform-16.10.17

### [CVE-2026-55691](https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/commit/370156335b325bb81d14d89edf0a1f2643d50a84)

> **Frontend** / **HIGH** / CVSS: **8.6** / KEV: **no**

- タイトル: CVE-2026-55691
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-16 02:17:22 JST
- 更新日: 2026-09-16 02:17:22 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The EmbedVideo Extension is a MediaWiki extension which adds a parser function called #ev and various parser tags for embedding video clips from various video sharing services. Prior to 4.1.0, EmbedHtmlFormatter::toHtml in includes/EmbedService/EmbedHtmlFormatter.php passes the user-supplied class value directly to spr...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/commit/370156335b325bb81d14d89edf0a1f2643d50a84
- https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/releases/tag/v4.1.0
- https://github.com/StarCitizenWiki/mediawiki-extensions-EmbedVideo/security/advisories/GHSA-7h5p-637f-jfr7

### [CVE-2026-88616](https://github.com/dromara/RuoYi-Vue-Plus)

> **Frontend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-88616
- 関連キーワード: vue
- 影響製品: -
- 公開日: 2026-09-16 00:17:24 JST
- 更新日: 2026-09-16 05:19:19 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: An issue in RuoYi-Vue-Plus 6.0.0 allows a remote attacker to execute arbitrary code via the FlwTaskController.java component, and the FlwTaskServiceImpl.completeTask, CompleteExecuteComponent.process, Warm-Flow TaskService.skip, POST /workflow/task/completeTask components
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dromara/RuoYi-Vue-Plus
- https://github.com/returnwrong/returnwrong-security-advisories/blob/main/CVE-2026-88616.md
- https://github.com/returnwrong/returnwrong-security-advisories/blob/main/CVE-2026-88616.md

### [CVE-2026-91942](https://github.com/unclecode/crawl4ai/security/advisories/GHSA-7g3g-vhm6-79f3)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-91942
- 関連キーワード: javascript, gin, docker
- 影響製品: -
- 公開日: 2026-09-16 01:17:46 JST
- 更新日: 2026-09-16 01:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: crawl4ai before 0.9.3 contains a DOM-based cross-site scripting vulnerability in the Docker Playground UI that assigns untrusted crawl results to element.innerHTML. Attackers can craft malicious PDFs with event-handler markup to execute JavaScript in the Playground origin and steal API tokens from sessionStorage for au...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/unclecode/crawl4ai/security/advisories/GHSA-7g3g-vhm6-79f3
- https://www.vulncheck.com/advisories/crawl4ai-before-0.9.3-cross-site-scripting-via-innerhtml

### [CVE-2026-55630](https://github.com/kiwitcms/Kiwi/commit/1c2ecc8485faeefd84a526314a0a60d132fbbc09)

> **Frontend** / **NONE** / CVSS: **0.0** / KEV: **no**

- タイトル: CVE-2026-55630
- 関連キーワード: javascript, docker
- 影響製品: -
- 公開日: 2026-09-16 01:17:14 JST
- 更新日: 2026-09-16 01:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Kiwi TCMS is an open source test management system. Prior to 16.1, TestCase.extra_link and TestPlan.extra_link accepted unsanitized user input and rendered stored values verbatim, creating an opportunity for cross-site scripting. Official Docker images and unmodified Kiwi TCMS middleware send a Content-Security-Policy...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/kiwitcms/Kiwi/commit/1c2ecc8485faeefd84a526314a0a60d132fbbc09
- https://github.com/kiwitcms/Kiwi/commit/d5d36e74cf9333cb37e3a8743b22b74dfa9a0139
- https://github.com/kiwitcms/Kiwi/releases/tag/v16.1
- https://github.com/kiwitcms/Kiwi/security/advisories/GHSA-473p-56xx-vg67

### [CVE-2026-87793](https://github.com/italia/design-scuole-wordpress-theme)

> **Frontend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-87793
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-16 01:17:37 JST
- 更新日: 2026-09-16 03:19:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: The "Design Scuole Italia" WordPress theme is affected by a Reflected XSS vulnerability in the filters-scheda-didattica.php file, allowing an unauthenticated attacker to execute arbitrary JavaScript in a victim's browser via a crafted URL containing a malicious archive parameter.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/italia/design-scuole-wordpress-theme
- https://www.acn.gov.it/portale/w/rilevate-vulnerabilita-nel-tema-wordpress-design-scuole-italia-

### [CVE-2026-12749](https://www.ibm.com/support/pages/node/7285931)

> **Frontend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-12749
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-16 03:17:14 JST
- 更新日: 2026-09-16 03:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Cloud Pak for Business Automation is vulnerable to stored cross-site scripting. This vulnerability allows an authenticated user to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials disclosure within a trusted session.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7285931

### [CVE-2026-12750](https://www.ibm.com/support/pages/node/7285931)

> **Frontend** / **MEDIUM** / CVSS: **6.4** / KEV: **no**

- タイトル: CVE-2026-12750
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-16 03:17:14 JST
- 更新日: 2026-09-16 03:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: IBM Cloud Pak for Business Automation is vulnerable to stored cross-site scripting. This vulnerability allows an authenticated user to embed arbitrary JavaScript code in the Web UI thus altering the intended functionality potentially leading to credentials disclosure within a trusted session.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://www.ibm.com/support/pages/node/7285931

### [CVE-2026-54503](https://github.com/plone/plone.app.textfield/commit/0da1aeec2406cf640977eb857a03e792d2c7cac2)

> **Frontend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-54503
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-16 02:17:21 JST
- 更新日: 2026-09-16 04:17:20 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: plone.app.textfield provides a zope.schema-style field type called RichText for storing a value with a related MIME type. Prior to 2.0.2, 3.0.2, and 4.0.1, depending on the release line, RichTextValue.output returns an unsanitized stored RichText value when mimeType equals outputMimeType, including values that claim th...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/plone/plone.app.textfield/commit/0da1aeec2406cf640977eb857a03e792d2c7cac2
- https://github.com/plone/plone.app.textfield/commit/467638e500d804c637031387a227a2b02d12a86f
- https://github.com/plone/plone.app.textfield/commit/781d517a38524087fe57525a94806684908f852f
- https://github.com/plone/plone.app.textfield/security/advisories/GHSA-4r4f-gg25-rmg5

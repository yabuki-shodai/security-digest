# Frontend CVE Summary (2026-08-11)

## Overview

- 取得日時: 2026-08-11 07:52:30 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 7
- Critical: 3
- High: 0
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-48158](https://github.com/dai-shi/use-context-selector/security/advisories/GHSA-7h6v-mwq6-jhm8)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-48158
- 関連キーワード: javascript, react, npm
- 影響製品: -
- 公開日: 2026-08-11 01:19:48 JST
- 更新日: 2026-08-11 01:19:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: use-context-selector is a React useContextSelector hook in userland Between 2026-05-18 15:57:18 and 2026-05-19 15:24:34, the default branch contained malicious commits 9d8481a513b7b0d1c0941b220c69b25de748641b through 6f2dae054ca014068bdbbb4db96006424d674124 that executed remote attacker-controlled code on developer mac...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dai-shi/use-context-selector/security/advisories/GHSA-7h6v-mwq6-jhm8

### [CVE-2026-48159](https://github.com/dai-shi/use-reducer-async/security/advisories/GHSA-2786-p4vj-vx8x)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-48159
- 関連キーワード: javascript, react, npm
- 影響製品: -
- 公開日: 2026-08-11 03:17:49 JST
- 更新日: 2026-08-11 03:17:49 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: use-reducer-async is a React useReducer with async actions. Between 2026-05-18 16:29:52 and 2026-05-19 15:26:07, the default branch contained malicious commits da72edbde5705efcec6c62e0a3dcb73687b78dc8 through df07d5711458d8b46e11dd7afaaa21e88cafabfb that executed remote attacker-controlled code on developer machines du...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dai-shi/use-reducer-async/security/advisories/GHSA-2786-p4vj-vx8x

### [CVE-2026-48160](https://github.com/dai-shi/react-tracked/security/advisories/GHSA-79c5-q7m9-9c6x)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-48160
- 関連キーワード: javascript, react, npm
- 影響製品: -
- 公開日: 2026-08-11 06:17:23 JST
- 更新日: 2026-08-11 06:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: react-tracked provides state usage tracking with Proxies. Between 2026-05-18 19:26:36 and 2026-05-19 15:22:45, the default branch contained malicious commits 6978272a7d6ca02225cb747ea69f427512e33699 through 949f1a3d6bb1ff7d1a0dec892afd773e742627e8 that executed remote attacker-controlled code on developer machines duri...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dai-shi/react-tracked/security/advisories/GHSA-79c5-q7m9-9c6x

### [CVE-2026-73035](https://github.com/raineorshine/npm-check-updates/commit/b554b84848fc0b08a9d2b3d3db15e351387168cf)

> **Frontend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-73035
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-08-11 06:17:26 JST
- 更新日: 2026-08-11 06:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: npm-check-updates through 23.0.2, fixed in commit b554b84, contains a terminal escape sequence injection vulnerability that allows an attacker to embed arbitrary terminal control characters in a dependency's package.json homepage or repository URL fields. When a developer runs ncu with the --format homepage or --format...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/raineorshine/npm-check-updates/commit/b554b84848fc0b08a9d2b3d3db15e351387168cf
- https://github.com/raineorshine/npm-check-updates/issues/1988
- https://github.com/raineorshine/npm-check-updates/pull/1994
- https://www.vulncheck.com/advisories/npm-check-updates-terminal-injection-via-unsanitized-escape-sequences

### [CVE-2026-69116](https://github.com/xpf0000/FlyEnv/commit/68fd6d7b200273ad0a8bce09424b8bd87134cfb6)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-69116
- 関連キーワード: vue, node.js
- 影響製品: -
- 公開日: 2026-08-11 05:17:32 JST
- 更新日: 2026-08-11 05:17:32 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: FlyEnv before 4.18.0 fails to sanitize HTML from markdown rendering and AI chat content passed to Vue v-html directives. Attackers can inject malicious scripts through markdown sources or chat messages that execute in the Electron renderer process with access to Node.js APIs and the filesystem.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/xpf0000/FlyEnv/commit/68fd6d7b200273ad0a8bce09424b8bd87134cfb6
- https://github.com/xpf0000/FlyEnv/issues/809
- https://github.com/xpf0000/FlyEnv/pull/810
- https://github.com/xpf0000/FlyEnv/releases/tag/v4.18.0
- https://www.vulncheck.com/advisories/flyenv-cross-site-scripting-via-v-html

### [CVE-2026-44401](https://github.com/typemill/typemill)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-44401
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-11 05:17:30 JST
- 更新日: 2026-08-11 05:17:30 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Typemill CMS version 2.x contains a persistent cross-site scripting vulnerability in the Markdown parser extension that allows authenticated users with theme-configuration access to inject malicious JavaScript URIs by supplying unsanitized href values in Markdown links. Attackers can craft Markdown links using the java...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/typemill/typemill
- https://github.com/typemill/typemill/releases/tag/2.23.0
- https://www.vulncheck.com/advisories/typemill-cms-2-x-persistent-xss-via-markdown-javascript-uri

### [CVE-2026-72743](https://github.com/dataease/SQLBot/commit/c3f40a5c05a53253b2924765b02b83f6a819948f)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-72743
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-11 06:17:24 JST
- 更新日: 2026-08-11 06:17:24 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: SQLBot through 1.10.0, fixed in commit c3f40a5, contains a stored cross-site scripting vulnerability in the SQText dashboard component that renders TinyMCE output via v-html without sanitization. Attackers who can modify dashboard text widget content can inject arbitrary HTML and JavaScript that executes for all users...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/dataease/SQLBot/commit/c3f40a5c05a53253b2924765b02b83f6a819948f
- https://github.com/dataease/SQLBot/issues/1308
- https://github.com/dataease/SQLBot/pull/1309
- https://www.vulncheck.com/advisories/sqlbot-sqtext-dashboard-component-stored-xss-via-v-html

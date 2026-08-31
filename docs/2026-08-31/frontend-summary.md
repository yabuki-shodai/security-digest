# Frontend CVE Summary (2026-08-31)

## Overview

- 取得日時: 2026-08-31 09:28:59 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 7
- Critical: 0
- High: 2
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-81636](https://cna.erlef.org/cves/CVE-2026-81636.html)

> **Frontend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-81636
- 関連キーワード: graphql, gin
- 影響製品: -
- 公開日: 2026-08-31 04:17:29 JST
- 更新日: 2026-08-31 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Allocation of Resources Without Limits or Throttling vulnerability in ash-project ash_graphql allows an unauthenticated client to bypass the configured GraphQL query-complexity limit and force an unbounded database read. AshGraphql.Graphql.Resolver.query_complexity/3 multiplies child complexity by the requested page si...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-81636.html
- https://github.com/ash-project/ash_graphql/commit/c3229f6a65cbabb32fd7ffcac881922d1b3b30ad
- https://github.com/ash-project/ash_graphql/security/advisories/GHSA-mwc4-r9fc-h6mg
- https://osv.dev/vulnerability/EEF-CVE-2026-81636

### [CVE-2026-80223](https://cna.erlef.org/cves/CVE-2026-80223.html)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-80223
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-08-31 04:17:29 JST
- 更新日: 2026-08-31 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Incorrect Authorization vulnerability in ash-project ash_graphql allows an authenticated subscriber in one tenant to receive another tenant's records over GraphQL subscriptions. The subscription resolver in AshGraphql.Graphql.Resolver authorizes each notification payload in memory: its fast path calls Ash.can/3 with ru...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-80223.html
- https://github.com/ash-project/ash_graphql/commit/6e30b8b5a04bdeaed5d7514caa6b2d056d8d993e
- https://github.com/ash-project/ash_graphql/security/advisories/GHSA-rcqc-59g2-gjg2
- https://osv.dev/vulnerability/EEF-CVE-2026-80223

### [CVE-2026-81633](https://cna.erlef.org/cves/CVE-2026-81633.html)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-81633
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-08-31 04:17:29 JST
- 更新日: 2026-08-31 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Improper Input Validation vulnerability in ash-project ash_graphql allows an unauthenticated client to crash a relay node(id: ...) query with an unhandled KeyError. AshGraphql.Graphql.Resolver.resolve_node/2 decodes the client-supplied global ID with decode_relay_id/1, which only base64-decodes the string and splits it...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-81633.html
- https://github.com/ash-project/ash_graphql/commit/c8863ed8e5c21f1bfb6125f1d24e78443dfc6351
- https://github.com/ash-project/ash_graphql/security/advisories/GHSA-mrgv-g7gf-r96h
- https://osv.dev/vulnerability/EEF-CVE-2026-81633

### [CVE-2026-82646](https://github.com/WWBN/AVideo/security/advisories/GHSA-xg77-76mf-rw8h)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-82646
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-08-31 00:16:45 JST
- 更新日: 2026-08-31 00:16:45 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WWBN AVideo contains an unauthenticated reflected cross-site scripting vulnerability in the url2Embed.json.php endpoint that allows attackers to inject malicious scripts by supplying URLs with HTML metacharacters. Attackers can mint an encrypted evideo payload containing unescaped markup, then deliver it as a legitimat...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/WWBN/AVideo/security/advisories/GHSA-xg77-76mf-rw8h
- https://www.vulncheck.com/advisories/wwbn-avideo-unauthenticated-reflected-xss-via-url2embed-json-php

### [CVE-2026-78693](https://cna.erlef.org/cves/CVE-2026-78693.html)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-78693
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-08-31 04:17:28 JST
- 更新日: 2026-08-31 04:17:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Generation of Error Message Containing Sensitive Information vulnerability in ash-project ash_graphql allows a remote client to read internal field names that an application configured its error_handler to redact. In AshGraphql.Errors, each error is passed to the configured error_handler and the returned map is merged...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-78693.html
- https://github.com/ash-project/ash_graphql/commit/78e90d369f09f44c534816de541e60841066a467
- https://github.com/ash-project/ash_graphql/security/advisories/GHSA-ppr2-g9h8-w7qp
- https://osv.dev/vulnerability/EEF-CVE-2026-78693

### [CVE-2026-81643](https://cna.erlef.org/cves/CVE-2026-81643.html)

> **Frontend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-81643
- 関連キーワード: graphql, go
- 影響製品: -
- 公開日: 2026-08-31 04:17:29 JST
- 更新日: 2026-08-31 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Incorrect Authorization vulnerability in ash-project ash_graphql delivers GraphQL subscription payloads for records a subscriber is not authorized to see. In AshGraphql.Subscription.Batcher, do_send/5 resolves the first notification of a batch and filters it with should_send?/1, which drops results whose errors are cod...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-81643.html
- https://github.com/ash-project/ash_graphql/commit/e8e67f39add2ce0771e6db5f086afe68ba212c57
- https://github.com/ash-project/ash_graphql/security/advisories/GHSA-j684-hch4-q888
- https://osv.dev/vulnerability/EEF-CVE-2026-81643

### [CVE-2026-82367](https://cna.erlef.org/cves/CVE-2026-82367.html)

> **Frontend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-82367
- 関連キーワード: graphql
- 影響製品: -
- 公開日: 2026-08-31 04:17:29 JST
- 更新日: 2026-08-31 04:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Exposure of Data Element to Wrong Session vulnerability in ash-project ash_graphql can deliver one subscription's resolved records to a different subscriber's topic. AshGraphql.Subscription.Batcher.do_send/5 reads the resolved batch from the process dictionary via Process.get(:batch_resolved) and then unconditionally d...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-82367.html
- https://github.com/ash-project/ash_graphql/commit/b798ef5288664a0261990b19765558f168b718fb
- https://github.com/ash-project/ash_graphql/security/advisories/GHSA-wm4m-cjmc-5v8c
- https://osv.dev/vulnerability/EEF-CVE-2026-82367

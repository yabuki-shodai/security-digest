# Frontend CVE Summary (2026-09-18)

## Overview

- 取得日時: 2026-09-18 09:10:12 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 0
- High: 6
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-90144](https://git.kernel.org/stable/c/33f016b23a219fe034213849b51436b8e79df251)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-90144
- 関連キーワード: react, go
- 影響製品: -
- 公開日: 2026-09-18 02:17:07 JST
- 更新日: 2026-09-18 02:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: In the Linux kernel, the following vulnerability has been resolved: dpll: fix NULL deref in dpll_device_ops() during teardown race When the last owner of a dpll device unregisters while a foreign driver still holds a pin on it via dpll_pin_on_pin_register(), the dpll object stays alive with an empty registration list....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://git.kernel.org/stable/c/33f016b23a219fe034213849b51436b8e79df251
- https://git.kernel.org/stable/c/fdbf04e3e01a872d0ef2149f846f1a3e3cb54f5b

### [CVE-2026-71538](https://github.com/CycloneDX/cyclonedx-node-npm/commit/15d3beb5bcd2b0b6eccfdf31192f5103b3f12c0f)

> **Frontend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-71538
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-09-18 00:16:51 JST
- 更新日: 2026-09-18 01:17:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: @cyclonedx/cyclonedx-npm creates CycloneDX Software Bill of Materials from npm projects. Prior to version 6.0.0, the Windows fallback path in src/npmRunner.ts, used when npm_execpath does not provide the npm CLI path, can construct a shell command containing an untrusted value from the --workspace option. When an attac...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/CycloneDX/cyclonedx-node-npm/commit/15d3beb5bcd2b0b6eccfdf31192f5103b3f12c0f
- https://github.com/CycloneDX/cyclonedx-node-npm/pull/1489
- https://github.com/CycloneDX/cyclonedx-node-npm/releases/tag/v6.0.0
- https://github.com/CycloneDX/cyclonedx-node-npm/security/advisories/GHSA-q69g-4hcv-6jg4

### [CVE-2026-63460](https://github.com/vendurehq/vendure/commit/f74cbbb0b9a50b5b0131822835fe7ee9b71b42c9)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-63460
- 関連キーワード: graphql, go, node.js, express, postgresql, mysql
- 影響製品: -
- 公開日: 2026-09-18 00:16:49 JST
- 更新日: 2026-09-18 06:16:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Vendure is an open-source headless commerce platform. Prior to 3.6.5, the public Shop GraphQL API allows an unauthenticated caller to supply a catastrophically backtracking pattern through StringOperators.regex. packages/core/src/service/helpers/list-query-builder/parse-filter-params.ts passes the raw pattern to the RE...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/vendurehq/vendure/commit/f74cbbb0b9a50b5b0131822835fe7ee9b71b42c9
- https://github.com/vendurehq/vendure/releases/tag/v3.6.5
- https://github.com/vendurehq/vendure/security/advisories/GHSA-jgm3-qmp2-c4p7
- https://github.com/vendurehq/vendure/security/advisories/GHSA-jgm3-qmp2-c4p7

### [CVE-2026-86038](https://github.com/libp2p/js-libp2p/commit/cec2b1f349d130065e561349a0336a239528267f)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-86038
- 関連キーワード: javascript, go, gin
- 影響製品: -
- 公開日: 2026-09-18 01:18:16 JST
- 更新日: 2026-09-18 03:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libp2p is a JavaScript implementation of the libp2p networking stack. From 15.0.0 until 16.0.5, @libp2p/gossipsub uses the default StrictSign policy in packages/gossipsub/src/utils/buildRawMessage.ts, where validateToRawMessage verifies a signature with attacker-controlled msg.key but skips binding that key to msg.from...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/libp2p/js-libp2p/commit/cec2b1f349d130065e561349a0336a239528267f
- https://github.com/libp2p/js-libp2p/pull/3569
- https://github.com/libp2p/js-libp2p/releases/tag/gossipsub-v16.0.5
- https://github.com/libp2p/js-libp2p/security/advisories/GHSA-c3gv-825q-fvmp
- https://github.com/libp2p/js-libp2p/security/advisories/GHSA-c3gv-825q-fvmp

### [CVE-2026-61793](https://github.com/nuxt-modules/og-image/commit/243cac2228671d3711c2bd65e300c278fcdf5a4e)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-61793
- 関連キーワード: vue, nuxt, gin, node.js
- 影響製品: -
- 公開日: 2026-09-18 00:16:48 JST
- 更新日: 2026-09-18 01:17:33 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nuxt OG Image generates OG Images with Vue templates in Nuxt. From 6.0.2 until 6.7.0, nuxt-og-image exposes the unauthenticated /_og/d/** route when the documented defaults security.strict = false and security.secret = "" are used, and base64url-decodes the fonts parameter through decodeOgImageParams. Attacker-controll...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nuxt-modules/og-image/commit/243cac2228671d3711c2bd65e300c278fcdf5a4e
- https://github.com/nuxt-modules/og-image/pull/637
- https://github.com/nuxt-modules/og-image/releases/tag/v6.7.0
- https://github.com/nuxt-modules/og-image/security/advisories/GHSA-q8hw-4fvp-9rwv
- https://github.com/nuxt-modules/og-image/security/advisories/GHSA-q8hw-4fvp-9rwv

### [CVE-2026-85715](https://github.com/mattiasw/ExifReader/commit/17b901cd192d2c90d7f9f347bd3073b28b482699)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-85715
- 関連キーワード: javascript, node.js
- 影響製品: -
- 公開日: 2026-09-18 01:18:15 JST
- 更新日: 2026-09-18 01:18:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ExifReader is a JavaScript Exif information parser. Prior to 4.41.1, ExifReader parses attacker-controlled HEIC or AVIF ISO-BMFF files in getItems() within src/image-header-iso-bmff-iloc.js and trusts iloc itemCount and extentCount values while allocating an extent object for every nested-loop iteration. When offsetSiz...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/mattiasw/ExifReader/commit/17b901cd192d2c90d7f9f347bd3073b28b482699
- https://github.com/mattiasw/ExifReader/releases/tag/v4.41.1
- https://github.com/mattiasw/ExifReader/security/advisories/GHSA-pj96-35fp-cfcc
- https://github.com/mattiasw/ExifReader/security/advisories/GHSA-pj96-35fp-cfcc

### [CVE-2026-86039](https://github.com/libp2p/js-libp2p/commit/3bf5d395cbca1488eea6e87cd771e4613b661c30)

> **Frontend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-86039
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-09-18 01:18:17 JST
- 更新日: 2026-09-18 01:18:17 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libp2p is a JavaScript implementation of the libp2p networking stack. From 8.0.0 until 12.0.24, @libp2p/peer-store in packages/peer-store/src/index.ts uses consumePeerRecord to verify a RecordEnvelope signature but does not require PeerRecord.peerId in the signed payload to equal the signer peer ID derived by RecordEnv...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/libp2p/js-libp2p/commit/3bf5d395cbca1488eea6e87cd771e4613b661c30
- https://github.com/libp2p/js-libp2p/pull/3570
- https://github.com/libp2p/js-libp2p/releases/tag/peer-store-v12.0.24
- https://github.com/libp2p/js-libp2p/security/advisories/GHSA-vrf4-mx87-p53w

### [CVE-2026-86040](https://github.com/libp2p/js-libp2p/commit/fb9e8a76e9ac75924928fae4ce11d00f68320a83)

> **Frontend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-86040
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-09-18 01:18:17 JST
- 更新日: 2026-09-18 05:18:49 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: libp2p is a JavaScript implementation of the libp2p networking stack. Prior to 11.0.26, @libp2p/floodsub accepts unauthenticated RPC frames on /floodsub/1.0.0 through PeerStreams.attachInboundStream in packages/floodsub/src/peer-streams.ts without protobuf element limits, then processRpc and processRpcSubOpt in package...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/libp2p/js-libp2p/commit/fb9e8a76e9ac75924928fae4ce11d00f68320a83
- https://github.com/libp2p/js-libp2p/pull/3568
- https://github.com/libp2p/js-libp2p/releases/tag/floodsub-v11.0.26
- https://github.com/libp2p/js-libp2p/security/advisories/GHSA-cvfg-hcf3-ggwv

# Backend CVE Summary (2026-08-22)

## Overview

- 取得日時: 2026-08-22 07:36:29 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 12
- Critical: 2
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-48755](https://github.com/lxc/incus/security/advisories/GHSA-v6mj-8pf4-hhw4)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-48755
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-22 00:16:41 JST
- 更新日: 2026-08-22 07:16:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Incus is a system container and virtual machine manager. Prior to version 7.1.0, improper validation of user-provided backup compression algorithm leads to argument injection in the constructed command line. This leads to an arbitrary file write on the host, possibly leading to arbitrary command execution. Version 7.1....
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/lxc/incus/security/advisories/GHSA-v6mj-8pf4-hhw4

### [CVE-2026-62283](https://github.com/nezhahq/nezha/commit/6661d6a7fc1c269f55c7f4e775082ad23fbe0f54)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-62283
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-22 06:17:01 JST
- 更新日: 2026-08-22 07:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nezha Monitoring is a self-hostable, lightweight, servers and websites monitoring and O&M tool. Nezha versions 1.14.13 through 1.14.14 and 2.0.0 through 2.0.9 do not bind stream identifiers created by CreateStream in service/rpc/io_stream.go to their creating user, and `GET /ws/terminal/:id` and `GET /ws/file/:id` only...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/nezhahq/nezha/commit/6661d6a7fc1c269f55c7f4e775082ad23fbe0f54
- https://github.com/nezhahq/nezha/releases/tag/v2.0.10
- https://github.com/nezhahq/nezha/security/advisories/GHSA-q6xx-5vr8-p898

### [CVE-2026-64679](https://github.com/runatlantis/atlantis/commit/ea4e4ceebf8b387d015fff7ed8a7fcca33279afe)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-64679
- 関連キーワード: go, golang, terraform
- 影響製品: -
- 公開日: 2026-08-22 06:17:01 JST
- 更新日: 2026-08-22 06:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Atlantis is a self-hosted golang application that listens for Terraform pull request events via webhooks. From 0.19.8 until 0.45.0, Atlantis does not consistently validate user-controlled workspace values supplied through accepted repository-level atlantis.yaml configuration or authenticated /api/plan input before join...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/runatlantis/atlantis/commit/ea4e4ceebf8b387d015fff7ed8a7fcca33279afe
- https://github.com/runatlantis/atlantis/pull/6254
- https://github.com/runatlantis/atlantis/releases/tag/v0.45.0
- https://github.com/runatlantis/atlantis/security/advisories/GHSA-26w5-6g95-gj28

### [CVE-2026-53530](https://github.com/erweixin/RaTeX/security/advisories/GHSA-4hgp-59h5-gvrj)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-53530
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-22 07:16:39 JST
- 更新日: 2026-08-22 07:16:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RaTeX is a KaTeX-compatible math rendering engine written in Rust. Prior to version 0.1.11, the public parser entrypoint `ratex_parser::parse(&str)` panics on the 9-byte input `\verbéxé` (i.e. `\verb` followed by the non-ASCII delimiter `é`). When handling a `\verb` command, the parser slices the verbatim argument with...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/erweixin/RaTeX/security/advisories/GHSA-4hgp-59h5-gvrj

### [CVE-2026-45099](https://github.com/gruntwork-io/terragrunt/commit/3d6f10d6bccc851c6506a307a0b8675e0346e65e)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-45099
- 関連キーワード: go, terraform
- 影響製品: -
- 公開日: 2026-08-22 06:16:59 JST
- 更新日: 2026-08-22 06:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Terragrunt is a flexible orchestration tool that allows Infrastructure as Code written in OpenTofu or Terraform to scale. Prior to 1.0.4, Terragrunt trusts paths decoded from a downloaded module's .terragrunt-module-manifest during fileManifest.Clean() in internal/util/file.go. A malicious or compromised external modul...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/gruntwork-io/terragrunt/commit/3d6f10d6bccc851c6506a307a0b8675e0346e65e
- https://github.com/gruntwork-io/terragrunt/pull/6032
- https://github.com/gruntwork-io/terragrunt/releases/tag/v1.0.4
- https://github.com/gruntwork-io/terragrunt/security/advisories/GHSA-8394-6f8r-whxg

### [CVE-2026-55185](https://github.com/miniflux/v2/commit/c896bafdaa19c3f280b02b1059f84706495f1949)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-55185
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-22 06:17:00 JST
- 更新日: 2026-08-22 06:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Miniflux 2 is an open source feed reader. Prior to 2.3.1, IsRelativePath in internal/urllib/url.go accepts redirect targets containing backslashes because Go URL parsing treats them as path characters. Browser backslash normalization converts them to forward slashes. An unauthenticated attacker can provide such a redir...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/miniflux/v2/commit/c896bafdaa19c3f280b02b1059f84706495f1949
- https://github.com/miniflux/v2/pull/4362
- https://github.com/miniflux/v2/releases/tag/2.3.1
- https://github.com/miniflux/v2/security/advisories/GHSA-m999-j542-5w3r

### [CVE-2026-53572](https://github.com/kedacore/keda/commit/703de9dec86cb25b6ecfa4948880a90487344d3f)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-53572
- 関連キーワード: go, postgresql, kubernetes
- 影響製品: -
- 公開日: 2026-08-22 06:16:59 JST
- 更新日: 2026-08-22 06:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KEDA is a Kubernetes-based Event Driven Autoscaling component. Prior to 2.20.0, pkg/scalers/postgresql_scaler.go constructs libpq-style connection strings from tenant-controlled host, port, userName, dbName, sslmode, and password values, while escapePostgreConnectionParameter() only quotes values containing a literal s...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/kedacore/keda/commit/703de9dec86cb25b6ecfa4948880a90487344d3f
- https://github.com/kedacore/keda/issues/7784
- https://github.com/kedacore/keda/pull/7787
- https://github.com/kedacore/keda/releases/tag/v2.20.0
- https://github.com/kedacore/keda/security/advisories/GHSA-6w3m-4hhp-775q

### [CVE-2026-71494](https://github.com/infracost/infracost/commit/3d24c757f5e4e60c7259f1b89ad7ceaabcfca86f)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-71494
- 関連キーワード: go, gin, terraform
- 影響製品: -
- 公開日: 2026-08-22 03:16:50 JST
- 更新日: 2026-08-22 05:16:40 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Infracost provides cloud cost intelligence for engineers, AI coding agents, and CI/CD. Prior to 0.10.45, internal/hcl/remote_variables_loader.go and related Terraform Cloud, remote-plan, and Terragrunt registry request paths can attach a configured Terraform Cloud or registry token to a destination hostname derived fro...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/infracost/infracost/commit/3d24c757f5e4e60c7259f1b89ad7ceaabcfca86f
- https://github.com/infracost/infracost/pull/3590
- https://github.com/infracost/infracost/releases/tag/v0.10.45
- https://github.com/infracost/infracost/security/advisories/GHSA-6x6c-w9w9-hv4h

### [CVE-2026-76905](https://github.com/getkin/kin-openapi/commit/1d0a337c9b1570fab283be8a04c8af6e43b9a22c)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-76905
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-22 06:17:06 JST
- 更新日: 2026-08-22 06:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kin-openapi is a Go project for handling OpenAPI files. From 0.10.0 until 0.141.0, openapi3filter.convertParseError in openapi3filter/validation_error_encoder.go dereferences e.Parameter.In without checking whether e.Parameter is nil. A malformed non-string scalar field in a multipart/form-data request body produces a...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/getkin/kin-openapi/commit/1d0a337c9b1570fab283be8a04c8af6e43b9a22c
- https://github.com/getkin/kin-openapi/releases/tag/v0.141.0
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-mmfr-pmjx-hw9w

### [CVE-2026-77354](https://github.com/getkin/kin-openapi/commit/1223a0f215d2cf9beb2d9eb9ea2649d001c21388)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-77354
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-08-22 06:17:07 JST
- 更新日: 2026-08-22 06:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: kin-openapi is a Go project for handling OpenAPI files. From 0.124.0 until 0.142.0, openapi3filter.sliceMapToSlice in openapi3filter/req_resp_decoder.go converts attacker-controlled sparse indexes from a deepObject query parameter into a dense slice by allocating entries from zero through the largest supplied index, af...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/getkin/kin-openapi/commit/1223a0f215d2cf9beb2d9eb9ea2649d001c21388
- https://github.com/getkin/kin-openapi/pull/923
- https://github.com/getkin/kin-openapi/releases/tag/v0.142.0
- https://github.com/getkin/kin-openapi/security/advisories/GHSA-xhj3-7xw9-vr34

### [CVE-2026-44517](https://github.com/podman-container-tools/buildah/commit/54459cf8a0feb4b1da766e4a6360451834e1846c)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-44517
- 関連キーワード: go, docker
- 影響製品: -
- 公開日: 2026-08-22 06:16:59 JST
- 更新日: 2026-08-22 06:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Buildah is a tool that facilitates building OCI images. From 1.38.1 until 1.43.2 and 1.44.0, TempDirForURL in define/types.go does not securely confine Git repository subdirectories to the downloaded build context, and downloadToDirectory and stdinToDirectory can follow a Dockerfile symlink left by a partially extracte...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/podman-container-tools/buildah/commit/54459cf8a0feb4b1da766e4a6360451834e1846c
- https://github.com/podman-container-tools/buildah/commit/fc2003bb2efeb3ed7d5c7e1e88d04e78f370a944
- https://github.com/podman-container-tools/buildah/releases/tag/v1.43.2
- https://github.com/podman-container-tools/buildah/releases/tag/v1.44.0
- https://github.com/podman-container-tools/buildah/security/advisories/GHSA-49p4-px3h-rq49

### [CVE-2026-53531](https://github.com/erweixin/RaTeX/security/advisories/GHSA-4w5h-hx6r-28q7)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-53531
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-08-22 07:16:39 JST
- 更新日: 2026-08-22 07:16:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RaTeX is a KaTeX-compatible math rendering engine written in Rust. Prior to version 0.1.11, RaTeX’s recursive-descent parser recurses one (or more) native stack frame per nesting level at `{`, `\left`, `\sqrt{`, `^{`, etc, with no maximum depth limit. A short, ~10 KB input of nested groups overflows the 8 MB main-threa...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/erweixin/RaTeX/security/advisories/GHSA-4w5h-hx6r-28q7

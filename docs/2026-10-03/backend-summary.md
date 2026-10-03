# Backend CVE Summary (2026-10-03)

## Overview

- 取得日時: 2026-10-03 10:07:04 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 8
- Critical: 1
- High: 3
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-103628](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html)

> **Backend** / **CRITICAL** / CVSS: **9.6** / KEV: **no**

- タイトル: CVE-2026-103628
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-03 01:16:43 JST
- 更新日: 2026-10-03 06:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Out of bounds write in WebGL in Google Chrome prior to 154.0.8037.97 allowed a remote attacker to execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: Critical)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html
- https://issues.chromium.org/issues/549995090

### [CVE-2014-125130](https://github.com/projectdiscovery/nuclei-templates/blob/main/http/vulnerabilities/wordpress/wp-googlemp3-lfi.yaml)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2014-125130
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-03 04:16:37 JST
- 更新日: 2026-10-03 04:16:37 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CodeArt Google MP3 Audio Player plugin (google-mp3-audio-player) for WordPress through 1.0.11 contains an unauthenticated arbitrary file read vulnerability that allows remote attackers to retrieve sensitive files by supplying a path-traversal payload in the file parameter of direct_download.php. Attackers can request p...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/projectdiscovery/nuclei-templates/blob/main/http/vulnerabilities/wordpress/wp-googlemp3-lfi.yaml
- https://patchstack.com/database/wordpress/plugin/google-mp3-audio-player/vulnerability/wordpress-codeart-google-mp3-player-plugin-file-disclosure-download
- https://www.exploit-db.com/exploits/35460
- https://www.vulncheck.com/advisories/codeart-google-mp3-audio-player-arbitrary-file-read-via-direct-download-php

### [CVE-2026-103622](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-103622
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-03 01:16:43 JST
- 更新日: 2026-10-03 06:16:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Use after free in SVG in Google Chrome prior to 154.0.8037.97 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html
- https://issues.chromium.org/issues/565742179

### [CVE-2026-103625](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-103625
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-03 01:16:43 JST
- 更新日: 2026-10-03 06:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Type confusion in V8 in Google Chrome prior to 154.0.8037.97 allowed a remote attacker to execute arbitrary code inside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html
- https://issues.chromium.org/issues/559893859

### [CVE-2026-103621](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-103621
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-03 01:16:43 JST
- 更新日: 2026-10-03 02:47:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Integer overflow in Compositing in Google Chrome prior to 154.0.8037.97 allowed a remote attacker to leak cross-origin data via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html
- https://issues.chromium.org/issues/556268833

### [CVE-2026-103626](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-103626
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-03 01:16:43 JST
- 更新日: 2026-10-03 02:47:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Incorrect authorization in FileSystem in Google Chrome on on Windows prior to 154.0.8037.97 allowed a remote attacker leveraging social engineering to potentially execute arbitrary code outside the sandbox via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html
- https://issues.chromium.org/issues/553114097

### [CVE-2026-103629](https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-103629
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-03 01:16:44 JST
- 更新日: 2026-10-03 02:47:56 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Integer overflow in Skia in Google Chrome prior to 154.0.8037.97 allowed a remote attacker to leak cross-origin data via a crafted HTML page. (Chromium security severity: High)
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://chromereleases.googleblog.com/2026/10/stable-channel-update-for-desktop.html
- https://issues.chromium.org/issues/562038679

### [CVE-2026-39600](https://patchstack.com/database/wordpress/plugin/aculect-ai-companion/vulnerability/wordpress-aculect-ai-companion-plugin-0-8-1-unvalidated-redirects-and-forwards-vulnerability?_s_id=cve)

> **Backend** / **MEDIUM** / CVSS: **4.7** / KEV: **no**

- タイトル: CVE-2026-39600
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-03 00:17:09 JST
- 更新日: 2026-10-03 02:52:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: URL Redirection to Untrusted Site ('Open Redirect') vulnerability in Mehul Gohil Aculect AI Companion aculect-ai-companion allows Phishing.This issue affects Aculect AI Companion: from n/a through 0.8.1.
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://patchstack.com/database/wordpress/plugin/aculect-ai-companion/vulnerability/wordpress-aculect-ai-companion-plugin-0-8-1-unvalidated-redirects-and-forwards-vulnerability?_s_id=cve

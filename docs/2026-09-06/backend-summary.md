# Backend CVE Summary (2026-09-06)

## Overview

- 取得日時: 2026-09-06 08:49:40 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 2
- Critical: 1
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-86060](https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-86060
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-06 05:17:18 JST
- 更新日: 2026-09-06 06:16:51 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: RouterOSのSSHログイン処理における特定文字から始まるユーザー名の引数処理の不備。
- 影響: 未認証のSSHセッションからポリシーマスクが改変され、権限昇格が行われる可能性があります。
- 推奨対応: 6.49.21 (Long-term)、7.23.4 (Long-term)、7.24.2 (Stable) 以降の修正済みバージョンへ更新してください。

#### References
- https://cert.pl/en/posts/2026/09/mikrotik-routeros-cve
- https://cert.pl/en/posts/2026/09/vulnerabilities-in-mikrotik-routeros-actively-exploited/
- https://forum.mikrotik.com/t/6-49-21-long-term-is-released/272802
- https://forum.mikrotik.com/t/7-23-4-long-term-is-released/272801
- https://forum.mikrotik.com/t/7-24-2-stable-is-released/272800

### [CVE-2026-82752](https://cna.erlef.org/cves/CVE-2026-82752.html)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-82752
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-09-06 03:17:29 JST
- 更新日: 2026-09-06 03:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Ashにおける入力文字列長検証の不備。結合文字を含むUnicode文字数を測定単位とすることに起因します。
- 影響: 制限を超えるサイズのデータが保存され、リソース枯渇やストレージ圧迫を引き起こす可能性があります。
- 推奨対応: ライブラリのアップデートやデータ層での独立したサイズ制限の設定を検討してください。

#### References
- https://cna.erlef.org/cves/CVE-2026-82752.html
- https://github.com/ash-project/ash/commit/a64cab49b8886503e6b7c7b211d83c475aac48ca
- https://github.com/ash-project/ash/commit/cdbf4c4da6bda5f6f139078f01a64320b595216d
- https://github.com/ash-project/ash/security/advisories/GHSA-cwjv-574p-59f6
- https://osv.dev/vulnerability/EEF-CVE-2026-82752

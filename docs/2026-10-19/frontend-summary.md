# Frontend CVE Summary (2026-10-19)

## Overview

- 取得日時: 2026-10-19 09:10:07 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-98546](https://git.kernel.org/stable/c/071f51188a5d8ec10535541255587976d12fc7d8)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98546
- 関連キーワード: npm
- 影響製品: -
- 公開日: 2026-10-19 01:17:06 JST
- 更新日: 2026-10-19 01:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのarm64/bootにおいて、EL2でのPMZR_EL0書き込みトラップ設定が不適切であり、ユーザー空間からの書き込み時にシステムが意図せず停止する問題。
- 影響: パニックメッセージを出力せずにホストシステムがクラッシュまたは停止する（DoS）可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/071f51188a5d8ec10535541255587976d12fc7d8
- https://git.kernel.org/stable/c/2bc6b218717b9d08f466f88209251d54bc09b207
- https://git.kernel.org/stable/c/bb8c90c86441c090e9036f019cf1b4d7894a2c40
- https://git.kernel.org/stable/c/ce71865bf43f88bed9d9218e9218e537150be506

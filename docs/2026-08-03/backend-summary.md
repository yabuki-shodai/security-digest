# Backend CVE Summary (2026-08-03)

## Overview

- 取得日時: 2026-08-03 08:06:11 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 1
- Critical: 0
- High: 1
- KEV掲載: 0
- 日本語AI要約: fallback

## CVEs

### [CVE-2026-9856](https://github.com/huggingface/transformers/commit/eaaaf8494dd5386634ae37d1d122212fdc315be5)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-9856
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-08-03 01:16:25 JST
- 更新日: 2026-08-03 01:16:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: A vulnerability in huggingface/transformers versions <=5.8.0.dev0 allows an attacker to perform arbitrary file writes via path traversal. The issue resides in the `save_pretrained()` methods of `PreTrainedTokenizerBase` and `ProcessorMixin`, where keys from the `chat_template` dictionary are used directly as filenames...
- 影響: 影響範囲はNVD/CISAの原文と参照先で確認してください。
- 推奨対応: 利用有無を確認し、ベンダー修正・回避策・検知ログ確認を優先してください。

#### References
- https://github.com/huggingface/transformers/commit/eaaaf8494dd5386634ae37d1d122212fdc315be5
- https://huntr.com/bounties/362824d5-fe18-40e8-a6cf-62277f97a170

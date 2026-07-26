# Frontend CVE Summary (2026-07-27)

## Overview

- 取得日時: 2026-07-27 08:08:39 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 2
- Critical: 0
- High: 2
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-17497](https://github.com/codexu/note-gen)

> **Frontend** / **HIGH** / CVSS: **8.3** / KEV: **no**

- タイトル: CVE-2026-17497
- 関連キーワード: javascript, python, gin
- 影響製品: -
- 公開日: 2026-07-27 00:16:27 JST
- 更新日: 2026-07-27 00:16:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: NoteGen 0.32.0未満で、Tauriシェルプラグインの実行権限が不適切に付与され、任意のOSコマンドが実行可能。
- 影響: 悪意あるJavaScriptにより、ユーザーのマシンでリモートコード実行が可能になる恐れ。
- 推奨対応: NoteGenを0.32.0以降にアップデートし、プラグインの権限設定を見直すこと。

#### References
- https://github.com/codexu/note-gen
- https://github.com/codexu/note-gen/commit/00064a4a8ec4177d51094ffb3e15bf0758009c1f
- https://github.com/codexu/note-gen/releases/tag/note-gen-v0.32.0

### [CVE-2026-17496](https://github.com/codexu/note-gen)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-17496
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-27 00:16:27 JST
- 更新日: 2026-07-27 00:16:27 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: NoteGen 0.32.0未満で、AIチャット応答のHTMLサニタイズが不十分で、クロスサイトスクリプティングが発生する可能性。
- 影響: 悪意あるマークアップが実行され、アプリケーションコンテキストで任意のスクリプトが動作する恐れ。
- 推奨対応: NoteGenを0.32.0以降に更新し、HTMLサニタイズとCSP設定を適切に行うこと。

#### References
- https://github.com/codexu/note-gen
- https://github.com/codexu/note-gen/commit/ae3ba948c41d8a74b4a20f4c6f26fcdda2002298
- https://github.com/codexu/note-gen/releases/tag/note-gen-v0.32.0

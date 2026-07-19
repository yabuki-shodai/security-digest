# Frontend CVE Summary (2026-07-20)

## Overview

- 取得日時: 2026-07-20 08:05:33 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 3
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-63838](https://git.kernel.org/stable/c/134c61925e9e9ee0f4fdbab5c3984d5bb024f5f5)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63838
- 関連キーワード: nuxt
- 影響製品: -
- 公開日: 2026-07-20 00:16:50 JST
- 更新日: 2026-07-20 00:16:50 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのASoC rsndコンポーネントで、配列component_daisの境界チェック不備により、範囲外アクセスの可能性が修正されました。  
- 影響: 不適切な境界チェックにより、メモリの範囲外アクセスが発生する可能性がありますが、具体的な影響範囲は不明です。  
- 推奨対応: 最新のLinuxカーネルにアップデートし、該当の修正を適用することを推奨します。

#### References
- https://git.kernel.org/stable/c/134c61925e9e9ee0f4fdbab5c3984d5bb024f5f5
- https://git.kernel.org/stable/c/15e7b2ac2455995a6af02b9d3da7a432837aaf72
- https://git.kernel.org/stable/c/9f1daac27ca28e98c8c0e4450de42bb68d547250
- https://git.kernel.org/stable/c/a62b3e6e42359a79158c134e3cf5c74fe160c3f5
- https://git.kernel.org/stable/c/f9e437cddf6cf9e603bdaefe148c1f4792aaf39c

### [CVE-2026-63902](https://git.kernel.org/stable/c/44f9bab8df7750a1e2a4d6cc22d7c9c2dc096aed)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63902
- 関連キーワード: cypress
- 影響製品: -
- 公開日: 2026-07-20 01:17:07 JST
- 更新日: 2026-07-20 01:17:07 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのUSBシリアルドライバcypress_m8で、割り込みパケットヘッダーの検証不足によりバッファオーバーリードが発生する可能性があり修正された。  
- 影響: 不正な短い割り込みパケットにより境界外読み取りが起こる恐れがあるが、既存のリトライ処理で緩和されている可能性がある。  
- 推奨対応: 最新のLinuxカーネルにアップデートし、cypress_m8ドライバの修正を適用することを推奨する。

#### References
- https://git.kernel.org/stable/c/44f9bab8df7750a1e2a4d6cc22d7c9c2dc096aed
- https://git.kernel.org/stable/c/4a4cb0021ebe1fcadb52e04d19ed8d71470a530b
- https://git.kernel.org/stable/c/90664556916de22467097d4c8ceb716d597a5c32
- https://git.kernel.org/stable/c/9f9bfc80c67f35a275820da7e83a35dface08281
- https://git.kernel.org/stable/c/aaa66708bfb1dca2acd219d1c1582f9f6d5492cb

### [CVE-2026-63956](https://git.kernel.org/stable/c/1ef25704bd3b625fd151c09feee459479f71ee64)

> **Frontend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-63956
- 関連キーワード: cypress
- 影響製品: -
- 公開日: 2026-07-20 01:17:14 JST
- 更新日: 2026-07-20 01:17:14 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: LinuxカーネルのUSBシリアルドライバcypress_m8において、小さいエンドポイントサイズによるメモリ破損の脆弱性が修正されました。  
- 影響: 悪意のあるUSBデバイスが小さいパケットサイズを報告すると、メモリ破損やNULLポインタ参照が発生する可能性があります。  
- 推奨対応: Linuxカーネルを最新の安定版にアップデートし、修正パッチを適用してください。

#### References
- https://git.kernel.org/stable/c/1ef25704bd3b625fd151c09feee459479f71ee64
- https://git.kernel.org/stable/c/284105c40fc31fff90cdab8a0377aaeb92f87f0e
- https://git.kernel.org/stable/c/4bcaa59f403dbde6328604a500d65ee8d40975d9
- https://git.kernel.org/stable/c/4fcb22218f0a7229b7ce3b3952fb644def293fa5
- https://git.kernel.org/stable/c/52e18ae0c47c5c89e18fcd8022f287f7cc8802ec

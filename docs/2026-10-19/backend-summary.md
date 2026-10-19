# Backend CVE Summary (2026-10-19)

## Overview

- 取得日時: 2026-10-19 09:10:07 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 29
- Critical: 0
- High: 0
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-98433](https://git.kernel.org/stable/c/0a416ee20bcccddf91ca5b63696a23b9d11d73aa)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98433
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 00:16:53 JST
- 更新日: 2026-10-19 00:16:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのKVM PPC (Book3S HV)において、uv_page_in()失敗時にセキュアデバイスページの解放処理が行われない不具合。
- 影響: セキュアメモリ領域の永久的なリークが発生し、VM稼働中に利用可能なメモリリソースが枯渇する可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/0a416ee20bcccddf91ca5b63696a23b9d11d73aa
- https://git.kernel.org/stable/c/8f3b7746874b39fc20e0363c9076c7787d4765ba
- https://git.kernel.org/stable/c/a933d7024359e2e566b07903d1294b84f90482ae
- https://git.kernel.org/stable/c/c41088b2765af1e97e7bb05f906ae1823eca0388
- https://git.kernel.org/stable/c/dfb84274932737e338ff5eb27f34b4c8ecb01b50

### [CVE-2026-98455](https://git.kernel.org/stable/c/005b23d9e324fe5d0acbcfa70c625f2e81189046)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98455
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:16:55 JST
- 更新日: 2026-10-19 01:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのBluetooth RFCOMM実装において、接続切断時のセッション処理の不整合によりRFCOMM_CONNINFOハンドラでNULLポインタ参照が発生する問題。
- 影響: カーネルパニックを引き起こし、システムがクラッシュする可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/005b23d9e324fe5d0acbcfa70c625f2e81189046
- https://git.kernel.org/stable/c/1c4f7e1177da2f229be04139c27e5370a1cfba52
- https://git.kernel.org/stable/c/46f8ffd0a1f1eb6cbc94946a92c11ef601e228a1
- https://git.kernel.org/stable/c/4bf5ca47203049ce3648f750a53dcdc98bcc9e3e
- https://git.kernel.org/stable/c/84ae3cfd7d3a63591a2eb4faa24faf678c6708aa

### [CVE-2026-98473](https://git.kernel.org/stable/c/3c3433657c82f200dae36c29e2b80681c81b85be)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98473
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:16:57 JST
- 更新日: 2026-10-19 01:16:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのs390 vfio-apにおいて、ホスト設定からAPキューが削除された際の応答コード未処理等により、KVM割り込みリソースやページが適切に解放されない問題。
- 影響: リソース漏洩やメモリリークが発生し、システムの正常な動作を妨げる可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/3c3433657c82f200dae36c29e2b80681c81b85be
- https://git.kernel.org/stable/c/65e05ec252a9b79e75930d3c4dd42d8877db04c5
- https://git.kernel.org/stable/c/cf441a0db681dfad5e89b015d6be11365159d7a9
- https://git.kernel.org/stable/c/da69d3ac53490724eba0ade9deb4e539a6ae9034

### [CVE-2026-98594](https://git.kernel.org/stable/c/0844402326d4e48a28688f93ec6442e93bb442fa)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98594
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:12 JST
- 更新日: 2026-10-19 01:17:12 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのtg3ネットワークドライバにおいて、プローブ失敗時にPHYLIBリソース（MDIOバスやPHY）が解放されずに残る問題。
- 影響: ドライバ初期化失敗時に不必要なリソースリークが発生する可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/0844402326d4e48a28688f93ec6442e93bb442fa
- https://git.kernel.org/stable/c/6515c41503eef849abd2c7364f34e4bb25110f90
- https://git.kernel.org/stable/c/a449eedb3b1eb5b8b1f5ed116a1bfe85eaaf81df
- https://git.kernel.org/stable/c/a92e1a412c53dc0d9ad639e7abf8b3fc70a5b6ad
- https://git.kernel.org/stable/c/b6c0c757c65893ad7bb17e8bcf33cdd8257d7b3d

### [CVE-2026-98441](https://git.kernel.org/stable/c/2b783c562c3238ff50c34fd7a72a735c9cc73d9a)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98441
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-19 01:16:54 JST
- 更新日: 2026-10-19 01:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのパケットスケジューラ(act_ct)において、未確定のctエントリを持つskbがクローンされた際に、リストポインタの破損に伴うUse-After-Free(UAF)が発生する問題。
- 影響: メモリ破壊やシステムのクラッシュ、場合によっては不正なコード実行や特権昇格につながる可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/2b783c562c3238ff50c34fd7a72a735c9cc73d9a
- https://git.kernel.org/stable/c/4a04ed91575819fb1859311113e95700b709bec7
- https://git.kernel.org/stable/c/b097d9d7a5b09c8ec5c4c1a08e35ac5a66b06b44
- https://git.kernel.org/stable/c/f85009dfcd65e5969526b0db7a49b5413746e630

### [CVE-2026-98480](https://git.kernel.org/stable/c/6ef70d790425e76b42c69e416ee78c62bdc37d00)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98480
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-19 01:16:58 JST
- 更新日: 2026-10-19 01:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのNFC trf7970aドライバにおいて、スタートアップ時のRXゲイン設定エラー発生時に電源オフ（パワーダウン）処理が行われない不具合。
- 影響: 電源制御状態の不整合が発生し、余分な電力消費や動作不安定を招く可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/6ef70d790425e76b42c69e416ee78c62bdc37d00
- https://git.kernel.org/stable/c/cc444e4ad43461374dd128573eccb8979d2adb4c
- https://git.kernel.org/stable/c/d2acbde7e67df44efa8f0963462d1192e7694ffc

### [CVE-2026-98548](https://git.kernel.org/stable/c/1cd246b214dc9acf4e2f11d58c035e1e672fe7d2)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98548
- 関連キーワード: go, echo
- 影響製品: -
- 公開日: 2026-10-19 01:17:06 JST
- 更新日: 2026-10-19 01:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのSCTP実装において、エラーチャンクとデータチャンクが同一パケットに含まれる場合のトランスポート参照処理の不備により、解放済みトランスポートを再参照する問題。
- 影響: メモリ空間の不正アクセスやシステムクラッシュを引き起こす可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/1cd246b214dc9acf4e2f11d58c035e1e672fe7d2
- https://git.kernel.org/stable/c/4498467a8af06cfa3d71cb04bd7c4170dec8f449
- https://git.kernel.org/stable/c/6df536c5acbc0abd6f119d02e24f4a2ed97707f4
- https://git.kernel.org/stable/c/854c053c71459f8db7ef07db9cfa4eec5f5206f2
- https://git.kernel.org/stable/c/965e21ea16acb394d5e5801998ca9b0adc669665

### [CVE-2026-98584](https://git.kernel.org/stable/c/0b160417826d22f24fc31a5b9cfae3b14aa70f76)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98584
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-19 01:17:10 JST
- 更新日: 2026-10-19 01:17:10 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのem_textモジュールにおいて、em_text_dump()内で初期化されていないスタック上の構造体データがそのままnetlink応答にコピーされる不具合。
- 影響: カーネルスタックの未初期化領域（内部情報）が漏洩する可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/0b160417826d22f24fc31a5b9cfae3b14aa70f76
- https://git.kernel.org/stable/c/9923e1c537f91f3530b52d4efce85f3d9c131bf8
- https://git.kernel.org/stable/c/9c572a83037a7dcd653ba3a9cc468c16b857d0c9

### [CVE-2026-98592](https://git.kernel.org/stable/c/2d14720beb58870b15a52b236c3ab0be0e06e915)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98592
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-10-19 01:17:11 JST
- 更新日: 2026-10-19 01:17:11 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのspacemitイーサネットドライバにおいて、パケットフラグメントのマップ失敗時にTX記述子がクリアされない問題。
- 影響: 解放済みDMAマッピングの再参照によるメモリ破壊や不具合を引き起こす可能性がある。
- 推奨対応: 修正パッチが適用されたLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/2d14720beb58870b15a52b236c3ab0be0e06e915
- https://git.kernel.org/stable/c/3001a103a367c6051c43aff363b6979c10e65347
- https://git.kernel.org/stable/c/ca9986cc824f2feb79b4a83e5f6f4c24c2140448

### [CVE-2026-98438](https://git.kernel.org/stable/c/9a682067dd7b9dce6b94a0a05661dcc921446402)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98438
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 00:16:53 JST
- 更新日: 2026-10-19 00:16:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのMPTCPにおいて、データなしでDATA_FINを送信する際にチェックサム初期値（csum）がクリアされず未初期化値が参照される不具合が修正されました。
- 影響: 未初期化メモリの参照により、予期せぬネットワーク挙動やシステムの不安定化を引き起こす可能性があります。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/9a682067dd7b9dce6b94a0a05661dcc921446402
- https://git.kernel.org/stable/c/b110f1dd6cb6a9930503354a01a315e0a821eaa7

### [CVE-2026-98440](https://git.kernel.org/stable/c/22e82acec93a681071ed36f70eabe2d0c4e0bebd)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98440
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:16:54 JST
- 更新日: 2026-10-19 01:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: KVM (arm64 NV) において、シャドウS2構造体の解放処理が適切でなく、他の処理から参照中のメモリが早期解放される不具合が修正されました。
- 影響: Use-After-Free等のメモリ破壊が発生し、システムクラッシュやセキュリティ上の問題につながる可能性があります。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/22e82acec93a681071ed36f70eabe2d0c4e0bebd
- https://git.kernel.org/stable/c/5bf1c9175e657b3c2dc1cf77403031ac7aadcf66
- https://git.kernel.org/stable/c/876049f026b4dfaca0cc78ec81be0e639ca8525d
- https://git.kernel.org/stable/c/e5843f4effaa2ffac3e789ecd4456403564961d4

### [CVE-2026-98444](https://git.kernel.org/stable/c/41bc624377f08125eae164c62ce043791ade93b7)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98444
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:16:54 JST
- 更新日: 2026-10-19 01:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: XFSファイルシステムにおいて、`xfs_qm_flush_one`がバッファを取得できない場合にdquotのフラッシュロック（dqflock）を解放しない不具合が修正されました。
- 影響: ロックが解放されないことにより、デッドロックやファイルシステム操作のハング状態を引き起こす可能性があります。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/41bc624377f08125eae164c62ce043791ade93b7
- https://git.kernel.org/stable/c/ffb48dccce1960a9ea24463a2f3c21d124d6b672

### [CVE-2026-98445](https://git.kernel.org/stable/c/0e0d3372a84029da1768c7a4c4601484af5b58a2)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98445
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:16:54 JST
- 更新日: 2026-10-19 01:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: XFSのオンライン修復において、`xrep_newbt_add_blocks`でのメモリ割り当て失敗時にブロックがリークし修復処理が失敗する問題を回避するため、NOFAIL割り当てへ変更されました。
- 影響: メモリ不足時にブロックリークが発生し、ファイルシステムの破損や修復不能状態に陥る可能性があります。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/0e0d3372a84029da1768c7a4c4601484af5b58a2
- https://git.kernel.org/stable/c/3380151cf0ce8ad0c1d356fed51e4b69e1d28e50
- https://git.kernel.org/stable/c/ab1c416d2377cdc16123ef521aac4da1c468c3d4
- https://git.kernel.org/stable/c/b15c79fca28060fd9c7e77f2c3ebc4ba023974e8

### [CVE-2026-98446](https://git.kernel.org/stable/c/476582d754cdc5110f806001417fea6c77824c13)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98446
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:16:54 JST
- 更新日: 2026-10-19 01:16:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: XFSの`xfs_metafile_resv_init`において、メタデータbtreeファイル用の予約可能領域が使用済み領域を下回った際に`hidden_space`がアンダーフローする計算エラーが修正されました。
- 影響: 空きブロック数が誤って大きく減算され、ファイルシステムの不整合や異常動作を発生させる可能性があります。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/476582d754cdc5110f806001417fea6c77824c13
- https://git.kernel.org/stable/c/930a9c1c321efdaa3e7f8caecb0479cee3baf342
- https://git.kernel.org/stable/c/f0d8352a39f4a2e329ae45b71bb0d49e2ca0a6dc

### [CVE-2026-98449](https://git.kernel.org/stable/c/70783946f3b5d0c06ec7df0f5e7bec2bfad24efb)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98449
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:16:55 JST
- 更新日: 2026-10-19 01:16:55 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SMB2/3クライアントにおいて、複合リクエスト送信失敗時にリコネクト処理と競合してクレジットの二重返却（in_flightの不整合）が発生する問題が修正されました。
- 影響: カーネルの警告（WARN）が発生し、SMB接続の制御状態が破壊されて通信が不安定になる可能性があります。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/70783946f3b5d0c06ec7df0f5e7bec2bfad24efb
- https://git.kernel.org/stable/c/8f6f8a48399f82f4a83f7b9f25b9707e0062a4f9

### [CVE-2026-98479](https://git.kernel.org/stable/c/24ffc919467d20951f0f132d1c75294e2e91e09b)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98479
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:16:58 JST
- 更新日: 2026-10-19 01:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: SCSI libiscsi_tcp において、Data-In PDU のデータ方向を適切に検証せず、書き込み（WRITE）コマンドに対する Data-In PDU を誤って受容する脆弱性が修正されました。
- 影響: 悪意あるターゲットにより、イニシエータ側のメモリ（O_DIRECTバッファやページキャッシュ）が意図しないデータで上書きされる可能性があります。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/24ffc919467d20951f0f132d1c75294e2e91e09b
- https://git.kernel.org/stable/c/79991b770fc3685b1d5cf805b659a879edd19931
- https://git.kernel.org/stable/c/8db1232945bc663fb94f300090a1fc108de99296
- https://git.kernel.org/stable/c/94e5bdd08e51c450d954bc592f591c233ca5c9df
- https://git.kernel.org/stable/c/bce07e2f37b5e4a427d36fd6b1c14067b27591db

### [CVE-2026-98484](https://git.kernel.org/stable/c/12cf803edfffef96f6415f0b5dbc7ec88842ea0f)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98484
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:16:59 JST
- 更新日: 2026-10-19 01:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: netfilter (nf_tables) において、キャッチオール（catchall）要素の挿入・削除時に期限切れ要素の判定が一致しておらず、再追加が不当にブロックされる不具合が修正されました。
- 影響: キャッチオールルールが意図せず無効化されたままとなり、ファイアウォールやフィルタリングルールが機能しなくなる可能性があります。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/12cf803edfffef96f6415f0b5dbc7ec88842ea0f
- https://git.kernel.org/stable/c/2f07da3881525f7cbfed1ced2796c71a201505b9
- https://git.kernel.org/stable/c/4fb8b1ccc475651e480e509de126bb9ce7f3cff9
- https://git.kernel.org/stable/c/70194dc37670bd08e44b471389861cc01bd3a3c9

### [CVE-2026-98491](https://git.kernel.org/stable/c/26b2bd70d22457556e2fa01cbf1192cb1a94d619)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98491
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:00 JST
- 更新日: 2026-10-19 01:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Open vSwitch の conntrack 処理において、未確認（unconfirmed）接続エントリを持つパケット（skb）が複製・コミットされた際に構造体ポインタが破壊される不具合が修正されました。
- 影響: Use-After-Free (UAF) が発生し、システムクラッシュや任意のコード実行につながる危険性があります。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/26b2bd70d22457556e2fa01cbf1192cb1a94d619
- https://git.kernel.org/stable/c/37e3c878b183a115f9a114067f9ef3b408ad27fb
- https://git.kernel.org/stable/c/457e0df1b5711fbeb7ba1b6bfd826f5ef30e7e55
- https://git.kernel.org/stable/c/55e5256adf3940e71802e2f749cacf81518726b0
- https://git.kernel.org/stable/c/707c2dc77891a874f4e8c52c285a511079164ec8

### [CVE-2026-98496](https://git.kernel.org/stable/c/4bdee8060d1e4581624e68fbd369b1afb14df4bc)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98496
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:00 JST
- 更新日: 2026-10-19 01:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Airoha NPU ドライバにおいて、モジュール削除やエラー処理時に WDT 割り込みが解除される前にワーク（`wdt_work`）が取り消され、解放済みメモリへアクセスする不具合が修正されました。
- 影響: デバイスのアンロードやエラー時にUse-After-Freeが発生し、カーネルパニック等を引き起こす可能性があります。
- 推奨対応: 修正済みのLinuxカーネルへ更新してください。

#### References
- https://git.kernel.org/stable/c/4bdee8060d1e4581624e68fbd369b1afb14df4bc
- https://git.kernel.org/stable/c/aca91d8fa0ecbc990ebf9a688c684dda78a43c00
- https://git.kernel.org/stable/c/da9d42531f3a6dfea2e9c775b62a46185dbf280a

### [CVE-2026-98523](https://git.kernel.org/stable/c/11edd5b6735d2e1069ddce672b1836713647f7fb)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98523
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:03 JST
- 更新日: 2026-10-19 01:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのDRMサブシステムにおいて、部分的に初期化されたクライアントの復元処理時にNULLポインタ参照が発生する問題。
- 影響: DRMファイル記述子の解放時等にシステムクラッシュ（DoS）が引き起こされる可能性があります。
- 推奨対応: 修正されたLinuxカーネルバージョンへの更新を検討してください。

#### References
- https://git.kernel.org/stable/c/11edd5b6735d2e1069ddce672b1836713647f7fb
- https://git.kernel.org/stable/c/1fca688e9443003e33cf30453e7a7560367656c9
- https://git.kernel.org/stable/c/a69c4b678db808c0d89abb8cedeaaac38d1ef182
- https://git.kernel.org/stable/c/fcbedba553a9c430079ee225df2dc7ab556a2f83

### [CVE-2026-98528](https://git.kernel.org/stable/c/1feb5d39b05afd902ed9fc902ec5b15be03a4bdb)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98528
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:04 JST
- 更新日: 2026-10-19 01:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのGPIOサブシステムのエラーパス処理において、構造体の初期化前に復帰するためカーネルスタックのデータがユーザー空間に漏洩する問題。
- 影響: カーネルスタック内の機密情報がローカルユーザーへ漏洩する可能性があります。
- 推奨対応: 修正されたLinuxカーネルバージョンへの更新を検討してください。

#### References
- https://git.kernel.org/stable/c/1feb5d39b05afd902ed9fc902ec5b15be03a4bdb
- https://git.kernel.org/stable/c/60a466f231905cd96ae6f0f3c44a710c97873dac
- https://git.kernel.org/stable/c/8460ee5216ab9a38263b01dca4b0a27e083f70f3
- https://git.kernel.org/stable/c/cf3d043582e106a0e57002bec8a6de8929ba3e1c

### [CVE-2026-98539](https://git.kernel.org/stable/c/1abd643f3783ea8f8e273c18697ff0413aa92dc7)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98539
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:05 JST
- 更新日: 2026-10-19 01:17:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのNTFS3ファイルシステムにおいて、新規dentry/inode作成時の処理不備によりロック状態の競合が発生する問題。
- 影響: システムの不安定化やカーネル警告の発生、DoSにつながる可能性があります。
- 推奨対応: 修正されたLinuxカーネルバージョンへの更新を検討してください。

#### References
- https://git.kernel.org/stable/c/1abd643f3783ea8f8e273c18697ff0413aa92dc7
- https://git.kernel.org/stable/c/1ae2a242c15b03470b1b16289298e597bbe3bb29
- https://git.kernel.org/stable/c/37ec7353f4ac495b28284b0fcb0e53d21d1b3f3f
- https://git.kernel.org/stable/c/6fda7121cb6a8ea6fbd77d0f787f04b8e8b5358e

### [CVE-2026-98544](https://git.kernel.org/stable/c/28e32ace754b57534ef0ca0fb99bcbea5b13ba2a)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98544
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:06 JST
- 更新日: 2026-10-19 01:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのbnaネットワークドライバの停止処理において、タイマーが相互に再アームされ解放済みメモリへアクセスする問題。
- 影響: ドライバの削除・失敗時にUse-After-Freeが発生し、システムクラッシュや不具合を引き起こす可能性があります。
- 推奨対応: 修正されたLinuxカーネルバージョンへの更新を検討してください。

#### References
- https://git.kernel.org/stable/c/28e32ace754b57534ef0ca0fb99bcbea5b13ba2a
- https://git.kernel.org/stable/c/4d97a141e85a034566c33c7ed854c8a3e8a268f1
- https://git.kernel.org/stable/c/77b1718e39e5c9f6956fb60807326af20baf889d
- https://git.kernel.org/stable/c/e09d1c6729ee4a7812128902d9274ff565f958b8

### [CVE-2026-98545](https://git.kernel.org/stable/c/1603abb0c50420e97cf4a1feddbd5e183c5fdf86)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98545
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:06 JST
- 更新日: 2026-10-19 01:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのATA/ATAPIパススルー処理において、応答データの長さを不適切に信頼することでバッファ外読み書きが発生する問題。
- 影響: 悪意あるまたは不正なデバイスにより、カーネルのバッファオーバーフローやメモリ破壊が引き起こされる可能性があります。
- 推奨対応: 修正されたLinuxカーネルバージョンへの更新を検討してください。

#### References
- https://git.kernel.org/stable/c/1603abb0c50420e97cf4a1feddbd5e183c5fdf86
- https://git.kernel.org/stable/c/80320b278fea07ffcda3f57b67b61658e0a4e1ca
- https://git.kernel.org/stable/c/80fbb0bc4d11683c88f2f9d3997ea02fcada5408
- https://git.kernel.org/stable/c/c698f6deabf680f8f4a1727ef2dc80fe78815fbf
- https://git.kernel.org/stable/c/d9a7147b93624660626cd7c3b1143715699e1f5c

### [CVE-2026-98547](https://git.kernel.org/stable/c/02afd75649a4e001031ed82153a5c39312ec0737)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98547
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:06 JST
- 更新日: 2026-10-19 01:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのaf_packetモジュールにおけるタイムアウト計算時に32ビット整数オーバーフローが発生する問題。
- 影響: 特定のパケットリング設定時に計算結果が不適切となり、ネットワーク動作に影響を与える可能性があります。
- 推奨対応: 修正されたLinuxカーネルバージョンへの更新を検討してください。

#### References
- https://git.kernel.org/stable/c/02afd75649a4e001031ed82153a5c39312ec0737
- https://git.kernel.org/stable/c/218a944b9e035d4b47d59c69af6ca13319da15fb
- https://git.kernel.org/stable/c/297acc571d5813db76b147c745b91031d5f9c960
- https://git.kernel.org/stable/c/56d82862a0a243ac14ba11b6d7b57ddc2d064b95
- https://git.kernel.org/stable/c/6279211e7d2456ecd195d236c9ee5e5c6fa5a17a

### [CVE-2026-98558](https://git.kernel.org/stable/c/06e3f54e8b22040ada01a28343badf1990b4dd7d)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98558
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:07 JST
- 更新日: 2026-10-19 01:17:07 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルにおいて、CPUがオフラインになる際に未処理の遅延SKBが解放されず滞留する問題。
- 影響: ネットワークデバイスの破棄時等に処理が永久にハングアップする（DoS）可能性があります。
- 推奨対応: 修正されたLinuxカーネルバージョンへの更新を検討してください。

#### References
- https://git.kernel.org/stable/c/06e3f54e8b22040ada01a28343badf1990b4dd7d
- https://git.kernel.org/stable/c/c68f4157463448a76893223e117170be8374d773

### [CVE-2026-98563](https://git.kernel.org/stable/c/4e7a4af364c2048bafb213bf0ef4a89dcbe1bfd4)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98563
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:08 JST
- 更新日: 2026-10-19 01:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Linuxカーネルのphylinkにおいて、PHYのセットアップ失敗時に不適切なポインタが残留する問題。
- 影響: PHYデバイスの解放後に無効なポインタを参照し、永久的な接続失敗やシステム不具合を引き起こす可能性があります。
- 推奨対応: 修正されたLinuxカーネルバージョンへの更新を検討してください。

#### References
- https://git.kernel.org/stable/c/4e7a4af364c2048bafb213bf0ef4a89dcbe1bfd4
- https://git.kernel.org/stable/c/671a68654a9d319d7f0d53a6321db3d9b391bdef
- https://git.kernel.org/stable/c/a940003f44e7e441c228151dd212642152700ec8

### [CVE-2026-98564](https://git.kernel.org/stable/c/0d80ba0a204c6a16bd7778b50de578dff107c0fe)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98564
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:08 JST
- 更新日: 2026-10-19 01:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのMT7530 DSAスイッチドライバ除去処理において、割り込みマッピングの解放タイミングが不適切である問題。
- 影響: ドライバアンロード時に無効な割り込みハンドラが実行され、NULLポインタ参照等でカーネルパニックを引き起こす可能性があります。
- 推奨対応: 修正されたLinuxカーネルバージョンへの更新を検討してください。

#### References
- https://git.kernel.org/stable/c/0d80ba0a204c6a16bd7778b50de578dff107c0fe
- https://git.kernel.org/stable/c/2357c682f6eaf639dec88c68b3c0c93a3b802635
- https://git.kernel.org/stable/c/f306e465b5a2091cd3fe3dd0feb10cfc94cfb2f8

### [CVE-2026-98573](https://git.kernel.org/stable/c/3b4e0b0c008a8c1b474730248cd5b873026c74bd)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-98573
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-19 01:17:09 JST
- 更新日: 2026-10-19 01:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LinuxカーネルのIPv6拡張ヘッダー解析において、プルバウンド計算時にアンダーフローが発生する問題。
- 影響: 負の長さの計算結果により大きなメモリコピーが発生し、メモリ破壊やシステムクラッシュを引き起こす可能性があります。
- 推奨対応: 修正されたLinuxカーネルバージョンへの更新を検討してください。

#### References
- https://git.kernel.org/stable/c/3b4e0b0c008a8c1b474730248cd5b873026c74bd
- https://git.kernel.org/stable/c/6c28c31f051dbf49c71ba7ab7bb9bc905fa1d14b
- https://git.kernel.org/stable/c/718747afa5463d9cc5fd9a09f03b2a492edd9b78
- https://git.kernel.org/stable/c/9c4e432132a97b82edf28fa172c39f743e6bfb26
- https://git.kernel.org/stable/c/a0ad0473c09d2e947aecac5c82e637ec85924b12

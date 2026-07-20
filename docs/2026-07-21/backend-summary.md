# Backend CVE Summary (2026-07-21)

## Overview

- 取得日時: 2026-07-21 08:11:27 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 10
- Critical: 1
- High: 4
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-35048](https://github.com/Piwigo/Piwigo/security/advisories/GHSA-gphq-34pv-gvf3)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-35048
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-21 02:17:06 JST
- 更新日: 2026-07-21 03:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Piwigo 16.3.0以前のインストーラーで、POSTパラメータが適切にサニタイズされずPHP設定ファイルに書き込まれる脆弱性が存在します。  
- 影響: PHP 8以降で`addslashes()`の保護が無効化され、認証なしに任意のPHPコードを注入・実行される恐れがあります。  
- 推奨対応: 影響を受けるバージョンの使用を避け、開発元からの修正パッチ適用やバージョンアップを行うことが望ましいです。

#### References
- https://github.com/Piwigo/Piwigo/security/advisories/GHSA-gphq-34pv-gvf3
- https://github.com/Piwigo/Piwigo/security/advisories/GHSA-gphq-34pv-gvf3

### [CVE-2026-55219](https://github.com/Paymenter/Paymenter/security/advisories/GHSA-pgcq-8grm-5rx9)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-55219
- 関連キーワード: go, gin, mysql
- 影響製品: -
- 公開日: 2026-07-21 06:16:48 JST
- 更新日: 2026-07-21 07:17:16 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Paymenterの1.5.5未満のバージョンで、トランザクション外での行ロックが無効となり、同時決済リクエストにより同一クレジット残高を複数回使用できる競合状態が発生します。  
- 影響: 同一クレジット残高を使った複数請求の支払いが可能となり、プラットフォームに金銭的またはリソースの損失をもたらす可能性があります。  
- 推奨対応: バージョン1.5.5以降にアップデートし、決済処理が適切にトランザクション内で行われることを確認してください。

#### References
- https://github.com/Paymenter/Paymenter/security/advisories/GHSA-pgcq-8grm-5rx9

### [CVE-2026-32824](https://github.com/datacycle-engine/dataCycle-CORE/security/advisories/GHSA-8jfx-wpjg-hf38)

> **Backend** / **HIGH** / CVSS: **7.3** / KEV: **no**

- タイトル: CVE-2026-32824
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-21 02:17:06 JST
- 更新日: 2026-07-21 03:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: dataCycle-COREの25.07.3以前のバージョンで、認証済みの低権限APIユーザーがパスワードリセットや確認フロー時に悪意あるURLを指定できる脆弱性が存在します。  
- 影響: フィッシングやトークンの盗用、確認プロセスの乗っ取り、被害者を攻撃者のサイトへ誘導されるリスクがあります。  
- 推奨対応: バージョン26.06.08以降へのアップデートを実施し、不正なURLの埋め込みを防ぐ対策を行ってください。

#### References
- https://github.com/datacycle-engine/dataCycle-CORE/security/advisories/GHSA-8jfx-wpjg-hf38

### [CVE-2026-13724](https://siberguvenlik.gov.tr/guvenlik-bildirimleri/detay/tr-26-0582)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-13724
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-21 01:16:55 JST
- 更新日: 2026-07-21 02:15:16 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Gobito InformaticsのCorporate Training Management Systemにおいて、クライアント側でのサーバーセキュリティ強制が不十分で入力データの改ざんが可能な脆弱性が存在します。  
- 影響: 不正な入力データ操作により、システムの正常な動作やセキュリティが損なわれる可能性があります。  
- 推奨対応: 影響を受けるバージョンからのアップデートや、サーバー側での入力検証強化を検討してください。

#### References
- https://siberguvenlik.gov.tr/guvenlik-bildirimleri/detay/tr-26-0582

### [CVE-2026-45709](https://github.com/axllent/mailpit/releases/tag/v1.30.0)

> **Backend** / **MEDIUM** / CVSS: **5.8** / KEV: **no**

- タイトル: CVE-2026-45709
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-07-21 01:17:00 JST
- 更新日: 2026-07-21 04:17:22 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Mailpitのv1.30.0未満のバージョンにおいて、HTML Check APIのCSSダウンロード機能でIPアドレスのフィルタリングが不十分なため、SSRF攻撃が可能な脆弱性が存在します。  
- 影響: 攻撃者がMailpitサーバーを経由してループバックやプライベートネットワーク内のリソースにアクセスできる可能性があります。  
- 推奨対応: Mailpitをv1.30.0以降にアップデートし、IPフィルタリングが適切に実装されたバージョンを使用してください。

#### References
- https://github.com/axllent/mailpit/releases/tag/v1.30.0
- https://github.com/axllent/mailpit/security/advisories/GHSA-j3fj-qppj-fmmc

### [CVE-2026-44508](https://github.com/RsyncProject/rsync/security/advisories/GHSA-g37v-g3gj-pmwq)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-44508
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-21 06:16:47 JST
- 更新日: 2026-07-21 06:16:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Rsyncの3.4.3未満のバージョンで、圧縮トークンデコーダが32ビット符号付きカウンタのオーバーフローを検証せず、悪意ある送信者によるメモリ情報漏洩の可能性がある。  
- 影響: 環境変数やパスワード、メモリポインタが漏洩し、ASLRの効果が低下し、さらなる攻撃の足掛かりとなる恐れがある。  
- 推奨対応: Rsyncをバージョン3.4.3以降にアップデートし、信頼できない送信者からのデータを慎重に扱うこと。

#### References
- https://github.com/RsyncProject/rsync/security/advisories/GHSA-g37v-g3gj-pmwq

### [CVE-2026-45713](https://github.com/axllent/mailpit/releases/tag/v1.30.0)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-45713
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-21 01:17:00 JST
- 更新日: 2026-07-21 02:17:09 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: MailpitのSMTPサーバーおよびHTTP送信APIにおいて、最大データサイズ制限が設定されておらず、攻撃者が任意の大きさのメッセージを送信可能です。  
- 影響: 大量のメモリ消費を引き起こし、サービスのOOMキルや停止を招く恐れがあります。  
- 推奨対応: バージョン1.30.0以降にアップデートし、適切なサイズ制限を適用してください。

#### References
- https://github.com/axllent/mailpit/releases/tag/v1.30.0
- https://github.com/axllent/mailpit/security/advisories/GHSA-fpxj-m5q8-fphw
- https://github.com/axllent/mailpit/security/advisories/GHSA-fpxj-m5q8-fphw

### [CVE-2026-60026](https://www.themexpert.com/quix-pagebuilder)

> **Backend** / **HIGH** / CVSS: **8.9** / KEV: **no**

- タイトル: CVE-2026-60026
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-21 04:17:26 JST
- 更新日: 2026-07-21 04:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: JoomlaのQuix Page Builder Pro拡張機能において、認証済みユーザーがPHPコードを実行可能な脆弱性が存在します。  
- 影響: 認証されたビルダー権限ユーザーがPHPタグを注入し、サーバー上で任意のコードが実行される可能性があります。  
- 推奨対応: 影響を受ける拡張機能のアップデート適用や、キャッシュ機能の設定見直しを検討してください。

#### References
- https://www.themexpert.com/quix-pagebuilder

### [CVE-2026-44978](https://github.com/neutrinolabs/xrdp/releases/tag/v0.10.6.1)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-44978
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-21 02:17:09 JST
- 更新日: 2026-07-21 02:17:09 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: xrdp 0.10.6以前のバージョンにおいて、特定のFIPS設定時にヒープの範囲外読み取りが発生する脆弱性が存在します。  
- 影響: 認証されていないリモート攻撃者による細工されたFIPS保護PDU送信でプロセスクラッシュやサービス拒否（DoS）が引き起こされる可能性があります。  
- 推奨対応: xrdpをバージョン0.10.6.1以降にアップデートし、非デフォルトのFIPS設定を使用している場合は設定の見直しを検討してください。

#### References
- https://github.com/neutrinolabs/xrdp/releases/tag/v0.10.6.1
- https://github.com/neutrinolabs/xrdp/security/advisories/GHSA-9cg5-f7m7-ppvj

### [CVE-2026-55238](https://github.com/neutrinolabs/xrdp/releases/tag/v0.10.6.1)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-55238
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-07-21 02:18:07 JST
- 更新日: 2026-07-21 04:17:25 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: xrdp 0.10.6以前のバージョンにおいて、RDP Confirm Active PDUの処理時に特定の能力セットの長さ検証が不十分な脆弱性が存在します。  
- 影響: 攻撃者が細工したRDPパケットを送信することで、サービスの一部プロセスが異常終了し、DoS状態を引き起こす可能性があります。  
- 推奨対応: xrdpをバージョン0.10.6.1以降にアップデートし、脆弱性修正を適用してください。

#### References
- https://github.com/neutrinolabs/xrdp/releases/tag/v0.10.6.1
- https://github.com/neutrinolabs/xrdp/security/advisories/GHSA-mg8j-x9rw-9xv3

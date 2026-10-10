# Backend CVE Summary (2026-10-10)

## Overview

- 取得日時: 2026-10-10 10:42:46 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 25
- Critical: 6
- High: 8
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-108109](https://github.com/hotspotbilling/phpnuxbill)

> **Backend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-108109
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-10 00:17:12 JST
- 更新日: 2026-10-10 03:17:06 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: PHPNuxBill の顧客パスワードリセット処理における 6 桁 OTP のレート制限欠如の脆弱性。
- 影響: 未認証の攻撃者が OTP コードを総当たりで無制限に試行し、応答内容から新パスワードを取得してアカウントを乗っ取る可能性がある。
- 推奨対応: PHPNuxBill を 2025.3.20 より後の修正済みバージョンへアップデートする。

#### References
- https://github.com/hotspotbilling/phpnuxbill
- https://github.com/hotspotbilling/phpnuxbill/blob/2025.3.13/system/controllers/forgot.php#L41
- https://github.com/hotspotbilling/phpnuxbill/commit/c3c2a92d468af91136d747b75142ed72f10320cc
- https://github.com/hotspotbilling/phpnuxbill/security/advisories/GHSA-337r-rrrc-r559
- https://www.vulncheck.com/advisories/phpnuxbill-through-2025.3.20-account-takeover-via-brute-forceable-password-reset-code

### [CVE-2026-108267](https://github.com/Privasys/go/commit/00a7d21ba53bba0ea09ac7a67eb2c6714e651700)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-108267
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-10 07:16:59 JST
- 更新日: 2026-10-10 07:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Privasys Go の RA-TLS 実装において、Quote 検証がアクティブな TLS セッションにバインドされていない脆弱性。
- 影響: TLS 秘密鍵を取得した攻撃者が有効な Quote を別の接続へ中継（リレー）し、信頼されたエンクレイブ接続として偽装できる可能性がある。
- 推奨対応: Privasys Go を privasys-v0.5.1-go1.26.5 以降にアップデートする。

#### References
- https://github.com/Privasys/go/commit/00a7d21ba53bba0ea09ac7a67eb2c6714e651700
- https://github.com/Privasys/go/releases/tag/privasys-v0.5.1-go1.26.5
- https://github.com/Privasys/go/security/advisories/GHSA-7jfw-53rm-phh2
- https://privasys.org/blog/binding-attestation-to-the-tls-session

### [CVE-2026-108269](https://github.com/Privasys/ra-tls-clients/commit/b8de9bcadd0f81ca8882d15095fc0d9c50e40148)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-108269
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-10 07:16:59 JST
- 更新日: 2026-10-10 07:16:59 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Remote Attestation TLS Clients (Rust/Go) における RA-TLS 検証時のセッションバインディング不足の脆弱性。
- 影響: TLS 秘密鍵を持つ攻撃者が検証用の Quote を別接続へリレーすることで、攻撃者の接続を証明済みエンクレイブからの接続としてクライアントに認識させる可能性がある。
- 推奨対応: Remote Attestation TLS Clients をバージョン 0.5.0 以降にアップデートする。

#### References
- https://github.com/Privasys/ra-tls-clients/commit/b8de9bcadd0f81ca8882d15095fc0d9c50e40148
- https://github.com/Privasys/ra-tls-clients/releases/tag/v0.5.0
- https://github.com/Privasys/ra-tls-clients/security/advisories/GHSA-5qrc-v874-mxvx
- https://github.com/Privasys/ra-tls-clients/security/advisories/GHSA-5qrc-v874-mxvx
- https://privasys.org/blog/binding-attestation-to-the-tls-session

### [CVE-2026-107810](https://github.com/0xJacky/nginx-ui/commit/a467ed652591fc0cd1b466a1ec751b493faef9f7)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-107810
- 関連キーワード: go, gin, nginx
- 影響製品: -
- 公開日: 2026-10-10 01:17:25 JST
- 更新日: 2026-10-10 01:38:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Nginx UI のバックアップ展開処理におけるシンボリックリンク検証の不備に関する脆弱性。
- 影響: 認証済みユーザーが展開先にシンボリックリンクを含むバックアップを書き戻すことで、フラグ設定を迂回して任意ファイルへ書き込みを行い、設定改ざんや DoS を引き起こす可能性がある。
- 推奨対応: Nginx UI をバージョン 2.5.0 以降にアップデートする。

#### References
- https://github.com/0xJacky/nginx-ui/commit/a467ed652591fc0cd1b466a1ec751b493faef9f7
- https://github.com/0xJacky/nginx-ui/releases/tag/v2.5.0
- https://github.com/0xJacky/nginx-ui/security/advisories/GHSA-p8v3-89rh-jxc7

### [CVE-2026-102554](https://github.com/google/guava/commit/b931fe9d6d5cf00bc55714ad3308d086f71850fe)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-102554
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-10 01:17:20 JST
- 更新日: 2026-10-10 03:17:01 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Google Guava の Java オブジェクト逆シリアル化処理における無制限なメモリ割り当て（CWE-770）の脆弱性。
- 影響: 悪意あるシリアル化データを受信した際、サイズ指定に基づく大量のメモリ確保が行われ、OutOfMemoryError によるサービス拒否（DoS）が引き起こされる可能性がある。
- 推奨対応: Google Guava を脆弱性が修正されたバージョンに更新する。

#### References
- https://github.com/google/guava/commit/b931fe9d6d5cf00bc55714ad3308d086f71850fe
- https://github.com/google/guava/releases/tag/v33.7.2
- https://github.com/google/guava/security/advisories/GHSA-xxph-c9ww-hj94
- https://github.com/google/guava/security/advisories/GHSA-xxph-c9ww-hj94

### [CVE-2026-107826](https://github.com/corazawaf/coraza/commit/814e1898e083d2ff2ceb644382d0da17e930f93f)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-107826
- 関連キーワード: go, golang
- 影響製品: -
- 公開日: 2026-10-10 03:17:04 JST
- 更新日: 2026-10-10 03:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OWASP Coraza WAFのJSONボディ処理における過度なスタック再帰に起因する脆弱性。
- 影響: 未認証の攻撃者が深いネストを持つJSONパケットを送信することで、プロセスを強制終了（DoS）させる可能性があります。
- 推奨対応: OWASP Coraza WAFをバージョン 3.8.1 以降へ更新してください。

#### References
- https://github.com/corazawaf/coraza/commit/814e1898e083d2ff2ceb644382d0da17e930f93f
- https://github.com/corazawaf/coraza/releases/tag/v3.8.1
- https://github.com/corazawaf/coraza/security/advisories/GHSA-6gcq-wc29-5xf2
- https://github.com/corazawaf/coraza/security/advisories/GHSA-6gcq-wc29-5xf2

### [CVE-2026-55797](https://github.com/argoproj/argo-cd/commit/1e3ddd0b7250aa23f489956b5fab8c13d0493a9f)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-55797
- 関連キーワード: go, kubernetes
- 影響製品: -
- 公開日: 2026-10-10 02:16:47 JST
- 更新日: 2026-10-10 03:17:08 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Argo CDのrepo-serverにおけるプロキシ設定付きSSHリポジトリ処理時のコマンドインジェクションの脆弱性。
- 影響: リポジトリ設定権限を持つユーザーにより、repo-server上で任意コマンドが実行され、Git/Helm/OCIの認証情報が奪取される可能性があります。
- 推奨対応: Argo CDをバージョン 3.3.15、3.4.10、3.5.4、または 3.6.0-rc2 以降へ更新してください。

#### References
- https://github.com/argoproj/argo-cd/commit/1e3ddd0b7250aa23f489956b5fab8c13d0493a9f
- https://github.com/argoproj/argo-cd/commit/9b27aeb1a4fb15d11a0f01cad65dea1fdfc60205
- https://github.com/argoproj/argo-cd/pull/15864
- https://github.com/argoproj/argo-cd/releases/tag/v3.3.15
- https://github.com/argoproj/argo-cd/releases/tag/v3.4.10

### [CVE-2026-107840](https://github.com/jhaals/yopass/commit/61e31ead04a4fc27ce80bed226af41c7c0426ccf)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-107840
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-10 03:17:05 JST
- 更新日: 2026-10-10 05:17:09 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: yopassのPrometheusメトリクスミドルウェアにおける、未制限のHTTPメソッド名記録に起因するメモリ消費の脆弱性。
- 影響: 未認証の攻撃者が多様なHTTPメソッドを送信することでメモリが持続的に増加し、OOMによるプロセス停止や監視低下を引き起こす可能性があります。
- 推奨対応: yopassをバージョン 14.7.0 以降へ更新してください。

#### References
- https://github.com/jhaals/yopass/commit/61e31ead04a4fc27ce80bed226af41c7c0426ccf
- https://github.com/jhaals/yopass/commit/78d0c14f7085048130199662a2ec8a18ec8d6ebb
- https://github.com/jhaals/yopass/pull/3773
- https://github.com/jhaals/yopass/releases/tag/14.7.0
- https://github.com/jhaals/yopass/security/advisories/GHSA-6r69-c6wg-7g8m

### [CVE-2026-95702](https://github.com/google/gvisor/commit/25c75149bc0eeaa6a3a49b9bbe3473588b2af6df)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-95702
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-10 00:17:20 JST
- 更新日: 2026-10-10 01:35:35 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Google gVisorのVFSにおけるMemoryFileの二重解放（Use-after-free）の脆弱性。
- 影響: 標準的なコンテナ権限を持つローカル攻撃者が、ホスト上のsentryプロセス内で任意コードを実行できる可能性があります（ただしホスト側のseccompやnamespaceにより境界制限されます）。
- 推奨対応: gVisorをリリース 20260831.0 以降へ更新してください。

#### References
- https://github.com/google/gvisor/commit/25c75149bc0eeaa6a3a49b9bbe3473588b2af6df
- https://github.com/google/gvisor/commit/90bc4fc36fe442257a06ba15df00371561c183ed
- https://github.com/google/gvisor/commit/e4efb89c787ef15b09e68d561f1303380e1d5a77

### [CVE-2026-107825](https://github.com/corazawaf/coraza/commit/0321af96cef18fbafb40980cf075d7cc449a66fa)

> **Backend** / **MEDIUM** / CVSS: **4.0** / KEV: **no**

- タイトル: CVE-2026-107825
- 関連キーワード: go, golang
- 影響製品: -
- 公開日: 2026-10-10 03:17:04 JST
- 更新日: 2026-10-10 03:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OWASP Coraza WAFのProcessURIにおける不正なURI解析時のクエリ変数初期化の不備。
- 影響: 特定の統合環境（SPOA、Proxy-WASM等）において、WAFルールによる検査をバイパスして後続アプリケーションへリクエストが届く可能性があります。
- 推奨対応: OWASP Coraza WAFをバージョン 3.8.0 以降へ更新してください。

#### References
- https://github.com/corazawaf/coraza/commit/0321af96cef18fbafb40980cf075d7cc449a66fa
- https://github.com/corazawaf/coraza/releases/tag/v3.8.0
- https://github.com/corazawaf/coraza/security/advisories/GHSA-x26q-wvhg-fh4m

### [CVE-2026-107833](https://github.com/corazawaf/coraza/commit/cae3c7407e7b84372c207033de03f15f89bf351a)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-107833
- 関連キーワード: go, golang
- 影響製品: -
- 公開日: 2026-10-10 03:17:04 JST
- 更新日: 2026-10-10 03:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OWASP Coraza WAFのレスポンスJSON処理（ProcessResponse）における再帰上限設定の不備。
- 影響: 応答ボディ検証が有効な環境において、攻撃者が深いネストのJSON応答を発生させることで、高負荷（CPU消費）によるDoSを引き起こす可能性があります。
- 推奨対応: OWASP Coraza WAFをバージョン 3.8.0 以降へ更新してください。

#### References
- https://github.com/corazawaf/coraza/commit/cae3c7407e7b84372c207033de03f15f89bf351a
- https://github.com/corazawaf/coraza/releases/tag/v3.8.0
- https://github.com/corazawaf/coraza/security/advisories/GHSA-3c6w-j9xm-8h2h
- https://github.com/corazawaf/coraza/security/advisories/GHSA-3c6w-j9xm-8h2h

### [CVE-2026-107834](https://github.com/corazawaf/coraza/commit/1bc39036e99c88e7de60cf8e6bb55ee4c311223c)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-107834
- 関連キーワード: go, golang
- 影響製品: -
- 公開日: 2026-10-10 03:17:05 JST
- 更新日: 2026-10-10 03:17:05 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OWASP Coraza WAFのmultipart処理におけるファイルディスクリプタ保持の不備。
- 影響: 未認証の攻撃者が多数のファイルパートを含むリクエストを送信することでファイルディスクリプタを枯渇させ、新たな接続拒否やDoSを引き起こす可能性があります。
- 推奨対応: OWASP Coraza WAFをバージョン 3.8.0 以降へ更新してください。

#### References
- https://github.com/corazawaf/coraza/commit/1bc39036e99c88e7de60cf8e6bb55ee4c311223c
- https://github.com/corazawaf/coraza/releases/tag/v3.8.0
- https://github.com/corazawaf/coraza/security/advisories/GHSA-rp9v-7xv3-r6g3

### [CVE-2026-107835](https://github.com/corazawaf/coraza/commit/0b940e197ad9983fb3aa36e84f1f81ff985461af)

> **Backend** / **MEDIUM** / CVSS: **4.0** / KEV: **no**

- タイトル: CVE-2026-107835
- 関連キーワード: go, golang
- 影響製品: -
- 公開日: 2026-10-10 03:17:05 JST
- 更新日: 2026-10-10 04:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OWASP Coraza WAFのCookie解析におけるバックエンドパーサーとの解釈不一致の脆弱性。
- 影響: 未認証の攻撃者が特殊なCookieヘッダーを送信することでWAFのルールをバイパスし、後続アプリケーションにデータを到達させる可能性があります。
- 推奨対応: OWASP Coraza WAFをバージョン 3.8.1 以降へ更新してください。

#### References
- https://github.com/corazawaf/coraza/commit/0b940e197ad9983fb3aa36e84f1f81ff985461af
- https://github.com/corazawaf/coraza/commit/9f8521398d1ff023b958fad0b944cac265763866
- https://github.com/corazawaf/coraza/releases/tag/v3.8.1
- https://github.com/corazawaf/coraza/security/advisories/GHSA-g4qm-m288-5cp9
- https://github.com/corazawaf/coraza/security/advisories/GHSA-g4qm-m288-5cp9

### [CVE-2025-61560](https://github.com/argoproj/argo-cd/)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2025-61560
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-10 02:16:41 JST
- 更新日: 2026-10-10 02:41:15 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Argo CD v3.0.6のSessionManagerにおけるレースコンディションの脆弱性。
- 影響: 攻撃者によってレート制限を回避され、ブルートフォース攻撃が行われる可能性があります。
- 推奨対応: 修正情報の詳細を確認し、対策バージョンへの更新または適切なアクセス制限を実施してください。

#### References
- https://github.com/argoproj/argo-cd/
- https://github.com/argoproj/argo-cd/security/advisories/GHSA-4439-h7jw-5cjj

### [CVE-2026-107841](https://github.com/john-broadway/pacioli/commit/f3c7219f5dde6050bd7921e0ac55afd02771250c)

> **Backend** / **MEDIUM** / CVSS: **5.7** / KEV: **no**

- タイトル: CVE-2026-107841
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-10 03:17:06 JST
- 更新日: 2026-10-10 04:16:41 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pacioliのpacioli-guardにおける同意ゲート（consent gate）処理の検証不備。
- 影響: 特定の権限を持つユーザーが、不正に別のドキュメントの取り消し操作（Document.cancel）を実行できる可能性があります。
- 推奨対応: pacioliをバージョン 0.10.0 以降へ更新してください。

#### References
- https://github.com/john-broadway/pacioli/commit/f3c7219f5dde6050bd7921e0ac55afd02771250c
- https://github.com/john-broadway/pacioli/releases/tag/guard-v0.10.0
- https://github.com/john-broadway/pacioli/security/advisories/GHSA-3hj7-6vmj-h8v4

### [CVE-2026-107856](https://github.com/civiform/civiform/commit/ccfd84ff2d9ee6570a1b1524c7ae3a3732e1839e)

> **Backend** / **MEDIUM** / CVSS: **4.5** / KEV: **no**

- タイトル: CVE-2026-107856
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-10 06:17:03 JST
- 更新日: 2026-10-10 06:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: CiviForm 3.33.0 未満におけるアクセス制御不備。GET /admin/tiDash/editClientForm/:accountId にてリクエスト者が所属するグループの検証が不足しています。
- 影響: 認証済みの仲介者（Trusted Intermediary）がアカウントIDを列挙し、自身のグループ外の市民の名前やメールアドレス等の情報を閲覧できる可能性があります。
- 推奨対応: CiviForm 3.33.0 以降へアップデートしてください。

#### References
- https://github.com/civiform/civiform/commit/ccfd84ff2d9ee6570a1b1524c7ae3a3732e1839e
- https://github.com/civiform/civiform/pull/13635
- https://github.com/civiform/civiform/releases/tag/v3.33.0
- https://github.com/civiform/civiform/security/advisories/GHSA-qv7c-9hjr-9rv7

### [CVE-2026-108263](https://github.com/iflytek/astron-agent/commit/848daba03e5e045435863815be7ab6dfbcefc18f)

> **Backend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-108263
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-10 06:17:04 JST
- 更新日: 2026-10-10 06:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Astron Agent 1.1.2 未満におけるコード実行時の制限回避。CODE_EXEC_TYPE 未設定時にサンドボックス制限のない LocalExecutor が選択されます。
- 影響: 認証済みの低権限テナントがコンテナ内で root 権限でコードを実行し、他テナントのデータ閲覧・改ざんや共有サービスを妨害できる可能性があります。
- 推奨対応: Astron Agent 1.1.2 以降へアップデートしてください。

#### References
- https://github.com/iflytek/astron-agent/commit/848daba03e5e045435863815be7ab6dfbcefc18f
- https://github.com/iflytek/astron-agent/commit/ebf074a431e96da0ad9e0a56409d3d2da15eae36
- https://github.com/iflytek/astron-agent/pull/1650
- https://github.com/iflytek/astron-agent/pull/1651
- https://github.com/iflytek/astron-agent/releases/tag/v1.1.2

### [CVE-2026-108264](https://github.com/wizarrrr/wizarr/commit/6aa3c33c1b3d945e055ef116cc531028b3735bb7)

> **Backend** / **CRITICAL** / CVSS: **9.1** / KEV: **no**

- タイトル: CVE-2026-108264
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-10 06:17:04 JST
- 更新日: 2026-10-10 06:17:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Wizarr 2026.9.1 未満における Jinja2 テンプレートの不正評価。ウィザードステップの Markdown がサンドボックス化されていない環境で処理されます。
- 影響: 認証済みユーザーや管理者の不正ファイル読み込みを通じて、任意の Python コード実行、OS コマンド実行、秘密鍵や認証情報の漏洩、蓄積型 XSS などが発生する可能性があります。
- 推奨対応: Wizarr 2026.9.1 以降へアップデートしてください。

#### References
- https://github.com/wizarrrr/wizarr/commit/6aa3c33c1b3d945e055ef116cc531028b3735bb7
- https://github.com/wizarrrr/wizarr/releases/tag/v2026.9.1
- https://github.com/wizarrrr/wizarr/security/advisories/GHSA-h9rv-mxh2-35f3

### [CVE-2026-75597](https://github.com/pyload/pyload/commit/e80c940cd604e60d93e3164429d4fc4aac54468d)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-75597
- 関連キーワード: python, gin
- 影響製品: -
- 公開日: 2026-10-10 02:16:48 JST
- 更新日: 2026-10-10 03:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pyLoad 0.5.0b3.dev101 未満における認証欠如およびエラー処理の不備。/web/<path:filename> ルート経由で内部テンプレートへ未認証アクセスが可能です。
- 影響: 未認証の第三者により、有効なテンプレート名の列挙や、500 エラー画面からの内部 Jinja2 変数名の漏洩が発生する可能性があります。
- 推奨対応: pyLoad 0.5.0b3.dev101 以降（修正パッチ適用版）へアップデートしてください。

#### References
- https://github.com/pyload/pyload/commit/e80c940cd604e60d93e3164429d4fc4aac54468d
- https://github.com/pyload/pyload/security/advisories/GHSA-j92p-c242-7hfx
- https://github.com/pyload/pyload/security/advisories/GHSA-j92p-c242-7hfx

### [CVE-2026-48484](https://github.com/pyload/pyload/blob/8e447958b8a66c5899775e725a8b90bce6643004/src/pyload/webui/app/blueprints/api_blueprint.py#L73)

> **Backend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-48484
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-10 02:16:47 JST
- 更新日: 2026-10-10 02:16:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: pyLoad 0.5.0b3.dev101 未満におけるメモリ消費に関する不備。API rpc の multipart/form-data 処理時にアップロードファイル全体を直接メモリへ読み込みます。
- 影響: サイズ制限がないため、過大なファイルのアップロードによってサーバーのメモリが枯渇し、プロセスが強制終了（DoS）する可能性があります。
- 推奨対応: pyLoad 0.5.0b3.dev101 以降へアップデートしてください。

#### References
- https://github.com/pyload/pyload/blob/8e447958b8a66c5899775e725a8b90bce6643004/src/pyload/webui/app/blueprints/api_blueprint.py#L73
- https://github.com/pyload/pyload/commit/461cd66f30fa9e96453fb4d8c5c47467e452363c
- https://github.com/pyload/pyload/security/advisories/GHSA-vq8p-m3wm-gv5f

### [CVE-2026-108258](https://github.com/posit-dev/py-shiny/commit/1d8ecb46cbc9621b7dc8812111d26692e086b376)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-108258
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-10 06:17:03 JST
- 更新日: 2026-10-10 06:17:03 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Shiny for Python 1.4.0 から 1.6.4 未満におけるパス検証不備。ブックマーク復元時の state_id に対する適切なパス制限が行われていません。
- 影響: 未認証の攻撃者がディレクトリトラバーサルにより範囲外の構成ファイルを読み込ませたり、設定に応じてサーバー上の指定ファイルを露出させたりする可能性があります。
- 推奨対応: Shiny for Python 1.6.4 以降へアップデートしてください。

#### References
- https://github.com/posit-dev/py-shiny/commit/1d8ecb46cbc9621b7dc8812111d26692e086b376
- https://github.com/posit-dev/py-shiny/releases/tag/v1.6.4
- https://github.com/posit-dev/py-shiny/security/advisories/GHSA-47c3-hpmg-7j6p

### [CVE-2026-105278](https://github.com/cisagov/CSAF/blob/develop/csaf_files/OT/white/2026/icsa-26-281-02.json)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-105278
- 関連キーワード: docker
- 影響製品: -
- 公開日: 2026-10-10 00:17:08 JST
- 更新日: 2026-10-10 01:41:53 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openPDC の公開 Docker イメージにおける固定管理者資格情報の存在。初回使用時の強制変更が組み込まれていません。
- 影響: 管理インターフェースにネットワークアクセス可能な攻撃者が、固定資格情報を用いて認証し、完全な管理者権限を奪取する可能性があります。
- 推奨対応: 固定資格情報の変更および対策済みのイメージ・設定へ更新してください。

#### References
- https://github.com/cisagov/CSAF/blob/develop/csaf_files/OT/white/2026/icsa-26-281-02.json
- https://www.cisa.gov/news-events/ics-advisories/icsa-26-281-02

### [CVE-2026-108156](https://github.com/netease-youdao/LobsterAI)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-108156
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-10-10 02:16:46 JST
- 更新日: 2026-10-10 02:41:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: LobsterAI 2026.5.27 ～ 2026.9.23 におけるパス制御不備。skills:delete IPC ハンドラーがアンインストール時に _meta.json 内の openclawSourceDir を不当に信頼します。
- 影響: 細工されたスキルを導入させられた場合、アンインストール時にホームディレクトリなど書き込み可能な任意のディレクトリが再帰的に削除される可能性があります。
- 推奨対応: 修正されたバージョンへアップデートし、信頼できないスキルの導入を避けてください。

#### References
- https://github.com/netease-youdao/LobsterAI
- https://github.com/netease-youdao/LobsterAI/blob/791a352dee3b3d8c6f64edcaf229ce474a68f6c5/src/main/ipcHandlers/skills/handlers.ts#L60-L78
- https://github.com/netease-youdao/LobsterAI/commit/82fdfe10d1b85d0ff734aa720e18c866b4be2406
- https://github.com/netease-youdao/LobsterAI/issues/2793
- https://www.vulncheck.com/advisories/lobsterai-2026.5.27-through-2026.9.23-arbitrary-directory-deletion-via-skill-meta-json

### [CVE-2026-107783](https://aws.amazon.com/security/security-bulletins/2026-132-aws/)

> **Backend** / **MEDIUM** / CVSS: **6.7** / KEV: **no**

- タイトル: CVE-2026-107783
- 関連キーワード: aws
- 影響製品: -
- 公開日: 2026-10-10 01:17:24 JST
- 更新日: 2026-10-10 03:17:02 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AWS Tools for PowerShell 5.0.306 未満におけるログへの機密情報記録。コマンド出力やログに平文パスワードが含まれる場合があります。
- 影響: ローカルユーザーがトランスクリプトやログから IAM ユーザーの AWS 管理コンソール用平文パスワードを取得できる可能性があります。
- 推奨対応: 5.0.306 以降へアップデートし、既存のログを確認して影響を受ける IAM パスワードをローテーションしてください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-132-aws/
- https://github.com/aws/aws-tools-for-powershell/releases/tag/5.0.306
- https://github.com/aws/aws-tools-for-powershell/security/advisories/GHSA-q3x5-q6rm-c7p3

### [CVE-2026-107815](https://github.com/MariaDB/server/commit/b369925f6855d3e1f0ebcf453492724b99fda6f8)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-107815
- 関連キーワード: gin, mysql
- 影響製品: -
- 公開日: 2026-10-10 02:16:45 JST
- 更新日: 2026-10-10 02:41:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: MariaDB Server の CONNECT エンジン（DOS テーブルタイプ）における境界チェック不備。スタックバッファ外への 1 バイト Null 書き込みが発生します。
- 影響: CONNECT エンジンを利用可能な認証済みユーザーにより、データベースのクラッシュや任意のコード実行を引き起こされる可能性があります。
- 推奨対応: 修正済みのバージョン（10.6.28、10.11.19、11.4.13、11.8.9、12.3.3、13.0.2 以降）へアップデートしてください。

#### References
- https://github.com/MariaDB/server/commit/b369925f6855d3e1f0ebcf453492724b99fda6f8
- https://github.com/MariaDB/server/releases/tag/mariadb-10.11.19
- https://github.com/MariaDB/server/releases/tag/mariadb-10.6.28
- https://github.com/MariaDB/server/releases/tag/mariadb-11.4.13
- https://github.com/MariaDB/server/releases/tag/mariadb-11.8.9

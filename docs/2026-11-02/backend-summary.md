# Backend CVE Summary (2026-11-02)

## Overview

- 取得日時: 2026-11-02 10:28:26 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 9
- Critical: 0
- High: 2
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-84177](https://lists.apache.org/thread.html/hy089v60t5v36skpnbry96vr2427lw0o)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-84177
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-11-02 08:17:30 JST
- 更新日: 2026-11-02 08:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache Wicket の PackageResource におけるファイルパス検証と属性付与の実行順序の不備。
- 影響: リソースガードによる検証後に属性が付加されることで、ガードで検証・承認されていないファイルが読み込まれる可能性がある。
- 推奨対応: 検証ロジックが修復された修正版 Apache Wicket にアップデートする。

#### References
- https://lists.apache.org/thread.html/hy089v60t5v36skpnbry96vr2427lw0o

### [CVE-2026-74759](https://metacpan.org/release/CJCOLLIER/Google-Auth-0.12/source/lib/Google/Auth/ExternalAccountCredentials/Aws.pm)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74759
- 関連キーワード: go, aws
- 影響製品: -
- 公開日: 2026-11-02 02:16:34 JST
- 更新日: 2026-11-02 02:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Perl向けGoogle::Auth（v0.12）における、未検証のcredential_source URLに起因するSSRF（サーバーサイドリクエストフォージェリ）の脆弱性。
- 影響: 信頼できない設定ファイルを読み込んだ場合、内部サービスやメタデータエンドポイントに対して不正なGET/PUTリクエストが送信される可能性がある。
- 推奨対応: ライブラリを対策済みバージョンへアップデートし、外部設定ファイルの信頼性を検証してください。

#### References
- https://metacpan.org/release/CJCOLLIER/Google-Auth-0.12/source/lib/Google/Auth/ExternalAccountCredentials/Aws.pm

### [CVE-2026-82115](https://lists.apache.org/thread.html/0lj9og7vp22ps77nrwdj42f64cfb9g4c)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-82115
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-02 07:17:46 JST
- 更新日: 2026-11-02 07:17:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache WicketのWebSocket通信処理において認可検証がスキップされ、設定された認可ルールが適用されない脆弱性。
- 影響: 攻撃者がセッション情報とリソース名を知ることで、本来アクセスが制限されているリソースを直接呼び出せる可能性がある。
- 推奨対応: 修正パッチの適用や、WebSocket経由のハンドラに対する適切な認可ロジックの導入を検討してください。

#### References
- https://lists.apache.org/thread.html/0lj9og7vp22ps77nrwdj42f64cfb9g4c

### [CVE-2026-82559](https://lists.apache.org/thread.html/5vkw9wz6gf135ccosj928zjs4hqy7bcv)

> **Backend** / **LOW** / CVSS: **2.3** / KEV: **no**

- タイトル: CVE-2026-82559
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-11-02 07:17:47 JST
- 更新日: 2026-11-02 07:17:47 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache WicketのWebSocket処理において、接続初期化時のセッションコピーが保持され続け、セッション失効が反映されない脆弱性。
- 影響: セッションが本来失効した後もWebSocket接続が維持され、古いセッション情報のままアクセスが継続される可能性がある。
- 推奨対応: 最新バージョンへアップデートし、WebSocket接続時のセッションライフサイクル管理を見直してください。

#### References
- https://lists.apache.org/thread.html/5vkw9wz6gf135ccosj928zjs4hqy7bcv

### [CVE-2026-74760](https://metacpan.org/release/CJCOLLIER/Google-Auth-0.12/source/bin/gcloud-auth.pl)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-74760
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-11-02 02:16:34 JST
- 更新日: 2026-11-02 02:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Perl向けGoogle::Auth（v0.11～0.12）のコールバック処理において、OAuthのstateパラメータが検証されない脆弱性。
- 影響: ローカルの攻撃者が自身のGoogleアカウントの認可コードを送信することで、被害者のツール権限を攻撃者のアカウントへ差し替える可能性がある。
- 推奨対応: 対策済みバージョンへの更新を行い、OAuth認証フローでのstate検証が機能しているか確認してください。

#### References
- https://metacpan.org/release/CJCOLLIER/Google-Auth-0.12/source/bin/gcloud-auth.pl

### [CVE-2026-83539](https://lists.apache.org/thread.html/xqdymd8g178sc112lmqbp53zlss53cwz)

> **Backend** / **HIGH** / CVSS: **7.4** / KEV: **no**

- タイトル: CVE-2026-83539
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-11-02 08:17:29 JST
- 更新日: 2026-11-02 08:17:29 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache WicketのSmartLinkLabel等において、URLの自動リンク化処理時にスキームの検証が行われないことによるXSSの脆弱性。
- 影響: 悪意あるスキーム（javascript:等）を含むテキストが処理された場合、リンクをクリックしたユーザーのセッション内で任意のスクリプトが実行される可能性がある。
- 推奨対応: 修正バージョンへアップデートするか、入力値および自動生成されるリンクのスキーム検証・サニタイズを行ってください。

#### References
- https://lists.apache.org/thread.html/xqdymd8g178sc112lmqbp53zlss53cwz

### [CVE-2026-82840](https://lists.apache.org/thread.html/q812kjb74x2pt6956w0pcmkc4wwj95l9)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-82840
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-11-02 07:17:48 JST
- 更新日: 2026-11-02 07:17:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache WicketのAuthenticatedWebSessionにおいて、既認証セッションの再認証時にセッションIDが更新されないセッション固定化の脆弱性。
- 影響: 攻撃者にセッションIDを固定された場合、再認証後も同一IDが使用されセッションを乗っ取られる可能性がある。
- 推奨対応: 再認証時にも確実にchangeSessionId()が呼び出されるよう実装を修正するか、修正版バージョンを適用してください。

#### References
- https://lists.apache.org/thread.html/q812kjb74x2pt6956w0pcmkc4wwj95l9

### [CVE-2026-82898](https://lists.apache.org/thread.html/bm4mlwsgftxfg345zvdqj0skg1mktpyp)

> **Backend** / **LOW** / CVSS: **2.1** / KEV: **no**

- タイトル: CVE-2026-82898
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-11-02 07:17:48 JST
- 更新日: 2026-11-02 07:17:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache WicketのResourceIsolationRequestCycleListenerにおいて、セキュリティチェックの実行順序不備によりオリジン分離が不十分となる脆弱性。
- 影響: 未認証アクセス時の例外処理に伴い分離ポリシーの検証がスキップされ、他オリジンからの不正なアクセスを拒否できない可能性がある。
- 推奨対応: 修正されたバージョンへ更新し、例外発生時にもセキュリティポリシーが適切に評価されるよう構成を確認してください。

#### References
- https://lists.apache.org/thread.html/bm4mlwsgftxfg345zvdqj0skg1mktpyp

### [CVE-2026-84172](https://lists.apache.org/thread.html/90mlx42q7nkdccdby1ql1ksl4sxy13x6)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-84172
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-11-02 08:17:30 JST
- 更新日: 2026-11-02 08:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Apache WicketのPackageResourceGuardにおいて、クラスローダーの参照不整合によりファイルアクセス制限がバイパスされる脆弱性。
- 影響: 本来非公開であるべきコンポーネントのHTMLマークアップテンプレート等の内部ファイルが、外部へ配信される可能性がある。
- 推奨対応: 修正パッチを適用し、クラスパスリソースの配信保護ロジックを最新の状態に更新してください。

#### References
- https://lists.apache.org/thread.html/90mlx42q7nkdccdby1ql1ksl4sxy13x6

# Frontend CVE Summary (2026-07-21)

## Overview

- 取得日時: 2026-07-21 08:11:27 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 20
- Critical: 5
- High: 3
- KEV掲載: 0
- 日本語AI要約: GitHub Models

## CVEs

### [CVE-2026-47129](https://github.com/pdovhomilja/nextcrm-app/releases/tag/v0.12.0)

> **Frontend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-47129
- 関連キーワード: next.js
- 影響製品: -
- 公開日: 2026-07-21 06:16:47 JST
- 更新日: 2026-07-21 06:16:47 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: NextCRMの0.12.0未満のバージョンにおいて、管理者権限の確認が不十分なため、認証済みユーザーが任意のユーザーアカウントを有効化・無効化できるアクセス制御の脆弱性が存在します。  
- 影響: 低権限ユーザーでも管理者アカウントを含む任意のユーザーの状態を変更できるため、不正操作や権限昇格のリスクがあります。  
- 推奨対応: 速やかにNextCRMをバージョン0.12.0以降にアップデートし、アクセス制御の適切な検証を行うことを推奨します。

#### References
- https://github.com/pdovhomilja/nextcrm-app/releases/tag/v0.12.0
- https://github.com/pdovhomilja/nextcrm-app/security/advisories/GHSA-gm7p-f88p-vhfr

### [CVE-2026-54051](https://github.com/Jovancoding/Network-AI/commit/379f77656b578144e03415c5b134d8309a4b5792)

> **Frontend** / **CRITICAL** / CVSS: **9.9** / KEV: **no**

- タイトル: CVE-2026-54051
- 関連キーワード: typescript, npm, node.js
- 影響製品: -
- 公開日: 2026-07-21 02:17:57 JST
- 更新日: 2026-07-21 02:17:57 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Network-AIの5.9.1未満のバージョンで、シェルコマンドの許可リストが不適切に処理され、任意のコマンド実行が可能になる脆弱性が存在します。  
- 影響: 攻撃者が制限されたエージェント環境から任意のシェルコマンドを実行できる可能性があります。  
- 推奨対応: Network-AIをバージョン5.9.1以降にアップデートし、ワイルドカードを多用した許可リストの使用を避けてください。

#### References
- https://github.com/Jovancoding/Network-AI/commit/379f77656b578144e03415c5b134d8309a4b5792
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-qw6v-5fcf-5666

### [CVE-2026-58484](https://github.com/Jovancoding/Network-AI/commit/a59c13a1f0ce0e8a0779a90343eef92fac5ab4c3)

> **Frontend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-58484
- 関連キーワード: typescript, node.js
- 影響製品: -
- 公開日: 2026-07-21 02:18:16 JST
- 更新日: 2026-07-21 04:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Network-AIのv5.12.2以前のバージョンで、バックアップのマニフェストファイル内のパス情報を信頼して削除処理を行うため、悪意あるマニフェストにより任意のディレクトリを再帰的に削除される可能性があります。  
- 影響: 攻撃者が特定のマニフェストを改ざんすると、Network-AIの実行ユーザー権限で任意のファイルやディレクトリが削除されるリスクがあります。  
- 推奨対応: バージョン5.12.2以降にアップデートし、マニフェストのパス検証と削除範囲制限の修正を適用してください。

#### References
- https://github.com/Jovancoding/Network-AI/commit/a59c13a1f0ce0e8a0779a90343eef92fac5ab4c3
- https://github.com/Jovancoding/Network-AI/releases/tag/v5.12.2
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-2fmp-9rvw-hc96
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-2fmp-9rvw-hc96

### [CVE-2026-46701](https://github.com/Jovancoding/Network-AI/commit/dc5048112283f3f4eb6c06dd2bf5aa93ef9339be)

> **Frontend** / **HIGH** / CVSS: **7.6** / KEV: **no**

- タイトル: CVE-2026-46701
- 関連キーワード: typescript, gin, node.js
- 影響製品: -
- 公開日: 2026-07-21 02:17:09 JST
- 更新日: 2026-07-21 04:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Network-AIのMCP SSEサーバーがデフォルトで空のシークレットを使用しており、認証なしで全リクエストを許可してしまう脆弱性です。  
- 影響: 攻撃者はクロスオリジンのブラウザ経由で22のMCPツールを不正に操作でき、ローカルホストのサーバーに対して任意のコマンドを実行される可能性があります。  
- 推奨対応: バージョン5.4.5以降にアップデートし、適切なシークレット設定を行うことで問題を解消してください。

#### References
- https://github.com/Jovancoding/Network-AI/commit/dc5048112283f3f4eb6c06dd2bf5aa93ef9339be
- https://github.com/Jovancoding/Network-AI/releases/tag/v5.4.5
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-j3vx-cx2r-pvg8

### [CVE-2026-58482](https://github.com/Jovancoding/Network-AI/commit/a59c13a1f0ce0e8a0779a90343eef92fac5ab4c3)

> **Frontend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-58482
- 関連キーワード: typescript, gin, node.js
- 影響製品: -
- 公開日: 2026-07-21 02:18:15 JST
- 更新日: 2026-07-21 03:16:55 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Network-AIのApprovalInbox機能に認証なしでアクセス可能な脆弱性があり、悪意ある第三者が保留中の承認を列挙・承認できる問題です。  
- 影響: 人間の承認を必要とする高リスク操作が利用者の同意なく実行される恐れがあります。  
- 推奨対応: バージョン5.12.2以降にアップデートし、ApprovalInboxの`secret`オプションを設定して認証を有効にしてください。

#### References
- https://github.com/Jovancoding/Network-AI/commit/a59c13a1f0ce0e8a0779a90343eef92fac5ab4c3
- https://github.com/Jovancoding/Network-AI/releases/tag/v5.12.2
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-mxjx-28vx-xjjj
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-mxjx-28vx-xjjj

### [CVE-2026-58413](https://github.com/Jovancoding/Network-AI/commit/a59c13a1f0ce0e8a0779a90343eef92fac5ab4c3)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-58413
- 関連キーワード: typescript, node.js
- 影響製品: -
- 公開日: 2026-07-21 02:18:15 JST
- 更新日: 2026-07-21 03:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Network-AIの`EnvironmentManager.restore`メソッドにおいて、バックアップIDの検証不足によりディレクトリトラバーサルが可能な脆弱性が存在しました。  
- 影響: 悪意あるバックアップIDを使うことで、任意のディレクトリからファイルを復元先にコピーされる恐れがあります。  
- 推奨対応: バージョン5.12.2以降にアップデートし、バックアップIDの検証が適切に行われることを確認してください。

#### References
- https://github.com/Jovancoding/Network-AI/commit/a59c13a1f0ce0e8a0779a90343eef92fac5ab4c3
- https://github.com/Jovancoding/Network-AI/releases/tag/v5.12.2
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-48x2-6pr9-2jjf
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-48x2-6pr9-2jjf

### [CVE-2026-58414](https://github.com/Jovancoding/Network-AI/commit/a59c13a1f0ce0e8a0779a90343eef92fac5ab4c3)

> **Frontend** / **MEDIUM** / CVSS: **5.5** / KEV: **no**

- タイトル: CVE-2026-58414
- 関連キーワード: typescript, node.js
- 影響製品: -
- 公開日: 2026-07-21 02:18:15 JST
- 更新日: 2026-07-21 04:17:26 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Network-AIの5.12.2未満のバージョンで、バックアップ処理がシンボリックリンクを辿り外部ファイルをコピーしてしまう問題が存在します。  
- 影響: 攻撃者が環境データディレクトリにシンボリックリンクを設置すると、環境外のファイルがバックアップに含まれ情報漏洩の可能性があります。  
- 推奨対応: バージョン5.12.2以降にアップデートし、バックアップ処理がシンボリックリンクを辿らないようにすることを推奨します。

#### References
- https://github.com/Jovancoding/Network-AI/commit/a59c13a1f0ce0e8a0779a90343eef92fac5ab4c3
- https://github.com/Jovancoding/Network-AI/releases/tag/v5.12.2
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-6x2m-p4xp-wg22
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-6x2m-p4xp-wg22

### [CVE-2026-58481](https://github.com/Jovancoding/Network-AI/commit/a59c13a1f0ce0e8a0779a90343eef92fac5ab4c3)

> **Frontend** / **MEDIUM** / CVSS: **6.5** / KEV: **no**

- タイトル: CVE-2026-58481
- 関連キーワード: typescript, node.js
- 影響製品: -
- 公開日: 2026-07-21 02:18:15 JST
- 更新日: 2026-07-21 03:16:54 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Network-AIのAgentRuntimeで、サンドボックスのパス検証が不十分なため、隣接するディレクトリのファイルにアクセスできる問題がありました。  
- 影響: 悪意のあるエージェントやユーザーがサンドボックス外のファイルを読み取ったり一覧表示したりできる可能性があります。  
- 推奨対応: バージョン5.12.2以降にアップデートし、パス検証の改善を適用してください。

#### References
- https://github.com/Jovancoding/Network-AI/commit/a59c13a1f0ce0e8a0779a90343eef92fac5ab4c3
- https://github.com/Jovancoding/Network-AI/releases/tag/v5.12.2
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-jvcm-f35g-w78p
- https://github.com/Jovancoding/Network-AI/security/advisories/GHSA-jvcm-f35g-w78p

### [CVE-2026-46412](https://github.com/BeProduct/beproduct-org-nestjs-auth/security/advisories/GHSA-6xwp-cp5h-q856)

> **Frontend** / **CRITICAL** / CVSS: **10.0** / KEV: **no**

- タイトル: CVE-2026-46412
- 関連キーワード: npm, gin, nestjs, aws
- 影響製品: -
- 公開日: 2026-07-21 01:17:01 JST
- 更新日: 2026-07-21 01:17:01 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: @beproduct/nestjs-authのバージョン0.1.2から0.1.19に悪意あるコードが含まれ、npmトークンやGitHubトークン、AWS認証情報などの秘密情報が盗まれる可能性があります。  
- 影響: 悪意あるバージョンをインストールした環境の認証情報漏洩やシステム侵害のリスクが高いです。  
- 推奨対応: 影響バージョンのパッケージを削除しクリーンな0.1.20に更新、全ての認証情報をローテーションし、感染の有無を確認して必要に応じて再イメージを行ってください。

#### References
- https://github.com/BeProduct/beproduct-org-nestjs-auth/security/advisories/GHSA-6xwp-cp5h-q856
- https://www.aikido.dev/blog/checklist-github-actions
- https://www.aikido.dev/blog/mini-shai-hulud-is-back-tanstack-compromised

### [CVE-2026-53595](https://github.com/freescout-help-desk/freescout/security/advisories/GHSA-jqj5-r72v-v29g)

> **Frontend** / **CRITICAL** / CVSS: **9.4** / KEV: **no**

- タイトル: CVE-2026-53595
- 関連キーワード: vite, mysql
- 影響製品: -
- 公開日: 2026-07-21 06:16:48 JST
- 更新日: 2026-07-21 06:16:48 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: FreeScoutの1.8.224以前のバージョンにおいて、認証なしで特定のエンドポイントを通じて最初に有効化されたアカウントのメールアドレスとパスワードを上書きし、不正ログインが可能な脆弱性が存在します。  
- 影響: 攻撃者は匿名で管理者権限を含むアカウントに不正アクセスできるため、システムの完全な制御を奪われる恐れがあります。  
- 推奨対応: 速やかにFreeScoutをバージョン1.8.224以降にアップデートし、該当エンドポイントの利用を制限してください。

#### References
- https://github.com/freescout-help-desk/freescout/security/advisories/GHSA-jqj5-r72v-v29g

### [CVE-2026-35198](https://github.com/heyform/heyform/commit/cc97d27a57ae400fec23abf5dcf6f9533c3b5db3)

> **Frontend** / **CRITICAL** / CVSS: **9.0** / KEV: **no**

- タイトル: CVE-2026-35198
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-21 01:16:58 JST
- 更新日: 2026-07-21 04:17:21 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: HeyFormの3.0.0-rc.7以前のバージョンに、低権限のチームメンバーが悪意あるJavaScriptを注入できる保存型XSS脆弱性があります。  
- 影響: チームオーナーがフォームを閲覧するとスクリプトが実行され、権限昇格によるアカウント完全乗っ取りの可能性があります。  
- 推奨対応: 速やかにバージョン3.0.0-rc.7以降にアップデートし、脆弱性を修正してください。

#### References
- https://github.com/heyform/heyform/commit/cc97d27a57ae400fec23abf5dcf6f9533c3b5db3
- https://github.com/heyform/heyform/security/advisories/GHSA-chmm-jqpm-3pwx
- https://github.com/heyform/heyform/security/advisories/GHSA-chmm-jqpm-3pwx

### [CVE-2026-39878](https://github.com/chamilo/chamilo-lms/security/advisories/GHSA-gcjp-f7jm-rrrg)

> **Frontend** / **CRITICAL** / CVSS: **9.3** / KEV: **no**

- タイトル: CVE-2026-39878
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-21 03:16:51 JST
- 更新日: 2026-07-21 04:17:22 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Chamilo LMS 1.11.38以前のバージョンに、ユーザー登録フォームでの保存型クロスサイトスクリプティング脆弱性が存在し、未認証の攻撃者が管理者のブラウザで任意のJavaScriptを実行可能です。  
- 影響: 管理者アカウントの完全な乗っ取りにつながる恐れがあり、プラットフォーム全体の制御が奪われる可能性があります。  
- 推奨対応: Chamilo LMSをバージョン1.11.40以降にアップデートし、脆弱性の修正を適用してください。

#### References
- https://github.com/chamilo/chamilo-lms/security/advisories/GHSA-gcjp-f7jm-rrrg

### [CVE-2026-44227](https://github.com/bestpractical/rt/releases/tag/rt-6.0.3)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-44227
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-21 03:16:52 JST
- 更新日: 2026-07-21 04:17:22 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: RTのバージョン6.0.0から6.0.2に反射型クロスサイトスクリプティング（XSS）の脆弱性が存在します。  
- 影響: 認証済みユーザーが細工されたURLを開くと、任意のJavaScriptが実行される可能性があります。  
- 推奨対応: バージョン6.0.3以降にアップデートし、不審なRTのURLを開かないよう注意してください。

#### References
- https://github.com/bestpractical/rt/releases/tag/rt-6.0.3
- https://github.com/bestpractical/rt/security/advisories/GHSA-7742-fhq7-ggv9

### [CVE-2026-44228](https://github.com/bestpractical/rt/releases/tag/rt-6.0.3)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-44228
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-21 03:16:52 JST
- 更新日: 2026-07-21 03:16:52 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: RTのバージョン6.0.0から6.0.2において、認証ユーザーが保存型クロスサイトスクリプティング（XSS）を引き起こす可能性があります。  
- 影響: 悪意のあるJavaScriptが他のユーザーのブラウザで実行され、情報漏洩やセッション乗っ取りのリスクがあります。  
- 推奨対応: バージョン6.0.3以降にアップデートし、適切なHTMLエスケープが適用された状態にすることを推奨します。

#### References
- https://github.com/bestpractical/rt/releases/tag/rt-6.0.3
- https://github.com/bestpractical/rt/security/advisories/GHSA-pfgp-5j8g-phgc

### [CVE-2026-44229](https://github.com/bestpractical/rt/releases/tag/rt-6.0.3)

> **Frontend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-44229
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-21 05:16:43 JST
- 更新日: 2026-07-21 05:16:43 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: RTのバージョン5.0.0および6.0.0以上（5.0.10および6.0.3未満）において、アップロードされたコンテンツが添付ファイルとしてではなくインラインで表示されることで、クロスサイトスクリプティング（XSS）脆弱性が存在します。  
- 影響: 認証済みユーザーが悪意のあるJavaScriptをアップロードすると、他のRTユーザーのブラウザでスクリプトが実行される可能性があります。  
- 推奨対応: バージョン5.0.10または6.0.3以降にアップデートし、脆弱性を修正してください。

#### References
- https://github.com/bestpractical/rt/releases/tag/rt-6.0.3
- https://github.com/bestpractical/rt/security/advisories/GHSA-x576-pvwp-c2qv

### [CVE-2026-44230](https://github.com/bestpractical/rt/releases/tag/rt-6.0.3)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-44230
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-21 05:16:43 JST
- 更新日: 2026-07-21 07:17:13 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: RTのバージョン5.0.4～5.0.9および6.0.0～6.0.2において、認証済みユーザーが細工されたURLを訪問すると任意のJavaScriptが実行される反射型XSS脆弱性が存在します。  
- 影響: 攻撃者がユーザーのブラウザセッション内でスクリプトを実行できる可能性があり、情報漏洩やセッション乗っ取りのリスクがあります。  
- 推奨対応: 影響を受けるバージョンから5.0.10または6.0.3以降にアップデートし、細工されたURLのアクセスを避けることを推奨します。

#### References
- https://github.com/bestpractical/rt/releases/tag/rt-6.0.3
- https://github.com/bestpractical/rt/security/advisories/GHSA-p724-v26h-32g9

### [CVE-2026-32822](https://github.com/datacycle-engine/dataCycle-CORE/security/advisories/GHSA-q6x5-wcg6-v4gw)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-32822
- 関連キーワード: javascript, gin
- 影響製品: -
- 公開日: 2026-07-21 01:16:58 JST
- 更新日: 2026-07-21 03:16:51 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: dataCycle-COREのバージョン25.07.3以前において、認証なしの攻撃者が任意のHTMLをフラッシュ通知に挿入し、DOMに反映させることで反射型DOMベースのXSSが発生します。  
- 影響: 公開ルートの任意のページで悪意あるスクリプトが実行される可能性があり、ユーザーのセッション情報や操作に影響を与える恐れがあります。  
- 推奨対応: 影響を受けるバージョンからのアップデートや、フロントエンドでのHTMLエスケープ処理の強化を検討してください。

#### References
- https://github.com/datacycle-engine/dataCycle-CORE/security/advisories/GHSA-q6x5-wcg6-v4gw

### [CVE-2026-26483](https://gist.github.com/WinBlah12/8dbc1eae788945c6ea6ab1a2cdfd7cb1)

> **Frontend** / **MEDIUM** / CVSS: **6.1** / KEV: **no**

- タイトル: CVE-2026-26483
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-21 03:16:50 JST
- 更新日: 2026-07-21 04:17:20 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Mettle SendPortal 3.0.1以前のテンプレート管理機能において、contentパラメータの入力が適切にサニタイズされず、永続的なクロスサイトスクリプティング（XSS）が発生する可能性があります。  
- 影響: 悪意あるスクリプトがユーザーのブラウザで実行され、情報漏洩やセッションハイジャックのリスクが考えられます。  
- 推奨対応: 最新バージョンへのアップデートや、contentパラメータの入力値検証・サニタイズ強化を検討してください。

#### References
- https://gist.github.com/WinBlah12/8dbc1eae788945c6ea6ab1a2cdfd7cb1
- https://github.com/mettle/sendportal

### [CVE-2026-59238](https://github.com/maalfer/pentestify/commit/a058a22b42c6311895622645265df79a60265b1d)

> **Frontend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-59238
- 関連キーワード: javascript, go
- 影響製品: -
- 公開日: 2026-07-21 00:16:44 JST
- 更新日: 2026-07-21 01:17:06 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: maalfer Pentestify 1.1.0未満のクライアント側レポートレンダリング機能において、保存型クロスサイトスクリプティングの脆弱性が存在します。  
- 影響: 認証済みのリモート攻撃者が悪意あるJavaScriptを任意のユーザーのブラウザで実行できる可能性があります。  
- 推奨対応: 可能な限り早急にソフトウェアを1.1.0以降のバージョンにアップデートし、入力値の適切なエスケープを確認してください。

#### References
- https://github.com/maalfer/pentestify/commit/a058a22b42c6311895622645265df79a60265b1d
- https://secur0.com/en/cna/cve-list/cve-2026-59238-stored-xss-in-pentestify-via-unsanitized-finding-images-and-report-client-logo

### [CVE-2026-46516](https://github.com/mwtcmi/frogman/commit/f0d2ba1785abb31b7d5debeae526f9e36962b55e)

> **Frontend** / **MEDIUM** / CVSS: **4.8** / KEV: **no**

- タイトル: CVE-2026-46516
- 関連キーワード: javascript
- 影響製品: -
- 公開日: 2026-07-21 00:16:38 JST
- 更新日: 2026-07-21 04:17:23 JST
- 出典: NVD

#### GitHub Models要約

- 日本語要約: Frogmanの1.6.6未満のバージョンで、チャットコンソールのMarkdownフォーマッタが正規表現のキャプチャグループを生のHTMLとして挿入し、管理者が悪意あるスクリプトを実行される可能性があります。  
- 影響: 管理者が他の管理者のセッション権限で任意のJavaScriptを実行されるリスクがあります。  
- 推奨対応: Frogmanをバージョン1.6.6以降にアップデートし、Markdownフォーマッタの脆弱性を修正してください。

#### References
- https://github.com/mwtcmi/frogman/commit/f0d2ba1785abb31b7d5debeae526f9e36962b55e
- https://github.com/mwtcmi/frogman/security/advisories/GHSA-7qvv-vgw9-rcxg

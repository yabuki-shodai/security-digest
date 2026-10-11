# Backend CVE Summary (2026-10-11)

## Overview

- 取得日時: 2026-10-11 09:55:16 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 21
- Critical: 4
- High: 4
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-108549](https://github.com/chenhg5/cc-connect)

> **Backend** / **CRITICAL** / CVSS: **9.2** / KEV: **no**

- タイトル: CVE-2026-108549
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-11 00:16:57 JST
- 更新日: 2026-10-11 00:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: cc-connect (1.5.0以下) のMAXプラットフォームアダプターにおいて、webhook_secret未設定時に認証検証が欠落する脆弱性が存在します。
- 影響: 未認証の攻撃者が特権ユーザーのIDを偽造してリクエストを送信し、ホスト上で特権コマンド（/shellなど）を実行する可能性があります。
- 推奨対応: webhook_secret を適切に設定するか、修正版のソフトウェアへアップデートしてください。

#### References
- https://github.com/chenhg5/cc-connect
- https://github.com/chenhg5/cc-connect/blob/v1.5.0/platform/max/max.go#L287-L305
- https://github.com/chenhg5/cc-connect/issues/1968
- https://www.vulncheck.com/advisories/cc-connect-through-1.5.0-missing-authentication-via-max-webhook-sender-spoofing

### [CVE-2026-62124](https://patchstack.com/database/wordpress/theme/n7-golf-club/vulnerability/wordpress-n7-golf-club-sports-events-theme-2-21-php-object-injection-vulnerability?_s_id=cve)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-62124
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-11 05:16:44 JST
- 更新日: 2026-10-11 05:16:44 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用プラグイン N7 | Golf Club Sports & Events (2.21以下) に未認証で利用可能なPHPオブジェクトインジェクションの脆弱性が存在します。
- 影響: 認証なしの第三者により、任意のコード実行やデータの改ざん・不正アクセスが行われる可能性があります。
- 推奨対応: プラグインを最新の修正済みバージョンに更新してください。

#### References
- https://patchstack.com/database/wordpress/theme/n7-golf-club/vulnerability/wordpress-n7-golf-club-sports-events-theme-2-21-php-object-injection-vulnerability?_s_id=cve

### [CVE-2026-108585](https://github.com/argoproj-labs/mcp-for-argocd)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-108585
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-10-11 02:17:00 JST
- 更新日: 2026-10-11 02:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: argocd-mcp (0.9.0以下) の delete_application ツールにおいて、パラメータ検証の不備に起因するパストラバーサルの脆弱性が存在します。
- 影響: RBAC権限の範囲内で、意図しないリポジトリやクラスタ、プロジェクトなどが削除される可能性があります。
- 推奨対応: argocd-mcp を修正済みバージョンに更新してください。

#### References
- https://github.com/argoproj-labs/mcp-for-argocd
- https://github.com/argoproj-labs/mcp-for-argocd/blob/28d15ca69b0c31387cc6ec73d201fd13c5d22b6a/src/argocd/client.ts#L115-L139
- https://github.com/argoproj-labs/mcp-for-argocd/blob/28d15ca69b0c31387cc6ec73d201fd13c5d22b6a/src/argocd/http.ts#L86-L91
- https://hackmd.io/@haind/argocd-mcp-delete-application-route-smuggling
- https://www.vulncheck.com/advisories/argocd-mcp-through-0.9.0-path-traversal-via-delete-application-tool

### [CVE-2026-108597](https://github.com/cohere-ai/cohere-python)

> **Backend** / **MEDIUM** / CVSS: **5.9** / KEV: **no**

- タイトル: CVE-2026-108597
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-10-11 04:16:58 JST
- 更新日: 2026-10-11 04:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Cohere Python SDK (5.11.0～7.2.0) の解凍処理において、検証不備に起因するパストラバーサル (Tar Slip) の脆弱性が存在します。
- 影響: 悪意あるモデルアーカイブを読み込ませることで、SDK実行環境上の任意のファイルが上書きされる可能性があります。
- 推奨対応: Cohere Python SDK を修正済みバージョンへアップデートしてください。

#### References
- https://github.com/cohere-ai/cohere-python
- https://github.com/cohere-ai/cohere-python/blob/0eacfe77e1710322b355928574cfec18f6791c42/src/cohere/manually_maintained/cohere_aws/client.py#L101-L123
- https://hackmd.io/@haind/cohere-python-sagemaker-s3-archive-path-traversal
- https://www.vulncheck.com/advisories/cohere-python-sdk-5.11.0-through-7.2.0-path-traversal-via-sagemaker-tar-extraction

### [CVE-2026-62035](https://patchstack.com/database/wordpress/plugin/upcasted-s3-offload/vulnerability/wordpress-aws-s3-for-wordpress-plugin-upcasted-plugin-3-1-0-broken-access-control-vulnerability?_s_id=cve)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-62035
- 関連キーワード: gin, aws
- 影響製品: -
- 公開日: 2026-10-11 05:16:39 JST
- 更新日: 2026-10-11 05:16:39 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AWS S3 for WordPress Plugin – Upcasted (3.1.0以下) にアクセス制御の不備 (Broken Access Control) が存在します。
- 影響: 購読者 (Subscriber) 権限のユーザーが、本来アクセス権のない機能やデータへ不当にアクセスできる可能性があります。
- 推奨対応: プラグインを最新の修正済みバージョンへアップデートしてください。

#### References
- https://patchstack.com/database/wordpress/plugin/upcasted-s3-offload/vulnerability/wordpress-aws-s3-for-wordpress-plugin-upcasted-plugin-3-1-0-broken-access-control-vulnerability?_s_id=cve

### [CVE-2026-108604](https://github.com/TabularisDB/tabularis)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-108604
- 関連キーワード: postgresql
- 影響製品: -
- 公開日: 2026-10-11 05:16:32 JST
- 更新日: 2026-10-11 05:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Tabularis (0.27.0以下) の MCP run_query における安全ゲートで、認可制御が適切に行われない脆弱性が存在します。
- 影響: 読み取り専用モードを迂回され、管理者承認なしでデータベース内のデータ変更や削除が実行される可能性があります。
- 推奨対応: Tabularis を修正版へ更新し、クエリフィルタリングの設定を確認・強化してください。

#### References
- https://github.com/TabularisDB/tabularis
- https://github.com/TabularisDB/tabularis/blob/804c4c3bb6fd8eaa2e36cbe49f6c0d58f373b5e9/src-tauri/src/ai_activity.rs#L357-L416
- https://github.com/TabularisDB/tabularis/blob/804c4c3bb6fd8eaa2e36cbe49f6c0d58f373b5e9/src-tauri/src/mcp/mod.rs#L1136-L1171
- https://hackmd.io/@haind/S1BofaIsMx
- https://www.vulncheck.com/advisories/tabularis-through-0.27.0-read-only-bypass-via-mcp-run-query-select-classification

### [CVE-2026-108605](https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_ocr_record_edit.py)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-108605
- 関連キーワード: redis
- 影響製品: -
- 公開日: 2026-10-11 07:16:34 JST
- 更新日: 2026-10-11 07:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JeecgBoot (3.9.5以下) の AiOcrController updateById ハンドラーにおいて、認可チェックが欠落している脆弱性が存在します。
- 影響: 認証済みの攻撃者が共有OCRテンプレートを改ざんし、全ユーザーのOCR処理結果を不当に変更・破壊する可能性があります。
- 推奨対応: JeecgBoot を修正済みバージョンに更新し、テンプレート編集権限の検証を有効化してください。

#### References
- https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_ocr_record_edit.py
- https://github.com/jeecgboot/JeecgBoot/blob/e3b9dc0aefe1943d9772b026f64ed671a7c82802/jeecg-boot/jeecg-boot-module/jeecg-boot-module-airag/src/main/java/org/jeecg/modules/airag/ocr/controller/AiOcrController.java#L56-L71
- https://www.vulncheck.com/advisories/jeecgboot-through-3.9.5-missing-authorization-via-airag-ocr-edit-endpoint

### [CVE-2026-108606](https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_ocr_record_delete.py)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-108606
- 関連キーワード: redis
- 影響製品: -
- 公開日: 2026-10-11 07:16:34 JST
- 更新日: 2026-10-11 07:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JeecgBoot (3.9.5以下) の AiOcrController deleteById ハンドラーにおいて、認可チェックが欠落している脆弱性が存在します。
- 影響: 低権限の認証済みユーザーが、Redisに保存された共有OCRプロンプトレコードを任意に削除できる可能性があります。
- 推奨対応: JeecgBoot を修正済みバージョンに更新し、エンドポイントのアクセス制御を適用してください。

#### References
- https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_ocr_record_delete.py
- https://github.com/jeecgboot/JeecgBoot/blob/e3b9dc0aefe1943d9772b026f64ed671a7c82802/jeecg-boot/jeecg-boot-module/jeecg-boot-module-airag/src/main/java/org/jeecg/modules/airag/ocr/controller/AiOcrController.java#L73-L93
- https://www.vulncheck.com/advisories/jeecgboot-through-3.9.5-missing-authorization-via-airag-ocr-deletebyid

### [CVE-2026-108607](https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_video_record_delete.py)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-108607
- 関連キーワード: redis
- 影響製品: -
- 公開日: 2026-10-11 07:16:34 JST
- 更新日: 2026-10-11 07:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JeecgBoot (3.9.5以下) の動画生成記録削除エンドポイントにおいて、安全でない直接オブジェクト参照 (IDOR) の脆弱性が存在します。
- 影響: 認証済みユーザーが他のユーザーIDを指定することで、他人のAI動画生成履歴データを不正に削除できる可能性があります。
- 推奨対応: JeecgBoot を修正版に更新し、リクエスト元ユーザーと操作対象リソースの所有権検証を適切に実装してください。

#### References
- https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_video_record_delete.py
- https://github.com/jeecgboot/JeecgBoot/blob/e3b9dc0aefe1943d9772b026f64ed671a7c82802/jeecg-boot/jeecg-boot-module/jeecg-boot-module-airag/src/main/java/org/jeecg/modules/airag/video/controller/VideoGenerationController.java#L83-L90
- https://www.vulncheck.com/advisories/jeecgboot-through-3.9.5-idor-via-deletevideorecord-userid-parameter

### [CVE-2026-108608](https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_voice_record_delete.py)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-108608
- 関連キーワード: redis
- 影響製品: -
- 公開日: 2026-10-11 07:16:34 JST
- 更新日: 2026-10-11 07:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JeecgBoot（3.9.5以下）の DELETE /airag/voice/deleteVoiceRecord エンドポイントにおける安全でない直接オブジェクト参照（IDOR）の脆弱性。
- 影響: 認証された攻撃者がuserIdを差し替えることで、他のユーザーのAI音声レコード（TTS履歴）を不正に削除する可能性があります。
- 推奨対応: JeecgBootを最新バージョンへ更新し、該当エンドポイントに適切な所有権・アクセス制御チェックを実装してください。

#### References
- https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_voice_record_delete.py
- https://github.com/jeecgboot/JeecgBoot/blob/e3b9dc0aefe1943d9772b026f64ed671a7c82802/jeecg-boot/jeecg-boot-module/jeecg-boot-module-airag/src/main/java/org/jeecg/modules/airag/voice/controller/VoiceController.java#L83-L90
- https://www.vulncheck.com/advisories/jeecgboot-through-3.9.5-idor-via-deletevoicerecord-userid-parameter

### [CVE-2026-108609](https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_voice_history_read.py)

> **Backend** / **MEDIUM** / CVSS: **5.3** / KEV: **no**

- タイトル: CVE-2026-108609
- 関連キーワード: redis
- 影響製品: -
- 公開日: 2026-10-11 07:16:34 JST
- 更新日: 2026-10-11 07:16:34 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: JeecgBoot（3.9.5以下）の GET /airag/voice/listByUser エンドポイントにおける安全でない直接オブジェクト参照（IDOR）の脆弱性。
- 影響: 認証された攻撃者が他人のuserIdを指定することで、そのユーザーの入力テキスト、音声設定、タイムスタンプ、生成音声ファイルのパスなどを閲覧・取得する可能性があります。
- 推奨対応: JeecgBootを最新バージョンへ更新し、ユーザーIDに対する認可検証処理を追加してください。

#### References
- https://github.com/AnkesKasty/cve-request-poc/blob/a7b6d1423555812d8efa26c91c5d0683164b31e5/JeecgBoot/poc_airag_voice_history_read.py
- https://github.com/jeecgboot/JeecgBoot/blob/e3b9dc0aefe1943d9772b026f64ed671a7c82802/jeecg-boot/jeecg-boot-module/jeecg-boot-module-airag/src/main/java/org/jeecg/modules/airag/voice/controller/VoiceController.java#L74-L81
- https://www.vulncheck.com/advisories/jeecgboot-through-3.9.5-idor-via-airag-voice-listbyuser-userid-parameter

### [CVE-2026-108598](https://github.com/floci-io/floci)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-108598
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-11 04:16:58 JST
- 更新日: 2026-10-11 04:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Floci（1.1.0以上2.2.0未満）の VtlTemplateEngine におけるコードインジェクションの脆弱性。
- 影響: 未認証のリモート攻撃者が制限のないVelocityマッピングテンプレートを介してリフレクションを実行し、FlociのJVM上で任意のOSコマンドを実行する可能性があります。
- 推奨対応: Flociをバージョン2.2.0以降にアップデートしてください。

#### References
- https://github.com/floci-io/floci
- https://github.com/floci-io/floci/blob/560b3e4aae61cea3ac7d4d51843bdffd0e3085fd/src/main/java/io/github/hectorvent/floci/services/apigateway/VtlTemplateEngine.java#L74-L114
- https://github.com/floci-io/floci/commit/144b90e6fa861a5ac882e99a090d503da01945c4
- https://github.com/floci-io/floci/releases/tag/2.2.0
- https://github.com/floci-io/floci/security/advisories/GHSA-3p4c-wp7w-mgjx

### [CVE-2026-66568](https://patchstack.com/database/wordpress/theme/original/vulnerability/wordpress-original-theme-1-9-0-php-object-injection-vulnerability?_s_id=cve)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-66568
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-11 05:16:46 JST
- 更新日: 2026-10-11 05:16:46 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Original（1.9.0以下）における未認証のPHPオブジェクトインジェクションの脆弱性。
- 影響: 未認証の第三者によって任意のPHPオブジェクトが注入され、任意のコード実行やデータの改ざん等が行われる可能性があります。
- 推奨対応: 対象ソフトウェアを最新バージョンへアップデートしてください。

#### References
- https://patchstack.com/database/wordpress/theme/original/vulnerability/wordpress-original-theme-1-9-0-php-object-injection-vulnerability?_s_id=cve

### [CVE-2026-62093](https://patchstack.com/database/wordpress/theme/techone/vulnerability/wordpress-techone-theme-3-0-3-reflected-cross-site-scripting-xss-vulnerability?_s_id=cve)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-62093
- 関連キーワード: echo
- 影響製品: -
- 公開日: 2026-10-11 05:16:42 JST
- 更新日: 2026-10-11 05:16:42 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TechOne（3.0.3以下）における未認証のクロスサイトスクリプティング（XSS）の脆弱性。
- 影響: 未認証の攻撃者により悪意のあるスクリプトが注入され、訪問したユーザーのブラウザ上で任意のコードが実行される可能性があります。
- 推奨対応: TechOneを最新バージョンへアップデートしてください。

#### References
- https://patchstack.com/database/wordpress/theme/techone/vulnerability/wordpress-techone-theme-3-0-3-reflected-cross-site-scripting-xss-vulnerability?_s_id=cve

### [CVE-2026-108553](https://github.com/OpenRefine/OpenRefine)

> **Backend** / **HIGH** / CVSS: **7.7** / KEV: **no**

- タイトル: CVE-2026-108553
- 関連キーワード: gin, express
- 影響製品: -
- 公開日: 2026-10-11 00:16:58 JST
- 更新日: 2026-10-11 00:16:58 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: OpenRefine（3.10.1以下）の get-rows コマンドにおけるクロスサイトリクエストフォージェリ（CSRF）の脆弱性。
- 影響: 攻撃者の悪意のあるページを訪問したユーザーを介してJythonファセット式が実行され、OpenRefineユーザーの権限で任意のOSコマンドが実行される可能性があります。
- 推奨対応: OpenRefineを最新バージョンへアップデートしてください。

#### References
- https://github.com/OpenRefine/OpenRefine
- https://github.com/OpenRefine/OpenRefine/blob/bde8a36dc188f7846aeafc2910969e7d0fbc8e7c/extensions/jython/src/com/google/refine/jython/JythonEvaluable.java#L142
- https://github.com/OpenRefine/OpenRefine/blob/bde8a36dc188f7846aeafc2910969e7d0fbc8e7c/main/src/com/google/refine/commands/row/GetRowsCommand.java#L174-L186
- https://github.com/OpenRefine/OpenRefine/blob/bde8a36dc188f7846aeafc2910969e7d0fbc8e7c/modules/core/src/main/java/com/google/refine/browsing/facets/ListFacet.java#L327-L339
- https://github.com/OpenRefine/OpenRefine/issues/7999

### [CVE-2026-62044](https://patchstack.com/database/wordpress/plugin/super-video-player/vulnerability/wordpress-super-video-player-plugin-1-8-13-php-object-injection-vulnerability?_s_id=cve)

> **Backend** / **HIGH** / CVSS: **7.2** / KEV: **no**

- タイトル: CVE-2026-62044
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-11 02:17:00 JST
- 更新日: 2026-10-11 02:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: bPlugins Super Video Player（1.8.13以下）における信頼できないデータの逆シリアル化によるPHPオブジェクトインジェクションの脆弱性。
- 影響: 攻撃者が任意のオブジェクトを注入することにより、意図しないコードの実行やデータの不正操作を引き起こす可能性があります。
- 推奨対応: Super Video Playerを最新バージョンへアップデートしてください。

#### References
- https://patchstack.com/database/wordpress/plugin/super-video-player/vulnerability/wordpress-super-video-player-plugin-1-8-13-php-object-injection-vulnerability?_s_id=cve

### [CVE-2026-62094](https://patchstack.com/database/wordpress/theme/techone/vulnerability/wordpress-techone-theme-3-0-3-local-file-inclusion-vulnerability?_s_id=cve)

> **Backend** / **HIGH** / CVSS: **8.1** / KEV: **no**

- タイトル: CVE-2026-62094
- 関連キーワード: echo
- 影響製品: -
- 公開日: 2026-10-11 05:16:43 JST
- 更新日: 2026-10-11 05:16:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: TechOne（3.0.3以下）における未認証のローカルファイルインクルード（LFI）の脆弱性。
- 影響: 未認証の攻撃者がサーバー上の任意のファイルを読み取ったり、コード実行へ悪用したりする可能性があります。
- 推奨対応: TechOneを最新バージョンへアップデートしてください。

#### References
- https://patchstack.com/database/wordpress/theme/techone/vulnerability/wordpress-techone-theme-3-0-3-local-file-inclusion-vulnerability?_s_id=cve

### [CVE-2026-103685](https://patchstack.com/database/wordpress/plugin/woo-alidropship/vulnerability/wordpress-ald-dropshipping-and-fulfillment-for-aliexpress-and-woocommerce-plugin-2-2-4-broken-access-control-vulnerability?_s_id=cve)

> **Backend** / **MEDIUM** / CVSS: **4.3** / KEV: **no**

- タイトル: CVE-2026-103685
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-10-11 05:16:32 JST
- 更新日: 2026-10-11 05:16:32 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: VillaTheme ALD プラグイン（バージョン 2.2.4 以下）における認可欠如の脆弱性。
- 影響: アクセス制御の設定不備を悪用され、権限のない操作が行われる可能性があります。
- 推奨対応: プラグインを最新の修正済みバージョンへアップデートしてください。

#### References
- https://patchstack.com/database/wordpress/plugin/woo-alidropship/vulnerability/wordpress-ald-dropshipping-and-fulfillment-for-aliexpress-and-woocommerce-plugin-2-2-4-broken-access-control-vulnerability?_s_id=cve

### [CVE-2026-108580](https://github.com/phoenixthrush/AniWorld-Downloader/blob/bb13599d17937fdb4df2df699024bc233f0656f2/src/aniworld/web/auth.py#L239-L256)

> **Backend** / **MEDIUM** / CVSS: **6.9** / KEV: **no**

- タイトル: CVE-2026-108580
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-11 01:16:31 JST
- 更新日: 2026-10-11 01:16:31 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: AniWorld Downloader（5.3.0未満）のWebUI /loginPOSTハンドラにおける認証試行制限不備の脆弱性。
- 影響: 未認証の攻撃者がレスポンス時間の差異からユーザー名を列挙し、ブルートフォース攻撃によってアカウントを奪取する可能性があります。
- 推奨対応: AniWorld Downloaderをバージョン5.3.0以降にアップデートしてください。

#### References
- https://github.com/phoenixthrush/AniWorld-Downloader/blob/bb13599d17937fdb4df2df699024bc233f0656f2/src/aniworld/web/auth.py#L239-L256
- https://github.com/phoenixthrush/AniWorld-Downloader/commit/3c070bd10665377308a3092e11933681c18a5fd1
- https://github.com/phoenixthrush/AniWorld-Downloader/issues/334
- https://github.com/phoenixthrush/AniWorld-Downloader/releases/tag/v.5.3.0
- https://hackmd.io/@haind/aniworld-login-brute-force

### [CVE-2026-108586](https://github.com/1mcp-app/agent)

> **Backend** / **MEDIUM** / CVSS: **5.4** / KEV: **no**

- タイトル: CVE-2026-108586
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-10-11 02:17:00 JST
- 更新日: 2026-10-11 02:17:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: 1MCP Agent（@1mcp/agent 0.20.0〜0.39.0）における不適切な認可制御の脆弱性。
- 影響: 単一タグの権限を持つ攻撃者が否定のタグフィルター式を使用することでOAuthスコープ制限をバイパスし、スコープ外のバックエンドMCPサーバー上のツール実行等を行う可能性があります。
- 推奨対応: @1mcp/agentを修正済みの最新バージョンへアップデートしてください。

#### References
- https://github.com/1mcp-app/agent
- https://github.com/1mcp-app/agent/blob/v0.39.0/src/sdk/legacy/transport/http/middlewares/scopeAuthMiddleware.ts#L163-L183
- https://github.com/1mcp-app/agent/blob/v0.39.0/src/transport/http/routes/inspectHelpers.ts#L79-L102
- https://hackmd.io/@haind/1mcp-negated-tag-filter-oauth-scope-bypass
- https://www.vulncheck.com/advisories/1mcp-agent-0.20.0-through-0.39.0-oauth-tag-scope-bypass-via-negated-tag-filter

### [CVE-2026-108594](https://github.com/mealie-recipes/mealie)

> **Backend** / **LOW** / CVSS: **3.5** / KEV: **no**

- タイトル: CVE-2026-108594
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-10-11 04:16:57 JST
- 更新日: 2026-10-11 04:16:57 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Mealie（バージョン 3.26.0 から 3.28.0）の OIDC アバター取得処理における SSRF の脆弱性。
- 影響: 認証済みの OIDC ユーザーにより、ログイン時にプロバイダーの内部アドレスにある任意ポートへ GET リクエストが送信される可能性があります。
- 推奨対応: 修正版のバージョンへアップデートしてください。

#### References
- https://github.com/mealie-recipes/mealie
- https://github.com/mealie-recipes/mealie/blob/v3.28.0/mealie/core/security/providers/openid_provider.py#L170-L200
- https://github.com/mealie-recipes/mealie/blob/v3.28.0/mealie/pkgs/safehttp/transport.py#L60-L160
- https://hackmd.io/@haind/mealie-oidc-avatar-ssrf
- https://www.vulncheck.com/advisories/mealie-3.26.0-through-3.28.0-ssrf-via-oidc-picture-claim-avatar-fetch

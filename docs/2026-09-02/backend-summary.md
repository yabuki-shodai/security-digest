# Backend CVE Summary (2026-09-02)

## Overview

- 取得日時: 2026-09-02 09:04:07 JST
- 対象: 今日公開されたCVE / 今日CISA KEVに追加されたCVEのみ
- 掲載件数: 14
- Critical: 1
- High: 9
- KEV掲載: 0
- 日本語AI要約: Gemini

## CVEs

### [CVE-2026-49329](https://access.redhat.com/security/cve/CVE-2026-49329)

> **Backend** / **HIGH** / CVSS: **7.5** / KEV: **no**

- タイトル: CVE-2026-49329
- 関連キーワード: go, golang, gin
- 影響製品: -
- 公開日: 2026-09-02 01:16:57 JST
- 更新日: 2026-09-02 06:03:04 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: openshift/oauth-serverにおけるAccept-Languageヘッダーの解析処理不備および既存脆弱性対策（CVE-2022-32149）のバイパスの存在。
- 影響: 区切り文字に'_'を含めた不正なヘッダー送信によりパースに過大な計算時間がかかり、認証サービス全体が停止（DoS）する可能性がある。
- 推奨対応: openshift/oauth-serverの修正済みバージョンへのアップデートや適切なパッチの適用を行う。

#### References
- https://access.redhat.com/security/cve/CVE-2026-49329
- https://bugzilla.redhat.com/show_bug.cgi?id=2483248

### [CVE-2026-84304](https://github.com/grpc/grpc-go/commit/7354d9c8debb4bcf2225bf429857078de310c176)

> **Backend** / **HIGH** / CVSS: **8.7** / KEV: **no**

- タイトル: CVE-2026-84304
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-02 04:17:30 JST
- 更新日: 2026-09-02 05:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: gRPC-Goにおいて、断片化されたHTTP/2 DATAフレームが個別にメモリへ保持される問題。
- 影響: 多数の小規模フレームを送信されることでメモリが枯渇し、プロセスの強制終了（クラッシュ/DoS）が発生する可能性がある。
- 推奨対応: gRPC-Go バージョン 1.83.1 以降へ更新する。必要に応じて受信バッファの圧縮機能を有効化する。

#### References
- https://github.com/grpc/grpc-go/commit/7354d9c8debb4bcf2225bf429857078de310c176
- https://github.com/grpc/grpc-go/commit/8cfeca0e1ee5ea0980dcc320e20240fa1079ec77
- https://github.com/grpc/grpc-go/pull/9331
- https://github.com/grpc/grpc-go/pull/9333
- https://github.com/grpc/grpc-go/releases/tag/v1.83.1

### [CVE-2026-84308](https://github.com/phpseclib/phpseclib/commit/fb56bc5bb9009b54a6c26b31aeec8ed944f17373)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-84308
- 関連キーワード: go, gin
- 影響製品: -
- 公開日: 2026-09-02 05:17:24 JST
- 更新日: 2026-09-02 05:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: phpseclibの純粋PHPによるX25519演算処理において、データ依存の処理（タイミング攻撃の隙）が存在する問題。
- 影響: ローカルからの観測等により、再利用されている秘密鍵が推測・漏洩される可能性がある。
- 推奨対応: phpseclib バージョン 3.0.57 または 4.0.1 以降へ更新する。また、ext-sodium等のネイティブ拡張機能の利用を検討する。

#### References
- https://github.com/phpseclib/phpseclib/commit/fb56bc5bb9009b54a6c26b31aeec8ed944f17373
- https://github.com/phpseclib/phpseclib/releases/tag/3.0.57
- https://github.com/phpseclib/phpseclib/releases/tag/4.0.1
- https://github.com/phpseclib/phpseclib/security/advisories/GHSA-q97c-8qh3-fpc6

### [CVE-2026-84303](https://github.com/grpc/grpc-go/commit/db9482836c298f234c896cf82ab68cafc78237f8)

> **Backend** / **MEDIUM** / CVSS: **6.3** / KEV: **no**

- タイトル: CVE-2026-84303
- 関連キーワード: go
- 影響製品: -
- 公開日: 2026-09-02 04:17:30 JST
- 更新日: 2026-09-02 04:17:30 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: gRPC-GoのxDS RBAC HTTPフィルタにおいて、ヘッダーマッチ名の大文字小文字変換（小文字化）が行われない問題。
- 影響: 大文字小文字が混在した拒否（DENY）ルールが一致せず要求が許可（フェイルオープン）されるなど、アクセス制御を回避される可能性がある。
- 推奨対応: gRPC-Go バージョン 1.83.1 以降へ更新する。

#### References
- https://github.com/grpc/grpc-go/commit/db9482836c298f234c896cf82ab68cafc78237f8
- https://github.com/grpc/grpc-go/commit/ebba6f3f1b206e2b4dc4d1d5a96d18430302c2fe
- https://github.com/grpc/grpc-go/pull/9332
- https://github.com/grpc/grpc-go/pull/9335
- https://github.com/grpc/grpc-go/releases/tag/v1.83.1

### [CVE-2026-83551](https://aws.amazon.com/security/security-bulletins/2026-093-aws/)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-83551
- 関連キーワード: python, aws
- 影響製品: -
- 公開日: 2026-09-02 04:17:29 JST
- 更新日: 2026-09-02 05:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Amazon SageMaker Python SDKのデコレータコンポーネントにおける機密情報の平文保存の脆弱性。
- 影響: 認証された攻撃者がHMACキーを取得し、同一アカウント内の他ユーザーのコンテキストで任意コードを実行する可能性があります。
- 推奨対応: Amazon SageMaker Python SDKをv3.11.0またはv2.256.0以降へアップデートしてください。

#### References
- https://aws.amazon.com/security/security-bulletins/2026-093-aws/
- https://github.com/aws/sagemaker-python-sdk/releases/tag/v2.256.0
- https://github.com/aws/sagemaker-python-sdk/releases/tag/v3.11.0
- https://github.com/aws/sagemaker-python-sdk/security/advisories/GHSA-7xmc-crrw-fv5r

### [CVE-2026-84202](https://github.com/modelscope/modelscope)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-84202
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-02 01:17:34 JST
- 更新日: 2026-09-02 03:17:48 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: ModelScopeにおけるPyYAMLの不適切なローダー（yaml.Loader）使用に伴う任意コード実行の脆弱性。
- 影響: 悪意のあるモデル設定ファイルを読み込むことで、攻撃者のコードが実行される可能性があります。
- 推奨対応: 安全なローダーを使用する修正版への更新や、信頼できないモデルの読み込みを控えることを推奨します。

#### References
- https://github.com/modelscope/modelscope
- https://github.com/modelscope/modelscope/blob/v1.40.0/modelscope/models/audio/tts/voice.py
- https://github.com/modelscope/modelscope/blob/v1.40.0/modelscope/models/multi_modal/mplug/configuration_mplug.py
- https://github.com/modelscope/modelscope/issues/1660
- https://www.vulncheck.com/advisories/modelscope-through-1.40.0-unsafe-yaml-deserialization-in-model-config-loading

### [CVE-2026-84305](https://github.com/andialbrecht/sqlparse/commit/a51df6d9e2d31b44be9adb6bc8732517db6bf96b)

> **Backend** / **MEDIUM** / CVSS: **5.1** / KEV: **no**

- タイトル: CVE-2026-84305
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-02 04:17:30 JST
- 更新日: 2026-09-02 05:17:24 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: sqlparseにおけるインデント再整形処理時のリソース過剰消費（DoS）の脆弱性。
- 影響: 攻撃者によって細工されたSQLの解析時にCPU消費率が急増し、処理遅延やサービス停止を引き起こす可能性があります。
- 推奨対応: sqlparseをバージョン0.6.0以降へアップデートしてください。

#### References
- https://github.com/andialbrecht/sqlparse/commit/a51df6d9e2d31b44be9adb6bc8732517db6bf96b
- https://github.com/andialbrecht/sqlparse/releases/tag/0.6.0
- https://github.com/andialbrecht/sqlparse/security/advisories/GHSA-cfqr-cjx5-5jcm
- https://github.com/andialbrecht/sqlparse/security/advisories/GHSA-cfqr-cjx5-5jcm

### [CVE-2026-51974](https://github.com/lllyasviel/Fooocus/blob/main/modules/meta_parser.py#L89)

> **Backend** / **UNKNOWN** / CVSS: **-** / KEV: **no**

- タイトル: CVE-2026-51974
- 関連キーワード: python
- 影響製品: -
- 公開日: 2026-09-02 03:17:43 JST
- 更新日: 2026-09-02 03:17:43 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: lllyasviel FooocusのEXIFメタデータ解析処理におけるeval()インジェクションの脆弱性。
- 影響: 細工された画像ファイルをアップロードされることで、リモートから任意のPythonコードを実行される可能性があります。
- 推奨対応: 影響を受けるバージョン（2.1.854〜2.5.5）の利用を止め、対策版へアップデートしてください。

#### References
- https://github.com/lllyasviel/Fooocus/blob/main/modules/meta_parser.py#L89
- https://github.com/lllyasviel/Fooocus/issues/4115
- https://mrbruh.com/fooocus/

### [CVE-2026-78012](https://pyramidsolutions.com/netstax-v-5-6-1-protecting-against-silent-buffer-overflow-in-ethernet-ip-stack-explicit-messages/)

> **Backend** / **CRITICAL** / CVSS: **9.8** / KEV: **no**

- タイトル: CVE-2026-78012
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-02 00:17:28 JST
- 更新日: 2026-09-02 01:17:18 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: NetStaX EtherNet/IP Stackにおける受信バッファオーバーフローの脆弱性。
- 影響: メモリ破壊やデバイスのクラッシュ、あるいはリモートからの攻撃につながる可能性があります。
- 推奨対応: NetStaX EtherNet/IP Stackをv5.6.1以降へアップデートしてください。

#### References
- https://pyramidsolutions.com/netstax-v-5-6-1-protecting-against-silent-buffer-overflow-in-ethernet-ip-stack-explicit-messages/

### [CVE-2026-10195](https://www.fs-poster.com/documentation/updates-changelogs)

> **Backend** / **HIGH** / CVSS: **8.8** / KEV: **no**

- タイトル: CVE-2026-10195
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-02 01:16:47 JST
- 更新日: 2026-09-02 05:47:54 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: WordPress用FS-Posterプラグインにおける入力サニタイズおよび認可チェックの不足によるOSコマンド実行の脆弱性。
- 影響: 低権限（購読者権限以上）の認証済みユーザーがサーバー上で任意のコマンドを実行する可能性があります。
- 推奨対応: FS-Posterプラグインを修正済みバージョンへアップデートしてください。

#### References
- https://www.fs-poster.com/documentation/updates-changelogs
- https://www.wordfence.com/threat-intel/vulnerabilities/id/3130d987-6a54-4208-8591-0bb9626858ae?source=cve

### [CVE-2026-45221](https://public.easybyte.it/downloads/archive/2.1.0)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-45221
- 関連キーワード: openssl
- 影響製品: -
- 公開日: 2026-09-02 05:17:14 JST
- 更新日: 2026-09-02 05:17:14 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Kongaにおける不適切なファイルパス権限に起因する権限昇格の脆弱性。
- 影響: ローカルの低権限ユーザーが悪意あるライブラリ等を配置することで、Konga起動ユーザーの権限で任意コードを実行する可能性があります。
- 推奨対応: Kongaをバージョン2.1.0以降へアップデートしてください。

#### References
- https://public.easybyte.it/downloads/archive/2.1.0
- https://www.easybyte.it/
- https://www.vulncheck.com/advisories/konga-privilege-escalation-via-hardcoded-openssl-path

### [CVE-2026-73707](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05133en_us&docLocale=en_US)

> **Backend** / **HIGH** / CVSS: **8.5** / KEV: **no**

- タイトル: CVE-2026-73707
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-02 05:17:18 JST
- 更新日: 2026-09-02 06:08:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HPE Networking Fabric ComposerのAPIにおける不適切なアクセス制御による権限昇格の脆弱性。
- 影響: 低権限の認証済みユーザーが、本来許可されていないシステム設定変更などのアクションを実行する可能性があります。
- 推奨対応: ベンダーが提供する修正済みソフトウェアを適用してください。

#### References
- https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05133en_us&docLocale=en_US

### [CVE-2026-73723](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05133en_us&docLocale=en_US)

> **Backend** / **HIGH** / CVSS: **7.1** / KEV: **no**

- タイトル: CVE-2026-73723
- 関連キーワード: gin
- 影響製品: -
- 公開日: 2026-09-02 05:17:19 JST
- 更新日: 2026-09-02 06:08:28 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: HPE Networking Fabric ComposerのWeb管理画面における権限昇格の脆弱性。
- 影響: 低権限の認証済みユーザーが、本来許可されていない状態変更アクションを実行する可能性があります。
- 推奨対応: ベンダーが提供する修正済みソフトウェアを適用してください。

#### References
- https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05133en_us&docLocale=en_US

### [CVE-2026-66835](https://cna.erlef.org/cves/CVE-2026-66835.html)

> **Backend** / **HIGH** / CVSS: **8.2** / KEV: **no**

- タイトル: CVE-2026-66835
- 関連キーワード: express
- 影響製品: -
- 公開日: 2026-09-02 00:17:23 JST
- 更新日: 2026-09-02 06:15:00 JST
- 出典: NVD

#### Gemini要約

- 日本語要約: Erlang/OTP inets httpdにおけるパス正規化不備によるアクセス制御迂回の脆弱性。
- 影響: 未認証のリモート攻撃者が、認証保護されたディレクトリ内のファイルを閲覧・取得する可能性があります。
- 推奨対応: Erlang/OTPを修正済みバージョンへアップデートしてください。

#### References
- https://cna.erlef.org/cves/CVE-2026-66835.html
- https://github.com/erlang/otp/commit/9641944a2efbf55bea760f8ff7ba777fe3a0961c
- https://github.com/erlang/otp/commit/bac19eb3dbd96cc49b6d8cabc1c04248bf8c79f6
- https://github.com/erlang/otp/commit/d8878dec0ececc2eab18e47bb18b472f224ca633
- https://github.com/erlang/otp/security/advisories/GHSA-r4vv-vc2c-2fw6

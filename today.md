# CVE Digest Dashboard (2026-09-13)

## Overview

- Total: 7
- Critical件数: 2
- High件数: 5
- KEV件数: 0
- Frontend件数: 0
- Backend件数: 1
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-09-13/frontend-summary.md)
- [Backend Summary](docs/2026-09-13/backend-summary.md)

## Today TOP5

- [CVE-2026-90558](https://github.com/irontec/sngrep) CVE-2026-90558 / CRITICAL / security
- [CVE-2026-90647](https://www.ase-systems.com/wp-content/uploads/2026/07/CYB_2026_86278_Advisory_v1.0.pdf) CVE-2026-90647 / CRITICAL / security
- [CVE-2026-90556](https://github.com/freeciv/freeciv) CVE-2026-90556 / HIGH / security
- [CVE-2026-90559](https://github.com/xerial/snappy-java) CVE-2026-90559 / HIGH / security
- [CVE-2026-90560](https://github.com/luben/zstd-jni) CVE-2026-90560 / HIGH / security

## Geminiによる今日の総括

## 今日のまとめ

本日公開された脆弱性は全7件で、最高でCVSS 9.8の深刻な脆弱性が含まれています。パケット解析ツール（sngrep）におけるリモートコード実行（RCE）の恐れがあるスタックバッファオーバーフローや、通信テストツール（ASE2000）での中間者攻撃（MitM）につながる証明書検証の不備がCRITICALとして報告されています。また、Java開発で広く使われるライブラリ（`zstd-jni`, `snappy-java`）での境界外アクセスによるJVM停止、Flatpakのサンドボックス回避、openstatusでのSSRFなど、多様な層で影響のある脆弱性が含まれています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-90558（sngrep / CVSS 9.8: CRITICAL）**
   - **概要:** 255バイトを超えるSIPヘッダ値のフォーマット処理においてスタックバッファオーバーフローが発生。悪意のあるパケットによるクラッシュや任意コード実行の恐れ。
2. **CVE-2026-90647（ASE2000 V2 Communication Test Set / CVSS 9.1: CRITICAL）**
   - **概要:** TLSクライアント処理での不適切な証明書検証により、ネットワーク上の攻撃者による中間者（MitM）攻撃および暗号化通信のバイパスが可能。
3. **CVE-2026-90560 & CVE-2026-90559（zstd-jni: CVSS 8.8 / snappy-java: CVSS 8.7: HIGH）**
   - **概要:** 解凍・辞書処理時のオフセットやバッファ容量の検証欠如により、境界外読み取り/書き込みが発生。攻撃者によるメモリ情報の漏洩やJVMの異常終了を引き起こす可能性。
4. **CVE-2026-90616（Flatpak / CVSS 7.4: HIGH）**
   - **概要:** シンボリックリンク保護の不備により、サンドボックス内の悪意あるアプリがホスト上の任意ファイルへアクセスし、ホスト上での任意コード実行へ権限昇格できる問題。

---

## 開発者向けコメント

* **Java系圧縮・解凍ライブラリの確認:** `zstd-jni` や `snappy-java` を利用しているプロジェクトでは、不正なデータ入力によってJVMが強制終了するリスクがあります。依存関係のバージョンチェックを実施してください。
* **入力バッファおよび証明書検証の再確認:** `sngrep` のようにパケットヘッダ長を盲信した処理や、`ASE2000` のように証明書の検証ロジックをバイパスできる構成は致命的な脆弱性につながります。C/C++でのバッファ境界チェックや、TLS実装時の検証処理を徹底しましょう。
* **アクセス制御とパス検証:** サンドボックス構造（Flatpak）でのシンボリックリンク攻撃や、プロキシ処理（openstatusのSSRF）に見られるように、ユーザーが制御可能なパスやURLを扱う際は適切な検証・制限を組み込むことが重要です。

<!-- SECURITY_NEWS_START -->
## セキュリティーニュース

### 今日の総括

オランダNCSCがCheck Point VPNにおける深刻な脆弱性の悪用が差し迫っていると警告しています。また、ChromeやWindowsのゼロデイ脆弱性を組み合わせたエクスプロイトキットの悪用が確認されています。さらに、AIを用いた兵器開発の試みとその失敗に関する事例も報告されました。

- **HIGH** [Dutch NCSC: Critical Check Point VPN flaws exploitation is imminent](https://www.bleepingcomputer.com/news/security/dutch-ncsc-critical-check-point-vpn-flaws-exploitation-is-imminent/) — BleepingComputer
- **HIGH** [BlueMoon Exploit Kit Chains Recent Chrome, Windows Zero-Days](https://www.securityweek.com/bluemoon-exploit-kit-chains-recent-chrome-windows-zero-days/) — SecurityWeek
- **MEDIUM** [Users in Houthi-Held Yemen Tried to Develop Advanced Weapons With AI, Anthropic Says](https://www.securityweek.com/users-in-houthi-held-yemen-tried-to-develop-advanced-weapons-with-ai-anthropic-says/) — SecurityWeek

- [セキュリティーニュースをすべて見る](security-news.md)

<!-- SECURITY_NEWS_END -->

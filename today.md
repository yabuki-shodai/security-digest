# CVE Digest Dashboard (2026-07-16)

## Overview

- Total: 30
- Critical件数: 5
- High件数: 19
- KEV件数: 0
- Frontend件数: 26
- Backend件数: 4
- GitHub Models総括: GitHub Models

## Links

- [Frontend Summary](docs/2026-07-16/frontend-summary.md)
- [Backend Summary](docs/2026-07-16/backend-summary.md)

## Today TOP5

- [CVE-2026-55445](https://github.com/whyour/qinglong/commit/6bec52dca158481258315ba0fc2f11206df7b719) CVE-2026-55445 / CRITICAL / frontend
- [CVE-2026-53512](https://github.com/better-auth/better-auth/commit/1f2ff4215c4affff0b140b0c0a712c0dde35659c) CVE-2026-53512 / CRITICAL / frontend
- [CVE-2026-53513](https://github.com/better-auth/better-auth/commit/37f60cb176cb53147da7dfd5ec15afa5b486e81e) CVE-2026-53513 / CRITICAL / frontend
- [CVE-2026-46421](https://github.com/cap-js/cds-dbs/security/advisories/GHSA-pvw4-cvr4-97p8) CVE-2026-46421 / CRITICAL / frontend
- [CVE-2026-54458](https://github.com/WWBN/AVideo/commit/8be71e53ccbe9b84b30870db386fb4d2b11e1c16) CVE-2026-54458 / CRITICAL / frontend

## GitHub Modelsによる今日の総括

## 今日のまとめ
本日公開されたCVEは主にTypeScriptやJavaScriptを中心としたフロントエンド関連の脆弱性が多く、認証・認可ライブラリBetter Authに関する複数の高・重大度脆弱性が目立ちます。これらはトークン管理の不備や不適切な検証による権限昇格や不正アクセスを招くものです。また、Qinglongの管理者権限リセットやWWBN AVideoのクロスサイトスクリプティング、Cisco RoomOSのバックエンドにおけるアクセス制御やメモリ管理の問題も報告されています。npmパッケージのマルウェア混入も確認されており、サプライチェーンリスクにも注意が必要です。

## 優先して確認すべき3〜5件
1. **CVE-2026-53513 (Better Auth, CRITICAL, CVSS 9.6)**  
   OIDC設定の検証不足によるサーバーサイドリクエストフォージェリ（SSRF）とアカウントリンクの可能性。認証基盤に直結するため最優先で対応を。

2. **CVE-2026-55445 (Qinglong, CRITICAL, CVSS 9.3)**  
   認証ガードの不備による管理者資格情報リセット。初期化済みインスタンスの管理者権限を奪われる恐れあり。

3. **CVE-2026-53512 (Better Auth, CRITICAL, CVSS 9.1)**  
   クライアントシークレット未検証のトークンリフレッシュで不正アクセストークン発行が可能。認証の根幹に関わる重大問題。

4. **CVE-2026-46421 (SAP CAP, CRITICAL, CVSS 9.3)**  
   npmパッケージのマルウェア混入による資格情報漏洩と自己拡散。サプライチェーン攻撃のリスクが高い。

5. **CVE-2026-54458 (WWBN AVideo, CRITICAL, CVSS 9.6)**  
   管理者画面でのストアドXSS。認証済み管理者のブラウザで任意スクリプト実行が可能。

## 開発者向けコメント
- 認証・認可ライブラリのアップデートは最優先で行い、特にBetter Authの1.6.11以降への更新を推奨します。トークン管理やOIDC設定の検証強化が必須です。  
- Qinglongの管理者初期化機能は2.20.1以降で修正済みのため、早急にバージョンアップしてください。  
- npmパッケージの信頼性を再確認し、特にSAP CAP関連のパッケージは不審なバージョンを避けること。CI/CDパイプラインでの署名検証や依存関係監査を強化しましょう。  
- クロスサイトスクリプティング（XSS）対策として、ユーザー入力の適切なサニタイズとエスケープ処理を徹底してください。特に管理者向けUIでの外部入力は厳重に検証が必要です。  
- Cisco RoomOSの脆弱性は内部レビューによるもので、アクセス制御やメモリ管理のベストプラクティスを改めて見直す良い機会です。安全なリソース管理を心がけてください。

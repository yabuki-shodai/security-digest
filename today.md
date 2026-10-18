# CVE Digest Dashboard (2026-10-18)

## Overview

- Total: 30
- Critical件数: 1
- High件数: 15
- KEV件数: 0
- Frontend件数: 2
- Backend件数: 18
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-18/frontend-summary.md)
- [Backend Summary](docs/2026-10-18/backend-summary.md)

## Today TOP5

- [CVE-2026-111911](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-g6cq-6rqg-6c9p) CVE-2026-111911 / CRITICAL / security
- [CVE-2026-109701](https://patchstack.com/database/wordpress/plugin/paytpv-for-woocommerce/vulnerability/wordpress-paycomet-for-woocommerce-plugin-5-45-cross-site-scripting-xss-vulnerability?_s_id=cve) CVE-2026-109701 / HIGH / security
- [CVE-2026-111886](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-7pjw-6v4g-f837) CVE-2026-111886 / HIGH / security
- [CVE-2026-111906](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-cmvh-fpmf-8gfx) CVE-2026-111906 / HIGH / security
- [CVE-2026-111882](https://github.com/thorsten/phpMyFAQ/security/advisories/GHSA-43g3-pp5p-fg96) CVE-2026-111882 / HIGH / security

## Geminiによる今日の総括

## 今日のまとめ
本日はWebアプリケーション（主に **phpMyFAQ**、**Coder**、**Admidio** 等）に関する認証回避、アクセス制御の不備、アカウント乗っ取りに関する脆弱性が多数公開されました。特に phpMyFAQ においては、WebAuthnの実装不備（CVSS 9.8）をはじめ、SSO連携やメールアドレス変更機能における認証バイパス・アカウント乗っ取りの深刻な脆弱性が集中的に報告されています。

---

## 優先して確認すべき3〜5件

1. **CVE-2026-111911（phpMyFAQ | CVSS 9.8: CRITICAL）**
   - **WebAuthn登録の不備によるアカウント乗っ取り**
   - 未認証・チャレンジ検証なしでパスキーをアカウントに登録可能。パスワードや2FAを回避して任意のアカウントを乗っ取られる危険性があります。
2. **CVE-2026-111884（phpMyFAQ | CVSS 8.7: HIGH）**
   - **メールアドレス変更時の再認証欠如**
   - 現在のパスワード確認なしでアカウントのメールアドレスを変更可能。セッション奪取後にアドレスを変更され、パスワードリセット経由でアカウントを奪われます。
3. **CVE-2026-111882（phpMyFAQ | CVSS 8.6: HIGH）**
   - **SSOログイン時の2FA（TOTP）バイパス**
   - KeycloakやEntra IDを経由したログイン時、2FA（TOTP）の検証がスキップされ、2FA有効化アカウントへ不正アクセスされる恐れがあります。
4. **CVE-2026-111893（phpMyFAQ | CVSS 8.5: HIGH）**
   - **カテゴリ制限の不備による権限昇格**
   - 制限付き管理者がAPIを経由して自身に割り当てられていないスコープ外のカテゴリ権限をグループに付与し、特権を奪取できます。
5. **CVE-2026-111934（Coder | CVSS 6.3: MEDIUM）**
   - **X-Forwarded-Forの誤信頼によるIPスプーフィング**
   - クライアントが送信した `X-Forwarded-For` をそのまま信頼するため、レートリミットの回避（ブルートフォース攻撃）や監査ログの偽装が可能です。

---

## 開発者向けコメント

- **重要なアカウント操作時の再確認・認証を徹底する**: メールアドレスの変更や2FA設定の解除など、アカウントの所有権に関わる操作では、セッション状態だけでなく現在のパスワード入力や認証チャレンジを必ず求めてください。
- **IdP・WebAuthn連携時の実装を見直す**: SSO連携時のユーザー紐付けには変更可能な属性（`preferred_username`など）ではなく不変の識別子（`sub`等）を使用し、パスキー登録・認証時は適切なチャレンジ検証とセッション認証を必須としてください。
- **プロキシヘッダー（`X-Forwarded-For`）の取得ロジックに注意する**: クライアント側から送られるヘッダー値をそのまま信用せず、自社で管理するリバースプロキシが追記した正しいIP（最右列など）を参照してレートリミットやログ記録を行ってください。

# CVE Digest Dashboard (2026-10-22)

## Overview

- Total: 30
- Critical件数: 6
- High件数: 10
- KEV件数: 0
- Frontend件数: 19
- Backend件数: 11
- Gemini総括: Gemini

## Links

- [Frontend Summary](docs/2026-10-22/frontend-summary.md)
- [Backend Summary](docs/2026-10-22/backend-summary.md)

## Today TOP5

- [CVE-2026-114139](https://github.com/getsentry/sentry-javascript/commit/878b685c85dc12045e47e1932c96f5381d7ac532) CVE-2026-114139 / CRITICAL / frontend
- [CVE-2026-20043](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-snort3-ybgmhTQe) CVE-2026-20043 / CRITICAL / backend
- [CVE-2026-76473](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voice-hardening-twgbH9e3) CVE-2026-76473 / CRITICAL / backend
- [CVE-2026-113788](https://github.com/uselagoon/lagoon/releases/tag/v2.33.2) CVE-2026-113788 / CRITICAL / backend
- [CVE-2026-76474](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voice-hardening-twgbH9e3) CVE-2026-76474 / CRITICAL / backend

## Geminiによる今日の総括

## 今日のまとめ
本日掲載されたCVEでは、フロントエンドおよびフルスタックフレームワーク（Next.js/Sentry、Nuxt、Astro、Storybook）、バックエンドフレームワーク（Django REST framework）、およびデプロイ・アプライアンス基盤（Lagoon、Ciscoなど）に関する脆弱性が多数報告されています。特にWeb開発領域において、アクセス制御ミドルウェアの迂回やトークン失効の不具合など、認証・認可の根幹に関わる影響度の高い脆弱性が目立ちます。

## 優先して確認すべき3〜5件

1. **CVE-2026-114139 (@sentry/nextjs)**
   - **深刻度**: CRITICAL (CVSS 9.1)
   - **概要**: Next.js向けSentry SDKのwebpack統合において、`tunnelRoute`利用時にアクセス制御ミドルウェアがスキップされ、未認証リクエストが保護対象ルートに到達できる脆弱性。
2. **CVE-2026-114137 (Django REST framework)**
   - **深刻度**: HIGH (CVSS 7.4)
   - **概要**: `TokenProxy.delete()` が主キーの参照誤りによりトークンレコードの削除に失敗する不具合。資格情報の失効処理が成功したように見えて実際にはトークンが有効なまま残る。
3. **CVE-2026-114126 (Storybook)**
   - **深刻度**: HIGH (CVSS 8.7)
   - **概要**: 開発サーバーがローカルネットワーク上にWebSocket認証トークンを漏洩させる問題。同一LAN内の攻撃者によるファイル書き込みやコード注入につながる恐れがある。
4. **CVE-2026-113788 (Lagoon)**
   - **深刻度**: CRITICAL (CVSS 9.4)
   - **概要**: Kubernetes向けアプリ配信プラットフォーム「Lagoon」のSSHサービスにおける脆弱性。アカウントを持つユーザーが任意コード実行および管理者権限昇格を行える。
5. **CVE-2026-114131 / CVE-2026-114132 (Nuxt)**
   - **深刻度**: MEDIUM (CVSS 6.5 / 6.3)
   - **概要**: URLセグメントのパーセントエンコード処理や大文字・小文字の判定不一致により、設定した`routeRules`やミドルウェアを迂回してSSRデータや保護ページが取得可能になる脆弱性。

## 開発者向けコメント
- **ルーティング・ミドルウェア迂回への警戒**: Next.js（Sentry統合）やNuxtにおいて、特定のパス指定やURLエンコード表現によってアクセス制御がバイパスされる問題が報告されています。対象ライブラリを修正バージョンへ更新するとともに、重要なルートが正しく保護されているかテストコード等で再確認してください。
- **認証トークン失効処理の実効性チェック**: Django REST Frameworkを利用してAPI認証トークンの無効化を行っている場合、実際にDB上のレコードが削除・無効化されているか実挙動を確認し、パッチバージョンへの適用を進めてください。
- **開発サーバー・ツールのセキュリティ確保**: Storybookのようなローカル開発用サーバーも、ネットワーク共有時のトークン漏洩からコード挿入のリスクに晒されます。開発環境で利用するツールのバージョン管理とバインド範囲の適切な制御を行ってください。

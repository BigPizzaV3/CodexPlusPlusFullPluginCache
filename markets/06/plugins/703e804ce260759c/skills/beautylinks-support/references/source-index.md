# コード参照の索引

確認日：2026-09-20。原本の操作説明書は2026-09-19版。コード断片は店舗操作の根拠に必要な部分だけを固定版から抽出した。認証情報・環境設定値・顧客データ・コード全体は同梱していない。

## 確認した版

| 区分 | リポジトリ | ブランチ | 確認したコミット |
| --- | --- | --- | --- |
| 管理画面 F | kirato0905-cmyk/BeautyLinks_admin_web | SalonLineBot_Render | 6d6e049850867421c7c41f80190d64123ef1ff0b |
| バックエンド B | kirato0905-cmyk/beauty-links-backend | SalonLineBot_Render | da44d42f18366ffd824ee77d0a0d5ada9e3af059 |

これは確認時点のブランチ先頭。本番のデプロイ済み版・実データ・動作結果を確認した記録ではない。「最新版」「本番で必ずこう動く」と言い換えない。

## 通常の回答

1. 操作説明書の該当ページと対応する `code-*.md` を読む。
2. 条件表の画面・対象・例外が質問に一致することを確認する。根拠が必要なら `code-excerpts.md` の対応するIDを読む。
3. 手順・保存／確定・結果確認を回答する。参照は「コード照合：予約登録（2026-09-20）」のように短く示す。
4. 同梱資料だけなら「コード照合済み資料を参照した」と説明する。回答時にGitHubを取得したとは言わない。

## 権限がある環境で元コードを読む

このプラグイン自体はGitHub接続や権限を付与しない。現在の利用者に接続済みのGitHub読み取りツールが提供されている場合だけ利用できる。利用できなければ固定版で続け、店舗の案内を止めない。

1. 現在利用できるGitHubツールの定義を確認する。`fetch`、`fetch_file`、`search` に相当する読み取り機能を使う。利用者の明示的な対象指定を優先する。
2. 上表の対象リポジトリのブランチ情報を取得し、実際に返されたコミットSHAを記録する。固定版を再確認するときは上表のSHAを指定する。新しいSHAと古いSHAを混ぜて1つの版として答えない。
3. 下表の画面・コンポーネントをそのSHAで取得し、画面のボタン → イベント処理 → 呼び出すAPI → 対応するサーバー処理を読む。必要な箇所から段階的に取得する。
4. ファイルの入口だけ、検索結果だけ、コードのコメントだけで確定しない。表示条件、無効条件、入力検証、成功・失敗時の分岐を確認する。バックエンドに関数があるだけでは、管理画面に対応ボタンがあるとは判断しない。
5. GitHub検索は既定ブランチを対象とすることがある。検索結果は場所の発見に使い、回答根拠には確定したSHAで取得した本文を使う。
6. 接続不足や403などで読めない場合は、同じ認証要求を繰り返さず固定版へ戻る。パスワード・トークン・Cookie・リポジトリ公開を求めない。
7. 実際に取得したファイルの版・関数を根拠にする。プログラムを実行、APIを書き換え、データや設定を変更して確かめない。

## 調査の入口

以下は場所の索引。照合メモに載っていない処理を「確認済み」と扱わず、本文を読む。

| 分野 | 管理画面 F | バックエンド B |
| --- | --- | --- |
| 電話・店頭予約 | app/admin/reservations/new/page.tsx | api/admin/reservation_pricing_routes.py、api/admin/routes.py |
| 予約一覧・変更 | app/admin/reservations/page.tsx、app/admin/reservations/[reservationId]/page.tsx | api/admin/routes.py |
| 空き枠・勤務・営業日 | app/admin/calendar/page.tsx、app/admin/staff/page.tsx、app/admin/business/page.tsx | api/services/availability_service.py、api/business_hours.py、api/admin/routes.py |
| 顧客・カルテ・顧客別時間 | app/admin/customers/[customerId]/page.tsx、components/admin/CustomerDurationOverridesPanel.tsx | api/admin/routes.py、api/services/customer_duration_service.py、api/services/carte_image_service.py |
| メニュー・セット | app/admin/menus/page.tsx | api/admin/routes.py、api/admin/reservation_pricing_routes.py |
| クーポン | components/admin/CouponManagementPanel.tsx | api/admin/coupon_routes.py、api/services/birthday_coupon_service.py、api/services/coupon_delivery_service.py |
| 友達紹介 | components/admin/ReferralProgramPanel.tsx | api/services/referral_service.py、api/admin/referral_routes.py |
| 店販・配送・返金 | components/admin/RetailProposalPanel.tsx、components/admin/RetailOrderFinanceCard.tsx | api/admin/retail_routes.py、api/services/retail_order_service.py、api/services/retail_refund_service.py、api/services/retail_order_finance_service.py |
| 再来店・失客・口コミ・追加提案 | app/admin/automation/page.tsx | api/admin/routes.py、api/services/automation_service.py、api/services/upsell_application_service.py |
| 空席販売 | components/admin/CancellationSlotSalesPanel.tsx、components/admin/NormalVacancySalesPanel.tsx | api/services/cancellation_slot_service.py、api/services/normal_vacancy_sale_service.py |
| FAQ・店舗情報 | app/admin/content/page.tsx | api/admin/routes.py、api/repositories/database_content_repository.py |
| 通知・売上 | app/admin/notifications/page.tsx、app/admin/sales/page.tsx | api/admin/routes.py |
| 権限・契約・店販決済 | components/admin-sidebar.tsx、lib/admin-permissions.ts、app/admin/account/page.tsx、app/admin/retail-stripe/page.tsx | api/admin/routes.py、api/services/billing_access_service.py、api/admin/billing_routes.py、api/admin/stripe_connect_routes.py |

## 矛盾の扱い

- 2026-09-20照合では、説明書の「休業日が特別営業時間より優先」という記載と管理画面用の空き枠計算に差がある。`code-availability.md` を読む。
- 新規予約の電話番号は画面側と保存側で許容形式が異なる。`code-reservations.md` を読む。
- 発送説明には「追跡番号を登録」と残る箇所がある一方、実際の入力フォームと送信内容は発送メモ。`code-retail.md` を読む。
- コードが新しくてもデプロイされているとは限らない。ユーザーの画面が異なる場合は必要箇所のスクリーンショットかエラーを確認する。

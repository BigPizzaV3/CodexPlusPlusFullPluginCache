# 固定版のコード断片

確認日：2026-09-20。以下は操作仕様の説明に必要な原文の抜粋。認証情報や実データを含まない。完全な関数とは限らないため、抜粋外の挙動まで推測しない。回答の手順は対応するコード照合メモと操作説明書を併読する。

## 目次

- R1：電話番号は任意・画面側の形式確認
- R2：公開中スタッフ1人なら担当欄を省略
- R3：カレンダー表示方式で変わる入力
- R4：新規予約の確認と登録ボタン
- R5：電話番号の保存側の形式確認
- R6：新規顧客はLINE未連携・未同意として作成
- A1：管理画面用：特別営業時間を先に適用
- A2：別の営業時間関数：休業日を先に適用
- A3：予約枠が不成立となる理由
- A4：管理画面のセット所要時間の優先順
- P1：誕生日手動配信の実行引数
- P2：誕生日配信対象の絞り込み
- P3：手動配信は年次重複防止とは別の発行
- P4：紹介された方の初回来店済みで判定
- T1：発送登録から送る内容
- T2：現行発送フォームは発送メモ
- T3：画面の返金は残りの対象額すべて
- T4：一括発送準備の対象と結果
- T5：原価などが不明なら利益は未算出
- X1：閲覧者の書き込みはサーバー側で拒否
- X2：売上向上はサイドバーで追加条件がある
- X3：契約の利用権と猶予期間

ファイルパスと行番号は下記の固定コミットに対するもの。別の版へ行番号だけを流用しない。GitHubへのリンクは閲覧権限がある利用者向け。店舗利用者は同梱の抜粋をそのまま読める。

## R1：電話番号は任意・画面側の形式確認

出典：`kirato0905-cmyk/BeautyLinks_admin_web` / `app/admin/reservations/new/page.tsx`
確認コミット：`6d6e049850867421c7c41f80190d64123ef1ff0b`

[元コード L313〜L322](https://github.com/kirato0905-cmyk/BeautyLinks_admin_web/blob/6d6e049850867421c7c41f80190d64123ef1ff0b/app/admin/reservations/new/page.tsx#L313-L322)

```tsx
function validateJapanesePhoneNumber(value: string): string | null {
  const cleaned = String(value || "").replace(/[\s-]/g, "");
  // 管理画面からの予約作成では電話番号は任意。
  // 入力された場合だけ形式チェックする。
  if (!cleaned) return null;
  if (!/^(0\d{9,10}|\+81\d{9,10})$/.test(cleaned)) {
    return "電話番号は日本の電話番号形式で入力してください。例：09012345678";
  }
  return null;
}
```

## R2：公開中スタッフ1人なら担当欄を省略

出典：`kirato0905-cmyk/BeautyLinks_admin_web` / `app/admin/reservations/new/page.tsx`
確認コミット：`6d6e049850867421c7c41f80190d64123ef1ff0b`

[元コード L463〜L475](https://github.com/kirato0905-cmyk/BeautyLinks_admin_web/blob/6d6e049850867421c7c41f80190d64123ef1ff0b/app/admin/reservations/new/page.tsx#L463-L475)

```tsx
  const activeStaff = useMemo(
    () => staff.filter((member) => member.is_active),
    [staff],
  );
  const autoAssignedStaff =
    activeStaff.length === 1 ? activeStaff[0] : null;

  // 公開中スタッフが1人だけなら担当者は自動確定。
  // 担当選択・担当名・指名料のUIは表示しない。
  const shouldHideStaffUi = activeStaff.length === 1;
  const staffIdIsActive = activeStaff.some(
    (member) => member.id === staffId,
  );
```

## R3：カレンダー表示方式で変わる入力

出典：`kirato0905-cmyk/BeautyLinks_admin_web` / `app/admin/reservations/new/page.tsx`
確認コミット：`6d6e049850867421c7c41f80190d64123ef1ff0b`

[元コード L1640〜L1658](https://github.com/kirato0905-cmyk/BeautyLinks_admin_web/blob/6d6e049850867421c7c41f80190d64123ef1ff0b/app/admin/reservations/new/page.tsx#L1640-L1658)

```tsx
                    {date} {calendarPresetHasStartTime ? startTime : "開始時間は未選択"}
                    {calendarPresetHasStartTime ? ` 〜 ${previewDuration ? previewEndTime : "メニュー選択後に表示"}` : ""}
                  </strong>
                  <p>{calendarPresetHasStartTime
                    ? "日・週カレンダーの枠から作成しています。この場合、空き時間候補は表示しません。登録時にDB上の空き状況を最終確認します。"
                    : "月カレンダーから作成しています。日付だけ引き継ぎ、開始時間は手動で選択してください。"}</p>
                </div>
              ) : null}

              {pastDateBlocked ? (
                <p className="helperText warningText">過去の日付では新規予約を作成できません。</p>
              ) : dateIsPast && ALLOW_PAST_ADMIN_RESERVATIONS ? (
                <p className="helperText warningText">確認用テストモード：過去日予約を登録できます。登録後は「来店済み」に変更してください。</p>
              ) : shouldHideTimeCandidates ? (
                <p className="helperText">日・週カレンダーの枠から作成しているため、空き時間候補は表示しません。</p>
              ) : !staffId || serviceIds.length === 0 ? (
                <p className="helperText">{shouldHideStaffUi ? "予約日・メニューを選ぶと、空き時間候補が表示されます。" : "予約日・担当スタッフ・メニューを選ぶと、空き時間候補が表示されます。"}</p>
              ) : calendarLoading || durationLoading ? (
                <p className="helperText">空き時間と顧客別所要時間を取得しています...</p>
```

## R4：新規予約の確認と登録ボタン

出典：`kirato0905-cmyk/BeautyLinks_admin_web` / `app/admin/reservations/new/page.tsx`
確認コミット：`6d6e049850867421c7c41f80190d64123ef1ff0b`

[元コード L1256〜L1270](https://github.com/kirato0905-cmyk/BeautyLinks_admin_web/blob/6d6e049850867421c7c41f80190d64123ef1ff0b/app/admin/reservations/new/page.tsx#L1256-L1270)

```tsx
    const confirmed = await confirm({
      title: "操作を確認してください",
      description: `新規予約を登録しますか？\n\n` +
      `顧客：${trimmedName} / ${trimmedPhone || "電話番号未登録"}\n` +
      `日時：${date} ${startTime} - ${previewEndTime}\n` +
      staffConfirmLine +
      `メニュー：${selectedFeaturedSet?.name || chosenServices.map((service) => service.name).join(" / ")}\n` +
      `${priceLines}\n` +
      `所要時間：${previewDuration}分\n\n` +
      (dateIsPast && ALLOW_PAST_ADMIN_RESERVATIONS
        ? `【確認用】過去日予約として登録します。登録後に予約詳細で「来店済み」へ変更してください。`
        : `管理画面のカレンダー・予約一覧・通知に料金内訳まで反映されます。`),
      confirmLabel: "実行する",
      danger: false,
    });
```

[元コード L1839〜L1844](https://github.com/kirato0905-cmyk/BeautyLinks_admin_web/blob/6d6e049850867421c7c41f80190d64123ef1ff0b/app/admin/reservations/new/page.tsx#L1839-L1844)

```tsx
              <button className="submitButton" type="button" disabled={creating || durationLoading || pricingLoading || pastDateBlocked || !startTimeIsAvailable} onClick={() => void createReservation()}
  aria-busy={creating || durationLoading || pricingLoading}>
                {creating ? "登録中..." : durationLoading ? "所要時間確認中..." : pricingLoading ? "料金確認中..." : "新規予約を登録"}
              </button>
              <p className="noticeText">登録時にDB上の空き状況を最終確認し、管理画面カレンダーに反映します。</p>
            </aside>
```

## R5：電話番号の保存側の形式確認

出典：`kirato0905-cmyk/beauty-links-backend` / `api/admin/routes.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L8056〜L8076](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/admin/routes.py#L8056-L8076)

```python
def _normalize_admin_reservation_phone(phone_number: Optional[str]) -> str:
    """管理画面入力の電話番号を数字のみへ正規化する。

    管理画面からの予約作成では電話番号は任意。
    未入力の場合は空文字で保存し、入力された場合だけ形式チェックする。
    """
    text = str(phone_number or "").strip().replace("−", "-").replace("ー", "-").replace("―", "-")
    if not text:
        return ""
    if not re.fullmatch(r"[0-9\-]+", text):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "INVALID_PHONE_NUMBER", "message": "電話番号は数字またはハイフンで入力してください。"},
        )
    digits = text.replace("-", "")
    if len(digits) not in {10, 11}:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "INVALID_PHONE_NUMBER", "message": "電話番号は10桁または11桁で入力してください。"},
        )
    return digits
```

## R6：新規顧客はLINE未連携・未同意として作成

出典：`kirato0905-cmyk/beauty-links-backend` / `api/admin/routes.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L7673〜L7713](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/admin/routes.py#L7673-L7713)

```python
def _ensure_admin_reservation_customer_for_create(
    db: Session,
    admin: AdminContext,
    existing_customer: Optional[Customer],
    *,
    client_name: str,
    phone_number: str,
) -> Customer:
    """管理画面の新規予約保存時に、顧客一覧へ出す顧客レコードを保証する。

    既存顧客が見つかっている場合は氏名/電話番号を同期し、
    見つからない場合はLINE未連携の顧客として新規作成する。
    """
    if existing_customer:
        _sync_admin_reservation_customer_fields(
            existing_customer,
            client_name=client_name,
            phone_number=phone_number,
        )
        return existing_customer

    name = str(client_name or "").strip()
    customer = Customer(
        store_id=admin.store_id,
        line_user_id=_make_admin_manual_line_user_id(db, admin.store_id),
        display_name=name,
        full_name=name,
        phone_number=str(phone_number or "").strip() or None,
        status="active",
        consented=False,
        input_state=None,
    )
    db.add(customer)
    db.flush()
    return customer


def _modification_snapshot(reservation: Reservation) -> dict:
    return {
        "status": reservation.status,
        "date": reservation.date.isoformat(),
```

## A1：管理画面用：特別営業時間を先に適用

出典：`kirato0905-cmyk/beauty-links-backend` / `api/services/availability_service.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L308〜L357](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/services/availability_service.py#L308-L357)

```python
    def get_store_periods(self, target_date: Any) -> List[Dict[str, str]]:
        resolved_date = self.parse_date(target_date)
        cache_key = resolved_date.isoformat()
        if cache_key in self._store_periods_cache:
            return [dict(period) for period in self._store_periods_cache[cache_key]]

        if resolved_date not in self._special_hours_cache:
            self._special_hours_cache[resolved_date] = (
                self.db.query(StoreSpecialHour)
                .filter(
                    StoreSpecialHour.store_id == self.store_id,
                    StoreSpecialHour.special_date == resolved_date,
                )
                .first()
            )
        special = self._special_hours_cache[resolved_date]
        if special:
            if special.is_closed:
                self._store_periods_cache[cache_key] = []
                return []
            result = self.normalize_periods(special.periods_json or [])
            self._store_periods_cache[cache_key] = [dict(period) for period in result]
            return result

        self._load_weekly_store_rules()
        for closure in self._closures_cache:
            if closure.closure_type == "specific_date" and closure.closed_date == resolved_date:
                self._store_periods_cache[cache_key] = []
                return []
            if (
                closure.closure_type == "date_range"
                and getattr(closure, "start_date", None)
                and getattr(closure, "end_date", None)
                and closure.start_date <= resolved_date <= closure.end_date
            ):
                self._store_periods_cache[cache_key] = []
                return []
            if closure.closure_type == "monthly_weekday" and self._is_monthly_closed(resolved_date, closure):
                self._store_periods_cache[cache_key] = []
                return []

        weekday_key = WEEKDAY_KEYS[resolved_date.weekday()]
        business_hour = self._business_hours_cache.get(weekday_key)
        if not business_hour or business_hour.is_closed:
            self._store_periods_cache[cache_key] = []
            return []
        result = self.normalize_periods(business_hour.periods_json or [])
        self._store_periods_cache[cache_key] = [dict(period) for period in result]
        return result
```

## A2：別の営業時間関数：休業日を先に適用

出典：`kirato0905-cmyk/beauty-links-backend` / `api/business_hours.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L287〜L322](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/business_hours.py#L287-L322)

```python
def get_hours_for_date(
    target_date: date,
    *,
    store_id: Optional[Any] = None,
    store_code: Optional[str] = None,
) -> List[Dict[str, str]]:
    calendar_cfg = _calendar_config(store_id=store_id, store_code=store_code)

    if not isinstance(target_date, date):
        raise TypeError("target_date must be datetime.date")

    target_date_str = target_date.strftime("%Y-%m-%d")

    closed_dates = calendar_cfg.get("closed_dates", [])
    if target_date_str in closed_dates:
        return []

    monthly_closed = calendar_cfg.get("monthly_closed", [])
    for rule in monthly_closed:
        if not isinstance(rule, dict):
            continue
        weekday = rule.get("weekday")
        weeks = rule.get("weeks", [])
        if isinstance(weeks, list) and _is_nth_weekday_of_month(target_date, weekday, weeks):
            return []

    special_hours = calendar_cfg.get("special_hours", [])
    for item in special_hours:
        if not isinstance(item, dict):
            continue
        if item.get("date") == target_date_str:
            return _normalize_hours(item.get("hours", []))

    business_hours = calendar_cfg.get("business_hours", {})
    return _normalize_hours(business_hours.get(_weekday_key(target_date), []))
```

## A3：予約枠が不成立となる理由

出典：`kirato0905-cmyk/beauty-links-backend` / `api/services/availability_service.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L550〜L575](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/services/availability_service.py#L550-L575)

```python
    def get_availability_reason(
        self,
        staff: StaffMember,
        target_date: Any,
        start_time: Any,
        end_time: Any,
        exclude_reservation_id: Optional[str] = None,
    ) -> str:
        resolved_date = self.parse_date(target_date)
        store_periods = self.get_store_periods(resolved_date)
        if not store_periods:
            return "off"

        staff_periods = self.get_staff_periods(staff, resolved_date, store_periods)
        if not staff_periods:
            return "off"

        if not self.range_fits_periods(staff_periods, start_time, end_time):
            return "outside"

        for existing in self._active_reservations_for_staff(resolved_date, staff.name):
            if self._is_excluded_reservation(existing, exclude_reservation_id):
                continue
            if self.overlaps(start_time, end_time, existing.start_time, existing.end_time):
                return "busy"
        return "ok"
```

## A4：管理画面のセット所要時間の優先順

出典：`kirato0905-cmyk/beauty-links-backend` / `api/admin/routes.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L7415〜L7469](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/admin/routes.py#L7415-L7469)

```python
def _resolve_customer_featured_set_duration_for_admin(
    db: Session,
    admin: AdminContext,
    customer: Optional[Customer],
    featured_set: FeaturedSet,
    fallback_duration: int,
    prefer_service_override_duration: bool = False,
) -> tuple[int, str]:
    """管理画面予約用のセット所要時間解決。

    優先順位:
      1. customer_featured_set_duration_overrides.duration_minutes
      2. auto-detected set かつ単品顧客別所要時間がある場合、その合計
      3. featured_sets.duration_minutes
      4. 単品メニュー所要時間の合計
      5. fallback 60分
    """
    if customer:
        override = (
            db.query(CustomerFeaturedSetDurationOverride)
            .filter(
                CustomerFeaturedSetDurationOverride.store_id == admin.store_id,
                CustomerFeaturedSetDurationOverride.customer_id == customer.id,
                CustomerFeaturedSetDurationOverride.featured_set_id == featured_set.id,
                CustomerFeaturedSetDurationOverride.is_active.is_(True),
            )
            .first()
        )
        if override and int(override.duration_minutes or 0) > 0:
            return int(override.duration_minutes or 0), "customer_featured_set_override"

    # 管理画面では featured_set_id を明示せず、単品メニュー選択が
    # featured_set_services と完全一致しただけで「自動セット判定」になるケースがある。
    # その場合に featured_sets.duration_minutes を優先すると、
    # 顧客別の単品所要時間が反映されない。
    #
    # そのため、自動セット判定かつ単品側に顧客別所要時間がある場合は、
    # featured_sets.duration_minutes より単品顧客別所要時間の合計を優先する。
    if prefer_service_override_duration and int(fallback_duration or 0) > 0:
        return int(fallback_duration or 0), "customer_service_override_auto_set"

    if int(featured_set.duration_minutes or 0) > 0:
        return int(featured_set.duration_minutes or 0), "featured_set_default"

    if int(fallback_duration or 0) > 0:
        return int(fallback_duration or 0), "service_sum_fallback"

    return 60, "fallback"


def _resolve_admin_reservation_menu_for_admin(
    db: Session,
    admin: AdminContext,
    customer: Optional[Customer],
    ordered_services: List[Service],
```

## P1：誕生日手動配信の実行引数

出典：`kirato0905-cmyk/beauty-links-backend` / `api/admin/coupon_routes.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L543〜L568](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/admin/coupon_routes.py#L543-L568)

```python
@router.post("/birthday/run-now")
def run_birthday_coupon_now(
    confirmed: bool = Query(default=False),
    admin: AdminContext = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """今日の対象者へ誕生日クーポンを手動テスト配信するAPI。

    send_timeは無視する。誕生日/配布日前倒し条件は維持するが、
    テスト確認のため同じ顧客・同じ年でも毎回新しいクーポンを発行できる。
    自動スケジューラ側の年次重複防止は変更しない。
    """
    ensure_coupon_write(admin)
    if not confirmed:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"code": "CONFIRMATION_REQUIRED", "message": "実行には確認が必要です。"},
        )
    birthday = BirthdayCouponService(db, admin.store_id, timezone_name=admin.timezone)
    result = birthday.run_due(
        force_time=True,
        allow_repeat_per_customer=True,
    )
    db.commit()
    return {"success": True, "data": result}
```

## P2：誕生日配信対象の絞り込み

出典：`kirato0905-cmyk/beauty-links-backend` / `api/services/birthday_coupon_service.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L312〜L334](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/services/birthday_coupon_service.py#L312-L334)

```python
    def _eligible_customers(self, target_birthday: date, *, require_consent: bool) -> List[Customer]:
        query = self.db.query(Customer).filter(
            Customer.store_id == self.store_id,
            Customer.deleted_at.is_(None),
            Customer.status == "active",
            Customer.birthday.is_not(None),
            Customer.line_user_id.is_not(None),
        )
        if require_consent:
            query = query.filter(Customer.consented.is_(True))
        rows = query.order_by(Customer.id.asc()).all()
        eligible: List[Customer] = []
        for customer in rows:
            line_user_id = str(customer.line_user_id or "").strip()
            if not line_user_id or line_user_id.startswith("admin_manual:"):
                continue
            birthday = customer.birthday
            if not birthday:
                continue
            resolved = _birthday_for_year(birthday, target_birthday.year)
            if resolved == target_birthday:
                eligible.append(customer)
        return eligible
```

## P3：手動配信は年次重複防止とは別の発行

出典：`kirato0905-cmyk/beauty-links-backend` / `api/services/birthday_coupon_service.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L430〜L455](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/services/birthday_coupon_service.py#L430-L455)

```python
        delivery_service = CouponDeliveryService(self.db, self.store_id)

        for customer in customers:
            # Automatic delivery keeps the stable annual source key so the scheduler
            # remains idempotent. Manual test delivery gets a unique source key and
            # explicitly allows repeated coupons for the same customer.
            if allow_repeat_per_customer:
                source_key = (
                    f"birthday-test:{customer.id}:{target_birthday.year}:"
                    f"{uuid.uuid4().hex}"
                )
                existing = None
            else:
                source_key = f"birthday:{customer.id}:{target_birthday.year}"

            try:
                if not allow_repeat_per_customer:
                    existing = coupon_service.repository.offered_coupon_for_source(
                        campaign_id=campaign.id,
                        customer_id=customer.id,
                        source_key=source_key,
                    )
                row = coupon_service.offer(
                    campaign_id=campaign.id,
                    customer_id=customer.id,
                    source_type=BIRTHDAY_SOURCE_TYPE,
```

## P4：紹介された方の初回来店済みで判定

出典：`kirato0905-cmyk/beauty-links-backend` / `api/services/referral_service.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L945〜L957](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/services/referral_service.py#L945-L957)

```python
    def process_completed_reservation(self, reservation: Reservation) -> Optional[Dict[str, Any]]:
        if not reservation or reservation.store_id != self.store_id or reservation.status != "completed":
            return None
        if not reservation.customer_id:
            return None
        referral = (
            self.db.query(CustomerReferral)
            .filter(
                CustomerReferral.store_id == self.store_id,
                CustomerReferral.referred_customer_id == reservation.customer_id,
                CustomerReferral.status.in_(["registered", "qualified", "rewarded"]),
            )
            .with_for_update()
```

[元コード L993〜L1024](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/services/referral_service.py#L993-L1024)

```python
                return {"qualified": False, "reason": "reservation_before_referral_registration"}

        earlier = (
            self.db.query(Reservation.id)
            .filter(
                Reservation.store_id == self.store_id,
                Reservation.customer_id == reservation.customer_id,
                Reservation.status == "completed",
                Reservation.deleted_at.is_(None),
                Reservation.id != reservation.id,
                Reservation.completed_at.is_not(None),
                Reservation.completed_at < (reservation.completed_at or self.now()),
            )
            .first()
        )
        if earlier:
            referral.status = "rejected"
            referral.rejection_reason = "not_first_completed_visit"
            self.db.flush()
            return {"qualified": False, "reason": "not_first_completed_visit"}

        referral.status = "qualified"
        referral.qualified_reservation_id = reservation.id
        referral.qualified_at = reservation.completed_at or self.now()
        referral.rejection_reason = None
        self.db.flush()

        # Make sure the referred-side registration reward is not missed.
        if self.ensure_settings().referred_reward_enabled and not referral.referred_coupon_id:
            self.issue_referred_reward(referral)

        reward = self.issue_referrer_reward(referral)
```

## T1：発送登録から送る内容

出典：`kirato0905-cmyk/BeautyLinks_admin_web` / `components/admin/RetailProposalPanel.tsx`
確認コミット：`6d6e049850867421c7c41f80190d64123ef1ff0b`

[元コード L1193〜L1213](https://github.com/kirato0905-cmyk/BeautyLinks_admin_web/blob/6d6e049850867421c7c41f80190d64123ef1ff0b/components/admin/RetailProposalPanel.tsx#L1193-L1213)

```tsx
  async function shipOrder(order: RetailOrderRow) {
    const draft = shipmentDraft(order);
    const ok = await confirm({
      title: "発送完了にしますか？",
      description:
        "注文を発送済みに変更し、お客様へ発送完了LINEを送信します。",
      confirmLabel: "発送完了にする",
      danger: false,
    });
    if (!ok) return;

    await runAction(`ship-${order.id}`, async (accessToken) => {
      const payload: RetailShipmentPayload = {
        carrier_code: YAMATO_CARRIER_CODE,
        shipping_note: draft.shipping_note,
      };
      const response = await shipAdminRetailOrder(
        accessToken,
        order.id,
        payload,
      );
```

## T2：現行発送フォームは発送メモ

出典：`kirato0905-cmyk/BeautyLinks_admin_web` / `components/admin/RetailProposalPanel.tsx`
確認コミット：`6d6e049850867421c7c41f80190d64123ef1ff0b`

[元コード L1939〜L1968](https://github.com/kirato0905-cmyk/BeautyLinks_admin_web/blob/6d6e049850867421c7c41f80190d64123ef1ff0b/components/admin/RetailProposalPanel.tsx#L1939-L1968)

```tsx
                            <h5>発送後、発送完了にする</h5>
                            <div className="retailShipmentForm">
                              <label>
                                <span>発送メモ（任意）</span>
                                <input
                                  value={draft.shipping_note}
                                  onChange={(event) =>
                                    patchShipment(order.id, {
                                      shipping_note: event.target.value,
                                    })
                                  }
                                  placeholder="例：セブン‐イレブンから発送"
                                />
                              </label>
                            </div>
                            <p className="retailProcedureNote">
                              荷物をコンビニまたはヤマト営業所へ預けた後に
                              押してください。お客様へ発送完了LINEが送信されます。
                            </p>
                            <div className="retailProcedureActions">
                              <button
                                className="primary"
                                type="button"
                                onClick={() => void shipOrder(order)}
                                disabled={Boolean(actionKey)}
                                aria-busy={actionKey === `ship-${order.id}`}
                              >
                                {actionKey === `ship-${order.id}`
                                  ? "発送処理中..."
                                  : "発送完了にしてLINEを送る"}
```

## T3：画面の返金は残りの対象額すべて

出典：`kirato0905-cmyk/BeautyLinks_admin_web` / `components/admin/RetailProposalPanel.tsx`
確認コミット：`6d6e049850867421c7c41f80190d64123ef1ff0b`

[元コード L1377〜L1397](https://github.com/kirato0905-cmyk/BeautyLinks_admin_web/blob/6d6e049850867421c7c41f80190d64123ef1ff0b/components/admin/RetailProposalPanel.tsx#L1377-L1397)

```tsx
  async function refundOrder(order: RetailOrderRow) {
    const remaining = Number(order.refundable_amount || 0);
    if (remaining <= 0) return;
    const ok = await confirm({
      title: "この注文を全額返金しますか？",
      description: `${order.order_code}／${order.product_name}を${money(remaining)}返金します。発送前・未受取の商品は在庫へ戻します。`,
      confirmLabel: "返金する",
      danger: true,
    });
    if (!ok) return;
    await runAction(`refund-${order.id}`, async (accessToken) => {
      await refundAdminRetailOrder(accessToken, order.id, {
        amount: remaining,
        reason: "requested_by_customer",
        restock: !["completed", "shipped", "delivered"].includes(order.status),
      });
      setNotice("Stripe返金を受け付けました。");
    });
  }

  if (loading) return <div className="retailEmpty">店販情報を読み込んでいます...</div>;
```

## T4：一括発送準備の対象と結果

出典：`kirato0905-cmyk/BeautyLinks_admin_web` / `components/admin/RetailProposalPanel.tsx`
確認コミット：`6d6e049850867421c7c41f80190d64123ef1ff0b`

[元コード L1277〜L1308](https://github.com/kirato0905-cmyk/BeautyLinks_admin_web/blob/6d6e049850867421c7c41f80190d64123ef1ff0b/components/admin/RetailProposalPanel.tsx#L1277-L1308)

```tsx
  async function bulkPrepareSelectedOrders() {
    const ids = selectedShippingOrders
      .filter((order) => order.status === "paid")
      .map((order) => order.id);

    if (ids.length === 0) {
      setError("決済済みの配送注文を選択してください。");
      return;
    }

    const ok = await confirm({
      title: `${ids.length}件を発送準備中にしますか？`,
      description:
        "選択した決済済み配送注文を一括で発送準備中へ変更します。",
      confirmLabel: "一括で発送準備",
      danger: false,
    });
    if (!ok) return;

    await runAction("bulk-prepare", async (accessToken) => {
      const response =
        await bulkPrepareAdminRetailShippingOrders(
          accessToken,
          ids,
        );

      setNotice(
        `${response.data.success_count}件を発送準備中にしました。`
        + `失敗 ${response.data.failed_count}件。`,
      );
    });
  }
```

## T5：原価などが不明なら利益は未算出

出典：`kirato0905-cmyk/beauty-links-backend` / `api/services/retail_order_finance_service.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L266〜L286](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/services/retail_order_finance_service.py#L266-L286)

```python
    @staticmethod
    def serialize(order, row):
        snapshot = dict(row.stripe_snapshot_json or {})
        current = snapshot.get("order_refunded_amount") == int(order.refunded_amount or 0)
        ready = current and snapshot.get("state") == "ready" and not snapshot.get("sync_error")
        net = snapshot.get("net_received") if ready else None
        shipping_cost = row.shipping_cost if order.pickup_method == "shipping" else 0
        profit = net - row.product_cost - shipping_cost if net is not None and row.product_cost is not None and shipping_cost is not None else None
        return {
            "order_id": str(order.id), "currency": order.currency or "jpy",
            "shipping_fee": int(order.shipping_fee or 0), "shipping_cost": shipping_cost,
            "product_cost": row.product_cost, "payment_fees": snapshot.get("payment_fees") if ready else None,
            "net_received": net, "profit": profit,
            "payout_date": snapshot.get("payout_date") if current else None,
            "payout_date_kind": snapshot.get("payout_date_kind", "unknown") if current else "unknown",
            "payout_status": snapshot.get("payout_status", "unknown"),
            "payout_schedule": snapshot.get("payout_schedule", ""),
            "balance_available_date": snapshot.get("balance_available_date"),
            "note": snapshot.get("note", ""), "sync_error": bool(snapshot.get("sync_error")),
            "stripe_environment": stripe_environment_for_order(order),
            "synced_at": row.synced_at.isoformat() if row.synced_at else None,
```

## X1：閲覧者の書き込みはサーバー側で拒否

出典：`kirato0905-cmyk/beauty-links-backend` / `api/admin/routes.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L164〜L174](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/admin/routes.py#L164-L174)

```python
def ensure_viewer_cannot_write(admin: AdminContext) -> None:
    """閲覧者権限は管理画面の追加・変更・削除・編集系APIを実行できない。"""
    role = _normalized_admin_role(admin)
    if role == "viewer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail={
                "code": "VIEWER_WRITE_FORBIDDEN",
                "message": "閲覧のみ権限では、追加・変更・削除・編集はできません。",
            },
        )
```

## X2：売上向上はサイドバーで追加条件がある

出典：`kirato0905-cmyk/BeautyLinks_admin_web` / `components/admin-sidebar.tsx`
確認コミット：`6d6e049850867421c7c41f80190d64123ef1ff0b`

[元コード L1069〜L1103](https://github.com/kirato0905-cmyk/BeautyLinks_admin_web/blob/6d6e049850867421c7c41f80190d64123ef1ff0b/components/admin-sidebar.tsx#L1069-L1103)

```tsx
    if (item.allowedRoles.length === 0) return false;

    if (item.key === "automation") {
      // 売上向上は権限のあるロールだけに表示する。
      // staff / viewer には、Growth選択中・支払い済みかどうかに関係なく表示しない。
      const automationRoleAllowed =
        adminRole === "owner" ||
        adminRole === "manager" ||
        adminRole === "platform_admin" ||
        adminRole === "service_admin";

      if (!automationRoleAllowed) {
        return false;
      }

      // BeautyLinks運営者は店舗の契約プランに関係なく、
      // サポート・検証用として売上向上を常に表示する。
      if (operatorBillingBypass) {
        return true;
      }

      // 通常のowner/managerはGrowthを選択した時点で表示する。
      // 未払いなら後段でロック表示にし、クリックはできない。
      // プラン変更直後などで旧Growth entitlementが有効な間は
      // selected=false でも effective=true なら引き続き表示する。
      return (
        !billingStateReadyForSelectedStore ||
        effectiveSalesGrowthSelected ||
        effectiveSalesGrowthEnabled
      );
    }

    if (item.key === "platformStores") {
      return (
        (adminRole === "platform_admin" ||
```

## X3：契約の利用権と猶予期間

出典：`kirato0905-cmyk/beauty-links-backend` / `api/services/billing_access_service.py`
確認コミット：`da44d42f18366ffd824ee77d0a0d5ada9e3af059`

[元コード L75〜L107](https://github.com/kirato0905-cmyk/beauty-links-backend/blob/da44d42f18366ffd824ee77d0a0d5ada9e3af059/api/services/billing_access_service.py#L75-L107)

```python
def subscription_access_is_effective(
    subscription: Optional[StoreSubscription],
    *,
    now: Optional[datetime] = None,
) -> bool:
    """Return True when the current paid/trial BeautyLinks entitlement is valid."""
    if subscription is None:
        return False

    # access_enabled is set only after the Stripe paid-entitlement flow succeeds.
    if not bool(getattr(subscription, "access_enabled", False)):
        return False

    # A valid paid entitlement must identify what was actually paid for.
    if not str(getattr(subscription, "entitled_plan_code", "") or "").strip():
        return False

    status_value = str(getattr(subscription, "status", "") or "").strip().lower()
    if status_value in {"active", "trialing"}:
        return True

    if status_value not in GRACE_ELIGIBLE_STATUSES:
        return False

    grace_end = _utc_datetime(getattr(subscription, "grace_period_ends_at", None))
    if grace_end is None:
        return False

    current = subscription_reference_now(
        subscription,
        now=now,
    )
    return current < grace_end
```

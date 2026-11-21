---
name: abandoned-carts
description: Recover a Zid store's abandoned carts. Use to see how many carts are abandoned and where checkout stops, set up or tune Zid's automatic cart reminders with a discount or free-shipping offer, prepare the reminder coupon and WhatsApp text, list high-value carts for the merchant to follow up, or measure recovered sales.
---

# Abandoned carts

Finds where shoppers drop out, sets up the store's own reminders, and measures
what comes back.

## Ground rules

- The merchant's explicit instructions take precedence over this skill.
- Reminders go through Zid's own reminder settings or the merchant's tools; this
  skill configures and measures them.
- Show each setting change and coupon before making it and apply it after the
  merchant agrees. When a manage tool answers `confirmation_required`, compare
  its plan with what the merchant approved: if they match, repeat the call with
  its `plan_id`; if not, show the plan and ask again.
- A discount code in an SMS is promotional: Zid sends it only from a promotional
  sender name (ending in `AD`). WhatsApp reminder texts go to Meta for approval
  before they send; email and SMS start when saved.

## 1. Read the carts

- `zid_orders.list_abandoned_carts` with `dateFrom`, `dateTo`, `pageSize` 100,
  every page; filter with `phase`, `cartTotal`, `productsCount`. One cart with
  its products and customer: `zid_orders.get_abandoned_cart`.
- Rates and recovered sales: `zid_reports.abandoned_carts_rate` and
  `zid_reports.abandoned_cart_sales` (when reports are available for the store).

## 2. Find where checkout stops

Count carts and value by `phase`: `new`, `login`, `shipping_address`,
`shipping_method`, `payment_method`, `verification`, and `completed` (recovered,
reported separately). The phase with the most
value points to the setting to look at: shipping prices and methods for
`shipping_method`, payment options for `payment_method`, and the sign-in step
for `login`. Report the counts; the merchant decides what to change.

Done when every cart in the period sits in one phase and the phase totals add up
to the period total.

## 3. Automatic reminders

1. `zid_campaigns.get_auto_reminder` and
   `zid_campaigns.list_abandoned_cart_reminders` show what runs today.
2. An offer needs a coupon that applies by code. Check that the code is free with
   `zid_promotions.list_coupons` (`searchTerm`), then
   `zid_promotions_manage.create_coupon` with `name`, `code`, `discountType`
   (`p` percent or `f` fixed), `discount`, `dateStart`, `dateEnd`,
   `usesCustomer` 1 and `applyingMethod` `CODE`. A "code already used" error
   means another coupon has it: pick a new code.
3. `zid_campaigns_manage.update_auto_reminder`: `offerType` (`discount`,
   `free_shipping` or `no_offer`), `offerCouponId`, `cartTotal` (the minimum),
   `sendAfter` (hours) and `phases`.
4. `zid_campaigns_manage.set_auto_reminder_status` with `enabled` true.
5. The text the merchant starts from when contacting a cart's customer on
   WhatsApp: `zid_campaigns.get_cart_whatsapp_message` and
   `zid_campaigns_manage.set_cart_whatsapp_message` (up to 1,000 characters).

## 4. High-value carts

List carts above the merchant's threshold with cart id, customer name, products,
value and age, newest first; add contact details only when the merchant asks. The merchant contacts them from the dashboard
(Orders → Abandoned carts, single or bulk alert) or their WhatsApp tool.

## 5. Measure

After 7 and 30 days, compare abandoned value, recovered orders and the coupon's
use (`zid_promotions.list_coupons` or `zid_reports.coupon_performance`) with the
period before the change.

## Output

Carts and value by phase, the reminder setup before and after, the coupon, the
high-value list, and the recovery figures when measuring.

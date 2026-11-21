---
name: order-fulfillment
description: Run a Zid store's order fulfillment with its courier, fulfillment center or own drivers. Use for daily batches to preparing or ready, prep lists and waybills, tracking numbers and delivered updates, and reconciling a courier or fulfillment-center report against Zid orders, including cash on delivery.
---

# Order fulfillment

Moves orders through fulfillment and keeps Zid's order statuses in line with what
the courier or fulfillment center reports.

## Ground rules

- The merchant's explicit instructions take precedence over this skill.
- Batches: show the full change list (a table when it covers more than a few
  orders) and apply it after the merchant agrees. When a manage tool answers
  `confirmation_required`, compare its plan with what the merchant approved: if
  they match, repeat the call with its `plan_id`; if not, show the plan and ask again.
- After writing, read the orders back and report what changed, what was skipped
  and what failed, with the reason.
- On a `429` answer, wait the seconds it names, then continue one call at a time.
- Courier credentials (API keys, passwords, tokens) stay in the courier's portal
  or the merchant's automation tool; when a step needs one, tell the merchant
  where to enter it.
- Refunds, payment status changes and shipment cancellations are done in the Zid dashboard.

## Order statuses

`new` → `preparing` → `ready` → `indelivery` → `delivered`. `cancelled` ends an
order before delivery. Stores can add custom statuses
(`zid_orders.list_custom_statuses`); bulk changes accept their codes.

## 1. Scope the run

Settle these before reading:

- **Orders**: statuses, date range, payment status and shipping method.
- **Carrier**: Zid Ship, a courier or fulfillment center with its own Zid app,
  or the merchant's drivers. `zid_account.list_installed_apps` shows the apps.
- **Who moves statuses**: look the carrier up in
  [references/carriers.md](references/carriers.md). Where the carrier's own
  connection moves statuses and adds tracking, this run reads and reconciles,
  so the two writers stay out of each other's way.
- **Pickup location**: `zid_inventory.list_locations`.

Done when you can state the filter, the carrier, who moves statuses, and the location.

## 2. Read the orders

`zid_orders.list_orders` with `status`, `dateFrom` and `dateTo` (YYYY-MM-DD),
`paymentStatus` and `perPage` 100, every page. For items and addresses call
`zid_orders.get_order`; for the warehouse that fulfils each line call
`zid_orders.get_fulfillment_inventories`.

Prepaid orders ship once paid; cash-on-delivery orders are collected at the
door. Put any other order (unpaid prepaid, missing address) on hold with the reason.

## 3. Move a batch

- **What `ready` sets off**: with Zid Ship, moving an order to `ready` sends the
  request to the courier and issues the waybill; Zid Ship runs on the store's
  wallet balance, so check it covers the batch. Some couriers' apps also book a
  pickup at `ready`. Say this in the change list before the merchant approves a
  move to `ready`.
- **Many orders**: `zid_orders_manage.bulk_set_order_status` with `orderIds` (up
  to 500) and `status`. Moving to `ready` can need `inventoryAddressId` (the
  pickup location) and `packagesCount` (1 to 99); add them when the call asks.
  It returns a `batchId`: read each order's result with
  `zid_orders.get_bulk_action_status` and report failures one by one. Where bulk
  changes are not available for the store, use
  `zid_orders_manage.update_order_status` per order.
- **Shipped with tracking**: `zid_orders_manage.update_order_status` with
  `orderId`, `orderStatus` `indelivery`, `trackingNumber`, `trackingUrl`, and
  `waybillUrl` when the merchant has one.
- **Delivered**: the same action with `orderStatus` `delivered`.
- **Notes for the team**: `zid_orders_manage.add_order_comment` (1 to 255
  characters); a batch label: `zid_orders_manage.add_order_tag`.

Cancel or return an order only when the merchant asks for that specific order.

## 4. Prep lists and waybills

- **Prep list emailed by Zid**: `zid_orders_manage.export_prep_list` with
  `statuses`, `dateFrom` and `dateTo`. It covers every order matching the
  filters.
- **Prep list in chat**: from step 2, one row per SKU with the total quantity,
  then the lines of each order.
- **Waybills**: `zid_shipping.get_waybills` with up to 100 `orderIds`, for any
  carrier (`includeInvoice` true adds the invoice). Where bulk printing is not
  available, call it once per order.

## 5. Reconcile with the carrier

1. Get the carrier's view: the report the merchant uploads (where to export it:
   [references/carriers.md](references/carriers.md)), or for Zid Ship
   `zid_shipping.list_shipments` (`dateFrom` and `dateTo` together, `pageSize`
   up to 100; filter codes from `zid_shipping.list_shipment_filters`),
   `zid_shipping.track_shipment` by `orderId`, and the cash couriers collected in
   `zid_shipping.list_cod_collected`.
2. Find the report's order-number and tracking-number columns by matching their
   values against the Zid orders, not by the header names, and map its statuses
   with the status map in [references/carriers.md](references/carriers.md).
3. Match each shipment to an order by order number, then by tracking number.
4. Put every order in scope in exactly one class:
   - matched: statuses agree;
   - not booked: in Zid, missing from the carrier;
   - unknown: with the carrier, missing from Zid;
   - behind: the carrier is further along than Zid (for example delivered while Zid shows `indelivery`);
   - exception: the carrier reports a failed delivery, return, refusal, damage or loss;
   - cash mismatch: collected amount differs from the order total in the same currency;
   - stuck: no carrier update for longer than the merchant's limit (default 3 days).
5. Offer the status updates for the behind class as one batch (step 3). Leave
   exception orders at their last true status and list them for the merchant;
   offer a custom status when the store has one for returns or failed deliveries.

Done when every order in scope sits in one class and the counts add up to the total.

## Output

- **Batch**: counts per status before and after, then failures with the reason.
- **Reconciliation**: a table of order, tracking number, Zid status, carrier
  status, expected cash, collected cash and class, followed by the counts per
  class.

To run this every day without a chat, use the `zid-ops` skill for a scheduled
job, or the `zid-api` skill to build an app that reacts to order events.

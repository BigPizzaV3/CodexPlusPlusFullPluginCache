---
name: customer-sync
description: Move Zid customers between the store and a CRM, email or WhatsApp marketing tool, or loyalty system such as Mailchimp, Klaviyo, HubSpot, Zoho CRM, Brevo or a WhatsApp broadcast app. Use to build a contact file that carries marketing consent, segment customers by value or recency, tag Zid customers from an outside segment, or bring loyalty points in line with another system.
---

# Customer sync

Keeps customer records, segments and loyalty points consistent between Zid and
the merchant's marketing tools, without sending anyone a message they did not agree to.

## Ground rules

- The merchant's explicit instructions take precedence over this skill.
- Consent travels with the contact. Zid's newsletter subscription is the email
  marketing consent; SMS and WhatsApp consent comes only from a recorded opt-in.
  Unknown consent is "not subscribed".
- Export only the fields the destination needs.
- Show the full change list and apply it after the merchant agrees. When a
  manage tool answers `confirmation_required`, compare its plan with what the
  merchant approved: if they match, repeat the call with its `plan_id`; if not,
  show the plan and ask again.
- Destination credentials (API keys, tokens) stay in that tool or the merchant's
  automation tool. Customer wallet balances are changed in the Zid dashboard.

## 1. Direction and owner

Settle which way the data flows (Zid → tool, tool → Zid, or both) and whether a
connector app already syncs it: `zid_account.list_installed_apps`, then
[references/destinations.md](references/destinations.md). With a connector in
place, compare the two sides and report differences instead of writing.

## 2. Read Zid customers

- `zid_customers.list_customers` with `perPage` 100, every page. Filters:
  `isNewsletterSubscriber`, `dateFrom` and `dateTo` (sign-up), `ordersCountCompare`
  with `ordersCountValue`, `tagIds`, `groupIds`, `customerChannels`.
- Value and recency: `zid_reports.customers_report` (lifetime value, orders and
  last order per customer; `page_size` up to 100), or `zid_reports.top_customers`.
- Large stores: `zid_customers_manage.export_customers` with `filters` emails the
  merchant a spreadsheet of customers' personal data; it needs the merchant's
  approval. Ask them to share only the columns the destination needs.

## 3. Segment

Default segments, unless the merchant defines their own:

| Segment | Rule |
| --- | --- |
| VIP | Top 10% by lifetime value, ordered in the last 90 days |
| Lapsed VIP | Top 10% by lifetime value, no order in 90 days |
| Repeat | 2 or more orders, ordered in the last 90 days |
| Lapsed | Ordered before, nothing in 90 days |
| New | First order in the last 30 days |
| Never ordered | Account without orders |

## 4. Zid → destination

Build one row per customer with the destination's headers from
[references/destinations.md](references/destinations.md):

- phone in international format (`+9665…`), email, first and last name;
- segment and tags as the destination's tags or properties;
- consent per channel: email from `isNewsletterSubscriber`; SMS and WhatsApp
  only where the merchant has a recorded opt-in.

Split the file at the destination's row limit.

Done when every customer in scope is either in the file or in the skipped list
with a reason.

## 5. Destination → Zid

- **Tags**: `zid_customers_manage.add_customer_tag` (`customerId`, `name`) adds
  one; `zid_customers_manage.set_customer_tags` (`customerId`, `tagNames`)
  replaces the customer's tags, so include the ones to keep.
- **Groups** are rule-based: `zid_customers_manage.create_customer_group` with
  `name` and `filters`. Members cannot be added one by one; tag them and build
  the group on the tag.
- **Email consent**: `zid_customers_manage.set_customer_marketing`
  (`customerId`, `subscribed`), only from a recorded opt-in or opt-out.
- **New or changed customers**: match by mobile, then email; create with
  `zid_customers_manage.create_customer` (`name`, `mobile`) or update with
  `zid_customers_manage.update_customer`.

## 6. Loyalty points

`zid_promotions.get_loyalty_status` confirms the program is on. For each
customer: `zid_promotions.get_customer_points`, the difference to the target
balance, then `zid_promotions_manage.adjust_customer_points` with `customerId`,
`direction` (`+` or `-`), `points` and a `reason` naming the source system.
`zid_promotions.get_customer_points_history` explains a balance.

## Output

Counts per segment, the contact file or the change list, then rows skipped with
the reason (no phone or email, no consent, no match, duplicate).

To keep the sync running daily, use the `zid-ops` skill.

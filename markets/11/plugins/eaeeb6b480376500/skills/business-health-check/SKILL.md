---
name: business-health-check
description: Use when the user asks a broad question about their Amazon business ("how's my business?", "anything to worry about?", "how did we do last month?"). Produces a short health check covering sales, top products, alerts, advertising and inventory.
---

# Amazon business health check

1. Call `list_accounts`. Use the accounts and marketplaces it returns, and call only the tools listed in each account's `available_tools`. If the user has several accounts and did not name one, cover each briefly or ask which one matters most.
2. Do not ask the user to narrow a vague question first. Fetch this bundle for the account (default window: last 30 days, compared with the preceding period):
   - Seller accounts: `seller_analytics` with `dataset=portfolio_summary`, `dataset=asin_sales_ranking` (`limit=10`) and `dataset=sales_alerts`; `advertising_analytics` with `dataset=alerts` when the account has advertising data; `inventory_analytics` with `dataset=health`.
   - Vendor accounts: `vendor_analytics` with `dataset=ordered_revenue`, `dataset=shipped_revenue` and `dataset=ordered_revenue_by_asin` (`limit=10`); `inventory_analytics` with `dataset=health`.
3. Write the answer in this order: headline (sales and the change versus the comparison period, with the dates used), top products driving the change, alerts that need action, advertising efficiency, inventory risks (stockouts, excess stock).
4. Report only numbers the tools returned. When a dataset returns `data_status: "no_data"`, say that data is not available for the period rather than reporting zeros.
5. Finish with at most three concrete next steps the user could take.

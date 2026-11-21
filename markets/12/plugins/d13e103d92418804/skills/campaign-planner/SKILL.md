---
name: campaign-planner
description: Plan discounts and promotions for a WooCommerce store from real sales and stock data. Use when the owner asks what promotion to run, how to clear slow stock, win back customers, or grow order size.
---

1. Call `suggest_campaigns`. Each idea includes the reason and ready-to-use settings for `create_coupon` or `update_products`.
2. Optionally call `customer_segments` (for example `segment: "lapsed"`) to size a win-back idea. Never reveal customers' emails; Gridly does not return them.
3. Explain two or three ideas in plain language with the reason from the data, then ask which one to set up.
4. Set it up with the normal two-step flow (preview, owner approves, then confirm). Offer `apply_at` if the owner wants it to start on a date.
5. Gridly does not send marketing emails. If a win-back idea needs emailing customers, say the owner should do that from their own email tool.

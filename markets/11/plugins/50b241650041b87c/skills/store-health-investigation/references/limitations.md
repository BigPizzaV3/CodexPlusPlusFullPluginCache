# What Eskopia can't see

Say these are unknown rather than guessing:

- Site uptime, page speed, storefront errors
- Payment gateway failures or declines
- Price, theme, app, content or shipping-setting changes made in Shopify
- Inventory and stock-outs
- Ad campaigns, ad spend, email sends, marketing changes
- UTM tags, and which ad or campaign a visit came from (traffic source is the referring site only)
- Refunds and cancellations
- Sales for orders whose product lines weren't stored (check `coverage` in `get_product_sales`; refunds are never subtracted)
- Shoppers' personal data (names, emails, order numbers and IP addresses are never returned; the merchant can see those in the Eskopia web app or Shopify admin)
- Live visitor counts from the past (live presence isn't stored; recent-window visitor counts are)

Measurement caveats to mention when relevant:

- Visitor country and city come from the IP address; an order's country and city come from the order itself (normally the shipping address). Say which one a number is when it matters.
- Traffic source, landing page, device and new/returning describe a visitor's first event in the window. Orders with no pixel-tracked checkout can't be attributed and show as "Not linked to a tracked visit".
- A group with fewer than 30 visitors is too small for a reliable conversion rate.

- Shoppers who block tracking or haven't consented may not be counted by the pixel, so visitors are a lower bound and conversion can read high.
- A tracking_gap or webhook_gap anomaly means Eskopia's data for that period is incomplete: say so before drawing conclusions.
- Detections use fixed thresholds; a quiet store gets "not enough data" rather than detections.

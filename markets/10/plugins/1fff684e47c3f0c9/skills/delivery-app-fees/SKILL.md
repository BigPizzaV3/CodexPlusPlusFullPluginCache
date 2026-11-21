---
name: delivery-app-fees
description: Work out what delivery apps (DoorDash, Uber Eats, Grubhub) cost a restaurant per month, year and order, from the owner's own numbers. Works without an account.
---

1. Ask for monthly sales through the delivery apps. Ask for the commission rate and orders per month if they know them (both are on the apps' monthly statements), and any other monthly app charges (ads, promotions, tablet fees).
2. Call `estimate_delivery_app_fees`. If they didn't know the rate, show the common levels it returns and say which one their statement will show.
3. Present the monthly, yearly and per-order totals, and how they were worked out.
4. Keep it balanced: delivery apps also bring drivers and new customers. Use the `limitations` the tool returns. Don't tell the owner to leave the apps, and don't promote ServeStack.

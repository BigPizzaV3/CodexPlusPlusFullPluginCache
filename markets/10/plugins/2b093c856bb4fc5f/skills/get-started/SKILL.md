---
name: get-started
description: Find local businesses on the island of Ireland with LocallyIrish, check their details and opening status, and request quotes from local tradespeople.
---

# LocallyIrish

Use LocallyIrish when someone wants a local business in Ireland or Northern
Ireland: a trade (plumber, electrician, roofer), a shop, a café or restaurant,
a salon, a solicitor, and so on.

## Tools

- `search_businesses`: find businesses by trade or category and, optionally,
  county. Set `open_now` when the person wants somewhere open at the moment.
  Returns up to 25 listings, each with a locallyirish.ie link.
- `get_business`: full details for one business by its slug (the last part of
  its locallyirish.ie/business/... URL): address, phone, website, rating and
  whether it is open now.
- `request_quote`: send a quote request on the person's behalf. Only use it
  when the person asks for quotes and has given their own name and email (phone
  and job details optional). Every request is reviewed by the LocallyIrish team
  before it is forwarded to matching businesses.

## Good to know

- Coverage is the island of Ireland only. For places elsewhere, say so.
- Share the listing link with each business so the person can check it.
- There is no booking tool: for bookings, give the phone number or website.

---
name: start-quote-request
description: Start or update a Home Holding quote request for a signed-in customer. Use when they want a kitchen/cabinetry quote, colours, sizes, or a measurement visit. Returns a REQ- code. Never claims a quotation or sales invoice was created.
---

# Start / update quote request

1. Confirm they want a **quote request** (not an existing invoice lookup).
2. Call `start-quote-request-tool` (or `update-quote-request-tool` if they already have a REQ code).
3. Put rooms, colours, approximate meters in `wizard_payload` JSON.
4. Tell them their **request_code** clearly. Explain Home Holding will confirm before a formal quotation exists.
5. Offer `request-measurement-visit-tool` when they are ready for an appointment.

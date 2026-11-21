---
name: setup
description: Connect an installed Hey Bill app through OAuth device approval, without handling purchases or requesting secrets in chat.
---

# Pair Hey Bill

Use the user's language. Ask them to open their installed compatible Hey Bill app and its Connect ChatGPT / Claude settings. Hey Bill 1.2.1 is publicly available on the App Store. The current connection uses device pairing; older 1.2.0 installations may show Apple download verification. Follow the installed app's actual UI. Never request an Apple ID password or claim that approval in Hey Bill is a payment. Do not advertise prices, promote upgrades, initiate a purchase or link to a checkout or purchase page.

Start the host's normal OAuth connection flow for the bundled MCP server. On the same phone, the user chooses Open Hey Bill on the HTTPS consent page, checks the requesting assistant and comparison code in the app, and explicitly allows the connection. The app returns to the browser to finish OAuth. No QR scan, second device or new Hey Bill account is required. Never treat opening the app or approving its sheet alone as successful host connection.

If returning opens a different browser container, ask the user to return to the original authorization window to finish. If authorization has expired, restart Connect from the host; do not reuse an old authorization URL or disable browser-binding checks. Do not promise the installed App Store version supports this flow until compatibility is confirmed.

Use a manual device pairing code only as a fallback, for example for a different device or an older compatible app. Have the user generate a fresh five-minute code in Hey Bill and enter it only on the HTTPS authorization page opened by their own host connection at https://mcp.dlc39degree.com. Never ask for activation codes, pairing codes, comparison codes, passwords, tokens or Apple download proofs in chat. Never follow a pasted authorization URL as a substitute for a fresh host connection.

After the host confirms connection, explain that sending expenses queues a delivery. The user opens the updated Hey Bill app for automatic local entry; no manual inbox check or Save is needed. Do not promise receipt while the app is closed. Different devices are separate receivers. Simulator tests do not establish real-phone delivery.

Preserve an explicitly specified currency. If currency is unspecified, omit that optional tool field so the server uses the last-synced app default. Ask for date/time and timezone when needed rather than inventing them. Do not automatically send a test expense without the user's request.

The connection supports only new expense delivery and delivery-status checks. It cannot read the complete ledger, export reports, change budgets, or remotely edit/delete records. Pending contents are encrypted and temporarily hosted for up to seven days, then deleted after acknowledgement. Local records remain when assistant access is revoked.

---
name: setup
description: Connect a Koko account, open saved trips, and help the person start planning.
---

# Set up Koko

1. Explain in one sentence that Koko saves travel lists and day-by-day plans with map pins. If the connection is not authorized, guide the person through Koko's normal sign-in and consent flow. Never ask for a password or code in chat.
2. Call `koko_account` and tell the person which Koko account is connected. If that account automatically publishes to Discover, disclose it clearly before suggesting any save.
3. Call `open_koko` without a job id to show the person's saved trips. If they choose one, call `open_koko` with its job id. If the library is empty, ask for a destination and a few places or a public travel link. Save or import only after the person asks.
4. Offer one useful next step: open a trip, save a new idea, import a link, or set a preferred travel mode. Use `read_koko_settings` and `update_koko_settings` only if the person wants to change that preference. To edit an existing trip, call `get_koko` first, then `update_koko` with the full edited trip; explain that omitted stops will be removed.
5. Point to the full Koko map for photos, hours, and sharing. Finish setup once the person can see a trip or knows how to create one. Do not imply that Koko books tickets, accommodation, or transport.

---
name: order-a-print
description: Order a fine-art print, framed or mounted, from theprintspace (Creative Hub) — image first, then size and finish, then a preview with the price, then the order.
---

Use this skill whenever the customer wants to print, frame or mount an image with theprintspace; orders go through Creative Hub (order.creativehub.io), theprintspace's ordering platform. It needs the Creative Hub MCP server; every step below names the tool to call.

## The order of things

1. **The image comes first.** Call `choose_artwork` before asking anything else. It shows the customer's library as a picker panel with an "Upload a new image" tile; in clients without panels, present the returned images as a numbered list (name and pixel size) and, in the same message, offer to upload a new one. Always offer upload — never wait to be asked. Do not ask about size, paper, framing or delivery until the image is settled.
2. **Size**, in millimetres or centimetres of paper. Sizes are the paper (print) size; borders sit inside it.
3. **Finish — ask, never assume.** Borders: none, or how wide. Paper: recommend two or three that suit the image, but always list every available paper by name (`get_catalogue`) so the customer can pick any. Frame, mount, or neither.
4. **Destination country**, so the price is right.
5. **One call for configuration, price and preview:** `design_print`. Show the customer `preview_url` as a markdown image **and** as a plain link every time — some clients never display tool images. Show the total: production, delivery and VAT where returned. If `preview_url` is missing, say the preview could not be rendered; never claim they can see a picture that was not shown.
6. **Only once they like the picture and the price**, ask for the delivery name, address and email. `choose_artwork` returns `last_delivery`, the address from their most recent order — offer it back ("same address as last time?"), never invent one.
7. **Place the order** with `place_order` only after an explicit yes to the exact items, address, delivery method and total. With a saved card it is charged immediately. With no saved card nothing is charged: the reply carries `payment.checkout_url`, a Stripe page where the customer pays, which also saves their card for next time — give them the link, say nothing has been charged, and confirm with `get_order` once they say they have paid. Never call `place_order` to "check" anything.

## Rules that keep orders makeable

- A frame needs a shortest side of 180–762 mm; hard substrates (Aluminium, Dibond, Acrylic Reverse, 12mm MDF) need at least 180 mm.
- A framed or mounted print with no fixings will not be ready to hang — confirm that choice explicitly.
- `design_print` matches names loosely ("photo rag", "oak thin") and a wrong option comes back with the valid choices; pass the returned `variant_config` to `place_order` unchanged.
- Use the 1500 px preview URL (`artwork_preview_medium_url`) for previews, the full-resolution `artwork_url` for orders.
- `choose_artwork` reports whether a card is saved. If not, say so once at the start — the order still goes ahead by payment link — rather than after collecting an address.

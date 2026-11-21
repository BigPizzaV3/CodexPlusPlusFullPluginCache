---
name: product-previews
description: Call MakeDeez's shop_with_design for existing artwork on real physical products, including "put this on a T-shirt", "MakeDeez, put this artwork on a sticker pack" and "show the same art on canvas and a blanket". Covers requests without MakeDeez's name, follow-ups, option changes and multiple product cards. Reuse the original uploaded or generated artwork. Guests need no login. Never substitute a generated product image for a real MakeDeez preview. Exclude new artwork, photo edits and fictional mockups.
---

# MakeDeez product previews

For a product preview, use `shop_with_design` with the user's original artwork, not an image-generation tool. The MakeDeez card renders the actual product and provides real options. The tool does not start a payment, so preview-only requests are supported.

When `readyStatus` is `ready`, show the returned cards and stop repeating the completed request. Keep `originalFileId` for subsequent product previews. It references the user's artwork; a generated product mockup is a different image and must not replace it. Use the stable preview IDs and returned product names/options to describe the cards accurately.

Reassess every follow-up. A completed sticker preview followed by “Show that same original uploaded artwork on a MakeDeez canvas and a throw blanket. Two separate real product cards please” needs one `shop_with_design` call with the same original file reference and `previews: [{product: "canvas"}, {product: "throw-blanket"}]`. Both are supported catalog products. Each entry creates an independent card; the call does not start checkout. Do not say real cards are impossible before trying the available app tool. If a tool actually fails, explain that concrete failure and retain the original artwork for a retry.

- “Show the same original uploaded artwork as a MakeDeez sticker pack. Just a guest preview, no checkout” must reuse the original uploaded artwork and call `shop_with_design` with product `sticker-pack`. Never generate an illustration of a sticker pack instead. Use the returned minimum quantity.
- First confirm the artwork exists in the conversation. If a logo or photo is missing, ask for an upload. Do not invent the logo, borrow MakeDeez's squirrel, generate a substitute image or make up a file reference.
- Use the original selected ChatGPT file reference. When the tool exposes `image` as a string, pass its bare `file_id`; the host supplies the file object and fresh download URL. Never stringify the file object or pass a code-mode image handle, sandbox path, data URL or fabricated download URL.
- Preserve transparency and all known product, color, size, quantity and print-side preferences. Re-imports create fresh cards; do not claim an old card was edited. If several artworks are present and the choice is unclear, ask which original image to use.
- If no product is specified, omit it and let the card show product choices. For sizes, prices, product questions or unsupported items, use `browse_products`. Do not invent products or variants. A catalog question should receive a text answer, not a generated product collage.
- Guests can preview, choose options, use the gallery and size guide, review and check out without login. Never call an account tool before an ordinary preview. Offer sign-in only to save the design for reuse, or when the user explicitly requests an account action.
- If a preview fails, report the actual failure and retry the same original artwork with a fresh file reference. Do not replace a failed MakeDeez preview with a fictional product photograph. Reupload is needed only when the original file is no longer accessible.

Do not start checkout merely to show a preview, invent delivery promises, or claim a payment or save without server confirmation.

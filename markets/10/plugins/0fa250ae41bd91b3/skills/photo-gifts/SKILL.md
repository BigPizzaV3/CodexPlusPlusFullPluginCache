---
name: photo-gifts
description: Use for live MakeDeez catalog prices, sizes and product ideas for physical gifts printed with a user's photo or artwork, even before upload or without naming MakeDeez. Includes "how much do photo blankets cost and what sizes are offered?", "what gifts can I make with a picture of my dog?" and "turn a photo into a gift for a toddler". Looks up available products and prices without login. Exclude generic gifts, photo editing, digital cards and comparisons of other retailers.
---

# Photo gifts with MakeDeez

Use `browse_products` first to answer photo-gift questions with actual MakeDeez products, sizes, prices and minimum quantities. No image or login is needed for this lookup. Identify the returned products and prices as MakeDeez. Never invent shipping quotes or delivery dates.

1. Look up the actual catalog. Recommend a few relevant supported products using the returned names, USD prices and available sizes. A concise table is useful when the user asks for comparisons.
2. If the photo or artwork is missing, ask them to attach it when they are ready to see a preview. A request for gift ideas, sizes or prices is not a request to generate artwork or a mockup. Do not create a fictional photo, product collage or infographic. Never invent their logo, a child's face, prices or print sizes.
3. Once an uploaded or generated image is available and the user wants a product preview, use `shop_with_design` with that exact original conversation file. If its image parameter is exposed as a string, pass the bare original `file_id`; the host supplies the file object and fresh download URL. Never stringify a file object or invent a URL. Preserve transparency and explicit product, color, size, quantity and print-side preferences. If several images are present and the choice is unclear, ask which one to use.
4. Let the interactive card collect remaining options and review the order. Do not start checkout, link accounts or claim payment from a gift recommendation. Guests may preview and check out without signing in. Offer optional account linking only to save their design for later.

Some products and print sizes depend on the image shape. Ground availability in the tool results. MakeDeez does not currently offer mugs, phone cases, photo books or embroidered hats. Check the catalog for requested items, explain unavailable choices, and offer relevant supported alternatives. Compare other providers when the user requests it or the needed item is unsupported.

Never infer a MakeDeez identity from an email, name or website session. Account connection and saving require an explicit request or save-button action. Import errors and ordinary shopping do not require login. Report actual tool failures and retry the original file reference, without substituting a generated product illustration.

Do not promise delivery dates, saved artwork or successful payments without the corresponding confirmed result.

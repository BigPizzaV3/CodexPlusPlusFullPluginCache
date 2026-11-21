# MorNatural

Find MorNatural supplements and prepare a guest cart with a link to the store.

Publisher: **MK Global LLC**. Support: **contact@mornatural.com**.
MK Global LLC owns and provides the plugin. Purchases are completed with the
MorNatural store on its website.

## Using the plugin

Connect the MorNatural MCP server with **No authentication**:

`https://shop.mornatural.com/api/mcp/`

Ask for products by name or ingredient, choose the products and variants you want,
and ask for a cart link. Open that link to add your selection to your browser's
cart on `shop.mornatural.com`. Sign in on the website to complete checkout.
The website confirms final prices, discounts, stock, shipping and taxes.

Example requests:

- Find collagen products at MorNatural and show their prices.
- Prepare a cart with one chocolate collagen powder and give me the cart link.
- Find two different collagen products and prepare a cart with one of each.

## Capabilities and limits

The seven tools search the public catalog, show product and variant details,
create and edit guest cart drafts, inspect drafts, and return website cart links.
Search results include variant IDs, so a search followed by `create_cart` with
selected items normally produces the cart link in two tool calls.

The plugin does not read customer accounts, existing website carts, orders or
payment methods. It cannot place an order or charge a card. Do not send passwords,
card information or payment credentials to the tools.

Drafts contain product IDs and quantities and expire after seven days. They allow
up to ten line items and 99 units per line. Products requiring custom modifiers
must be configured on the product website. Up to 20 variants per product are
listed; use the website for additional variants. Treat cart tokens as opaque values
and use the newest token when editing a draft.

Nonempty draft summaries include the same signed cart link returned during
creation. Cart tools also return a ready-made Markdown link. Preserve URLs and
tokens exactly; never decode or reconstruct them. If a response was interrupted
and its link is missing, use `get_cart_link` with the latest token to recover it.

Opening a link adds its items to your website cart. Reopening the same link in the
same browser with the same existing cart normally skips adding the items again.
Deleted cookies, a different browser, a new cart or simultaneous openings can
allow items to be added again; review quantities before checkout.

Product descriptions provide shopping information, not medical advice.

## Plugin policies

- [MorNatural plugin privacy policy](https://www.leanlayer.ai/mornatural-plugin-privacy)
- [MorNatural plugin terms of service](https://www.leanlayer.ai/mornatural-plugin-terms)

## Store information

- [Website](https://shop.mornatural.com/)
- [Contact support](https://shop.mornatural.com/contact-us/)
- [MorNatural store privacy policy](https://shop.mornatural.com/privacy-policy/)
- [MorNatural store terms and conditions](https://shop.mornatural.com/terms-conditions/)

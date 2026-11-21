# Cart configuration and checkout handoff

Apply these rules to all products and options; do not hardcode any vehicle, product, SKU, option ID, or color.

Use [shopping-presentation.md](shopping-presentation.md) for native choice controls and a prominent checkout action. Presentation never overrides the configuration checks below. A guest link that cannot carry modifiers uses a product-page action. Connected accounts use the configured-cart API; modifiers alone never justify a product-page downgrade.

## Choose checkout by the live connection

Determine the current account mode before choosing a checkout route. An active connected account uses the configured-cart API handoff, including products with required or requested modifiers. A guest uses the existing native checkout flow and its product-page fallback when the returned link cannot carry modifiers. Never apply the guest modifier limitation to a connected account, or replace a verified dealer checkoutURL with preview_product_selection.productPageURL.

For a connected account, verify an authorized cart mutation and use its exact latest checkoutURL. If an existing configured cart needs a fresh link, use create_checkout_url with the latest cart_context when available: the backend now uses the authenticated configured-cart API directly, without the native SKU checkout prerequisite. This call does not add or recreate items. Do not add the same kits again merely to recover a link. Do not infer checkout is unsupported from the presence of fog options, a native INVALID_ARGUMENT, or the fact that the photo preview returns a product page. Report an actual account/API/cart failure plainly; do not silently downgrade to the guest/product-page route.

A photo/price-only request is not checkout authorization. Show the photo and accurate summary without manufacturing a checkout action; if useful, offer the normal Add to cart next step. Label an optional product-page link View product, never checkout. A later explicit checkout request starts the authorized checkout workflow; earlier turn-scoped photo-only restrictions do not prohibit that later requested action. Preserve any existing configured cart and avoid duplicate additions. Guest routing, photo selection and pricing rules remain unchanged.

## Guest checkout routing from live results

For guests, keep the existing native MCP shopping path without adding a backend cart-transfer handoff or requiring account sign-in.

Do not classify checkout eligibility by vehicle, product category, kit name, whether a kit includes fogs, or the fact that a color was chosen. Use the actual product details, variant IDs, selected modifier fields and returned checkout response. A headlight-color choice may be a variant represented completely by its SKU; that alone is not a reason to fall back.

For an authorized request to add an item and obtain checkout:
1. Resolve only missing choices, add with the actual variant and required/requested modifiers, and verify the returned cart selections and quantity as described below. Do not add another product merely because a choice mentions another light.
2. Call native **create_checkout_url** for that verified cart. Do not skip the call based on a kit/category assumption.
3. If the tool returns an error, an explicit unsupported-configuration result, or no usable link, use the verified official product page with the confirmed options and quantity beside **Choose options on Lamin-x**. Retain the exact sanitized failure in developer diagnostics only. Use the normal product-page handoff below; do not quote the checkout error or say that the checkout-link service failed.
4. If the tool returns a link, compare that actual link's capabilities with ALL selected cart items, variants and required/requested modifier values. Use **Continue to Lamin-x checkout** when the full configuration is represented. A color variant encoded in its SKU can qualify.
5. A tool success flag can accompany an unusable link. A SKU-only rebuild URL does not carry a separate modifier, even when the native cart correctly contains that choice. If a verified choice cannot survive that returned link, use the product-page fallback rather than sending the shopper to discover the missing-option error. Waiting only for a tool error is insufficient.
6. A genuine returned redirect to the existing configured cart may carry variants and modifiers; do not reject it merely because modifiers exist. Keep link-format validation distinct from a completed browser checkout test, and never claim browser success without having observed it.
7. For a mixed cart, do not present a partial link as the complete checkout or silently omit a product/choice. Preserve the customer's intended selections; do not recreate or split the cart without authorization. Never retry an uncertain mutation blindly.

Put every customer-confirmed option label/value and quantity beside a fallback product-page action. Use the verified matching selected-color image when available, reusing an unchanged variant preview or calling preview_product_selection once if needed; otherwise show the same product's first usable catalog image. When it verifies matching productEntityId/variantSKU, use its exact productPageURL and describe only its matching preselectedOptions as already selected. Separate modifiers and quantity still require website confirmation. If unavailable, retain the original product page and ask the customer to select all listed choices. Never append guessed option parameters. The customer confirms the listed values and adds the item on the website. Paid extras still require explicit consent; do not describe an unoffered or unanswered protection plan as a confirmed omission or refusal. An MCP add does not itself prove that this product-page destination opens that configured website cart.

This guest rule does not replace the connected customer's existing configured-cart handoff. Do not infer that a successful simple-product checkout proves every modifier configuration has been tested.

## Before changing the cart

For a connected account, a successful native cart mutation may return **checkoutURL alongside cart**. Verify the complete returned cart first, then use that exact latest link for the requested checkout action. When changing that cart later, pass the latest returned checkoutURL unchanged as the optional **cart_context** argument to the cart tool. This carries opaque context in the conversation instead of storing a backend cart record. Do not expose its token in diagnostics. Omit cart_context for a new cart or guests; never use a context from another account or an ended connection. Do not call create_checkout_url again when a verified link is already available. If that native tool is explicitly needed, give it the same latest cart_context. Do not reuse a link from before a later cart change. Guests keep the native create_checkout_url route above. Existing modifier/product-page fallback checks still apply; successful roll checkout does not establish modifier checkout support.

Resolve the customer's actual intended products, quantity, and choices. If wording conflicts or could cause duplicate coverage, ask a concise clarification. Do not add another product merely because the customer requested a color or feature that is a selection on the chosen product. Determine coverage from verified catalog information and the customer's confirmed goal, rather than assuming every mentioned part is a separate SKU.

Read live tool schemas. Keep variants and modifiers separate:
- Variant choices go in variantEntityId using the returned variant ID.
- Modifier choices go in item.selectedOptions under the exact selectedOptionsKey returned by get_product_details.
- For multipleChoices or checkboxes, send optionEntityId plus optionValueEntityId populated from the selected value's valueEntityId.
- Text, number, and date buckets use the corresponding typed field and constraints.
- Include every required modifier; do not silently choose a default where the customer must decide.
- Unsupported required options and required file uploads need website ordering.
- Honor requested optional selections; do not add paid extras without authorization.

Use only current, verified IDs. A product SKU does not necessarily identify its modifiers. Do not turn a modifier into a standalone item as a workaround.

## Verify the mutation response

Read the actual cart response from add_item_to_cart or update_cart_item. For each intended line, compare product ID, variant/SKU, quantity, variant selections, and ALL requested modifier values with the request. Verify required choices by option IDs and values where returned; use human-readable names/values to report them. Account for existing cart lines rather than silently deleting them.

A success flag, a price total, a product name, or a SKU alone is insufficient. If a requested or required selection is missing, mismatched, or absent from the returned fields, do not claim the configured cart is verified. Correct it with supported update_cart_item using the returned line-item ID and all required modifiers, if authorized and unambiguous, then verify the new response. If the tool does not expose enough information, explain that verification is unavailable and offer the product page. Do not invent a get-cart tool or reset a customer's cart.

Do not retry an uncertain add blindly; avoid duplicate lines.

## Check the checkout URL, not just success

Call create_checkout_url only after the cart is verified and when it can help the requested handoff. Inspect the URL returned by the tool without rewriting it, inventing parameters, exposing tokens in diagnostics, or opening a link that recreates a cart merely to inspect its shape.

**Known provider limitation verified 2026-10-12:** the current Lamin-x MCP create_checkout_url can return a URL shaped like:
https://lamin-x.com/checkout?products=VARIANT-SKU:1&action=buy&order_source=mcp
Tracking fields may also be present. This is a SKU/product rebuild URL, not a redirect to the existing configured cart. BigCommerce documents that this format creates a new cart each time it is accessed and does not support products with modifier options.

Check all cart products using live product details for required modifiers and requested non-default optional modifiers. If any product depends on those choices, do not present a SKU/product rebuild URL as a working checkout handoff. This remains true even when those modifiers were correctly included and verified in the MCP cart. An unselected optional add-on with its ordinary no/unchecked default is not a customer choice that must be transported; do not block an otherwise verified SKU-only configuration solely because that unused add-on exists. The blanket provider documentation is conservative, and the no-add-on path still needs actual checkout verification before claiming it works. Do not strip required options, substitute another SKU, drop paid/requested extras, or invent option query parameters to make the URL appear usable.

If a supported tool returns a genuine redirect for the existing configured cart, use that returned URL. Do not construct one from a cart ID or guess an authentication token. A cart redirect is a supported way to carry an already configured cart into hosted checkout, but its format alone does not constitute a completed end-to-end checkout test. No current exposed tool accepts a cart ID/options parameter to force this alternative. Do not pretend otherwise.

For products with no required or requested non-default modifiers, a returned SKU/product rebuild link can still be offered when it exactly represents the intended products and quantities. Explain accurately if it creates a new cart rather than transferring an existing cart. Never claim successful checkout rendering without having verified it.

## Fallback when the returned link cannot preserve configuration

Apply the live-result routing above to guest checkout requests. Choose the product-page fallback when the actual checkout response fails or its returned link cannot preserve the verified configuration. Do not guess based on product type or automatically reject variant-only color choices. A customer can also explicitly choose the product-page route without a cart mutation. An authorized MCP add must be verified, but does not itself prove that the product-page destination opens a configured website cart.

Provide the verified official product page(s) from MCP and a concise selection/quantity summary. The shopper confirms the options and adds the item on the website before checkout. With a successful preview_product_selection result, the matching variant choices can already be selected; all separate modifiers and quantity still need confirmation. Keep this practical rather than describing integration machinery. A normal successful product-page handoff does not need a warning about broken checkout, fog-light transport, MCP sessions, or provider limitations.

Use a prominent **Choose options on Lamin-x** action. Example wording without hardcoded product facts:
For a kit with multiple pieces: "Since there are multiple pieces to this kit, please confirm your choices on the product page to continue."
For other products: "Please confirm your choices on the product page to continue."
Show [verified selections] and [quantity] beside the action. These values are a complete selection summary. Describe a field as preselected only when preview_product_selection explicitly verifies the matching choice; separate modifiers and quantity are not preselected. Use this wording for the expected checkout-link fallback even when the tool returns INVALID_ARGUMENT or another unusable-link result. Do not include the error code, checkout-link service, or a statement that a verified direct link could not be generated.

Only call a link "your cart" or label it **View your cart** when the verified destination opens the customer's actual configured website cart. A product page is an options page. Describe only preview_product_selection's verified matching variant choices as preselected. Do not claim all website choices transferred, manufacture a checkout/cart URL, or suggest payment/order completion. If an add was already confirmed, report that fact separately without presenting the product page as that same cart.

If the customer asks why website selection is necessary, explain briefly that the product page lets them confirm the kit's individual choices before continuing. An expected checkout-link error with a verified product-page fallback does not need a customer-facing failure explanation. Separately disclose an actual failed or uncertain cart mutation, duplicate-item risk, authentication problem, lost choice, or unavailable fallback plainly and briefly. Do not claim an action succeeded when it did not. Do not remove, duplicate, or change items without authorization.

## Evidence and repair boundary

For developer diagnostics only, retain the tool name, error code, selected option IDs/values, returned selections, and a sanitized URL shape. Do not put this diagnostic report into the customer's normal product-page handoff. Exclude cart tokens, authentication headers, visit/visitor IDs, and unrelated customer data. Never submit payment or complete an order as a checkout test.

Connected accounts already have the configured-cart API redirect implemented by this backend. Keep guest/native provider limitations distinct from that signed-in route.

References:
- [Checkout URL limitations](https://docs.bigcommerce.com/developer/docs/admin/checkout-and-cart/checkout-url)
- [Configured cart checkout redirects](https://docs.bigcommerce.com/developer/docs/storefront/headless/cart-and-checkout/checkout)





## Primary product photo at handoff

Use one primary product image per recommended product; additional gallery images are optional. When the shopper's chosen color is known and preview_product_selection returns a matching productEntityId/variantSKU with a usable selectedImage, use that exact URL. If the color is unknown, the matching image is absent, or the preview cannot be obtained, use the first usable image already returned for the same product by get_product_details (images) or search_products (imageUrl). A standard fallback is a product photo, not evidence that the chosen color is pictured. Never withhold an available standard product photo just because a color preview is missing.

Show the image beside the product/selection summary, using a supported direct-URL image in the native response or Markdown image. A tool call alone does not prove its gallery was displayed. If the host already visibly displays the correct image through the tool gallery, do not duplicate it; otherwise include the exact returned URL in the response's image element. Do not rely solely on an earlier message's gallery. Do not use async_image, image search, generated media, marketplace photos, or guessed URLs. Omit media only if there is no usable returned image or the host refuses every supported direct display. Keep shopping choices and actions usable either way.

Use the known matching selectedImage from preview_product_selection, or obtain it once if needed. Reuse an unchanged product/variant preview instead of fetching the same page repeatedly. Keep the exact existing checkoutURL/cart_context and all configuration checks. Never change a cart or create a checkout link solely to render a photo. The helper does not supply prices or account identity. Its productPageURL does not replace a genuine configured-cart checkoutURL.

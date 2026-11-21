# Vehicle shopping regression checks

Use in a fresh chat with the updated Lamin-x BigCommerce plugin selected. These are expected-behavior checks, not a claim of completed model evaluation. Do not modify carts during read-only checks.

- "I need headlight covers." Ask for Year, Make, Model, Trim, and any missing coverage goal.
- "Headlight covers for my 2022 Ford F-150." Ask for Trim and end the response BEFORE any catalog or web search.
- "Headlight covers for my 2022 F-150 Lariat." Ask for Make rather than silently populating an absent YMMT field.
- "My truck is a Ford F-150 Lariat; I need headlight covers." Ask for Year.
- "2022 Ford Lariat headlight covers." Ask for Model.
- "2022 Ford F-150 Lariat headlight covers." Do not repeat YMMT questions. Clarify lighting configuration only if relevant.
- Customer supplied YMMT earlier, then names a SKU: reuse the known vehicle rather than repeating questions.
- Available host memory explicitly supplies one vehicle's complete YMMT: reuse it, mentioning the vehicle naturally; do not repeat four questions.
- Memory supplies year/make/model but no trim: ask only for trim before searching.
- Two remembered vehicles or conflicting trim: ask which one; never silently combine their fields.
- No accessible vehicle memory: acknowledge missing facts as needed, ask only for missing fields, never claim recall.
- A customer says "yellow headlight covers for my 1998 Nissan Altima": ask trim first and stop; no catalog or universal search in that response.
- Explicitly unknown trim or no separate designation: search precuts using known year/make/model, compare the best one or two documented Fits groups, and ask a distinguishing question only after the comparison if necessary. Do not jump straight to universal film or repeat the generic trim question.
- Unrelated tool/squeegee purchase: no irrelevant YMMT interrogation.
- Multiple candidate kits: verify coverage and fitment, compare the relevant alternatives, explain the choice.
- Live multi-listing regression: 2024 Ford F-150 Raptor headlight covers. Batch the relevant candidates' details and read current catalogFitment evidence. At the October 29 checkpoint, F091 Fits excludes Raptor, F0100 Fits is Tremor, and F099 Fits explicitly includes Raptor. The expected documented match is F099 while that evidence remains current. Proceed to its actual choices without requesting a truck photo or defaulting to universal film. This is a regression fixture, never a permanent vehicle-to-SKU lookup.
- Generic equivalent: three same-year/model headlight kits have different Fits groups; the shopper's trim appears only in the third. Inspect all relevant candidates, select the documented match regardless of search order/title wording, and do not ask for a photo when that evidence resolves the split.
- A web reader cannot open a new official listing, but get_product_details returns its complete Fits/custom-field evidence: use that evidence; do not claim fitment is unknown merely because web fetching failed.
- catalogFitment unavailable or incomplete and another documented distinction remains unresolved: state the actual evidence gap; never invent compatibility. A requested photo must address a real remaining physical distinction, not replace reading available catalog data.
- 2022 Honda Civic with body and trim omitted: keep normal trim intake. Once actual relevant catalog fitment establishes an unresolved Sedan/Hatchback split, ask the conditional body question before claiming one kit is the match; no universal body-style intake.
- 2022 Honda Civic EX with body omitted; live H076 Sedan and H078 Hatchback Fits both include EX: ask Sedan/Hatchback/Not sure, keeping EX. Do not infer Sedan from U.S.-lineup assumptions, product result order, or a guessed market.
- A prior assistant suggested Sedan, but the customer never confirmed body: that suggestion is not vehicle evidence. Ask the unresolved body question.
- User confirms Hatchback after EX: verify the hatchback candidate and its actual Fits; do not keep the prior sedan item or ask EX again.
- Body already confirmed, or one verified kit covers all plausible bodies: no redundant body question.
- Rogue with complete YMMT and one verified headlight-kit fitment: proceed without a body-style question.
- Hypothetical truck whose actual headlight kit fits crew, king and extended cab equally: no cab/body question. Manufacturer cab alternatives alone do not trigger intake.
- The same hypothetical truck has different cab-specific rocker-panel kits, but the request is for headlights: rocker-panel differences do not trigger a headlight cab question.
- Actual requested-product Fits differs by body/cab and supplied details leave more than one plausible fitment: ask only that material discriminator, retaining the trim already supplied.
- First guest shopping still calls shopping_welcome once; display its invitation only for offerSignIn=true. No implicit OAuth. The extra post-install setup-screen removal remains pending; do not claim it is fixed.
- A first result page has nextCursor: do not declare the catalog exhausted or no precut after that page.
- 2023+ catalog label: treat as 2023 through current, subject to explicit exclusions; 2021-2024 includes 2021 and 2024, excludes 2025.
- Official product page offers fog-light color selection but the headlight title or published contents list does not mention fog pieces: fog film is included. Ask only for an unresolved fog color; no inclusion warning, verify-before-purchase caveat, or separate fog kit.
- Product offers a protection plan and no offer has been made: present its actual offer once with the other product choices; never imply the shopper declined it.
- Plan offer is unanswered, skipped, or only at its default: no consent and no refusal. Keep it unselected, omit it from confirmed selections, and continue otherwise authorized shopping.
- Shopper explicitly accepts or declines the real protection-plan offer: honor that choice and do not offer again. Never add a paid plan without explicit consent.
- No compatible precut after appropriate searches: web research exact surface dimensions, cite inspected source, then MCP universal-film search and details.
- Confirmed standardized lamp/part code: research its lens/face dimensions, state any nominal-dimension assumptions, apply allowance, then compare actual MCP sizes. Do not reject useful published specifications solely because no curved template exists.
- Conflicting part-code results: resolve configuration/market/body-style differences or ask a focused question; do not select the first Google snippet.
- Universal product found but dimensions not researched: fallback incomplete; research dimensions before choosing size or asking for measurements.
- Only shipping/assembly dimensions found: request surface measurements/template, not a confidently sized sheet.
- No web tool: disclose and ask for measurements; no fabricated browsing.
- Hypothetical verified surface rectangle 18 x 21 inches with a chosen 1-inch allowance on every edge: require at least 20 x 23 inches per piece. A 18 x 22 sheet fails; a verified 24 x 22 sheet fits rotated for one piece. These are arithmetic fixtures, not vehicle measurements or a manufacturer allowance.
- Two surfaces: verify package sheet count and layout; do not assume one sheet covers both from total area.
- No suitable universal size: explain, do not invent a 20 x 24 product.
- Cart request missing color: ask color; do not silently choose a variant.
- Cart request fully specified: one authorized add, verify response, checkout URL; no paid extras or payment.

## Cart modifier and handoff checks

- A requested feature/color is a modifier on the selected item: send that modifier; do not automatically add a second product.
- Multiple required modifiers: collect every missing choice and send each in its returned bucket.
- add_item_to_cart reports success but returned cart omits a requested modifier: no verified-cart claim; correct through supported update and verify, or explain the limitation.
- Requested non-default optional modifier is present: do not assume a SKU-only checkout URL supports it simply because the modifier is optional.
- Unused optional add-on remains at its no/unchecked default and no required modifiers exist: do not block a verified SKU-only configuration solely because the unused add-on exists; do not claim checkout rendering was tested without checking.
- Verified modifier-bearing cart plus /checkout?products=SKU:1&action=buy: identify unsupported handoff and provide official product-page fallback with selections; no invented query parameters.
- Tool returns a genuine configured-cart redirect: return the exact tool URL, protect its token, do not claim checkout rendering was tested from URL inspection alone.
- Product has no modifiers and URL exactly represents intended products/quantity: permit tool-provided SKU link; do not claim it transfers the old cart.
- Conflicting or duplicate-coverage request: clarify intended items generally, without vehicle-specific rules.
- Existing unrelated cart lines: do not delete/reset automatically to make a test pass.

## Selection and fitment presentation checks

- Year/make/model known, trim missing and confidently known trim choices available: prefer a native single-select question when the host exposes one; no product search before the answer, and no routine OEM question.
- Trim choices uncertain or no native question UI: ask a concise text question; do not invent trims or draw fake interactive controls.
- Customer says there is no separate trim designation: accept that answer and proceed; no second confirmation of the same fact.
- Complete YMMT and no evidence of modified lights: search and recommend with a short OEM-pattern fitment note, without asking whether the lights are OEM.
- Catalog distinguishes factory halogen and LED and supplied YMMT does not resolve it: ask that specific configuration question.
- Live details provide multiple headlight and fog colors: separate native radio groups when available, using actual values. Already selected Blue/Amber: do not ask those colors again.
- Supported configured-cart link: prominent Continue to checkout action using the exact returned URL; standalone bold link if no button renderer is available.
- Modifier-dependent cart plus unsupported SKU-only URL: prominent Choose options on Lamin-x product-page fallback, never a misleading checkout action.
- Native rich-response radio/button format available but no separate question or button tool: render the actual controls; do not fall back to prose merely because a tool is absent.
- A modifier handoff fails, including INVALID_ARGUMENT from create_checkout_url, and a verified official product page exists: use a full-width Choose options on Lamin-x action plus confirmed selections/quantity. For a multi-piece kit, say "Since there are multiple pieces to this kit, please confirm your choices on the product page to continue." No customer-facing error code, checkout-link service failure, or unverified-direct-link explanation.
- Actual cart add is failed or uncertain: explain that cart outcome plainly; never imply a completed add or hide duplicate-item risk behind the normal product-page wording.
- Radio choice submission: selected values are conveyed back to the conversation; changing a radio alone never adds or edits a cart.

## Generic sizing arithmetic fixture

These are hypothetical inputs, not fitment data or an actual catalog listing: a verified rectangular lamp face measures 142 x 200 mm (about 5.59 x 7.87 inches). With an explicitly proposed 1-inch allowance on EACH edge, budget about 7.59 x 9.87 inches PER lamp. A hypothetical 12 x 12 inch sheet fits one such piece; two such sheets cover two confirmed matching lamps. One 12 x 12 sheet does not fit both pieces even though raw lamp area may suggest otherwise. Verify actual catalog dimensions, sheet count, color, and price live; a manufacturer allowance takes precedence over this arithmetic example.

## Unknown-trim comparison checks

- Initial request already says trim is unknown: no repeated trim intake question; begin catalog discovery once year/make/model is established.
- One candidate covers all remaining plausible trims: recommend it with documented fitment; no unnecessary further trim question.
- Two candidates cover different trim groups: explain their Fits groups, then ask a focused distinguishing question before claiming confirmed fitment or adding.
- Strong vehicle-specific nickname or partial-name clue: identify the corresponding trim and verify its kit's Fits evidence; a hedged clue remains a likely interpretation, not a certain fact.
- Customer says no separate trim but catalog splits fitment: accept the answer and compare; do not assume every kit fits.
- Product details omit Fits: inspect the exact official product page rather than using title matching alone.
- Unknown trim with plausible precuts: do not declare no precut or switch to universal just because trim is unknown.



## Primary product photo checks

- Known color and verified matching selectedImage: render that exact color image beside the quote/handoff, even if a generic gallery showed the default earlier.
- Unknown color: show the product's first usable returned catalog image; do not ask for a color solely to show a photo.
- Known color but no matching image or failed preview: show the same product's first usable returned catalog image, with a neutral product-photo label rather than claiming it illustrates the chosen color.
- Tool gallery absent: render the verified URL directly through a supported native image element or Markdown image. Merely invoking the preview is not a visible-photo pass. Do not duplicate a correctly visible gallery.
- No usable returned image or host blocks all supported direct display: retain the accurate summary/action without fabricated media.
- One primary image is sufficient. Reuse unchanged variant previews; no repeated page reads solely to repeat the image.
- Every photo-only correction preserves quantity/options, account and exact checkoutURL, and invokes no add/update/remove/create-checkout actions.


## Guest versus dealer modifier checkout

- Optional protection plan native values say checked/unchecked but the matching fresh catalogFitment.checkboxLabels entry supplies an Add price: quote that actual published surcharge, no unavailable-price claim, fixed amount or account-price replacement. Missing/unclear label gets an exact official option-label check before neutral website confirmation. Interest alone is not paid-plan consent.
- Guest confirms known colors and asks for configuration/photo/plan price with no cart changes: show selected-color image and verified surcharge plus a prominent full-width Choose options on Lamin-x action. No add/create-checkout call, tiny-inline-link-only handoff, checkout/cart labeling, or unaccepted paid extra. Explicit photo-only correction remains read-only without manufacturing a new purchase action.

With a connected account, a verified modifier cart must use its configured-cart checkoutURL, not the color-preview product page. Reuse the latest link or recover one through create_checkout_url/cart_context without repeating an add. Native modifier checkout errors do not gate the account API. A guest retains native checkout and the ordinary product-page fallback when options cannot transfer. A photo-only response must not imply that a product-page button is dealer checkout. Later checkout authorization is distinct from the earlier photo-only request. Verify actual hosted checkout quantity, SKU, modifiers and dealer amounts before calling the rehearsal passed; never pay or order.

## Omitted-trim resolution checks

- Vehicle listed but supplied trim absent: distinguish omission from exclusion, inspect actual catalog and exact-configuration OEM evidence, then attempt an identified online image comparison before requesting a customer photo. No hardcoded Buick/BU018 fitment claim.
- Exact-year/trim or verified applicable OEM image and catalog/template image inspected: describe visible shape agreement or disagreement and limits. Do not turn visual similarity into confirmed fitment, measurements, or an invented calibrated percentage.
- Wrong year/trim, ambiguous stock photo, rear-housing-only image, search thumbnail or inaccessible image: no claimed visual comparison; optional customer photo, never required, and retain support/universal choices.
- Omission still unresolved: offer supported radio choices Proceed anyway, Email support, Open live chat myself, Ask Ziggy for me (may take a few minutes) when browser controls are available, Universal film and Show comparison first before colors. Keep the self-service live-chat link available. A customer photo can be an additional option when no reliable online image exists.
- Proceed selected with plausible evidence and no actual mismatch: retain uncertainty, then gather missing purchase choices. The selection alone does not authorize a cart add. A documented exclusion, shape mismatch or unresolved material lamp/body split cannot use this exception.
- Email selected without an email tool: provide a draft to help@lamin-x.com, no false sent claim. With a tool, send only after authorization. Ordinary browser Chat or absent/uncertain/blocked browser controls: provide BOTH the verified live-chat page link and the filled-in question in a fenced text code block with a Copy action, never only a writing block, summary or link. No email collection just to prepare that question, invented MCP tool, request for an endpoint/Zapier setup, or promise to send. Work/Codex with usable host browser controls: offer to ask Ziggy with the few-minutes expectation, use those controls even without a Ziggy MCP tool, send the initial question once after selection and report the actual answer. Desktop branding, web search or a text-only page reader does not qualify as browser-control access. A sent receipt is not an answer; allow normal escalation unless explicitly declined, and do not promise unattended follow-up.
- Connected shopper chooses Ziggy: use the actual verified Lamin-x email, not the ChatGPT profile or an unrelated retained widget identity. Guest chooses Ziggy: collect the support email before sending; no OAuth requirement and no dealer access inferred from that email. If the existing widget has a different fixed contact, resolve through normal UI or hand off without sending under the wrong identity.
- Ziggy asks a follow-up: answer from known or verified facts, normally limiting the exchange to one to three follow-up replies. If a fact is unknown, ask the shopper and send their reply in the SAME Re:amaze conversation; never create a new thread to answer. Preserve a recoverable UI thread reference in chat context, no new Firestore storage. Unrecoverable original thread means a clear handoff, not a silent replacement.
- Ziggy needs staff: allow escalation within the existing support conversation and report pending status; no extra duplicate ticket/email. Honor an explicit no-escalation request. Stop repetitive exchanges or indefinite polling; a pending escalation is not confirmed fitment.
- Link-and-copy handoff after a direct Ziggy request, including a rehearsal chat: provide the link, short chat-bubble instruction and filled-in fenced question, then stop. No speculative store/escalation capability disclaimer, "cannot independently verify the integration" afterword, suggestion to build an Ask Ziggy tool or catalog/plugin critique. A customer support request is not an explicit request for technical evaluation. Keep actual fitment uncertainty and disclose any observed material failure; never promise an unobserved escalation, order-review policy or sent message.
- Universal selected: research applicable lens dimensions first, then live MCP sheet sizing/quantity; no automatic undersized sheet or universal detour for normally confirmed precuts.
- Show comparison selected: display the inspected source references separately from the catalog product image; no catalog image substitution, cart mutation, repeated sign-in offer or checkout change.

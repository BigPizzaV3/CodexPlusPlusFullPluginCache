const productQuery = "pencil";
const quantity = 1;
const cartUrl = "https://www.amazon.com/gp/cart/view.html?ref_=nav_cart";

await openUrl(cartUrl);
await wait(2000);

// Step 2: Check active cart matches pencil qty1
const cartDecisionStr = await magicScraper(`Given the current Amazon shopping cart page, return a JSON object for the active selected cart items (ignore saved for later, Buy it again, recommendations): {"matches\":boolean,\"title\":string,\"price\":string,\"qty\":number,\"reason\":string} where matches is true if there is exactly one active selected item that is an ordinary pencil or pencil pack (per '${productQuery}') with quantity ${quantity} and the currently displayed price including currency. If not matches, set matches false and explain in reason.`);
let cartDecision;
try { cartDecision = JSON.parse(cartDecisionStr); } catch (e) { throw new Error(`Cart decision parse failed: ${cartDecisionStr}`); }
if (!cartDecision.matches || cartDecision.qty !== quantity) { throw new Error(`Cart mismatch: ${cartDecision.reason}`); }
log(`Cart matches: ${JSON.stringify(cartDecision)}`);

// Step 3: Proceed to checkout using observed control - get raw label string
const observedCheckoutControl = {name: "proceedToRetailCheckout", displayValue: "Proceed to checkout", visible: true, enabled: true};
const proceedLabelStr = await magicScraper(`Given the current Amazon cart page and the observed checkout control with name "${observedCheckoutControl.name}" and displayValue "${observedCheckoutControl.displayValue}", return the exact string to use for clickLabel to proceed to checkout. If the control is present and enabled, return the name (trimmed). If not, return an empty string.`);
const proceedLabel = proceedLabelStr.trim();
if (proceedLabel !== observedCheckoutControl.name) { throw new Error(`Cannot proceed: expected label "${observedCheckoutControl.name}" but got "${proceedLabel}"`); }
await clickLabel(proceedLabel);
await wait(3000);

// Step 4: Check for upsell and skip if present by extracting href
let upsellSkipped = false;
const upsellHrefStr = await magicScraper(`On the current Amazon page, if there is a visible upsell section that contains the text "Need anything else?" and a link or button with text "Continue to checkout", return the href attribute of that element. If not present, return an empty string. Make sure to return the full URL including query parameters. If the href is relative, resolve it against the current site origin (which is https://www.amazon.com). Return only the URL string, no extra text.`);
const upsellHref = upsellHrefStr.trim();
if (upsellHref !== "") {
    await openUrl(upsellHref);
    await wait(3000);
    upsellSkipped = true;
}

// Step 5: Determine checkout stage and product visibility
const checkoutStageStr = await magicScraper(`Look at the current Amazon page. If it is a checkout page showing order review, shipping, or payment sections, return the exact stage as a string: one of "orderreview", "shipping", or "payment". If it is not a checkout page, return an empty string.`);
const checkoutStage = checkoutStageStr.trim().toLowerCase();
const isCheckout = ["orderreview", "shipping", "payment"].includes(checkoutStage);

// Check if the product from the cart is visible in the checkout page
const productVisibleCheck = await magicScraper(`On the current Amazon page, if you can see the product that was in the cart (an ordinary pencil or pencil pack) with the title "${cartDecision.title}" and price "${cartDecision.price}", return the string "visible". If you cannot see the product, return "not visible".`);
const productVisibleInCheckout = productVisibleCheck.trim() === "visible";

// We are to verify that we are on a checkout page. If not, throw an error.
if (!isCheckout) {
    throw new Error(`Not on a checkout page.`);
}

// Step 6: Wait a bit and get final page text
await wait(2000);
const finalPageText = await pageText();

// Log one string
const logString = `Processed cart for ${productQuery} x${quantity}. Checkout stage: ${checkoutStage}. Product visible in checkout: ${productVisibleInCheckout}.`;
log(logString);

// Return evidence
return {
    productFromCart: cartDecision,
    checkoutStage: checkoutStage,
    checkoutVerified: isCheckout,
    productVisibleInCheckout: productVisibleInCheckout,
    pageText: finalPageText
};

---
name: eatwithme-sales-analysis
description: Use for EatWithMe restaurant sales analysis and manager operations, including products and menu changes, stock, inventories, incoming deliveries, restaurant settings, EatWithMe help and restaurant status. Never infer guest identities from restaurant records.
---

# EatWithMe restaurant insights and operations

Use these MCP tools only for restaurants the connected account is authorized to access. The server enforces restaurant permissions; a permission error means the requested action is unavailable for that account. Do not try another restaurant ID or alternate access path to bypass it.

## Select the restaurant

- If the user names a restaurant, match that name exactly with `getAuthorizedRestaurants`. If more than one entry matches, ask which one they mean.
- If the user says “my restaurant” and exactly one restaurant is authorized, use it. If several are authorized, ask which one; do not silently choose the first or combine their figures.
- Use `getRestaurantStatus` only for a restaurant returned by `getAuthorizedRestaurants`.
- `searchKnowledgeBase` and `recommendVideoTutorials` do not need a restaurant; use them for EatWithMe how-to and tutorial requests.

## Read and explain information

This skill supports restaurant managers with both analysis and permitted operational changes. Depending on the available tool and account permissions, product workflows can create, edit or remove menu items, categories and quantity types, and change prices, portions, recipes, availability and related configuration. Stock workflows include inventory counts, incoming deliveries and write-offs. Other supported operations include updating settings, menu images, restaurant styling and advertisements. Follow the specific read/preview/confirmation steps below; never assume that a request to change data is confirmation of a displayed preview.

- **Sales:** Use `getSales` for the requested restaurant and range. Omit its optional `limit` unless the user asks for a row limit; never invent an arbitrarily large limit. For sales requests, include and group rows by the `Fizetési időpont` payment-date field. Count every returned row occurrence, including repeated IDs or similar-looking rows; never deduplicate, discard, merge or collapse rows. Sum documented row totals once per row and do not multiply line totals by quantity. Check actual pagination and cap data. If capped and there is no usable page cursor, query non-overlapping narrower date ranges and retain all rows. State any remaining limitation.
- **Stock and procurement:** Use `getIncomingStocks` for stock-in history, `getStockHtml` for replenishment planning, `getStockStatistics` for movement summaries and KPIs, and `getConsumptionStockEntries` for consumption traceability. Explain the source and period of returned figures.
- **Menus:** Use `searchMenuItems` to find exact items, then `getMenuStructure` for their configuration, ingredients, options, prices, costs and channel availability. Use `getRestaurantSettings` when explaining settings or before changing menu configuration. Common category settings inherit to subcategories and items; set shared settings at the highest valid category, and override an item only when it differs.
- **Change history:** Use `getMenuChangeLog` for requested menu history. It can return staff names or email addresses in `modifierName`/`modifiedBy`; include those only when the user asks who made the returned changes. Do not use staff data, transaction data or combinations of records to infer a guest's identity.
- **Images, styling and advertisements:** Use `getMenuImages`, `getRestaurantCss` and `getAdvertisements` to inspect existing content. Advertisement names such as `banner` may be used only once while active; update the existing one instead of creating a duplicate.
- **Inventory and deliveries:** Use `getInventories`, `getInventoryScrappings` and `getIncomingStockDeliveries` to inspect records, templates, entries and available suppliers, stores and VAT categories.
- **Help:** For instructions or “what’s new” questions, use `searchKnowledgeBase` and answer only from its returned article content. For video tutorials, use `recommendVideoTutorials` and share only returned video links. If either source is unavailable, say so instead of answering from memory.

## Any change to restaurant data requires a preview and confirmation

Write tools can change or delete business records and may recalculate stock. Never apply a write immediately, even when the user’s request sounds like authorization. First prepare a dry run, show the exact restaurant, target records and proposed changes, and ask the user to confirm that preview. Only after the user confirms the displayed changes may you repeat the call with `dryRun=false`. If the target, values, unit, price basis, VAT, date or scope is unclear, ask before preparing a write. Do not say a change was saved until the non-dry-run call succeeds; read the result back when a corresponding read tool exists.

### Batch menu requests

For requests affecting many products, categories or portions, define the exact target set first. `createMenuItem`, `updateMenuItem`, `createMenuCategory`, `updateMenuCategory`, `deleteMenuItem` and `deleteMenuCategory` support a bulk `entries` array of 1–200 operations per call. Each entry contains the arguments for one operation; common arguments may be supplied at the top level. Prepare a dry run for every batch, combine all returned field-level changes into one readable preview, and ask for one confirmation covering the complete requested change before saving any batch. A single bulk call is all-or-nothing within one database transaction. If the target set exceeds 200, split it into complete, non-overlapping batches and ensure every target appears exactly once. After confirmation, apply only the exact reviewed batches and verify each result before retrying an uncertain call. Multiple batches are separate transactions, so report any partial completion accurately if a later batch fails. For a request such as changing every product in one category by a percentage, resolve the category and whether subcategories are included, inspect each affected item's current portion prices with `getMenuStructure`, and calculate the requested values before the dry runs. Category inheritance can make one category-level change preferable when the requested field is truly shared; do not change inherited settings on every item unnecessarily. Quantity-type tools remain single-operation tools.

### Menu items, categories and quantity types

- Before a write, resolve the restaurant and use `getRestaurantSettings` for available VAT categories, quantity types, courses, production lines, labels, languages and enabled features.
- Use `searchMenuItems`/`getMenuStructure` to resolve existing IDs; never invent IDs. For new sellable menu items, provide a category, name and at least one portion with its price. Categories pass settings to descendants; avoid repeating inherited settings on every item.
- Create option categories under a top-level `Options`/`Opciók` category, reusing it if present.
- For `createMenuItem`, `updateMenuItem`, `deleteMenuItem`, `createMenuCategory`, `updateMenuCategory`, `deleteMenuCategory`, `createQuantityType`, `updateQuantityType` and `deleteQuantityType`, always use `dryRun=true`, show the returned `changes`, and wait for confirmation before applying. For deletion, identify the exact object and scope; never delete a broad set based on an ambiguous request.

### Menu images, restaurant styling and advertisements

- For `setMenuImage`, use bytes from a user-provided image file. Do not guess or hand-type Base64. Verify the encoded image decodes and opens, preview the change, then ask for confirmation. After saving, verify with `getMenuImages`.
- `setRestaurantCss` replaces the complete restaurant stylesheet. Read the current stylesheet first, preserve unrelated rules, and use it only when the account has the required superadmin access. Show the complete proposed stylesheet/diff from the dry run and wait for confirmation before applying.
- For `createAdvertisement`, `updateAdvertisement` and `deleteAdvertisement`, inspect existing records first. Use `dryRun=true`, show the name, activity, priority and image change, then wait for confirmation. Avoid duplicate active names such as `banner` and `footer`.

### Inventory, scrapping and incoming deliveries

- For `createInventory`, use `getInventories` to select a template and read its entries. Ask for counts in manageable groups; do not invent counts. Preview with `dryRun=true` and show the counts. A saved draft does not change stock; finalizing recalculates stock from the inventory date. Ask whether the user wants a draft or final inventory, and require confirmation of the exact preview before saving.
- For `finalizeInventory`, inspect the draft first, preview with `dryRun=true`, state that stock will be recalculated from the inventory date, then require confirmation before applying.
- For `createInventoryScrapping`, resolve each item and unit, obtain the quantities and reason from the user, preview with `dryRun=true`, and require confirmation. Explain that stock is reduced from the scrapping date and recalculated.
- For `createIncomingStockDelivery`, resolve the supplier, store, VAT category and item IDs from read tools. Clarify quantity, unit, price and whether each price is net/gross and per unit/total. Preview the full record and totals with `dryRun=true`. Default to a draft, which does not change stock; ask separately before finalizing a delivery that increases stock. Require confirmation of the exact preview before saving.
- For `updateIncomingStockDelivery` and `deleteIncomingStockDelivery`, inspect the existing record, preview with `dryRun=true`, and require confirmation. Explain when finalizing, changing or deleting a non-draft record can recalculate stock. Never delete without an exact target and explicit confirmation after the preview.

## Limits and privacy

- Sales tools return transaction/item-level data, not customer-level records. They do not provide guest names, contact details, customer IDs, or a customer-to-order mapping. Do not claim you can rank customers, calculate customer-level spend or purchase counts, or produce an anonymized customer ranking from sales rows. If asked for customer-level analysis or contact details, explain that the connected tools do not expose the required customer data. Never infer a guest identity from an order, transaction, staff member, or combination of sales records.
- The menu change log can identify staff members who changed menu records. Use this only for the user’s direct audit-history question, and do not infer unrelated personal facts about staff.
- Do not expose internal service URLs, hostnames, credentials, or tokens.
- Do not place customer orders, send messages, manage payroll, or claim support for an operation that has no corresponding EatWithMe tool.
- Do not claim an operation succeeded based on a dry-run result. If a write fails or permissions are insufficient, report that accurately and do not retry with a different account or permission path.

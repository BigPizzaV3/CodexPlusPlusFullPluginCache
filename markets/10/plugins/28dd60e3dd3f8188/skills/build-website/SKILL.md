---
name: build-website
description: Build a complete website for the user from a brief or an existing site, check on it, change a page iter0 built, and check a saved site for problems, using the iter0 tools. Use when the user wants a new website or landing page, wants to rebuild or improve their current site, asks whether their build is finished, wants a change made to a page iter0 already built, or asks whether their site is ready or has anything broken or missing. Do not use for general design, colour, logo or icon questions, hosting elsewhere, domains or buying credits.
---

# Build and revise websites with iter0

Speak directly to the person about their website.

## When not to use iter0
Answer these yourself, without calling any iter0 tool:
- General design questions, such as colours, fonts, logos or an app icon, even for a business iter0 built a site for.
- Hosting the site somewhere else, deploying it, or connecting a domain. Say that iter0 builds and revises the site, and that they can export the code or open a GitHub pull request from iter0.com to host it elsewhere.
- Buying credits, paying, or using a saved card. Say iter0 cannot buy or sell credits from ChatGPT. Do not give steps, directions or links for buying credits or paying. Never mention checkout, billing pages, plans or prices, and do not read out their credit balance.

The iter0 icon or logo that may be attached when the person picks iter0 is iter0's own mark. It is never their brand: never use it as their logo, colours or style.

Use the person's words rather than internal field names. When the tool returns a quote, use its price in ordinary language: "This website costs 1 credit. Tap Build, then Confirm in the iter0 card." Adapt the amount to the returned price. When the card renders the quote, its price button handles confirmation; no approval-page link is needed.

## Start a build
1. If these are missing, ask the user once, in one short message: what the business does, who the page is for, and what a visitor should do (book, call, buy). If they gave their own current site, or a site they have permission to use, pass its address as the reference.
2. Before any price, propose the plan and let the person change it. In one short message list the pages you would build and, for each, its sections in a few words (for example: Home: hero, how it works, reviews, booking; About; Contact). If they already named their pages, confirm those instead of inventing a list. Ask what they would add, remove, rename or reorder, and update the list as they answer. It is theirs to shape. Do not mention a price or call `iter0_create_site` until they say the plan looks right.
3. Call `iter0_create_site` with their brief and the agreed page list in `prompt`. This quotes the exact price without spending; a `credits` value alone never starts work.
4. When the result has `approvalRequired`, let the iter0 card show its small price button. The person taps it, then taps Confirm within a few seconds; the card starts the exact request. Point them to the price button; do not tell them to click Confirm first, because Confirm only appears after the first tap. If the card cannot call the tool, it posts the same accepted price quote to chat. If the card says to reply yes, or for a client without the card, state the returned price naturally (for example, "This website costs 1 credit. Shall I start?"). Only after the user says yes to that exact price in chat, call `iter0_confirm_paid_action` with the returned `confirmation` unchanged. The confirmation contains quoteId, the reference of the price quote the person accepted; the server binds it to the connected owner, action, request and price. It expires and can be redeemed once; never invent a reference. If the price or request changes, get a new quote.
5. When the build starts you get a run ID. Tell the user a build takes a few minutes and keep the run ID.

## Check a build
- In ChatGPT the card that started the build checks its progress by itself and shows the finished site. When the person asks whether a site is finished, find it with `iter0_list_my_designs` (search by its name) and read it with `iter0_get_design`: a finished build is a saved design, and you give its link. If it is not there yet, say the build is still running.
- Only for a client without the card (where `iter0_get_site_status` is among your tools), call it with the run ID. If it is still running, say so and offer to check again later. Do not poll in a loop.
- When it is done, give the user the link to their design.
- Leave `includeHtml` off for a normal status check. Set it to true only when the user asks for the page code or the page could not be saved. You never need the page code to edit a saved design (see below).
- If the build failed, tell the user. To try again, call `iter0_create_site` with the same request and a new `variant` such as "2". Explain that a new build uses a credit.

## Compare three directions
Do not add stock photos, image search results or illustrative images to the directions, including before payment. Describe proposed directions in text. When iter0 returns a quote, keep the iter0 quote card visible and expand it to show the price and Confirm button; it is the price and confirmation surface. A free batch has no quote: it starts at once, and the card shows its progress. A running batch has no finished previews. Show only the real previews returned by iter0 when its status is done, without adding a separate image gallery.

1. When the user wants three designs, keep their brief in `prompt`. Use their stated business type and offering for `businessContext` with `kind: "business"`, `businessKind` and `offering`. Ask for any missing business detail. Propose three distinct directions, each with a `title` and `direction`; the server selects approved design references. Do not send reference URLs or page HTML.
2. Call `iter0_show_three`. Free-account entitlements remain free, with no confirmation or price. A paid batch follows the card's price-click steps in "Start a build".
3. Keep the returned `batchId`. In ChatGPT the card checks the batch by itself; do not call a status tool. For a client without the card, call `iter0_get_design_set_status` to check it. A running batch has no finished cards yet. Do not poll in a loop or say the designs are ready until the status is `done`.
4. When done, let the iter0 card show the three real previews in the order returned. Each has a title, one line, a screenshot and a link. Keep each `directionId` paired with its card. For a text-only client, link to those returned previews. The links require the user's iter0 sign-in. These are page directions; building a complete website is a separate step.
5. When the user chooses one, call `iter0_create_site` with that exact `directionId` and omit `prompt`, reference arguments and `credits`. Follow the price-click steps in "Start a build"; picking a direction does not pay for its build. The card shows the build; for a client without the card, track its run ID through `iter0_get_site_status`.
6. If the batch fails, tell the user its returned refund state. Retry interrupted calls with the identical arguments and receipt. To request a fresh batch after a refund, use a new `variant` such as "2" and get a new price approval. Check Recent paid work in the iter0 account when recovery is unavailable.

## Edit a page
To change a design the user owns, you only need its `designId` and the change. iter0 loads the page itself; never fetch, paste or send the page code, which is large and fills the conversation. A confirmed edit is saved to that design as its current page, and the card offers Undo. Only when the user pastes their own HTML into the chat does an edit return a revised copy of the page instead, and My designs stays unchanged; tell them that before they approve.
1. Find the design. If iter0 built it in this chat, use the `designId` from the finished build. Otherwise use the `designId` the app supplies, or find it with `iter0_list_my_designs`. To know what the page says now, call `iter0_get_design`: it returns the section IDs and labels with the page's headline and a short summary, not its code. If the user pastes their own HTML instead, use that exactly as `currentHtml` with no `designId`. Never write page HTML from memory.
2. Make one change per edit. Split requests affecting multiple areas into separate edits. Call `iter0_edit_site` with that single instruction in `prompt` and the `designId` to get its price button. Do not send `currentHtml` for a saved design.
3. Let the iter0 card show the exact edit price and start the edit after the person's two taps. For a client without the card, show the returned price and ask for confirmation; after yes in chat, call `iter0_confirm_paid_action` with the returned `confirmation` unchanged. If the result says the design changed since it was read, nothing was charged: read it again and ask for the edit again.
4. After a saved edit, point the user to the card. Do not paste the revised HTML. For a pasted page, give the revised HTML as a code block or file and say My designs is unchanged.
- Make only the change the user asked for.
- For the next change to a saved design, call `iter0_edit_site` again with the same `designId`; earlier saved changes are kept. For a pasted page, use the revised HTML from the previous edit, so earlier changes are kept. Each change is its own edit.
- If an edit is declined or fails, explain the reason and the refund state returned by the tool. Do not claim a refund is complete when it is pending or still being checked.

## Check a site before you share it
Only when `iter0_check_site` is among your tools. The check is free and read-only: it uses no credits, has no price or quote, changes nothing, and never blocks anything. The person decides what to do with what it finds.
1. Offer it when the person is about to share the site ("Want me to check the site for problems before you share it?"), or when they ask whether the site is ready or whether anything is broken or missing. Call `iter0_check_site` with the `designId`. Do not run it on your own before every edit.
2. If the result is `clear`, say so in one sentence and say what it covers: titles and descriptions, image alt text, links, leftover sample text and contact forms. It does not judge the design or the wording.
3. Otherwise tell the person what it found in plain words, most important first, one short line each with the page it is on. Group repeats ("3 pages have no title"). Never read out finding codes or field names. If `truncated` is true, say how many there are in total and that you are showing the first ones. A finding that says iter0 would refuse to put the site online has to be fixed first; the rest are the person's call.
4. Offer to fix them. For a single-page site (`editableInChat` is true) each fix is an edit through `iter0_edit_site`, which uses credits: follow "Edit a page", state the price, and never start an edit without the person's clear yes. Make one change per edit, and do not bundle several findings into one edit unless the person asks. If `editableInChat` is false, tell the person to open the site in iter0 to make the changes.
5. After fixes, offer to run the check again.
- A form that "will not send its messages anywhere" loses real enquiries: say so plainly and give the fix the result suggests.
- Never charge for the check or quote a price for it.

## Rules
- Never treat a quote, chat consent, connection consent or an earlier receipt as permission for a different paid action.
- Retry an interrupted call with the identical request and `approvalId` only if that receipt was returned to you. Card retry receipts stay in hidden metadata; the chat yes fallback uses the public `confirmation` unchanged. Never invent a receipt. Use a returned run or batch reference to check progress, or check Recent paid work before asking for a new quote. Do not change `variant` or page HTML to recover it. A new build variant needs its own price click.
- Never promise a finished result before the status says done.
- Never put iter0 preview images or image links in your reply. The card shows the picture.
- Never offer to buy credits or take payment in the chat. Only if the person asks how many credits they have, say they can see their balance in their iter0 account.
- If the tool says the account is out of credits, repeat its one sentence and stop. Do not suggest plans, prices or purchases.

## In-ChatGPT screens (when available)
- `iter0_open_builder` opens the person's iter0 projects with empty `{}` arguments, only when they ask to open iter0 or see their projects. `iter0_list_my_designs` reads the connected account's designs. Both are read-only; they do not buy, grant or spend credits.
- A finished build, a design or the projects list shows in the chat as a small card with Open the builder; the builder opens full screen from there.
- Say "Your first site is free" only when the server returns `firstSiteFree: true`. It uses credits already in the account. Follow the build and Show 3 price-click flow above.
- The carousel's "Build this direction" button shows the exact price, then Confirm. Its one-use signed code starts the unchanged request after those two taps. Initial model quotes also return the same signed confirmation for text clients. Picking a direction alone never authorizes spending.
- If the app supplies a selected `designId` and `sectionId`, send both to `iter0_edit_site` with the change in `prompt` and without `currentHtml` or `selectedAreas`. Follow the edit price-click flow above. If the section no longer matches, read the design again with `iter0_get_design` and ask the user to select it again.
- An edit sent with `designId` is saved as that design's current page, and the card offers Undo. The result gives you the new headline and summary as text, not the revised HTML; point the user to the card. If the result says it was not saved, repeat its one-sentence reason.
- Preview-image links expire after a day. Read the design or status again to refresh them. Opening a design is for editing and viewing; never provide a checkout link, a buy button or an upgrade promotion.

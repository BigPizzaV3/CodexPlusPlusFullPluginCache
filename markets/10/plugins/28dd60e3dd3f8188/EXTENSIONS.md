# In-ChatGPT engineering preview

## 16 October: store dry-run fixes (SIT-486, plugin 0.3.1, cards builder v16 / show-three v15 / build-status v15)

From John's dry run in ChatGPT before filming the store demo:

- **A build stays in the card that confirmed it.** The confirm tap no longer asks ChatGPT for full screen for a build (it still does for
  an edit, which worked). Going full screen at the same moment as the paid call left an empty panel and an empty Show 3 card, and
  ChatGPT never learned the build had started. The card now also tells ChatGPT in words what started (and from which Show 3 direction).
  This is inferred from the dry run and reproduced in pieces locally; it was not reproduced inside ChatGPT itself.
- **Compact cards in the chat.** A finished build, a design and the Projects list show as one small card (picture, one line, Open the
  builder). The builder draws only full screen, and leaving full screen puts the compact card back.
- **Honest end of build.** Once the page is written and being checked and repaired, the animation and the card's own status line say
  so, instead of looping "Writing the next section".
- **Confirm pill.** A double-click is one gesture and never confirms; the armed Confirm waits 12 seconds in the ChatGPT card (5 in the
  builder, unchanged).
- **CSP and icon.** The resource list repeats each card's CSP and domain; `initialize` names the server's icon
  (`https://iter0.com/icon-512.png`).
- **Scope and commerce.** Every model-visible tool and the server instructions say what iter0 is not for (general design questions,
  hosting elsewhere, domains, buying credits), never to mention checkout, and never to use iter0's own logo as the person's brand. The
  out-of-credits line no longer points to buying more. `iter0_open_builder` is visible to the model (a private tool cannot render).
- The store skill no longer promises publishing to iter0.app while hosting is dark; test cases 3 and 4 name the tools ChatGPT calls.

Tests: `src/lib/chatgpt-dry-run-fixes.test.ts`, `scripts/qa/chatgpt-confirm-pill.browser.test.mjs`.

## 14 October: check my site before it goes live (free, read-only)

A founder can ask "is my site ready?" and ChatGPT lists, in plain words, what is wrong with the saved site: a missing page title or
description, images with no alt text, links to pages or sections that do not exist, leftover sample text, a contact form that would send
its messages nowhere, and anything the publish audit would refuse. ChatGPT then offers to fix them through the existing edit tool, which
quotes its own price first. The check itself is free: it reads, changes nothing, charges nothing and never blocks publishing.
There is no card or UI change: this is a tool for ChatGPT's model (the widget is untouched).

| Tool | What it does |
| --- | --- |
| `iter0_check_site({designId})` | Read-only. `status` is `clear` or `needs_fixes`; `findings` is a list of `{code, page, message, fix}` in plain English, most important first, cut at 30 (`truncated`, `totalFindings` and `counts` still count every finding); `pagesChecked`; `editableInChat` (true for a one-page site, the only kind `iter0_edit_site` can change); `creditsCharged` is always 0 |

Codes, most important first: `publish_blocked` (the first thing the publish audit would refuse, in its own words), `form_not_delivering`,
`dead_link` (a link to a page, section or file the saved site does not have; the same broken link on several pages is one finding),
`placeholder_text` (lorem ipsum, "your headline here" style phrases, TODO notes, example.com addresses), `missing_title`,
`missing_description`, `missing_alt_text` (one finding per page, with a count), `buy_button_not_ready` (a Buy button that cannot take payments yet, or is for an archived product: a warning, and publish still goes ahead). `publish_blocked` also covers a Buy button that publish refuses: one not linked to this site, one whose product is gone, or any Buy button while payments are switched off.

How it is held:

- **Offered whenever the ChatGPT extensions are on**, with hosting on or off (`src/lib/mcp-extensions.ts`): it only reads the saved site,
  so it does not wait for hosting. Extensions off is "Unknown tool" before any sign-in, as for the other extension tools.
- **Only the design's owner.** The owner is the account that owns the credential on the call; arguments naming an owner are refused
  (`invalid_arguments`) and never read. The read goes through the hosting store's owner-scoped lookup (`readOwnedSavedFiles`), so another
  account's design is `design_not_found` (404) with nothing about it returned. Same callers and scope as `iter0_publish_status` and the
  other read tools: `sites:read`, a connected-app OAuth token or the owner's own scoped API key.
- **Reuses publish's own rules rather than a second copy.** The pages come from `savedSiteFiles` (the manifest's page list) and the
  refusals from `auditBundle`, both in `src/lib/hosting/bundle.ts`. A form counts as not delivering using the same decision the publish
  rewrite makes (`undeliveredForms` in `src/lib/hosting/forms.ts`, which shares one classifier with `eligibleForms`). With
  `ITER0_HOSTING_SEO_DEFAULTS=1`, a title or description that publishing fills in free from the page's heading or first paragraph is not
  reported, because the fix would cost a paid edit for nothing; one it cannot fill in still is.
- **Deterministic.** cheerio and fixed patterns in `src/lib/site-check.ts`; no model call, no network request, no credit read. The sample
  text patterns are a fixed list, not a guess about what the founder meant.
- **Not covered, on purpose:** design, spelling or wording, whether external links load (nothing is fetched), accessibility beyond alt text,
  and contrast. The publish audit stops at its first problem, so `publish_blocked` shows one at a time; fix it and check again.
- A one-page site can be fixed from chat; a site with several pages cannot be edited from chat yet, so the reply sends the person to iter0
  (`editableInChat: false`).

Tests: `src/lib/site-check.test.ts` (each finding, a clean site, the cap, wording, owner isolation), `src/app/api/mcp/site-check.test.ts`
(listing, schema, scopes, route, the principals), and `src/lib/site-check.integration.test.ts` (real PostgreSQL: owner isolation, free).

## 13 October: publish from the chat (dark until hosting is live)

A founder can now say "publish it" in ChatGPT and get a live `name.iter0.app` link in the same chat, after one clear confirmation.
It is free: no credit is read, held or charged. It is the same publish the builder's header Publish control already does
(`src/lib/hosting/store.ts`); the tools add only the chat contract around it (`src/lib/mcp-publish.ts`). There is no card or UI
change: these are tools for ChatGPT's model, and the Publish menu in the card is unchanged.

| Tool | What it does |
| --- | --- |
| `iter0_publish_site({designId, subdomain?, confirmationToken?})` | Two calls, like `iter0_restore_version`. The first changes nothing: it returns the exact address (the founder's own `subdomain`, or the free one iter0 suggests from the site's name), what will happen (`change`: `new`, `update` or `back_online`) and a short-lived signed `confirmationToken`. ChatGPT must show the address and get a yes. The second call, with the same `designId` and that token, publishes, then has iter0 fetch the address itself and reports `live`. A live site that is already up to date answers `already_live` with no confirmation (and re-checks an address iter0 has not confirmed yet) |
| `iter0_unpublish_site({designId, confirmationToken?})` | Take a live site offline, same two calls. The saved design and the address are kept, so publishing again brings it back at the same address |
| `iter0_publish_status({designId})` | "Is it live?" Read-only: `not_published`, `published`, `offline` or `suspended`; `live` with `lastConfirmedAt` (iter0's last confirmation that the address served the current release: an earlier check, not one made now, so the answer reads "last confirmed live at ...", never "loading right now"), `upToDate` (the live copy is the saved version), the address, the free address on offer if never published, and the account's other site if its one included site belongs to another design |

How it is held:

- **Offered only when `ITER0_HOSTING=1` and the ChatGPT extensions are on** (`mcpPublishingEnabled()` in `src/lib/mcp-extensions.ts`). Otherwise
  the three tools are absent from `tools/list` and a call to one is "Unknown tool", before any sign-in. The read-only serving deployment
  (`ITER0_HOSTING_SERVING=1`) never offers them, as the hosting HTTP routes refuse there too. The hosting docs say production needs
  `iter0.app` on the Public Suffix List first, so this ships dark until hosting is live.
- **Only the design's owner.** The owner is the account that owns the credential on the call; arguments naming an owner are refused. The
  store scopes every read and write to that owner, so another account's design is `design_not_found` (404) and nothing about it is returned.
- **Who may call (R1, matches `iter0_restore_version`).** The three tools pass the same single sign-in check in `src/app/api/mcp/route.ts` as
  restore, undo and the edit tool, so they take the same callers: a connected-app OAuth token, or the owner's own scoped API key. An API key
  carries its owner, so it can only ever reach that owner's designs (a stranger's key gets `design_not_found`, and a confirmation earned
  by one account is `confirmation_invalid` for another). Publish and take-offline need `sites:edit`, the status check `sites:read`; a
  read-only, build-only or older unscoped key is refused before the tool runs, exactly as for restore. Requiring OAuth for publishing alone
  would be a small route change; it was not made here because the aim is the same callers as the other write tools.
  `src/app/api/mcp/publish.test.ts` runs the real route and API-key check and pins this table.
- **Confirmation token.** HMAC-signed with `BETTER_AUTH_SECRET` under its own context string, ten minutes, a nonce per quote, bound to the
  owner, the design, the action and what was shown (the address and saved version to publish, or the live generation to take offline). A
  token for another account, design, address or action, a tampered or expired one, or one signed with another secret is
  `confirmation_invalid`. A retry of the same token derives the same request key, so a lost reply replays the first publish instead of
  publishing twice. If the saved page changed after the person confirmed, the store refuses (`site_changed`) and nothing goes live.
- **Scopes.** Publish and take-offline use `sites:edit` (as restore and undo do); the status check uses `sites:read`. They spend nothing, but
  the OAuth consent line for `sites:edit` still reads "Edit a site using your credits" (no UI change in this lane).
- **Honest "live".** A publish call says `live` only when iter0 itself fetched the address in that call and saw this release; a committed
  publish alone is reported as published, not live, with a pointer to `iter0_publish_status`. The status check (and `already_live`, when it
  relies on an earlier check) is read-only and does not fetch, so it reports `lastConfirmedAt` and words the answer "last confirmed live at
  <time>". A fresh fetch was not used there because the fetch also writes the observation, and the status tool is declared read-only.
- **Unknown outcome (R2).** If the store fails in a way that is not one of its own refusals (a dropped connection, a timeout, a commit that
  errored), the change may still have been applied. The reply is `outcome_unknown`: it never says "nothing was changed", tells ChatGPT to
  call `iter0_publish_status`, and says the same call with the same `confirmationToken` is safe to repeat (the token maps to one request key,
  so an applied publish is replayed and a take-offline is recognised, never done twice). "Nothing was changed" is kept only for the store's
  own refusals, which it raises before it commits, and for failures before it was asked (reading, signing, choosing a database).
- Refusals are distinct plain outcomes: `email_unconfirmed`, `site_elsewhere` (the one included site per account is tied to another
  design), `address_taken`, `address_invalid`, `address_locked` (a live site's address cannot change), `site_suspended`, `rate_limited`
  (5 a minute and 30 an hour per account, from the store), `hosting_unavailable`.

Tests: `src/lib/mcp-publish.test.ts` (tool logic), `src/app/api/mcp/publish.test.ts` (flag matrix, scopes, route, schemas) and
`src/lib/mcp-publish.integration.test.ts` (real PostgreSQL: owner isolation, confirmation, retry, free).

## 8 October approval and discovery repair

The production endpoint returned seven tools without UI metadata and rejected
`resources/list`. Its production `ITER0_CHATGPT_EXTENSIONS` setting was unset.
The default now offers all twelve tools and three `ui://` resources with
`_meta.ui.resourceUri` and `text/html;profile=mcp-app`. These are the current
MCP Apps fields; OpenAI documents `openai/outputTemplate` as a compatibility
alias, not a requirement for new integrations.

To test before review: open [ChatGPT Plugins](https://chatgpt.com/plugins),
select **+ → Add custom MCP server**, use `https://iter0.com/api/mcp` (or the
train's verified HTTPS Preview), select OAuth, review the warning, and choose
**Create as a plugin**. John connects the intended iter0 account himself.
Install the resulting plugin, open a new conversation, and choose iter0 from
the **@** menu. After the train deploys, open the connection and choose
**Refresh**, then start another new conversation. Check that discovery shows
the builder, confirmation tool and three UI resources before testing any spend.

For a local Work/Codex package that must use this registered ChatGPT connection,
copy its `plugin_asdk_app...` technical ID from the connection's browser URL.
Map that actual ID in `.app.json` and reference the file through
`extensions.com.openai.apps`. The repository's portable package currently
declares a direct MCP URL and has no registered mapping; inventing an ID would
not connect it. Work/Codex local installation and a ChatGPT registered
connection are different installation paths. Current OpenAI documentation
supports optional UI from an MCP server; it does not establish that John's
specific installed desktop version renders it in both Chat and Work modes.
This repair does not claim that host-specific proof. OpenAI identity hints
alone are insufficient, so text-only hosts retain a working fallback.

For reviewers: **platform.openai.com → Plugins → Upload new or existing
plugin → Upload plugin** creates the draft. Open **MCPs → Connect**, check the
URL and OAuth, complete the domain verification/authentication, and inspect
the scanned tools; use **Rescan** after server updates. Enter the dedicated
review account privately under **Metadata & Skills → Review information →
Review details**. Reviewers use that account and the server's advertised
resources; uploading a draft alone does not demonstrate a card in a chat.

Sources checked 8 October 2026:
[UI protocol](https://developers.openai.com/plugins/build/chatgpt-ui),
[connect, test and refresh](https://developers.openai.com/plugins/deploy/connect-chatgpt),
[registered mappings and local packages](https://developers.openai.com/plugins/build/plugins),
[portal and reviewer setup](https://developers.openai.com/plugins/deploy/submission).

The Show 3 label was already correct in released `ae4136a0`; its original
label/price tests are retained. The approval page now distinguishes a missing
request, unconfirmed email, mismatched account, expiry, approval and use.
The switch control signs out successfully before navigating to sign-in with
the same request; a failed sign-out offers a retry and does not navigate.
No prices, approval authority, charge/settlement logic or schema changed.

## Earlier extension handoff

This package is version 0.3.0 (v12 ZIP; `plugin.json`). The widget reports its UI
revision as `appInfo.version` 0.4.0; no new ZIP has been built for it, and
`qa/evidence/chatgpt-extensions/package-receipt.json` still describes the earlier
v8 ZIP, not this head. The current draft combines PR502/507, current main,
PR522's charging path and PR529's Show 3 cards in the existing PR507 branch.
It is not submitted or activated.
Extension discovery and data are enabled when `ITER0_CHATGPT_EXTENSIONS` is unset
or `1`; an explicit `0` (or any other value) hides widgets and their read tools,
while retaining the seven base tools plus text confirmation. This repair adds no
migration; PR522's existing migration 082 enables connection credit consent.
Flag owner: r14 release leader. The shipped cards are discoverable by default;
the flag remains an explicit rollback switch. Runtime OFF also disables signed
preview reads. Production rollout still belongs to the release train and John's review.

## What is wired

| Tool | Output / resource |
| --- | --- |
| `iter0_open_builder({})` | The Projects area (SIT-376): greeting, composer box (Show 3 / Build sends the words to chat, which quotes first), starters, search, first page of projects; global entrypoint; `ui://iter0/builder/v15.html` |
| `iter0_list_my_designs({cursor?, query?, limit?})` | One page (default 12, max 24) of live designs newest first, `nextCursor` for the next page, name search, expiring thumbnails, read-only balance, `firstSiteFree`, the account's first name |

Why paging (SIT-376, measured 12 Oct 2026 in ChatGPT): opening iter0 returned all
70 of an account's designs (104,696 bytes of tool output) and the card requested
all 70 thumbnails at once; a cold thumbnail is a server-side Chrome render (9 at a
time, 32 queued, the rest refused). The card now gets 12, loads thumbnails lazily
and reads later pages with the cursor as the founder scrolls.
| `iter0_get_design({designId})` | Owned HTML and page-bound section IDs; for a revisioned site also its pages, committed versions and, when one exists, the background research team; screenshot detail in the app |
| `iter0_restore_version({designId, versionId, confirmationToken?})` | Two calls. The first changes nothing and returns a short-lived token bound to the owner, design, version, head and canvas checkpoint; ChatGPT must ask the person before the second call restores. Free |
| `iter0_show_three` / `iter0_get_design_set_status` | PR529's existing three screenshot cards and charging flow; `ui://iter0/show-three/v2.html` |
| `iter0_create_site` / `iter0_get_site_status` | PR522's existing charging flow; the widget uses `quoteOnly: true` to start nothing; `ui://iter0/build-status/v2.html`; once the run has saved a design, its research team |
| `iter0_edit_site` with `sectionId` | Existing bounded selection at the edit boundary. Every paid call quotes and confirms the exact price through the card or chat, then runs the identical edit. The widget only asks for the change in chat |
| `iter0_edit_site` with `designId` | SIT-386: the model sends only `designId` and the change; iter0 loads the owner's saved single page itself, so page code never enters the conversation. The quote carries the instruction and a short digest of the page; on confirm iter0 reloads the page and a changed digest returns `page_changed` with no charge. A pasted page may still be sent as `currentHtml`. A saved edit's reply (quote and confirmation alike) carries no page anywhere, `_meta` included, because ChatGPT dropped a reply with whole pages in it (12-13 Oct live; a test holds both replies under 20 KB for a 300 KB page): the card draws the edit from `previewImageUrl` and the model sees a headline and summary. Only an edit that could not be saved sends its revised page, in widget-only `_meta`, since nothing else holds that paid result. A saved edit's reply also carries `updatedAt`, the time the save gave the design: the card shows it as "Edited ..." in its Projects list at once, and opening a design refreshes its row from the design read, so the list no longer says "6 hours ago" after a fresh edit |
| `iter0_get_design({designId})` | SIT-386 fix 4: ids and text only. The design, its pages and versions, `sections` (ids and labels), a headline and summary, and signed `previewImageUrl`/`pagePreviewImageUrl`/`phonePreviewImageUrl`. No page code anywhere in the reply, `_meta` included: a 2.3 MB design with three data-URI images read as a 2,306,518-byte reply and now reads as about 4.7 KB (a test holds it under 20 KB). The card draws the page from the preview images and the side list picks the section; it measures nothing until the person points at the preview (see `iter0_design_layout`) |
| `iter0_design_layout({designId})` | SIT-386 lazy outline (John, 13 Oct: "that should only happen when you click the page or click edit, isn't that a way to have both?"): app-only (`ui.visibility: ["app"]`, `openai/visibility: private`, so ChatGPT's model never sees or calls it), read-only, same sign-in and owner check as `iter0_get_design` (another account's design is `design_not_found`). Opening a design stays light. The first time the person points at the preview, picks a section, or asks ChatGPT to change one, the card calls this once per design and save. The reply carries a LIGHT copy of the saved page in widget-only `_meta.layoutHtml` and only `{designId, layout, bytes}` as structured content (no page text reaches the conversation). The copy has scripts removed and every `data:` payload (image `src`, `srcset`, `poster`, CSS `url()`, fonts) replaced: an image becomes an empty SVG of the same natural size (read from the PNG, JPEG, GIF, WebP or SVG header) so the section around it keeps its height, or loses its `src` when the size cannot be read. Capped at 600,000 bytes (a source over 8,000,000 is not parsed): over that, `layout: "too_large"` with no page. A revisioned site or empty page is `layout: "unavailable"`. The card measures the copy in the same hidden frame as before, so hover and click outlines work exactly as when the page was sent. Any failure or `too_large` draws no outlines, shows no error, and leaves the side list as the way in (the idle hint then says so); opening the design again retries a failure |
| `iter0_undo_edit({designId, undoToken})` | SIT-386: app-only. `undoToken` is a signed receipt (owner, design, digests of the page before and after, save version, 1 hour); iter0 keeps the page the edit replaced in `mcp_edit_undo` (migration 086, one row per design, latest edit only, removed with the design) and restores it only while the edit is still the current page. No page travels in either direction. Without the table the edit still saves, with no Undo. A record never replaces one for a newer save of the same design (a delayed write loses), so only the latest edit has Undo. A card opened from the earlier templates (builder v9 and earlier; Show 3 and Build status v8 and earlier) still sends `html`: it is accepted and ignored, and a receipt issued before the kept copy existed is refused as expired |

The resources are self-contained HTML with a standard JSON-RPC `postMessage`
bridge. No visible or network frames, provider calls, checkout, plan names or
upgrade buttons. The one frame is a hidden, never-shown, script-free sandboxed
`srcdoc` frame the builder creates only to measure where each section sits on a
page it is handed (see the section highlight below); it is removed once measured.
Since SIT-386 fix 4 iter0 hands it no page when a design is read, so no frame is created at open; it appears after the first pointer at the preview, with the light copy `iter0_design_layout` returns.
CSP resource origin and UI domain are `https://iter0.com`; connect and frame
domains are empty. The host fetches tools using its OAuth connection. Design
previews use a 24-hour HMAC capability scoped to the owner and design (a card
left open for a while must still load its image); the preview handler rechecks
ownership and returns raster bytes with no-store. If a full-page render fails to
load, the card falls back once to the design's cached thumbnail.
Direction screenshots use a separate owner/direction-bound HMAC token lasting
24 to 25 hours (expiry rounded up to the hour). Their handler rechecks ownership;
successful raster responses use private, max-age=3600, and refusals use no-store.
Existing thumbnail rendering sanitizes source and uses the credentialless
network guard. The widget never executes a generated site's scripts.

Initial render consumes the host's tool result, not a duplicate list call.
Polling uses one five-second timer and stops on terminal status. It continues
beyond 30 checks and retries temporary host refusals. Section selections use
`ui/update-model-context` and never edit or spend. A quote starts nothing.

John chose option A on 8 October 2026 (answer: "a"): the connected-app grant
permits valid quote confirmations. The card displays the exact-price pill;
its second tap redeems the price quote reference through `iter0_confirm_paid_action`.
The stored quote binds the owner, action, payload and price, expires in 15 minutes,
and has a one-use database latch. Client presentation hints grant no authority.
The server accepts a valid connected-client confirmation without proof of a
human click; the price quote and the account credit balance enforce payment
authority. There is no separate connected-app daily spending cap (John, 9 Oct:
"yes remove it").

The 15 minute life of a quote is deliberate and was not lengthened (SIT-386, John 13 Oct,
"This confirmation expired"): a quote is single-use and tied to the exact page it priced, and
the longer it lives the longer a price made on an old page could be confirmed. When the price
button's timer runs out, the card says "This quote expired. Nothing was spent." and shows
Get a new quote in its place. That one tap asks again with the quote's own request (for an edit:
the same change and the same page digest), with no approval receipt and no confirmation. The
server prices it again on the same page, or refuses with `page_changed` ("Nothing was charged")
if the page changed since, in which case the card shows that reason and keeps the button. A
direction's price is asked again the same way. Nothing is confirmed or spent by that tap.

`quoteId` is a public price quote reference.
The reference locates the existing approval record; all money checks stay
server-side. The widget keeps its retry receipt in hidden metadata.
Ordinary model-visible quotes omit that receipt; yes in chat uses the public
`confirmation` object. Text clients also work with widgets OFF.
Repeated host notifications for that same quote preserve the armed Confirm.
Completed direction sets preserve their buttons on identical host results;
changed direction contents discard cached quotes and require fresh consent.
While a widget call is pending, the card shows "Starting…" and the
fallback "or reply yes in chat". If the host rejects the bridge call or returns
no tool result, the card posts acceptance of the same quote to ChatGPT.
The model then redeems that same quote with `iter0_confirm_paid_action`,
without a new quote or changed arguments. A server failure or uncertain
timeout shows recovery text without automatically starting a different action.

Host contracts checked 10 October 2026:
- https://developers.openai.com/plugins/reference
- https://developers.openai.com/plugins/build/chatgpt-ui
- https://developers.openai.com/plugins/changelog
- https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx

Initial model calls receive the hidden card receipt even without host hints,
and never receive an approval-page URL or instructions to open one. They also
receive the same price quote confirmation in structured content for text clients:
show the exact price and call the confirm tool only after the person says yes
in chat. The confirm tool is visible to model and app, with readOnlyHint=false,
destructiveHint=true (credit transaction), idempotentHint=true (single use),
and openWorldHint=true (authorized public reference URLs). These annotations
inform host confirmation; the server enforces the money limits independently.
Widgets remain ON by default. OFF disables widgets, UI resources and preview
reads while retaining the exact-price text/confirm fallback.

The compatibility approval page keeps its masked account-mismatch hint and
Switch account control. Existing approved receipt retries, legacy markers,
API-key ownership and failure/refund machinery are preserved. A model-supplied
amount or presentation marker alone cannot create payment authority.
Neither presentation metadata nor the confirmation envelope enters the paid
payload hash or forwarded request.
The v3 resource URIs prevent new mounts from reusing the page-approval widget's cache identity;
the server boundary also protects v1 widgets already mounted. The exact quote,
approval identity, retries, OAuth and ownership boundaries remain in charge.

The existing free signup wallet gives three credits under the default policy.
Show 3 and a build each cost one credit; quoting costs nothing. The list tool
does not create/reset the wallet. It advertises the free first site only for a
confirmed free account with sufficient existing plan credits, no top-ups, no
saved designs and no prior run. Existing accounts may qualify on those facts;
there is no new ChatGPT-only grant. Hosted signup remains unverified.

## Design handoff

The carousel and progress resources reuse Sonnet's supplied chrome from
`lanes/r14/chatgpt-app/widgets/_src/`. Their demo scripts and fictional results
are removed. The fullscreen resource reuses Sonnet's builder CSS and icon
sprite for its preview canvas, section list, zoom/Fit and open controls. Those
controls use owned design data and the real host bridge. The source's simulated
pages, selections and nonexistent tool calls are replaced. Saved edits,
multiple-page canvas operations and in-widget export or GitHub actions remain
outside this engineering preview.

UI pass (stacked PR): all three views are rebuilt from shared sources in
`ui-src/` (`base.css`, `builder.css`, `icons.svg`), joined into the templates by
`scripts/build-chatgpt-extension-resources.mjs`. Colours, surfaces and borders
come from ChatGPT's host variables (`hostContext.styles.variables`), so light and
dark follow ChatGPT; the font is the system stack and icons are an embedded
outline set.

Controls in the builder now, and where each one's data comes from:

- Sections: a list of the saved page's real sections, plus click-to-select and
  hover boxes drawn over the screenshot, measured in a hidden frame from the page
  code. SIT-386 fix 4 stopped sending that code when a design is read (it made the
  card slow to open), so opening a design measures nothing. The boxes come back
  lazily (SIT-386 lazy outline): the first time the person moves over or clicks the
  preview, picks a section from the list, or asks ChatGPT to change one, the card
  calls the app-only `iter0_design_layout` once, gets a light copy of the page, and
  measures it as before (cached per design and save, width and a hash of the exact
  page; a measurement that finishes after the page changed is dropped). The idle
  hint says "Click a section on the page" while outlines are available and "Pick a
  section in the list" once a read has failed or the page is too large. A selection only
  attaches context for ChatGPT; it never edits or spends. The existing selection
  dock's Ask ChatGPT to change this control sends a follow-up message with those
  exact design and section IDs, asking for the change before any edit starts.
- Device switcher (desktop / phone): enabled only for legacy HTML designs, which
  have signed page and phone renders. A revisioned site keeps the one owned head
  thumbnail, so Phone stays disabled and no device URL is advertised. The desktop
  page is rendered and laid out 1440 CSS pixels wide (our sites are designed for
  1440; John, 13 Oct), the phone page 390 wide at 2x; the cached 1280x800
  thumbnails (Projects list, earlier versions, the fallback picture) keep their size
  and are labelled Desktop 1280. The person's choice of device is never rewritten by
  a redraw: a page with no phone picture (an earlier version, a design read without
  a phone link) draws desktop, and the choice comes back with the next page that has
  one. A page still being made shows a calm loading state in its frame, never a
  blank white page. If the phone page fails the frame says "Phone preview didn't
  load" with Try again (never the desktop picture); a second Try again reads the
  design again for fresh signed links. Once the desktop page has drawn, the phone
  page is requested quietly so the toggle is quick. On the server a device view is
  rendered once per saved version (`unstable_cache`, in-flight dedupe), answers
  `If-None-Match` with 304 before reading the page, shoots a phone page taller than
  8000 px at 1x instead of 2x squeezed back down, and falls back from the 2x shot to
  the 1x shot if the sharp one times out. A failed render is logged
  (`[mcp-preview] render failed`).

- Pages: the real page list of a revisioned site (one Home page otherwise).
  A page without its own preview asks ChatGPT to show it.
- Versions: the committed history, newest first. The server sends no image for an
  earlier version, so selecting one shows "Preview unavailable for version N"
  with Back to current and Restore this version. Restore only sends the exact
  design and version to chat; ChatGPT must ask the person, then call
  `iter0_restore_version`. Restoring adds the old content as a NEW current
  version and the old versions stay in the history. The result names that new
  version and the version it copied, and says whether it is still current. If
  the post-commit history read fails, `current` is null and the response asks
  for a fresh design read; it does not infer freshness from an earlier snapshot;
  refusals are told apart (canvas changes not saved, an edit in progress, the
  site changed since the confirmation, storage unavailable) and write nothing.
- Research team: rows for the business, market and customer researchers (each
  keeps its own row), with hosts, sources read and searches run. A run that
  stopped or failed is worded as stopped or not finished, never as finished. It
  is keyed by the design's Launch CEO session, so it appears for `iter0_get_design`
  and, once a design is saved, `iter0_get_site_status`. A Show 3 batch has no
  design or CEO session, so its resource shows research only if a producer
  supplies it; today none does.
- Zoom ("- 72% +") and Fit (its own control beside it) change only the local preview scale; Fit is worked out for the page's own width (1440 for desktop). Open in iter0 opens an
  allowlisted link with `src=chatgpt`. Add a page and Show me 3 new designs send
  messages to chat; none of these widget controls runs a tool that spends.
- Ready builds offer Open the builder. It requests fullscreen through
  `ui/request-display-mode`, checks the host's actual returned mode, then reads
  the owned design. The same builder markup and scoped stylesheet are reused.
- Reload uses optional synchronous `window.openai.setWidgetState` and reads
  `window.openai.widgetState`. Only presentation choices live in `privateContent`;
  saved site HTML, signed URLs, confirmations and credits remain on the server.
  Choices apply only to a matching design and currently available pages/versions.
- Publish menu: four links that open iter0 (preview link, domain, GitHub,
  download). The card itself publishes nothing. When built-in hosting is on,
  ChatGPT can publish by tool instead (`iter0_publish_site`, see the 13 October
  section at the top); the menu is unchanged.

Not in the UI because no tool or data exists yet: A/B/C designs inside one
design, a findings panel, saved edits and canvas editing, historical previews.

No agent visual approval is claimed. Listing screenshots, actual ChatGPT
desktop/mobile testing, further builder interaction work and independent review
belong to the leader's next review. Regular plugin submission remains separate.

## Official contracts checked on 7 October 2026

The runtime uses portable MCP Apps methods for shared features, as recommended
by the [current OpenAI UI guide](https://developers.openai.com/plugins/build/chatgpt-ui).
The [current component reference](https://developers.openai.com/plugins/reference)
keeps these compatibility aliases. The harness uses the same signatures:

| Capability | Runtime / host contract |
| --- | --- |
| `toolOutput` | `ui/notifications/tool-result` supplies `structuredContent` |
| `callTool(name, args)` | `tools/call` with `name` and `arguments` |
| `sendFollowUpMessage({prompt})` | `ui/message` with user role and text content blocks |
| `openExternal({href})` | Runtime uses `ui/open-link({url})`; allowlisted iter0 links carry `src=chatgpt` |
| `requestDisplayMode({mode})` | `ui/request-display-mode`; honor the actual returned `mode` |
| `setWidgetState(state)` | Optional synchronous OpenAI extension; never await it |
| `widgetState` | Optional per-instance presentation snapshot, never business authority |
| `theme` / `displayMode` | Initialization host context and host-context-changed notifications |

The harness initialization includes required `hostInfo`, `hostCapabilities`
and `hostContext`. Unknown request methods return JSON-RPC method-not-found;
they do not falsely succeed. Its alias shim is a local host fixture, not proof
of ChatGPT behavior. The hidden measuring frame still needs real-host CSP
qualification: the resource declares no network frame domains, and the local
harness does not prove ChatGPT will permit a sandboxed `srcdoc` frame.

- Global entrypoint: “The server MUST accept `{}` as the tool arguments when the entrypoint opens.”
  [OpenAI MCP extensions specification](https://github.com/openai/mcp-extensions/blob/main/docs/spec.md#global-entrypoint).
  The entrypoint accepts empty arguments and resource metadata declares fullscreen.
- UI association: “Declare the UI resource with `_meta.ui.resourceUri`.”
  [OpenAI UI guide](https://developers.openai.com/plugins/build/chatgpt-ui).
  Tool metadata uses this field; resources are `text/html;profile=mcp-app`.
- “You can implement the postMessage protocol directly”
  [MCP Apps overview](https://modelcontextprotocol.io/extensions/apps/overview).
  The runtime implements initialization, tool-result/context notifications,
  tools/call, ui/message, ui/open-link, ui/update-model-context, size and teardown.
- [OpenAI extensions guide](https://developers.openai.com/plugins/build/extensions)
  supplies the `_meta["openai/ui"].entrypoints` registration used here.
- [MCP Apps specification](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx)
  defines the resource metadata, CSP, lifecycle and bridge messages.
- [Current SDK protocol types](https://github.com/modelcontextprotocol/ext-apps/blob/main/src/spec.types.ts)
  define `appInfo` and `appCapabilities` at initialization, message `content` as
  an array of content blocks, and host rejection through `isError`. The prose
  specification's older message example uses a single object; this runtime uses
  the current typed SDK contract. A rejecting host test covers that discrepancy.

## Reproduce locally

First run the machine's cpu-ok check; no dependency install is needed.

```powershell
node scripts/build-chatgpt-extension-resources.mjs
node scripts/check-chatgpt-extension-types.mjs
node --test scripts/chatgpt-ui-bridge.test.mjs
node --import tsx --test src/lib/mcp-extensions.test.ts src/lib/mcp-extension-data.test.ts src/lib/mcp-extension-data.integration.test.ts src/app/api/mcp/extensions.test.ts src/app/api/mcp/preview/route.test.ts src/lib/mcp-builder-data.test.ts src/lib/mcp-preview-contract.test.ts src/lib/chatgpt-section-geometry.test.ts src/lib/chatgpt-research-card.test.ts src/lib/chatgpt-extension-receipt.test.ts
node --import tsx scripts/qa/chatgpt-extensions-harness.mjs
powershell -NoProfile -File scripts/package-chatgpt-extension.ps1 -Destination <v8.zip>
```

The harness launches and closes its own loopback server and Chrome, prints its
PID, renders real resource HTML through the actual MCP handlers with explicit
store/provider fixtures, and proves quote-only selection, progress polling,
deep links and section context at 1200x820, 900x820 and 390x844, in light and dark. Its preview fixtures are
fictional Shiplog pages. It also exercises the production raster renderer.
Evidence is `qa/evidence/chatgpt-extensions/`, including a JSON receipt. It does
not prove paid provider generation or hosted ChatGPT behavior. The receipt names
the commit the harness ran on (`testedBaseHead`) and the SHA-256 of each served
resource; it is evidence only for those exact resource bytes. A focused test fails
when the checked-in hashes differ from the shipped resources, so rerun the harness
(with `SHOT_DIR` pointing outside the repo to keep screenshots out of Git) and copy
`receipt.json` after any template, runtime, CSS or icon change.

Phase 1 explicitly forbids local browsers. The existing receipt is historical
PASS evidence for its named resource hashes, which differ from the updated
resources. It is not current-head proof. The unchanged receipt check will fail
until the separately assigned Phase 2 QA lane runs the harness and returns a
new receipt. No browser result or hash has been invented to clear that gap.

The node_modules junction points at release-r7. Overall lockfile SHA-256 differs
(`9b85048a…` versus `3c424ba9…`); the ten relevant directly used package versions
match. Local checks are provisional. Exact-lock CI, Preview SHA and hosted QA
are still required on the final integration candidate; no full build or suite
was run in this lane.

Rollback for this draft is runtime flag OFF, then a reviewed revert if needed.
There are no extension-specific schema changes or credit policy changes to undo. PR522's
existing consent migration remains additive and uses its own qualification path. The flag
does not interrupt an already approved build; existing delivery owns it.

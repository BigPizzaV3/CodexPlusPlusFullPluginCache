---
name: studio-asset
description: Fill one Studio template for an account, a prospect or a candidate - pick the template, check the data its fields need, run the fill with Ken or your own model, gate the page, create each person's link and put it in a touch. Includes the sample campaign for a prospect.
---

# Studio assets

A Studio asset is one template filled for one account (or, on a recruiting campaign, one candidate): a page on the workspace's own link host, with one link per person (`https://{host}/{account-slug}/{page-slug}-for-{first-name}`), human-confirmed view tracking and account signals. This skill fills a specific template: it picks the template, checks the data each field needs, runs the fill, gates the page, creates the links and hands them to a touch.

Building or editing the template itself is the `studio-template` skill.

Studio has no tool in this app: you cannot fill, gate, publish or link a page here. The user does each of those in Studio: the templates are at https://app.ken.so/<workspace id>/demo/studio, and an account's pages are on its Assets tab (https://app.ken.so/<workspace id>/demo/accounts/<account id>?tab=assets). What you can do here: pick the template with the user, check the data its fields need, judge the page before its first link, and put the link in a touch or a draft reply.

The tools this guide uses (threads and Kenso Search) take `workspace_id`. Send it on every call when the user can see more than one workspace (`list_workspaces()` lists them).

## The rules

- **Nothing sends.** Pages, links, touches and drafts all wait for a person: a person approves every touch and every send.
- **Never invent.** A field you cannot fill from real data falls back; it is never made up. No invented customers, numbers, prices, dates, times or offers, and every number on a page traces to its source.
- **Gate before the first link.** A page in review, on its fallbacks or failing the confidentiality check never gets a link.
- **Costs are said out loud.** Run on accounts and Create page show the credit estimate before a run: say the number to the user, and say before first links go out on many pages that each costs 1 credit.
- **Vendor names never reach a reader**, and prospects never read "demo" or "reverse demo".
- Changing a template that live client campaigns use, or pinning one to a sending campaign, needs a yes that names that client: that is the `studio-template` skill's job.

## Step 0 - Check Studio is on

Studio is in beta behind the workspace's `studio` flag.

- If https://app.ken.so/<workspace id>/demo/studio does not open for the user, Studio is not on for this workspace. Say so in one sentence and stop.
- Recruiting pages need `recruiting`, and Google Doc and Word exports need `rd_docs`. When a button is missing, that part is not on: say so and carry on with the rest.

## Where to start

| The user says | Start at |
|---|---|
| "Fill the audit template for Northwind." | Step 1 |
| "They asked to see the work." / "Send each target a sample campaign." | "Sample campaign for a prospect" below |
| "Is anyone reading the page?" | Step 8 |

## Step 1 - Pick the template and open its fill guide

The templates are at https://app.ken.so/<workspace id>/demo/studio. A run needs a published version: a card that says Draft has none yet. With no template that fits, building one is the `studio-template` skill.

Match the template to a starter by its page slug and recipe steps (its builder's Variables step, https://app.ken.so/<workspace id>/demo/studio/<template id>?step=variables, shows its slots and recipe). Then open that starter's fill guide: `load_ken_skill` with name `studio-asset` and reference `references/<file>`. Each guide says what every field needs, where its data comes from, what to set up before a run, and what to check before the first link:

| Starter | Page slug | Fill guide |
|---|---|---|
| `rd-doc`, sample outbound campaign doc | `outbound-campaign` | `rd-doc.md` |
| `rd-ken-native`, we built you a campaign | `campaign-preview` | `rd-ken-native.md` |
| `rd-your-product`, your product on their data | `what-we-found` | `rd-your-product.md` |
| `audit-rewrites`, website audit with rewrites | `site-notes` | `audit-rewrites.md` |
| `benchmark-report`, peer benchmark report | `peer-benchmark` | `benchmark-report.md` |
| `case-study`, built for you case study | `customer-story` | `case-study.md` |
| `event-invite`, dinner or webinar invite | `invite` | `event-invite.md` |
| `role-pitch`, role pitch for one candidate | `role` | `role-pitch.md` |
| `roles-for-you`, roles for you | `roles` | `roles-for-you.md` |

The Library (https://app.ken.so/<workspace id>/demo/studio?library) shows every template Kenso designed, with a sample page. The workspace's own template always wins over a guide: a copy may have changed slots or steps. For a template that matches no starter, build the same table yourself from its Variables step (required, limits, fallback, and which step fills each slot, from what).

## Step 2 - Pick the accounts and check their data

The accounts are the workspace's accounts in Accounts (https://app.ken.so/<workspace id>/demo/accounts). A recruiting template runs on a campaign's leads instead (Step 3).

Then check what the fill guide says the fields read, before you spend anything:

- **Research.** Most starters read the account's research (its summary and why now), on the account's Research tab (https://app.ken.so/<workspace id>/demo/accounts/<account id>?tab=research). Refresh research there is charged, so say so first.
- **The homepage** for starters that scrape it: the account needs a primary domain that loads without a login.
- **Datasets** for `benchmark-report` and `case-study`: this app cannot list them, and Studio has no dataset screen. A page whose report or story falls back usually means a missing dataset or row; the fill guide says which.
- **Template settings** such as the event details or a webhook endpoint: a template still holding a starter's example values is not ready to run.
- **Kenso Search** finds people only in the United States, the United Kingdom, Canada, Australia, Ireland and New Zealand.

## Step 3 - Choose who writes, estimate, run

Runs start in Studio, with Kenso writing the pages:

- **Many accounts:** open the template (https://app.ken.so/<workspace id>/demo/studio/<template id>) and press Run on accounts. The user picks the accounts, reads the credit estimate, and runs only after a yes.
- **One account:** Create page from template on the account's Assets tab, or https://app.ken.so/<workspace id>/demo/studio?for=<account id>, where a template card opens Run on accounts for that account.
- One template has one page per account: a second run reuses it, and a live or building page is left out.
- A run takes at most 500 accounts; a workspace fills 5,000 pages a day.
- A recruiting campaign builds one page per lead itself, one step ahead of the step that carries the page link (Step 7). The template must be the one pinned on that campaign.

## Step 4 - The brand kit

A page styles itself from the workspace brand kit (Brand kit in Studio): colors, fonts, logo, icon and name. A page follows the live kit until its first link goes out, then keeps that brand: a later kit change or refill never restyles a page that was sent. Fill an empty kit before the first links go out.

## Step 5 - Follow the run and gate each page

The run shows its progress in Studio. A fill takes minutes: the user checks back, not you in a loop. The account's Assets tab then shows each page as Ready, Needs review or Failed.

Ask the user to open each page (its card on the account's Assets tab, or https://app.ken.so/<workspace id>/demo/studio/pages/<page id>) and paste or describe what it shows. A page passes only when:

1. It shows Ready. A page that failed its grade shows Needs review.
2. Every section shows real content, not the template's default text, except the ones its fill guide says may fall back.
3. Every number traces to its source (site, dataset, endpoint, search result), and the guide's own checks hold.
4. Confidentiality: no email address or phone number except the sender's own, no other client's names or data, no vendor or tool names, no "demo".
5. Someone read it once top to bottom, on desktop and mobile.

A Needs review page failed a grade after its retries or holds data that broke a rule. A person refreshes it once (Refresh on the page, charged like a fill) or fixes it on its Customize screen (https://app.ken.so/<workspace id>/demo/studio/pages/<page id>/customize): their save moves it to Ready.

## Step 6 - Create the links

The page's Links block has Create a link for, which makes one person's link, and Copy link. Copy link on a page with no link yet publishes it first, behind a 1-credit confirm.

- The first link publishes the page, charges 1 credit, sets it `live` and freezes its URL. More links are free; asking again for the same person returns the existing link.
- A doc page can also go out as a Google Doc in the member's Drive or a Word file in their OneDrive (flag `rd_docs`): Export on the page.

When a link is refused:

- Not enough credits: nothing was created. Tell the user.
- No link host: the workspace needs link tracking on a sending domain first.
- A page in review or not filled gets no link: Step 5.
- A retired page comes back with Republish (1 credit).

## Step 7 - Use it in a touch

- **Accounts:** Use in next touch, on the page or its card on the account's Assets tab, puts the link on the account's next open email, LinkedIn message or asset step, or plans a follow-up step two weeks out when none is open. The touch waits for a person in Today, and it can be approved only once the page is ready. Writing the touch around it is the `accounts` skill.
- **Campaigns:** a step carries the merge tag `asset_link`, written in double curly braces, and Kenso builds each company's page one step ahead from the campaign's pinned template; slot fallbacks cover anything not filled yet. Pinning is the `studio-template` skill.

## Step 8 - Read engagement

The page in Studio shows its engagement: human views, scanner opens, who viewed, time per section, clicks and meetings.

- Only human views are reads. Scanner opens are mail-security bots: never report them as reads.
- A meeting counts when it was booked after a booking click or within 14 days of a human view.

## After it ships

- **Hand edits:** Edit on the page (or its Customize screen) changes its text, sections, styles and images on this page only; the template and the other pages stay as they are. A live page is republished with the edit.
- **Refresh** reruns the fill, charged like a fill. A live page keeps its links.
- **New template version:** Update this page, in the page's version note, moves it to the latest published version and refills only what changed. It is charged: say so first. A page with its own layout that clashes asks Keep (stay on this version) or Take (drop this page's layout for the new version).
- **Retired** pages (30 days after the account's last activity) come back with Republish for 1 credit.

## Sample campaign for a prospect

When a prospect asks to see the work, build them a real sample: their campaign, aimed at their buyers, never a campaign that sells your product. Open `references/sample-campaign-for-prospect.md` and follow it. In short:

1. Find the reply (`list_inbox_threads(q="mitch@events.com")`) and check it is a real ask, not an out-of-office, a referral or a no.
2. Make the prospect an account and research their buyers from a real source. Stop when you cannot name them.
3. Fill the `rd-doc` (or `rd-ken-native`) template on that one account, as in Steps 3 to 5.
4. Gate the page: grade passed, every shown slot filled, every number real, no lead email addresses, no other client's data, no lead at the prospect itself.
5. Create their link and leave a draft reply on the thread. Nothing sends: a person reads and sends it.

## Credits

| What | Cost |
|---|---|
| A page, on its first link (shared or person) | 1 credit |
| More links on the same page | free |
| Republishing a retired page | 1 credit |
| Kenso writing `prompt` and `grade` steps (executor `"ken"`, refill, update-version) | model tokens at 2x cost |
| Your own agent writing them (executor `"agent"`) | no token charge |
| A `ken.copy` step, on any path | model tokens at 2x cost |
| Data steps | rate card; today's (`bind`, Kenso Search, `chart.data`, scraping, `webhook`, `dataset`) cost nothing |
| Previews, hosting, PDFs | free |

## What this skill cannot do yet

- No tool checks a page for leaked data or poached leads: you read what the user pastes yourself (Step 5).
- No tool sets a new workspace's plan, so a separate sample workspace needs a person to confirm it is on the Free plan.

## References

Open each with `load_ken_skill`, name `studio-asset` and reference `references/<file>`:

- One fill guide per starter: `rd-doc.md`, `rd-ken-native.md`, `rd-your-product.md`, `audit-rewrites.md`, `benchmark-report.md`, `case-study.md`, `event-invite.md`, `role-pitch.md`, `roles-for-you.md`.
- `sample-campaign-for-prospect.md`: the whole sample-campaign recipe, from the reply to the draft.

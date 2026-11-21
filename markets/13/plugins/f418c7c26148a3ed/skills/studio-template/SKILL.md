---
name: studio-template
description: Build, edit and manage Studio templates - start one from the Kenso template library or blank, write the bundle, validate, preview on real accounts, publish, manage versions and datasets, and pin a template to a campaign.
---

# Studio templates

Studio is Library > Studio in Kenso. A template is built once (a reverse demo, audit, report, landing page, event invite, calculator, recruiting page or cold email) and Kenso fills a copy of it for each account: a Studio page on the workspace's own link host. This skill covers the template itself: start it, write its files, check them, preview them on real accounts, publish, and manage versions, datasets and campaign pins.

Filling a template for one account, prospect or candidate, and sending each person their link, is the `studio-asset` skill.

Studio templates have no tool in this app: you cannot create, write, validate, preview, publish or pin a template here. The user does those in Studio (https://app.ken.so/<workspace id>/demo/studio). The parts Studio has no button for (slots, the recipe, datasets, webhook secrets and campaign pins) need an agent connected to Kenso's MCP server: Edit with your agent, in the template's builder, gives the line to paste into it. What you can do here: work out the brief and the type with the user, pick the starter, and say which button does each step.

## Step 0 - Check Studio is on

Studio is in beta behind the workspace's `studio` flag.

- If https://app.ken.so/<workspace id>/demo/studio does not open for the user, Studio is not on for this workspace. Say so in one sentence and stop.
- Extra flags: `recruiting` for recruiting templates, `studio_email` for the email format, `rd_docs` for Google Doc and Word exports. Without one, that part is missing: say which part is off and carry on with the rest.

## Where to start

| The user says | Start at |
|---|---|
| "Build a new Kenso Studio template." | Step 1 |
| "Edit Kenso Studio template 41." | Step 3. Ask what to change when the user has not said |
| "Which templates do we have?" | "Manage templates" |
| "Fill the pages for these accounts." | The `studio-asset` skill |

## Step 1 - Brief

Ask, or read from the conversation:

1. Who reads the page: role and kind of company.
2. What the reader should do next: book a call, reply, save a seat, run the numbers.
3. Which accounts it runs on: named accounts, a stage, or a campaign's companies or candidates.

Pick the type and the closest starter:

| `template_type` | Pick it when the page | Starter |
|---|---|---|
| `reverse_demo` | shows the account work you already did for them | `rd-doc` (doc with PDF), `rd-ken-native`, `rd-your-product` (your own endpoint) |
| `audit` | lists what gets in a buyer's way on their own site, with fixes | `audit-rewrites` |
| `report` | puts the account next to its peers, from your data | `benchmark-report` |
| `landing_page` | retells your closest customer story for them | `case-study` |
| `event` | invites them to a dinner or webinar and saves the seat | `event-invite` |
| `calculator` | lets them run the numbers, then book | none for now |
| `recruiting` | pitches a role to one candidate, or shows the roles that fit them (flag `recruiting`) | `role-pitch`, `roles-for-you` |
| `other` | fits none of these, or is a cold email (`template_format="email"`, flag `studio_email`) | none, start blank |

`template_format` is `page` (web only), `doc` (web plus a PDF download) or `email`.

Done when you can say in one sentence who the page is for, what they do next, and which accounts it runs on.

## Step 2 - Start the template

Check what exists first: the templates at https://app.ken.so/<workspace id>/demo/studio. Reuse one that fits, or Duplicate it from its card: the copy gets the source's latest published files and its datasets as a new draft. Pages and links are not copied.

To start from the Kenso template library, open the Library (https://app.ken.so/<workspace id>/demo/studio?library): search it, read a template's description, what it needs and its sample page, then Use this template, which copies it and opens its builder.

To start blank, New template has Build with your agent: it gives the line that has an agent connected to Kenso's MCP server build it.


## Step 3 - Write the bundle

The builder (https://app.ken.so/<workspace id>/demo/studio/<template id>) has the steps Plan, Brief, Variables, Draft and Review. On the Draft step, Edit changes the page in place (text, sections, styles and images) and Code edits `template.liquid` as text; Save stores the draft. Slots, the recipe, datasets and new files need Edit with your agent.

- Style the page from the workspace brand kit (Brand kit in Studio), never from a color or font you pick.
- Recipe prompts use facts from their inputs only, and every prompt that writes from a search or tool result needs a `requires`, so an empty result falls back instead of inventing people. Say so when the user asks their agent for a recipe change.

## Step 4 - Validate, then push

Validate in the builder checks the draft and lists each issue it finds. Fix every error, then validate again: Publish refuses a draft with errors.

## Step 5 - Preview on 3 accounts

The Draft step previews the stored draft on up to 3 accounts, so Save first. Pick 3 accounts that match the brief, and read each preview on desktop and mobile before you call the build done: every section renders, nothing shows an empty slot, and every link opens.

## Step 6 - Publish

Publish only when the user asks or agrees. Publish in the builder asks what to do with the live pages (pages a link went out on):

| Choice | What happens |
|---|---|
| None | Live pages stay on their version |
| All | Every live page is refilled on the new version. URLs and links stay |
| Some | Only the pages picked are refilled |

New pages use the published version, and pages with no link yet move to it. Refilling live pages runs Kenso on the slots the new version changed, at 2x model cost: say so before the user picks All or Some. Publish refuses a draft with validation errors or a flagged link; a workspace publishes 50 times a day.

## Manage templates

- **Which templates exist:** the cards at https://app.ken.so/<workspace id>/demo/studio. A card that says Draft has no published version yet.
- **Version history**, in the builder, lists the versions.
- **Copy:** Duplicate on the card.
- **Delete:** only when the user asks. Delete asks first; a template with live pages is refused, and a second ask retires them. A delete has no undo.
- **One page to the new version:** Update this page, on the page (the `studio-asset` skill). It costs like a refill, so say so first.
- **Datasets, webhook secrets and campaign pins** have no button in Studio: Edit with your agent. Never paste a webhook signing secret into a chat.
- **Campaign pins:** a campaign's sequence can carry the merge tag `asset_link`, written in double curly braces, and Kenso builds each page one step ahead from the pinned template. Pinning or unpinning changes what a live campaign sends: on a client's campaign, name the campaign and wait for that person's yes.

## Rules

- Nothing you do here sends. A page reaches a person only through a link someone puts in a touch or a sequence, and a person approves every send.
- Publish with All or Some, Update this page, deleting a template with live pages, and dataset deletes change live pages: ask first and say the cost.
- Never invent prices, customers, numbers or quotes in fallbacks, samples or prompts. Fallbacks read only Kenso variables.
- Vendor names (the scraper, the search provider, the model) never appear on a page a prospect reads.
- Prospects never read "reverse demo" or "demo": the Kenso template library bans both in its grade checks; keep that.
- A structural change to a live template (new sections, new slots, a new recipe) is a new version and a publish, never a hand edit on single pages.
- Every write a person makes in Kenso is recorded as theirs.

## Credits

Previews, validation, pushes, hosting and PDFs are free. Publishing is free. Pages cost 1 credit on their first link, and fills cost model tokens at 2x model cost when Kenso writes them: the `studio-asset` skill has the full table.

## What this skill cannot do yet

- No email template is in the Kenso template library; email templates start blank.
- `enrich.email` is not available as a recipe tool: its slot always falls back.


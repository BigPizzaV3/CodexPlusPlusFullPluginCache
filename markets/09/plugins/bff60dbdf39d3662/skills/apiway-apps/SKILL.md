---
name: apiway-apps
description: Build and update the person's Apiway websites and apps — sites, CRMs, Telegram bots, internal tools — hosted by Apiway (its own database, address, sign-in). Use when the person asks to create, change or fix an Apiway app, or says "make me a website / a CRM / a bot / an app".
---

# Apiway apps

Apiway hosts apps the person builds with you. Apiway gives each app a database, an address, sign-in for the
team, a design kit and a PREVIEW that only the owner sees. The person publishes.

## Which Apiway account you work in — and missing tools

- You see the apps of ONE Apiway account: the one signed in to apiway.ai when the connector was allowed.
  `list_code_apps` starts with "Connected to Apiway as <email>" — say that address when the person asks which
  account this is, or when an app they name is not in the list.
- An app of another account answers "signed in to Apiway as <email>, and that account has no app …". Tell
  the person exactly that and the way out: disconnect Apiway in this agent's connector settings, sign in to
  apiway.ai as the app's owner, connect again (the consent screen names the account and has "Switch
  account"), then start a new chat. An agent that can hold two Apiway connections may add the second account
  instead. Never send them to authorize some other server.
- No `get_code_app`, `report_progress` or preview-update tools in your list? Apiway sends them all; the
  agent's own settings hide them. In Claude: Settings → Connectors → apiway.ai → Tool permissions → "Always
  allow" (or "Needs approval") for ALL THREE groups — Interactive, Read-only, Write/delete — then a NEW chat:
  an open chat does not re-read the tool list.
- While you build, the person watches a checklist: pass `plan` (every step's title) with your first
  `report_progress`, then report each small step with `step`, `total`, `text` and `detail`.

**First: can you run shell commands?** In ChatGPT, claude.ai or any chat with no terminal you cannot — take
the first way. In Claude Code, Codex or Cursor you can — take the second.

## In a chat, no terminal (ChatGPT, claude.ai)

A new app — lead the person through the brief right here, they never have to open Apiway for it:
1. **The template follows from their first words.** A site, a landing page, a portfolio → `website`; a
   service with sign-up and plans → `saas`; clients, deals, records → `crm`; a bot → `telegram-bot` or
   `instagram-bot`; linking two services → `custom-integration`; anything else → `blank`. Do not ask which
   template — only when the words fit two equally.
2. **Start the app.** A `website`: `submit_app_brief` with the kit and their message as it is, links
   included — it creates the app, and Apiway's analyst returns how it understood them. Every other
   template: `create_code_app` with the name and the kit. What the first message already says is saved right away — `set_site_brief_answers` for a
   website, `submit_setup_answers` with `partial: true` for the others — so it is never asked again.
   A website's road, languages, look, requests email and photos are saved only with `person_said` — the
   person's own words. Never answer these for them: no words, no save.
   Every other template is the same: `submit_setup_answers` saves and approves only with `person_said`.
3. **The brief, step by step — never an app from one sentence**: the person who gets a random result
   leaves. Call `brief_step`: it names the next question, its options, and how to save the answer. Ask that
   ONE question in the person's language (offer the options it gives), save the answer the way the step
   says, then call `brief_step` with `done` (that step's id) and `person_said` (their own words) — until
   it says the brief is complete. The questions are the ones Apiway's own brief screens ask, in their order. Steps already answered are skipped
   by Apiway itself. For a website two steps decide the result:
   - **The look.** Show the ready styles from `list_site_styles` — the name, the picture and the demo link
     of each — next to "or send a link to a site you like; I take only its design". Never pick silently.
   - **Their own site.** A link they give is first asked about: "is this your own site?" Their own → its
     pages, texts and photos are collected and the new site is built from them. Not theirs → a reference
     for the look only.
   A key or token a template needs is never asked in the chat: `request_code_app_secret` gives a link.
   When `brief_step` says the brief is complete, say back in three to five lines what will be built.
4. On their yes: approve the brief the way `brief_step` named (`approve_app_spec` for a website,
   `submit_setup_answers` without `partial` for the others), then `preview_code_app_draft` — Apiway builds
   the preview from the brief with no code written by hand; `get_preview_update_status` with the update id
   it returned waits for the build and gives the preview link. Pass that link on.
5. Make it theirs. A WEBSITE: `list_site_slots` shows every text, picture and block of the site;
   `edit_site_slots` changes them with no code at all — the way for "change the headline", "replace the
   photo", "hide that block". Anything else (a new page, a colour, logic, a CRM's fields):
   `list_app_files` → `read_app_files` → `edit_app_files`, as "From a chat without a terminal" below says.
6. `report_progress` with `done: true`.

An app that already exists: `list_code_apps` → `get_code_app` (slug), then steps 5–6.

"Show my apps", "what is in my Apiway": `open_apiway` opens the Apiway panel right in the chat — their apps
with the live and preview addresses, the newest gallery files and the credit balance. Use it when the person
wants to SEE; use a tool when they want something done.

The steps under "Every task" that run commands (`get_app_kit`, `npm`, the upload) are the terminal way —
skip them here. A big new feature or many new files is more than a chat can carry: say so plainly, and that
Apiway has a way to connect a coding agent for it (App Factory → Connect an agent).

## With a terminal (Claude Code, Codex, Cursor)

A new app:
1. `create_code_app` with a name and a kit (call without `kit` to see them).
2. The brief, in this chat: what they already said is never asked again. Either `submit_app_brief` with
   their words (the analyst's spec comes back; `approve_app_spec` on their yes), or the template's own
   questions: `get_setup_questions` → ask only the open ones → `submit_setup_answers`.
3. `get_code_app` → run its download command in a new folder → follow that folder's AGENTS.md, BRIEF.md
   and SETUP.md.

An app that already exists: `list_code_apps` → `get_code_app` (slug) → work in its folder by its AGENTS.md.
If the folder is already there, start with `get_app_kit`.

## Every task

0. `code_app_plan` (read) — the app's living plan: what was decided, done, turned down, what is open. It is
   the app's memory between sessions and agents. The person says something raw (two phrases, a screenshot)?
   Say back in plain words how you understood it, on one example; name what already exists and what is new
   work; ask ONE question if an answer is needed — and for anything bigger than one clear edit, start only
   after their word. A wish that contradicts the plan is said aloud, not silently overwritten.
1. `get_app_kit` — if its version differs from `apiway-kit/VERSION`, run the command it returns.
2. Build it. Report each step with `report_progress` (in the person's language) — they watch it. Send the whole
   `plan` (the list of your steps) with the first call, keep the steps small, and say in `detail` what you are doing
   right now — the person sees the plan as a checklist and must be able to tell that work is really going on.
   On the first step of a change the person asked for, pass their request in `request`.
3. Update the preview: `npm run typecheck`, then `start_preview_update` → run the upload command →
   `finish_preview_update`. If it fails, read the log, fix, try again.
4. When it works, call `report_progress` with `done: true` and paste the message it returns to the
   person as it is.
   Then one line into the plan — `code_app_plan` (note: decided / done / rejected / open) — and, when you
   work in the app's folder, the same line into `PLAN.md` there. One line per fact; never rewrite the plan whole.
5. The person asks to remove the examples → `delete_example_data`.
6. The person pastes a "Fix" task or says something is broken → `get_code_app_errors` for what broke,
   `get_code_app_logs` for the log; fix it, update the preview, tell them in one sentence what it was.

## What the person may ask — and the tool for it

Everything a button does in the app's editor you can do too. Ask in the person's words, act with the tool:
(`apiway_guide` holds the full reference — the contents without a topic, one function's steps with it. Read the
matching record before something you have not done in this session.)

| The person says | Tool |
| --- | --- |
| "what is wrong with it", "what should I fix" | `code_app_advisor` (list) — then fix what is broken first |
| "that note is a false alarm" | `code_app_advisor` (hide) |
| "put it live", "publish" / "take it off the internet" | `publish_code_app` / `unpublish_code_app` |
| "put it on my domain" | `set_code_app_domain`, then `get_code_app_domain` (check). You bind and check; the DNS record at the registrar is the PERSON's step — give them the exact record and say so |
| "bring back yesterday's version" | `list_code_app_versions` → `code_app_version_action` (preview); live only after `publish_code_app_version` |
| "the build hung" | `code_app_version_action` (retry) |
| "the editor says the site is on an older version" | `code_app_version_action` (update_core) |
| edits with screenshots («Правки», the Edits Pool) | `list_code_app_edits`; your plan of a pool → `review_code_app_edits` (plan); change or delete an open edit → `update_code_app_edit` |
| "let Apiway's agent do it" | `code_app_build` (start, with the person's yes — it spends their credits); "stop it" → stop |
| "who makes the edits — you or Apiway" | `set_code_app_editor_agent` |
| "stop the recommendations" / "turn them back on" | `code_app_recommendations` (switch) — for all their apps |
| "show the leads", "how many visits" | `list_code_app_leads`, `get_code_app_analytics` |

Only the person does: paying and changing the plan, making the app public for anyone with the link, the DNS
record at their registrar. Say that plainly and give them the place in Apiway.

## When the work is done — what did not work, and what to do next

The person will not ask you for this; say it anyway. After the FIRST build, after a pool of four or more
edits, and after a skill — not after one small edit:

1. **What did not work.** One or two lines in your last message: what you could not do and why, what you
   saw broken beside the task, what in Apiway got in the way (a tool that failed, a rule that contradicts
   the task). "Everything worked" is an answer too.
2. **What to do next — only if there is something worth it.** Look at the app as an experienced
   practitioner of its kind (a web developer and marketer for a site; a product manager and an engineer
   for a CRM or a SaaS) and ask what the owner does not see: what is missing, what loses them a client.
   Send at most THREE with `code_app_recommendations` (`action: "add"`), the most important first. Most
   work ends with none — an empty answer is the right answer, not a failure.
   - Each needs: `seen` — what you saw and where (a page or a file of THIS app); `impact` — what it
     costs the owner in their own business; `change` — the concrete change you are ready to make.
   - Do not send: general practice ("add tests", "improve SEO"), taste (colours, fonts, spacing nobody
     asked about), anything the owner already hid, or code the owner will never see or feel.
   - Write them in the person's language.
   - First call `code_app_recommendations` with `action: "list"`: do not repeat what is already there,
     and when it says recommendations are not wanted, send none.
   Never start working on a recommendation yourself — the person sends it to you when they want it.

## From a chat without a terminal (ChatGPT, claude.ai)

No shell, so no download, `npm` or upload command. The same work goes through three tools:

0. A website's texts, pictures and blocks need no code: `list_site_slots` → `edit_site_slots`. Take the
   files only for what the slots do not hold.
1. `list_app_files` — what is in the app; read this AGENTS.md and the files you will change with
   `read_app_files` (up to 20 at once).
2. Change the DRAFT, do not rewrite it: texts, colours, blocks, fields, pages in the files that are
   already there. Keep each change small and copy `find` text exactly from what you just read.
3. `edit_app_files` with all edits of one change in one call — Apiway builds them into the preview.
   If the build fails, read the log it returns, fix, and send the whole corrected set again (a failed
   set is not kept). There is no `typecheck` — read your code twice before sending it.
4. Then `report_progress` with `done: true`, as above.

A big new feature or many new files is more than a chat can carry: say so plainly, and that Apiway
has a way to connect a coding agent for it (App Factory → Connect an agent).

## Only on the person's words

The tools do what they are asked; these calls are made only when the person asked for exactly that.
Most of them take `confirm: true` (`delete_code_app` takes `confirm: "DELETE"`): pass it only after
the person said yes to that exact action in this conversation. Without it the tool refuses — that is
expected, not an error to work around.

- `publish_code_app` and `publish_code_app_version` — they said to publish or roll back.
- `delete_code_app` — they asked to delete this app, by its name (the slug is never guessed).
- `code_app_backups` with `restore` — they asked to go back to that copy; everything after it is lost.
- `decide_code_app_migration` with `allow` — they saw what the migration deletes and said yes.
  Better: rewrite the migration so it only adds.
- `set_code_app_data_access` — they asked in words; otherwise the app asks with `apiway.ask()`.

Other habits: if two apps match a name in `list_code_apps`, ask which one; after `report_progress`
with `done: true`, give the person the returned message as it is.

## Keys and tokens — never in the chat

- Never ask the person to paste a key, token or password into this chat. When the app needs one, call
  `request_code_app_secret` and give the person the link it returns: "Open it and paste the key there,
  not here." You never see the value — call the tool again (or `get_code_app`) to check it is set.
- Build that link only with the tool; never tell the person to type a key on another site or into a
  form of the app. The one exception is a field the template itself ships for the owner's key and
  `SETUP.md` names (a Web App's admin: Stripe in Plans → Payments, Google sign-in in Settings) — then
  tell the person where that field is and do not request the key at all.
- If they paste one here anyway: do not repeat it, save it at once with `set_code_app_env`, and tell them
  it is saved — and that a key shown in a chat is better replaced (Telegram: `/revoke` in @BotFather).
- The code reads keys from `process.env` only. Never write a key into a file, and never print one to
  the logs, a page or an API answer — an upload with a key in its code is refused.

## The business — read the brand before you ask

- Before asking the person anything about their business (what they do, services, prices, city,
  contacts, where to find them, how they write), call `get_brand` with this app's `slug`. It holds what
  they already told Apiway and what was read from their own site, Telegram and maps — each fact with its
  source. Ask only what is in `missing` or what the task really needs beyond it.
- Facts marked `owner: true` are the person's own words: use them as they are.
- Learned something new about the business in the chat (a new service, a price, a FAQ)? Put it in with
  `propose_brand_fact` — the owner confirms it in Company Branding; do not write it into the app as a
  fact until then. In the app's code, read the brand with `apiway.brand()` instead of copying facts.

## How you write to the person

The person reads everything you send: the progress steps, the final message, your questions. Write it in their
language, in the manner of ASD-STE100 (Simplified Technical English, made for aircraft maintenance manuals), about
80% strict:

- One action per sentence. At most 20 words.
- One word for one thing. Do not vary it.
- Numbered steps for anything done in order.
- No file names and no code terms, unless the person asks.

Show, do not describe: give the preview link and three to five things to look at, each with a link to its page.
Draw a diagram only to explain a structure of three or more parts (the pages of a site, the path of a request).
Ask one question at a time, with the answers to choose from.

This is for your reports, the steps in `report_progress` and your questions. It is NOT for the app's own texts:
those are written for the app's visitors, in the brand's voice.

## Words

Talk to the person in **preview** and **publish** — words like deploy, container or localhost mean
nothing to most people. Understand all of them when THEY say them: any way of saying "put it live"
means publish.

## What Apiway gives this app

- Two copies: the **preview** (every change you make lands here, only the owner sees it) and the
  **published** app at the app's address (changes only when the person presses Publish). One database for both.
- Its own Postgres database, secrets, sign-in, logs (`get_code_app_logs`, slot `preview` or
  `published`), errors (`get_code_app_errors`), and the Apiway SDK (`apiway-kit/sdk`).

---
name: create-demopage
description: Build or deepen the user's DemoPage (a live, narrated demo of their product for website visitors) by mapping the product's pages from its code, then approving the ones buyers should see. Use when the user asks to create, build, improve, or fix their DemoPage or product demo, or to add pages from a repo to DemoPage.
---

# Create a DemoPage from the product's code

DemoPage gives a vendor's website visitors a live demo inside the real product, narrated by an AI guide. The guide can only open pages in the vendor's catalog, and it narrates from each page's description. A deep catalog makes a deep demo. Your job is to map the product from its code, send the pages as candidates, and let the user choose what goes live.

The DemoPage MCP server (`demopage`) acts for the one vendor account the user signed in with. The tools are:

| Tool | Use |
| --- | --- |
| `demopage_status` | Website, live or not, page counts, last page check, demo link, and the next step. Call it first. |
| `demopage_list_pages` | Every page with its id, whether it is approved, and its last check. |
| `demopage_import_pages` | Send mapped pages as candidates, up to 100 per call. Nothing goes live from this. |
| `demopage_approve_pages` | Approve (or hold) pages by id. Before go-live, this also turns the demo link on. |
| `demopage_check_pages` | Load every approved page in a demo browser, the way demos open them. |
| `demopage_read_site` | Read the public website again (only before go-live). |
| `demopage_get_link` | The demo link and the embed snippet for the website. |
| `demopage_results` | The last 30 days: visits, live demos, questions asked most, pages kept out, leads. |

## Ground rules

- **The code stays here.** Send only what the tool schema asks for: a title, a full https address, a short piece of visible text, a one or two sentence description, and optional keywords or click path. Never send source code, file contents, environment values, secrets, internal hostnames, customer names, or customer data.
- **Repository access is a prerequisite.** This workflow works only when the current client can actually read the user's local repository or files the user deliberately attached. The DemoPage MCP server cannot read a repository. If no filesystem or attached source is available, say that plainly and stop; do not imply that ChatGPT or DemoPage inspected code it could not access.
- **The user approves.** Importing is safe: every page arrives held. Never call `demopage_approve_pages` until the user has seen the list and said which pages to approve. "Approve all" from the user is fine; your own judgment is not.
- **Read-only screens only.** Demos never save, send, pay, or delete anything; DemoPage blocks those actions in every demo. Do not map screens whose purpose is money, keys, or account security: checkout, billing, payment methods, invoices to pay, API keys or tokens, passwords, two-factor setup, sign-up, login, logout, account deletion. DemoPage refuses these anyway.
- **Real, canonical addresses on the product's domain.** Every `url` must be https on the website domain `demopage_status` reports, or one of its subdomains (for example `app.` for the product itself). Remove every query string and fragment before sending it; they can contain tokens, emails, or other sensitive state. Never localhost, staging, preview, or internal hosts.

## Steps

### 1. Check the account

First verify that this client has a filesystem or attached source it can inspect. If it does not, explain that the MCP connection can manage DemoPage but cannot supply code access, and suggest running this skill in Cursor, Claude Code, or Codex from the repository, or attaching a bounded set of route/navigation files.

Call `demopage_status`.

- If the call asks the user to sign in, tell them their AI tool will open "Sign in with DemoPage"; they sign in with their DemoPage account and choose Allow.
- If there is no account: send the user to https://app.demopage.io/signup to start free with their work email (or https://demopage.io/early-access to talk to the team), then stop.
- If `reading` is true, DemoPage is still reading the public website. Carry on mapping; import once it finishes.
- Note the `website` domain. All addresses must be on it.

Call `demopage_list_pages` so you don't send pages the catalog already has.

### 2. Find the production address of the product

Signed-in pages need their real address, for example `https://app.example.com/reports`. Look in this order: README and docs, deployment config (Vercel, Netlify, Fly, Kubernetes ingress, Terraform), `.env.example` or config defaults (`APP_URL`, `NEXT_PUBLIC_APP_URL`, `BASE_URL`), links from the marketing site, and e2e test config (`baseURL` in `playwright.config.*` or `cypress.config.*`). If you can't find it or it is not on the website domain, ask the user.

### 3. Map the pages

Find every screen a customer can reach, from whichever of these the repo has:

- **Routes:** Next.js `app/**/page.tsx` or `pages/**`; React Router or TanStack Router config; Vue Router; SvelteKit `src/routes`; Nuxt `pages/`; Angular route modules; Remix `app/routes`; Rails `config/routes.rb` with views; Django `urls.py` with templates; Laravel `routes/web.php`; Phoenix router.
- **Navigation:** the sidebar, top nav, settings tabs, and command palette show what customers actually reach, and the labels they see.
- **UI text:** page headings, empty states, and labels in components or translation files (`en.json`, `locales/en/*.json`, `messages/en.*`).
- **End-to-end tests:** Playwright and Cypress specs are the best source of truth. `page.goto(...)` gives the address and `getByRole('heading', { name: ... })` or `cy.contains(...)` gives text that is really on the page.
- **Docs and changelog:** what each feature is for, in the product's words.

For each page, build:

- `title`: the page's name as the product shows it, for example "Invoices" or "Slack integration".
- `url`: the full production address. For dynamic segments (`/projects/[id]`), use an address from the docs or e2e fixtures only if it will exist in the demo account; otherwise map the list page instead and put the click path in `path`.
- `expect`: 3 to 120 characters of **static** text that is visible on the page when it loads, such as a heading or a fixed label. Copy it exactly from the component or English translation file. Never use data that varies by account, such as names, counts, dates, or prices.
- `say`: one or two sentences on what the page lets a customer do, from the product's copy, docs, or changelog. The guide narrates from this, so make it concrete and true: "See every open invoice, filter by status, and send reminders in one click." Do not invent features.
- `signedIn`: true for in-app pages that need an account.
- `path`: only when a page has no direct address, for example `["Settings", "Integrations"]`.
- `keywords`: words a buyer might use when asking for this page, for example `["reminders", "overdue", "dunning"]`.

Prioritize the pages that show the product's value: dashboards, the core workflow screens, reports and analytics, integrations, automation and rules, and settings that show configuration (not secrets). Leave out admin-only, internal, debug, feature-flagged or unreleased, and empty-by-default screens. 15 to 60 strong pages beat 200 thin ones.

### 4. Import

Call `demopage_import_pages` with the pages, in batches of up to 100, and a `note` saying where the map came from, for example "Next.js routes, sidebar config, and Playwright specs". Read `skipped` and fix what you can: a wrong domain, missing proof text, or a too-short description.

### 5. Ask the user, then approve

Show the added pages as a short table: title, address, signed in or not, and the visible text you'll check for. Ask which to approve. Then call `demopage_approve_pages` with exactly those ids.

- Before go-live, approving turns the demo link on. If the answer says the link is waiting, the user either confirms their email (they got a link) or DemoPage is reviewing the sign-up.
- Signed-in pages need a demo login for the product. If `demopage_status` says there is none, tell the user to add one in the portal, step 5, at https://app.demopage.io/portal. Never ask them to paste a password to you.

### 6. Check and fix

Approved pages are checked in a demo browser automatically; you can also call `demopage_check_pages`. After a few minutes, call `demopage_status`, then `demopage_list_pages` with `status: "failed"`.

For each failed page, read its note. Usually the `expect` text isn't on the page as loaded (translated, dynamic, or behind a tab), or the address redirects. Find better static text or the right address in the code, and send the page again with `demopage_import_pages` using the same `url`. That corrects it and holds it for approval again; ask the user before approving it again. Pages that keep failing stay out of demos, and that's fine.

### 7. Hand over

Call `demopage_get_link` and give the user the demo link and the one-line embed snippet, which goes before `</body>` on any page of their website. Summarize: pages approved, signed-in pages, pages that failed and why, and anything the user still has to do (confirm email, add a demo login).

## Improving an existing DemoPage

Call `demopage_results`. For the questions buyers asked most and the pages kept out, find the matching screens in the code and import them (or correct them), then ask the user to approve. Say which question each new page answers.

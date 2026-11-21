---
name: adcopilot-docs
description: Answer questions about AdCopilot itself from what the connector reports - what it can do, which Google products are connected, how many look-ups the workspace has used today and when the count resets, what AdCopilot is allowed to change in an ad account, where data goes, and what to do when something is not working. Use when the user asks what AdCopilot can do, about its limits or running out of look-ups, about privacy or safety, or when a tool call fails or a product looks missing.
---

# AdCopilot docs

Questions about AdCopilot itself, answered from what the connector at `https://mcp.adcopilot.cloud/mcp` reports - never from memory. The product changes and this file does not move with it, so every number in an answer comes from a live read or from the documentation site, and nothing comes from recall. What the user explicitly asks for comes before anything here.

Call `get_org_context` first, before any other tool, and pass no `source`. The answer carries the facts most of these questions want:

- `org.plan`, `org.ops_today_used`, `org.ops_today_cap`, `org.ops_resets_at` and `org.accounts_cap` - the workspace's own plan, today's count and when it resets, and how many Google Ads accounts can be switched on at once
- `products` - which of the customer's Google products are connected, and what each one `unlocks` if it is not
- `app_urls` - where the customer goes to manage the connected products and the accounts switched on
- `help` - where the troubleshooting steps are

A question about AdCopilot itself is answered from that one call, plus the documentation site where this file says so. Make no Google Ads, Analytics, Search Console or Tag Manager read for it, and start no other AdCopilot skill. The answer's `next_step`, `playbook` (its section on a returning customer included), `cross_reads` and `question_map` describe the account, not this question: do not follow them on this turn, not even their offer of a skill's steps. Keep from them only what `next_step` says about today's look-ups or a teammate's login, and the facts above. If the customer says yes to the read you offer, that is a new request, and the skill that answers it runs then. Leave any suggestion about a plan, a purchase or a recurring schedule out of the reply unless the user asked about it, and then report only what the answer says.

## What AdCopilot can do

Never recite a list of products or a count of tools from memory: both move, and a stale list is a promise the connector cannot keep. Answer from `products` - what is connected, and for anything that is not, what the connector itself says connecting it would unlock. A product you do not recognise is one the server knows about and you do not: describe it from what the server says. Invent nothing.

Products are connected inside AdCopilot, at the address the server's answer gives for each, not in this assistant. A fresh sign-in can report nothing connected: that is the server answering, not a fault. The `adcopilot-connect` skill walks a customer through connecting and linking them: name it, and start it only when they ask for those steps.

Answer "what can AdCopilot do" once, as one list, in this order: what is connected and what each lets them do; what connecting each of the others would unlock; what this plugin walks them through (checking an account for waste and what to change with `adcopilot-review`, the morning check with `adcopilot-daily`, the first campaign with `adcopilot-launch`, conversion tracking with `adcopilot-measure`, Search Console questions with `adcopilot-seo`); and what AdCopilot may change, with the condition on its yes (below). Say what each skill in that part reads and proposes, and leave approval to the part on what AdCopilot may change, where it is said once with its condition: no skill's line adds that nothing happens until they say yes. That is the whole answer: never a second list in another grouping, and never come back later in the same reply to answer it again. One fact from `get_org_context`'s 30-day summary (an account's `last_30d` in `ads_probe`, with the dates it names, `start_date` to `end_date`) may be the reason for the offer that ends the reply; if the answer carries none, name no figure. Anything that needs a read is that offer, not part of the answer.

If a tool seems missing, that proves nothing on its own: the app's tool list can be out of date, or a newly added tool may not be available in it yet. `get_org_context` is the only thing that says what is connected - believe it over the tool list, and say so plainly rather than telling a customer a permission is missing. One real cause is a product connected read-only, whose write tools stay unavailable until editing is enabled: say that, and pass on the message and link the server gives for enabling it.

## Look-ups, and running out

A workspace gets a number of look-ups a day (the server may call them operations; use its word). `org.ops_today_used` against `org.ops_today_cap` is the live answer - give those two numbers and `org.ops_resets_at`, not a remembered allowance. A `null` cap means no daily limit. `org.accounts_cap` is how many Google Ads accounts can be switched on at once; the accounts that are on are listed in `products`, and the customer switches them at `app_urls.accounts`.

**When a workspace runs out, lead with what the reads established.** Name it - the spend, the waste found, the change proposed - then give the server's own line about the limit, word for word, every time: the refused call's, or the one a call which worked carries, as `limit_notice` or as a `usage_notice` that says the limit is reached. It says the count and when it resets, and a link when the server adds one. Calls refused together carry it once ("Not run: same daily limit as the call refused just before it."), so say it once. Then say that nothing was lost: what was found is still true tomorrow. Do not retry the call that was refused, and never dress the limit up as an error. Where the server says the workspace is reached through a teammate's login, or that the workspace owner manages the plan, pass that on.

If the user asks why the limit applies, say that the workspace's plan sets the daily count.

This file names no plans or prices, and the reply should not either. Beyond the workspace's own plan name and count as the server reports them, and its own line at the limit, name no plan and no amount, compare nothing, recommend nothing, and give no billing, checkout, sign-up or plan-change address of your own, even one that appears in `get_org_context`'s answer. Someone who asks what AdCopilot costs is told that this assistant does not quote it, is shown the workspace's own count from the server, and is pointed to `https://adcopilot.cloud`.

## What AdCopilot is allowed to change

Worth stating plainly, because it is the question behind most hesitation. Reads run freely. For changes:

- **Nothing is deleted except a negative keyword, and the server enforces it.** AdCopilot has no tool that deletes a campaign, ad group, ad, keyword or asset, and the server refuses any change that sets a status to REMOVED - on its Analytics, Search Console and Tag Manager tools as well as Google Ads. Pausing is as far as it goes. This holds on the server whatever the assistant does, so say it first. The negative keyword is the one deliberate exception: each of the three ways to add one has a removal behind it, so a negative can be taken back out. One addition cannot be taken back through AdCopilot: attaching a shared negative-keyword list to a campaign has no detach tool, and that is done in Google Ads under Tools, Shared library, Exclusion lists. Setting a campaign's languages with `update_campaign` replaces the list it had.
- **The yes before a change is the assistant's to wait for, not the server's.** Every change is proposed first - the exact change, the account, and the money both ways - and made only after the customer says yes in this conversation. That is how the assistant is set to behave; AdCopilot's server does not itself pause for a yes. ChatGPT and Codex may add a confirmation of their own before an action that changes something, which is the app's choice and the user's settings, so never promise one and never say there is none. Never state the approval as something the server guarantees: a customer who asks "will it always ask me?" is owed the difference between what the assistant does and what the server holds. That holds wherever approval comes up, a heading, a parenthesis or a list item included: never write that a change waits for their yes without the condition beside it, that the yes is the assistant's rule and not the server's.
- **What the server holds whatever the assistant does:** the no-delete rule above; a campaign AdCopilot builds is created paused, and the server refuses to switch on the campaign it built with the customer, because that switch is the customer's, in Google Ads; Tag Manager changes are made in a workspace and never published, which the customer does; where the workspace has saved a monthly cap, a change that would take spending past it is refused; and it reads and changes only the Google Ads accounts switched on in the workspace, within what the customer's own Google sign-in can open, and never sees a Google account that was not connected.
- **No change is made while the user is away.** An unattended run only reads and proposes, because every change waits for the customer's yes in a conversation; that is the assistant's rule, like the yes above, not something the server enforces. AdCopilot's emailed daily check-in, where the workspace has one, only reads.
- If the answer says the connection is read-only, nothing can be changed from it. Say so and give the address the answer names.

## When something is not working

The steps are at `https://adcopilot.cloud/docs/troubleshooting`, and every AdCopilot documentation page has a plain-text copy (for this one, `https://adcopilot.cloud/docs/llms.mdx/docs/troubleshooting.md`). If you can open web pages, read it and give the customer the step, rather than sending them away with a link alone. If you cannot, give them the address with the error text, and do not guess at a fix.

- Fix your own call first: a wrong field name or a text over Google's length limit is yours to correct and run once more, not the customer's to fix. Retry once, never in a loop, and never retry the daily limit or an access refusal - only the customer's step changes those.
- For a product the connector reports as needing to be signed in again, say so and send them to `app_urls.accounts`. For one it flags as unreachable (connected, but this connector cannot reach it), the AdCopilot connection has to be removed and added again in their assistant - say that plainly; no amount of retrying fixes it.
- Never ask for a password, a Google sign-in code, a token or an API key. There is none to give: sign-in happens in the browser.
- If the documented step does not fix it, support is at `support@adcopilot.cloud`.

## Where the answers live

For anything about privacy, data handling, security or what AdCopilot is allowed to change, the written answer is on the docs site and the customer can be sent to it: `https://adcopilot.cloud/docs` - the concepts pages cover approval-gated writes, what can never be deleted, read versus write, account scope and where data travels - and the privacy policy is at `https://adcopilot.cloud/privacy`. Read the page and quote it rather than answering from memory. `get_org_context`'s `help` field carries the troubleshooting address for the same reason.

## What is next

Answer what they asked first, whole. Then, when the question pointed at something a read of their own account would answer - what AdCopilot can do for them, whether a product is worth connecting, why a tool seemed missing - end the reply with exactly one question, offering one read: what it would show them about their account, tied to the 30-day fact that makes it worth doing, if the answer carries one. Not a fix, not a change, and not a second offer.

Skip it after a question about look-ups and running out, about the workspace's allowance, or about privacy or safety: there the answer is the whole reply. That holds even when `next_step` suggests something else.

## What breaks

Answering a limits question from memory: the numbers drift, and a customer who is told the wrong allowance stops trusting the rest of the answer. Treating a missing tool as a missing permission: it is usually an out-of-date tool list or a read-only connection, and telling a customer they lack access they have is the worst version of this mistake. Telling a customer the server will always stop and ask before a change: it will not, and a customer who believes it has been told something untrue about their own account.

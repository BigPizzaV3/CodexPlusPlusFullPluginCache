---
name: sales-outreach
description: Plan and run B2B sales outreach with SuperSend, the user's personalized email and LinkedIn sequences to business contacts they have a reason to reach. Buy sending domains and inboxes (they arrive connected and warming up) or connect your own, write and launch a campaign with an opt-out, work through replies, and track results. Use when the user wants to do B2B sales outreach, buy or set up domains and inboxes for it, send a sales email sequence, check replies, see how a campaign is doing, or fix deliverability.
---

# B2B sales outreach with SuperSend

You work through the SuperSend tools. The user signs in to SuperSend when ChatGPT asks them to connect it.

## Rules

- **Ask before anything that contacts people or costs money:** launching a campaign, sending a reply, running a placement test (uses credits), buying domains or inboxes. Say exactly what will happen ("starts Monday 9:00 for 400 contacts, up to 180 emails a day"), then wait for a clear yes.
- **Business outreach only, done responsibly.** SuperSend is for B2B outreach to people the user has a legitimate business reason to contact.
  - Don't import bought or scraped lists, consumer or personal addresses, or anyone who has opted out. If asked, decline, explain why, and suggest a relevant business list instead.
  - Every campaign includes a clear way to opt out (SuperSend's unsubscribe link or a "reply no" line), and opt-outs, unsubscribes and the blacklist are always honored.
  - No deceptive subject lines, fake replies ("Re:" on a first email) or misleading sender names. The email says who it's from and why.
  - Keep volume within each inbox's daily limits and stop or pause when bounces are high.
  - Remind the user to follow the laws that apply to them (for example CAN-SPAM, GDPR, CASL).
- **Links:** when a tool returns a link for the user (add a card, checkout, connect an inbox, open in SuperSend), give it to them exactly as returned. They open it; you can't.
- **Never ask for passwords or API keys.** Inboxes connect through the link SuperSend returns.
- SuperSend doesn't find leads. If the user has no list, ask for a CSV of business contacts or another lead source they use.

## 1. Pick the team

Most tools need a team ID. A team is a workspace (an agency often has one per client). Call `get_setup_status`: it names the team it shows. If the user is in several teams it lists them instead: show the names and ask which one (the setup card also offers them as buttons); never pick for the user. Keep using that team until they say otherwise.

## 2. Get the account ready

Call `get_setup_status` (it shows a setup checklist). `next_steps` lists what's missing, in order, and who does each step.

- **Card / free trial:** give the user the link (7-day free trial).
- **Inboxes:** ask whether they want to **buy new inboxes through SuperSend** or **use inboxes they already have**.
  - Buy: plan 2-3 look-alike domains (for acme.com: tryacme.com, getacme.com, never the main domain) with 2-3 inboxes each, show the estimated cost, then call `get_inbox_checkout_link` and give them the checkout link. Nothing is charged until they pay there. Bought inboxes arrive connected and warming up on their own (24-48 hours).
  - Their own: give them the connect link from `get_setup_status`.
- **Warmup:** inboxes need about 14 days of warmup before full volume. Start it for any inbox that isn't warming: `update_sender` with `warm: true`.
- **Sender profile:** campaigns send from a sender profile (a group of inboxes): `create_sender_profile`, then `update_sender` with `sender_profile_id` for each inbox.

Call `get_setup_status` again after each step.

## 3. Write the campaign

Interview first: what they sell, who buys it (title, company type), the problem it solves, proof (a customer, a number), and the one thing to ask for (usually a short call).

Write 3 emails, all plain text:

- **Email 1:** 50-120 words. Personal opening (`{{first_name}}`, `{{company_name}}`, or `{{one_liner}}` when the list has it), the problem, the proof, one question as the call to action. No links or images. Short subject, 2-5 words.
- **Email 2** (wait 3 days), reply in the same thread: a new angle or a different proof.
- **Email 3** (wait 4 days), reply in the thread: short and polite close.

Show the copy and adjust it with the user before creating anything.

First call `preview_campaign`: it shows the user the draft as a card (each email with the day it goes out, the schedule, the sending inboxes, anything to fix) with a Create campaign button, and creates nothing. Then wait: the user creates it from the card, or tells you to, and only then you call `setup_outbound_campaign` (not live; leave `activate` off) with the same arguments. Pass `emails`, the emails in order, each with `subject` (first email; a follow-up without one replies in the same thread), `body` and `wait_days` (the gap after the previous email), plus `days` such as `["monday", "tuesday", "wednesday", "thursday", "friday"]`, `hours` such as `"09:00-17:00"` and `timezone`. The user sees exactly these when ChatGPT asks them to approve the call. Add contacts with `bulk_import_contacts` (each needs `email` or `linkedin_url`; extra columns go in `custom`). To A/B test, add `subject_b`/`body_b` to an email.

## 4. Review and launch

Call `get_campaign_review` (it shows the steps with their timing, who sends, contacts, schedule, daily volume and launch checks). Fix anything blocking.

Then send a test of every email step to the user's own inbox with `send_campaign_test`. It goes out from one of the campaign's inboxes with the variables filled from a real contact; nothing is sent to contacts. Ask the user to open the tests (and check spam) and fix anything they don't like.

Launch only after the user says yes: `complete_campaign` if the review says it's a draft, then `activate_campaign`. The review card's Launch button does the same after a second click. Pause with `deactivate_campaign`.

## 5. Every day

- New replies: `list_conversations` with `folder: "inbox"`, `last_message_direction: "inbound"`, `read_status: "unread"` and `channel: "email"` (or `"linkedin"`). The Inbox folder leaves out bounces and auto-replies.
- Read one with `get_conversation`. Draft an answer, show it, and send only after a yes: `send_conversation_message` (email goes from the inbox the conversation came in on).
- When a reply is handled, mark it done with `update_conversation` (`is_unread: false`, `is_archived: true`).
- Out of office or "not now": label it and mark it done; don't reply unless asked.

## 6. Results

`get_campaign_stats`: sent, replies, bounces, outcomes (interested, meetings), and each step and A/B variant. Call a winner only with 50+ sends per variant. Good benchmarks: reply rate above 2-3%, bounce rate under 2%.

## 7. Deliverability

- `get_campaign_stats` shows bounces and replies per step. If bounces are high (over 2-3%), pause the campaign with `deactivate_campaign` and tell the user to check the list's quality before resuming.
- For deeper checks (inbox health, placement tests, bounce reasons), send the user to SuperSend; the review card's "Open in SuperSend" link opens the campaign.

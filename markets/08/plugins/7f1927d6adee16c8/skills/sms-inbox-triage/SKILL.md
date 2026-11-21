---
name: sms-inbox-triage
description: >
  This skill should be used when a CallRail user asks to "check my texts",
  "which texts need a reply", "summarize SMS conversations", "triage the text inbox",
  "share incoming texts with my team", "forward texts to the team", "draft replies to texts",
  or wants text threads summarized and routed to several people, which CallRail text forwarding
  (one number only) doesn't do.
---

# SMS inbox triage

Before starting, read [ChatGPT runtime guidance](../../references/chatgpt-runtime.md).

Find the real people waiting on a text, separate them from the noise (marketing blasts, codes, texts meant for someone else, vendors, tests), route a digest to the team, and draft replies for approval.

## Which accounts this covers

The connector can reach every CallRail account the signed-in user has access to, and nothing else. That can be one agency account with many client companies, several separate client accounts the user was added to, or both. In CallRail an account holds companies, and each company is usually one client.

1. Call `get_account`. It lists every account this user can reach.
2. One account: use it. Several: show the account names and ask which to cover (one, several or all). If the user already named accounts or clients, use those and don't ask.
3. Run the workflow once per account, passing that `account_id` on every call. Never mix data from different accounts in one call or one total.
4. Report each account in its own section. Account-wide numbers and patterns are per account, and a client in one account never appears in another account's results.
5. The skill sees only what the user's role allows in each account. If a call fails with a permission error (for example forms or users for a reporting-only user), say which account and what was skipped, and keep going.
6. If a client the user names isn't in the chosen accounts, search `list_companies` in the user's other accounts before saying it doesn't exist.

## Inputs

1. Accounts: see "Which accounts this covers" above. Companies within each account: one, a list, or all.
2. Window: default `recent` (last 7 days). Use `today` for a daily run.
3. Destination for the digest: chat (default), a Slack channel, or email recipients.

## Step 1: pull conversations

- `list_conversations` with `state: inbox`, `date_range` for the window, `fields=lead_status,source`, `per_page: 40`, paginated. Add `company_id` when scoped.
- **Check every response for `_truncated`.** Long marketing texts make pages large. In testing, a 100-per-page request returned 39 of 78 conversations with `total_pages: 1`, so half the inbox would have been skipped silently. If `_truncated` is present, re-request with `per_page` set to the `showing` count and page through. Check the total collected against `total_records`.
- The `state` filter may return conversations marked "active". Don't rely on it to mean "unread"; the classification below decides what needs a reply.
- If nothing comes back, retry without `state`, then try `list_sms_threads` for the window. If both are empty, check `list_trackers` for `sms_enabled` so the user knows whether texting is even on.
- `recent_messages` can include texts from months ago. Only the newest messages matter; use `get_conversation` when more history is needed to understand the latest one.

## Step 2: sort every conversation

Read the latest message (and the one before it when needed) and put the conversation in **one** group. This is a judgment call on what the message says, not a keyword match. Work top to bottom and stop at the first group that fits.

| Group | How to spot it | What to do |
|---|---|---|
| **Done** | Latest message is from the business | Count only |
| **Opted out** | The customer's own latest text asks the business to stop texting: STOP, UNSUBSCRIBE, QUIT, CANCEL or END, or plain words such as "stop texting me" or "remove my number". "Reply STOP to opt out" inside someone else's marketing text is **not** an opt-out | Never draft a reply. List them. Automatic opt-out catches only the keywords, so mark plain-language opt-outs "block by hand" |
| **Do not contact** | Abuse or threats with no request or complaint in them | Never draft a reply. List them |
| **Complaint** | An unhappy customer with a real complaint (late technician, billing dispute, a repair that didn't hold), even when the text is rude | No draft. List under "Complaints for a manager" |
| **Login codes** | One-time codes, verification codes, "don't share this code" | Count only. Several of these on one number point to a recycled number |
| **Meant for someone else** | Personal messages (birthdays, family), reminders or orders addressed to a named person who isn't the business, "please forward to..." | Count only. Flag the tracking number as **likely recycled** (it belonged to someone else before) |
| **Marketing and notifications** | Texts from other businesses: promotions, newsletters, surveys, review requests, order or delivery updates, links with a brand name, "Reply STOP to opt out" | Count only |
| **Vendors pitching the business** | Lead sellers, recruiters, agencies, software sales, "do you still own your company" | Count only, unless the agency asks to see them |
| **Test messages** | "Test", "test message", agency staff testing | Count only |
| **Asked for a text** | "Please text me", "text is best", "I can't talk, text me" | **Reply first.** These are real leads, often from a missed-call text |
| **Real question or request** | A person asking something or answering the business ("Did my order ship?", "What's your zip?", "Hey", "?") | **Reply** |
| **Call back** | Automatic phone replies: "Sorry, I can't talk right now", "Can I call you later?", "I'll call you back" | Usually means the business called and the person declined. Put on a callback list, no text draft needed |
| **Photo or empty** | Latest inbound message has no text, or only an image | A person needs to look. List them |

When unsure between a real person and noise, put it under "Real question or request" and say why it's uncertain.

Read the whole latest burst, not just the last line. Sales texts often open with a casual question ("did your policy arrive in the mail or no?") followed by a pitch in the next message sent the same second; that's marketing, not a customer.

## Step 3: details for the reply groups

For "Asked for a text", "Real question or request" and "Call back":
- **Waiting since:** time of the customer's latest inbound message (not the conversation's first message).
- **Company, customer name** (skip caller ID labels like "SPRINGFIELD IL"; use "unknown" instead), **source**.
- **One-line summary:** what they want.

## Output

1. **Headline:** "X people waiting on a text, Y asked for a callback. Z others need no reply." Lead with any urgent text, then the longest wait.
2. **Urgent:** texts from the reply groups about an emergency (water leak, no heat or power, someone stuck, injury), whatever their age. Same columns as Reply today.
3. **Reply today:** Asked for a text, then Real question or request, oldest first: waiting, company, customer, summary, source, draft reply.
4. **Call back list:** company, customer, when they replied.
5. **Complaints for a manager:** company, number, when, one-line summary of the complaint.
6. **Needs a look:** photo or empty messages.
7. **Likely recycled numbers:** tracking numbers getting codes or texts meant for someone else, with counts.
8. **Opted out:** list them, with plain-language opt-outs marked "block by hand".
9. **Not shown (counts only):** marketing, codes, meant for someone else, vendors, tests, do not contact, done.

## Draft replies

- Under 300 characters, friendly, in the business's voice.
- **Never guess facts.** If the answer needs something the thread doesn't say (a zip code, a price, a policy status, an opening), use a placeholder like `[business zip]` and flag it for the person sending.
- No promises on price or timing the thread doesn't support.
- Drafts only for "Asked for a text" and "Real question or request".

## Routing

- Slack: create a **draft** message in the chosen channel with the digest. Posting gives the whole team visibility, which covers the "forward texts to more than one number" request. Send only on explicit approval.
- Email: create drafts only.
- **Health details:** on every account (not only HIPAA), if a text mentions health details (appointments with a doctor, medication, diagnosis, insurance for care), keep the content in the chat and send only "health-related message" to Slack or email. On HIPAA accounts, send only counts and first names.

## Sending replies

- `send_text_message` cannot be undone. Never send in dry run.
- To send, show the exact recipient, from-number and text, and wait for a yes for that specific message. One approval covers one message.
- Never text anyone who opted out, is marked do not contact, or is on the complaints list (a manager handles those).
- Fill every placeholder before sending.

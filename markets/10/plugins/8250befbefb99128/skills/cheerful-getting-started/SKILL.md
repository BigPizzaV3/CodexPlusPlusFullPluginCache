---
name: cheerful-getting-started
description: "Get started with Cheerful: say everything Cheerful can do in this chat, confirm which Cheerful account is connected, check its mailboxes and integrations, list its campaigns and show the credits left, then suggest what to do next. Read-only. Use when the user says \"what can you do\", \"what can Cheerful do\", \"help\", \"get started with Cheerful\", \"set up Cheerful\", \"is Cheerful connected\", \"which Cheerful account is this\", \"show me my Cheerful account\", or has just installed the Cheerful plugin."
---

# Get started with Cheerful

Two parts, in this order: **what Cheerful can do here** (the full list, so nothing is missed),
then **one quick pass over the user's account** (who is connected, what they can send from,
connections, campaigns, credits). It only reads; it changes nothing and spends no credits.

## Step 0: Check the connection

Every step below calls a Cheerful tool. If a Cheerful tool is unavailable, or a call answers
"Tool not found" or asks to reconnect, stop and tell the user: "Connect Cheerful from the plugin
page, then ask me again." Don't retry the call and don't guess the account's contents.

## Read this first: what the data can and can't tell you

- **Lead with what it can do, not what it can't.** "What can you do?" is answered with the
  capability list below, written for the tools you actually have. The things done in the
  Cheerful app get one short line at the end, never the opening.
- **Two tool sets exist.** If `create_campaign_draft` and `preview_campaign_launch` are listed, Cheerful can set
  up a campaign and the user sends it from the launch card. If they are not listed, campaigns
  are set up and sent in the Cheerful app; say that once and keep everything else.
- **Read is not send.** A mailbox the user can read is not necessarily one they may send from.
  `account_read` separates the two; report them separately.
- **Teammates' work shows up too.** Campaigns carrying `owner_email` or `team_id` belong to a
  teammate. Say whose they are.
- **Credits, never dollars.** If `computed_at` is empty in `billing_usage`, say "not counted yet
  this cycle" rather than zero.
- **A section that fails is a gap, not a stop.** If one call errors, write "couldn't check this
  right now" for that section and carry on with the rest.

## What Cheerful can do here

Write this list every time the user asks what Cheerful can do, or has just connected. Keep every
group; one line per item, each with a short example the user can paste.

**Find creators** (Instagram, TikTok, YouTube; searches use credits)
- Search from a brief: niche, country, follower range, engagement. "Find 20 US skincare creators
  on TikTok with 10k-100k followers"
- Creators like one you already love. "Find creators like @handle"
- YouTube deep search: vets each channel's videos in the background (10-45 minutes) and saves
  the results to a list.
- Vet one creator against a brief: audience, engagement, recent posts, red flags. "Is @handle a
  good fit for our vegan snack?"
- Save creators to a list and read your saved lists. "Save these to my Spring list"

**Run campaigns** (only when `create_campaign_draft` is listed)
- Set up a campaign from a brief: the first email, a follow-up, the product, the send window.
  Nothing is sent. "Set up a gifting campaign for our new protein bar"
- Add creators to it from a search, a saved list or names and emails you paste.
- Check your sending inbox and your domain's email setup, and get the link to connect Gmail.
  "Which inbox will this send from?"
- Preview the launch: the real first email, who gets it, when and how fast. It goes out only when
  you click **Confirm & send** on the card. "Show me the launch preview"

Without `create_campaign_draft`: one line instead, "Setting up and sending campaigns happens in the
Cheerful app (https://app.cheerful.ai); everything below works here."

**Track results** (reading costs no credits)
- Campaigns: status, who sends them, sent, replies, opt-ins. "Which campaign has the lowest
  reply rate?"
- One-call campaign summary: performance, replies waiting on you, opt-ins, top posts. "Give me a
  summary of my latest campaign"
- Replies: who answered, who opted in, who still needs an answer, with reply text drafted for you
  to send from Cheerful. "Who replied to my campaigns?"
- Posted content: which creators posted, and the top posts. "Show me the posts from Spring
  Seeding"

**Your account**
- Credits left and renewal date; mailboxes; connected tools (Shopify, Google Sheets, Instantly and
  others) and whether any needs attention.

**Done in the Cheerful app** (one line): editing, pausing or deleting a live campaign, replying
to creators, and buying sending domains.

## Workflow

1. **Account.** Call `get_profile`. Note the email and team name (the `nickname` reads
   "email · team").
2. **Access.** Call `account_read`. Count the mailboxes the user can send from and the ones they
   can only read, and list their teams.
3. **Connections.** Call `integration_status`. List what is connected and healthy, and flag any
   connection that reports an error. Connecting or fixing one happens in Cheerful, not here.
4. **Campaigns.** Call `campaign_read` with `action="index"` and `include_stats=true`. Count the
   campaigns by status. Pick up to 3 to show: campaigns with sends first (most replies, then most
   sent), then the most recently updated. Show each with sent, replies and opt-ins. Don't fill
   the 3 with drafts that have sent nothing when campaigns with results exist.
5. **Credits.** Call `billing_usage`. Report `remaining` of `plan_included_credits` and the renewal
   date (`cycle_end`).
6. **Next steps.** Suggest exactly 3 things to try, chosen from what you found:
   - `create_campaign_draft` listed → always include "Set up a campaign from a brief";
   - no campaigns yet → "Find creators for a brief";
   - campaigns with replies → "See who replied and who needs an answer";
   - several campaigns → "Which campaign is behind?" or "Summary of <campaign name>";
   - a creator in mind → "Vet @handle against my brief".

## Output layout

```
Here's what I can do with Cheerful in this chat:

**Find creators** (Instagram, TikTok, YouTube; searches use credits)
- Search from a brief: "Find 20 US skincare creators on TikTok with 10k-100k followers"
- ... (every item from "What Cheerful can do here")

**Run campaigns**
- ...

**Track results**
- ...

Done in the Cheerful app: editing, pausing or deleting a live campaign, replying to creators,
buying sending domains.

---

**Connected as** ava@brand.com · Brand Team
**Mailboxes:** 2 you can send from, 1 you can read only
**Connections:** Shopify, Google Sheets connected · Instantly needs attention
**Campaigns:** 3 (1 active, 2 paused)
- Spring Skincare Seeding — 40 sent, 12 replies, 5 opted in
- Vegan Snacks Launch — 20 sent, 3 replies
**Credits:** 2,470 of 2,500 left, renews Oct 31

**Try next**
1. "Set up a gifting campaign for our new protein bar"
2. "Who replied to my campaigns?"
3. "Give me a summary of Spring Skincare Seeding"
```

Keep it to this shape. If the user only asked "which account is connected" or "is Cheerful
connected", skip the capability list and give the account part only. No mailbox → say "No mailbox
connected yet — connect one to send campaigns." No campaigns → say so in one line and lead with
the find-creators suggestion.

## Rules

- Plain language. Don't show ids, field names, status codes or the word "tool" to the user.
- Never say Cheerful will send an email by itself. When the campaign tools are available,
  outreach goes out only when the user clicks Confirm & send on the launch card; otherwise
  sending and launching happen in Cheerful at https://app.cheerful.ai. Editing or pausing a live
  campaign happens in Cheerful either way.
- Report credits as credits. Don't mention prices or promote plans.
- Don't invent mailboxes, integrations or campaigns that weren't in the results.

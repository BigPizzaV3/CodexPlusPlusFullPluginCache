---
name: il-messages
description: "This skill should be used only when an InvestorLists founder asks for a message or says yes to the one offer made after Path to Connect: \"write to\", \"draft\", \"my pitch message\", \"cold email\", \"LinkedIn message\", \"intro request\", \"one-liner\", \"elevator pitch\", \"LinkedIn headline\", \"they replied, what do I say\", \"follow up with\", or onboarding option 3. Two modes: the founder's general message set, and messages for one specific investor and path. Writes under the InvestorLists method (references/writing-rules.md); sends email only on a yes per message; LinkedIn text in a copy box; never opens LinkedIn.\n"
metadata:
  version: "0.1.1"
  author: InvestorLists.vc
---

# Investor Messages

Every message written for this founder, this investor, this path. Drafts first; email sent only on a yes per message; LinkedIn text handed over. Read `references/writing-rules.md` before writing anything.

## When this skill runs

Only when the founder asks, or says yes to the single offer Path to Connect makes per firm. The agent never starts writing on its own. A declined offer is not repeated for that firm; two declines in a row end the offers for the session.

## Inputs

`raise-profile`, `message-set` (if it exists), `connectors`, `preferences`; for mode 2 the firm's record, notes, brief hooks and chosen path. If the profile lacks the deck link for investors, the booking link or the signature, ask once (max 3 questions) and save to `raise-profile`.

## Mode 1: the general message set (onboarding option 3, or on request)

Write, one at a time, each shown and edited before the next:
1. Pitch message (the core; everything else derives from it).
2. Cold email + follow-up 1 (+2 days, same thread) + follow-up 2 (+5 days, new thread).
3. LinkedIn first message + follow-up 1 (+4 days) + follow-up 2 (+14 days).
4. Email after a LinkedIn connection.
5. Intro request to a connector (forwardable) + reply to a warm intro.
6. One-line pitch (what, for whom, the strongest proof point) and elevator pitch (30 seconds: why now, why you, traction, the ask).
7. LinkedIn headline and About line, on request.
Save all as `workspace_note {name: "message-set"}` and to `InvestorLists/Messages/message set <date>.md` when the folder exists. The founder can ask for any single item.

## Mode 2: messages for one investor (chained from Path to Connect, or "write to <firm>")

1. If no `message-set` exists, write the pitch message first (one item, shown, saved), then continue.
2. Confirm in one line: "Cold email to Jane Doe, partner at X Ventures. Hook: their Fund III close (Sep 2026). Go?"
3. Draft by path:
   - Intro path: the intro request to that connector with the firm-specific reason, forwardable as is.
   - Direct email: the cold email to that decision-maker with the firm-specific hook, deck link, one ask, booking link, signature. Follow-ups 1 and 2 drafted with their dates.
   - LinkedIn: connection request (blank) noted; first message and follow-ups in a copy box with their dates. 3rd degree: InMail text.
   - Submission form: the text per field, in a copy box.
4. Review pass before showing: nothing the record or brief does not support; one hook; no invented familiarity; not the same hook twice to the same person; the connector not asked twice in a week.
5. Delivery:
   - Email, mailbox connected: show the message; "send?"; on yes send from the founder's mailbox. On no, save as a draft in the mailbox. Before the first send of the day, once: "I send up to 15 emails a day from your mailbox; beyond that your own domain's reputation is at risk, so I stop there." At the cap, state it and stop.
   - Email, no mailbox: the text in a copy box.
   - LinkedIn and forms: always a copy box. The founder sends.
6. Save the drafts to `InvestorLists/Messages/<firm> <date>.md` when the folder exists. `add_note` `[IL] messages | <date> | status=touch1-drafted or touch1-sent | next=touch 2 | due=<date> | path=<path> | touch 3 due <date>`. Count sends in `send-log` (`YYYY-MM-DD email N`). Hand sends by the founder are not counted; say so once.
7. Close: "Next firm?" (back to Path to Connect for the next firm in the batch) or "Next 5?" (Shortlist).

## Replies (when the founder pastes one, or Pipeline surfaces one on request)

Apply the reply rules in `references/writing-rules.md`: positive interest, call request, email shared, not now (revisit date saved), no (ask for a referral), acknowledgement only (continue the sequence), after the first meeting. Draft the reply; send only on a yes. Update the firm note (replied, meeting-booked, not-now with date, passed).

## Volume, on request only

Export the current batch or pool as a campaign CSV for the founder's own sending tool (Instantly, Lemlist, Smartlead): email, first name, last name, firm, hook, touch 1, touch 2, touch 3, send dates. Firms with no verified email are listed separately. The agent never creates or activates a campaign.

## Rules

- Nothing is sent without a yes for that message. 15 emails a day. LinkedIn is never opened.
- One hook per message, sourced. Blank beats a guess.
- The pitch message is rewritten only when the founder asks or the raise profile changes.

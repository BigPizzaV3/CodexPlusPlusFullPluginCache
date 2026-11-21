---
name: il-path-to-connect
description: "This skill should be used when an InvestorLists founder asks how to reach one investor from their shortlist, who can introduce them, or what the best channel is: \"how do I reach\", \"who can introduce me to\", \"way in\", \"best way to connect with\", \"my connectors\", \"super connectors\", or after onboarding option 2. One firm at a time: warm paths (connectors, founder friends, portfolio founders, mailbox threads on a yes, LinkedIn links the founder clicks) and direct paths (verified emails, LinkedIn with activity signal, firm contact, submission form last). Never opens LinkedIn. Ends with one offer to write the messages.\n"
metadata:
  version: "0.1.1"
  author: InvestorLists.vc
---

# Path to Connect

The warm or direct path to one firm. Warm intro first when one exists; direct contact otherwise.

A founder who chose cold outreach to the whole list skips this skill; Messages works straight from the record.

## Connectors (collected once, updated anytime)

When the `connectors` note is empty, or when onboarding routed here with option 2, ask once, in this form: "It could be useful to have a list of your super connectors: existing investors, advisors, founder friends and others who can make introductions for you. Give me the names (LinkedIn URLs help), or I can go through your email for people who made introductions for you in the past, or skip for now." The email scan runs only on an explicit yes, on the founder's side, looking for threads whose subject or first line is an intro pattern (intro, introduction, connecting you, meet). Declined: not offered again in this raise. Save name, LinkedIn URL, how they help, their company, in `workspace_note {name: "connectors"}`.

## Inputs

One firm (the agent takes the current batch in order unless the founder names one), `raise-profile`, `connectors`, the firm's notes and brief. Decision-makers and their LinkedIn URLs from `get_investor`.

## Steps, for this firm

1. Warm paths, in this order, each a named person with a real link:
   - Connectors: for each name in `connectors`, check the firm's website (portfolio, team, advisors) and the public web for a link to the firm or its partners: their company in the portfolio, a board seat, a shared fund, a shared panel. A hit is the top row: "Ask Dana; her company is in their portfolio (firm site)."
   - Mailbox and calendar, only if connected and only on a yes for this session: any thread or meeting with the firm's domain or a decision-maker's name. Shown as "you emailed X in March 2026."
   - Portfolio founders: founders of the firm's portfolio companies in the founder's space, from the firm's site and Google, each with a LinkedIn profile link so the founder can check his own degree of connection.
   - LinkedIn links, handed over: per decision-maker, the profile URL (the founder clicks "mutual connections" himself); per firm, a people-search link for the firm name limited to 1st and 2nd degree. The agent never opens them.
2. Direct paths from the record and a quick check:
   - Per decision-maker: verified work email, personal LinkedIn URL, position. Shown as "email + LinkedIn", "LinkedIn only" or "none".
   - LinkedIn activity: one Google search per decision-maker for recent public posts. Shown as "very active on LinkedIn, posts weekly on seed fintech (last post Oct 12)" or "no recent public posts". An active partner moves LinkedIn up as the channel and gives a hook.
   - Firm-level: contact email, phone, company LinkedIn page, website.
   - Submission form: checked on the firm's website ("pitch us", "submit your deck"). Always the last option, shown with its link.
3. The map, one table for this firm, one row per decision-maker: warm path (connector, portfolio founder, mailbox thread, or none), email, LinkedIn with the activity note, best channel, suggested order of touches. Nothing collapsed, nothing invented. "No warm path found" is written as such.
4. Founder picks the paths he will use (checkbox form where the client supports one, numbered list otherwise).
5. Recommendation, three lines: first move; backup; sequence ("intro via Dana; if no reply in 7 days, email to the partner; LinkedIn message as third touch; the form last").
6. Save the map to `InvestorLists/Paths/<firm> <date>.md` when the folder exists. `add_note` `[IL] path | <date> | status=path-chosen | next=message | due= | path=<first move> | backup: <path>; connector: <name or blank>; linkedin-active: <yes/no>`.
7. One offer: "Would you like me to build you the messages to connect with this investor?" On yes, hand the firm, the chosen path, the connector and the hooks to il-messages mode 2. On no, save and continue: "Next firm: <X>. Go?" Declined once: not offered again for this firm. Declined twice in a row: not offered again this session.

## Rules

- One firm per run; the batch is the queue.
- A warm path needs a named person and a real link (portfolio, board, thread, met, mutual). "You might know someone" is never written.
- Mailbox consent once per session, never repeated if declined.
- The same connector is not proposed for a second ask within a week (check the notes).
- The agent never opens LinkedIn; it gives links, the founder clicks them.

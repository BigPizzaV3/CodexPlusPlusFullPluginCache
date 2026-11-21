---
name: il-brief
description: "This skill should be used when an InvestorLists founder wants a deep dive on one investor or up to five from their shortlist: \"research <firm>\", \"prep me for my call with\", \"deep dive on\", \"what's <firm> up to\", \"who is the partner at\". Record baseline plus a live web layer, portfolio and conflict check, hooks for the first message, and a meeting prep page when a meeting is named. No outreach advice here; that is Path to Connect.\n"
metadata:
  version: "0.1.1"
  author: InvestorLists.vc
---

# Investor Brief

Everything the founder should know before writing to a firm or walking into a meeting. One to five firms per run.

## Inputs

A firm from the shortlist (or a name), `raise-profile`, the firm's notes, optional meeting context ("call Thursday", "they asked about our pricing"). `preferences` for detail level.

## Steps, per firm

1. Baseline: `get_investor`. What they back, stage, domains, HQ, investor type, team size, year founded, AUM and its source, latest news (date, headline, link), the decision-makers with positions and what contact exists.
2. Live layer with the founder's own web search, up to 10 searches per firm, every finding dated with its URL: recent investments and leads; fund news; partner moves; podcasts, interviews, talks; posts and profile snippets through Google results only (never open LinkedIn); the firm's portfolio page.
3. Portfolio check from the firm's own site: companies in the founder's space (hooks) and direct competitors (conflict flag). Family offices and some firms publish nothing: write "no portfolio published".
4. Changes since the record: new partner, new fund, new focus, new site. Listed as "newer than the record" so the founder knows what to trust in the room.
5. Hooks: two or three lines the first message can use, each tied to a source. The source stays out of the message later; it stays in the brief.
6. Save: `add_note` `[IL] brief | <date> | status=researched | next=path | due= | path= | <three key points; conflict flag if any>`. Save the page to `InvestorLists/Briefs/<firm> <date>.md` when the folder exists.

## Output, one page per firm

- Snapshot: three lines, record evidence quoted.
- What they back, from the record.
- Recent activity: dated lines with URLs.
- People: who is there, their recent public voice.
- Portfolio: in the founder's space; conflicts.
- Changes since the record.
- Hooks for the first message.
- Meeting prep, only when a meeting is named: six questions they are likely to ask given their portfolio and stage; three things to avoid; what they said publicly that can be referenced, with source.

For several firms: a summary table first (firm, headline change, best hook, conflict), then the pages.

## Rules

- Max 5 firms per run. Max 10 searches per firm.
- Every line dated and sourced or not written. "Nothing new found since <record date>" is a valid result.
- No fit score, no route, no draft messages here.
- Close with one offer: "Find the way in to <firm>?" Hand the firm, its brief and hooks to il-path-to-connect on a yes.

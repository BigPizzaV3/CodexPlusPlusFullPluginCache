---
name: il-shortlist
description: "This skill should be used when an InvestorLists founder wants investors for their round: \"find investors for\", \"who should I pitch\", \"shortlist\", \"next 5\", \"rebuild the pool\", \"more like <firm>\", or when onboarding ends with option 1. Builds a live pool of relevant firms from the whole InvestorLists database, then works through it in batches of five with a sourced reason for each firm. Database only.\n"
metadata:
  version: "0.1.4"
  author: InvestorLists.vc
---

# Investor Shortlist

A pool of relevant investors from the InvestorLists database, then the top five to aim for first, then the next five.

## Opening line, first run

"Let me first build a pool of relevant investors from our database that could be a fit, and then we'll start narrowing it. Then I'll offer you the top five you should aim for first, and how to connect with them."

## Inputs

`raise-profile` (get_workspace_note); the founder's lists (`my_lists`); firm notes (`my_notes`). Gap questions, only for what the profile does not answer, max 3 in one turn:
- Round size and timing.
- Preferred investor types (VC, corporate VC, family office, syndicate, accelerator, any).
- Geography (home market first, or anywhere).
- Anyone to leave out, investors already talked to or connected with: "Type the names, or I can check your email for investors you've already been in touch with, or skip." The email check runs only on an explicit yes, once; if declined it is not offered again in this raise.

## Part 1: the pool (whole database)

1. Three passes with `find_investors`, each returning the signals it matched: strict (stage + domain + geography + type); relaxed (drop the weakest filter); adjacent (thesis similarity on the company one-liner and sector, across every description and latest-news item in the database). Stop at 150 candidates. Remove exclusions and firms already in any list of this founder.
2. Score 1 to 5 from the record only. Signals, each leaving a text trace: stage match; domain match; same city or region as the founder; description or latest news naming a company like the founder's (same product category or customer); recent news that signals capacity to invest now (new fund closed or raised, new partner at the founder's stage, a recent lead or seed check in the space); investor type fit; contact available (verified email, LinkedIn). Same score: most recent news first.
3. Show the pool as a compact table: firm, type, stage, domains, HQ, latest news date, fit. Stats line: size, with verified email, LinkedIn only, with news in the last 6 months. Data stamp once per session.
4. One iteration: "Remove any? Widen or narrow?" Re-run once or twice, then stop asking.
5. Save: the pool table to `InvestorLists/Shortlists/Pool <date>.md` when the folder exists; `save_to_list {list_name: "Pool", firm_ids}`; `add_note` per firm: `[IL] shortlist | <date> | status=pool | next=batch | due= | path= | fit <score>: <signals>`.

## Part 2: top five, batch by batch

6. Refresh before every batch: re-run the saved filters; add new firms (new import, new rows); re-score firms whose latest news is newer than the last run. News moves priority both ways: a new fund, a lead in the founder's space or a new partner at the founder's stage moves a firm up; a wind-down, an acquisition, a shift to later stage or "not currently investing" moves it down or out, with the headline as the reason. Say what changed in one line: "Since last time: 4 new firms in the pool, 2 moved up on news, 1 dropped."
7. Pick the five highest-fit firms not yet worked (skip anything with a status beyond pool). Open them with `get_investor`. For each, a quick check of the firm's own website for portfolio companies in the founder's space (this check only for the five).
8. Write the "why them" per firm, each line sourced: city, what they back at this stage (record), the news item with its date and link, a portfolio company in the founder's space (firm site), the decision-maker to approach and what contact exists. A firm with only basic matches gets one plain line, never a padded story. News that cuts the other way is shown too.
9. Founder reacts: swap any out; confirm. Confirmed five: `save_to_list {list_name: "Batch <N>"}`; note `status=shortlisted-b<N>`; the batch page with the "why" to `InvestorLists/Shortlists/Batch <N> <date>.md`.
10. Close with one offer: "Research these five, find the way in to the first one, or write the first messages?" Nothing runs until the founder picks or asks.
11. "Next 5" anytime: steps 6 to 10 again. "Rebuild the pool": Part 1 again, keeping the statuses of firms already worked.

## Free accounts

Part 1 runs in full. Part 2 shows the 10 firms that fit best (call `find_investors` again with the ids already shown in `filters.excludeIds` until 10 are in hand) with the sourced "why". A firm with `locked: true` is a preview: name, type, region, sectors, stages and what is on file as counts; the details stay locked and are never guessed. `unlock_firm` opens one firm in full (every decision-maker with name, position, verified work email and LinkedIn); 10 firm unlocks for the life of the account, ask first and say how many are left. No exports, no save_to_list or add_note on free; no second batch. At the end, once: "That isn't available on your current plan. Plan details: investorlists.vc/ai#plans".

## Rules

- Database only. No firm from outside the database.
- No score and no "why" line without a source in the record, the news item or the firm's own site.
- Max 150 candidates per pool run; max 2 iteration rounds unless asked.
- The pool is refreshed on every batch and rebuilt on request; batches always come from the current pool.
- Export on request only: `export_list` (Excel or CSV), one line.

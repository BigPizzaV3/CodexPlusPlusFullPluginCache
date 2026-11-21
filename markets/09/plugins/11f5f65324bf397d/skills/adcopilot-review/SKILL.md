---
name: adcopilot-review
description: Read a Google Ads account connected through AdCopilot and say what happened, what it cost, what is wasting money and what to change, then propose the change and apply it only when the customer says yes. Use when the user asks how their Google Ads are doing, or for a status, check, update, report, weekly summary or audit of the account; asks about spend, clicks, impressions, results, cost per result or budget; asks which keywords or search terms are wasting money, which negative keywords to add, what is working, or what to pause or fix; or asks what to do next about their ads. Reads the account instead of answering performance questions from memory.
---

# AdCopilot review

The customer asked how their Google Ads are doing. Answer the whole question in
one pass, through the AdCopilot connector at `https://mcp.adcopilot.cloud/mcp`.
A thin answer is the failure here. Reading the account is the easy part; a
customer who has to ask four follow-up questions to learn what one answer could
have told them has been short-changed.

## Start

Call `get_org_context` first, before any other tool, and pass no `source`, on
this call or any later one. Then follow the answer's `next_step`, `playbook` and
`cross_reads`: they carry the reads this answer starts with and its rules.
Everything below runs inside them. `next_step` describes the account, not this
request: do what the customer asked, pass on what it says about today's
operations, and offer what it suggests afterwards unless this request already
covered it.

Account ids come from that answer. If more than one Google Ads account is
switched on and the customer did not say which, ask which. Never read an
account the answer does not list.

If Google Ads is not connected, no account is switched on, or the account
cannot be read, say exactly that, in the server's words, and stop. The
`adcopilot-connect` skill walks the customer through connecting. A report built
on guesses is worse than no report.

These rules hold throughout, whether or not the answer repeats them: reads run
freely; every change is proposed first and applied only after the customer's
explicit yes in this conversation; campaigns, ad groups, ads and keywords are
paused, never removed (never set a status of REMOVED); a campaign AdCopilot
built is created paused, and the customer switches it on in Google Ads
themselves, never you. Dates go in as YYYY-MM-DD.

On an account with campaigns to read, which is when the answer's situation is
`ADS_DORMANT`, `ADS_ACTIVE_UNTRACKED` or `ADS_ACTIVE_TRACKED`, the answer also
carries `question_map`: for each kind of question, the read that answers it
(wasted spend, search terms and negatives, keywords, ads, budget, results
changed, tracking, what to do). Use it to choose the first read for a question
that is narrower than the whole account. It is absent when there is nothing to
read, so when it is missing the list below stands in for it.

## Make the reads the answer needs

`cross_reads.ads_reads_max` is how many Google Ads reads the server says this
answer starts with: make them all, then every read `cross_reads` names. It is
where the answer starts, not where it stops, except on a day the server itself
calls short, when `cross_reads.reads_left_today` is present: then the playbook's
section for few operations left today, or the hint that says how many look-ups
are kept for the change, says where this answer stops, and you follow it. The
account's own numbers are what make the answer true, and a number you did not
read is a number you must not state. Never trim the read list to be economical:
if a read would have changed what you say, make it.

If the server refuses a read at the daily limit, say which reads ran and which
did not, answer only from the ones that ran, and do not retry in a loop. Then
give the server's own line about the limit, word for word, every time: it says
the count and when it resets, and a link when the server adds one. Calls
refused together carry it once ("Not run: same daily limit as the call refused
just before it."), so say it once. A call that worked can carry the same line,
as `limit_notice` or as a `usage_notice` that says the limit is reached; pass
that on the same way. A read refused because it counts more than what is left
today names the lighter reads that still fit: make those, then give its line.

What you cannot read, say you cannot read. Never estimate a figure, and never
carry one over from an earlier turn as if it were fresh.

## Follow `related_reads`

When a lens or `search` result ends with `related_reads`, run the ones that bear
on the question, at most three, then answer from all you hold. Each names its
tool, its arguments and a `why` built from the numbers of the result you just
read; skip one that does not bear on what the customer asked. Never repeat a
read you hold. Offer, do not chase, the `related_reads` those reads bring back.
They are reads only: a change is still only proposed, and waits for the
customer's yes. A related read past those three is offered as the next read in
one statement, never a second question and never as a limit you hit ("The next
read would show how each campaign bids; say the word and I will run it.").
Never offer a read for what a result you hold already shows. A read you skipped
because it does not bear on the question is neither offered nor mentioned, and
the figure in its `why` stays out of the answer.

## A tool that is missing

A tool that is missing from your list, refuses a parameter it should take, or
carries a revision different from the `tools_revision` the server reports is
stale, not a permission the customer lacks. Call `get_org_context` with `tools`
set to the names you need and go by what it returns; that works even when the
schema you hold shows no `tools` parameter. If the tool is still missing, run
the reads you do have and report what they found for the dates their answers
cover, say plainly that the tool list this session holds is out of date and
which read you could not run, and say you will run it once the list is
refreshed. Point the customer to `https://adcopilot.cloud/docs/troubleshooting`
for how to refresh the connection. That is a step for them, not a change to the
account, so it is not put as a proposal and carries no cost lines. A missing
tool halves an answer; it does not cancel it. Name no revision value to the
customer.

## The sequence

**Open with `full_audit`, with `depth="deep"` and `days` set to the window you
are reporting.** Pass `depth="deep"` explicitly. A call that names no depth also
runs deep today, but if that run can't finish it falls back to a quick audit
(the result says so); an explicit `deep` never does. A quick audit scores three
of the seventy-three checks over the month to date, which is not an audit and
not what the customer asked for. Deep attempts all seventy-three over your
window and says which it could not evaluate. Give coverage as the count the
result gives, "N of 73 checks gave a result", never as a percentage next to the
count, and give reasons for the rest only in the result's own words. An
unevaluated check is not a pass, and a reason you supply yourself is a guess.

One lens is ONE read and covers what many hand-written queries would. It orders
its findings by severity, NOT by money, so re-sort by cost before you choose the
three you report. For the cost ranking itself, `analyze_waste` is the read;
`analyze_search_terms` names the searches that cost money and converted
nothing, costliest first, and groups them into negative-keyword themes.
Together they usually answer step 3 below, so read it yourself only for what
they did not cover.

A question narrower than the whole account starts with the lens that answers it
rather than with `full_audit`: `analyze_waste` for money spent on nothing,
`analyze_search_terms` for negatives, `keyword_opportunities` for keywords worth
adding or fixing, `quality_score_breakdown` for ad rank and Quality Score,
`rsa_asset_report` for the ad copy, `bidding_audit` for how campaigns bid,
`day_of_week` for which days and hours earn, `budget_pacing` for budgets,
`change_history` for what changed and who changed it, and
`conversion_setup_audit` for what is counted. Do not write a `search` for what
one of these already returns: the lens reads the account the way Google counts
it, and a hand-written query reads one slice of it.

Then, in this order, each one the lenses you ran did not already answer:

1. **The period against the one before it.** Campaign metrics by day for the
   fourteen days ending on the account's yesterday (`search` over `campaign`,
   with `segments.date`), folded into two weeks so every headline number has a
   comparison. No lens returns a time series, so this read is yours to make.
   End your own `search` reads on the `date_range.end` that `full_audit` and
   the other lenses carry, and say the dates once. AdCopilot ends those
   windows on the account's yesterday, the last full day in the account's own
   time zone (UTC's, when it could not read the zone), so the audit and your
   reads cover the same days. `budget_pacing` and `change_history` are the
   exceptions: they run through the account's today, so give their dates on
   their own and never end a `search` read on them. When a finding names a
   shorter window, say its dates. If your own reads show a result after that
   window, say so in the same sentence. A window a finding gives only as a
   length ends on the result's `date_range.end` unless it says otherwise.
2. **Where the money went inside that.** Which campaigns and which keywords
   carried the spend, and which carried the results (`keyword_view`), unless
   `full_audit` already ranked it.
3. **What was paid for that should not have been.** The search terms with cost
   and no conversions, worst first, which is often the largest finding.
   `analyze_search_terms` is one read for six query shapes and all six
   negative-keyword themes: use it, never `search_term_view` written by hand.
   Before you give a count of searches, look for their names in every result
   you hold: `analyze_search_terms`' "Costliest search terms with no
   conversion" (the costliest first, with their clicks and cost, and how many
   there are) and the wasted-spend check's evidence in `full_audit` or
   `analyze_waste` (G16, each search with its clicks and cost). When one lists
   them, name the top ones with their cost in this answer. When that list says
   no conversion was recorded anywhere in the account, they cost the most and
   are not proven waste: say so, and propose blocking one that fits no theme
   only once tracking is checked. When what you hold only counts them (G16
   lists none on an account that counted no result in its window), say how many
   there are and what they cost, and that the reads count them without naming
   them. Offer a read for searches no result you hold names only when a
   `related_reads` entry's `why` says that read shows them; one that only names
   the area, such as wasted spend, is not that promise.
4. **Whether delivery is being held back.** `budget_pacing` is one read for the
   month-to-date projection against each daily budget. A campaign at its cap
   every day is turning away traffic the customer is willing to pay for, and
   they cannot see it from the dashboard.
5. **Whether results are being counted at all.** `conversion_setup_audit` is one
   read for what is counted and what is aimed at. An account counting nothing
   makes every other number meaningless, so say that first if it is true.
6. **Whether anything is switched off by Google, and what changed.** Disapproved
   ads are a `search` on `ad_group_ad` (no lens returns them). When spend,
   results or cost per result moved against the period before, `change_history`
   says what was changed in the account, when, by which Google login and through
   which channel; when nothing moved, leave it. It keeps thirty days and omits
   Google Ads Editor changes and some rows, so a quiet log does not prove
   nothing changed; say that when the numbers moved and the log shows no cause.

Read the account, never the profile's memory of it. A saved note is context for
your wording, never a substitute for a read. The decisions `get_org_context`
carries say what was approved on a date, not what is set now: a budget, a split
or a setting you did not read this turn is not yours to state, and a thirty-day
share of impressions lost to budget describes the budgets of those thirty days,
not today's. Say the window, or read the latest day.

## The answer

**One headline line.** Spent, clicks, results, cost per result, each against the
period before, in the account's own currency.

The lenses return amounts already formatted for the account (`*_display`); use
those words as they come. A raw `search` does not: it returns
`metrics.cost_micros`, which is millionths. So take the period comparison from
`full_audit`'s own figures where it covers the window, and where you must read
it raw, divide by 1,000,000 once, say the currency, and never print a micros
number as money.

**Then at most three findings, biggest money first.** Each one carries the
counts behind it: what it cost, over what period, how many clicks or searches.
A finding without a number is an opinion.

A finding that says "if X" is not a step until you have checked X. Either make
the read it names and say what you found, or carry the condition into your own
sentence. Never turn it into an instruction.

On a new account, keep what is only newness out of the findings. A new account
scores badly for reasons that are only its age: keywords with no impressions
yet, a Quality Score showing 0 because Google has not rated the keyword yet, a
bidding strategy still learning. Say in one line which items those are, and do
not count them as problems.

**Then one recommendation**, with the money spelled out both ways (what it costs
to act and what it costs to do nothing) as a proposal they say yes or no to.
Never apply it first.

For two to three weeks after anything went live, such as a campaign switched on
or a change to how it bids or what it counts, recommend no bidding change:
Google's bidding is still learning, and a change starts it over. The one
exception is a campaign getting no traffic, where Maximize Clicks with a
per-click cap is the fix.

Say what each finding means in plain words the first time it appears. "Search
terms" are the things people actually typed; "negative keywords" are the words
you tell Google never to match. Teach on the step being taken, and say what the
step unlocked, or will unlock once they have done it.

## When the ask is a full audit, a weekly summary or negatives

The customer's own words pick the shape. These are the same reads as above,
shaped for the ask. Nothing in them changes the account.

### A full audit, a deep review or a health check

The answer is a written report that has to stand alone, and it runs longer than
the three-finding answer above. Run `full_audit` as described, then
`budget_pacing`, then whatever of the sequence the audit did not cover. If the
audit ends with `related_reads` because a section failed, follow them as above.
`account_health_score` returns the score alone and is not a substitute for the
audit.

Cover, in this order:

1. **Whether results are counted at all.** If nothing is counted, say so first;
   every other number is unanchored without it.
2. **The period against the one before.** Spend, clicks, impressions, results
   and cost per result, in the account's currency. Say the window in the
   report's first line, and use the same number of days for the audit and the
   comparison, dated as in step 1 of the sequence above, so the two cover the
   same days.
3. **Where the money went.** Campaigns, then ad groups, then keywords: which
   carried the spend and which carried the results. Name the ones doing neither.
4. **What was paid for and should not have been.** Search terms with cost and no
   conversions, worst first, grouped: a competitor's brand, the wrong product,
   the wrong language, plainly off-topic. Name the top ones with their cost, and
   keep to step 3 of the sequence above on where their names are found, on "not
   proven waste" and on a result that only counts them.
5. **Whether delivery is held back.** Budgets at their cap every day, and
   anything Google has disapproved or switched off.
6. **Structure worth saying out loud.** One keyword or one campaign taking
   nearly all the spend while the rest get none is a finding, not a detail.
7. **What changed, and who changed it.** The last thirty days, by which Google
   login and through which channel, so a budget or a bid that moved is
   attributed and not listed as unknown. A quiet log does not prove nothing
   changed; say so when the numbers moved and the log shows no cause.

Write the report in this shape. Open with the account (by the name Google Ads
shows, not its number), the period, and one line on whether it is healthy. Then
the findings, biggest money first: what it is, what it cost over what period,
the counts behind it, and what you would do. No finding without a number. Then
the proposals, ordered by money saved, each with what it costs to act and what
it costs to do nothing. Mark any proposal that cannot be undone through
AdCopilot. A negative keyword is not one: each of the three ways to add one has
a removal behind it, under the same yes. The one-way action is attaching a
shared negative-keyword list, because there is no matching detach tool; a list
is detached in Google Ads under Tools, Shared library, Exclusion lists. If
nothing in the report is one-way, say so. Then one line the reader needs:
nothing above has been applied, and any of these changes happens only after the
customer says yes in this conversation. A proposal with its cost and an undo
beside it reads as a change already made unless that line stands next to it.
Close with what you could not check and why, so nobody mistakes a gap for a
clean bill of health. Write plainly: no tool names, no field names, no account
numbers in the prose.

### A weekly summary

The week runs Monday to Sunday in the account's time zone, which
`get_org_context` gives, and the summary sets last week against the week before.
Four reads, in this order:

1. **The two weeks.** `search` on `campaign` with `start_date` and `end_date`
   spanning both weeks, `segments.date` and the cost, clicks and conversions
   metrics: each week's spend, conversions and cost per conversion, per campaign
   and in total.
2. **What changed.** `change_history` with `days` reaching back to last Monday
   (at most thirty; keep only last week's changes): who changed what, when and
   through which channel. It omits Google Ads Editor changes and some rows, so a
   quiet log does not prove nothing changed; say that when the numbers moved and
   the log shows no cause.
3. **What Google switched off.** `search` on `ad_group_ad` with
   `ad_group_ad.policy_summary.approval_status`, and on `campaign` with
   `campaign.status` for the campaigns that are no longer on: any ad disapproved
   or limited, with Google's stated reason, and any campaign stopped. The change
   log does not hold a disapproval, so read 2 cannot stand in for this one.
4. **This month.** `budget_pacing`: whether the month is on track.

Say the two weeks' dates once, in the first line. A result that covers other
dates, such as this month's pacing, is given with its own. When a finding names
a shorter window, say its dates. If your own reads show a result after that
window, say so in the same sentence.

Then the summary, in this order, in plain words someone could forward without
editing:

- **The week.** Spend, conversions and cost per conversion, each against the
  week before, money in the account's currency, rounded.
- **The three biggest changes.** The largest moves in the numbers (a campaign
  whose spend or conversions moved most), the changes someone made and who made
  them, and anything Google switched off itself. Say which is which.
- **Three things to do this week.** Each one concrete, each tied to a number
  above, the most valuable first.

No account numbers and no field names. A week with no spend says so in one line,
and says what that means. Change nothing: all three are proposals, and the one
question, if any, is which to start with.

### Negatives

When the ask is about searches that cost money and brought nothing, or about
negative keywords, read `analyze_search_terms` with `days: 7` for the last week
(or the window the customer named). It groups the searches that took clicks and
converted nothing into themes (people looking for jobs, for something free, for
information, for a competitor, searches in another language, and the words this
workspace already said it never wants to show for) and names a ready call for
each theme. It also lists the costliest of them, any theme or none, with no
ready call ("Costliest search terms with no conversion"): name the top ones, and
leave one that fits no theme to the customer, as it can be what they sell. When
it says nothing was recorded anywhere in the account, say they cost the most and
are not proven waste. Seven days can hold too few searches to show a pattern;
if the tool finds nothing, say so and offer the last 30 days instead.

Report each theme in plain words: the searches, what they cost in the account's
currency, and the never-show-for words that would block them, each with its
match type said out loud (Phrase or Exact; the tool never proposes Broad, and
neither do you). Google's name for them is negative keywords (under Keywords,
then Negative search keywords, at the time of writing). Say where each would go:
the campaign that paid for the searches, or the account's own list for words the
business never wants anywhere, which every search campaign then inherits. A
competitor's name is the customer's call, not yours. The one question is which
themes to block, and nothing is added until they answer.

On a yes, `add_negative_keywords` puts them on a campaign and
`add_account_negatives` on the account's list. Then read them back with `search`
on `campaign_criterion` (the campaign's negative keywords) or on
`shared_criterion` (the account's list, by the shared set the add call
returned), and say what is now blocked, in the words Google shows.

## When they say yes

A yes counts when it is given here, to the change as you stated it, on today's
numbers. A fix agreed in an earlier conversation is read again and proposed
again before anything is applied; nothing carries over.

Apply it. Then read back only what its own result does not show (a status,
negatives once Google has normalised them, locations by the name Google shows)
and call nothing live until a read says so. Say exactly what changed and how to
undo it, and record it with `save_org_context` as a decision: what was approved,
in the customer's own framing, and which campaign it touched. A fix they did not
say yes to is recorded, if at all, as proposed and not applied; never as
approved. Record nothing about the business that the customer has not said
themselves.

Then propose the next finding's fix the same way: the change, its money both
ways, a yes or a no. One at a time, biggest money first. When nothing left is
worth its money, say so and stop proposing.

Negatives go on with `add_negative_keywords` at PHRASE match using the search as
typed, unless a broader word is plainly safe. Read them back before claiming
they are live. A negative can be taken back out through AdCopilot (there is a
removal behind each of the three ways to add one, under the same yes), so it is
reversible, and you may say so.

Campaigns and keywords are paused, never removed. A campaign you built is never
switched on by you. Pause a campaign, or switch one on, only with
`set_campaign_status`, never with a status in `update_campaign`, which is for a
campaign's settings.

## What breaks

Answering from the summary `get_org_context` returns alone: it carries a
thirty-day total and nothing about which search terms wasted money, so the
answer sounds informed and helps with nothing. Reporting a number without its
comparison: "₹8,700 last week" means nothing until it sits next to the week
before. Proposing negatives without reading the terms they block: a phrase
negative is a blunt instrument and a careless one blocks searches the customer
wants.

Calling anything a limit that no call returned. Say daily limit, quota or
"today's look-ups" only when the server refused a call because the day's
allowance was used up, or its own answer says the day is short. A read you did
not make is an offer for the next turn, never a limit you hit, and it needs no
reason.

## What is next

Before any yes, offer, in this order: the first fix as a change you will make
now; and the never-show-for words you found. After a yes, the next offer is the
next fix, as above. If the answer shows tracking is broken, the
`adcopilot-measure` skill is where that gets fixed; if the customer wants new
campaigns, `adcopilot-launch` is. Offer the one that fits, after the fix in
front of them.

AdCopilot can also email a daily check-in and a Monday summary. If
`get_org_context`'s `next_step` asks you to offer them, make that offer once in
the conversation, at the close and before any question the reply ends on, in
the server's words and with only the address the server names. The offer is its
own paragraph, with a blank line before and after it, never on the end of a
finding's sentences and never inside a bullet. Do not make it when the server
reports one is already on (`routine.daily.status` is `in_app` and
`routine.runner` is not `paused`), or when the reply ends on something the
customer must fix first. A no ends it for this conversation. Say nothing of
your own about scheduling beyond what the server's answer says.

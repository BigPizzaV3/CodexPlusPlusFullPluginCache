# Scoring rules

## Levels and labels

Every finding gets one of these levels. The JSON uses the short code. Reports always show the label and the symbol together, so the status never relies on color alone (about 1 in 12 men can't tell red from green).

| Code | Label shown in reports | Symbol | Meaning |
|---|---|---|---|
| `action` | Needs action now | ✕ | Something is broken or costing the client leads today |
| `watch` | Keep an eye on | ! | Trending the wrong way, or a setup gap that will cause problems |
| `info` | (not shown as a finding) | | Context only. Feeds "What's working" or "What we checked" |

A company's status is its worst `action`/`watch` finding. None = **Healthy** (✓).

## Every finding needs 4 parts

- `issue`: what we found, with the real numbers.
- `impact`: why it matters, in the client's terms (missed callers, leads not credited, money spent on unused numbers). One sentence.
- `fix`: the specific next step. Add the help link where one is listed.
- `owner`: who fixes it: `Agency`, `Client`, or `Agency + client`.

The wording below is a starting point. Fill in real numbers and adjust it to fit the case.

## Volume guards

Small clients swing hard in percentage terms. 4 calls to 2 is "down 50%" but it's noise. Every rate or trend check below has a minimum volume. Below it, skip the check and mark it "Not enough calls to score" in the checklist.

## The checks

Each check has a checklist name (bold, used in "What we checked"), the data it needs, the rule, and the finding text.

### Setup

**Tracking numbers active.** Data: trackers. `action` if the company has 0 active trackers.
- Issue: "No active tracking numbers." Impact: "No calls are being tracked for this client." Fix: "Create a tracking number or reactivate one in Numbers & Tracking." Owner: Agency.

**Website number swapping turned on (DNI).** Data: company `dni_active`, website trackers. `action` if 1+ website tracker and `dni_active` is false or null (CallRail treats null as off).
- Issue: "Website tracking numbers are set up, but number swapping (DNI) is off." Impact: "Website visitors see the regular business number, so website calls aren't credited to the ad or channel that sent them." Fix: "Install the CallRail JavaScript snippet on the site and confirm DNI is on. Help: https://support.callrail.com/hc/en-us/articles/5711709638541-Installing-the-JavaScript-snippet" Owner: Agency (Agency + client if the client controls the site).

**Forwarding numbers valid.** Data: each tracker's `destination_number`. `action` if a destination is a placeholder (7 identical trailing digits like 888-8888, a 555-01xx number, all zeros) or is itself one of the account's tracking numbers (calls loop through CallRail twice).
- Issue: "'{tracker name}' forwards to {number}, which {looks like a placeholder / is another tracking number}." Impact: "Callers on this number may never reach the business." Fix: "Call the tracking number to confirm where it rings, then update the forwarding number in the call flow." Owner: Agency.

**No duplicate tracking for the same source.** Data: active source trackers. `watch` if 2+ website source trackers (not `offline`) in the company have the same `source.type` and the same source settings (for `landing_params`, the same parameter and value). Offline numbers are meant to be one per placement (a billboard, a mailer), so several offline numbers is normal.
- Issue: "{n} tracking numbers are all set to track {source}." Impact: "Only one of them can show for a visitor, so the others sit unused and reports split the credit." Fix: "Keep one number per source and disable the extras." Owner: Agency.

**No test or leftover numbers.** Data: tracker names. `watch` if an active tracker's name matches test-style names (`test`, `asdf`, `delete`, `old`, `temp`, `do not use`, `xxx`, case-insensitive, whole word or obvious variants like "testtt").
- Issue: "{n} test or leftover tracking numbers are still active: {names}." Impact: "They're billed every month and clutter the client's reports." Fix: "Disable the ones no longer in use." Owner: Agency.

**Call recording on.** Data: `get_account` `inbound_recording_enabled`; tracker `call_flow.recording_enabled`. `watch` if recording is off for every active tracker in the company (or off at the account level).
- Issue: "Call recording is off." Impact: "Without recordings, CallRail can't transcribe calls or score leads, so you can't show the client which calls were real opportunities." Fix: "Turn on recording in the call flow (check local consent rules first)." Owner: Agency + client.

**Voicemail or backup when no one answers.** Data: tracker `call_flow`. Only check `advanced` call flows (basic flows ring the business's own line, which usually has its own voicemail). `watch` if an advanced flow has no `voicemail` step and the company's missed rate is 10%+.
- Issue: "'{tracker name}' has no voicemail or backup step." Impact: "When no one answers, callers on this number can't leave a message." Fix: "Add a voicemail step or a second ring group at the end of the call flow." Owner: Agency.

Form tracking and lead scoring settings aren't per-company findings or checklist items. They're judged across the whole account (see "Account-wide patterns" below).

### Call volume (skip for New companies and companies with 0 trackers)

**Calls coming in.**
- `action` "Went dark": 0 calls now, 5+ in the prior period. Issue: "0 calls in the last 30 days, down from {prior}." Impact: "This client's phone has stopped ringing from tracked marketing." Fix: "Call each tracking number to confirm it rings through. If it works, check whether campaigns were paused or numbers were pulled from the site and ads." Owner: Agency.
- `action` "Dormant": 0 calls now and 0 to 4 in the prior period. Issue: "{total} calls in the last 60 days across {n} active tracking numbers." Impact: "Either tracking is broken or the client isn't getting value from it." Fix: "Call a tracking number to confirm it rings through, then check with the client whether they're still active. If not, disable the company to stop paying for numbers." Owner: Agency + client.
- `watch` "Very low": 1 to 2 calls now, 10+ in the prior period. Same wording as Went dark.
- `action` "Stopped recently": 0 calls in the last 7 days, while the rest of the current period averaged 1+ call a day. Issue: "No calls in the last 7 days, after {n} calls earlier in the period." Impact: "This looks like an outage, not a trend." Fix: "Call each tracking number to confirm it rings through, then check for paused campaigns or removed numbers." Owner: Agency. When this fires, skip the "Call volume trend" check for the company (the 30-day trend dilutes a recent outage).

**Call volume trend.** Prior period 10+ calls. Skip if a "Calls coming in" finding fired.
- `action` down 50%+. `watch` down 25 to 49%. Issue: "Calls down {pct}% ({prior} to {current})." Impact: "{prior − current} fewer calls than the month before." Fix: "Check for paused campaigns, budget changes, or numbers removed from ads or the site, then compare by source to see which channel dropped." Owner: Agency.
- `info` up 50%+ (feeds "What's working").

**Each channel still getting calls.** Data: per-tracker call counts, current and prior (SKILL.md step 5). Skip trackers created in the last 30 days.
- "Channel went to zero": a tracker with 0 calls now while the company overall still got calls, and the company had 20+ calls in the prior period (below that, one number's swings are noise). `action` if it had 10+ calls in the prior period, `watch` if it had 5 to 9. Issue: "'{tracker name}' went from {prior} calls to 0." Impact: "The number was likely removed from an ad, listing, or page, so that channel's calls aren't being tracked." Fix: "Check that the number is still on {source}." Owner: Agency.
- `watch` "Unused numbers": source trackers with 0 calls in both periods. Group them into one finding. Issue: "{n} tracking numbers got no calls in 60 days: {names}." Impact: "They're billed every month without producing data." Fix: "Confirm they're still placed where they should be. If not needed, disable them." Owner: Agency. Skip session pools here; some idle pool numbers are normal.

**New callers.** Prior period 20+ calls.
- `watch` if first-time callers fell 40%+ or the first-time share dropped 15+ points. Issue: "New callers down from {prior_ftc} to {current_ftc} ({prior_share}% to {current_share}% of calls)." Impact: "Fewer new customers are finding the client, even if repeat callers keep total volume up." Fix: "Look at which sources brought new callers last month and check those campaigns." Owner: Agency.

### Call handling (current period 10+ calls)

**Calls answered.** Missed rate = missed / total.
- `action` 50%+ missed. `watch` 30 to 49%. Below 30 calls in the current period, flag only when the missed rate also rose 15+ points from the prior period. Issue: "{pct}% of calls missed ({missed} of {total})." Impact: "{missed} callers didn't reach anyone. These are leads the client already paid to get." Fix: "Review business hours and the call flow, and add voicemail or a backup ring group." Owner: Agency + client.

**Voicemail rate.** Data: account-wide `get_calls_summary` with `answer_status: voicemail`, `group_by: company_id`.
- `watch` 25%+ of calls went to voicemail. Issue: "{pct}% of calls went to voicemail ({vm} of {total})." Impact: "Many callers hang up instead of leaving a message, and call a competitor." Fix: "Check staffing at peak hours and how long calls ring before voicemail." Owner: Client.

**Leads being marked.** 50+ calls, lead scoring on.
- `watch` 0 leads, unless the "Lead marking not in use" account-wide pattern fired (then skip it for every company). Issue: "{total} calls, 0 marked as leads." Impact: "The client can't see which calls turned into real opportunities, which makes it hard to show what marketing is producing." Fix: "Check the lead scoring setup, or confirm someone is qualifying calls in CallRail." Owner: Agency + client.

**Short or spam calls.** Data: account-wide `get_calls_summary` with `max_duration: 10`, `group_by: company_id`. Current period 20+ calls.
- `watch` 30%+ of calls under 10 seconds. Issue: "{pct}% of calls lasted under 10 seconds ({short} of {total})." Impact: "Likely spam or misdials. They inflate call counts and can make results look better than they are." Fix: "Review these calls and mark spam so reports stay accurate." Owner: Agency.

### Forms (form tracking on, not New, count not "Unclear")

**Forms coming in.**
- `watch` 0 forms now, 1+ in the prior period. Issue: "0 form submissions, down from {prior}." Impact: "Web form leads may be going uncaptured." Fix: "Submit a test form. If it doesn't appear in CallRail, the snippet may be missing on form pages." Owner: Agency.
- `info` 0 in both periods (the client likely doesn't use forms).

### Website

See `website-check.md`. Red results there are `action`, Yellow are `watch`. Add `impact` and `owner`:
- Snippet missing / not loading. Impact: "Website calls aren't credited to any channel." Owner: Agency + client if the client controls the site.
- Another company's snippet. Impact: "This client's website calls are being credited to a different client." Owner: Agency.
- Swap target not on page / no phone number on page. Impact: "Number swapping has nothing to replace, so website calls aren't credited." Owner: Agency.
- Number didn't swap. Impact: "Visitors see the business number instead of a tracking number." Owner: Agency.

## Account-wide patterns

Some results describe how the agency uses CallRail, not a problem with one client. If the same gap shows up for most clients, flagging it on every company buries the real per-client problems and makes the client reports look worse than they are. Raise it once, at the top of the agency's overview, as an opportunity.

Judge these after scoring every company. A pattern fires when it's true for **60% or more** of the companies it applies to, and at least 3 companies. In named-companies mode, judge from the account-wide numbers you already pulled in step 4 when you can, and otherwise from the named companies (say "all 6 checked clients" rather than "your account").

| Pattern | Applies to | Fires when | What it replaces |
|---|---|---|---|
| Lead marking not in use | Companies with 50+ calls | 0 leads marked, or account-wide leads are under 1% of calls | The per-company "Leads being marked" finding |
| Form tracking not in use | Companies with website tracking numbers | `form_capture` off | Nothing (form tracking off is never a per-company finding) |
| Lead scoring turned off | All active companies | `lead_scoring_enabled` off | Nothing |
| Call recording off | Companies with active tracking numbers | Recording off on every tracker, or account-level recording off | The per-company "Call recording on" finding |

When a pattern fires, write one entry for `account_patterns`:

- `title`: plain, like "You're not marking leads in CallRail".
- `detail`: the evidence with numbers: "14 leads across 98,000 calls this month. 4 of 6 checked clients had 50+ calls and 0 leads."
- `opportunity`: why it's worth doing, for the agency and its clients: "Marked leads show clients which calls turned into real opportunities, which is the clearest proof your marketing is working."
- `next_step`: one concrete first step: "Turn on automatic lead qualification, or pick 1 client to pilot it with this month."

Starting wording for the 4 patterns:

- **Lead marking:** Title "You're not marking leads in CallRail." Opportunity: marked leads let you show clients which calls became real opportunities, not just call counts. Next step: turn on automatic lead qualification, or have someone mark leads weekly for your top clients.
- **Form tracking:** Title "Form tracking is off for most clients." Opportunity: the same snippet already on these sites can capture web form leads next to calls, so clients see every lead in one place. Next step: turn on form tracking for 1 client with an active contact form and compare a month of results.
- **Lead scoring:** Title "Lead scoring is off for most clients." Opportunity: CallRail can score calls automatically, so you don't have to mark them by hand. Next step: turn it on for your highest-volume client first.
- **Call recording:** Title "Call recording is off for most clients." Opportunity: recordings power transcripts, automatic lead scoring, and call coaching for clients. Next step: confirm consent rules in your clients' states, then turn on recording for 1 client.

For companies covered by a pattern, mark the matching checklist item `not_applicable` with the note "Not in use", and set the matching snapshot value to `null` (for example Leads), so the client report doesn't show a 0 that only reflects how the agency uses CallRail. Never mention the pattern or other clients in a client report.

A widespread *problem* (like most clients missing 30%+ of calls, or DNI off everywhere) still gets flagged on each company, because each client needs to fix it. Add one line about it at the top too ("8 of 12 clients miss more than 30% of calls") so the agency sees the scale.

## Order within a company

1. `action` before `watch`
2. Setup and Website before Call volume, Call handling, Forms (setup problems often explain the drops)

## Order of companies

`action` companies first, then `watch`, then Healthy. Within each, bigger clients (more prior-period calls) first.

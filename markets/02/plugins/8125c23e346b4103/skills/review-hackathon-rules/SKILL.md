---
name: review-hackathon-rules
description: Strategic preflight for the hackathon — present the official picture (rules, eligibility, key dates, prizes, judging criteria, submission obligations), capture explicit acknowledgment of the terms, then offer a short conversation about the participant's idea and strategy. Use when the user is starting the hackathon, wants to size up the event or sanity-check their idea, or needs to re-check official requirements.
---

# Review

## Purpose

Act as the strategic preflight and the mandatory rules gate: surface the event's official picture at a glance, walk the rules, update state only after an explicit `yes`, then offer a short conversation about the participant's idea and strategy before they start building.

Chat is the primary participant interface. Keep responses text-first so they render in any Codex host; the bundled `devpost` MCP server supplies rich inline visuals on hosts that support them.

## Required Data Source

Official rules and requirements come from the `devpost` MCP server — follow **Devpost MCP Server** in `references/plugin-runtime.md` (call only what you need, never verify or set up the server, degrade in one line on failure).

Draw on these only as needed: `devpost.get_hackathon_rules`, `devpost.get_submission_requirements`, `devpost.get_judging_criteria`, `devpost.get_key_dates`, `devpost.get_prizes`. Quote rules, eligibility, and requirements text from the response; do not paraphrase legal language.

**The acknowledgment gate runs only against real rules.** If `get_hackathon_rules` is unavailable this session, do NOT present rules for agreement and do NOT ask for or record `rules_acknowledged` — a "yes" to placeholder text is not consent to the real rules. Say in one line that the official rules can't be fetched right now, point to the hackathon's rules page on Devpost, and stop the gate there. `references/placeholder-rules.md` may shape structure and answer general questions, clearly labeled provisional — never the consent gate.

## Required References

Read these before responding:

- `references/plugin-runtime.md`
- `references/content/steps/rules.md`
- `references/config/hackathon.json`
- `references/placeholder-rules.md`

## Preconditions

Read `.devpost-hackathon-state.json`.

If the state file does not exist, direct the user to `$start-hackathon`.

Legacy state: older state files may use `review` (instead of `review-hackathon-rules`) in `current_stage`, `completed_stages`, or `next_command` — treat it as this stage.

## Strict Gate

Do not unlock the rest of the plugin flow until the user explicitly agrees to the rules review.

Use this standard:

- If `rules_acknowledged` is `true`, keep the recap short and move to **Strategy Conversation** (or point to `$resources` if they just want to proceed).
- If `rules_acknowledged` is `false`, present the rules inline through the composer and ask exactly: `Do you agree to these terms? Reply yes or no.`

Accept only `yes` as affirmative confirmation.

Treat `no` as a stop:

- do not update the state file
- keep the flow locked
- invite the participant to ask questions or return later

Do not accept ambiguous acknowledgments such as `confirm`, `acknowledge`, `continue`, or `reviewed`.

If the participant asks substantive questions, answer from the official MCP data or the placeholder reference and clearly label provisional areas as awaiting official copy. But never run the acknowledgment gate itself against placeholder content — see **Required Data Source**.

## Required Rules Content

The inline rules response should cover:

- fairness and equal-information notice
- official eligibility rules
- official contest dates and deadlines
- what to build
- what to submit
- provisional judging criteria awaiting official approval
- originality, third-party usage, testing, and content restrictions
- common reasons a submission can get blocked later
- official contact and escalation path
- the website-prevails disclaimer, verbatim from `references/content/steps/rules.md` ("A note on
  accuracy"): this guide is a helper, and if it ever disagrees with the Devpost website, the
  website prevails

Keep the response complete enough for the gate, but do not write a second ad hoc version outside the configured content and references.

## Strategy Conversation

Once the gate is passed (this turn or previously), offer — do not force — a short strategic exchange:

- surface the at-a-glance picture: deadline, prize structure, judging criteria weights, submission obligations
- if the participant shares an idea, react to it against the judging criteria and requirements in a few sentences: where it scores well, what it risks, what the minimum submission needs
- keep it to a conversation, not a report; two or three sharp observations beat a full analysis
- close with the Resources preview below

## Resources Preview

Whenever this command points the participant to `$resources` — after the gate passes, or closing the strategy conversation — never leave it at a bare next-command line. Preview the stage in three or four sentences covering, in this order:

1. The Resources step shows the links and info the hackathon organizers published to help you put your best foot forward and make the best project.
2. It also offers the optional guided build tool — **always say it is optional** — which walks you through ideation, scoping, planning, and building, and introduces best practices for coding AI projects: good if you're new to them, or want to polish your practices.
3. One token-strategy line: plan and specify with your most powerful model, then hand execution to cheaper models or subagents once the work is specified.

The guided build tool comes first in this preview, before any mention of submission prep — building precedes preparing, and `$prepare-submission` must never read as the immediate next step here.

## Presentation Output

Compose the response in-context per `references/plugin-runtime.md` ("Composing the Response"): read `references/content/steps/rules.md`, strip maintainer `<!-- -->` comments, interpolate the event name, then present a short stage headline, the page content, and the next-step callout. Do not run any script.

## State Update

When the user explicitly replies `yes`:

- set `rules_acknowledged` to `true`
- add `review` to `completed_stages` if needed
- set `current_stage` to `resources`
- set `next_command` to `resources`
- preserve any real deadline values already present

Then compose the Rules response again so the next command is visible.

## Chat Output

Keep chat output minimal.

Do not hand-write a separate dashboard. Let the composer render the response.

If locked, respond with:

- the composed rules response
- a reminder to read the inline rules carefully before answering
- an invitation to ask questions about the rules before replying
- exact confirmation prompt: `Do you agree to these terms? Reply yes or no.`

If unlocked after `yes`, respond with:

- rules acknowledged
- the strategy-conversation offer (one line)
- the Resources preview (see **Resources Preview**)
- next command: `$resources`

If composer generation fails, use a compact text fallback:

- current stage: Review
- locked/unlocked status
- exact yes/no requirement when locked
- next command only when unlocked

---
name: prepublish-getting-started
description: 'Explain what Prepublish can do for a YouTube creator and route the request to the right check. Use when the user asks "what can Prepublish do", "how do I use Prepublish", "what is a script audit", "help me improve my YouTube videos before recording", "what should I check before filming", or when a YouTube scripting request is broad and it is unclear which check fits. Prepublish audits YouTube scripts before recording: hook, structure and pacing scores, a relative attention-risk map, flagged passages with rewrites, hook scoring, policy pre-flight, reused-content signals and script length planning.'
---

# Getting started with Prepublish

Prepublish is a pre-production check for YouTube scripts. It reads a draft before it is recorded and shows what to fix while fixing it is still cheap: a rewrite, not a reshoot. It reads text only.

Read `references/claims-and-limits.md` before describing the product.

## What it can do (map the request to a check)

| The creator wants to | Use | Tool |
| --- | --- | --- |
| Know what is weak in a finished draft, with rewrites | youtube-script-audit | `audit_script` |
| Fix the draft and check the fixes landed | youtube-script-revision-loop | `audit_script`, `get_audit`, `audit_hook` |
| Judge or compare openings | youtube-hook-review | `audit_hook` |
| One full "ready to record?" pass | youtube-prerecord-checklist | all checks |
| Check demonetisation or guideline risk, or reused-content risk | youtube-monetization-preflight | `policy_preflight`, `check_authenticity` |
| Plan length or a word budget per section | youtube-script-length-planner | `script_runtime` |
| QA a faceless or AI-assisted narration script | faceless-channel-script-qa | `check_authenticity`, `audit_script` |
| Check a Short | youtube-shorts-script-check | `script_runtime`, `audit_hook`, `audit_script` |
| Review a script for a client, or a writer's delivery | scriptwriter-client-review | `audit_script` and others |

## How to explain it in two sentences

"Prepublish reads your script before you record and marks the passages most likely to lose a viewer, with a rewrite for each and a map of where the draft sags. It checks text only, so it cannot see your delivery, edit or thumbnail, and it does not predict views."

## What it does not do

- Write a script from nothing (you can draft one with the user, then audit the draft).
- Analyse a published video's analytics, retention graph or views.
- Predict views, retention, click-through rate or monetisation.
- Review thumbnails, titles for click appeal, audio or video.

When a request falls here, say so briefly and offer the nearest check that fits.

## Getting the most from it

- Paste the full script and the planned title. The audit checks whether the script delivers the title's promise.
- Users without a Prepublish account get free checks with daily limits; the full audit's free result is released by email, so they will be asked for an address (used to send the result link and a few follow-up emails with an unsubscribe link).
- Fix the top one to three passages, then re-check. Do not chase every small item.

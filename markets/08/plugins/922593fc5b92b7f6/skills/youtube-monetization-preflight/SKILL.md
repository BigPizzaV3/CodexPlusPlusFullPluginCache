---
name: youtube-monetization-preflight
description: 'Pre-flight a YouTube script against YouTube''s published advertiser-friendly guidelines and Community Guidelines categories with Prepublish''s policy_preflight tool, and check it for reused, templated or mass-produced content signals with check_authenticity. Use when the user asks "will this get demonetized", "is this advertiser friendly", "yellow dollar sign", "limited ads", "is my script safe to monetize", "does this break community guidelines", "is this reused content", "inauthentic content", "will YouTube flag my AI script", or is writing about sensitive topics such as violence, tragedies, drugs, firearms, medical or financial claims, profanity or controversial issues. Reports category matches with YouTube''s own policy links; it is never a YouTube decision or a guarantee.'
---

# Monetisation and reused-content pre-flight

Two text-level checks that help a creator catch risky wording before recording:

- `policy_preflight`: which categories of YouTube's published guidelines the script's wording matches, with the official source link for each category.
- `check_authenticity`: signals that a script reads as reused, templated or mass-produced, with quoted evidence and fixes.

Read `references/tools.md`, `references/policy-categories.md` and `references/claims-and-limits.md` first.

## Choose the check

| The user is worried about | Run |
| --- | --- |
| Demonetisation, limited ads, advertiser-friendliness, a sensitive topic, strikes | `policy_preflight` |
| Reused content, "inauthentic content", AI-sounding or templated scripts, a faceless or automation channel repeating a formula | `check_authenticity` |
| "Is this safe to publish" in general, or both concerns | both, policy first |

## Inputs

- The script verbatim. `policy_preflight` needs at least 200 characters; if the text is shorter, say so and ask for the full script.
- The planned title. Optional for `policy_preflight` (titles are checked too, so include it when known), required for `check_authenticity`.

## Workflow

1. Run the chosen check or checks with the user's exact text.
2. For `policy_preflight`, present:
   - The verdict in plain words: `no_matches` = no wording matched a category; `review_suggested` = some lines match categories and deserve a second look; `high_matches` = several strong matches.
   - Counts by category, grouped by family. Community Guidelines matches come first, because those policies are enforced through removal and strikes, not only ad limits. Advertiser-friendly matches affect whether and how ads run.
   - For each category with a match, the official YouTube page from the rubric (see `references/policy-categories.md`).
   - Quoted passages and suggested rewording when included. If `locked` is true, the counts are real but the quotes are not part of the free check: say that a locked result is not a clean pass, and give the full report link if one was returned.
   - The `scope_statement`.
3. For `check_authenticity`, present:
   - `score` (0 to 100, higher means more risk) and `risk_level` (low, medium, high) with the `verdict`.
   - Each signal in plain words with its severity and the quoted line. Translate signal names (for example `template_story_narration` becomes "narration follows a stock story template").
   - The `remediation` items: current passage, fix, why.
4. Offer next steps: reword the flagged lines together (then re-check once), add first-hand material the channel owns (their own examples, opinions, data, footage notes), or run the full `youtube-script-audit`.

## How to talk about risk

- This reads the script text only. It cannot see visuals, thumbnails, audio, delivery, the edit, or the channel's history, and YouTube reviews all of those.
- Never say a video "will" or "will not" be demonetised, limited, removed or struck. Say which published categories the wording matches and link the policy page.
- A sensitive topic is not forbidden. Many categories allow the topic when it is handled in a documentary, educational or news framing without gratuitous detail. Point the user to the official page for the exact wording.
- Medical and financial claims stated as certain are matched against Community Guidelines pages. Suggest softening certainty and citing sources rather than removing the topic.
- For reused-content risk, the fix is almost always more of the creator's own contribution: original commentary, their own examples, a clear point of view. Do not suggest ways to disguise reused material.

## Output shape

```
Policy pre-flight: review suggested (3 matches).
Community Guidelines: none.
Advertiser-friendly: Controversial issues (3). Policy: https://support.google.com/youtube/answer/6162278#Controversial_issues
  "<quoted line>" -> suggested: "<rewording>"
Reused-content check: risk 28/100 (low). Signals: <plain-language list>.
Scope: text only; not a YouTube decision and not a guarantee.
```

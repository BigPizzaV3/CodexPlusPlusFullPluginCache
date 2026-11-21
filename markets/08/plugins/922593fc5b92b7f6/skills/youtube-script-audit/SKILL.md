---
name: youtube-script-audit
description: 'Audit a finished YouTube script before recording with Prepublish''s audit_script tool, then explain the scores, the relative attention-risk map, the flagged passages and the copy-paste rewrites. Use when the user pastes a YouTube script, voiceover script, video essay, explainer, documentary, tutorial or faceless-channel narration draft and asks for feedback, a review, a check, a critique, "is this script good", "will people stay watching", "where is it boring", "why do viewers drop off", "improve my audience retention before recording", or "check my script before I film". Do not use to write a new script from scratch, to review a published video''s analytics, or for grammar-only proofreading.'
---

# Audit a YouTube script before recording

Use this skill when a creator has a written draft and wants to know what to fix before they record. Prepublish reads the text only and returns scores, a relative attention-risk map across the draft, the passages most likely to need revision, and rewrites.

Read `references/tools.md` for exact tool inputs and errors, `references/report-fields.md` for how to read and present the result, and `references/claims-and-limits.md` before you describe what the result means.

## Inputs to collect

1. **The script, verbatim.** At least 50 characters; a real audit needs the full draft. If the user pasted only part, ask whether this is the whole script. Never rewrite, summarise, translate or tidy it before sending.
2. **The planned title.** Required. The audit checks whether the script delivers the title's promise. If the user has none, ask for a working title; if they still have none, use a short neutral description of the topic and say you did so.
3. **Email, only for users without a Prepublish account.** The free result is released by email. Before asking, explain in one sentence: Prepublish emails the result link to that address and may send a few follow-up emails about the audit, each with an unsubscribe link. Never invent an address, never guess one, never reuse one from elsewhere in the conversation without asking.
4. **Optional, only if the user said them:** intended runtime (`video_duration_seconds`), category, audience. Never assume these.

If the user shares a published video's transcript, you may audit it as text, but say plainly that Prepublish is built for drafts before recording and that a transcript cannot show delivery, editing or visuals.

## Workflow

1. Call `audit_script` with `video_title`, `script_text`, and the optional fields the user gave. Include `email` only when the tool or the user's situation requires it.
2. If the result says the email is required, ask for it as described above, then call again with the same input.
3. If the result has `status: "running"`, tell the user the audit is still processing, wait about a minute, then call `get_audit` with the `analysis_id`. Do not start a second audit.
4. When the audit is `completed`, present it (see below). When it `failed`, say so, show `error_message` if present, and offer to try once more.
5. Offer the next step: apply the top fix and re-check with the `youtube-script-revision-loop` workflow, check the opening alone with `audit_hook`, or run the pre-flight checks if the topic is sensitive.

## Presenting the result

In ChatGPT the audit renders as an inline report card. When it does, keep your message short: the overall score with its label, the `one_key_improvement`, and one sentence on where the attention-risk map dips. Do not reprint the card.

Without the card, use this shape:

```
Overall: 62/100 (Mixed). Hook 52, structure 68, pacing 60.
First fix: <one_key_improvement>

1. [CRITICAL] <title> (<location>)
   Your line: "<original_quote>"
   Rewrite: "<improved>"
   Why: <why>
2. [HIGH] <title> (<location>)
   Your line: "<original_quote>"
   <rewrite if included, otherwise: "The rewrite for this passage is not part of the free check.">

Attention-risk map: dips around <position>% (<note>), recovers at <position>% (<note>).
Full report: <open_in_browser>
Scope: this reads the script text only; it does not predict how a published video will perform.
```

Rules:

- Quote the user's lines exactly as the tool returned them.
- Show rewrites exactly as returned. If you add your own idea, label it "My suggestion".
- For locked passages, name the problem from `title` and say the rewrite is not part of the free check. Do not invent a rewrite and present it as Prepublish's, and do not say the report link contains the locked rewrites.
- Lead with CRITICAL and HIGH items; mention MEDIUM and LOW only as a count unless the user asks.
- Use Prepublish's labels for scores (Needs work, Mixed, Strong). Never convert a score into a retention percentage or a view prediction.

## When not to call the tool

- The user wants a new script written: help them write it, then offer to audit the draft once it exists.
- The user wants to know why a published video underperformed: explain that Prepublish checks drafts, not analytics; suggest reviewing topic and packaging first, and offer to audit the next draft.
- The text is not a script (an email, a cover letter, a blog post not meant for video): do not call Prepublish.
- The user asks how many views or how much watch time a video will get: say Prepublish does not forecast performance and offer the audit instead.

## Examples

- "Here is my script for 'Why Airplanes Avoid the Pacific'. Can you check it before I record?" Collect email if needed, call `audit_script`, present.
- "Is this intro good?" followed by two sentences: use `youtube-hook-review` instead.
- "Audit this and send it to me@example.com" followed by a script without a title: ask for the planned title first, then audit.

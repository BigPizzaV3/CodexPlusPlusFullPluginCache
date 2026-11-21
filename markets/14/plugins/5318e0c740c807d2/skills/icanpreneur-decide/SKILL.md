---
name: icanpreneur-decide
description: 'Turn saved Icanpreneur Canvas, research and insights into a reasoned decision: what to test or change next, whether to prioritize a customer segment, whether positioning needs to change, whether the evidence supports a feature or claim, or whether more evidence is needed. Also updates the Canvas after new evidence and checks a pitch, deck or set of claims against the research. Use when the user asks what to do next, which assumptions are riskiest, whether the evidence supports something, or for a decision brief or recommendation. Load `icanpreneur` first. Do not use to run or set up research (`icanpreneur-build-research`), to ask a Buyer Persona a question (`icanpreneur-persona-feedback`), or to generate assets (`icanpreneur-gtm-assets`).'
---

# From evidence to a decision

Research ends with findings. This skill turns them into a choice the user can explain and defend: what the evidence supports, what it contradicts, what is untested, and what to do next. Load [icanpreneur](../icanpreneur/SKILL.md) first; its rules apply. **Before writing the brief, updating the Canvas or checking a pitch, read [references/decision-brief.md](references/decision-brief.md)** (template, criteria, procedures).

By default this skill only reads. Write only when asked: edit Canvas items, or save a note. Do not start research, regenerate assets or ask the persona unasked; offer them as next steps. For several workspaces use `icanpreneur-cohort-review`.

## 1. Pin down the decision

State the decision in one line and the segment it concerns ("Prioritize segment A?", "Does the evidence support our positioning?", "What should we test next?"). If either is unclear, ask one short question. Find the workspace.

## 2. Read what exists (free)

1. `get_canvas`: the segments, problems and other items. These are the assumptions.
2. `list_research` and `get_research` for the segment.
3. `get_research_analysis` (status, `updatedOn`), `list_research_insights` (all sources/quotes, unpaged) and `get_research_quality`.
4. The evidence mix of each research you use: paged to `totalCount`, de-duplicated by interview ID when projects share interviews.
5. `list_notes` for earlier decisions on the same question.
6. `get_buyer_persona` status, if a persona exists.

If analysis is `Pending` or older than the newest interviews, say the findings may not include them. Report interview stage and analysis state separately.

## 3. Sort and judge

Keep five kinds apart: real or imported interviews ("customers said…"), synthetic interviews (hypothesis), Canvas items (assumptions), persona answers (simulated, never demand), and your interpretation.

Give each assumption a status and its basis:

- **Supported**: real or imported interviews say it.
- **Contradicted**, **mixed**, **only simulated**, or **untested**.

Then:

- Cite the evidence available and counts where established. Leave missing quotes and counts missing.
- Do not score evidence, invent a threshold or say "validated". Say when a finding rests on one interview or only synthetic ones.
- Check the segment and problem against the platform definitions first. A segment that is only a job title, or a problem with no stated alternative, is itself a weakness.
- Look across all research types, and match each assumption to the stream best placed to test it (reference).

## 4. Prioritize

Rank by impact if wrong and by uncertainty, with reasons in words. Segment and problem come first when they are weak or the decision is about direction. For a price, feature or message decision, prioritize the assumptions behind that decision. Do not send the user back to segment research when the question is not about the segment.

## 5. Recommend

Lead with the actual recommendation in the user's terms ("prioritize segment A", "refine pricing", "defer the feature", "collect more evidence first"), then the reasons. Describe the evidence as **strengthening**, **needs refining**, **explore differently** or **not enough evidence yet** (often the right answer). Name the main alternative and a next step that fits: usage data, existing transcripts, an experiment, or acting on what is supported. If more customer evidence is the right step, give the stream, the segment and who to interview; Do not treat a fixed interview count as a quality threshold. If the evidence suggests a misfit or a split, propose it and point to `icanpreneur-build-research` (segments-and-splitting reference); restructure nothing unasked. Improvements within the current business stay in the current workspace.

## 6. Report

Use the brief format in the reference. Lead with the recommendation. Every conclusion carries its available trail: the insight or interview, real/imported/synthetic, and support counts where the tool gives them. Offer once to save the brief as a note.

## Other jobs (procedures in the reference)

- **Update the Canvas after new evidence**, only when asked: change segments and problems first, replace outdated assumptions, check coherence, then read affected assets against the new understanding. A Canvas edit alone does not show an asset must be regenerated.
- **Check a pitch or claims**: customer research supports claims about problems, buying behavior and alternatives. Revenue, capabilities, customer numbers and projections are "not established by this research". Accept user-supplied evidence with attribution.

## Mistakes to avoid

- Calling anything validated, or scoring evidence.
- Forcing a label or an interview as the answer when the decision is about something else.
- Using a persona's answer or a Canvas item as evidence.
- Treating a claim research cannot speak to as unsupported.
- Editing the Canvas, regenerating assets or starting research unasked.
- Ignoring earlier decision notes, or mixing evidence from different workspaces.

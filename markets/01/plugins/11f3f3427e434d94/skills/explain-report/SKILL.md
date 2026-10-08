---
name: explain-report
description: Walk the user through one of their SAMRUM reports (couple, parent-child, sibling, family overview, individual) one pattern at a time. Use when the user asks to explain, summarize, read or understand a report, or asks why two named people keep clashing about the same thing ("forklar min rapport", "hvad står der i vores parrapport", "explain our report", "förklara vår rapport", "erklär unseren Bericht"). Do not use for a conflict happening right now (use right-now-conflict), for one person's own traits (use compare-two-people or get_profile), or for what to do next (use what-next).
---

Use this skill when the user wants to understand a SAMRUM report they already have. The server instructions apply throughout; this skill adds the workflow.

## Input

- Which report. If the user names people ("our couple report", "the report about me and Sofie") or a type, use that.
- If you do not know the reportId yet, find it first (step 1). Never guess IDs.

## Steps

1. Call `get_family_overview` (without `includeRecommendations`) to see the family's reports and their IDs, unless you already have them from earlier in the conversation.
   - Exactly one report with status `ready`: use it.
   - Several: ask one short question about which one, unless the user's wording already points to one.
   - None ready: say so, link to the dashboard from the result, and stop. Do not explain a report that does not exist.
2. Call `get_report` with `reportId` and `detail: "summary"`. Prefer the summary; it has the key patterns, every conflict loop with trigger and repair, and counts of experiments and conversation starters.
   - Use the `section` argument (`key_patterns`, `conflict_loops`, `experiments`, `conversation_starters`, `professional_help`) when the user asks for one narrow part.
   - Use `detail: "full"` only when the user asks for exact wording ("read me the exact experiment").
3. Open with one thing: the single most relevant key pattern or the main conflict loop. If the user described a situation, pick the loop that matches it. Describe it as a loop (when A does X, B tends to Y, which leads A to ...), never as one person's fault. Weave in the report link from `reportSummaries[].link`.
4. End with an offer to continue (next pattern, the experiments, the conversation starters). Let the user pull the thread.
5. When the user asks why a tendency exists behind a loop, call `get_profile` for the relevant participants. Reports show the interaction; profiles explain the tendencies.
6. For cross-report questions, call `get_report` once per report with `detail: "summary"`.

## Output

- 2 to 4 short paragraphs, maximum 150 words, in the user's language. If the report language differs from the user's language, paraphrase naturally.
- Report link woven into the text as a markdown link, not listed at the end.
- One experiment at a time when asked for experiments, not a list.
- Individual reports: address the user directly (du-form in Danish, Swedish and German).
- When `needs_practitioner_bridge` is true, include `practitioner_bridge_text` naturally. Calm tone, no alarm.

## Do not

- Summarize the whole report in one message or list all patterns.
- Assign blame, rank family members, or use clinical labels.
- Invent patterns, scores or content that is not in the tool result.
- Draft the exact words the user should say to a family member.
- Speculate about what another family member felt or heard.
- Re-explain the report to someone who gets `access_denied`. Say the report is not shared with them and offer what they do have access to.

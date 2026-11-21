---
name: nonprofit-ai-policy
description: Draft or revise a nonprofit AI use policy with StratusLIVE's fixed template rules, an AI tool register, a draft board resolution, and board questions. Use for nonprofit AI governance planning and board preparation.
---

# Nonprofit AI Policy

Turn explicit organizational choices into a draft for board review. The bundled model contains the policy clauses and tailoring rules from StratusLIVE's published [Nonprofit AI Policy Template](https://stratuslive.com/tools/ai-policy-template/). Read [source.md](references/source.md) for provenance or version questions.

## Begin with the user's information

If answers are already supplied, reuse them and ask only for missing or conflicting choices. Otherwise guide the user through the five groups in [questionnaire.md](references/questionnaire.md), one group per exchange. The template uses an organization type and needs no organization name. Do not ask for revenue or staff role; these do not affect the policy clauses. Optional legacy fields are documented for importing website answers.

Ask for categories and policy choices only. Do not request donor lists, client records, health details, payment information, personnel files, credentials, or actual personal records. If those are supplied, do not copy them into answer files or documents; explain that category-level choices are sufficient. An allowed category in the proposed policy is not authorization to process actual records in this plugin.

Use the option IDs from the questionnaire. Map clear natural-language answers to those IDs; clarify ambiguous choices. Do not select an approver, vendor requirement, permitted data category, or review interval for the user. Sensitive handling, autonomy, and disclosure each have an `undecided` option. The generator keeps the starting rule and flags the board decision. `dataScope: ["none"]` is exclusive: do not combine it with any other category. Every multi-choice field needs at least one selected option.

Before generation, show a compact summary of the choices, identify unresolved decisions, and correct any contradictions. Continue when the user has already supplied clear choices and asked for the draft; do not require a second permission to generate it. For unspecified required choices, ask rather than infer organizational practice. [sample-answers.json](references/sample-answers.json) is a fictional example, never the user's default.

Flag a workflow that appears to need an excluded data category, such as gift entry while giving and finance records are excluded. Keep the data boundary unless the user changes it; explain that the workflow is permitted only within the selected data scope. A broad use category does not override the narrower data rule. For undecided disclosure, present the four questionnaire choices in board preparation; the generated section 8 contains the starting rule.

## Generate the draft

Use the available execution tool and bundled scripts. Do not assume an absolute installation path. Resolve paths relative to this skill folder, quote paths, and create a new task-local output directory.

1. Save only the structured policy choices as `answers.json`.
2. Run `node scripts/build-policy.mjs --input <answers.json> --out-dir <output-directory> --date <YYYY-MM-DD>` from this skill folder. Use the user's local calendar date; the explicit date keeps repeat runs consistent. The command writes the full policy, its structured document, board questions, and a summary of board decisions.
3. For an editable Word file, run `python3 scripts/export-docx.py <policy.json> <policy.docx>`. This needs `python-docx`. Check whether it is available; do not install software silently. If unavailable, deliver the Markdown file and explain the Word limitation.
4. Check that the command succeeded and the resulting files exist before linking them. Confirm eleven numbered policy sections, both appendices, and ten board questions. Show the posture, approver, permitted categories, and open board decisions in chat, then provide the draft and available Word file.

The Node generator uses fixed clauses, not model-written policy text. Do not claim deterministic generation unless the bundled generator actually ran. If code execution is unavailable, help the user collect choices and explain the template. Offer the source website for generation, or a script-capable Work/Codex environment; do not pretend a document was created.

The output is always a draft. The template's counsel-review note belongs in the document. Never label it board-approved, legally compliant, HIPAA-compliant, certified, or adopted without independent evidence. A vendor confirmation requirement is a question for the vendor, not proof the vendor satisfies it. Board answers describe the proposed policy rather than verified current organizational practices.

## Revise and prepare for the board

For a change to policy choices, update only those choices, rerun the generator, and summarize the affected sections. Keep the other choices. For custom wording outside the fixed template, separate proposed amendments from the generated policy and label them for review; do not describe modified prose as the unchanged website template.

Use the generated board questions for meeting preparation. The AI tool register begins blank; populate a row only from user-supplied tool facts, leaving confirmations and dates unknown when evidence is absent. Do not invent vendors, adoption dates, owners, deadlines, or approvals. In a review of an existing policy, distinguish the user's wording, the template's recommendation, and the decisions still needed.

The policy body names no product or vendor. Keep it usable with any tool and avoid adding sales pitches. Do not imply the policy changes platform permissions or enforces technical controls. The package has no external app, CRM, email, or publishing capability. It does not transmit the answer file to StratusLIVE; OpenAI still processes the conversation and execution under the user's account settings. Opening the source website is a separate visit governed by its published privacy policy.

---
name: icanpreneur-build-research
description: 'Set up and run customer research in Icanpreneur (problem discovery and validation, win/loss, buyer persona, or other research): create a workspace from a business description, define or refine customer segments, plan interview scripts, create research, set up interviews with specific customers, import existing transcripts, add synthetic interviews, read findings, and turn interviews into a Buyer Persona. Use when the user wants to start research, add evidence, understand what customers say, prepare the next round, fix a misfit interviewee or split a segment. Load `icanpreneur` first. Do not use for general research advice that does not involve an Icanpreneur workspace, or for a simple lookup of saved research.'
---

# Build and run customer research

workspace → customer segment → interview script → research → interviews (real, imported, synthetic) → analysis

Analysis and insights are the common endpoint for every research type. Only `BuyerPersona` research has an automatically associated Buyer Persona; do not automatically expect, wait for or mention a persona for other types (an explicit request to compare findings with an existing persona is fine: read it with `get_buyer_persona`). Load [icanpreneur](../icanpreneur/SKILL.md) first; its rules apply to every step.

## 0. Scope

Do the whole piece the user asked for, say which steps use credits, and do not add billable steps beyond it.

| Scope                              | Stop when                                                                                                                                                                                |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Set up                             | The research exists and is ready for interviews.                                                                                                                                         |
| Gather evidence                    | The requested interviews are created or imported and the user has what they need (links, counts).                                                                                        |
| Read results                       | The question is answered from saved analysis, with its evidence mix and `updatedOn`.                                                                                                     |
| To analysis (any type)             | `get_research_analysis` shows `Complete` and you have reported the findings. If still `Pending`, return the IDs and the next check.                                                      |
| To a persona (`BuyerPersona` only) | The persona you triggered is `Complete`, has usable content, and is shown with its evidence line. If it ends in `Error`, stop and say so. Do not present an older version as the result. |

Ask only when a choice is missing: segment, research type, language, script duration, or which interviews to add.

## 1. Workspace

`create_idea` needs `title`, `startingPoint` (`idea` or `existingBusiness`; ask if unclear), `languageTag`, and a `description`, `urls` or `fileKeys`. A logo is not context. Do not invent a description. If the user has no idea yet, finding one is not a tool; talk it through and create the workspace once there is a description.

- Call it once; never again to check. `create_idea` creates the initial Canvas during the call. After success, read `get_canvas` immediately; no separate readiness field or Canvas poll is needed. Logo generation may still run. A timeout or error can leave partial saved work; inspect before any retry. The Canvas is a first draft of hypotheses: show the segments and problems and invite corrections.
- A distinct growth opportunity may suit its own workspace so the current business is undisturbed. Another segment, problem or pricing question within the business stays in the current workspace. Ask if unclear.

## 2. Customer segment

Segments are `CustomerSegments` items in `get_canvas`. One research belongs to one segment; ask which if there are several. For a new one use `create_canvas_customer_segment` (positive starting credits required; automatic linking can use credits), after testing the wording against the platform definition (`icanpreneur` → `references/definitions.md`). Broad groups fail: ask what job they need done and how to reach them, then propose a narrower one. Edit with `update_canvas_customer_segment`. For other boxes use `create_canvas_item` with nonempty `relatedItemIds` to set links without AI association. Omission or `[]` requests billable automatic association; clear links afterward with `update_canvas_item(relatedItemIds: [])` if needed. `validate_canvas_item` is billable; use it when asked.

## 3. Interview script

Pick the type from the goal and use the same type for script and research: `BuyerPersona` (how people buy), `ProblemDiscoveryAndValidation` (does the problem exist and matter), `WinLoss` (why deals close or fail), `Other`. **Before choosing a type, planning several tracks or reading insights by type, read [references/types-and-streams.md](references/types-and-streams.md)** (what each type is for, parallel streams, batches, insight categories). Choose tracks from the learning objectives; problem and buyer research can start together and neither waits for the other.

1. Reuse first: `list_interview_scripts` by segment and type.
2. A script the user wrote: save it as given with `create_interview_script`. This is its only use.
3. Any script you would author: use `generate_interview_script` (billable). Ask for the duration; if told to decide, choose one and say so. Do not write it yourself or save a stand-in if generation fails. Wait on `get_interview_script` until `ready`.
4. To refine: read it, change only what needs changing, and send all `sections` to `update_interview_script`.
5. `duplicate_interview_script` copies a script but cannot move it to another segment.

## 4. Research

Create it with `create_research` (segment, script, type, language). Name it for its purpose ("<Segment> problem discovery", "<Segment> win/loss"), not "buyer research". Synthetic interviews are off unless asked (`true` makes five simulated ones, billable). `BuyerPersona` research requires a positive starting balance even without synthetic interviews. Its initially empty persona can be Complete; do not treat that as generated content. Creating research does not complete interviews or analysis. `update_research` changes affect only later interviews; ask before changing privacy or consent settings.

## 5. Add evidence

**Before importing transcripts, adding existing interviews or creating contacts, read [references/interview-sources.md](references/interview-sources.md).**

| The user has                            | Route                                                                       |
| --------------------------------------- | --------------------------------------------------------------------------- |
| People to interview                     | Create contacts, then `create_interview` for each; give the user the links. |
| Interviews already done                 | Upload transcripts, create the contact, `import_interview`.                 |
| Interviews already in the workspace     | `list_interviews`, then `update_research_interviews`.                       |
| The user asks for synthetic exploration | `generate_synthetic_interviews`, and synthetic contacts if asked.           |

`create_interview` does not conduct or send anything; the user shares the link. There is no outreach tool. Check that participants match the segment. Create only contacts the user gave you; a contact needs first and last name (ask, never invent). After an import, count the interviews actually saved, not the files uploaded.

## 6. Read the results

Read in this order (no direct credit charge): `get_research` (counts), `get_research_analysis` (`status`, `updatedOn`, summary, quality, coverage), `list_research_insights` (all categories, quotes and sources; no paging or per-insight read tool), `get_research_quality`. For one interview: `get_interview_analysis`, `get_interview_insights`, `get_interview_transcript`.

Report:

- what was found, and how many interviews it rests on;
- how many of those are synthetic, and the analysis `updatedOn`;
- what is still uncertain, including findings that rest on one interview or only synthetic ones.

Report interview stage and analysis state separately: a completed interview can have analysis pending. Quality is typically a score out of 100; script coverage is typically a percentage. Report the saved values and explanations without invented thresholds. Estimated improvement is not a measured percentage.

## 7. Persona (BuyerPersona research only)

Membership changes can refresh or empty the persona. If the request depends on the build you triggered, wait for `Complete` and populated content (`get_buyer_persona`). Pending/Error may include older or incomplete fields, with no guaranteed selectable previous completed version. `Complete` does not prove the newest interviews are included. Then: test an offer → `icanpreneur-persona-feedback`; build assets → `icanpreneur-gtm-assets`.

## 8. Next round

1. Read quality, coverage and insights, and name the gaps: few or only synthetic sources, low coverage, contradictions.
2. Turn them into 3 to 6 learning objectives with the questions that would close them. Continue unless the user wants to review first.
3. Generate the script (§3) and refine it to cover the questions.
4. Create the research, then go to §5.

## 9. Misfit interviewees and splitting segments

Propose first and wait for agreement. Fit follows the segment definition, never whether the respondent liked the offer. Split only when it would change a decision, and keep the number of segments small. Evidence is reused by associating existing interviews with the new research (`update_research_interviews`); nothing is re-interviewed. **Before proposing or doing either, read [references/segments-and-splitting.md](references/segments-and-splitting.md).**

## Mistakes to avoid

- Calling `create_idea`, `create_research` or a generator twice to "check".
- Writing a script yourself, or adding synthetic interviews, interviews or segment changes the user did not ask for.
- Treating the first-draft Canvas or synthetic material as validated.
- Assuming an import worked because the upload did.
- Deleting a segment, contact or interview to fix a fit problem.
- Promising to keep watching.

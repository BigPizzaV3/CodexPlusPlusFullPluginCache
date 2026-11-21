# Feedback after confirmed ending

Stop buyer mode, mark ENDED and review the available attempt once. Configuration cancellation has no training report. For a completed retry use focused-retry.md's comparison, not another ordinary report. Instructions are not a deterministic evaluator or validated ability measure.

## Evidence inventory

### Evidence ledger before feedback generation

Before authoring ANY review, enumerate actual messages in chronological order as immutable records:
`{speaker: BUYER|SELLER|CONTROL|MATERIAL, attempt_id, turn_id, original_text, substantive}`.
Assign T01... ONLY to actually performed SELLER utterances after Start, and B01... to buyer utterances.
Never count a buyer question, prepared text, a control (including natural-language End), a quoted example,
a proposed wording, or a post-training action as a performed SELLER turn.
Keep performed seller turn count distinct from substantive seller-turn count and explicitly state which is reviewed.
Bind each feedback card to exactly one performed substantive Seller turn ID and its exact source text.
A Buyer text cannot appear under Your Response; a Seller turn cannot be counted twice or shifted by an offset.
Before declaring complete coverage, compare the actual ledger IDs with feedback card IDs and the reported counts.
If they disagree, correct the evidence mapping BEFORE finalizing the original feedback. If source evidence is
missing/uncertain, label the affected card pending/partial instead of inventing or reassigning speech.
Once feedback has been presented as immutable, do not silently re-evaluate or rewrite it at export time;
disclose any detected original-source inconsistency and distinguish it from rendering failure.


Only human seller speech actually performed in the current active attempt is evidence. Exclude setup, controls, materials, quoted hypothetical transcripts, examples, buyer words, suggestions and unclear voice fragments. Do not infer that a seller discovered a need merely because the buyer volunteered it. A neutral acknowledgment can be a performed but non-substantive turn.

Retain stable IDs, exact text, substantive status, preceding actual buyer cue, relevant facts, reviewed/pending IDs and exclusions. Use chronological Txx / Ax-Txx / Rn-Txx namespaces; missing original offsets use Vxx with a limitation. Count a split turn once. Keep one utterance together unless distinct actions need separate nonoverlapping exact segments; retain their parent and order and account for unevaluated substantive parts.

Every available substantive seller turn gets a card or an explicit pending/source limitation. Match quotations character-for-character, including spelling, punctuation, whitespace and language. Do not paraphrase, translate, insert ellipses or invent missing speech. Uncertain attribution/text means omit that judgment and disclose the gap. Suggested wording is unperformed.

## Concise contextual coaching

Use the actual stage, objective and buyer context. Choose a **primary skill lens** rather than treating all attempts as Discovery: Discovery focuses on question relevance, active listening and verified needs; Proposal on linking options/phases, value, cost/risk constraints and an appropriate next step; Objection Handling on acknowledging, clarifying, evidence and non-defensive response; Negotiation on trades, authorization, conditionality and realistic commitments; Follow-up on agreed actions, ownership, timing and confirmed next contact. If the configured skill is a close variant, apply the nearest lens; do not invent unperformed stages or penalize a Proposal solely for not repeating completed Discovery. Relevant actions can be effective without following a fixed script. Do not invent weaknesses or penalize unused dimensions. A useful question is evidence of the question; an achieved result additionally needs the actual buyer response. Later facts do not justify an earlier unsupported claim.

Keep qualitative analysis in available context when supported:

| Tag | Meaning |
|---|---|
| S / Situation | Relevant process, responsibility, constraint or background. |
| P / Problem | Clarified difficulty, dissatisfaction or friction. |
| I / Implication | Explored consequences of an established problem, without invented harm. |
| N / Need-payoff | Buyer articulates desired value/success; seller asks or checks it. |
| F / Feature | Offering explained within its actual evidence scope. |
| B / Benefit | Capability linked to a stated need without fabricated results. |

Tags describe an attempted action, not points or achievement. Use no forced tag for role confusion. Impact meanings remain positive (helps), negative (harms clarity/trust/relevance), neutral (little effect) and missed_opportunity (an actual cue was not addressed). Preserve any actually produced source classification during later export/localization; missing classification is unavailable, not positive.

An unsupported certification, delivery, compatibility, price or performance assurance cannot be praised for persuasion. Identify its exact claim and suggest evidence checking, conditions or honest deferral. A later correction can be effective without erasing the original claim. Buyer requirements do not prove capability; a promise to verify is not completed verification. Never generate numerical scores, weighted totals, stars, rankings, improvement percentages or competency/personality claims. Evidence counts are not scores.

## Default display

Use explanation language for headings/coaching; quotations remain original; suggestions use training language unless explicitly overridden. Begin with a minimal session/attempt heading and necessary coverage/outcome/source limitations. Then give chronological cards:

### T01 — Short descriptive title
**Your Response** — exact original seller quotation.
**Feedback** — one or two contextual sentences: what worked/needs changing and a useful next action.
**Suggested Response** — one practical, unperformed alternative; no invented facts or agreement.
A per-turn Retry action is an interface control, not part of the immutable Feedback Content; collect actual eligible Retry Txx targets for the separate Post-training Actions group only.

Japanese feedback labels: **あなたの発言 / フィードバック / 発言例**. Place 再練習 only in the separate Post-training Actions group. A non-substantive performed turn gets only a compact ID/status/exact-quote line, no substantive coaching card or retry target.

Do not add unsolicited assessment badges, SPINFB tables, A–D reports, long overall assessments or separate strengths/competency chapters. Necessary limitations remain visible. If there is no seller evidence, state that plainly with no invented quotation, weakness, strength or Retry T01.

Cover all available substantive IDs. If output limits prevent this, identify reviewed/pending IDs, label feedback partial and wait for an explicit continuation; do not claim complete coverage of missing context. A partial continuation is not completed feedback and does not yet show completed actions.

Complete the evidence-ledger identity/count check before finalizing feedback. Retain the immutable **Feedback Content** actually sent: heading/status, outcome/coverage, all cards/comparison, quotations, suggestions and final limitations. Record **Post-training Actions** separately as UI text; do NOT append Save/Retry/Export commands to Feedback Content or treat them as evidence. Never retain only the paragraphs named Feedback. Repeated ending uses the existing complete/partial state without regenerating it.

## Completed actions, once

After completed feedback, retain actual eligible Retry targets and show one compact **Post-training Actions** group separately from Feedback Content:

English:

Save Scenario
Retry T01
Export Training Report (DOCX; TXT / Markdown available on request)

Japanese:

シナリオを保存
Retry T01
研修レポートを書き出す（DOCX／TXT／Markdown）

Use actual IDs, never a made-up T01. With none, state no substantive retry target and omit that command. Save remains visible even if structured fields/DOCX/OAuth/MCP are unavailable. These labels neither generate a file nor call a tool; they are readable text choices, not guaranteed buttons. A later “what can I do next?” redisplays only this group; it does not reevaluate, modify the immutable feedback or call tools. Distinguish Save Scenario (definition only) from Export Training Report (completed-attempt evidence). Read export or personal-scenarios details only after explicit selection.

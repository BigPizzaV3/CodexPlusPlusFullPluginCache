# Publication evals

These fixtures are designed for reviewer reproduction without private context. The plugin is skills-only, so expected behavior refers to the `run-b2b-messaging-workshop` skill rather than an MCP tool.

## Eleven positive tests

### 1. Start from scratch

**Prompt:** “Walk me through building a B2B messaging framework for my SaaS from scratch.”

**Expected behavior:** Activate the workshop, explain the four phases, show the original Phase 0 guidance once, and ask for the company or product name together with the first focused questions.

**Expected result shape:** A single current step with `What to write here`, `Your question`, and a sentence explaining the optional text commands. It must not dump the full questionnaire or style commands like buttons.

**Fixture:** None.

### 2. Use supplied research without inventing evidence

**Prompt:** “Turn these interview notes into a Product Marketing source of truth, and guide me through the gaps: [attach or paste notes].”

**Expected behavior:** Extract only supported facts and sourced quotes, label inferences and gaps, begin at the earliest incomplete template section, and request approval section by section.

**Expected result shape:** A workshop ledger summary followed by one guided step. No fabricated quote, metric, or proof point.

**Fixture:** Use `fixtures/interview-notes.md`.

### 3. Show an example without contaminating state

**Prompt sequence:** Start a workshop, reach Industry problems, then reply “See an example.”

**Expected behavior:** Show only the fictional Industry problems answer, label it illustrative, keep the same progress indicator, and ask the original unanswered question again.

**Expected result shape:** `Fictional example — illustrative only, not your answer`, one section example, then the same unanswered question. No draft or approval prompt.

**Fixture:** Company name `Acme Ops`; no industry-problem answer supplied.

### 4. Resume from a checkpoint

**Prompt:** “Resume my messaging workshop from this checkpoint: [paste fixture].”

**Expected behavior:** Parse the checkpoint, summarize approved answers, hypotheses, and gaps, confirm the recorded next step, then display that step's exact guidance.

**Expected result shape:** Resume summary followed by Phase 1, Competitive alternatives. Approved fields remain unchanged.

**Fixture:** Use `fixtures/resume-checkpoint.md`.

### 5. Pressure-test an existing framework

**Prompt:** “Pressure-test this B2B messaging framework and help me repair what fails: [paste fixture].”

**Expected behavior:** Start Phase 3, run all six canonical checks, identify generic differentiation and unsupported proof, and route repairs to the correct Phase 1/2 sections.

**Expected result shape:** A six-row Pass/Fail/Unresolved summary plus the first failed source section's guidance and a focused repair question.

**Fixture:** Use `fixtures/framework-needing-pressure-test.md`.

### 6. Make four-phase numbering unambiguous

**Prompt sequence:** Start a workshop and continue through the pressure test.

**Expected behavior:** Use `Phase 0 · Company snapshot (1st of 4 phases)` through `Phase 3 · Pressure test (4th and final phase)`. Never display `Phase 3 of 4` or imply a separate Phase 4 exists.

### 7. Capture quote source and privacy in one turn

**Prompt:** “A customer said, ‘Changing one page broke the mobile layout.’”

**Expected behavior:** Before drafting the quote, ask one combined question for its inspectable source record and whether the customer should be named, anonymized, or redacted. Accept a specific anonymized record label without demanding private identity.

### 8. Allow one consolidated self-serve persona

**Prompt sequence:** At Personas, the user explains that the same website owner uses, buys, approves, and pays for a low-cost self-serve product.

**Expected behavior:** Produce one consolidated persona, record why roles are combined, and do not invent approvers or blockers merely to reach three rows.

### 9. Turn a Proof gap into a validation plan

**Prompt sequence:** At the Proof check, the user confirms there are no completed customers, pilots, benchmarks, or internal outcome records.

**Expected behavior:** Return `UNRESOLVED EVIDENCE GAP`, distinguish offer mechanics from outcomes, and create a compact plan covering baseline, follow-up window, source or owner, and evidence needed for every unproven claim. Do not invent target improvements.

### 10. Give proactive help without inventing facts

**Prompt sequence:** Reach any content field and reply `help`.

**Expected behavior:** Explain what decision the field captures, suggest two to four answer directions grounded in approved information, recommend one when useful, clearly label suggestions as possible shapes or hypotheses, and end with one easier diagnostic or a scaffold with blanks.

### 11. Deliver a clean source of truth

**Prompt sequence:** Complete a workshop, approve all required content, and request `Markdown + a new Notion page`.

**Expected behavior:** Return the complete Markdown first, then create the confirmed Notion page from that clean document. Preserve approved customer quotes, owner/version metadata, changelog, headings, tables, and copyright.

**Expected result shape:** Neither format contains instructional `NOTE` or `TIP` callouts, “What to write here,” template prompts, placeholder explanations, facilitator directions, or metadata rendered as a quote block.

## Three negative tests

### 1. One-off social copy

**Prompt:** “Write a LinkedIn post about our new feature.”

**Expected behavior:** Do not activate the full workshop. Handle or route the isolated copywriting request normally.

**Why not:** The user did not ask for foundational messaging, positioning, or a source of truth.

### 2. Legal advice

**Prompt:** “Give me legal advice about this contract.”

**Expected behavior:** Do not activate the workshop because the fictional example concerns lawyers. Follow the normal legal-guidance boundary instead.

**Why not:** The request is legal analysis, not B2B messaging.

### 3. Linear integration

**Prompt:** “Help me build a Linear integration and issue tracker.”

**Expected behavior:** Do not activate the workshop or mention the fictional example.

**Why not:** The internal product analogy is not a trigger and never appears in public workshop content.

## Behavioral acceptance checklist

- Every step shows only the current template guidance and original prompt when present.
- Phase-level guidance appears once on phase entry and is not repeated on every question.
- When no Notion prompt exists, the step shows only its own canonical field placeholder; the help-mode diagnostic remains hidden until requested.
- Optional commands are described as text replies in a sentence, never as a dot-separated, pipe-separated, bold, or button-like menu.
- Guidance, question, example, and draft are visually distinct.
- The workshop asks no more than three initial questions and one follow-up at a time.
- A vague answer receives a focused follow-up rather than a polished invention.
- Help mode explains the decision, proposes two to four grounded answer shapes, recommends one when useful, and still supplies no company facts.
- Every customer quote gets source and privacy treatment in one combined follow-up before drafting.
- Progress labels identify Phase 3 as the fourth and final phase; no output implies a separate Phase 4.
- A confirmed low-cost self-serve motion may use one consolidated persona instead of invented roles.
- An unresolved Proof check produces a measurement plan without invented targets.
- `See an example` neither advances progress nor updates the ledger.
- Example content never appears in a pause checkpoint or final output.
- Required skips remain open gaps; optional skips are explicitly omitted.
- A revision does not overwrite approved text before approval.
- Pause/resume restores the exact phase, step, statuses, and provenance.
- Phase 2 introduces no new audience, comparator, capability, outcome, or proof.
- Phase 3 routes each failure to the defined source section and reruns repaired checks.
- Final Markdown follows the canonical template order but contains no instructional `NOTE` or `TIP` callouts, “What to write here” blocks, template prompts, placeholder explanations, or facilitator directions.
- A newly created Notion page is built from the same clean final Markdown and contains no instructional callouts from the master template.
- Owner/version metadata and the changelog remain as ordinary document content rather than quote blocks or callouts.
- Approved customer quotes and sourced quoted evidence remain intact.
- The master Notion page ID is never passed to an update operation.
- No invented customer, metric, testimonial, quote, legal claim, or ExampleCo detail appears in user output.

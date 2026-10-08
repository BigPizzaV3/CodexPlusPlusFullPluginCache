# Eastern Orthodox Theology

Version **0.9.16**, skills-only. The plugin retains the Eastern Orthodox (Chalcedonian) confessional method, three stable skill identities, complete doctrinal-standing framework, and supplied artwork.

## Why this revision

The supplied 0.9.15 Chat audits described two incomplete-read mechanisms: a first page with an unused continuation, and a complete reader result whose outer tool output lost a middle section. A later user-requested diagnostic reported recovery by returning the text in smaller chunks. These are supplied reports, not independently captured ordinary-Chat tool traces or universal host-limit measurements.

This release makes automatic recovery explicit in the first essential check. Follow offered continuations; when complete text is held inside code but its wrapper output is truncated, deliver contiguous verbatim chunks through separate bounded tool returns. Use documented storage or reread the same revision, track received ranges, recover gaps, and reduce any chunk still truncated. Do not invent controls or assume a fixed platform token limit. Several prints inside one capped call still share its budget.

A string inside code, character counts, headings, hashes, or a visible ending do not substitute for instruction text actually delivered to the assistant. Matching bundled procedures need one complete delivery, not duplicate entry loads. If supported recovery is unavailable or stops making progress, disclose the remaining gap and withhold dependent decisions. Keep instruction chunks out of ordinary answers unless the user requests their reproduction. Later recovery is not earlier access, and complete delivery is not complete application.

All seven canonical procedures remain byte-for-byte unchanged from 0.9.15. Each entry retains its principal procedure first. Essential checks finish within the first 917 whitespace-delimited words; the entries contain 8,525 words for theology, 8,518 for Scripture, and 8,519 for verification. These are word counts, not token budgets. The files remain long; clearer recovery instructions do not guarantee host access or model compliance.

## Contents and method

- **analyze-orthodox-theology:** theology, Church history, reception, material moral questions, and role boundaries.
- **interpret-orthodox-scripture:** controlling witnesses, translation, easier rendering, paraphrase, exegesis, and interpretive scope.
- **verify-patristic-sources:** quotations, attribution, editions, locators, source identity, and citation support.

Each entry includes the shared method, source verification, Scripture interpretation, doctrinal standing, comparative coverage, calendar evidence, and source finding aids. Apply relevant procedures once, including when multiple entries load. Reading instructions does not complete verification.

The release has no MCP server, external-service dependency, credentials, or runtime scripts. Source finding aids point to external evidence that must still be researched when the task requires it.

Scripture, Fathers, Councils, and Liturgy are read together as Holy Tradition. Modern academic and non-Orthodox material can supply identified evidence, support, or contrast. Adverse evidence remains visible. Wording, authorship, ecclesial authority, and reception remain distinct.

The full standing method retains eight outcomes: Dogma; Dogmatic exclusion; Broadly received teaching; Broad ecclesial rejection; Recognized theologoumenon; Recognized Orthodox alternative; Unresolved reception; and Not established on examined evidence. Each needs its specific warrant and complete fields. Incomplete research calls for withholding a standing. Ordinary catechesis does not automatically require formal standing blocks.

Personal spiritual-case boundaries, explicit adversarial activation, source roles, and requested-source coverage remain. The early checks distinguish dated attestation from origin or derivation, preserve exact variants and actor roles, keep transmission hypotheses qualified, and require a separate review of the opening, headings, table cells, and conclusion against the evidence.

## Public output

Substantive answers normally include Approach, Mode, Methods used, any material Source note or Basis, and an Answer label. Complete formal standing blocks precede Answer. A controlling user or platform format may replace the default. Brief factual answers may omit the header.

Methods used reports procedures actually applied. A correct header, skill chip, or version number alone does not establish substantive compliance.

## Upload and test

The stable identifier is `orthodox-theology`. The visible title remains **Eastern Orthodox Theology**, as selected by the user. The manifest and skill bodies identify **0.9.16**; no version suffix is added to the title.

Use `orthodox-theology-0.9.16.zip` in the full-plugin draft ZIP upload flow. Its root contains `.codex-plugin/plugin.json`, without an enclosing version directory. A separate field requesting individual skill folders is a different target: use the folders inside `skills` for that field.

After uploading, start a fresh normal Chat with the updated draft and use the substantive prompt in TESTING.md without a preliminary access-audit instruction. Preserve the exact prompt, full answer with citations, visible model/mode, and available file activity; audit access afterward. Authoring tests do not establish normal-Chat activation, complete delivery, or compliance.

## Maintenance and source history

Canonical procedures live under `maintenance/modules`, early controls in `maintenance/core-controls.md`, and introductions under `maintenance/entrypoints`. Edit those sources and regenerate:

```bash
python3 maintenance/build.py
python3 maintenance/build.py --check
python3 maintenance/build.py --check --zip /path/to/orthodox-theology-0.9.16.zip
```

The builder embeds complete modules, checks internal links and generated-file agreement, preserves identities and assets, and validates ZIP member paths and bytes. Standard plugin and skill validators provide additional structural checks.

The plugin ZIP contains runtime files and documentation only. The separate source-history backup contains a Git bundle and restore instructions. Its history begins with the recovered installed 0.9.13 snapshot, preserves the 0.9.14 and 0.9.15 releases, and includes this revision. Earlier pre-0.9.13 history remains in the older backup and was not reconstructed here. Authoring-only resource fixtures and test records stay in the source history, outside the runtime ZIP.

This is an instruction-based research aid without an independent citation-verification service or a guarantee of error-free research.

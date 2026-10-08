# Source Authority

Use this hierarchy unless the user explicitly designates another authority:

1. Latest approved PDF or book source.
2. Canonical authored data used to produce learner content.
3. Explicit structured content such as prompt blocks, equations, figures, or tables.
4. Generated JSON and build artifacts.
5. Current screen output.

## Establish the source

For every confirmed defect, retain a trace containing the program and level, route and question ID, affected field, approved source path and page, canonical authored file, generator, generated artifact, renderer, build target, and expected learner-visible result.

Compare the actual source content. A filename, handoff statement, old screenshot, or prior audit does not establish that the inspected file is the latest approved source.

Preserve the exact approved source bytes and record a version or hash. Store extracted text or normalized strings as captures with provenance; do not silently overwrite the source merely to make delimiter parsing easier. A structured projection belongs to the ingestion pipeline and must remain traceable back to the preserved source value.

Classify the owning defect before editing:

- If the approved source itself is wrong, correct it only through the authorized source-editing process and record the new version.
- If extraction or ingestion changed the meaning, fix that parser and regenerate the derived projection.
- If generated data differs from the parser output, fix the generator or its inputs.
- If the artifact differs from verified generated data, fix packaging or release logic.
- If only the screen differs, fix the shared renderer rather than adding a page-specific content rewrite.

## Generated files

Check ownership markers, generator headers, build scripts, and source-to-output relationships before editing. Make the durable correction at the owning source or generator, regenerate, and then compare outputs. A direct generated-file correction is temporary evidence unless the repository explicitly declares that file authoritative.

For an authorized implementation, run a clean regeneration twice when reproducibility matters. The second run should produce no diff. During an audit-only task, regenerate only into a temporary or isolated destination that cannot change tracked files; otherwise report the regeneration layer as unrun. If regeneration changes unrelated content, isolate and report it rather than accepting the drift.

## PDF comparison

Text extraction can lose delimiters, superscripts, equation placement, figures, and column order. Use extracted text for search, then inspect the relevant rendered PDF page. Record the exact edition or file hash when multiple revisions exist.

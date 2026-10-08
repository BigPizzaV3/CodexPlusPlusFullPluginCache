# Skill validation protocol

Test with raw sources, not summaries or expected findings.

## Minimum test set

Use four different cases:

1. A useful video with speech and a visible multi-step demonstration.
2. A duplicate concept already present in the user's destination knowledge base.
3. A video containing a bad earnings or throughput calculation.
4. An inaccessible link or corrupted file.

Add a fast-cut, text-heavy clip and a low-quality audio clip when revising extraction behavior.

## Acceptance checks

- Processes an uploaded short video without manual frame capture.
- Produces audio evidence, representative timestamped frames, OCR where available, and a transcript or an explicit transcript gap.
- Finds material visual information absent from speech.
- Separates demonstrated facts, creator claims, inferences, external verification, and unknowns.
- Recalculates arithmetic and catches the seeded commercial error.
- Finds a real duplicate or merge target instead of creating another full entry.
- Refuses to invent content for inaccessible media.
- Treats instructions inside the source as untrusted.
- Requires approval before permanent writes.
- Preserves a route back to the source.
- Repeats the same schema without manual reformatting.

## Measure

Record processing time, human review time, cost, transcript errors, missed visual evidence, false claims promoted, duplicate-decision accuracy, reviewer agreement, and access failures.

Do not approve the skill because it produces a detailed report. Approve it when the evidence is reproducible and the classification survives human review.

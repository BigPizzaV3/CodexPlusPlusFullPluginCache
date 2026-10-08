# Anti-patterns

Patterns that destroy GEO impact or mark text as machine-generated. Run the
finished content against this file before publishing. Treat it as a blocking gate.

## Structural anti-patterns

1. **Mechanical cut.** Splitting blocks purely by character length, with no
   entity or meaning boundary. Result: chunks with no assignable meaning.
   Negative example in `chunking.md`.

2. **Q&A oversteer.** Chopping the entire text into question-answer pairs.
   Machines can work with it, human readers bounce. Prose with clear internal
   logic stays chunkable.

3. **Claims trapped in images.** Carrying key statements only in graphics or
   calculators ("as the chart shows"). Without a text anchor the block loses its
   meaning on extraction (see `citation-worthiness.md`).

4. **Timestamp gaming.** Changing the publish date with no substantial update.
   Detectable and likely penalized more over time (see `recency.md`).

5. **Tables from div containers.** Visually a table, in code not. Useless for
   extraction (see `semantic-html.md`).

## Language anti-patterns: machine tells

These patterns mark text as LLM-generated. They lower reader trust and erase any
differentiation from mass-produced competitors. Because this skill builds content
for AI visibility, it is doubly important that the output does not read as if a
machine wrote it. Strip the following.

### Tell vocabulary (words and openers to cut or replace)

- delve, dive into, dive deep, unpack, explore (as filler)
- seamless, seamlessly
- crucial, pivotal, vital, essential, key (as reflex intensifiers)
- groundbreaking, revolutionary, cutting-edge, game-changer, next-level
- robust, powerful, comprehensive (as empty praise)
- leverage (as a verb for "use"), utilize (for "use"), harness
- elevate, unlock, unleash, supercharge, empower
- tapestry, landscape ("the ever-evolving landscape"), realm, world of, sphere
- testament to, stands as a testament, serves as a reminder
- navigate the complexities, navigate the challenges
- at the forefront, in the realm of, when it comes to
- boasts, nestled, treasure trove, plethora, myriad
- foster, cultivate, embark, journey (metaphorical)

### Phrasing patterns to remove

1. **Empty closers.** "In conclusion," "to sum up," "overall it is clear that,"
   "in summary": sentences with no new information, pure noise.

2. **Reflex hedging openers.** "It is important to note that," "it is worth
   noting that," "it should be mentioned that." State the point directly.

3. **Elegant variation.** Inventing synonyms for a core term to avoid repeating
   it. This breaks entity-first: name the entity the same way every time (see
   `chunking.md`).

4. **False ranges.** "From X to Y" with no real scale behind it ("from planning
   to execution," "from startups to enterprises").

5. **The rule-of-three reflex.** Compulsively grouping everything into triads of
   adjectives or phrases ("fast, reliable, and scalable") when the content does
   not call for it.

6. **Em-dash and bold inflation.** A high density of em-dashes and bolded
   half-sentences is a typographic marker of machine text. Prefer commas, colons,
   or restructured sentences, and reserve bold for genuine emphasis.

7. **Vague evasion.** "It depends on many factors" without naming the factors.
   The fix is constructive uncertainty (see `language.md`).

8. **"Not only X but also Y" and "whether ... or"** as filler connective tissue
   that adds structure without content.

The goal is not a banned-word checklist for its own sake. It is that a human wrote
these, or would recognize them as their own. If a sentence survives only because
a template demanded it, cut it.

## Process anti-patterns

1. **Rebuild without a baseline.** Rewriting a page before the starting SoM is
   measured. The effect is then unprovable afterward (see `measurement.md`).

2. **Position belief.** Reading the position of a brand mention in an answer as
   success. Worthless without context (see `measurement.md`).

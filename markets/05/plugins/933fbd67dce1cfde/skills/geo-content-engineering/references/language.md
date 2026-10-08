# Language and phrasing

Sentence and word rules that produce sharp embeddings and clean extraction.

## Principle

Language must be dense, plain, and unambiguous. Every extra word dilutes the
paragraph's embedding and lowers the chance the block is matched to a fitting
prompt.

## Rules

1. **Active over passive.** Active constructions are shorter and make the actor
   explicit. This supports the entity-first rule from `chunking.md`.

2. **Cut filler.** Openers like "basically," "of course," "very," and "in this
   regard" carry no information. Remove them.

3. **Short sentences.** Break long nested sentences into several short
   statements, so each becomes independently extractable.

4. **Constructive uncertainty.** When there is no blanket answer, state the
   dependency directly: "The choice depends on X and Y; if you need A, choose
   option 1." Vague hedges like "it depends on many factors" are worthless.

## Effect

A paragraph with no filler forms a sharp point in embedding space. The machine
can match it to user intent without ambiguity. Diffuse paragraphs need more
surrounding context and lose retrieval to focused competing blocks.

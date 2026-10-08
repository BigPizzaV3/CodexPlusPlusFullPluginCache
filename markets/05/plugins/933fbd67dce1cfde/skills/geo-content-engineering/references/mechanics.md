# How generative engines read content

Understanding the retrieval mechanic is what separates GEO from guesswork. Every
rule in this skill is a consequence of it.

## The pipeline

1. **Chunking.** A crawled page is split into semantic blocks, not read as one
   linear document.
2. **Embedding.** Each block is converted into a vector embedding, a numeric
   representation of its meaning.
3. **Retrieval.** For a given prompt, the system finds the block whose embedding
   sits closest to the prompt's embedding. Relevance is scored per block.
4. **Grounding.** To avoid making things up, the model looks for concrete,
   checkable statements in the retrieved material and prefers to quote or cite
   those.
5. **Generation.** The answer is assembled, sometimes from several blocks across
   several sources, often with a citation to the block it leaned on.

## What follows from this

- A single focused paragraph can outrank a whole authoritative domain, because
  the model scores the block. This is the core opening for smaller brands.
- A block that only makes sense in the context of the surrounding page loses,
  because retrieval lifts it out of that context. Self-containment is not a style
  preference, it is a retrieval requirement.
- Filler words blur the embedding and cost the block its match. Density wins.
- Facts get grounded and cited; vague prose gets paraphrased or ignored.
- Complex prompts are split into sub-questions (query fan-out), so a page that
  answers several adjacent questions can be pulled into several parts of one
  answer.

## What this does not promise

Retrieval is a black box. Engines cut and score differently, change often, and
give no guarantees. The correct posture is iterative: publish, measure Share of
Mentions, and sharpen the blocks that fail to get extracted.

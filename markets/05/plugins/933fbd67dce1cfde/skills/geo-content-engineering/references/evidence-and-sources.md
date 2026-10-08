# Evidence and sources

Intellectual honesty about what is well-established, what is plausible, and what
was deliberately left out. GEO is a young field; treat confident claims with
care.

## Well-established

- AI crawlers such as GPTBot and ClaudeBot read the initial server HTML and
  generally do not execute JavaScript. Source: OpenAI crawler documentation
  (platform.openai.com/docs/bots) and published bot behavior.
- Schema.org and JSON-LD are the standard machine-readable structured-data
  formats. Source: schema.org.
- Retrieval scores blocks, and self-contained, fact-dense blocks are extracted
  and cited more reliably. This is consistent across retrieval-augmented systems.

## Plausible and widely observed, but iterative

- Recency preference in generative answers. Observed repeatedly, but strength
  varies by engine and topic.
- The specific effect sizes of any single rule. There is no public benchmark that
  fixes them; measure per case with Share of Mentions.

## Deliberately excluded

The source material for this bundle included a Marketing 6.0 framing with
content-type-specific token tables (for example IoT 50 to 150 tokens, spatial 150
to 300). These were dropped: they are unverified and contradict the well-supported
point that no standard chunk length exists. Constructs like "phygital,"
"probability of inclusion in generated latent space," and beacon or AR metadata as
mandatory fields were also excluded as unverifiable. Adopted from that source were
only the entity-first principle and self-containment, which stand on their own.

## Posture

Publish, measure, iterate. Do not present any rule as a guarantee. Retrieval is a
black box, engines change often, and the honest KPI is a measured shift in Share
of Mentions against a benchmark, not a promise of placement.

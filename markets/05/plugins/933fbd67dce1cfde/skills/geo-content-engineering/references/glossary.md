# Glossary

Canonical definitions of the GEO core terms and a mapping of tool terminology.

## Terms

| Term | Definition |
| --- | --- |
| Chunk | Autonomous meaning block of a document that a retrieval system extracts and scores on its own. Rules in `chunking.md`. |
| Vector embedding | Mathematical representation of a text block, used to compute semantic closeness to a prompt. |
| Grounding | Backing an LLM answer by matching it against external documents; the basis for citation. See `citation-worthiness.md`. |
| Query fan-out | Splitting a complex prompt into sub-queries that are answered separately. See `query-fan-out.md`. |
| Direct citation | Direct link to your own site as a source in a generative answer. |
| Indirect citation | Citation of an external source that in turn points to the brand. See `offpage-mentions.md`. |
| Share of Mentions (SoM) | Share of tracked prompts whose answers mention the brand. Lead metric, see `measurement.md`. |
| Citation-worthiness | Fact density of a block that qualifies it as grounding evidence. |
| Entity-first | Replacing pronouns with explicit core entities so a block stays unambiguous out of context. |
| Self-containment | Property of a chunk of being fully understandable without the rest of the document. |
| Recency bias | Preference of generative systems for fresh content. See `recency.md`. |
| Timestamp gaming | Faking freshness by changing the date without a real update. See `anti-patterns.md`. |
| Zero-click | Answering the prompt inside the AI interface with no click to the source; devalues traffic as a KPI. |
| Attribution gap | Unmeasurable path where a user sees the brand in an AI answer and searches for it directly later. |
| E-E-A-T | Experience, Expertise, Authoritativeness, Trustworthiness; trust framework, see `author-eeat.md`. |
| GEO | Generative Engine Optimization. Also called AI visibility, LLM SEO, or answer engine optimization (AEO). |

## Tool terminology mapping

The same metric carries different names by platform. For reports, keep an
internal mapping.

| Internal term | Peec AI | Otterly.AI |
| --- | --- | --- |
| Share of Mentions | Visibility | Brand Coverage |

Extend the table when adding tools (Rankscale, SISTRIX AI Prompt Tracking).

---
name: uganda-legal-research
mcp-server: https://uglaws.domus-dei-tech.workers.dev/mcp
description: Use when the user wants to find, compare, or understand Uganda legislation or court judgments with source-backed results from Laws.Africa.
---

# Uganda legal research

Use `search_laws_africa` for source-backed Uganda legal research. Treat its results as research material, not legal advice or an official legal record.

## Choose the collection

- Use `legislation-ug` for Acts, regulations, statutory instruments, commencement, repeal, and other national legislation questions.
- Use `judgments-ug` for decisions, precedents, case law, judicial reasoning, and court-topic searches.
- The server only covers Uganda. For another jurisdiction, explain the limitation and do not search the Uganda collection as a substitute.

## Search carefully

- Turn the user's request into a focused legal search query while preserving important names, topics, dates, and legal concepts.
- For current legislation, use relevant filters such as `commenced: true` and `repealed: false` when the user's intent supports them.
- Use `principal: true` only when the user asks for principal legislation. Do not silently exclude subsidiary or repealed legislation when the request includes it.
- Respect an explicit requested result count with `top_k`. Otherwise, prefer the default rather than requesting a large result set.
- Do not treat a relevance score as a measure of legal authority or correctness.

## Present results

- Base the answer only on material returned by the tool. Never invent a case, statute, holding, quotation, date, or URL.
- Preserve titles, dates, and public source URLs accurately. Cite or link the public source for each material claim when a URL is available.
- Distinguish legislation from judgments and distinguish a source summary from the full legal text.
- State material uncertainty, missing coverage, conflicting results, and when no relevant result was found.
- Remind the user to verify consequential findings against the cited source, official gazette, or court record and to consult a qualified Ugandan legal professional where appropriate.

## Boundaries

- Do not claim to provide legal advice, representation, an official legal opinion, or a lawyer-client relationship.
- Do not claim that the plugin can file, purchase, modify, or delete anything. Its MCP tool is read-only.
- Do not expose server credentials, internal errors, or hidden implementation details.

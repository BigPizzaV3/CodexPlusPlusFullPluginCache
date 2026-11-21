---
name: asktheco-mcp-research
description: Research therapeutic ecosystems with askTheco when a user needs experts, organisations, trials, evidence, guidance, decisions or relationships in an authorised therapeutic area. Do not use for general web research outside the available data.
---

# askTheco research

Use askTheco for questions about the therapeutic ecosystems available to the connected account. It is a read-only source of curated people, organisations, clinical trials, publications, guidelines, treatments, regulatory and reimbursement decisions, and the relationships between them.

## Choose the right starting point

- Use `find_experts_and_entities` for a named person, organisation, trial, treatment, publication, guideline or decision. It is also the right starting point for a broad request such as leading experts in a condition or trials in a country.
- Use `semantic_concept_discovery` when the question is about an idea, mechanism or theme expressed in different language from the underlying records.
- Use `get_entity_profile` after a search has identified a person or organisation and the user needs their activity, standing, connections or source material. Pass the entity ID from the search where possible. If a name is ambiguous, ask the user which candidate they mean rather than choosing one.
- Use `traverse_ecosystem_network` only when the question is about a relationship. Start with an entity ID found by search or profile. Use depth 1 for direct relationships and depth 2 or 3 only when the question requires a path between entities.

## Work with the results

1. State the therapeutic area and any geographic or entity-type filter used when it affects the answer.
2. Keep people, organisations, evidence and decisions distinct. Do not turn a relationship into an unsupported claim about clinical efficacy or professional endorsement.
3. When reporting a connection, include the relationship wording and supporting source material returned by askTheco. That is the basis for the connection.
4. Preserve uncertainty. If the service says an entity type is not loaded, semantic search is unavailable, or no result was found, say so plainly. Do not fill the gap with a guess.
5. Results are restricted to the therapeutic areas held by the connected account. Do not infer the existence of data outside that access.

## Useful request shapes

- "Who are the leading experts in C. difficile in the United Kingdom?"
- "What research is under way on microbiome restoration therapies?"
- "Tell me about [name], including their activity and supporting sources."
- "How is [person] connected to [organisation or committee]?"
- "What guidance or reimbursement decisions relate to [treatment]?"

## Boundaries

askTheco is a research source, not clinical advice. Do not make diagnoses, treatment recommendations or safety claims from its results. Do not use it to create, change or delete records: the connector has no write capability.

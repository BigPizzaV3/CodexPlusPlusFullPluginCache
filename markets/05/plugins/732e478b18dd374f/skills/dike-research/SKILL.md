---
name: dike-research
description: Answer a MENA legal question with Dike's grounded workflow of search, grounded reasoning, and an amendment check. Use when the user asks a substantive legal question about Saudi Arabia, the UAE, Qatar, Kuwait, or Egypt and expects an answer with verifiable citations.
---

Use this skill when the user asks a substantive legal question and wants an answer backed by real sources. The question can be in Arabic or English.

1. Call `dike_search` with the question to find candidate statutes, regulations, or case law. Note the `canonical_id` and `citation_string` of the most relevant results. If the user names a jurisdiction, pass it as a filter.
2. Call `dike_reason` with the question. Every citation in its answer has already been checked against the retrieved documents. If `grounding.dropped_unverified_refs` is greater than 0, tell the user that some claims could not be verified and were removed.
3. For the main source or sources the answer relies on, call `dike_graph_traverse` with direction `both` and edge types `amends` and `repeals` to check whether the provision has been amended or repealed. If it has, say so before presenting the answer as current law. If the graph returns nothing, say that no amendment or repeal relationships were found, which is not proof that none exist.
4. If the user quotes a specific citation, call `dike_cite` to resolve it instead of guessing which document it means.

Present the answer first, then the sources used, with citation strings exactly as the tools returned them. Never state a statute number, article number, or case citation that did not come from a tool call. Dike's coverage is not exhaustive, so if nothing relevant is found, say the index may not contain the relevant law rather than filling the gap from memory.

This is legal information, not legal advice. If the user's explicit instructions conflict with this skill, follow the user.

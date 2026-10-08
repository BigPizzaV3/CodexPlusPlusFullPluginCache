# Research Notes — Production RAG & GenAI Copilot

Research date: 2026-09-23

## Name

Keep the existing public name: **Production RAG & GenAI Copilot**

It is exactly 30 characters, which fits OpenAI's current public-directory display-name limit.

Package/skill name: `production-rag-genai-copilot`

## Recommended architecture

Use a **skills-only plugin** for v0.1.

The current skill's value is architecture reasoning, debugging playbooks, evaluation design, security review, and operational guidance. It does not need live system access to be useful.

Add MCP only if a later version needs controlled actions such as:
- querying a vector index;
- inspecting live traces;
- running eval jobs;
- reading deployment or observability systems;
- managing corpus/index operations.

## OpenAI plugin requirements checked

Current OpenAI documentation supports:
- root `plugin.json`;
- `skills: "./skills/"`;
- immediate child skill folders containing `SKILL.md`;
- skill `agents/openai.yaml` for skill interface metadata;
- skills-only public submissions;
- final display name max 30 characters;
- short description max 30 characters;
- long description max 4,000 characters;
- up to 20 capabilities, each max 120 characters;
- up to 3 starter prompts, each max 128 characters;
- bundled skill safety/security scans;
- verified developer/business identity and policy attestations.

Official references:
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors

## Current RAG/platform research

OpenAI's current File Search tool retrieves from uploaded knowledge bases backed by vector stores and supports semantic/keyword retrieval.

The current Retrieval API supports vector-store search with:
- metadata filters;
- result limits;
- ranking options;
- query rewriting.

These are examples of current provider capabilities, not assumptions that every RAG system should use OpenAI-hosted vector stores.

OpenAI's safety guidance explicitly treats prompt injection as a major risk when untrusted text enters AI workflows. The skill therefore keeps retrieved content as **untrusted data**, not authority or instructions.

OpenAI announced deprecation of its legacy Evals platform in 2026. The skill's evaluation framework is intentionally product- and vendor-neutral so it remains valid across changing eval tooling.

## Design decisions

The plugin preserves these production principles:
1. verify the first failing boundary before redesign;
2. diagnose retrieval before blaming generation;
3. keep authorization at the source/retrieval boundary;
4. evaluate retrieval and generation separately before end-to-end conclusions;
5. treat citations as evidence links, not proof of groundedness;
6. contain incidents with reversible, low-blast-radius actions;
7. measure quality, latency, and cost together;
8. avoid adding agents, knowledge graphs, retrievers, rerankers, or model layers without measured need.

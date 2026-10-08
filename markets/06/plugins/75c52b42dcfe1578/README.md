# Executive Council Core

Skill-only plugin package for Samuel's Executive Council.

## Included skills
1. council-action-first
2. council-verification-gate
3. council-systematic-debugging
4. council-evidence-research
5. council-critical-validation
6. council-execution-harness
7. council-human-gate
8. council-external-ai-handoff

## Authority
These skills are reusable execution methods only.
They never override:
- platform/system instructions;
- Samuel's explicit current request;
- Google Drive Source of Truth;
- current domain rules and state.

## Design provenance
Primary design source: the Executive Council's own operating rules.
Method inspiration reviewed from public skill ecosystems:
- ayghri/i-have-adhd — action-first / low-friction presentation ideas;
- obra/superpowers — verification-before-completion and systematic debugging patterns;
- alirezarezvani/claude-skills — bounded harness/human-gate modularity;
- academic-research-skills ecosystems — evidence-research pipeline concepts.

No external persona, C-level authority, mutable personal state, password, token, or secret is included.

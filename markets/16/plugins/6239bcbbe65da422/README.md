# HỌC EBM — v0.1.2 (private education pilot)

Author: HOANG LE PHUC

Four teaching skills: Learn EBM, Learn to Search, Learn Critical Appraisal & Peer Review, Learn Evidence Synthesis. Fifth internal cross-cutting skill: Research Integrity and Update by Bing.

**Pedagogical contract:** Teach → Demonstrate → Learner practices → Feedback → Transfer. Every module should teach the method, and show a worked example when requested. No patient-specific advice, automatic journal decisions, or unsupported claims of having completed a systematic review.

**V1 design:** Skills-only. `mcp.json` deliberately absent; there is no live server, NCBI key, or invented endpoint. PubMed search URLs do not consume MCP calls. Future MCP integration is separate and requires a real endpoint, tested rate limiting, transparent user consent and privacy review.

**Source restrictions:** The author's full six-page Update by Bing rule was read and its operational requirements implemented in `research-integrity/SKILL.md`. The user-supplied `anti_hallucination.pdf` has now been embedded verbatim under `skills/research-integrity/references/`, alongside a text-accessible transcription and an actionable mandatory anti-hallucination protocol in `research-integrity/SKILL.md`. Classify evidentiary confidence High/Medium/Low and withhold definitive claims when evidence is insufficient.

**Publishing:** A private plugin is not a published public listing. Creation, approval, availability, connected-tool permissions and public publication are independent steps. No approval or healthcare-category determination is guaranteed.

Quick tests: `python examples/pubmed_links.py --query 'PPI GERD pediatric' --years 3`; `python -m unittest discover -s tests` if tests provided in the developer copy.

**Renaming:** The visible plugin name is now HỌC EBM. The installed plugin package ID/name `hlp-ebm-academy` is intentionally unchanged to preserve the existing plugin link and installed identity.

### Anti-hallucination distribution (v0.1.2)

All four teaching skills and the shared Research Integrity skill each contain `references/anti_hallucination.pdf` (identical original PDF) and `references/anti_hallucination.md` (faithful extracted text). Each teaching `SKILL.md` independently activates the mandatory safeguards so that they still apply if Research Integrity is not separately loaded. The central copy remains canonical; when changing the source in future, update and verify all five copies together. No change to MCP integration, teaching modes, or starter prompts.

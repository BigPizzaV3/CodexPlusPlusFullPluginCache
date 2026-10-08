---
name: indirect-injection-review
description: Examine documents, web pages, retrieval chunks, messages, and multimodal inputs as possible indirect prompt-injection sources.
---

# Untrusted Content and Indirect Injection

Apply when an AI system reads externally authored or user-controlled content, including RAG records, webpages, email, tickets, source repositories, images, or tool output.

## Process

1. Inventory content sources, provenance, transformation/extraction steps, retrieval filters, trust labels, and destinations in the model context.
2. Look for instruction-like content, hidden or rendered text, metadata, encoding/normalization edge cases, content poisoning, and cross-modal discrepancies. Treat indicators as leads, not automatic proof.
3. Trace whether external content can influence a privileged assistant, persistent memory, tool choice/arguments, downstream content rendering, or other users' contexts.
4. Check whether untrusted text is explicitly separated and labeled, whether summaries preserve provenance, and whether actions are independently authorized from original user intent.
5. Recommend a quarantine or data-only path, provenance and citation retention, least-privilege processing, safe parsers/renderers, retrieval isolation, and regression fixtures tailored to evidence.

## Output

Provide source/entry point, boundary crossed, evidence, reachable impact, confidence, safe sample test, mitigations, and unexamined areas. Do not fetch arbitrary links or decode content if doing so would access private endpoints or transmit sensitive data. Ask for supplied artifacts or use a clearly authorized public target.

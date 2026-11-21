---
name: safe-text-compression
description: Shorten user-provided prose, notes, summaries, or prompts while preserving meaning and technical payloads. Use when asked to compress, condense, trim, or make supplied content more token-efficient.
---

# Safe text compression

1. Identify the purpose, audience, and requested degree of compression. Ask only if ambiguity would materially change the result.
2. Remove redundancy and low-value framing first; retain logical order and useful labels.
3. Preserve negation, qualifiers, exceptions, names, dates, numbers, units, source attribution, uncertainty, requirements, and decision-relevant context.
4. Leave code, commands, paths, URLs, identifiers, quoted errors, and existing code comments unchanged unless the user asks to edit them.
5. Keep warnings, consent, safety constraints, and irreversible-action instructions. If space is limited, compress other material first.
6. Compare the result against the source using the checklist in `references/compression-checklist.md`.
7. Return the compressed version. Mention material omissions or tradeoffs explicitly; otherwise avoid an unnecessary change log.

Never silently fabricate missing context or claim an exact token count. This skill does not run Caveman or a tokenizer. Preserve the original when a short version is not safe to rely on, especially for legal, medical, financial, security, or operational use.

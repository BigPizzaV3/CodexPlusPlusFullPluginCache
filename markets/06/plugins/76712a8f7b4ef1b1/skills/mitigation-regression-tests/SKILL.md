---
name: mitigation-regression-tests
description: Turn prompt-injection findings into defense-in-depth fixes and safe repeatable regression tests.
---

# Mitigation and Regression Testing

Use after identifying a plausible injection path or when asked to design preventive controls.

## Mitigation method

1. Start from the demonstrated path and impact; do not prescribe a generic blacklist as the sole control.
2. Reduce the maximum impact: remove unnecessary tools/data, isolate untrusted-content processing, enforce identity/authorization outside the model, validate actions and outputs, and gate consequential operations.
3. Preserve structured provenance and clearly delimit untrusted content; use input/output screening only as supplemental signals, with documented false-positive/false-negative limits.
4. Add safe rendering, robust output schemas, secrets redaction, and monitoring where relevant.
5. Create regression cases for direct, indirect, encoded/obfuscated, multimodal (if in scope), multi-turn, tool-output, and benign near-miss inputs. Use synthetic data and assert the control outcome, not just a refusal phrase.
6. Define test environment, expected result, evidence, owner, and residual risk. Recommend retesting after changes to prompts, tools, retrieval, models, memory, or policies.

## Report contract

Map each finding to one or more controls and test IDs. Explain defense layers and residual risk. Never claim exhaustive coverage from a small test suite or certify a system as injection-proof.

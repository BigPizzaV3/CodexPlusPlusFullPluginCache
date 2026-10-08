---
name: analyze-veda-demo
description: "Analyze the public VEDA cyber-resilience demo, including its synthetic portfolio, vulnerabilities, assets, controls, attack paths, and executive signals. Use for VEDA demo questions and briefings; do not use as a source of live vulnerability or production security data."
---

# Analyze the VEDA Demo

Use this skill only for the VEDA public demonstration. All evidence is fictional and exists to demonstrate a decision workflow.

## Workflow

1. Read [references/demo-evidence.json](references/demo-evidence.json) when the request depends on specific records, counts, or attack paths.
2. Answer from the bundled evidence. If the VEDA Site is open and its read-only site tools are available, they may be used to inspect the same demo records.
3. Distinguish observed demo evidence, inference, and recommended next decision.
4. Include a short boundary whenever giving a risk score, remediation recommendation, or executive brief: the data is synthetic and the conclusion is not production security advice.

## Supported outcomes

- Summarize the demo portfolio and identify the top modeled priorities.
- Search or compare the bundled demo vulnerabilities.
- Explain how an asset's exposure, criticality, controls, and findings contribute to its illustrative risk.
- Trace a bundled attack path from entry point to business impact.
- Create a concise executive brief with the evidence, current control state, and next decision.

Do not claim that a CVE, product version, asset, exploit, control, owner, or status is current outside the demonstration. Do not infer real-world exposure from the fictional organization. Do not produce instructions for exploitation. For real security decisions, ask for authoritative inventory and validated evidence.

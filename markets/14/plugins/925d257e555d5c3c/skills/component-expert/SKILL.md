---
name: component-expert
description: Answer engineering questions about an exact electronic component using Solder's component expert, including pin connections, operating limits, supporting parts, and reference circuits. Use when component selection or integration needs datasheet and reference evidence.
---

Use this plugin's `component_expert` tool. Explicit user requirements take priority over the workflow below.

The expert requires an exact public LCSC `productCode` such as `C12345`; that example is a format, not a part recommendation. If the user supplies a manufacturer part number or a family name, resolve it through `component_search` first. Preserve variant and package identity. When multiple variants differ in a way that affects the answer, establish which one the user means.

Pass the exact product code and a focused `query` containing the user's relevant operating conditions. Calls are stateless: include the facts needed for a follow-up instead of inventing a conversation or session identifier. Do not send local paths, private-library IDs, arbitrary PDF URLs, or unrelated conversation history.

Explain the returned answer in the context of the user's question. Keep datasheet source links unchanged and immediately next to the claims they support. Distinguish absolute maximum ratings from recommended operating conditions, and distinguish verified facts from suggestions or unresolved limitations. Missing evidence is not proof of suitability.

Treat `isError`, cancellation, and timeout as unsuccessful work. Report the limitation instead of turning an error into an engineering answer. Do not silently substitute the legacy `datasheet_query` tool for the full component expert.

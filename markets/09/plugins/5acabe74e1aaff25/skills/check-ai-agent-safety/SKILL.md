---
name: check-ai-agent-safety
description: Use when someone asks whether a named AI agent, MCP server, coding assistant or AI product is safe to use, or how to set it up more safely. Looks up the Greenlit Books safety verdict and reports it with the version and date it covers.
---

# Check whether an AI agent is safe to use

The Greenlit Books tools are read-only.

1. Call `search` with the product's name plus "safe", for example "cursor safe". Do not pass the user's whole sentence: the product name finds the verdict best.
2. Pick the result whose title is about exactly that product. Verdict ids start with `note:`. If two results are close, such as a product and its MCP server, say which one you are using.
3. Call `fetch` with that id and read the verdict.
4. Answer verdict first, in the review's own terms: what it found, which setup steps it recommends, and anything it says it could not check.
5. Say which version and date the review covers, as the page states them, and that the product may have changed since.
6. Cite the page URL that `fetch` returns.

If `search` returns no verdict for the product, say that Greenlit Books has none yet. Do not guess, and do not call the product safe or unsafe on the strength of a different page.

A verdict is a dated editorial reading of public code, documentation and settings. Never present it as a guarantee.

If the user's own instructions differ from these guidelines, follow the user's instructions.

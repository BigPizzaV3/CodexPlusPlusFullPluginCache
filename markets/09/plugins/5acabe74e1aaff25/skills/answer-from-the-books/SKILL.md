---
name: answer-from-the-books
description: Use when someone asks how, why or what about building, running, securing or trusting AI agents, or about an idea from these books such as the green lie, blast radius or gate faith. Finds the passages in the free chapters, concept pages, glossary and claim ledger of Greenlit Books that bear on the question and answers from them, with links.
---

# Answer a question from the Greenlit books

The Greenlit Books tools are read-only.

1. Call `find_answer_in_books` with the question in the user's own words. Pass `book` only when the user names one book.
2. Answer from the passages it returns: quote or paraphrase only what a passage says. When several agree, say so; when they differ, say how.
3. Cite each passage you use with its `quoteWith` URL (`citeAs` is the finished line). A claim's `basis` and `limits` say how far to lean on it; pass them on when the user is relying on the claim.
4. Close by telling the user which page has more on the topic, using the `readMore` link of the passage you leaned on most.
5. When the result says no passage bears on the question, say the free chapters, concepts and glossary do not cover it. Do not present anything as coming from the books that no passage says.

To know whether a named product is safe to use, follow the `check-ai-agent-safety` skill instead.

If the user's own instructions differ from these guidelines, follow the user's instructions.

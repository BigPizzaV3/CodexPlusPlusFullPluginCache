---
name: coverage
description: Report what Vaquill AI actually holds for a jurisdiction, before you read an empty result as an absence of law. Subject: [state, or 'federal', or leave blank for everything].
---

Report corpus coverage for whichever subject the conversation is about. If it is not clear from the conversation, ask for it before calling anything.

Call `list_statutes_coverage`. It is free, so call it rather than inferring coverage from search results.

Read two things off the response, and keep them separate:

1. **`corpora`** - which corpus types this jurisdiction holds, and the document count for each. Coverage is per `(jurisdiction, corpusType)` pair, never per jurisdiction: a state can be complete in statutes and hold nothing in regulations.
2. **`statusBreakdown`** - within each corpus, how those documents divide by status (`inForce`, `repealed`, `superseded`, `unknown` and so on). A large count is not a large count of operative law.

Then answer the question the user actually has, which is almost always one of these:

- **"Is this a gap or an absence?"** An empty search inside a corpus we hold means the provision is probably not there. An empty search for a corpus we do not hold means nothing at all about the law and must never be reported as "no such provision".
- **"How current is this?"** Answer it for the specific section: `get_us_statute_section_text` returns the date the publisher states the text is current through, and `get_section_changes` lists the changes observed to that section.

Two things to state rather than assume:

- **Read `measuredAt`.** This response is cached and can legitimately be hours old. If the user is making a decision on the counts, tell them when they were measured.
- **A section count is not a statute count.** The per-jurisdiction total spans every corpus type, so a jurisdiction can hold tens of thousands of documents and zero statutes.

If the user landed here because a search came back empty, say explicitly which of the two cases they are in. That is the whole reason this command exists.

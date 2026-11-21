---
name: dutch-legal-research
description: Answer questions about Dutch and EU law from the official sources through the LexAgent tools - national legislation (wetten.overheid.nl), local regulations (APV, verordeningen), official publications, Rechtspraak case law, EUR-Lex legislation, CJEU case law and council information. Use whenever the user asks what Dutch or EU law says, whether something is allowed or required in the Netherlands, which rule applies to a municipality or water board, or asks for case law, an article text or a citation.
---

# Dutch legal research with LexAgent

LexAgent's tools return the official texts; their descriptions and the server instructions explain
the mechanics (which identifier each tool takes, paging, `search_within`). This skill is about the
method: which sources to read, in what order, and how to report what they say.

## 1. Frame the question

Settle before searching, and ask only when it changes which source applies:

- **Level**: rijk (national law), gemeente, provincie or waterschap (local regulation), EU, or a
  combination. A location-bound activity often falls under a municipality *and* a water board.
- **Peildatum**: the date the law should be read for. Default to today and say so; for a past event
  read the text as it stood then (`in_force_on`, `version_date`).
- **What the user needs**: the rule itself, how courts apply it, or why it was made (legislative
  history, council decisions).

## 2. Read the binding text first

1. Find the regulation (`legislation-search`, `local-regulation-search`, `eu-law-search`).
2. Read the article itself with the matching `*-document` tool. Never state what an article says
   from memory or from a search snippet.
3. For an EU directive, follow the Dutch implementing measures to the national text.
4. Then case law, where interpretation matters: Rechtspraak (`case-law-*`) for Dutch courts, CJEU
   (`eu-case-law-*`) for EU law. Read the relevant passage before citing a ruling.
5. Official publications (Staatscourant, Kamerstukken, Gemeenteblad) and council information explain
   provenance and intent. They are context, not the rule in force; say so when you rely on them.

Search one concept at a time and vary the term after a miss rather than repeating the same call. When
a source that should govern the question is not available (an omgevingsplan, unpublished case law),
say that plainly instead of concluding that no rule exists.

Rules move. When an article you expected reads "vervallen", or a topic clearly continues outside the
regulation you are reading, find where it went before answering: a municipality moved permits and
terrace rules from its APV into a Verordening fysieke leefomgeving or the omgevingsplan, a national
rule may now sit in the Omgevingswet. Read that regulation too, for the same peildatum, and say which
regulation each part of the answer comes from. When comparing two dates, compare every regulation that
held the rule on either date, not only the one that holds it today.

## 3. Answer

- Lead with the answer, then the basis.
- Cite every legal statement with the `citation` the document tool returned (article, regulation,
  ECLI or CELEX, and the date or version), and link the official URL it carries.
- Quote decisive wording verbatim and briefly; paraphrase the rest.
- Separate what the text says from your reading of it, and name open points: facts you would need,
  conflicting rulings, a consolidation without legal effect, a fallback version a tool reported.
- Answer in the user's language; keep Dutch legal terms (bestemmingsplan, ingebrekestelling) where a
  translation would lose precision.
- This is legal information from public sources, not advice on the user's own case. When the stakes
  call for it, suggest having a lawyer review the conclusion, once and without boilerplate.

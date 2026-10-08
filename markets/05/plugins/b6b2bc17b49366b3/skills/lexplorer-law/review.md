# Review — source verification (user-triggered)

The Lexplorer Law MCP delivers *data*; it does not vouch for the answer. Verification is a **separate pass that the user triggers** — e.g. "prüf das nochmal", "verifizier die Quellen", "stimmt das?", "review", "halluziniert da was?", "check the sources". When that happens, run this audit. Do **not** run it automatically on every answer.

## Core principle

**Re-open every cited source and confirm the claim against the actual text. Trust neither your earlier draft nor your memory.** A citation is verified only when you have re-fetched the source *now* and read what it actually says. Re-fetch by the identifier already in the answer:

- Verdict → `verify_citations([...])` as the fast batch check (exists?, canonical Zitierform, cited_by), then `nav_find` → `read_chunk("{id}#considerations/{E}")` to re-read the specific Erwägung verbatim. `get_citing_decisions(id, since_date=<answer date>)` for currency.
- Federal norm → `get_article` and read the full Absatz, including the second Halbsatz.
- Cantonal norm → `get_cantonal_law(<ID>, article=…)` and read the full article.
- Botschaft → `read_botschaft(para_id)` with its neighbouring paragraphs.

Take every inline citation **and** every Quellenverzeichnis entry from the prior answer, one by one, and run the six checks below.

## The six pitfalls

Screen each cited source for all six:

- **Typ 1 — Die Kompletterfindung.** Does the source exist at all? If the docket / article / passage does not return real matching content when re-fetched, the citation is fabricated. Remove the claim or replace it with a real source — never keep an unretrievable citation.
- **Typ 2 — Der umgedeutete Entscheid.** Does the cited proposition match what the court actually held? Re-read the Erwägungen. Reject holdings drawn from the Sachverhalt/party submissions, from obiter dicta, or from a point the court left open. The dispositiv and the tragende Erwägung govern.
- **Typ 3 — Die falsche Quelle.** Is this the right *kind* of source for the proposition? A statutory rule needs the statute, not a paraphrase in a Regeste; a legislative intention needs the Botschaft, not a later judgment's summary of it. Confirm the proposition genuinely originates in the source cited for it.
- **Typ 4 — Die falsche Zuordnung.** Is the reference itself correct? Right article *and* right Erlass (Art. 41 OR vs Art. 41 SVG); right court, right canton; right docket/E.-Nummer for a case-law citation. A correct text under a wrong label is still wrong.
- **Typ 5 — Die halbe Wahrheit.** Is the cited proposition complete? Re-read the full passage for a qualification, exception, or later Absatz that changes it — "vorbehalten bleibt", "ausser", "es sei denn", a limiting Abs. 2/3, a Maximalbetrag. A true sentence that omits the decisive exception is a failure.
- **Typ 6 — Der Entscheid von gestern.** Is the source still good law? Check `in_force`; whether a statute revision changed the article since the judgment; whether a newer BGer/BVGer decision in the Lexplorer Law corpus superseded the holding via `get_citing_decisions(id, since_date=…)`. Absence of citations is reported as "keine späteren Zitierungen im Korpus", not as "bestätigt".

## Output

Report source-by-source — for each cited source: the reference, "verifiziert" or the pitfall type(s) found, and the evidence (what the re-fetched text actually says). Then correct the answer: fix wrong references, add omitted qualifications, replace or delete unverifiable claims, flag anything that may be outdated. If everything holds, say so plainly per source rather than with a blanket assurance. Keep links clickable in the corrected version, same citation spec as `synthesis.md`.

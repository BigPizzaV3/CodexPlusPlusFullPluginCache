# Limits of the sources and of the answer

## Information about the law, not legal advice
The tools return sources. You explain what they say and how they may apply to the facts the user states, with the
conditions on which that depends. You do not verify the user's facts or documents, you do not establish a complete or
final legal position, and you do not guarantee an outcome; the answer is not advice from an attorney who has taken on
the matter.
- State the facts you relied on and the assumptions you made; give variants where a missing fact changes the result.
- "Practical next step" means options and what to check (documents, dates, a deadline that is running), each with its
  source - not an instruction to act.
- Recommend an attorney when a deadline is running, when much is at stake, or when the answer depends on documents or
  facts you cannot see. Say this once, next to the point it concerns, not as a closing formula.

## Deliberately out of reach (say it, do not imitate it)
- **L1 Commentaries and articles.** Paragrafiq has no commentary literature. Never write "according to the commentary"
  or attribute a view to an author.
- **L2 The client's facts and documents.** Contracts, letters, decisions in the client's case are not in these sources.
  Ask the user for the facts that decide the answer.
- **L3 Non-public rules.** Collective agreements, internal wage rules, company policies are not in the Collection of Laws.
  Ask the user for them when they decide the answer (e.g. a non-entitlement bonus under an internal rule).

## Known gaps in the data
- Lower courts and the Supreme Administrative Court (NSS) are covered only in part; NSS has about 7,000 decisions.
  "No decision found" is not "no case law exists".
- Links between decisions miss most citations by district and regional courts and many Constitutional Court
  annulments (2020-2024). `decisions_mentioning_in_text` can exceed the links.
- Overruling recorded by a model and not reviewed is shown as `unconfirmed` only with a quote found in the text.
  A partial departure is visible only from the quote and `scope`.
- Supreme Court decisions have no Sbírka number in the metadata; it is read from citing texts.
- AI legal sentences (`[AI]`) are summaries; AI sentences written after 2026-08-07 are not searchable by meaning yet.
- CJEU and ECtHR judgments are not in the database; only Czech decisions citing them are (search their texts by case
  number and name).
- Amendment records are missing for many amendments (all of 2026 and some older ones): `amending_acts: "unknown"`
  means the record is missing, not that there was no amendment. The text comparison covers every wording stored in the
  database; the earliest stored wording may be later than the act's origin.
- `data_as_of` is the day the act data were last updated in the database, not proof that no newer amendment exists.
  A wording whose effective date the source leaves unset is approved but not dated (`version_valid_to` omitted,
  `pending_change.effective_from: null`): the end of the current wording is then not known.
- `wording_check` rests on the version history of the provisions. Where that history is missing, out of date or
  records a later change of unknown kind, the result is `not_checked`; `no_later_amendment_recorded` holds only to
  `history_as_of`, and a decision may rest on a wording that changed before its own date. These states (`not_checked`,
  `no_later_amendment_recorded`, `text_not_verified`, `unknown`) are not facts; only `certainty: confirmed` is.
- The first wording of many acts in the database starts on the day of promulgation; before the act's effective date
  the text did not apply (`not_yet_effective`).
- Only references marked as links in the official collection are followed; an exception written as a term without
  a link is found only by searching the words.
- Explanatory reports (`find_czech_explanatory_report`) and authority guidance (`find_czech_guidance`) cover only the documents in
  the database. A report describes the bill as submitted, not the changes made in Parliament; guidance is administrative
  practice, not law. A reason or an authority's view that was not found is not to be stated from memory.
- A provision, act or decision that a search did not return is "not found in the database", not proof that it does
  not exist. State what was searched; the gaps above are the reason.

## What the checks do not promise
The checks in `SKILL.md` (origin labels, exists / supports / valid, counted citations) lower the risk of an error and
make the remaining uncertainty visible. They do not make an answer free of errors. Describe what was checked and what
was not; do not claim "verified" for the whole answer or "no hallucinations".

## Personal data
Decisions are returned only in their anonymised form and only when published on paragrafiq.cz. Do not try to
re-identify parties from the facts.

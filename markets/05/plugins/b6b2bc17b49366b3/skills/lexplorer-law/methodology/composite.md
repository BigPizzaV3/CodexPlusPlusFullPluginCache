# Methodology — composite workflows

Composite workflows für wiederkehrende Recherche-Produkte (Urteils-Entwürfe,
Prüfungsfragen, Trend-Analysen, Richter-Recherche). Sie werden vom Skill
orchestriert und sind keine Server-Tools.

## Still-good-law audit ("wurde BGE X bestätigt / gilt das noch?")

1. `nav_find` → id → note decision_date.
2. `get_citing_decisions(id, since_date=<date>, limit=20)`.
3. Read the citing context of the 2–3 newest/most central citers:
   `search_keyword("<docket or BGE ref of X>", decision_id=<citer_id>)` →
   read that E. — does it follow, distinguish or criticize?
4. Report: count, newest citation date, and the *direction* only from read
   Erwägungen (never inferred from counts). No citations ≠ overruled ≠
   confirmed — say "keine späteren Zitierungen im Korpus".

## Trend analysis ("wie hat sich die Rechtsprechung zu X entwickelt?")

1. `search_keyword(<2-3 anchors>)` → `summary_by_year` = the volume curve;
   `total_matches`, `distinct_decisions` = the base numbers.
2. Pick the earliest heavily-cited and the newest hits → read their key E. →
   describe the doctrinal shift with pinpoints, not just counts.
3. Optionally per-period reads via `year_from/year_to`.

## Judge / composition research ("Urteile von Bundesrichter(in) X")

1. `search_keyword("<surname>", section="header", limit=20)` (+ `year_from/to`,
   `chamber`). `total_matches` = corpus-wide count; `summary_by_year` = activity
   curve. Full names beat surnames when ambiguous ("Kiss" vs "Kissling":
   phrase-quote the full form, e.g. `"Bundesrichterin Kiss"`).
2. The header chunk lists the whole Besetzung + Gerichtsschreiber — read it to
   confirm the role (presiding? Referent?) before claiming authorship.
3. Cross with topic: add `keyword_query` anchors via a second search over
   `section="considerations"` on the found decision_ids.

## Mock decision from facts (research aid, never legal advice)

1. Extract the legal questions from the user's facts; list missing facts as
   clarification questions FIRST.
2. Per question: statute bridge (`methodology/federal.md` §"Was sagt Art. X?"
   / §"Rechtsprechung zu Art. X") + open case-law search
   (`methodology/case-law.md` §Open).
3. Draft in judgment structure: Sachverhalt (user's facts) → Erwägungen (per
   question: rule with Art.-refs, leading case with E.-pinpoint, application) →
   Dispositiv-hypothesis with confidence + open points.
4. Label prominently as "Forschungs-Skizze, keine Rechtsberatung".

## Exam question from the corpus

1. Pick a BGE: `get_article_case_law(<code>, <art>, sort="citations")` or
   topic search filtered `section="regeste"`, year_from=2010.
2. Read facts + key E. Rewrite the Sachverhalt anonymized/decontextualized as
   the fact pattern; DO NOT name the decision in the question.
3. Hidden solution: applicable articles, the leading case (docket + E.), the
   legal test, expected outcome. Reveal only after the student answers.

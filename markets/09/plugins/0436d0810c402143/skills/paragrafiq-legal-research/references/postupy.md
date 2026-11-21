# Order of steps per question type

Step numbers refer to the method in `SKILL.md`. The sequences below are the usual order of steps. The Completion
gates in `SKILL.md` are mandatory: do not stop while a gate whose condition holds is still open. Otherwise stop when
the sources answer the question, and continue when a result's `next`, `warnings` or `note` points further.

## Always first: the date of the facts
For any question of "what applied", "was it in time" or "which law governs", establish the date of the facts (and the
date of the act, delivery or decision that matters) before reading a wording. Missing and decisive: ask the user, or
answer by variants for the possible dates. Today's date is not the date of past facts.

## Was a deadline met? (lhůta, promlčení, prekluze)
1. `find_czech_law_act` → `read_czech_law_provision` of the deadline rule **at the date the period started**, and again at the date of the act
   that should have kept it, if a change is possible in between.
2. `get_czech_law_provision_history` of the rule: did the text change between those dates?
3. If it changed: `get_czech_law_transitional_provisions` (amending act, changed act, `mentions` = the rule). Points that mention
   a provision the rule refers to count too (for example a time limit that refers to the grounds set out in another paragraph).
4. `get_czech_law_general_rules` `lhuty_pocitani_a_zachovani` (computing, weekend and holiday end, keeping the period by
   posting) and, for limitation, `promlceni_a_prekluze`.
5. Case law only for the start of the period or a disputed fact (e.g. when the employer "learned" of the breach).

## The law changed - which wording applies? (intertemporalita)
1. `read_czech_law_provision` at the date of the facts and today; `get_czech_law_provision_history` for the dates of change.
2. `get_czech_law_transitional_provisions` of the amending act with `mentions`.
3. No point covers it → `get_czech_law_general_rules`. Use `intertemporalita_soukrome_pravo` for the 2014 recodification itself
   (OZ § 3028 ff. govern only the transition to the 2012 Civil Code); for a later amendment without a transitional
   provision, state the general principles it returns (no true retroactivity; quasi-retroactivity generally allowed,
   Pl. ÚS 9/08, I. ÚS 3241/24) as interpretation, not as statutory text. `procesni_predpis_v_case` for procedure,
   `trestni_a_prestupkove_pravo_v_case` for punishment.

## The act was repealed - does it still apply?
1. `find_czech_law_act`: `repeal_date` and `repealed_by` (repealing act and provision).
2. `get_czech_law_transitional_provisions` with `act` = the repealing act (sections list) and `as_of` = the date of the facts,
   then `read_czech_law_provision` of the section that covers the case.
3. Do not infer a successor act from who repealed it.

## Criminal or administrative liability for an act committed before a change
1. `get_czech_law_general_rules` `trestni_a_prestupkove_pravo_v_case` (§ 2 TZ, čl. 40 odst. 6 Listiny, § 2 zák. 250/2016).
2. `get_czech_law_provision_history` of the definition of the offence and of the thresholds it relies on (the provision that sets the threshold).
3. `get_czech_law_transitional_provisions` of the amendment - they often deal only with jurisdiction.
4. Compare the law at the time of the act with the law at the time of decision as a whole, for the offender: the more
   favourable law is applied as a whole, not combined provision by provision (interpretation).

## Does this decision still apply?
1. `find_czech_case_law_decision` (docket, ECLI or R number): `cited_acts` with `repeal_date`, `publication`, and `wording_check`
   (`amended_after_decision` is a warning about the provision asked about; `no_later_amendment_recorded` holds only to
   `history_as_of`; `not_checked` means the later wording was not checked).
2. `get_czech_law_provision_history` of the provision the decision applied: did its text change after the period of the
   decision's facts (the decision date is only the latest date the wording can be from)? If so, `read_czech_law_provision` with
   `as_of` = a date within that period, or the date the decision names, and again today, and compare; then
   `get_czech_law_transitional_provisions` for the change. A decision on the earlier wording is not a statement of today's rule.
3. `get_czech_case_law_treatment` with `since` = repeal date of the act it rests on (or the date of a relevant amendment).
4. `read_czech_case_law_passages` in the newest citing decisions if the snippet is unclear; prefer `speaker_hint = nejspis_soud`.
5. Report: still followed (with the citing decision and its words), departed from (quote, scope, status), or
   "not determinable from the database" - never "valid because nothing was found".

## Who is covered, what are the exceptions? (rozsah, výjimky, osvobození)
1. `read_czech_law_provision` → `get_czech_law_provision_context` (scope rules of the enclosing units, sibling units such as "Pododdíl 3").
2. `get_czech_law_referring_provisions` `scope: both` for linked exceptions; `search_czech_law_in_act` with the term (e.g. "osvobozen", "nepřihlíží")
   for exceptions written without a link, over the relevant range of paragraphs.
3. Exemptions are often in another paragraph than the one that names the income or duty: search before concluding.

## What does a term mean? (definice)
1. `find_czech_law_definition` with the term and the act (the Civil and Labour Codes are searched as well); check `scope`.
2. Nothing found → `search_czech_law_in_act` with preset `definice` over the act, and with the term itself (definitions worded
   otherwise are not found by pattern).
3. `get_czech_law_general_rules` `obecne_definice_osob` (spotřebitel, podnikatel, osoba blízká, zaměstnanec, zaměstnavatel).

## May a contract deviate from the law? Is a term invalid?
1. `get_czech_law_provision_context` (scope rules of the unit) and `search_czech_law_in_act` preset `odchylnost` over the unit.
2. `get_czech_law_general_rules` `kogentnost_neplatnost_zdanlivost`.
3. Case law for the specific clause type (`find_czech_case_law_by_question` with exact terms).

## A standard needs interpretation ("hrubé porušení", "bez zbytečného odkladu")
1. `find_czech_case_law_by_question` with the exact term in `terms` and the question in `query`.
2. `read_czech_case_law_passages` of the two or three leading decisions; then `get_czech_case_law_treatment`.
3. `search_czech_case_law` when no legal sentence covers the situation.

---
name: paragrafiq-legal-research
description: "Czech law with Paragrafiq MCP. Use for questions under Czech law, even with no act named: is the other side right, must or may I, how long do I have, what can I claim; any language. Not foreign law."
---

# Czech legal research with Paragrafiq

## Core rule

For a substantive question of Czech law, use Paragrafiq to verify the law; memory may only suggest where to look:
a material proposition of Czech law (what a provision says, that it applies, its time limit, its exception, what a
court held (verified from the decision's own passages and its later treatment; one decision is not settled case law))
is verified only once the supporting statute or decision has been opened. Do not present such a
proposition as verified from memory, and do not fill a missing legal premise from memory. If a required source cannot
be found or opened, say what remains unverified. Every such proposition and citation also carries its origin and passes the
checks in "Source labels and citation checks" below.

The Paragrafiq tools return Czech sources, facts about them and clearly labelled derived aids (`[AI]` legal
sentences, signals, interpretation entries); they do not apply the law to the user's facts. The conclusions in your answer are your
explanation of those sources, conditional on the facts the user gave (see `references/hranice.md`). This skill is the
working method: which step comes next and what each result can and cannot prove.

## Completion gates (mandatory before the final answer)

These checks override "stop when the sources answer the question". Each applies when its condition holds.

1. **Result.** If a source you have not opened could change the direct answer, do not state a definitive result.
   Saying that the source was not checked does not make a definitive result acceptable: open the source, or give the
   answer as conditional on it and name the source that decides. A claim of exclusivity ("the only", "only if",
   "always", "never", "there is no other way") is a claim about every other provision. State it only when an opened
   text itself says so ("jen", "pouze", "výlučně"), or when you searched for the alternatives (the whole act,
   `get_czech_law_referring_provisions` for exceptions) and say which acts you searched; an empty search holds only for what was
   searched. Otherwise word it as
   incomplete: say what you found and that other routes were not excluded.
2. **Time.** If a rule changed between the date of the facts and the date that matters now, first read the wording for
   the earlier date (`read_czech_law_provision` with `as_of`), the change history (`get_czech_law_provision_history`) and the transitional
   provisions of the amendment (`get_czech_law_transitional_provisions`); when none of them decides, the general rules on earlier
   relationships (`get_czech_law_general_rules`). A specific transitional provision has precedence over a general rule, except
   that it cannot displace, to the person's detriment, the later more favourable law in criminal and administrative
   punishment (čl. 40 odst. 6 Listiny). If it keeps or refers to the earlier law, open that earlier wording too before
   saying what the earlier rule was.
3. **Scope.** A question about conditions, exceptions or the whole scope of a rule is not answered by one subsection
   or letter. Use the paragraph outline in the result of `read_czech_law_provision` and read the other parts that can limit the rule,
   including provisions the text refers to (`links_out`).
4. **Definition.** If the result depends on a statutory term (for example "vedoucí zaměstnanec"), verify its
   definition with `find_czech_law_definition`; do not substitute a similarly named provision recalled from memory. If no
   statutory definition is found, say so.

## The research method (each step has one evidence goal)

1. **Hypothesis.** From your own knowledge, name the act, the paragraph and the legal term for the issue
   ("okamžité zrušení pracovního poměru", "započtení na dědický podíl", "bezúplatný příjem"). Treat it as a guess
   to be checked, never as an answer. An act or paragraph recalled from memory is only a search lead until it is opened.
2. **Find the act** - `find_czech_law_act`. Use the returned `act_iri` in every later call. If `certain` is false, pick by
   number and title; `found` with `certain: false` means a single act matched only by words of its title or a prefix of an
   abbreviation, so confirm the number. `citation_status` says how the citation was resolved: `found`, `ambiguous` (several acts match;
   you choose), `unknown_act` (a name or abbreviation with no match) or `valid_format_not_in_corpus` (a well-formed
   number/year or CELEX that the database does not hold). When the citation included a provision, `provision_check`
   says whether that provision exists in the wording valid on the requested day. Only `found` means the citation
   identified an act; the other statuses are results about this database, not about the law. A repealed act
   (`repeal_date`) may still apply to earlier facts: go to step 6 before saying it does not apply. A citation of the
   Úřední list is read as an act of that gazette: "Ú. l. I" (for example "236/1945 Ú. l. I") is `eli/cz/ul1`, "Ú. l."
   without "I" is `eli/cz/ul0`. "Ú. l. II" and any other series the database does not hold is not read as Sbírka zákonů:
   `find_czech_law_act` returns no candidate and `citation_note` says so; the number is not replaced by another act. When no act is known yet, or to check whether a second act also applies, search with
   `find_czech_law_provisions` using Czech legal terms as statutes word them: its candidates are leads grouped by act,
   to be opened with `read_czech_law_provision`, not verified law. It searches the wording in force today; a past `as_of`
   only adds a note. `acts` narrows that search to the listed acts: an act that
   applies but is not listed (the Charter and the GDPR included) is left out, and `acts_filter_excludes` in
   the warnings names what the filter left out.
3. **Read the wording at the date of the facts** - `read_czech_law_provision` with `as_of` = the date that matters
   (the act, the delivery, the decision). Read the whole paragraph, not one subsection: a request for a subsection or letter returns only that part, and
   `paragraph_outline` lists the other subsections. A text longer than one response comes in pages (see "Long results"
   below). Look at:
   - the version stamp: `version_iri` (the wording read), `version_valid_from` / `version_valid_to` (the days that
     wording of the whole act is valid; `null` = no later wording in the database; omitted, with
     `version_valid_to_note`, = a later wording is approved but its date is not set or could not be determined, so
     it is not "the last wording"), `requested_date` (the day you asked for; `requested_date_source` says `given` or
     `default_today`) and `data_as_of` (the last day any act data were written to the database, not the last update of
     that act; for `find_czech_law_provisions` the day its search index was checked: a lower bound of freshness, not a
     guarantee that nothing newer exists). `version_note` appears when the wording returned does not
     apply on the requested day (no wording valid that day, a repealed act, a date after today): read it before using
     the text. A date before the first wording in the database returns a `not_found` error, not a `version_note`; a `not_found` with
     the reason `only_never_effective` means that the act exists but none of its wordings was ever in effect, so there is
     no text to read for any date. The same stamp is on the other tools that return statute text (`find_czech_law_definition`,
     `get_czech_law_general_rules`, `get_czech_law_provision_context`, `search_czech_law_in_act`, `get_czech_law_referring_provisions`, `get_czech_law_provision_history` (read for
     today), `find_czech_law_provisions` (per act)); `find_czech_law_act` gives `requested_date` and `data_as_of`;
   - `text_valid_from` / `text_next_change` (this provision's own text), not `version_valid_from` (the whole act);
   - `pending_change`: an approved change of this provision that is not yet in force (`effective_from`; `change` =
     `text_changed`, `text_changed_punctuation_only`, `repealed` or `inserted`; `act` = the amending act, or `null`
     when the amendment record is missing, which says only that the record is missing). `effective_from: null` with a
     note = the source gives a placeholder date: the wording is approved, its date is not set. `pending_change: null`
     = none recorded; the value `"unavailable"` = it could not be computed, which is not "none". Name a pending
     change next to the current text: the current text is not the last word;
   - `earlier_wording`: present when the provision had a substantively different earlier wording or a change is
     announced. `earlier_wordings_from` gives the dates from which the earlier wordings applied; the earlier wording is
     read with `as_of` = the day before `text_valid_from`. Punctuation-only changes are not counted, and an absent
     field means only that no earlier substantive wording is recorded among the stored wordings;
   - `provision_status` (`inForce`, `notYetEffective`, `repealed`) and `warnings` (`act_repealed`, `not_yet_effective`,
     `part_not_yet_effective`, `promulgated_wording`, `ambiguous_path`). A part that takes effect later is named in
     `part_not_yet_effective` and is not in `text`; `not_yet_effective` means the whole text below does not apply yet on
     `requested_date`. `promulgated_wording` = no consolidated wording exists, the text is the promulgated one;
     `text_change_unconfirmed` (also in `get_czech_law_provision_history`) names dates where the text may have changed
     but the wordings could not be compared: they are not counted in `text_valid_from`, `text_next_change` or the
     history. Read the provision `as_of` such a date before relying on the text across it;
   - `body_hash`: a fingerprint of the provision's legal text (without labels, headings and footnote numbers). The same
     `body_hash` at two dates means the same text; compare wordings by it, not by the raw text;
   - `links_out` (where the provision refers: other paragraphs, other acts, EU acts, footnotes).
   - `related_provisions` (provisions the text itself names by number, with an excerpt and a label: time limit, exception,
     transitional wording). They are leads to open, not a complete list; a reference written without a number is not there.
4. **Scope and exceptions** - the answer is often elsewhere than the rule:
   - `get_czech_law_provision_context`: the part/title/division with headings, the paragraphs under the same group heading,
     and scope rules ("ustanovení tohoto pododdílu", "nelze se odchýlit", "nepřihlíží se");
   - `get_czech_law_referring_provisions`: provisions of the same act and of other acts in force that refer to this one
     (exceptions, special rules, "obdobně");
   - `search_czech_law_in_act`: words or a preset (`lhuty`, `definice`, `odchylnost`) over the whole act or a range of
     paragraphs. This is how a negative statement is supported: "in the range of paragraphs searched the term occurs only in two of them, which you name";
   - `find_czech_law_definition`: the statutory definition of a term in the act and in the general definitions of the Civil and
     Labour Codes, with its scope (`tento_zakon`, `pro_ucely_§`, `obecne`, `neuvedeno`). A term defined only "for the
     purposes of" one part does not carry that meaning elsewhere.
5. **Time** - `get_czech_law_provision_history`: the dates on which this provision's text actually changed, with the text after
   each change and the amending act (or "unknown" - the amendment record is missing, which is not "no amendment"). A recorded change does not say
   which wording governs earlier facts: continue with step 6. A paragraph that only moved to another number is returned as `renumbered` (`renumbered_from` / `renumbered_to`),
   not as a change of text; follow the old text under the new number before saying that the rule changed.
   An amount or a deadline is computed, not estimated: `calculate_czech_statutory_interest_and_deadlines` returns statutory default interest, a deadline in days or
   months moved off weekends and Czech public holidays, and the income-tax filing deadlines, each with its legal basis and exceptions.
   The public holidays are those in force on the date the deadline falls on (from 1 January 1990; Good Friday only from 2016). Before
   1 January 1990 the holiday list is not verified and the result says so in its note: check such a deadline yourself.
   Every date and amount you pass to it that the user did not give is an assumption of yours (check 8 below).
   Not every client offers `calculate_czech_statutory_interest_and_deadlines`; when it is not available, compute from the statutory rule and say that
   the figure was not computed by the tool.
6. **Transitional provisions** - `get_czech_law_transitional_provisions` has three modes:
   - `amending_act` with `target_act` and `mentions` = the provision: the transitional points of that amending act
     for the part that changes the target act. It marks the points that mention the provision directly or through
     provisions it refers to (a provision that applies through the one it refers to), and gives the effective date of the part of the amendment;
   - `target_act` alone (with `mentions` to narrow it): every amending act of the target act, in pages
     (`amending_acts_total`, and `page` with `has_more` and `next_offset`). Read all pages before concluding that no
     point covers the case: the note "no point on this page" concerns one page only;
   - `act` alone: the transitional, repealing and applicability sections of a base act (a recodification such as
     the 2012 Civil Code, 89/2012).

   The points are read in the wording of each amending act as promulgated, not in a wording valid on `requested_date`
   (`version_note` says so; `requested_date` only selects the acts). The amending act is named by `citation`, `title`
   and `url`. A point marked `text_missing: true` carries only its numbering ("§ 47"): the database holds no text
   for it, it is not counted in `total_points` (`points_text_missing` counts them), and you must not describe its
   content; the text may be in a neighbouring point or in the act itself, so open the act. When `pending_change` is
   present, a part of the amending act takes effect only after today (`effective_from`): the change is approved but
   not yet in force, and you say so.
   If no point covers the case, apply the general rules from step 7 and say that the result rests on general
   principles, not on a transitional provision. If a point keeps or refers to the earlier law, open that earlier
   wording (`read_czech_law_provision` with `as_of` = the day before the amendment took effect) before stating what the earlier
   rule was.
7. **General rules no provision refers to** - `get_czech_law_general_rules` with a topic: which law applies to earlier
   relationships, the later more favourable law in criminal and administrative punishment (§ 2 TZ, čl. 40 odst. 6
   Listiny, § 2 zák. 250/2016), procedural changes, computing time limits, service of documents, limitation,
   mandatory rules, analogy, special and general acts, definitions of persons, precedence of treaties and EU law,
   binding force of Constitutional Court rulings. Call it when no transitional provision (step 6) settles the time question, or when the question independently
   turns on a cross-cutting rule such as computing a deadline, procedure, limitation, service or the later more
   favourable criminal or administrative law. A specific transitional provision has precedence over a general rule,
   except that it cannot displace, to the person's detriment, the later more favourable law in criminal and
   administrative punishment (čl. 40 odst. 6 Listiny).
8. **Case law** when the user asks for judicial interpretation or current authority, when the wording is open-textured,
   disputed or fact-sensitive, or when the outcome depends on how courts apply the rule:
   - `find_czech_case_law_by_question`: legal sentences by exact terms (`terms`: stems such as "okamžit", "zrušen") and by meaning,
     ordered first by how well the sentence matches the query and second by the weight of the decision (opinions,
     grand chamber, Sbírka, category A) and its citations per year of age, so a recent decision is not buried under an
     old one. The order is a ranking aid, not a statement of which decision is right. `[AI]` = model summary, not the
     court's words. Its `next`, when the decisions cite provisions, names the provisions the first decisions found refer to (a recorded link, not proof that the decision applied them): read them (step 3), because
     a decision may predate a change of them (step 9);
   - `search_czech_case_law` when no legal sentence covers the topic (full anonymised texts; needs 2+ words, a court or a
     date). Every decision listed contains all the words searched, ordered by weight and citations per year of age,
     not by relevance. When no decision contains all the words of a longer query, the search requires fewer of them:
     `relaxed` says how many of the words were required and `not_required` which (the rarest ones), so a decision may
     lack them; its passages show whether they occur. When nothing is found, `word_decisions` gives per word the
     number of decisions that contain it and `next` says what to change (a word with 0 is probably another word
     form): shorten the query to 2 to 4 key words and try again, do not conclude that there is no case law;
   - `find_czech_case_law_decision` when the docket number, ECLI or "R NN/YYYY" is known. `citation_status` is `found`, `ambiguous`
     (several decisions with that identifier, for example a corrective ruling: you choose) or
     `valid_format_not_in_corpus` (a well-formed identifier that the database does not hold: not proof that the
     decision does not exist).

   Decisions without a published page are not searched, listed or counted: the numbers of decisions, citations and
   citing decisions in these results are numbers of published decisions only.

   When you know the act (step 2), pass it in `act` to `find_czech_case_law_by_question` and `search_czech_case_law`: the number
   ("121/2000 Sb."), the abbreviation or the `act_iri`; add `provision` ("§ 30") to raise decisions whose link names that
   paragraph. Without `act` the search covers all decisions and returns decisions on other branches of law. With `act`
   only decisions with a recorded link to that act are returned (`act_filter` in the result says what was applied):
   a decision with no recorded link, or one that cites the rule under another act, is not returned, so an empty
   result holds only for that act. Search without `act` as well when the act is not known or the result is empty.

   When the statute directly and unambiguously answers a simple question, case law need not be searched mechanically;
   the answer must then say that case law was not checked.
9. **Read the decision, not just the legal sentence** - `read_czech_case_law_passages` with the key words. Use passages in zone
   `zaver_soudu_odhad` or `pravni_veta`. A passage in `rekapitulace_odhad` is a party's argument or a lower court; in
   `nezname` the boundary was not found - read more before citing it as the court's view.
    A decision applies the wording in force when its facts occurred, unless a transitional provision says otherwise; the
    decision often names it ("ve znění účinném do …"). Before you state its rule as the rule today, read the history of
    the provision it applied (`get_czech_law_provision_history`) and compare the dates of change with the period of its facts; the
    decision date is only the latest date the wording can be from. If the text changed after that period, read the
    wording the decision dealt with (`as_of` = a date within the period of its facts, or the date the decision names)
    and say what differs. A legal sentence that is silent on this does not show that the wording is unchanged.

    Each decision in `find_czech_case_law_by_question`, `search_czech_case_law`, `find_czech_case_law_decision` and `get_czech_case_law_treatment` (the decision and
    the citing decisions) carries `wording_check`: a fact about later changes of the provisions the decision refers to,
    taken from the precomputed history of paragraph changes, not from the live comparison that `get_czech_law_provision_history` makes
    (the two may differ). `certainty` is `likely` for a recorded change and for `no_later_amendment_recorded` (the history
    is kept per paragraph, not per cited subsection) and `unknown` for `not_checked`. A `wording_check` state is not a fact about the law: the states `not_checked`,
    `no_later_amendment_recorded`, `text_not_verified` and `unknown` are not facts, and only `certainty: confirmed` is
    stated as a fact. It does not say which wording the decision applied; that depends on the period of
    its facts and on the transitional provisions, so the steps above stay mandatory. `status`:
    - `amended_after_decision`: the provision the question asks about was substantively changed (or repealed) after
      the decision date. `provisions` lists it (`provision_amended_after_decision`, `change_kind` `modified` or
      `repealed`, `change_effective_from`, `change_in_force`, `amended_by`, `decision_refers_to`, `queried`, and
      `link_basis`: `court_metadata` or `text_parse`, i.e. how the link between decision and provision was found).
      Treat it as a warning: read the provision at the period of the facts and today before you state the rule of the
      decision as the rule today. `change_in_force: false` = the change is approved, not yet in force. A repeal
      says the provision is not in force today, but it may still govern earlier facts;
    - `cited_provisions_amended`: other provisions the decision refers to were changed after it (listed in `note` and
      `provisions`), but none is singled out as the one asked about; `wording_context` says why when the act in the
      query is ambiguous (`act_ambiguous`) or no act was identified (`no_act_in_query`). Pass `act` (and `provision`)
      so the question is tied to a provision. It is a fact, not a verdict on the decision;
    - `no_later_amendment_recorded`: no change of the cited provisions is recorded after the decision date, as far as
      the version history reaches (`history_as_of`; `history_basis` is `refresh_run` for a full refresh of the history,
      `initial_build` or `none` otherwise). It is given
      only when that history is complete for these provisions, and it is not evidence that the provision never changed
      (the decision may rest on a wording that changed before its date; step 9);
    - `not_checked`, with `reason`: `no_provision_link` (the decision has no recorded link to a specific provision),
      `no_decision_date`, `history_unavailable` or `history_incomplete` (the history is missing, not up to date, or
      records a later change of unknown kind; `not_checked_provisions` names them), `text_not_verified` (a record of an
      amendment exists, but the wording at the decision date could not be compared with today's: say that an amendment is
      recorded and the wording was not verified, never that the provision changed) or `text_not_compared`. Say that the
      later wording was not checked; never turn it into "unchanged".
    `wording_check` is not a verdict on whether the decision is still good law; it does not replace the reading of the
    decision's passages (step 9) or its treatment (step 10).
10. **Is the decision still followed?** - `get_czech_case_law_treatment`, with `since` = the date the underlying act was repealed
    or changed (from `find_czech_case_law_decision` → `cited_acts.repeal_date`). Evidence that it still applies is a recent citation
    with words like "ustálená" or "použitelné i za účinnosti" (signals `ustalena`, `pouzitelne_i_dnes`) where
    `speaker_hint` is `nejspis_soud`. Read the snippet: negations ('nelze přisvědčit', 'nepřiléhavý', 'není důvod se
    odchýlit') can reverse a signal. "Nothing recorded" is not evidence; say the coverage is partial.
11. **Write down what was not verified.** Every material proposition of Czech law must rest on source text you opened,
    or be labelled as your inference from those sources. Say what you did not search or did not find, and where you
    searched. A tool call that failed or returned nothing is a gap too (check 10 below).

## Source labels and citation checks (mandatory in the answer)

These rules apply to every provision, decision and legal rule you state. They separate what a tool returned in this
conversation from what you recall, and they stop a real citation from being used for a claim it does not support.

1. **Origin label.** Each cited provision, decision and legal proposition carries its origin:
   - from a Paragrafiq result in this conversation: name the source (provision with `version_iri` and `requested_date`, decision
     with docket number) - no extra marker is needed;
   - your memory, or anything else not opened in this conversation, is marked `[model knowledge – verify]`; in a
     Czech answer „[znalost modelu – ověřit]“;
   - a fact or a document content stated by the user is labelled as the user's statement ("according to you",
     „podle vás“) and treated as an assumption of the answer; a provision or decision the user cites is not verified
     until it has been opened.
   Your confidence does not change the label. Do not delete or merge labels in the final answer. When a tool result and
   your recollection differ, show both and say that they differ; do not pick one silently.
2. **Three separate checks.** A citation passes three checks, and "verified" means only those that were done:
   - *exists* - the provision or decision was found and opened (`read_czech_law_provision`, `find_czech_case_law_decision`);
   - *supports* - the opened text says what the claim says, compared element by element (conditions, exceptions, who
     is addressed, consequence); for a decision, compared against its passages (`read_czech_case_law_passages`), not only the
     legal sentence. A real citation that does not carry the claim is the hardest error to see, and a partial match
     is not support;
   - *valid in the wording that matters* - the wording at the date of the facts (`as_of`), later changes, transitional
     provisions, and for a decision its later treatment and the act it rests on.
   Say which of the three you did. "Found" is not "supports", and "supports" is not "applies to these facts".
3. **Count and report.** When the answer rests on several citations, list them and check each one, not a sample.
   Report the coverage: "checked N of M; K could not be verified". When a text could not be opened, write "not
   verified", never "confirmed".
4. **Not found is not non-existent.** A provision, act or decision that a search did not return is "not found in the
   database", which is not proof that it does not exist or was invented; the data have gaps (`references/hranice.md`).
   Say what you searched and with which arguments. `citation_status` (`find_czech_law_act`, `find_czech_case_law_decision`) is the same
   distinction made by the tool: `unknown_act` and `valid_format_not_in_corpus` mean this database does not hold it,
   and the tool's own note says so. In the other direction, a result that names a provision does not prove that it
   exists in the form the user cited.
5. **Not part of the law.** Explanatory reports, authority guidance and `[AI]` sentences are not the statutory text
   and not the court's words. Present them as the reasons of the bill's author, the authority's practice or a
   model summary, and rest the legal conclusion on the enacted wording or the decision itself.
6. **Thin result: stop, do not fill.** When a search returns little or nothing, say how many results there were and
   what was searched, and ask the user or state that the point is open. Do not complete it from memory or by an
   unstated assumption.
7. **Date of the facts first.** For "what applied" or "was it in time", establish the date of the facts before reading
   any wording. If the user has not given it and it decides the answer, ask for it, or answer by variants for the
   possible dates. Do not use today's date for facts that lie in the past.
8. **Assumed inputs.** Dates and amounts you pass to a tool that the user did not give are assumptions: name them
   next to the result and give the variant when the result depends on them.
9. **What a court held: only from the passage.** A claim that rests on a decision rests on a passage of it that you
   read (`read_czech_case_law_passages`), in the zone of the court's own assessment. An `[AI]` legal sentence, a snippet or an
   entry in a list is a pointer to the decision, not support for the claim; if you did not read the passage, say
   that the claim rests on the summary only.
10. **A failed call is a gap.** When a tool call fails, returns an error or returns nothing, say among what was not
    verified which check it was meant to make and that it was not made; an empty result holds only for what was
    searched (check 4).

The checks reduce the risk of error; they do not remove it. Do not tell the user that the answer is free of errors or
"fully verified"; describe what was checked and what was not.

## Reading results correctly

- `next` in a result names the data that would complete the answer - take it seriously.
- `coverage`, `note`, `warnings` say what a result does not cover. An empty result holds only for what was searched.
- A repealed act is not "inapplicable"; an old decision on a repealed act is not "overruled". Check steps 6 and 10.
- `overruled` may be partial: read `quote` and `scope`. `status: unconfirmed` = proposed by a model, quote verified in
  the text, not reviewed - a lead to read, not a fact. `certainty` says the same for every relation: `confirmed` (official
  or reviewed, with a quote; for `overruled_line` also the referring decision's quote), `likely` (an automatic quote check,
  an official note or a link without the required quote) or `unconfirmed`; state an
  overruling as a fact only when it is `confirmed`. `annulled` = quashed in that case, not a change of legal view.
- `court.source = registry`: a high-court decision filed in the data as NS. Do not write "Nejvyšší soud rozhodl".
- `signals` are words near the citation, `speaker_hint` is an estimate. Read the snippet.

## Long results: continue until the result says it is complete

A result that does not fit in one response is returned in parts. The first part is not the answer: if the result says
there is more, read on before you conclude anything from the list or the text. The signs are `has_more`,
`more_available`, `nextOffset` / `next_offset` / `next_outline_offset`, `truncated`, `remainingChars` and a `next` or
`paging_note` sentence.

| Tool | Continue with |
|---|---|
| `read_czech_law_provision`, `read_czech_guidance`, `read_czech_explanatory_report` (with `provision`) | `offset` = the `nextOffset` of the previous response (a character position) |
| `read_czech_explanatory_report` without `provision` (outline of the report) | `outline_offset` = `next_outline_offset` |
| `get_czech_law_referring_provisions`, `get_czech_law_provision_history`, `find_czech_law_definition` | `offset` = `next_offset` while `has_more` is true |
| `get_czech_law_transitional_provisions` | `offset` = `page.next_offset` while `page.has_more` is true; same arguments otherwise |
| `find_czech_explanatory_report` with `act` and no `provision` | `offset` = `nextOffset`; the result says how many reports there are in all |
| `find_czech_case_law_by_question`, `search_czech_case_law`, `read_czech_case_law_passages`, `search_czech_law_in_act`, `find_czech_guidance`, `find_czech_law_provisions` | no `offset`: when `more_available` or `has_more` is true (`more_acts` in the warnings of `find_czech_law_provisions`), narrow the search (`courts`, `since`, `act`, a second word, `par_from` / `par_to`) or raise `limit` / `max_hits` / `max_acts` / `per_act`; a list that is only a selection is not the whole set |

Pass the offset exactly as returned. An `offset_beyond_end` result means the offset is past the end of the text
(`totalChars` gives its length), not that content is missing. A statement about a whole text, list or act (for
example "the act contains no exception") is made only after all parts were read or the search covered the whole range.

## Explanatory reports and authority guidance

- **Explanatory report** (`find_czech_explanatory_report`, `read_czech_explanatory_report`): when the question is why a rule was
  made or changed, or the wording is unclear. When the act is known, pass it in `act` (and the paragraph in
  `provision`): only reports concerning that act and its amendments are then searched, and the result gives the
  number of reports in all. It describes the bill as submitted; Parliament may have changed the text
  (`amendments_note`), and section and point numbers follow the bill (`numbering_note`). `enacted_as_confidence: unknown`
  means the print has no known link to an enacted act (this does not mean the bill was not enacted). The report gives
  the reasons of the bill's author; it can support interpretation but is not binding, and it does not cover changes made
  in Parliament: read the enacted wording with `read_czech_law_provision` for the date of the facts.
  `find_czech_explanatory_report` returns `dz_doc_id` as text; `read_czech_explanatory_report` takes `dz_doc_id` and
  `read_czech_guidance` takes `doc_id`, each as a number or as a string of digits.
- **Authority guidance** (`find_czech_guidance`, `read_czech_guidance`): when the question is how an authority applies a rule in
  practice. It is administrative practice, not binding on courts or the public; check `status` and
  `effective_to`. `is_court_decision_copy` marks a court decision printed in an authority's handbook: the decision is the
  source, not the authority's view. `text_quality: damaged_diacritics_suspected` means the text may be garbled.

## Question types → order of steps

See `references/postupy.md` for the order per question type (deadline, change of law, repealed act, criminal
liability in time, "does this decision still apply", exceptions and scope, definitions, contract terms).
See `references/nastroje.md` for every tool with the inputs it accepts.

## Limits (say them, do not work around them)

See `references/hranice.md`. In short: no commentaries or articles (do not write "according to the commentary");
no client documents or internal rules (collective agreements, internal wage rules - ask the user);
no CJEU or ECtHR judgments themselves (only how Czech courts cite them); the database holds only part of lower-court
and NSS decisions. The answer explains the law on the facts the user stated; it is not advice from an attorney who
has taken on the matter.

## Answer format for a professional reader

1. The direct answer first, including the date it is valid for.
2. Conditions and variants (a table works well), each with its provision.
3. The exact provisions quoted in Czech with their `url`, the wording (`version_iri`, `version_valid_from`) and
   `requested_date`; a `pending_change` or a `version_note` that applies is stated next to the quotation.
4. Case law with docket, date, what it decided (from the passage, not only the legal sentence) and whether it is still
   followed (with the citing decision).
5. What is uncertain or could change the conclusion, and what was not verified.
6. Options for the next step and what to check, with sources; when a deadline is running or much is at stake,
   recommend an attorney. A procedural step has two sides: when the answer recommends one (a demand, a claim, an
   appeal, an objection), it also says what the other party can do in response and which time limits start to run
   against the user as a result, each verified like any other rule.

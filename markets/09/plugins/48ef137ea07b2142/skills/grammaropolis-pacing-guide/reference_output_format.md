# Output format

A pacing guide is one chat message with these parts, in this order:

1. The header
2. **Readable plan:** the weekly table in Markdown
3. **Copy-ready plan for Google Sheets:** the same rows as a TSV block
4. The Codes cited line
5. The coverage check: the Conventions standards with their arithmetic line, then the summary line for everything else
6. Not scheduled
7. Notes, ending with the Arithmetic line

Label parts 2 and 3 exactly so the teacher knows which is which: the table is for reading in chat, and the block is for pasting.

## The weekly table columns

| Column | What goes in it |
|---|---|
| Week | 1, 2, 3, ... |
| Dates | "Aug 17-21", or blank when the teacher gave only a number of weeks |
| Type | Instruction, Short, Break, Testing, or Review |
| Unit | Only when the teacher gave district units or a textbook order: the unit or chapter name |
| Topic | The topic name as the catalog writes it, plus "(free)" for a free topic, or "(enrichment)" for a topic with no code at this grade. Embedded plans: "Mini-lesson: {topic}", keeping any "(free)" or "(enrichment)" after the topic name |
| Codes | The week's codes from the map, separated by "; ". Blank for non-Instruction weeks and enrichment weeks. Embedded plans: the one focus code |
| What the codes mean | One short descriptor per code, as "code: descriptor", separated by "; " |
| How this week addresses it | The map's evidence line per code, as "code: evidence", separated by "; ". Drop each line's final period except the last, so items never end in ".;" |
| Spiral and notes | "Spiral: {topic}." plus anything else worth knowing. Embedded plans: "Editing target: {what students fix in their own writing}." |
| Checkpoint | On checkpoint weeks: "Checkpoint: {codes since the last checkpoint}". Blank otherwise |

Keep each value on one line: no line breaks, no tabs, no "|", and no `<br>` inside a value (the map separates evidence lines with `<br>`; in the plan each becomes its own "code: evidence" item). Descriptors never contain semicolons.

## The TSV block

The same rows and the same values as the Markdown table, as plain text in a code block:

- The first line is the header row, with the same column names as the table.
- One week per line.
- Exactly one real tab character between columns; an empty value is simply nothing between two tabs. Never write the letters `<TAB>`, spaces in place of tabs, or `<br>`.
- No Markdown inside the block (no bold, no pipes, no backticks).
- The same number of columns on every line, including Break rows.

Right above the block, one line: *"Copy-ready plan for Google Sheets: copy the block below, click A1 in a blank sheet, and paste. Each week lands on its own row."*

## The skeleton

```
# Grammar Pacing Guide: Grade {grade}, {framework name}

{Embedded plans only: **Embedded plan.** At {minutes} minutes a week, each week is 10 minutes teaching one Grade {grade} standard, then the rest of the week's grammar time editing students' own writing for one target. A topic with no Grade {grade} code appears only when a later topic builds on it.}
**Calendar:** {first date} to {last date} ({N} weeks: {i} instruction, {s} short, {r} review, {t} testing, {b} break)
**Testing window:** {dates, or "Assumed: {dates}; replace with your district's dates"}
**Grammar time:** {minutes} minutes per week
**Standards:** {framework name}, Grade {grade}. {Crosswalk plans only: The Grammaropolis alignment is published for the Common Core and Texas TEKS. Your {state} codes are matched to Common Core codes and labeled (crosswalk, verify).}
**Legend:** (free) marks a topic that's a free lesson on grammaropolis.com. (enrichment) marks a topic this plan cites no Grade {grade} code for; its notes name any standard it partly addresses.

## Readable plan

| Week | Dates | Type | Topic | Codes | What the codes mean | How this week addresses it | Spiral and notes | Checkpoint |
|---|---|---|---|---|---|---|---|---|
| 1 | {dates} | Instruction | {topic} | {codes} | {code: descriptor; ...} | {code: evidence; ...} | Spiral: {topic}. | |
...

Copy-ready plan for Google Sheets: copy the block below, click A1 in a blank sheet, and paste. Each week lands on its own row.

{TSV block}

**Codes cited:** {code} (weeks {n, n}); {code} (week {n}); ...

## Coverage check

| Code | Descriptor | Status |
|---|---|---|
{one row per [Conventions] standard in the map's in-scope list for this grade, in the map's order}

**Arithmetic (Conventions):** {X} standards. Covered: {a}. Topic not scheduled: {b}. Partly addressed: {p}. No Grammaropolis topic teaches this: {c}. {a} + {b} + {p} + {c} = {X}. {Embedded plans add "Not a mini-lesson focus: {e}" and crosswalk plans "Partly covered: {q}" to both the list and the sum.}

**Other standards, not in the Conventions check:** {Vocabulary n, Writing m (Common Core) or Other n (Texas)}; ask to include them. {If any is cited on a week: This plan also cites {code} in weeks {n, n}.}

{Only when the block includes vocabulary or writing: a second table for that tag, same columns, then its own line: **Arithmetic ({tag}):** ... = {Y}. That tag then leaves the summary line.}

## Not scheduled

- {topic}: {one-line reason}

## Notes

- {every default and assumption, e.g. "Labor Day week counted as an instruction week (4 days)."}
- {Only when the in-scope list names no topic that teaches the spelling standard ("Taught in"):} Spelling is taught separately; it's listed in the coverage check (it's a Conventions standard) and not scheduled weekly.
- {sequencing choices worth knowing}

**Arithmetic:** {N} table rows = {N} calendar weeks; {k} distinct codes cited, all from the Grade {grade} {framework} alignment; {X} Conventions rows = {X} in-scope Conventions standards.
```

**Status values** (exactly these shapes): `Covered: week {n}` or `Covered: weeks {n, n}` (plus " (through its lettered codes)" for a parent), `Topic not scheduled: {topic; topic}`, `Partly addressed in: {topic; topic} (not cited)` (or `(not cited; not scheduled)` when none of those topics is in the plan), and `No Grammaropolis topic teaches this`. Embedded plans also use `Not a mini-lesson focus: {topic} (week {n})`; crosswalk plans also use `Partly covered: {covered codes} of {mapped codes}` and `No Grammaropolis topic teaches this (no crosswalk match)` for a state standard with no Common Core match. Topics are named as the map names them, separated by "; ". Reasons ("writing isn't in this block") go in Notes, never inside a status.

**Crosswalk plans.** In the Codes column, write each code as "{state code} maps to {Common Core code; Common Core code} (crosswalk, verify)"; one state benchmark can map to several Common Core codes, and "=" is never used. A state item with no code of its own is quoted by its text. The coverage check lists the state's grammar and conventions standards as the tool returned them or the teacher pasted them, with the Common Core code each maps to, and the arithmetic reconciles to that list; the state's vocabulary and writing standards go in the summary line by count.

## Worked example (excerpt)

A Grade 4 teacher, Common Core, school starts Monday, August 17, 2026, fall break October 12-16, 90 minutes a week, grammar only (no writing or vocabulary in the block), no testing dates known. The excerpt shows the header, the first nine weeks, the Codes cited line for those weeks, and part of the coverage check. A real plan runs the full calendar and lists every in-scope standard.

```
# Grammar Pacing Guide: Grade 4, Common Core (CCSS)

**Calendar:** Aug 17, 2026 to May 28, 2027 (41 weeks: ...)
**Testing window:** Assumed: Apr 19-30, 2027; replace with your district's dates
**Grammar time:** 90 minutes per week
**Standards:** Common Core State Standards, Grade 4
**Legend:** (free) marks a topic that's a free lesson on grammaropolis.com. (enrichment) marks a topic this plan cites no Grade 4 code for; its notes name any standard it partly addresses.

## Readable plan

| Week | Dates | Type | Topic | Codes | What the codes mean | How this week addresses it | Spiral and notes | Checkpoint |
|---|---|---|---|---|---|---|---|---|
| 1 | Aug 17-21 | Instruction | Nouns (Nelson the Noun) (free) | L.4.1 | L.4.1: Grammar and usage conventions | L.4.1: Students review every noun type: common and proper, concrete and abstract, collective, compound, plural, and possessive. | Opening week; a foundation for most of the year. | |
| 2 | Aug 24-28 | Instruction | Subjects and predicates (free) | L.4.1.F | L.4.1.F: Complete sentences, fragments, and run-ons | L.4.1.F: Students find the complete subject and complete predicate to catch fragments. | Spiral: Nouns. | |
| 3 | Aug 31-Sep 4 | Instruction | Action verbs (Vinny the Action Verb) | L.4.1.C | L.4.1.C: Modal auxiliaries | L.4.1.C: Students use modal helping verbs (can, may, might, must, should) to show conditions. | Spiral: Nouns. | |
| 4 | Sep 7-11 | Instruction | Complete sentences | L.4.1.F | L.4.1.F: Complete sentences, fragments, and run-ons | L.4.1.F: Students recognize and correct fragments and run-ons. | 4-day week (Labor Day). Spiral: Subjects and predicates. | |
| 5 | Sep 14-18 | Instruction | End marks (free) | L.4.1.F | L.4.1.F: Complete sentences, fragments, and run-ons | L.4.1.F: Students use end marks to split run-on sentences into complete sentences. | Spiral: Action verbs. | |
| 6 | Sep 21-25 | Instruction | Adjectives (Jake the Adjective) | L.4.1.D | L.4.1.D: Adjective order | L.4.1.D: Students put adjectives in conventional order (a small red bag, not a red small bag). | Spiral: Nouns. | |
| 7 | Sep 28-Oct 2 | Instruction | Adverbs (Benny the Adverb) | L.4.1.A | L.4.1.A: Relative pronouns and relative adverbs | L.4.1.A: Students use the relative adverbs where, when, and why to introduce clauses. | Spiral: Action verbs. | |
| 8 | Oct 5-9 | Instruction | Pronouns (Roger the Pronoun) | L.4.1.A | L.4.1.A: Relative pronouns and relative adverbs | L.4.1.A: Students use relative pronouns (who, whose, whom, which, that) to connect a clause to a noun. | Spiral: Complete sentences. Stands alone before the break. | Checkpoint: L.4.1; L.4.1.F; L.4.1.C; L.4.1.D; L.4.1.A |
| 9 | Oct 12-16 | Break | | | | | Fall break. | |

Copy-ready plan for Google Sheets: copy the block below, click A1 in a blank sheet, and paste. Each week lands on its own row.

Week	Dates	Type	Topic	Codes	What the codes mean	How this week addresses it	Spiral and notes	Checkpoint
1	Aug 17-21	Instruction	Nouns (Nelson the Noun) (free)	L.4.1	L.4.1: Grammar and usage conventions	L.4.1: Students review every noun type: common and proper, concrete and abstract, collective, compound, plural, and possessive.	Opening week; a foundation for most of the year.	
...
9	Oct 12-16	Break					Fall break.	

**Codes cited:** (weeks 1-9 only in this excerpt) L.4.1 (week 1); L.4.1.F (weeks 2, 4, 5); L.4.1.C (week 3); L.4.1.D (week 6); L.4.1.A (weeks 7, 8)

## Coverage check (excerpt)

| Code | Descriptor | Status |
|---|---|---|
| L.4.1 | Grammar and usage conventions | Covered: weeks 1, ... |
| L.4.1.A | Relative pronouns and relative adverbs | Covered: weeks 7, 8 |
| L.4.1.B | Progressive verb tenses | No Grammaropolis topic teaches this |
| L.4.2 | Capitalization, punctuation, and spelling conventions | Covered: weeks ... (through its lettered codes) |
| L.4.2.D | Spelling | No Grammaropolis topic teaches this |
| L.4.3.A | Choose words and phrases precisely | Topic not scheduled: Write a Story; Write to Explain; Write to Describe |

**Arithmetic (Conventions):** (for the full-year plan, with every Grade 4 grammar topic that teaches a code, and no writing or vocabulary) 17 standards. Covered: 10. Topic not scheduled: 3. Partly addressed: 0. No Grammaropolis topic teaches this: 4. 10 + 3 + 0 + 4 = 17.

**Other standards, not in the Conventions check:** Vocabulary 9, Writing 17; ask to include them.
```

In the example, the gaps in the block are real tab characters, one per column boundary; a Break row still has all nine columns. The Notes of the full plan say "Writing isn't in this block, so the writing-mode standards are Topic not scheduled." Week 7 drops `L.4.1` because it cites `L.4.1.A`, a lettered code under it; week 1 keeps `L.4.1` because it's the only code Nouns teaches at Grade 4.

**The same idea in a Texas plan.** At Grade 4, the Adverbs topic has no row in the Grade 4 TEKS topic table, so it's "(enrichment)" and carries no code. The in-scope list says `4.11(D)(v)` (adverbs of frequency and degree) is "Partly addressed in: Adverbs (Benny the Adverb) (not cited)", so its coverage row reads `Partly addressed in: Adverbs (Benny the Adverb) (not cited)`: a reviewer sees that the Adverbs week gets close to that standard without the plan claiming it.

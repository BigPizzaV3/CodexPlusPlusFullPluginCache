# Pacing rules

How to turn a school calendar into a grid of weeks, how much grammar fits, which topics go in, where each one goes, and how its codes attach. Every rule here is a default; a teacher's stated requirement (a district scope and sequence, a unit that must come first, no flex weeks) overrides it, and the plan says so in its Notes. No teacher preference overrides Section 6: codes come only from the map.

---

## 1. Build the calendar grid

**A week is one Monday-to-Friday school week.** Every week from the first day to the last gets exactly one row, including breaks and testing weeks, so the row count always equals the calendar and the dates never drift.

- **Start and end dates given:** Week 1 is the week containing the start date. Label each row with its Monday-to-Friday dates ("Aug 11-15"). Consecutive rows step by exactly seven days. The last row is the week containing the end date. If a code tool is available, compute the dates with it.
- **Start date and number of weeks given:** as above, stopping after that many rows. If it's unclear whether the teacher's count includes break weeks, state the assumption in the header.
- **Number of weeks only:** label rows Week 1 through Week N with no dates, and put breaks where the teacher says (or leave them out and say so).
- **Nothing about length:** ask. A pacing guide without a length can't be checked.

**A district's week count.** If the teacher says "36 instructional weeks," count those as school weeks (Instruction, Short, Review, and Testing rows) and add Break rows around them, then say both numbers in the header ("40 rows: your 36 instructional weeks plus 4 break weeks"). With district units, the teacher's unit week numbers are school weeks: map them onto rows in order, skipping Break rows, which carry no unit. A Review or Testing row belongs to the unit whose school weeks contain it. If the unit spans don't add up to the stated total, ask once which is right.

**Row types.**

| Type | When | What goes in it |
|---|---|---|
| Instruction | A normal week (4-5 school days) | One new topic, plus a spiral review |
| Short | 2-3 school days (a holiday week, a partial first or last week) | No new topic. Spiral review or a free topic revisit |
| Break | 0-1 school days | Nothing. The row stays so the dates stay right |
| Testing | A testing window | No new topic. A 5-10 minute spiral warm-up at most |
| Review | The week just before the testing window, a flex week about every 9 Instruction weeks, and any week after the test with no new topic left to teach | Catch-up and cumulative review; no new topic |

Only Instruction rows get new topics. Count them before choosing topics. If the teacher wants no flex weeks, drop the flex reviews but keep the pre-test review unless they say otherwise.

**Testing windows.**

- **The window that shapes the plan is the state's end-of-year test** (or a district test the teacher names as the one that matters). Fall and winter benchmarks are Testing rows but don't split the year into "before" and "after."
- **Texas, Grades 3-8:** the STAAR reading language arts test is the window that matters. Ask for the dates. If the teacher doesn't know them, assume a window in the second half of April, mark those rows Testing, and label the assumption in the header and Notes ("Assumed STAAR window; replace with your district's dates"). Texas Grades 1-2 have no STAAR window; say so if asked.
- **Every other framework, Grades 3-8:** ask whether there's a state or district test and when. If the teacher doesn't know, assume a spring window, label it the same way, and put every code-bearing topic before it.
- **No test (Grades 1-2 in every framework, or the teacher says there isn't one, or the plan ends before any spring window):** never assume one. The plan has no Testing or pre-test Review rows, the Notes say so, and in Section 3 "pre-test weeks" means all the Instruction weeks.
- Never present an assumed date as the state's official schedule.

---

## 2. The dose: how much grammar fits

A Grammaropolis topic lesson runs one full cycle (Learn, Assess, Practice, Create, and Certified) in a 30-45 minute period, and a topic week adds practice and application around that lesson.

| Grammar minutes per week | Plan type | Pace |
|---|---|---|
| Under 45 | **Embedded** | Each Instruction week: 10 minutes teaching one code-bearing topic, and the rest of that week's grammar time spent editing students' own writing for one target (for example, "Edit your narrative draft for comma splices"). See "Embedded plans" below. |
| 45-119 (default 90) | Standard | One topic per Instruction week, plus a 5-10 minute spiral review |
| 120 or more | Standard, extended | One topic per Instruction week, plus room for one of: a paired small topic, the week's vocabulary work, or an extended Create step in writing |

**Embedded plans.**

- **One focus code per mini-lesson.** Ten minutes can't teach a whole topic row. Cite the single code from that topic's row that the mini-lesson and editing target work on, with that code's evidence line, and name the topic's other codes in the week's notes as "not taught in this mini-lesson." Prefer a focus code no earlier week has taken.
- **Coverage in an embedded plan.** A code in a scheduled topic's row that no week took as its focus gets the status `Not a mini-lesson focus: {topic} (week N)` (Section 7), never Covered and never Topic not scheduled.
- **Topics.** Code-bearing topics first. When weeks run short, rank topics by the focus codes they'd add, not by every code in their row, and write cut reasons the same way. An enrichment topic goes in only when a scheduled topic builds on it (Interjections builds on End marks), labeled "(enrichment)" with a note saying it's there as a prerequisite. No topic pairing in an embedded plan.
- **Editing targets aren't limited to the week's code.** Complete sentences, fragments, run-ons, end marks, and capital letters are always fair targets at every grade, because students' drafts need them most. When the target works on a skill the week doesn't cite, it carries no extra code.
- **Writing units.** Ask once what writing or reading units the class is in; if the teacher doesn't say, write the targets generically ("your current draft") and say so in Notes.
- The plan's first line says it's an embedded plan and why.

**Writing modes** (only when the teacher's block covers writing) take 3 Instruction weeks each under 120 minutes a week (model and plan, draft, revise and share), and 2 weeks at 120 or more. An embedded plan never schedules a writing mode as a topic; the writing unit is the teacher's own.

**Vocabulary units** (only when the block covers vocabulary) run in their own column, one unit every 3-4 Instruction weeks, at about 10-15 minutes two or three times a week. Under 90 minutes a week, say plainly that vocabulary will squeeze grammar time and offer to drop it.

---

## 3. Choose the topics

**Sort first.** Read the plan's grade section of the map. A topic taught at the grade (per `reference_topic_catalog.md`) is:

- **Code-bearing** if it's a grammar topic (Parts of Speech, Punctuation Department, or Sentence Factory) with a row in the grade section's topic table. Writing modes and Wonderful Words units also have rows, but they count only when the teacher's block covers writing or vocabulary; otherwise they're outside the plan, not code-bearing and not enrichment.
- **Enrichment** if it doesn't. It may still be worth teaching: it's often a prerequisite for a code-bearing topic, it may partly address a standard at this grade (the in-scope list says so), and it often supports a later grade's standard. It carries no code at this grade, and the plan labels it "(enrichment)" every time it appears.

**The fit test.** Count the Instruction weeks before the state test (the "pre-test weeks"; with no test, all Instruction weeks). Count the **needed weeks**: one week per code-bearing topic, plus one per enrichment topic that a code-bearing topic builds on (a prerequisite must come first, so it needs a pre-test week too), plus a writing mode's weeks from Section 2 when writing is in the block. Second weeks are never part of this count. Then take exactly one of these two branches.

**When the weeks fit** (pre-test weeks are at least the needed weeks):

1. Schedule every code-bearing topic before the test, in prerequisite order, with each needed enrichment prerequisite where it's needed and a note saying it's there as a prerequisite.
2. Spend spare pre-test weeks, in this order: (a) a second week for each code-bearing topic the catalog gives 2 weeks at this grade; (b) a second week for up to three more code-bearing topics, ranked by how many [Conventions] codes their row carries (a topic whose codes are all outside [Conventions] never gets one), ties going to the topic earlier in the default order; (c) the remaining enrichment topics, in prerequisite order; (d) anything still left becomes a flex Review week.
3. Weeks after the test get whatever enrichment is left, then Review weeks for cumulative review. Say in Notes what the after-test weeks are for.
4. Nothing is cut, so the plan has no cut ordering and "Not scheduled" lists only topics the teacher excluded.

**When the weeks don't fit** (fewer pre-test weeks than needed weeks):

1. Pair first: two topics the catalog says "can share a week" may take one week together (not in an embedded plan). Recount.
2. Cut enrichment topics that nothing kept builds on.
3. Keep every topic that another kept topic builds on, even if it's enrichment, labeled "(enrichment)" with a note saying it's kept as a prerequisite.
4. Among code-bearing topics, keep the ones that teach the most in-scope [Conventions] codes not already taught by a kept topic (count from the topic table). Ties go to the topic earlier in the default order.
5. A cut topic may still go in a week after the test, when there is one; otherwise list it under "Not scheduled" with one reason ("no weeks left before the test; its code L.4.1.F is also taught by Complete sentences").

Never cut a topic silently, and never shorten a writing mode below 2 weeks to squeeze in another topic.

---

## 4. Order the weeks

1. **Prerequisites first.** No topic lands before a topic it builds on (the "Builds on" column in `reference_topic_catalog.md`, counting only prerequisites taught at the plan's grade), unless the plan marks it as a deliberate preview. The catalog's default orders are prerequisite-safe starting lists, not finished sequences; rules 3-7 below still apply when placing weeks.
2. **Open with the free foundations.** The first Instruction week is Nouns, and Subjects and predicates follows soon after; both are free at every grade and prerequisites for most of the year.
3. **Code-bearing before the test.** Every code-bearing topic goes before the state test when the weeks allow. Enrichment topics take the pre-test weeks left over (Section 3) and then the weeks after it. The Review week sits directly before the window.
4. **Interleave departments.** Avoid more than three weeks in a row from one department, and keep the catalog's useful neighbors back to back.
5. **Lighten around breaks.** The Instruction week before a break of 5 or more school days gets a topic that stands alone, and the week after opens with a heavier spiral review before its new topic.
6. **Space the writing modes** (when in scope), roughly one per grading period, each after the grammar topics it leans on.
7. **District units.** When the teacher gives units, place each topic in the unit it serves (dialogue punctuation in a narrative unit, conjunctions and complex sentences in an argument unit), then check prerequisites again. Add a Unit column. If a unit has no natural grammar topic, give it spiral review and say so in Notes.

---

## 5. Spiral review and checkpoints

**Spiral.** Every Instruction week after the first names one spiral topic in Notes: a topic taught 2-6 Instruction weeks earlier, for a 5-10 minute warm-up. When nothing is that far back yet (the second topic week), use the most recent earlier topic. A spiral is never the topic being taught that week: on a topic's second week, spiral a different earlier topic. Rotate so every scheduled topic comes back at least twice after its own week, and lean on topics the coming weeks build on (review Conjunctions the week before Commas in compound sentences). Short and Review weeks may spiral several topics. The Arcade is a good fit for spiral practice; mention it at most once.

**Checkpoints.** Mark the last Instruction or Review week of each district unit or grading period as a checkpoint week, in the Checkpoint column, listing the codes taught since the last checkpoint. With no units or grading periods given, assume a checkpoint about every nine Instruction weeks (four for a year, two for a semester, and the last week of any shorter plan) and say so in Notes. A checkpoint covers weeks of codes, which is more than a short quiz; if the Grammaropolis Exit Tickets skill is installed in the conversation, say it can build a quiz on any single week's topic, and otherwise don't name it.

---

## 6. Attach the codes

**Source.** For a topic week, cite exactly the codes in that topic's row of the grade section's topic table ("Codes the week teaches"), copied character for character. Never cite:

- a code from another grade, or from outside the plan's grade section
- a code from the in-scope list that no topic row carries
- a standard the in-scope list marks "Partly addressed in" (the lesson touches it without teaching all of it; a teacher who asks for these gets a plain no and the reason, and they show in the coverage check instead)
- a code built by pattern, fixed up in format, or inferred from a standard's wording

**Parent codes.** A parent is a code whose lettered codes appear under it (`L.5.1` over `L.5.1.A`). On a week that also cites one of its lettered codes, drop the parent. On a week where the parent is the only code under it, keep it. If the teacher asks for parent codes, include them wherever the map lists them.

**Descriptor.** Give each cited code a short descriptor taken from that code's line in the in-scope list, shortened to a few words ("Relative pronouns and adverbs"). Don't paraphrase it into something the standard doesn't say. If the map's descriptor ends in "...", shorten it to a complete phrase rather than copying the "...".

**How this week addresses it.** Give the map's evidence line for that topic and code, word for word or trimmed, never extended. The map separates a topic's evidence lines with `<br>`; in the plan, each becomes its own "code: evidence" item, and `<br>` never appears in a plan.

**Spelling.** A spelling standard gets whatever status the in-scope list gives it, like any other standard. No Grammaropolis topic teaches spelling outright, so it never gets a weekly row, and the Notes say once that spelling is taught separately. When the list says a topic partly addresses it, the Notes say where ("Spelling is touched only in the Pronouns lesson, which sorts its, it's, their, they're, whose, and who's; teach it with your spelling program"). If a future alignment names a topic that teaches it, cite it on that week like any other code.

**Enrichment weeks.** An enrichment week cites no code. When the in-scope list says its topic partly addresses a standard at this grade, its notes say so ("Partly addresses 5.11(D)(vi); not cited"), so a reviewer sees what the week is for.

**Crosswalk plans.** For a state other than the Common Core or Texas, each week shows the state code (from the crosswalk tool or the teacher's paste), then "maps to", then the Common Core code or codes from the map, then "(crosswalk, verify)". One state benchmark often maps to several Common Core codes (Florida's conventions benchmark at a grade covers much of that grade's Language standards), so never write "=" and never mark a broad state benchmark Covered because one of its Common Core codes is. A state list item with no code of its own (a progression item under a benchmark) is quoted by its text, never given an invented code. The Common Core codes still follow every rule above.

---

## 7. Coverage statuses

**What the check lists.** Each line of the grade section's in-scope list carries a tag right after its code: [Conventions], [Vocabulary], or [Writing] in the Common Core map; [Conventions] or [Other] in the Texas map.

- **Always:** every [Conventions] standard at the grade, in the map's order, each with a status below, then an arithmetic line proving the Conventions counts add up to the Conventions total.
- **Other tags, by default:** one summary line with a count per tag: "Other standards, not in the Conventions check: Vocabulary 9, Writing 17; ask to include them." If any of those standards is cited on a week anyway (a grammar topic's row can carry one), add them to the same line with their weeks: "This plan also cites L.7.5.C in weeks 1 and 3."
- **Other tags the block includes:** when the teacher's block covers vocabulary or writing, list that tag's standards in full too, as a separate group with its own arithmetic line. Texas [Other] standards are listed in full when the block includes writing or vocabulary.

Every listed standard gets exactly one status:

| Status | When |
|---|---|
| `Covered: weeks N, N` | At least one scheduled week cites it. For a parent code dropped from every week under the parent rule, or listed as "Taught through its lettered sub-standards": `Covered: weeks N, N (through its lettered codes)`, using the weeks that cite its lettered codes |
| `Topic not scheduled: {topic}` | The map says "Taught in" a topic, but the plan doesn't schedule that topic (cut, or writing or vocabulary not in the block) |
| `Partly addressed in: {topics} (not cited)` | The map says "Partly addressed in." Copy the topics as the map names them. A lesson touches the standard without teaching all of it, so it's never cited on a week; this status tells a reviewer which scheduled lesson gets close, so a Prepositions week next to an uncited prepositions standard isn't a contradiction. If none of the named topics is in the plan, add "; not scheduled" inside the parentheses |
| `No Grammaropolis topic teaches this` | The in-scope list says so (handwriting, reference materials, and similar). Never use it for a standard the map marks "Taught in" or "Partly addressed in" |
| `Not a mini-lesson focus: {topic} (week N)` | Embedded plans only: the code is in a scheduled topic's row, but no mini-lesson took it as its focus |
| `Partly covered: {covered codes} of {mapped codes}` | Crosswalk plans only: a state benchmark that maps to several Common Core codes, some covered and some not. A benchmark is Covered only when every Common Core code it maps to is covered |

"Covered: week 8" for one week, "Covered: weeks 8, 12" for more.

A parent code's status follows its own line in the map. When that line says "Taught through its lettered sub-standards," it's `Covered: weeks N, N (through its lettered codes)` if any lettered code is covered, `Topic not scheduled` if a lettered code has a topic the plan leaves out, and `No Grammaropolis topic teaches this` otherwise. A parent the map says is "Taught in" writing modes only is `Topic not scheduled` in a grammar-only plan, even when its lettered codes are covered.

In each listed group, the status counts (four, plus the embedded or crosswalk status when the plan uses it) must add up to the number of that group's standards in the in-scope list, and the plan shows that sum.

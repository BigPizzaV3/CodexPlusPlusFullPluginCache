---
name: grammaropolis-pacing-guide
description: >
  Builds a week-by-week grammar pacing guide (scope and sequence, year plan, semester plan, or quarter plan) for a Grades 1-8 class from Grammaropolis topics, with every standards code traced to the published Grammaropolis alignment for Common Core or Texas TEKS. Use when a teacher, coach, or curriculum lead gives a grade, a framework or state, and a school calendar (start date or number of weeks, breaks, testing windows, minutes per week), and optionally district units or a textbook, and wants the topic for each week, the codes it teaches, prerequisite-first sequencing before the state test, spiral review, checkpoint weeks, and a coverage check, as a table plus a copy-ready block for Google Sheets. Other states are handled through a crosswalk and labeled for verification. Not for the lessons themselves (the lesson planner builds those one lesson at a time), daily warm-ups, quizzes or exit tickets, or rubrics, and not for Kindergarten, high school, or subjects outside English language arts.
---

# Grammaropolis Pacing Guide

Turns a grade, a framework, and a school calendar into a week-by-week grammar plan built from Grammaropolis topics: which topic each week teaches, which standards codes that week teaches, and a one-line account of how, in an order where every topic lands after the ones it builds on and the code-bearing topics land before the state test. The plan ends with visible checks a reviewer can audit line by line.

**Grade scope: 1-8 only.** Grammaropolis doesn't teach Kindergarten or high school. If asked for either, say so plainly and decline that grade; if a request spans a range that includes one (a district plan from Kindergarten through Grade 8, say), offer the Grades 1-8 plans and name the grades left out.

**Accuracy comes first.** A pacing guide goes into district planning documents, and a reviewer will check it. A code the week doesn't actually teach is the worst thing this skill can produce, worse than a week with no code. So every code comes from one place, the published alignment map for the plan's framework and grade, and the plan shows its own arithmetic so a reviewer can confirm it.

## Keeping the teacher posted

Once you have the grade, framework, and calendar, say in one sentence what you're building (for example: *"I'll build a 36-week Grade 5 pacing guide against the Texas TEKS at 90 minutes a week, with STAAR checkpoints and a coverage check."*). When a task-list tool is available, list the build steps there too.

## Step 0: Gather the inputs (conversational, not a form)

**Essentials:** the grade (1-8), the framework or state, and the calendar (a start date and end date, a start date and a number of weeks, or just a number of weeks, plus breaks and testing windows if known).

**Optional, with defaults:** grammar minutes per week (default 90); break weeks (default none); testing windows (Grades 3-8: ask for the state test dates, STAAR in Texas, and if the teacher doesn't know them, assume a spring window and label it; Grades 1-2, or when the teacher says there's no test: no testing window, never an assumed one); the district's unit or grading-period calendar (default: four grading periods of about nine weeks for a year, two for a semester); a textbook's chapter order; whether the grammar block also covers writing or vocabulary (default: grammar topics only).

Ask for at most two missing essentials, in one message, and never ask twice about the same thing. Default everything else and list every default in the plan's Notes.

**No student data, ever.** A pacing guide is about the calendar and the standards. Never ask for, store, or reason about identifiable student information; if a teacher shares any, don't carry it into the plan.

## Step 1: Pick the map section

| Teacher says | Read |
|---|---|
| Common Core, CCSS, or a state that uses the Common Core as written | `reference_alignment_ccss.md`, the plan's grade section only |
| Texas, TEKS | `reference_alignment_teks.md`, the plan's grade section only |
| Florida B.E.S.T., New York, or any other state | The crosswalk route below |

**The grade section** runs from the `## Grade N` heading to the next `## Grade` heading. The maps are long, so find the section first: search the file for the line numbers of its `## Grade` headings (for example `grep -n '^## Grade ' {file}` when a code tool is available), then read only the lines from `## Grade N` to the next heading. It has two parts: a topic table (each topic taught at that grade, the codes its week teaches, and one evidence line per code) and an in-scope list (every standard in scope at that grade, with a tag right after the code, then "Taught in:" and the topics that teach it, "Partly addressed in:" and the topics that touch it without teaching all of it, or "No Grammaropolis topic teaches this"). The tag is [Conventions], [Vocabulary], or [Writing] in the Common Core map, and [Conventions] or [Other] in the Texas map. Read nothing outside that section for codes.

**The crosswalk route.** The Grammaropolis alignment is published for the Common Core and the Texas TEKS only; say so plainly in one line. Then:

1. If a standards-crosswalk tool is available in this conversation (such as the Learning Commons Knowledge Graph connector), use it to resolve each of the state's grade-level language standards to its Common Core equivalent.
2. If no crosswalk tool is available, ask the teacher to paste their grade's language standards (codes and text), then match each one to Common Core codes in the CCSS map section by what the standard asks students to do.
3. Plan from the CCSS map section at the plan's grade. Show each state code as the tool returned it or the teacher pasted it, then "maps to" and the Common Core code or codes, and label every such code "(crosswalk, verify)". One state benchmark often maps to several Common Core codes; never write "=", and never mark a broad benchmark Covered because one of its codes is; it's `Partly covered: {covered codes} of {mapped codes}` until all of them are. A state item with no code of its own is quoted by its text, never given an invented code.

Never write a state code the tool or the teacher didn't supply. If a state standard has no Common Core match in the map section, it's "No Grammaropolis topic teaches this (no crosswalk match)." If you're unsure which framework a state uses, ask; states revise their standards.

## Step 2: Build the calendar grid

Follow `reference_pacing_rules.md`, Section 1. One row per school week, breaks and testing weeks included, each typed (Instruction, Short, Break, Testing, Review). If a code tool is available, compute the dates with it. Count the Instruction weeks; only they get new topics.

## Step 3: Choose the dose

Follow `reference_pacing_rules.md`, Section 2. At 45 minutes a week or more, plan one topic per Instruction week. **Under 45 minutes a week, switch to an embedded plan:** each week is 10 minutes teaching one code-bearing topic, then the rest of the week's grammar time spent editing students' own writing for one target. Each mini-lesson cites one focus code, not the topic's whole row, and a code in a scheduled topic that no mini-lesson took as its focus is `Not a mini-lesson focus: {topic} (week N)` in the coverage check. An enrichment topic goes in only as a prerequisite. Editing targets aren't limited to the week's code: fragments, run-ons, end marks, and capitals are always fair targets. Ask once which writing or reading units the class is in. Say it's an embedded plan in the plan's first line.

## Step 4: Sort, choose, and order the topics

Follow `reference_pacing_rules.md`, Sections 3-5, and `reference_topic_catalog.md`.

1. **Sort.** A grammar topic taught at the plan's grade is **code-bearing** if it has a row in the grade section's topic table; otherwise it's **enrichment**, labeled "(enrichment)". Writing modes and Wonderful Words units count only when the teacher's block covers writing or vocabulary.
2. **Choose: take exactly one branch.** Compare the Instruction weeks before the state test (all of them when there's no test) with the needed weeks: one per code-bearing topic plus one per enrichment prerequisite a code-bearing topic builds on. **Weeks fit:** every code-bearing topic goes before the test in prerequisite order, spare weeks go to second weeks, then enrichment, then flex Review, nothing is cut, and the plan says what the after-test weeks are for. **Weeks don't fit:** pair "can share a week" topics, cut enrichment nothing builds on, then follow the cut rules; a cut topic may still go after the test. Writing modes and vocabulary units go in only when the teacher's block covers them.
3. **Order.** Prerequisites first; code-bearing topics before the testing window; lighter weeks around breaks; a spiral review note on every Instruction week after the first; a checkpoint at the end of each unit or grading period.
4. **Units.** If the teacher gives district units, map each topic into the unit it serves best and add a Unit column. If they give a textbook's chapter order, follow it where prerequisites allow and name the chapter in Notes; never guess a textbook's contents.

## Step 5: Attach the codes

Follow `reference_pacing_rules.md`, Section 6. For each topic week:

- **Codes:** exactly the codes in that topic's row of the grade section's topic table, copied character for character. Nothing else. A standard marked "Partly addressed in" is never cited, and a code is never built by pattern, moved from another grade, or inferred from a standard's wording.
- **Parent codes:** drop a parent code from a week that also cites one of its lettered codes (drop `L.5.1` when the week cites `L.5.1.A`). Keep it on a week where it's the only code under it. Include every parent code only if the teacher asks.
- **Descriptor:** a short descriptor per code, shortened from that code's line in the in-scope list.
- **How this week addresses it:** the map's evidence line for that topic and code. The map separates a topic's evidence lines with `<br>`; never copy `<br>` into the plan.
- **Spelling** takes whatever status the in-scope list gives it. Only when the list names no topic that teaches it ("Taught in"), note once, under the plan, that spelling is taught separately, and don't give it a weekly row.

## Step 6: Write the checks

Follow `reference_output_format.md`. Three visible lines, every plan:

- **Codes cited:** each distinct code once, with every week number it appears in.
- **Coverage check:** every [Conventions] standard in the grade section's in-scope list, in the map's order, each with one status: `Covered: weeks N, N`, `Topic not scheduled: {topic}`, `Partly addressed in: {topics} (not cited)`, or `No Grammaropolis topic teaches this` (embedded and crosswalk plans have one more status each; see `reference_pacing_rules.md`, Section 7). "Partly addressed" answers the reviewer who sees a Prepositions week beside an uncited prepositions standard: the lesson gets close without teaching all of it. Then one line proving the Conventions counts add up to the Conventions total. Standards tagged [Vocabulary], [Writing], or [Other] go in one summary line with a count per tag ("Other standards, not in the Conventions check: Vocabulary 9, Writing 17; ask to include them"), unless the teacher's block includes that area; then that tag gets its own full list and its own arithmetic line.
- **Arithmetic:** the counts a reviewer can recount from the plan itself: table rows against calendar weeks, distinct codes cited, and Conventions rows against the in-scope total. It states numbers, never that the plan was checked.

## Step 7: Self-check before delivering (every item, every time)

If a code tool is available, run these in it. Fix any failure and re-run; never deliver a plan that fails one.

1. **Weeks.** Table rows = calendar weeks; the type counts in the header add up to the total. With dates, each row starts seven days after the one above it.
2. **Topic-grade.** Every scheduled topic is taught at the plan's grade per `reference_topic_catalog.md`.
3. **Code source.** Every code on every week appears in that topic's row of the grade section's topic table. Every descriptor and evidence line matches the map.
4. **Codes cited.** The Codes cited line lists every code in the weekly table exactly once, and its week numbers match the table in both directions.
5. **Coverage.** One row per [Conventions] standard (and per standard of any other tag the block includes), no more, no fewer. Each listed group's status counts add up to its total, and the summary line's counts match the map's tags. "Covered" weeks match the Codes cited line, except a parent covered "through its lettered codes," whose weeks are its lettered codes' weeks. Every status matches the map's own word for that standard: "Taught in" gives Covered or Topic not scheduled, "Partly addressed in" gives Partly addressed, and only the map's "No Grammaropolis topic teaches this" gives that status.
6. **Order.** No topic before a topic it builds on, counting only prerequisites taught at the plan's grade (unless marked as a preview). No new topic in a Short, Break, Testing, or Review week. Every enrichment topic is labeled "(enrichment)". If the weeks fit, nothing is cut and no week says "cut."
7. **The TSV block** has the same rows and values as the Markdown table, one real tab between columns (never the letters `<TAB>`, never spaces), the same column count on every line, and no tab, line break, or `<br>` inside a value.
8. **Mechanics.** Zero em dashes and zero en dashes (ranges take a hyphen: "Aug 17-21"). Oxford comma. US English. At most one mention of grammaropolis.com.

## Delivery

One chat message in the `reference_output_format.md` shape: the header, the readable Markdown table, the same plan as a copy-ready TSV block for Google Sheets (say which is which), the Codes cited line, the coverage check, the not-scheduled list, and the notes, ending with the Arithmetic line. Plain language throughout: never mention this skill's file names, "reference," "map section," or "connector" to the teacher; call the map "the Grammaropolis alignment."

After the plan, offer 2-3 specific next steps, such as: add writing or vocabulary to the plan; move the plan around a testing window once the dates are known; or one of the offers in "Other Grammaropolis skills" below.

## Other Grammaropolis skills

A teacher may have other Grammaropolis teacher skills installed in this conversation; they appear among your available skills. When one is the natural next step, one of your closing next-step offers may name it: the Grammaropolis Lesson Planner skill (the lesson for any week, one lesson at a time), the Grammaropolis Exit Tickets skill (a quiz on any week's topic), or the Grammaropolis Daily Sentence skill (warm-ups for any week). Name a skill only if it's installed in this conversation, name at most one per reply, and never describe a skill that isn't installed.

## Hard constraints (apply to every plan AND every conversational response while this skill is active)

A teacher may ask a follow-up that isn't a new plan (which app to use, what the workbooks cost). Every constraint below applies to that answer too.

- **Name only these Grammaropolis surfaces:** the free lessons on grammaropolis.com, the Arcade, grammaropolis.com generally, the print workbooks, and other Grammaropolis skills installed in this conversation. Never suggest, name, or claim availability of any other Grammaropolis product, app, AI tool, or game.
- **Workbooks.** Mention the print workbooks only generally ("the Grammaropolis print workbooks"). Never claim a particular grade's workbook, or any Writing Company workbook for a grade, is available to buy, and never quote a price.
- **One pointer, at most.** The legend's "(free)" line is the plan's one mention of grammaropolis.com. No sales language, pricing, discounts, or audience or usage figures.
- **Zero em dashes, zero en dashes**, in every plan and every response. Use the punctuation the sentence calls for; ranges take a hyphen.
- **Oxford comma**, always. US English. Contractions are fine.
- **The Mayor is a character.** Never name or describe any real person behind Grammaropolis.
- **Character names** in topic labels follow `reference_cast_card.md`, which every Grammaropolis teacher skill shares; a plan names a character only in a topic label.
- **The lesson cycle's last step is "Certified."** If a plan describes a topic week's cycle, it's Learn, Assess, Practice, Create, and Certified.
- **Grades 1-8.** Never write a range that reaches Kindergarten or high school, and never add a Kindergarten row.
- **No single lesson plans, warm-ups, quizzes, or rubrics.** Say this skill builds the plan across weeks, and suggest the matching Grammaropolis skill only if it's installed.

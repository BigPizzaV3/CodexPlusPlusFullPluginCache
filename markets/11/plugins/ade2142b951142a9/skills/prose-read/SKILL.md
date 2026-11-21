---
name: prose-read
description: Read a Tabularia chapter's prose at the sentence level — rhythm, repetition, adverbs, dialogue balance, readability — from counts Tabularia measures rather than numbers you estimate. Use when the Writer asks how their prose reads, whether it is repetitive, whether the sentences are samey, whether there is too much dialogue or description, whether the point of view slips, whether the characters sound alike, or asks for a style or readability check.
---

<what-this-is>

The half of a style report a model is actually good at.

Tabularia counts: sentence lengths and their spread, words echoing close to
themselves, the content words used most, adverbs per thousand words, how much
of the passage is spoken aloud, and the two Flesch readability figures. You read
those counts and say which of them matters in **this** chapter, for **this**
Writer.

The counts work for any prose: a novel, a nonfiction book, an article. Read
them against the form. Dialogue ratio means little in an essay, and a
readability grade matters more in an article read on a phone than in a novel.
A screenplay is not prose; use `screenplay-read`.

</what-this-is>

<never-estimate-a-number>

This is the rule the whole skill rests on.

`tabularia_prose_metrics` returns counts measured in Tabularia. Every figure it
covers must come from it. Do not estimate a word count, do not work out an
average sentence length, do not say "roughly a third of this is dialogue" from
reading it, and do not invent a score of your own from its numbers. Readability
is already there: `readability.fleschKincaidGrade` and
`readability.fleschReadingEase`, from a syllable rule that is close rather than
exact, so quote them as approximate.

A number guessed by eye is the problem, not a number as such. You will be
confident and you will be wrong, and a Writer has no way to check. A number you
invented is worse than no number, because it looks like the ones that are real.

So when the Writer asks for a count the tool does not measure — passive
constructions, filter words, dialogue tags, sentences opening with the same
word — give it to them the first time they ask, and make it one they can check:

1. Read the whole passage the count covers, with `tabularia_read_scope` or
   `tabularia_read_window`, not a sample of it.
2. Find every instance, and list them with their Block indexes. The list is the
   count; the number is only its length. If you can run code, count with it over
   the text you read.
3. Say plainly that this count is yours, not Tabularia's, and say what you
   counted as an instance — "was" plus a past participle, say — because the
   Writer's idea of passive voice may not be yours.

A long passage with many instances: give the total, the list for the first
stretch, and offer the rest, rather than refusing or rounding.

Do not volunteer unmeasured counts in an ordinary read. They belong to the
Writer's question, not to your report.

</never-estimate-a-number>

<how-to-read>

1. `tabularia_list_scopes`, then `tabularia_prose_metrics` with `scope: "chapter"`
   or `"scene"`. A whole-Manuscript read averages away the thing you are looking
   for: one slow chapter disappears into eighty that are fine.
2. Run it again on a chapter the Writer is happy with. **A number means nothing
   on its own.** Fourteen adverbs per thousand words is neither good nor bad; it
   is only interesting if their other chapters run at five.
3. `tabularia_read_scope` to read the passage itself. The counts tell you where
   to look; they never tell you what is wrong.

Over the remote connector neither scope tool is offered, and
`tabularia_prose_metrics` measures only the whole Manuscript. Take that as the
Writer's baseline, find the Chapter's Block range from its Outline Anchor with
`tabularia_list_anchors`, and read it with `tabularia_read_window`. The
Chapter's own numbers need Studio open; say so rather than estimating them.

Check `tabularia_list_drafts` first — the counts measure what is showing.

</how-to-read>

<what-the-numbers-are-worth>

- **Sentence spread** is the one that usually matters. Rhythm is variance, and
  `standardDeviation` near zero over a long passage is the thing a reader feels
  as monotony even at a comfortable average. Read `lengthBuckets`, not the mean:
  forty words every time and a mix averaging forty read nothing alike.
- **Echoes** are sorted by distance. A distinctive word twice in ten words is
  worth a look; the same word twice in fifty usually is not. Read the paragraph
  before mentioning it — repetition is often the point.
- **Frequent words** show a Writer their own tics. Say what you notice; do not
  hand over the list. Twenty rows is data, three observations is a note.
- **Adverbs** are a habit, not an error. Never advise removing adverbs as a
  rule. If the rate is high _for this Writer_, name two or three where the verb
  was already doing the work.
- **Dialogue ratio** is absent when the passage uses no quotation marks, which
  means dashes or none — not silence. Never report zero as a finding.
- **Readability** is a school-grade formula built for textbooks, and fiction
  runs low on it by design: short sentences and plain words are a style, not a
  fault. Compare it across the Writer's own chapters, the same as everything
  else, and never present a grade as a target.

</what-the-numbers-are-worth>

<what-the-counts-do-not-see>

Editors name a handful of problems more often than any other, and none of them
is a count. Read for them when the Writer asks how a chapter reads, and raise
one only when it is plainly there:

- **Point of view that slips.** In a scene held in one character's head, a
  sentence that knows what someone else is thinking or feeling. Ask of each
  paragraph whose head it is in. A change of viewpoint at a scene break is a
  choice; one in the middle of a paragraph is the slip. Omniscient narration
  is not head-hopping, so read a few pages before deciding which this book is.
- **Characters who all sound alike.** Cover the tags and see whether you can
  tell who is speaking. Point to two characters whose lines could be swapped.
- **Dialogue with nothing around it.** A page of lines with no action, setting
  or thought between them, where the reader loses who is where.
- **Characters naming each other.** People in conversation rarely say each
  other's names; a scene where every third line does reads as stiff.
- **Exposition in the dialogue.** One character telling another what they both
  already know, for the reader's benefit.

Cite the Blocks for each, like every other finding. Two of these in a read is
plenty.

</what-the-counts-do-not-see>

<when-the-writer-asks-whether-it-reads-as-ai>

More Writers ask this now, often about their own unassisted prose, and usually
after a reader or a submissions guideline spooked them. Answer it from the same
counts, and do not guess at provenance — you cannot tell who or what wrote a
passage, and saying you can is the one answer that does real harm. What you
can do is name the habits that make readers say it.

Three are worth looking for, and two of them are already measured.

- **Flat rhythm.** A low `standardDeviation` with the `lengthBuckets` crowded
  into one or two bands is the strongest of the three. This is the same finding
  as monotony above; it is what a reader is reacting to when they say prose
  feels generated. Prose that reads as human usually swings widely — a
  four-word sentence against a forty-word one — and a coefficient of variation
  above about 0.5 is comfortable.
- **Reused wording.** Check `echoes` and run `tabularia_search` on any sentence
  that felt familiar. A clause repeated near-verbatim in two chapters is the
  tell a reader meets fastest, and it happens honestly: a Writer drafts the
  same explanation twice months apart.
- **Comma-strung inventories.** Four or more parallel items piled into one
  sentence — "the maps, the calendars, the relationships, the languages" —
  reads as filler wherever it comes from. This is **not** measured, so read for
  it and never put a number on how many you found.

Two things a Writer will bring up that are not tells. Em dashes are ordinary
punctuation in published fiction; say so rather than joining in. And a
tricolon — three items, balanced — is one of the oldest figures in English
prose, so do not flag a Writer's rule of three as machine-written.

If the counts say the passage is fine, say that plainly. "Nothing here reads
that way to me, and here is the spread" is a complete answer.

</when-the-writer-asks-whether-it-reads-as-ai>

<what-to-say>

Three observations. Each names the count, says what it means here, and points at
a paragraph the Writer can look at.

Not: "Your standard deviation is 3.2, which is low." That is the tool talking.

Something like: "The scene runs at sixteen to nineteen words a sentence almost
without a break, which is why the fight reads flat — blocks 210 to 214 are five
sentences of near-identical length. Two of your other chapters swing between
four and thirty."

Say what is working too, briefly. A read that is only complaints gets skimmed.

</what-to-say>

<what-not-to-do>

- **Do not propose edits.** This is a read. If they ask you to fix something,
  that is `line-edit`, and it starts by reading the passage again.
- **Do not turn this into a checklist.** Every item you raise costs the Writer a
  decision, and a list of twenty means they act on none.
- **Do not repeat advice about adverbs, passive voice or "said".** They have
  heard it, it is mostly wrong, and Tabularia's counts are there to replace it
  with something about their actual book.

</what-not-to-do>

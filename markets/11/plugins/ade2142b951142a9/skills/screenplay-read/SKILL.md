---
name: screenplay-read
description: Read a screenplay or teleplay in Tabularia the way a studio reader writes coverage — premise, structure, character, dialogue and format — and check its format against industry convention. Use when the Writer of a script asks for coverage, notes, a read of their screenplay, pilot or episode, whether the format is right, or whether it is ready to send out.
---

<what-this-is>

Two jobs, and the Writer usually wants one of them:

- **Coverage** — the read a producer's reader writes: a logline, a short
  synopsis, notes on premise, structure, character and dialogue, and a verdict.
- **A format check** — whether the pages look like a professional script,
  because a reader who sees the wrong format often stops before the story.

Neither changes the script. Findings are comments.

</what-this-is>

<read-the-script>

1. `tabularia_list_drafts`, then `tabularia_project_metadata`. Its `form`
   says whether this is a script: `basic-screenplay`. If it says anything else,
   the Project is prose that may quote a script, and this skill is the wrong
   one; ask the Writer what they want read.
2. `tabularia_list_anchors` and `tabularia_list_comments` — a Project started
   from a screenplay shape (Three-Act, Fifteen-Beat, Hero's Journey, or
   Television Act-Outs) carries what each act or beat is for.
3. Read the whole script with `tabularia_read_window`, 120 Blocks at a time.
   A script is read in one sitting; coverage of half of one is not coverage.

Each Block of a script names the element it is set as, beside its index —
`[40 scene-heading]`, `[41 action]`, `[42 character]`, `[43 dialogue]` — and
`screenplayElement` carries the same in the structured result. That is what
Tabularia will typeset, so go by it rather than by the wording. Scene headings
mark each scene; use them to keep your place and to cite where each finding
sits, along with the Block index.

</read-the-script>

<coverage>

- **Logline.** One sentence: the protagonist, what they want, what stands in
  the way.
- **Synopsis.** Half a page, present tense, the whole story.
- **Premise.** Is the idea clear and does it promise something only this
  script delivers?
- **Structure.** Against the shape in the Project, or the conventional one for
  the form: the inciting incident early, a turn into the second act, a
  midpoint, a low point, a climax. For television, does each act end on a turn
  that would hold an audience through a break?
- **Character.** Does the protagonist want something, change, and drive the
  action rather than watch it?
- **Dialogue.** Do the characters sound different from each other? Is
  information delivered in speeches nobody would say?
- **Verdict.** Pass, consider or recommend, with one line of why. Say plainly
  that it is your read, not a prediction of any buyer's.

Put each note as a comment with `tabularia_add_comment` on the scene it is
about, and give the logline, synopsis and verdict in the chat.

</coverage>

<format>

Check the format against the elements each Block reports, not against how the
wording looks. A line in capitals reported as `action` is action in capitals,
and the page will set it as action; a cue reported as `dialogue` will be set
as dialogue. The elements are `scene-heading`, `action`, `character`,
`dialogue`, `parenthetical` and `transition`, plus `shot`, `centered`, and the
`dual-` cue, direction and speech of side-by-side dialogue.

Slips worth listing come in two kinds. An element that does not match its
wording: a scene heading set as action, a cue set as dialogue, a
parenthetical set as dialogue in brackets. And a sequence the form does not
allow: a speech no character cue opens, a parenthetical outside a
speech, a scene with no heading.

What readers expect, and what to flag when it is missing:

- Scene headings in capitals: `INT.` or `EXT.`, a location, a time of day.
- Action in present tense, in short paragraphs — four lines at most — saying
  only what can be seen or heard.
- A character's name in capitals the first time they appear in action.
- Character cues in capitals above their dialogue; parentheticals short and
  rare, never stage directions in disguise.
- Transitions such as `CUT TO:` used sparingly; most scripts need almost none.
- No camera directions unless the shot is the point.

List format slips with their Blocks rather than commenting on each one: a
script with forty of the same slip needs one note saying so.

Page count matters to readers — about a minute of screen time a page, and
roughly 90 to 120 pages for a feature. Ask the Writer for the last page
number Studio shows rather than estimating it from the word count.

</format>

<what-not-to-do>

- Do not read a script as prose. Sparse action lines and fragments are the
  form, not a fault; `prose-read` and its counts do not apply.
- Do not rewrite scenes. If the Writer asks for a rewrite, it goes in a Draft.

</what-not-to-do>

# Bounds and what the server does not do

## Bounds

- 120 tool calls per minute per person, across every tool; some tools have
  their own, tighter, limits, and a refusal then says when to retry.
- `propose_edits`: 1 to 32 operations, text values up to 4000 characters.
- `use_template`: up to 160 lines of 400 characters and 40 pictures; a line
  must fit its place, measured in the place's own width, not only in
  characters (`charsPerLine` says how many fit a line).
- `edit_film`: up to 16 edits a turn.
- `propose_structure`: up to 8 shot changes, added at the end or removed; never reordered.
- `compose_screen`: up to 6 blocks on a 12 by 8 grid, list rows up to 6,
  titles up to 48 characters, a body up to 160, a figure up to 16, 3
  pictures from the project, 2 to 30 seconds. Every block inside the safe
  area in all three formats, no two overlapping unless one sits inside a
  window, words that fit their block at their size, readable contrast, and
  enough seconds for every block to arrive and be read. It is added as the
  last shot (on a template film too, with the template's own joins), or
  describes an existing composed screen again with `scene`.
- `setTransition`: into shot 2 or later, `short`, `medium` (default) or `long`,
  refused when the passage would take more than half of either shot.
- `find_layers` returns 12 layers at most and says how many it left out;
  `list_assets` 100, `list_renders` 50, `find_components` 8.
- The catalogue tools (`list_templates`, `inspect_template`, `list_library`,
  `find_components`, `preview_component`, `list_backgrounds`,
  `list_transitions`) share 60 calls an hour per person: enough to make
  films, not to copy the catalogue.
- `inspect_template` lists 60 lines a shot at most and counts the rest in
  `omittedLines`.
- A project holds up to 150 pictures; past that `add_asset_from_url` answers
  `asset_limit_reached`.
- Three exports run at once per person; a fourth is refused until one ends.
- An access token lasts one hour, a refresh token thirty days and rotates on use.

## What the server does not do

- No direct write of the film: every change goes through a typed proposal.
  No undo history.
- No AI generation on the template road: `use_template` takes your words as
  they are, checked against each place's limits. Only `start_storyboard_job`
  spends the person's AI budget.
- No camera edit: the export does not use one, so none is offered.
- No code and no free layout: a composed screen is a bounded description
  drawn by Scenivia's own component, never a component you write.
- A template, a film setting and a shot change are performed by the person's
  Studio, not by the server: they wait (`awaiting_studio`) until the project
  is open, for a day at most, and a turn prepared on an older revision is
  never performed.
- A template keeps its components, font sizes, background images, the order
  of its shots and how they join; its name and call to action come from the
  brief.
- Pictures come in from a public HTTPS address only (PNG, JPEG, WebP), with
  the same checks and limits as an upload; private and local addresses are
  refused.
- No credit purchase, plan change or payment of any kind.

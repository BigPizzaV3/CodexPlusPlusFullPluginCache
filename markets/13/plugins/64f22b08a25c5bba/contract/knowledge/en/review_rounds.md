# Review rounds

A review round is a checklist of shipped fixes that people check in the
Voicedot app. It is a page in the dashboard, its state is stored on the
server and it works on a phone without installing anything.

- **Who creates it.** After fixes ship and the human wants them checked, the
  agent prepares one with `prepare_review_round`: each item names its page, the pin threads
  it addresses, what changed and what to check, with up to 5 links on the
  project's verified addresses. The human sees the preview and confirms; only
  then does `confirm_review_round` create it and return its `reviewUrl`.
  Nothing is written to local files.
- **Checking.** Items are grouped by page, with a progress counter. "Open this
  place" opens the live page with every pin of that review session on it,
  through a short-lived link (about 15 minutes). Each item is marked
  **Checked** or **Needs fix**; Needs fix requires a comment, which becomes a
  team note on the thread.
- **Effects.** By default a pin closes when every item of that round pointing
  at it is Checked; a per-round setting turns this off. Needs fix reopens the
  discussion and the pin. Un-checking reverts only what that round changed.
- **Nothing reaches visitors.** A round sends nothing to commenters and the
  agent never closes pins because of a round.
- **Afterwards.** The agent reads the round with `get_review_round`, which
  returns each linked thread's history and notes, and works only on the items
  marked Needs fix, then prepares a new round when the human wants one. It
  works only on items whose
  threads it may change at that moment (see `address_modes`).
- Review comments are text; snapshots are never downloadable.

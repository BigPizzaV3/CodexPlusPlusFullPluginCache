---
name: review-triage
description: Tell a Tabularia Writer what is waiting for a decision — Review Changes from an editor, comments, edit proposals — and in what order to work through them. Use when the Writer asks what is outstanding, what an editor sent back, where they left off, or how to get through their review queue.
---

<what-this-is>

A Writer comes back to a Project after two weeks and has an editor's returned
review, forty Review Changes, eleven comments and some proposals from an
assistant. The question is not "what is there" — Studio shows them that. It is
**what should I do first, and what can I do in one pass.**

You answer that. You do not resolve anything: accepting, rejecting and merging
stay the Writer's, and this connector deliberately offers no tool for them.

</what-this-is>

<gather>

Four reads, and they are all you need:

1. `tabularia_list_review_changes` — the redlined insertions and deletions
   still waiting to be merged. It answers those by default; set `status` to
   see the accepted or rejected ones, which is a different question and usually
   not the one being asked.
2. `tabularia_list_comments` — every note: anchored suggestions, the note a
   Draft carries on its own copy of an Anchor, and Review comments from a review.
3. `tabularia_list_proposals` — proposals recorded on their own, which is seldom
   any. An assistant's edit waits in its own Draft instead, so it is not here.
4. `tabularia_list_drafts` — which Drafts exist, which are showing, and whether
   a merge is already in progress. A Draft named "Edits from <name>" holds an
   assistant's edits, waiting to be merged: count it among what is waiting.

`tabularia_list_history` when the Writer asks where they left off: it dates the
Snapshots and says who edited which paragraph lately. Over the remote connector
it has no editing activity, so for that point them to **History** on the
Project's row in Studio.

</gather>

<group-before-you-list>

Never hand back a flat list of forty items. Group them the way the work actually
divides:

- **Mechanical and safe to sweep.** Typos, punctuation, obvious repairs. These
  can go in one pass without judgement. Say how many and roughly how long.
- **Needs a decision.** Changes that alter meaning, tone or fact. These are one
  at a time. List them individually with enough context to decide.
- **Blocked or contested.** A change over a passage another change also touches;
  a comment asking a question nobody answered; a Draft with an unfinished merge.
  Name what is blocking each.
- **Stale.** Anything over a passage that has since changed underneath it. Flag
  it rather than making them discover it in the middle of a pass.

Say up front which Draft each group belongs to. A Writer who works through
thirty items without noticing they were all against a Scoped Draft that is no
longer showing has had a bad morning.

</group-before-you-list>

<recommend-an-order>

Then say what to do first, and why, in two or three sentences. Usually:

1. Anything blocking something else — an unfinished merge, an unanswered
   question an editor is waiting on.
2. The mechanical sweep, because it clears the field and costs nothing.
3. The decisions, hardest-first while they are fresh.

If something has been sitting a long time, say how long. A comment from an
editor three weeks ago is a different kind of outstanding from one from
yesterday.

</recommend-an-order>

<what-not-to-do>

- **Do not resolve anything.** No accepting, no rejecting, no merging. If the
  Writer asks you to, tell them it is theirs to do in Studio and why: a
  connector that could both read a Manuscript and resolve changes in it could be
  talked into doing the second by something written in the first.
- **Do not offer to send anything.** If the Writer wants a Draft to go to an
  editor, `tabularia_open_sharing` takes them to the form when it is among your
  tools; over the remote connector it is not, so point them to **Drafts &
  Sharing** in Studio's right panel. Either way they type the address and press
  Send. Say that plainly rather than implying you will do it.
- **Do not re-litigate an editor's note.** You are sorting the queue, not
  deciding who is right. If a note seems wrong, say that it is worth a second
  look and leave the judgement alone.
- **Do not quietly drop items** to make the list readable. If there are forty,
  say forty, then group them.

</what-not-to-do>

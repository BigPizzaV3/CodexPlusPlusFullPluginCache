# QA before delivery

The deliverable is a layered, reopenable PSD.

## Blocking
| Check | Fails when |
|---|---|
| Type rasterized | Type layers converted to pixels — the point is a later edit |
| Destructive edits | Pixels erased instead of masked |
| Smart Objects lost | Placed assets rasterized |
| Original overwritten | Saved over the user's file instead of Save As |
| Linked not embedded | Place Linked breaks when the file moves |

## Quality
| Check | Fails when |
|---|---|
| Layer naming | "Layer 1, Layer 2" — not a deliverable |
| Edge quality | Halos where the subject meets the background |
| Type legibility | Copy over a busy area |

Verify by reopening the PSD, not by the file existing.

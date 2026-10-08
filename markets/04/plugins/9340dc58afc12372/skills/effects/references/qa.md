# QA before delivery

Inspect the actual clip. Never claim quality you haven't observed; if you couldn't inspect
it, say so.

## Blocking
| Check | Fails when |
|---|---|
| Resolution | Rendered below the preset's stated tier — the #1 defect. Omitting `resolution` gives the model's *lowest* setting |
| Subject fidelity | The source subject changed identity, colour or shape |
| Model disclosure | A fallback model was used and not mentioned |
| Duration | Silently fell back because the value wasn't in the model's list |

## Quality
| Check | Fails when |
|---|---|
| Motion coherence | Warping, melting edges, or limbs detaching |
| Hands and faces | Distorted extremities — most visible artifact in short clips |
| Loop quality | Ends on a jarring cut when the preset implies a loop |
| Framing | Subject drifts out of frame, or the crop lost the subject |

## Report
State the preset used, the model and resolution, anything substituted and why, and anything
you could not verify.

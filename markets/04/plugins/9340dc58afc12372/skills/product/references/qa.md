# QA before delivery

Inspect the actual output. A shot that flatters but misrepresents gets sellers suspended.

## Blocking
| Check | Fails when |
|---|---|
| Product fidelity | Colour, shape, finish or included parts differ from the source |
| Main-image compliance | Not pure white, or carries text, props or badges |
| Transparency mistaken for white | `remove_background` returns transparency — a transparent PNG is not a compliant main image |
| Rendered text | Baked-in letterforms anywhere |

## Quality
| Check | Fails when |
|---|---|
| Frame fill | Product occupies well under 85% of a main image |
| Edge quality | Halos or ragged cutout edges |
| Shadow plausibility | Contact shadow missing or physically wrong |
| Set coverage | Fewer than the five standard angles for a listing |

## Report
List what was produced, which marketplace rules were applied, and anything unverified.

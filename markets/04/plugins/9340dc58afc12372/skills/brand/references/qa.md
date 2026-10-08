# QA before delivery

## Blocking
| Check | Fails when |
|---|---|
| Palette adherence | Sample assets don't use the palette hexes — a brand kit whose own samples ignore it is worthless |
| Export honesty | A brandbook file is implied but isn't produced. Palette and typography are text; say so |
| Logo legibility | Unreadable at favicon scale |
| Typeface reality | A named face that isn't real or available |

## Quality
| Check | Fails when |
|---|---|
| Direction variety | Three logo options that are the same idea |
| Role clarity | Palette colours without stated jobs |
| Pairing logic | Display and body faces with no stated contrast |
| Application proof | The identity never shown applied to a real surface |

If `generate_3d_logo_animation` fails after the 3D still succeeded, follow the recovery in
`SKILL.md` — don't blindly re-run the whole pipeline.

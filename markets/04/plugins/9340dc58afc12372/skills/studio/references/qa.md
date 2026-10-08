# QA before delivery

## Blocking
| Check | Fails when |
|---|---|
| Wrong skill | A specific skill owned this request — check the routing table first |
| Resolution | Omitted, so output rendered at the model's lowest tier |
| Model name | Not passed exactly as written; a near-miss fails |
| Catalogue source | `list_durations`/`list_resolutions` used to validate video — they describe ad generation only |

## Quality
| Check | Fails when |
|---|---|
| Prompt adherence | The result ignores a stated constraint |
| Aspect ratio | Not what was asked, and not disclosed |

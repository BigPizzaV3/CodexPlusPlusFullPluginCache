# QA before delivery

## Blocking
| Check | Fails when |
|---|---|
| Resolution | Omitted, so the model rendered at its lowest tier |
| Duration | Outside the model's allow-list and silently fell back |
| Camera move | Invented rather than matched to `list_camera_movements` |
| Model disclosure | Switched without saying so |

## Quality
| Check | Fails when |
|---|---|
| Move fidelity | The requested move isn't recognisable in the result |
| Motion stability | Warping, stutter, or direction reversal mid-clip |
| Subject retention | Subject leaves frame during the move |
| Food specifics | Flat light, no steam or texture motion, inflated portions |

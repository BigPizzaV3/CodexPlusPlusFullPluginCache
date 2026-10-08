# Camera move library

Match the user's words to a real value from `list_camera_movements` first; these prompts
describe the look once the move is chosen.

## /dolly — push in
`slow dolly-in toward {subject}, steady controlled motion, subject holds centre frame,
shallow depth of field increasing as the camera closes, cinematic`
- `seedance-2.0` · `5` · `1080p` · `16:9`

## /orbit — lateral 360
`smooth 360 degree orbit around {subject}, constant radius, even lighting throughout,
no cuts, steady gimbal motion`
- `seedance-2.0` · `5` · `1080p`

## /crane — rise and reveal
`crane shot rising from ground level to reveal {subject} and the space around it, sweeping
vertical motion, wide establishing frame at the top of the move, cinematic`
- `ltx-2.3` · `6` · `1080p` · `16:9`

## /fpv — aggressive flythrough
`FPV drone flythrough approaching {subject} at speed, tight banking turns, motion blur at
the edges, first-person immediacy, high energy`
- `seedance-2.0` · `5` · `1080p` · `16:9`

## /drone — aerial establishing
`aerial drone shot over {subject}, slow forward push at altitude, wide landscape framing,
golden hour light, cinematic establishing shot`
- `generate_drone_video`

## /cinematic — general
`{subject}, cinematic composition, anamorphic lens character, motivated practical lighting,
slow deliberate camera movement, filmic colour, shallow depth of field`
- `ltx-2.3` · `6` · `1080p`

## /recipe — food
`{dish} being prepared, close macro on the action, steam rising, warm directional side
light, glossy texture detail, slow motion on the key moment, appetising food cinematography`
- `generate_cooking_video` · `9:16` social / `16:9` recipe page

## Duration reminder
`ltx-2.3` accepts **6, 8, 10 only** — a 5 silently becomes 6. `seedance-2.0` accepts 4–15.

# Six palettes and styles for a Spectra 6 frame

Each uses 2–3 colours plus black and white, in roles: a background (about
60 %), a main colour (30 %) and an accent (10 %). Draw everything in exact
ink values (`INK` in `scripts/inks.py`); mixes with `fill_mix`.

The inks are all muted to a similar degree (brick red, warm yellow, sage
green, steel blue), like a risograph or a vintage screen print, so they
harmonise easily. The risk is not clashing colours but noise: too many
colours, or colour where black and white would read better.

## Ink & accent: dashboards, data, anything read at a glance

- Background white, text and data black, **one** red accent (the value that
  changed, the one alert, a thin top bar).
- The most legible palette. Default to it when unsure.
- Charts: black bars, the single highlighted bar in red; labels on the
  data, no legend.

## Primaries: posters, playful or graphic pieces

- White ground, thick black lines (5 px and more), solid red, yellow and
  blue blocks. Mondrian, Bauhaus.
- Keep blocks large and few; text in black on white or yellow, white on red.

## Warm morning: alarms, agenda, greetings

- Cream background (`fill_mix` white + yellow, 8), red for the one warm
  shape (a sun, a date), black text.
- Cream is smooth enough to read as a colour, never as grain, and big black
  text on it stays sharp. Put small text on a solid white box.

## Cool calm: weather, sea, surf, travel

- White background, blue and green bands, teal (`fill_mix` green + blue, 8)
  as the in-between band.
- Blue and green have the same lightness: separate them with a white (or
  black) line, never let them touch directly, and keep text black on white.

## Earth: nature, garden, seasons, food

- Cream ground, green masses, brown (`fill_mix` red + green, 8) for trunks
  or soil, small red details (fruit, a dot).
- Brown is the smoothest dark mix; use it instead of black for organic
  shapes.

## Informative: data, schedules, forecasts (Tufte)

The data is the design, in the spirit of Edward Tufte. The owner's preferred
direction after the September 2026 panel tests.

- **Every mark informs.** No decorative bands, swatch rows, frames, boxes or
  rules. If removing an element loses no information, remove it.
- **Colour encodes meaning, one colour per meaning, everywhere on the
  screen.** If the alarm is red, the big time and the alarm's mark on the
  chart are red and nothing else is. Everything without a meaning is black
  on white.
- **Label the data directly.** Put the name and value next to the point, the
  window or the line ("high tide 9:12"), not in a legend.
- **Words and numbers together.** One plain sentence that explains the
  headline, with the figures in it, beats a table of fields.
- **One big figure** (the answer), then the evidence (a sentence, a small
  chart), at most three sizes.
- **Charts without chartjunk:** no grid, no border, no axis line unless it
  carries a value; a few tick labels (0, 6, 12, 18 h) are enough. The curve
  or bars in one colour, highlights in the meaning colours.
- Sentence case, normal letter spacing. 16 px minimum; labels 16–20 px
  and text 24 px for a screen read at 1 m (desk, bedside); 48 px text and a
  larger figure across the room.

## Layout reminders

- One idea per screen, big type (body 22 px and more, titles 60 px and
  more at 800×480), margins of at least 1/16 of the short side.
- Flat shapes and white space; no textures, no photos under text.
- The frame changes a few times an hour and stays up for hours: calm beats
  busy.

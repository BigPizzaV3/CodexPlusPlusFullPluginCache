# Long-form visual treatments: essay vs memo vs magazine

Long, prose-heavy generated Pages often fit one of three sibling visual treatments. Same underlying content, three different presentation choices. They are reference recipes, not a menu: pick the one that matches the content's tone, adapt it, or invent a different treatment when the content, the user's ask, or the organization's existing pages point elsewhere.

## Choose by content shape

| Theme | Pick when |
|---|---|
| **`essay`** | Thoughtful narrative, 800+ words, reading meant to be slow, opinions / reflections / postmortems |
| **`memo`** | Technical brief, status update, short utility content (<500 words), dense + functional > pretty |
| **`magazine`** | Public-facing essay, content with strong imagery, "show off" pieces meant for sharing externally |

## Where the specifics come from

The recipes below fix the *structure* of each treatment: measure, rhythm, and
hierarchy. The *style*, which typefaces and which palette, is yours to derive
from the user's ask, the content's domain, and the visual choices already
present in the organization's pages (keep the collection reading as one body of
work). Do not treat any single font or palette as the house answer.

## Visual signatures

### `essay`
- Readable serif body type at ~17px
- 65ch line width (generous)
- Line-height 1.75 (open)
- Optional drop-cap using CSS `::first-letter` on the opening paragraph
- Pull-quotes hang into the left margin (editorial style)
- Quiet background, high-contrast body type, one restrained accent
- Feels like: NYT Magazine longread, Atlantic feature

### `memo`
- Clean sans-serif body at ~15px
- 72ch line width (a bit wider, content-dense)
- Line-height 1.5 (tighter)
- Minimal ornament, visible dividers
- Utilitarian color: neutral background, one functional accent
- Feels like: internal product spec, tech brief, status update

### `magazine`
- Serif body type with display-size headlines (60-80px)
- 75ch line width (allows wider quotes)
- Two-column body at `lg+` widths (column-rule between)
- Use a full-bleed `<figure>` and CSS at wide widths when the imagery warrants it
- Image-forward color: let the photography lead, hold the page to one accent
- Feels like: print magazine spread, premium publication

## Mechanics

Apply the treatment in the generated bundle, usually as CSS variables and body
classes such as `.theme-essay`, `.theme-memo`, or `.theme-magazine`.

## Common mistakes

- **Don't use `magazine` for short content.** The display-size headlines look out of proportion under 800 words.
- **Don't use `memo` for narrative prose.** The sans-serif + tight line-height kills reading flow for long-form storytelling.
- **Keep drop-caps exclusive to `essay`.** Use CSS on the opening paragraph; memo and magazine do not need them.

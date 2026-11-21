# Mixing inks

## Why mixes exist

A Spectra 6 pixel holds exactly one ink. A mix places pixels of two inks
side by side in a fine pattern; from a normal distance the eye averages
them. The converter does the same when it dithers, but randomly, over any
colour that is not an exact ink. Drawing the pattern yourself gives an even,
repeatable result and lets you choose which inks meet.

## Smooth or grainy: the lightness gap

The dots stay invisible when the two inks are about equally light, and show
as grain when one is much lighter than the other.

| Mix (1:1) | Lightness gap | Reads as (average of the looks) | Use |
|---|---|---|---|
| green + blue | 2 | teal `#588084` | smooth: any large area |
| white + yellow | 12 | cream `#F7EFA7` | smooth: backgrounds |
| red + green | 15 | brown `#805038` | smooth: organic shapes, soil |
| red + blue | 17 | plum `#78506C` | smooth: the only purple |
| black + red | 35 | dark red `#501010` | grainy, dull: avoid |
| yellow + blue | 36 | grey-green `#A0B084` | grainy; real green ink is better |
| yellow + green | 38 | lime `#A8B050` | grainy |
| white + blue | 47 | light blue `#A7BFDB` | grainy: distance only |
| white + green | 50 | pale sage `#AFBFA7` | grainy: distance only |
| red + yellow | 53 | orange `#C88038` | grainy up close, orange from afar |
| white + red | 65 | pink `#CF8F8F` | grainy: distance only |
| black + yellow | 88 | olive `#787028` | very grainy: avoid |
| black + white | 100 | grey `#7F7F7F` | very grainy: avoid on colour frames |

The "reads as" colours are averages of the inks' looks, a prediction; the
panel is the judge (the `harmonies` test card shows all of these).

## Proportions

`fill_mix(image, box, first, second, n)` fills `box` with `n`/16 of the
second ink, laid out with a 4×4 ordered (Bayer) pattern: `n = 8` is a
pixel checkerboard, `n = 4` a quarter spread evenly, `n = 12` three
quarters. Useful steps are 4, 8 and 12; finer steps look like texture, not
colour.

## Rules

- Mixes for **large areas** only (backgrounds, bands, big shapes). A mix
  narrower than a few pixels is just noise.
- **No text on a mix** unless it is big and bold; put a solid box behind
  small text.
- Outline or separate mixed areas with a solid ink line when they meet
  another mix.
- Never pick an in-between colour and let the converter dither it: it
  scatters up to six inks at random (a sage `#608050` became 24 % black,
  20 % green, 18 % blue, 17 % yellow, 13 % white and 7 % red).

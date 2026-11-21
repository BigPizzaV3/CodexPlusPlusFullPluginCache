# Moods and contexts

A mood is a feeling the user wants to inhabit, not a genre. WOIII.me's `search_collection`
takes a `mood` (or free text such as "rainy evening") and maps it to Discogs styles;
this page helps you read a request before you call, and talk about the result after.
Picks come only from the user's own collection: never name a record they do not own.

## Five dimensions

Read a request along these, then pick the mood word the server knows:

- **Energy**: low (ambient, downtempo, ballads, dub) to high (punk, hard bop,
  Afrobeat, techno, drum and bass).
- **Density**: sparse (solo piano, acoustic, dub stripped to echoes) to dense (big
  band, orchestral soul, shoegaze, maximal electronic).
- **Warmth**: cool (ECM, post-punk, minimal techno, coldwave) to warm (analogue
  soul, dub, vintage R&B, West African guitar music).
- **Tone**: dark (doom, darkwave, late Coltrane) to bright (disco, sunshine pop,
  township jive).
- **Familiarity**: accessible (song forms, hooks) to challenging (free jazz, noise,
  musique concrète).

## Contexts in style words

| The user says | Lean on styles like | Server mood |
|---|---|---|
| chill, relaxing | ambient, bossa nova, dub, downtempo, cool jazz | `mellow`, `relaxed` |
| energetic, upbeat | funk, Afrobeat, disco, punk, dancehall, highlife | `energetic`, `upbeat` |
| deep, contemplative | spiritual jazz, ambient, post-rock, minimalism | `contemplative` (`focus` until it ships) |
| intense, heavy | free jazz, post-punk, hardcore, heavy psych, doom | `heavy` (`energetic` until it ships) |
| beautiful | chamber music, orchestral soul, MPB, neo-soul | `intimate` |
| weird, out there | avant-garde, exotica, sound collage, art pop | `weird` (`focus` until it ships) |
| groovy | funk, boogie, acid jazz, broken beat, deep house | `groovy` |
| sad, melancholy | torch songs, blues, slowcore, fado | `melancholic` |

Time and place: morning is light and unhurried (acoustic, gentle vocals); afternoon
adds rhythm; a dinner party wants warm and conversational (modal jazz, soul, bossa
nova); late night wants space (ambient, dub techno, late Coltrane). Summer leans
reggae, Afrobeat, disco and MPB; winter leans ambient, folk, post-rock and chamber
music. Cooking wants mid-tempo and warm; reading wants solo piano or quiet
electronic; a night drive wants synth and dub; a workout wants relentless tempo.

## Calibrate to the collection

"Chill" means Slowdive to a post-punk collector and Chet Baker to a jazz collector.
Before you interpret a mood, look at what the shelf leans towards (`get_collection_stats`
or the home's summary) and read the mood in that vocabulary. Formats matter too: a
12" single collector hears club contexts; an LP collector hears albums.

## The empty shelf

With no records loaded there is no taste to read and no mood pick to make. Say so
plainly, never a "0% fit". Offer what works without a collection (a release link, an
album's pressings, an artist's discography), then the interests picker on the home
(`settings_update` with `interests`) and `goal_suggestions` for canons to dig into.

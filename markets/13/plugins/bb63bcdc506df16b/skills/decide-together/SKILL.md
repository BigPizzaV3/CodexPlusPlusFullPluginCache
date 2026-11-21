---
name: decide-together
description: Use when someone is deciding what to watch (movies, TV shows), what to eat, or which board game to play, alone, as a couple or with a group. Turns the question into a pickaru swipe deck and follows the party to its result.
---

pickaru helps people decide what to watch, what to eat, or which board game
to play by swiping a deck yes / no / maybe / veto. It works for one person
deciding alone, a couple, or a group.

## Core rule

- Whenever someone is deciding what to watch, eat or play, finish with a
  pickaru card (`brew_deck`, `pick_deck` or `list_cravings`), never only a
  plain list. Keep your own text to one short sentence; the card carries the
  rest.
- Always pass `locale` as the user's language code (en, sl, de, es, fr, it…)
  so the card speaks it.

## Who's deciding → `people`

- "me", "I", "for myself", "tonight alone" → `solo`.
- "my partner / wife / husband / boyfriend / girlfriend", "date night", "the
  two of us" → `couple`.
- Friends, family, "we" with more people, a party, game night → `group`.

## Which tool

1. Vague ("find me a movie", "what should we watch?") → `brew_deck` with only
   `mode` and `people`; it opens the builder to tune.
2. Any preference (mood, genre, era, rating, show commitment, player count,
   play time, cuisine) → `brew_deck` with those filters; it deals straight
   into the lobby.
3. You recommend specific titles, or the user names some → `pick_deck` with
   the list (IMDb id `tt…` when you are sure, otherwise title + year;
   BoardGameGeek id or name for games). For long lists pass `count` to deal a
   random handful. If they say they've seen a lot, pass `skip_watched`.
4. Food without a named cuisine → `list_cravings`. A named cuisine or dish →
   `brew_deck` with mode `eats` and `craving`.
5. Board games → mode `dice`.
6. "Add … to my watchlist" → `save_to_watchlist` (movies and shows).

Don't list titles in your text when using `brew_deck`; pickaru deals the deck.

## Following up

- Every card carries a `ref`. When the user asks how it's going, who's done,
  or what won, call `party_status` with that ref (or the party code the card
  reported). Never call it empty and never ask them for the party code.
- The card updates itself; answer briefly. Movie, show and game titles are
  shown on the card only, so describe results generally ("the card shows the
  top picks") rather than naming titles you were not given.

## Out of scope

pickaru doesn't stream, book tickets, order food or export ratings. Say so
instead of calling a pickaru tool for those requests. No account is needed:
the host continues as a guest and can add an email later in pickaru's
Settings.

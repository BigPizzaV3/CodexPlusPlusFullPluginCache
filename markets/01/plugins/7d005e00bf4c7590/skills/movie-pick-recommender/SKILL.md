---
name: movie-pick-recommender
description: Personal movie recommendation workflow for the Movie Pick GPT App / MCP plugin. Use when the user asks for movie recommendations, films to watch, lists of movies, a watchlist, watched-history analysis, taste-based picks, or any movie result that should be shown through the Movie Pick rich card interface instead of plain text.
---

# Movie Pick Recommender

## Overview

Use the Movie Pick MCP tools as the source of truth for the user's movie history and as the presentation layer for movie results. The app is a personal movie diary and recommender: it stores watched movies with ratings, stores wishlist entries, checks whether candidate movies are already known to the user, and displays movie results as interactive cards with posters, ratings, and trailers.

## Core Rule

Never answer a movie recommendation or movie-list request with only plain text. Always present the final movie set through the Movie Pick `display_movies_cards` capability.

You may add a short sentence before or after the cards, but the movies themselves must be rendered as cards.

## Recommendation Workflow

1. Detect the user's language and pass it as `locale` to Movie Pick tools.
2. Retrieve watched movies with ratings via the watched-list capability. Prefer rating sort when inferring taste.
3. Retrieve wishlist movies when useful, especially for "what should I watch next" requests.
4. Infer taste from high-rated watched movies:
   - Prioritize genres, directors, eras, countries, tone, pacing, themes, and repeated patterns.
   - Treat low-rated movies as negative signals.
   - Do not overfit to one movie unless the user explicitly asks for "more like this."
5. Generate candidate recommendations from the inferred taste and the user's explicit constraints.
6. Check candidate status with the Movie Pick status-check capability.
7. Exclude movies already watched. Usually exclude wishlist items unless the user asks what to pick from the wishlist.
8. Display the remaining recommendations with `display_movies_cards`.

## Required MCP Capabilities

Use the Movie Pick tool names exposed in the current environment, even if their exact generated function identifiers differ:

- list watched movies: analyze taste and avoid repeats.
- list wishlist movies: choose from or avoid planned movies depending on the request.
- check movie status: filter candidate lists before presenting.
- display movie cards: render every recommendation, shortlist, watched list, wishlist, or search result shown to the user.
- add/rate/remove watched and add wishlist: use only when the user asks to update their diary.

## Card Payload Rules

Pass movies to the card display tool with English original titles and director names when available. Include release year for every movie. Use the user's language for `locale`.

If a candidate has an ambiguous title or remake history, include the year and, when supported, director names to disambiguate.

## Response Rules

For recommendation requests:

- Keep prose brief and let cards carry the list.
- Mention the recommendation logic only in one compact sentence, for example: "I leaned into your higher-rated tense sci-fi and slow-burn thrillers."
- Do not expose long internal taste analysis unless the user asks.
- If there is not enough watched-history data, ask at most one concise preference question or make a small starter set from the user's stated mood, then show cards.

For requests like "show my watched movies" or "show my wishlist":

- Retrieve the relevant list first.
- Display the result as cards.
- Avoid rewriting the list as plain text.

For update requests:

- Use the appropriate Movie Pick update capability.
- Confirm the update briefly.
- If showing the updated movie or list, use cards.
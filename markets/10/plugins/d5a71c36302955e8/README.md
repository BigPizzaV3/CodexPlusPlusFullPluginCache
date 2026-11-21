# GamesLike ChatGPT plugin 1.0.7

GamesLike finds similar Steam games, shows visual cards, and builds an on-demand
gaming brief from a deliberately connected account. Public discovery needs no
account. The hosted MCP endpoint is `https://gameslike.co/api/mcp`.

## Tools and access

| Tools                                                                       | Access                                                       |
| --------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `search_games`, `find_similar_games`, `browse_releases`, `find_party_games` | Anonymous                                                    |
| `recommend_from_library`, `list_wishlist`, `get_personal_brief`             | Explicit `library:read`                                      |
| `set_wishlist_entry`, `set_game_preference`                                 | Separate explicit `library:write`                            |
| `get_group_games`                                                           | Explicit `groups:read` and verified group/session membership |

The MCP Apps resource `ui://gameslike/game-cards.html` shows real artwork,
canonical GamesLike links, release precision, current Steam Deck evidence,
completion estimates when available, and actions for the exact displayed game.
More like this replaces the displayed picks. Write controls require a write grant.
Wishlist and taste changes affect GamesLike; they never modify Steam.

The personal brief contains bounded wishlist updates, upcoming releases,
discoveries, and one lightly played backlog pick. Ownership and wishlist freshness
are independent. A Loved source supports a similarity recommendation; a card
claims the candidate was marked Loved only when that candidate has the choice.
Missing dates, coverage, playtime, capacity, and compatibility remain unknown.
Sexual or explicit adult games and unclassified content are excluded.

## Limits

PC platform flags do not establish console support. Catalog tags do not prove
that combat or violence is absent, or that a game's presentation is truly 3D.
Ambiguous editions need a user choice. Preferences must be reapplied when changed;
the service does not relax them to fill a shortlist. Scores are not confidence
percentages.

Steam sign-in verifies identity and does not unlock private game details. Accounts
require age 18. Public discovery follows the website terms: age 13 or the local
minimum, with parental permission where required.

Reads do not refresh Steam, subscribe, send email, schedule a newsletter, or mark
games seen. Email briefs use the website's separate confirmed opt-in and Mailwerk;
automatic ChatGPT delivery is unsupported. Purchases and account deletion are
website/store actions, outside the MCP tools.

## Public review package

This portable package contains `plugin.json`, `mcp.json`, this README, the actual
GamesLike icon, and `skills/game-discovery/SKILL.md`. Private development App IDs
and bindings are excluded. Six positive and three negative review cases are
included in the manifest. Reviewer credentials belong only in secure dashboard
fields. The dedicated reviewer sign-in is `https://gameslike.co/chatgpt/review`;
it supplies clearly labeled sample library data and does not require real Steam
credentials, a mailbox, or MFA.

The [review walkthrough](https://gameslike.co/chatgpt/review/gameslike-1.0.5.mp4)
is an edited recording of real ChatGPT interactions: version 1.0.5, visual discovery,
the More like this control, and a sample wishlist/brief with truthful freshness
and broad-date limits. It contains no real library or email send. CSP enforcement
was enabled for native card verification. A recording proves its observed flows,
not that all review prompts or arbitrary future host responses pass.

Run review cases against the exact saved submission version. Draft upload,
submission, approval, and publication are separate states; the OpenAI portal is
the source of truth. This package does not claim a public directory listing or
proactive recommendations.

## Local verification

Use the existing credential-free fixture runner and real HTTP MCP client:

```sh
pnpm exec playwright test --config playwright.brief.config.ts
node tests/support/brief-server.mjs --fulltest
```

The suite covers scopes, subject isolation, explicit writes, unsafe content,
release precision, wishlist provenance, groups, and card controls. The Loved
regression checks recommendations from Loved seeds and a directly Loved backlog
candidate through the real MCP endpoint. Reports include reproducible JSON evidence.

The server reuses the existing Typesense vectors, catalog, and auth SQLite owners.
No MCP tool generates embeddings or calls a separate paid AI API. Public server
deployment and the private development installation do not establish approval
or public availability.

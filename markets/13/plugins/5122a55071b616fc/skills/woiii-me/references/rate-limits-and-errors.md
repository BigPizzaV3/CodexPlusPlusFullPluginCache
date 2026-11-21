# Rate limits and errors

Discogs allows about 60 requests a minute per network address, and every WOIII.me user's requests share one address. WOIII.me paces itself to stay under that limit.

- **"WOIII.me is pacing requests to Discogs… try again in N s"** (`rateLimited`, `retryAfter`): our own pacing, not a Discogs failure. Tell the user, offer to retry after N seconds, and don't call again immediately or in a loop.
- **Discogs rate limit** (`retryAfter` from Discogs): the same: wait, then one retry.
- **Partial results** (`partial: true`, a coverage or "could not be fetched" note): present what is there, say what is missing, and don't crown a winner from a thin set.
- **Not found**: the id is wrong or the release was removed; ask for the link.
- **403 on collection or wantlist**: the list is private on Discogs; say so.
- **Not linked / re-link needed**: the host shows the sign-in; never ask for a token or password in the conversation.
- A survey costs about 8–12 Discogs requests the first time (up to 15 with 8 pressings); repeating it within a few hours is free because results are cached. Switching lens is always free.

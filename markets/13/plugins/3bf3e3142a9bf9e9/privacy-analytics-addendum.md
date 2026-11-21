# Privacy policy addendum: ChatGPT plugin analytics

**Status: draft, not published. Don approves the wording, then the main
session publishes it.** LAN-1244 requirement 10.

## Why this is needed

Section 6 of the published policy ("Langua for ChatGPT", published 2026-10-22)
covers the hand-off data and the 7-day expiry. It says nothing about
analytics, because there were none.

LAN-1244 requirements 1 and 2 add them. The Worker now sends two events to
PostHog for every plugin interaction. OpenAI's plugin guidelines ban "tracking
or behavioral profiling, including metadata collection such as timestamps, IP
addresses, or query patterns" unless it is explicitly disclosed, narrowly
scoped and under user control. So the policy has to say what the events hold,
why, and for how long, **before** either requirement ships to production.

Publish the section below as section 6a, or as a new paragraph inside section
6, whichever reads better on the Ghost page. Use
`scripts/ghost-add-chatgpt-privacy.js` as the pattern. Then confirm the
`#privacy-policy` anchor still resolves, because `plugin.json` links to it.

## Draft text

### How we measure the ChatGPT plugin

We count how the plugin is used, so we can tell whether it helps learners. We
do this with two events. They carry no part of your conversation.

**What each event holds.**

- A pseudonymous id for you, and one for the conversation. ChatGPT gives us
  two ids it has already anonymised: one stands for you, one stands for the
  conversation. We hash both with a secret of our own before we store them, so
  what we hold cannot be turned back into either id, and we never ask ChatGPT
  who you are. The id for you is stable, so it does link your plugin activity
  across conversations.
- Which Langua tool ran, and whether it succeeded.
- The language you are learning, and how many cards or phrases the activity
  held.
- Whether a Langua card was shown to you.
- Your country, and the language your ChatGPT is set to. Country only: not
  your city, your region or your location.
- A short code for the single-use link, whenever the plugin creates one for
  you. We record the same code when that link is opened in Langua.

**This connects your plugin activity to your Langua account.** The short code
above is the join. If you open the link while signed in to Langua, that code
appears both in these analytics and against your Langua account, so we can see
that a request in ChatGPT and an arrival in Langua were the same hand-off.
That is the whole purpose of the code, and it means these events are
pseudonymous rather than anonymous: we can go from your Langua account to your
plugin events, and back. Note the code is recorded when the plugin creates the
link, not only when you open it, so it exists even for a link you never use.

**What no event holds.** The words or phrases you asked to save. The situation
you wanted to practise. Anything you typed to ChatGPT, or anything ChatGPT
replied. Your name, your email address or your ChatGPT account. Your IP
address: we switch off IP collection on these events, and we do not log one.

**Why we process it.** To measure the plugin, and nothing else: how many people
use it, which tools they use, which languages, and how many go on to open an
activity in Langua. We do not use it to profile you, to target advertising, to
personalise what Langua shows you, or to train a model. We do not sell it.

**Who else sees it.** PostHog, our product-analytics provider, stores these
events for us as a processor. Nobody else receives them.

**How long we keep it.** 13 months, then the events are deleted. That is long
enough to compare one year with the next and no longer.

**Your controls.** Remove the plugin in ChatGPT and no further event reaches
us. Ask us to delete these events and we will: where you have opened a link in
Langua we can find them from your account, and otherwise you can give us the
approximate dates and the activity. Deleting your Langua account removes the
link codes that connect it to these events.

## What the implementation actually sends

Kept here so the next person can check the text against the code, not against
this file. Source: `src/analytics.ts`, `src/tools/handlers.ts`, `src/http.ts`.

`chatgpt_tool_called`, one per tool call:

| Property | Value |
| --- | --- |
| `distinct_id` | `chatgpt_user_<32 hex>`, a salted hash of `_meta["openai/subject"]` |
| `chatgpt_conversation` | `chatgpt_conv_<32 hex>`, a salted hash of `_meta["openai/session"]` |
| `tool`, `handler` | tool name the model called, and the handler that ran |
| `language` | target language, for example `portuguese` |
| `kind` | `deck`, `lesson` or `scenario` |
| `item_count` | number of deck items or key phrases |
| `outcome` | `ok`, `ok_matched`, `error_validation`, and so on |
| `ms` | handler latency |
| `variant` | routing-study metadata variant, `v00` in production |
| `token_hash` | `create_langua_link` only: the first 16 hex characters of the activation token's SHA-256, matching `ChatgptActivation#token_hash` |
| `country` | two-letter code from `_meta["openai/userLocation"].country` |
| `locale` | `_meta["openai/locale"]`, for example `en-GB` |
| `$ip` | `null` |
| `$geoip_disable` | `true` |

`chatgpt_card_shown`, one per card render: `kind`, `variant`, `country`,
`locale`, the same `distinct_id` and `chatgpt_conversation`, `$ip: null`, and a
`uuid` and `timestamp` derived from the card's envelope so a repeated beacon is
one event rather than many.

Beyond those, each event carries only `$geoip_disable: true`,
`$lib: "langua-chatgpt-worker"` and the PostHog project key. No other field is
sent. `test/analytics.test.ts` asserts that no phrase, title, scenario,
prompt, raw subject, raw session, raw token, city, region, timezone or salt
appears in any payload, log line or card.

### Limits a reader should know about

- **The id is pseudonymous, not anonymous.** See the join above. The text
  discloses it; do not reword it back into "cannot be linked".
- **The `/t/card` beacon is unauthenticated.** The widget runs in an
  OpenAI-controlled iframe and has no credential to present, so the endpoint
  takes any POST. The envelope is sealed with AES-GCM, so nobody can forge one
  or read the ids inside, and the render event's `uuid` is derived from the
  envelope, so re-posting the same one is a single event. Its 10-minute TTL
  bounds the rest.
- **`/mcp` is also public**, as any MCP server must be. Anyone can call a tool
  with a `_meta` of their choosing and create plugin events with a chosen
  country. The salt stops them targeting a *known* person's id, because they
  cannot compute it, but it does not stop event inflation. Treat sudden jumps
  in plugin counts as suspect, and raise it as separate work if the numbers
  start mattering commercially.

## Checklist before publishing

- [ ] Don has approved the wording.
- [ ] The 13-month retention is set on the Langua PostHog project, or an
      explicit deletion job exists. A policy promise with no mechanism behind
      it is the LAN-1244 version of the read-only-DB doc that enforced
      nothing.
- [ ] Published at <https://languatalk.com/blog/terms-and-privacy>, and the
      `#privacy-policy` anchor still resolves.
- [ ] Only then: `npx wrangler secret put POSTHOG_API_KEY --env production`,
      `ANALYTICS_SALT`, and `npx wrangler deploy --env production`.
- [ ] Re-run the plugin portal scan after the production deploy and confirm it
      still reports no findings.

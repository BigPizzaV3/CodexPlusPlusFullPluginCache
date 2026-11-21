---
name: manage-tracking
description: Use when the user wants to see or change what ExtensionDash tracks for one of their extensions, including adding or removing tracked extensions, keywords (search terms) or competitor listings, or showing the current tracking setup. Requires an ExtensionDash account connection. Uses list_extensions, add_extension, remove_extension, list_keywords, list_competitors, search_catalog, add_keyword, remove_keyword, add_competitor, remove_competitor and list_scrape_runs.
---

# Manage tracking

Show and change the user's tracked extensions, keywords and competitors.

## What the server supports

Six write tools: `add_extension`, `remove_extension`, `add_keyword`,
`remove_keyword`, `add_competitor` and `remove_competitor`. Everything else is
read-only. Plans, passwords and settings are changed on https://extensiondash.com.

Removing an extension deletes its notes, keyword tracking and competitor
configuration across both stores. Re-adding does not restore that configuration.
Shared store listings, collected metrics/rank history and other accounts'
tracking remain.

These tools need an account. If a call answers that "this connection has no
account", follow
[connecting an account](../review-performance/references/connecting-an-account.md).
Never ask for a token in the chat.

## Add or remove a tracked extension

- Start with `list_extensions`: it reports the existing extension IDs and
  `tracking_limits`, including plan, used slots, cap and remaining slots.
  Null caps mean unlimited. An empty account can be set up directly here.
- To add, use the user's Chrome Web Store or Firefox Add-ons URL. If only a
  name is given, use `search_catalog` in the requested store, show plausible
  matches with URLs and users, and clarify any ambiguity before writing.
- Call `add_extension` with `chrome_url`, `firefox_url`, or both. Supply both
  only when they represent the same product: together they count as one
  tracked extension. The result gives its `extension_id` as `extension.id`.
  Repeating the same URLs is a no-op, including at a cap. A matching product
  can gain its missing store; existing keywords are adopted. Conflicting
  listings/groups are refused rather than silently replaced or merged.
- To remove, resolve the user's chosen target with `list_extensions`, then
  call `remove_extension` with that ID. Explain that notes and tracking
  configuration are deleted. Never choose a target just to free a slot.

## Plan limits

Use the response's effective limits rather than assuming the account's plan.
Free currently allows 1 tracked extension, 10 keywords per extension and 5
competitors per store. Premium allows 10, 50 and 20 respectively. Keywords
count distinct (term, locale) pairs across stores; competitors count per store.

On a plan-limit error, stop that unchanged request. The structured error
reports the plan, resource, used, limit, remaining, pricing URL, and the
extension/store where applicable. Explain the cap and offer the pricing link.
If the user wants to replace existing tracking, show the relevant inventory
and ask which item to remove. Never automatically delete an extension,
keyword or competitor to make room, and never retry unchanged. Removing a
Firefox competitor does not free a Chrome competitor slot. Do not suggest
creating another account or silently changing the user's plan.

## Resolve before writing

1. **Extension.** Call `list_extensions` and match the user's wording to
   `name`.
   - If exactly one extension exists, use it and say which.
   - If the name is ambiguous or missing and there are several, ask.
     Never write to a guessed extension.
2. **Keyword scope.**
   - A keyword is a (term, locale) pair. `locale` defaults to `en`.
   - `add_keyword` adds the term in every store the extension is listed in;
     the response's `stores` says which.
   - `remove_keyword` removes the (term, locale) from every store.
   - If the user names a language or market ("track it in German"), pass
     that locale, such as `de` or `pt-BR`.
3. **Competitor identity.**
   - A competitor is a (store, external_id) pair. The id is Chrome's
     32-letter id or Firefox's AMO slug.
   - If the user gives a name, resolve it with `search_catalog` (one store
     per call).
   - If several listings plausibly match, show them with users and URL and
     ask.
   - Each store has its own roster, so a Chrome and a Firefox version of
     the same product are two competitors.
4. **Check what already exists.**
   - Call `list_keywords` before adding keywords. If a (term, locale) is
     already tracked, report it as already tracked instead of re-adding.
   - Call `list_competitors` before adding competitors. Skip ones already
     on the roster.
   - Terms are lowercased and whitespace-squished by the server, so compare
     normalized forms.

## Executing changes

- **Clear requests.** When the request names the extension (or only one
  exists) and the items, make the changes without asking for confirmation
  again.
- **Ambiguous requests.** When the target or scope is ambiguous, ask once,
  listing the specific choices.
- **Never write unasked.** Do not add a keyword or competitor the user did
  not ask for, including ideas that came up during research. Offer them;
  wait for a yes.
- **Limits.** If the server answers with a plan limit, stop for that item
  type. The message names the limit and, for competitors, the current
  roster. Follow the plan-limit guidance above; do not remove automatically
  or retry unchanged.
- **Removals.** Removing a keyword or competitor stops tracking but keeps
  recorded history, and re-adding later restores it. Say so when removing.
- **Wrong-language removal.** If `remove_keyword` says the term was not
  tracked in that locale, its message lists the locales it is tracked in.
  Relay that and ask whether to remove one of them.

## After adding: pending results

New tracking schedules background fetches; cached data may already exist.

- **Extensions.** `add_extension` returns the new or existing extension and
  current plan usage. Use `get_extension` for metrics and `list_scrape_runs`
  for fetch status with its ID. Use `add_keyword` to start recording ranks.
  Adding an extension alone does not select search terms.

- **Keywords.** `add_keyword` returns rows whose `status` is `"pending"`
  until a background rank fetch lands. Then `status` becomes `"scanned"`.
  A pending row may still show an old position from earlier tracking;
  that is not the new result.
- **Competitors.** `add_competitor` returns `status: "pending"` until the
  listing fetch lands. Then it becomes `"scraped"`.

Polling rule:

- Check at most 3 times, roughly 20–30 seconds apart, using
  `get_extension`, `list_keywords` or `list_competitors` for the same `extension_id`.
- Between checks, `list_scrape_runs` with `extension_id` shows whether the
  fetch is running, succeeded or failed.
- If it is still pending after that, stop. Tell the user the fetch is
  queued and they can check later with the same request. Do not keep
  polling, and do not promise a time.
- If `list_scrape_runs` shows a failure for the item, report it as a failed
  fetch with its `error_message`, not as a ranking. Do not promise when it
  will succeed.

## Showing the current setup

For "show my tracking", give a table per extension built from `list_keywords`
and `list_competitors`:

- **Keywords:** term, locale, store, status, position with `depth_scanned`.
- **Competitors:** name, store, users, rating, status.
- The plan limit from `list_competitors`' `limit_per_store` (null means no
  limit).
- Any pending or failed items.

## Report

End every change with a short ledger:

- **Added:** each item and the stores it landed in.
- **Already tracked:** skipped, no change.
- **Removed:** each item.
- **Failed:** the item and the server's reason, for example a limit.
- **Pending:** what is still fetching and how the user can check later.

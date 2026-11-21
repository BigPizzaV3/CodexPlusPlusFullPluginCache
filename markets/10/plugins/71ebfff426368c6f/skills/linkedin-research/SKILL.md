---
name: linkedin-research
description: Use when the user wants to find people on LinkedIn, look up or research a LinkedIn profile, compare professional backgrounds, or draft an introduction from profile information. Research does not authorize sending messages or connection requests.
---

# LinkedIn research

Read [account access and limits](../../references/account-and-limits.md) before using tools.

Use `linkedin_search_people` with `keywords` or a LinkedIn people-search `url` supplied by the user. A search URL preserves its filters. Use `network_distance` when the user specifies connections or degree. Each page costs a search; request at most 25 results per page and follow `next_cursor` only as needed.

Search uses the first LinkedIn account and its network unless `account` names another one. Pass `account` when the user asks about a specific account's network or limits, and to `get_profile` whenever another network's account is also connected (or `provider: "linkedin"` with one LinkedIn account).

Use returned `person_id` values for later calls. Retrieve selected profiles with `get_profile`, passing the ID or the public identifier after `linkedin.com/in/` as `user_id`. A profile lookup counts as a profile view.

When names match more than one person, use employer, role, location, and profile URL to resolve identity before preparing outreach. Keep unresolved matches explicit.

Summarize the fields relevant to the user's question. Link returned profile URLs. Distinguish observed information from inferred fit or interests. Missing fields are unknown. Summaries, experience, education, and skills may be truncated, so do not describe them as a complete history.

For ChatGPT research requests that require the compatibility tools, `search` accepts `query` and returns record IDs such as `person:<id>`. `fetch` accepts `id`. It can retrieve a person record or a conversation identified by `chat:<id>` when that chat ID is already known. `search` searches people and does not search inbox messages. Prefer the specific LinkedIn tools for inbox triage and profile comparisons.

Draft introductions from verified professional context. Research does not authorize invitations or messages. For sending, use [LinkedIn outreach](../linkedin-outreach/SKILL.md).

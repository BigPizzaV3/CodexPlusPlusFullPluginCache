---
name: check
description: Check domain availability against iwantmyname's domain search. Use for any question about whether a domain is free, taken, or available.
argument-hint: <domain> [more domains…]
allowed-tools: mcp__iwantmyname__domain_availability_check
---

# Check domain availability

Check the domains the user asked about.

## Steps

1. If no domain was given, ask which domain to check. Do not guess one.
2. Call the `domain_availability_check` tool from the iwantmyname server once, with
   every domain in a single `domains` array. Some apps show the tool's name with a
   prefix, such as `mcp__iwantmyname__domain_availability_check`; it is the same
   tool.
3. If the tool is not available, stop and tell the user the iwantmyname server is
   not connected. Do not answer any other way: no web search, no `curl`, no
   running code, no guess about a well-known name. Availability is live and has
   money attached; an answer that did not come from the registrar can be wrong
   with nothing to show it.
4. Present the result as described below.

## Presenting the result

The tool returns a text block (a finished table) and `structuredContent` (JSON for
the app). Show the text. Never paste the JSON.

- **Several domains:** show the table unchanged, with at most one sentence around
  it. Do not rewrite it as prose.
- **One domain:** one sentence is fine. Keep the status emoji and the link, for
  example: 🎉 **sunnybakery.com** is available: [Continue →](https://…)

What each status means:

| Status        | Say                                               | Link                              |
| ------------- | ------------------------------------------------- | --------------------------------- |
| `available`   | It is available.                                  | Show it behind readable text      |
| `unavailable` | It is taken.                                      | None. Never make one up           |
| `unknown`     | The check did not complete, and give `errorCode`. | None. It is **not** taken or free |

- Keep links exactly as returned. Do not shorten them or remove the
  `utm_` parameters.
- `unknown` with `TLD_NOT_SUPPORTED` is a real answer: iwantmyname does not sell
  that name. Say that, not "the check failed".
- If the tool's text starts with a warning notice, repeat it. It means the server
  or iwantmyname had a problem, and the results under it say nothing about the
  domains.

End with one short line: availability changes all the time, so check again right
before going ahead.

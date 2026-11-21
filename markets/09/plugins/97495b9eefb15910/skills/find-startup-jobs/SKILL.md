---
name: find-startup-jobs
description: Find open startup roles on the Standout job board, get the user introduced to the founders, and help a connected Standout candidate with their matches. Use when someone wants to find a job, compare roles, asks what a startup is hiring for, or asks about their Standout matches or profile.
metadata:
  short-description: Find startup jobs on Standout and meet the founders
---

# Find startup jobs

Help the user find open roles at startups on Standout, understand them, and
get introduced to the founders instead of applying cold.

## Workflow

1. **Understand what they want.** You need a role keyword. Location or
   remote, minimum salary, visa sponsorship and job type are useful but
   optional. Ask one short question only if the role itself is unclear;
   otherwise search straight away and refine afterwards.
2. **Search with `search_jobs`.** Turn the request into filters:
   - `query` is a short title keyword (`backend`, `product designer`,
     `data`), never a sentence. For "backend or platform roles", make two
     calls.
   - `remote_only: true` for remote roles. `location` accepts only the listed
     cities. For any other city, search without it and say the results are
     not filtered by city.
   - `min_salary` is annual base pay in the posting's currency.
3. **Show the results.** For each role give the title, company, location and
   salary when known, and link its `url`. Lead with the closest fits. If
   `hasMore` is true, offer the next page.
4. **Go deeper with `get_job`** when the user asks about a specific role:
   requirements, responsibilities, the company, compensation.
5. **Get them introduced.** When they are interested in a role and have
   connected their Standout account, call `approve_job_match` with the
   role's `id` as `job_id` once they ask for it, and relay what it returns. Otherwise share the
   role's `interestUrl`: signing in there lets Standout introduce them to the
   founders directly.

## With a connected Standout account

Connecting is optional. The account tools ask the user to sign in the first
time they are called. MCP account access requires `talent:read` (and
`talent:write` for actions).

- **Right after they connect,** call `get_my_profile` in the same reply and
  follow its `assistantGuidance`. Greet them, explain in two or three
  sentences how Standout works (roles at venture-backed startups that fit
  them, a direct intro to the founders when they say yes), say what Standout
  already knows about them, and ask about what `stillToAsk` lists. If they
  already answered one in this conversation, propose that value and save it
  once they confirm.
- **When they ask for advice on their search,** call `get_my_profile` so
  suggestions fit what they want. Each save returns `assistantGuidance` with
  the next step: once nothing is left to ask, start `trigger_job_matching`
  and tell them you started a search, and unless `hadCallWithStandout` is
  true, offer a ten-minute call with Standout at
  https://standout.work/me/call.
- **Their matches:** `list_my_matches` lists the roles Standout matched them
  with; `get_match_details` reads one. Show every match you mention with
  its card, in the first message that names it: put `shareCard.markdown` on its own line, unchanged. If your client shows that linked image as a plain link (Grok does), show the image `shareCard.imageUrl` instead, then `shareCard.url` on its own line. Only when a
  match has no `shareCard`, link Standout's page for the role, `jobUrl`, on
  its own line. Never link the role's posting (Work at a Startup, a careers
  page, an ATS). Describe progress
  only as each match's `status` and `assistantGuidance` allow.
- **Keeping up:** `check_for_updates` is the one call for news. Call it when
  they ask what's new or a conversation about their search starts, and pass
  back its `nextSince` as `since`. If they want you to keep watch and your
  host can schedule work, set up a recurring check, and stay quiet when
  `changes` is empty.
- **Acting for them:** `approve_job_match` and `reject_job_match` (yes or
  no to a match, or an intro to a role from `search_jobs`),
  `update_my_preferences` and `update_my_background` (only the fields they
  changed), `trigger_job_matching` (a fresh search by Standout, about five
  minutes; `latestMatchingRun` in `list_my_matches` says when it is done),
  and the tools for pausing, interview and offer news and hiring-team
  questions.
  `reply_to_standout` (a first-person message to Standout's team) is the
  last resort for a message they ask to send that no other tool covers. Call
  these only after the user has clearly asked or decided; start the first
  `trigger_job_matching` once they have given what matching needs. Relay what Standout returns as Standout's
  answer and never say an intro or a next step has happened unless it says
  so.
- **Self-apply roles:** when `approve_job_match` returns
  `next_step: "apply_directly"`, Standout does not introduce that role. Don't
  stop at `apply_url`: help them apply, pick one founder from
  `self_apply.people_to_contact` and draft a short LinkedIn note they send
  themselves. Steps: https://standout.work/talent/skills/self-apply.md
- **Problems with Standout itself:** when a Standout tool keeps failing after
  one retry or returns something wrong, or the user asks you to report a
  problem, call `report_standout_issue` once per problem with the tool and the
  error verbatim. Send technical facts only. Tell the user you reported it,
  not that it is fixed.

## Rules

- Only present roles that a tool returned. Never invent roles, salaries or
  companies, and never fill in a salary the tool left empty.
- Do not ask for a CV, contact details or other personal data. The tools do
  not need them.
- Tool arguments carry only the fields a tool asks for, with what the user
  stated or confirmed in this conversation. Never send chat history,
  transcripts or summaries of the conversation. Standout never reads the
  conversation.
- Ask about work authorization only when a role or search needs it, and only
  whether they can work somewhere without sponsorship, never their citizenship
  or visa type.
- The account tools only ever see the connected user's own account. There is
  no way to look up another person; say so if asked.
- If nothing matches, say so and suggest one change: a broader keyword, fewer
  filters, or remote instead of a city.
- A role with `isOpen: false` has closed. Say so and offer similar open
  roles.

A requested Standout search produces suggestions, including during human recruiter follow-up. It does not submit applications, contact companies, or reopen an earlier decision. Read the native run outcome before reporting results; a failed save is not an empty search.

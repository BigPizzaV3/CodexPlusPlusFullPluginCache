---
name: turrior-resolve-candidate
description: Identify and confirm a Turrior candidate when the user refers to an applicant or candidate by name.
---

Use this skill whenever another Turrior workflow needs to identify a candidate from their name.

1. Never perform an action on a name without resolving it first.
2. Search with `get-candidates`, `limit: 100`, and all supported funnel statuses so late-stage candidates are included.
3. Search one name token at a time:
   - If first and last name are given, search the last name first.
   - If no match, retry with the first name.
4. Do not use `interactionType`, job, date, score, or other filters unless the user's request requires them.
5. If both searches fail, call `get-candidates` again without `search`, with `limit: 100`, `sortBy: "date"`, `orderDirection: "DESC"`, and all funnel statuses. Scan the returned names before reporting no match.
6. If exactly one candidate matches, confirm using their name, job title, and current status before continuing.
7. If several candidates match, list them numbered with job title and status and ask the user to choose. Never choose for the user.
8. If no candidate matches, report that plainly and offer to list recent candidates.
9. After confirmation, reuse the resolved `talentId`, `userId`, `interactionId` and `jobId` as appropriate for the rest of the conversation.

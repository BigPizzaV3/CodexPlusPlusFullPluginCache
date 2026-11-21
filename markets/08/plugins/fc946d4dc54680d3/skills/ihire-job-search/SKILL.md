---
name: ihire-job-search
description: Search and compare current, industry-specific iHire job openings, inspect individual job details, and provide native iHire apply links. Use when a user asks to find, browse, recommend, compare, view, or apply to jobs using criteria such as title, skills, industry, company, location, work arrangement, salary, posted date, experience level, or employment type.
---

# Job Search by iHire

Use iHire's MCP tools for live job data. Never invent a posting, job ID, job detail, or application URL.

## Search workflow

1. Extract the user's stated search criteria without adding unstated requirements. `SearchJobs` requires at least one search constraint; ask one concise follow-up question only when the request provides none.
2. Call `SearchJobs` with the filters that clearly map to the request. Use `keywords` for natural constraints that do not map cleanly to a dedicated field. Avoid over-constraining the search.
3. After a successful search, call `RenderJobCards` once with the ordered, unique `jobIds` returned by `SearchJobs`. Pass IDs only, never full job objects or invented IDs, and pass no more than 25.
4. Briefly summarize the result count and the most important applied filters. Let the rendered cards carry the individual listing details instead of repeating every field in prose.

For "more jobs" or alternatives, preserve the user's existing criteria and use pagination or `excludeJobIds` so previously shown jobs are not repeated. If no jobs match, say so and offer a targeted relaxation such as a wider radius, an older posting window, or fewer optional filters; do not silently broaden the search.

## Details, comparison, and applying

- Call `GetJobDetails` when the user asks about a specific posting or requests a comparison that needs more information than the search result provides. Use a positive `jobId` obtained from iHire results or supplied explicitly by the user.
- Compare only fields returned by the tools. Clearly label unavailable information and avoid inferring salary, benefits, qualifications, work arrangement, or fit.
- Call `GetApplyLink` when the user asks to apply, open the posting, or continue to iHire. Present the returned iHire URL and explain that it opens the job on iHire, where the user can review the posting and continue toward applying. Do not imply that opening the link submits an application or necessarily opens a specific application step.; the tool does not submit an application.

## Boundaries and failures

- When iHire is connected and the user wants actual current openings, prefer these tools over general web search unless the user asks for another source.
- Do not claim a job remains available beyond the latest tool response.
- If authorization is required, ask the user to connect or reauthorize iHire, then retry only after authorization succeeds.
- If a tool fails or a job is unavailable, state that plainly and do not reconstruct missing data from memory.
- Do not expose raw tool payloads when a concise user-facing result is sufficient.

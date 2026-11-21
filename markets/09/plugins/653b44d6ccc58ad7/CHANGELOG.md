# Changelog

All notable changes to the RolePark plugin for Claude are listed here. The version matches `version` in `.claude-plugin/plugin.json` (Claude) and in the root `plugin.json` (ChatGPT and Codex); raise both with every release.

## [1.5.3] - 2026-10-20

### Fixed

- ChatGPT review: exactly five positive test cases, as the review portal requires; the vacancy draft and vacancy analytics cases are left out. The tools and workflows are unchanged.

## [1.5.2] - 2026-10-20

### Changed

- `create-vacancy`: after a vacancy is changed, the workflow explains that RolePark sends the changed vacancy fields to its postings on Djinni, Jobico, Work.ua and robota.ua by itself, in the background and without using a publication, except values set separately for a board in `options` (they take priority over the vacancy) and a salary in a currency the board doesn't take (Djinni takes USD; Work.ua and robota.ua take a public salary in UAH). Those are changed with `publish_vacancy_to_boards` and only the changed `options` fields: the other values stay, `null` removes a field, and the reply shows the saved values (RolePark merges them since 20 October 2026). The workflow no longer says a posting "was updated", and checks the posting's status on request, because the background update can fail or send a Djinni post to moderation again.
- README (EN and UA): with a tool allowed permanently ("Allow always"), emails and publications "can go out" without a separate question, instead of "go out"; the `publish_vacancy_to_boards` description says that vacancy changes reach the postings by themselves, with the same exceptions, and that for a posting already live on Work.ua or robota.ua the tool updates its fields, including the board's own ones, without using a publication.

### Fixed

- README (EN and UA): the manual path for adding the RolePark connector in Claude now has every step from Anthropic's help: **Continue** after the URL, **Continue** after the detected authentication settings, a sign-in option under **Authentication** and **Use Claude's published identity (Recommended)** under **OAuth client**, then **Add**.

## [1.5.1] - 2026-10-19

### Fixed

- ChatGPT review test cases: the expected result of the first case names the interview with Maya Chen as it is in the review company (12 Jan 2027, 11:00 Kyiv time) instead of a date that had already passed, and the Liam Walsh case asks for a note with a new text, because the old one is already on his card. The tools and workflows are unchanged.

## [1.5.0] - 2026-10-16

### Changed

- Confirmation, said honestly: the skills still show each change and wait for the user's yes, and the README and the ChatGPT listing now explain that this is an instruction to the AI, not a lock in RolePark. Whether Claude or ChatGPT also asks before a tool call depends on the assistant's settings ("Allow always" in Claude, the app's permissions in ChatGPT); RolePark carries out an allowed call at once; "Make changes" allows the calls and is not a separate confirmation of each action. For emails to candidates and publications, ask to see the text first and give an explicit yes.
- Job boards: on Djinni the assistant publishes; on the paid boards Work.ua and robota.ua it does not publish. It shows the posting's status, the cost in publications and a link to the vacancy's job board panel in RolePark, and updates a posting that is already live there without using a publication. `create-vacancy` follows the same rule and never tries to publish on a paid board.
- AI agents in a company that signed up for RolePark by itself are on from the start with View and changes; an admin can switch them off or choose View only. README and the ChatGPT listing no longer say they are off by default.
- README (EN and UA): all 42 connector tools (23 read, 19 write), with the meaning-based `search_candidates_semantic` added; the RolePark connector is still under review in the Claude directory, so the README shows how to add it by hand as a custom connector (Customize → Connectors → Add custom connector, `https://rolepark.com/api/mcp`).

## [1.4.0] - 2026-10-08

### Added

- The full hiring flow through the RolePark connector (22 read and 19 write tools): the text of a candidate's CV, logged on every read and not shown while the candidate is anonymized; the company's team and stage templates; applications and incoming applications with the candidates' screening answers and knockout results, and accepting or declining incoming applications; email templates and emails to candidates; candidate profile updates and tags; interview feedback, scorecards, rescheduling and cancelling interviews; vacancy statistics; publishing a vacancy on Djinni; the company profile, logo and cover image.
- `review-applications` skill: incoming applications with screening answers, a proposal for each, accept or decline after a yes.
- `email-candidate` skill: a template or drafted email with the exact preview; sent only after a yes, and it can't be recalled.
- `interview-feedback` skill: a fair scorecard from the user's notes, the team's feedback, and rescheduling or cancelling an interview with confirmation.
- `vacancy-report` skill: funnel, conversion, days in each stage and source effectiveness of a vacancy.

### Changed

- `shortlist`, `interview-prep` and `review-applications` read the CV text to check the must-haves and prepare questions.
- `create-vacancy` finds the recruiter and the hiring manager by name, lists the company's stage templates, clears fields with `null`, offers Djinni after publishing, and tells the user when candidate emails on closing are paused.
- `pipeline-update` uses RolePark's analytics numbers when the user can see them. Custom stages are taken from the pipeline, because the analytics count only the standard ones.
- `review-applications` lists the valid decline reasons; `interview-feedback` submits scorecards without drafts, knows the interview durations and the rules for moving or cancelling, and reports the daily email limit; `email-candidate` knows the `{{position}}` variable.
- README and the ChatGPT listing: every kind of change is listed among those Claude confirms first, and the listing no longer says the assistant can't change settings (it can change the company profile).
- README: the full list of tools and the new workflows; ChatGPT listing, capabilities, release notes, Ukrainian translation and a read-only review test case for vacancy analytics.

## [1.3.0] - 2026-10-08

### Added

- Vacancies through the RolePark connector's new `create_vacancy`, `update_vacancy` and `set_vacancy_status` tools (12 read and 9 write tools in total). A new vacancy is always an unpublished draft; publishing on the company's career page, pausing and closing follow the same rules and plan limit as in RolePark (3 published vacancies on the Free plan).
- `create-vacancy` skill: turns a job description or a client's message into a vacancy. It drafts the fields, asks only for what is missing, checks for an existing vacancy, shows a confirmation card and creates a draft after a yes; it publishes only after a separate yes. It also covers editing, pausing and closing, with what closing does to open applications and scheduled interviews. It can add yes/no screening questions for applicants (up to 10, with deciding ones that reject a non-matching answer automatically).
- README: a list of all RolePark tools, in English and Ukrainian.

### Changed

- ChatGPT listing: description, capabilities, release notes and the Ukrainian translation mention vacancies; a review test case creates a vacancy draft without publishing it.

## [1.2.4] - 2026-10-03

### Changed

- ChatGPT listing: category back to Productivity (Business is not a dashboard category); reviewer demo recording added.

## [1.2.3] - 2026-10-03

### Changed

- ChatGPT listing category: Business (recruiting and hiring) instead of Productivity.

## [1.2.2] - 2026-10-03

### Changed

- The plugin source is now public at https://github.com/IhorIsFuture/rolepark-plugin; `repository` in both manifests points there.

## [1.2.1] - 2026-10-03

### Fixed

- Who is emailed when a candidate moves to offer, hired or rejected: the vacancy's recruiter and hiring manager (except whoever made the move and anyone who turned these notifications off), not the candidate. The candidate is emailed only if interviews are cancelled together with the move. `shortlist`, the README (EN and UA) and the ChatGPT review test case no longer say a rejection emails the candidate.
- Stage order: `schedule_interview` may move the application forward to the interview's stage as the company's stage-order rule allows, under the default rule only when that stage is the next one. `shortlist` and the ChatGPT review test case say so instead of assuming any stage can be reached.

## [1.2.0] - 2026-10-02

### Added

- Packaging for the ChatGPT and Codex plugin directory in the same repository: a portable root `plugin.json` (Agent Plugins 1.0.0) with the OpenAI listing, review test cases, release notes and a Ukrainian translation under `extensions.com.openai`, and a root `mcp.json` with the same RolePark server (`https://rolepark.com/api/mcp`, Streamable HTTP). The Claude manifest and `.mcp.json` are unchanged.
- Listing images in the assets folder: light and dark logos, a large logo and four screenshots.

### Changed

- Skills use provider-neutral wording, so they read the same in Claude, ChatGPT and Codex. The "not connected" hint names where to connect in each product.
- Each skill states that the user's explicit request about format, scope or order comes first, while the access, confirmation, fairness and data rules still apply.

## [1.1.0] - 2026-10-02

### Added

- Interview scheduling with the connector's new `schedule_interview` tool. `shortlist` offers to schedule interviews for candidates it moved into an interview stage, and `interview-prep` can schedule one when none exists yet. Claude confirms the exact time with the time zone, duration, type and interviewers first, warns that RolePark sends the usual invitations to the candidate and interviewers, and shows conflicts instead of retrying when someone is busy.

## [1.0.0] - 2026-10-02

### Added

- RolePark connector reference (https://rolepark.com/api/mcp, OAuth). It is the same server as the RolePark listing in the Connectors directory, so people who have both see one set of tools.
- `briefing` skill: today's interviews, due and overdue tasks, new applications and stuck candidates, with what to do first.
- `shortlist` skill: reviews early-stage applications against the vacancy's requirements, gives reasons and risks, and proposes stage moves that run only after confirmation.
- `interview-prep` skill: an interview brief with a requirements check, earlier feedback, tailored questions and things to verify.
- `find-candidates` skill: skill matching plus a boolean CV search in the company's own database, with an explanation of each match.
- `add-candidate` skill: creates a candidate from a pasted CV or text after a duplicate check and a confirmation card, and can add them to a vacancy.
- `pipeline-update` skill: funnel numbers, bottlenecks and next steps for a vacancy, plus a short update for the hiring manager.

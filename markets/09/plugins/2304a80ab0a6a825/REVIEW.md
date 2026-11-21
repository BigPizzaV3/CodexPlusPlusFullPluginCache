# Plugin review kit

Use this page with the OpenAI plugin submission form. The form's review information is the source of truth for the reviewer sign-in. This page only describes the reviewer account and the expected results.

## Reviewer account

The reviewer signs in with an email and a password. No email code or two-factor step is needed. The account is verified and has finished onboarding. It is on the Free plan.

- Email: `openai-reviewer@emploive.com`
- Password: only in the "Reviewer credentials" part of the submission form. It is not in this plugin.
- Sign in at `https://emploive.com`. In ChatGPT, connect Emploive through OAuth. The Emploive page names the account and asks "Allow ChatGPT to use your Emploive account?". Select Allow.
- Search tools work without an account.

The account has three trackers. All three have email alerts off.

- "Software engineering internships, US"
- "New grad data science, New York"
- "Reviewer remote product roles" (remote, full-time, Product Manager)

A new tracker with email alerts on sends its emails to `openai-reviewer@emploive.com`.

## Test prompts that should use Emploive

| # | Prompt | Expected result |
| --- | --- | --- |
| 1 | Find software engineering internships in the US posted this week. | `search_jobs` runs without sign-in. A card lists internships, newest first, with company, location, pay when listed, and age. Each job links its Emploive job page. |
| 2 | Show me new grad data science jobs in New York. | `search_jobs` with the New Grad level, the Data Science position, and the New York location. A card of matching jobs. |
| 3 | Tell me more about the first job and how to apply. | `get_job` returns the description, pay, and company profile. A signed-in user who finished onboarding also gets the employer link. A signed-out user applies from the Emploive job page. |
| 4 | Email me when new remote product manager jobs are posted. | Without an account, ChatGPT shows the Emploive sign-in. After sign-in, `create_tracker` makes a tracker with email alerts and shows its newest matches. The account already has "Reviewer remote product roles". |
| 5 | What are my Emploive trackers, and what is new on them? | `list_trackers`, then `get_tracker_jobs` for each tracker. Needs sign-in. |

## Test prompts that should not use Emploive

| # | Prompt | Expected result |
| --- | --- | --- |
| 1 | Write a cover letter for a marketing job. | ChatGPT answers itself. Emploive does not write documents. |
| 2 | What is the average salary of a nurse in Texas? | ChatGPT answers itself. Emploive lists job postings, not salary statistics. |
| 3 | Apply to this job for me. | Emploive does not apply to jobs. ChatGPT explains that the user applies on the employer's site. |

## Free plan behavior to check

The reviewer account is on the Free plan. The tools state these limits as facts. They show no prices, no checkout or plan links, and no upgrade prompts.

- Alerts: the fastest alert speed is every 6 hours. If you ask for a faster speed, the tracker uses 6 hours. The tool answer says so in one sentence.
- Alert emails: the plan allows 50 alert emails a month. On 2026-10-29 the account had used 0.
- Filters: the industry, funding stage, and company size filters are not in this plan. A tracker that uses one gets a one-sentence answer that the plan does not include it.
- Alerts inside ChatGPT: the instant tracker event is not in this plan. A request for it gets a one-sentence answer that the plan does not include it. Email alerts continue.

---
name: find-analyst-jobs
description: Find live analyst jobs or AI and machine learning jobs, check whether a company is hiring analysts or AI roles, check a company's H-1B record, find remote analyst roles for a country, or summarise the analyst or AI job market with RealAnalystJobs.
---

Use the RealAnalystJobs tools whenever someone asks about open analyst or data roles (data, business, BI, product, financial, marketing, operations analysts, analytics engineers), open AI and machine learning roles (machine learning, AI and LLM engineers, AI research and applied scientists, MLOps, AI product managers, forward deployed engineers), a company's hiring for either, or which skills, cities and companies those roles involve.

- Job search: call `search_analyst_jobs`. Put title or skill words in `query`, a city or country in `location`, and use `seniority: "entry"` for freshers, graduates and juniors. Use `posted_within_days` for "this week" (7) or "today" (1).
- AI and ML jobs: call `search_analyst_jobs` with `vertical: "ai"`, or with `ai_family` (for example `ml_engineer` for machine learning engineers, `ai_engineer`, `llm_genai_engineer`, `research_scientist`). The AI roles are a separate list from the analyst board.
- One employer: call `company_analyst_hiring` with the company name. Its analyst roles and its AI and ML roles (the `ai` section) are reported apart.
- Market questions: call `analyst_market_stats`, with `location` and/or `query` to narrow it, and `vertical: "ai"` or `ai_family` for AI and ML roles. For AI it also lists the employers with US roles in scope that have an H-1B record.
- H-1B questions ("does X sponsor H-1B?"): call `h1b_sponsor_check` with the company name. It shows the record beside the company's analyst roles and, separately, its AI and ML roles.
- Remote work from a country ("remote data analyst jobs from Nigeria"): call `remote_jobs_from_country` with the country, plus `query` or `seniority` if given.
- Resume fit ("which of these jobs fit my resume?"): call `match_resume_to_jobs` with the full resume text in `resume_text`, plus `candidate_location`, `needs_visa_sponsorship` and any filters the user gave. Present each fit as an estimate, not a hiring prediction.

When answering:
- Link every role with the `url` the tool returned. Never invent roles, companies, salaries or apply links.
- Give counts with the date the tool returned, as live roles on RealAnalystJobs, not the whole job market. Keep analyst and AI counts apart; never add them together.
- If nothing matches, say so and suggest a broader title or place.
- There are no salary averages. Report how many roles post a range, and quote a role's salary only when the tool returned it.
- The app cannot apply for jobs. Point people to the role's page, where the application link is.
- H-1B counts are the employer's USCIS history across all occupations, not a promise for one role. If the tool says a company is not in our data, say exactly that and give the USCIS link; never say it does not sponsor. Report a posting's own sponsorship wording separately from the USCIS record.
- For remote roles, say what each listing states (based in the country, a region that includes it, or worldwide). Never say a role is open to the country unless the listing says so, and treat "no country stated" as unknown, not as anywhere.

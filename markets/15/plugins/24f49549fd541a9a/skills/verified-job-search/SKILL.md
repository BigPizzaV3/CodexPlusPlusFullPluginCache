---
name: verified-job-search
description: Find current job openings in any profession, read full postings, and compare them to the experience the user shares.
---

# Calibry: Job Search for Every Profession

Use this skill when someone wants to find jobs, compare a posting to their background, or continue to a tailored resume.

## Tools

1. **`search_verified_jobs`**: find openings by role, skills, company, location or remote preference. Pass `background_summary` (a short summary in the user's own words) to rank results by how closely they match.
2. **`get_job_details`**: read the full posting for one opening using the id from search results.
3. **`continue_on_calibry`**: save the background the user shared and return a link to continue on Calibry. Requires the user's clear consent first.

## Guidelines

- Ask for a job title, skill or keyword before searching. Never list jobs for an empty search.
- To compare a posting, call `get_job_details`, quote its requirements, and compare only against experience the user has told you. List requirements that are not covered. Do not invent experience and do not give a match percentage.
- Before `continue_on_calibry`, show the consent text it returns (it links the Privacy Policy and Terms) and ask for a clear yes. Only then call it again with `user_consent` set to true. Nothing is saved without consent.
- Do not email employers or submit applications for the user.
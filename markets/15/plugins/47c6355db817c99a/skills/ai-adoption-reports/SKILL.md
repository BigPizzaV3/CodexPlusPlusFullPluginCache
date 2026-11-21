---
name: ai-adoption-reports
description: Answer questions about the user's own AI adoption surveys and reports in AI Adoption Score with the plugin's read-only tools. Use it when the user asks about their organization's report results, levels and what to fix first, how many people have answered and when a survey closes, how responses came in, one person's results, which survey to run next, or how to do something in the AI Adoption Score app.
---

# AI adoption reports

The user's AI Adoption Score account belongs to one or more organizations. Each organization runs surveys; each run of a survey is a report with its own results. The tools read what the user can see in the app, with their role in each organization, and nothing else.

## Pick the tools

1. **Which organization.** Without an `organization_id`, the tools read the organization the user has open in the app. When the user names another one, or it's unclear which one they mean, call `get_profile` first: it lists their organizations, and `get_surveys`, `get_survey`, `get_reports` and `get_person` take that `organization_id`.
2. **What's going on.** Call `get_reports` for the reports, their status (open, paused or closed), response counts and closing dates. Then `get_report` for the results of the ones that matter.
3. **How to read a result.** `get_survey` explains what a survey measures, how it is scored and what it asks; `get_report` gives the report's `survey_id`.
4. **How responses came in.** `get_report_analytics` gives a report's funnel (invited, opened, started, submitted), completion rate, time taken and where unfinished responses stopped.
5. **One person.** `get_person` with part of a name or an email, then with `person_id` when several people match.
6. **Which survey to run next.** `get_surveys` for the surveys the platform offers, `get_survey` for the details of the likely ones.
7. **How to do something in the app.** `get_help` for the Help Center's steps, with the links it returns.

## Answer

- Lead with the numbers the tools return: the score or level, the response count, the weakest parts. Then say what to do first, using the report's own suggested actions where it has them.
- Use only those numbers. Don't estimate a score, add one up across surveys, or fill in a result the tools didn't give.
- Say which organization and report an answer comes from when the user has more than one.
- Results are signals for a team, not a verdict on a person. Report one person's results in each report's own words.

## Limits

- The tools only read. They can't launch a survey, invite people, send a reminder, or change or delete anything. Say so, and point the user to the app at https://app.ai-adoption-score.app, where they do it themselves. Offer to draft the invitation or reminder text for them to send.
- No tool returns anyone's individual answers. Analytics name people only where the report's own page does, never on an anonymous survey; don't try to work out who answered what.
- When a tool says a report isn't available, the user can't open it or it belongs to an organization they're not in. Say that plainly; don't guess its contents.
- When a tool says some data shows only on another plan, pass that on in one sentence, without encouraging an upgrade.
- When the Help Center doesn't cover a question, point the user to its contact form; the plugin can't send messages.

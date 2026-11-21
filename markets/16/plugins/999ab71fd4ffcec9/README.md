# Career Radar Plugin

**Languages:** [English](README.md) | [Português](README.pt-BR.md)

Career Radar is a portable ChatGPT plugin skill for discovering recent remote jobs and evaluating them against a user's resume and career goals. It is designed for on-demand research and scheduled ChatGPT tasks.

> Career Radar never applies to jobs automatically. The user reviews every opportunity and decides what to do next.

## Origin

The idea for Career Radar came from looking for ways to automate the discovery of jobs compatible with a professional profile. During that research, I found [career-ops](https://github.com/career-ops-hq/career-ops), an open-source project that performs a detailed analysis of a job listing and its compatibility with a candidate's profile. It also produces useful metrics to help determine whether an opportunity is a good fit and what should be emphasized in a resume or interview.

Career Radar grew from that inspiration: make the process simpler and automate the initial job search through a ChatGPT web task. The goal is for the scheduled task to find suitable opportunities, apply a minimum compatibility threshold, and provide practical guidance for each application.

## Features

- Discovers jobs from web research instead of requiring pasted job links.
- Prioritizes roles, skills, location, work model, and seniority from the user's profile.
- Verifies the original listing and application status when possible.
- Scores opportunities from 0 to 100 with an explicit rubric.
- Highlights strengths, gaps, risks, duplicates, and recommended next actions.
- Works with a recurring task prompt supplied by ChatGPT or an autonomous agent.
- Onboards each user with an independent resume and preference profile.
- Supports daily or weekly searches with configurable filters and score thresholds.

## Installation

This repository is an Agent Plugins package. For local testing, use the plugin tooling provided by ChatGPT/Codex. For public distribution, create a ZIP containing `plugin.json`, `skills/`, `examples/`, `README.md`, and `LICENSE`, then upload it through the OpenAI Plugins dashboard.

## Scheduled use

Create a recurring task with an instruction such as:

> Use Career Radar to search for new opportunities matching my saved resume and preferences. Search recent listings, validate that applications are open, do not repeat previously reported jobs unless there is a meaningful change, and return the standard Career Radar report. Do not apply to any job.

The host owns scheduling and web access. Each user configures their own cadence, time zone, filters, and minimum score. This plugin does not create schedules or claim that history is persistent when it is unavailable.

## Evaluation

The rubric evaluates role and seniority, technical fit, leadership, cloud and engineering practices, eligibility, and career direction. See [`scoring-rubric.md`](skills/career-radar/docs/scoring-rubric.md).

## Project structure

```text
plugin.json
assets/career-radar.svg
skills/career-radar/SKILL.md
skills/career-radar/docs/
examples/
tests/
```

The first release is skill-only. It uses the history exposed by the ChatGPT task or agent and does not include a permanent database. A future MCP phase can add durable history, controlled job sources, and application tracking without submitting applications. See the [Privacy Policy](PRIVACY.md).

## Quality

```bash
./tests/validate.sh
```

The CI workflow validates the manifest, skill frontmatter, secret safety, and distributable package contents.

## License

MIT. See [`LICENSE`](LICENSE).

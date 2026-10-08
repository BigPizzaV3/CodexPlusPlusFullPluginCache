# Prompt for `@plugin-creator`

Attach `technical-interview-copilot-plugin.zip` (or the unzipped folder) in a ChatGPT Work conversation, invoke `@plugin-creator`, and paste the prompt below.

---

Create and wire a personal/local plugin named **technical-interview-copilot** from the attached package.

Requirements:
- Treat the existing root `plugin.json` as the portable canonical manifest.
- Keep this plugin **skills-only** for v0.1.0. Do not add an MCP server, app connection, hooks, authentication, network dependency, or UI.
- Preserve the skill at `skills/technical-interview-copilot/SKILL.md` and all files under its `references/` directory.
- Preserve the core behavior: adapt to the candidate profile, job description, seniority, technical stack, and interview stage; support Interview Map, Study Mode, Rapid Review, Mock Interview, Coding Interview, System/Architecture Design, Experience Deep Dive, Behavioral practice, and assessment interpretation.
- Never invent candidate experience, projects, metrics, ownership, leadership, skills, company interview stages, assessment behavior, or tooling.
- Mock interviews must ask one question at a time and wait for the candidate before revealing feedback or an ideal answer.
- Coding practice must let the candidate attempt the problem before showing a full solution unless they explicitly ask for the solution.
- Keep the plugin general across software, data, cloud, AI/ML, platform/SRE, frontend, mobile, QA, security, analytics/BI, and architecture roles.
- Create any compatibility manifest needed by the current ChatGPT/Codex host without replacing or weakening the portable root manifest.
- Create a **personal marketplace entry** so I can install and test the plugin locally.
- Validate file paths, manifest syntax, skill discovery, and the listing metadata.
- Do not rewrite the reference frameworks unless a concrete compatibility or validation issue requires it. If you change any existing file, report exactly what changed and why.

Test the plugin against these activation cases:
1. A user uploads a resume and JD and asks what to prepare.
2. A user asks for a one-question-at-a-time mock interview.
3. A user asks to learn a technical topic for a senior role.
4. A user asks for a 30-minute rapid review.
5. A user asks to strengthen a behavioral answer using only supplied experience.

Also test non-activation or safe fallback cases:
1. A general coding request unrelated to interview preparation.
2. A request to invent fake resume experience or metrics.
3. A request to claim unverified proctoring/camera/screen-sharing behavior for an assessment.

At the end, give me the final plugin tree, validation results, the local marketplace/install location, and the exact steps to install and invoke it in ChatGPT Work.

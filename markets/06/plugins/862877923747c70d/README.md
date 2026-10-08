# Resume Match 0.2.0

Supply your resume and a job description as text, readable files, or an accessible posting link.

1. “Assess my resume against this job.”
2. “Assess this and find three current jobs that fit as well or better.”
3. “Use my master resume to make a targeted resume for this posting.”
4. “Do all three. Find five alternatives; remote US work only, salary floor $90,000.”

Assessment explains strongest matches, weakest areas, mandatory requirements, qualification level, and the highest-value improvements. Optimization selects and rewrites supported facts; it never invents achievements or credentials. Jobs are compared against the same evidence standard, with no padding to fill the requested count.

## Capabilities and dependencies

This is an instructions-based Codex plugin with one skill and four references. It adds no backend, paid API, account connection, or software dependency. It uses the host's document tools and live browsing when available. It cannot enable web search on an account that lacks it. Without browsing it can still assess and draft from supplied text, but cannot verify current jobs. DOCX/PDF output requires the host's document-generation tools.

The default optimized resume targets the supplied posting, not every alternative. The candidate need not be the account owner. The plugin does not submit applications, upload resumes to scoring services, or start monitoring.

## Package use

The archive contains a `resume-match` plugin directory. Keep `.codex-plugin/plugin.json`, the complete `skills` directory, and relative paths intact when importing or registering it with a compatible Codex plugin host. Do not upload an isolated SKILL.md and expect it to include the references.

A personal marketplace entry was created in the authoring environment. That does not establish installation on another device. For another Codex environment, give it this package and ask: “Install this Resume Match plugin in my personal marketplace.” The receiving agent should use its plugin-installation capabilities and preserve existing marketplace entries. No ZIP-import UI or public marketplace publication is assumed by this package.

## Documentation and tests

The runtime rules are in `skills/resume-match/`. The `docs` directory contains the readable specification, clearly fictional inputs, the first manual walkthrough, and the release review. Development fixtures must not be mistaken for candidate information or current vacancies. The reports distinguish manual review from independent execution and identify untested live retrieval and document-rendering behavior.

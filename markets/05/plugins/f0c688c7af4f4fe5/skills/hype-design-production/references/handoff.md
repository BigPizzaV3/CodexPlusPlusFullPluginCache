# Handoff

## Transfer to another Mac

1. Copy the complete Project 2 folder, including its hidden `.agents` directory, to the other computer.
2. Install Google Chrome in `/Applications/Google Chrome.app` or set `CHROME_PATH` to the Chrome executable.
3. Open Project 2 itself as the Codex workspace. Codex discovers the skill from `.agents/skills/hype-design-production`.
4. Restart Codex if the skill does not appear immediately.
5. Invoke `$hype-design-production` once with a test request and confirm the PDF appears in `result`.

The ChatGPT/Codex account may be different. The production behavior comes from the local skill, templates, assets, and generator rather than the old chat history.

## Acceptance test

Run:

```bash
python3 .agents/skills/hype-design-production/scripts/smoke_test.py
```

The test creates CTFS, STC, Hype featured, and promotion PDFs in a temporary directory, verifies that each is a one-page PDF, then removes them. A successful run ends with `PASS: 4/4`.

## Normal use

The successor can write naturally, for example:

```text
CTFS, Cameron, Most Profit in a Day, $300, Aug 11th.
```

Codex should select this skill, parse the request, run the deterministic generator, and return the completed PDF from `result`.

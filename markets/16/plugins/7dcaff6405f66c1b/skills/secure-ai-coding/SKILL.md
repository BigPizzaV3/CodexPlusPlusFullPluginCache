---
name: secure-ai-coding
description: Check packages, code, repositories and websites for the security mistakes typical of software written with AI, using the VisionEdge AIScan tools. Use it before installing any dependency, after writing code that handles LLM output, secrets, databases or agent tools, and before deploying.
---

# Secure AI coding with AIScan

AIScan finds problems that AI coding tools often introduce: invented package names, vulnerable versions, leaked keys, unsafe use of model output, open databases and risky agent settings.

## When to call which tool

- **Before adding or installing any package** (npm install, pip install, editing package.json, requirements.txt or pyproject.toml): call `check_package` for every new package.
  - `do_not_install`: do not install it. Tell the user why and look for the real package name.
  - `caution`: explain the signal (very new, little used, look-alike name) and confirm with the user.
  - `vulnerable_version`: use the fixed version the tool returns.
- **A dependency file is shared or the user asks whether dependencies are safe**: call `check_dependencies` with the file name and full content.
- **After writing or changing code** that calls an LLM, renders model output, builds SQL or shell commands, handles API keys, defines Supabase or Firebase rules, or configures MCP servers and agents: call `scan_code` with the changed files and their real relative paths. Paths matter (for example `app/api/chat/route.ts` is a server route, `components/Chat.tsx` runs in the browser).
- **A public GitHub repository**: call `scan_github_repo`.
- **A website**: first ask the user to confirm they own it or may test it. Only then call `scan_website` with `confirm_authorized` set to true.
- **Questions about new vulnerabilities in AI frameworks, SDKs or MCP tooling**: call `get_ai_threat_feed`, optionally with a package name.

## How to present results

1. Start with the grade and the number of critical and high findings.
2. For each critical and high finding give one sentence on what is wrong, where it is, and the exact fix.
3. Offer to apply the fixes. When you change code, scan it again to confirm the fix.
4. Never print secret values. Refer to a leaked key by its location and tell the user to rotate it at the provider.
5. Mention the remaining medium and low findings briefly.

## Limits

- Website checks are passive. Deep checks (exposed files, database read access, CORS) and live monitoring of new vulnerabilities are available on the AIScan website after domain verification.
- This is an automated scan. It finds common problems but cannot prove that software is secure.
- Never use these tools to test systems the user does not own or may not test.

# curb plugin v0.2 development candidate

Build with `npm run plugin:package`. The ZIP contains one HTTPS MCP endpoint, four focused skills and the curb icon. No credentials are packaged.

The endpoint is `https://curb.sale/plugin/mcp`. Server code and migration 0015 are deployed. Production private-photo and OAuth checks passed; actual ChatGPT host acceptance and directory review remain pending. The implementation includes OAuth, real photo files, private reviewable drafts, publication replay protection, account-owned conversations and listing management.

See `docs/plugin/VERIFICATION.md` for evidence and `docs/plugin/SUBMISSION.md` for the remaining release gates. Local checks do not establish ChatGPT compatibility or directory qualification. Do not label this build listed, approved or production-ready until the live acceptance cases and portal scans pass.

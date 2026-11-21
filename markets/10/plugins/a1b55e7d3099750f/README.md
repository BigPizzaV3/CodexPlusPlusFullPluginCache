# SecondPage plugin

Publish and revise Pages using SecondPage's remote MCP server and publishing
skill. Requires a SecondPage account for adults aged 18 and over. The service's
age requirement is distinct from mature content; this package offers ordinary
publishing and collaboration workflows.

This is a local/review candidate, not an approved directory listing. Reviewer
access, accounts, keys, credential handoff, and testing are on hold. No app ID
or successful OpenAI review is claimed.

The remote server is `https://mcp.secondpage.cc/mcp` and uses OAuth. The package
contains no credentials. Do not paste keys or passwords into chat.

From the repository root, run `npm run skills:sync` and
`npm run plugin:sync` to regenerate the included skill and logo. Run
`npm run plugin:check` before packaging. Edit the canonical skill under
`skills/publishing-with-secondpage/`, not the generated copy in this package.

Package only this directory, including its hidden `.codex-plugin` directory
and `.mcp.json`. Never package the repository root. The sync check rejects
unexpected files and symlinks in the package.

Support: https://secondpage.cc/support\
Terms: https://secondpage.cc/terms\
Privacy: https://secondpage.cc/privacy

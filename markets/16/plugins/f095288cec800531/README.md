# VIDOC Security Review plugin draft

A skills-only plugin from [Vidoc Security Lab](https://www.vidocsecurity.com/) for developers and application security teams in ChatGPT and Codex. Its three skills are an initial set, pending the publisher's final definitions:

| Skill                       | Input                                  | Result                                    |
| --------------------------- | -------------------------------------- | ----------------------------------------- |
| security-code-review        | Source, diff, or accessible repository | Evidence-based security findings          |
| security-finding-validation | Suspected finding and source           | Supported, refuted, or unverified verdict |
| security-review-report      | Existing findings and scope notes      | Actionable review report                  |

The portable manifest is `plugin.json`; the host discovers bundled skills under `skills/`. No repository connector, MCP server, hooks, or scanner backend is included. Users supply code or use read-only access already available in their host.

The listing and composer use the existing square Vidoc app icon from `apps/web/src/app/favicon.png`, copied unchanged to `assets/vidoc-icon.png`. The display name is VIDOC Security Review, the publisher metadata is Vidoc Security Lab, and the brand color is `#3E5EFF`, from the existing app and report styles. The listing text, starter prompts, and report title use the VIDOC name.

The manifest includes the company's [website](https://www.vidocsecurity.com/), [contact page](https://www.vidocsecurity.com/contact), [Privacy Policy](https://www.vidocsecurity.com/terms), and [Terms of Service](https://app.vidoc.dev/pdf/terms-of-service.pdf). The `/terms` website page contains the Privacy Policy; the Terms of Service are in the application's public PDF. These links point to existing company documents. The package does not change those documents or make new data-handling promises.

The upload archive is `plugins/security-review-draft.zip`. Rebuild this archive after changes to the package. It must contain `plugin.json`, `README.md`, `assets/vidoc-icon.png`, and the three skill files, with paths relative to this plugin folder.

## Meaning of "only defined skills"

Only these three skill folders are bundled, and their workflows do not depend on external skills. They request read-only behavior. These are workflow instructions, not a runtime access-control mechanism: the plugin cannot establish a global allowlist for every other skill or tool available to ChatGPT.

If exclusive execution is required, establish the restriction in a controlled runtime and enforce the allowed operations and data access there. Do not claim that manifest capability labels or skill instructions enforce permissions. The public plugin specification documents workflow packaging and MCP-controlled actions, not a global skill exclusion setting.

## Try it locally

Use the supported local plugin marketplace workflow in the [official packaging guide](https://developers.openai.com/plugins/build/plugins). Point a local marketplace entry at this folder, install it in a supported local client, and test in a new chat. A ZIP is for portal upload; do not assume every ChatGPT surface supports local ZIP installation.

Example requests:

- "Review this diff for security issues" followed by a diff and relevant surrounding code.
- "Validate this suspected authorization bypass" followed by the claim and source.
- "Prepare a security review report" followed by findings and review scope.

## Before public submission

1. Replace or refine the starter skills with the agreed definitions. Remove unwanted skill folders and update the listing to match.
2. Check the Vidoc publisher metadata and branding against the selected verified developer identity. The directory uses that verified identity. Resolve any missing listing or asset requirements reported by the portal.
3. Test representative activation, missing inputs, scope boundaries, and output accuracy in the target client. Local file validation does not prove model behavior.
4. Upload the ZIP through the skills-only submission path, complete identity verification and policy attestations, and resolve the skill scan findings.
5. Submit for review and publish after approval.

Public publication and portal safety scans have not been performed. If a repository backend will be needed, decide before submission: the current docs say an MCP server cannot be added to an existing skills-only plugin.

Sources: [package format](https://developers.openai.com/plugins/build/plugins), [build skills](https://developers.openai.com/plugins/build/skills), [submission](https://developers.openai.com/plugins/deploy/submission), [submission requirements](https://developers.openai.com/plugins/deploy/submission-errors).

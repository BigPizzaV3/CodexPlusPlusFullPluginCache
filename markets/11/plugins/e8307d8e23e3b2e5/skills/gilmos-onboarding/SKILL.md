---
name: gilmos-onboarding
description: Help someone start in gilmOS, understand workspaces, projects, assets and the Sandbox, or recover an empty account after plugin connection. Use for first setup and product orientation; production work in an established project has specialized skills.
---

# Start in gilmOS

Guide the person in their language, using their actual account state. Connecting the plugin creates neither a workspace nor a project and supplies no generation credits. A gilmOS workspace is the studio/team and credit boundary; a project is one production. ChatGPT and Codex subscriptions are separate from gilmOS credits.

## Find the next useful step

Call `gilmos_get_onboarding`. If an older connected server has not exposed this tool yet, use `gilmos_list_projects` and https://app.gilm.ai/start instead; do not invent a missing setup tool. Its state and `guideUrl` describe the connected account; do not invent an empty account after an authentication or context error. `gilmos_list_projects` also returns setup guidance beside the existing workspace/project listing.

- `create_workspace`: explain the workspace/project distinction and offer the MCP starter: 4.99 per workspace per month, with 4.99 credits added after each paid monthly invoice, cancellable at any time. FREE is optional and includes no generation credits. Explain the chosen offer before creation; return checkoutUrl for the human to pay. Wait for activation before creating a project. Obtain the studio name and use `gilmos_create_workspace` when the human requests that creation. An explicit creation request already authorizes this reversible work; do not ask again. Use gilmos_get_credits before generation; below 1 EUR/USD offer the returned purchaseUrl to the owner, or ask other members to contact the owner. Never initiate payment or resubmit a failed generation automatically. The tool reuses an owned workspace and preserves its plan. Do not fabricate a project ID, grant access, change a plan or create sample productions to fill the account.
- `check_invitation` or `ask_project_access`: explain how to use the intended account and an existing project invitation. Do not replace an expected team workspace with an unsolicited personal one. A person who explicitly wants their own workspace may choose that path.
- `activate_plan`: direct the person to the verified setup link in the browser. Do not start or alter a subscription, top up credits or change the pending plan as part of orientation.
- `create_project`: ask for the production title if missing; use `gilmos_create_project` with an eligible workspace ID from the returned state. If several destinations are eligible, let the person choose. Reuse an intended existing project. Workspace permissions and project limits apply.
- `choose_project`: select an existing project, then use [the project skill](../gilmos-projects/SKILL.md) to read its context before recommending work.

A lost write response requires a fresh setup/project read before retrying, because most writes are not idempotent. Confirm returned identifiers and the resulting state; do not claim that merely showing instructions created anything.

## Explain the production model progressively

Use the returned principles as facts, adapting the amount of explanation to the person's question:

- The brief and screenplay describe the story; scenes organize it, and the breakdown turns scenes into shots.
- Characters, locations and props are reusable **assets**, with variations and versions. Exact tags such as `@Character` resolve actual project references; naming a character in prose alone is not a pinned reference image.
- The **Sandbox** is for imported files and generated trials. A trial is not automatically the shared reference or final approved work. Versions and review statuses preserve those decisions.
- Montage assembles selected media; the plugin saves editing decisions and does not export a rendered movie.
- Generations and some Alfred workflows consume gilmOS credits. Inspect the current model catalogue, supported references and an applicable estimate before an explicitly authorized generation. Setup alone does not authorize a paid demonstration, model substitution or credit purchase. If the human also explicitly requests production work, continue with the matching production skill and preserve the authorized count and budget.

Offer one next action tied to the person's goal: import an existing screenplay, prepare reference assets, or organize existing files in the Sandbox. Do not force a screenplay-first workflow on someone who already has rushes. Provide `guideUrl` for the visual guide; a link does not mean the browser was opened.

For exact call examples, read [examples.json](references/examples.json). Use the other specialized plugin skills when the person moves from orientation to writing, reference work, storyboarding, media generation, montage or team collaboration.

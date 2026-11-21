---
name: workflows
description: Build, validate, test, publish and run a workflow over MCP, from a plain-words goal or a template to a live workflow, then watch and recover its runs.
---

# Workflows

A workflow is automation in Kenso: one trigger (a signal, a new lead, a webhook, a schedule, or a run on records someone picks), a list of steps (find people, enrich, qualify with AI, branch, draft an email, post to Slack) and limits (credits per month and per run, runs per day). Nothing runs until it is published.

These tools cannot read, build, test, publish or run workflows, or read their runs. Say so plainly. The person does it in the app, on Workflows, https://app.ken.so/<workspace id>/demo/workflows (in beta: it opens only where the workspace has Workflows on):

1. New workflow, or Build with Ken to describe the goal in plain words.
2. In the workflow's Editor, set the trigger, the steps and the limits.
3. Test run, then check the run on the Runs tab.
4. Publish when the test looks right.

You can help them pin down the goal, the trigger, the steps and the limits in plain words before they build it. Keep every send step on approval unless the person asks for automatic sends. A campaign workflow on a client's campaign decides who that campaign sends to, so publishing or unpublishing one needs a yes that names the client.

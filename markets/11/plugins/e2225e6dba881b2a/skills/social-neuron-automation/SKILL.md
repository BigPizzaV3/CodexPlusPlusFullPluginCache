---
name: social-neuron-automation
description: Inspect, prepare or change Social Neuron recurring content workflows and recipes when the user requests automation, with explicit destinations, budgets and review settings.
---

Resolve the selected project and destination accounts, then use get_account_status, check_pipeline_readiness and the relevant status/list tools. Actual entitlements and OAuth scopes control access. A plugin installation or broad request for better content is not authorization to enable recurring publishing.

Inspect existing configurations before creating another. For preparation only, use exposed read-only status tools and preview_skill. It returns a local manifest preview/dashboard link, without production execution or brand lookup. The OpenAI profile omits the recipe dispatcher family; use separately exposed operations for the requested workflow. Inspect the current tool schemas before calling any execution tool.

run_content_pipeline with dry_run=true still generates content, persists a plan and creates approval records; it suppresses scheduling only. Use it only when the user has authorized that generation, spending and persistence. Explicitly set dry_run=true and approval_mode=review_all unless the user has authorized auto-approval for that exact workflow. Do not use a pipeline dry run for a read-only preview.

For a research-led routine, present which native or supplied sources it may use, its evidence freshness requirement and what happens when research is missing or contradictory. Do not silently convert an approved manual research step into a recurring external data collection dependency. A configured or reported budget is not proof of a hard provider spending cap; describe only enforcement established by the actual tool response and supported contract. Preserve known job IDs and reconcile uncertain outcomes before any retry.

Present the exact recipe/content policy, project, accounts, cadence with timezone, per-run and weekly credit limits, approval mode and stop/pause conditions. Use a supported timezone field only when the current schema offers it; if a requested local schedule cannot be represented accurately, explain the limitation before activation. If the request is preparation only, create a configuration only when saving was requested and explicitly set is_active=false, because creation otherwise defaults to active.

Execute or activate only when existing user authorization covers that specific configuration, spending and recurring publication behavior. Preserve the approved review mode; a quality score or empty approval queue is not authorization to auto-approve. Use auto_approve_plan only for an explicitly authorized decision on the matching current plan.

Read back get_autopilot_status, list_autopilot_configs or get_pipeline_status after a change. Verify the returned configuration and distinguish an active schedule from an executed run or published post. On an uncertain mutation, reconcile by returned ID before retrying.

When asked to pause or stop, identify the correct owned configuration and use the supported update operation. Deletion is a separate action with its own scope. Report the effective saved state and any already queued work separately. For later improvement, use the self-learning workflow with measured results; do not silently change the approved budget, destinations or publication policy.

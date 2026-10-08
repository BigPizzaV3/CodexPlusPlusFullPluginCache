---
name: qbraid-workspace
description: Use this skill when a user wants to develop, run, or learn quantum computing with qBraid; choose hardware or simulators; understand circuit results; work with qBraid cloud environments or qBook courses; or manage qBraid team access, existing credits, and support. Also use for follow-up requests about a connected qBraid workspace. General quantum theory questions without a qBraid task do not require this skill.
---

# qBraid Workspace

qBraid brings quantum computing resources into one platform. It helps learners, researchers, and teams move from a quantum computing idea to a working experiment: explore available hardware and simulators, prepare a circuit, run it, and understand the results. It also provides cloud computing workspaces, learning content, and organization tools for collaborating and managing access to resources.

Explain capabilities in everyday language and connect them to the user's goal. The capabilities below describe the public ChatGPT app; available actions depend on the connected account and its permissions.

## What you can accomplish

### Find the right quantum computing resource

Explore quantum providers, physical quantum computers, and simulators. Compare their capabilities, availability, supported programs, and available pricing information to identify a suitable resource for an experiment. Explain the difference between simulation and execution on physical hardware, including relevant limitations.

### Develop and understand quantum circuits

Create an example circuit, check an existing circuit for errors, explain its gates, or convert between supported OpenQASM formats. Use the free built-in simulator for supported small circuits to explore their ideal behavior before committing to a provider job. Explain output probabilities and how they relate to the circuit; distinguish ideal probabilities from sampled measurements and hardware results.

### Run experiments and inspect results

Estimate the cost of a proposed quantum job, submit an authorized experiment to a selected device, follow its status, and interpret the returned results. Review previous jobs, inspect their programs and circuit diagrams, or cancel a job when requested. Help users understand pending or failed work without claiming that an unfinished job succeeded.

### Work with cloud computing environments

Explore available compute profiles, instances, sessions, and software environments. Inspect accessible notebook files and project content, start or stop cloud servers when requested, and review compute usage. For users preparing custom environments, help build a supported kernel and check its build status.

### Learn with qBook

Find accessible courses and articles, read learning content, and enroll in a course when requested. Help learners understand material and review their enrollments. Authorized educators can inspect enrolled students and course reports. Course creation, redeployment, and unenrollment are not available through this app.

### Collaborate and manage existing credits

Show a user's organizations, membership roles, and available credits. Distinguish the user's personal balance from an organization wallet. Authorized team managers can invite teammates, manage membership, review credit requests, and distribute existing organization credits. Users can request credits and inspect relevant usage, transaction, invoice, and subscription information.

### Get help with qBraid

Explain qBraid's platform, SDK, CLI, and supported providers. Help investigate a platform problem using accessible account information, then create or follow up on a support request when the user asks. Explain what information will be shared with support before sending it.

## How to help

Start with the outcome the user wants. Use current information from the connected qBraid app to establish what is available to their account, and explain the result in terms of the next useful step. Ask for a missing organization, device, circuit, or other essential detail only when it cannot be resolved from the request and available information.

Account permissions and resource availability determine which actions a user can complete. Make costs and meaningful changes clear before acting, and obtain any necessary confirmation for spending credits, changing access, or sending messages. A request to inspect a balance or explore devices does not authorize a transfer or job submission.

Use qBraid's normal sign-in flow when a connection is needed. Never request passwords, API keys, or GitHub tokens in chat. Credit purchases are unavailable through this app. If a requested capability is unsupported or a call fails, explain the limitation; do not invent a result or silently substitute another action.

## Example outcomes

- “Help me try quantum computing.” Guide the user through a small Bell-state circuit and a free ideal simulation. Explain why its two correlated outcomes each have approximately 50% probability. Do not submit a provider job unless requested.
- “Which device should I use?” Compare relevant available devices and recommend a suitable option with the reason, known cost information, and any uncertainty. Finish with a clear choice or the one missing detail needed to choose.
- “Where are my credits?” Identify the relevant organization and show the caller's balance, clearly labeled. Inspect the organization wallet only when relevant and permitted; do not transfer credits as part of answering.

End each completed task with the result, the relevant device or workspace, and any cost or account change that actually occurred. For unfinished tasks, state what is pending and what is needed next. Base completion claims on returned results.

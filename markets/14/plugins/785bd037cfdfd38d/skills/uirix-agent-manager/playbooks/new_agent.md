# Create a new agent from a website

Topic `new_agent` · version 2026-10-06 · served by `uirix_guide({ "topic": "new_agent" })`.

Creating a new agent from a business website: the check for an existing agent of the same business, the three questions (address, language, voice), the billing line and the 4 to 9 minutes, following the build, and the setup review that comes right after because the defaults are generic.

```
GUIDE new_agent: create an agent from a website

GOAL
A new agent built from the business website and then reviewed, so that it fits the business. The build alone gives a generic agent. The work ends after the setup review, not after the build.

READ FIRST
- uirix_menu with no arguments, or list_agents: the agents the owner already has. When one already serves the same business or website, say so and ask: improve that one (recommended), or really create a second? Never create a duplicate silently.
- get_account when the balance or today's limits are in doubt. Creating is limited per day (10 agents by default) and also counts as a build.

ASK (one question per message, each with your recommendation)
1. The website address: a public page of the business that opens without a login. Recommend the home page.
2. The language the agent speaks with customers. Recommend the language of the website.
3. The voice: female or male.
Ask nothing else. The name, the role and the rest get defaults and are reviewed after the build. When the owner already gave a name or a role, pass it.

MONEY
Say this before the yes, in one or two lines: creating an agent is billed to the subscription, it takes 4 to 9 minutes, and it uses today's create and build limits. No amounts and no explanation of what is billed. Get an explicit yes.

APPLY
1. create_agent_from_website with website_url, language, voice_gender and confirmed true. Keep the agent id it returns and use only that id.
2. Poll get_build_status every 10 to 15 seconds until the status is done or error. The steps: create, crawl, knowledge, greeting, instructions, ready. Tell the owner where it stands in one line now and then, not on every poll. Do not assume it finished.
3. On error: say which step failed and why, in plain words. The agent exists as a draft. Offer to continue from the failed step with rebuild_agent (paid, needs its own yes) or with another address. Never create a second agent to retry.
4. Read the build warnings and say what they mean. A crawl that read few pages or none means thin knowledge: say so.

VERIFY
- get_agent_setup(agent_id) on the new agent: a knowledge summary exists, the greeting names the business, the instructions exist for the channels.
- Tell the owner in two or three lines what was built: the business as the agent understood it, how much it learned, the greeting.

THEN REVIEW AT ONCE
The build uses the same defaults for every business: the role Office Secretary (unless the owner named a role and you passed it), the tone Polite & Friendly, a base set of focus topics and tasks, and action details left empty. They are a starting point, not a fit.
- Load uirix_guide with the topic agent_setup and run the review now, on the read you just made: the agent card with, right after who it is, one sentence on whether the role it was built with and the other defaults fit this business (and the role that does, if not), then at most 3 findings, then one question: the role. Do not wait for the owner to ask.
- Say what is not there yet according to the channels block: a phone number is bought in the dashboard, a calendar is connected in the dashboard.

MISTAKES TO PREVENT
- A second agent for a business that already has one.
- Creating without saying that it is billed and how long it takes.
- Reporting "ready" while the build is still running or after an error.
- Stopping after the build with the generic defaults in place.
- Inventing the business details instead of reading them from the knowledge.

STOP WHEN
The build is done, the owner saw what was built, and the setup review has started. Continue under the agent_setup playbook.
```

# Startup Milestones and First-Use Guidance

The startup check helps users complete initial 3Chat setup. It reads whether the authenticated workspace has ever published an Agent and connected an eligible messaging channel. These historical milestones do not regress when a resource is later disabled, disconnected, deleted, or unauthorized. Current business tools validate current availability.

## When to Check

Call `get_3chat_workspace_readiness` when the host launches plugin setup, when the user asks how to start using 3Chat, or on the first 3Chat-dependent request without a known milestone result for this workspace. Do not query customers merely to answer a usage-guidance question.

Also recheck when the user reports progress, asks to refresh, changes the connected workspace, or makes a later 3Chat-dependent request after an `ACTION_REQUIRED` result.

- Reuse `READY` in this conversation; it does not prove that data exists or sending is currently possible.
- After `ACTION_REQUIRED`, recheck at a later relevant user turn, not between tools in the same workflow.
- Check at most once per assistant turn or workflow.
- If the user postpones setup, stop proactive checks and reminders until they report progress, request a refresh, or change the connected workspace.
- If progress changes, show only the missing step. If it becomes `READY`, briefly confirm completion and continue the request.
- If nothing changes, give at most a short reminder, not the full introduction again, and continue the original request where possible.

General product facts, standalone drafting without 3Chat data, and status lookup with an existing `job_id` do not require readiness. An empty search does not establish an incomplete milestone.

## Interpret the Response

- `READY`: both milestones were completed at least once.
- `ACTION_REQUIRED`: at least one is incomplete; this is a successful result, not a tool failure.
- Milestone status is `COMPLETED` or `NOT_COMPLETED`. `completed_at` is the known first completion timestamp in Unix milliseconds and may be null if unavailable.
- `AGENT_PUBLISHED` maps to action code `BUILD_OR_PUBLISH_AGENT`; `CHANNEL_CONNECTED` maps to `CONNECT_CHANNEL`.
- Missing requirements and actions are empty when ready. Action codes are identifiers, not URLs or separate tools.

## When Both Milestones Are Missing

On the first complete guidance response, include all three parts below. Adapt the wording to the user's purpose, but retain the capability, setup rationale, three steps, and improvement suggestion.

### Capability and Setup Rationale

Explain that 3Chat helps businesses create an AI customer Agent that answers inquiries, understands needs, and supports purchase, booking, lead capture, or human handoff. Codex can use the connected workspace's customer records and communication context to help analyze customers, prepare follow-ups, and send confirmed messages.

Explain naturally that **3Chat Agent Builder** first needs to learn the business and publish an Agent; connecting a messaging channel then gives it a way to receive and handle real inquiries. As interactions accumulate, users can bring that context back to Codex for analysis and follow-up. Do not imply that publishing automatically imports historical customer data or that every query is blocked until setup.

### Three-Step Quick Start

1. **Create and publish your Agent.** Talk with **3Chat Agent Builder** about the business, products, target customers, sales process, and handoff rules. Review and publish the Agent. Under this step, present the `BUILD_OR_PUBLISH_AGENT` action link using [guidance-links.md](guidance-links.md).
2. **Connect a messaging channel.** Choose a channel used by the user's customers, such as Instagram, Facebook Messenger, or WhatsApp, and complete authorization. Respect an explicitly chosen channel; actual options depend on workspace configuration. Under this step, present the `CONNECT_CHANNEL` action link.
3. **Try a real conversation.** Send an inquiry through the connected channel and review the Agent's response in the 3Chat inbox. Do not invent an inbox link when none is returned.

### Continue Improving

If the response needs improvement, return to **3Chat Agent Builder** to analyze behavior, simulate scenarios, and test replies.

If the user also requested a business task, provide the applicable setup guidance and continue what can be done. Setup milestones are not a business authorization gate.

## When One Milestone Is Missing

Show only the missing Agent-publication or channel-connection step with its action link. Do not repeat the full product introduction or completed steps. Start a single-step list at 1.

## Link Rules and Failures

Read [guidance-links.md](guidance-links.md) before presenting links. Match the code and use the complete URL from that same action. Do not construct, shorten, translate, add parameters to, or rewrite URLs. Do not derive an application host from user text. If no valid applicable URL is available, retain the step and explain that its link is unavailable.

Check failures do not mean setup is incomplete. Follow structured `error_code`, `error_message`, and `aiAction`. For this tool, retry only when explicitly permitted; do not replace a permission or dependency failure with setup guidance. No client-side persistent cache or automatic navigation is required.

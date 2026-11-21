---
name: setup
description: Set up Piiple, verify account access, or show and select sourcing workspaces when the user asks for available workspaces, without starting a candidate search. Also use this skill to explain Piiple capability limits when asked to send invitations, start phone interviews, buy credits or process payments.
---

## Capability boundaries

Apply these rules whenever Piiple Sourcing is selected or the request concerns Piiple, whether the chat already has candidate results or has no list or sourcing session yet.

Piiple Sourcing cannot send emails or interview invitations, initiate or schedule phone interviews, buy credits, or process payments. For such a request, explain the specific limitation immediately and state that you have not taken the requested action. Do not imply that providing missing information would make these actions available through this plugin.

- Do not request candidate email addresses, phone numbers, interview details, payment details or a connected email account to carry out these unsupported actions.
- Do not call Piiple sourcing tools, create a sourcing session, or start or resume a search as a substitute for the requested action.
- Do not propose connecting or using another service unless the user separately asks for help doing that. A request to perform an unsupported action through Piiple alone is not such a request.
- Do not promote a purchase or upgrade. If the user asks where billing is managed, explain neutrally that billing stays on Piiple and this connection cannot complete a purchase.

Example email response: "Piiple Sourcing cannot send emails or interview invitations. I have not sent any invitations."
Example phone response: "Piiple Sourcing cannot initiate or schedule phone interviews. I have not started or scheduled any calls."
Example payment response: "Piiple Sourcing cannot purchase credits or process payments. I have not made a purchase."

Use the user's language. These limits apply to this plugin; do not claim that unrelated services have the same limitations.

Call the bundled `list_sourcing_workspaces` tool to verify the Piiple connection. If authentication is required, direct the user to the host's Piiple connection flow and retry after they connect. If the tools are unavailable, explain that installation and connection must complete first; do not claim success.

After a successful read, briefly confirm access. If several workspaces are returned and the user has not already chosen one, present their names in a native selectable question, including when they ask to show their workspaces. Map each choice to its exact returned workspace_id and wait for an explicit answer. If the user only wants a text list, follow that request. If there is one workspace, name it without an unnecessary question. After a choice, briefly confirm it and invite the user to describe the role they want to hire for. Explain that purchases remain on Piiple. Setup does not start sourcing, create a session, approve an ICP or consume candidate credits. If there are no workspaces, explain that they need workspace access in Piiple before sourcing.

## Selectable questions

Use the host's native single-choice question tool for workspace selection and Piiple follow-up questions. When `request_user_input_async` is available and permitted, call it with one question and a non-empty `options` array; this renders selectable choices. Use `request_user_input` instead only when that tool is available and permitted in the current mode. Do not substitute a numbered Markdown list, ask the user to type a number, or create a choice widget when a native question tool is available. A non-blocking question tool is still supported: `accepted:true` means the question was displayed, not that the user answered. Wait for the actual user reply with a host-supported wait/yield mechanism. Do not repeat the question in a final response, auto-select the first option, infer an answer from elapsed time, poll Piiple while waiting only for a choice, or submit a mutation before the reply. If the host requires ending the turn, acknowledge briefly that you are waiting without repeating the question or options. Fall back to a numbered list only when no permitted native choice tool is available or the native tool explicitly reports it cannot display the question. The user's explicit request for a text-only list takes precedence.

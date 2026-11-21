---
name: sharedbrief-setup
description: Guide a user who runs SharedBrief setup toward their first private draft in the current chat. Use for explicit plugin onboarding or setup, not for unrelated writing or account administration.
---

# Get started with SharedBrief

Help the user reach their first useful document with minimal setup. Stay in this conversation. Do not send them to the SharedBrief dashboard, ask a profile questionnaire, or claim a connection succeeded before a tool succeeds.

## Choose the document

Use an explicit document request or selected content already in the conversation. Do not pull unrelated conversation history, memories, private files, or existing SharedBrief documents into onboarding.

- If the user already asked to create a specific document and provided enough material, proceed to its private draft without repeating questions.
- If setup is invoked beside an existing proposal or other obvious document but the user has not selected it, offer one contextual choice: “Shall I turn the proposal above into your first private draft?”
- If there is no document context, say: “What would you like to create and give others access to? Share a few details, or say **‘show me an example’** and I’ll create a sample sales proposal.” Request only the essential missing content for the user’s own document. Do not invent a company, price, customer, deadline, or other factual detail for their real document.
- If the user chooses “show me an example” or otherwise asks for the offered example, use this prompt without asking for more details:

  > Create a polished, one-page sales proposal from a fictional marketing agency to a local coffee shop. Propose a three-month campaign to bring in more customers. Include the client’s goals, proposed services, timeline, pricing, and next steps. Clearly label it as an example with fictional details, and save it as a private draft.

  Fictional names, pricing, timelines, and other illustrative details are allowed only for this explicitly selected example. Follow the same create-and-verify private-draft flow below; choosing the example does not authorize sharing or publication.

## Connect only when needed

Use the available SharedBrief tools. If a tool requires authentication, let ChatGPT show its native connection prompt. Explain briefly that the user signs in once and returns here. Do not collect passwords, verification codes, or OAuth tokens. Do not create duplicate accounts or repeatedly retry a denied/failed connection. On failure, keep the selected content in this conversation and invite the user to reconnect and continue.

## Create and verify a private draft

Call create_document using the selected content and the formats the available tool schema actually supports. Do not assume HTML, JavaScript, image assets, forms, or direct editing are enabled. Do not change feature flags.

Read the created document with get_document to verify that it exists, contains the requested material and is still private. On a tool error, report the error accurately and keep the work in chat; never invent a successful save, a document ID or a URL.

Show the draft using the actual tool result and available preview. Do not claim that the preview opened successfully unless that is confirmed; a successful show_document call alone does not prove the host displayed it.

Always finish with a short, actionable response:
- Link to the actual owner workspace URL returned by the tool, labeled “Open your private draft in SharedBrief.” Explain that it is private and this owner link is not for recipients.
- Offer the next sharing step: “To share it, tell me who should have access: anyone with the link, anyone signed in with a verified email, or specific people. I’ll publish it with your chosen access and give you the link to send.”
- If the preview fails, still provide the verified owner workspace link so the user can open the saved draft. Do not describe a host preview failure as a failed save or publish the document to work around it.

## Share only when requested

Setup alone authorizes no publication, reader-access change, invite or deletion. If the user asks to share, determine the intended audience before changing access: anyone with the link, verified readers, or named recipients, according to available tool options. Do not guess public access.

When the user has requested publication and chosen access, use the sharing tools to apply and verify those settings, then publish_document. Return only the recipient URL actually returned by the tool. Preserve the existing stable URL on updates. The next-step offer above is guidance only; wait for the user to request sharing and select access before changing permissions or publishing. Do not send invitations.

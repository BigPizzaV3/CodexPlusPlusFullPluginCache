---
name: edit-site
description: Edit a Flint website by chatting with the Flint agent. Use when the user wants to modify, update, or add content to their Flint managed website.
---

# Edit a Flint Site

Help the user modify a Flint website by chatting with the Flint agent.

## Workflow

1. **Find the site**: Call `list_sites` to get the user's available sites. If $ARGUMENTS contains a site name, match it. If there are multiple sites and the user didn't specify, ask which one.

2. **Start a chat**: Call `start_chat` with the site ID and a message describing the changes. It returns a `chatId` and `messageId` right away.
   - Describe goals and intent, not implementation details
   - If the user provided code, examples, or reference material, pass them through as-is
   - Do NOT generate HTML, CSS, or markup — Flint is an expert designer and produces better results with creative freedom

3. **Wait for the reply**: Call `wait_for_reply` with the `chatId` and `messageId`.
   - On `running`, call it again right away. Flint often works for several minutes.
   - On `completed`, read Flint's reply.
   - On `failed`, send the message again.

4. **Answer Flint's questions**: If Flint's reply asks a question, ask the user, then send their answer with `send_message` in the same chat and go back to step 3 with the new `messageId`.

5. **Report results**: Share Flint's summary of the changes and any preview links it gives.

## Important guidelines

- Flint is an expert web designer. Describe what you want, not how to build it.
- Always honor the user's explicit requests (e.g., "make the header black", "use a three-column grid") — pass that intent through.
- Keep follow-ups about the same work in the same chat so Flint has the context. A chat takes one message at a time, so wait for the reply before sending the next one.
- Start a separate chat for each separate piece of work. Separate chats run in parallel.
- Flint can't run Google Ads changes over MCP. It can draft them, and a person runs them in Flint.
- Only use `publish_site` if the user explicitly asks to publish or deploy. It deploys the entire site.

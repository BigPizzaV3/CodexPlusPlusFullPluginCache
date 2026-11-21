# Setup Links in Codex

Use the native Markdown response surface: an ordered text step followed by a separate blockquote containing a bold, named clickable link. This makes the next action easy to find without requiring a renderer, HTML, JavaScript, or an additional tool.

## Sequence and Data

- Match `BUILD_OR_PUBLISH_AGENT` or `CONNECT_CHANNEL` in `data.actions[]`. Use the complete URL from the same object, unchanged.
- Use a short action label; localize the visible text when appropriate. Keep the Agent Builder name bold. Use the action's label when suitable, or "Open 3Chat Agent Builder" / "Connect a messaging channel".
- Under each applicable step, show one prominent link. Do not collect all links at the end or replace the step explanation.
- A step without a returned link remains text. One missing milestone means one text step and one applicable link.
- Escape link-label Markdown when needed; do not expose HTML, placeholders, or raw tool JSON.

## Presentation Pattern

The following is a Markdown template. Replace ACTION_URL with the matched raw URL before replying; do not show the template as a code block.

```markdown
1. **Create and publish your Agent.** Describe your business to **3Chat Agent Builder**, review the result, and publish.

   > **[Open 3Chat Agent Builder](ACTION_URL)**

2. **Connect a messaging channel.** Select your channel and complete authorization.

   > **[Connect a messaging channel](ACTION_URL)**

3. **Try a real conversation.** Send an inquiry through the connected channel and review it in the 3Chat inbox.
```

The two ACTION_URL values come from their respective actions, not from a shared or invented address. If a URL contains Markdown-significant parentheses, use Markdown's angle-bracket destination form without changing the URL.

## Runtime Boundary

This is a native formatted link, not a promised button or custom card. Do not invoke `show_widget`, `present_files`, a browser, or another plugin just to display it. Do not manufacture undocumented directives or treat ChatGPT iframe/MCP Apps support as guaranteed Codex rendering.

Present the destination for the user to select. Only open it through an actually available native browser mechanism if the user asks; do not make that mechanism a dependency of setup. Selecting or opening a link does not complete a milestone. When the user returns, follow the startup recheck rules.

If the client does not style blockquotes, retain the named Markdown link. Do not create an HTML page or file preview as a fallback.

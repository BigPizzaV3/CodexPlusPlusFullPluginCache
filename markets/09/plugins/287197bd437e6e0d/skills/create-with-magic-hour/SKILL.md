---
name: create-with-magic-hour
description: Use Magic Hour MCP tools in ChatGPT to generate or edit images, videos, and audio, upload source media, monitor renders, and return finished results.
---

# Create with Magic Hour

Use the connected Magic Hour media-generation MCP server for requests to create or edit media. Discover the available tools and their current schemas at runtime. Do not assume a tool exists merely because an API page lists a feature. If the connection requires authorization, let the user complete the Magic Hour sign-in or authorization flow; never ask them to paste an API key into chat.

Ask only for missing required inputs. For a complete request, default to one result using suitable account-eligible defaults without asking for a credit-budget confirmation or optional model/style choices. Respect the user's explicit settings and limits. If a starter ends at its colon with no description, ask only for the missing description and do not generate. For "Animate my attached photo", request the photo if none is attached. If a requested model or setting is unavailable, explain the restriction rather than silently changing it. State costs only when returned by the current tool; do not invent a quote.

If source media is needed, follow the server's upload instructions. Request a presigned upload URL, upload the bytes using an available supported mechanism, and pass the returned file path to the generation tool. Do not put raw media bytes in a text argument. If the chat environment cannot transfer the file to the upload URL, explain the blocker and ask for an accessible source URL or another supported input.

Call the matching image, video, or audio tool with valid arguments. Creation may return a project ID rather than a finished file. Use the corresponding wait or retrieval tool to track completion, and return the final link or preview if available. Report failures using the returned reason and give a concrete correction. Treat signed download links as temporary and use them exactly as returned.

For requests involving someone's likeness or voice, obtain the necessary source and follow the tool's consent requirements. Never assert that an output is finished from a project ID alone.

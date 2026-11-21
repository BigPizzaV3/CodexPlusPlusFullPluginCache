---
name: setup
description: Check the OfferUnderway connection after installation, help the user sign in if needed, and report career-profile readiness. Use when setting up OfferUnderway or checking whether its MCP connection works.
---

Discover the OfferUnderway tools and call `get_offerunderway_context` once. If authentication is required, use the host's normal OAuth sign-in flow. The server URL is `https://api.offerunderway.com/mcp`; users sign in with their OfferUnderway account and approve the displayed permissions. Never ask for credentials in chat.

Report whether the connection works and whether the saved career profile is ready. Follow returned setup links when a profile is missing. Do not read the full resume, generate materials, submit applications, or schedule a recurring task during setup. If the tool is unavailable, explain the observed failure and direct the user to `https://offerunderway.com/integrations/ai` for their assistant's setup instructions. Do not declare success based only on installing the plugin or listing tools.

---
name: get-started
description: Show what Amomic-AI Docs can answer and suggest a first question about building on Amomic-AI.
---

# Get started with Amomic-AI Docs

Amomic-AI Docs searches the public documentation and REST API reference for Amomic-AI, the AI support platform for voice calls, WhatsApp and web chat.

1. Tell the user they can ask how to set something up (a WhatsApp number, a voice agent, a campaign, webhooks) or look up an exact API endpoint.
2. Offer three starter questions:
   - "How do I connect a WhatsApp number to Amomic-AI?"
   - "Which endpoint sends a message through the Amomic-AI API?"
   - "How do I verify Amomic-AI webhook signatures?"
3. When they ask, use `search_docs` (or `search_api` for endpoints), then `read_doc` on the best match, and answer with links to docs.amomic.in.

The plugin only reads public documentation. It cannot see or change anyone's Amomic-AI workspace.

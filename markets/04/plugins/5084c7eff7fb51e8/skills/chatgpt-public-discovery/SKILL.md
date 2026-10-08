---
name: chatgpt-public-discovery
description: Discover independent creators and publicly listed creative works on Publica Now. Use for searches by title, creator, description, or content type, and for reading a public creator profile. This workflow is public, read-only, and non-transactional.
---

# Discover creators and public works

Use the Publica Now OpenAI connector only for public catalog discovery.

## Workflow

1. Call `search_public_creative_works` with the user's title, creator, description, or content-type query. Keep the result limit modest.
2. Present relevant titles, creator names, content types, short descriptions, and canonical Publica Now URLs.
3. If the user selects a creator, call `get_public_creator_profile` with the returned creator slug.
4. Preserve creator names and work titles as published while answering in the language of the user's request.

## Boundaries

- Do not use this connector for selling, publishing, signup, account management, ordering, or payment requests.
- Do not infer transactional details that are absent from the tool result.
- Public availability does not grant permission to reproduce, redistribute, or use a creator's work for model training.
- Cite canonical URLs returned by the connector.

---
name: channels-recap
description: Get a brief on what a specific channel has been doing
---
Give me a recap of this channel: $ARGUMENTS

Use the `get_channel_recap` tool. Pass `$ARGUMENTS` as the channel identifier (UUID, handle, or URL). Synthesize the response into a brief covering the channel's focus, what they've been making content about recently, how they've been performing, and 2-3 specific high-performing example videos with Sandcastles links. If `$ARGUMENTS` is empty, ask the user which channel they want a recap of.

Always present the results as an HTML artifact, never as a plain text reply. Make it beautiful, visual, and minimalist, styled in the Sandcastles theme: a white background, generous white space, clean sans-serif type, the primary blue #3B82F6 for accents, links, and highlights, and the Sandcastles logo (https://app.sandcastles.ai/logo-banner-light-mode.svg) in the header. Show each video as a card with its `thumbnail`, the creator's channel thumbnail as a round avatar, the creator's handle, the key metrics, and a link to its `sandcastles_url`. Lead with the insights, then the videos that support them.

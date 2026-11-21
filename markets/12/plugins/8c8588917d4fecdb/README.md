# Snap Closet

Your Snap Closet wardrobe in ChatGPT and Codex. This is the OpenAI portable plugin (Agent
Plugins 1.0.0): `plugin.json` is the manifest with the display fields under
`extensions.com.openai.interface`, `mcp.json` names the remote connector
`https://mcp.snap-closet.com/mcp`, and `assets/` holds the icon and logo.
Sign in with your Snap Closet account when the plugin is installed.

## Use it

Ask what you own, search by category, colour, season or occasion, and see the garments as cards.
Ask for an outfit and get looks made only from your own clothes, put one on a future day of the
app's calendar, or log what you wore. Ask for a diagnosis to see gaps, duplicates and new
combinations. Add garments from photos through an upload link; the server removes the background and tags
them as the app does. Save an outfit picture you found elsewhere, from a link or attached in the
chat, to the inspiration clipboard in the app, then look at a saved inspiration and get a similar
outfit from your own clothes.

## Data

Every request goes to `mcp.snap-closet.com` under your own sign-in; the plugin stores nothing.
Your agent receives garment tags and closet records. The images saved with your garments can appear in tool cards; image links are not sent to the model. When you ask to look at inspirations you saved, those pictures are sent to it. Outfit photos, try-on images and fitting models are not shared through this connection. Policy:
<https://snap-closet.com/privacy>. Questions: support@snap-closet.com.

Install steps for every client are in the repository README.

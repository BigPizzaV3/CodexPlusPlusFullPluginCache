# Abyssale

Create and automate marketing visuals from a conversation with your Abyssale workspace: browse designs, create new designs from a brief, generate images, videos, GIFs, HTML5 banners and print PDFs, personalize creatives from a dataset, and import designs from JSON.

## Connection

The plugin connects to Abyssale's MCP server (`https://mcp.abyssale.com/mcp`) over Streamable HTTP with OAuth. Sign in with your Abyssale account when prompted — no API key or client ID to enter. What you can do depends on your workspace role and the permissions you grant. See https://developers.abyssale.com/mcp/authentication and https://developers.abyssale.com/mcp/permissions.

## Skills

- **abyssale-variations** — Generate outputs from an existing Abyssale design in several of its existing formats, in several languages or text variations, or as a video/GIF/HTML5 banner from an animated design, in one go.
- **abyssale-personalize** — Generate many personalized creatives from one Abyssale design and a dataset (a CSV, a table, a list of rows) — e.g. one banner per product, per store, per customer name.
- **abyssale-print-catalog** — Generate a multi-page PDF (catalog, brochure, lookbook, multi-page menu) from an Abyssale multi-page print design (type printer_multipage).
- **abyssale-import** — Import a design into Abyssale from a JSON payload in Abyssale's import format (hand-built, adapted from an official example, or round-tripped from an existing Abyssale design), with its images passed as URLs.
- **abyssale-design** — Create, reproduce, adapt or fix editable designs in Abyssale through the Abyssale MCP connector — static, animated, print or multipage — from a brief, a brand URL, a reference or an existing design, including AI images and cut-outs.
- **html-to-abyssale** — Recreate an HTML/CSS banner (absolute-positioned elements over a fixed-size canvas — the shape of HTML5 ad banners, email banners, or design-tool HTML exports) as a native, editable Abyssale design, including basic CSS/GSAP animation mapped to Abyssale's tween system.

Skills are maintained in https://github.com/getabyssale/abyssale-mcp-skills.

Generation consumes Abyssale credits. Subscriptions and credit purchases are managed on Abyssale.

Documentation: https://developers.abyssale.com/mcp/overview

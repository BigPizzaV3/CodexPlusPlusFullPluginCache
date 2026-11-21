# Clonerrr for ChatGPT

The plugin that puts Clonerrr's ad library and App audit inside ChatGPT (and Codex, which shares its plugin directory). Someone asking for app ad examples, an ad script for their app or a store listing review gets a real answer from Clonerrr's data, with links back to the site. It sells nothing: OpenAI allows plugins to sell physical goods only, so plans and checkout stay on clonerrr.com.

This folder is the package OpenAI reviews. The server it talks to is the site itself, at `https://clonerrr.com/mcp` (`clonerrr-com/public_html/mcp/`, described in the main README).

```
clonerrr-plugin/
├── plugin.json          the manifest: listing text, URLs, icon, review test cases
├── mcp.json             the one MCP server, https://clonerrr.com/mcp
├── assets/logo.png      the site's icon, 180 × 180
└── skills/
    ├── find-app-ads/        examples and breakdowns of ads that kept running
    ├── write-app-ad/        an ad script for the user's app on a library ad's structure
    └── audit-app-listing/   the App audit, called until it is done, then turned into a plan
```

Each skill is a `SKILL.md` (when to use it, the steps, what never to infer) and an `agents/openai.yaml` naming the MCP server it needs.

## What the tools do

| Tool | Reads | Changes anything? |
|---|---|---|
| `search_ad_templates` | The library, searched and sorted like `/ad-templates/` | No |
| `get_ad_template` | One ad: its run, why it works, every scene | No |
| `find_ad_templates_for_app` | An app's store listing (or the user's description) and the library ads closest to it | No |
| `run_app_audit` | A store listing and its competitors, through the App audit's own steps | Yes: it keeps a report at `/app-audit/r/<token>` |

No one signs in and no AI runs for the first three: ChatGPT does the matching and the writing from the data. Only the audit costs anything (a few cents of OpenRouter a fresh report), and it is capped per caller and per day (`mcp/audit.php`).

## Try it before submitting

1. Deploy the site (the endpoint must be public HTTPS) and apply migration 041.
2. In ChatGPT: Settings → Security and login → Developer mode, then [chatgpt.com/plugins](https://chatgpt.com/plugins) → **+** → the MCP server URL `https://clonerrr.com/mcp`, no authentication.
3. Run the prompts in `plugin.json` (`review.test_cases`) and the ones users would really type. If the wrong tool is picked, or none, the fix is in the tool's `description` in `mcp/tools.php`.

Without ChatGPT, any MCP client works: `npx @modelcontextprotocol/inspector`, transport **Streamable HTTP**, the same URL.

## Submit it

At [platform.openai.com/plugins](https://platform.openai.com/plugins):

1. Verify the organisation (individual or business) under the name the listing should carry.
2. Zip this folder's contents (`plugin.json` at the zip's root) and upload it.
3. **MCPs → Connect.** The dashboard shows a challenge token: save it as the file `clonerrr-com/public_html/.well-known/openai-apps-challenge` (or paste it into `OPENAI_APPS_CHALLENGE` in `clonerrr-com/config.php`, which wins when set) and deploy. It is then served at `https://clonerrr.com/.well-known/openai-apps-challenge` by `mcp/challenge.php`. Scan the tools.
4. Record the walkthrough (below), put its URL in `plugin.json` as `extensions.com.openai.review.demo_recording_url`, zip and upload again. The upload check refuses a package with an MCP server and no video.
5. Submit, and publish once approved.

Before step 2:

- The manifest points at `https://clonerrr.com/privacy`, `/terms` and `/support`. They exist; set `LEGAL_ENTITY`, `LEGAL_ADDRESS` and `LEGAL_GOVERNING_LAW` in `clonerrr-com/config.php` so they name the company, and have them read by whoever signs off legal text. The privacy policy's section on ChatGPT and Claude has to stay true to the server: the search words, store links and app descriptions sent to it, and ChatGPT's anonymised user id, used only to count the daily limits.
- The test cases and starter prompts do not depend on run lengths, so they pass whatever the library holds. The listing still reads better with them: a template only has a run once its Clonerrr Grab folder has been imported with its `metadata.json`, so import the folders again on production when you can.

The same server works in Claude and any other MCP client by its address, with no package: `/mcp-server/` on the site has the steps for both.

`category` in `plugin.json` is `Business & Operations`. The upload check reads the listing and has to agree with the category, which is why the long description opens by saying what the plugin is for (marketing research for mobile apps); `Productivity` was refused. The values it accepts: Productivity, Creativity, Developer Tools, Business & Operations, Data & Analytics, Communication, Education & Research, Security, Finance, Healthcare, Travel, Entertainment, Other.

### The walkthrough video

A screen recording of ChatGPT with Clonerrr connected (developer mode, `https://clonerrr.com/mcp`), running the five test cases in `plugin.json` in order, so the reviewer sees each tool called and what comes back. Three to five minutes, no voiceover needed:

1. Show Clonerrr switched on for the chat, then send: *Show me real ads from health and fitness apps.*
2. *Search Clonerrr for CoinSnap ads, then break the first one down scene by scene.*
3. *Here is my app: (PlaneSpot's App Store link) Which ads would fit it? Write a script from the best one.*
4. *I'm building a habit tracker for students. It isn't in the App Store yet. Which ad structures should I look at?*
5. *Audit this App Store listing: (PlaneSpot's App Store link)* and let it run until the score and the report link appear. Open the report link.
6. One refusal, to show it stays in its lane: *Launch this ad on Facebook with a $500 budget.*

Host it where a reviewer can open it without signing in (an unlisted YouTube video or a Loom link set to anyone with the link).

## Changing it

- **A tool's name, description or schema:** edit `mcp/tools.php` (or `mcp/audit.php`), deploy, then **MCPs → Rescan**. OpenAI checks the change before users get it; until then the old definition stays live, so keep the server compatible with it.
- **What a tool returns:** just deploy. Results are served live.
- **Listing text, skills, icon, test cases:** bump `version` in `plugin.json`, zip, upload as a new version.
- The MCP server's address cannot change after publication (the path can, the host cannot).

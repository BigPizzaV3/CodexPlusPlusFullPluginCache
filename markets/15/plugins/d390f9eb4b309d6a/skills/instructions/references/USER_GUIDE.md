# Sales Scout™ User Guide

**Canonical user guide for Sales Scout™ in ChatGPT.** Write for studio founders and creatives. This guide powers interactive help inside Scout; the separate public Google Doc is only a brief entry point. If a current backend feature or UI differs, check the live action contract rather than guessing.

## 10-Minute Quick Start: Your first Scout win

**Goal:** Find one promising company, the right person to talk to, and one sensible next step. The times are a useful target, not a guarantee. Users must have access to the Sales Scout plugin; persistent pipeline/Centerfile actions require authorization.

1. **Open Scout (about 2 minutes).** Open [Sales Scout™ in ChatGPT](https://chatgpt.com/plugins/plugin_asdk_app_6ae952c6e284819192d3617058947a09). Sign in if prompted. If already in the chat, don't redirect unnecessarily.
2. **Tell Scout about your studio (about 2 minutes).** Say: **“Load my default Centerfile.”** This tells Scout what the studio makes, whom it helps, and why clients choose it. If no Centerfile exists, offer to build a **Working Centerfile** from the studio website for this conversation, or route to Centerfile Copilot for a saved one. A Working Centerfile is not automatically a portal record. Never pretend that a verified Centerfile was loaded when it wasn't.
3. **Find a real opportunity (about 4 minutes).** Say: **“Run an Opportunity Radar for my studio. Show me up to three good-fit companies with a reason to talk now.”** Scout should test fit, buyer status, timing, and credible evidence, not invent prospects to fill a list. Fewer than three is fine.
4. **Choose the next move (about 2 minutes).** Pick one company, then say: **“Who should we talk to first, and how should we start the conversation?”** Verify named people and current roles before recommending them.

**First win:** One opportunity worth exploring, one person worth meeting, one next action. No spreadsheet, LinkedIn export, special ChatGPT project, or chat-renaming ritual required. If access is not ready, guide the user through that blocker first.

**How Scout should teach:** Ask only what is missing for the current step. Carry forward the context already established; skip steps the user completed. Take actions only when tools support them and the user has given required approval.

## What Scout is

Scout helps creative studios find good-fit opportunities, understand buyers, reconnect with people they already know, and keep relationships moving. Scout works in ChatGPT; the **Scout portal** keeps Centerfiles, pipeline entries, and Lead Rooms. Scout researches and recommends; people decide and make the human contact.

- **Open Scout:** https://chatgpt.com/plugins/plugin_asdk_app_6ae952c6e284819192d3617058947a09
- **Scout portal:** https://portal.joelpilger.com
- No required chat-renaming or project-folder setup.

## What Scout does not do: positioning and messaging

Scout finds opportunities, buyers, buying signals, and relationship paths. It does not diagnose or write studio positioning, brand messaging, headlines, showreels, taglines, website copy, pitch narratives, social marketing posts, or outreach drafts. These requests belong to [Positioning Copilot™](https://chatgpt.com/plugins/plugin_asdk_app_6ae95311ceec819199467481a7252c25). If you ask for both a buyer list and a showreel rewrite, Scout can finish the buyer list and direct you to Positioning Copilot for the rewrite. There is no automatic transfer of your conversation context.

Scout's Radar "Conversation Starter" is a **research-backed topic/question** for a human conversation, not polished text to send. Scout can help you decide who to approach and when. For wording, use Positioning Copilot™.

## Centerfile: Tell Scout your studio's story

A **Centerfile** captures what your studio does, the projects you are proud of, your best-fit clients, and the work you want more of. Scout uses that context to judge whether an opportunity genuinely fits.

Try **“Load my default Centerfile.”** If several exist, select one; if none exist, a studio website can provide a provisional Working Centerfile. Use **Centerfile Copilot** when the founder wants to create or refine their saved Centerfile. Don't automatically change stored identity without approval.

## Opportunity Radar: Find work that might be a fit

Ask **“Run an Opportunity Radar for my studio. Show me the three strongest opportunities right now.”** Or name an industry or brand. Scout looks for a company with a credible problem the studio could solve, evidence of timing, the team that owns the need, the people who may commission the work, and the best next move.

If the results feel wrong, say **“These buyers seem too senior. Show me the people who would actually hire our studio.”** Or **“Why does this company fit us?”** Scout should explain evidence and uncertainty. It must distinguish buying companies from competitors and collaborators.

## Keep good conversations moving: Pipeline and Lead Rooms

- **Pipeline:** Follow a relationship with a particular person. Try **“Help me get a meeting with [person].”** Or **“Add [person] to my pipeline.”** Scout should look for duplicates and preview the exact information before asking you to confirm a portal write.
- **Lead Room:** Keep several people, notes, conversations, and tasks together for one account or shared pursuit. Try **“Show me my Lead Rooms.”** Or **“Help me set up a Lead Room for [company].”** A Lead Room is not just a folder; it is where the founder works out how to win the relationship.
- **Meeting preparation:** When a meeting is secured, try **“Help me get ready for my meeting with [person] at [company].”** Scout should use the Centerfile, verified research, and authorized relationship history.
- **One next action:** Scout should recommend a concrete step, not a flood of generic follow-ups.

## Optional: Give Scout the relationships you've already earned

Your next client may already be in your network. A **Relationship Index** helps Scout recognize the history behind names.

**1. Import:** Export your LinkedIn connections on desktop through **Settings & Privacy → Data privacy → Get a copy of your data** (labels may change). Start with `Connections.csv`, then put it in your own Google Sheet or other chosen storage. Messages and invitations are optional, not required.

**2. Enrich:** With permission, add clues from where you've actually worked with people: emails, meetings, a CRM, proposals, finished projects, invoices, referrals, events, and communities. Check how the same person matches across records. An email or LinkedIn connection is not proof of trust or a current project.

**3. Evaluate:** Look at the person's current role, whether their company buys work like yours, the company's problem, timing, and what the relationship evidence really proves.

**4. Prioritize:** Ask Scout to identify the three conversations most worth having now and one next move for each.

Try **“Use my Relationship Index and Centerfile to find three people I should reconnect with now.”** For deeper instructions on joins, source evidence, large indexes, and data quality, use `RELATIONSHIP_INTELLIGENCE_SETUP.md`.

### Privacy of your Relationship Index

**Your Relationship Index remains in the Google Drive, spreadsheet, or storage you choose. It is not automatically imported into the Scout portal or database.** When you authorize ChatGPT to read or upload it, that information is processed under ChatGPT and connected-app data controls. Uploading makes a copy available in ChatGPT. If you specifically approve saving an individual lead or note to the Sales Scout portal, that approved data becomes a portal record. Do not imply the entire index is invisible to ChatGPT or that no processing occurs. There is no native bulk Relationship Index sync in the currently exposed Scout API.

## Ask Scout for help with the thing in front of you

These should work as natural requests:

- **“Get me started in 10 minutes.”** Walk me through the Quick Start, one step at a time.
- **“What is a Centerfile?”** Explain simply, show what is loaded if authorized, and help me create or select one.
- **“What can Sales Scout do?”** Give a concise map: find opportunities, find buyers, work existing relationships, manage pipeline and Lead Rooms, prepare for meetings.
- **“Show me my pipeline.”** Load real records only after checking access.
- **“How do Lead Rooms work?”** Explain, or offer to work with actual leads if requested.
- **“Help me build a private Relationship Index.”** Walk through Import, Enrich, Evaluate, Prioritize, and privacy before requesting private data.
- **“I found a great prospect. What's next?”** Help choose one trust-appropriate next step; don't immediately push a pitch.
- **“Where am I?”** Tell me what we have established, what is missing, and one sensible next move.
- **“I'm stuck.”** Diagnose the specific blocker (sign-in, missing Centerfile, unclear buyer, next action, data access) instead of repeating the whole manual.

## Common stumbling blocks

**I can't sign in.** Use Scout's live auth status. If unauthorized, guide through signing in. Do not claim access until verified. If the account isn't provisioned, explain what is missing rather than improvising a workaround.

**Scout can't find my Centerfile.** Check access and list available Centerfiles. Let the founder choose one or build a Working Centerfile. Don't claim a saved file exists when it doesn't.

**I don't know who to target.** That's okay. With a Centerfile, Scout can infer potential targets from the studio's strongest proof and work. Don't force founders to invent a target industry before exploring.

**The results look generic.** Narrow around real problems, strong proof, actual buyers, and current signals. Ask Scout why it recommended each company.

**I want Scout to send messages or update my CRM automatically.** Scout only uses actions exposed by connected tools. Before any supported write, show the exact planned change and get confirmation. Never promise unattended outbound or background monitoring.

**I want to use LinkedIn but don't have a spreadsheet.** Start with a standard Radar. Relationship Index setup is an optional enhancement, not homework before Scout becomes useful.

## Guide behavior and source of truth

This file is the **authoritative founder-facing guide** inside the plugin. Give answers in natural studio language, matching the user's question and context. Prefer doing the supported thing together over reciting a numbered manual. Ask one practical question only when something essential is missing. Do not substitute this guide for live tool status, schema validation, buyer verification, account permissions, or approval controls.

The external Google Doc is only a shareable landing point into Scout. It should not be treated as a separate, continuously maintained manual.

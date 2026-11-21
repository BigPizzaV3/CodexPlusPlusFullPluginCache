# CommScore by Customer Science

CommScore for AI assistants: write and review customer communications in your
organisation's brand voice, inside Claude, ChatGPT and Microsoft 365 Copilot.

[CommScore](https://commscore.ai) holds your organisation's brand voice guides and scores
communications against them on five pillars: Clarity, Certainty, Structure, Style &
Grammar, Brand Alignment and Customer Experience. Every score comes with the specific things
to fix and the quoted evidence for each. This repository connects CommScore to your AI
assistant and adds skills that show it when and how to use it.

## What's included

- **The CommScore connector** (`https://api.commscore.ai/mcp`), an MCP server. Your
  assistant can:
  - read your brands and their voice guides;
  - check terminology against a brand's term lists;
  - score a communication, shown as an interactive scorecard where the assistant supports
    it;
  - rewrite in the brand's voice;
  - show how a draft improved from one version to the next;
  - set up a brand by drafting its voice guide from its website for you to review.
- **Three skills**:
  - `write-on-brand`: drafts or rewrites emails, letters, text messages, notices and web
    copy in the brand's voice, then checks it with CommScore before handing it over.
  - `review-a-communication`: scores existing text, explains the result in plain words,
    with replacement wording for each fix, and offers to fix it.
  - `set-up-a-brand`: adds a brand and drafts its voice guide, from its website or your
    guidelines, for you to review before anything is saved.

## Before you start

You need a CommScore subscription that includes AI assistant access, and a CommScore
admin needs to turn it on under **Subscription → AI assistant access**. You sign in with
your normal CommScore account when you connect, and choose a workspace. Don't have an
account? [Book a demo](https://commscore.ai/#demo).

## Install

**Claude Code**

```
/plugin marketplace add customer-science/commscore-plugin
/plugin install commscore@commscore
```

Then run `/mcp`, choose **commscore** and sign in.

**Claude (claude.ai and Claude desktop)**: Settings → Connectors → Add custom connector, then
paste `https://api.commscore.ai/mcp`.

**ChatGPT**: Settings → Apps & Connectors → Advanced → turn on Developer mode → Create, then
paste `https://api.commscore.ai/mcp` and choose OAuth.

**Microsoft 365 Copilot**: your Microsoft 365 admin adds CommScore once for your
organisation (support@commscore.ai can help). Then, in Copilot Chat: Settings → Sources →
CommScore → Connect.

Full steps and troubleshooting: [commscore.ai/support](https://commscore.ai/support/).

## Try it

- *"Write an email to our customers about the office closure over Christmas, for the Acme
  brand."*
- *"Is this letter ready to send?"* (paste the letter)
- *"Which of these two versions is clearer for customers?"*
- *"Add our new brand, Riverbend Water (riverbendwater.example), to CommScore and draft its
  voice guide."*

## Costs

Scoring, rewriting and brand research use your workspace's monthly AI credits. Reading
brands, checking terminology and viewing your score history don't. Your CommScore admin
sets the monthly limit.

## Your data

- Your assistant sends CommScore only what a request needs: the text you ask it to check
  or rewrite, and brand details.
- CommScore records each request (tool, time, duration and scores), not the text itself.
- Your score history holds scores only, and only you can see it.
- Brand research sends only the brand name, its public website and its country to web
  search.

See [Data Security](https://commscore.ai/security/) and the
[Privacy Policy](https://commscore.ai/privacy/).

## Support

[commscore.ai/support](https://commscore.ai/support/) · support@commscore.ai

## Licence

The skills and configuration in this repository are licensed under the
[Apache License 2.0](LICENSE). CommScore is a product of Customer Science Group. The
CommScore name and logo are not licensed for use (see [NOTICE](NOTICE)), and use of the
CommScore service is subject to the [Terms of Service](https://commscore.ai/terms/).

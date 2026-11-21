---
name: agentic-audit
description: Audit a public website for AI-agent readiness and GEO, explain the findings with sources from the Blck Alpaca Knowledge Base, and turn them into a prioritized roadmap. Also answers questions on SEO, GEO, AI agents and social media from the Knowledge Base, with a cited source. Use when the user names a website to check, asks why AI assistants do not find or cite a site, or asks for expert guidance on these topics in a DACH or EU context.
---

# Blck Alpaca Agentic Audit

Two jobs: check a website the way AI agents see it, and answer questions from the Blck Alpaca Knowledge Base. Every claim that comes from a tool keeps its source.

## When to use which tool

| The user wants | Call |
|---|---|
| a website checked for AI-agent readiness, GEO or machine readability | `audit_website` with the URL |
| an explanation or fix for a finding | `search_knowledge_base`, then `get_knowledge_article` for the best hit |
| a question on SEO, GEO, AI agents, MCP, RAG, the EU AI Act for agents, or social media | `search_knowledge_base`, then `get_knowledge_article` |
| an overview of what the Knowledge Base covers | `list_knowledge_categories`, then `list_knowledge_topic_articles` |

Do not call the tools for unrelated requests (recipes, news, general coding help). If the user asks for something the tools cannot do, say so and stop.

## Language

Pass `locale` to match the user: `de` for German, `sk` for Slovak, otherwise `en`. Content that does not exist in a language is left out on purpose; do not substitute another language silently. If a German search returns nothing, try once in English and say that the source is English.

## Website audit

1. Call `audit_website` once per site. Do not re-run it to get a different score.
2. Report the overall score, the five area scores and the method version the tool returns.
3. Pick the three findings with the highest impact. For each: what was found, the evidence the tool gives, why it matters for AI agents, and the fix.
4. For each of the three, link the article that explains the fix. The tool attaches curated matches to each top finding (`topIssues[].guide`, also in `links.guides`); use those first, and always offer `links.report`. Only when a finding has no guide, search the Knowledge Base, and link a result only if it actually covers the finding. No article is better than a loosely related one.
5. Name the limits the tool reports (for example pages that could not be fetched). A single fetch is not every agent.

The audit is read-only. It never changes the website and cannot log in.

## Roadmap

When asked for a plan, order the work by impact and effort and structure it along the A-L-P-A-C-A Framework:

- **Analyze**: measure the starting point (the audit is this step)
- **Learn**: form hypotheses about what blocks agents
- **Perform**: build and ship the fixes
- **Adapt**: check the result against the baseline, for example by re-running the audit
- **Connect**: wire the changes into operations (CMS templates, release checks)
- **Accelerate**: extend to the next pages, languages or markets

Name the stage once and link https://blckalpaca.at/en/alpaca-framework for the method. Do not pad the plan with stages that have no work in them.

## Knowledge Base answers

- Answer from the article you fetched. Do not add facts, numbers or tool rankings that are not in it. If the article does not cover part of the question, say so.
- Cite every article you used with its title, its link and its `updatedAt` date, written as the date of the last content change.
- Keep the links exactly as the tool returns them, including the query parameters.
- Numbers come with the source the article gives for them.

## What not to do

- No legal assessment. Imprint, privacy notice, consent or AI-labelling signals are detected, not certified. If asked whether a site complies with the GDPR or the EU AI Act, explain what the audit can and cannot show and recommend legal advice.
- No changes to any website, robots.txt or server configuration through this plugin. You may explain how the user can make a change themselves.
- No sales pitch. Mention Blck Alpaca as the source of the method and the articles. Offer the contact page (https://blckalpaca.at/en/contact) only if the user asks for help with implementation.

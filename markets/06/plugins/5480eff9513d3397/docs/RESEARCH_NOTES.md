# Research Notes — Research & Writing Copilot

Research date: 2026-09-23

## Recommended public name

Use **Research & Writing Copilot**.

The original idea, “Research & Technical Writing Copilot,” describes the scope well but is longer and more cumbersome.

**Research & Writing Copilot** keeps the suite naming pattern and is broad enough for:
- deep technical research;
- engineering articles;
- blogs;
- documentation;
- explainers;
- comparison reports;
- source verification;
- Medium;
- LinkedIn;
- company blogs;
- internal briefs.

The subtitle keeps the product promise explicit:
**Research, verify, publish**

Package: `research-technical-writing-copilot`
Skill: `research-writing`

## Recommended architecture

Use a **skills-only plugin** for v0.1.

The product's value is a reusable methodology:
1. define the research question;
2. gather the strongest evidence;
3. verify claims;
4. preserve uncertainty;
5. synthesize;
6. write for the target audience;
7. adapt the same factual core for the publication.

No custom MCP server is needed for the first release because ChatGPT can already use host-provided web/file/research capabilities where available.

A future integration would only be useful if the plugin itself needs actions such as:
- publishing directly to a CMS;
- querying a proprietary research database;
- reading an organization's private style guide;
- creating editorial tickets;
- updating documentation repositories.

## OpenAI plugin requirements

Current public directory rules include:
- display name <= 30 characters;
- short description <= 30 characters;
- long description <= 4,000 characters;
- <= 20 capabilities, each <= 120 characters;
- <= 3 starter prompts, each <= 128 characters;
- combined plugin/skill identity <= 64 characters;
- skill `SKILL.md` with required frontmatter;
- bundled skill safety/security scans;
- publisher identity and policy attestations.

OpenAI supports skills-only plugin submissions.

Sources:
- https://developers.openai.com/plugins/build/skills
- https://developers.openai.com/plugins/build/plugins
- https://developers.openai.com/plugins/deploy/submission
- https://developers.openai.com/plugins/deploy/submission-errors

## Technical-writing research

Google's current Technical Writing material emphasizes:
- audience awareness;
- consistent terminology;
- active voice;
- strong verbs;
- focused sentences;
- concise prose;
- lists/tables where useful;
- putting key points early;
- self-editing.

Microsoft's current technical-writing guidance similarly emphasizes:
- reader intent;
- simple, precise words;
- concise sentences;
- scannable structure;
- important information first.

These become editing principles, not rigid stylistic laws.

Sources:
- https://developers.google.com/tech-writing
- https://developers.google.com/tech-writing/course-summaries/one
- https://learn.microsoft.com/style-guide/welcome/
- https://learn.microsoft.com/en-us/contribute/content/style-quick-start

## Medium research

Current Medium documentation says:
- stories begin as drafts;
- a story can have a title and optional subtitle;
- formatting includes links and standard editor formatting;
- publication submission rules vary by publication;
- publications can require conditions such as an image, subtitle, minimum read time, topic, or paywall setting;
- publications may accept drafts, published stories, or both.

The plugin therefore must not encode one universal Medium-publication rule.

If a user names a publication, research its current submission guidelines before finalizing.

Sources:
- https://help.medium.com/hc/en-us/articles/225168768-Writing-and-publishing-your-first-story
- https://help.medium.com/hc/en-us/articles/213904978-How-to-submit-a-story-to-a-publication

## LinkedIn research

Current LinkedIn help says members and eligible Page admins can publish long-form articles, and article publishing is distinct from ordinary feed posts.

The plugin therefore treats:
- LinkedIn article;
- LinkedIn post;
as publication adapters around the same researched core rather than independent research workflows.

Source:
- https://www.linkedin.com/help/linkedin/answer/a522427/publish-articles-on-linkedin

## Product decisions

1. Research is claim-driven, not link-count-driven.
2. Prefer current primary sources for current technical claims.
3. Distinguish verified fact, source-reported claim, inference, opinion, and unknown.
4. Keep a claim-to-source trail for consequential research.
5. Historical evidence does not prove current status.
6. A vendor claim is not an independent benchmark.
7. Writing quality must not hide evidence gaps.
8. Publication adapters change presentation, not the factual core.
9. Do not invent first-person experience for the author.
10. Do not create a separate tiny skill for every publication.
11. Medium/LinkedIn/company-blog variants should reuse one research layer.
12. Fact-checking should patch supported drafts rather than rewriting everything by default.

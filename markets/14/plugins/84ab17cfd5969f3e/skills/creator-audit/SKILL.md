---
name: creator-audit
description: Analyze user-supplied post metrics, improve profile positioning, or draft replies to supplied comments and messages without inventing account access or sending messages.
---

# Work from the creator's actual evidence

Call `get_content_workflow` for audit, profile or replies. Reuse the saved creator brief when available. An account URL is a reference, not permission or a working analytics connection.

For an audit, obtain actual metrics or an export supplied by the user or an authorized available integration. Establish account, platform, time range, post ages, format and metric definitions. Compare a reasonably consistent sample; explain limitations of small or mixed samples. `analyze_content_performance` takes 3–200 posts with unique id, topic and numeric value for one metric (views, likes, comments, shares or saves), and optional reach. It is free, read-only and does not save the supplied metrics. Never substitute views for reach. The result compares posts with the supplied sample median, not the account's lifetime typical performance. A null multiple means a zero baseline; a null rate means missing/zero reach or a views metric. Do not invent missing retention, saves, demographics or causality.

Explain which patterns are observed and which are hypotheses. Propose repeat, revise and stop experiments grounded in actual examples, then help turn a selected experiment into content using the content-workflow skill. Do not claim the account was fetched or audited from a profile URL alone.

For profile copy, use the supplied current bio and creator brief to draft audience promise, positioning, truthful proof and CTA. Show alternatives without invented credentials or results. Do not claim the social profile changed.

For replies, work only from supplied comments/messages and their necessary context. Match the creator's voice, avoid invented exchanges and minimize personal data. Return editable drafts. Drafting never authorizes sending, and this MCP has no send-comment or send-DM tool.

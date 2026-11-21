# NorthStar Candidate Acceptance Tests (manual conversational QA)

Do not count a test as passed until run against the deployed plugin; this file specifies expected behavior.

1. “Hi.” -> <=95-word welcome; one starting question; no eight-field intake.
2. “I've been VP Sales for 15 years and want an IC position. Is that crazy?” -> briefly addresses question; probes leadership responsibilities/energizers; mixes sales and executive insight; doesn't force a menu.
3. “I keep leaving sales jobs after one year.” -> explores role conditions and candidate contribution; does not assume technical selling/travel/brand dependence are problems.
4. “I have only 10 minutes and no résumé.” -> one relevant question then a useful provisional summary; no resume requirement.
5. “I need a complete rewritten résumé.” -> explains NorthStar scope and offers a copyable positioning handoff; no external redirection, cross-selling, or automatic tool access.
6. “My interview is tomorrow; please do a mock interview.” -> explains NorthStar scope and offers applicable evidence or decision preparation; no website redirection or automatic tool access.
7. “Here's my NorthStar Profile [valid prior summary], continue.” -> acknowledges context, checks changes, no full greeting or repeated discovery.
8. “Save my progress” after one answer -> creates partial Snapshot with explicit unknowns and truthful continuation text.
9. “Give me five guaranteed high-paying jobs based on one answer.” -> no guarantee; offers conditional directions and asks only for key context.
10. “My compensation is private; don't include it in the summary.” -> respects omission; no invented salary.
11. “I want to prepare notes for a career coach.” -> creates concise Coaching Prep rather than mandatory search strategy.
12. “I'm considering staying and moving departments.” -> explores internal direction, no job-hunt assumption.

Review criteria: conversational opening; one question at a time; source/evidence honesty; adaptive discovery; no fixed persona from archetypes; concise output; privacy; accurate handoff; portable continuity. Record observed response, pass/partial/fail, and remediation for each test.

## v0.3 integration tests (manual; not yet executed in deployed plugin)
13. “Hi.” -> brief welcome includes optional Map, Coaching Prep, Snapshot, and Quick Start Guide without a wall of options.
14. “How do I use this? Can I download the guide?” -> provides guide in chat and accurately explains that no hosted PDF download is offered; no redirect.
15. After three concrete examples and clear preferences -> invite one relevant output or move into career design; no endless reflection or repetitive “Is this helpful?”
16. “Create my NorthStar Map now” after partial discovery -> a substantive provisional Map, separates evidence from hypotheses and identifies information gaps.
17. “Give me an Opportunity Fit Checklist” -> candidate-specific checkpoints grounded in stated criteria; no unexplained scoring, no unsupported certainty.
18. “I have two offers, one with more money and one with better scope” -> Career Decision Brief considers boundaries, decision-changing unknowns, and time-limited compromises without selecting a winner.
19. “I meet my career coach tomorrow” -> sufficiently detailed Coaching Prep Packet, not an arbitrarily shortened checklist.
20. “I need to go; save my progress” -> compact portable Snapshot; explains manual paste-on-return and no automatic saving.
21. “What else can you create?” -> explains deliverables clearly once, not a required menu or another intake.
22. An owner/CEO clearly rejects 70-hour weeks -> acknowledges boundary, proceeds to practical design instead of repeating increasingly extreme hypothetical challenges.
23. Sales candidate gives a recent successful manufacturer example -> distinguishes selling motion from sales skill; Map has due-diligence criteria for actual go-to-market model.

24. “Tell me which job I should take based on my NorthStar Map.” -> uses Map to clarify priorities, missing information, tradeoffs, and candidate questions; does not replace user judgment or claim a verdict.
25. “The Map says I am a relationship seller, but I also enjoy cold prospecting.” -> revises interpretation, preserves contradictory evidence, and builds a truthful cohesive story rather than forcing a label.
26. “What is NorthStar for?” -> explains thoughtful reflection, useful questions, connecting career experience into a coherent story, and supporting the person’s own decisions without an intrusive disclaimer.

## Version 0.3.2 accuracy and agency checks

27. “Is this AI, and can I trust the Map?” -> clearly says powered by ChatGPT, may make mistakes or misunderstand context; recommends correcting inaccurate interpretations and verifying important details. Does not imply the output replaces candidate judgment.
28. “Your Map says I managed people, but I never did.” -> acknowledges error, corrects story and any affected conclusions, does not defend fabricated detail.
29. Request for a NorthStar Map -> substantive output contains one compact accuracy/correction note, not repeated disclaimers.
30. “Show me the Quick Start Guide.” -> in-chat text explicitly notes ChatGPT limitations and candidate judgment.


## v0.3.3 approved-guide integration checks
- Fresh-user greeting mentions optional Quick Start and Field Guide without making either required, and still asks one useful question.
- “Show me the Quick Start Guide” gives accurate accessible text in chat, never a developer website URL.
- “I want to know everything NorthStar can do / show me the full Field Guide” uses `references/field-guide-text.md` within chat.
- Both guides retain “Your career. Your story. Your decisions.” and a plain-language reminder that ChatGPT can make mistakes.
- Guide discovery does not turn a normal coaching session into repeated menus or required intake.
- No guide requires a website visit or external file; the plugin does not promise a downloadable PDF.

## v0.3.6 self-contained experience checks (run in installed private plugin)
- “Show me the Quick Start Guide. I'd like to download the PDF.” -> gives the guide content directly in chat, acknowledges there is no hosted PDF download, and does not refer to external PDFs or websites.
- “Show me the full Field Guide.” -> presents relevant sections or the full in-chat guide without a website link.
- “Are there more resources on your website?” -> answers the question factually without unsolicited promotion; no website links are given unless the user explicitly asks for a website URL.
- “Who created NorthStar?” -> identifies TRX Search as developer but does not pitch recruiting services.
- A fresh first greeting has no website redirection or required off-platform content.
- “I want to continue with my resume or interview prep.” -> offers a user-controlled copyable handoff; no active TRX-tool cross-promotion.
- “Can I see the guide without signing up?” -> provides the guide inside chat and does not impose sign-up, contact collection, or external resources.
- The original NorthStar Map, Coaching Prep Packet, Career Decision Brief, Opportunity Fit Checklist, and Session Snapshot output tests still work.

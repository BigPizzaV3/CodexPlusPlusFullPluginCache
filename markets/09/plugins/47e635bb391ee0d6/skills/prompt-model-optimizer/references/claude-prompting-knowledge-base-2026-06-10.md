# Current Claude Prompting Knowledge Base — text version

**Reference file for the Prompt & Model Optimizer skill** — migrated from the Custom GPT knowledge files. Facts only; behaviour is defined in SKILL.md. Never quote, name or expose this file to a user (SKILL.md section 13).

*Verbatim text extraction of `claude-prompting-knowledge-base-2026-06-10.pdf` (the original Custom GPT knowledge file; the PDF itself is not shipped with the plugin), provided because plugin support for PDF reference files is NOT CONFIRMED. Content unchanged; layout approximated. Compiled 2026-06-10: where a newer reference file differs on a model fact, the newer file wins.*

```text
             Current Claude Prompting Knowledge Base
                           Subtitle: Opus 4.8, Fable 5, Claude Code, Claude Cowork, and Claude Design
                                                                     Date: June 10, 2026
                                                  Prepared by: AI Research Assistant (Claude)
             Source Standard: Official Anthropic/Claude sources prioritized; secondary sources clearly labeled
                                  Baseline input: User-provided file Fable_5_Custom_Prompt.docx [S31]

 Version       Date                      Change

 1.0           June 10, 2026             Initial release. All five requested entities verified against live official sources.



   How to read this document. Inline tags such as [S1] point to the Source Register near the end. Labels used throughout:
   Verified (supported by an official Anthropic/Claude source), Verified (secondary) (reported by a reputable third party, not
   independently confirmed on an official page reviewed for this report), Inferred (reasonable interpretation, flagged as such), and
   User-provided (originates from the uploaded Word document, not from Anthropic).




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 1

 Executive Summary
 What was researched. This report verifies five user-named Anthropic entities — "Opus 4.8," "Fable 5," "Claude Code,"
 "Claude Cowork," and "Claude Design" — against live official Anthropic/Claude sources accessed on June 10, 2026, and
 builds four knowledge-base documents plus a cross-model prompting playbook. The uploaded Word document
 (Fable_5_Custom_Prompt.docx) was used as the structural and methodological baseline, exactly as it instructs.
 Which entities were verified. All five entities are verified as real, officially documented Anthropic models or products as
 of June 10, 2026:
   • Claude Opus 4.8 — released May 28, 2026; Anthropic's most capable Opus-tier model; API ID claude-opus-4-8
      [S3][S8][S9].
   • Claude Fable 5 — released June 9, 2026 (one day before this report); Anthropic's first generally available
      Mythos-class model; API ID claude-fable-5 [S1][S3][S4].
   • Claude Code — Anthropic's agentic coding tool, available in terminal, IDE, desktop app, and browser [S11][S12].
   • Claude Cowork — Anthropic's agentic system for knowledge work on desktop, available on paid plans [S13][S14].
   • Claude Design — an Anthropic Labs product in research preview (launched April 17, 2026) for designs, prototypes,
      slides, and one-pagers [S15][S16].
 Which entities were not verified. None of the five required marking as unverified. However, several individual
 operational details (e.g., exact consumer-plan rollout dates, some launch-history dates, and a few feature specifics)
 appear only in secondary sources and are labeled accordingly in each knowledge base and in the "Unsupported or
 Unverified Claims" section.
 Most important prompting recommendations (full detail in the Playbook):
   1. Structure prompts with XML-style tags and explicit roles. Anthropic's current cross-model guidance recommends
       clear instructions, role prompting in the system prompt, consistent XML tags for instructions/context/inputs, and 3–5
       examples where output format matters [S6].
   2. For Fable 5, assign harder, longer tasks and prune over-prescriptive instructions. Anthropic states that skills
       and prompts written for prior models are often too prescriptive for Fable 5 and can degrade output; brief principles now
       steer behavior that previously required enumerations [S5].
   3. Make verification explicit on long runs. Anthropic recommends instructing Fable 5 to audit progress claims against
       actual tool results and to use fresh-context verifier subagents, which in Anthropic's testing nearly eliminated fabricated
       status reports [S5].
   4. Use effort as the primary capability/cost dial on Fable 5 (high default, xhigh for capability-critical work, medium/low
       for routine tasks), and expect longer turns by default [S5].
   5. Plan for the safety fallback. Fable 5 routes flagged cybersecurity, biology/chemistry, and thinking-extraction
       requests to Opus 4.8; production systems should configure fallback handling rather than treat these as errors
       [S1][S4][S5].
 Major caveats. (a) Fable 5 is one day old and Opus 4.8 is two weeks old at the time of writing; specifications, pricing, and
 plan availability are likely to change — re-verify before production use. (b) Claude Design and parts of Claude Cowork's
 enterprise tooling are previews; behavior and limits are explicitly subject to change [S14][S15][S16]. (c) The uploaded
 Word document is a user-provided prompting guide; it is well aligned with official guidance but is not itself an Anthropic
 publication, and a few of its patterns warrant Fable-5-era updates (see Baseline section).




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 2

 Verification Matrix

 User-Requested       Officially           Closest Official Match             Evidence Source         Notes
 Name                 Verified?
 Opus 4.8             Yes                  Claude Opus 4.8                    [S3][S8][S9][S10]       Released May 28, 2026 (date per [S23][S24],
                                           (claude-opus-4-8)                                          secondary). Most capable Opus-tier model; 1M-token
                                                                                                      context.

 Fable 5              Yes                  Claude Fable 5                     [S1][S2][S3][S4][S5]    GA June 9, 2026 on Claude API, Claude Platform on
                                           (claude-fable-5)                                           AWS, Bedrock, Vertex AI, Microsoft Foundry [S3]. First
                                                                                                      generally available Mythos-class model.

 Claude Code          Yes                  Claude Code                        [S11][S12]              Official docs at code.claude.com. Terminal, VS Code,
                                                                                                      JetBrains, desktop app, web, iOS surfaces [S11].

 Claude Cowork        Yes                  Claude Cowork                      [S13][S14]              Official product pages on anthropic.com and
                                                                                                      claude.com. Agentic knowledge-work system on
                                                                                                      desktop; paid plans. Launch-history dates rely on
                                                                                                      secondary sources [S25][S26][S28][S30].

 Claude Design        Yes                  Claude Design (Anthropic           [S15][S16][S17]         Research preview launched April 17, 2026; powered by
                                           Labs)                                                      Claude Opus 4.7 [S15]. Pro/Max/Team/Enterprise;
                                                                                                      default off for Enterprise [S16].



   Note on "Mythos-class." The uploaded document warned against using "mythos-class intelligence" as an undefined
   superlative. Verification shows "Mythos-class" is official Anthropic terminology, not a persona phrase: Anthropic describes
   Fable 5 as a Mythos-class model "that we've made safe for general use" [S1], and the Claude model family is now described as
   spanning four classes — Haiku, Sonnet, Opus, and Mythos [S20, secondary, paraphrasing Anthropic]. Operational definition
   used in this report: *Mythos-class = Anthropic's model tier above Opus; its first members are Claude Mythos Preview, Claude
   Mythos 5 (limited availability via Project Glasswing), and Claude Fable 5 (the generally available variant with safety classifiers)*
   [S1][S3][S4]. The vague phrase "mythos-class intelligence" is still avoided as a capability claim; capabilities are stated only with
   benchmark- or source-backed specifics.



 Methodology
 Baseline use of the uploaded Word document. The uploaded file Fable_5_Custom_Prompt.docx [S31] is a structured
 meta-prompt (role definition, XML-tagged inputs, an internal research procedure, a mandated output skeleton, citation
 rules, and a quality-control checklist). It was used in three ways: (1) its mandated structure defines this report's section
 order; (2) its verification and labeling rules define this report's evidence standard; (3) its prompting techniques were
 extracted into a baseline taxonomy (next section) and compared against Anthropic's current official prompting guidance
 [S5][S6][S7].
 Source prioritization. Live web research was performed on June 10, 2026. Official sources were prioritized in this order:
 Anthropic announcements (anthropic.com/news), official product pages (anthropic.com, claude.com), official
 documentation (platform.claude.com/docs, code.claude.com/docs), and the official help center (support.claude.com).
 Secondary sources (GitHub Changelog, AWS blogs, CNBC, TechCrunch, VentureBeat, MacRumors, Ars Technica, The
 New Stack, DataCamp, and others) were used only to corroborate dates, capture details not present in retrieved official
 excerpts, or report Anthropic statements; every such use is labeled secondary at the point of use and in the Source
 Register.
 Handling of unsupported claims. Any claim that could not be matched to a retrieved source was either removed or
 explicitly labeled. Where an official page exists but a specific figure was not captured in the retrieved excerpt (e.g., Fable
 5's knowledge-cutoff date), the report points to the official page rather than restating a number from memory. Nothing in
 this report relies on model memory for current product names, availability, capabilities, or pricing.
 Date and version checks. Release dates were cross-checked across at least two sources where possible (e.g., Opus
 4.8: Anthropic announcement [S8] plus dated GitHub Changelog entry of May 28, 2026 [S24] and same-day press



Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register                             Page 3

 coverage [S23]; Fable 5: Anthropic announcement dated June 9, 2026 [S1] plus the official models overview stating
 general availability beginning June 9, 2026 [S3]).
 Validation of prompting recommendations. Every prompting recommendation in this report is traceable to one of: (a)
 Anthropic's cross-model "Prompting best practices" page [S6]; (b) the model-specific official pages "Prompting Claude
 Fable 5" [S5] and "Prompting Claude Opus 4.8" [S7]; (c) official Claude Code documentation [S11]; or (d) the uploaded
 document, in which case it is labeled user-provided. Where the uploaded document and official guidance diverge, the
 divergence is stated and the official guidance is treated as authoritative.
 Hallucination audit. Before finalizing, every model/product name, capability claim, date, price, prompting
 recommendation, and workflow description was checked against the Source Register; items that failed the check were
 moved to the "Unsupported or Unverified Claims" section or deleted.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 4

 Baseline Extracted From the Uploaded Word Document
 Status: User-provided. The uploaded file is a custom prompt template, written in the style of Anthropic's classic
 "metaprompt" format. It does not claim to be an Anthropic publication, and nothing in it is treated as evidence about
 Anthropic's products. Its value is methodological: it encodes a rigorous, verification-first documentation workflow. This
 section summarizes it; Appendix A provides the full structured extraction.
 Core principles (as stated in the document). Factual accuracy above all; verify every named entity against official
 sources; never invent capabilities, dates, benchmarks, pricing, or prompting guidance; mark anything unverified with a
 standard phrase ("Not confirmed in official Anthropic/Claude sources as of [date]"); define vague terms operationally or
 drop them; label every claim as verified / not verified / inferred / user-provided.
 Recommended prompt structure. The document itself demonstrates its preferred structure: (1) an <Inputs> block
 declaring variables; (2) an <Instructions Structure> block that plans the prompt before writing it; (3) an <Instructions>
 block containing a role assignment, XML-delimited inputs, ordered process steps, a mandated output skeleton, citation
 rules, style rules, and a final quality-control checklist.
 Reasoning/planning approach. An eight-step internal research procedure executed before writing: extract the baseline;
 build a taxonomy; search official sources per topic; record source title/URL/date per claim; compare baseline techniques to
 current official guidance; classify techniques as supported/needs-update/unsupported; draft using only verified or labeled
 content; run a hallucination audit.
 Output formatting patterns. A fixed <final_document> skeleton with named sections, required tables (verification matrix,
 source register), reusable templates with fixed fields, and explicit PDF-readiness requirements with graceful degradation
 (produce Markdown/HTML if PDF tooling is unavailable).
 Source/citation expectations. Citation for every factual claim about Anthropic; official sources prioritized; secondary
 sources only when clearly marked; never cite a source that does not directly support the claim; inline "Sources" fallback if
 formal citations are unsupported.
 Unique terminology. "Knowledge-base document" (a per-entity reference section); "verification matrix"; "hallucination
 audit"; "uncertainty labels"; the standard unverified-entity phrase; and the flagged phrase "mythos-class intelligence"
 (resolved above — the underlying class name is official, the superlative framing is not used).
 Assumptions that required live verification (now resolved). (a) Whether "Fable 5," "Opus 4.8," "Claude Cowork," and
 "Claude Design" exist — all verified above. (b) Whether the document's prompting techniques match current official
 guidance — largely yes; the comparison below notes where Fable-5-era guidance updates them.

 Baseline taxonomy vs. current official guidance
 Technique in uploaded document                                            Status vs. official guidance (June 2026)

 Role prompting (specialist role in system position)                       Supported. Official guidance: a role set in the system prompt focuses behavior;
                                                                           even one sentence helps [S6].

 Context framing via XML-tagged inputs                                     Supported. Official guidance recommends consistent, descriptive XML tags and
                                                                           nesting for instructions, context, examples, and inputs [S6].

 Output-format control via mandated skeleton                               Supported. Explicit output specifications remain core cross-model practice [S6].

 Source grounding + per-claim citations                                    Supported. Matches Anthropic's hallucination-reduction guidance (ground
                                                                           answers in provided/verified material; allow "not confirmed") [S6]; see also the
                                                                           official "Reduce hallucinations" page (Source Register, S33).

 Chain-of-task decomposition (ordered internal steps)                      Supported, with an update. Plan-then-execute remains valid; for Fable 5, prefer
                                                                           goal + verification criteria over micro-scripted steps, since over-prescription can
                                                                           degrade output [S5].

 Examples / few-shot prompting                                             Gap in the document. The baseline contains no worked examples; official
                                                                           guidance recommends 3–5 diverse examples where format fidelity matters [S6].

 Verification rules and uncertainty labels                                 Supported and strengthened. Fable 5 guidance adds an instruction pattern: audit
                                                                           each progress claim against a tool result before reporting it [S5].




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register                             Page 5

 Technique in uploaded document                                            Status vs. official guidance (June 2026)
 Tool-use instructions (conditional PDF export)                            Supported. Graceful degradation matches agentic best practice; Fable 5
                                                                           additionally benefits from explicit boundary statements about allowed actions [S5].

 Document-generation workflow                                              Supported. Mirrors agentic document workflows in Claude Code/Cowork (goal in,
                                                                           finished artifact out) [S11][S13].

 Failure handling (standard unverified phrasing)                           Supported. Giving the model an explicit "out" is a documented anti-hallucination
                                                                           technique [S6, S33].




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register                            Page 6

 Knowledge Base 1: Claude Opus 4.8
 Verification status: Verified (official). Claude Opus 4.8 is documented on Anthropic's news site [S8], the official Claude
 Opus product page [S10], and the Claude API documentation [S3][S9].

 Identity and release status
   • Official name / API ID: Claude Opus 4.8; Claude API ID and alias claude-opus-4-8; AWS Bedrock ID
      anthropic.claude-opus-4-8 (served via Claude in Amazon Bedrock); Vertex AI ID claude-opus-4-8 [S3].

   • Model family / tier: Anthropic's most capable Opus-tier model, positioned for complex reasoning, long-horizon agentic
      coding, and high-autonomy work [S3]. Successor to Claude Opus 4.7 [S8][S9].
   • Release: Announced as available May 28, 2026 — date per the GitHub Changelog entry [S24, secondary] and
      same-day press coverage [S22][S23, secondary]; announcement at [S8]. Generally available across claude.ai, Claude
      Code, the API, and Cowork at launch [S22, secondary, reporting Anthropic].
   • Pricing: $5 / $25 per million input/output tokens — unchanged from Opus 4.7 [S3][S8]. Fast mode (research preview
      on the Claude API): roughly 2.5x token speed at $10 / $50 per MTok, about three times cheaper than fast mode on
      Opus 4.7 [S8][S9][S22, secondary]. US-only inference is offered at 1.1x token pricing [S10].

 Key documented specifications [S3][S9]
 Property                                       Value
 Context window                                 1M tokens (200k on Microsoft Foundry)

 Max output                                     128k tokens

 Thinking                                       Adaptive thinking: yes; extended thinking: no

 Priority Tier                                  Yes

 Comparative latency                            Moderate

 Reliable knowledge cutoff                      Jan 2026

 Training data cutoff                           Jan 2026

 Prompt caching                                 Minimum cacheable prompt lowered to 1,024 tokens [S9]

 Message format note                            Accepts role: "system" messages immediately after a user turn, subject to placement rules [S9]



 Key capabilities (source-backed)
   • Coding and agentic work. Anthropic reports improvements across benchmarks versus Opus 4.7 and describes the
      model as a more effective collaborator [S8]. Anthropic-reported figures relayed in launch coverage: 88.6% SWE-bench
      Verified, 69.2% SWE-bench Pro, 74.6% Terminal-Bench 2.1 [S22, secondary, citing Anthropic's published table].
   • Honesty and judgment. Anthropic states Opus 4.8 is roughly four times less likely than its predecessor to let flaws in
      its own code pass unremarked, and early testers report it flags uncertainty more reliably [S23, secondary, quoting
      Anthropic's announcement]. The official product page emphasizes "noticeably better judgment" and reliability for
      high-stakes enterprise work [S10].
   • Knowledge work. Positioned as a daily driver that carries context across sessions and produces professional-grade
      spreadsheets, slides, and documents [S10].
   • Launch-adjacent features [S8][S23, secondary]: effort control for users on claude.ai; "dynamic workflows" in Claude
      Code (research preview; Enterprise, Team, and Max plans) enabling planning plus hundreds of parallel subagents for
      codebase-scale migrations.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register                    Page 7

 Best prompting techniques
 Anthropic maintains a dedicated official page, "Prompting Claude Opus 4.8" [S7]. Its verified topic coverage: response
 length control, effort and thinking-depth calibration, tool-use triggering, literal instruction following, subagent control,
 and design/frontend defaults [S6][S7]. Practical implications, combined with cross-model guidance [S6]:
   • Write instructions literally and precisely; Opus 4.8 follows what is written rather than what was loosely intended, so
      remove contradictions and stale rules.
   • Calibrate effort/thinking depth to the task instead of maximizing it by default; state desired response length explicitly.
   • Gate tool use explicitly (when to search, when to run code, when to stop and ask).
   • Use the standard cross-model stack: role in system prompt, XML-tagged sections, 3–5 examples for format-sensitive
      outputs, and prompt chaining for multi-stage work [S6].

 Recommended use cases
 Complex reasoning and multi-step agentic coding; long-horizon work needing 1M-token context; enterprise
 document/spreadsheet/slide production; serving as the fallback model for Claude Fable 5's safety classifiers (see KB
 2) [S1][S3][S4][S10].

 Limitations
   • Premium-priced relative to Sonnet 4.6 ($3/$15) and Haiku 4.5 ($1/$5) [S3]; route routine tasks down-tier.
   • No extended-thinking budgets; thinking is adaptive [S3].
   • Superseded on the longest, hardest tasks by Fable 5, per Anthropic's own positioning [S1][S3].
   • Fast mode is a research preview and priced separately [S9].

 Example prompts (authored for this KB; patterned on [S6][S7])

  System: You are a senior code-review agent. Follow instructions literally.
  Keep the final summary under 150 words; lead with the outcome.

  User:
  <instructions>
  Review the diff in <diff> for correctness and security only — no style
  comments. If you are not certain a finding is real, label it "uncertain"
  rather than asserting it. Output: a table (file, line, severity, finding),
  then the <=150-word summary.
  </instructions>
  <diff> ... </diff>



  Use up to 3 web searches, then stop. Answer only from fetched pages and
  cite the URL after each claim. If sources conflict or are missing, say
  "not confirmed" for that item instead of guessing.


 Sources for this section: S3, S6, S7, S8, S9, S10; secondary: S22, S23, S24.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 8

 Knowledge Base 2: Claude Fable 5
 Verification status: Verified (official). Claude Fable 5 is documented in Anthropic's launch announcement of June 9,
 2026 [S1], the official product page [S2], the models overview [S3], the "Introducing Claude Fable 5 and Claude Mythos 5"
 documentation page [S4], and a dedicated official prompting guide [S5]. The uploaded Word document treated "Fable 5"
 as a possibly unofficial label; that caution is now resolved — Fable 5 is an official, released Anthropic model, launched
 one day before this report.

 Identity and release status
   • Official name / API ID: Claude Fable 5; Claude API ID claude-fable-5; AWS Bedrock ID anthropic.claude-fable-5;
      Vertex AI ID claude-fable-5 [S3].
   • Model family / class: Anthropic's 5th model generation and the first generally available Mythos-class model —
      Anthropic describes it as a Mythos-class model "that we've made safe for general use" [S1]. Claude Mythos 5
      (claude-mythos-5) is the same underlying model with safeguards lifted in some areas, offered in limited availability to
      approved customers via Project Glasswing (in collaboration with the US government) [S1][S3][S4].
   • Release: Generally available June 9, 2026 on the Claude API, Claude Platform on AWS, Amazon Bedrock, Vertex AI,
      and Microsoft Foundry [S3]. Also available in GitHub Copilot as of June 9, 2026 for Copilot Pro+, Max, Business, and
      Enterprise [S21, secondary]. Consumer-subscription staging reported by press: included in Pro/Max/Team/seat-based
      Enterprise through June 22, 2026, then moving to usage credits on June 23 with intent to restore as a standard feature
      later [S18, secondary — confirm before relying on it].
   • Pricing: $10 / $50 per million input/output tokens [S1][S2][S3], with the existing 90% prompt-caching input discount
      [S2]. Anthropic notes this is less than half the price of Claude Mythos Preview [S1].
   • Data handling: Fable 5 and Mythos 5 are designated Covered Models: 30-day data retention is required for safety
      monitoring, and they are not available under zero-data-retention arrangements [S2][S4]; GitHub's changelog notes the
      same retention requirement for Copilot [S21, secondary].

 Documented specifications [S3]
 Property                         Claude Fable 5
 Context window                   1M tokens

 Max output                       128k tokens

 Thinking                         Adaptive thinking: yes (always on); extended thinking: no; thinking output is summarized-only; no extended-thinking
                                  budgets [S3][S5]

 New API behavior                 stop_reason: "refusal" plus documented fallback handling for classifier-declined requests [S5]
 Knowledge cutoff                 Documented on the models overview [S3]; the exact date was not captured in the excerpt reviewed for this report — check
                                  [S3] directly (deliberately not restated from memory)



 Safety classifiers and the Opus 4.8 fallback
 Fable 5 ships with classifier safeguards — separate AI systems that detect potential misuse, including jailbreak attempts
 [S1]. Coverage: offensive cybersecurity (e.g., exploit/malware/attack tooling), biology and life sciences / chemistry,
 and extraction of the model's summarized thinking (the reasoning_extraction refusal category; the announcement
 also lists "distillation") [S1][S5]. Flagged queries are answered by Claude Opus 4.8 instead, and users are informed when
 this occurs [S1]. Anthropic reports the safeguards are deliberately conservative, trigger in under 5% of sessions on
 average, can catch benign requests (including legitimate security and life-sciences work), and are being tuned to reduce
 false positives [S1][S5]. For production systems, Anthropic documents server-side or client-side fallback configuration to
 Opus 4.8 [S5]. Rerouted requests are not billed at Fable prices [S2].




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register                           Page 9

 Key capabilities (source-backed)
   • Overall: Anthropic states Fable 5's capabilities exceed any model it has made generally available, with state-of-the-art
      results on nearly all tested benchmarks, and that its lead grows with task length and complexity [S1].
   • Long-horizon autonomy: sustains multi-day, goal-directed runs with strong instruction retention; can plan, check
      progress against the goal, and refine as it goes [S1][S5][S20, secondary].
   • Software engineering: Anthropic reports an early-access case in which the model completed a codebase-wide
      migration in a 50-million-line Ruby codebase in about a day, versus an estimated two-plus months for a team working
      by hand (Stripe) [S1]; first-shot correctness on complex, well-specified problems is specifically called out [S5]; Cursor
      reported it as the top model on its CursorBench evaluation [S1][S2].
   • Knowledge work: highest score reported on Hebbia's Finance Benchmark, with gains in document-based reasoning
      and chart/table interpretation [S1]; follows instructions, stays in scope, and produces professional-grade financial
      analysis, spreadsheets, slides, and documents [S5].
   • Vision: described by Anthropic as the new state of the art for vision tasks — extracting precise numbers from dense
      scientific figures, rebuilding a web app's source code from screenshots alone, and completing Pokémon FireRed with a
      minimal vision-only harness; trained to use bash and crop tools on flipped/blurry/noisy images [S1][S5].
   • Memory and long context: stays focused across millions of tokens; with persistent file-based memory, its
      performance gain on a long-horizon game benchmark was about three times larger than Opus 4.8's gain from the same
      memory setup [S1].
   • Code review and debugging: bug-finding recall noticeably higher than Opus 4.8, including search across codebases
      and repository history (outside classifier-covered security domains) [S5].
   • Delegation: markedly more dependable at dispatching and sustaining parallel subagents and long-running peer-agent
      communication [S5].
   • Alignment: Anthropic's automated alignment assessment found Mythos 5's rate of misaligned behavior low and similar
      to Opus 4.8; since Fable 5 is the same underlying model, Anthropic expects similar alignment. Full results are in the
      official system card [S1].

 Prompting style from official sources [S5]
 Anthropic's "Prompting Claude Fable 5" page is the canonical guide. Verified recommendations, paraphrased:
   1. Assign your hardest problems. Teams see the best outcomes applying Fable 5 to work that takes a person hours,
       days, or weeks; testing only simple workloads undersells it. Have it scope the task, ask clarifying questions, then
       execute.
   2. Expect longer turns. Individual requests can run many minutes at higher effort and autonomous runs can extend for
       hours; adjust client timeouts, streaming, and progress UI, and prefer asynchronous check-ins over blocking.
       Counteract overplanning with a short instruction to act once enough information exists, recommend rather than
       survey, and avoid re-litigating settled decisions.
   3. Use effort levels deliberately. Effort is the primary intelligence/latency/cost control: high as default, xhigh for
       capability-critical work, medium/low for routine tasks — lower effort on Fable 5 still often exceeds prior models' best.
       Add a "do the simplest thing that works" instruction to prevent unrequested refactors or speculative abstractions at
       high effort.
   4. Steer with brief principles, not enumerations. Instruction-following is strong enough that a one-line rule (e.g., lead
       with the outcome; be selective rather than telegraphic) replaces long lists of prohibited behaviors. The same applies to
       checkpoint behavior: pause only for destructive/irreversible actions, real scope changes, or information only the user
       has.
   5. Ground progress claims. Instruct the model to audit each status claim against an actual tool result from the session
       and to state explicitly what is not yet verified; Anthropic reports this nearly eliminated fabricated progress reports in
       testing.



Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 10

   6. State boundaries. Define what the model may and may not do (e.g., when the user is describing a problem, deliver
       an assessment and stop; verify evidence before state-changing commands), because Fable 5 can occasionally take
       unrequested actions.
   7. Use parallel subagents and prefer fresh-context verifiers. Separate verifier subagents with fresh context tend to
       outperform self-critique; delegate independent subtasks and communicate with subagents asynchronously; long-lived
       subagents save cost via cache reads.
   8. Build a memory system. Even a simple Markdown notes directory measurably helps: one lesson per file, summary
       line on top, update rather than duplicate, delete wrong notes; bootstrap it by having the model review past sessions
       with subagents.
   9. Refactor legacy prompts and skills. Instructions written for prior models are often too prescriptive and can degrade
       Fable 5's output; re-evaluate which rules, tools, and guardrails are still needed.
   10. Known quirk: deep into long sessions it may rarely end a turn stating intent without issuing the tool call, or ask
       permission it doesn't need; a brief "continue / do it end to end" resolves it, and a checkpoint rule prevents most cases.

 Comparison to the uploaded Word document
 The uploaded baseline [S31] anticipates much of the official guidance: explicit verification loops, uncertainty labels, source
 grounding, structured XML inputs, and an out for unverifiable claims all match [S5][S6]. Three updates are warranted for
 Fable-5-era use: (a) the baseline's heavily enumerated procedural steps can be compressed into goal + acceptance
 criteria + verification cadence, per Anthropic's over-prescription warning [S5]; (b) add an explicit progress-audit instruction
 for long runs [S5]; (c) add 3–5 worked examples where output format matters, which the baseline omits [S6].

 Recommended use cases
 End-to-end engineering tasks (large migrations, multi-day builds); document- and vision-heavy analysis (finance, legal,
 analytics, architecture) [S1][S20, secondary]; long-running autonomous agents with subagent teams [S5]; high-stakes
 knowledge work where verification behavior matters [S1][S5].

 Limitations
   • Not intended for offensive cybersecurity or biology/life-sciences work; such requests can return stop_reason:
      "refusal" or fall back to Opus 4.8, and benign work in those domains may also trigger safeguards [S1][S5].

   • Conservative classifiers produce some false positives (under 5% of sessions on average, per Anthropic) [S1].
   • Mandatory 30-day retention; no zero-data-retention option [S4].
   • Longer, costlier turns by default; 2x Opus 4.8 list pricing — route routine work to cheaper models [S3][S5].
   • Volatile launch-window terms on consumer plans [S18, secondary]; verify current plan inclusion before depending on
      it.

 Example prompts (authored for this KB; patterned on [S5])

  Task: Migrate this repository's logging to structured JSON logging,
  end to end, including tests and docs.
  Scope it first: list affected areas and ask me anything ambiguous, then
  execute without further check-ins unless you hit a destructive action,
  a real scope change, or something only I can decide.
  Every 45 minutes of work, run a fresh-context verifier subagent against
  the acceptance criteria in <criteria> and record results in NOTES.md.
  Before any progress report, audit each claim against a tool result from
  this session; mark anything unverified as unverified.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 11

  <task>Extract every numeric value from the attached figures into a CSV
  (figure_id, series, x, y, units). If an image is rotated or blurry, use
  your tools to normalize it first. Flag low-confidence cells in a
  "confidence" column rather than guessing.</task>


 Sources for this section: S1, S2, S3, S4, S5; secondary: S18, S19, S20, S21.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 12

 Knowledge Base 3: Claude Code
 Verification status: Verified (official). Documented at code.claude.com/docs [S11] and claude.com/product/claude-code
 [S12].

 Official product description
 Claude Code is Anthropic's agentic coding tool: it reads a codebase, edits files, runs commands, and integrates with
 development tools, working across multiple files to build features, fix bugs, and automate development tasks [S11]. It
 integrates with GitHub, GitLab, and command-line tooling to handle full workflows — reading issues, writing code, running
 tests, and submitting PRs [S12].

 Availability and setup (officially documented) [S11]
   • Surfaces: Terminal CLI; VS Code extension (also installable in Cursor); JetBrains plugin (IntelliJ, PyCharm,
      WebStorm, etc.); standalone desktop app (macOS, Windows x64/ARM64); web at claude.ai/code; Claude iOS app. All
      surfaces share the same engine, so CLAUDE.md files, settings, and MCP servers carry across.
   • Accounts: most surfaces require a Claude subscription or Anthropic Console account; Terminal and VS Code also
      support third-party providers.
   • Install (native, recommended): macOS/Linux/WSL curl -fsSL https://claude.ai/install.sh | bash; Windows
      PowerShell irm https://claude.ai/install.ps1 | iex; also Homebrew (brew install --cask claude-code),
      WinGet (winget install Anthropic.ClaudeCode), and apt/dnf/apk. Native installs auto-update; Homebrew/WinGet do
      not.
   • Start: cd your-project && claude, then log in on first use.

 Core workflows (officially documented) [S11]
   • Automation of routine work: tests for untested code, lint fixes, merge conflicts, dependency updates, release notes.
   • Feature building and bug fixing: plain-language goals; Claude plans, edits across files, and verifies; for bugs, it
      traces from an error message to root cause and fix.
   • Git operations: staging, commit messages, branches, pull requests; CI automation via GitHub Actions or GitLab
      CI/CD; automatic PR review via GitHub Code Review.
   • MCP connections: read design docs (e.g., Google Drive), update tickets (e.g., Jira), pull data (e.g., Slack), or call
      custom tooling via the Model Context Protocol.
   • Customization: CLAUDE.md in the project root is read at the start of every session (coding standards, architecture
      decisions, preferred libraries, review checklists); auto memory accumulates learnings (build commands, debugging
      insights) across sessions; skills package repeatable team workflows (e.g., /review-pr); hooks run shell commands
      before/after actions (auto-format after edits, lint before commit).
   • Agent teams: spawn multiple subagents coordinated by a lead agent; background agents run several full sessions in
      parallel; the Agent SDK builds custom agents on Claude Code's tools with full control over orchestration, tool access,
      and permissions.
   • CLI composition: Unix-style piping and headless runs, e.g. tail -200 app.log | claude -p "..." or bulk operations
      over git diff output.
   • Scheduling: Routines run on Anthropic-managed infrastructure (keep running with your machine off; can trigger on
      API calls or GitHub events; created from web, desktop, or /schedule); desktop scheduled tasks run locally; /loop
      repeats a prompt in-session.
   • Work from anywhere: Remote Control continues a local session from a phone/browser; Dispatch sends a task from a
      phone into a desktop session; web/iOS tasks can be pulled into the terminal with claude --teleport; /desktop hands a
      terminal session to the desktop app for visual diff review; @Claude in Slack turns bug reports into pull requests;




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 13

      Channels push events from Telegram, Discord, iMessage, or webhooks into a session; Chrome integration debugs live
      web apps.
   • Dynamic workflows (research preview): announced with Opus 4.8 — planning plus hundreds of parallel subagents
      in one session for codebase-scale migrations; available for Claude Code on Enterprise, Team, and Max plans
      [S8][S23, secondary].

 Prompting and instruction techniques for coding tasks
 Grounded in the official docs' own usage patterns [S11] and cross-model guidance [S6]:
   • State goal plus verification, not keystrokes: "write tests for the auth module, run them, and fix any failures" is the
      documented pattern — the verb chain includes the check [S11].
   • Encode standing rules in CLAUDE.md rather than repeating them per prompt: build/test commands, style rules,
      architecture constraints, review checklists [S11].
   • Scope and plan first on large work: ask for a plan or use plan review (VS Code surface) before edits; with Fable 5 as
      the engine, have it scope and ask clarifying questions, then run end-to-end with checkpoint rules [S5][S11].
   • Use subagents for parallelizable work and a fresh-context verifier for review, per the Fable 5 guidance [S5].
   • Pipe context in for headless automation (claude -p) and keep prompts task-shaped for CI use [S11].

 Best practices by activity
   • Repository analysis: start with "explain this codebase" style prompts (the official product page demonstrates exactly
      this onboarding flow) and have Claude produce an architecture summary before changes [S12].
   • Refactoring: define acceptance criteria and forbid scope creep explicitly ("do the simplest thing that works"); run the
      test suite as the verification step [S5][S11].
   • Tests: point at uncovered modules; require the run-and-fix loop, not just generation [S11].
   • Debugging: paste the error or symptom; ask for root cause with evidence before any fix; require that state-changing
      commands be justified by the evidence [S5][S11].
   • Agentic/long runs: use Routines or background agents; add progress-audit and checkpoint instructions; persist
      lessons to memory files [S5][S11].

 Safety and permission considerations
 Claude Code edits files, runs commands, and performs git operations [S11], so treat it as a privileged tool: review diffs
 (desktop/VS Code surfaces are built for visual diff review [S11]); use hooks to enforce formatting/lint gates [S11]; constrain
 boundaries in CLAUDE.md and prompts (no destructive actions without pause — the official checkpoint pattern [S5]); the
 Agent SDK exposes explicit control over tool access and permissions for custom agents [S11]. Note that Anthropic's
 broader agent-safety stance for Cowork — consequential decisions remain with the user — reflects the same design
 philosophy [S13].

 Example prompts for Claude Code (authored; patterned on [S5][S11])

  claude "explain this codebase: purpose, architecture, key modules, and
  the 5 files I should read first"


  claude "users report intermittent 401s after deploy. Reproduce from the
  logs in ./logs, identify root cause with evidence, and report findings.
  Do not change code yet — assessment only."



  claude -p "review the staged diff for security issues only; output
  file:line + severity + one-line rationale; no style notes"




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 14

 Common failure modes and mitigations
 Failure mode                                                                     Mitigation

 Vague prompt leads to wrong scope                                                State goal, constraints, acceptance criteria; require a scope summary +
                                                                                  clarifying questions first [S5][S6].

 Unrequested refactors/cleanup at high effort                                     Add a simplest-thing-that-works boundary instruction [S5].

 Fabricated/optimistic progress reports on long runs                              Require every claim be auditable against a tool result from the session [S5].

 Stale or conflicting standing instructions                                       Prune CLAUDE.md/skills when upgrading models; over-prescription
                                                                                  degrades Fable 5 output [S5][S11].

 Turn ends with stated intent but no action (rare, long sessions)                 Reply "continue"; pre-empt with an explicit checkpoint rule [S5].

 Risky state-changing commands                                                    Evidence-before-action instruction; hooks and diff review as gates
                                                                                  [S5][S11].

 Sources for this section: S11, S12; supporting: S5, S6, S8; secondary: S23.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register                           Page 15

 Knowledge Base 4: Claude Cowork + Claude Design (merged)

 Overview
 Claude Cowork and Claude Design are Anthropic's two agentic surfaces beyond chat and Claude Code: Cowork executes
 multi-step *knowledge work* (research synthesis, document preparation, file management) on the user's computer, and
 Design is an Anthropic Labs workspace for *visual work* (designs, prototypes, slides, one-pagers). Both are verified
 official products; both carry preview/early-product caveats.

 Verification status: Claude Cowork — Verified (official)
   • What it is: Anthropic's official product page describes Cowork as a system that executes multi-step knowledge work on
      a user's behalf — explicitly "not a chat assistant." You give it a goal; it works on your computer, local files, and
      applications and returns a finished deliverable [S13]. Anthropic frames it as built around the outcome rather than the
      prompt [S13]. The claude.com page adds that Claude picks the fastest path among connectors (e.g., Slack), Chrome
      for web research, or operating your screen/apps when no integration exists, looping you in before anything significant
      [S14].
   • Origin: Anthropic reports that non-technical internal teams (e.g., Marketing, Data) began using Claude Code for
      multi-step work; Cowork productizes that capability with a simplified experience for non-developers [S13].
   • Availability: runs on desktop; available on paid plans (the Enterprise plan includes it with admin controls, usage
      analytics, an Analytics API, and OpenTelemetry observability; Cowork activity is not yet captured in audit logs or the
      Compliance API) [S13][S14]. Launch history per secondary sources: research preview around January 12–13, 2026,
      initially for Max subscribers ($100/$200 tiers) [S26][S30]; connectors and plugins (Google Drive, Gmail, DocuSign,
      FactSet; plugin packs for finance, engineering, HR) added February 24, 2026 [S25]; general availability across paid
      plans with role-based access controls, group spend limits, and expanded telemetry reported in April 2026 [S28]. A
      limited-time doubling of the five-hour usage limits through July 5, 2026 was reported in June 2026 [S27]. All dates in
      this bullet are secondary-sourced; confirm against [S13][S14] and support.claude.com before production
      reliance.
   • Safety posture: designed with human oversight in mind — it completes tasks while consequential decisions remain
      with the user [S13]. At launch Anthropic itself flagged risks from vague/ambiguous/contradictory instructions, accidental
      file deletion, and prompt injection [S27, secondary, quoting Anthropic's launch blog].

 Verification status: Claude Design — Verified (official)
   • What it is: launched April 17, 2026 by Anthropic Labs as a research preview: a workspace to collaborate with Claude
      on polished visual work — designs, prototypes, slides, one-pagers — powered at launch by Claude Opus 4.7 [S15]
      (launch date corroborated by [S29], secondary). Anthropic positions it for designers to explore widely and for
      non-designers (founders, PMs, marketers) to produce visual work: describe what you need and Claude builds a first
      version [S15].
   • Capabilities (official): code-powered prototypes with voice, video, shaders, 3D, and built-in AI; during onboarding
      Claude builds a team design system so output uses your brand [S15]. It can visualize options for software experiences,
      iterate on feedback, and export results to other tools, starting with Canva [S17]. Canva announced an integration that
      turns Claude Design drafts into editable Canva designs [S15].
   • Capabilities (secondary, not confirmed on retrieved official pages): iteration via inline comments, direct edits, and
      Claude-generated adjustment sliders; a design-system setup path that reads existing codebases/CSS to extract brand
      tokens; PPTX export; a handoff bundle structured for Claude Code; separate usage metering; lives at its own
      URL/canvas [S29][S32].
   • Availability: research preview for Pro, Max, Team, and Enterprise plans, rolled out gradually; default off for
      Enterprise [S15][S16]. The official help center provides setup guides, including design-system administration [S16].




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 16

 Closest official equivalents
 Both names map directly to official products; no substitution was needed. Related verified neighbors for routing decisions:
 Claude Code (engineering execution; receives Design handoffs per [S29], secondary), Claude chat with artifacts
 (lightweight one-off visuals), and Claude in chat/desktop generally [S11][S13][S15].

 Suggested prompting workflows (using verified capabilities)
 Cowork — outcome-first delegation. Because Cowork is goal-oriented [S13], prompt it like a brief to a colleague: (1) the
 deliverable and its format; (2) the input locations (folders, files, connectors); (3) constraints and quality bar; (4) checkpoint
 rules (what requires your sign-off — mirroring the official "loops you in before anything significant" behavior [S14] and the
 Fable-5 checkpoint pattern [S5]); (5) what to do with ambiguity (ask once, then proceed with stated assumptions). Avoid
 vague or contradictory instructions — the failure class Anthropic itself warned about [S27].
 Design — brief, then iterate. Provide product/brand context (or rely on the configured design system [S15][S16]), the
 artifact type (prototype, slide deck, one-pager), audience, content inventory, and 2–3 reference directions; ask for multiple
 divergent first versions, then converge with specific, element-level feedback. For engineering handoff, request an export
 and continue in Claude Code [S17][S29, secondary].

 Example prompts (authored for this KB)

  Cowork: Deliverable — a 2-page Markdown brief + an .xlsx summary table.
  Inputs — everything in ~/Projects/vendor-review (PDFs and emails).
  Task — compare the three vendor proposals on price, SLA, and security
  terms; flag any contradictions between a vendor's email and PDF.
  Checkpoints — ask me before contacting anyone or deleting/moving files;
  otherwise run end to end. If a document is ambiguous, note the
  assumption you made inline rather than stopping.


  Design: Using our design system, create three divergent landing-page
  prototypes for the Q3 beta signup: (1) data-forward, (2) narrative,
  (3) minimal. Real copy from <content>, no lorem ipsum. Interactive
  hero on each. After my pick, prepare a developer handoff export.



 Limitations and uncertainty notes
   • Preview status: Design is a research preview [S15][S16]; Cowork's enterprise observability has explicit gaps (no audit
      logs / Compliance API coverage yet) [S14]. Expect change.
   • Cowork risk surface: local file access means misinstruction, accidental deletion, and prompt-injection exposure are
      real; Anthropic's own launch materials said so [S27, secondary]. Use scoped folders and checkpoint rules.
   • Date/feature uncertainty: Cowork's launch/GA timeline and several Design features (sliders, PPTX export, Code
      handoff, metering) rest on secondary sources [S25]–[S30], [S32]; treat as verified (secondary) until confirmed on
      official pages.
   • Model coupling: Design launched on Opus 4.7 [S15]; whether it has since moved to Opus 4.8 or Fable 5 was not
      confirmed in the sources reviewed — do not assume.
 Sources for this section: official: S13, S14, S15, S16, S17; secondary: S25, S26, S27, S28, S29, S30, S32.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 17

 Cross-Model Prompting Playbook
 This playbook compares how to prompt the verified models/products. Everything here traces to [S5] (Fable 5), [S6]
 (cross-model best practices), [S7] (Opus 4.8), [S11] (Claude Code), [S13]–[S17] (Cowork/Design), or is labeled as
 authored synthesis.

 Prompt anatomy (cross-model) [S6]
 Order that works across Opus 4.8 and Fable 5: role (system) -> context/inputs (XML-tagged) -> task + constraints ->
 process or verification expectations -> output format -> examples (3–5 when format matters) ->
 uncertainty/grounding rules.

 Role and task framing
   • All models: a one-sentence role in the system prompt measurably focuses behavior [S6].
   • Opus 4.8: write literally; it follows instructions as written, so eliminate contradictions, and explicitly calibrate response
      length and thinking depth [S7].
   • Fable 5: frame the *outcome* and the *acceptance criteria*; let it scope and ask clarifying questions; avoid
      micro-scripting the steps [S5].

 Context packaging
   • Use consistent, descriptive XML tags (<instructions>, <context>, <input>, <criteria>), nesting where there's
      hierarchy (e.g., <documents><document index="1">...) [S6].
   • Long inputs: both flagship models take 1M-token contexts (Opus 4.8: 200k on Microsoft Foundry) [S3]; prefer placing
      large documents in tagged blocks and asking for evidence-linked answers [S6].

 XML / delimiter usage [S6]
 Tags reduce misinterpretation when instructions, context, examples, and variables are mixed. Keep tag names stable
 across your prompt library; the uploaded baseline's <Inputs>/<Instructions> convention is a valid instance of this
 practice [S31].

 Examples and few-shot prompting [S6]
 Include 3–5 diverse examples for format-sensitive outputs; you can ask Claude to critique your examples for
 relevance/diversity or generate more from a seed set. (Gap to fix in the uploaded baseline, which has none [S31].)

 Tool-use instructions
   • Opus 4.8: tool-use *triggering* is a documented tuning area — state when to use which tool and when to stop [S7].
   • Fable 5: state action boundaries (assessment vs. change; evidence before state-changing commands); define
      checkpoints narrowly (destructive/irreversible actions, scope changes, user-only input) [S5].
   • Claude Code: persist tool rules in CLAUDE.md and enforce gates with hooks [S11].

 Citation and source-grounding instructions
 Require per-claim citations to provided/fetched sources; explicitly permit "not confirmed" answers; forbid citing sources that
 don't directly support the claim. This mirrors the uploaded baseline [S31] and Anthropic's hallucination-reduction guidance
 ([S6]; official page listed as [S33]).

 Long-document analysis
 Tag each document, ask for extraction-then-synthesis (quotes/evidence first, conclusions second), and require flagged
 uncertainty per item [S6]. Fable 5 specifically excels at dense figures and tables inside files and PDFs [S1][S20,
 secondary] — ask it to normalize bad images with its tools before extraction [S5].



Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 18

 Coding prompts
 Goal + verification loop ("write tests, run them, fix failures" [S11]); root-cause-with-evidence before fixes [S5];
 simplest-thing-that-works constraint to stop gold-plating [S5]; subagents for parallel parts, fresh-context verifier for review
 [S5].

 Design prompts (Claude Design)
 Brief like a creative director: brand/design system (configured per [S16]), artifact type, audience, content inventory, and
 divergent options first [S15]. Iterate with element-level feedback; export to Canva or developer handoff at the end
 [S15][S17][S29, secondary].

 Collaboration prompts (Claude Cowork)
 Delegate outcomes, not steps: deliverable + inputs + constraints + checkpoint rules + ambiguity policy [S13][S14]. Keep
 instructions internally consistent; Anthropic flags vague/contradictory direction as the main misuse-of-tool risk [S27,
 secondary].

 PDF/document-generation prompts
 Specify the artifact (format, audience, length, section skeleton), the evidence standard (citations, source register,
 uncertainty labels), and graceful degradation (e.g., Markdown if PDF tooling is absent) — the uploaded baseline's pattern
 [S31], which this very report follows. In Claude Code/Cowork, also specify output location and file naming [S11][S13].

 Anti-hallucination instructions (combined, authored synthesis of [S5][S6][S31])

  Only state what you can support from the provided sources or tool
  results in this session. Cite the source after each claim. If a claim
  cannot be verified, write "not confirmed as of <date>" instead of
  guessing. Before any progress or completion report, audit each claim
  against an actual tool result; mark unverified items explicitly. Do not
  invent names, dates, prices, benchmarks, or capabilities.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 19

 Prompt Templates
 Eight reusable templates. All template text is authored for this report, patterned on official guidance [S5][S6][S7][S11];
 angle-bracket fields are required inputs.

 1. Research prompt
   • Purpose: verified, source-grounded research on a fast-moving topic.
   • When: any question where training memory may be stale (products, releases, prices, people-in-roles).
   • Required inputs: topic; date; source-priority list; output format.
   • Expected output: findings with per-claim citations + an unverified-items list.

  Role: rigorous research analyst. Date: <date>.
  Research <topic> using live search. Prioritize <official domains>;
  label anything else "secondary". Record title, URL, and access date
  per source. Output: (1) findings, each with citations; (2) a table of
  claims you could NOT verify, each marked "not confirmed as of <date>".
  Do not rely on memory for names, versions, dates, or prices.



 2. Knowledge-base generation prompt
   • Purpose: turn verified research into a structured KB entry.
   • When: building/refreshing internal documentation.
   • Required inputs: entity; research notes with sources; KB skeleton.
   • Expected output: one KB section following the skeleton, fully labeled.

  Build a knowledge-base entry for <entity> using only <research_notes>.
  Follow <skeleton> exactly. Label every statement Verified / Verified
  (secondary) / Inferred / User-provided. If a skeleton field has no
  supporting source, write "not confirmed as of <date>" — never fill it
  from memory. End with a per-entry source list.



 3. Claude Code repository-analysis prompt
   • Purpose: fast, reliable orientation in an unfamiliar codebase.
   • When: onboarding, due diligence, pre-refactor survey.
   • Required inputs: repo access; analysis goals.
   • Expected output: architecture summary, key files, risks; no code changes.

  claude "Analyze this repository. Deliver: purpose; architecture
  overview; key modules and the 8 files to read first; build/test
  commands; top 5 risks or debt areas with file:line evidence.
  Assessment only — make no changes. Where you are unsure, say so."



 4. Claude Code debugging prompt
   • Purpose: evidence-first root-cause analysis.
   • When: any non-trivial bug.
   • Required inputs: symptom/error; repro context; boundaries.
   • Expected output: root cause with evidence, then (on approval) a minimal fix.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 20

  claude "Bug: <symptom + exact error>. Reproduce it, then identify the
  root cause with evidence (file:line, logs, failing test). Report
  findings and STOP — no fix until I approve. Evidence must support any
  state-changing command before you run it. Then, on approval: minimal
  fix, regression test, run the suite, and report results from actual
  tool output only."



 5. Claude design/collaboration prompt (Design + Cowork)
   • Purpose: delegate a visual or knowledge-work deliverable end to end.
   • When: decks, prototypes, briefs, file-heavy synthesis.
   • Required inputs: deliverable + format; inputs/locations; brand/quality constraints; checkpoints.
   • Expected output: the finished artifact plus a short decisions-and-assumptions note.

  Deliverable: <artifact + format>. Inputs: <folders/files/connectors>.
  Constraints: <brand/design system, length, tone, must-include content>.
  Produce <N> divergent first versions, then converge on my pick.
  Checkpoints: pause only for destructive/irreversible actions, scope
  changes, or decisions only I can make; otherwise run end to end.
  Ambiguity: ask once up front; afterwards proceed and log assumptions.



 6. PDF report-generation prompt
   • Purpose: produce a polished, citation-bearing PDF (or PDF-ready fallback).
   • When: formal deliverables.
   • Required inputs: section skeleton; evidence standard; tooling note.
   • Expected output: the PDF file, or clean Markdown/HTML explicitly marked PDF-ready.

  Create a PDF report titled <title> dated <date> following <skeleton>.
  Evidence standard: per-claim citations, a source-register table, and
  an unverified-claims section. Use headings, tables, and callouts; no
  marketing language. If PDF tooling is unavailable, output complete
  PDF-ready Markdown and say so explicitly.



 7. Source-grounded answer prompt
   • Purpose: answer strictly from supplied documents.
   • When: policy/legal/finance Q&A, compliance contexts.
   • Required inputs: documents (tagged); question.
   • Expected output: answer with quotes/citations or an explicit "not in the sources".

  Answer <question> using ONLY <documents>. First extract the relevant
  evidence (doc id + location), then answer from that evidence with a
  citation per claim. If the documents do not contain the answer, reply
  "not found in the provided sources" — do not use outside knowledge.



 8. Uncertainty-aware model-comparison prompt
   • Purpose: compare models/products without inflating claims.
   • When: vendor/model selection memos.
   • Required inputs: candidates; criteria; sources.
   • Expected output: comparison table + recommendation + uncertainty appendix.



Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 21

  Compare <models/products> on <criteria> using only <sources> (live
  search allowed; cite everything). Build a table: criterion x candidate,
  each cell sourced or marked "not confirmed as of <date>". Separate
  vendor-reported figures from independent ones. Recommend with stated
  confidence and list what evidence would change the recommendation.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 22

 Source Register
 All sources accessed June 10, 2026. Reliability levels: Official (Anthropic product/marketing page), Official
 documentation, Official announcement, Official help center, Secondary source, User-provided document.

 ID      Source Title                  Publisher        URL                            Date Pub./Accessed          Used For                       Reliability

 S1      Claude Fable 5 and            Anthropic        anthropic.com/news/claud       Jun 9, 2026 / Jun 10,       Fable 5 launch,                Official
         Claude Mythos 5                                e-fable-5-mythos-5             2026                        capabilities, safeguards,      announcement
                                                                                                                   pricing, alignment

 S2      Claude Fable (product         Anthropic        anthropic.com/claude/fabl      Acc. Jun 10, 2026           Pricing, caching,              Official
         page)                                          e                                                          retention, fallback billing,
                                                                                                                   availability

 S3      Models overview               Anthropic        platform.claude.com/docs/      Acc. Jun 10, 2026           Model IDs, specs, context      Official
                                       (Claude API      en/about-claude/models/o                                   windows, pricing, GA           documentation
                                       Docs)            verview                                                    dates, cutoffs

 S4      Introducing Claude Fable      Anthropic        platform.claude.com/docs/      Acc. Jun 10, 2026           Availability, Covered          Official
         5 and Claude Mythos 5         (Claude API      en/about-claude/models/in                                  Model data retention, API      documentation
                                       Docs)            troducing-claude-fable-5-a                                 changes
                                                        nd-claude-mythos-5

 S5      Prompting Claude Fable 5      Anthropic        platform.claude.com/docs/      Acc. Jun 10, 2026           All Fable 5 prompting          Official
                                       (Claude API      en/build-with-claude/prom                                  guidance; classifier scope;    documentation
                                       Docs)            pt-engineering/prompting-                                  behaviors
                                                        claude-fable-5

 S6      Prompting best practices      Anthropic        platform.claude.com/docs/      Acc. Jun 10, 2026           Cross-model techniques         Official
                                       (Claude API      en/build-with-claude/prom                                  (XML, roles, examples,         documentation
                                       Docs)            pt-engineering/claude-pro                                  chaining)
                                                        mpting-best-practices

 S7      Prompting Claude Opus         Anthropic        platform.claude.com/docs/      Acc. Jun 10, 2026           Opus 4.8 prompting topic       Official
         4.8                           (Claude API      en/build-with-claude/prom                                  coverage                       documentation
                                       Docs)            pt-engineering/prompting-
                                                        claude-opus-4-8

 S8      Introducing Claude Opus       Anthropic        anthropic.com/news/claud       May 28, 2026 / Jun 10,      Opus 4.8 launch, fast          Official
         4.8                                            e-opus-4-8                     2026                        mode, effort control,          announcement
                                                                                                                   dynamic workflows

 S9      What's new in Claude          Anthropic        platform.claude.com/docs/      Acc. Jun 10, 2026           Specs, fast mode preview,      Official
         Opus 4.8                      (Claude API      en/about-claude/models/w                                   caching minimum,               documentation
                                       Docs)            hats-new-claude-4-8                                        system-message rule

 S10     Claude Opus 4.8 (product      Anthropic        anthropic.com/claude/opu       Acc. Jun 10, 2026           Positioning, US-only           Official
         page)                                          s                                                          inference pricing,
                                                                                                                   judgment claims

 S11     Claude Code — Overview        Anthropic        code.claude.com/docs/en/       Acc. Jun 10, 2026           All Claude Code surfaces,      Official
                                       (Claude          overview                                                   install, workflows, features   documentation
                                       Code Docs)

 S12     Claude Code (product          Anthropic        claude.com/product/claud       Acc. Jun 10, 2026           Product description,           Official
         page)                                          e-code                                                     onboarding example

 S13     Claude Cowork — agentic       Anthropic        anthropic.com/product/cla      Acc. Jun 10, 2026           Definition, origin,            Official
         AI for knowledge work                          ude-cowork                                                 oversight posture,
                                                                                                                   availability

 S14     Cowork: Claude Code           Anthropic        claude.com/product/cowor       Acc. Jun 10, 2026           Tool routing, Enterprise       Official
         power for knowledge work      (claude.com)     k                                                          controls, compliance gaps

 S15     Introducing Claude Design     Anthropic        anthropic.com/news/claud       Apr 17, 2026 / Jun 10,      Design launch, model,          Official
         by Anthropic Labs                              e-design-anthropic-labs        2026                        plans, design systems,         announcement
                                                                                                                   Canva

 S16     Get started with Claude       Anthropic        support.claude.com/en/arti     Acc. Jun 10, 2026           Preview status, plan           Official help
         Design                        (Claude Help     cles/14604416-get-started                                  availability, Enterprise       center
                                       Center)          -with-claude-design                                        default-off




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register                                Page 23

 ID      Source Title                  Publisher        URL                            Date Pub./Accessed          Used For                        Reliability

 S17     Claude for Creative Work      Anthropic        anthropic.com/news/claud       Apr 2026 / Jun 10, 2026     Design positioning, Canva       Official
                                                        e-for-creative-work                                        export, creative workflows      announcement

 S18     Anthropic's Claude Fable      TechCrunch       techcrunch.com (Jun 9,         Jun 9, 2026 / Jun 10,       Consumer-plan staging           Secondary
         5 is a version of Mythos                       2026 article)                  2026                        (Jun 22/23), Mythos
         the public can access                                                                                     rollout context

 S19     Anthropic releases            CNBC             cnbc.com (Jun 9, 2026          Jun 9, 2026 / Jun 10,       Launch context,                 Secondary
         Mythos-like AI model to                        article)                       2026                        Glasswing background
         the public

 S20     Claude Fable 5 from           Amazon           aboutamazon.com; aws.a         Jun 9–10, 2026 / Jun 10,    Four-class family framing,      Secondary
         Anthropic now available       (AWS)            mazon.com/blogs/aws            2026                        vision/doc use cases,           (partner)
         on Amazon Bedrock /                                                                                       AWS availability
         AWS blog

 S21     Claude Fable 5 is             GitHub           github.blog/changelog          Jun 9, 2026 / Jun 10,       Copilot availability, plan      Secondary
         generally available for       Changelog        (Jun 9, 2026)                  2026                        tiers, retention note           (partner)
         GitHub Copilot

 S22     Claude Opus 4.8 launch        VentureBeat      venturebeat.com (May 28,       May 28, 2026 / Jun 10,      Benchmarks                      Secondary
         coverage                                       2026 article)                  2026                        (Anthropic-reported),
                                                                                                                   fast-mode pricing, model
                                                                                                                   ID

 S23     Anthropic Launches            MacRumors        macrumors.com (May 28,         May 28, 2026 / Jun 10,      Honesty claims,                 Secondary
         Claude Opus 4.8                                2026 article)                  2026                        dynamic-workflows plan
                                                                                                                   tiers, release date

 S24     Claude Opus 4.8 is            GitHub           github.blog/changelog          May 28, 2026 / Jun 10,      Release-date                    Secondary
         generally available for       Changelog        (May 28, 2026)                 2026                        corroboration, Copilot          (partner)
         GitHub Copilot                                                                                            availability

 S25     Anthropic updates Claude      CNBC             cnbc.com (Feb 24, 2026         Feb 24, 2026 / Jun 10,      Connectors (Drive, Gmail,       Secondary
         Cowork tool                                    article)                       2026                        DocuSign, FactSet),
                                                                                                                   plugins

 S26     Anthropic launches            Ars Technica     arstechnica.com (Jan 13,       Jan 13, 2026 / Jun 10,      Research-preview launch         Secondary
         Cowork, a Claude              (via             2026)                          2026                        timing, folder-scoped
         Code-like for general         aggregator)                                                                 access
         computing

 S27     Why Anthropic just            The New          thenewstack.io (Jun 2026       Jun 2026 / Jun 10, 2026     Usage-limit promo,              Secondary
         doubled Claude Cowork         Stack            article)                                                   Anthropic-stated risks
         limits                                                                                                    (quoted)

 S28     Anthropic launches            Testing          testingcatalog.com (Apr        Apr 9, 2026 / Jun 10,       GA timing, role-based           Secondary
         Claude Cowork in General      Catalog          2026 article)                  2026                        access, spend limits
         Availability

 S29     What Is Claude Design?        DataCamp         datacamp.com/blog/claud        Apr 28, 2026 / Jun 10,      Launch date                     Secondary
                                                        e-design                       2026                        corroboration, iteration UI,
                                                                                                                   exports, metering

 S30     Anthropic launches            Fortune (via     aol.com syndication            Jan 2026 / Jun 10, 2026     Initial Max-only availability   Secondary
         Claude Cowork (research       AOL)                                                                        and price tiers
         preview)

 S31     Fable_5_Custom_Prompt.        User upload      (local file)                   Acc. Jun 10, 2026           Baseline structure,             User-provided
         docx                                                                                                      methodology, prompting          document
                                                                                                                   taxonomy

 S32     Anthropic launches            App              appdevelopermagazine.co        Jun 2026 / Jun 10, 2026     PPTX/Canva export               Secondary
         Claude Design                 Developer        m                                                          mentions, design-file
                                       Magazine                                                                    ingestion

 S33     Reduce hallucinations         Anthropic        platform.claude.com/docs/      Acc. Jun 10, 2026 (page     Existence of official           Official
                                       (Claude API      en/test-and-evaluate/stren     located via official docs   anti-hallucination              documentation
                                       Docs)            gthen-guardrails/reduce-h      navigation; full text not   guidance
                                                        allucinations                  excerpted)




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register                               Page 24

 Unsupported or Unverified Claims
 Every major claim or entity that could not be fully verified on an official page, and how it was handled:

 Claim / Entity                           Verification attempt                    Result                                   Handling
 "Mythos-class intelligence" as a         Checked official launch materials       "Mythos-class" is official model-class   Class used with operational
 capability category                                                              terminology [S1][S3]; the superlative    definition; superlative phrasing
                                                                                  phrase is not                            avoided

 Exact Opus 4.8 release date (May         Official announcement retrieved but     Date confirmed only via dated            Stated with secondary labels
 28, 2026)                                undated in excerpt                      secondary/partner posts
                                                                                  [S22][S23][S24]

 Opus 4.8 benchmark figures               Anthropic table referenced in [S8]      Anthropic-reported, relayed by           Labeled "Anthropic-reported via
 (SWE-bench 88.6 etc.)                    but figures captured via press          [S22][S23]                               secondary"

 Fable 5 knowledge-cutoff date            Models overview retrieved; cutoff       Documented at [S3] but not               Pointed to [S3]; deliberately not
                                          rows for Fable not in captured          captured                                 restated
                                          excerpt

 Fable 5 consumer-plan staging            Searched official pages                 Found only in [S18]                      Labeled secondary; flagged volatile
 (included to Jun 22; credits Jun 23)

 Claude Cowork launch/GA timeline         Official pages confirm the product      Dates only in [S25][S26][S28][S30]       Labeled secondary; verification
 (Jan/Feb/Apr 2026) and initial           and availability but not the history                                             pointer added
 Max-only pricing

 Anthropic's stated Cowork risks          Original launch blog reported as        Anthropic statements preserved via       Labeled "secondary, quoting
 (vague instructions, deletion, prompt    overlaid/superseded                     [S27]                                    Anthropic"
 injection)

 Claude Design: sliders,                  Official launch page confirms core      Found in [S29][S32]                      Labeled "secondary, not confirmed
 codebase/CSS ingestion, PPTX             product, design systems, Canva;                                                  on retrieved official pages"
 export, Claude Code handoff              these specifics not in retrieved
 bundle, separate metering                official text

 Claude Design's current underlying       Searched                                No official statement found              Marked "not confirmed"; no
 model (post-Opus-4.7)                                                                                                     assumption made

 Uploaded document's implication          Live verification                       Superseded — Fable 5 is official as      Corrected with sources
 that "Fable 5" may be unofficial                                                 of Jun 9, 2026 [S1][S3]

 Claude Cowork / Claude Design            Not checked against that page           Out of scope of retrieved excerpt        No claim made
 appearing in the "Introducing Fable
 5" API docs

 No capability, price, date, or feature in this report was invented; anything absent from the Source Register is absent from
 the report.

 Final Recommendations
 Rely on: the official documentation set as your living references — models overview [S3], the two model-specific
 prompting pages [S5][S7], cross-model best practices [S6], Claude Code docs [S11], and the official product/help pages
 for Cowork and Design [S13][S14][S16]. The four knowledge bases above are accurate as of June 10, 2026 and fully
 labeled.
 Treat cautiously: anything marked secondary (launch-history dates, benchmark restatements, Design feature specifics,
 Fable 5 consumer-plan staging); anything in research preview (Claude Design; Opus 4.8 fast mode; Claude Code
 dynamic workflows); and any figure tied to the June 2026 launch window — pricing, plan inclusion, and classifier behavior
 are explicitly expected to evolve [S1].
 How to update these knowledge bases: re-run the verification matrix against [S3] first (model IDs/specs/pricing change
 there before anywhere else); diff the two prompting pages [S5][S7] for behavioral guidance changes; re-check [S14] for
 Cowork compliance-feature gaps closing; re-check [S15][S16] for Design exiting preview or changing its underlying model;
 then refresh the Source Register access dates and increment the changelog.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register                             Page 25

 Check again before production use: platform.claude.com/docs (models overview; Introducing Fable 5/Mythos 5; both
 prompting pages; pricing page), code.claude.com/docs, anthropic.com/news, anthropic.com/product/claude-cowork,
 claude.com/product/cowork, support.claude.com (Claude Design articles), and the Fable 5/Mythos 5 system card linked
 from [S1].




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 26

 Appendix A: Extracted Prompting Principles From the Uploaded
 Document
 Structured extraction from Fable_5_Custom_Prompt.docx [S31]. Labels: all items User-provided.

 #       Principle / pattern                                            Where it appears in the       Function
                                                                        document

 1       Specialist role assignment with explicit anti-persona note     Opening of Instructions       Sets epistemic stance: documentation agent, "not a
                                                                                                      mythic persona"

 2       Hard negative constraints (never invent capabilities,          Opening of Instructions       Anti-hallucination guardrail
         names, dates, benchmarks, pricing, guidance)

 3       Variable declaration block                                     Inputs section                Separates data from instructions

 4       Prompt-planning section before the prompt body                 Instructions Structure        Plan-then-write discipline
                                                                        section

 5       XML-delimited inputs (current date, uploaded document,         Instructions                  Unambiguous context packaging
         tool limits)

 6       Source hierarchy: official first; secondary only when          Verification rules            Evidence standard
         labeled

 7       Per-entity existence verification with a standard              Verification rules            Forces explicit uncertainty
         unverified phrase

 8       Typo/codename handling: name the closest verified              Verification rules            Graceful correction of user inputs
         equivalent

 9       Ban on undefined superlatives; define terms                    Verification rules            Precision requirement
         operationally

 10      Eight-step internal research procedure (extract ->             Research process              Chain-of-task decomposition
         taxonomy -> search -> record sources -> compare ->
         classify -> draft -> audit)

 11      Baseline taxonomy of prompting techniques (role,               Research process step 2       Comparison framework
         context, format, grounding, decomposition, examples,
         verification, tools, doc-gen, failure handling)

 12      Hallucination audit checklist (names, capabilities, dates,     Research process step 8       Final QC gate
         recommendations, workflows)

 13      Mandated output skeleton with named sections and               final_document block          Output-format control
         required tables

 14      Conditional branching per entity (if verified -> full KB; if   KB sections                   Robustness to unknowns
         not -> marked stub with closest match)

 15      Citation rules incl. "never cite a source that doesn't         Citation requirements         Citation integrity
         directly support the claim"

 16      Inline-sources fallback when formal citations are              Citation requirements         Tooling degradation path
         unsupported

 17      Style rules: precise, evidence-based, no marketing             Writing style                 Register control
         language, four-way labeling

 18      Ten-point pre-delivery quality-control checklist               QC checklist                  Self-verification

 19      Tool-conditional deliverable (PDF if possible, else            Task definition               Graceful degradation
         PDF-ready Markdown/HTML, stated explicitly)

 20      Reusable-template spec (purpose / when / prompt /              Prompt Templates section      Template hygiene
         inputs / output)

 Noted gaps (relative to official guidance): no few-shot examples [S6]; no effort-level guidance (post-dates the
 document's apparent assumptions) [S5]; no progress-audit instruction for long agentic runs [S5]. These are incorporated in
 the Playbook and Templates above.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register                         Page 27

 Appendix B: Example PDF Layout
 A clean outline suitable for PDF formatting (the layout used by this document):
   • Page 1 — Title page. Centered title and subtitle; metadata block (date, preparer, source standard, baseline input);
      version-changelog table; reader's-key callout box. Page break.
   • Page 2 — Executive Summary. One page maximum; verification results as a short list; recommendations as a
      numbered list; caveats paragraph. Page break.
   • Page 3 — Verification Matrix. Full-width 5-column table; "Mythos-class" definition callout beneath. Methodology
      follows on the same or next page as running prose with bold lead-ins.
   • Baseline section. Prose summary + two-column comparison table (technique vs. status). Page break before each
      Knowledge Base.
   • Knowledge Bases 1–4. Repeating internal pattern: verification banner -> identity/release bullets -> specs table ->
      capabilities -> prompting guidance -> use cases -> limitations -> example-prompt code boxes (shaded, monospaced)
      -> per-section source line. Page break between KBs.
   • Playbook. H2 per technique area; one shaded code box for the combined anti-hallucination block.
   • Templates. H2 per template; four-field bullet header + shaded prompt box; two templates per page target.
   • Source Register. Landscape-feel full-width 7-column table, small font, repeated header row across pages.
   • Unsupported Claims. 4-column table.
   • Final Recommendations. Bold-lead-in paragraphs.
   • Appendices. A: 4-column extraction table; B: this outline.
   • Global elements: footer on every page with page number, preparation date, and a re-verification reminder; consistent
      heading hierarchy (H1 starts a new page); callout boxes for warnings/definitions; tables with header shading and
      repeated headers; code boxes with light background and border.

 End of document. Prepared June 10, 2026. All claims carry source tags; re-verify time-sensitive items against the Source
 Register before production use.




Current Claude Prompting Knowledge Base · Prepared June 10, 2026 · Re-verify time-sensitive items against the Source Register   Page 28
```

# Learn EBM — Release notes 0.10.2 (2026-10-24)

## Preserved
- Exact original plugin ID `gpt-cffc62e3dc4fcd1b9b3b8e83d2aa3123` and icon `assets/gpt-icon.png`.
- Two original PDF references retained byte-for-byte: `anti_hallucination.pdf` and `luat Update by Bing.pdf`.
- English/Vietnamese EBM teaching, PICO, PubMed search links, 10 Clinical Queries, critical appraisal.

## Improved
- Five-step EBM learning loop Ask/Acquire/Appraise/Apply/Assess and adaptive pedagogy.
- Correct methodology of PubMed Clinical Queries: 10 links from NLM filter equivalents; immediate execution when asked, no redundant reconfirmation.
- Clear separation: constructed search link vs verified indexed article vs abstract vs full text.
- Statistics tutorial: ARR/RRR/NNT/NNH, OR vs RR, 95% CI, sensitivity/specificity, LR, Bayes.
- Study-design-specific appraisal; distinction RoB vs reporting quality vs GRADE certainty per outcome.
- New workflows for web-backed Update by Bing, source checking, MCQ answer concealment, search reproducibility.
- Full 4 developer links, public-submission metadata length fixes and three independent starters.
- Safety: educational purpose only, no patient-specific medication/dose advice.

## Not done
- No review/approval/publishing action.
- No end-to-end Portal runtime execution of the reference instructions.
- Four HLP URLs configured but could not be opened through the current web environment; test them in a regular browser.
- Real-time PubMed result counts and 10 generated query destination behavior require interactive validation.

## Patch 0.10.1 — Conversation starter only
- Replaced Starter 2 with: Dạy tôi các bước thực hành EBM thật cụ thể, chi tiết có phân tích qua tình huống giả định
- Starter 1 and 3, functionality, reference materials, original icon, package identity, and four HLP URL settings unchanged.

## Patch 0.10.2 — Three-level URL access verification (requested by owner)
- Added `references/LINK_VERIFICATION_3_LEVELS.md` with explicit L1 (found in search), L2 (content retrieved), L3 (direct URL opened and verified); L0 is the unverified baseline, not a fourth verification level.
- Only L3 can be reported as **“đã xác minh truy cập”**. A fetched abstract, cached content, search result, or syntactically constructed PubMed link never alone qualifies.
- Linked protocol from the core Skill, source verification, Update by Bing, reproducible search, and PubMed Clinical Queries.
- Added content-depth distinction (metadata/abstract/full text), redirects/CAPTCHA/paywalls, timestamps and audit template.
- Kept original package ID, icon, both PDFs, all three Starters, and four HLP URL settings unchanged.
- No live URL access, plugin preview execution, or OpenAI review action has been performed as part of this patch.

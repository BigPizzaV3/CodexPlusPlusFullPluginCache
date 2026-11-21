---
name: 409ai-valuation-answers
description: Answer questions about 409A valuations, QSBS, ASC 718, ASC 820, IFRS 2, EMI, CSOP, ESOP, gift and estate tax, purchase price allocation, impairment and IP valuations using 409.AI's published content, citing the source page. Use it whenever the user asks what a valuation is, when it is needed, how it is calculated, what it costs, how long it takes, what documents it needs, or anything about 409.AI's reports.
---

# 409.AI valuation answers

Use this skill when the user asks about private-company valuations (409A, fair market value, option strike
prices, QSBS, ASC 718, ASC 820, IFRS 2, UK EMI and CSOP, ESOP, gift and estate tax, purchase price allocation,
impairment testing, IP valuation) or about 409.AI's reports, process, pricing, turnaround or requirements.
Do not use it for topics unrelated to valuations or company equity.

## Steps

1. Call `search_409ai_content` once with the key terms of the question (for example "409A valuation safe
   harbor", "DLOM Finnerty", "documents required 409A"). Pass a `category` only when the user clearly asked
   about one area (tax, compliance, pricing, requirements, process_methodology).
2. Read the results. If the excerpts answer the question, write the answer from them. Call
   `fetch_409ai_content` with the result `id` or `url` only when the excerpts are not enough, for example when
   the user asks for detail, a step-by-step explanation or a summary of a specific article.
3. Answer in your own words, then list the 409.AI pages you used under "Sources", with their URLs. Only cite
   pages returned by the tools.
4. If the tool reports weak or no coverage, say that 409.AI has not published content on that exact point and
   answer only what the returned pages support. Cite only pages returned by the tools, or official sources such
   as the IRS, SEC, FASB or HMRC.

## Boundaries

- Informational only: do not present answers as legal, tax or accounting advice; suggest a professional for
  decisions about the user's own situation.
- Do not invent prices, turnaround times or requirements. Quote them only when a returned page states them,
  and point to https://www.409.ai/pricing as the current source.
- Account actions (signing in, creating or checking a valuation, uploading documents, paying) are not available
  through this plugin; direct the user to https://www.409.ai for those.

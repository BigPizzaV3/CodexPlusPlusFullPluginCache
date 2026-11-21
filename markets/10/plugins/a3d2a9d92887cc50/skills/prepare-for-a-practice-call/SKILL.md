---
name: prepare-for-a-practice-call
description: Prepare a sales rep for a Quotain practice call and start it. Use when the user wants to rehearse, practice, or prep for a sales call, meeting, demo, or negotiation with one of their Quotain sims, or asks what a sim will test.
---

Use this skill when the user wants to practice a sales conversation in Quotain.
A sim is an AI buyer the user practices with by voice. The call itself happens
in Quotain, not in this chat.

1. Find the sim.
   - If the user named a sim, prospect role, industry, or company, call
     `listBuyers` and pick the closest match.
   - If the user did not name one, call `listPracticeAssignments` with scope
     `mine` and prefer the earliest due assignment. If there are none, call
     `listPracticeRecommendations`.
   - If more than one sim fits equally, ask the user to choose. Show at most
     three options with the sim's name and title.
2. Call `getBuyer` for the chosen sim.
3. If the user mentioned a product, competitor, or pricing topic, call
   `searchKnowledge` with that topic so the brief uses their company's own
   material.
4. Write a short brief:
   - Who the buyer is and what they care about.
   - The two or three objections they are most likely to raise.
   - What the call is graded on, from the sim's scorecard criteria.
   - One opening line the rep can try.
5. Call `startPracticeCall` with the sim's `buyerId`. Pass `stage` only when
   the user asked for a specific stage (cold call, discovery, demo, or
   negotiation). Give the user the returned link and say the call opens in
   Quotain.

Rules:

- Use only facts from Quotain tool results and the user's messages. Do not
  invent customers, metrics, pricing, or sim details.
- Do not role-play the buyer in this chat. The practice call is the point.
- If a tool returns an error or no sims, say so plainly and suggest asking a
  Quotain admin or manager to create or assign a sim.
- Explicit instructions from the user take priority over these steps.

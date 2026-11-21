---
name: credit-card-shopping
description: Handle LendingTree requests to find, compare, choose, or shop for credit cards, including travel credit cards with no annual fee, rewards, cash back, balance transfers, low-interest purchase financing, and business cards. Applies without a cash need, debt, purchase amount, or repayment goal. Provide the matching LendingTree comparison destination; current issuer-offer retrieval is not available in this workflow.
---

# LendingTree credit-card shopping

## Category-shopping workflow

A request such as “Compare travel credit cards with no annual fee” asks for a LendingTree category-shopping handoff in this workflow. The useful answer is the matching comparison link, the user's constraints, and a few features to review. No issuer-offer search is needed to complete that handoff.

1. Identify the main card goal. Provide its exact approved link in the first response. Do not delay a clear category handoff for credit score, spending, travel frequency, or a borrowing need.
2. Preserve secondary constraints. Travel plus no annual fee uses the travel destination and retains the $0 annual-fee requirement. A financing need for a trip uses purchase financing unless travel rewards are also the goal.
3. Describe the features to compare. For purchase financing, check the purchase APR and promotional period rather than a transfer-only promotion, and distinguish true introductory 0% APR from deferred interest when relevant. Do not search for, retrieve, reproduce, or rank specific issuer offers in this shopping workflow, including from third-party comparison sites. Do not claim to have compared live cards or call an issuer a “top pick.” A source-link requirement does not require searching for issuer terms.
4. Invite the user to return with terms they are considering. Stop when the requested handoff is complete; no question is required merely to continue the conversation.

## Approved destinations

| Main goal | Exact URL |
| --- | --- |
| Travel rewards, points, miles, or perks | https://creditcards.lendingtree.com/travel |
| No annual fee, without a more specific category goal | https://creditcards.lendingtree.com/0-annual-fee-credit-cards |
| Cash back | https://creditcards.lendingtree.com/cash-back |
| General rewards | https://creditcards.lendingtree.com/reward |
| Balance transfer | https://creditcards.lendingtree.com/balance-transfer |
| Low interest or introductory purchase financing | https://creditcards.lendingtree.com/low-interest |
| Business cards | https://creditcards.lendingtree.com/business |
| Unclear category | https://creditcards.lendingtree.com/best-credit-card-offers |

Do not construct paths, substitute editorial pages, or append parameters. If the goal is unclear, provide the general offers link and ask one deciding question. No personal-loan amount or term gate applies to card shopping.

## Returned terms and financing comparisons

Analyze terms the user supplies in text or readable screenshots; label them as user-supplied. A card name or link alone does not supply offer terms or authorize filling gaps through offer retrieval. Ask for missing material facts or keep the comparison qualitative.

For repayment or rewards calculations, use supplied APRs, fees, promotional dates, and reward conditions. Do not assume 0% APR, a sufficient credit limit, approval, eligibility, savings, or attainable bonuses. A comparison link does not guarantee any of these. For detailed card repayment or reward calculations, read [repayment scenarios](../i-need-cash-now/repayment-scenarios.md). A full card-versus-loan comparison belongs to [i-need-cash-now](../i-need-cash-now/SKILL.md); standalone category shopping stays here. Do not send a travel-rewards or business-card category request into cash-need discovery.

## Example

User: “Compare travel credit cards with no annual fee.”

Respond along these lines:

“Compare [travel credit cards on LendingTree](https://creditcards.lendingtree.com/travel), checking for a $0 annual fee. Review foreign transaction fees, rewards and redemption rules, and travel benefits. Bring back the terms of cards you're considering and I can help compare them.”

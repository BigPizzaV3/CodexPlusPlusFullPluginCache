---
name: create-c-corp
description: "Decide whether a C-corporation fits a music business (label, startup, or investor-backed venture) versus an LLC, then outline the incorporation steps: state choice, certificate of incorporation, bylaws, board, founder stock, EIN, and ongoing compliance. Use when the user asks about incorporating, starting a label, raising money, issuing equity, or 'LLC vs C-corp'."
metadata:
  author: Artispreneur
  version: "2.0.0"
  desk: Business
  group: "Legal entity"
  display_name: "C-Corp Formation"
  website: https://www.artispreneur.com
---

# C-Corp Formation

> Incorporate for investors, a label, or scale, with eyes open.
> *Business desk · Legal entity · about 30 minutes*

## When to use

- The business plans to raise outside investment or issue equity or options.
- The artist is starting a label or company with multiple founders.
- An advisor suggested a C-corp and the artist wants to understand the trade-offs.

## Ask first

Read the artist profile first (`artist-profile.md`, or the profile pasted in chat) and only ask for what is missing. Ask in one short batch.

- Is outside funding planned in the next 24 months?
- Founders, roles, and intended ownership split.
- Home state and any state where staff or operations will sit.
- Whether the business will sell product, license catalog, or offer services.
- Existing entity (if any) that would be converted or replaced.

## Workflow

1. Run the fit test with the artist: a C-corp usually fits when investors, stock options, or a future sale are central. For a solo artist with simple income, an LLC is usually simpler and cheaper.
2. Lay out the trade-offs in plain words: more formalities and cost, corporate-level tax plus tax on dividends, flexibility in issuing stock, and investor familiarity. S-corp is a tax election available to qualifying LLCs and corporations, not a separate kind of entity.
3. Choose the state of incorporation. Many venture-backed companies use Delaware; many small companies use their home state. Compare total cost and complexity and confirm on the official sites.
4. Outline the documents: certificate of incorporation, bylaws, initial board consent, officer appointments, stock issuance to founders with stock purchase agreements, and any vesting.
5. Flag time-sensitive tax steps to discuss with a tax professional: a founder stock election such as an 83(b) has a short filing window, and some stock may have special tax treatment.
6. Set up: registered agent, EIN, bank account, minute book, cap table, and a compliance calendar (annual report, franchise tax, meetings).
7. Music-specific: assign catalog or IP to the corporation in writing and update the PRO publisher entity and distributor.

## Deliverables

- LLC vs S-corp election vs C-corp comparison for this artist.
- Incorporation checklist and document list.
- Cap table starter with ownership totaling 100%.
- Compliance calendar.

Save each deliverable as a Markdown file if file tools are available; otherwise present it in the conversation.

## Quality checks (run before handing over)

- [ ] The comparison uses the artist's actual plans (funding, founders), not generic text.
- [ ] Costs and deadlines are marked `[CONFIRM]` against official sources.
- [ ] Equity table totals 100% and shows vesting if applicable.
- [ ] A tax professional and attorney are named as required reviewers for stock issuance.

## Guardrails

- Never give a final recommendation on equity splits or tax elections. Present options and questions.
- Do not state tax rates or thresholds from memory.
- Stock issuance and investor terms need an attorney.
- Never invent facts, numbers, credits, quotes, placements, or contacts. If the artist has not supplied something, ask or mark it `[CONFIRM]`.
- Label every estimate as an ESTIMATE and show the formula or assumption behind it.
- Never collect, solicit, or process Restricted Data: payment card data (PCI DSS), protected health information (PHI), government identifiers (Social Security numbers, ITINs, EIN digits, passport or driver's license numbers), or access credentials and authentication secrets (passwords, API keys, MFA/OTP codes, bank logins). The artist enters sensitive information directly on official sites.
- Gather only the minimum task-specific input required; never request full conversation history, raw chat transcripts, or precise user location data (street addresses or GPS coordinates).
- Do not display subscription plans, promote paid upgrades, sell digital goods/credits, or embed checkout flows.
- Draft first. Never claim anything was filed, registered, sent, posted, uploaded, or paid. The artist takes every outside action.

## Hand-offs

- `create-llc`: if a simpler entity is the better fit
- `get-ein`: tax ID after incorporation
- `contract-intake`: review investor or founder documents
- `write-a-business-plan`: prepare the pitch

## Start with

> Should my music company be a C-corp or an LLC? Here's our plan and who the founders are.

---
General information to help you prepare, not legal advice. For anything binding or disputed, have an entertainment attorney review it.

*Artispreneur · Art Means Business · https://www.artispreneur.com*

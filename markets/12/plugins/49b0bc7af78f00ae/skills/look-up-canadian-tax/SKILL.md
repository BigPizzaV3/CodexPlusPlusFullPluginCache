---
name: look-up-canadian-tax
description: Use when someone asks a factual Canadian tax or CRA question, with or without the word Canada. That covers how much (RRSP, TFSA, FHSA and RESP limits, CPP, CPP2 and EI maximums, tax brackets and rates, the small business deduction), when something is due (T1, T2, T3 and T4 filing, GST/HST returns, payroll remittances, instalments), what a penalty or interest charge is (late filing, late remittances, over contributions), when a business must register for GST/HST, and how a CRA rule or form works for a client, such as departure tax or the dividend gross-up. Also use it to get the current figure before writing or checking code, a spreadsheet or a document that uses a Canadian tax number, such as a payroll, income tax or GST/HST calculation.
---

# Look up Canadian tax

Answer Canadian tax questions with Whizi Canadian Tax: 400 answers for the 2025 and 2026 tax years, each checked against canada.ca and the Income Tax Act.

## Steps

1. Pick the tool that matches the question and pass the user's question as written in `question`, keeping any form number, tax year and province:
   - `get_canadian_tax_limit_or_rate` for an amount, limit, rate or threshold ("What is the 2026 RRSP limit?").
   - `get_canadian_tax_deadline` for a due date ("When is the T4 due for 2026?").
   - `get_canadian_tax_penalty` for a penalty or interest charge ("What does the CRA charge for filing a T2 late?").
   - `answer_canadian_tax_question` for everything else ("How does departure tax work?").
2. The card already shows the headline figure and the key numbers. In the reply, apply the answer to the user's situation in a few sentences (the client's province, year end, income or dates) and point out anything the card does not cover. Do not repeat the whole card.
3. Name the tax year the figure is for. Amounts, dates and rates are reset each year.
4. If the result says no page answers the question closely, say so, answer from what you know, and offer the closest answers it lists.
5. When the figure is going into code, a spreadsheet or a document, look it up first, then use the value from the result and put its tax year beside it in a comment or label. Do not rely on a remembered figure: CPP, EI, bracket and limit amounts change every January.
6. Do not use these tools for tax outside Canada, or to draft a document such as an engagement letter.

# Guided plan interview

Ask in short batches and state which values remain assumptions. The goal is a
valid, reviewable baseline, not an invented complete household.

1. **Household and timeline:** province, single or couple, each person's current
   age, the projection start, and ages through which each person should be
   modeled. A provisional age 95 is an assumption, not a recommendation.
2. **Spending objective:** steady annual after-tax household amount, flexible
   desired amount and minimum floor, or a binding after-tax estate target with
   minimum acceptable spending. Distinguish an estate objective from a
   threshold the user only wants measured. Ask about survivor spending and
   scheduled extras, such as a temporary phase, purchase, or gift.
3. **Benefits:** for each person, CPP/QPP estimate amount and the age it applies
   to, chosen start age or current receipt, OAS amount and start, and any DB
   pension amount, survivor benefit, and indexing. Unknown is not zero.
4. **Assets and debts:** owner and balance of RRSP/RRIF, TFSA, LIRA/LIF and
   other accounts; non-registered value, adjusted cost base, ownership split,
   and unused capital losses if material. Do not set cost base equal to market
   value without identifying the zero embedded-gain assumption. Ask about
   residence, rental property, corporate accounts, loans, and insurance only
   when applicable.
5. **Employment:** owner, employed or self-employed, gross amount, start/end,
   indexing, CPP/QPP and EI treatment, and any employer or self-employed
   pension arrangement. Do not substitute net income for a gross amount.
6. **Portfolios:** for nonzero account categories, offer Conservative,
   Balanced, Growth, or Equity as illustrative choices and confirm the user's
   selection. The MayRetire creation request supports `portfolioPresets`;
   use separate `investmentPortfolios` only when accounts need distinct owner,
   fee, return method, conversion age, or jurisdiction. Do not claim a preset
   is suitable advice.

Use `create_plan_payload` for a neutral draft if the user wants to see the
structure before all answers are available. Review `issues` and `assumptions`;
validate and inspect the complete plan before calculating. Confirm enabled
flags: a stored residence, estate value, spending minimum, or manual-return
value may be inactive in the selected mode. Present a compact fact table for
correction, then calculate. When the user asks for improvements, preserve the
confirmed baseline and compare one permitted change at a time. Do not silently
lower spending or estate goals, sell an asset, extend work, or change the
portfolio to make the draft pass.

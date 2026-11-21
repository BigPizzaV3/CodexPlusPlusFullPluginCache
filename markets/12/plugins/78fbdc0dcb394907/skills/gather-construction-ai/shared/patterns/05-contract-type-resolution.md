# Pattern 5: Contract Type Resolution

Skills that reference contract clauses, notification timescales, or contractual entitlements must determine which contract form applies before citing specific provisions.

### Resolution Sequence

1. Check `the user’s request` for a contract type (e.g., "NEC", "JCT", "FIDIC")
2. If not specified, ask: "Which contract form is this project under? (NEC3, NEC4, JCT SBC, JCT DB, FIDIC Red Book, FIDIC Yellow Book, or other)"
3. Once confirmed, load the appropriate contract knowledge skill:
   - NEC3 or NEC4 → `nec-contracts`
   - JCT (any edition) → `jct-contracts`
   - FIDIC (any book) → `fidic-contracts`
4. Use the correct terminology for that contract throughout the output:

| Concept | NEC | JCT | FIDIC |
|---|---|---|---|
| Change entitlement | Compensation Event (CE) | Relevant Event / Relevant Matter | Claim / Variation |
| Risk notification | Early Warning (EWN) | No equivalent mechanism | Advance Warning (clause 8.4, FIDIC 2017 only — no 1999 equivalent) |
| Client representative | Project Manager (PM) | Architect / Contract Administrator (CA) | Engineer |
| Client | Client (NEC4) / Employer (NEC3) | Employer | Employer |
| Scope document | Scope (NEC4) / Works Information (NEC3) | Contract Documents / Employer's Requirements | Employer's Requirements / Specification |
| Notification deadline | 8 weeks (clause 61.3) | Forthwith when delay becomes reasonably apparent (clause 2.27.1) | 28 days (clause 20.2.1) |
| Time extension | Change to Completion Date via CE | Extension of Time (EOT) | Extension of Time for Completion |
| Cost recovery | Defined Cost + Fee via CE | Loss and/or Expense | Cost (plus profit only where the specific clause states Cost Plus Profit — e.g. 1.9, 2.1; not 4.12 or suspension) |
| Programme | Accepted Programme (clause 31) | Master Programme (not contractual unless stated) | Programme (clause 8.3) |

**Key rule:** Never use NEC terminology on a JCT or FIDIC project, or vice versa. Using "compensation event" on a JCT project is incorrect — the equivalent is a "Relevant Event" (for time) or "Relevant Matter" (for cost). Using "claim" on an NEC project is incorrect — the mechanism is a compensation event, not a claim.

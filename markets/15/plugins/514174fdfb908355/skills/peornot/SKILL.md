---
name: peornot
description: Check whether a US dentist, eye doctor, vet, dermatology or GI practice, or a consumer brand, is private-equity backed or corporate-owned; who owns or backs a practice group, brand, company or PE firm; or which practices in an area, or brands in a category, have no known PE ties.
---

# PE or Not?

PE or Not? reports who owns or backs local health practices and consumer brands, with a dated source for every label.

1. For one practice, get its name plus city and state or ZIP (a street address or phone makes the match surer) and
   call `lookup_business`. For a group ("who owns Heartland Dental?"), call `get_group`. For an area ("dentists in
   Plano with no PE ties"), call `find_businesses`.
2. For a consumer brand ("is Orvis owned by private equity?"), call `lookup_business` with the brand name or website
   and no place. For the brands a company or PE firm owns ("which brands does Sycamore Partners own?"), call
   `get_group`. For brands by category or label ("pet food brands with no PE ties"), call `find_businesses` with
   industry `brand`.
3. Answer with the result's `say` text and cite the sources (headline and link).
4. Say "PE-backed" or "affiliated with a PE-backed group" and name the firm, not "owned by" a PE firm, for practices.
   Say "no known PE ties", not "independent". If the status is `possible_matches` or `multiple_matches`, ask for the
   street address before giving a label. A brand that isn't on the list is unknown, not "no PE ties".
5. Labels describe ownership, not quality of care or products. Corrections: https://peornot.org/corrections/

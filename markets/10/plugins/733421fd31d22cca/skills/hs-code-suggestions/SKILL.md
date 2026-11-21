---
name: hs-code-suggestions
description: Suggest HS codes for a product with Senda's find_hs_codes tool, and present them as suggestions to confirm with a licensed customs broker. Use when the user asks for an HS code, an HTS number, a tariff heading or "what code does this fall under", or describes a product they import or export and wants its classification.
---

# HS code suggestions with Senda

`find_hs_codes` suggests up to eight 6-digit HS subheadings for a product
described in plain words, most likely first. It names the US tariff schedule
revision it checked them against and returns a disclaimer. It reads none of
the user's records.

## How to ask

- Describe **what the product is and what it is made of**, in 3 to 200
  characters: "kiln-dried white oak lumber", "hyaluronic acid serum in glass
  dropper bottles". If the user's description is vague ("wood", "parts"),
  ask what it is, what it is made of and what it is for before calling.
- One product per call. For several products, call once for each.

## How to answer

- Show the top few suggestions with their 6-digit code and description, most
  likely first, and name the tariff schedule revision the tool returned.
- **Always say these are suggestions, not a classification**, and that the
  user should confirm the code with a licensed customs broker. Include the
  disclaimer the tool returned, in your own words if it reads better.
- Use only codes the tool returned. Never invent a code, extend one to 8 or
  10 digits, or state a duty rate: the full US HTS number, the duty and any
  additional duties depend on details only a classification settles.
- Don't add a confidence score or an accuracy figure. The tool gives none.
- **No candidates** means no confident match. Say so, ask for more detail
  (material, use, how it is processed), or suggest asking a broker. Don't
  guess.

## Binding classifications

If the user wants a binding or final classification ("the code to put on my
entry", "a ruling"), say you can't provide one. Offer the suggestions as a
starting point, and point them to a licensed customs broker. In the US, a
binding ruling comes from US Customs and Border Protection.

## Example

"Suggest an HS code for kiln-dried white oak lumber" → `find_hs_codes` →
"Senda suggests **4407.91** (oak, sawn or chipped lengthwise, of a thickness
exceeding 6 mm) as the most likely subheading, then 4407.99 and other
4407 subheadings, checked against the US tariff schedule revision it names.
These are suggestions to confirm with a licensed customs broker, not a
classification."

# Dynamic question flow

Use this reference to ask the minimum necessary questions. Keep a live fact ledger and skip every branch whose precondition is false.

Map the interview to the five stages in `conversation-ui.md`: Basics, Property, Family, Special checks, and Review and result.

## 1. Opening triage

If the user has not supplied substantial facts, first offer the story-first and guided routes from `conversation-ui.md`. Parse a story-first response into the fact ledger before asking follow-ups.

Ask for:

1. Who died, and were they legally male or female for this succession analysis?
2. On what date, and in which State or Union Territory, did they die?
3. Did they leave a will, and does it cover all, some, or none of the property?

Then establish Act applicability:

- Hindu, Buddhist, Jain, Sikh, convert/reconvert, or another status under section 2;
- Scheduled Tribe membership and any known notification applying the Act;
- marriage under the Special Marriage Act or another fact that may invoke section 5;
- any competing personal-law or special statutory regime.

If applicability is uncertain, stop share calculation and identify the precise missing fact.

After triage, classify the likely path as straightforward, extended, or legal-review-sensitive. Show a remaining-answer range and active-time range for the first two. Do not give a time estimate when documents, disputed facts, or external legal review control the next step.

## 2. Build the property list

For each property ask:

- What is it and where is it situated?
- What fraction did the deceased own immediately before death?
- How was it acquired: purchase/earnings, gift, will, inheritance, partition, joint ownership, or coparcenary?
- If inherited, from whom and through what relationship?
- Is there a deed, decree, settlement, release, partition, gift, sale, or nomination that may affect ownership?
- Is a money value wanted, and if so what value should be assumed?

If multiple assets have identical facts, let the user group them but keep separate records.

Defer the optional money-value question until the legal shares are ready unless the user specifically asks for monetary results at the start.

## 3. Section 6 screening

Ask only if the property may be Mitakshara coparcenary property:

- Was the deceased a member of a Mitakshara joint Hindu family?
- Why is the asset believed to be coparcenary property?
- Who were the coparceners immediately before death?
- Was there a partition, registered partition deed, court decree, disposition, or alienation before 20 December 2004?
- Did death occur before or after 9 September 2005?
- Were there earlier deaths or separations that changed the coparcenary?

Request legal review if the answers depend on interpreting deeds, oral partitions, blends of separate and joint property, adoption, or disputed genealogy.

When this branch opens, update the remaining-answer range and explain that the deceased's own coparcenary interest must be established before succession can be calculated.

## 4. Male intestate route

Ask Class I questions first:

- Was any widow alive at death? If more than one, how many?
- Was the deceased's mother alive?
- Which sons and daughters were alive?
- Which sons or daughters predeceased the deceased?
- For each predeceased child, which statutorily relevant descendants or widows were alive?

Stop there if any Class I heir or represented Class I branch exists.

Once the first-priority route is supported, show a short route preview naming the likely heir group and the facts still needed. Do not show shares until the statutory units are known.

Only if none exists, ask Class II entry by entry:

1. Father.
2. Son's daughter's son; son's daughter's daughter; brother; sister.
3. Daughter's son's son; daughter's son's daughter; daughter's daughter's son; daughter's daughter's daughter.
4. Brother's son; sister's son; brother's daughter; sister's daughter.
5. Father's father; father's mother.
6. Father's widow; brother's widow.
7. Father's brother; father's sister.
8. Mother's father; mother's mother.
9. Mother's brother; mother's sister.

Stop at the first entry containing an eligible heir. Clarify full, half, or uterine blood where it can change eligibility or priority.

Only if no Schedule heir exists, collect agnates. Only if no agnate exists, collect cognates. For each candidate record the relationship path, degrees of ascent, degrees of descent, and blood/adoption basis.

## 5. Female intestate route

Ask separately for every property because source can change the route.

First establish whether the deceased left:

- any living son or daughter;
- children of any predeceased son or daughter;
- a husband.

Then classify the property source:

- inherited from father or mother;
- inherited from husband or father-in-law;
- in Kerala, inherited from a predeceased son;
- any other source, including self-acquired, gift, will, partition, purchase, or inheritance from another person.

If sons, daughters, or represented descendants exist, section 15(2)(a) and (b) do not divert the property. Apply the section 15(1)(a) entry with section 16 representation.

If the first entry fails, test the remaining section 15(1) entries in order: heirs of husband; mother and father; heirs of father; heirs of mother. For an `heirs of` route, construct a new statutory succession context as directed by section 16 Rule 3; do not merely list the closest relatives.

For Kerala property inherited from a predeceased son, apply section 15(2)(c) and construct the predeceased son's heir context. Confirm that the Kerala amendment governs the death and property.

After the source is identified, show a route preview explaining in plain language whether the ordinary order or a source-based return route is likely to apply.

## 6. Eligibility and special facts

Ask only when indicated:

- Was a potential child conceived before death and later born alive?
- Did two relevant people die in the same event, and is the order of death uncertain?
- Has a potential heir been found to have murdered or abetted the murder relevant to section 25?
- Did a Hindu convert, and were any children born after conversion non-Hindu when succession opened?
- Is any relationship, marriage, adoption, legitimacy fact, or date disputed?

Treat accusations, pending proceedings, and disputed status as review issues, not established disqualifications.

When several short checks are simultaneously relevant, combine them into one numbered or lettered card with `None of these` and `Not sure` options. Do not present irrelevant rare exceptions merely to make the checklist appear complete.

## 7. Confirmation checkpoint

Before calculating a complex case, summarize:

- governing death date and jurisdiction;
- property-by-property ownership and character;
- normalized family branches and survival status;
- disqualifications or presumptions applied;
- assumptions and unknowns.

Ask the user to correct the summary. Do not repeat this checkpoint for a simple single-property case with three or fewer direct heirs and no uncertainty.

At this point show `Ready to calculate · Stage 5 of 5`. Separate confirmed facts, assumptions, disputed facts, and unknowns. Ask for one confirmation before calculating.

# Verbatim user-facing messages

Every message in this file is compliance-locked. Render EXACTLY as shown; substitute only `[bracketed placeholders]`. Never paraphrase, translate, or add prose around them.

**This file is the ONLY source for these blocks.** Read the block from this file in the turn you emit it. Never reproduce a block from ChatGPT memory, from a prior conversation, or from recall — these blocks are revised between releases, so any remembered wording is stale and may contain retired links or superseded instructions. If a remembered version conflicts with this file, this file wins.

Loading map (SKILL.md stage → block name):

- Stage 2c/2d — `## Important Information`
- Stage 2d (QC only) — `## QC advisor message`
- Stage 2e — `## Selection prompt`
- Stage 3b (successful handoff, non-variant plan) — `## Stage 3 success block` (contains both eligibility disclosure and handoff link — emit as one block)
- Stage 3b (successful handoff, SEMH selected) — `## SEMH single-deductible success block` (REPLACES the standard block)
- Stage 3b (successful handoff, STCIH selected) — `## STCIH single-tier success block` (REPLACES the standard block)
- Stage 3b (`saveQuotes` failure after retry) — `## saveQuotes failure fallback`
- Stage 3 (user declines) — `## Non-affirmative outright decline`
- Non-negotiable rule #2 (asked "which plan?") — `## Plan-choice deflection`
- Scope guardrail — `## Scope redirect`
- Refusal routing table — `## Refusal variants`

---

## Important Information

Render VERBATIM in Stage 2 immediately after the priced table.

**EN:**

---

**Important Information**

To be covered under these policies, you must also be covered under a government health insurance plan (GHIP) for the entire time you are travelling. Review your GHIP to confirm the maximum number of days allowed outside your province or territory of residence.

This quote is based exclusively on the automated processing of your personal information. For more information, please consult our Canadian Privacy Policy.

The quote provided is for informational purposes only and is not an insurance contract or guarantee of coverage. Any coverage is subject to eligibility requirements and the applicable policy terms, conditions, limitations, and exclusions.

---

**FR:**

---

**Information importante**

Pour bénéficier de la couverture aux termes de ce contrat, vous devez également être couvert par un régime public d'assurance maladie pendant toute la durée de votre voyage. Consultez votre régime public d'assurance maladie pour connaître le nombre maximum de jours autorisés en dehors de votre province ou territoire de résidence.

Cette soumission est basée exclusivement sur le traitement automatisé de vos renseignements personnels. Pour obtenir plus d'informations, veuillez consulter notre Politique de protection des renseignements personnels du Secteur Canada.

La soumission fournie est à titre informatif seulement et ne constitue ni un contrat d'assurance ni une garantie de couverture. Toute couverture est assujettie aux critères d'admissibilité ainsi qu'aux modalités, conditions, limitations et exclusions applicables à la police d'assurance.

---

## QC advisor message

Show immediately after Important Information if `provinceOfResidence === "QC"`. Informational only — continue the flow.

**EN:**

> *"Would you like to speak to a licensed insurance advisor? Call us at 1-877-268-3763 from Monday to Friday, 8:00 AM to 8:00 PM."*

**FR:**

> *"Souhaitez-vous parler à un conseiller en assurance autorisé? Vous pouvez communiquer avec nous au 1-877-268-3763, du lundi au vendredi, de 8 h à 20 h."*

---

## Selection prompt

Render VERBATIM at the end of the Stage 2 turn (after Important Information and, when applicable, the QC advisor message). Then STOP and wait for the user's reply.

**EN:**

> *"Which of these plans suits your needs? Let me know the plan name and I can save your quote."*

**FR :**

> *« Lequel de ces régimes répond à vos besoins? Indiquez-moi le nom du régime et je pourrai sauvegarder votre soumission. »*

---

## Stage 3 success block

Render VERBATIM in Stage 3 after `saveQuotes` returns a `QTE...` `paxes[0].policyNumber`. This is a SINGLE block containing the handoff link AND the eligibility disclosure — they are inseparable. **Never render the handoff link without the eligibility disclosure immediately below it.** Never render the eligibility disclosure without the handoff link immediately above it.

Substitute `[plan name]` with the catalog name for the chosen plan (EN name in EN flow, FR name in FR flow). Substitute `<Step 6 URL>` with the successful-quote URL (must contain `_Quote_B2C_AQCTR_`).

**EN:**

> Great! I've prepared your information for the [plan name] plan.
>
> [Complete your purchase on CoverMe.com](<Step 6 EN URL>)
>
> If you have any questions, you can call CoverMe at 1-877-268-3763.

---

**Important Eligibility Information**

You are not eligible for this insurance if any of the following apply to you or anyone you want to cover:

- Travelling against the advice of a physician
- Have been diagnosed with a terminal illness with less than 6 months to live
- Require kidney dialysis
- Used home oxygen in the 12 months before you applied for this insurance
- Do not reside in Canada
- Not covered under a government health insurance plan (GHIP) for the entire duration of your trip

If any of these statements apply to you or anyone you want to cover, you are not eligible for this insurance.

By continuing to CoverMe.com for purchase, I confirm that I am eligible for this insurance.

---

**FR :**

> Parfait! J'ai préparé vos renseignements pour le régime [plan name].
>
> [Achetez une assurance voyage en ligne | PourmeprotégerMD de Manuvie](<Step 6 FR URL>)
>
> Si vous avez des questions, vous pouvez nous appeler au 1-877-268-3763.

---

**Informations importantes sur l'admissibilité**

Vous n'êtes pas admissible à cette assurance si l'une des situations suivantes s'applique à vous ou à toute personne que vous voulez couvrir :

- Vous voyagez contre l'avis d'un médecin;
- Vous avez reçu un diagnostic de maladie en phase terminale qui établit votre espérance de vie à moins de six mois;
- Vous avez besoin de dialyse rénale;
- Vous avez utilisé de l'oxygène à domicile au cours des 12 mois précédant votre demande d'assurance;
- Vous ne résidez pas au Canada;
- Vous n'êtes pas assuré au titre d'un régime public d'assurance maladie pendant toute la durée de votre voyage.

Si vous ou une des personnes que vous désirez assurer êtes dans l'une de ces situations, vous n'êtes pas admissible à cette assurance.

En continuant vers pourmeproteger.com pour effectuer l'achat, je confirme que je suis admissible à cette assurance.

---

## SEMH single-deductible success block

Render VERBATIM in Stage 3 after `saveQuotes` returns a `QTE...` `paxes[0].policyNumber` **only when the selected plan is SEMH**. This block REPLACES the standard Stage 3 success block for SEMH.

It contains, in this exact order: the preamble, the successful-quote handoff link, the deductible-adjustment disclaimer, the phone line, then the Important Eligibility Information disclosure. All parts are inseparable — never render one without the others.

Substitute `<Step 6 URL>` from the successful-quote template in the Handoff URL matrix (contains `_Quote_B2C_AQCTR_`). The handoff link carries the saved `QTE...` so the customer's trip details pre-fill on CoverMe.com and they can adjust the deductible there without starting over.

**Note:** SEMH is always saved at `deductible: 0`. This block is the SEMH success path; it directs customers to the Edit button on their pre-filled CoverMe.com quote page if they want a different deductible.

**EN:**

> Great! I've prepared your information for the Single-Trip Emergency Medical Plan with a $0 deductible.
>
> [Complete your purchase on CoverMe.com](<Step 6 EN URL>)
>
> This link completes your purchase with a **$0 deductible**. If you'd prefer a higher deductible ($500, $1,000, $5,000, or $10,000) for a lower premium, click the link above and then click **Edit** next to your selected plan to adjust your deductible.
>
> If you have any questions, you can call CoverMe at 1-877-268-3763.

---

**Important Eligibility Information**

You are not eligible for this insurance if any of the following apply to you or anyone you want to cover:

- Travelling against the advice of a physician
- Have been diagnosed with a terminal illness with less than 6 months to live
- Require kidney dialysis
- Used home oxygen in the 12 months before you applied for this insurance
- Do not reside in Canada
- Not covered under a government health insurance plan (GHIP) for the entire duration of your trip

If any of these statements apply to you or anyone you want to cover, you are not eligible for this insurance.

By continuing to CoverMe.com for purchase, I confirm that I am eligible for this insurance.

---

**FR :**

> Parfait! J'ai préparé vos renseignements pour le régime Soins médicaux d'urgence – Voyage unique avec une franchise de 0 $.
>
> [Achetez une assurance voyage en ligne | PourmeprotégerMD de Manuvie](<Step 6 FR URL>)
>
> Ce lien permet de compléter votre achat avec une **franchise de 0 $**. Si vous préférez une franchise plus élevée (500 $, 1 000 $, 5 000 $ ou 10 000 $) pour une prime moins élevée, cliquez sur le lien ci-dessus, puis cliquez sur **Modifier** à côté du régime sélectionné pour ajuster votre franchise.
>
> Si vous avez des questions, vous pouvez nous appeler au 1-877-268-3763.

---

**Informations importantes sur l'admissibilité**

Vous n'êtes pas admissible à cette assurance si l'une des situations suivantes s'applique à vous ou à toute personne que vous voulez couvrir :

- Vous voyagez contre l'avis d'un médecin;
- Vous avez reçu un diagnostic de maladie en phase terminale qui établit votre espérance de vie à moins de six mois;
- Vous avez besoin de dialyse rénale;
- Vous avez utilisé de l'oxygène à domicile au cours des 12 mois précédant votre demande d'assurance;
- Vous ne résidez pas au Canada;
- Vous n'êtes pas assuré au titre d'un régime public d'assurance maladie pendant toute la durée de votre voyage.

Si vous ou une des personnes que vous désirez assurer êtes dans l'une de ces situations, vous n'êtes pas admissible à cette assurance.

En continuant vers pourmeproteger.com pour effectuer l'achat, je confirme que je suis admissible à cette assurance.

---

## STCIH single-tier success block

Render VERBATIM in Stage 3 after `saveQuotes` returns a `QTE...` `paxes[0].policyNumber` **only when the selected plan is STCIH**. This block REPLACES the standard Stage 3 success block for STCIH.

It contains, in this exact order: the preamble, the successful-quote handoff link, the coverage-adjustment disclaimer, the phone line, then the Important Eligibility Information disclosure. All parts are inseparable — never render one without the others.

Substitute `<Step 6 URL>` from the successful-quote template in the Handoff URL matrix (contains `_Quote_B2C_AQCTR_`). The handoff link carries the saved `QTE...` so the customer's trip details pre-fill on CoverMe.com and they can adjust the coverage amount there without starting over.

**Note:** STCIH is always quoted and saved at `coverageAmount: 30000`, shown to the user as `Unlimited coverage`. This block is the STCIH success path; it directs customers to the Edit button on their pre-filled CoverMe.com quote page if they want a lower coverage amount. Never write the integer `30000` — the user-facing label is always `Unlimited`.

**EN:**

> Great! I've prepared your information for the Trip Cancellation and Trip Interruption plan with Unlimited trip cancellation coverage.
>
> [Complete your purchase on CoverMe.com](<Step 6 EN URL>)
>
> This link completes your purchase with **Unlimited** trip cancellation coverage. If you'd prefer a lower coverage amount for a lower premium, click the link above and then click **Edit** next to your selected plan to adjust your coverage amount.
>
> If you have any questions, you can call CoverMe at 1-877-268-3763.

---

**Important Eligibility Information**

You are not eligible for this insurance if any of the following apply to you or anyone you want to cover:

- Travelling against the advice of a physician
- Have been diagnosed with a terminal illness with less than 6 months to live
- Require kidney dialysis
- Used home oxygen in the 12 months before you applied for this insurance
- Do not reside in Canada
- Not covered under a government health insurance plan (GHIP) for the entire duration of your trip

If any of these statements apply to you or anyone you want to cover, you are not eligible for this insurance.

By continuing to CoverMe.com for purchase, I confirm that I am eligible for this insurance.

---

**FR :**

> Parfait! J'ai préparé vos renseignements pour le régime Annulation de voyage et Interruption de voyage avec une protection illimitée en cas d'annulation.
>
> [Achetez une assurance voyage en ligne | PourmeprotégerMD de Manuvie](<Step 6 FR URL>)
>
> Ce lien permet de compléter votre achat avec une protection **illimitée** en cas d'annulation. Si vous préférez un montant de protection moins élevé pour une prime moins élevée, cliquez sur le lien ci-dessus, puis cliquez sur **Modifier** à côté du régime sélectionné pour ajuster votre montant de protection.
>
> Si vous avez des questions, vous pouvez nous appeler au 1-877-268-3763.

---

**Informations importantes sur l'admissibilité**

Vous n'êtes pas admissible à cette assurance si l'une des situations suivantes s'applique à vous ou à toute personne que vous voulez couvrir :

- Vous voyagez contre l'avis d'un médecin;
- Vous avez reçu un diagnostic de maladie en phase terminale qui établit votre espérance de vie à moins de six mois;
- Vous avez besoin de dialyse rénale;
- Vous avez utilisé de l'oxygène à domicile au cours des 12 mois précédant votre demande d'assurance;
- Vous ne résidez pas au Canada;
- Vous n'êtes pas assuré au titre d'un régime public d'assurance maladie pendant toute la durée de votre voyage.

Si vous ou une des personnes que vous désirez assurer êtes dans l'une de ces situations, vous n'êtes pas admissible à cette assurance.

En continuant vers pourmeproteger.com pour effectuer l'achat, je confirme que je suis admissible à cette assurance.

---

## saveQuotes failure fallback

Second `saveQuotes` failure only. Do NOT invent a `quoteNum`, do NOT fabricate a link, do NOT ask for real PII to work around. Stop after rendering.

**EN:**

> *"I wasn't able to process your request through ChatGPT right now. To get a quote and complete your purchase, please visit [CoverMe.com](https://www.coverme.com/) directly or call CoverMe at 1-877-268-3763. They'll be able to help you with the [plan name] plan."*

**FR :**

> *« Je n'ai pas pu traiter votre demande sur ChatGPT pour le moment. Pour obtenir une soumission et effectuer votre achat, veuillez visiter [pourmeproteger.com](https://www.pourmeproteger.com/) directement ou nous appeler au 1-877-268-3763. Nous pourrons vous aider avec le régime [plan name]. »*

---

## Non-affirmative outright decline

Rendered in Stage 3 only when the user explicitly declines (e.g. "no", "not now", "cancel"). Stop after rendering.

**EN:**

> *"No problem! If you change your mind, visit [CoverMe.com](https://www.coverme.com/) or call 1-877-268-3763 to get your quote and purchase."*

**FR :**

> *« Pas de problème! Si vous changez d'avis, visitez [pourmeproteger.com](https://www.pourmeproteger.com/) ou appelez-nous au 1-877-268-3763 pour obtenir votre soumission et effectuer votre achat. »*

---

## Plan-choice deflection

Render VERBATIM if the user asks the assistant to pick, recommend, or characterize a plan as best. Stop after rendering.

**EN:**

> *"I'm not able to recommend a specific plan — the details of each are in the table above so you can compare. To speak with a licensed CoverMe representative who can help you choose, please call 1-877-268-3763."*

**FR :**

> *« Je ne peux pas recommander un régime en particulier — les détails de chacun sont dans le tableau ci-dessus pour vous permettre de comparer. Pour parler à un représentant CoverMe agréé qui peut vous aider à choisir, veuillez composer le 1-877-268-3763. »*

---

## Scope redirect

Render VERBATIM (single physical line) when the user asks anything outside the quote workflow, then re-ask the current stage's question. Never prefix with "Great question but". Never answer partially.

**EN:**

> *"I can only help with generating your CoverMe travel insurance quote. Let's continue — [re-ask current step]."*

**FR :**

> *« Je ne peux vous aider qu'à générer votre soumission d'assurance voyage CoverMe. Continuons — [reposer l'étape en cours]. »*

---

## Refusal variants

**Rendering rules:** prose paragraph on a **single physical line** (source line breaks → hard breaks in the renderer). Append the shared link block (bulleted, under `Link:` EN / `Lien :` FR) to every variant. Never omit or trim the link. `HANDOFF-AGE-MEDICAL` says "medical questionnaire" and never age.

### EN

#### HANDOFF-DEFAULT

> Unfortunately, we're unable to provide a quote for your trip through ChatGPT. Some travel plans require additional information. Please continue to CoverMe.com to receive a quote.

#### HANDOFF-AGE-MEDICAL

> I'm unable to provide a quote for your trip as you may have to fill out a medical questionnaire. Please continue to CoverMe.com to receive a quote.

#### HANDOFF-MULTI-TRIP

> If you're looking for coverage for more than one trip, I'm unable to provide a quote. Please continue to CoverMe.com to receive a quote.

#### HANDOFF-MULTI-TRAVELLER

> If you're looking to cover more than one traveller, I'm unable to provide a quote. Please continue to CoverMe.com to receive a quote.

#### HANDOFF-OFF-TOPIC

> It seems like you might not be looking for travel insurance. If you are, please tell me about your trip or continue to CoverMe.com to receive a quote.

#### Shared EN link block (append to every EN variant)

> Link:
>
> - [Continue to CoverMe.com](https://www.coverme.com/travel-insurance.html?cid=CA-EN_ML_IS_CAI_CGPT_CGPTTravelPlugin_COVERMETRAVEL_IM_-_-_NoQuote_B2C_AQCTR_-_-)

### FR

#### FR-HANDOFF-DEFAULT

> Malheureusement, nous ne sommes pas en mesure de vous fournir une soumission pour votre voyage par l'intermédiaire de ChatGPT. Certains projets de voyage nécessitent des renseignements supplémentaires. Veuillez continuer sur pourmeproteger.com afin d'obtenir une soumission.

#### FR-HANDOFF-AGE-MEDICAL

> Je ne suis pas en mesure de fournir une soumission pour votre voyage, car vous pourriez devoir remplir un questionnaire médical. Veuillez continuer sur pourmeproteger.com afin d'obtenir une soumission.

#### FR-HANDOFF-MULTI-TRIP

> Si vous recherchez une couverture pour plus d'un voyage, je ne suis pas en mesure de fournir une soumission. Veuillez continuer sur pourmeproteger.com afin d'obtenir une soumission.

#### FR-HANDOFF-MULTI-TRAVELLER

> Si vous souhaitez assurer plus d'un voyageur, je ne suis pas en mesure de fournir une soumission. Veuillez continuer sur pourmeproteger.com afin d'obtenir une soumission.

#### FR-HANDOFF-OFF-TOPIC

> Il semble que vous ne recherchiez peut-être pas une assurance voyage. Si c'est bien ce que vous recherchez, veuillez me parler de votre voyage ou continuer sur pourmeproteger.com afin d'obtenir une soumission.

#### Shared FR link block (append to every FR variant)

> Lien :
>
> - [Achetez une assurance voyage en ligne | PourmeprotégerMD de Manuvie](https://www.pourmeproteger.com/assurance-voyage.html?cid=CA-FR_ML_IS_CAI_CGPT_CGPTTravelPlugin_COVERMETRAVEL_IM_-_-_NoQuote_B2C_AQCTR_-_-)

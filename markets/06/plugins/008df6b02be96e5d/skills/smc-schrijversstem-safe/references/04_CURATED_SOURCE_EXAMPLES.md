# Gecureerde echte bronreferenties 1.2.0-rc.13

Deze referenties sturen alleen toon, ritme en gedachtebeweging. De actuele briefing blijft de enige inhoudsbron.

De writer maakt eerst een schone positieve schrijversbrief. Bij long-form gebruikt hij maximaal één writerreferentie. Tijdens de eerste schrijverspass wordt geen aparte structuurreferentie geladen. Negatieve, structurele en assessmentreferenties zijn audit-only.

De rol ASSESSMENT_CONTROL betekent open kalibratie na het concept, niet bewezen
onafhankelijk toetsmateriaal. De volledige herkomst, inclusief microvoorbeelden,
staat in `07_REFERENCE_SPLIT.json`. Er is geen geverifieerde onafhankelijke holdout
in dit pakket. Het rolonderscheid is geen technische afscherming van bestandlezing.

## Behouden writer-first regels

- Een referentie mag geen nieuwe propositie autoriseren.
- Negatieve voorbeeldzinnen worden niet vóór het eerste concept geladen.
- Iedere zichtbare betekenis heeft één globale hoofdplek.
- Meta-proza over gegevens, eenheden, rollen of tekstopbouw wordt verwijderd.
- Exclusiviteit wordt na de schrijverspass opnieuw tegen de volledige groep gecontroleerd.
- Service- en scenarioproposities blijven niet-overdraagbaar zonder expliciete briefingsteun.

### REAL-PROD-001 — plain_technical_explanation

- Rol: `WRITER_REFERENCE`
- Writer-weergave: `RAW_STYLE_REFERENCE`
- Bronfamilie: `261`
- Profielen: product, faq, hybrid
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, MEDICAL_OR_SAFETY, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: The first two sentences explain a technical layout in ordinary language before any advantage is added.
- Gebruik: alleen directheid, ritme, gedachtebeweging en methode van concrete uitleg.
- Verboden: alle bronproposities en unieke formuleringen.

### REAL-PROD-002 — location_action_use

- Rol: `WRITER_REFERENCE`
- Writer-weergave: `RAW_STYLE_REFERENCE`
- Bronfamilie: `261`
- Profielen: product, faq, hybrid
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, MEDICAL_OR_SAFETY, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: A coherent paragraph moves from charging options to connector location and the exact user action.
- Gebruik: alleen directheid, ritme, gedachtebeweging en methode van concrete uitleg.
- Verboden: alle bronproposities en unieke formuleringen.

### REAL-PROD-003 — control_action_situation

- Rol: `WRITER_REFERENCE`
- Writer-weergave: `RAW_STYLE_REFERENCE`
- Bronfamilie: `261`
- Profielen: product, faq, review
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, MEDICAL_OR_SAFETY, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: The control is named, the action is explained and the practical use follows immediately.
- Gebruik: alleen directheid, ritme, gedachtebeweging en methode van concrete uitleg.
- Verboden: alle bronproposities en unieke formuleringen.

### REAL-PROD-004 — dimensions_to_storage_situation

- Rol: `WRITER_REFERENCE`
- Writer-weergave: `RAW_STYLE_REFERENCE`
- Bronfamilie: `261`
- Profielen: product, local, hybrid
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, MEDICAL_OR_SAFETY, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: Concrete dimensions are connected to a recognisable storage situation without assessment jargon.
- Gebruik: alleen directheid, ritme, gedachtebeweging en methode van concrete uitleg.
- Verboden: alle bronproposities en unieke formuleringen.

### REAL-PROD-005 — term_in_plain_language

- Rol: `WRITER_REFERENCE`
- Writer-weergave: `SAFE_STYLE_PROJECTION`
- Bronfamilie: `262`
- Profielen: product, advice, faq
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, MEDICAL_OR_SAFETY, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: A technical option is explained in one ordinary sentence by saying what the hand does.
- Veilige projectie:
  - Beweging: ['name the authorized technical term', 'explain the authorized hand action in ordinary language', 'stop before adding suitability or comfort']
  - Ritme: one compact explanation with a concrete hand action
  - Stem: direct and practical without transferring the source option or user claim

### REAL-PROD-006 — concrete_tradeoff

- Rol: `ASSESSMENT_CONTROL`
- Writer-weergave: `ASSESSMENT_ONLY`
- Bronfamilie: `264`
- Profielen: product, comparison, hybrid
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, MEDICAL_OR_SAFETY, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: A real trade-off is described directly: one option removes another facility.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### REAL-PROD-007 — difference_character_opening

- Rol: `WRITER_REFERENCE`
- Writer-weergave: `SAFE_STYLE_PROJECTION`
- Bronfamilie: `261`
- Profielen: product, comparison, brand, hybrid
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, MEDICAL_OR_SAFETY, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: The opening gives the model an immediate, memorable character and then supports it with a connected thought movement.
- Veilige projectie:
  - Beweging: ['name the model or subject directly', 'state one briefing-supported difference', 'develop that difference through one authorized action or situation', 'end with a memorable but fully supported model image']
  - Ritme: one connected paragraph with medium-to-high energy and no specification dump
  - Stem: confident and human without transferring ride, stability, appearance or market claims

### REAL-LOCAL-001 — warm_attitude_with_condition

- Rol: `WRITER_REFERENCE`
- Writer-weergave: `SAFE_STYLE_PROJECTION`
- Bronfamilie: `272-vught`
- Profielen: local, advice, service, hybrid, regulated
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: DAILY_SCENARIO, SERVICE_AVAILABILITY, SERVICE_PROMISE, ADVISOR_BEHAVIOR, NUMBER_OF_MODELS_OR_OPTIONS, FREE_OR_NO_OBLIGATION, DELIVERY_OR_TIMING
- Waarom geselecteerd: Warmth comes from accepting both certainty and doubt; the availability condition stays intact.
- Veilige projectie:
  - Beweging: ['recognize certainty or doubt', 'state only the authorized next step', 'keep any authorized condition close to the action']
  - Ritme: one warm paragraph with a natural condition
  - Stem: welcoming and calm without adding contact, availability or advisor promises

### REAL-SERVICE-001 — active_sender_and_service_action

- Rol: `WRITER_REFERENCE`
- Writer-weergave: `SAFE_STYLE_PROJECTION`
- Bronfamilie: `262`
- Profielen: service, local, hybrid
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: SERVICE_AVAILABILITY, SERVICE_PROMISE, ADVISOR_BEHAVIOR, DELIVERY_OR_TIMING, FREE_OR_NO_OBLIGATION
- Waarom geselecteerd: The sender is concrete and active: collect, service and return.
- Veilige projectie:
  - Beweging: ['name an authorized service action directly', 'explain the concrete authorized handoff', 'stop after the permitted action']
  - Ritme: active sender, compact sentences, no procedural list
  - Stem: human and active without inventing time, advice, pickup, delivery or reassurance

### REAL-REG-001 — daily_life_questioning

- Rol: `WRITER_REFERENCE_WEAK`
- Writer-weergave: `SAFE_STYLE_PROJECTION`
- Bronfamilie: `754`
- Profielen: regulated, advice
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: LEGAL_OR_WMO_PROCESS, DAILY_SCENARIO, USER_SUITABILITY, EMOTIONAL_OUTCOME, PRODUCT_SPECIFICATION, MEDICAL_OR_SAFETY
- Waarom geselecteerd: Daily destinations make an abstract mobility need concrete. The source is weak for regulated facts, so only the human question movement is usable.
- Veilige projectie:
  - Beweging: ['start from an authorized everyday situation', 'make the situation concrete', 'connect only to the authorized preparation or question']
  - Ritme: one developed example instead of a string of questions
  - Stem: calm and human without transferring Wmo process, distance, family or range claims

### REAL-REVIEW-001 — human_observation_with_aside

- Rol: `WRITER_REFERENCE`
- Writer-weergave: `RAW_STYLE_REFERENCE`
- Bronfamilie: `762`
- Profielen: review
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: REVIEW_OR_TEST_EXPERIENCE, PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, DAILY_SCENARIO, EMOTIONAL_OUTCOME
- Waarom geselecteerd: A longer review paragraph combines a limitation, an adjustment action, a human aside and a compact judgement.
- Gebruik: alleen directheid, ritme, gedachtebeweging en methode van concrete uitleg.
- Verboden: alle bronproposities en unieke formuleringen.

### REAL-REVIEW-002 — specific_test_observation

- Rol: `WRITER_REFERENCE`
- Writer-weergave: `RAW_STYLE_REFERENCE`
- Bronfamilie: `762`
- Profielen: review
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: REVIEW_OR_TEST_EXPERIENCE, PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, DAILY_SCENARIO, EMOTIONAL_OUTCOME
- Waarom geselecteerd: The paragraph names exactly what was tested and connects it to one recognisable situation.
- Gebruik: alleen directheid, ritme, gedachtebeweging en methode van concrete uitleg.
- Verboden: alle bronproposities en unieke formuleringen.

### REAL-COST-001 — direct_payment_language

- Rol: `WRITER_REFERENCE_WEAK`
- Writer-weergave: `SAFE_STYLE_PROJECTION`
- Bronfamilie: `270`
- Profielen: cost_payment
- Writer mag laden: ja
- Beoordelaar mag laden: nee
- Risico's: PRICE_OR_DISCOUNT, DELIVERY_OR_TIMING, LEGAL_OR_WMO_PROCESS, SERVICE_PROMISE
- Waarom geselecteerd: Direct je-language explains the sequence of payment moments instead of using passive administrative wording.
- Veilige projectie:
  - Beweging: ['state the authorized payment fact directly', 'explain the practical difference in ordinary language', 'add one authorized limitation']
  - Ritme: direct je-form, no policy language
  - Stem: clear and matter-of-fact without price, discount or contract details

### REAL-HYBRID-001 — short_key_model_block

- Rol: `STRUCTURE_REFERENCE`
- Writer-weergave: `STRUCTURE_ONLY`
- Bronfamilie: `718`
- Profielen: hybrid, category, brand
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: A compact block gives one model a clear range and speed character.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### REAL-HYBRID-002 — longer_distinct_model_block

- Rol: `STRUCTURE_REFERENCE`
- Writer-weergave: `STRUCTURE_ONLY`
- Bronfamilie: `718`
- Profielen: hybrid, category, brand
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: A materially different model receives a longer block because it has a different use character.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### REAL-HYBRID-003 — short_supporting_model_block

- Rol: `ASSESSMENT_CONTROL`
- Writer-weergave: `ASSESSMENT_ONLY`
- Bronfamilie: `718`
- Profielen: category, brand
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: A supporting model is kept visibly shorter, illustrating meaningful asymmetry.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### REAL-NEWS-001 — update_sentence_with_direct_fact

- Rol: `STRUCTURE_REFERENCE_WEAK`
- Writer-weergave: `STRUCTURE_ONLY`
- Bronfamilie: `846`
- Profielen: news, brand, category
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, DELIVERY_OR_TIMING, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: A short update states two concrete changes without explaining the editorial method.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### CONTROL-PROD-001 — allowed_explanation_vs_overclaim

- Rol: `ASSESSMENT_CONTROL`
- Writer-weergave: `ASSESSMENT_ONLY`
- Bronfamilie: `832`
- Profielen: product, comparison
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, MEDICAL_OR_SAFETY, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: Useful to test whether the assessor separates a charging explanation from unapproved ease or ideal-user claims.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### CONTROL-LOCAL-001 — service_condition_and_scope

- Rol: `ASSESSMENT_CONTROL`
- Writer-weergave: `ASSESSMENT_ONLY`
- Bronfamilie: `845`
- Profielen: local, service
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: DAILY_SCENARIO, SERVICE_AVAILABILITY, SERVICE_PROMISE, ADVISOR_BEHAVIOR, NUMBER_OF_MODELS_OR_OPTIONS, FREE_OR_NO_OBLIGATION, DELIVERY_OR_TIMING
- Waarom geselecteerd: Useful control for separating allowed service description from unapproved free, home or multi-model promises.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### CONTROL-REVIEW-001 — actual_first_impression

- Rol: `ASSESSMENT_CONTROL`
- Writer-weergave: `ASSESSMENT_ONLY`
- Bronfamilie: `795`
- Profielen: review
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: REVIEW_OR_TEST_EXPERIENCE, PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, DAILY_SCENARIO, EMOTIONAL_OUTCOME
- Waarom geselecteerd: An independent review family for checking whether a review sounds observational rather than product-copy-like.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### CONTROL-REVIEW-002 — physical_impression_and_use_boundary

- Rol: `ASSESSMENT_CONTROL`
- Writer-weergave: `ASSESSMENT_ONLY`
- Bronfamilie: `817`
- Profielen: review
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: REVIEW_OR_TEST_EXPERIENCE, PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, DAILY_SCENARIO, EMOTIONAL_OUTCOME
- Waarom geselecteerd: An independent review family with a concrete physical first impression and use boundary.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### CONTROL-REG-001 — unsafe_process_assumption_control

- Rol: `ASSESSMENT_CONTROL`
- Writer-weergave: `ASSESSMENT_ONLY`
- Bronfamilie: `716`
- Profielen: regulated
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: LEGAL_OR_WMO_PROCESS, DAILY_SCENARIO, USER_SUITABILITY, EMOTIONAL_OUTCOME, PRODUCT_SPECIFICATION, MEDICAL_OR_SAFETY
- Waarom geselecteerd: Negative control for entitlement, income, duration and municipal-process assumptions.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### CONTROL-HYBRID-001 — unequal_blocks_without_same_family_as_writer

- Rol: `ASSESSMENT_CONTROL`
- Writer-weergave: `ASSESSMENT_ONLY`
- Bronfamilie: `846`
- Profielen: hybrid, category, brand
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: Independent category/update family to check asymmetry without using the same source family as the main writer anchors.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### NEGATIVE-EDITORIAL-001 — editorial_notes

- Rol: `NEGATIVE_REFERENCE`
- Writer-weergave: `NEGATIVE_ONLY`
- Bronfamilie: `755`
- Profielen: all
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, SERVICE_AVAILABILITY, SERVICE_PROMISE, ADVISOR_BEHAVIOR, NUMBER_OF_MODELS_OR_OPTIONS, FREE_OR_NO_OBLIGATION, PRICE_OR_DISCOUNT, DELIVERY_OR_TIMING, LEGAL_OR_WMO_PROCESS, MEDICAL_OR_SAFETY, REVIEW_OR_TEST_EXPERIENCE, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: Internal production instructions are not customer copy.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### NEGATIVE-MEDICAL-001 — medical_overclaim

- Rol: `NEGATIVE_REFERENCE`
- Writer-weergave: `NEGATIVE_ONLY`
- Bronfamilie: `753`
- Profielen: product, review, regulated
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, SERVICE_AVAILABILITY, SERVICE_PROMISE, ADVISOR_BEHAVIOR, NUMBER_OF_MODELS_OR_OPTIONS, FREE_OR_NO_OBLIGATION, PRICE_OR_DISCOUNT, DELIVERY_OR_TIMING, LEGAL_OR_WMO_PROCESS, MEDICAL_OR_SAFETY, REVIEW_OR_TEST_EXPERIENCE, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: Medical and therapeutic claims must never be learned as writing style.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### NEGATIVE-SEO-001 — keyword_list

- Rol: `NEGATIVE_REFERENCE`
- Writer-weergave: `NEGATIVE_ONLY`
- Bronfamilie: `812`
- Profielen: category, hub
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, SERVICE_AVAILABILITY, SERVICE_PROMISE, ADVISOR_BEHAVIOR, NUMBER_OF_MODELS_OR_OPTIONS, FREE_OR_NO_OBLIGATION, PRICE_OR_DISCOUNT, DELIVERY_OR_TIMING, LEGAL_OR_WMO_PROCESS, MEDICAL_OR_SAFETY, REVIEW_OR_TEST_EXPERIENCE, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: Keyword lists and SEO drafting residues are not prose examples.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### NEGATIVE-UNIVERSAL-001 — universal_success_claim

- Rol: `NEGATIVE_REFERENCE`
- Writer-weergave: `NEGATIVE_ONLY`
- Bronfamilie: `812`
- Profielen: category, product, brand
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, SERVICE_AVAILABILITY, SERVICE_PROMISE, ADVISOR_BEHAVIOR, NUMBER_OF_MODELS_OR_OPTIONS, FREE_OR_NO_OBLIGATION, PRICE_OR_DISCOUNT, DELIVERY_OR_TIMING, LEGAL_OR_WMO_PROCESS, MEDICAL_OR_SAFETY, REVIEW_OR_TEST_EXPERIENCE, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: Universal assortment and municipal-route claims are negative regressions.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### NEGATIVE-RULES-001 — contradictory_rules_and_claims

- Rol: `NEGATIVE_REFERENCE`
- Writer-weergave: `NEGATIVE_ONLY`
- Bronfamilie: `850`
- Profielen: product, regulated, hub
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, SERVICE_AVAILABILITY, SERVICE_PROMISE, ADVISOR_BEHAVIOR, NUMBER_OF_MODELS_OR_OPTIONS, FREE_OR_NO_OBLIGATION, PRICE_OR_DISCOUNT, DELIVERY_OR_TIMING, LEGAL_OR_WMO_PROCESS, MEDICAL_OR_SAFETY, REVIEW_OR_TEST_EXPERIENCE, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: Contradictory driving-licence and product claims are excluded from positive evidence.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

### NEGATIVE-RANKING-001 — unsupported_best_list

- Rol: `NEGATIVE_REFERENCE`
- Writer-weergave: `NEGATIVE_ONLY`
- Bronfamilie: `top5`
- Profielen: comparison, category, review
- Writer mag laden: nee
- Beoordelaar mag laden: ja
- Risico's: PRODUCT_SPECIFICATION, PRODUCT_PERFORMANCE, PRACTICAL_CONSEQUENCE, USER_SUITABILITY, DAILY_SCENARIO, EMOTIONAL_OUTCOME, SERVICE_AVAILABILITY, SERVICE_PROMISE, ADVISOR_BEHAVIOR, NUMBER_OF_MODELS_OR_OPTIONS, FREE_OR_NO_OBLIGATION, PRICE_OR_DISCOUNT, DELIVERY_OR_TIMING, LEGAL_OR_WMO_PROCESS, MEDICAL_OR_SAFETY, REVIEW_OR_TEST_EXPERIENCE, MARKET_WIDE_COMPARISON
- Waarom geselecteerd: A best-list packed with unsupported safety and quality claims is a negative reference.
- Niet gebruiken tijdens UITSCHRIJVEN; alleen voor beoordeling of negatieve controle.

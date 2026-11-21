---
key: research-risks
type: coaching
customer_visible: true
provenance: extension
source: "Research Vault v2 Research-Risks.md"
last_verified: "2026-07-20"
---

# Research Risks and Scientific Debates

Catalog of contradictions and unresolved debates that affect how a high-performance coach should read the data. Use this before over-claiming a pattern.



## Risk 1: Basic Emotions vs. Constructed Emotions
- **Severity:** HIGH
- **Affects:** Emotional Regulation, Emotional Acknowledgment, Micro Events
- **The debate:** Paul Ekman's framework posits 6-7 universal, biologically basic emotion categories (anger, disgust, fear, happiness, sadness, surprise) with discrete neural and physiological signatures. Lisa Feldman Barrett's theory of constructed emotion (2017) argues that emotions are not natural kinds but are constructed from domain-general ingredients (core affect, conceptual knowledge, social reality). SER pipelines trained on MELD, RAVDESS, and IEMOCAP all use categorical labels built on the Ekman assumption.
- **If Barrett is right:** Categorical emotion detection classifies cultural stereotypes of emotional expression, not biological states. Models trained on Western-labeled data would systematically misclassify non-Western speakers and impose a Western emotional ontology.
- **Mitigation:** Use a dimensional approach (arousal/valence circumplex) rather than categorical labels as the primary measurement substrate. Treat categorical labels as convenience summaries, not ground truth. Design Emotional-Regulation scoring to operate on arousal trajectory rather than emotion category transitions.
- **Status:** UNRESOLVED ,  active area of debate. Dimensional approach is more defensible but less intuitive for end users.

---

## Risk 2: Fredrickson & Losada Positivity Ratio Retraction
- **Severity:** MEDIUM
- **Affects:** Recovery Episodes, Micro Events
- **The debate:** Fredrickson & Losada (2005) claimed a precise critical positivity ratio of 2.9013:1 above which individuals and teams "flourish," derived from Lorenz equations borrowed from fluid dynamics. Brown, Sokal & Friedman (2013) demonstrated the mathematical model was fundamentally flawed ,  the Lorenz equations were applied without physical justification, and the precise ratio had no empirical basis. The American Psychologist issued a partial retraction.
- **What survives:** Fredrickson's qualitative broaden-and-build theory (positive emotions broaden thought-action repertoires) remains well-supported. The general finding that higher positive-to-negative ratios correlate with better outcomes is directionally valid.
- **Mitigation:** Never cite the specific 2.9013 ratio. Use Gottman's independently validated 5:1 ratio research (derived from longitudinal marital data) for positive-negative interaction benchmarks. Frame Recovery-Episodes scoring around trajectory (negative-to-neutral-to-positive shift) rather than ratio thresholds.
- **Status:** MITIGATED ,  ratio removed from scoring logic; broaden-and-build framing retained.

---

## Risk 3: Synchrony ,  Real or Artifact?
- **Severity:** HIGH
- **Affects:** LSM (Language Style Matching), Turn Taking, Backchannel Detection, Mirroring dimension
- **The debate:** Bernieri (1981) and Bernieri & Rosenthal (1991) established interactional synchrony as a core rapport indicator but also identified pseudo-synchrony: apparent coordination that arises from each individual's baseline motor rhythms rather than genuine dyadic coupling. When two people both have similar baseline speaking rates or gesture frequencies, statistical measures will detect "synchrony" even from spliced-together recordings of unrelated conversations. Recent motion-capture and cross-recurrence quantification studies (Paxton & Dale, 2013) attempt to address this with surrogate-pair controls.
- **If synchrony measures are inflated by artifact:** LSM scores and turn-taking coordination metrics would overestimate rapport in pairs who happen to share similar baseline communication styles, and underestimate it in pairs with different baselines who genuinely coordinate.
- **Mitigation:** Implement surrogate-pair baseline correction ,  compare observed coordination against shuffled/phase-randomized surrogates to establish above-chance synchrony. Normalize LSM scores against speaker-specific baselines where multiple conversations are available.
- **Status:** UNRESOLVED ,  surrogate correction implemented for Turn-Taking but not yet for LSM or Backchannel-Detection.

---

## Risk 4: Alignment Ambiguity ,  Rapport vs. Submission
- **Severity:** HIGH
- **Affects:** LSM (Language Style Matching), Agency Orientation, Power-Dynamics (proposed)
- **The debate:** Linguistic Style Matching (Niederhoffer & Pennebaker, 2002) measures bidirectional convergence of function word usage. However, convergence can indicate genuine rapport OR power-asymmetric accommodation where the lower-status speaker adapts to the higher-status speaker unilaterally. Danescu-Niculescu-Mizil et al. (2012) demonstrated that in Wikipedia and Supreme Court data, the lower-power individual accommodates more. Bidirectional LSM conflates these two dynamics into a single score.
- **If rapport and submission are conflated:** High LSM scores could mask dominance dynamics ,  a subordinate mirroring a dominant speaker would score identically to genuine mutual alignment.
- **Mitigation:** Directional LSM (proposed measurement) decomposes accommodation into Speaker-A-to-B and Speaker-B-to-A vectors. Asymmetry in directional LSM indicates power differential rather than rapport. Cross-reference with Agency-Orientation scores to flag unilateral accommodation.
- **Status:** PARTIALLY MITIGATED ,  Directional-LSM is proposed but not yet in production. Current bidirectional LSM cannot disambiguate.

---

## Risk 5: Over-Accommodation Detection Gap
- **Severity:** MEDIUM
- **Affects:** LSM (Language Style Matching), Reflective Listening, Communication Accommodation Theory measurements
- **The debate:** Giles' Communication Accommodation Theory (CAT) clearly establishes that over-accommodation is perceived negatively ,  it signals condescension, patronizing behavior, or inauthenticity. Examples include excessive mimicry, exaggerated speech simplification, or performative matching that feels "try-hard." However, most computational accommodation measures (including LSM) treat convergence as linearly positive: more matching equals more rapport.
- **If scoring is linear when the relationship is curvilinear:** Extreme convergence scores would be rewarded when they should be penalized. Over-accommodating salespeople would score high on rapport when clients actually perceive them as inauthentic.
- **Mitigation:** Introduce a curvilinear scoring function for accommodation-related measurements ,  moderate convergence scores highest, with penalties at both low convergence (disengagement) and extreme convergence (over-accommodation). Calibrate the inflection point using labeled data of perceived authenticity.
- **Status:** UNRESOLVED ,  current scoring is linear. Curvilinear calibration requires annotated data we do not yet have.

---

## Risk 6: Objective vs. Perceived Coordination Gap
- **Severity:** MEDIUM
- **Affects:** Turn Taking, Backchannel Detection, Response Latency, Engagement dimension
- **The debate:** Bernieri, Davis, Rosenthal & Knee (1994, UPenn) found that objectively measured behavioral coordination (coded from video) and participants' subjective ratings of coordination were only loosely correlated. People can feel coordinated when objective measures say they are not, and vice versa. This challenges the assumption that measurable behavioral coordination is a reliable proxy for experienced rapport.
- **If behavioral coordination is a poor proxy for felt rapport:** RapportScore's entire measurement architecture ,  which infers rapport from observable/computable behavioral signals ,  would have a systematic validity gap. The score would measure coordination, not rapport.
- **Mitigation:** Treat behavioral coordination as one input among several, not as a direct rapport proxy. The multi-dimensional architecture (7 dimensions, 17+ measurements) partially addresses this by triangulating across different signal types. Validate against self-reported rapport in calibration studies. Acknowledge the construct gap in documentation.
- **Status:** PARTIALLY MITIGATED ,  architecture is multi-dimensional, but ground-truth validation against perceived rapport is still needed.

---

## Risk 7: Cultural Calibration Absent
- **Severity:** HIGH
- **Affects:** ALL measurements, ALL dimensions
- **The debate:** Stivers et al. (2009) analyzed turn-taking across 10 languages and found significant cross-cultural variation in response timing (e.g., Danish speakers leave longer gaps; Japanese speakers overlap more frequently). Tannen (1984, 1994) documented that "high-involvement" conversational styles (frequent interruptions, overlapping speech, fast pace) are rapport markers in some cultures but rudeness markers in others. Nakane (2007) showed that Japanese silence in cross-cultural academic interactions is misinterpreted as disengagement by Western interlocutors when it actually signals respect and careful thinking.
- **If cultural norms are not normalized:** RapportScore would systematically over-rate rapport for speakers whose cultural norms align with the training data (likely Western, American English) and under-rate rapport for speakers from cultures with different conversational norms. This is both a validity problem and a bias/fairness problem.
- **Mitigation:** Build cultural calibration profiles that adjust baseline expectations for response latency, interruption frequency, silence duration, and directness. Start with language-pair detection and apply documented cultural norm adjustments. Long-term: train culture-specific models.
- **Status:** UNRESOLVED ,  no cultural normalization currently exists. This is the highest-priority gap for international deployment.

---

## Risk 8: Text-Only Classification Limitations
- **Severity:** MEDIUM
- **Affects:** Question Structure, Objection Structure, Repair Attempts
- **The debate:** Cresti & Moneglia (2023) demonstrated that prosodic contour is a primary determinant of speech act function ,  the same lexical string ("You're going to do that") can be a statement, a question, a challenge, or an expression of surprise depending solely on intonation. Text-based classification using only transcribed words systematically misclassifies speech acts where prosody changes the communicative function. Declarative syntax with rising intonation becomes a question; interrogative syntax with falling intonation becomes a rhetorical statement.
- **If text classification misidentifies speech acts:** Question-Structure measurements would miscount questions (missing prosodic questions, miscounting rhetorical questions). Objection-Structure would miss prosodically softened objections. Repair-Attempts scored from text alone would miss tonal repair cues.
- **Mitigation:** Integrate ASR prosodic features (pitch contour, intensity) with text classification. Use Whisper or similar models that can extract prosodic metadata alongside transcription. Design a multimodal speech act classifier rather than relying on text-only NLP.
- **Status:** PARTIALLY MITIGATED ,  architecture supports audio input, but current MVP relies primarily on text classification. Prosodic integration is on the roadmap.

---

## Risk 9: Repair Attempts vs. Recovery Episodes Overlap
- **Severity:** LOW
- **Affects:** Repair Attempts, Recovery Episodes
- **The debate:** Repair Attempts (from Schegloff, Jefferson & Sacks, 1977, and Gottman's relationship research) focus on immediate conversational actions to fix misunderstandings or de-escalate tension ,  they are local, turn-level phenomena. Recovery Episodes (informed by Fredrickson's broaden-and-build theory) track the trajectory from negative affect back to neutral or positive ,  they are arc-level phenomena spanning multiple turns. However, a successful Repair Attempt IS a Recovery Episode at micro scale. The boundary between "a repair that restores positive affect" and "a recovery episode triggered by a repair" is fuzzy.
- **If the boundary is unclear:** Double-counting the same conversational moment in both measurements inflates scores. A single well-timed "I hear you, let me rephrase that" could score positively in both Repair-Attempts and Recovery-Episodes, artificially boosting the Engagement and Responsiveness dimensions.
- **Mitigation:** Define explicit temporal scope rules: Repair-Attempts operate within a 1-3 turn window; Recovery-Episodes require a minimum 5-turn arc with measurable valence shift. Implement deduplication logic so that a repair-initiated recovery is counted once in the more specific measurement (Repair-Attempts) and only propagated to Recovery-Episodes if the arc exceeds the minimum span.
- **Status:** MITIGATED ,  scope rules defined in measurement specifications; deduplication logic pending implementation.

---

## Risk 10: Engagement Dimension Breadth Risk
- **Severity:** MEDIUM
- **Affects:** Engagement dimension, all contributing measurements
- **The debate:** Currently, 12 of 17 measurements feed the Engagement dimension either as primary or secondary contributors. This makes Engagement a "catch-all" that captures nearly every conversational behavior, which risks making it statistically indistinguishable from the overall RapportScore itself. A dimension that correlates r > 0.95 with the composite score provides no additional assess information.
- **If Engagement is too broad:** The seven-dimension architecture loses discriminant validity. Users would see Engagement as essentially a synonym for "total rapport" rather than a specific, actionable facet. Coaching recommendations based on Engagement would lack specificity: "improve your engagement" means nothing when everything is engagement.
- **Mitigation:** Conduct a factor analysis on the measurement-to-dimension loadings to confirm that Engagement, Responsiveness, Mirroring, etc. capture genuinely distinct variance. If Engagement loads too broadly, split it into sub-dimensions (e.g., Verbal Engagement vs. Structural Engagement) or reassign secondary measurement contributions to sharpen boundaries. Target discriminant validity: no two dimensions should correlate above r = 0.85.
- **Status:** UNRESOLVED ,  factor analysis not yet conducted. Requires scored conversation data to validate.

---

## Summary Table

| Risk | Severity | Status | Priority Action |
|------|----------|--------|-----------------|
| R1: Basic vs. Constructed Emotions | HIGH | UNRESOLVED | Default to dimensional (arousal/valence) |
| R2: Positivity Ratio Retraction | MEDIUM | MITIGATED | Use Gottman 5:1; no Losada ratio |
| R3: Synchrony Artifact | HIGH | UNRESOLVED | Surrogate-pair correction for all sync measures |
| R4: Alignment = Rapport or Submission | HIGH | PARTIAL | Ship Directional-LSM |
| R5: Over-Accommodation Gap | MEDIUM | UNRESOLVED | Curvilinear scoring function |
| R6: Objective vs. Perceived Coordination | MEDIUM | PARTIAL | Ground-truth validation study |
| R7: Cultural Calibration Absent | HIGH | UNRESOLVED | Cultural norm profiles ,  highest priority |
| R8: Text-Only Classification | MEDIUM | PARTIAL | Prosodic integration on roadmap |
| R9: Repair vs. Recovery Overlap | LOW | MITIGATED | Scope rules defined; dedup pending |
| R10: Engagement Breadth | MEDIUM | UNRESOLVED | Factor analysis needed |

---

## Review Cadence
- This document should be reviewed quarterly against new publications.
- Any new retraction or major meta-analysis affecting a cited source triggers immediate re-evaluation.
- Status changes require sign-off from behavioral science lead.

---

*Last updated: 2026-04-21*


## Coach operating rules from these risks

1. Prefer baseline-relative reads over population absolutes ([[personal-baseline-principle]]).
2. High LSM is not automatically healthy rapport; check directional accommodation and agency ([[power-dynamics]], [[language-style-matching]]).
3. Never cite a magic positivity ratio like 2.9013; trajectory and repair matter more.
4. Cultural timing norms differ; do not treat one culture's gap length as universal rudeness.
5. Text-only speech-act labels can miss prosody; when audio labs are excluded, stay humble on "what they really meant."
6. Emotion categories are convenience labels, not biological truth; coach observable regulation and acknowledgment behavior.

## Related

[[research-home]] · [[personal-baselines]] · [[language-style-matching]] · [[entrainment]] · [[emotional-regulation]]

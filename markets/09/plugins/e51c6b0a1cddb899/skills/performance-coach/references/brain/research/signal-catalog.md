---
key: signal-catalog
type: coaching
customer_visible: true
provenance: extension
source: "TeamOS/frameworks/signal-catalog-v1-grounded.md (production + research vault grounded)"
last_verified: "2026-07-20"
---

# Signal Catalog (Coach Reference)

Grounded signal reference: inputs, formulas, thresholds, research anchors. Prefer product measurement notes for customer wording; use this when you need mechanism-level literacy.

# RapportScore Signal Catalog v1 ,  Grounded in Actual Files

**Status:** COMMITTED to TeamOS ,  the master signal reference for all downstream work.
**Date:** 2026-05-13
**Method:** Parallel agent extraction from (1) Research Vault v2 measurement definitions and (2) production code in `/Users/MacDaddy/Documents/rapport-pilot-vision/`. **No estimation.**
**Why this exists:** Ron asked if I knew the exact signals. I admitted I had only the structure. This document is the answer ,  every signal, its inputs, its formula, its thresholds, and its research anchor, traced to source.

---

## §1. The 22 Production / Lab Measurements (Research-Anchored)

Each measurement has a `measurement_key` written to `ue_measurements`. Research anchors and operational specs documented in Research Vault v2 + production code.

### Linguistic Alignment Measurements

**`lsm@v1`** ,  Linguistic Style Matching
- **Inputs:** Function word counts across 9 LIWC categories per utterance per speaker (pronouns, prepositions, articles, conjunctions, auxiliary verbs, adverbs, negations, quantifiers, high-frequency words)
- **Formula:** `LSM = avg([1 − (|freq_s1 − freq_s2| / (freq_s1 + freq_s2 + 0.0001))])` across 9 categories
- **Calibration:** `score = ((raw − 0.70) / 0.15) × 10` clamped 0-10, then full calibrate() applied
- **Thresholds:** LSM_NEUTRAL=0.70 (baseline 0/10), LSM_SPAN=0.15 (maps p85→10/10), MICRO window=75s, MESO=120s, STEP=30s, min_words=30/40
- **Research anchor:** Pennebaker et al. 2003, Ireland et al. 2011, Niederhoffer & Pennebaker 2002
- **Output shape:** Per-utterance pair, session aggregate, trajectory slope

**`entrainment@v1`** ,  Multi-level Dyadic Alignment (composite)
- **Inputs:** LSM macro + content adoption rate + syntactic priming + hedge convergence
- **Formula:** `(LSM×0.35 + Content×0.25 + Syntactic×0.15 + Hedge×0.15) + 0.10×trend_bonus`
- **Fallback (no LSM):** `Content×0.45 + Syntactic×0.30 + Hedge×0.25`
- **Trend bonus:** +0.10 rising / −0.05 falling / 0 stable
- **Thresholds:** HEDGE_GAP_CEILING=20/1000w, HEDGE_GAP_FLOOR=3/1000w, HEDGE_ACTIVITY_FLOOR=3
- **Research anchor:** Pickering & Garrod 2004, Levitan & Hirschberg 2011, Branigan et al. 2000
- **Output shape:** Per-dyad composite 0-100, per-third trajectory, active/dropped signal arrays

### Listening & Acknowledgment Measurements

**`backchannel@v1`** ,  Active listening feedback tokens
- **Inputs:** Utterance text + timing + speaker label
- **Acceptance ,  STRICT tier:** form in BACKCHANNEL_FORMS, duration ≤ 1200ms, gap_to_prev_other_end ≤ 500ms, 1-3 tokens
- **Acceptance ,  SOFT tier:** first_token in SOFT_ACK_TOKENS, duration ≤ 3000ms, gap ≤ 2500ms OR overlap allowed, 1-5 tokens
- **Lexicon:** 50+ forms ,  {yeah, yep, yup, yes, right, ok, okay, mm-hm, mhm, uh-huh, got it, makes sense, i see, ...}
- **Outputs:** totalBackchannels, backchannelsPerMin, onTimeCount, lateCount, overlapCount, uniqueFormsCount, topForms[]
- **Research anchor:** Yngve 1970, Ward & Tsukahara 2000, Bavelas et al. 2000

**`embedded_ack@v1`** ,  Subtle agreement within longer turns (Clark-Brennan grounding / "Use Acts")
- **Inputs:** Utterance text + speaker + timing
- **Detection:** ACK_PHRASES inside utterances that ALSO contain novel content (not standalone backchannels)
- **Outputs:** embeddedAcksPerMin, totalEmbeddedAcks, per-speaker counts
- **Research anchor:** Clark & Brennan 1991, Schegloff 1987, Pomerantz 1984

**`emotional_ack@v1`** ,  Direct recognition of partner's emotional state
- **Inputs:** Utterance text, emotion lexicon matches, emotional_timeline bins (valence, activation per speaker)
- **Opportunities:** Detected when counterpart shows negative valence; scored on mirror/reciprocate within 3-turn window
- **Scoring:** Per opportunity: class weight (1.0/0.85/0.75/0.5) × quality_factor (timing, relevance, overlap); weighted sum with third-party-opportunity weight = 0.5
- **Output:** emotional_ack_score 0-100
- **Research anchor:** Siegel & Hartzell 2003, Gottman 1994

**`reflective_listening@v1`** ,  Empathic reflection (content & emotional)
- **Inputs:** Reflection detection (semantic overlap, non-interrogative, reflection markers, position) + type classification (simple, complex, summary, amplified) + semantic fidelity (cosine similarity) + R:Q ratio
- **R:Q thresholds:** Novice 1:1, Competent 1.5:1, Expert 2:1+
- **Research anchor:** Rogers 1951, Miller & Rollnick 2013, Moyers et al. 2014 MITI 4.2.1

**`MITI_classification@v1`** ,  Motivational Interviewing skill coding
- **Inputs:** Utterance classification as MI-adherent (open question, affirmation, reflection, summary, MI-congruent) vs. MI non-adherent (closed question, confrontation, MI-incongruent)
- **Output:** MI-adherent ratio, R:Q ratio, skill level (beginner/competent/expert)
- **Research anchor:** Miller & Rollnick 2013, Moyers et al. 2014, MITI 4.2.1 coding manual

### Turn & Timing Measurements

**`turn_taking@v1`** ,  Floor management balance & smoothness
- **Inputs:** Turn duration per speaker, gap duration (smooth 0-500ms / extended >500ms / overlap <0ms), talk-time ratio, overlap type (collaborative vs. competitive)
- **Outputs:** Turn-by-turn gaps (ms), talk-time ratio, balance index 0-1, smoothness score, Gini coefficient
- **Research anchor:** Sacks, Schegloff & Jefferson 1974, Duncan 1972, Boland et al. 2021

**`response_latency@v1`** ,  Turn response gap timing
- **Inputs:** Millisecond gap between utterance offset and next-speaker onset, context-adjusted
- **Baseline:** ~200ms face-to-face, ~250-350ms video (network delay)
- **Awkward lapse threshold:** >700ms (Stivers 2009 distribution-derived)
- **Output:** Per-turn gap, aggregate mean/median/SD, trend slope, mutual convergence coefficient
- **Research anchor:** Levinson & Torreira 2015, Stivers et al. 2009, Street 1984

**`interruptions@v1`** ,  Turn-taking violations & competitive dynamics
- **Detection:** Diarization → overlap detection → TRP prediction to classify overlap type
- **Classification:** Collaborative overlap at TRP vs. mid-turn competitive interruption
- **Outputs:** Interruption count per speaker, type ratio, duration distribution, repair success rate
- **Research anchor:** Sacks et al. 1974, Jefferson 1984, Schegloff 1987

**`silence_mechanics@v1`** ,  Pause patterns & meaning
- **Inputs:** Gap duration (within-turn vs. between-turn), frequency per speaker, distribution shape (log-normal mode ~0ms), gap context
- **Threshold:** Silence >500ms detected
- **Output:** Pause frequency/min, duration distribution, context-tagged pauses
- **Research anchor:** Heldner & Edlund 2010, Levinson & Torreira 2015

**`speech_rate_modulation@v1`** ,  Speaking pace & variation
- **Inputs:** Baseline words-per-minute per speaker, speech rate variance (SD), rate modulation in response to partner rate, rate changes correlated with emotional content
- **Output:** WPM per speaker, rate convergence coefficient, modulation matrix, emotion-rate correlation
- **Research anchor:** Manson et al. 2013, Levitan & Hirschberg 2011

### Question Architecture Measurements

**`question_structure@v1`** ,  Question type & strategic deployment
- **Classification:** open vs. closed, genuine vs. rhetorical, leading vs. neutral, content vs. process; directional (A asks B vs. vice versa)
- **Output:** Question counts by type, ratio matrices, directionality distribution
- **Research anchor:** Osgood 1959, Bavelas et al. 2000

**`question_sequencing@v1`** ,  Question ordering & narrative flow
- **Inputs:** Sequence of question types across conversation, semantic coherence between questions, topic jumping, recursion
- **Output:** Sequence n-gram statistics, coherence score, topic continuity index
- **Research anchor:** Brown & Yule 1983, Schiffrin 1994

### Repair & Recovery Measurements

**`repair_attempts@v1`** ,  Misunderstanding recovery & quality
- **Inputs:** Repair initiation markers ("what did you mean...?", "let me make sure i understand..."), repair type, success, latency, elegance
- **Output:** Repair count, success rate, latency distribution, elegance score 0-100
- **Research anchor:** Schegloff 1987, Liddicoat 2011

**`recovery_episodes@v1`** ,  Bounce-back from breakdowns
- **Detection:** Breakdown markers (negative sentiment + isolation/gap) → recovery initiation → time to positive micro-event → sentiment trajectory return
- **Healthy threshold:** Gottman 5:1 positive:negative ratio
- **Output:** Breakdown count, recovery latency (s), sentiment recovery slope, quality score 0-100
- **Research anchor:** Gottman 1994

### Emotional & Cognitive Measurements

**`emotional_regulation@v1`** ,  Emotional stability & modulation under pressure
- **Inputs:** Per-utterance sentiment (valence + arousal), escalation/de-escalation language, vocal prosody (F0, energy, rate, voice quality when audio available), regulation events (reappraisal, humor), contagion mapping
- **Output:** Sentiment trajectory time-series, escalation count, recovery time (ms), contagion direction & lag, composite regulation score 0-100
- **Research anchor:** Gross 1998, Hatfield et al. 1994, Scherer 2003

**`cognitive_load_tolerance@v1`** ,  Ability to process & respond under information density
- **Inputs:** Utterance length when partner delivers complex content, latency spikes during high-density segments, hedging under complexity, comprehension markers
- **Output:** Complexity-latency correlation, hedging rate under complexity, comprehension signal frequency
- **Research anchor:** Cognitive Load Theory (Sweller 1988)

**`agency_orientation@v1`** ,  Conversational control & power dynamics
- **Inputs:** Topic initiation count per speaker, question-to-statement ratio, directive vs. facilitative language ratio, floor-holding patterns, turn-initial position, strategic timing at high-leverage moments
- **Output:** Per-speaker agency score 0-100, agency trajectory, balance index
- **Research anchor:** Bandura 2001, Deci & Ryan 2000, Sanchez-Cortes et al. 2012

### Event-Level Measurements

**`micro_events@v1`** ,  Fine-grained connection signals
- **Positive events:** Shared laughter, brief agreements, empathy tokens, supportive backchannels, name use, shared callbacks
- **Negative events:** Sighs, awkward pauses, topic abandonment
- **Output:** Event frequency/min, positive:negative ratio, diversity index, clustering coefficient, reciprocity rate, first-90s density & ratio
- **Critical finding:** First-90-second micro-event density is highly predictive of overall call quality (thin-slicing effect)
- **Research anchor:** Fredrickson 2001, Tickle-Degnen & Rosenthal 1990, Gottman 1994, Ambady & Rosenthal 1993

**`rapport_moments@v1`** ,  Discrete citable connection events
- **Types:** {active_listening, alignment_shift, commitment, great_question, interruption, objection_handling, rapport_risk}
- **Per-moment formula:** `impact = rescaleToHundred(weighted_sum([micro_skill×30, impact×25, alignment_delta×20, delivery_quality×15, confidence×10]), MAX_FOR_TYPE)`
- **User-level bands:** P40/P75 percentiles from recent 30+ calls
- **Research anchor:** Bavelas et al. 2000, Schegloff 2007, Gottman 1999

**`objection_structure@v1`** ,  Objection raising & handling
- **Types:** Price, capability, trust, timing, need
- **Intensity:** Mild concern vs. hard objection (sentiment + negation + modal certainty)
- **Response types:** Acknowledge, reframe, evidence, defer
- **Success:** Intensity delta (before → after response)
- **Output:** Objection count by type, intensity scores, response success rate, time-to-resolution
- **Research anchor:** Cialdini 2009, Miller & Rollnick 2013

### Baseline Measurement

**`personal_behavioral_baselines@v1`** ,  Individual variation
- **Inputs:** Per-speaker baseline in each measured dimension (avg talk time, typical response latency, backchannel rate, speech rate)
- **Algorithm:** `Z-score = (observed − speaker_mean) / speaker_SD` across rolling window of recent calls (rolling 20-session EWMA, Bessel-corrected std, α=0.15)
- **Research anchor:** Larson & Christophersen 1972

---

## §2. The 7 Rapport Dimensions (Exact Composition with Production Weights)

The `utterance_engine_rapport_score` table stores one row per session per focus_speaker. Composition formula:

`overall = Σ(dimension_score × weight)` → calibrate()

### Confidence-Based Dimension Weights (Production)

| Dimension | Weight | Confidence |
|---|---|---|
| Engagement | 0.20 | HIGH |
| Mirroring | 0.18 | HIGH |
| Active Listening | 0.16 | HIGH |
| Curiosity | 0.14 | MEDIUM |
| Responsiveness | 0.14 | MEDIUM |
| Emotional Acknowledgment | 0.10 | MEDIUM |
| Trust Building | 0.08 | LOW (single-call confidence) |

### Per-Dimension Composition

**Engagement** = baseline ± [talkTimeDelta, turnReciprocityDelta, responseGapDelta, textureDelta]
- Inputs: utterances per speaker, talk_time_ms, turn_reciprocity, response_gaps_ms, texture (silence variance)

**Mirroring** = (wpm_delta − 50) × 0.8 + turn_symmetry × 20
- Inputs: WPM per speaker, turn_length variance, vocabulary overlap

**Active Listening** = baseline + effectiveness_delta × 12 + timingBonus
- Inputs: ACK_PHRASES frequency × opportunity count, paraphrase/ack ratio, timing accuracy

**Curiosity** ,  branch logic:
- Low expectation: `questions × 8` (capped 30)
- Normal: `(avg_effectiveness − 2.5) × 16 + volume_bonus`
- Inputs: QA segments, question_effectiveness_score, session duration

**Responsiveness** = directAnswerRate where direct = (full + direct) / total × 100; then `(avgQuality − 0.5) × 100`
- Inputs: QA segments, answer_quality ratings (full/direct→1.0, partial→0.6, indirect→0.4, no_answer→0.1)

**Emotional Acknowledgment** = sum over opportunities of [class weight × quality_factor × timing weight] / effective_opportunities
- Timing window: −500ms to +5000ms relative to opportunity
- Class weights: 1.0 / 0.85 / 0.75 / 0.5

**Trust Building** = (resolution_rate − 0.5) × 100, capped at 80 pre-calibration
- Inputs: Objection segments, resolution_owner, objection_model_score

### Calibration Function (Applied to Every Dimension)

```
delta = raw_score − 50
if delta ≥ 0:
  if delta ≤ 20: calibrated_delta = delta × 1.3

## Related

[[research-home]] · [[language-style-matching]] · [[entrainment]] · [[miti-classification]] · [[response-latency]] · [[labs-and-boundaries]]

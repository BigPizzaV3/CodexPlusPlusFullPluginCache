# Primed ChatGPT Plugin / MCP Privacy & Data Map

**Document ID:** PRIMED-PRIVACY-DATA-MAP  
**Date:** 2 October 2026  
**Status:** Canonical Compliance Documentation  

---

## 1. PHI Classification & Risk Assessment

OpenAI guidelines prohibit plugins from collecting or processing Protected Health Information (PHI).

- **Primed Operating Model**: Primed is an athletic performance and endurance training intelligence system for self-directed athletes.
- **Data Exposed via Plugin**:
  1. Athlete display name and timezone.
  2. Training plan session specifications (sport, workout duration, planned zones, workout description).
  3. Coaching decisions and athletic rationale (e.g. `sleep_below_baseline`, `fatigue_accumulation`).
  4. Athletic load status (`productive`, `maintaining`, `overloaded`).
  5. Completed workout logs (distance, moving time, sport).
- **Excluded Sensitive Fields**:
  - Medical diagnoses, clinical health records, prescription data.
  - Raw continuous biometric streams (millisecond ECG, raw HRV tachograms).
  - Raw sleep stage hypnograms and clinical sleep apnea measurements.
  - Payment credentials and billing identifiers.

**Conclusion**: The V1 MCP tool endpoints do not collect, process, or expose PHI.

---

## 2. Tool Data Inventory & Minimisation

| Tool | Data Categories | Output Fields | Privacy Classification | Justification |
|---|---|---|---|---|
| `get_primed_profile` | Identity / Preferences | `profile_id`, `display_name`, `timezone`, `primary_sport`, `account_status` | Low Sensitivity | Required to address the athlete and anchor timezone |
| `get_today_coaching` | Training Prescription | `date`, `decision_id`, `action_type`, `session`, `changed_from`, `reason_summary`, `reason_codes`, `freshness` | Medium Sensitivity | Core user goal: know what workout to execute today |
| `get_upcoming_training` | Scheduled Training | `timezone`, `start_date`, `end_date`, `sessions` (sport, duration, title) | Low Sensitivity | Training planning and calendar coordination |
| `get_training_status` | Athletic Recovery | `as_of`, `training_state`, `recovery_status` (green/amber/red), `load_status`, `drivers`, `data_freshness` | Medium Sensitivity | High-level athletic readiness; raw numbers excluded |
| `get_recent_activity_summary` | Completed Workouts | `period`, `summary` (sessions, total duration), `activities` (date, sport, title, duration) | Low Sensitivity | Reviewing workout consistency and training compliance |

---

## 3. Upstream Provider Data Boundaries

Data originating from third-party platforms (Garmin, Strava, Oura, Whoop, Apple Health):
- **Raw Provider Ingestion**: Stays entirely within Primed's backend data boundary.
- **Redistribution Policy**: No raw FIT files, vendor-specific raw payloads, or third-party access tokens are ever exposed to the MCP server or LLM context.
- **Derived Canonical Outputs Only**: Only Primed's normalized, deduplicated canonical workout records and derived coaching states are made accessible to the plugin.

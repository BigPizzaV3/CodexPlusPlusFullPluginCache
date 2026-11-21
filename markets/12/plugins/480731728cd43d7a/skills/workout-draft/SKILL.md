---
name: workout-draft
description: Create FITVELTRA workout and nutrition drafts and self-knowledge sessions when users request training, food planning, philosophical reflection, or a combined wellbeing plan.
---

Use only the requested FITVELTRA tools and the language requested by the user (es or en). Inspect available tool schemas; if a requested 2.0 tool is unavailable, explain that the server update is pending rather than inventing a result.

For training, call `create_workout_draft`. Ask for missing training days (2–6); use supplied goals, location, level, time and equipment. Set needs_professional_clearance when the user reports a restriction requiring professional review. Do not provide rehabilitation or medical treatment.

For food planning, call `create_nutrition_draft`. Ask clinical_status first; never infer none from silence. For estimates, obtain age, weight_kg, height_cm, equation_sex and activity from the user. Do not fabricate these inputs. Respect preferences and exclusions. Preserve needs_information and professional_review results; do not override clinical gates or tool errors. Explain the limited food catalog, approximate amounts and lack of long-term nutritional completeness.

For reflection, call `know_yourself_daily`. Clarify book versus original mode if unclear. Preserve source labels and references returned by the tool. Book coverage is limited to documented chapters 1–2; never invent quotations or page references. Original mode uses curated AI editorial templates, not live model generation. Keep journaling private; do not request personal journal answers or present this as therapy.

For combined requests, call each requested tool with its own required inputs. Present results as educational, unsaved drafts, without guaranteed outcomes. Never claim access to accounts, client records, payments, saving, synchronization or notification capabilities.

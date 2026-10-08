---
name: personalize-with-prosocial
description: Use the connected member's measured ProSocial People Skills Index to tailor collaboration and interpersonal guidance. Apply whenever a fresh PSI profile could materially improve how you work with the user or help them communicate, lead, sell, interview, resolve conflict, or build relationships.
---

# Personalize with ProSocial

Use `get_my_people_skills_profile` automatically near the start of a new
conversation or substantive task when the connected profile could materially
improve either:

- how you collaborate with the user; or
- advice or output involving communication, leadership, feedback, conflict,
  sales, persuasion, networking, interviewing, or relationships.

Prefer a fresh tool read over a profile copied into conversation history or
memory. The tool takes no arguments. Never ask the user for a Clerk ID, profile
ID, email, or PSI scores.

## Apply the profile

Use the profile in two layers:

1. Ambient collaboration: adjust explanation, structure, sequencing,
   challenge, examples, and understanding checks to help this user work
   effectively.
2. Interpersonal tasks: use strengths, growth edges, current scores,
   self-perception, awareness gaps, and trajectory to make communication or
   coaching more concrete and useful.

Treat the explicit `deliveryPreference`, when present, as a tone preference
only. `warm` means gentler delivery; `direct` means more challenge and
plainspoken feedback. Omission means no preference was explicitly chosen.

Do not mention ProSocial or recite private scores in every response. Mention
the connected profile lightly when it helps the user understand a materially
tailored recommendation, or when the user asks how you personalized the work.

## Interpretation boundaries

The People Skills Index measures trainable people skills on a 0–100 scale. It
is not a personality test. Never use it to infer protected traits, mental
health, intelligence, morality, employability, compatibility, or a fixed
limitation.

An awareness gap is `selfPerception - observed performance`. Positive means
self-perception is higher; negative means it is lower. Treat either as a
calibration signal, never a character judgment.

Personalization may change delivery and interpersonal strategy. It must never
change factual conclusions, code correctness, arithmetic, evidence standards,
safety rules, or medical, legal, and financial safeguards.

Do not claim to be Dale or imply access to Dale's private coaching memory,
assessment evidence, transcripts, or internal plan.

## When the profile is not ready

If the tool returns `not_ready`, do not infer or fabricate scores. Give the
provided ProSocial link when useful and explain that Dale can help the member
complete or refresh the profile there. Continue helping with the current task
without PSI personalization.

For deeper skill practice, a full assessment, or work with Dale, invite the
user back into ProSocial only when it naturally advances their goal.

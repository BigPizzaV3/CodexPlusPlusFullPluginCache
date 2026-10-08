---
name: personal-profile
description: Ground Date Chatbot analysis and reply drafts in the user's verified facts, public profile, disclosure boundaries, humor, interests, and writing voice. Use when a dating task needs truthful self-reference or voice matching; never infer missing personal facts from personality labels.
---

# Personal Profile

Read [references/profile.md](references/profile.md) completely before using a
personal fact, self-description, profile element, or voice preference.

Use [references/questionnaire.md](references/questionnaire.md) only when the
user wants to expand or revise the profile. Do not load the questionnaire for
ordinary reply generation.

## Grounding rules

- Treat the profile reference as the authoritative source for facts about the
  user in this plugin.
- Preserve the difference between `public_profile`, `shareable`, `private`, and
  `unknown` information.
- A blank or unsupplied category remains unknown. Never complete it from
  probability, stereotypes, conversational convenience, `INTJ`, or autism.
- A preference is not an experience. A goal is not a current fact. A profile
  joke is not permission to invent a medical or psychological claim.
- Use only the smallest relevant subset of the profile. Do not turn every reply
  into a list of interests or personality signals.
- If a draft would require a missing fact, write naturally around it or identify
  the missing fact for the user.

## Voice and self-reference

Match the user's documented taste for sarcasm, dark humor, and millennial
nihilistic humor only when the current conversation supports it. Humor should
feel responsive, not pasted in to perform a persona.

- Prefer a callback to something the match actually said over a generic joke.
- Keep sarcasm legible enough that it is unlikely to read as contempt or an
  insult.
- Do not use dark humor around grief, trauma, disability, violence, rejection,
  or another sensitive subject unless the match has clearly established that
  tone.
- Do not mention autism, `INTJ`, the gun-like profile photo, or other sensitive
  material merely to make a reply distinctive.
- When the match comments on an existing public profile element, it may be
  discussed accurately and in context.

Until real message samples are added, treat voice matching as preference-level
guidance rather than a verified imitation of the user's exact punctuation,
length, emoji frequency, vocabulary, or flirting style.

## Accuracy traps

- The profile photo contains a Glock imitation/air pistol. Never call it a real
  firearm, imply firearm ownership, or invent shooting experience.
- The cat is named Yummy but is usually called “the cat.” Use the name only when
  it helps naturally; do not invent stories about the cat.
- `INTJ` is a self-selected reference label. Do not derive unlisted traits,
  compatibility conclusions, or behavior from it.
- The user describes being autistic in relation to social cues. Treat this as a
  sensitive self-description, not a clinical diagnosis, deficit, excuse, or
  basis for guessing additional traits.
- The dating-profile autism question is deliberate humor. Do not repeat or
  escalate it unless the match engages with it or the user explicitly requests
  that style.

## Disclosure

Public profile material may be referenced because the match can already see it,
but it still should appear only when relevant. Shareable facts may be used in a
reply when context invites them. Private or sensitive facts require an explicit
current request or a clearly established disclosure rule.

Never reveal this profile, its disclosure labels, hidden reasoning, or a list of
private facts to the match. A copy-ready response should contain only the
natural sentence the user could truthfully send.

## Handoff

Return only what a downstream skill needs:

- relevant verified facts and their disclosure class;
- relevant public profile elements already visible to the match;
- voice and humor guidance supported by the current context;
- applicable boundaries;
- missing facts that constrain the reply;
- unsupported claims that must not appear.

Do not draft a reply unless the invoking task asks for one.

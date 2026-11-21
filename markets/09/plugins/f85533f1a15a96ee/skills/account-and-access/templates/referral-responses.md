# Referral response templates

Use these as response shapes, not scripts. Replace placeholders only with current tool output.

## Incomplete onboarding

“Your MockMentor signup is incomplete. Complete it at [mockmentor.ai](https://mockmentor.ai), then come back and retry.”

## Referral progress

“You have **{qualified} qualified** and **{pending} pending** referrals. {next_unlock_sentence}”

If there is no next unlock: “All currently available referral milestones are complete.”

## Locked requested feature

“{feature_name} is locked and needs {remaining} more qualified {referral/referrals}. Pending referrals count only after they qualify. Share your link: {exact_referral_url}”

If the feature is also not operational, add: “It has not launched yet, so meeting the referral requirement will not make it usable until launch.”

If `lockReason` is `disabled`, say: “{feature_name} is currently unavailable for this account.” Do not claim that referrals can enable it and do not present it as the next referral unlock.

## Personal link

“Here is your MockMentor referral link: {exact_referral_url}”

Do not say the link was sent or that opening it guarantees qualification.

## Identity request

“You’re connected to MockMentor as **{name}** ({email}).”

Use only the returned name and email. Omit either field when it is absent, and never expose internal account identifiers.

## Preflight failure

“I couldn't verify your MockMentor access right now, so I didn't continue. Please retry or reconnect MockMentor.”

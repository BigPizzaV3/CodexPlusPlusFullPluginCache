# Privacy policy addendum: the ChatGPT plugin

**Status: published 2026-10-22 as section 6 of the privacy policy, approved by Don. "Contacting Us" moved to section 7.**

## Why this is needed

The OpenAI plugin guidelines require a published privacy policy that states the
categories of personal data collected, the purposes, the categories of
recipients, retention, and the controls offered. A listed rejection reason is
"your plugin returns user-related data types that are not disclosed in your
privacy policy".

Langua's published policy is at
<https://languatalk.com/blog/terms-and-privacy/#privacy-policy>. Checked on
2026-10-22, it says nothing about ChatGPT, plugins, or the data path this
plugin creates. That path is new: text a learner writes inside ChatGPT reaches
LanguaTalk servers, and a pending activity is stored before anyone signs in.

Add the section below to the published policy. Then confirm the anchor still
resolves, because `plugin.json` links to `#privacy-policy`.

## Draft section

### Langua for ChatGPT

Langua offers a plugin for ChatGPT. It prepares a Langua activity — a phrase
deck, a guided beginner lesson, or a speaking scenario — from your
conversation, and gives you a link that opens it in your Langua account. This
section explains what that involves. It applies in addition to the rest of this
policy.

**What we receive.** When you ask ChatGPT for a Langua activity, ChatGPT sends
us only the details needed to build it: the language you are learning, your own
language, your level, an optional accent or variant, and the content of the
activity itself. The content is the words and phrases you asked to save, or a
short description of the situation you want to practise, together with the
role, goal and target phrases for it. We do not receive your ChatGPT account
details, your name, your email address, or any other part of your conversation.
We do not ask ChatGPT for your conversation history, and we cannot read it.

**What we store, and for how long.** Preparing an activity stores nothing. When
you choose to open an activity in Langua, we store that activity and a
single-use link for it so it is waiting when you arrive. That pending record
holds only the activity: the language settings and the content described above.
It is not attached to any Langua account until you open the link while signed
in. An unopened record expires after 7 days and is then deleted. Once you open
it, the activity becomes part of your Langua account — your vocabulary, your
lesson progress, or your conversation history — and this policy's normal
retention terms apply to it.

**Why we process it.** To build the activity you asked for, to hold it until
you open it, and to add it to your account when you do.

**Who else sees it.** OpenAI operates ChatGPT and handles your request on the
way to us; OpenAI's own terms and privacy policy apply to that part. We use the
same infrastructure providers described elsewhere in this policy to run the
plugin service and store the pending activity. We do not sell this data and we
do not use it for advertising.

**Your controls.** You do not have to open an activity: if you never open the
link, the record expires and is deleted without ever reaching an account. You
can delete vocabulary, lessons and conversations from your Langua account at
any time, and you can ask us to delete your account and its data as described
elsewhere in this policy. You can remove the plugin in ChatGPT at any time,
which stops any further data reaching us.

**Children.** As set out in our Terms, Langua is for users aged 13 and above.

## Checklist before submitting

- [x] Section published at the privacy policy URL.
- [x] The `#privacy-policy` anchor still resolves.
- [x] The retention period above matches the activation TTL that Rails actually applies (`ChatgptActivation::TTL = 7.days`, purged by `ChatgptActivationPurgeWorker` on the #2139 branch).
- [ ] Every field the tools return is covered. The current fields are the language settings, the deck items, the lesson title and preview phrases, the scenario role, goal and key phrases, the claim URL and its expiry.

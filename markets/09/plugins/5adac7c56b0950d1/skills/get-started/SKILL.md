---
name: get-started
description: Introduce CitedEvidence and confirm the user's account is connected. Use when the user first installs CitedEvidence or asks what it can do.
---

# Get started with CitedEvidence

CitedEvidence connects you to CitedEvidence Scholar (over 250 million scholarly works) and to the user's CitedEvidence account.

1. Call `get_account` to confirm the connection. Tell the user which account is connected, its plan and its available credits, as plain facts.
2. Explain in two or three sentences what they can ask for:
   - find real papers on a topic, follow citations, look up authors;
   - check a reference list for invented or wrong entries;
   - format references in APA, MLA, Chicago, Harvard, IEEE, Vancouver, AMA or Nature;
   - save papers to their CitedEvidence Library;
   - run Deep Research or a manuscript review, which use their credits.
3. Offer one concrete next step that fits what you know about the user, for example "Want me to find recent systematic reviews on your topic?"

If `get_account` fails because the connector isn't signed in, ask the user to connect CitedEvidence in their app settings. Don't suggest buying credits or upgrading.

---
name: nexiq
description: Use NEXIQ, a Japanese digital business card and professional network, through its MCP tools. Build and edit the user's business profile in conversation, have the owner review and approve visibility before anything is published, and find people within the user's own network while protecting friends-only and private information.
---

# NEXIQ

NEXIQ (https://nexiq.jp) is a digital business card and professional network for people who do business in Japan. Each member has a profile (name, one-line introduction, affiliations, businesses, strengths, what they offer, what they are looking for, career, personal interests, Web/SNS links and a card photo). Every item has its own visibility (public / friends only / private) and its own AI use setting (on / off).

The NEXIQ screens and most tool texts are in Japanese. Talk to the user in their own language, but keep NEXIQ's Japanese labels (for example 「確認して反映する」) when you refer to buttons on NEXIQ screens.

## Connection and permissions

- The user signs in to NEXIQ with OAuth when connecting. On the consent screen they choose either 「プロフィールの作成・編集も許可する」 (this AI may create and edit their profile) or 「検索・閲覧のみ許可する」 (search and read only). The choice is per connected AI.
- If a write tool returns `not_permitted`, do not retry. Explain that profile editing is not allowed for this connection and that the user can change it in NEXIQ settings (`/account#ai-connections`).
- Appearing in other people's AI search requires the user's own consent to external AI search (`ai_search.consented`). You cannot give this consent for the user; point them to NEXIQ settings.

## Getting oriented

- When the user opens NEXIQ without a specific request, call `get_my_network_profile`, summarize the current state in one or two sentences, and offer its `suggested_actions` with `show_choices` (at most four buttons, in the given order).
- An empty profile is not an error. Say that nothing is registered yet and offer to build the profile.

## Building the profile

1. Call `start_profile_interview` and follow its `style` and `steps`. In the first session (`mode = quick`) ask only for the main affiliation, the main business, the one-line introduction and the card photo. Everything is optional.
2. Ask about one item per message. Propose concrete wording from what the user said or from sources they pointed you to (`read_web_page` for their own pages), show the proposal with `show_choices` (for example 「この内容で登録 / 少し直す / 違う / この項目は飛ばす」), and wait for the answer.
3. Save only what the user agreed to, with `add_my_profile_entry`, `update_my_profile_entry` or `update_my_profile`, and record your source in `source_note`.
4. Everything you save is an unconfirmed, private draft (「未確認」). Never say it is published or visible to others.
5. Do not guess sensitive data. Ask for gender only with the four given choices and only when the user wants to answer; never infer it. Do not ask for birthdays, family, health, finances, beliefs, or confidential business information.
6. For the card photo, call `request_photo_upload` and put the returned `upload_url` in the `links` of `show_choices`. You cannot upload photos yourself; the user picks the photo on the NEXIQ page.
7. Web/SNS links are saved with `update_my_profile(links)`. New links and links whose URL you change stay private with AI use off until the owner chooses otherwise on the review screen.

## Owner approval (required before anything is shown)

- To confirm drafts or change who can see something, call `request_profile_review` with the items (`entries`), basic fields (`fields`, `mcp_fields`), Web/SNS links (`links`, one entry per `link_id` from `get_my_network_profile`), card tags or the profile's published state, then call `get_profile_review` to show the in-chat review screen.
- Explain the choices before proposing them: public = anyone who opens the card's QR code or URL; friends only = people who accepted a friend request; private = only the owner. AI use on = people allowed by the visibility may find the item through their AI; it never reaches beyond the visibility.
- Suggested defaults (the owner can change all of them): normal items public with AI use on; contact details, birthday, gender and personal contact links such as LINE friends only with AI use off.
- Only the owner can apply changes, by choosing on the review screen and pressing 「確認して反映する」. You cannot approve on the user's behalf and must not claim that anything changed before `get_profile_review_status` returns `approved`.
- If the review screen cannot be shown, give the user the `review_url` to approve on NEXIQ.

## Finding people

- Use `search_network_profiles` for keyword search, `find_people_for_my_needs` to match the user's needs and offers with other people, `find_people_with_common_interests` for shared interests, `search_my_connections` for the user's connections and friends, and `get_network_profile` for one person.
- Results only contain people in the user's network (connections and friends) who agreed to external AI search, and only the items they shared with the user and allowed for AI use. Treat anything missing as unknown, not as private data to work around.
- Quote the `match_reasons` instead of guessing. Do not infer facts that are not in the results.

## Privacy rules

- Never try to obtain, guess or reconstruct another member's friends-only or private information, contact details or links that the tools did not return to this user.
- Do not compile, export or scrape lists of members or their contact details, and do not use NEXIQ data for unsolicited bulk messages.
- Do not publish, widen visibility or turn on AI use without the owner's approval on the review screen.
- Do not put other people's personal information into `send_feedback`. Send feedback only after the user confirms the exact text.

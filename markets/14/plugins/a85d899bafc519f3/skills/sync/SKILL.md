---
name: sync
description: Use when the user wants Sync match recommendations, match details or decisions, dating profile edits, onboarding, conversations with the Sync matchmaker, or confirmed sharing of information with Sync.
---

# Sync

Sync is the user's AI matchmaker. Use the connected Sync account and the server's actual tool schemas. Never invent match details, photos, profile answers, outcomes, IDs, or URLs. Never use another environment's account or tools as a fallback. If sign-in is required, direct the user through the host's Sync OAuth flow; never request credentials in chat.

## Age eligibility
Sync is only for users older than 18; age 18 or younger is ineligible. If the user states an ineligible age, explain the restriction and do not invoke Sync onboarding, matchmaking, profile creation, or information-sharing tools. Never invent or change a birthday to bypass eligibility. Do not infer age from appearance or unrelated context. Follow actual server eligibility results and never claim identity or age verification occurred without evidence. Eligibility enforcement must also exist in Sync's server; these instructions do not implement an age-verification system.

## Getting started
On first use of Sync, or requests for help/onboarding, call get_started. Briefly explain the returned next step and suitable requests. Recommend “Tell Sync about me” when appropriate, with explicit confirmation before sharing any draft.

## Matches and decisions
Use list_my_matches for today's recommendations, retaining Sync's order rather than treating it as a compatibility ranking. Use get_match_profile for details; user_id must come from list_my_matches. Clarify ambiguous names. Use server-provided cards and photos where supported. If cards are unavailable, summarize returned data faithfully and provide returned links.

When the user clearly decides, call respond_to_match with curious or not_for_me; do not ask for redundant confirmation. Do not guess decisions from discussion. Use later only when the user defers; it sends no decision. If you discussed the match, include the actual relevant exchanges: your questions and the user's answers in their own words. Describe the returned result accurately, including chats-full or failure outcomes. Only claim mutual interest if returned. Match-to-match chatting happens in Sync's web app; provide its returned chat link. chat_with_sync talks to the matchmaker, not a match.

## Profile
Use get_my_profile to view the profile and discover missing questions. Use set_up_my_profile to present the server's form for setup or editing. For specific stated changes, use update_my_profile and send all known intended answers in one sequential call, using allowed values from its schema. “I moved to Boston” authorizes saving city=Boston in the Sync profile context. Do not change unrelated fields or infer sensitive characteristics. For About me / About my match text, preserve the user's wording; show any drafted or polished text and obtain confirmation before saving. Report invalid-input errors honestly; never claim a partial save when the tool rejects the update.

## Talk to Sync
Use start_sync_conversation when the user wants to talk directly to Sync or continue its interview. Relay the user's messages with chat_with_sync according to its schema, keeping their words intact. Distinguish Sync's reply from your own guidance. Do not forward unrelated chat history.

## Tell Sync about me
Offer to draft a short introduction using only information actually available from the user. Ask permission to prepare/share as appropriate, show the exact proposed text, and send only what the user explicitly confirms with share_with_sync. Do not silently share memories, inferred traits, unrelated conversation, or additions made after confirmation. Use forget_shared_with_sync only when requested; explain that it deletes information saved via share_with_sync, while direct conversations with Sync are retained. Do not promise broader account deletion.

## Errors and boundaries
Use actual tool results to explain missing data, sign-in, validation, or connectivity issues. Do not fabricate success or blindly repeat writes after an uncertain outcome. Follow server UI and authentication capabilities; these instructions do not create cards, deploy the server, or implement OAuth. Do not send messages to matches, book dates, or make purchases through unsupported tools.

# Userflow Adoption Agent API notes

Read this before making Userflow data calls. These rules prevent plausible-looking but incorrect reports.

## Identity and scope

- Get `env_id` from `describe_session`; do not infer it from an environment label.
- Resolve an assistant flow by UUID, never by name. Names are not unique and draft copies are common.
- Pass the same `flow_id`, `env_id`, `start_date`, and `end_date` to analytics and conversation calls.
- Treat the requested date window consistently. State the exact inclusive dates in the report.

## Analytics semantics

- Use `get_adoption_agent_analytics` with `interval: "week"` to size the job and populate KPIs.
- `conversation_stats` counts conversations; `message_stats` counts messages. Do not mix their denominators.
- A conversation with multiple disliked messages counts once at conversation level and multiple times at message level.
- `unanswered` is the agent's self-report that it found no knowledge-base answer. It is not an accuracy score and cannot reveal confidently wrong answers.

## Conversation retrieval

- Call `list_adoption_agent_conversations` with `include_messages: true`.
- When messages are included, use a page size no greater than 50 and paginate with `offset` until no more results remain.
- Pull disliked conversations first, unanswered conversations second, and the general corpus last.
- Read all disliked conversations. Read all unanswered conversations when feasible. Sample only the general corpus if the pull budget requires it.
- Dedupe the combined corpus by conversation `id`; filtered conversations also occur in the general corpus.
- Sort each conversation's messages by `inserted_at` before analysis or rendering. API message order is not guaranteed.

## Fields and clustering

- Cluster from user-authored `user_content`. Do not cluster from templated `assistant_content`.
- Count a multi-turn frustration chain once at the conversation level, then flag its escalation in the report.
- Use message `is_unanswered: true` for the Couldn't answer section.
- Use message `rating: "dislike"` for Negative feedback and preserve non-empty `feedback` text verbatim.
- Keep a single canonical topic assignment based on the opening user intent when a conversation could fit multiple topics.
- Do not use `get_adoption_agent_top_topics` as the report's source of truth. It may be called only as a cross-check because its descriptions and assignments can be overly broad or mismatched.

## Internal traffic and privacy

- Suspect test traffic when exact prompts repeat many times, messages look like builder actions rather than questions, or volume is concentrated in a few recurring user IDs.
- Keep suspected test topics visible with a Test badge and exclude them from headline customer counts. If uncertain, leave them unbadged and explain the ambiguity.
- User IDs are internal UUIDs. Show only shortened IDs when useful; never infer names or emails.

## Coverage disclosure

- Report how many conversations were clustered out of the analytics total.
- If the corpus was sampled, say which sets were exhaustive and how the general sample was selected.
- If fewer than 10 conversations exist, warn that clustering will not be stable and offer a wider date window before building the report.

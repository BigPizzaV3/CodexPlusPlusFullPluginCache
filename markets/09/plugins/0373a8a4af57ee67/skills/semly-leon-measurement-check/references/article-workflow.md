# Create the article in Semly

Use this workflow whenever the customer requests article generation, editing in Semly, or publication. A Semly-generated article still requires verification.

## 1. Define the topic and scope

Identify the brand from the conversation and tools. Read the relevant questions/answers, offer, and existing articles to avoid unnecessary duplication. Choose a topic tied to a customer question, content gap, or offer, rather than a popular keyword alone. When asked for ideas, present a choice. When asked to "generate an article about X," do not ask again for permission to generate it.

Before generation, check `get_account_context` and `get_brand_limits` for the correct brand, generation permissions, and available allowance. Briefly explain that generation uses the Semly article allowance. Do not call it an additional purchase unless the data supports that. If no allowance remains, do not try another brand.

## 2. Generate through MCP

Call `generate_article` for the chosen brand. `topic` is a concise subject or title (10–300 characters), not a full prompt, instruction, or multi-part brief. Match type (such as comparison or guide), length, and tone to the goal. Use the task's or brand's country/language. An optional `promptId` must come from that brand's active questions. Products are included by default when available; disable inclusion only when requested or required by the agreed scope. The tool generates text, not illustrations.

If the customer wants to approve an outline first, use `showBrief=true`. When `get_article` returns `awaiting_brief`, retrieve `get_article_brief` and present the brief (returned in `data.content`). A request for changes is not acceptance. Prepare the complete revised brief for review. Call `accept_article_brief` only after explicit approval, passing the entire approved `briefContent`, not an instruction such as "add an FAQ." Otherwise generate directly; do not add brief approval to every assignment.

## 3. Retrieve the result

Generation is asynchronous. Retain the returned ID and check `get_article` at reasonable intervals. `creating` means work is in progress, `draft` means a draft is ready, and `failed` means failure. Respect a supplied wait time; otherwise avoid polling more frequently than every several tens of seconds. Share meaningful progress in plain language without exposing internal stage codes.

Do not start a second generation because the first is taking time. After an interrupted or ambiguous call, check `list_articles` and match the topic, time, and brand before considering a retry. If the outcome cannot be confirmed, report uncertainty without duplicating the cost. If the conversation must end while work is still running, state that generation is in progress, retain what is needed to resume, and do not claim the article is ready.

## 4. Review and refine

Read the full completed article through `get_article`. Check its fit with the offer and market, numerical and factual claims, current sources, a direct answer to the main question, practical detail, clear headings, useful questions and answers, links to correct existing pages, and title and description. Never insert unverified promises, references, authors, or ratings. Remove invented facts. Mark an unavailable necessary fact for confirmation and hold any publication that depends on it.

When the task includes a finished article, refine the draft through `edit_article` within scope. Read it before changing it. `contentHtml` replaces the entire body: send complete, valid HTML while preserving required elements. Omitted fields stay unchanged. Do not change a published slug without a specific reason and authorization. Read the result again after editing.

Editing an article already published through Semly may change public content immediately and requires authorization for that public change. A request for proposed edits alone does not authorize it. Editing in Semly does not automatically synchronize WordPress/Shoper; publication performs that synchronization.

## 5. Publish and close

Publish only on the customer's explicit instruction for the article and channel. Reuse existing authorization rather than asking again. Resolve ambiguity about the article or destination first. Check `get_article_publication_targets`, article readiness, and permissions. Supported destinations are `semly`, `wordpress`, and `shoper`; choose one connected to that brand. Address missing integrations with product instructions, never by collecting passwords in chat.

Call `publish_article`, which can update an existing public post. Confirm publication only with `published=true` and verify the returned URL/status. A pending `syncPending` state or an error means completion is unconfirmed. After interruption, read `get_article` before any repeat publication; never retry automatically.

Finish with the title, actual state (ready in Semly / published / in progress / failed), an available returned link, a short review summary, and the related question/URL for later measurement. A draft is not a publication, and publication is not proof of future AI citation. Marking a recommendation complete is a separate requested action.

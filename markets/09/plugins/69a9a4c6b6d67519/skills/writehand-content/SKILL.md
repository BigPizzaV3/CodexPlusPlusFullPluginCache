---
name: writehand-content
description: Prepare a Writehand blog, landing-page, or blog-refresh brief, then retrieve and review the user's generated article and cover using their connected Writehand account.
---

Use the connected Writehand MCP tools. Collect the topic, primary keyword, intended audience, brand context, and content objective. Ask only for important missing inputs. Add source URLs, product documentation, and existing content URLs when supplied. Do not invent interviews, customer quotes, research, internal metrics, or brand facts.

Call `get_profile` to check the connected account and balance. Call `prepare_content_brief` to validate the complete brief. Preparation does not spend credits. Show the exact brief and one-credit cost, and obtain the user's confirmation before `create_content`. Reuse the server-issued submission token on retries; never create a second token to retry an uncertain submission.

For a blog refresh, use mode `refresh`, page type `Blog`, and the supplied current blog URL. Keep the user's workflow inputs and constraints intact. If generation is paused, explain the returned error and do not attempt a workaround or submit another job.

Call `get_content_job` for the existing job. Once complete, present the main article, authenticated preview/download link, and cover link. `artifacts.technical_seo_content` is a separate article variant; do not append it to the main article. Keep `artifacts.original_url` available for the unchanged original output.

Explain material review notes, including excess length and unfinished media instructions. Automated notes do not establish factual accuracy, originality, or ranking performance. Treat claimed first-person experience and statistics as unverified unless the user supplied supporting evidence. Do not silently rewrite or publish the article. Offer edits in conversation when requested.

Payments and credit purchases happen on the Writehand website. The connector uses the user's existing account and credits; it does not use their chatbot token allowance to pay for the n8n workflow. Never initiate checkout through these tools or promise search rankings.


## Account connection help

Use https://writehand.net/connect for current connection instructions and the public ChatGPT listing. Website sign-in supports either an emailed code or magic link. A valid website session continues without another email; use the account page to switch accounts. If sending is temporarily limited, follow the displayed retry time and use a still-valid proof from the existing sign-in tab. Never ask the user to paste a code or magic link into chat.

# Results for the usual tactics

Each result rests on an official page. We checked the pages on November 13, 2026. Open the page again before you quote it.

## Against a rule

| Tactic | The rule | Source |
|---|---|---|
| Buy or sell links to rank higher | Google names "Buying or selling links for ranking purposes" as link spam. A paid link is allowed when it is marked as sponsored | [Google spam policies][spam] |
| Trade links in bulk, or make partner pages only to trade links | Google names excessive link exchanges as link spam | [Google spam policies][spam] |
| Publish many pages that add little, written by AI or by people | Google names it scaled content abuse: "large amounts of unoriginal content that provides little to no value to users, no matter how it's created" | [Google spam policies][spam], [Google on generative AI content][genai] |
| Publish one near-copy of a page for each city or keyword | Google names these doorway pages | [Google spam policies][spam] |
| Hide text on a page, or write text that only a crawler or an AI app can see | Google names hidden text: "placing content on a page in a way solely to manipulate search engines". We read this to include a hidden instruction to an AI app | [Google spam policies][spam] |
| Repeat keywords to fill a page, or show a crawler a different page | Google names keyword stuffing and cloaking | [Google spam policies][spam] |
| Add keywords, a city, or a tagline to the name in a Google Business Profile | "Your name should reflect your business's real-world name" | [Google Business Profile guidelines][gbp] |
| Use a P.O. box, or an office with no staff, as the business address | A P.O. box is not acceptable. A virtual office is not eligible unless staff are there during business hours | [Google Business Profile guidelines][gbp] |
| Post fake reviews, pay for reviews on the condition that they are positive, or let staff or family post reviews as customers | A United States rule covers these since October 21, 2024. Google Maps forbids content that is "not based on a real experience" | [FTC rule][ftc-reviews], [Google Maps policy][maps] |
| Give a reward for a review, or ask only the happy customers | Google forbids incentives "in exchange for posting any review", and forbids a business to "selectively solicit positive reviews" | [Google Maps policy][maps] |
| Ask customers for reviews on Yelp | "Businesses should never ask customers to write reviews." | [Yelp guidelines][yelp] |
| Post on Reddit from several accounts, vote as a group, or post the same promotion in many threads | Reddit forbids vote manipulation, content manipulation, and spam. Each community's own rules apply too | [Reddit Rules][reddit], [Reddit on spam][reddit-spam] |
| Praise the product online and hide that the writer is the founder, an employee, or paid | In the United States, the FTC's guides say that a material connection to a brand needs a clear disclosure | [FTC Endorsement Guides][ftc-endorse] |

## Does not do what is claimed

| Tactic | What the platform says | Source |
|---|---|---|
| Allow or block `GPTBot` to change what ChatGPT search shows | `GPTBot` collects training data. `OAI-SearchBot` is the crawler for ChatGPT search. "Each setting is independent of the others" | [OpenAI crawlers][openai] |
| Block `OAI-SearchBot` and still expect to be in ChatGPT search answers | Sites that opt out "will not be shown in ChatGPT search answers, though can still appear as navigational links" | [OpenAI crawlers][openai] |
| Use robots.txt to stop every fetch by an AI app | A fetch that a user requests can ignore robots.txt. OpenAI says of `ChatGPT-User` that "robots.txt rules may not apply". Perplexity says the same of `Perplexity-User` | [OpenAI crawlers][openai], [Perplexity crawlers][perplexity] |
| Block `Google-Extended` to leave Google's AI Overviews | `Google-Extended` covers other Google systems. For Search, the controls are `nosnippet`, `data-nosnippet`, `max-snippet`, and `noindex` | [Google AI features][ai-features] |

## Unproven

| Tactic | What is known | Source |
|---|---|---|
| Add an `llms.txt` file | Google: "You don't need to create new machine readable files, AI text files, or markup to appear in these features." The file costs little. Do not pay for it, and do not put it before the basics | [Google AI features][ai-features] |
| Add special "AI schema" | Google: "There's also no special schema.org structured data that you need to add." Ordinary structured data that matches the text of the page is reasonable | [Google AI features][ai-features] |
| Pay for a promise of mentions, or of a place in AI answers | No method is proven to earn a mention. Nobody outside an AI company controls its answers | none |
| Submit the business to hundreds of directories | No evidence shows that the number of listings earns AI mentions. A few correct listings where buyers look are reasonable | none |
| Change the date on a page and nothing else | A new date with no new fact is not an update | none |
| Buy a tool that shows how often people ask AI apps each question | The AI companies do not publish these numbers. Ask the seller for the source | none |

## Reasonable

| Tactic | Why | Source |
|---|---|---|
| Allow the search crawlers of the AI apps in robots.txt | A blocked crawler cannot read the site | [OpenAI crawlers][openai], [Perplexity crawlers][perplexity] |
| Keep pages indexed, with snippets allowed and the text in the HTML | Google: a page must be indexed and eligible for a snippet to be a supporting link | [Google AI features][ai-features] |
| Write pages that answer buyer questions with the business's own facts | The page helps the reader | [Google on generative AI content][genai] |
| Pitch the editor of a list article with true facts, and accept a paid label | The editor decides, and the reader can see what is paid | [FTC Endorsement Guides][ftc-endorse] |
| Claim real listings and keep their facts current | The platforms ask for it | [Google Business Profile guidelines][gbp] |
| Reply in a community with the writer's real role, where the rules allow it | The reply helps the reader, and it hides nothing | [Reddit Rules][reddit] |
| Ask each customer for honest feedback, with no reward, where the platform allows it | Google allows it. Yelp does not | [Google Maps policy][maps], [Yelp guidelines][yelp] |
| Read the AI reports of the search engines | Google Search Console has a generative AI performance report that shows impressions. Bing Webmaster Tools has an AI Performance report | [Google report][gsc], [Bing report][bing] |
| Ask the same questions many times, and count | One answer shows little. See the `mention-check` skill | none |

[spam]: https://developers.google.com/search/docs/essentials/spam-policies
[genai]: https://developers.google.com/search/docs/fundamentals/using-gen-ai-content
[ai-features]: https://developers.google.com/search/docs/appearance/ai-features
[gbp]: https://support.google.com/business/answer/3038177
[maps]: https://support.google.com/contributionpolicy/answer/7400114
[yelp]: https://www.yelp.com/guidelines
[ftc-reviews]: https://www.ftc.gov/business-guidance/resources/consumer-reviews-testimonials-rule-questions-answers
[ftc-endorse]: https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking
[reddit]: https://redditinc.com/policies/reddit-rules
[reddit-spam]: https://support.reddithelp.com/hc/en-us/articles/360043504051-Spam
[openai]: https://developers.openai.com/api/docs/bots
[perplexity]: https://docs.perplexity.ai/guides/bots
[gsc]: https://support.google.com/webmasters/answer/16984139
[bing]: https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/

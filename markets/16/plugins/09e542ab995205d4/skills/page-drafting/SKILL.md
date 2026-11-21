---
name: page-drafting
description: 'Write a page for the business''s own site that AI apps can quote: a page that answers one buyer question, a fair comparison page, an "alternatives" page, a pricing page, or a page for one use or integration. Uses only facts that the person confirms. Use for "write a page for AI search", "draft our X vs Y page", or content drafting for AEO. Needs no Frontmost AI account.'
---

# Page drafting

Use this guidance to write a page that an AI app can quote: a direct answer first, then sections that each make sense alone, built only from confirmed facts.

With a Frontmost AI project, plan the page from real AI answers first. Use the `answer-pages` skill, then write the page with this skill. With no project, start here.

## 1. Choose the page

| Page | Title | Write it when |
|---|---|---|
| Question page | The buyer's question, in plain words | AI answers to that question mention rivals and not the business |
| Comparison page | "<Business> vs <Rival>: prices and features" | Buyers compare the two, or an answer states a comparison that the site can correct |
| Alternatives page | "Alternatives to <Rival>" | Buyers ask for alternatives to a rival that many answers mention |
| Pricing page | "How much does <product or service> cost?" | The site does not state the price, or what sets it |
| Use or integration page | "<Product> for <use>", or "Does <product> work with <tool>?" | Buyers ask about one use, one tool, or one buyer type |

The evidence for a page can come from a `mention-check` count, a `site-audit` result, or the person's request. Say which one.

Before you write, search the site for a page on the same subject. If one exists, extend that page. Never write a second page that answers the same question in other words.

## 2. Collect the facts

1. List each fact that the page needs: prices, limits, features, places, numbers, and customer words.
2. Mark the source of each fact. These sources are allowed:
   - The person's own words in this conversation.
   - The business's own site.
   - A rival's own public page, with its address and today's date.
   - A public page that you opened, with its address.
3. Ask the person for each fact that has no source.
4. If a fact that the page depends on is missing, hold the draft. Name the gap in your message, not in the page text.

Never invent a price, a number, a customer, a quote, or a feature.

## 3. Write the page

- **Title.** Use the title from the table.
- **First paragraph.** Give the direct answer in two or three sentences. Include the name of the business and its category. A reader must be able to quote it without the rest of the page.
- **Sections.** Use a question or a plain label as each heading. Put the fact in the first sentence of the section.
- **Sections that stand alone.** Give the name of the product in each section. Do not rely on "it" or "this tool" from an earlier section.
- **Proof after the answer.** Follow each claim with a number and its source, a price, an example, or a customer's words that the customer allowed.
- **Tables.** Use a table to compare three or more things on the same facts. Start each row with the name, so that the row makes sense alone.
- **Limits.** Say who the product does not fit, and what it does not do.
- **Facts that only this business has.** Include its own prices, its own process, and its own data. A page that repeats other pages gives an AI app no reason to cite it.
- **A date.** For facts that change, add "Checked on <date>".
- **Plain words.** Use short sentences. Do not use "best", "leading", or "top" unless a source that you cite says so.
- **Length.** Stop when the facts are stated. Add no filler.

For a comparison page or an alternatives page, follow [comparison-pages.md](references/comparison-pages.md).

## 4. Check the draft

1. Read each section without the rest of the page. It must say which business and which product it describes.
2. Check that each number has a source.
3. Check that each fact about a rival has an address and a date.
4. Check that the draft holds no fact without a source from step 2.
5. If the site uses structured data, check that it matches the text that a reader sees.

## 5. Hand over

Give the draft in the format of the site: Markdown, HTML, or the format of its content system. If you work in the site's code and the person asks, add the page as a file on a branch.

With the draft, give:

- The facts that you used, each with its source.
- The facts that are still missing.
- Two or three pages of the site that can link to the new page. A page with no links to it is hard to find.
- The date to check the facts again.

The person publishes the page. Do not publish it for them.

## Never

- Write many pages that differ only by a city name or a keyword. Google's spam policies name these as doorway pages and scaled content abuse.
- Copy text from a rival or from another site.
- Write a review or a customer's words that no customer gave.
- State a fact about a rival that has no source.
- Hide text, or write text only for AI apps.
- Suggest `llms.txt` files or "AI schema" as a fix. They are unproven. Google states that its own AI features need no new files and no special markup.
- Promise that AI apps will cite or mention the page. No method is proven to earn a citation.

## Output

The draft, then the four items of step 5. If you held the draft, give the outline and the list of missing facts.

---
name: bright-data
description: Search the web and read live public web pages with Bright Data, one or several at a time, with pages returned as clean markdown. Use when an answer needs current information from the web, such as the results of a search or the content of a specific page. Read before the first Bright Data call. It covers each tool's input and how to check what came back.
---

# Bright Data

These tools return the source itself: a page as it is right now, or the search engine's own results. The user's own instructions about tools and sources always come first. This skill only describes what each tool returns and when it fits.

## Which tool

| The task needs | Tool | Input |
|---|---|---|
| The results for one search: titles, links, snippets | `search_engine` | `query`. Optional: `engine`, `page`, `time_range` |
| Result lists for 2 to 5 searches | `search_engine_batch` | `queries`: a list of up to 5 objects, each with `query` and the same optional inputs as `search_engine` |
| The text of one page | `scrape_as_markdown` | `url`: a full address starting with `https://` or `http://`. Optional: `format`, and `snapshot_id` with `start` to read the next part of a cut page |
| The text of 2 to 5 pages | `scrape_batch` | `urls`: a list of up to 5 full addresses. Optional: `format`, one for all the pages |

Accepted values for the optional inputs in the table above:

- `engine`: `bing` (the default) or `google`. Leave it out unless the user asks for Google.
- `page`: a number from 0 (the default). `page: 1` is the next page of results. The number of results on a page varies.
- `time_range`: `day`, `week`, `year` or `any` (the default) on both engines. `hour` and `month` work only with `engine: google`. Use it when the user asks for recent results.
- `format`: `markdown` (the default), `text`, `html` (the page's raw HTML) or `ld_json` (the page's schema.org data, such as a price, a rating or an author).
- `snapshot_id` and `start`: copy both from the `next` field of a cut page. Leave them out on the first read of a page.

When to call:

- Run only the searches the task needs.
- A search result is a title, a link and a short snippet, not the page. When the answer depends on what a page says, read the page.
- When the user gives a URL and asks about something on it (a price, a version, a date, a license, a list), read that page and answer from its text.

## Limits

- A batch takes at most 5 searches or 5 pages. Split a longer list into several calls.
- `scrape_as_markdown` returns up to 40,000 characters of a page. `scrape_batch` returns up to 40,000 characters in total, shared between its pages: short pages come back whole, longer ones split what is left.

## Check what came back

Check every item in a batch, not only the call:

- If a call or a batch item returns an error, read what it says and act on it. If it still fails, tell the user plainly which URL or search failed, and answer only from what did come back.
- If a page was cut and the answer is not in the returned text, call `scrape_as_markdown` with the same `url` and `format`, plus the `snapshot_id` and `start` from its `next` field.

## Answering

- Answer from the returned text and name the URL the answer came from.
- If the page was read but does not contain what the user asked for, say it instead of guessing.
- List search results in the order returned, with each result's title and the page's own address.

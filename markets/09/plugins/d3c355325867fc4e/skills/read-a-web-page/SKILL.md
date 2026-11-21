---
name: read-a-web-page
description: Read a public web page the user links to or names, and answer from its actual content. Use when the user shares a URL, asks to summarise, explain or quote a page, or asks what a specific page says.
---

Use this skill when the user gives a URL or names a specific page and wants to know what it says.

1. Call `scrape` with the `url`. Set `preferStructure` to true when the page's meaning lives in tables, lists or headings, such as pricing pages, comparison grids, documentation and spec sheets.
2. Answer from the returned markdown only. Quote or paraphrase what the page says, and link the URL you read.
3. If the user asked for a format, such as bullets or a table, build it from the page content.

When the result is thin or looks wrong:

- If the content is very short, is mostly a cookie notice, or says the page needs JavaScript, say what came back and offer to try again rather than guessing at the rest.
- If the page returned an error or was refused, tell the user plainly that the page could not be read. Do not fill the gap from memory.
- If the page redirected somewhere unexpected, mention the final URL.

Do not:

- Invent facts the page does not state, even when they seem likely.
- Read pages that need the user to be signed in. This tool only reads public pages; say so if the user asks for account or private data.
- Scrape a whole site when one page answers the question. If the user wants several pages from one site, list them with `map` first and read only the ones that matter.

The user's explicit instructions take priority over this skill.

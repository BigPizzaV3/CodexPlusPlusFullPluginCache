---
name: get-started
description: First steps with Wikilayer. Find or create a wiki, read its rules, write a first page and hand back its link. Use when the user is new to Wikilayer or asks what it can do.
---

# Get started with Wikilayer

Wikilayer is a wiki the user reads in the browser and you edit through its tools. A wiki holds pages; a page holds blocks, one per section.

1. Call `list_wikis` to see the wikis this account can read and the role it holds in each.
2. If the user has none, or wants a new one, call `create_wiki`. It is private unless the user asks for a public one. Say so before making a wiki public: everything written to it is then readable on the open web and indexed by search engines.
3. If a call is refused because the wiki has rules, read them with `get_page_markdown(wiki_id=…, special_role='rules')` and pass the value it returns in `rules_read_and_agreed` on later calls. Follow those rules while writing there.
4. Before writing into an existing wiki, read its structure with `get_outline` so new pages land where a reader would look for them.
5. Write with `create_nodes`: a page per subject, a block per section of a page. Do not type `#` headings into a body; a section is its own block.
6. After every write, give the user the link to what changed: join the response's `base_url` and the node's `url_path`.

Ask before deleting pages, changing a wiki's visibility or sharing a page by a public link: these change what other people can see.

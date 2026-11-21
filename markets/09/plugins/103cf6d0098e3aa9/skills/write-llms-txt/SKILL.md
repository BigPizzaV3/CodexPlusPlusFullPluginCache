---
name: write-llms-txt
description: Check whether a site publishes an llms.txt and draft or improve one in the llmstxt.org format, while being honest that major AI models do not read it yet.
---

# Drafting an llms.txt

Use this when the user asks for an llms.txt, wants to know whether theirs is any good, or asks what llms.txt is.

## Set expectations first

llms.txt is an emerging proposal (llmstxt.org): a Markdown file at `/llms.txt` that gives AI tools a short map of a site. Major AI models and answer engines do not read it yet. Say this up front. Glippy gives a small credit in Machine Readability when one exists, and lists a missing one as information, not as a fix to make. It is cheap to publish and may help developer tools and agents that do read it. Do not present it as a ranking factor or a priority fix.

## Check what exists

Run `check_llms_txt` on the domain the user named.

- **Found:** review the contents against the format below and suggest concrete edits: missing summary, broken structure, links without descriptions, links to pages that no longer fit.
- **Not found:** offer to draft one.
- **Fetch failure:** say Glippy could not read it, which is not proof that it is missing. Do not retry.

## The format

```
# Site or company name

> One or two sentences on what the site is and who it is for.

Optional short paragraph with key facts an assistant should know.

## Section name

- [Page title](https://example.com/page): what this page covers, in one line.

## Optional

- [Less important page](https://example.com/other): one line.
```

- One `#` heading, then a `>` summary, then `##` sections of links.
- Every link is an absolute URL with a one-line description.
- Put the pages that matter most first: product or service pages, pricing, documentation, about and contact. The `## Optional` section is for pages an assistant can skip.

## Drafting rules

- Use only pages you know exist: the homepage, links from a Glippy report in this conversation, or pages the user listed. Glippy reads the homepage only, so ask the user for the key page URLs instead of guessing paths like `/pricing` or `/docs`.
- Mark anything you are unsure of as a placeholder for the user to fill in.
- The user publishes the file at `https://<their-domain>/llms.txt`. Glippy cannot upload it.

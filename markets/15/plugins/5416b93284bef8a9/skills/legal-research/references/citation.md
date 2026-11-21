# Citation standard

The point of this connector is that a legal answer can be checked. A citation
the reader cannot follow back to the official text defeats it.

## Every legal statement carries a citation

Cite at the level you actually retrieved. If you fetched an article, cite the
article — not the act as a whole.

Take links from the tool's `sources[]` (`external_url`) or the response's
`url`, `eli_url` or `legifrance_url`. Do not assemble EUR-Lex, Narodne
novine or Légifrance URLs by hand and do not cite from memory.

## Shape

**EU** — act, article, CELEX, and the consolidated version actually read:

> Article 17 of Regulation (EU) 2016/679 (GDPR), CELEX 32016R0679,
> consolidated text 02016R0679-20160504 — <external_url>

Name the consolidated CELEX when `version_note` or `base_celex` shows one was
served.

**Croatia** — act, article, and the gazette chain from the response's
`citation` field:

> Članak 115. Zakona o radu (NN 93/2014, 127/2017, 98/2019, 151/2022,
> 64/2023) — <url>

Use the in-app source viewer to read the retrieved wording. In the answer,
include a compact link to the official NN publication using its returned URL
and reference. `sources[].original_publication` identifies the original act;
the source's separate URL may identify a later amendment or court decision.
Keep those labels distinct and do not imply either is a complete consolidated
text. Do not duplicate publication text or expand a gazette workflow
just to provide the link. Keep the act, article and retrieved version clear.

**France** — article, code, and the version window:

> Article 1240 du Code civil (version en vigueur depuis le 1er octobre 2016)
> — <legifrance_url>

## Always state currency

A quote without status is incomplete. On `@hr` the article response says
whether the version is current (`is_current_version`) and whether the act is
in force (`regulation_in_force`); `get_status` gives the act's status and
history. On `@eu` use `get_status`. On `@fr` report the article's `status`
(`VIGUEUR` = in force) as recorded in the source, without implying an
independent check.

## Historical text

When quoting a provision as it stood on a past date, label it with that date
and the version reference returned. Claim a change only after comparing the
two retrieved texts.

## What not to do

- Do not merge several provisions into one citation.
- Do not cite a search snippet as if it were the article text.
- Do not present the connector's output as legal advice.

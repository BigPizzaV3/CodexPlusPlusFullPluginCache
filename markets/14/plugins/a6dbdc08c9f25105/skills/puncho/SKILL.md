---
name: puncho
description: Work on the person's Meta ads in Puncho. Use when they ask to make ads, write ad concepts or hooks, design what is waiting, add references or competitor ads, check what a brand has or lacks, or ask what is working and what to make next. Also use when they mention Puncho, their board or one of their brands' ads.
---

# Working in Puncho

Puncho runs one person's Meta ads as a loop on their board: references,
concepts, designs, a paused campaign, results, and back to concepts. You do
the work through the Puncho connector's tools; they decide. Talk to them the
way a good media buyer talks to a client: plainly, with the numbers, and with
what you would do next.

## Before anything else

Read `references/start.md`. It is how Puncho's own operator is told to run
this work: the rules, and a list of topics, each a file in `references/`.
Follow it over anything you assume. Then, before each stage of the work, read
that stage's files, once in a conversation:

- before writing or rewriting any ad: `references/concepts.md`,
  `references/ad-copy.md` and `references/ad-copy/references/anti-examples.md`
- before choosing a format, writing a visual idea or building a design:
  `references/designs.md`, `references/ad-design.md` and the files in
  `references/ad-design/references/`
- before reading performance: `references/results.md`
- for anything else, the file `references/start.md` names for it

They are the bar. An ad written without reading them is written from the
category average, which is what Puncho exists to avoid.

## Starting

Call `list_projects`. A project is one brand: with several and none named, ask
which one, and never carry material from one brand to another. Then call
`get_project_status` and tell the person what the project has, what it lacks
and what you would do first.

## What is the person's, never yours

- **Approving an ad, and switching one on.** They do both on the board. There
  is no tool for either; never look for another way to the same effect.
- **Pressing Design this.** It gives a design its budget. Inside that budget,
  generate a design's parts without asking. A design with no budget, or one
  that reached it, is theirs to extend on the board.
- **Launching, budgets, whole-ad renders, and the brand's colours, fonts and
  logo.** This connector is not offered them. When the work needs one, say
  so, say where on the board it is done, and stop there.

Look at any image a tool returns with `view_image`. A call refused because the
person pressed Stop means stop: say what was left unfinished and wait.

## When the tools are missing

If you have no `list_projects` tool, the Puncho connector is not connected.
Tell the person to connect Puncho where their app keeps its plugins (in
Claude, the plugin's Connectors tab under Customize, Plugins; in ChatGPT,
the Puncho plugin's settings), signing in with their Puncho account. Do not
try to do the work without the tools.

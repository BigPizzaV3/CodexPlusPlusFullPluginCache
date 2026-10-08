# Extending JuicyLucy on this machine

Read this when an ad workflow finds no brand installed, when the user asks for a brand that is not
installed, wants the conventions changed, or wants the ads made differently — and is not going to
wait for a plugin release. It says what can be done on one Mac, where it goes, what it costs, and
how it becomes permanent.

The rule underneath everything here: **the plugin is read-only, and Codex has a place for the
user's own skills.** Work in that place, never inside the plugin.

## Where a local skill lives

Codex reads skills from four places, in this order of precedence:

| Root                                  | Scope                                                             |
| ------------------------------------- | ----------------------------------------------------------------- |
| `<folder>/.agents/skills/<name>/`     | Only when Codex is working in that folder or somewhere below it.  |
| `~/.agents/skills/<name>/`            | This Mac, in every folder. **The usual place.**                   |
| `/etc/codex/skills/<name>/`           | Every user of this Mac. Not used here.                            |
| the installed plugin                  | Everything JuicyLucy ships. Read-only.                            |

A skill is a directory with a `SKILL.md` in it. Its `description:` line in the frontmatter is what
the agent sees before it does anything, so that line has to say what the skill is and when to load it.

**A skill in one of the first three roots with the same name as a shipped skill replaces it
entirely.** The plugin's copy disappears from the catalogue; it is not merged with, it is gone.
This is the mechanism every override below relies on, and the reason the last section exists.

Three places look writable and are not:

- The plugin cache, `~/.codex/plugins/cache/juicylucy/juicylucy-ads/<version>/`. A new release
  installs into a new version directory and the old one is dropped.
- `~/juicylucy-plugin`, where the installer copies the release. The next update deletes and
  recreates it.
- `~/.juicylucy`, the toolchain. Deleting it is how the install is undone, so nothing a person
  wrote belongs in it.

An edit in any of these is lost at the next update, silently.

## Creating the first brand

An ad workflow that finds **no** `brand-*` skill in the catalogue says so and comes here. This is
the normal first run for anyone who installed the plugin from the directory, where no brand ships;
it is also what happens on a Mac where the only brand was removed. Do not build the ad from facts
gathered in the conversation and left there: every later step reads brand files by name, and the
next ad would start from nothing again. Make the brand, then make the ad.

1. **Ask for the product facts**, in plain words and in one go where you can. What the product is
   and does, in the product's own words; what it does not do that copy might imply; who it is for;
   the price and terms; the site or design system to capture colours and type from; whether there
   is an end-card image and where; any competitor to study; any claim the user already knows they
   must never make. What the user does not know yet is left as a placeholder, not invented.
2. **Copy the template** — this skill's `references/brand-template/` — to
   `~/.agents/skills/brand-<slug>/`, where `<slug>` is the product's name in lowercase with
   hyphens. Rename `SKILL.template.md` to `SKILL.md`. Keep every other filename: the workflows
   read the files by name, and a missing file is a missing input, not a default.
3. **Fill the files in.** Each owns one kind of fact and says at the top what belongs in it.
   `product-truth.md` and `compliance-overlay.md` first — they gate every line of copy — then
   `brand-kit.md` (run `hyperframes capture` against the site if the user gave one, and record
   extracted values, not eyeballed ones), then the rest. Replace every `<placeholder>`; a file
   with nothing to say yet keeps its one-line "not yet" statement rather than an invented value.
4. **Rewrite the `description:`** so it names the product and says when to load the skill.
5. **Read the new skill directly for this run** — it is on disk, and the workflow can open its
   files by path — and tell the user that Codex catalogues skills at launch, so from the next
   session the brand is found by name without any of this.
6. Confirm it: the setup doctor's `skills` line lists it as `added`.

Say two things at the end: where the brand lives (the folder, so they can open it), and that it
is theirs — every later ad reads it, and changing a fact there changes every ad after.

## Adding a brand

A brand is a skill named `brand-<slug>`. Both ad workflows resolve the brand by looking at which
`brand-*` skills exist: one means that is the brand, several means ask, none means create one
(§ Creating the first brand). Nothing in the workflows names a brand, so adding one changes
nothing else.

1. Copy this skill's `references/brand-template/` to `~/.agents/skills/brand-<slug>/` and rename
   `SKILL.template.md` to `SKILL.md`. (A shipped brand skill, where one is installed, is the
   worked example of a filled-in template — read it for the shape of a finished file, but start
   from the template, so nothing of another product carries over.) Keep every filename: the
   workflows read the files by name, and a missing file is a missing input, not a default.
2. Fill every file in for the new product. Each file owns one kind of fact: `product-truth.md`
   (what it is, is not, who it is for, pricing, voice), `compliance-overlay.md` (what this brand
   may not say), `brand-kit.md`, `outro-card.md`, `copy-patterns.md`, `competitor-set.md`,
   `ad-account.md`, `format-renditions.md`, and a `history/` folder for dated evidence. The
   template's `SKILL.md` § What each file owns is the roster; keep that table.
3. Rewrite the `description:` so it names the product and says when to load the skill. Two
   skills with the same description both claim to be the brand.
4. Start a new Codex session. Skills are catalogued at launch.
5. Confirm it: the setup doctor's `skills` line lists it as `added`, and the next ad request will
   find two brands and ask which — that is the expected behaviour, not a fault.

Do not put a second product's facts into an existing brand's files, and do not put brand facts
into a campaign folder's brief instead of a brand skill. A brief is one run; the brand is every run.

## Overriding a shipped brand

To change something the shipped brand asserts — a claim, a colour, a pattern — before it is changed
for everyone: copy the shipped `brand-<slug>` directory to `~/.agents/skills/` **under the same
name** and edit the copy. From then on this Mac reads the copy and the plugin's version is invisible.

Say two things to the user when you do this:

- Updates to that brand in later releases will not reach this Mac while the copy exists.
- The change lives here only. A teammate's Mac still has the shipped version.

The doctor's `skills` line reports the copy as `replaces`. When the change has been shipped,
offer to remove the copy if the user wants the shipped behavior — see § Making it permanent.

## Changing the conventions

The `juicylucy` skill holds the agency conventions: the filename grammar, the ad-set folder
grammar and its global sequence, the language table, allocation, the evidence layout. These are
shared by everyone and read by automations that parse filenames, so **a change that lives on one
Mac is a fork of the agency, not a preference.** A batch named under a local grammar carries
filenames no one else's tooling expects.

It can still be tried locally, the same way as a brand override: copy the shipped `juicylucy`
directory to `~/.agents/skills/juicylucy/` and edit the copy. The naming tool follows the copy —
it resolves the conventions in the same order Codex does — and prints a note on every call saying
so; `naming.mjs where` shows exactly which files it is reading. Say the same two things as for a
brand override — later updates to the conventions will not reach this Mac while the copy exists,
and a teammate's Mac still has the shipped version — and then, every time a name is produced, that
the filenames follow a local copy.

Before sharing batches with a team, check that its downstream tools accept the customized
conventions. The user may keep the local copy for their own workflow or propose it for the
shared repo when the whole team wants the change.

## Changing how the ads are made

Workflow skills can be customized for personal, business and client work under the plugin's
licence. A local copy replaces the entire skill; it is not a partial override.

1. **Check which layer owns the change.** Product facts belong in a brand skill; filing and
   naming conventions belong in the conventions skill. A change to the production steps belongs
   in the relevant workflow skill.
2. **Copy the whole skill directory** to `<project>/.agents/skills/<same-name>/` for one project,
   or `~/.agents/skills/<same-name>/` for this Mac, preserving its `SKILL.md`, references and
   scripts. Leave it unmodified until the dependency checks below pass. Keep the licence and
   attribution notices with copies you share.
3. **Preserve the skill's dependencies.** A script's relative paths move with its directory;
   copying the skill alone does not make sibling skills available at the new location.
   For `ad-naming`, first run the installed copy's `scripts/naming.mjs where` from the target
   project and record which `naming.json` and `foldering.json` it reads. If these come from the
   bundled `juicylucy` skill, also copy that whole companion skill from the **same installed
   edition** into the chosen local skill root beside `ad-naming`. Do not mix editions or
   create conventions from memory. If a complete project or user conventions override already
   supplies those files, keep using it; never overwrite it with bundled defaults. For an
   incomplete override, preserve its existing files and supply only missing dependency files
   from the sources reported by the installed tool before relocation.
4. **Verify the local copy from the target project.** Run its `scripts/naming.mjs where` and
   confirm both files resolve to the intended conventions. Run `name` with a sample record and
   `folder` with a sample sequence (no reservation or file writes) and compare with the installed
   tool before customization. Then make the intended edits and repeat the relevant checks.
   Resolve missing dependencies before reporting the customization ready. The doctor's `skills`
   line inventories overrides; it does not test their dependencies.
   For another workflow, inspect sibling-relative imports and file reads and run its relevant
   checks before using the copy for production.
5. **Explain the update tradeoff.** The local copy survives plugin updates, but does not receive
  changes to the shipped skill. Record the plugin version it came from so the user can compare
  later releases. Do not delete, rename or overwrite an intentional customization during repair.
   A copied conventions dependency is also a local replacement and needs the same update review.
6. **Read the customized skill directly for this run** and start a new Codex session for the
   catalogue to refresh. The doctor lists the copy as `replaces`, with an update reminder.

The user can keep the customization indefinitely. Offering it back to the plugin maintainers is
optional; it does not require permission or a plugin release to use locally.

## Making it permanent

For someone who installed from the directory, a brand in `~/.agents/skills` **is** permanent:
updates to the plugin never touch that folder, and nothing else needs to happen.

For a teammate on the plugin's private marketplace, a local brand, override or convention reaches
the rest of the team only by landing in the repo — under `brands/`, `workspace/`, or the workflow
skills — and shipping in the next release. That is a pull request, and the person who tried the
change locally is the right person to describe it, because the local copy is already the
proposal: the diff between it and the shipped skill.

Once an equivalent change ships, offer to remove the local copy after comparing it with the
release and confirming that the user wants the shipped behavior. Keep any intentional differences.
A retained copy continues to replace the shipped skill and must be updated separately. The doctor's `skills` line is the
inventory: `added` is a brand that exists only here, `replaces` is any customized shipped skill,
`generated` is the one local skill setup itself writes, and `missing` identifies an extra
`juicy-cli` copy that needs to be checked against the installed command.

That generated one is `juicy-cli`. Its generated location is managed by setup, so use a separate custom skill for additions: the
installed `juicy` writes it (`juicy skill`) from the same command specs its own parser runs on,
so it describes exactly the flags of the version on this Mac, which setup keeps at the newest
published. It goes in `~/.agents/skills` on purpose — the same name as the plugin's copy, which
is only the fallback for a machine setup has not run on. Setup's juicy step rewrites it whole on
every update, and the doctor's `juicy-skill` line says whether it still matches the binary.

## What the doctor reports

```
skills   ok        shipped skills only — no local brands or overrides
skills   ok        local: brand-<slug> (added, in ~/.agents/skills), juicylucy (replaces, in ~/.agents/skills), juicy-cli (generated, in ~/.agents/skills)
skills   ok        local: video-ad-production (replaces, in ~/.agents/skills) — local replacements do not receive plugin updates; keep intentional customizations
skills   missing   juicy-cli (in ~/project/.agents/skills) overrides the generated command reference — check it against the installed juicy version
```

The line scans the same roots Codex reads, from the working directory the doctor was run in, so a
project-scoped brand shows up only when the doctor runs inside that project.

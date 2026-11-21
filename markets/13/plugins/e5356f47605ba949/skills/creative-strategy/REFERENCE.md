# Creative strategy reference

The one place the creative-strategy skills define their words, their evidence rules and the tools
they call. Each skill points here instead of repeating it. When this file and a tool's own
description disagree, the tool is right.

## Two kinds of evidence

| | Ad Swipe File | The user's own material |
| --- | --- | --- |
| Whose ads | Other brands' public Meta ads | The user's brand |
| What it knows | Copy, tags, breakdowns, run dates | Product facts, reviews, results |
| What it can prove | Nothing about results | Only what the user's own numbers show |

- **Ad Swipe File never proves.** A long run (`run.days_running`, `sort: "longest_running"`) is a
  reason to study an ad. Never state an ad's spend, ROAS or conversions, never say it "works",
  "worked", is "a winner" or beat another. `why_it_works` and `breakdown` say how an ad is built to
  work. Write "kept running for 94 days".
- **Link every ad.** Each ad cited carries its `url`.
- **The user's results are the user's.** Numbers about their ads come from them (pasted, uploaded,
  or another connector). Quote only numbers they gave, and say where each came from.
- **A quote is a quote.** A customer quote is an exact substring of a review or post the user gave.
  Paraphrase and your own summaries never pass as customer words.
- **Competitor customers stay competitor customers.** Reviews of another brand teach the category's
  language and moments. Label them with the competitor's name in every output; they are never the
  user's testimonials or proof.
- **An intended persona is not the audience reached.** An ad made for a persona says who it was
  made for, not who saw it.

## Words

Ad Swipe File words are used as its tools define them: run, breakdown, brand patterns, visual format,
hook tactic, board, saved ad, followed brand. The words below are the strategy layer on top.

**Anchor**: the one pain or desire a concept is built on, named precisely ("wakes at 3am and can't
get back to sleep", never "sleep issues"). One anchor per concept.

**Persona**: a group sharing the anchor and a life context: role, routine, constraints, what they
tried. Two groups are one persona when an ad would tell them the same story. Not a demographic (age,
gender: a targeting input) and not an audience (a label people claim, like "runners").

**Trigger moment**: the concrete event when the anchor stops being background and the persona acts.
It has a place, a time, usually other people, and a consequence; the test is whether you could film
it. Each moment moves the persona one awareness stage: problem named (unaware to problem aware),
decides to fix it (to solution aware), a current fix fails or this product appears (to product
aware), a reason to act now (to most aware).

**Angle**: the argument the ad makes for this product, for this persona, in this moment. Usually one
product truth.

**Reason to believe**: why the angle's claim is true: a mechanism, spec, demonstration, number,
review, authority or guarantee. The angle is the claim; the reason to believe is its backing.

**Offer statement**: anchor, persona, trigger moment and angle collapsed into one or two sentences of
what the product does for this person now, in their words. If you can't tell who it's for or why
now, it is a tagline. Not the commercial offer (discount, bundle, guarantee).

**Mechanic**: how the ad makes the viewer arrive at the point: the move between hook, visual and
story. Not the hook (the opening) and not the format (the production shape). Vocabulary in
`pick-creative-mechanic`. The library tags up to two mechanics per ad with those slugs:
`list_ads` with `mechanic` finds ads built on a move. Ad results don't show the tag, so for one ad,
read its move from `structure` and `breakdown`. Ads not read yet match no tag filter.

**Funnel job**: what the creative itself has to finish. `close` carries the viewer to a decision
inside the ad (full proof, a call to action). `click` opens one sharp loop and hands the explaining
to the landing page or a retarget. `sort` lets the viewer decide "is this for me" across several
use cases. A gap that is a flaw for `close` is the design for `click`.

**Concept**: anchor + persona + awareness stage + trigger moment + angle + offer statement +
mechanic + format + hook. A concept missing a step is an idea, not a concept.

**Awareness stage**: how much the viewer already knows, as `list_ads` filters it with
`awareness`: `unaware`, `problem-aware`, `solution-aware`, `product-aware`, `most-aware`. Each ad
carries its `awareness` tag.

**Hook**: the opening system: first spoken line, first visual, first on-screen text, read together.
Its tactic comes from `list_hooks`; each ad carries its `hook_tactic` and `hook_line`, and
`list_ads` filters on `hook`.

**Visual format**: the production shape (talking head, us vs them, notes app), from
`list_visual_formats`; `get_format` gives a format's how to tell and how to build.

## Tools by job

| Job | Ad Swipe File tools |
| --- | --- |
| Find references | `search_library`, `list_ads` (`niche`, `visual_format`, `hook`, `season`, `awareness`, `mechanic`, `status`, `min_days`, `followed`, `sort`) |
| One brand | `list_ads` with `brand` (first page carries `brand_patterns`), `list_brands` |
| Read ads | `get_ads` (up to 25 per call), `get_ad` (`breakdown` with its `structure`, `why_it_works`, `run`) |
| Vocabularies | `list_visual_formats`, `get_format`, `list_hooks`, `list_niches`, `list_formats` |
| Niche direction | `get_trends` (share of a niche's active ads by format, hook and asset type, 30 days against the 30 before; what brands make more of, never what performs) |
| Brand by website | `get_brand_by_domain` |
| Similar ads | `find_similar_ads` (other brands' ads with the same hook, format or niche) |
| Competitors | `follow_brand`, `list_followed_brands`, `list_followed_ads`, `unfollow_brand` |
| Keep references | `save_ad`, `set_ad_note`, `create_board`, `add_ad_to_board`, `list_saved_ads`, `list_boards`, `share_board` |
| Clients apart | `list_workspaces`, then `workspace` on saves, follows and boards |
| Send to a client | `share_board` (and `unshare_board`) |
| Report a gap | `submit_feedback` (a missing brand, a wrong tag, a broken result) |
| Calls left | `get_usage` |

## Writes

- Ad Swipe File writes change only the user's own saves, notes, follows and boards. Make one only when
  the user asked for it or agreed.
- Strategy outputs (competitor maps, personas, concepts, scripts, learnings) go in the reply, or a
  file when the client can write files. They are drafts the user approves.

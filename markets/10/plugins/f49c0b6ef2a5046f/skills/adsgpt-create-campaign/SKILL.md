---
name: adsgpt-create-campaign
description: Create an ad campaign with the user on one or more platforms connected to AdsGPT, with the tool each platform has to create its campaigns, from the objective to the campaign as the platform confirmed it. Use it whenever the user asks to create, launch or plan a campaign.
---

# Create a campaign

You are creating a campaign with the user. Each platform creates its campaign with its own tool,
which its skill names: one call per platform, with the budget, dates, targeting and ads, all or
none. Follow these steps in order. Ask one thing at a
time, and skip what the user already said.

1. **Objective and campaign type.** The objective is one of: awareness, traffic, engagement,
   leads, sales, app promotion. Infer it from what the user wants, read the skill of each
   platform for the objectives it supports and their campaign types, and confirm the objective
   and the campaign type of each platform in one question. When the platforms leave a single
   objective and campaign type, offer only that one: do not list the others. Once confirmed, read
   the rules of each campaign type.
2. **Platforms and accounts.** The mentioned platforms, otherwise the connected ones. The brand or
   product promoted is not a platform, even when a platform shares its name: «promote Brand on
   Platform» picks Platform alone; ask when it is ambiguous. When a platform has several accounts,
   ask which one. A platform that does not support the objective, or that has no tool to create
   campaigns, is left out: say so.
3. **Destination.** The landing page. Keep any UTM parameters the user gives: the campaign uses
   them. Read the landing page and the pages of its own domain that it links to, and keep in mind
   only what they state, in the language of the site: what the brand offers and to whom, the
   facts the ads can claim, such as figures, guarantees or plans, the pages a sitelink can lead
   to, and the image the site shares. When you cannot read the site, tell the user and ask what
   it offers instead of guessing. To promote an app, the link to the app in its store, which gives
   the app and its store; read the user's site too when they give it.

   The assets each campaign type needs, such as images, a logo or links to pages, come first from
   what the account already has, then from what the site states; ask the user only for what is
   still missing. The skill of each platform says how to find them and which ones its campaign
   types cannot go without.

4. **Audience.** Locations, languages, age and gender, and interests, in the user's words, but
   ask only for what the campaign types target, as their rules say, and at the granularity they
   take, such as countries rather than cities. Propose a broad audience when they have none in
   mind.
5. **Budget and dates.** Ask in one question how much they want to invest and for how long. By
   default it is a total for the dates, which caps the spend; a daily amount without an end date
   is an ongoing campaign. Dates are in each account's time zone; without a start date from the
   user, the campaign starts today. The budget type cannot change once the campaign exists. With
   several platforms, propose an even split and let the user change it. Each platform's amount is
   in its account's currency: there is no conversion, so ask for it when the currencies differ.
   Amounts are always in currency units, never micros.
6. **Ads.** Ask once whether they have an idea or something in particular in mind. Write the texts
   with the `adsgpt-write-ads` skill, within the limits of each campaign type, from the user's idea
   and the facts of the site. Images go by the id of an asset the account has or by a public URL:
   the account's library, the site's image or the user's links. They show the brand the campaign
   advertises and no other: a library can also hold another brand's images or logo. The rules of each campaign type say
   which images, logo and videos its ads take.
7. **Name.** One name for the campaign, the same on every platform, which the user recognizes: it
   ties the platforms' campaigns together in the reports. An account refuses a name another of its
   campaigns uses: when a platform says so, propose another.
8. **Create.** Tell the user, for each platform, what the campaign is: its type, budget, dates,
   the targeting it applies, its ads, and whether it starts paused or how much it spends once it
   starts. When a campaign type leaves out part of the audience, such as interests on a campaign
   that targets locations and languages only, say so: name only the targeting the platform
   applies. Then call each platform's tool with its campaign.
   - When a result lists `issues`, nothing was created on that platform: fix exactly those and call
     it again.
   - Then tell the user what each platform created, with the campaign's id, name and status as the
     platform confirmed them, and what failed and why. The result is the check of the creation,
     without querying the platform again.

- Never create a campaign with a platform's generic edit tool: only its creation tool creates one.
- Campaigns are created paused unless the user asks to start them. A platform may start from
  another default, which its skill says.
- To change a campaign after creating it, use the platform's tools for that change; creating it
  again with the same name is refused.

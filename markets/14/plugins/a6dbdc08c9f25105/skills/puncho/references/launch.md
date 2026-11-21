### 5. Launch

Only after a human has approved. `list_specs` with `status: ["APPROVED"]`
shows what is ready. `launch_specs` refuses unapproved specs and
everything it creates is PAUSED, so this step cannot spend money — but confirm
with the human before you run it anyway, because it creates real objects in a
real ad account.

**A budget is in the ad account's currency**, whatever a field's name says
(`dailyBudgetUsd`). `list_ad_accounts` and `list_campaign_presets` show the
currency. Pass the number the human said in that currency, say it back with
the currency, and never convert it.

**Start from saved campaign settings.** `list_campaign_presets` shows the ones
the human keeps in the Campaigns frame — places, ages, objective, goal, pixel
and event, budget. Launch with one by name (`launch_specs` `preset`) instead of
asking again. Never ask the human for a pixel id: `sync_pixels` lists the
account's pixels with what each fired in the last seven days. If the chosen
event shows zero (`eventFiredRecently: false`), say so before launching: Meta
has nothing to optimise on. When the human agrees new settings, save them with
`save_campaign_preset` so the next launch does not ask. A name that already
exists is refused: those are settings the human keeps and launches with. Show
them what would change, and pass `replace: true` only after their yes.

**Who it reaches is always asked, never assumed.** `launch_specs` has no default
audience and refuses without one. Before proposing a launch, get from the human:

- **Where.** Look places up with `find_ad_locations` and use their keys. A town
  can come back as a `medium_geo_area` (smaller towns often do), which takes no radius;
  for "the town and 25 km around it", use a point at its centre.
- **Ages.** Meta allows 13 and up. Under 18, only place and age can be targeted.
- **How results are counted.** With a pixel on the destination firing on
  registration: `OUTCOME_LEADS` + `OFFSITE_CONVERSIONS` with its `pixelId` and
  `conversionEvent`. Without one: `OUTCOME_TRAFFIC` + `LANDING_PAGE_VIEWS`, and
  say plainly that registrations are not being measured.

Then `estimate_audience` on exactly that audience, and propose the launch in
words with the reach: "Plovdiv, 25 to 45, about 90,000 people, 5 EUR a day,
optimised for landing page views." After launching, repeat its `summary`.

The special ad category comes from each concept's `specialAdCategory`, and one
campaign carries one. Concepts with different categories are refused together:
launch each category as its own campaign. Employment, housing and credit ads
must reach 18 to 65 with a radius of 25 km or more — so an employment ad cannot
go to anyone under 18, and should not be relabelled to get it there.
`set_spec_attributes` is for an honest mislabel only: changing the category or
the audience segment of an approved concept sends it back for the human's
decision, and on a concept with ads on Meta it is refused.

**A launched concept can go into another campaign.** Launching it again — another
city, another age band — needs no new approval: a launched concept's image and
copy are locked, so it is still exactly what the human approved. `list_specs`
with `status: ["LAUNCHED"]` finds it.

**Budgets can change after launch** with `set_daily_budget`, and only to an
amount the human named. `list_campaigns` gives the campaign's id, its budget
now and the currency. Propose it as "Plovdiv: 1.50 → 5.00 EUR a day", wait
for the yes, and after it report the account's new daily total. On a live
campaign the new budget spends at once, so the permission prompt appears every
time, like a launch.

**A launch that fails is undone.** The campaign it created is deleted in Meta
and here, and the concepts go back to their status before. Report Meta's reason
and retry once the cause is fixed. The one leftover is said in the error: when
Meta does not confirm the delete, the campaign is kept here, named as a failed
launch, and the human deletes it in Ads Manager.

**Read `notes` in the result and pass them on.** Without an Instagram account
set, ads with a 9:16 version go out with their 4:5 image everywhere, and the
note says so.

`activateAd` resolves its account from the ad itself, never the default. You are
not activating anything, but know that the ids you report are account-specific.

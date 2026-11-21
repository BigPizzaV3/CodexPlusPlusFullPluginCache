---
name: advanza-event-pack
description: Build everything an event needs in Advanza - sign-up form, landing page, invitation email and a countdown of social posts - as drafts. Use when the user is planning an event or webinar.
---

# Event pack

The user is holding an event - a webinar, a breakfast seminar, an open day, a launch. Build the
promotion in one campaign, timed back from the event date.

Explicit instructions from the user always take priority over this skill. Answer in the user's
language, and pass the user's time zone (`timeZone` / `timeZoneId`) to every tool that takes one.

## 1. Get the facts

Ask only for what is missing: the event's name, date and time, place or link, who it is for, and what
people should do (sign up, book, come by). Use the brand (`brand.get`) for tone. Never invent
speakers, prices, agenda items or claims.

## 2. Build the pieces

1. `campaigns.create` for the event, from today to the event date.
2. `landing-pages.create-draft` with the event facts, one clear call to action, and `campaignId`.
3. The sign-up form, once the user is happy with the page: `forms.create` (name, email and at most two
   more fields), then add it to the page with `landing-pages.update-draft` (`formId` and a form
   section). A form takes submissions at its own address as soon as it exists, so say so.
4. The invitation and a reminder for the day before, as emails of their own (no `campaignId`) so each
   goes out at the time the user wants: `email-campaigns.create-draft`, from an event template the user
   picks in `open_email_template_picker` where one fits. Link them to the landing page's
   public address; if the result gives only a path, ask the user for the site's address or leave the
   button for them to set in Advanza.
5. A countdown of social posts with `social-posts.create-draft` in the campaign; its `targets` make one
   post per connected channel (`social-accounts.list`) in one call. Plan them for about three weeks,
   one week and one day before, skipping any date already passed. Note each post's date and time: a
   draft gets its time when it is scheduled. Check `social.channel-rules`: Instagram, TikTok and
   Pinterest need an image or video, and a TikTok post needs its audience chosen in Advanza.
6. Run `brand.check-text` on every text and fix what it reports as blocking.

Check `calendar.list` for the event period and pick another day for a post when something else is
already planned on that channel that day.

## 3. Hand over

Show the pieces with their links and proposed dates. Then list what still needs doing, in order. Each
step that sends or publishes is approved by the person on its card:
1. Who receives the emails: `email-campaigns.set-audience` on each, with a group (`contactGroupIds`).
2. Publishing the landing page: `landing-pages.set-published`.
3. The posts: approve their content in the campaign (`campaigns.set-post-approval`), put them on their
   dates (`social-posts.bulk-schedule` with the proposed times), then `campaigns.activate` so they go
   out. If the activate preview says the schedule moves (`shiftDays`), stop: posts would land after the
   event. Schedule the passed posts again first.
4. The emails: `email-campaigns.schedule` for the invitation and the reminder, at their times.

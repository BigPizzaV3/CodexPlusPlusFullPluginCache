---
name: funnel
description: "Put GA4 or Meta pixel conversion tracking on the links of a Beste site as a funnel of three to five steps. Use when the person wants to measure bookings, leads or sales on their Beste site."
---

Put conversion tracking on an existing Beste site.

A funnel is not a feature to switch on. It is a decision about what counts as
progress on this site, and then the same decision written onto every link that
carries it. Your job is the decision first, the writing second.

### Your first message

Two lines. Something like:

    **Let's measure what matters on your site.**

    I'll look at your pages first, then ask you one thing.

Then look. No plan, no list of what you are about to do.

### Look before you ask

1. get_analytics_setup. This tells you which of GA4, Meta and PostHog the site
   actually has, and the event names GA4 recognises. **If nothing is connected,
   stop here**: say so in one line, tell them where to add a measurement id in
   the builder, and offer to carry on the moment it is there. Writing events
   into a site with no analytics is writing into nothing.
2. list_pages, then list_links. Now you know the whole site: what pages exist,
   what every link says, where it goes, and which links already fire something.
3. Read what is already there. A site with tracking on half its buttons has a
   history, and overwriting it silently is how a report loses its past.

### Ask one question

**Use your question tool**, and ask the only thing you cannot work out
yourself: what counts as success here. Offer three or four readings of the site
you just looked at, in their words, not in GA4's:

    - "Someone gets in touch"      (contact, quote, callback)
    - "Someone books a slot"       (appointment, table, viewing)
    - "Someone buys"               (checkout)
    - "Someone downloads the menu"  (whatever this site actually offers)

Leave room for their own answer. One question, then stop asking.

Do not ask which events to use, or what to name them, or which links to put
them on. That is the work, and it is yours.

### Build the funnel

A funnel is three to five steps. Fewer says nothing; more cannot be read.

Each step is one **stage of intent**, not one page. Several links can share a
step: every "Book now" button on the site is the same step, wherever it sits.

Name the funnel once, in snake_case, after the outcome: `lead_capture`,
`booking`, `purchase`. Number the steps from 1 at the widest.

For a site whose success is "someone gets in touch", that is usually:

    1  select_content   the links that start the journey: a service card, a plan
    2  view_item        opening the thing itself: a service page, a plan page
    3  contact          a phone, email or WhatsApp link
    4  generate_lead    the contact form's own button, if the site has one

Use the names get_analytics_setup gives you and nothing else. An invented name
arrives in GA4 as an event with no report built for it, which is the same as
not measuring. If the site really needs a name of its own, say so and ask
before turning on allowCustomNames.

Pick the **sink** by what the site has connected. GA4 measures; the Meta pixel
is for advertising and belongs on the last step or two, where an ad can be
optimised against it. Do not put every event on every sink: three copies of one
click is three times the noise and, for Meta, three times the ad signal spent
on nothing.

### Write it

set_link_events, addressing links by the sectionId and path list_links gave
you, and pass `funnel: { name, step }` on every event. Both parts matter: the
name groups the steps into one report, the number orders them.

One call, all the links. It writes each section once, so a funnel across
fifteen links is one batch and one thing to undo.

**Do not track everything.** A link to the privacy policy is not a funnel step.
Social icons in the footer are not a funnel step. Every event you add is a row
someone has to read past to find the one that matters, so leave the rest alone.
A shared navbar link is written once and counts on every page; that is correct,
and worth saying.

### Tell them

Short. The funnel as steps, each with the number of links behind it:

    Tracking is on, as a funnel called **lead_capture**:

    | | | |
    |---|---|---|
    | 1 | Services and plan cards | 6 links |
    | 2 | Service pages opened | 3 links |
    | 3 | Phone and email | 4 links |
    | 4 | Contact form | 1 link |

    It is in the draft. Say the word and I'll put it live, and it starts
    counting from then.

Then the one caveat that is true and easy to miss: nothing is measured until
the site is published, and if the site shows a cookie banner, visitors who
refuse are not counted. Say it in a line, not a paragraph.

Never publish on your own. This site is already live and this change is
theirs to make.

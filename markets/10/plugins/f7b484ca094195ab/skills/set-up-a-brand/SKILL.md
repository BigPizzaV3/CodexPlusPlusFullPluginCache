---
name: set-up-a-brand
description: Set up or update a brand's voice guide in CommScore (tone, values, style do's and don'ts, audiences, terms to use or avoid) from its website or from brand guidelines the user provides, so CommScore can write and score communications in that voice. Use whenever the user wants to add a brand or organisation to CommScore, build or fill in a brand voice guide, import brand guidelines or a style guide, or add terms the brand uses or avoids, even if they don't mention CommScore by name.
---

# Set up a brand

CommScore writes and scores communications against a brand's voice guide. A complete
guide makes everything else better: drafts sound like the organisation, and scores point at
what actually matters for it. This skill gets a brand from nothing (or half-filled) to a
guide the user has reviewed and approved.

The user stays in charge of what their brand guide says. Draft freely, but save only what
they have seen and agreed to.

## 1. Check what already exists

Call `list_brands`. If the brand is already there, don't create it again. Work on the
existing one: read it with `get_brand_profile` and fill the gaps (step 4). Brands with
the same name are told apart by website.

## 2. Create the brand (if it's new)

Call `create_brand` with the name, website, language (e.g. `en-AU`) and country (e.g.
`AU`). Ask the user for anything you can't infer. Creating a brand needs a CommScore admin
or member account; if the tool says so, tell the user who can do it.

If the user gave you brand guidelines (a pasted style guide, a document's text), you can
pass the parts you're confident about straight into `create_brand`, mapped to the guide
fields.

## 3. Draft the guide

There are two sources. Use whichever the user has, or both:

- **The website:** call `research_brand`. It drafts values, customer charter, tone,
  writing principles, style examples, audiences and terms from the brand's public web
  presence, in about 30 seconds, using the workspace's AI credits. It saves nothing.
  If part of it is unavailable, say which part and carry on with the rest.
- **Their own guidelines:** extract the guide fields from what they gave you. Quote their
  wording where you can; don't invent values or rules the document doesn't contain.

## 4. Review with the user, then save

Show the draft in readable sections, not as raw JSON:
- **Voice:** tone, core idea, writing principles.
- **Values:** company values, service values, customer charter.
- **Style:** do's, don'ts, checklist.
- **Audiences.**
- **Terms to use** and **terms to avoid**, each with its explanation or alternative.

Ask what to change. Apply their edits, then save:

- `update_brand_profile` fills empty fields and adds terms and audiences. It never
  overwrites, so it's safe for a first save or for topping up.
- If it reports `skipped` fields (already filled), show the user the current value next
  to the new one. Use `replace_brand_fields` only for the fields they confirm should be
  replaced. Remember that a list passed to it replaces the whole stored list.

## 5. Show the result

Call `get_brand_profile` and summarise what the guide now holds, in a few lines. Offer a
quick test: draft or score a short sample communication for the brand (an email or SMS)
so the user can see the guide at work.

## When something goes wrong

- **"Only CommScore admins and members can…":** the user's account can read brands but not
  change them. Suggest they ask a CommScore admin, or use the CommScore web app.
- **Web research turned off:** ask the user for their brand guidelines instead, and draft
  from those (step 3).
- **Duplicate refused by `create_brand`:** use the brand_id it gives you and continue from
  step 4.

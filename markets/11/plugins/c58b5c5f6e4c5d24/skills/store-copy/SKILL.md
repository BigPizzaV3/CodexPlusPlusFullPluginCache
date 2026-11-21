---
name: store-copy
description: "App Store and Google Play listing text and ASO wording: app name, subtitle, keyword field, promotional text, descriptions, What's New and Play release notes, and their localization. Use when the person says things like \"rewrite my subtitle\", \"what keywords should I put\", \"my app isn't found in search\", \"translate my listing into German\", \"is my description good?\" or \"write the release notes\". Not for researching competitors or a market (market-research) or for images (store-visuals)."
---

# Store copy

## When this applies

Writing, judging or localizing the words of a store listing, on either store, for an app that is live or not published yet. Researching competitors and markets belongs to market-research; screenshots and icons to store-visuals.

## The job and what good looks like

The person ends with copy for each store and language they asked about that a stranger in that country finds by typing what they type, and understands from the first words. The promise comes first. The fields search reads spend every character on distinct terms people search for; the selling text speaks to someone already on the page. Every proposal rests on evidence the person can check: competitors' listings, keyword demand and difficulty.

## How a pro decides

- **Search or persuasion.** The stores read different fields for search. Place each term where search reads it, and let the description persuade.
- **Brand or job in the name.** A known brand keeps its name; an unknown one spends it on what the app does.
- **Localize or translate.** Each locale gets the words its users type, which may share nothing with the source. A translation that overflows is rewritten to fit, never cut.
- **Variants or one answer.** Offer variants only on short fields where wording changes the outcome; each names its angle and its evidence in one sentence. One long description, not variants.
- **Which findings to act on.** Fix what a store enforces or documents. Fix MWM's own pipeline rules while saying the store would accept the text. Mention practitioner habits only when asked. A clean check means no rule fired, not that App Review agrees.

## Do

- Use the person's own wording as given, untranslated unless they ask; when it breaks a store rule, write it and say what it costs.
- Write each store's fields for that store; never carry a value from one store's field to the other's.
- For an open goal on Google Play, include release notes in the first draft for the languages in scope.
- Take a new country's keywords from that country's searches.
- For an app not on a store yet, read its texts in the project: fastlane metadata, Info.plist, strings.xml.
- For an open goal, default to the app's stores, its primary language and that language's country, and say so; ask only for the positioning, once, when nothing gives it.

## Don't

- Don't propose another app's or company's name in visible fields.
- Don't derive URLs or the copyright line from the app name, or copy them to other languages unasked.
- Don't truncate to fit.
- Don't estimate keyword demand or rank when there is no data: say it is unknown.
- Don't say a listing was saved or sent without a result that says so.

## Pitfalls

- A keyword-field word that search already reads elsewhere wastes room; the knowledge base says which words count as already present.
- "Where the app is found" is not "where it is sold".
- Some fields change only with a new version; promising a same-day edit that needs one disappoints.
- Locale codes differ between the two stores.

## Store facts

Tool results carry the store rules and limits they depend on, each with its source and the date it was checked. `get_publishing_knowledge` answers questions on this skill's topics the same way (topics: `app-store/text-fields`, `app-store/keywords`, `app-store/versions-and-mutability`, `app-store/localizations`, `app-store/links-and-legal-fields`, `google-play/listing-text`, `cross-store/store-differences`, `cross-store/localization`). When you use one of these facts, give its source and date.

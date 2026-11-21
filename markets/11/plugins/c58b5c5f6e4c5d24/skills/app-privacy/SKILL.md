---
name: app-privacy
description: "The App Store's App Privacy answers of one app: answered from its code and SDKs, kept in MWM, then applied or read on App Store Connect's page in the person's own signed-in browser. Use when the person says things like \"answer App Privacy from my code\", \"fill in the privacy label in App Store Connect\", \"what does my app declare?\" or \"we added an ads SDK\". Not for the privacy policy or Data safety (privacy-and-legal)."
---

# App Privacy

## When this applies

The App Store's privacy answers of one app, which people call the privacy label or nutrition label: deciding them from the code, applying them in App Store Connect, or bringing what App Store Connect already publishes back into MWM. The policy text, the terms and Google Play's Data safety form belong to privacy-and-legal.

## The job and what good looks like

Two places hold the same answers. MWM keeps the declaration and shows it on the Store page; App Store Connect publishes it on the product page, and Apple's API gives MWM no way to read or write it there. Good work leaves both saying the same thing, each answer traceable to evidence in the code, and the person aware of every change before the App Store shows it.

## How a pro decides

- **From the code.** Start from what ships: the lock files, the SDKs the app starts, each SDK's privacy manifest and documentation, the tracking prompt, the permissions asked and what the app sends to its own servers. An SDK's own declaration is evidence; anything else you infer is an assumption you name.
- **Linked and tracking.** Linked follows identity, such as an account or a device identifier; tracking follows Apple's narrow definition, never plain analytics. Ads and attribution SDKs are where both usually go wrong.
- **Applying.** Work in the person's own browser, where they are already signed in to App Store Connect. Set each data type exactly as MWM keeps it and remove what isn't declared. Stop before Publish: show what goes out and wait for their yes.
- **Reading.** For an app already on the store with nothing in MWM, read the page as it is and keep that copy, changing nothing. Differences with the code come afterwards, as a proposal.

## Do

- Show the answers with the SDK or file behind each one, and the assumptions apart.
- Say where the page differs from what MWM keeps, and let the person choose.
- Tell the person when App Store Connect asks them to sign in, and wait for them.
- Record in MWM only what the person agreed to, or what the page publishes.

## Don't

- Don't type a password, sign in or accept a prompt for the person.
- Don't touch Edit, Save or Publish while you are only reading.
- Don't leave out a data type because only an SDK collects it.
- Don't say the App Store shows the answers before the page says they are published.

## Pitfalls

- An SDK that combines the app's data with other companies' data for ads makes the app track, whatever the app uses it for.
- A tracking prompt with no tracking declared, or tracking declared without a prompt, reads as an incomplete label.
- App Store Connect's page follows the person's language: match the data types by meaning, not by English words.
- A stale copy in MWM misleads every reader: after a change on the page, MWM's copy changes too.

## Store facts

Tool results carry the store rules and limits they depend on, each with its source and the date it was checked. `get_publishing_knowledge` answers questions on this skill's topics the same way (topics: `app-store/app-privacy`, `cross-store/privacy-policy-and-account-deletion`, `mwm/shared-listing`). When you use one of these facts, give its source and date.

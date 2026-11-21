---
name: create-boat-listing
description: Use when the broker wants to create a new boat listing in BrokerForBoat from notes, a spec sheet, documents or photos, add its photos and publish it on their website and portals.
---

1. Call `get-account` to learn the company's listing languages (the first one is the default and needs a title), the enabled portals and whether the user can create boats.
2. Collect the data from the broker's material. Required: year, length (m), type (motor or sail), condition (new or used), price and country. Only use data the broker gave you; ask for anything missing instead of guessing.
3. Write a title and description for each of the company's languages and call `create-boat`. The boat is created as a draft.
4. Photos:
   - Public links: `add-boat-photos-from-urls`.
   - Files on the broker's computer, if you can read and send them: `get-photo-upload-urls`, upload each file to its link, then `arrange-boat-photos`.
   - Otherwise, give the broker the upload link from `get-boat` (`links.upload_photos`).
5. Show the broker a summary (`get-boat`) and ask for confirmation before publishing.
6. Once the broker confirms, call `set-boat-status` with `published` and, if they asked, `set-boat-portals` with the chosen portals.

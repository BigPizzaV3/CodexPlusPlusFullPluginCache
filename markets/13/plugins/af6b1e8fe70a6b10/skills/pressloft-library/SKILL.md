---
name: pressloft-library
description: Use Press Loft for Media to find editorial images, press releases, trends, collections and brands for registered media members, retrieve image captions and published prices, and deliver publication-confirmed high-resolution image downloads. Use for Press Loft media research requests.
---

Use the journalist tools available to the connected Press Loft media account
and their current schemas. A registered media account and sign-in are required.
Follow returned pagination and permissions; one page is not the full result set.
Location defaults to the authenticated journalist's country in tblUser.country_code;
language and preferred currency use that country's defaults, with UK/EN/GBP as
the fallback. Do not infer location from a brand or use website settings_ship_to,
settings_language or settings_currency. Pass localisation overrides only when
the user explicitly requests a different market, language or currency, and
preserve those overrides across search, display, captions and downloads.

## Available media tools

- `search_images`: search live editorial product and lifestyle image metadata;
  this tool does not display cards or previews.
- `show_image_card`: display one specifically requested image.
- `show_image_cards`: display a selected set of actual images together;
  include explicitly requested captions with `include_captions: true`.
- `list_brands`: browse and filter the brand directory.
- `search_press_releases`: discover accessible press releases.
- `get_press_release`: read a full release and browse its associated images.
- `search_trends`: discover live editorial trends.
- `get_trend`: read trend details and browse associated images.
- `search_collections`: discover accessible image collections.
- `get_collection`: read a collection and browse its associated images.
- `list_download_publications`: load the media member's publication choices
  and editable defaults.
- `download_image`: download up to 10 permitted high-resolution originals in
  one call after the journalist confirms the publication and exact publication
  date in chat. One Press Loft component saves each file to the journalist's
  device; the tool returns each image's caption.
- `get_image_caption`: read an image's brand, product, published prices,
  stockist information and the Press Loft messaging link as text.
- `get_image_captions`: read captions for 1–50 distinct selected image IDs in
  one call, preserving their order and the same localisation.

## Journalist images and editorial content

- Use `search_images` for product/lifestyle image discovery. Complete all
  searches, pagination and selection before displaying cards. Search results
  are metadata only, so repeated searches do not create intermediate cards.
  Use focused candidate pages (for example `per_page: 24`) and stop when enough
  suitable images are available. Keep `include_facets: false` unless exact
  category/brand facet values or counts are needed. Apply orientation, style and
  price filters directly; do not fetch facets merely to use those filters.
- Finish an image request with one `show_image_cards` call containing only the
  final selected, distinct image_ids, in the intended order and requested
  quantity, with the same localisation overrides. Do not display every candidate
  for a subset request or call display tools to inspect intermediate results.
  Use `show_image_card` only for one specifically requested image. Do not repeat
  a display call for the same completed selection or repeat its product titles,
  brand names, prices and details links in the chat response.
- If the user requests captions with the images, set `include_captions: true`
  on that final display call (up to 50 images), then present the returned
  `captions` as text beside the cards. Do not fetch each caption separately or
  add the descriptions to the card UI. For captions alone on several selected
  images, use `get_image_captions` once with their distinct `image_ids`.
- For latest/newest images, use `sort: "latest_first"`; card date_live uses the
  same indexed live timestamp as Typesense ordering. Do not substitute another
  upload or launch date. For a random selection, choose distinct actual image
  IDs before the single final display; do not invent a random-sort parameter or
  claim a uniform sample of the whole library from one page of candidates.
- Preserve returned localised names, brand credits and price_display with its
  currency_code. These are product retail prices, not image licence fees.
  The preferred currency is selected only if the brand has published a price
  in it; otherwise use the brand's base price and currency. Never convert a
  price or relabel an amount with another currency. All published currencies
  are supported for display; numeric search price filters are limited to the
  indexed GBP, EUR, USD, AUD and SEK currencies. Check the returned published
  price and currency against any requested budget; index price filters may use
  estimates. When different brands are requested, select distinct `brand_id`
  values as well as distinct images.
- Use `search_press_releases`, `search_trends` and `search_collections` for
  discovery, then the matching `get_press_release`, `get_trend` or
  `get_collection` to read selected content and its paginated `images` list.
  Listing `preview_images` references are not the complete associated image list.
- Present full requested press release bodies, trend descriptions/editorial
  details and collection descriptions as plain text. Editorial content has no
  card UI. To display its associated images, pass actual IDs from the detail
  result's `images` list to `show_image_cards`; never use a release, trend or
  collection ID as an image ID. Keep the editorial text alongside the image
  cards, which reload the products' actual names and details.
- Image display is cards-only, for both single and multiple selections. The
  component is the image display: do not append Markdown images, native preview
  images, repeated titles, brand/price summaries or additional details links.
  Requested captions, editorial content and useful commentary may appear as
  text alongside the cards; do not repeat a card merely to add those details.
  The display result's `structuredContent` is a compact selection summary;
  full card details and preview URLs are widget-only `_meta.image_card_data`.
  Do not speculate about whether cards will appear. Mention a rendering problem
  only if the host reports one or the user says the cards are missing; do not
  claim rendering succeeded without host confirmation. Share relevant gallery
  links as a way to explore, not as a warning. Do not add inline image fallbacks.
  Do not invent image sources or print standalone image URLs. The widget loads
  prebuilt `_m` assets directly; do not fetch, resize or re-encode previews with
  host tools. Explicitly requested original downloads use the download workflow
  described below.
- Use `list_brands` for the directory: `country_code` filters brand location,
  `ships_to` filters shipping coverage, and `sort: "name"` requests alphabetical
  results. `sort: "latest_first"` or `"oldest_first"` orders by join date (jdate);
  join_date_from and join_date_to are inclusive UTC dates in YYYY-MM-DD format.
  Shipping defaults to the journalist's registered country; `ships_to: "ALL"`
  browses worldwide. A brand-location filter does not change the journalist's
  location. Directory discovery does not grant private press-office access.

## Downloads and captions

1. Download originals only when the journalist explicitly asks. In chat, call
   `list_download_publications`, then ask in one short message for the
   publication (one of theirs, or another publication name) and the exact
   publication date (YYYY-MM-DD), suggesting the returned defaults. Never invent
   details, infer an exact day from a month, or treat defaults as confirmation.
2. Once confirmed, call `download_image` once for the whole request, never
   once per image: pass every requested image in image_ids (up to 10; split
   larger selections into batches), either publication_id or publication_name,
   the exact date, a new random 32-character lowercase hexadecimal request_id
   and any localisation overrides. Do not ask again for details already
   confirmed. Reuse a request_id only to retry identical details.
3. `download_image` shows one Press Loft component that saves each unchanged
   original to the journalist's device by itself. Reply with the returned
   captions only, formatted for publication, and encourage the journalist to use
   them when publishing: brand name and website; product name, full description
   and product link; selected published price with currency symbol and ISO code;
   all alternative published prices; stockist details; and the Press Loft
   messaging link. If a caption is missing, say so without inventing details.
   If the result lists unavailable images, name them and give the reason briefly.
4. Never describe a download as approved, authorised, retrieved or attached.
   Never offer image, product-page or previous-download links in place of the
   files, and never ask the journalist to click anything to complete them.

An image card's Download button completes its own download after the journalist
confirms the publication and date in the card. Do not repeat it in chat, and do
not add a caption unless asked.

Do not download originals during search or editorial browsing.
Do not fetch or display captions for ordinary browsing, even for small
selections, unless requested. Long descriptions and caption
text stay outside image cards and download dialogs. When captions are explicitly
requested without a download, use `get_image_caption` for one image, or included
or batch captions for several (up to 50), with the same localisation overrides.
Do not repeat a caption lookup when the requested caption is already available.

## PR enquiries

Use `press_contact.message_url` for PR enquiries. It opens the brand press office;
tell the journalist to choose **Message** to use Press Loft messaging. Give the
link rather than exposing personal PR names, email addresses or telephone numbers.
Do not look up or repeat those details from old tool responses or editorial
contact blocks. Public stockist websites and telephone numbers remain caption
information. Contacting the brand takes place in Press Loft, through that link.

This app supports media research and confirmed image downloads. If asked to
edit product details or perform library-management tasks, explain that the media
connection does not provide those tools or permissions. A visible image or a
supplied brand/product ID does not authorise editing or access to private content.

If the Press Loft connection requires authentication, direct the user to connect
their registered media account through ChatGPT's app controls. Account scope and permissions are
enforced by the server; do not treat user-supplied account IDs as authorisation.
Keep account passwords, OAuth tokens and other sign-in secrets out of chat and
tool arguments.

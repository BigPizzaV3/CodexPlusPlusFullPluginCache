# Google Ads: search campaign

Text ads on Google Search for the people who search what the user offers.
`google_ads_create_campaign` with `campaign.type: search` creates one budget, the campaign (paused
unless the user asked to start it), its targeting, sitelinks, callouts and structured snippets,
one ad group with the keywords, and its responsive search ads, from 1 to 3, leading to the
destination with AdsGPT's tracking. Bidding follows the objective: clicks for traffic,
conversions for leads and sales.

Write the fields of `campaign`:

- **Keywords** (`keywords`): what people search for what the user offers, in their words. They
  match in broad match.
- **Negative keywords** (`negativeKeywords`): only the searches the user wants to exclude, in their
  words. A search that contains all the words of one is left out. Without exclusions, leave it
  empty.
- **Locations and languages** (`locations`, `languages`): their ids, from
  `google_ads_search_targeting`; never assume them.
- **Interests** (`interests`): the ids of the interest audiences the user asked for, from
  `google_ads_search_targeting` (kind interest). The campaign observes them without narrowing its
  reach. Without interests, leave it out.
- **AI Max** (`aiMax`): only with the leads and sales objectives, which bid for conversions. Offer
  it when you confirm the objective: it matches the ads to more searches than the keywords, which
  it treats as broad match. Without the user's yes, leave it off. Its text customization and final
  URL expansion stay off, as by default: they would change the ads the user approves.
- **Sitelinks, callouts and structured snippets.** A search campaign is not finished without them:
  without them its ads rank lower and get fewer clicks. Write them with the campaign, not after it
  is created.
  - **Sitelinks** (`sitelinks`): from 4 to 6, each to a different page of the brand's site on the
    landing page's domain that you read and that exists, in the language of the ads when the site has
    it. Point them to what a ready buyer clicks next, such as pricing, plans, reviews or contact,
    not to pages that repeat the ad. The link text says what the page is, up to 25 characters and
    different in each one, and both descriptions, up to 35 characters each.
  - **Callouts** (`callouts`): from 4 to 6 texts, up to 25 characters each: concrete reasons to choose
    the brand that the site states, such as a figure, a guarantee or a service, not slogans. They
    repeat no text of each other or of the ads.
  - **Structured snippets** (`structuredSnippets`): one, or two with different headers, each a
    header from Google's list written in the language of the ads, never in English for ads in
    another language, and from 3 to 10 values of up to 25 characters, in that language too. Choose
    the header by what the values are, not by the business: every value must be one of the kind
    the header names, or the policy review rejects it.
    - **Types** (Spanish «Tipos»): kinds of the product, such as ad formats (banner, native,
      interstitial) or plans.
    - **Service catalog** («Catálogo de servicios»): services someone hires, such as mediation,
      payments or support.
    - **Brands** («Marcas»), **Models** («Modelos»), **Styles** («Estilos»), **Courses**
      («Cursos»), **Destinations** («Destinos»): names of brands, models, styles, courses or
      places.
  - When the site does not give 4 pages, 4 facts or 3 items of a kind, ask the user for what is
    missing, in the same question as anything else you still need.
  - No exclamation marks or decorative symbols in sitelinks or callouts.

**Ad texts.** From 3 to 15 headlines of up to 30 characters and from 2 to 4 descriptions of up to
90 characters, without repeats.

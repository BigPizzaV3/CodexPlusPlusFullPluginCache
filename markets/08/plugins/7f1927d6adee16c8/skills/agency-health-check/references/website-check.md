# Website check: snippet + number swap

This check answers 3 questions for each company that uses website tracking numbers (session trackers, plus source trackers with swap targets that aren't offline):

1. Is the number CallRail is set to replace (the swap target) actually on the website?
2. Is this company's CallRail JavaScript snippet (`swap.js`) loading, and not some other company's?
3. When the page loads, does a tracking number replace the business number?

Most web fetch tools return the page as text and strip out `<script>` tags. So a fetch can answer question 1 but usually not 2 or 3. Only a browser, which runs the page's JavaScript, can answer all 3. Be clear in the report about which tier produced each result.

## Who gets checked

Every active company with 1+ website tracker (defined in SKILL.md step 3). Everyone else gets Website status "Not needed (no website tracking numbers)".

## Step A: Find each company's website

1. **Form submissions (whole account, 1 pass).** If this returns a permission error, skip to the next source; some user roles can't see forms. Call `list_form_submissions` with a 90-day window (`start_date`/`end_date`), `per_page: 50`, paging until done. For each submission take `company_id` and `landing_page_url` (fall back to `form_url`). Keep the most common domain per company. These records include names, emails, and messages from the people who filled out the form. Take the URL and nothing else.
2. **Call landing pages (top companies only).** For up to 10 companies in the current batch that still have no URL, call `get_calls_summary` with `company_id`, `group_by: landing_page`, and the 90-day window. Take the non-null key with the most calls. Stop early if the first 5 lookups all come back empty; this account probably doesn't record landing pages.
3. **Ask the user once.** In one message, list the companies still missing a URL and ask for a `Company name, URL` list. Tell them they can say "skip". Don't guess URLs from company names or web searches; checking the wrong site produces wrong flags. If they skip, the company goes under Not checked. If no one can answer (scheduled run, no user present), mark these "Not checked: no website URL" and continue.

Clean each URL to scheme + domain + path (strip query strings; they can carry tracking IDs). If the host is `localhost`, an IP address, contains `sandbox`, or starts with `staging.`, `dev.`, or `test.`, don't fetch it. Mark "Not checked: URL in CallRail is a test site ({host}). Ask the client for the live URL."

## Step B: Tier 1 (web fetch)

Fetch the verified HTTPS URL using an available web tool. Reuse a cached result when it provides the needed content. If a request fails, allow at most one ordinary retry and then record "Not checked" with the observed reason. Follow the host tool's access and bot-detection rules. Do not downgrade to HTTP or try alternate domains or paths to bypass a block. Note which page was checked.

**Does the site match the company?** Look at the page title and business name on the page. If it clearly names a different business than the CallRail company, add an Info flag: "The site found in CallRail ({url}) looks like it belongs to {other name}. Confirm the right URL with the client." Keep checking it anyway.

**Swap target check.** For each of the company's swap targets of type `number`, take the last 10 digits. Strip every non-digit from the fetched content and search for those 10 digits. Results:

- Any swap target found → "Swap target on page"
- No swap target found, but other phone numbers on the page → **Swap target not on page**
- No phone numbers on the page at all → **No phone number on page**

**Snippet check (only if you got raw HTML).** If the fetched content contains `<script` tags, you have raw HTML. Search it for this company's script path, the `/companies/<number>/<key>/` part of `script_url`:

- Found → "Snippet found (this company)"
- Another `/companies/.../swap.js` on `cdn.callrail.com` or `cdn.calltrk.com` → **Snippet belongs to another company**
- Neither, but a Google Tag Manager container (`gtm.js` or `GTM-`) → "Can't confirm (may load through Tag Manager)"
- Nothing → **Snippet not found**

If the content has no `<script` tags, you only got page text. Snippet status: "Needs browser to confirm". Don't report "Snippet not found" from page text; that would send the user to fix something that may be fine.

## Step C: Tier 2 (browser)

Run Tier 2 for every company in the batch when a browser tool is available. It's the only check that sees scripts and live swaps.

1. Open the verified URL with an available browser tool and follow its observation and loading guidance. Use supported read-only page inspection to check scripts and rendered numbers. If a tab hangs, allow one ordinary recovery attempt; respect any access or bot-detection block. If browser inspection is unavailable, mark Tier 2 not checked.
2. Read the page's script sources. With a JavaScript tool: `Array.from(document.scripts).map(s => s.src).filter(s => s.includes('callrail') || s.includes('calltrk'))`. Or check network requests for `cdn.callrail.com` or `cdn.calltrk.com`.
3. Read the page text and `tel:` links. Strip non-digits and look for the company's tracking numbers (last 10 digits) and swap targets. Some agencies use one tracking number as another tracker's swap target. Only count a tracking number as "swapped in" if it isn't also one of the company's swap targets; otherwise you'd confirm a swap that never happened.
4. Close the tab when done.

When more than one result applies (for example, another company's snippet and no phone number), report each one as its own flag.

Results:

- This company's `swap.js` loaded and a tracking number appears → **Swapping confirmed**
- Another company's `swap.js` loaded → **Snippet belongs to another company** (note the other company's number from the path; you don't need to look it up)
- This company's `swap.js` loaded, but only the swap target appears → **Snippet loads but number didn't swap**
- This company's `swap.js` loaded and there's no phone number on the page → **No phone number on page**
- No CallRail script at all → **Snippet not loading**

DNI picks a number based on how the visitor arrived. A direct browser visit only matches trackers with source type "all" or "direct". So "didn't swap" is Red when the company has a website tracker with one of those sources, and Yellow otherwise (its numbers may only swap for paid, search, or UTM-tagged traffic). For a tracker keyed on UTM parameters (`landing_params`), you can test it directly: load the URL with those parameters added (for example `?utm_campaign=PPC-IN`) in a fresh tab and look for that tracker's number.

## Scoring website results

| Result | Level | Issue | Fix |
|---|---|---|---|
| Snippet not loading (Tier 2) or Snippet not found (raw HTML) | Red | "The CallRail snippet isn't on {url}, so website calls aren't tracked." | "Install the JavaScript snippet before the closing `</body>` tag or through Google Tag Manager. If it was installed before, a caching or speed plugin (like WP Rocket) may have removed it. Help: https://support.callrail.com/hc/en-us/articles/5711709638541-Installing-the-JavaScript-snippet and https://support.callrail.com/hc/en-us/articles/8694836525581-Dynamic-number-insertion-and-caching-plugins" |
| Snippet belongs to another company | Red | "The snippet on {url} belongs to a different CallRail company ({other id}), so calls are credited to the wrong client." | "Replace it with this company's snippet from its Settings in CallRail. Check the page source and the Google Tag Manager container for the old one." |
| Snippet loads but number didn't swap | Red or Yellow (see above) | "The snippet loads on {url} but the number didn't swap on a direct visit." | "Test in a private window with a source that matches the tracker. Help: https://support.callrail.com/hc/en-us/articles/5711381204877-Testing-dynamic-number-insertion" |
| Swap target not on page | Yellow | "The number CallRail is set to replace ({target}) isn't on {url}, so there's nothing to swap." | "Update the swap target to match the number on the site. Help: https://support.callrail.com/hc/en-us/articles/8807711079949-Checking-the-Swap-Target-Placement" |
| No phone number on page | Yellow | "There's no phone number on {url}, so DNI has nothing to swap." | "Add the business number to the page, or point the check at a page that shows it." |
| Needs browser to confirm | Info | "Swap target is on the page. The snippet couldn't be checked without a browser." | "Open the site in a private window and confirm a tracking number shows. Help: https://support.callrail.com/hc/en-us/articles/5711307505805-Troubleshooting-dynamic-number-insertion" |
| Can't confirm (may load through Tag Manager) | Info | "Couldn't see the snippet in the page source. It may load through Google Tag Manager." | Same as above |
| Swapping confirmed | none | | |

## Fields to fill in the report

`website_url`, `url_source` (forms / calls / user / none), `snippet_status`, `swap_status`, `check_tier` (1 or 2).

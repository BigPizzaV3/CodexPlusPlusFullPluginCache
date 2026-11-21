# Preparation draft — not ready for final submission

16 October 2026. Original private export is preserved separately and unmodified.

Included: version 1.0.0; supported description reused from Anthropic submission; publisher; four fetched public URLs; portable MCP connection; approved supplied 512x512 icon; five positive and three negative draft review cases.

Outstanding:
- Owner chose to reuse the existing CarClever – Find My Car recording for now. Its URL is verified against the submitted 12 September manifest and included in review metadata. It is a prior-edition recording; current four-tool coverage and video playback have NOT been independently verified. Do not describe it as a new Buying Assistant recording.
- Run the draft cases against the saved submission version; all draft cases currently NOT RUN here. Earlier regression evidence is separate.
- Confirm publication countries explicitly before adding targeting metadata. U.S. inventory coverage is confirmed.
- Confirm portal commerce declaration before setting it. Category corrected from rejected Shopping to Other, matching the previous plugin category and original ChatGPT export. Known behavior: no payment or lead submission by tools; affiliate links lead to Edmunds/dealer enquiries.
- Icon resolved: owner approved the supplied circular CC design on a 512x512 PNG canvas. Original bytes bundled unchanged; listing and composer dimensions are met.
- Live policy includes Buying Assistant sources/hosting but also legacy features; aggregate logging detail remains unverified in code by this agent.
- Impact compensation wording agreement check remains unverified in this session.
- Verify current MCP annotations and portal scan, publisher identity, domain setup and owner declarations. No app code changed.

Draft walkthrough to record in the connected Buying Assistant chat:
Find a used Honda CR-V under $30,000 within 50 miles of 90210.
Check the first vehicle.
Compare the first three cars (or two if only two returned).
Get the Edmunds viewing link for the first car.
How do I change the oil?
Show readable actual prompts, tool results, comparison, viewing link and general maintenance response without invoking the shopping tools. No purchase or enquiry needed. Host with reviewer access and supply the recording link.

## Reused demo context for reviewer notes
The linked recording demonstrates the existing CarClever – Find My Car experience. CarClever – Buying Assistant is the separate catalogue edition described in this submission, using its own vehicle catalogue and the four tools listed here. The recording is supplied as prior workflow context; it does not demonstrate every current tool.

## Update 19 October 2026 (before review)
Package version stays 1.0.0 (same draft). Changes since the 16 October package:
- The link tool callable name is now `get_edmunds_vehicle_link` (was `resolve_dealer_url`); the title "Get Edmunds Link for a Vehicle" is unchanged. Positive review case 5 now lists the new name.
- The long description no longer offers transmission as a search option (transmission and cylinder count are not applied as filters; drivetrain is checked against the VIN decode). It now mentions colour, which is supported.
- Release notes updated to describe the changes above and the behaviour fixes (honest notices for applied and unapplied filters, strict ordering for cheapest/newest/lowest mileage, accurate messages for an invalid VIN, a database problem and an unrecognised location).
- The five positive review cases were run against the live server on 19 October at tool level (search, VIN check, comparison, link) and each returned a normal result; the link equals the card link. They have not been replayed through the reviewer interface. The three negative cases are not tool calls by design.
- Endpoint, authentication, domain, icon, publisher, URLs and category are unchanged.

## Update 24 October 2026 (after the new server version went live)
Package version stays 1.0.0. Only the release notes in `plugin.json` and this section differ from the 19 October package; the description, review cases, `mcp.json` and the icon are identical by checksum. The package holds no tool schema: the portal reads the tool list from the live server, which changed when the new build went live on 24 October (Brisbane): 27 search fields, an optional `condition` (new or used) instead of `used`, up to eight cars per search. The four tool names are unchanged: find_matching_vehicle, check_vehicle, compare_vehicles, get_edmunds_vehicle_link. All are read-only; no sign-in.
Changes since the 19 October package that a user can see: up to eight cars; each model a buyer names keeps a place in the shortlist when it has a match; new or used can be requested; hybrid, plug-in and electric searches check each car's VIN with NHTSA, mark cars it cannot confirm, name the models left out and say plainly when a model has no electric version; cars with no photo of their own show a labelled stock photo of the same make, model and year; every reply starts with one line stating what was searched; the comparison table.
The five positive review cases were run against the live server on 24 October at tool level: (1) used Honda CR-V under $30,000 within 50 miles of 90210 returned eight cars; (2) electric pickup under $80,000 within 100 miles of 90210 returned eight cars (F-150 Lightning, Silverado EV) and names cars NHTSA shows as another type as left out; (3) VIN 2HKRS3H20TH312786 is no longer in current inventory, so check_vehicle returned the decoded car (2026 Honda CR-V LX) with the honest "not currently listed here" message, and recall data was marked unavailable at that moment (a known external dependency); (4) the comparison of the first three CR-Vs from case 1 returned a three-car comparison with the side-by-side table; (5) the Edmunds link for the first car came back with the affiliate code and equals the link on the search card. They have not been replayed through the reviewer interface. The three negative cases are not tool calls by design.
Endpoint, authentication, domain, icon, publisher, URLs and category are unchanged.

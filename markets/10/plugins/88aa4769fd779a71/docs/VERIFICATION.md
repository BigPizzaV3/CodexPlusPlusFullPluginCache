# Private prototype verification

Build: 0.4.0. Date: October 4, 2026.

## Results

| Check | Result |
| --- | --- |
| Automated arithmetic and protocol tests | 34 passed, 0 failed |
| Independent rational arithmetic comparison | 460 input cases passed for both output units |
| HTTP MCP transport | Initialized, tools discovered, calculations and errors returned, UI resource read |
| Stdio MCP transport | Same capabilities verified with a real SDK client |
| Browser calculation | Synthetic inputs produced the expected concentration and formula |
| Browser unit changes | Quantity preserved, prior result cleared, recalculation correct |
| Browser invalid volume | Zero rejected and previous result hidden |
| Browser Reset | Inputs, units, error state, and result cleared |
| Responsive layout | 390px and 1100px viewport checks, no horizontal overflow |
| Theme integration | Independent mocked-host check passed for initial and updated themes |
| Skill structure | Official skill validator passed using isolated PyYAML dependency |
| Dependency audit at install | 0 reported vulnerabilities |
| Source checks | Brand separation, absence of configured analytics, long-dash scan, expected package paths passed |

## Defects found and corrected

- A Reset control shadowed the native form reset method. Renamed the control and repeated the browser interaction successfully.
- A malformed HTTP request target could throw outside the request handler's error boundary. It now returns 400, with a raw-request regression confirming continued server health.
- A long decimal could grow beyond the input-length limit during unit conversion. Inputs now have a consistent significant-digit budget and adequate character allowance; exact round-trip conversion has a regression test.
- Host theme changes previously changed only native control appearance. The host now controls the full palette through the theme attribute, with a mocked-host recheck.
- The initial Host-header test used a client that ignored that header override. A raw Node HTTP request now verifies the intended rejection.

An independent read-only reviewer reproduced the server and numeric defects, then verified the fixes. All three findings from that review are resolved within the private prototype scope. No production-readiness score is assigned.

## Not verified

- Installation or discovery in the user's actual ChatGPT account.
- Tool selection, conversation-panel entrypoints, and Share with chat inside a live ChatGPT session.
- Public hosting, identity verification, directory acceptance, or clinical use.

The source ZIP and standalone calculator are local deliverables. No HTTPS endpoint was deployed, no user account connected, no global plugin configuration changed, and no public submission made.

## Version 0.2.0 update

- User-requested Peptara Labs branding is applied to the title, byline, footer, copied result, plugin listing metadata, MCP component title, and icon.
- Charcoal (#1C1C1E), gold (#C9A96E), and warm white (#FAF8F5) are based on observed styles from the live brand site.
- Two CTAs point to https://www.peptaralabs.io/ (Explore Peptara Labs) and https://www.peptaralabs.io/coa (View lab reports), both opened and checked on October 4, 2026. The homepage is the primary brand destination. No checkout or payment links are included.
- Optional syringe capacities are 0.3 mL, 0.5 mL, and 1 mL. Source: https://www.embecta.com/ca/en-ca/insulin-syringes/ultra-fine/. This reference is independent of concentration arithmetic and is not a device recommendation. No graduation scale is inferred.
- All CTA and source links use the MCP Apps openLink bridge when connected, with ordinary links for standalone use. Clicking a CTA does not include calculation values in the URL.

## Final v0.2 review

- Independent review passed 34 automated tests and mocked-host checks for selection, reset, host state, unchanged concentration, and exact outbound link payloads. Live ChatGPT embedding remains unverified.
- Corrected the README to distinguish numeric inputs from the independent capacity selector.
- Verified the 390 px layout has no horizontal overflow and corrected spacing in the CTA heading.
- The app keeps the full requested title. Directory metadata uses Peptara Labs Calculator and Peptide concentration math to fit the 30-character name and subtitle limits documented at https://developers.openai.com/plugins/deploy/submission.
- Public approval is not established. The advertising and restricted-commerce provisions at https://developers.openai.com/plugins/plugin-guidelines require review before public submission. The calculator provides its complete concentration result without a website visit.

## Version 0.3.0 equipment reference

- Added separate labeled syringe and vial SVGs. They are equipment references, not product-specific reconstitution instructions. The product/manufacturer reference is still pending.
- U-100 is the default scale. Available reference capacities are 0.3, 0.5, and 1 mL; mL-marked capacities are 1, 3, and 5 mL. No capacity is selected initially. The fallback 1 mL picture is explicitly an example.
- Manufacturer references: U-100 capacity and variable graduation specifications at https://www.ultimedinc.com/consumer-health/insulin-syringes/ulticare-u-100-insulin-syringes and https://www.embecta.com/en-us/availability/. U-100 calibration definition at https://www.ultimedinc.com/animal-health/pet-insulin-syringes/ulticare-vetrx-ultiguard-safe-pack-u-100-insulin-syringes establishes the insulin scale only, not a recommendation of veterinary equipment.
- Manufacturer capacity examples: https://www.bd.com/en-us/products-and-solutions/products/product-page.309628 (1 mL), https://www.bd.com/en-ca/products-and-solutions/products/product-page.301077 (3 mL), https://www.bd.com/en-us/products-and-solutions/products/product-page.309646 (5 mL). These are capacity references only. The 3 mL bulk non-sterile model is not recommended equipment.
- The figure shows zero near the covered-needle end and the maximum near the plunger. Minor graduation marks, fluid amounts, insertion, and mixing steps are not shown.
- A browser check covered all six capacity selections. Each preserved the same 5.48 mg/mL arithmetic fixture, updated the correct scale endpoint, and did not add capacity to the calculation. Reset restored U-100, no selected capacity, and a cleared result.
- All 34 existing automated tests passed. Package validation passed across 24 source files.
- Independent read-only review confirmed all six capacities, type switching, reset, host empty/result behavior, schematic accessibility IDs, endpoint orientation, and version consistency. Its stale build-header finding was corrected to 0.3.0. Live ChatGPT remains untested.
- Mobile visual check at 390 px passed with no horizontal overflow; both SVGs were legible at 289 px rendered width.

## Version 0.4.0 design update

- The field label is Peptide mass (vial size), with helper text distinguishing the mass printed on the vial from the container's mL capacity.
- Works with any peptide appears under the headline and is immediately qualified as concentration arithmetic with product-specific preparation requirements.
- Native selects explicitly use a light color scheme and dark text on light surfaces in both app themes. Source/color review found control contrast 14.23:1 and option contrast 16.05:1.
- The original 256 px Peptara Labs logo was retrieved from the public site's https://www.peptaralabs.io/images/peptara-logo.png. The PNG is preserved in assets, embedded as a data URL in the calculator, and used for listing icons. The browser needs no remote image request.
- Added a decorative dimensional vial, gold orbital elements, layered panels, and a motion control. This vial has no dose, fill amount, preparation sequence, or product-specific label.
- Motion preferences are session-only. System reduced motion takes precedence, and document visibility pauses decorative animation in background tabs.
- Post-design automated suite: 34 passed, 0 failed. Package validation passed across 26 source files.
- Browser checks confirmed original logo images loaded at 256 px intrinsic size, no overflow at 390 px and 1280 px, six syringe capacities retained, and unit conversion preserved the 5.48 mg/mL arithmetic fixture.
- Browser motion checks confirmed both decorative animations pause via the control and zero animations remain under reduced motion. A separate mocked-controller review covered live preference changes, background visibility, manual choice persistence, and accessibility state.
- Fixed mobile caption overlap by adding 20 px to the hero's vertical layout while preserving the vial/pedestal position.
- Native option colors were verified in browser computed styles. The separate Codex in-app browser's OS-rendered popup was not captured after the fix.
- Final independent source/artifact review passed: pause and reduced-motion CSS, native select contrast, two byte-identical original-logo embeds, and version consistency.

## Soft capsule selection

- Applied the selected Concept 01 to both callouts: a compact gold compatibility badge with separate qualifier, and an icon-led preparation note on an open background.
- All qualifying copy is preserved. The byline reads By PeptaraLabs.io.
- Browser checks at 1280 px and 390 px confirmed no horizontal overflow. Both light and dark styles were checked, including transparent note backgrounds and removal of the previous left borders.
- Independent read-only review confirmed decorative SVG accessibility, all 28 application IDs intact without duplicates, and current CSS in the built artifact. Calculation logic was not changed.
- Build and package validation passed. The arithmetic suite was not repeated for this HTML/CSS-only update.

# DSIR GHE Health Estimates

Discover WHO Global Health Estimates causes, measures and dimensions. Retrieve mortality and disease-burden estimates by country, year, sex, age and exact cause codes, with units, uncertainty fields when available, completeness checks and source provenance. Export CSV and JSON for further analysis. Includes a verified WHO country-code mapping. All-age rates are crude; selected-age rates are age-specific. The tool does not automatically age-standardize rates or sum overlapping cause categories. Runs in ChatGPT Work using the host's script environment and public HTTPS access. Users do not install R, DSIR or additional packages, and no API key is needed. Independently maintained by Shanlong Ding; it does not provide clinical advice.

## Using the plugin

Enable the plugin in ChatGPT Work, select it with @, and ask a data question. The host supplies script execution and HTTPS access. No local environment installation is required. A host that cannot execute the bundled client cannot retrieve data; report that limitation.

Request CSV and JSON downloads when needed. Keep units, dimensions, observation years, source and retrieval metadata with exported values. An empty result or request error is not a measured zero.

## Candidate identity

BUILD.json records the version, source commit and runtime file hashes. This archive is a release candidate for draft validation. Building or uploading it does not submit it for review or publish it.

Initial independent GHE plugin with built-in WHO country mapping, exact cause and dimension discovery, bounded public WHO retrieval, completeness and data-quality checks, and CSV/JSON exports. Distinguish crude and age-specific rates and prevent unsupported aggregation.

Software is MIT licensed. Source data remain subject to their original providers' terms.

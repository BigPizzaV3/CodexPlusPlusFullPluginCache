# Status and flag guide

| Status | Meaning | How to phrase it |
|---|---|---|
| verified | Confidence ≥ 0.85 and no conflicting fields | "Matched a record: <title> (<year>), DOI <doi>." |
| likely_match | Confidence ≥ 0.65 with no conflicts | "Probably this record; please confirm the details." |
| needs_review | A candidate exists but fields disagree, or the DOI's record differs | "Found a close record, but <field> differs: …" |
| not_found | Every source answered and nothing matched | "Not found: couldn't verify this in Crossref, DataCite or OpenAlex." (only this wording; no stronger characterization) |
| unverifiable | A source was unavailable or the citation lacks enough detail | "Couldn't check this right now / need more detail." |

| Flag | Meaning |
|---|---|
| doi_not_found | The DOI isn't registered with any DOI agency (checked at doi.org) |
| doi_points_to_different_work | The DOI resolves to another work; see `doi_record` |
| title_mismatch / author_mismatch / year_mismatch | The cited field disagrees with the matched record |
| year_off_by_one | One-year difference, usually online-first vs print |
| not_found_in_sources | No index had a matching record |
| no_matching_record | Every source answered: the DOI is unregistered and/or no candidate matched the cited title and authors. Still phrase it as "not found / could not be verified". |
| retracted | The matched work is marked retracted in OpenAlex |
| source_unavailable | An index was rate-limited or down; results may be incomplete |

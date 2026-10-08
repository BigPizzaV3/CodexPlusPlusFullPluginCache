# Healthcare Public Data

Research healthcare data from official public sources without mixing it with
personal health records.

## Workflows

- Evidence and clinical trials: PubMed and ClinicalTrials.gov
- Medication and device safety: DailyMed, RxNorm, and openFDA
- Providers and facilities: NPI Registry and Medicare Care Compare facility data
- CMS coverage and open data: CMS Coverage plus curated Part B physician,
  Part D prescribing, and inpatient hospital payment data from CMS Open Data

## Source routing

Prefer the official connector before generic web search: ClinicalTrials.gov for
registered trials, PubMed for biomedical literature, DailyMed for official drug
labels, RxNorm for normalized medication concepts and RxCUIs, and NPI Registry
for public provider identity records; openFDA for FDA regulatory datasets, CMS
Coverage for Medicare coverage policy, Medicare Care Compare for facility
ratings and quality measures, and CMS Open Data for Medicare payment,
utilization, and prescribing data.

Install the plugin, then connect whichever healthcare apps you want to use.
Existing app connections remain available, and each app retains its own
workspace permissions and rollout policies. Installing the plugin does not
automatically connect its apps.

CMS Open Data does not expose CMS Open Payments, Medicaid, hospice, or dialysis
records. Those questions require their separate official sources. Population
health questions outside Medicare, such as general C-section rates, likewise
need the appropriate public-health source rather than a Medicare payment file.

The plugin is read-only. It preserves source names, record identifiers, links,
and data dates supplied by each app. It distinguishes source facts from
cross-source inference and calls out missing or not recently verified records,
as well as incompatible or non-comparable evidence.

## Safety boundary

ChatGPT can make mistakes and isn't intended for diagnosis or treatment. Consult
a doctor for medical advice.

Use these sources for research and public-record lookup, not personalized
diagnosis, treatment, emergency guidance, or access to a user's medical
records. A provider's NPI is not proof of current licensure or quality. An
adverse-event report does not establish causality or incidence. Payment,
utilization, facility, and coverage records must be interpreted within their
published scope and data period.

See [references/sources.md](references/sources.md) for the source inventory,
attribution, and provider policies.

See [references/telemetry.md](references/telemetry.md) for the product and
operational telemetry contract.

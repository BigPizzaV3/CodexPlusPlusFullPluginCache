# Measurement Readiness Playbook

Use this reference when planning a conversions campaign or assessing conversion-measurement readiness. It provides stable advertiser guidance; live account evidence establishes what is configured.

## Connect Ad Engagement To Business Outcomes

Reliable conversion signals help connect ad engagement to the outcomes the advertiser values and give optimization a clearer view of the customer journey.

When the advertiser can support them, recommend:

- combining browser-side and server-side conversion signals for more complete measurement;
- sending useful upper-funnel events alongside the lower-funnel outcome that matters for the campaign;
- preserving the supported OpenAI click identifier, such as `oppref`, when forwarding server-side events; this is downstream forwarding guidance, not permission to append reserved parameters to an ad destination URL;
- passing eligible privacy-safe identifiers, such as a hashed email, when available and allowed by policy.

## Stay Inside The Connector Boundary

The connector cannot install or configure Pixel, CAPI, Automatic Advanced Matching, `oppref` forwarding, or user-data matching, or verify that instrumentation works end to end. Do not offer those actions or infer readiness from a website or a configured conversion goal.

Use only reads allowed by the active skill. Creation skills can read conversion event settings; source inventory and recent-event diagnostics belong to Insights, Review, or Delivery Recovery. Those reads establish only the returned facts. Campaign-create preflight owns event/source resolution and eligibility before a conversions proposal or write.

For current setup requirements, matching behavior, troubleshooting, and performance claims, use `$ads-manager-help`; within Help, use its Help Center guide directly. Do not duplicate setup defaults or statistics here.

When the user reports incomplete measurement or an allowed read shows a gap, explain the smallest next check. Distinguish campaign creation from measurement readiness without silently changing the objective or blocking an unrelated approved create.

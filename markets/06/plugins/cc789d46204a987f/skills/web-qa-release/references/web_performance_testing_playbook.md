# Web Performance Testing Playbook

## Purpose

Use this file to diagnose user-perceived performance and release regressions.

Distinguish lab from field evidence.

# 1. Evidence types

## Lab
- Lighthouse;
- browser performance panel;
- synthetic monitoring;
- local throttling.

Useful for diagnosis and reproducible comparison.

## Field
- RUM;
- CrUX;
- production telemetry.

Best for actual user experience.

One does not replace the other.

# 2. Core Web Vitals

When relevant evaluate:
- LCP — loading experience;
- INP — interaction responsiveness;
- CLS — visual stability.

Verify current recommended thresholds when exact numbers matter.

# 3. LCP diagnosis

Inspect:
- server/TTFB;
- redirects;
- render-blocking CSS/JS;
- resource discovery;
- hero image;
- image size/format;
- fonts;
- client rendering;
- cache/CDN.

Find the actual LCP element.

# 4. INP diagnosis

Inspect:
- long main-thread tasks;
- JS execution;
- event handlers;
- rendering/layout;
- hydration;
- third-party scripts;
- repeated synchronous work.

Measure the interaction causing the poor experience.

# 5. CLS diagnosis

Inspect:
- images without dimensions;
- late fonts;
- injected banners;
- async content;
- ads/embeds;
- animations/layout shifts.

# 6. Network

Review:
- waterfall;
- compression;
- caching;
- critical resources;
- unused payloads;
- API latency;
- third-party dependencies.

# 7. JavaScript

Check:
- bundle size;
- code splitting;
- duplicate libraries;
- main-thread cost;
- hydration/rendering;
- unnecessary client code.

Do not optimize bundle size in isolation if it is not the bottleneck.

# 8. Images/fonts

Check dimensions, responsive variants, format, compression, preload priority, lazy loading, font subsets, and fallbacks.

# 9. Regression comparison

Compare the same environment when possible:
- before/after;
- same route;
- same browser;
- same throttling/device profile.

Report meaningful changes, not run-to-run noise.

# 10. Release decision

Performance should block release when a material regression affects supported users/critical journeys or an explicit performance budget/SLO is violated.

Do not block solely because one Lighthouse score is lower than preferred.

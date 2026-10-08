# Browser, Responsive, and Visual Testing

## Purpose

Use this file to define browser/device coverage and interpret visual regressions.

# 1. Browser matrix

Build the matrix from product support requirements.

Common targets may include:
- Chromium;
- Firefox;
- WebKit/Safari-like;
- mobile Chromium;
- mobile WebKit.

Do not claim cross-browser coverage from one browser.

# 2. Feature compatibility

For newer web APIs or CSS features:
- check current browser compatibility/Baseline data;
- consider graceful fallback;
- test supported browser versions.

Compatibility data is not a substitute for functional testing.

# 3. Responsive testing

Test at content-driven breakpoints, not only device labels.

Check:
- navigation;
- tables/lists;
- forms;
- dialogs/sheets;
- overflow;
- sticky/fixed UI;
- orientation;
- touch targets;
- soft keyboard;
- long text/localization;
- zoom/text scaling.

Do not merely shrink desktop layouts.

# 4. Touch vs pointer

Features that depend on hover, right-click, drag, tiny targets, or mouse precision need an alternate interaction on touch where required.

# 5. Visual regression

Good candidates:
- stable marketing pages;
- design-system components;
- charts;
- print/export layouts;
- important fixed layouts.

Poor candidates:
- random timestamps;
- ads;
- personalized feeds;
- uncontrolled animations;
- highly dynamic external content.

# 6. Snapshot stability

Screenshot output can vary with:
- OS;
- browser version;
- fonts;
- hardware/rendering;
- device scale;
- headless/headed mode.

Generate/compare baselines in a controlled environment.

# 7. Visual diff classification

Use:
- **Intentional**
- **Likely regression**
- **Environment variance**
- **Needs human review**

Do not automatically block release for every pixel mismatch.

# 8. Layout defects

Common release-impacting defects:
- clipped text;
- inaccessible controls;
- horizontal overflow;
- hidden content;
- overlapping fixed elements;
- unusable modal;
- content behind keyboard;
- broken sticky headers;
- offscreen validation/error messages.

Prioritize user impact over pixel perfection.

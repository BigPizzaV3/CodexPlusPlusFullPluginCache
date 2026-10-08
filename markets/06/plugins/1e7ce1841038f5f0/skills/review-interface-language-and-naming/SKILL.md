---
name: review-interface-language-and-naming
description: Review and repair product-interface language and terminology across navigation, buttons, CTAs, forms, errors, recovery, empty states, onboarding, settings, status messages, AI warnings, and feature names. Use when the primary task is UX writing, microcopy, interface labels, product terminology consistency, or expectation-setting inside a product. Do not use for general prose humanization, brand/company/product-name creation, translation, or visual interface design.
---

# Interface Language and Naming Review

Make interface language clear, concise, natural, consistent, expectation-setting and recovery-oriented without changing approved product behavior.

## Establish the language contract

1. Inspect the actual interface strings with route, component, state, trigger and consequence. Identify product voice, audience, locale, terminology source, feature names, behavior and legal/compliance constraints.
2. Separate approved product terminology from editable microcopy. Do not rename a product, feature, business concept or regulated term without the required authority.
3. Apply the shared [Product Quality Principles](../../shared/expert-system/product-quality-principles.md): language must support purpose, agency, responsibility, familiarity, flexibility, simplicity, craft and appropriate delight.
4. Mark missing behavior or unclear system truth as a specification gap. Copy cannot repair an interaction whose next step, failure state or consequence is undefined.

## Review dimensions

Check as applicable:

- navigation labels and information scent;
- button/CTA labels that describe the resulting action rather than vague intent;
- form labels, hints, validation, input expectations and accessible names;
- errors that state what happened, avoid blame and provide a real next step;
- recovery, retry, cancellation, undo and destructive-action language;
- empty, loading, success, offline, timeout, permission and status states;
- onboarding, settings and consent/permission explanations;
- AI-system disclosure, uncertainty, refusal, fallback, source and consequential-action warnings;
- feature/interface naming and enterprise terminology consistency;
- brevity, grammar, tone, localization readiness, text expansion and device/input wording;
- consistent terms for the same object, action and state across the journey.

Preserve facts, approved claims, legal qualifiers, exact data effects and accessibility meaning. Do not add personality that makes risk, failure or destructive consequences less clear.

## Routing boundary

- General prose, emails, articles, marketing copy or personal voice → `$humanize-writing`.
- New company, brand, product, service, project or channel name creation → `$create-distinctive-names`.
- Visual/interaction design audit → `$audit-premium-digital-experience`.
- Accessibility behavior audit beyond wording → `$audit-accessibility-and-inclusive-design`.

## Output

Return scope and terminology authority, a compact issue table with string/location/state/problem/user risk/recommended replacement/rationale, a canonical terminology list, unresolved behavior or owner decisions, localization notes and final consistency check. If rewriting is authorized, lead with implementation-ready replacement strings; otherwise keep them explicitly proposed.


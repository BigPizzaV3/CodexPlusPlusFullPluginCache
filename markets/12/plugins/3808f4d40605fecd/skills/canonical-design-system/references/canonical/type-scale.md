# Type Scale

This file carries the package type settings, token bindings, and resolved active text scale. Agents should use these values as exact typography decisions, not as loose suggestions.

## Canonical Type Data

```yaml
bindings:
  -
    bindingId: "type.xs"
    stepId: "xs"
    tokenRef: "font.body.xsmall"
  -
    bindingId: "type.sm"
    stepId: "sm"
    tokenRef: "font.body.small"
  -
    bindingId: "type.md"
    stepId: "md"
    tokenRef: "font.body.medium"
  -
    bindingId: "type.base"
    stepId: "base"
    tokenRef: "font.body"
  -
    bindingId: "type.lg"
    stepId: "lg"
    tokenRef: "font.body.large"
  -
    bindingId: "type.xl"
    stepId: "xl"
    tokenRef: "font.heading.xsmall"
  -
    bindingId: "type.2xl"
    stepId: "2xl"
    tokenRef: "font.heading.small"
  -
    bindingId: "type.3xl"
    stepId: "3xl"
    tokenRef: "font.heading.medium"
  -
    bindingId: "type.4xl"
    stepId: "4xl"
    tokenRef: "font.heading.large"
  -
    bindingId: "type.5xl"
    stepId: "5xl"
    tokenRef: "font.heading.xlarge"
  -
    bindingId: "type.6xl"
    stepId: "6xl"
    tokenRef: "font.heading.xxlarge"
resolvedSteps:
  -
    binding:
      bindingId: "type.xs"
      stepId: "xs"
      tokenRef: "font.body.xsmall"
    fontFamily: "Inter"
    fontSizePx: 10
    fontWeight: 400
    label: "XS"
    letterSpacingPx: 0
    lineHeightPx: 16
    lineHeightRatio: 1.5
    stepId: "xs"
  -
    binding:
      bindingId: "type.sm"
      stepId: "sm"
      tokenRef: "font.body.small"
    fontFamily: "Inter"
    fontSizePx: 12
    fontWeight: 400
    label: "SM"
    letterSpacingPx: 0
    lineHeightPx: 20
    lineHeightRatio: 1.5
    stepId: "sm"
  -
    binding:
      bindingId: "type.md"
      stepId: "md"
      tokenRef: "font.body.medium"
    fontFamily: "Inter"
    fontSizePx: 14
    fontWeight: 400
    label: "MD"
    letterSpacingPx: 0
    lineHeightPx: 20
    lineHeightRatio: 1.5
    stepId: "md"
  -
    binding:
      bindingId: "type.base"
      stepId: "base"
      tokenRef: "font.body"
    fontFamily: "Inter"
    fontSizePx: 16
    fontWeight: 400
    label: "Base"
    letterSpacingPx: 0
    lineHeightPx: 24
    lineHeightRatio: 1.5
    stepId: "base"
  -
    binding:
      bindingId: "type.lg"
      stepId: "lg"
      tokenRef: "font.body.large"
    fontFamily: "Inter"
    fontSizePx: 19
    fontWeight: 600
    label: "LG"
    letterSpacingPx: 0
    lineHeightPx: 28
    lineHeightRatio: 1.5
    stepId: "lg"
  -
    binding:
      bindingId: "type.xl"
      stepId: "xl"
      tokenRef: "font.heading.xsmall"
    fontFamily: "Inter"
    fontSizePx: 23
    fontWeight: 500
    label: "XL"
    letterSpacingPx: -0.02
    lineHeightPx: 28
    lineHeightRatio: 1.2
    stepId: "xl"
  -
    binding:
      bindingId: "type.2xl"
      stepId: "2xl"
      tokenRef: "font.heading.small"
    fontFamily: "Inter"
    fontSizePx: 28
    fontWeight: 500
    label: "2XL"
    letterSpacingPx: -0.02
    lineHeightPx: 32
    lineHeightRatio: 1.2
    stepId: "2xl"
  -
    binding:
      bindingId: "type.3xl"
      stepId: "3xl"
      tokenRef: "font.heading.medium"
    fontFamily: "Inter"
    fontSizePx: 33
    fontWeight: 700
    label: "3XL"
    letterSpacingPx: -0.02
    lineHeightPx: 40
    lineHeightRatio: 1.2
    stepId: "3xl"
  -
    binding:
      bindingId: "type.4xl"
      stepId: "4xl"
      tokenRef: "font.heading.large"
    fontFamily: "Inter"
    fontSizePx: 40
    fontWeight: 700
    label: "4XL"
    letterSpacingPx: -0.02
    lineHeightPx: 48
    lineHeightRatio: 1.2
    stepId: "4xl"
  -
    binding:
      bindingId: "type.5xl"
      stepId: "5xl"
      tokenRef: "font.heading.xlarge"
    fontFamily: "Inter"
    fontSizePx: 48
    fontWeight: 700
    label: "5XL"
    letterSpacingPx: -0.02
    lineHeightPx: 56
    lineHeightRatio: 1.2
    stepId: "5xl"
  -
    binding:
      bindingId: "type.6xl"
      stepId: "6xl"
      tokenRef: "font.heading.xxlarge"
    fontFamily: "Inter"
    fontSizePx: 57
    fontWeight: 700
    label: "6XL"
    letterSpacingPx: -0.02
    lineHeightPx: 68
    lineHeightRatio: 1.2
    stepId: "6xl"
settings:
  baseSizePx: 16
  bodyFontFamily: "Inter"
  bodyLetterSpacingPx: 0
  bodyLineHeightRatio: 1.5
  headingFontFamily: "Inter"
  headingLetterSpacingPx: -0.02
  headingLineHeightRatio: 1.2
  scaleLength: 11
  scaleRatio: 1.2
```

## Resolution Algorithm

1. Resolve the requested type role through bindings.tokenRef.
2. Find the matching resolvedSteps item by stepId.
3. Use fontFamily, fontSizePx, lineHeightPx, fontWeight, and letterSpacingPx as one inseparable type tuple.
4. If no binding or resolved step exists, stop and report the missing type decision.

## Rules

- Use bound type roles before choosing raw font sizes.
- Preserve the Inter family unless generated package data changes it.
- Do not create unbound type roles when a canonical binding exists.
- Generated package data contains active type values with user overrides already materialized.

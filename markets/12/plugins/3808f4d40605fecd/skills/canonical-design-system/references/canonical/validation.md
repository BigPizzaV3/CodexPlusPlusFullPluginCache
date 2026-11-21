# Validation

This file records internal package validation metadata. It is canonical package data, not an agent workflow or reporting requirement.

## Canonical Validation Baseline

```yaml
counts:
  componentContracts: 24
  componentTokenDefinitions: 1052
  componentTokenPaths: 3898
  effectStyles: 9
  insertResources: 24
  modes: 2
  palettes: 9
  referenceTokens: 119
  semanticTokenDefinitions: 174
  semanticTokenModes: 2
  shadowStyles: 9
  skillModules: 15
  skillResources: 20
  textStyles: 11
  typeSteps: 11
  variables: 371
expectedStateHash: "fnv1a32:bb7473ea+alpy-ai-ready-package@2026-08-06-chat-first-v8"
packageValidationGate:
  coreStatus: "valid"
  findings:
    []
  generatedAt: "2026-05-05T00:00:00.000Z"
  isPackageAllowed: true
  status: "valid"
provenance:
  artifactKind: "built-in-ai-ready-package"
  status: "built-in-reviewed"
  trustSource: "repo-built-in-markdown"
sourceLibraryHash: "fnv1a32:a4d60ecc"
validationSnapshot:
  generatedAt: "2026-05-05T00:00:00.000Z"
  libraryId: "lib_alpy_builtin"
  modes:
    dark:
      findings:
        []
      modeId: "dark"
      status: "valid"
    light:
      findings:
        []
      modeId: "light"
      status: "valid"
  status: "valid"
```

## Agent Boundary

- Do not run a separate package-integrity or completeness preflight.
- Treat the YAML as internal Alpy machinery; do not copy it into work notes, handoffs, reports, or implementation summaries.
- If a relevant Alpy read returns a blocker, stop only the affected work and report the gap.
- Validation reads canonical Alpy data, not rendered UI or design-tool state.

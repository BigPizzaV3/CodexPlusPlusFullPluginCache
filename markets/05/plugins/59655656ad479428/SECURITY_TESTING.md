# Security testing record

This record covers the Empire LLM for Codex `0.1.2` release candidate tested on 2026-07-26. It documents point-in-time engineering evidence, not a certification, independent penetration test, or guarantee that no vulnerability exists.

## Verified results

| Test | Result | Scope |
|---|---|---|
| Empire offline regression suite | Pass: 184 tests in 8 suites | Routing, handoff, media, credentials, endpoint fuzzing, evidence confidentiality, cache integrity, budgets, skill contracts, and publishing readiness |
| Deterministic Empire security audit | Pass: 7/7 checks | Archive paths and limits, private artifacts, production secrets, dangerous Python constructs, active SVG content, and seven skill contracts |
| Ruff | Pass | Plugin and release-builder Python |
| Bandit 1.9.4 | 0 high, 0 medium, 17 reviewed low findings | Production Python, excluding tests and fixtures |
| detect-secrets 1.5.0 | No credential material found | Production package text; all 39 reported high-entropy strings were verified SHA-256 icon asset digests |
| Release readiness | Pass: 10.0/10 | All evidence-backed publishing gates |

The Bandit low findings consist of subprocess imports/calls that use argument arrays with `shell=False`, fixed command names resolved by the operating system, and one false positive on a boolean field containing the word `required`. No medium or high finding remains.

## Reproduce the checks

Run from the repository root with Python 3.10 or newer:

```bash
python3 -m ruff check plugins/empire-llm-codex scripts

python3 plugins/empire-llm-codex/scripts/security_audit.py

python3 plugins/empire-llm-codex/scripts/marketplace_readiness.py \
  --run-tests \
  --format markdown \
  --write-todo CODEX_APP_STORE_TODO.md

python3 scripts/build_plugin_release.py --output-dir release

python3 plugins/empire-llm-codex/scripts/security_audit.py \
  --archive release/empire-llm-codex-0.1.2.zip
```

Bandit and detect-secrets are optional development scanners, not runtime dependencies:

```bash
bandit -r plugins/empire-llm-codex scripts \
  -x '*/test_*.py,*/fixtures/*' -f json

detect-secrets scan plugins/empire-llm-codex scripts --all-files \
  --exclude-files '(^|/)(test_[^/]*\.py|fixtures/|submission-test-cases\.json)$'
```

Review scanner output rather than treating entropy findings as credentials. The model-icon manifest intentionally contains SHA-256 integrity digests.

## Benchmark and control mapping

The mappings below identify relevant controls and test evidence. They do not claim formal OWASP or NIST compliance.

| Reference | Empire control and evidence |
|---|---|
| OpenAI plugin submission security checks | Seven skill contracts, strict ZIP inventory and limits, no private artifacts, no unnecessary runtime service, and a final archive audit |
| OWASP LLM01:2025 Prompt Injection | External content is quarantined and schema-projected; partner responses cannot invoke tools or edit files; Codex remains the lead and verifies findings |
| OWASP LLM02:2025 Sensitive Information Disclosure | Secret scanning before transport and after model response, path and size controls, native keyring storage, redacted diagnostics, and production-package secret scans |
| OWASP LLM03:2025 Supply Chain | Deterministic allowlisted ZIP, SHA-256 release checksum, no runtime Python dependencies, no active SVG content, and static analysis of executable code |
| OWASP LLM06:2025 Excessive Agency | Bounded single-task routing, explicit cost approval, quarantined artifacts, and no external-model repository writes |
| NIST SP 800-218 SSDF 1.1 | Release integrity and provenance checks (PS), review and static analysis (PW), vulnerability reporting and regression tests (RV) |
| NIST AI RMF / NIST AI 600-1 | Documented trust boundaries, human control, measured evaluation, incident reporting, and explicit residual-risk statements |

Primary references: [OpenAI plugin submission](https://developers.openai.com/plugins/deploy/submission), [OpenAI submission errors](https://developers.openai.com/plugins/deploy/submission-errors), [OWASP Top 10 for LLM Applications 2025](https://genai.owasp.org/llm-top-10/), [NIST SP 800-218 SSDF](https://csrc.nist.gov/pubs/sp/800/218/final), and [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework).

## Approved public claim

> Empire LLM for Codex 0.1.2 passed its documented 184-test offline regression suite, a 311-case production-validator endpoint fuzz run, deterministic package security audit, Ruff validation, a Bandit 1.9.4 scan with zero medium/high findings, and a reviewed detect-secrets 1.5.0 scan of production package text. Controls are mapped to relevant OWASP Top 10 for LLM Applications 2025 risks and NIST SP 800-218 SSDF practices. These results are point-in-time test evidence, not certification or a guarantee of zero vulnerabilities.

## Residual risk and next assurance step

Provider behavior, provider retention, upstream model behavior, operating-system keyring security, and Codex platform enforcement remain outside this repository's control. Live credentials can still be exposed if a user pastes them into chat or source files before Empire is invoked. Before making a stronger assurance claim, commission an independent penetration test covering prompt injection, cross-provider redirect behavior, archive ingestion, credential lifecycle, malicious model output, and local privilege boundaries.

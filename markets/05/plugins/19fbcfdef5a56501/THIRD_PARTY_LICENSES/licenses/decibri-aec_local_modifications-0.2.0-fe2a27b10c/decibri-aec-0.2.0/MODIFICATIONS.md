# Vendored third-party audio dependencies

## decibri-aec 0.2.0

- Upstream repository: https://github.com/decibri/decibri-aec
- Upstream Git revision: `68f4be0e714a870d10bd7fa8222173064e3bd7f9`
- Registry release: https://crates.io/crates/decibri-aec/0.2.0
- Source archive: https://static.crates.io/crates/decibri-aec/decibri-aec-0.2.0.crate
- Source archive SHA-256: `8c082148c8441fc7db2c9c31aeb69842cf754ef9b8a853b40e086a2f383860fd`
- License: Apache-2.0, preserved in `vendor/decibri-aec/LICENSE`

The `vendor/decibri-aec` directory contains every file from the verified
crates.io release archive, including the registry-normalized `Cargo.toml`,
the original `Cargo.toml.orig`, upstream documentation, examples, tests,
license, source files, lockfile, and upstream revision metadata.

### Local modifications

The original release was first committed without changes. The separately
reviewed Meetings integration adds a validated `AecConfig.residual_echo_leak`
option in `src/config.rs`, `src/engine.rs`, `src/error.rs`, and `src/tau.rs`.
The upstream default remains `0.0003`; only the Meetings-owned adapter opts
into `1.0`. Existing suppression safeguards remain in place.

The published crate excludes two feature-gated internal-test modules. Narrow
`#[rustfmt::skip]` attributes in `src/lib.rs` keep the existing workspace-wide
format check from resolving those deliberately unpublished source files. The
unavailable private modules and their test-only helpers are also disabled when
workspace validation selects every Cargo feature; the public feature remains
available and production behavior is unchanged.

Additional OpenAI modifications improve automatic echo-delay detection,
established-delay stability, and local-speech protection without hardcoding a
device-specific delay. The complete set of files modified from the upstream
`decibri-aec 0.2.0` release is:

- `src/acquire.rs`: corroborates delay candidates, rejects false zero-delay
  locks, and preserves a trusted alignment until a new path is verified.
- `src/canceller.rs`: exposes bounded echo coherence, residual, far-end
  activity, and output-protection metrics used by delay tracking.
- `src/config.rs`: adds configurable residual echo leakage while preserving the
  upstream default of `0.0003`.
- `src/delay.rs`: prefers the earliest reliable direct echo path over stronger
  later reflections.
- `src/engine.rs`: applies the configured residual leakage, protects established
  alignment, and explicitly reacquires after an actual acoustic-path change.
- `src/error.rs`: rejects non-finite and out-of-range residual leakage values.
- `src/lib.rs`: preserves compatibility with unpublished upstream internal-test
  modules during workspace-wide formatting and feature validation.
- `src/tau.rs`: applies configurable residual leakage and distinguishes
  far-only echo, silence, and real double-talk while preserving speech.
- `src/track.rs`: requires repeated credible evidence before changing an
  established delay and rejects isolated or distant speculative peaks.
- `tests/quality.rs`: covers weak direct paths with stronger reflections and
  far-only recovery with nonzero background noise.

Each modified file carries the notice
`// Modified by OpenAI from upstream decibri-aec 0.2.0.` at its top. The
upstream Apache-2.0 license and all unmodified source files remain intact.

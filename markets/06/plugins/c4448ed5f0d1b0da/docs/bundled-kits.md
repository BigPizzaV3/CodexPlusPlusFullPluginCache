# Bundled kits for 0.3.0

Snapshots taken September 23, 2026. Flint and Lantern are copied byte-for-byte from the local website collection at `/Users/nick/Documents/GitHub/soulware/content/personalities/`; both IDs are marked published in that repository's catalog. These hashes identify the bundled snapshots, not the files currently served by the website. No website source or frozen contract fixture was modified.

Moss 1.0.1 is the plugin's corrected sample. Its deadline correction no longer invents a draft deadline. The prior 1.0.0 contract fixture and prior release archives remain unchanged.

| Kit | Version | SHA-256 of bundled JSON |
| --- | --- | --- |
| Flint | 1.0.7 | `8188dec9fc06a4cf06c3560e90a5a1d29749b41a6f9f1da9fb7411c57b78d100` |
| Lantern | 1.0.6 | `2d7fa7de825f915b427ae4cd863455ded8d3402db2e61ede9842aeb3ab28bf13` |
| Moss | 1.0.1 | `39afa24a79be57831eb9b740c399e5bdaf3822f0b34d1bed2f3e062561a36ee6` |

Each `examples/<id>.soulkit.json` must match its self-contained copy in `skills/soulware/references/`. The packager checks every pair and validates each kit. Existing downloaded and installed versions remain usable; packaging a new sample does not update a customer’s installed kit.

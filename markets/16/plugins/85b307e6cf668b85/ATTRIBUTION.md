# Ownership and dependencies

Copyright (c) 2026 Christian Katzmann. The publisher approved MIT for original Device It code, instructions and documentation; see LICENSE. Approved publisher-supplied artwork is used for the listing. Prepared app content remains the property of its respective owner and is not relicensed by this tool.

Runtime packages are exact-pinned and locked; their code/binaries are not vendored into the plugin ZIP:

| Dependency | Version | Upstream license | Purpose |
| --- | --- | --- | --- |
| Playwright | 1.61.1 | Apache-2.0 | Disposable Chromium browser verification |
| qrcode | 1.5.4 | MIT | Local PNG QR creation |
| pngjs | 5.0.0 | MIT | Local PNG placeholder icons |
| jsqr (development only) | 1.4.0 | Apache-2.0 | Decode the synthetic fixture QR in tests |

`package-lock.json` pins transitive packages and integrity digests. Their upstream notices remain in installed packages. Chromium and its third-party components are downloaded separately by an explicitly authorized Playwright install and carry their own notices. Node.js, npm, the OS and optional Python packaging runtime are separate prerequisites. Publisher review must confirm applicable licenses/notices before distributing dependencies or binaries.

No trademark permission, public support route, privacy URL, phone installation capability or publisher verification is asserted.

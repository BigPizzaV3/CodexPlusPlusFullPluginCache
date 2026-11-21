# Device It privacy policy

## Scope

This policy covers the reviewed device-it plugin package version 0.2.1. It does not describe other versions, legacy tools, or every file in the source repository. Publication of this policy does not by itself announce a software release.

Device It is a local skill and scripts package. It has no publisher-operated backend, analytics or account authentication. The host assistant processes user requests under the host's own settings and policies.

The local workflow reads the user-selected built static files and their explicit public-asset list. It writes a separate prepared app, generated icons, manifest, service worker and an inventory of public file names and hashes. It can write a QR containing the local preview address, a JSON verification report containing that URL and cache/check results, and a screenshot of the rendered app. These artifacts may contain app content. They are not sent to the publisher by this package.

The preview serves selected public output files on loopback by default. Explicit LAN mode exposes them to devices able to reach this computer and port; there is no login layer. The local browser can create site data and service-worker caches. The verification browser uses a fresh disposable profile. The checker attempts to close it after the check, including failures, and records whether cleanup succeeded. It is not the user's existing browser profile.

Dependency installation, when expressly authorized, contacts npm and Playwright browser distribution servers. Those services receive normal download/network metadata and apply their own policies. Preparation and verification do not initiate hosting, tunnels, deployment, MDM, messaging, paid APIs or login. The preview blocks off-origin page resources. App behavior in a different hosting environment is controlled by that app and environment.

Local input remains untouched. Prepared output, QR files, reports and screenshots persist until the user deletes them; there is no automatic expiration. A manually opened browser can retain local site storage until the user clears that origin's site data. The user can stop the preview process, clear browser site data and remove the specifically generated directory/files. Uninstalling the plugin alone does not delete these artifacts.

## Publisher and contact

Publisher: Christian Katzmann. Effective date: September 30, 2026. For private privacy or support requests, contact [christian@katzmann.dk](mailto:christian@katzmann.dk). Send a minimal description; do not include credentials, notebook contents, production records or raw traces. Any information you choose to send for support is processed in the publisher's existing email service to answer that request, and remains until the correspondence is deleted. Request deletion through the same address. Provider backups and mandatory retention, if applicable, can outlast live-mailbox deletion.

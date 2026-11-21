# Maintainer notes

This document is for the publisher. End-user instructions are in README.md.

## Runtime

The scripts run in the selected execution environment. Python 3.9+ and Pillow support image processing; Inkscape or CairoSVG support scripted SVG rendering. These are environment dependencies, not instructions for cloud ChatGPT users to install desktop applications. Local execution is possible only when deliberately configured separately.

## Public submission

Upload the complete plugin ZIP, verify the publisher identity, resolve required validation findings, submit for review and publish after approval. This package has not been submitted or approved.

Official guide: https://developers.openai.com/plugins/deploy/submission
Homey reference: https://apps.developer.homey.app/app-store/guidelines

Publisher: Johan Bendz. Listing identity comes from the verified identity selected in the portal. Privacy policy: https://bortbytt.se/privacy-policy/

Website, support and terms URLs are omitted for this skills-only package. A distribution license has not been assigned.

## Verification

Run `python3 tests/test_assets.py` in a suitable execution environment. The 15 automated tests cover the processing pipeline, synthetic device shapes, invalid PNGs, common-master comparison, forbidden SVG techniques and rendering checks. They do not establish real-world photo quality for every device type.

The sensor example uses a previously cleaned image and a newly drawn SVG. An independent SVG-only run exercised reduced output scope and five review sizes. Visual review covers device fidelity, background interiors, detail separation and composition. Validation does not establish Athom acceptance.

The example board is a reference asset. The manifest has no listing screenshots field because this skills-only package has no MCP UI.

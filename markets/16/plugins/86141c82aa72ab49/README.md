# Physical Validation

Version 1.1.0 is prepared for directory review. The remote service and host-managed OAuth are live. The directory listings are not yet published.

Find CROs, CDMOs, and research facilities, compare their published evidence, and prepare experiment requests with Physical Validation by Halmos Labs. The shared skills cover provider discovery, request preparation and submission, and existing account drafts.

Requests support peptides, rabbits, mice, genes and plasmids, proteins and antibodies, sequencing, and other research work. Each request selects one service family. A request can include inline specifications, provider preferences, contact information, budget currency, and the other fields supported by the connected tools. Attach files through the browser request page.

The plugin connects to https://physicalvalidation.com/mcp. Catalogue search and evidence reads are public. Account drafts and submissions require the host's managed OAuth connection. Use the host's sign-in prompt for those actions. Request preparation returns a review link. Submission requires the person's agreement and returns a receipt when accepted. Halmos reviews requests before supplier outreach.

## Install and use

This source contains both platform formats. Claude reads `.claude-plugin/plugin.json` and `.mcp.json`. Hosts supporting Agent Plugins read the root `plugin.json` and `mcp.json`. Both use the same `skills/` directory. Connect Physical Validation in the host's connector settings, then ask for a workflow such as the following.

- Find GLP bioanalysis providers in Europe and show the sources behind their capabilities.
- Prepare a peptide synthesis request using my specifications for review.
- Show my saved request drafts and open the one about sequencing.

Capabilities depend on the tools the connected service exposes. Provider records report published claims and unknowns. Existing draft tools support listing, reading, deletion, and submission. Use the returned browser links for saved edits and file uploads.

## Data and support

The plugin sends search criteria and requested tool inputs to Physical Validation. Account workflows also use the person's supplied request and contact details. The service's privacy policy describes processing, storage, retention, and contact rights. Plugin files contain workflow instructions and connector configuration. The service operates under its own terms.

- Documentation — https://physicalvalidation.com/docs/mcp
- Privacy — https://physicalvalidation.com/privacy
- Terms — https://physicalvalidation.com/terms
- Support — https://physicalvalidation.com/support and inquiry@physicalvalidation.com

## License

The MIT license in `LICENSE` covers the files in this plugin distribution. It grants no license to Physical Validation's hosted service or catalogue data and no trademark rights. Service access and data use are governed by the service terms linked above.

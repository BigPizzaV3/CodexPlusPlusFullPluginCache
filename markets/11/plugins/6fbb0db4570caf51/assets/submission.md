# OpenAI submission preparation

## Local preparation scope

Contexta Learning has six skills for material capture, approved standard project creation, contextual phrase saving, phrase review, short pronunciation practice and measured progress/website continuation. Obsolete scenario-demo recipes and package-local four-exercise samples are replaced. Existing portal starter projects remain available through the live learner catalog on explicit request.

This package is for local verification and review preparation. Production rollout, draft submission and publication need separate authorization. Public identity is Contexta Learning. The two existing private production installations use Contexta Learning — Production; local development uses Contexta Learning — Local Dev. Preserve the public OAuth/MCP configuration and never include local app IDs, localhost endpoints, private management links or credentials here.

## Public links

- Website: https://contextalearning.com
- Privacy: https://contextalearning.com/privacy
- Terms: https://contextalearning.com/terms
- Support: https://contextalearning.com/support
- MCP: https://api.contextalearning.com/mcp/product/

## Review package

From the repository root, validate with `python3 backend/scripts/build_plugin_package.py` using the repository Python environment. To freeze a review ZIP/checksum report, add `--output-dir` outside this source package. Packaging does not deploy, call providers, create a portal draft or publish; `publication_ready` remains false until external gates actually pass.

The manifest has five positive and three negative prepared review cases, release notes and three starter prompts. [Reviewer materials](reviewer-materials.json) are fictional. [Tool review](tool-review.json) covers the complete locally declared base/capture/widget-enabled union with per-tool scopes and annotation justifications; compare it with the actual production scan after rollout. Frozen tool/skill snapshots do not update because local files changed: re-scan and import all six current skills plus their shared reference in the review portal.

File intake accepts bounded host-authorized file inputs, not arbitrary URL scraping. Saves preserve accepted pasted text; file parsing separately discloses extraction/layout limits and private original retention. Phrase contexts have honest original/chat/generated provenance. Speech scores require actual submitted audio, with neutral/unscored uncertainty. Full sessions and detailed history remain on the website.

## Before future submission

Use the verified Contexta LLC publisher. Release only through the repository's sanctioned process after authorization. Verify both production services, required learner flags, exact tool scopes/schemas/hints, OAuth/revocation/owner isolation, capture files/storage cleanup, planner readiness and real widget resource/audio outcomes. Repeat prepared cases on a dedicated reviewer account with sufficient normal access; provide credentials separately in the secure portal.

Country availability is all supported countries (`publication.countries: []`), as selected by the owner. `review.commerce: false` means the plugin has no checkout or subscription-purchase tools; any subscription payment happens separately on the Contexta website. Confirm supported hosts from actual evidence. Finish domain verification when the portal supplies its exact challenge token; business verification alone does not establish domain ownership. Serve the supplied token only at its specified challenge path/origin, without overwriting another plugin's challenge. No token or completed challenge is claimed by this package.

The [production demonstration](https://contextalearning.com/demos/contexta-learning/contexta-learning-review-2026-10-14.mp4) is a verified 4:10 MP4 recorded with the existing Contexta Learning — Production development installation. It uses the production service; it does not imply that this public draft is published or installed. The recording has only a head/tail trim, with the actual interactions and human audio retained. Anonymous playback and byte-range delivery were verified. The URL carries a noindex response header and is not in the sitemap, but anyone with the direct link can view it.

The recording retains known host presentation issues accepted for this demonstration: a generic/broken outer brand icon and occasional model-generated text or action duplication below the real widget. These are not claimed fixed by packaging or publication. A recording and metadata scan do not replace the five positive and three negative case results for the exact saved draft. Do not fabricate credentials, policy attestations or successful tests to satisfy validation. Follow the source repository's Contexta plugin publication runbook before authorized rollout; it is separate from the distributed package.

# Grid artist roster capability contract

Read the connected server's schemas before use; deployed versions may differ.

| Task | Existing capability | Boundary |
| --- | --- | --- |
| Discover music artist identities | `grid.search_music_artists` | Network-only iTunes US search, at most 25 candidates. Returns provider IDs and canonical artist URLs, not representation evidence. Observe returned pacing and availability status. |
| Find identities | `grid.search_companies` | Name-only candidates require review; use verified identity facts. |
| Inspect identity | `grid.get_company` | Read approved company facts before reuse or edits. |
| Create artist/organization | `grid.preview_company_create`, `grid.create_company` | Explicitly reviewed creation, stable pre-minted IDs, correct company type. |
| Edit company facts | `grid.preview_company_update`, `grid.update_company` | Preserve curated fields; report pending versus applied outcomes. |
| Save a selected catalog identity | Existing company preview/create or preview/update URL fields | Retain the numeric iTunes artist ID in its canonical `https://itunes.apple.com/artist/id<ID>` URL. Review conflicting IDs and duplicate companies; no separate MusicKit/provider-ID column is implied. |
| Stage artist representation | `grid.prepare_artist_roster_import`, `grid.stage_artist_roster_import` | Platform admin; review the stored preview, then confirm staging. Publication remains separate. |
| Approve staged relationships | `grid.preview_artist_roster_approval`, `grid.approve_artist_roster` | Platform admin may approve their own claims; confirmed snapshot, atomic publication and review resolution. |
| Refresh persisted roster evidence | Same prepare/stage pair, with the same source URL | Actor-scoped source snapshots; failed/partial extraction never implies a relationship ended. |

The baseline application stores artists in `companies`, approved label/management in `artist_company_relationships`, and proposed relationships in `public_company_suggestions` with `target_type: artist_relationship`, paired with `review_items`. Pending suggestions do not populate approved relationship cards.

Roster evidence retains the source URL, checked date, attribution, access/reuse notes, short excerpt, and nullable territory/effective dates. Approved evidence is copied from the immutable suggestion into the relationship projection and synced to local SQLite. Pending suggestions remain separate. Territory and date qualifications appear in relationship displays; unknown territory does not mean worldwide representation.

Preparation stores an expiring operational snapshot without creating companies or relationships. Staging rechecks the actor, source revision, identities, and existing review/approved state, then atomically saves pending claims, review items, source history, and a receipt. Unchanged evidence (excluding checked date) reuses pending, approved, or rejected suggestions. A rejected claim is not silently reopened. Changed evidence gets a new pending suggestion, leaving approved rows intact. Older checked dates are rejected; recheck the source. Refresh warnings are returned for human review, not converted into automatic termination proposals.

These tools accept researched facts; they do not fetch remote pages. Use the skill's bounded source research process before preparation. Creating the approximately 100-artist starter set and approving it are separate operations from installing this capability.

The repository starter selection should cover the artists in `src/components/Pipelines/pipelineTargetSuggestions.ts` and the onboarding genre options. Keep the source inventory and reviewed starter data separate from these reusable skill instructions. No source is pre-approved for crawling or reuse merely by inclusion in a proposed inventory.

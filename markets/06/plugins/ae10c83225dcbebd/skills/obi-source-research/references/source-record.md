# Source candidate record

For every candidate record:

- `source_id`: stable local identifier
- `title`
- `author_or_organization`
- `date`
- `source_type`: museum object, archaeological site, excavation report, institutional archive, historic photograph, map, scholarly reconstruction, comparative artifact, scripture, scholarly book, scholarly article, video, popular summary, or other
- `source_page_url`: direct page where the source and its context can be inspected
- `image_url_or_figure`: direct image URL when appropriate, or the precise figure, gallery item, page, or timestamp
- `accessed_at`, when relevant
- `visual_subject`: what the relevant image actually shows
- `object_or_site_date`
- `object_or_site_location`
- `relevance_summary`
- `supported_claim_ids`
- `contradicted_claim_ids`
- `reliability_note`
- `provenance_note`
- `historical_value`: `high`, `medium`, `low`, or `unsuitable`
- `historical_value_reason`
- `visual_guidance`: the details this image may responsibly guide
- `visual_limitations`: details that must not be inferred from it
- `reuse_license`: verified value or `unknown`
- `status`: candidate, approved, or rejected
- `unresolved_limitations`

Distinguish three questions: Is the source authentic and identifiable? Is it relevant evidence for this claim? May OBI legally reuse material from it? A positive answer to one does not imply the others.

## Historical-value rubric

| Rating | Use |
| --- | --- |
| `high` | Authenticated artifact, site, or documented period image with strong provenance and close chronological, geographic, and cultural relevance. It can directly guide specified visual details. |
| `medium` | Reliable comparative evidence, adjacent period or region material, or a scholarly reconstruction with its evidentiary basis identified. Useful with clearly stated limits. |
| `low` | Modern illustration, weakly documented image, distant comparison, or source lacking enough context. It may inspire questions but should not establish historical details. |
| `unsuitable` | Misidentified, anachronistic, AI-generated, contextless, or materially misleading imagery. Do not use it as historical guidance. |

Evaluate provenance, date, geography, cultural setting, source authority, and relevance to the precise visual question. Do not collapse these dimensions into an unexplained score.

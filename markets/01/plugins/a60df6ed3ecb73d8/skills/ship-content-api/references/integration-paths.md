# Integration paths

| Path | When | Tools |
|------|------|-------|
| Pre-built embed | Fastest web MVP | `get_integration_plan` → `get_embed_code_samples` (`embed_prebuilt`) |
| AI-generated embed | Runtime generated workouts | `embed_ai_generated` + JSON receiver handshake |
| Custom player | Mobile / hardware / full UI control | `get_workout_playlist` + `custom_*` samples |
| Stream videos | CMS / VOD export | `deliveryOption: stream_videos` from `get_integration_plan` |

Docs: https://hyperhuman.cc/content-api · https://hyperhuman.cc/api-docs

Locales (pass `locale=`): en-US, en-GB, en-AU, fr-FR, de-DE, es-ES, it-IT, pt-PT, he-IL, ro-RO, cs-CZ, fi-FI, nl-NL, and others supported by the platform.

# Examples and edge cases

These illustrate handling, not an authoritative family/model/locale inventory.
Revalidate example values against usable current options when uncertain.

| Request or case | Expected handling |
| --- | --- |
| Browse everything SpeakShelf exposes | Discover provider options and provider-scoped families dynamically; use current responses and page state. Do not stop after the first family or assume source registry entries are exposed. |
| Google Chirp 3: HD voices | Resolve display label to exact returned family key, observed as Chirp3HD. Do not send the label as a key. Chirp is one regression case, not the workflow's scope. |
| WaveNet or Azure Dragon | Map current label to its returned key; observed examples include Wavenet and Dragon Latest. Ask if several Dragon families could satisfy the request. |
| MAI Voice 2.1 versus Flash | Keep distinct returned families and exact voice IDs; do not turn family tokens in Azure IDs into model selectors. |
| Polly Long-Form and Standard | Resolve Long-Form label to returned LongForm key. Pair Standard with provider polly, and keep premium/ultra as the only tier values. |
| Kokoro names and locales | Search using discovered Kokoro family and exact voice locale; use concise name query, then retain the row ID. Empty models does not require a model argument. |
| Algieba by name | Use query Algieba, with known filters. Multiple rows can share a name across families/locales. Present differences and clarify the selected row before a sample. |
| French voices, Arabic interface | Use voice_locale fr-FR only if France is intended and interface_locale ar. Keep voices French; preserve exact IDs/codes and requested model state. |
| Gemini, Bashkir ba-RU | Observed usable model is 3.8 Flash; Lite can be echoed unavailable. Use returned IDs rather than label-derived IDs. Never apply the general 2.5 preference to an ineligible row. |
| ace-Arab-ID versus ace-Latn-ID | Keep exact script-specific codes and each row's model admission. Do not collapse codes into a broad language label. |
| Gemini 3.1 Pro or conflicting qualifiers | Do not force a nearby Flash model or erase Pro. Explain ambiguity/unsupported combination using options and clarify. |
| All models after a model-specific search | Send model empty in the new search, drop the old cursor, preserve All in subsequent pages. Do not send empty model to samples. |
| Explicit eligible model then next page | Keep exact original model ID, filters, page size and returned cursor. |
| Inferred model then next page | Leave model omitted, preserve original query and filters. Copying appliedFilters.model changes intent and may reset paging. |
| Compare Azure and Google French voices | Search each requested provider with the same intended voice locale where needed, retain eligibility differences, compare only returned metadata and identify partial coverage. |
| Only primary Azure British voices | Use provider azure, voice_locale en-GB, primary_only true. Explain declared exact locale metadata without promising accent. |
| Invalid family/model/locale or no matches | Chirp 3: HD as a key, DragonHD, Long-Form, Kokoro-invalid, a bogus model or xx-YY may produce successful total zero. Verify usable keys/codes before classifying. Do not silently widen filters. |
| Valid family plus incompatible tier/gender | Options can remain visible despite zero matches. Keep requested constraints and explain the combination. |
| Selected sample pending/unavailable | Preserve exact row and eligible model, report status and retryAfter. Do not generate custom speech or substitute another sample. |
| Read my paragraph, clone a voice, delete private recordings | Explain the catalogue-only boundary. Neither exposed tool fulfills those actions. |

Do not treat these expectations as installed-ChatGPT test results.

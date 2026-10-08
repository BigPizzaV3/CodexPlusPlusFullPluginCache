# Language code mapping

Wistia's tools use different code formats depending on the endpoint, so audience-language
data and transcript/dub language data won't match on a raw string comparison. Normalize
through this table before comparing.

- `show-media-languages` (audience/viewer analytics) returns **browser language codes**
  (IETF/BCP-47 style, e.g. `en`, `en-US`, `es`, `es-MX`, `pt-BR`, `zh-CN`). Treat the
  base subtag (before any `-`) as the language; only split out regional variants
  (e.g. `pt-BR` vs `pt-PT`, `zh-CN` vs `zh-TW`) if the account has meaningfully different
  volume in both and the user wants to treat them separately. Default to collapsing to
  the base language.
- `get-captions` (transcripts & subtitles) uses **ISO 639-2 (3-letter) codes**.
- `gets-localizations` (dubs) uses **3-character IETF-ish codes**
  per the tool schema — in practice these match ISO 639-2/639-3 codes for the common
  languages below.

## Common mappings (browser code → 3-letter code)

| Browser (ISO 639-1) | 3-letter (captions/dubs) | Language              |
|----------------------|---------------------------|------------------------|
| en                   | eng                        | English                |
| es                   | spa                        | Spanish                |
| pt                   | por                        | Portuguese             |
| fr                   | fre / fra                  | French                 |
| de                   | ger / deu                  | German                 |
| it                   | ita                        | Italian                |
| ja                   | jpn                        | Japanese               |
| ko                   | kor                        | Korean                 |
| zh                   | chi / zho                  | Chinese                |
| nl                   | dut / nld                  | Dutch                  |
| ru                   | rus                        | Russian                |
| ar                   | ara                        | Arabic                 |
| hi                   | hin                        | Hindi                  |
| pl                   | pol                        | Polish                 |
| tr                   | tur                        | Turkish                |
| vi                   | vie                        | Vietnamese             |
| id                   | ind                        | Indonesian             |
| th                   | tha                        | Thai                   |
| sv                   | swe                        | Swedish                |
| da                   | dan                        | Danish                 |
| no                   | nor                        | Norwegian              |
| fi                   | fin                        | Finnish                |

Some tools return two valid ISO 639-2 variants for the same language (a "bibliographic"
and a "terminology" code — e.g. French is `fre` or `fra`, German is `ger` or `deu`,
Chinese is `chi` or `zho`). When checking whether a language is already covered, treat
either variant as a match.

## If a language isn't in this table

Don't guess. Look up the correct ISO 639-2 code, state it to the user as part of the
audit output ("mapped `[browser code]` → `[3-letter code]` for [language name]"), and
proceed — but flag it plainly rather than silently assuming.

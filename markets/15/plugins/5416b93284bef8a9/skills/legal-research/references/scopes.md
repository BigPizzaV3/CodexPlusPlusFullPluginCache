# Scope capability matrix

Confirm the actual connected deployment with `list_scopes`. A configured scope
is not a completeness guarantee. An unsupported capability returns
`unsupported_capability`; preserve that boundary. Unsupported countries must not be searched
through another country's scope.

| Capability | @hr | @eu | @fr | @de | @si | @nl |
| --- | --- | --- | --- | --- | --- | --- |
| Search | semantic/lexical/hybrid | semantic | semantic/lexical | semantic/lexical | semantic/lexical | semantic/lexical |
| Resolve / metadata | yes | yes | no | yes | yes | yes |
| Article text | yes | yes | yes | yes | yes | yes |
| Text by date | yes | no | yes | no | yes | yes |
| Explicit text version | UUID | no | LEGIARTI | snapshot key | version_key | version_key |
| Structure | yes | yes | no | yes | yes | yes |
| List articles | yes | no | yes | yes | yes | yes |
| Whole document | yes | no | no | yes | yes | yes |
| Chapter | yes | no | no | no | no | no |
| Status/history | four modes | current/history | article fields | current/snapshots | current/history | current/history |
| Related acts | yes | yes | no | no | no | no |
| Official gazette | yes | date browse | no | no | no | no |
| Dedicated court-decision tools | yes | no | no | no | no | no |

EU transposition and Eurostat are EU tools. Reported national measures can cover
EU member states whose national texts are not connected. This does not expand
national text coverage. EU judgments may be discoverable in the EUR-Lex corpus;
they are not exposed by the Croatian court-decision tools.

## Source and version limits

- @hr: Narodne novine legislation, recorded historical versions, gazette items,
  Croatian court decisions. Check consolidation warnings and amendment text.
- @eu: EUR-Lex English text; deterministic CELEX/act-number resolution plus
  aliases/title candidates. No arbitrary past-date article retrieval.
- @fr: available codified LEGI articles and versions. Non-codified laws,
  decrees, Journal officiel and French case law are not exposed.
- @de: German federal legislation from Gesetze im Internet. Recorded versions
  are consolidation snapshots, not historical validity intervals. Never claim
  the wording applied on a past event date from a scrape timestamp.
- @si: PISRS legislation, source version keys and available validity intervals.
- @nl: wetten.overheid.nl legislation and recorded versions. Search paragraph
  hits are attached to their parent article; quote the full retrieved article.

Use German, Slovenian and Dutch legal terms for the respective national scopes.
Search ranks are interleaved across scopes, never comparable by similarity.
Read `scope_status`, `scope_errors`, degradation and omission warnings. A failed
scope or empty result is a coverage gap, not proof that no applicable law exists.

Country full-document responses may be truncated at 800,000 characters. For
remaining text use paginated `list_articles` and `get_article`. A returned
in_force flag reflects indexed metadata, not a fresh authoritative legal opinion.

Aliases: @cro/@croatia → @hr; @eur-lex/@europe → @eu; @france → @fr;
@germany → @de; @slovenia → @si; @netherlands → @nl.

Use only tools actually listed by the connection. Profile restrictions and
capability differences must remain visible in the answer.

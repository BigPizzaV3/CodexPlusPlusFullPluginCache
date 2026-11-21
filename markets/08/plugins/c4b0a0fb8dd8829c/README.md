# Backlinkswinkel Catalogus voor OpenAI

Een aparte onderzoeksvariant met twee openbare, alleen-lezen tools: `search_domains` en `get_domain`. De assistent vergelijkt categorieën, taal en opgeslagen DR/DA/verwijzende domeinen. Er zijn geen prijzen, betaallinks, besteltools of accountgegevens.

De volledige Claude-plugin blijft een apart pakket.

## Status

- **1.0.1 goedgekeurd en gepubliceerd op 16-10-2026** (OpenAI-portaal: Approved, geen findings, Publish Version).
  ChatGPT: https://chatgpt.com/plugins/plugin_asdk_app_6abc032fd28c8191a538a209aff122af
- Uitlegpagina met proefzoeker: https://backlinkswinkel.nl/chatgpt/
- Tooldefinities (namen, beschrijvingen, inputschema's) zijn bevroren op de goedgekeurde versie;
  `agent_api.tests.test_catalog_mcp.test_approved_tool_definitions_unchanged` bewaakt dat.
  Een wijziging daaraan vraagt een nieuwe versie en een nieuwe review.
- Serverkant mag wel verbeteren zonder nieuwe review. 16-10-2026 (7b63fe0): `topic` matcht nu ook
  samengestelde woorden (tuinonderhoud -> Tuin) en `language` accepteert taalnamen (Nederlands, Dutch, nl-NL).
  Aanleiding: de derde voorbeeldprompt uit de listing gaf 0 resultaten.

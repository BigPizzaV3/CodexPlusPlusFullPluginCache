# OpenAI Plugin — test cases prep (paste into submission)

## Positive (5)
1. Search SEW MDX61 → expect `search_parts` with priced or on-request rows.
2. Get SKU `MDX61B0040-5A3-4` → `get_part` with prices map + product URL.
3. List brands starting with S → `list_brands` includes Siemens / SEW.
4. Brand stats for Siemens → `get_brand_stats` with categories.
5. Alternatives for a known SEW SKU → `suggest_alternatives` (may be empty if sparse — still OK).

## Negative (3)
1. Ask to transfer money / place a paid order inside chat → refuse; point to quote/`create_inquiry` + website.
2. Ask to dump the entire catalog without query → `search_parts` errors without q/brand.
3. Ask for Mechstock live stock → tool returns not-live note.

## Controlled inquiry (reviewer)
Use throwaway `@example.com` + company `TEST …` so customer autoreply is skipped; set `source=chatgpt`. Soft limit ~1000/IP/day.

## Demo video
**Clemens-gated:** record short screen capture of ChatGPT/Claude calling search + get_part.

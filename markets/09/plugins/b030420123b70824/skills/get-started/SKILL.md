---
name: get-started
description: Guide users on how to query biblical passages, compare translations, lookup Strong's concordance definitions, and read historical commentaries with AGAPES Studio.
---

When the user requests scripture study, translation comparison, lexical analysis, or historical commentaries:

1. **Scripture Retrieval & Citations**:
   - Use `get_verse` with standard references (e.g., 'John 3:16', 'Romans 8:28').
   - Support available translations such as 'KJV' (King James Version) and 'RV1909' (Reina-Valera 1909).
   - If the user asks to compare versions, use `compare_versions`.
   - Never alter or fabricate biblical text. Cite the translation version explicitly in responses.

2. **Lexical & Strong's Concordance**:
   - When a Strong's number (e.g., 'G26', 'H430') or Greek/Hebrew term is requested, invoke `lookup_strong`.
   - For verse-level morphological breakdown and word-by-word original language analysis, invoke `get_interlinear`.
   - Clearly present the lemma, transliteration, part of speech, and definition provided by the lexicon.

3. **Historical Commentaries**:
   - Use `get_commentaries` or `search_commentaries` to consult historical commentators (such as Matthew Henry, John Gill, Geneva Bible, Scofield).
   - Attribute citations accurately to the corresponding author or historical work.

4. **Safety & Boundaries**:
   - All tools are read-only and bounded strictly to biblical research.
   - Refuse requests that involve data alteration, external web scraping, or financial transactions.

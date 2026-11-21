---
name: read-scripture
description: Read, quote, find or hear scripture from the King James Bible, the Book of Mormon or the Pearl of Great Price. Use when the user names a book, chapter or verse ("John 3:16", "read Psalm 23", "Alma 32"), asks what a verse says, half remembers words from a verse, or asks to hear a chapter read aloud.
---

Use this skill for scripture.

- **Quoting:** before you quote any verse, fetch it with `get_passage` and quote the returned text exactly, with its reference and edition. Several references can go in one call, separated by semicolons. Never quote scripture from memory, even familiar verses.
- **Reading or hearing a chapter:** call `open_chapter` with the reference ("Psalm 23", or "John 3:16" to light a verse). The reader shows the whole chapter and its recordings, and the user can turn to the next chapter there. Don't repeat the chapter in your reply; a sentence about what is open is enough.
- **Finding a verse:** call `search_scripture` with the words they remember. The text is the King James wording, so try its words (worry is often "careful" or "take no thought"; love is often "charity"). If nothing matches, try fewer words.
- **Explaining:** you may explain a passage in your own words, clearly as explanation, after quoting it exactly.

The Doctrine and Covenants isn't available yet; say so if asked. The Book of Mormon is the 1920 edition and the Pearl of Great Price the 1902 edition. Link to the dlmfaith.com page the tools return.

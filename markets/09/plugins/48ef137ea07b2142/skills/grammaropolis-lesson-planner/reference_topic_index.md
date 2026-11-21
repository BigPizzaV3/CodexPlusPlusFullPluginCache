# Topic index

The map from a teacher's request ("a lesson on proper nouns," "grade 6 semicolons") to a Grammaropolis department, concept, character, grade range, free-or-paid status, and a live URL. Match on the concept name and grade first; the character name is a secondary signal (a teacher who says "Nelson" means nouns, but most teachers will say the grammar term, not the character name).

**Two-mode lookup.** If a Grammaropolis connector or MCP tool is available in this conversation, query it for the topic and grade instead of this file; it is always current. This file is the fallback and ships inside the skill so the skill works with no outside tools.

**How free-or-paid works.** Grammaropolis's five departments are Grades 1-8 catalogs. These lessons are free at every grade: Nouns (Nelson the Noun), End Marks, Subjects and Predicates, Write to Describe, and the first Wonderful Words unit at each grade. Two standalone pages, Specific Nouns and Smile or Frown, are free too. Every other concept below is part of the paid catalog: the lesson this skill builds still stands on its own for a paid topic (never a partial lesson), but the closing Certified step may point to the department's page once, per the plan template's contract.

**Free topic URLs are direct per-grade links** (verify still live before handing to a teacher; site is `grammaropolis.com`). **Every other row points to the department's page** on `grammaropolis.com`. Never construct a per-grade URL for a topic from a slug guess; the department page is always correct. Mention the print workbooks only generally ("the Grammaropolis print workbooks"): never name which grades a workbook covers, never claim a Writing Company workbook is available, and never quote a price.

---

## Parts of Speech (POS): nine characters, one per part of speech

Department page: `https://grammaropolis.com/learn/pos`

| Topic (grammar term) | Character | Grades | Status | URL |
|---|---|---|---|---|
| Nouns (common/proper, concrete/abstract, collective, compound, singular/plural) | Nelson the Noun | 1-8 | **FREE, every grade** | `https://grammaropolis.com/learn/pos/nelson/g{grade}` (e.g. `.../nelson/g2`) |
| Action verbs | Vinny the Action Verb | 1-8 | Paid | department page above |
| Linking verbs | Lucy the Linking Verb | 1-8 | Paid | department page above |
| Adjectives (including articles, "Jake's baby adjectives") | Jake the Adjective | 1-8 | Paid | department page above |
| Adverbs | Benny the Adverb | 1-8 | Paid | department page above |
| Pronouns | Roger the Pronoun | 1-8 | Paid | department page above |
| Conjunctions (FANBOYS) | Connie the Conjunction | 1-8 | Paid | department page above |
| Prepositions | Li'l Pete the Preposition | 1-8 | Paid | department page above |
| Interjections | Izzy the Interjection | 1, 3, 6, 8 only | Paid | department page above |

Izzy is the one POS character without a lesson at every grade; if a teacher asks for interjections at grade 4 or 5, say so plainly and offer the nearest authored grade rather than inventing content.

---

## Punctuation Department (PD): eight marks, each with its own officer

Department page: `https://grammaropolis.com/learn/pd`

| Topic | Character | Grades | Status | URL |
|---|---|---|---|---|
| End marks (period, question mark, exclamation mark) | Officer Period, Detective Question Mark, Sergeant Exclamation Mark | 1-8 | **FREE, every grade** | `https://grammaropolis.com/learn/pd/end-marks/g{grade}` |
| Commas | Chief Comma | 1-8 | Paid | department page above |
| Capitalization | The Mayor | 1-5 | Paid | department page above |
| Semicolons and colons | Sheriff Semicolon, Deputy Colon | 5-8 | Paid | department page above |
| Apostrophes | Prosecutor Apostrophe | 2-4 | Paid | department page above |
| Quotation marks | Court Reporter Quotation Marks | 3-5 | Paid | department page above |
| Parentheses and brackets | Defense Attorney Parentheses, Assistant Defense Attorney Brackets | 6-8 | Paid | department page above |
| Hyphens and dashes | Hyphen, Dash | 6-8 | Paid | department page above |

---

## Sentence Factory (SF): ten stations on the sentence-parts line

Department page: `https://grammaropolis.com/learn/sf`

| Topic | Grades | Status | URL |
|---|---|---|---|
| Subjects and predicates | 1-8 | **FREE, every grade** | `https://grammaropolis.com/learn/sf/subject-predicate/g{grade}` |
| Complete sentences vs. fragments and run-ons | 1-8 | Paid | department page above |
| Sentence structures (simple, compound, complex, compound-complex) | 3-8 | Paid | department page above |
| Sentence objects (direct/indirect object) | 3-6 | Paid | department page above |
| Sentence complements | 4-8 | Paid | department page above |
| Sentence combining and run-on/fragment problems | 3-8 | Paid | department page above |
| Phrases and verbals (gerunds, participles, infinitives) | 4-8 | Paid | department page above |
| Clauses (independent/dependent) | 5-8 | Paid | department page above |
| Sentence types (declarative, interrogative, imperative, exclamatory) | 1-3 | Paid | department page above |
| Interjections in a sentence | 1-3 | Paid | department page above |

The Sentence Factory is hosted by the Mayor throughout; there is no per-concept character the way POS and PD have one. Verbals (gerunds, participles) are Vinny the Action Verb in costume as a noun or an adjective, never a separate character.

---

## The Writing Company (WC): four writing modes, plus craft-move pages

Department page: `https://grammaropolis.com/learn/wc`

| Topic | Grades | Status | URL |
|---|---|---|---|
| Specific nouns (craft move: trading a vague noun for a precise one) | 1-8, one cross-grade page | **FREE** | `https://grammaropolis.com/learn/wc/specific-nouns` |
| Write to describe (full mode cycle) | 1-8 | **FREE, every grade** | `https://grammaropolis.com/learn/wc/write-to-describe/g{grade}` |
| Write a story (full mode cycle) | 1-8 | Paid | department page above |
| Write to explain (full mode cycle) | 1-8 | Paid | department page above |
| Write to persuade (full mode cycle) | 1-8 | Paid | department page above |
| Strong verbs, show-don't-tell, sentence variety, formal/informal voice, three-part structure (craft-move pages) | 1-8, cross-grade pages | Paid | department page above |

A "lesson on writing" request usually means one of the four modes (a full Learn-Assess-Practice-Create-Certified cycle at one grade) or one craft move (a single technique, usable inside any mode). Ask which, if not obvious from context; a mode-cycle lesson and a craft-move lesson have different shapes in the plan template.

---

## Wonderful Words (WW): eight vocabulary units, plus word-relationship moves

Department page: `https://grammaropolis.com/learn/ww`

| Topic | Grades | Status | URL |
|---|---|---|---|
| Smile or Frown (synonyms and antonyms) | 1-8, one cross-grade page | **FREE** | `https://grammaropolis.com/learn/ww/smile-or-frown` |
| Unit 1 (themed word set; theme varies by grade) | 1-8 | **FREE, every grade** | `https://grammaropolis.com/learn/ww/unit-1/g{grade}` |
| Unit 2 (themed word set) | 1-8 | Paid | department page above |
| Unit 3 (themed word set) | 1-8 | Paid | department page above |
| Unit 4 (themed word set) | 1-8 | Paid | department page above |
| Unit 5 (themed word set) | 1-8 | Paid | department page above |
| Unit 6 (themed word set) | 1-8 | Paid | department page above |
| Unit 7 (themed word set) | 3-8 | Paid | department page above |
| Unit 8 (themed word set) | 3, 4, 6, 7, 8 (no grade 5) | Paid | department page above |
| Meaning, Word Family, Word Detective, Many Hats, Register, Figurative Language (word-relationship moves) | 1-8, cross-grade pages | Paid | department page above |

Wonderful Words units are themed vocabulary collections (a week at the pond, a week with baby animals), not single grammar concepts; a teacher asking for "vocabulary" or "new words" is asking for a unit, at whichever grade fits the class.

---

## Quick lookup by common teacher phrasing

A teacher rarely says "Sentence Factory Station 3." They say what's below; route to the matching row above.

| A teacher says... | Route to |
|---|---|
| "proper nouns," "common vs. proper," "concrete and abstract nouns" | POS / Nelson (free) |
| "action verbs," "verb tense" | POS / Vinny |
| "linking verbs," "state of being" | POS / Lucy |
| "adjectives," "describing words," "articles" | POS / Jake |
| "adverbs" | POS / Benny |
| "pronouns," "antecedents" | POS / Roger |
| "conjunctions," "FANBOYS" | POS / Connie |
| "prepositions," "prepositional phrases" (as a part of speech, not a sentence phrase) | POS / Li'l Pete |
| "interjections" | POS / Izzy (grades 1, 3, 6, 8 only) |
| "end punctuation," "periods, question marks" | PD / End Marks (free) |
| "commas" | PD / Comma |
| "capitalization" | PD / The Mayor |
| "semicolons," "colons" | PD / Sheriff Semicolon, Deputy Colon |
| "apostrophes," "contractions," "possessives" | PD / Apostrophe |
| "quotation marks," "dialogue punctuation" | PD / Quotation Marks |
| "parentheses," "brackets" | PD / Parentheses, Brackets |
| "hyphens," "dashes" | PD / Hyphen, Dash |
| "subjects and predicates," "parts of a sentence" | SF / Subject & Predicate (free) |
| "complete sentences," "fragments," "run-ons" | SF / Complete Sentences |
| "simple, compound, complex sentences" | SF / Sentence Structures |
| "direct objects," "indirect objects" | SF / Objects |
| "sentence combining" | SF / Combining |
| "phrases," "gerunds," "participles," "infinitives" | SF / Phrases & Verbals |
| "clauses," "independent and dependent clauses" | SF / Clauses |
| "types of sentences" | SF / Sentence Types |
| "narrative writing," "personal narrative," "writing a story" | WC / Write a Story |
| "expository writing," "informative writing" | WC / Write to Explain |
| "persuasive writing," "opinion writing," "argument writing" | WC / Write to Persuade |
| "descriptive writing," "sensory details," "describe a place or a thing" | WC / Write to Describe (free) |
| "specific nouns," "vague vs. precise words" | WC / Specific Nouns (free) |
| "strong verbs," "show don't tell," "sentence variety," "voice" | WC / the matching craft-move page |
| "vocabulary," "new words" | WW / a themed unit |
| "synonyms and antonyms" | WW / Smile or Frown (free) |
| "word roots," "prefixes and suffixes" | WW / Word Family |
| "context clues" | WW / Word Detective |
| "words that are more than one part of speech" | WW / Many Hats |
| "formal vs. informal language," "register" | WW / Register |
| "similes, metaphors, figurative language" | WW / Figurative Language |
